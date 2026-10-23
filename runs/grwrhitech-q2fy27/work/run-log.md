# Run log: GRWRHITECH Q2 FY27 (/run-quarterly, 2026-10-23)

- Checkout guard: git fetch origin main OK; diff over .claude/ prompts/ frameworks/ CLAUDE.md LESSONS.md empty.
- Protocols present: Quarterly_Results_Review_Protocol_v1_4.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Document_Review_Protocol_v1_1.md.
- Toolchain: pdftotext, pdfinfo, pdffonts, pdftoppm on PATH; tesseract at C:\Program Files\Tesseract-OCR (not on PATH, not needed: text layer present).
- Fetch: BSE scrip 500655 announcements API, 1-23 Oct 2026. Files saved to C:\ConcallPipeline\Daily Concall Intelligence\Q2 FY27 Results\23 Garware Hi-Tech\. The BSE "Board Meeting Outcome" and "Unaudited Financial Results" attachments are byte-identical (43 pages).
- Class detection: results filing p1 "Outcome of the Board Meeting held on Thursday, October 22, 2026" with Reg 33 statements -> results. Presentation PDF p1 cover letter dated October 22, 2026, slides follow -> presentation.
- Presentation not run separately: pdftotext of results pp20-43 and presentation pp2-25 match word for word (20,145 bytes each, zero token diff). Its slides are inside the results extract.
- Concall: intimation (19-Oct-2026) sets the call on 23-Oct-2026 at 11:30 IST. At run start (07:25 IST) the call had not been held; no transcript or recording existed. Role 5 not run.
- Notion: COMPANIES MASTER page fetched read-only 2026-10-23 and saved to work/notion_context_grwrhitech_2026-10-23.md. companies/GRWRHITECH.md does not exist.
- Machine restart mid-run (A4 running). A4 output and block were complete on disk; not re-run.
- A1 gate pass (43/43 pages). A2 gate pass (all count tests, orphan_ids []). A3 gate pass (F1-F17 all statused).
- A5 iteration 0: INCOMPLETE (C1, M1, M2, M3, F1, F2 -> A4). Loop 1 run.
- A5 iteration 1: INCOMPLETE (F3 FACTUAL, A4 wording on transfer-price lean). Loop cap reached; stopped for the operator. Notion save not run; payload in notion-payload.md.
- Files in work/ not committed: raw.txt, body.txt, manual.py, tmp/, ocr_results/ (A1 scratch).
- 2026-10-24: Operator approval for correction loop 2, relayed by the coordinating session (local_75d06544): operator wrote "complete them fully" (2026-10-24). Loop 2 runs on A5 iteration 1 item F3 (A4). No third loop.
- Loop 2: A4 fixed F3 (diff vs b2cf309d: 9 lines in review, YAML only). First A5 loop-2 run stalled (watchdog, no output); mechanical re-run.
- A5 iteration 2: INCOMPLETE. F3 resolved; loop-0 fixes hold. Open: F4 FACTUAL (finance cost called lease-interest only; H1 5.34 on 15.66-12.61 leases does not fit, nature not disclosed; RV l.199, l.273, l.286), F5 FACTUAL (Q2 reported EBITDA 188.99 vs filed sum 189.00; RV l.130, l.223), M4 MISSING (receivable sale/discounting reading for F4 and 9.83 receivable days: add to cash-classification evidence list RV l.337 and a Q17). No third loop (cap). Carried into the concall-merge A4 as known open items.
