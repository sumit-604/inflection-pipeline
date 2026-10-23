# Run log: SUPREMEPWR H1 FY27 (/run-quarterly, 2026-10-23)

## Setup
- Checkout guard: git fetch origin main OK; framework diff empty. Branch claude/quarterly-supremepower-q2fy27-7e9233 at 041ffb92.
- Prior work: branch claude/quarterly-supremepower-q2fy27-fd3ab0 holds no commits beyond main (earlier session failed). Phase 1 run on branch run/supremepwr-2026-10-06 (not on main); companies/SUPREMEPWR.md read from that branch.
- Protocols present: Quarterly_Results_Review_Protocol_v1_4.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Document_Review_Protocol_v1_1.md, Master_Project_Prompt_v3_6.md.
- Toolchain: pdftotext, pdfinfo, pdffonts, pdftoppm on PATH; tesseract at C:\Program Files\Tesseract-OCR\ (not on PATH; passed to A1 by full path).
- Notion: search "Supreme Power Equipment" and "SUPREMEPWR" return no company page. Review framed as PRE-THESIS READ; Spear line and load-bearing facts passed from companies/SUPREMEPWR.md (run/supremepwr-2026-10-06).

## Documents (NSE SME, symbol SUPREMEPWR; NSE corporate-announcements API, index=sme)
| File | NSE attachment | Filed | Class decision |
|---|---|---|---|
| SupremePower_H1FY27_Results.pdf (15 pp) | SPEL_16102026164128_SPEL.pdf (same MD5 ca5111b8 as SPEL_16102026164605_SPEL.pdf; filed twice) | 16-Oct-2026 16:43 | results: Reg 33 outcome letter, LRR, "Un-Audited Financial Results ... Half Year ended 30th September, 2026" |
| SupremePower_H1FY27_Presentation.pdf (41 pp) | SPEL_21102026180524_InvestorPresentationH1FY27.pdf | 21-Oct-2026 18:05 | presentation: cover letter dated 21.10.2026, then slide structure |
| SupremePower_H1FY27_PressRelease.pdf (4 pp) | SPEL_21102026205440_SPELH1FY27PressRelease.pdf | 21-Oct-2026 20:54 | press release (presentation-class rules, doctype label pressrelease) |
| SupremePower_H1FY27_Concall_Transcript_ASR.txt | recording link filed SPEL_22102026133026 (22-Oct-2026); MP3 at supremepower.in/IPO_pdf/H1 FY27 Concall Audio Recording.mp3 | call held 22-Oct-2026 10:30 IST | concall (machine-transcribed; no transcript filed as of 23-Oct-2026) |

- Results date note: the board approved results on 16-Oct-2026, not 21-Oct. The deck and press release followed on 21-Oct.
- ASR: faster-whisper "small", int8, CPU, 10 chunks of 300 s, language en, beam 1, no VAD. Audio 2,960 s.

## Correction loops
- Loop 1: A5 INCOMPLETE (F1, F2, C1, C2, M1-M6). Fixes: A1 concall append R324-R326; A2 concall ledger; A3 presentation addendum FP-20, FP-21; A4 revision. A5 re-audit: all ten CLEARED; one new MISSING (M7, concall l.206-207 forward statement without a row).
- Loop 2 approval: operator batch approval dated 2026-10-24, relayed by the starting session (local_75d06544) in three messages; operator words quoted there: "complete them fully". Loop 2 runs once, then stops.
- Loop 2: A1 append R327-R344; A2 ledger 344/344; A4 revision (M7 cleared; archetype back to provisional EVASIVE). A5 final re-audit: INCOMPLETE on one FACTUAL item, F3 (ex-restated specificity ratio is 28/60 = 0.467 inside the 0.45-0.55 band, so 'both more than 0.05 below 0.5' at review l.832, l.914, l.948, l.1126 is wrong; label fragile). Text-only fix. No loop remains: F3 is an OPEN ITEM for the operator. Verdict PROCEED WITH FLAGS unaffected.
- Notion: not written (operator instruction). Payload saved at notion-payload.md.
