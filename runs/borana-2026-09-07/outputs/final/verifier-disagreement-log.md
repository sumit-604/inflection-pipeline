# VERIFIER DISAGREEMENT LOG — BORANA, run 2026-09-07 (phase 1)

Standing rule, orchestrator Section 4: a disagreement is any point where a
downstream step's conclusion conflicts with a Verifier A source-fidelity
finding, or where a source re-check clears one. Every disagreement is logged.
None is ever resolved silently. This log is NOT a REWORK trigger by itself.
It is the standing evidence that, over months, shows whether the out-of-family
Haiku verifier catches what the Opus verifiers miss, or whether its
disagreements are noise.

Six rows this run. Four are orchestrator source re-checks of verifier findings.
Two are corrections to claims that entered the run through the operator-written
manifest and company memory rather than through a stage.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-07 | borana-2026-09-07 | Board's Report Return on Net Worth FY26 23.03% vs Note 40 ROE 35.01% | CRITICAL, source_fidelity true. "Board's Report mislabels CLOSING net worth as 'Average', producing understated ROE" (AR FY2026 p.74 vs p.128) | B03 AR deep dive reported BOTH figures and logged the contradiction explicitly in its triple_pass_verification.discrepancies field | GATE HELD — figure corrected at source (correct anchor shown), severity downgraded CRITICAL to MAJOR by orchestrator | Orchestrator re-read both pages. AR p.74 carries "Net Profit after tax 6,486.89 / Average Shareholder's Equity 28157.50 / Return on Net Worth 23.03%"; p.128 carries "35.01% 59.45%". Both exist exactly as B03 described. The defect is the COMPANY's, inside its own annual report; no stage misread anything. The flag rules define CRITICAL as a fabricated or materially misread figure and expressly exclude a faithfully transcribed company anomaly. REWORK not triggered by this path. Re-checked by: orchestrator. |
| 2026-09-07 | borana-2026-09-07 | Lease liability FY26 Rs 130.80 lakh / FY25 Rs 150.12 lakh | MINOR, source_fidelity true, recorded as UNANCHORED: "claimed in B02 text but not located in grep search... likely present in AR but unanchored in extraction" | B02 notes triple-pass carried both figures as anchored to the Ind AS 116 lease note | FLAG CLEARED — source re-check found the number at a correct anchor | Orchestrator re-read the source. Both figures are present at AR FY2026 page 110. The verifier's grep did not reach them; the extraction is not deficient and B02's figures are correct. Re-checked by: orchestrator. |
| 2026-09-07 | borana-2026-09-07 | "Two secretarial-auditor resignations six days apart", 24-Jul-2026 and 29-Jul-2026 | Not a Verifier A finding. Raised by Verifier B (B12b pipeline_flags_not_supported, MAJOR) against B05, which cited it three times | Claim originated in the operator-written manifest.yaml and companies/BORANA.md ("Three filings in six days"), propagated into B00 input_gaps, B03, B05 and B08, and into the orchestrator's own interim reporting | GATE HELD — claim corrected at source | Orchestrator re-read both filings. There was ONE resignation. The 29-Jul-2026 filing opens "In continuation of our intimation dated 24/07/2026 regarding resignation of Mr. Jitendrakumar Rewashankar Rawal" and reports that "the Board of Director's at their meeting held Today, 29/07/2026 have noted the Resignation". It is the Board minuting the same resignation, filed the same day as the successor's appointment. A routine two-step reported as a pattern. Re-checked by: orchestrator. |
| 2026-09-07 | borana-2026-09-07 | Secretarial auditor resigned "with no reason stated" | Not a verifier finding. Raised by the orchestrator while verifying the row above | Claim originated in manifest.yaml and companies/BORANA.md; carried by B00 and repeated downstream | GATE HELD — claim corrected at source | The resignation letter enclosed with the 24-Jul-2026 filing (p.3) states: "Due to pre-occupation with professional assignments and unavoidable professional commitments, I regret my inability to continue as the Secretarial Auditor of the Company," and adds "I further confirm that there are no disputes, differences, or pending issues between me/us and the Company which have led to this resignation." Re-checked by: orchestrator. |
| 2026-09-07 | borana-2026-09-07 | Secretarial auditor resigned "~15 months into a 5-year mandate commencing Apr-2025" | Not a verifier finding. Raised by the orchestrator while verifying the two rows above | B08 promoter check carried this as its sole named deal_breaker; B12b repeated "mid-term exit" | GATE HELD — figure corrected at source | The same resignation letter states the appointment was "for the financial year 2025-26 and 2026-27", a TWO-year term. The resignation falls in the second year of a two-year term, not 15 months into five. The deal-breaker is not withdrawn (an auditor resignation inside three years still stands) but its stated basis is corrected and its weight is the operator's to reset at Halt 1. Re-checked by: orchestrator. |
| 2026-09-07 | borana-2026-09-07 | FY26 annual report approved 14-Aug-2026, "seven months after the call" | Not a Verifier A finding. Raised by Verifier B (B12b pipeline_flags_not_supported, MINOR) against B05 | B05 concall analysis used the date in sections 1C and 2D to size the gap between the call and the filing | GATE HELD — figure corrected at source | AR FY2026 p.126 states twice: "The financial statements for the year ended 31st March, 2026 were approved by the Board of Directors on 14th May, 2026." The interval from the 27-Jan-2026 call is 3.5 months, not seven. The underlying finding, that the margin driver management gave on the call is absent from the AR, is unaffected and stands. Re-checked by: orchestrator. |

## READING FOR THE STANDING RECORD

Verifier A (Haiku, the only out-of-family read on the numbers) raised seven
findings on its second run. Six were upheld as written. One was downgraded on
severity and one was cleared outright. Neither error was in the direction the
LESSONS catalogue warns about most: the catalogue records Verifier A inventing
false CRITICALs, and it did propose one here, but its first run was the
opposite failure, a shallow pass at 15 numbers with zero findings that needed
a coverage addendum to correct.

The more useful signal this run is that Verifier B (Opus) caught three
CRITICAL disclosure-integrity defects that no stage reached, and separately
caught two upstream claims that were not supported by their own sources. The
verification layer earned its cost this run, and it earned it in both
directions: it found what the stages missed, and it removed a governance
signal the stages had overstated.

Note on provenance for the operator. Three of the six rows correct claims
that entered the pipeline through manifest.yaml and companies/BORANA.md, not
through a stage. The stages carried them faithfully. That is a corpus-intake
failure mode, not a stage failure mode, and no verifier in the current design
audits the manifest.
