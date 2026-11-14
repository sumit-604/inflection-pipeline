# Verifier disagreement log: onwardtec-2026-11-12 (phase 1)

Source: outputs/blocks/confidence.yaml disagreement_set; outputs/run-log.md. Appended to the Notion "Verifier Disagreement Log" page at save time.

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-11-12 | onwardtec-2026-11-12 | Gate 0 E4 contingent liabilities Nil | CRITICAL MISMATCH; Annual_Report_2026.pdf p.87 Note 26(a)(ii) Rs 394.68 lakhs (USD 4.20 lakhs) | Stage 1 run 1: scored E4 on "Nil (note 25a)" | GATE HELD: forced REWORK; GATE HELD: figure corrected at source (correct anchor shown), cleared by remediation cycle 1 | Orchestrator identity check confirmed at p.87; B12a-recheck confirms the corrected input; E4 score unchanged at 5 |
| 2026-11-12 | onwardtec-2026-11-12 | R&D credit Rs 292.60 lakhs anchored to results p.4 / p.8 | MAJOR ANCHOR NOT FOUND; Results_Q2FY27_BoardOutcome_2026-10-16.pdf p.3 (consolidated) and p.9 (standalone) | Stage 5: cited p.4 / p.8 | GATE HELD: figure corrected at source (correct anchor shown) | Orchestrator re-read the results PDF text; figure unchanged, anchor corrected in 05-concall.md line 13 |
