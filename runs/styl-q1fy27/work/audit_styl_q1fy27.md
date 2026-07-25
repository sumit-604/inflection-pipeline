# A5 ADVERSARY / COMPLETENESS AUDIT — STYL Q1FY27

Company: Seshaasai Technologies Ltd (STYL) | Quarter: Q1FY27
Auditor: A5 ADVERSARY | Model: claude-opus-4-8
Under audit: `review_styl_q1fy27.md` (A4). Re-derived independently from A1
extracts + A2 ledgers only (no forensics files, no orchestrator commentary).
Unit: filing INR Mn, x0.1 = Rs Cr; concall already Rs Cr. On OCR pages
(7/8/11/12) both the primary and [OCR CROSS-CHECK] readings were used.

**This file now contains FOUR passes.**
- **PASS 4 (BINDING)** — re-audit of the Role-4+Role-5 merged review AFTER A4
  applied the two Pass-3 fixes (ARI-3, ADV-3). Verdict below is operative.
- PASS 3 — audit of the Role 5 (concall) upgrade; verdict INCOMPLETE (history).
- PASS 2 — re-audit of the Role-4-only base after ARI-1/BEAR-1/COV-1 (history).
- PASS 1 — initial Role-4-only audit (history).

The closing YAML at the very bottom reflects PASS 4 and supersedes all earlier
pass YAMLs.

---
---

# PASS 4 — RE-AUDIT (after A4 applied ARI-3, ADV-3)  [BINDING]

Scope: confirm the two Pass-3 fixes landed correctly at §5.2 and everywhere they
were threaded; confirm the load-bearing numbers, verdict, cap, scorecard tally,
gate score and Decision Status did not move; confirm the edits introduced no new
arithmetic or coverage error.

## Fix-by-fix confirmation

**ARI-3 — CONFIRMED (correct and fully threaded).**
- §5.2 (review L376-388) now states the bottom-up blend as
  **`Payments 0.42 × (10-12%) + CFS 0.40 × 0% + IoT 0.18 × 45% = +12.3% to
  +13.1%`**, i.e. **ABOVE** the 8-12% headline, and frames the honest implication
  (headline conservative OR a segment guide optimistic) as internal tension that
  **STRENGTHENS** the soft-guidance / deceleration read. My independent recompute:
  low 4.2 + 0 + 8.1 = **12.3**; high 5.04 + 0 + 8.1 = **13.14 → 13.1**. Correct.
  The erroneous "+5% to +10% / implies ~8-12%" wording is gone.
- **A3-01 remaining-9M math UNCHANGED and re-verified:** FY26 1,441 → +8-12% →
  1,556-1,614; less Q1 377 → 1,179-1,237; vs FY26 9M 1,130 → **+4.3% to +9.5%**
  (review L400-404). My recompute: 1,556.43−376.47 = 1,179.96 → +4.40%;
  1,614.08−376.47 = 1,237.61 → +9.50%. Unchanged, still A5-confirmed.
- Threaded consistently: §5.3 (L412-419), §5.8 archetype (L558-559), §5.10 A3-01
  row (L603), §6 gate paragraph (L692-694) and §6 gate reason (L853-854), §7B Q18
  (L739), §8 monitorable (L772), §9 flag reason 7 (L823-826), and YAML
  (a5_fixes_applied ARI-3 L903; lead_finding L906; decision_gate_score count L929;
  flags L981; monitorables L961; QfM Q18 L935). All say "~+12-13%, above the
  headline." No stray "+5-10%" remains.

**ADV-3 — CONFIRMED (false conflict retired everywhere).**
- §5.9 (review L582-591) is reversed: **"There is NO material narrative-vs-source
  conflict on the call"**; the 56%-vs-73% gap is explicitly a **FALSE conflict the
  deck resolves** — 56% = COMPANY-WIDE top-10, 73% = PAYMENT-SOLUTIONS SEGMENT
  top-10. The §5.9 table row (L579) now reads CONFIRMED (different bases — NOT a
  conflict).
- §5.7A (L519) "company-wide … NOT in conflict … different bases; A3-06,
  resolved"; §5.10 A3-06 (L608) "AMBIGUOUS → RESOLVED … Different bases — NOT a
  conflict"; §7B Q23 (L744) re-scoped to a company-wide-confirm + new-logo-
  pipeline monitorable question (no longer a reconciliation ask); §8 monitorable
  (L781) "NOT a discrepancy vs the deck's 73% Payment-segment figure"; §9 reason 1
  (L810-813) "FALSE conflict the deck resolves (ADV-3)."
- **Flag removed:** the old YAML flag "Top-10 concentration 56% (concall) vs deck
  ~73% — basis reconciliation needed (A3-06)" is deleted from the flags list
  (review L978-992 now carries 14 flags, exactly one fewer; no other flag lost).
  Prose "one material narrative-vs-source conflict" line is gone.
- **Citations verified against the extracts:** company-wide 56% at deck slide 22
  (presentation L683), slide 16 client-concentration (L489), press release
  (results L131), concall (L26); Payment-Solutions-segment 73% at deck slide 12
  (presentation L325); CFS-segment 77.16% at deck slide 13 (L362). All correct;
  the scope distinction is exactly as the source documents present it.

## No-regression confirmation

| Item | Expected | In revised review | Status |
|---|---|---|---|
| Protocol verdict | PROCEED WITH FLAGS | L800; YAML L895 | UNCHANGED |
| Cash-conversion cap | INDETERMINATE, subsumed by FLAGS | L832-842; YAML L896 | UNCHANGED |
| 15-trigger tally | 2 FF / 1 BM / 2 PARTIAL / 2 BREACH / 1 CN / 2 ADVERSE / 5 SILENT | L646-653; YAML L914-923 | UNCHANGED |
| Decision-gate score | ~1.5-2 of 4 (mover = soft revenue guide) | L688-694; YAML L924-929 | UNCHANGED |
| Decision Status | HELD 4% at Rs 287 (Notion ts 2026-06-16) | L843/L858; YAML L897 | UNCHANGED |
| Position branch | 8A | L858; YAML L898 | UNCHANGED |
| Re-engagement / hard-kill | NOT met / NOT mechanically met | L655-673 | UNCHANGED |
| A3-01 deceleration math | +4.3% to +9.5% 9M YoY | L400-404 | UNCHANGED |
| Headline scorecard / PAT bridge / ETR / C-S gap (§1-3) | as Pass-1/2-verified | §1-3 | UNCHANGED |

## No new error introduced by the edits

- Arithmetic: the only newly-inserted figure (segment blend +12.3% to +13.1%)
  is correct; it does not touch any headline, bridge, ETR, margin or S-vs-C
  number, all of which remain A5-confirmed from Passes 1-3. The direction of the
  ARI-3 correction is thesis-favourable (a ~12-13% bottom-up vs an 8-12% headline
  reinforces "guide is soft/conservative"), so no conclusion flips.
- Coverage: no ledger row was added, dropped or re-mapped; the QfM set (22 in 7B +
  2 answered-on-concall) is intact with Q23 re-scoped, not removed; the flags list
  lost exactly the one spurious conflict flag. The concall/results/presentation
  enumerations still reproduce the A2 ledgers exactly (no orphan, no gap).

## PASS-4 GATE VERDICT

**COMPLETE.** Both bounded Role-5 fixes landed correctly, accurately and
completely across every threaded location (§5.2/5.3/5.7/5.8/5.9/5.10/6/7B/8/9 and
the YAML): ARI-3 restates the segment blend as ~+12-13% (above the 8-12%
headline, strengthening the soft-guidance read) with the A3-01 +4-10% 9M math
untouched; ADV-3 retires the false 56%-vs-73% conflict as a company-wide-vs-
segment basis difference and removes the spurious flag. The PROCEED WITH FLAGS
verdict, the INDETERMINATE cash-conversion cap, the 15-trigger tally, the
~1.5-2-of-4 decision-gate score and the HELD Decision Status are all intact, and
no new arithmetic or coverage error was introduced. Coverage reproduces the A2
enumeration exactly; every derived metric re-foots. The merged Role 4 + Role 5
review is fit to proceed to Notion save.

---
---

# PASS 3 — AUDIT OF THE ROLE 5 (CONCALL) UPGRADE  (verdict INCOMPLETE) [HISTORY]

I re-ran the concall enumeration with a fresh pass, recomputed the deceleration
math from raw numbers, and stress-tested the concall-derived claims line by line.

## AXIS 1 — COVERAGE (fresh concall enumeration vs A2 ledger vs A4 citation)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Concall — speaker turns | 58 | 58 | none | PASS |
| Concall — questions (incl follow-ups) | 19 | 19 (Q1..Q8 = 2+3+3+3+2+1+2+3) | none | PASS |
| Concall — analyst firms | 7 | 7 (DRJ=Dia Jen resolved) | none | PASS |
| Concall — mgmt numbers | 59 | 59 | none | PASS |
| Concall — participants | 13 | 13 (Gautam Jain silent) | none | PASS |
| Concall — forward/hedge phrases | 18 | 18 | none | PASS |
| Results / Presentation (carried) | as Pass 1 | matches | none | PASS |

No orphan row (MGMT_ABSENCE→A3-09, REPEAT_QUESTION→A3-02, analyst-sourced
insurance count→A3-07 all dispositioned); no fresh-pass row the ledgers lack.

## AXIS 2 — ARITHMETIC

- All Section 1/2c/3 figures re-foot from OCR-cross-check raw numbers (revenue
  +21.1%/-6.9%, EBITDA 94.41/25.08%, operating EBITDA 87.31/23.19%, gross profit
  156.83/189.65/138.40, ETR 26.29%, PAT bridge +23.50, C-S gap ~Rs 1.3 Cr, COMC
  58.34%/54.23%/+411 bps, cash/IPO figures). CONFIRMED.
- **Deceleration math (task-mandated):** 8-12% off Rs 1,441 Cr net of Rs 377 Cr
  Q1 ⇒ remaining-9M **+4.4% to +9.5%** YoY (A4 +4.3-9.5%, within rounding) vs
  +21.1% Q1. A3-01 foots. CONFIRMED.
- **ARI-3 (defect):** §5.2 segment blend "+5% to +10% weighted / ~8-12%" does not
  foot; `0.42×(10-12) + 0.40×0 + 0.18×45 = +12.3% to +13.1%` (above the band).
  Above rounding → loop A4. LOW (conclusion reinforced, not flipped).

## AXIS 3 — ADVERSARIAL

- The three most-positive claims (Revenue +21.1% FF; IoT +145% FF; net cash
  Rs 369 Cr) each already carry their bear counter in A4 (A3-01; A3-03; COV-1 +
  A3-13). No NEW surviving bear counter to graft.
- **ADV-3 (defect):** A4 called the "56% vs 73% top-10 concentration" gap "the one
  material narrative-vs-source conflict" (flag + Q23). FALSE conflict — 56% is
  company-wide (deck slide 22 L683 / slide 16 L489 / PR L131 / concall L26), 73%
  is the Payment-Solutions segment top-10 (deck slide 12 L325; cf CFS 77.16%,
  slide 13 L362). A2 captured both; A4 conflated scopes → loop A4 (origin A3-06).
  LOW-MODERATE.

## PASS-3 GATE VERDICT

INCOMPLETE — loop to A4 for ARI-3 (correct the segment blend to ~+12-13%) and
ADV-3 (retire the false 56%-vs-73% conflict; re-scope Q23; drop the flag).
Everything else (deceleration math, trigger scorecard, INDETERMINATE cap,
PROCEED WITH FLAGS, HELD status) independently confirmed. (Superseded by Pass 4 =
COMPLETE after fixes applied.)

---
---

# PASS 2 — RE-AUDIT (after A4 applied ARI-1, BEAR-1, COV-1) — Role-4-only base [HISTORY]

**ARI-1 — CONFIRMED.** Gross profit Q4FY26 corrected 190.66 → 189.65 (Rev 404.18 −
net materials 214.52; deck 1,897 Mn = 189.7 Cr, pres L445); GM 46.9% unchanged.
**BEAR-1 — CONFIRMED.** Q1FY27 PAT margin 16.0% < FY26 16.7% grafted to §3 + QfM
row 17 (deck L529-532; derived FY26 16.65%). **COV-1 — CONFIRMED.** Net cash
~Rs 369 Cr disclosed (deck L950-951) marked NOT ND while cash CONVERSION stays
INDETERMINATE (no BS/CF). No-regression: PROCEED WITH FLAGS / INDETERMINATE cap /
HELD 8A intact. Pass-2 verdict: COMPLETE for the Role-4-only base (superseded by
the concall-upgrade audit).

---
---

# PASS 1 — INITIAL AUDIT (Role-4-only base, verdict INCOMPLETE) [HISTORY]

Coverage reproduced the A2 results+presentation enumeration exactly (12 notes / 60
line items / 10 auditor paras / 5 agenda / 2 entities / 3 zero-standing / 5
signatures / 20 Note-2 sub-rows; 32 slides / S6 12 / L1-11 / IPO table); no
Balance Sheet or Cash Flow in the filing (confirmed absence). Arithmetic
CONFIRMED except one digit slip. Three fixes issued: **ARI-1** (Q4FY26 gross
profit 190.66 → 189.65), **BEAR-1** (surviving bear counter: PAT margin 16.0% <
FY26 16.7%, deck L529-532), **COV-1** (net cash ~Rs 369 Cr disclosed at deck
L950-951, A4 had said "all ND"). Verdict INCOMPLETE, loop A4 (superseded by
Pass 2 = COMPLETE for the base).

---

```yaml
stage: A5-adversary
company: "STYL"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE                 # COMPLETE | INCOMPLETE
coverage:
  orphan_rows: []                 # concall/results/presentation enumeration reproduced exactly; no orphan
  missing_from_ledger: []         # fresh pass found nothing the A2 ledgers lack
arithmetic_mismatches: []         # ARI-3 corrected by A4 (segment blend now +12.3-13.1%, above the 8-12% headline, A5-verified); A3-01 +4-10% 9M math unchanged
surviving_bear_counters: []       # 3 most-positive claims' counters already incorporated (A3-01/A3-03/COV-1+A3-13)
loop_back_to: ""
gap: ""
notes: "Pass 4 re-audit after A4 applied ARI-3 + ADV-3. ARI-3: segment-guide bottom-up blend restated 0.42x(10-12%)+0.40x0%+0.18x45% = +12.3% to +13.1% (ABOVE the 8-12% headline), threaded through 5.2/5.3/5.10/6/7B-Q18/8/9 + YAML; A3-01 remaining-9M +4.3-9.5% YoY math unchanged and re-verified. ADV-3: false '56% vs 73% top-10' conflict retired everywhere (5.7A/5.9/5.10 A3-06/7B-Q23/8/9); 56% = company-wide (deck slide 22 L683 / slide 16 L489 / PR L131 / concall L26), 73% = Payment-Solutions segment (deck slide 12 L325; cf CFS 77.16% slide 13 L362); spurious flag removed from the YAML flags list (14 remain). No regression: PROCEED WITH FLAGS, INDETERMINATE cash cap, 15-trigger tally, ~1.5-2-of-4 gate score, HELD 8A all intact; no new arithmetic or coverage error. Fit to proceed to Notion save."
```
