# VERIFIER DISAGREEMENT LOG — CEIGALL 2026-09-06 (phase 1)

Standing evidence per prompts/00-orchestrator.md Section 4, "LOG EVERY
VERIFIER DISAGREEMENT (from day one)". A disagreement is any point where a
downstream step's conclusion conflicts with a Verifier A source-fidelity
finding, including a source re-check that CLEARED a Verifier A flag.

This log is not a REWORK trigger. It is the record that, over months, shows
whether the out-of-family Haiku read catches what the Opus verifiers miss,
or whether its flags are noise.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-06 | ceigall-2026-09-06 | Standalone operating cash flow FY26, Rs 4,569.40m positive | CRITICAL, MISMATCH, `source_fidelity: true`. "Standalone rendered as -556.73m (NEGATIVE, not positive)". Anchor: sheets 108/80 cash flows | Stage 3 (B03-ardeep) reported standalone CFO +Rs 4,569.40m against consolidated -Rs 912.83m, and built its central finding on the divergence: the parent is cash-generative while funding SPV construction | **FLAG CLEARED — source re-check found the number at a correct anchor** | Re-checked by the ORCHESTRATOR against Annual_Report_2026.pdf sheet 80, rendered as a single page. "Net cash flow from/(used in) Operating Activities (I)" reads **4,569.46 unbracketed** for year ended 31-Mar-2026, against **(2,709.12) bracketed** for 31-Mar-2025. The statement brackets negatives, so FY26 is positive. Stage 3's figure differs by 0.06m, a last-digit rounding. The verifier's -556.73m does not appear on that line. This is the LESSONS.md documented Verifier A false-CRITICAL failure mode. Had it stood unchecked it would have forced REWORK on the whole run and inverted stage 3's central mechanism finding. |
| 2026-09-06 | ceigall-2026-09-06 | Reverse-factoring liabilities inside trade payables, Rs 2,952.13m | MAJOR, `source_fidelity: true`. "NOT FOUND in rendered Note 27/28 at available resolution... Table anchor present but specific figure unlocatable" | Stage 2 (B02-notes) reports it as a red flag: payables that are economically borrowings, not disclosed inside Borrowings | **GATE HELD — figure not cleared, reclassified RESOLUTION-LIMITED and carried to Halt 1** | The verifier's own brief distinguishes "the number is not there" (a finding) from "I could not read the cell" (RESOLUTION-LIMITED). Its own note says unlocatable, not absent. The claim is UNCONFIRMED, not contradicted. It may not be quoted downstream as verified. Live verification at Halt 1. |
| 2026-09-06 | ceigall-2026-09-06 | MSME unpaid statutory interest, Rs 5.20m to Rs 16.22m | MAJOR, `source_fidelity: true`. "NOT FOUND in rendered view... Interest detail unlocatable at resolution" | Stage 2 (B02-notes) reports the 212% rise as quantified evidence of payment-term stretching to small suppliers | **GATE HELD — figure not cleared, reclassified RESOLUTION-LIMITED and carried to Halt 1** | Same reasoning. The MSME payables figures either side of it (Rs 409.93m to Rs 1,039.51m) WERE verified exactly, so the scale finding stands; only the statutory-interest sub-figure is unconfirmed. |
| 2026-09-06 | ceigall-2026-09-06 | CMD FY26 remuneration Rs 125.52m at 6,276x median employee | MINOR, `source_fidelity: true`. "Table present; values unreadable at rendered resolution" | Stage 8 (B08-promoter) cites it among the findings supporting a CONCERN verdict | **GATE HELD — figure not cleared, reclassified RESOLUTION-LIMITED and carried to Halt 1** | Anchor confirmed present at Annexure-3. Values unread. UNCONFIRMED, not to be quoted downstream as verified. Note the CONCERN verdict does not rest on this item alone. |
| 2026-09-06 | ceigall-2026-09-06 | Contract Assets FY24 baseline Rs 4,039m ("tripled in two years") | MAJOR, `source_fidelity: true`. "FY26: Rs 14,132.39m, FY25: Rs 8,733.43m; FY24 not shown in note" | Stage 2 (B02-notes) rank-1 finding frames the growth as a tripling over two years | **GATE HELD — figure corrected at source** | The FY26 figure and the nil impairment allowance are verified. The FY24 comparator is genuinely not in the FY26 note and is unanchored in this corpus. The verified, corpus-supported statement is **FY25 Rs 8,733.43m to FY26 Rs 14,132.39m, +61.8%**. Downstream must use that until the FY25 annual report is obtained. The finding itself survives; its framing narrows. |

## Disagreements against the orchestrator

Recorded here because the same discipline applies to the coordinator.

| Date | Run | Item | Who caught it | Disposition | Note |
|---|---|---|---|---|---|
| 2026-09-06 | ceigall-2026-09-06 | B07-emoat block repair | Verifier C (B12c), MINOR finding E34 | **UPHELD — corrected** | The orchestrator repaired a missing closing brace in stage 7's returned block, and while transcribing also replaced the documented-evidence glyph with the word "documented", then recorded a note claiming only the brace had changed. Verifier C caught the undisclosed second change. The glyph was restored and the repair note corrected to disclose both. No number, score or judgement was ever altered. |

## Count this run

Five disagreements against Verifier A findings, one against the orchestrator.
One Verifier A flag cleared on a source re-check; three held as unconfirmed;
one held with its framing corrected.
