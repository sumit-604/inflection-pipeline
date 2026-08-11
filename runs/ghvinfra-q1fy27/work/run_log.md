# RUN LOG — GHVINFRA Q1 FY27 Quarterly Review

- **Ticker:** GHVINFRA (BSE 505504, formerly Sindu Valley Technologies Ltd)
- **Run date:** 2026-08-11
- **Pipeline:** /run-quarterly (5-agent extraction-first review)
- **Orchestrator:** quarterly-00-orchestrator.md v1.0

## SETUP / PRECHECKS
- Toolchain: pdftotext, pdfinfo, pdftoppm, tesseract — MISSING at start, installed via apt (poppler-utils, tesseract-ocr). Now all present. PASS.
- Protocol files present: Quarterly_Results_Review_Protocol_v1_2.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Master_Project_Prompt_v3.3.md. PASS.

## DOCUMENTS SUPPLIED
1. `inputs/ghvinfra_media_release_q1fy27.pdf` (3 pages)
   - **Document class: Reg 30 MEDIA RELEASE** carrying Q1FY27 (quarter ended 30-Jun-2026) headline unaudited standalone results.
   - CAVEAT (material): This is NOT the Reg 33 "Statement of Unaudited Financial Results." It contains a single P&L headline table + narrative + board/award news. It has NO balance sheet, NO cash flow, NO notes, NO segment/order-book breakdown, NO consolidated figures, NO limited-review report. Doctype dispatched as `results` so the F1-F17 forensic checklist runs in full and concretely enumerates every omitted disclosure as N.A.-with-reason.
   - No concall or presentation supplied.

## COMPANY MEMORY / NOTION (fetched live 2026-08-11)
- Notion page: GHV Infra Projects Limited (id 387bb2b9-d3ab-81de-8c50-d96623d49e02)
- **Decision Status: AVOID** (permanent universe-exclusion record; NOT in active universe).
- Promoter Verdict: AVOID (hard gate). EM 27/100 MOAT STRENGTHENING. Gate 0 65/160 AVERAGE.
- AVOID drivers: (1) operating history <3yr; (2) cumulative CFO/PAT −3.36x, FY25 CFO −₹55.63 Cr; (3) Block B cash 3/20; active CBI bribery case naming promoter; 3 CFO + 3 CS changes in 13 months; auditor flagged audit-trail preservation failure; 100% FY25 receivables from parent GHV (India) Pvt Ltd; reverse-merger + BCA royalty/mgmt-fee extraction.
- 22-Jun-26: ₹213 Cr RPT work order from parent GHV (India) Pvt Ltd (confirming, not corrective).
- **Re-entry conditions (all three, simultaneously):** (a) >40% of order book from non-related parties for 4 consecutive quarters; (b) CBI matter closed/dismissed/exonerated; (c) 2 consecutive years positive cumulative CFO. None visible.
- Monitoring frame passed inline to A3/A4: test whether anything this quarter fires a re-entry trigger or deepens an AVOID driver (RPT concentration, cash conversion, governance stability).

## GATES
- GATE A1 (page coverage 100%): PASS — 3/3 pages, no OCR needed, 182-line extract.
- GATE A2 (count reconciliation): PASS — 59 positive-count rows reconcile grep vs sweep; 15 absence flags; flags NAME_CHANGE, DATE_DISCREPANCY, TABLE_OMISSION, INCOMPLETE_COMPARATIVE.
- GATE A3 (F1-F17 all statused, findings line-cited): PASS — 5 FINDING, 2 PASS, 10 N.A.; findings A3-01..A3-05.
- GATE A5 (verdict COMPLETE): PASS — 59/59 rows reproduced, 22 metrics recompute within rounding, brief complete, no surviving bear counters.

## OUTCOME
- Protocol verdict (v1.2): INSUFFICIENT EVIDENCE (media release only, not Reg 33 statement).
- Cash conversion: INDETERMINATE. Position branch: 8A-W.
- Decision Status: AVOID UNCHANGED. None of the 3 re-entry triggers fired or advanced.
- Notion saved (2026-08-11): full Q1FY27 review + forensics table + 6 management questions + monitorables + plain-language brief + A5 verdict appended to GHV Infra page; Key Notes audit trail prepended with dated entry; Decision Status untouched (no trigger fired).

## WORK FILES
- work/extract_results_ghvinfra_q1fy27.txt (A1)
- work/ledger_results_ghvinfra_q1fy27.md (A2)
- work/forensics_ghvinfra_q1fy27.md (A3)
- work/review_ghvinfra_q1fy27.md (A4 merged review)
- work/audit_ghvinfra_q1fy27.md (A5)
