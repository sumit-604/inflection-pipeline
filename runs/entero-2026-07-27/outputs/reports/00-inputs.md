# Stage 0 — Input Validation: ENTERO (Entero Healthcare Solutions Ltd)

Run folder: `runs/entero-2026-07-27` · Run date 2026-07-27 · CMP Rs 1,273 (manifest)
Spear gate: OVERRIDE 2026-08-29 (operator) — gate satisfied.
Empty-folder confirmation: operator instruction "run the full pipeline on these
files" = PROCEED WITH GAPS (explicit). No further gap question this run.

## Inventory (identified by content, not filename)

| Folder | Count | Documents |
|---|---|---|
| annual-report | 1 | FY26 AR, 276pg (filed 2026-07-27) |
| results | 3 | Q3 FY26 (12-Feb-2026); FY26 full-year audited; Q1 FY27 (07-Aug-2026) |
| concalls | 5 | Q1FY26 (Aug-25), Q2FY26 (Nov-25), Q3FY26 (Feb-26), Q4FY26 (Jun-26), Q1FY27 (17-Aug-26) |
| peer-concalls | 12 | RPTECH x4, MEDPLUS x4, REDINGTON x4 |
| presentation | 4 | Q1FY27 deck (07-Aug-26), FY26 deck (25-May-26), + 2 broker notes (misfiled) |
| rating | 1 | India Ratings, IND A-/Stable (03-Dec-2025); image PDF, renders via poppler |
| screening | 30 | ENTERO + RPTECH/MEDPLUS/REDINGTON/OPTIEMUS CSV sets |

Stage 5 uses the 3 newest concalls (oldest first): Q3 FY26 -> Q4 FY26 -> Q1 FY27.

## Gaps (recorded, run proceeds degraded)

- **prospectus — HIGH.** Entero listed ~Feb 2024, inside ~3 years. No DRHP.
  Backward baseline and promoter/group map lean on the FY26 AR and web.
- **announcements — MEDIUM.** No Reg 30 record; intent-and-action cross-check
  runs on concall/AR evidence only.
- **shareholding — MEDIUM.** No quarterly pattern; FII+DII unresolved, UA
  withheld at stage 11, pledge trend from AR with staleness noted.
- **research — LOW.** Folder empty; 2 broker notes misfiled in presentation/,
  treated as non-anchored leads.

## Freshness pair check

All four pairs PASS. Newest results (Q1 FY27) has its same-quarter concall;
rating carries its full rationale; no SEBI order referenced; FY26 AR matches the
latest audited annual. **Verdict: FRESHNESS PAIRS OK** — no freshness cap.

Note: rating rationale already states negative free cash flow since inception,
management guiding FCF positive from end-FY26. This feeds FLAG-CASH downstream.
