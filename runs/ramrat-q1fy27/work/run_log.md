# Ram Ratna Wires (RAMRAT) — Q1 FY27 Quarterly Review — Run Log

Ticker: RAMRAT (BSE 522281 / NSE RAMRAT) | Quarter: Q1 FY27 (ended 30-Jun-2026)
Filed: 31-Jul-2026 | Run date: 2026-07-31

## Document classification (evidence-based, per orchestrator Step 0d)
- inputs/RAMRAT_Q1FY27_Results_Reg33.pdf (12pp) -> doctype=results
  Marker: Reg 30 & 33, Board Outcome, Un-audited Standalone+Consolidated results + Limited Review Report.
- inputs/RAMRAT_Q1FY27_Presentation.pdf (31pp) -> doctype=presentation
  Marker: Reg 30 Investor Presentation, slide structure.
- inputs/RAMRAT_Q1FY27_PressRelease.pdf (3pp) -> doctype=pressrelease (presentation-class enumeration)
  Marker: Reg 30 Investor/Press Release, prose + one summary table + MD commentary + safe harbor.
  No concall transcript supplied in this set.

## Toolchain
- pdftotext/pdfinfo/pdftoppm/tesseract installed via apt (poppler-utils 24.02, tesseract 5.3.4).

## Protocol files verified present
- frameworks/Quarterly_Results_Review_Protocol_v1_2.md
- frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md
- frameworks/Master_Project_Prompt_v3.3.md

## Live Notion memory (fetched 2026-07-31, page 3adbb2b9-d3ab-8134-a6cf-c70458fde4fe)
- Decision Status: WATCHLIST / AVOID (deeply overvalued; on-valuation AVOID)
- CMP at last workup Rs 454.40 | Entry range Rs 134-153 | MoS Rs 114
- Gate verdict: PROCEED WITH CAVEATS (INDETERMINATE cash cap)
- Earnings basis FORWARD; prob-weighted 3yr CAGR -15.2%; Hurdle STOP
- Last run: runs/ramrat-2026-07-29 (first workup, NO-CONCALL MODE)

### Active flags (from prior workup)
- FLAG-CASH INDETERMINATE: FY26 CFO -96 Cr SA / -93 Cr CN vs record PAT 108 Cr; receivables +64%, inventory +108% vs ~40% revenue; zero write-downs.
- FLAG-PROMOTER CONCERN (professional CFO from 1-Apr-2026; promoter guarantees released 8-May-2026; 0% pledge; board 50% independent).
- FLAG-GATE0 AVERAGE (core 40/80).
- FLAG-GOVERNANCE (Ankit Kedia attendance 33%/40%; Kabra board concentration; R R Kabel 6.05% cross-holding + shared independent director).
- Section 132 IT search + Section 148 reassessment (merged Global Copper): contingent tax ~Rs 67-104 Cr; auditor Emphasis of Matter; unmodified opinion.

### MONITORING CHECKLIST / THESIS-BROKEN TRIGGERS (pass to A3 + A4)
1. FY27 CFO negative a second consecutive year (SA and CN) with WC days not normalising toward FY25 -> thesis broken.
2. Copper tubes segment revenue falls 2+ consecutive quarters below Rs 347.20 Cr (Q4 FY26) -> Bhiwadi ramp stalled.
3. Off-BS-financing gate: a positive FY27 CFO manufactured by expanding the Rs 647 Cr supplier-finance / Rs 187 Cr factoring lines does NOT count as a real reversal.
4. Contingent tax crystallises materially; CTC/HVDC commercial start near Q2 CY2026; Silvassa Rs 86 Cr capex commissioned.

### Press-release headline (management framing, to verify against filing)
Consolidated Q1FY27: Revenue 1,853.3 Cr (+88.6% YoY), EBITDA 89.6 Cr (+109%), PAT 35.2 Cr (+120.8%); EBITDA margin 4.8%; copper tubes now 26% of revenue (was ~22%).

## GATE A1 results
- results:      PASS (12pp, 100%, units=Lakhs x0.01, 623 lines)
- pressrelease: PASS (3pp, 100%, units=Crores x1, 133 lines)
- presentation: PASS (31pp, 100%, units=Crores x1, 919 lines, OCR pages 4,8,19,22,26)
No prior-quarter ledger exists (prior run ramrat-2026-07-29 was the annual/first workup, NO quarterly ledger). PRIOR_LEDGER_PATH = none for all docs.

## GATE outcomes (final)
- A1 x3: PASS (results 12pp / presentation 31pp / pressrelease 3pp; 100% coverage each)
- A2 x3: PASS (results 19 notes/121 items; presentation 31 slides/530 nums; pressrelease 50 units)
- A3 x3: PASS (all F1-F17 marked, 100% ledger reconciliation each)
- A4: PROCEED WITH FLAGS; cash INDETERMINATE; Decision Status verified WATCHLIST/AVOID
- A5: loop 1 INCOMPLETE (Slide-27 dividend orphan) -> A3 added FND-12 -> A4 incorporated -> A5 re-audit COMPLETE
- A5 noted 2 cosmetic non-verdict slips for tidy-up (CN Q1FY26 ETR base 28.88 vs 28.91 rounding; FND-07 net-debt components sum 661.3 vs stated ~660.5; ratio ~1.1x either way). Non-blocking.

## Thesis-broken triggers this quarter: NONE FIRED
- T1 (2nd-consec negative CFO): UNOBSERVABLE (no Q1 BS/CFO)
- T2 (copper tubes <347.20 x2): NOT fired (Q1 489.98 Cr)
- T3 (off-BS-financed CFO): UNOBSERVABLE
- T4 (contingent tax crystallises): NOT fired (silent/pending)
Decision Status UNCHANGED: WATCHLIST / AVOID.

## Notion save: DONE (page 3adbb2b9-d3ab-8134-a6cf-c70458fde4fe)
- Full review appended (verdict, YoY/QoQ/S-vs-C/segment/cash/monitoring/triggers/growth/QFM x16/monitorables/flags/A3-summary/A5-verdict/combined verdict).
- Key Notes audit trail prepended (2026-07-31 entry; prior 2026-07-29 entry preserved).
- Decision Status property unchanged (no pre-committed trigger fired).

## Run complete.
