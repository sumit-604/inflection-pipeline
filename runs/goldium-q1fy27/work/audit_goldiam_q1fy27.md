# A5 ADVERSARY / COMPLETENESS AUDIT — GOLDIAM Q1 FY27

Auditor: A5 (Opus 4.8) | Date: 2026-08-11
Under audit: `runs/goldium-q1fy27/work/review_goldiam_q1fy27.md` (A4 merged review)
Re-derived independently from: A1 extract (`extract_concall_goldiam_q1fy27.txt`, 201 lines) and A2 ledger (`ledger_concall_goldiam_q1fy27.md`). A3 reasoning NOT in scope — I re-derive; I do not defer to A4/A3 cites.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The A4 review carries a PLAIN-LANGUAGE BRIEF (review L408-430) with all four labelled parts present and non-empty:

| Part | Heading present | Real content | Status |
|---|---|---|---|
| (1) Summary narrative | "## 1. SUMMARY NARRATIVE" (L410) | ~20-line dense paragraph: revenue Rs 363.7 Cr, one-off Rs 22 Cr refund, withheld margins, ORIGEM erosion, verdict PROCEED WITH FLAGS | PRESENT |
| (2) Sector intelligence | "## 2. SECTOR INTELLIGENCE" (L413) | Demand/pricing/supply/tariffs, each anchored (T44/L91, T29/L61, T31/L65, T12/L27) | PRESENT |
| (3) Business-model intelligence | "## 3. BUSINESS-MODEL INTELLIGENCE" (L420) | Revenue mix, unit economics, margin-quality flag, model drift, each anchored | PRESENT |
| (4) Competition intelligence | "## 4. COMPETITION INTELLIGENCE" (L426) | Moat claims, sub-2% wallet share weakness, second-hand peer benchmark, price-break risk | PRESENT |

**Gate 0 = PASS.** All four parts present with substantive, anchored content (no placeholders).

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger)

Fresh grep + manual sweep over the A1 extract (content on odd lines 5-201 = 99 turns; header lines 1-3 excluded):

| Category | A2 count | My fresh count | Method / cross-check | Orphan rows | Status |
|---|---|---|---|---|---|
| Turns | 99 | 99 | (201-5)/2 + 1 = 99 blank-line-delimited paragraphs | none | MATCH |
| Participants (Q&A rounds) | 10 rounds / 7 unique | 10 / 7 | grep "question is (on\|from) the line of" = 10 hand-offs (L11 opening truncated in view + 9 shown); Doshi/Ganani/Saurabh each 2 rounds | none | MATCH |
| Questions | 32 (29 subst + 3 proc) | 32 (29 + 3) | Procedural = L13, L49, L147 (audio checks). Substantive rows in ledger table = 30 numbered, but Q24 (L137, deferred) and Q30 (L185, fulfils Q24) are ONE unique question -> 29 unique. Matches A2 count-test and A4's Step 4A (29 rows: #1-23, #25-30). | none | MATCH |
| Mgmt numbers | 27 | 27 | Re-walked every figure at L9 (12), L27 (2), L31, L71 (2), L83, L91, L99 (3), L115, L121, L159, L173, L189 = 27. Turn-92 "25-30/85 lakh" correctly held out as NUMBER_AMBIGUOUS. | none | MATCH |
| Forward/hedge phrases | 19 | 19 | Re-walked A2's 19 rows against T8,10,12,14,21,26,34,40,56,57,61,65,66,74,92; all present | none | MATCH |

**Orphan-row test (every ledger row cited in A4 OR marked reviewed-no-finding):**
- All 27 mgmt numbers surface in A4 (Step 1 opening inventory 14 rows + Steps 2/4/5/7/10/11 cover the remaining 13). No orphan.
- All 29 substantive questions appear in A4 Step 4A (29 rows). Q24 legitimately folded into Q30. No orphan.
- All 19 forward/hedge phrases are consumed collectively in Step 2 (guidance) and Step 6B (specificity ratio uses the 19 denominator). No orphan.
- All 99 turns accounted for via the Q&A decomposition + opening-remarks inventory. No orphan.

**Missing-from-ledger test (rows my fresh pass found that the ledger lacks):** none material. Within-answer illustrative figures (ORIGEM ASP ">Rs 70,000" L135; European retailer "150-200 / 400-800 store" ranges L135; "sold 200-250 times" L45) are qualitative context, not headline disclosures; they are captured at the turn level and A4 does use the ">Rs 70k" ASP (Step 4A row 23). A2's 27-count of substantive metrics is defensible and reconciled twice. Not a FAIL.

**Traceability observation (not a gate failure):** A4 lists **A3-F10-01** as "incorporated" (preamble L17, YAML L444) but it carries **no explicit F10 citation anywhere in the review body**, unlike every other listed finding (F06-01, F07-01/02/03/04, F12-01, F17-01/02 all appear inline). The A3 artifact is out of my scope, so I cannot confirm the substance is absent; on a concall the F10-active subject matter (tariff-refund cash receipt / other-income composition) IS substantively covered (Step 5A, Step 7A, Section 11, T19/L41). I therefore record this as an A4 tagging/traceability nit, not a coverage failure — the ledger (my defined diff scope) reconciles cleanly.

**Coverage verdict = PASS.** No orphan rows; no missing rows.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extracted numbers)

Raw inputs: Revenue Rs 3,637 mn = 363.7 Cr; EBITDA Rs 1,039 mn = 103.9 Cr (grew 120%); PAT Rs 740 mn = 74.0 Cr; tariff refund ~Rs 22 Cr (L27); prior-yr base Rs 235 Cr (L121); order book Rs 2,250 mn = 225 Cr vs Rs 140 Cr prior-June (analyst L17); cash+investments Rs 4,566.7 mn = 456.67 Cr; bonus 3,76,39,281 sh × Rs 2.

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Reported OI-inclusive EBITDA margin | 28.6% | 103.9 / 363.7 = 28.57% | L9 | MATCH |
| Margin ex Rs 22 Cr refund | 22.5% | (103.9-22)/363.7 = 81.9/363.7 = 22.52% | L9, L27 | MATCH |
| PAT ex refund | ~Rs 52 Cr | 74.0 - 22 = 52.0 (A4's stated "SEZ low-tax" assumption; full refund untaxed) | L9, L27 | MATCH (assumption flagged) |
| Revenue YoY | +54.8% / "~55%" | (363.7-235)/235 = 128.7/235 = 54.77% | L9, L121 | MATCH |
| Order book YoY | +60.7% | (225-140)/140 = 85/140 = 60.71% | L9, L17 | MATCH |
| Promise-vs-delivery score | 1.5/4 = 37.5% | 1.0+0+0.5+0 = 1.5; 1.5/4 = 37.5% | Step 3A | MATCH |
| Specificity ratio | 4/19 = 0.21 | 4/19 = 0.2105 | Step 6B | MATCH |
| Bonus rupee outlay | ~Rs 7.53 Cr | 3,76,39,281 × 2 = 7,52,78,562 = Rs 7.53 Cr (reconciles the garbled "7 cr 527 562") | L9 | MATCH |
| Best-store annualised | ~Rs 5-5.4 Cr | 40-45 L/mo × 12 = 4.8-5.4 Cr | L189 | MATCH (A4 "~5-5.4"; 40×12=4.8 within "~", immaterial) |
| Std-vs-consol PAT gap | ND | Standalone never disclosed on call; Rs 22 Cr refund (US sub) + Rs 5-6 Cr ORIGEM loss are consolidated-only -> gap genuinely un-quantifiable pre-filing | Sec 11 | MATCH (correctly ND) |

**No mismatch above rounding.** Arithmetic verdict = PASS.

Ancillary check on A4's central margin flag: A4 is correct that neither 28.6% nor 22.5% equals the management-quoted "steady-state 24%," so the 24% does not reconcile to disclosed EBITDA/revenue on any stated base — a genuine, correctly-surfaced arithmetic gap (Step 7A, Q7). The three revenue-growth framings (chairman 40% L19; chairman 50% L121; implied 54.8%) are also correctly flagged as mutually inconsistent.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive A4 claims, bear counter from the same text)

A4 is already strongly bear-leaning and PROCEED WITH FLAGS; it has pre-incorporated the obvious counters. I tested whether any counter SURVIVES un-incorporated and overturns a classification.

**Positive claim 1 — Revenue GREEN, up ~55% YoY (Sec 10 item 1; brief L411).**
Bear from text: management never states one clean YoY (40% at L19, 50% at L121, 54.8% implied); and the Rs 235 Cr prior base was itself tariff-pull-forward-inflated (chairman L121: prior year shipped next quarter's goods early to beat tariffs), so comparability is broken.
Survives? NO — already fully incorporated (Sec 10 item 1 caveat, Step 7A "CONTRADICTED framings," YAML flag). No graft needed.

**Positive claim 2 — EBITDA +120%, margin "inched to 24%," PAT "more than doubled" (brief L411; Step 1).**
Bear from text: Rs 22 Cr non-recurring tariff refund sits in other income; strip it and PAT is ~Rs 52 Cr (not "more than doubled") and margin 22.5% (not 24%). Stronger still, on management's own "we include all other income" definition (L27) and the analyst's un-contested ~Rs 37 Cr OI (L25), ex-OI operating EBITDA ≈ (103.9-37)/363.7 ≈ **18.4%** — at the thesis-broken <18% tripwire, worse than the 22.5% A4 highlighted.
Survives? PARTIAL — the refund/22.5%/Rs 52 Cr strand is already grafted (Step 7A, brief, YAML). The sharper ~18.4% ex-OI estimate is NOT shown; A4 declared the metric "NOT DISCLOSED / un-testable." I judge it does NOT cleanly survive as a must-graft because it rests on two management-unconfirmed inputs (OI = exactly Rs 37 Cr, and EBITDA Rs 103.9 Cr being fully OI-inclusive — noting the 24% figure itself does not reconcile to 103.9), so A4's conservative "withheld = adverse read" already captures the thesis impact (both margin tripwires marked un-testable/at-risk; flags fired). **Recommended enhancement, not a gate failure:** A4 should add the ~18.4% ex-OI figure as an explicit illustrative bear estimate (with the unconfirmed-input caveat) since it converts "un-testable" into "estimable at/near the thesis-broken line."

**Positive claim 3 — Net cash GREEN at Rs 456.67 Cr (Sec 10 item 9; Step 7A).**
Bear from text: the figure is gross "cash and cash equivalents INCLUDING investments" (L9), is flattered by the Rs 22 Cr refund just received in cash into Goldium USA (L41), and includes undeployed QIP funds being poured into loss-making ORIGEM store rollout (L45) — i.e. not a clean operating-net-cash number.
Survives? NO for verdict purposes — even stripping the full Rs 22 Cr one-off leaves ~Rs 434 Cr, still above the Rs 400 Cr green line, so the GREEN classification is unchanged. A legitimate quality caveat but immaterial to the verdict; recommended as a one-line footnote in Step 7A, not required for save.

**Adversarial verdict:** No bear counter survives that overturns an A4 classification or is absent in substance. A4's bear coverage is complete for gate purposes. Two optional enhancements logged (ex-OI ~18.4% illustrative estimate; net-cash-quality footnote); neither blocks save.

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four brief parts present).
- Coverage: PASS (turns 99=99, rounds 10=10, questions 32=32, mgmt numbers 27=27, hedges 19=19; no orphan, no missing).
- Arithmetic: PASS (every derived metric reconciles within rounding; the 24%-vs-disclosed and multi-framed-growth gaps are correctly surfaced as flags, not errors).
- Adversarial: PASS (no surviving un-incorporated counter overturns a classification).

Non-blocking notes for the record (do NOT gate the save; optional A4 polish next cycle): (a) A3-F10-01 is listed as incorporated but lacks an explicit inline citation — substance appears covered under the tariff/OI treatment; (b) add ex-OI ~18.4% as an illustrative bear estimate to Step 7A; (c) footnote net-cash as gross/one-off-inflated.

```yaml
stage: A5-adversary
company: "GOLDIAM"
quarter: "q1fy27"
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
