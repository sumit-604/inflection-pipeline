# Verifier disagreement log: MMP 2026-10-04 (phase 1)

Scope: every point where a stage output conflicted with a Verifier A source fidelity finding (`source_fidelity: true`), and what the gate did with it. Sources: run-log.md (2026-10-05 entries), B12a-run1.yaml, B12a-run2.yaml. Append each row to the Notion "Verifier Disagreement Log" page at save time.

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-10-05 | MMP-2026-10-04 | Anti-dumping duty on Chinese foil "Rs 619-873 per MT" | MAJOR, MISMATCH (currency): US$619-$873/MT, Q1 FY27 investor presentation [page 25], Foil bullet (B12a run 1) | Stage 4 report 04-bizmodel.md 1D carried the figure in rupees; stage 7 already had US$ | GATE HELD: figure corrected at source (US$619-873 per MT, Q1 FY27 deck p.25) | Corrected in place by the orchestrator, marked in the text |
| 2026-10-05 | MMP-2026-10-04 | Analyst question "Rs 150 Cr capex and Rs 18 Cr interest" | MAJOR, MISMATCH: May-26 call [page 15] states INR 13 Cr finance cost on INR 180 Cr gross borrowing, capex INR 30 + 15 + 90 Cr, CFO INR 53 Cr (B12a run 1) | Stage 5 report 05-concall.md 3C row 2 attributed 150 and 18 to the analyst | GATE HELD: figure corrected at source (May-26 call [page 15]) | Verifier B found the same misquote independently (B12b, MINOR). The unanchored "about Rs 150 Cr" rounding in B05 peer_questions and 06-peers Q8 is a separate non source fidelity row; synthesis does not carry it |
| 2026-10-05 | MMP-2026-10-04 | Current valuation "25.6x P/E" | MAJOR, UNANCHORED and material: no source in the run reproduces it; screener Data_Sheet (price 449.6, market cap 1,142.1) gives 36.8x on FY26 PAT and about 22.8x on trailing PAT (B12a run 1) | Stage 9 report 09-tam.md 5E used it from company memory (step 1 brief), labelled "not anchored" | GATE HELD: figure removed | Stage 11 owns the multiple; phase 1 synthesis carries no P/E |
| 2026-10-05 | MMP-2026-10-04 | Gate 0 E4 contingent liabilities 7,133.72 L (standalone Note 47) over consolidated net worth; "no separate consolidated note found" | MAJOR, source fidelity: consolidated Note 51 exists at AR26 [page 241], 445.72 L, 1.3% (B12a run 1) | Stage 1 run 1 scored E4 = 1 (20.6%). Verifier C run 1 F1 (CRITICAL) agreed with Verifier A | GATE HELD: figure corrected at source (stage 1 run 2: 445.72 L / 34,650.78 L = 1.29%, E4 = 5, AR26 p.241) | Remediation cycle 1. With the other run 1 fixes, core moved 39 to 54 and class AVOID to AVERAGE |
| 2026-10-05 | MMP-2026-10-04 | "Capital commitments 7,621.61 L" (Note 52) | MAJOR, MISMATCH on label and value: AR26 p.241 Note 52 capital 5,642.27 L, other 1,979.34 L, total 7,621.61 L (B12a run 2) | Stage 1 run 2 report 01-gate0.md Block E and B01 data_notes stated 7,621.61 L as capital commitments | GATE HELD: figure corrected at source (5,642.27 L capital, 1,979.34 L other, 7,621.61 L total, AR26 p.241) | Not an E4 score input; no score effect. Corrected in place by the orchestrator |

By disposition:
- GATE HELD, figure corrected at source: 4 rows.
- GATE HELD, figure removed: 1 row.
- GATE HELD, forced REWORK: none.
- FLAG CLEARED, source re-check found the number at a correct anchor: none.

Synthesis position: this synthesis kept no figure Verifier A flagged. It made no re-derivation on a flagged number and found no reason to dispute any source fidelity row.

Not counted as disagreements:
- Anchor only source fidelity rows (MINOR): B12a run 1 rows on 03, 05, 07 and 09, and B12a run 2 rows on 07. Each figure exists in the same document one page away. No step contested them. The run log leaves them for the dossier to cite at the correct marker. This synthesis uses the corrected markers where it cites them.
- Non source fidelity rows (derived arithmetic and provenance): 09-tam 5E 12.9% to 13.8%, corrected in place; 05-concall 1B growth range and 09-tam 1B 8.1%, both still open. These rows fall outside the gate, and synthesis carries none of the wrong figures.
