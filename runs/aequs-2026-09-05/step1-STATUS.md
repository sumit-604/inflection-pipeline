# STEP 1 STATUS — Aequs Ltd (AEQUS) — 2026-09-05

## OUTCOME: STOPPED AT THE CORPUS STEP (real blocker, per contract)

Step 1 ran in a REMOTE cloud container, not the operator's local Windows
machine. The screener corpus collector cannot run here. Two hard reasons:
- No collector `.env` (screener login). It is gitignored and absent in this
  ephemeral container. The Step-1 skill says: if `.env` is missing, STOP.
- screener.in is blocked by this container's network egress proxy. Even a
  manual screener fetch returns EGRESS_BLOCKED.

So Steps E-F (companies.txt collect) and Step H (Phase 1 stages 0-9 +
verifiers + dossier) did NOT run: there is no corpus on disk, and the
framework's Gate-0 screener CSVs cannot be produced here. Estimating those
numbers is barred (CLAUDE.md NEVER: "Never estimate a missing number").

## WHAT WAS DELIVERED (collector-independent shelf)
- Step A identity: AEQUS, BSE 544634, ISIN INE947N01017, listed 2025-12-10,
  CMP ~Rs 254, market cap ~Rs 16,250 cr. Screener consolidated URL recorded.
- Step B business brief with 4 load-bearing facts: step1-business-brief.md.
- Step C peers (economic-engine match): AZAD, DYNAMATECH, DIXON (Bull_AI
  confirmed). Rationale in the brief.
- Step D sector cap row: "Recycling / Manufacturing" 25x; aerospace-precision
  has no dedicated row (flag for phase-3).
- Step E companies.txt written for a LOCAL collector run.
- Step G spear override + load-bearing facts + rulings: companies/AEQUS.md.
- Run folder scaffold with empty inputs/ (from runs/_template).

## OPERATOR NEXT STEP (choose one)
1. LOCAL COLLECT (matches the documented flow). On the Windows machine, with
   the screener `.env` in place, from tools/collector run:
     PYTHONUTF8=1 py collect_to_repo.py --dry-run
   companies.txt is already written. Then repair the manifest defects
   (sector_cap_row is already set to "Recycling / Manufacturing"; confirm the
   FY26 AR and the screener CSVs), commit the corpus, and run /run-pipeline
   runs/aequs-2026-09-05 to Halt 1.
2. IN-CONTAINER via Bull_AI (needs operator go-ahead; a deviation from the
   documented collector flow). Bull_AI has AEQUS coverage: FY26 annual report,
   Q3/Q4 FY26 + Q1 FY27 transcripts, investor presentations, press releases.
   I can extract those to page-marked .txt into inputs/ and run the
   document-reading stages off primary filings. Gaps: the screener financial
   CSVs that feed the Gate-0 quantitative scorecard would be reconstructed
   from the AR/presentation P&L/BS/CF, a documented degradation, not the
   collector's CSVs. Bull_AI is metered; the annual report is large.

Bull_AI availability snapshot (2026-09-05), for reference:
- annual_report FY2026 (Reg. 34), uploaded 2026-08-13.
- concall transcripts: Q3 FY26, Q4 FY26, Q1 FY27 (latest 2026-08-04).
- investor presentations: Q1 FY27 (2026-07-29) and earlier.
- press releases, takeover/acquisition disclosures, postal ballots.

## GIT
Intake shelf committed to branch claude/aequs-step-one-42trpa. Hash and
git log -1 --stat in the session report.
