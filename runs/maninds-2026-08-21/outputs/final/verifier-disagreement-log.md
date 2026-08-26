# Verifier Disagreement Log — MANINDS (runs/maninds-2026-08-21)

One row per point where a downstream step's conclusion conflicted with a Verifier A source fidelity finding. Appended to the Notion "Verifier Disagreement Log" page at save time.

| Date | Run | Number / claim | Verifier A verdict + anchor | Downstream step + position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-08-21 | maninds-2026-08-21 | B03 standalone CFO/PAT 0.693x FY25 | MAJOR, source_fidelity true, "does not recalculate"; Verifier A used screener Data_Sheet CFO Rs67.99 Cr, the consolidated line | B03 (stage 3) sourced 0.693x from the AR FY25 standalone cash flow statement | FLAG CLEARED — source re-check found the number at the correct anchor: AR standalone CF, CFO Rs95.06 Cr / PAT Rs137.12 Cr = 0.693x. Screener CFO Rs67.99 Cr / standalone PAT reproduces the separately stated consolidated 0.444x. Re-checked by orchestrator against the AR standalone CF extract, 2026-08-21 | FLAG-CASH direction unaffected; standalone 0.693x and consolidated 0.444x both below the 0.7x threshold. Source fidelity gate PASS; 0 CRITICAL; acceptance 96.6% |

## Devil finding (not a Verifier A source fidelity item)

Recorded separately per the finalize spec. Not a source fidelity conflict; a modeling contradiction flagged by Role 3.

- B15 unreconciled contradiction, B11 corrected CE walk: B11 states the CE walk change is "the ONLY change" (Rs470 Cr bargain gain). Anchor npc_wc_per_revenue records NPC working capital at about Rs500 to 625 Cr per Rs1,000 Cr of revenue (transcript p.15), so the FY27 to FY29 NPC ramp adds about Rs650 to 800 Cr of working capital the CE walk does not carry. If reloaded, FY29 base ROCE falls from 16.5% toward 14.8% and base fair value from Rs611 toward Rs450 to 500. Disposition: carried as the load bearing devil caveat; the operator ruled no CE re-run beyond the bargain gain, so the primary entry zone Rs219 to 313 stands and the reload is flagged for operator revisit. This is a Role 3 modeling flag, not a Verifier A existence of a number finding.
</content>
