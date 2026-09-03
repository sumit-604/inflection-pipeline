# Verifier Disagreement Log — vilas-2026-09-03 (phase 1)

Two Verifier A (Haiku) source-fidelity flags were re-checked against the
source and CLEARED. Both are Verifier A arithmetic slips; the pipeline
report figures verify exactly at the source. Re-check performed by the
orchestrator by re-reading the FY26 audited results text sidecar (the same
source Verifier A used) and re-deriving on the fixed Gate 0 formulae.
Nothing was resolved silently.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-03 | vilas-2026-09-03 | FY26 Current Assets / Current Ratio | MISMATCH (source_fidelity:true). Verifier A: CA Rs 297.51 Cr, CR 3.97x, vs report Rs 287.51 Cr / 3.83x (12a Finding #8, Block D) | Orchestrator source re-check: report figure is correct | FLAG CLEARED — source re-check found the number at a correct anchor (orchestrator) | Sidecar FY26 current-asset line items (Inventories 7233.25 + Cur.Investments 1187.28 + Trade Rec 7749.58 + Cash 1847.36 + Bank 7589.08 + Loans 0.87 + Oth Fin Assets 4.47 + Oth Cur Assets 3139.28 Lacs) sum to 28,751.17 Lacs = Rs 287.51 Cr. CL = 7,504.67 Lacs = Rs 75.05 Cr. CR = 287.51/75.05 = 3.831x. Report correct; Verifier A over-added current assets by exactly Rs 10 Cr. |
| 2026-09-03 | vilas-2026-09-03 | FY26 Payable Days | MISMATCH (source_fidelity:true). Verifier A: ~50 days (COGS basis, trade payables Rs 53.33 Cr) vs report 22.25 days (12a Finding #19, Block B4) | Orchestrator source re-check: report figure is correct | FLAG CLEARED — source re-check found the number at a correct anchor (orchestrator) | Gate 0 fixed formula is Payable Days = Trade Payables / Revenue x 365 (revenue basis, not COGS). Trade Payables FY26 = MSME 25.51 + others 2782.37 = 2807.88 Lacs = Rs 28.08 Cr. 28.08 / 460.67 x 365 = 22.25 days. Report correct; Verifier A used a COGS basis and a trade-payables figure (Rs 53.33 Cr) that does not match the sidecar (Rs 28.08 Cr). Verifier A itself flagged this finding as unconfirmed ("cannot confirm component"). |

Effect on numerical acceptance: with both MAJORs cleared, Verifier A's
effective clean rate is 28/29 = 96.6% (the one remaining MINOR is a
25.33x-vs-25.4x interest-cover rounding, immaterial). The raw B12a
acceptance_rate of 89.7% is retained as the reported metric; the effective
figure is used in the confidence delta with this clearance noted.

No CRITICAL source-fidelity finding stands. No REWORK trigger from Verifier A.
