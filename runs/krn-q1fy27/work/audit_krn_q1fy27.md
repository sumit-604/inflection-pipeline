# A5 ADVERSARY / COMPLETENESS AUDIT — KRN Heat Exchanger (KRN) — Q1 FY27

Doctype: results (Q1 FY27 unaudited). Role 5 (concall/presentation) legitimately N.A.; confirmed
no concall content fabricated (review Role 5 N.A. at L31-34, L3; no utilisation/customer number is
presented as concall-sourced — all such items carried as UNKNOWN/monitorable).

Fresh context. I re-derived every number from the A1 extract (Lakhs x0.01 = Rs Cr) and re-ran the
enumeration independently against the A2 ledger. I did not defer to A4's or A3's cites.

This file records TWO passes: the loop-0 audit (which failed on one orphan) and the loop-1 re-check
after A3/A4 addressed it.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

| Brief part | Location | Present? |
|---|---|---|
| (1) Summary narrative | 5A | present (~26 lines, numbers-first, symmetric) |
| (2) SECTOR intelligence | 5B | present |
| (3) BUSINESS-MODEL intelligence | 5C | present |
| (4) COMPETITION intelligence | 5D | present |

Gate 0: PASS (both passes).

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledger)

| Category | A2 count | My fresh count | Status |
|---|---|---|---|
| Numbered notes | 18 | 18 (9 consol + 9 SA) | match |
| Board agenda items | 3 | 3 | match |
| P&L line items | 63 | 63 (35 consol + 28 SA) | match |
| Zero-standing rows | 51 | 51 | match |
| Segment rows | 36 | 36 (18 + 18) | match |
| Export-country rows | 22 | 22 (14 + 8) | match |
| Auditor paragraphs | 16 | 16 (10 + 6) | match |
| Consolidated entities | 2 | 2 | match |
| Annexure-II sub-rows | 8 | 8 | match |
| Signature blocks | 5 | 5 | match |

Enumeration reconciles exactly (no A2 loop-back). Standalone AND consolidated both present; zero-value
lines preserved; auditor Other-Matters verbatim (F4); Board agenda items 2/3 assessed (F13); every
forward/ambiguous finding became a management question.

**Loop-0 result: one orphan.** A2's fourth FIGURE_MISMATCH — standalone segment-note pre-exceptional
FY26 9,191.08 Lakh (L564) vs standalone P&L pre-exceptional FY26 9,111.66 Lakh (L434), Rs 0.79 Cr —
was flagged by A2 for A3/A4 reconciliation but never dispositioned; A4 had falsely claimed "x4 all
resolved / three inconsistencies." Verdict at loop 0: INCOMPLETE, loop_back_to A3.

---

## AUDIT 2 — ARITHMETIC (independent recompute from raw Lakhs)

Every derived cell in Steps 1B/1D/1.5/2/4, both entities, all four columns, recomputed from the
extract — no mismatch above rounding. A4's three claimed keying-error typos each CONFIRMED real:
line-139 consol PAT (3,269.56 typo vs true 3,289.56 -> 32.90); Q1 FY26 consol total tax (printed
566.82 vs components/PAT-reconciled 586.82 -> 5.87); FY26 consol income-tax short/excess sign (must
be −3.03 credit to foot PBT 97.96 − 21.49 = PAT 76.47). No arithmetic error in A4. (Full recompute
table retained from loop-0 pass; unchanged and still valid — none of the loop-1 edits touched a
derived metric.)

---

## AUDIT 3 — ADVERSARIAL READ

Three most positive claims (revenue +118.9%; Op-EBITDA margin +417 bps; subsidiary +14.23 Cr =
43.2% of group). Each has a surviving bear counter from the same extract (intra-group + unaudited
revenue quality; standalone margin −374 bps; unaudited/uncash-confirmed subsidiary PAT with Rs 143.18
Cr QIP cash idle). All three counters are ALREADY grafted into A4 (F1/F4/F6, Steps 1.5/2/4, Q1-Q5).
No new surviving counter to add. INDETERMINATE cash correctly capped at PROCEED WITH FLAGS (not
PROCEED); Notion prior-period figures all provenance-tagged, never asserted as this-quarter fact.

---

## LOOP-1 RE-CHECK (gate re-run after A3/A4 fix)

Re-read the A4 review fresh; independently re-derived F14-4 from the A1 extract. My inputs remain the
three canonical artifacts (A4 review, A1 extract, A2 ledger).

### F14-4 arithmetic — independently CONFIRMED
- Standalone segment "Profit Before Exceptional Items & Tax" FY26 = **9,191.08 Lakh** (extract L564).
- Standalone P&L "Profit Before Prior Period and Exceptional Item" FY26 = **9,111.66 Lakh** (L434).
- Gap = 9,191.08 − 9,111.66 = **79.42 Lakh = Rs 0.79 Cr**; and 79.42 = **2 x 39.71** (the exceptional
  item) — confirming the segment-note double-count root cause.
- Both reconcile to the same PBT: segment 9,191.08 − 39.71 = 9,151.37 (L566); P&L 9,111.66 + 39.71 =
  9,151.37 (L436). **L566 = L436 = 9,151.37**, confirmed. CONFIRMATORY-NEGATIVE, immaterial in rupees,
  changes no PBT/PAT anchor.

### Fix verification in A4 review
- Preamble (L20-27): now enumerates all four FIGURE_MISMATCH instances (i)-(iv), (iv) fully described.
- 1A note (L141-145): "three tax/PAT-line inconsistencies, together with the fourth F14 instance ...
  make **four** F14 drafting-control instances."
- Q13 (L549): "**Four** internal arithmetic inconsistencies," cites L564 vs L434.
- Plain-language brief 5A (L615): "**four** separate arithmetic inconsistencies."
- YAML question row (L724) and flags (L743): both now read "four F14 instances."

### No new orphan / no new error introduced
- Every residual "three" in the review is legitimate and unrelated: three Board notes (L78), three
  open Notion governance items (L530), Daikin evaded three times (L677), and the correct framing
  "these three tax/PAT-line inconsistencies together with the fourth" (L141). No lingering count
  contradiction.
- The edits are textual additions of numbers I independently verified (9,191.08 / 9,111.66 / 79.42 /
  39.71 / 9,151.37). No derived metric, verdict, Decision Status, or cash-conversion field changed:
  protocol verdict stays PROCEED WITH FLAGS, Decision Status HELD, cash conversion INDETERMINATE.
- Coverage now complete: all four A2 FIGURE_MISMATCH instances dispositioned; no orphan row remains;
  no row my fresh pass found is missing from the ledger.

The sole loop-0 blocker is resolved. No new blocker.

---

## VERDICT

**COMPLETE.** All four deliverable-brief parts present; enumeration reconciles exactly with the A2
ledger with zero orphans; all arithmetic (both entities, all columns, the three keying typos, and now
the fourth segment-note double-count F14-4) independently confirmed; adversarial read symmetric with
no ungrafted surviving counter; INDETERMINATE cash correctly capped; Notion provenance clean. Proceeds
to Notion save.

```yaml
stage: A5-adversary
company: "KRN"
quarter: "Q1 FY27"
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
