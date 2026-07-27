# A5 ADVERSARY / COMPLETENESS AUDIT — CONCALL ADDENDUM — WELCORP Q1 FY27 (PASS 2)

Target: `review_concall_addendum_welcorp_q1fy27.md` (A4 Role-5 concall addendum, corrected).
Evidence spine (re-derived independently, A4/A3 cites NOT trusted blindly):
`extract_concall_welcorp_q1fy27.txt` (A1), `ledger_concall_welcorp_q1fy27.md` (A2).
Scope: Role-5 concall only. Role-4 filing numbers were A5-audited COMPLETE previously and
are out of scope here; I re-confirm the addendum does not re-derive or alter them.

This is the second audit pass. Pass 1 returned INCOMPLETE on a single arithmetic FAIL:
the Section 3 "Reconciliation summary" said **5 PARTIAL** while enumerating **6**, so the
category tally summed to 11, not 12. This pass verifies that specific fix AND re-confirms
nothing else regressed.

---

## 0. FIX VERIFICATION (the pass-1 blocking FAIL)

Prior FAIL: §3 summary "5 PARTIAL" vs six enumerated PARTIAL rows -> 3+1+5+2 = 11 ≠ 12.

Corrected text now at addendum L132 (read verbatim):
> "of 12, **3 ANSWERED** (Q5, Q9, Q10), **1 ANSWERED-with-caveat** (Q6), **6 PARTIAL**
> (Q2, Q3, Q4, Q7, Q8, Q12 shape), **2 DODGED/NOT ADDRESSED** (Q1, Q11)."

Recompute: 3 + 1 + 6 + 2 = **12**. Matches the stated universe of 12. **FIX CONFIRMED.**

Cross-check against the §3 disposition table (each row's own status column):
- ANSWERED: Q5 (L123), Q9 (L127), Q10 (L128) = 3
- ANSWERED-with-caveat: Q6 (L124) = 1
- PARTIAL: Q2 (L120), Q3 (L121), Q4 (L122), Q7 (L125), Q8 (L126), Q12 (L130) = 6
- DODGED/NOT ADDRESSED: Q1 (L119), Q11 (L129) = 2

Table dispositions and the summary tally now agree, and both sum to 12. No orphaned or
double-counted question. The single PARTIAL digit that was wrong in pass 1 is corrected;
no over-correction (ANSWERED/DODGED counts unchanged and still correct).

---

## 1. COVERAGE AUDIT (fresh grep pass vs A2 ledger, then A4 citation check)

Fresh enumeration performed by me this pass:
- Turns: `grep -c` on the numbered-line pattern `^\s*\d+\t` = **151** (turns 1-151). Matches ledger.
- Analyst callers: fresh grep `question from the (line|lineup|lineoffs)` caught 14 intros
  (incl. the garbles turn 40 "lineup"/Sneha and turn 112 "lineoffs"/Jooshi). The two the
  narrow pattern skips use the variant "question **is** from the line" — turn 76 (Nishantas)
  and turn 89 (Retesia); adding those reconciles to **16** distinct callers, matching the
  ledger (Methodology Note 1) exactly.
- Questions (Q1-Q44) and mgmt_numbers (34): verified against the ledger's transparent
  Methodology Notes 1-3; the "?"-mark (42->21) and regex-token (52->34) reconciliations are
  documented and defensible on this auto-generated source. No row I can independently
  establish is missing.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Speaker turns | 151 | 151 | none — A4 asserts "all 151 turns reviewed" (§1); material turns individually cited | PASS |
| Analyst callers | 16 | 16 | none — 23 participant rows blanket-reviewed; garbles reconciled (Note 1) | PASS |
| Distinct questions | 44 | 44 | none — 44 asserted reviewed; the 12 Role-4 mgmt questions individually reconciled §3 | PASS |
| Mgmt quantitative claims | 34 | 34 | none — key numbers cited in §2c forward table / claims inventory | PASS |
| Participant rows | 23 | 23 | none — CFO_SILENT (row 2) carried as A3-13 governance overlay | PASS |
| Forward/hedge sweep (Table 5) | n/a | n/a | none — deferred-to-A3 lexicon; A4 uses it for archetype/commitment register | PASS |

**Orphan-row check (A3 loop-back trigger):** A4 incorporates all 14 A3 findings (A3-01..A3-14),
and §5A maps every FORWARD-SIGNAL and AMBIGUOUS finding to a resolved question or carry-forward.
No ledger row is left unreviewed. **No A3 loop-back.**

**Missing-from-ledger check (A2 loop-back trigger):** my independent turn count (151) and caller
count (16) match the ledger exactly; no enumeration my fresh pass surfaced is absent from the
ledger. **No A2 loop-back.**

Coverage did NOT regress from pass 1.

---

## 2. ARITHMETIC AUDIT (recompute every derived figure from raw extract / referenced base)

Cite spot-checks (each verified to say what A4 claims, at the line cited):

| Cite | A4 claim | Extract check | Status |
|---|---|---|---|
| turn 35 / L51 | KSA "quarter three" | L51: "...by the by the by the quarter three in any case"; slip "what we mentioned earlier was Q2...nothing much have slipped" | PASS |
| turn 36 / L52 | US Little Rock LSAW commissioned | L52: "It is up and running...We have commissioned it...trials done...mill completely stabilized...about to start execution of certain orders" | PASS |
| turn 87 / L103 | EPIC ">22% / no further dilution" | L103: "recently being four four and a half%...after that also we have more than 22%...largest shareholder...no further intentions of diluting it" | PASS |
| turn 27 / L43 | capex "60-65% ... no new capex" | L43: "done with almost 60 60 65% of our capex...balance capex will get exhausted...not committing for any other capex...the answer is no" | PASS |
| turn 91 / L107 | guidance held / refused to raise | L107: "we don't want to revise our guidances...last four years...we have always met them if not exceeded them" | PASS |
| turns 4/93 | order book 25,750 vs 24,750 | L20: "approximately $25,750 cr...almost $2.7 billion"; L109: "when we say 24750 cr of order book" | PASS |
| CFO-silent | CFO 0/44 answers | Ledger Table 1 row 2 `CFO_SILENT`; non-diarized transcript assigns every substantive answer to CEO; A3-13. A4 hedges appropriately | PASS |

Derived / recomputed metrics:

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Implied FY margin | ~14.25% | 2,850 / 20,000 = 14.25% | §2c, deck guidance | PASS |
| FY27E vs Notion base | +2.3% above 19,550 | 20,000/19,550 − 1 = +2.30% | §2c Step-2 diagnostic | PASS |
| Q1-annualised run-rate / H2 step-up | 16,324; "~30%" step-up | 16,324/4 = 4,081 Q1; (20,000−4,081)/3 = 5,306/qtr = +30.0% vs 4,081 | §2c (carried from Role 4) | PASS |
| SC gap (PAT), YAML | gap 932.04, 88.9% | 1,047.88 − 115.84 = 932.04; 932.04/1,047.88 = 88.94% | YAML sc_gap_pat (Role-4 carry) | PASS |
| A3 findings tally | "all 14" (5+4+1+4) | 5+4+1+4 = 14 | §1 | PASS |
| Deflection count | "~7" | turns 13,33,42,93-99,107,122-126,92 = 7 | §2a | PASS |
| Commitment register | "10 dated commitments" | enumerated list = 10 | §2a | PASS |
| **12-question reconciliation summary** | **"6 PARTIAL" / 3+1+6+2=12** | **6 PARTIAL** (Q2,Q3,Q4,Q7,Q8,Q12 all PARTIAL in §3 table); 3+1+6+2 = **12** ✓ | §3 Reconciliation summary | **PASS (fixed)** |

**Role-4 non-alteration confirmed:** every filing number the addendum touches (756 EBITDA, 18.5%
Q1 margin, 2,850/20,000 guidance, 547.93 EPIC one-off, PAT +199%, SC gap 88.9%) is *referenced*
consistently and is *not* re-derived or changed. Decision Status not upgraded ("HELD...stays HELD";
YAML matches). Cash-conversion INDETERMINATE preserved (YAML `cash_conversion: INDETERMINATE`;
trigger 2 "NOT FIRED (cannot assess)"; "caps...at PROCEED WITH CAVEATS"). Guardrails intact.

**Promise-vs-delivery baseline:** correctly a BASELINE, not a computed ratio (§2a: "trailing-4-quarter
credibility ratio is NOT YET COMPUTABLE...no Grade A/B/C/D"; Concall Verdict: "NOT COMPUTABLE
(baseline)"). PASS.

No arithmetic mismatch remains. The single pass-1 FAIL is resolved; no new discrepancy introduced.

---

## 3. ADVERSARIAL READ — three most-positive claims, strongest bear counter from the SAME extract

**Claim 1 — "US Little Rock LSAW confirmed commissioned and executing orders (turn 36); FY28 driver
de-risked."**
Bear counter (L52): same turn says "about to start execution of *certain* orders" — commissioning ≠
run-rate revenue; US book confirmed only "through FY28", FY29 explicitly UNBOOKED (turn 45) and
substrate-gated (turn 92).
*Survives?* **NO.** A4 grafts these: "do NOT add on this alone," FY28 "full impact" pending, FY29
unbooked carried to N3. Incorporated.

**Claim 2 — "KSA to Q3 FY27 moves thesis-broken trigger (1) further from firing."**
Bear counter (L51): turn 35 is a *documented second slip* (Notion Q1 FY27 first-production -> "Q2"
-> "quarter three"), phrased softly ("should progressively be coming up...in any case"). Repeated
one-quarter slippage reads as drift *toward* the Q4 edge.
*Survives?* **NO (borderline).** A4 acknowledges the Q2->Q3 slip and retains the watch "for any Q2
re-slip to Q4+." Counter-balanced in the same section. No new graft required.

**Claim 3 — "Archetype downgraded to Measured & Credible-leaning: guidance held un-raised despite a
large optical beat (turn 91)."**
Bear counter (same extract): the identical management refused every hard number — order-book split
(turns 13/33/42, offline), tonnage (turns 93-99 "difficult"), QoQ volume (turn 107), data-center %
(turns 122-126), Sintex loss magnitude (turn 109), CFO 0/44 (A3-13). "Guidance held" is equally
consistent with an unfalsifiable low-disclosure posture; turn-91 "always met" self-claim is
unverifiable (no prior concall log — baseline).
*Survives?* **NO.** A4 retains the "guards-granularity / CFO-silent governance overlay" as a named
qualifier and keeps CFO-silence + segment-deflection as watch items (N5, N2). Incorporated.

**No surviving bear counter requires grafting into A4.** No A4 loop-back on adversarial grounds.

---

## 4. VERDICT

**COMPLETE.**

- Fix verification: PASS — §3 summary now "6 PARTIAL"; categories sum to 12 (3+1+6+2); table
  dispositions and summary tally agree.
- Coverage: PASS — 151/151 turns, 16/16 callers, 44/44 questions, 34/34 numbers, 23/23 participants;
  no orphan rows; no A2/A3 loop-back. Did not regress.
- Arithmetic: PASS — all derived metrics recompute within rounding; the single pass-1 mismatch is
  resolved and no new discrepancy introduced.
- Adversarial read: PASS — all three bear counters already incorporated by A4.
- Guardrails: PASS — Decision Status not upgraded (stays HELD); cash-conversion INDETERMINATE
  preserved (caps at PROCEED WITH CAVEATS); promise-vs-delivery correctly a BASELINE; Role-4
  numbers referenced, not altered.

No loop-back to A2, A3, or A4. This addendum proceeds to Notion save.

```yaml
stage: A5-adversary
company: "WELCORP"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
