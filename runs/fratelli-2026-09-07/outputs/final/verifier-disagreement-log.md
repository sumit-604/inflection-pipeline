# VERIFIER DISAGREEMENT LOG — FRATELLI, run 2026-09-07

Every point where a downstream step's conclusion conflicts with a Verifier A
source-fidelity finding. Not a REWORK trigger by itself. It is the standing
evidence of whether the out-of-family numerical check catches what the
in-family verifiers miss.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|------|-----|--------------|------------------------------|--------------------------------|-------------|------|
| 2026-09-07 | fratelli-2026-09-07 | FY2025 revenue Rs 276.25 cr, used in Gate 0 | Run 1: CRITICAL, source_fidelity true. Says AR consolidated FY25 is Rs 302.10 cr (AR FY26 P&L, Rs 30,209.66 lakh) | Orchestrator did NOT clear or downgrade it. Verifier A's own claimed column recorded the figure as labelled "(screener-data)" in the Gate 0 report, which is the basis-difference category its severity rules exclude from CRITICAL. Re-invoked Verifier A once, per the LESSONS.md remedy, to re-decide on source. | PENDING — awaiting Verifier A run 2 | Orchestrator has no authority to resolve this. Verifier A run 2 decides. |
| 2026-09-07 | fratelli-2026-09-07 | FY2024 revenue Rs 421.35 cr, used in Gate 0 | Run 1: CRITICAL, source_fidelity true. Says AR consolidated FY24 is Rs 451.07 cr (AR FY25 P&L, Rs 45,107.48 lakh) | Same as the row above. Not cleared, not downgraded, re-put to Verifier A. | PENDING — awaiting Verifier A run 2 | Same. |
