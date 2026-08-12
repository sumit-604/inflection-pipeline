# A5 ADVERSARY / COMPLETENESS AUDIT — re-audit loop 2
# Max India Limited (MAXIND) | Q1 FY27 (quarter ended 30 June 2026)
# Model: claude-opus-4-8 | Doctype scope: CONCALL ONLY
# Inputs seen: A4 review, A1 extract, A2 ledger. A3 reasoning NOT seen (re-derived).
# All line refs are the A1 extract left-column content lines (5-141).

This is the SECOND pass. Loop 1 returned INCOMPLETE with one gap: A4 had
omitted a supported surviving bear counter on the CAPITAL pillar (the second-raise
deferral was bridged by drawing credit lines / new debt, l.109, plus one-time
Antara Noida gross collections, l.113, not operating cash — which sharpens
FLAG-CASH INDETERMINATE and undercuts the "better performance" framing). This
pass is a FULL re-audit (all four audits re-run independently), not only a spot
check of the patch.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run FIRST)

| Brief part | Location in review | Present / empty |
|---|---|---|
| (1) Summary narrative (10-20 lines) | lines 538-544 (three substantive paragraphs) | **PRESENT** — non-placeholder |
| (2) SECTOR intelligence | lines 546-548 | **PRESENT** — pricing move, regulation, labour codes, China logistics, unit-economics tenor |
| (3) BUSINESS-MODEL intelligence | lines 550-552 | **PRESENT** — three-engine holdco, capital-light vs capital-sink, finance-lease quality, cash-at-subs, funding-quality drift |
| (4) COMPETITION intelligence | lines 554-556 | **PRESENT** — IP/services moat, DLF named entrant, repeat-question signal |

All four labelled parts present and carry real content. **Gate 0 PASS.**

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

Fresh grep/sweep on the extract (lines 5-141; even lines are blank spacers):

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Speaker turns | 69 | 69 | odd lines 5-141 step 2 = (141-5)/2+1 = 69; header lines 1-3 excluded | none | **PASS** |
| Turn role-split | 9/41/19 | 9/41/19 = 69 | Operator (5,9,23,59,81,105,123,137,141)=9; Analyst 19; Mgmt 41 | none | **PASS** |
| Participants | 15 | 15 | 9 mgmt (incl. Ishan roster-gap l.53) + 5 analysts + 1 operator | none | **PASS** |
| Questions | 21 | 21 | turn-by-turn sweep of analyst turns; bundled sub-questions in turns 11/25/61 split correctly | none | **PASS** |
| Mgmt numbers | 79 | 79 (reconciled) | Table 4 rows spot-verified against source turns 7/13/35/65/69/75/85/95-97/101/109-117/127 | none | **PASS** |
| Fwd-commit/hedge | 24 | 24 | Table 5 lexical sweep confirmed | none | **PASS** |
| Zero-standing/nil | 1 | 1 | NOA SPV Q1 revenue = nil (l.25) | none | **PASS** |

**Ledger-row citation check (every row cited in A4 OR reviewed-no-finding):**
A4 preamble (l.11-22) asserts 69/69 turns, 21/21 questions, 79/79 numbers,
24/24 hedge phrases, 1/1 nil disclosure reviewed at line, and incorporates all
thirteen A3 findings (A3-01..A3-13). Substantive numeric rows flow into Step 1
(34-claim inventory), Step 4A (21-Q table), and the T-C segment walk. The two
purely qualitative Table-4 rows (row 47 HT award; row 48 NABH accreditation)
are immaterial and covered under the blanket "79/79 reviewed" as reviewed-no-finding
— same treatment that passed loop 1; no thesis bearing. **No orphan row. No row
in my fresh pass is missing from the ledger.**

COVERAGE: **PASS** (loop-1 coverage held; the loop-2 patch added no new
enumeration and dropped none).

---

## AUDIT 2 — ARITHMETIC (recompute every derived metric from raw numbers)

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Consol rev YoY growth | +66% | 68.6/41.3 - 1 = +66.1% | l.7 | **MATCH** |
| Consol rev QoQ | "marginally declined" | direction only (no prior-Q number spoken) | l.7 | **MATCH** (qualitative) |
| EBITDA loss YoY | widened 23.2 -> 25 | +Rs1.8cr wider loss | l.7 | **MATCH** |
| EBITDA loss QoQ | widened 6.8 -> 25 | +Rs18.2cr wider loss | l.7 | **MATCH** |
| Loss ratio 95% -> 63% | management figure, full-year | quoted, not A4-derived | l.101 | **MATCH** (mgmt-spoken, flagged as annual not Q1) |
| Opening % quantified | ~88% (30/34) | 30/34 = 88.2% | Step 1 | **MATCH** |
| Specificity ratio | ~0.53 (10/19) | 10/19 = 0.526 | Step 6B | **MATCH** |
| Hedge count | 7 ( >5 ) | l.13,l.101,l.47(x2),l.7 let's-see,l.131,l.7 hopefully = 7 | Step 6C | **MATCH** |
| Response-quality tally | A6 B11 C3 D0 E1 = 21 | recount of Q1-Q21 = 6/11/3/0/1 = 21 | Step 4A | **MATCH** |
| Q&A share of turns | 66 of 69 (~96%) | 66/69 = 95.7% | Table 2 | **MATCH** |
| US$20m in INR | ~Rs170cr | 20m x ~Rs85/USD = ~Rs170cr | Exchange 3, l.117/113 | **MATCH** (labelled approx; FX reasonable) |
| Peak capital fall | ~US$25m -> ~US$20m | verbatim | l.113 | **MATCH** |
| NOA demand / collected | Rs169cr / ~75% | verbatim | l.7 | **MATCH** |
| Standalone vs consol treasury | Rs21cr / Rs372cr | verbatim | l.7 | **MATCH** |
| Rs40cr pref tranche (July) | Rs40cr | verbatim | l.111,113 | **MATCH** |

No PAT bridge / filed YoY-QoQ walk / cash-flow reconciliation exists this run
(Role 4 N.A., no filing) — A4 correctly marks those cells UNVERIFIABLE / ND
rather than inventing figures. **No mismatch above rounding. The loop-2 patch
introduced no new derived metric (all patch content is direct quotation) and no
new unsupported figure.**

ARITHMETIC: **PASS.**

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims + strongest bear counter)

**Claim 1 — "Revenue FIRING / +66% YoY; guidance to double AGEasy and grow consol substantially."**
Bear counter (same text): consol revenue declined QoQ (l.7); senior-living income
includes ~Rs15cr one-time finance-lease re-lease that management EXCLUDES from
gross revenue and calls "exceptional" (l.35); NOA books NIL revenue in Q1 (l.25);
AGEasy sits at ~Rs19cr net Q1 run-rate against a Rs150cr full-year doubling (l.49).
Status: **ALREADY INCORPORATED** (Step 1 contradictions, A3-05 run-rate gap, A3-07
quality flag, Step 8A "ON TRACK, QoQ + AGEasy gap temper it"). Does not survive as
a new graft.

**Claim 2 — "Losses coming down (95% -> 63%); path to profitability."**
Bear counter (same text): the Q1 print is a LARGER loss, not a smaller one —
EBITDA loss widened YoY (23.2 -> 25) and sharply QoQ (6.8 -> 25); the 95% -> 63%
is a full-year ratio, and the Q1 deterioration is framed away as "exceptional DMP"
timing (l.7). Status: **ALREADY INCORPORATED** (Step 7A CONTRADICTED-internal,
A3-06, brief narrative). Does not survive as a new graft.

**Claim 3 — "Second raise deferred due to better performance; liquidity improved, peak need fell US$25m -> US$20m."**
Bear counter (same text): the deferral was bridged by (a) DRAWING CREDIT LINES —
new debt to manage working-capital inventory (l.109), and (b) ONE-TIME Antara
Noida possession GROSS COLLECTIONS (~Rs169cr demand, ~75% collected, l.7) that
"opened up" and were "utilized" (l.113) — neither is structural operating cash.
Set against a Rs21cr standalone holdco treasury (l.7, RED) and a REFUSED FY27/28
burn number (l.101), "better performance" dresses up leverage + a non-recurring
inflow as improved funding health. Symmetric bull read: NOA cash is real (residents
paid ~75% of Rs169cr), the Rs40cr pref tranche was in fact received in July
(l.111,113), and peak requirement genuinely fell to ~US$20m (l.113) — so absolute
liquidity did improve; the flag is about the QUALITY/durability of the improvement.

Status: **THIS IS THE LOOP-1 SURVIVING COUNTER. VERIFIED NOW GRAFTED** into:
- Step 4C Exchange 3 (l.219-221) — line-supported with symmetric bull read;
- Step 5A new-disclosures table (l.236) — dedicated capital-quality row;
- Step 8A Cash pillar (l.313) — "WEAKENED... bridge is debt + non-recurring inflow";
- Step 8D Cash-conversion pillar + FLAG-CASH note (l.348, l.352) — "reaffirmed AND SHARPENED", symmetric bull retained;
- Verdict block (l.393), T-A / Treasury headline tables (l.429, l.513), QM-7 (l.528),
  brief narrative (l.542) and business-model brief (l.552), and the YAML flags (l.602).

**No NEW surviving bear counter found this pass.** The three most-positive claims
each already carry their strongest same-text counter. The one that survived in
loop 1 is now present, correctly line-anchored, and symmetric.

---

## TASK-SPECIFIC VERIFICATION CHECKLIST

1. Grafted counter present and line-supported (l.109 credit lines / l.113 NOA
   one-time collections + peak US$25m->US$20m / l.7 Rs21cr treasury + Rs169cr/75% /
   l.101 refused burn) with symmetric bull read — **CONFIRMED** in Step 4C, 5A, 8D
   (and echoed in 8A, verdict, headline tables, brief, YAML).
2. Fix introduced no arithmetic error and no new unsupported figure — **CONFIRMED**
   (all patch content is direct quotation; Audit 2 clean).
3. Counts still reconcile 69 turns / 21 questions — **CONFIRMED** (Audit 1).
4. Every A3 FORWARD-SIGNAL / AMBIGUOUS finding maps to a management question —
   **CONFIRMED**: QM table (l.520-532) carries A3-01, A3-03, A3-04, A3-05, A3-06,
   A3-07, A3-08, A3-09, A3-10, A3-12, A3-13. The two non-forward/non-ambiguous
   findings (A3-02 treasury confirmatory-negative; A3-11 revenue-series contradiction,
   resolved to l.13) correctly do not require a QM row.
5. Plain-language brief present with sector / business-model / competition
   intelligence — **CONFIRMED** (Audit 0).
6. Decision Status still WATCHLIST (no trigger fired; Step 8C l.332-341) and verdict
   still PROCEED WITH FLAGS (l.396; YAML l.573) — **CONFIRMED**.

---

## VERDICT

**COMPLETE.** The loop-1 gap is closed: the surviving capital-pillar bear counter
is grafted into every required section, is line-supported (l.109 / l.113 / l.7 /
l.101), and retains a symmetric bull read. The full re-audit finds no orphan
ledger row, no arithmetic mismatch above rounding, no new unsupported figure
introduced by the patch, intact 69-turn / 21-question reconciliation, complete
A3 forward/ambiguous-to-question mapping, an intact four-part plain-language brief,
and unchanged Decision Status (WATCHLIST) / verdict (PROCEED WITH FLAGS). No new
surviving bear counter. Proceed to Notion save.

```yaml
stage: A5-adversary
company: "MAXIND"
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
surviving_bear_counters: []   # loop-1 counter now grafted; no new survivor this pass
loop_back_to: ""
gap: ""
```
