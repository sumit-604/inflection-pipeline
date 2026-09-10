# VERIFIER DISAGREEMENT LOG — INDNIPPON 2026-09-10

Per prompts/00-orchestrator.md Section 4, "LOG EVERY VERIFIER DISAGREEMENT
(from day one)". A disagreement is any point where a downstream step's
conclusion conflicts with a Verifier A source-fidelity finding. This set is
standing evidence on whether Haiku catches what the Opus verifiers miss, or
whether the disagreements are noise. It is NOT a REWORK trigger by itself.

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-10 | indnippon-2026-09-10 | TVS Educational Society apprentice-stipend growth, FY26 vs FY25 | Pass 1 raised MAJOR, `source_fidelity: true`. Its source_truth column read: "AR2026 Note 42.2: (3,059-2,458)/2,458 = +24.4%, not 26.7%" | B02-notes (stage 2 pass 1), carried into B03-ardeep monitorables and B08-promoter adverse_findings, all stating +26.7% | FLAG CLEARED — source re-check found the number at a correct anchor (re-checked by the orchestrator, then referred back to Verifier A for its own re-read in the single permitted re-invocation) | The base figure 2,458 does not appear anywhere in the FY26 AR; a grep of the extracted text returns nothing. The AR's FY25 comparative is **2,414**: "Stipend to apprentices 3,059 2,414" at extracted/annual-report__Annual_Report_2026.txt L15083 (standalone Note 42.2, PDF p.227), repeated identically in the consolidated set at L19268. (3,059 − 2,414) / 2,414 = 26.72%, which rounds to the +26.7% upstream reported. The upstream figure was correct and the source-fidelity flag was raised in error. This is the LESSONS.md recurring pattern: "Verifier A (haiku) first pass mislabels severity, inventing false CRITICALs ... a matched figure ... is not a finding." Here it produced a false MAJOR rather than a false CRITICAL. Consequence had it stood: a hard, non-overridable gate would have barred a **correct** figure from every downstream computation. |
| 2026-09-10 | indnippon-2026-09-10 | FY26 working capital days | Pass 1 raised MAJOR, `source_fidelity: true`, noting three figures: AR letter 42→40, investor decks 42 (up from 40), and its own Gate 0 recomputation of 51.48 days | B05-concall raised the same contradiction as FLAG-CASH; B04-bizmodel ruled the reported WC-days summary an irrelevant ratio; Verifier A's own note says the reports "correctly flagged" it | GATE HELD — figure retained and correctly reclassified as a COMPANY ANOMALY, not an analysis defect | Resolved on re-audit. Verifier A showed the arithmetic and sources for all three figures: AR2026 p.9 MD&A (extracted L421-423) states "successfully reduced working capital days from 42 to 40 days"; the Q4FY26 deck p.19 and Q1FY27 deck p.18 bar charts both display FY26 = 42; and its own independent calculation gives FY26 = 51.48 days (receivable days 70.55 + inventory days 31.06 − payable days 50.13, revenue basis, 01-gate0.md L167-169). All three are real and all three are traceable. The contradiction lies **inside the company's own filed documents**, so under the severity rules this is a company anomaly faithfully transcribed, not a finding against the analysis. Retained on that basis. It bears on execution credibility, which is where B05 already placed it. |

## RESOLUTION OF THE RE-INVOCATION (2026-09-10)

Verifier A's single permitted re-invocation returned and resolved both entries.

**Withdrawal, with the mechanism named.** Verifier A withdrew its stipend finding
and identified its own error precisely: it had conflated the FY25 combined line
(Reimbursement of expenses 54 + Stipend to apprentices 2,414 = 2,458) with the
stipend-only line of 2,414. That is a better outcome than a bare withdrawal,
because it explains how the false base arose and confirms the upstream +26.7%
exactly. The clearance rests on the source line, quoted at its anchor, which is
the only mechanism the orchestrator permits.

**Coverage tripled.** 57 claims at pass 1 became 180 at re-audit, with acceptance
rising from 94.7% to 97.2% (175 clean of 180). critical_count 0, so REWORK is not
triggered on numerical grounds.

**One externally-sourced claim now stands verified, and it matters.** The SIAM
two-wheeler growth figure behind B04's FLAG-GROWTH-RECONCILIATION was confirmed
exactly at 36.1% (1.96 crore to 2.67 crore units), and the basis question the
orchestrator raised was answered: the table measures **domestic sales, not
production**, and **two-wheelers only, not all vehicle categories**. No basis
mismatch exists. B04's full-year underperformance finding therefore stands on
verified ground rather than on an unchecked third-party number.

**Net effect on the run.** Zero CRITICAL findings across all four verifiers. One
false source-fidelity flag raised and withdrawn. No upstream figure was corrected,
because none was wrong.

## CROSS-VERIFIER CONFLICT, OPEN AT HALT 1 (added 2026-09-10)

This entry is not a Verifier A source-fidelity disagreement. It is recorded here
because the log is the run's standing place for verifier conflicts that must not
be resolved silently, and because this one is the most decision-relevant item the
run produced.

| Item | B12b (Verifier B, Opus) position | Verifier A position | Disposition |
|---|---|---|---|
| FY26 audited-basis EBITDA margin | CRITICAL. Audited-basis margin was 11.11% (FY25) → 11.10% (FY26), flat to down, against the deck's 11.27% → 11.44%. The deck nets FX gains (Rs 372L FY26 vs Rs 102L FY25) into operating expenses, while Note 29 classifies them inside Other Income. Anchored to the Reg 33 results filing p.4 (FY26: revenue 1,06,848; expenses 96,828; finance 52; depreciation 1,792) and AR2026 Note 29 / Note 35. | SILENT. The deck-versus-audited margin reconciliation was outside Verifier A's task scope on both passes, and its single permitted re-invocation is spent. | OPEN — referred to Halt 1 as the first verification item |
| FY26 ROCE | CRITICAL. Deck ROCE 34.97% is 2.06x the audited Note 51 ROCE of 17%, on an undisclosed definition that appears to strip the entire Rs 531.5 cr investment book out of capital employed. Implies a QUALITY LADDER move from R2 to R5. | SILENT, same scope reason. | OPEN — referred to Halt 1 |
| credibility_grade | Would grade **D**, not the **C** B05 filed. | Not in scope. | UNRESOLVED, both grades carried to the operator. The orchestrator does not adjudicate a credibility grade; that is analysis. |

**Why this is left open rather than settled here.** Under Section 4, Verifier A is
the sole final authority on whether a number exists in a source, and Verifier C's
re-derivations and the synthesis narrative are subordinate to it on that question.
The margin claim is exactly such a question. Verifier A has not examined it, and
the orchestrator may not substitute its own reading for a verifier's on a matter
of analysis. So the honest disposition is to carry the conflict forward, name it
as the first thing to verify, and bar any Phase 3 valuation from using an FY26
margin until it is resolved.

**What rides on it.** If B12b is right, the mix-shift margin thesis that stages 4,
5 and 7 all lean on loses its only quantitative support. That is a thesis-level
consequence, not a footnote.

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
