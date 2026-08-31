# VERIFIER DISAGREEMENT LOG — CMS Info Systems (CMSINFO)

One row per point where a downstream step conflicted with a Verifier A source fidelity finding. Appended to the Notion "Verifier Disagreement Log" page at save time.

| Date | Run | Number / claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-08-29 | cmsinfo-2026-08-29 | Receivables ageing: SA 1-2yr overdue Rs92.14m to Rs1,490.59m (16.2x); CON Rs177.94m to Rs1,516.32m (8.5x); SA loss allowance released 14.1% (Rs533.94m to Rs458.80m) | MAJOR, source_fidelity true. B12a: figures cited with correct AR note and page anchors (Note 12/37, SA p.99/147, CON p.131-133/147) but the ageing table structure was not independently re-verified in the available ASCII text; extraction limitation, not fabrication. | B02-notes (Rank 1 and 2, FLAG-CASH) and B03-ardeep (Phase 2 triple pass) carried the figures as the load bearing red flag; B11 valuation and the gate disposition rest on FLAG-CASH INDETERMINATE built on them. Position: keep and rely on the figures. | GATE HELD, figures confirmed at source. Orchestrator grep of the AR page marked text confirmed SA 1-2yr overdue Rs1,490.59m (line 9179, about p.99 SA), CON Rs1,516.32m (line 12284, about p.131 CON), SA prior Rs92.14m (line 9218), CON loss allowance Rs825.71m (line 11485). Re-checked by: orchestrator, 2026-08-29. | The verifier limitation was ASCII table collapse, not a source mismatch. Downstream reliance was correct. No figure was carried that Verifier A had flagged as non existent; the anchor was validated, not overridden. |

## Note on the Verifier D peer citation errors

The QUESS "Rs176cr Labour Code pass through" (CRITICAL) and the AGSTRA "high receivable days" Jul 2024 misattribution (MAJOR) are Verifier D peer citation findings against B06's supporting cross read, NOT Verifier A source fidelity findings. They do not belong in this log. Both were corrected at synthesis and are not cited anywhere in the recommendation; the core DSO contradiction verdict stands on independently confirmed Radiant and SIS anchors. Recorded here only to state their exclusion.
