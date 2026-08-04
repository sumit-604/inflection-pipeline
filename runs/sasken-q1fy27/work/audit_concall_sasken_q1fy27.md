# A5 ADVERSARY / COMPLETENESS AUDIT — SASKEN Q1 FY27 CONCALL

Audit target: `review_concall_sasken_q1fy27.md` (A4). Primary evidence:
`extract_concall_sasken_q1fy27.txt` (51 turns, 8 analysts). Fresh context;
cites re-derived independently, not deferred to A4/A3.

---

## 1. COVERAGE AUDIT (independent re-enumeration vs the ledger)

Fresh grep of the extract: `===== TURN NN` markers run 01 -> 51 contiguously
(no gaps, no duplicates). Eight named analysts (header l.8, confirmed at
turns t8, t14, t18, t22, t28, t32, t36, t44). Q&A spans t8-t49; 21 analyst
Q&A blocks. Opening t3-t6; host t1-t2, t7; close t50-t51.

| Category | Ledger (per A4 preamble) | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| Turns | 51 | 51 (t01-t51, contiguous) | none | PASS |
| Notes | 0 | 0 (transcript, no PDF/OCR) | none | PASS |
| Slides | 0 | 0 | none | PASS |
| Analysts | 8 | 8 (Surka, Priyanker, Chri, Naven Be, Maneka, Gulwani, Samar, Sanjay) | none | PASS |
| Q&A blocks | (8 primary + follow-ups) | 21 blocks (t8-t49) | none | PASS |
| Standing Qs (Role 4) | 12 | 12 all cross-referenced | none | PASS |

**Q&A block-by-block trace (every block A4 addressed in Section 6A):**
Q1/1b/1c (t8-13), Q2/2b (t14-17), Q3/3b (t18-21), Q4/4b/4c (t22-27),
Q5/5b (t28-31), Q6/6b (t32-35), Q7/7b/7c/7d (t36-43), Q8/8b/8c (t44-49).
All 21 present in A4's inventory. **No turn with material content was dropped.**
Opening claims t3-t6 inventoried (14 rows). Close t50 (recurring-call commit)
and t51 (moderator) both cited. **No orphan row; no ledger gap. COVERAGE PASS.**

The 12-question answer-status table (Section 4) covers Q1-Q12; tally
0 answered / 7 PARTIAL / 2 EVADED / 3 NOT ADDRESSED sums to 12 and the
membership lists (PARTIAL Q1,2,3,4,6,7,10; EVADED Q11,12; N/A Q5,8,9) are
internally consistent. Every EVADED (Q11 SSTPL, Q12 WC) and NOT ADDRESSED
(Q5 unnamed sub, Q8 disputed tax, Q9 Borqs goodwill) rolls forward into
Section 9 (Q2 items #3, #2, #6, #8, #7 respectively). PASS.

---

## 2. ARITHMETIC AUDIT (recompute every derived tally/metric)

| Metric | A4 value | My recompute (source line) | Status |
|---|---|---|---|
| Revenue split adds to total | 219 + 120 = 339 | 219+120 = 339 (t6 l.13) | PASS |
| Revenue YoY / QoQ | +24% / +1.6% | as spoken (t6 l.13) | PASS |
| PAT margin | Rs23 Cr @ 6.9% | 23/339 = 6.78% ~ 6.9% (t6 l.13) | PASS (rounding) |
| Blended EBIT | 9.5% (Rs31 Cr) | as spoken; 31/339 = 9.1% is a **transcript** internal gap, not A4's (t6 l.13) | PASS (A4 anchored to spoken 9.5%) |
| ACV $40.5M | $40.5M / $24M new | t6 garbles "about 4 million"; t17 l.35 states 40.5 — A4 reconciled correctly | PASS |
| Answer-status tally | 0/7/2/3 = 12 | 0+7+2+3 = 12; lists consistent | PASS |
| **Response-quality distribution (6A)** | **1A / 10B / 9C / 1D** | **1A / 11B / 8C / 1D** (see count below) | **FAIL** |
| Specificity ratio | "~0.3 to 0.35" | 4/(4+6..7) = 0.36-0.40 | soft-low; qualitative bucket LOW unchanged (immaterial) |
| Hedge count | "more than seven" | exactly 7 instances listed | immaterial |

**Response-quality miscount (the one hard arithmetic FAIL).** Re-tallying
A4's own 21 grade cells in Section 6A (review l.201-221):
- A (1): Q1c t12-13.
- B (11): Q1b t10-11, Q2b t16-17, Q3 t18-19, Q3b t20-21, Q4c t26-27, Q5 t28-29, Q5b t30-31, Q6 t32-33, Q7b t38-39, Q7c t40-41, Q8 t44-45.
- C (8): Q1 t8-9, Q4 t22-23, Q4b t24-25, Q6b t34-35, Q7 t36-37, Q7d t42-43, Q8b t46-47, Q8c t48-49.
- D (1): Q2 t14-15.

Total 1+11+8+1 = 21 (correct block count). A4's stated distribution
"1 grade A, 10 grade B, 9 grade C, 1 grade D" (review l.223) is wrong:
**one B is mis-bucketed into C.** Correct is **11B / 8C**. This is an exact
count, not a rounding artifact, so it clears the "above rounding = FAIL" bar.

Materiality: the miscount does NOT change any verdict, grade, or gate — the
distribution still "clusters at B/C." But per the arithmetic-audit discipline
(recompute every derived metric; any mismatch = FAIL, loop back to A4), this
is a blocking defect. The fix is a one-line correction, not an analytic rework.

---

## 3. QUOTE-CHECK OF LOAD-BEARING CLAIMS (every task-named claim)

| # | A4 claim | Cited turn | Verbatim check | Verdict |
|---|---|---|---|---|
| a | First live call; commits to recurring calls | t3 l.7; t50 l.101 | t3: "strengthen how we engage... regular and transparent communication... connect with you directly through these quarterly earnings call"; t50: "look forward to next quarter's earnings call" | SUPPORTED (see nuance below) |
| b | CFO FY27 "large consumption of cash"; distress denied | t37 l.75; t39 l.79 | t37: "we believe even this year we would have a large consumption of cash"; "not that we've had any challenges in our collections" | SUPPORTED |
| c | Top-5 ~56%; "stable" (CFO) vs analyst "up 52 to 56" | t6 l.13; t8 l.17 | t6: "top five... broadly stable at approximately 56%"; t8: "top five concentration is up 52 to 56" | SUPPORTED |
| d | Borqs breakeven reframed ~Rs120 Cr/qtr vs prior $60-70M annual | t40 l.81; t41 l.83 | t40 (analyst): "break even at a 60 $70 million top line"; t41 (CFO): "break even point would be about 20 million 12 million... on a quarterly revenue" | SUPPORTED as garbled reconstruction (see note) |
| e | 60x4x3 timeline slip to "one or two more years" | t9 l.19; t23 l.47 | t9: "3 years goes metaphoric. We may take maybe one or two more years"; t23: "we may take maybe one more year" | SUPPORTED |
| f | Margin history "2-3% to 11-12% EBIT in six quarters" | t27 l.55 | t27: "in a matter of six quarters really turn around... from maybe about 2 to 3% up to 11 12% EBIT... I'm talking software services" | SUPPORTED |
| g | Growth-over-margin tension | t25 l.51; t27 l.55 | t25: "growth is the most important imperative... I'm not stopping engines... to moderate it"; t27: "we will maintain our margins while we maintain our growth momentum" | SUPPORTED |

No misquote and no number that fails to reconcile among the load-bearing set.
Three precision nuances (non-blocking):

- **Claim (a) "management states this explicitly" (first call).** The verbatim
  t3 l.7 conveys a *commitment to strengthen engagement / recurring calls*, not
  a literal "this is our first-ever call" sentence. The "first live call" fact
  is carried by the A1 extraction annotation (header l.3, l.12) and the Role 4
  prior ("no concall existed"), which is legitimate context. The cap-lift logic
  does not actually depend on the word "first" — it depends on a live Q&A call
  now existing plus a recurring-call commitment, both of which ARE verbatim. So
  the phrasing slightly over-attributes to t3, but nothing downstream breaks.

- **Claim (d) numbers.** The transcript "20 million 12 million... quarterly" is
  genuinely garbled; A4 reads it as ~Rs120 Cr/qtr and flags it garbled. Sanity
  check favors A4: Rs120 Cr/qtr ~ Rs480 Cr/yr ~ US$58M/yr, i.e. the *same
  magnitude* as the prior "$60-70M annual," so the "reframe" is a change of
  denomination, not a 4x-higher bar. A4 correctly rolls confirmation to Q2 (#4).
  Defensible.

- **Claim (f) "corroborated on the record."** Section 8A calls the six-quarter
  software-services margin recovery "corroborated on the record." It is
  management's own unverified recollection (t27), volunteered while deflecting
  the growth-vs-margin question, and refers to *software services only* — while
  the same-quarter blended EBIT is 9.5% and Product-Solutions margin collapsed
  to 5.9% (t6 l.13). "Corroborated" over-credits an assertion; "management
  asserted (unverified)" is the accurate frame. See Adversarial claim #2.

Minor uncaught forensic (non-blocking): CFO states "93 active customers" (t6
l.13) while Modi says "total active customers of 96" (t9 l.19). 93 vs 96 is an
unreconciled internal count A4 did not flag; immaterial to the verdict.

---

## 4. ADVERSARIAL READ — three most-positive A4 claims, strongest bear counter each

**Positive claim 1 — "Management-Grade structural cap LIFTED" (t3 l.7; t50 l.101).**
Bear counter (same text): the call that supposedly restores the pressure test
delivered 0/12 specific answers, 8 explicitly declined disclosures (Section 3C),
and guidance refused >=4 times — a disclosure-averse first call is a thin
transparency signal, and "cap lifted" risks crediting form over substance.
**Survives? NO — already fully incorporated.** Section 2B ("no upgrade earned"),
the EVASIVE-to-MEASURED archetype, and flag #3 (0/12) all carry this counter.
The cap-lift is scoped narrowly to removing an *artificial ceiling*, not to
awarding credit. Already present.

**Positive claim 2 — "software-services margin recovery corroborated on the
record: 2-3% to 11-12% EBIT in six quarters" (t27 l.55).**
Bear counter (same text): this is management's own uncorroborated recollection,
software-services-only, stated while deflecting the margin question — and it
coincides with a *falling* consolidated picture (blended EBIT 9.5%, PS margin
5.9% at t6 l.13). It is an assertion, not independent corroboration.
**Survives? PARTIALLY — as a wording tighten, not a missing bear point.** A4
already flags PS 5.9%, blended 9.5%, and "anchor the thesis to filing numbers"
(3E) and the growth-vs-margin tension (6C Exchange 3). The substantive bear
content is present; only the single word "corroborated" in Section 8A
over-credits. Recommend A4 soften to "management asserted (unverified,
software-services only)." Non-verdict-bearing; a caveat graft, not a FAIL.

**Positive claim 3 — CFO "frank cash-consumption admission rather than spinning
it, and explicitly denied a collection problem" (t37 l.75).**
Bear counter (same text): candour on *direction* co-exists with total opacity
on *magnitude* — no CFO figure, no H1 commitment, no quantum/timing — plus an
admitted reliance on "external funds" to finance growth (t37 l.75), a
debt/dilution signal. Selective candour is not full candour.
**Survives? NO — already incorporated.** Section 5 quotes "external funds";
Section 6C Exchange 1 explicitly asks the follow-up "what net-debt figure funds
the external-funds portion"; Section 8B holds trigger (c) NOT FIRED and the
cash read INDETERMINATE-leaning-NEGATIVE, refusing to resolve positive. Present.

**Net:** two of three bear counters are already grafted into A4; the third is a
one-word over-credit ("corroborated" -> "asserted"), recommended but not
verdict-changing.

---

## 5. VERDICT-LOGIC STRESS TEST (task adversarial questions a-e)

**(a) "Grade B, cap lifted, no upgrade earned" — defensible.** Not too harsh
(the cap-lift explicitly credits the first voluntary call and recurring-call
commitment, t3/t50), not too generous (0/12 specific answers, 4x guidance
declined, cash guided the wrong way, first 60x4x3 slip all withhold the
upgrade). The split of "remove artificial ceiling" from "earn an upgrade on
merit" is the correct construction. DEFENSIBLE.

**(b) Cash read INDETERMINATE-leaning-NEGATIVE — correct; (c) is NOT pre-fired.**
Trigger (c) is defined on the *realized FY27 consolidated CFO sign*, an actual,
not on guidance. Management's "large consumption of cash" is directional
guidance; firing (c) off guidance would violate mechanical-trigger discipline
(CLAUDE.md: Decision Status changes only when a pre-committed trigger formally
fires) and the "never let INDETERMINATE cash silently resolve" rule. A4's
"NOT FIRED but MOVED CLOSER" plus INDETERMINATE-leaning-NEGATIVE is exactly
right. DEFENSIBLE.

**(c) Decision Status AVOID and verdict PROCEED WITH CAVEATS held — correct.**
No trigger fired, so Decision Status is unchanged per discipline; INDETERMINATE
cash caps the verdict at PROCEED WITH CAVEATS (house NEVER rule), which A4
applied. CMP Rs2,120.60 sits far above every entry band, so no position
mechanics engage regardless. DEFENSIBLE.

**(d) "MAINTAINED to modestly WEAKENED" — balanced.** The counter-case
(transparency step-up + services-margin recovery => net-neutral-to-positive)
has surface appeal, but (i) the margin recovery is a *confirmation* of the
existing Role 4 thesis, not new positive information, and (ii) transparency
does not move the decision gate, whereas the *gate metric* (consolidated CFO)
weakened on management's own guidance. Weighting the hard gate signal over soft
governance credit and landing at "modestly WEAKENED" is defensible and, if
anything, avoids over-crediting soft positives. DEFENSIBLE.

**(e) Roll-forward complete.** All 2 EVADED + 3 NOT ADDRESSED + open PARTIALs
carry into Section 9 (Q2 #1-#12), each tagged to its CN/results-FN origin.
PASS.

---

## 6. FINDINGS SUMMARY

- COVERAGE: PASS. 51/51 turns, 8 analysts, 21 Q&A blocks, 12 standing questions
  all addressed. No orphan row, no ledger gap, no dropped material turn.
- QUOTE-CHECK: PASS. All seven task-named load-bearing claims supported by
  their cited turns; no misquote; no number fails to reconcile. Three minor
  precision nuances noted (first-call attribution, garbled Borqs figure,
  "corroborated" over-credit) — none blocking.
- ARITHMETIC: **ONE FAIL.** Response-quality distribution stated 1A/10B/9C/1D;
  correct recompute from A4's own 21 grade cells is **1A/11B/8C/1D** (review
  l.223). Exact-count mismatch, above rounding. Loop back to A4.
- ADVERSARIAL: two of three bear counters already incorporated; the third is a
  recommended wording tighten ("corroborated" -> "management asserted,
  unverified, software-services only") — not verdict-bearing.
- VERDICT LOGIC: all five stress tests (grade, cash read, Decision Status,
  net-impact framing, roll-forward) defensible from the transcript.

The analysis is substantively sound and the verdict is defensible. The single
blocking defect is a mechanical tally miscount that the arithmetic-audit
discipline requires be corrected before save. Because a recomputation mismatch
above rounding exists, the run cannot be certified COMPLETE as-is.

**VERDICT: INCOMPLETE — loop back to A4.**
Gap: Section 6A response-quality distribution (review l.223) miscounts the
21 Q&A grades as 1A/10B/9C/1D; the correct tally is 1A/11B/8C/1D (one B
mis-bucketed as C). Correct the line and re-emit; no analytic rework required.
Recommended (non-blocking) at the same pass: soften "corroborated on the record"
(Section 8A) to "management asserted (unverified, software-services only)."

```yaml
stage: A5-adversary
company: "SASKEN"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "Q&A response-quality distribution (Section 6A)"
    a4_value: "1A / 10B / 9C / 1D"
    recomputed: "1A / 11B / 8C / 1D"
    source_line: "review l.223 (re-tallied from grade cells l.201-221)"
surviving_bear_counters:
  - claim: "software-services margin recovery 'corroborated on the record' (2-3% to 11-12% EBIT in six quarters)"
    counter: "management's own unverified recollection, software-services only, coincident with blended EBIT 9.5% and PS margin 5.9%; assert not corroborate"
    source_line: "t27 l.55; t6 l.13 (review Section 8A)"
loop_back_to: "A4"
gap: "Section 6A response-quality distribution miscounted as 1A/10B/9C/1D; correct tally is 1A/11B/8C/1D (one B mis-bucketed as C, review l.223). Verdict logic and all quotes pass; fix is a one-line correction, no analytic rework."
```
