# RUN LOG — Quarterly Analysis Pipeline
## BALAMINES (Balaji Amines Limited) — Q1 FY27 (quarter ended 30 June 2026)

Orchestrator: `/run-quarterly` (quarterly-00-orchestrator v1.0)
Run started: 2026-07-28
Operator request: "Please analyse the latest quarterly results of Balaji Mines."
Note: request said "Balaji Mines"; the actual issuer is **Balaji Amines Limited**
(NSE: BALAMINES, BSE: 530999), a speciality chemicals manufacturer. Confirmed from
both filings (Scrip Code 530999, CIN L24132MH1988PLC049387).

### Toolchain precheck
- pdftotext, pdfinfo: installed at session start via `apt-get install poppler-utils`
  (were absent initially; install succeeded after `apt-get update`).
- pdftoppm / tesseract: not needed — both documents have a healthy text layer
  (all pages > 1100 chars), no OCR fallback required.

### Documents supplied (2)
1. `inputs/results_balamines_q1fy27.pdf` (7 pp) — doctype **results**.
   Reg 33 Board Outcome cover (p1) + standalone & consolidated unaudited financial
   results, segment info, notes (p2-5) + Independent Auditor's Limited Review Reports:
   standalone (p6), consolidated (p7). Units: Rs Lakhs (x0.01 -> Crores).
2. `inputs/pressrelease_balamines_q1fy27.pdf` (5 pp) — doctype **presentation**.
   Press Release / Investor Release: cover (p1) + Key Financial Highlights table,
   segment volumes, project updates, MD quote, About, Safe Harbor (p2-5).
   Units: Rs Crore.
   DOCTYPE NOTE: labelled `presentation` (not the `pressrelease` variant seen in the
   atlantaelec-q1fy27 run) because this is an investor communication feeding both
   Role 4 and Role 5; enumerated via the INVESTOR PRESENTATION path (every number,
   every forward statement, every footnote/disclaimer). Functionally equivalent.

No concall transcript and no investor slide deck were supplied. Role 5 (concall)
input is therefore limited to the press-release management commentary; this is a
coverage limitation flagged for A4/A5.

### Notion / company memory
- No `companies/BALAMINES.md` exists (first coverage for this ticker).
- No prior quarterly run folder for BALAMINES.
- No live Notion thesis page located for this new-coverage name; A3/A4 run with
  "no prior Decision Status / no active tripwires" passed inline. No position
  framing is asserted. Notion save is treated as a flag, not an auto-create.

### Sequence and gates
- A1 EXTRACTOR (both docs): GATE A1 page-coverage = 100% / 100% -> PASS.
- A2 ENUMERATOR: in progress.
- A3 FORENSICS: pending.
- A4 ANALYST (merged): pending.
- A5 ADVERSARY: pending.
