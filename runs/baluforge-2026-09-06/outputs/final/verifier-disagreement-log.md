# VERIFIER DISAGREEMENT LOG — BALUFORGE 2026-09-06 (Phase 1)

A disagreement is any point where a downstream step's conclusion conflicts with a
Verifier A source-fidelity finding, or where a source re-check clears or overturns
a flagged figure. Logged from day one per prompts/00-orchestrator.md Section 4.
This is standing evidence, not a REWORK trigger.

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|------|-------------------|--------------|-----------------------------|-------------------------------|-------------|------|
| 2026-09-06 | BALUFORGE-2026-09-06 | FY2025 consolidated ROCE, 24.75% | MISMATCH. EBIT of 264.90 cr includes 17.14 cr of other income and FX gains. AR2025 p.161 MD&A gives EBITDA excluding other income separately, so EBIT is 247.76 cr and ROCE is 23.16%. source_fidelity true | B01 Gate 0 used 24.75% in Block A scoring. No downstream stage disputed it | GATE HELD — figure corrected at source (AR2025 p.161, ROCE 23.16%) | Decision-neutral for the Gate 0 classification, which is capped at AVERAGE by deal-breaker #4 either way. Binds Phase 3: stages 10 and 11 must consume 23.16%. |
| 2026-09-06 | BALUFORGE-2026-09-06 | Trade receivables >6mo overdue 32.8% to 58.8% of gross, with the ECL allowance cut 576.48 lakh in the same year | Re-checked against source and found EXACT (Note 15 p.129, Note 36 p.138). Verifier A states the flag stands as raised and is not a report error. source_fidelity false | B02, B03, B05 and B07 all carry this as a live FLAG-CASH finding | FLAG CLEARED — source re-check found the numbers at their stated anchors (re-checked by Verifier A, haiku, out of family) | Recorded because a verifier re-check confirmed rather than overturned a maker's finding. The company-quality flag is unaffected and propagates. |

## Non-A source-fidelity corrections this run

Verifier D is not the source-fidelity authority, but it found a citation that does
not exist in the source it names. Recorded here for the same standing-evidence
purpose.

| Date | Run | Claim | Verifier D verdict + anchor | Disposition | Note |
|------|-----|-------|-----------------------------|-------------|------|
| 2026-09-06 | BALUFORGE-2026-09-06 | B06 Claim 5, steel pass-through, attributed to "MMFL Feb 2026 p.10" | The quote does not appear in any MMFL transcript. It is verbatim from HAPPYFORGE Feb 2026 p.9 | GATE HELD — figure corrected at source (citation reassigned to HAPPYFORGE Feb 2026 p.9; MMFL struck from the claim's peer list, three peers reduced to two) | Classification stays PARTIALLY VERIFIED on two independent peers. B06's load-bearing CONTRADICTED verdict rests on Claims 1 and 2 and is unaffected. |
