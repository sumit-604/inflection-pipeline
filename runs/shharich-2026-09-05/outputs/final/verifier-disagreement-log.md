# VERIFIER DISAGREEMENT LOG

One row per point where a downstream step's conclusion conflicted with a Verifier A source
fidelity finding, or where a source re-check cleared one. Fixed row shape. This file is
appended to the Notion "Verifier Disagreement Log" page at save time.

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-05 | shharich-2026-09-05 | PAT FY26 Rs 411.81 lakh, consolidated | Run 1: MAJOR, source_fidelity true, "not a P&L line", cited anchor AR FY26 p. 59 (Board's Report). Run 2: MATCH at AR FY26 p. 59, source_fidelity false | Stage 1 Gate 0 (B01) used 411.81 as the FY26 consolidated PAT with the p. 59 anchor and held that position | FLAG CLEARED, source re-check found the number at a correct anchor (re-checked by Verifier A run 2 on the orchestrator's coverage addendum) | Source internal difference stands and is carried forward: the Board's Report p. 59 prints 411.81 while the audited consolidated P&L p. 145 prints 414.95. Verifier B logs that difference separately as a MAJOR finding against stage 5. It is a basis question for method selection downstream, not a source fidelity failure |
| 2026-09-05 | shharich-2026-09-05 | Promoter family components 370.22 + 94.70 + 132.00 = Rs 596.92 lakh, Note 35.7 pp. 128 to 129 | Run 1: MAJOR, source_fidelity true, "anchor not found in the sections reviewed". Run 2: MATCH at pp. 128 to 129, source_fidelity true, all components and total verified as anchored | Stage 2 notes (B02 finding 1) and stage 3 both used Rs 596.92 lakh at 112.7% of standalone FY26 PBT and held that position | FLAG CLEARED, source re-check found the number at a correct anchor (re-checked by Verifier A run 2 on the orchestrator's coverage addendum) | The totals are sums of printed per person rows, not printed totals: managerial remuneration 121.20 + 108.00 + 98.40 + 42.62 = 370.22; relatives' salary 22.70 + 24.00 + 24.00 + 24.00 = 94.70; rent 33.00 + 39.00 + 33.00 + 27.00 = 132.00 |

No other disagreement was found in the blocks. Verifier A run 2 is the binding B12a; run 1 is
retained at outputs/blocks/B12a-verifier-numerical-run1.yaml for the record.
