# VERIFIER DISAGREEMENT LOG — TITANBIO, phase 1, 2026-09-16

Every point where a downstream step's conclusion conflicts with a Verifier A
source-fidelity finding, or where the orchestrator struck or resolved a verifier
finding. Logged from day one per prompts/00-orchestrator.md Section 4. A disagreement
is not a REWORK trigger by itself. It is standing evidence on whether the out-of-family
Haiku read catches what the Opus verifiers miss.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-16 | titanbio-2026-09-10 | FY26 consolidated investing outflow: Rs 3,254.59 lakh or Rs 3,441.49 lakh | Re-run pass, MAJOR, source_fidelity true. Audited cash flow statement shows Rs 3,254.59 lakh on BOTH bases (AR FY26 p.116 standalone, p.162 consolidated). MD&A p.104 states Rs 3,441.49 lakh. Gap Rs 186.90 lakh, source of difference NOT FOUND. | Verifier B held that the 30-May-2026 consolidated filing shows (3,441.49) and that Rs 3,254.59 lakh "does not appear", and recomputed the FVTPL share as 73.1% against B05's 77% | GATE HELD — figure correct at source, anchor shown | Resolved AGAINST Verifier B. B02, B03, B05 and B07 used Rs 3,254.59 lakh as the audited figure and were right. The 77% share stands. The Rs 186.90 lakh MD&A-versus-audited gap is a real company disclosure inconsistency, first found by stage 2, independently re-verified by stage 3 and now by Verifier A. |
| 2026-09-16 | titanbio-2026-09-10 | FY26 exports Rs 80.33 cr, 39% of revenue, up 49.0% | Re-run pass verified the export figures clean against the source; no finding raised | Verifier B held these were "NOT FOUND in the AR sections read" and offered the Directors' Report "foreign exchange earned" series (Rs 5,208.41 / 5,295.20 / 8,897.37 lakh) as the disclosure that exists | GATE HELD — figure correct at source, anchor shown | Resolved AGAINST Verifier B, which had itself written "may sit in an unopened FOB export note; referred to Verifier A". Both measures exist and are different: exported goods (AR FY26 note, Rs 8,033.20 lakh) and foreign exchange earned (Directors' Report annexure, Rs 8,897.37 lakh). Verifier B's constructive point survives: the FX-earned series is disclosed in all three annual reports and implies exports supplied about 72% of the FY26 revenue increment, which stage 5 did not use. |
| 2026-09-16 | titanbio-2026-09-10 | Related-party purchases Rs 3,683.61 lakh, 37.1% of cost of materials consumed, used in B02, B03 and B04 | Re-run pass, MAJOR, source_fidelity true. Audited AR FY26 Note 41(a) itemises Peptech 44.79 + Phoenix 2,574.32 + Stalwart 986.20 + Titan Animal 78.30 = Rs 3,877.14 lakh, which is 39.1% of cost of materials consumed of Rs 9,916.35 lakh | B02 rank-1 finding, B03 FLAG-RPT-CONCENTRATION and B04 both state Rs 3,683.61 lakh and 37.1% | GATE HELD — figure corrected at source (correct anchor shown) | The audited total is HIGHER than the stages reported, so the finding those stages built on strengthens rather than weakens. Every downstream artifact in this run states the audited figure Rs 3,877.14 lakh and 39.1% with the Note 41(a) anchor, and names the stage figure it replaces. No stage re-run: the correction is a single figure with an audited anchor, and its direction does not change any verdict. |
| 2026-09-16 | titanbio-2026-09-10 | ADVENZYMES transcript corpus integrity | Not raised by Verifier A | Verifier D MINOR: an identical Q&A block "appears verbatim in two different ADVENZYMES transcript files", with the Nutrazyme and Wellfa content placed in the Nov-13-2025 transcript | GATE HELD — figure removed (finding struck on corpus evidence) | Struck by the orchestrator on a direct corpus check, not on judgment. The four ADVENZYMES PDFs carry four distinct md5 hashes, four distinct call dates and four distinct page counts (20, 24, 22, 23). The Nutrazyme and Wellfa block appears 3 times in the Feb-2026 file and 0 times in the Nov-2025 file. There is no duplication. Verifier D's misattribution finding against B06 STANDS; only its stated source_truth about where the content lives, and its duplication claim, are struck. |
| 2026-09-16 | titanbio-2026-09-10 | India microbiology culture media TAM, USD 194.4 million converted at Rs 96/USD | FIRST pass, MAJOR, source_fidelity true: claimed the correct conversion is Rs 18.66 crore against the stage's Rs 1,866 crore, "100x too large" | Stage 9 market sizing stated Rs 1,866 crore | FLAG CLEARED — source re-check found the number correct (re-checked by Verifier A itself on its re-run) | USD 194.4 million x 96 = 18,662.4 million rupees = Rs 1,866 crore. The stage was right; the verifier's own conversion was the error, and its internal cross-check ("global culture media USD 6.03 bn approx Rs 57.9 cr") carried the same million-versus-crore slip. The orchestrator re-invoked Verifier A once with the severity-semantics and coverage addendum per the standing LESSONS pattern; the re-run withdrew the finding and verified the market-sizing conversions clean. |

## Standing pattern this run adds to

The LESSONS.md recurring pattern "Verifier A (haiku) first pass mislabels severity,
inventing false CRITICALs" fired again, in a new form: not a false CRITICAL but a
false MAJOR built on the verifier's own arithmetic slip. The orchestrator check that
caught it was re-deriving the verifier's `source_truth` column, exactly as the pattern
prescribes. Two data points worth carrying forward: the slip was an Indian-unit
conversion (crore, lakh, million), and the re-run with the addendum both withdrew the
false finding AND surfaced two real ones the first pass had missed.

Second, and the opposite direction: the two Opus verifiers each produced a finding the
Haiku verifier's re-run then overturned on source (Verifier B on the investing outflow
and on the exports). The cross-family placement did its job in both directions this
run.
