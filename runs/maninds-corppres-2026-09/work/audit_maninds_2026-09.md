# A5 ADVERSARY / COMPLETENESS AUDIT — MANINDS (Man Industries (India) Ltd)
## Reg 30 Corporate Presentation, filed 2026-09-01 | Quarter tag 2026-09
## RE-AUDIT after loop-1 fixes (prior verdict INCOMPLETE, two gaps)

Independent re-derivation. Inputs seen: A4 review, A1 extract, A2 ledger, plus
the A3 forensics passed explicitly for fix-verification. Every figure below is
recomputed from the A1 raw INR-Mn lines (x0.1 = Rs Cr), not deferred to A4/A3.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

Plain-language brief (Section F of A4 review): all four labelled parts present
and carry real content.
- F1 Summary narrative (review L581-614): PRESENT, ~30 lines of prose.
- F2 Sector intelligence (review L616-635): PRESENT, 5 bullets.
- F3 Business-model intelligence (review L637-662): PRESENT, 7 bullets.
- F4 Competition intelligence (review L664-689): PRESENT, 5 bullets + provenance.

Gate: PASS. No missing or placeholder part.

---

## 1. TARGETED FIX VERIFICATION

### FIX 1 — ARITHMETIC: FY25 "Net debt / (net cash) ex-leases" (was FAIL)

Prior gap: FY25 cell read (77.7) net cash; correct is net DEBT Rs50.8 Cr.

Re-derivation from raw balance sheet (slide 30, INR Mn x0.1):
- FY25 Cash & Bank 3,792 = 379.2 Cr (L1150); Current Investments 260 = 26.0 Cr
  (L1148); Total Borrowings = LT 1,385 + ST 3,175 = 4,560 = 456.0 Cr (L1138+L1148).
- 379.2 + 26.0 - 456.0 = -50.8 -> net DEBT Rs50.8 Cr. CONFIRMED.

Corrected file state:
- Row (review L261): `(174.4) | 50.8 | (228.3)`, verdict cell reads
  "net cash FY24 & FY26; net DEBT Rs50.8 Cr FY25". FY25 is un-parenthesised
  (net debt convention), FY24 (174.4) and FY26 (228.3) UNCHANGED. Correct.
- Formula narrative (L265-271): FY25 = 379.2 + 26.0 - 456.0 = -50.8 net DEBT;
  FY24 = +174.4 net cash; FY26 = +228.3 net cash. Reproduces exactly.
- Mandatory-question bullet (L288-289): now reads "FY25 was net debt Rs50.8 Cr".
  No lingering "net cash on face" for FY25.
- Grep sweep of the whole review for "77.7": ZERO hits. The stale value is gone.
- Every "net cash" string remaining in the review (L266-295, L484, L534, L609,
  L667, L752) refers to FY24/FY26, to the general "net cash vs net debt" question
  on the Rs579.7cr line, or to a peer, not to an FY25 net-cash claim. Consistent.

FIX 1 status: RESOLVED. Cross-check of the two anchor cells: FY24 254.9 + 228.0
- 308.5 = +174.4 (matches); FY26 657.2 + 70.8 - 499.7 = +228.3 (matches).

### FIX 2 — ORPHAN: slide-15 API Monogram certificate RECONCILE_CHECK (was minor FAIL)

Prior gap: ledger L640-663 (API Monogram certificate #2, two-cert RECONCILE_CHECK,
ledger row at ledger-file L321) not marked reviewed-no-finding.

Verified: A3 forensics L116 now carries the explicit disposition —
"the two-certificate RECONCILE_CHECK at ledger L640-663: REVIEWED - NO FINDING.
Immaterial: a certification/licence detail with no financial or forensic
implication." The row is a forensic RECONCILE_CHECK, so A3 is its correct owner;
it is now dispositioned. No orphan remains.

FIX 2 status: RESOLVED.

---

## 2. COVERAGE AUDIT (light re-run)

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides (grep "^===== PAGE") | 37 | 37 | none | PASS |
| Ledger rows (37 inv + 379 disc + 23 fwd) | 439 | 439 | none | PASS |
| Notes (presentation) | 0 | 0 | n/a | PASS |
| Turns (no transcript) | 0 | 0 | n/a | PASS |
| Slide-15 API cert #2 RECONCILE_CHECK (L640-663) | 1 | 1 | none (A3 L116 reviewed-no-finding) | PASS |

All 16 A3 findings (FN1-FN16) incorporated in A4 (review L36-37, YAML L712).
No orphan row and no row-my-fresh-pass-found-that-the-ledger-lacks. Coverage
holds from the loop-1 pass; the one previously-open RECONCILE_CHECK is closed.

---

## 3. ARITHMETIC AUDIT (corrected row + 4 spot checks)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Net debt FY25 (corrected row) | net DEBT 50.8 | 379.2+26.0-456.0 = -50.8 | L1150/L1148/L1138 | MATCH |
| Net cash FY24 | (174.4) | 254.9+228.0-308.5 = +174.4 | L1150/L1148/L1138 | MATCH |
| Net cash FY26 | (228.3) | 657.2+70.8-499.7 = +228.3 | L1150/L1148/L1138 | MATCH |
| CO FY26 Op EBITDA margin ex-OI | 12.32% | (467.9-28.6)/3,563.9 = 12.33% | L1100/L1094/L1092 | MATCH (rounding) |
| CO FY26 effective tax rate | 28.1% | 66.5/237.0 = 28.06% | L1110/L1108 | MATCH |
| SA FY26 PAT YoY | +42.8% | (195.8-137.0)/137.0 = +42.9% | L1074 | MATCH (deck-stated 42.8%) |
| Q1FY27 PAT YoY | +122.5% | (61.4-27.6)/27.6 = +122.5% | L1226-1233 | MATCH |

No mismatch above rounding. The fix did not perturb any adjacent cell; FY24 and
FY26 net-position values are unchanged and reproduce independently.

---

## 4. ADVERSARIAL READ (unchanged from loop-1; spot re-confirmed)

The three most positive A4 claims and their strongest same-text bear counters
were all already grafted into the A4 review at loop-1 and survive:
- Standalone +42.8% PAT strength -> countered by consolidated +11.3% and the
  subsidiary flip +16.2 to -25.3cr (review Step 4B, FN1). Incorporated.
- 13.0% EBITDA margin clears the floor -> countered by 12.32% ex-OI, below 13%
  (review 1C, FN5, Tripwire 6). Incorporated.
- 18.4% ROCE quality -> rejected; ~13.9% on a clean basis (review 6A, FN3).
  Incorporated.
No new surviving bear counter surfaced by this re-audit.

---

## 5. NEW-ISSUE CHECK

No new inconsistency introduced by the two edits. FY24/FY26 net-position cells,
the balance-sheet source lines, the Rs579.7cr other-financial-liabilities flag
(which still governs the net-cash-vs-net-debt question), and all downstream
tripwire/question cross-references remain internally consistent with the
corrected FY25 net-debt reading. Nothing else material changed.

---

## VERDICT: COMPLETE

Both loop-1 gaps resolved: FY25 net-debt cell now reads net DEBT Rs50.8 Cr with
consistent wording and no lingering FY25 net-cash claim; FY24 (174.4) and FY26
(228.3) unchanged; the slide-15 API-certificate RECONCILE_CHECK is marked
reviewed-no-finding (A3 L116). Coverage and arithmetic spot checks reproduce.
No new issue. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "MANINDS"
quarter: "2026-09"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
