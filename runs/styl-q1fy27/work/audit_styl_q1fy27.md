# A5 ADVERSARY / COMPLETENESS AUDIT — STYL Q1FY27

Company: Seshaasai Technologies Ltd (STYL) | Quarter: Q1FY27
Auditor: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-24
Under audit: `review_styl_q1fy27.md` (A4). Re-derived independently from A1
extracts + A2 ledgers only. Unit: filing INR Mn, x0.1 = Rs Cr. On OCR pages
(7/8/11/12) both the primary and [OCR CROSS-CHECK] readings were used.

**This file contains TWO passes: Pass 1 (initial audit, verdict INCOMPLETE with
three bounded A4 fixes) and Pass 2 (re-audit after A4 applied the fixes, verdict
COMPLETE). The binding verdict is Pass 2 / the closing YAML.**

---
---

# PASS 2 — RE-AUDIT (after A4 applied ARI-1, BEAR-1, COV-1)

Scope: confirm each of the three bounded fixes landed correctly and accurately;
confirm nothing else in the review changed; confirm no new arithmetic or
coverage error was introduced by the edits.

## Fix-by-fix confirmation

**ARI-1 — CONFIRMED.** Section 2c (review L141) now reads Gross profit
`138.40 | 189.65 | 156.83 | ND`; the 190.66 slip is gone. Footnote L153-156
shows the working (Rev 404.18 − net materials 214.53 = 189.65 Cr) and the
independent deck cross-cite (slide 15 = 1,897 Mn = 189.7 Cr, presentation
extract L445), and states Q4FY26 gross margin 46.9% is unchanged. My independent
recompute: 404.176 − 214.524 = **189.652 → 189.65 Cr**; 189.65 / 404.18 =
46.92% → 46.9%. Both correct. (The intermediate net-materials shown as 214.53
vs the precise 214.52 is a 0.01 display-rounding of the subtrahend; it does not
change the stated 189.65 result — immaterial.)

**BEAR-1 — CONFIRMED.** Section 3 (review L192-198) now states "Q1FY27 PAT margin
of 16.0% is BELOW the FY26 full-year 16.7%" that management itself cites
(presentation extract L529-532), and ties it to the derived FY26 PAT margin
16.65% in Section 2c. A new Questions-for-Management **row 17** (L333) asks
whether FY27 PAT margin will exceed 16.7%. The question count is reconciled to
"all 17" (L343) and the closing YAML carries 17 QfM entries. The counter is also
surfaced in the Flag list (L382-383, L478). Text support verified: 16.03% <
16.65% (FY26 derived) and < 16.7% (management benchmark, L532).

**COV-1 — CONFIRMED.** Section 3 (review L204-219) is corrected: net cash is
"NOT ND" — the deck discloses cash & cash equivalents ~Rs 3,690 Mn (~Rs 369 Cr)
at 30-Jun-2026 incl ~Rs 1,700 Mn unutilised IPO (presentation extract L950-951;
A2 presentation ledger Table 4 narrative) — while the **cash-CONVERSION quality
remains explicitly INDETERMINATE** (no CFO / CFO-PAT / receivable / inventory /
payable days without the Cash Flow Statement). The verdict block (L390-401),
monitorables (L356), and QfM row 11 (L327) are updated consistently. Load-bearing
conclusion (cash conversion INDETERMINATE) preserved.

## No-regression confirmation

| Item | Expected | In revised review | Status |
|---|---|---|---|
| Protocol verdict | PROCEED WITH FLAGS | L370, YAML L433 | UNCHANGED |
| Cash-conversion cap | INDETERMINATE, subsumed by FLAGS | L396-398, YAML L434 | UNCHANGED |
| Decision Status | HELD 4% at Rs 287 (Notion ts 2026-06-16) | L402/408, YAML L435 | UNCHANGED |
| Position branch | 8A | L408, YAML L436 | UNCHANGED |
| Headline scorecard (§1) | as Pass-1-verified | L61-76 | UNCHANGED |
| PAT bridge (§3 table) | +23.50 (23.46 rounding) | L164-176 | UNCHANGED |
| FTTCP triggers + tally (§5) | 2 FF / 2 BREACH / 2 PARTIAL / 8 SILENT / 1 NA | L256-276 | UNCHANGED |
| A3 findings table (§4) | 20 findings | L227-246 | UNCHANGED |

## No new error introduced by the edits

- Arithmetic: every recomputed figure from Pass 1 still reconciles; the only
  changed cell (Gross profit Q4FY26) is now correct (189.65). The Notion-base
  delta added in COV-1 (369 − 339 = 30 Cr uplift) is internally consistent.
- Two minor, non-gating notes on the COV-1 additions (recorded for A4 awareness,
  not blocking): (i) the deck figure is labelled "cash & cash equivalents"
  (gross); residual finance cost of Rs 1.84 Cr/qtr (L407-408) implies some
  borrowings remain, so "net cash ~Rs 369 Cr" is marginally generous — but A4
  explicitly flags the figure unaudited and to-be-verified at the Q2 Balance
  Sheet, and the load-bearing cash-CONVERSION reading is correctly INDETERMINATE;
  (ii) the Rs 339 Cr Notion FY26 net-cash base is external-memory-sourced (not in
  the A1 extracts), consistently attributed, and affects no conclusion. Neither
  is an arithmetic or coverage error requiring a further loop.

## Pass-2 GATE VERDICT

**COMPLETE.** All three bounded fixes (ARI-1, BEAR-1, COV-1) landed correctly and
accurately. Coverage reproduces the A2 enumeration exactly (no orphan row, no
ledger gap); arithmetic is fully sound (the one prior mismatch is corrected); the
surviving bear counter is grafted into Section 3 and QfM row 17. The
PROCEED WITH FLAGS verdict, the INDETERMINATE cash-conversion cap, and the HELD
Decision Status are intact and no new error was introduced. The review is fit to
proceed to Notion save.

---
---

# PASS 1 — INITIAL AUDIT (verdict INCOMPLETE — retained for the record)

## AXIS 1 — COVERAGE AUDIT (fresh enumeration vs A2 ledger vs A4 citation)

Independent grep/sweep pass, diffed against both A2 ledgers.

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Results — numbered notes | 12 (6C+6S) | 12 | notes-section sweep L571/577/611/616/620/625 + L967/973/1005/1010/1015/1020 | none | PASS |
| Results — statement line items | 60 (32C+28S) | 60 | full sweep L385-500 / L813-905; NCI rows OCR-variant "Controlhng" confirmed | none | PASS |
| Results — auditor paragraphs | 10 (6C+4S) | 10 | C paras 1-6 (L270-349), S paras 1-4 (L718-774) | none | PASS |
| Results — board-agenda items | 5 | 5 | covering letter L52-63; no AGM/dividend/director/auditor/ESOP item | none | PASS |
| Results — consolidation entities | 2 | 2 | Rite Infotech (L304), Atoll Solutions (L305) | none | PASS |
| Results — zero-standing rows | 3 | 3 | C-OCI equity (L453), S-Exceptional (L847), S-OCI equity (L875) | none | PASS |
| Results — signature blocks | 5 | 5 | CS (L68), MD x2 (L629/1024), Auditor x2 (L351/777) | none | PASS |
| Results — Note-2 IPO sub-rows | 20 | 20 | 5 objects x 2 tables x 2 columns | none | PASS |
| Presentation — slides | 32 | 32 | `^\[page N\]` markers | none | PASS |
| Presentation — slide-6 claims | 12 | 12 | L153-188 | none | PASS |
| Presentation — slides 17/18 P&L | 20 | 20 | L503-533 / L543-574 | none | PASS |
| Presentation — slide-31 IPO objects | 4 (+Total) | 4+1 | L930-948 | see COV-1 | PASS w/ note |

Structural confirmations: No Balance Sheet / no Cash Flow in the results filing
(my grep for `Balance Sheet|Cash Flow|Assets|Liabilities` returns 1 hit = the
press-release phrase "strengthen cash flows" L187, not a statement header).
Standalone carries 4 fewer rows than Consolidated (2 NCI + duplicate "7."),
expected. Every A2 flag traced to an A4 disposition (no orphan forensic).

**COV-1 (initial):** A4 stated net debt/net cash "all ND," but slide 31 (L950-951,
in A2 ledger Table 4) discloses cash ~Rs 3,690 Mn. Required A4 correction. LOW.

Coverage verdict: complete; one incorporation correction (COV-1).

## AXIS 2 — ARITHMETIC AUDIT

All headline, extraction, derived, PAT-bridge, ETR, margin, and standalone-vs-
consolidated figures recomputed from OCR-cross-check readings and CONFIRMED,
with a single exception:

**ARI-1 (initial):** Gross profit Q4FY26 = 190.66 (A4) vs 189.65 (recomputed;
404.18 − 214.52; deck 1,897 Mn = 189.7 Cr, L445). +1.01 Cr digit slip,
non-load-bearing (GM% 46.9% correct), but above rounding → A4 correction.

## AXIS 3 — ADVERSARIAL READ

- Positive claim 1 (Revenue +21.1% FIRED FAVOURABLY): bear counter (subdued
  Q1FY26 base / flat-to-declining 3yr) already carried by A4 (X1/F16a/Q14) — does
  not survive as new.
- Positive claim 2 (EBITDA +28% / margin +135 bps): bear counter (other-income-
  driven, operating +22 bps) already fully made by A4 — does not survive.
- Positive claim 3 (PAT +63.8% / margin 16.0%): bear counter — 16.0% is BELOW
  FY26 full-year 16.7% (management's own benchmark, deck L529-532) — NOT stated
  by A4. **SURVIVES (BEAR-1)**, must be grafted.

## PASS-1 DISCREPANCY LIST

| ID | A4 claim | Recomputation / finding | Line cite | Loop | Materiality |
|---|---|---|---|---|---|
| ARI-1 | Gross profit Q4FY26 = 190.66 | 189.65 (404.18 − 214.52); deck 1,897 Mn = 189.7 | res 387/397-402/411; deck L445 | A4 | LOW |
| BEAR-1 | PAT margin flattered, sequential-vs-annual not stated | 16.0% < FY26 16.7% (mgmt benchmark) — surviving counter | deck L529-532 | A4 | LOW-MOD |
| COV-1 | "net cash … all ND" | Deck discloses cash ~Rs 369 Cr incl ~Rs 170 Cr unutilised IPO | deck L950-951 | A4 | LOW |

## PASS-1 GATE VERDICT

INCOMPLETE — loop to A4 for the three bounded fixes above. Coverage otherwise
complete; arithmetic otherwise sound; PROCEED WITH FLAGS / INDETERMINATE cap /
HELD status all supported. (Superseded by Pass 2 = COMPLETE after fixes applied.)

---

```yaml
stage: A5-adversary
company: "STYL"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []        # ARI-1 corrected by A4 (Q4FY26 gross profit now 189.65 Cr, verified)
surviving_bear_counters: []      # BEAR-1 grafted by A4 into Section 3 + QfM row 17, verified
loop_back_to: ""
gap: ""
```
