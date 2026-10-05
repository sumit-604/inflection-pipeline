# Verifier disagreement log: ESCONET, run 2026-10-05 (phase 1)

A row is a point where a downstream step's conclusion conflicts with a Verifier A source fidelity position. Append each row to the Notion "Verifier Disagreement Log" page at save time.

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-10-05 | ESCONET-2026-10-05 | FY26 operating margin 2.60% (CRISIL; FY25 5.09%) | B12a run 2 coverage_note: "Task-brief figures that have no source in the corpus (FY26 EBITDA 2.60%) were not counted". A coverage statement, not a findings row; source_fidelity not set. | Stage 13 synthesis: the figure exists in the corpus at inputs/rating/CRISIL_Esconet_Rating_Rationale_2026-07-02.txt line 29 ("Operating marg in has remained on the lower side at 2.60% in fiscal 2026 as compared to 5.09% in fiscal 2025"). The stage 5 report also cites it as CRISIL's (05-concall.md line 104). | FLAG CLEARED: source re-check found the number at a correct anchor. Re-checked by stage 13 synthesis (claude-opus-5-5) on the .txt extract; the HTML original (inputs/other/CRISIL_Esconet_RR_2026-07-02.html) was not opened. | The figure is CRISIL's operating margin, a different basis from the pipeline's FY26 EBITDA excluding other income (2.49%, B01). The B01 and B02 statements that 2.60% is not reproduced on their own basis stand. No final file uses 2.60%; the gate file uses CRISIL's 6% and 3% to 4% triggers at lines 36 and 39. Verifier A should confirm at its next pass. |

## Verifier A positions held without disagreement (not rows)

Listed so the record shows each standing source fidelity flag was respected. None of these is a disagreement.

- 03-ardeep promoter basis (82.50% / 60.09%): the final files use 89.18% before the IPO and 64.94% after it (PROSP p.21, p.35, p.182). GATE HELD, figure corrected at source.
- 04-bizmodel top five suppliers 52.35%: the final files do not use it; 53.15% is the correct figure (PROSP p.31, p.32). GATE HELD.
- 09-tam ZeaCloud turnover Rs 5.69 Cr: the final files use Rs 5.34 Cr (534.43 Lakhs, AR26 AOC-1 p.69). GATE HELD, figure corrected at source.
- 06-peers Netweb FY26 PAT 2,058 mn page cite: the final files do not use the figure or the derived 83% ratio. GATE HELD, figure removed.
- Verifier A run 1 MAJOR on the results filing balance sheet and CFO pages: stage 1 run 2 re-anchored to [page 14] and [page 15], and Verifier A run 2 verified them. Remediation in agreement, not a conflict.
- Verifier D confirmed Netweb FY26 PAT 2,058 at transcript lines 113 and 185, which sit on [page 3] and [page 5]. That matches Verifier A's source truth; no conflict.
- Verifier C run 2 re-derivations (N1 to N4) use B01 run 2 inputs, all clean in Verifier A's mandatory tier. N2 adds FY21 opening net worth 278.57 Lakhs (PROSP [page 232], [page 233]), a figure Verifier A has not yet checked. Not a conflict; listed for Verifier A's next pass.
