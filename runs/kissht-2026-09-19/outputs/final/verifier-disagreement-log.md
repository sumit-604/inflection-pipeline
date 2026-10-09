# Verifier disagreement log: KISSHT, run 2026-09-19 (phase 3, final)

Appended to the Notion "Verifier Disagreement Log" page at save time (claude.ai executes; the pipeline never writes).

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|

none

## Status of the one Verifier A source fidelity item (not a disagreement)

- Item: FY23 consolidated CFO, screener Rs 48.36 Cr against RHP restated Rs 111.48 Cr (RHP p.271).
- Verifier A: MINOR, source_fidelity true. Both values exist in their sources (screener line 57; RHP p.271). The conflict is disclosed and the basis is stated per calculation (B12a findings row 1).
- Downstream handling, phase 1 and phase 3: no step treated either value as settled. Stage 10 records "Neither (unresolved); both listed separately" (B10 conflicts). Stage 11 and the thesis stage use no FY23 CFO in any pillar input; the lender multiplier is Pillar 2L, not a cash multiplier (B11 pillar_detail.cash_multiplier_type). The operator's GROWTH INDUCED ruling (fttcp-deliberation ruling 7) rests on the Ind AS 7 loan disbursal mechanic, not on the FY23 value.
- Where the value travels: the cumulative CFO of minus Rs 1,648.00 Cr (ratio minus 2.46x) is built on the screener series and so embeds Rs 48.36 Cr (B01 B1). Every final deliverable carries it with the FLAG-DISAGREEMENT label. On the RHP value the cumulative would read minus Rs 1,584.88 Cr and the ratio minus 2.36x [INFERENCE: -1,648.00 + (111.48 - 48.36); / 671.20]. No band, flag determination or pillar input changes.
- Defect noted: B10 input_gaps line 19 labels this item "FY26 CFO conflict". The B10 conflicts section labels it correctly as FY23. The mislabel changes no value.
- Disposition: GATE HELD. Carried labelled as unresolved; not corrected against a source, not removed, no re-check cleared it.

## Routed to Verifier A, not yet checked by Verifier A

- Verifier C phase 3 F24 (MINOR): B10.bvps_fy26_rs Rs 131.33 divides Si Creva's equity (Rs 1,231.98 Cr, AR p.57 AOC-1) by OnEMI shares. Verifier C gives consolidated FY26 BVPS Rs 143.2. No final deliverable carries Rs 131.33 as valid. This is a Verifier C finding, so it is not a row in the table above.
