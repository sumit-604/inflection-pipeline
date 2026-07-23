# A5 ADVERSARY / COMPLETENESS AUDIT — AYE Finance, Q1 FY27

Auditor: A5 (Opus 4.8), fresh context. Inputs seen: A4 merged review, A1 line-numbered
extract, A2 ledger. A3 reasoning NOT seen — every A3 cite below was re-derived from the
A1 transcript line, not deferred to. All "L##" = A1 transcript line number.

---

## 1. COVERAGE AUDIT (fresh grep pass diffed against A2)

Independent re-enumeration of the gated categories:

| Category | A2 count | My fresh count | Method / evidence | Orphan rows | Status |
|---|---|---|---|---|---|
| Opening-remark topic blocks | 21 | 21 | All on transcript L8 (single continuous turn); A4 Step 1 table carries 21 rows | none | PASS |
| Q&A exchanges | 13 | 13 | 12 via `question comes (from\|on) the line of` (L10,26,35,43,48,64,78,84,94,99,112,121) + Pavan Kumar via the `next question **in** the line of` variant (L73) — exactly the second-pattern catch A2 documented | none | PASS |
| Q&A individual sub-questions | 35 | 35 (accepted) | A2 per-exchange breakdown 3+3+3+1+4+2+1+2+3+2+5+3+3; A4 Step 4A covers all 13 exchanges | none | PASS |
| Quantitative-disclosure lines | 42 | 42 (accepted) | A2 two-method reconciliation (−1 provenance L2, +1 L20 "kores/K", +1 L88 "60 odd/3.15") is sound; spot-checked L20/L22/L37/L39/L88/L95/L115/L122/L123 all present and correctly figured | none | PASS |
| Forward-statement / hedge lines | 31 | 31 (accepted) | A2 triage (37−9+3) verified against L8/L14/L22/L29/L31/L55/L95/L117; A4 Step 2L + Step 6 forward table cover them | none | PASS |
| Speaker turns | 108 | 108 (accepted) | Table 2 turns 1–108 map cleanly to content lines 4–130; A4 preamble reviews | none | PASS |
| Participants | 20 | 20 | 7 non-analyst (operator, IIFL host, Sanjay/Nirit/Gaurav/Sovan, SGA) + 13 analysts | none | PASS |

**A3-finding → management-question coverage.** A4 incorporates all 16 A3 findings
(F1.1, F1.2, F6.1–F6.5, F7.1–F7.3, F9.1, F17.1–F17.5). I re-derived each mapping against
the QfM master (Section C) and confirm every FORWARD-SIGNAL / AMBIGUOUS finding generated
≥1 question:
- F6.1→Q1; F1.2/F7.1/F17.4→Q2,Q3; F7.2→Q4; F17.5→Q5; F1.1/F9.1→Q6,Q11; F6.2→Q7;
  F6.3→Q8; F6.4→Q9; F6.5→Q10; F17.3/F7.3→Q12; F17.1→Q15; F17.2→Q16.
- Scope/variant items also questioned: CRAR→Q13, AUM 7,324/7,384→Q14.
- **No orphan finding. No orphan gated ledger row. No row my fresh pass found that the
  ledger lacks.**

**Two minor ledger flags NOT surfaced by A4 (advisory, non-blocking):**
- (a) A2 `AMBIGUOUS_UNIT` on L53 ("~780 crores" per-branch AUM). This sits inside the 42
  quant lines A4 marks "all reviewed," but A4 does not explicitly dispose of it. It is
  self-evident transcription noise (571 branches on a Rs 7,324 Cr book ⇒ ~Rs 12.8 Cr/branch
  average, so a single branch cannot hold Rs 780 Cr) and is thesis-irrelevant. Not a
  coverage failure; recommend a one-line "reviewed, transcription artifact, no finding" tag.
- (b) A2 `NUMBER_VARIANT` self-correction "48,000…44,000" (L27). A4 uses the correct 44,000
  throughout; immaterial. No action required.

Coverage verdict: **PASS.**

---

## 2. ARITHMETIC AUDIT (recomputed from A1-cited raw numbers)

| Metric (A4) | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| Ex-overlay credit cost | ~3.68% | 6 Cr ×4 (annualised) / 7,324 = 32.8 bps; 4.01% − 0.33% = 3.68% | L8, L39 | TIE |
| Overlay ≈ bps of book | ~33 bps | 24 Cr / 7,324 = 0.328% | L39 | TIE |
| Other-income step-down | ~Rs 32–35 Cr | 20 (DA) + 12 (forex) = 32; mgmt states "nearly 35… 32 to 33" | L20, L22 | TIE (range matches verbatim) |
| Implied Q1 FY26 PAT base | ~Rs 30.7 Cr | 75 / 2.44 = 30.74 | L8 (+144%) | TIE (labelled unanchored) |
| Implied Q1 FY26 AUM | ~5,722 | 7,324 / 1.28 = 5,721.9 | L8 (+28%) | TIE (labelled unanchored) |
| Implied Q1 FY26 disbursement | ~999 | 1,219 / 1.22 = 999.2 | L8 (+22%) | TIE (labelled unanchored) |
| Implied Q4 NIM | 15.7% | 15.9 − 0.20 | L8 (+20 bps QoQ) | TIE (labelled unanchored) |
| Implied Q4 credit cost | 4.30% | 4.01 + 0.29 | L8 (−29 bps QoQ) | TIE (labelled unanchored) |
| GNPA QoQ | −28 bps | 4.77 − 4.49 = 0.28 | L8 | TIE |
| GNPA YoY | −11 bps | 4.6 − 4.49 = 0.11 | L8 | TIE |
| AUM QoQ | +4% | 7,324 / 7,044 = +3.97% | L8 | TIE |
| Opex QoQ | −60 bps | 9.5 − 8.9 = 0.60 | L118/L119 | TIE |
| CRAR variance | −108 bps | 42.38 − 41.3 = 1.08 | L8 vs prior-workup | TIE |
| NIM above guidance | ~115 bps | 15.9 − 14.75 = 1.15 | L8, L36/L116 | TIE |
| PAR X QoQ | +11 bps | 7.01 − 6.9 = 0.11 | L8/L95, L115 | TIE |
| PAT annualised | ~Rs 300 Cr | 75 × 4 = 300 | L8 | TIE (labelled unanchored) |
| Book at 4–4.5x from 7,384 | ~Rs 14,000 Cr | 7,384 × ~1.9 ≈ 14,030 | L123 | TIE |
| Specificity ratio | ~0.6 | 20 [FC] / 31 total = 0.65 (A4 labels "roughly") | A2 Table 6 | TIE (approx, labelled) |

**No mismatch above rounding.** Every derived figure ties to its A1 source line, and every
figure with no spoken base (Q1 FY26 absolutes, Q4 NIM/credit cost) is explicitly labelled
"arithmetic implication, not anchored" — the discipline the concall-only scope demands.

**One immaterial imprecision (advisory, non-blocking):** Step 4 states removing the ~Rs 6 Cr
overlay leaves "underlying PAT ~Rs 6 Cr higher." That is the pre-tax effect; post-tax the PAT
uplift is ~Rs 4.5 Cr at a ~25% rate. A4 flags tax as ND, so this is a minor loose end, not an
error. Recommend labelling it "~Rs 6 Cr pre-tax."

Arithmetic verdict: **PASS.**

---

## 3. ADVERSARIAL READ (three most-positive claims, strongest same-text bear counter)

**Positive claim 1 — "PAT +144% is core-driven, not treasury-driven; if anything UNDERSTATED
by the loss of ~Rs 32–35 Cr of prior-period other income" (Step 2 answer 4; Step 4).**
Bear counter from the same text: the ~Rs 32–35 Cr (DA Rs 20 Cr + forex Rs 12 Cr) is
explicitly a **Q4 FY26 (QoQ) figure** — L20 says "last quarter." The +144% is a **YoY**
comparison to Q1 FY26, whose other income is **ND**. So the "understated by 32–35 Cr" clause
mis-times a QoQ item against a YoY base; you cannot assert the YoY growth is understated by it.
**Survives?** PARTIALLY — but the load-bearing claim ("this quarter's PAT does not lean on
DA/forex," which is TRUE: DA nil L20, forex→OCI L22) stands, and A4 elsewhere correctly frames
the Rs 32–35 Cr as a Q4/QoQ item and separately concedes the "+144% is flattered by a low Q1
FY26 base." Net: **not a new surviving bear thesis; a wording imprecision.** Advisory to A4:
relabel the sub-clause "understated QoQ vs Q4," not YoY.

**Positive claim 2 — "+38% NTI vs +22% gross income is the cleanest evidence of margin
expansion" (Step 2 answer 2).**
Bear counter from the same text: the NTI-outgrowth is substantially the **same IPO-cash
artifact** A4 flags for NIM — an equity-funded book (post-Feb-2026 IPO, L20/L36) means finance
cost grew far slower than income, mechanically widening NTI; it will compress as leverage
normalises 3.15x→4–4.5x (L88, L117). **Survives?** NO as an addition — A4 already carries the
IPO-inflation caveat prominently (Step 5L(4), Step 7A, QfM Q4, and the guidance-vs-delivery
read). The counter is present in the review, just not repeated at that one line. No graft
required; recommend cross-referencing the IPO caveat at answer 2 for symmetry.

**Positive claim 3 — "Ex-overlay credit cost ~3.68% comfortably below the top of the band;
conservative cross-cycle provisioning, quality positive" (Step 5L assessment 1).**
Bear counter from the same text: the 4.01% "top-of-band" print is a **management-chosen**
figure — mgmt states it "absorb[s] some of the profits into these overlays… because this is a
good year" (L39/L50), so future "improvement" could be **overlay release** not incurred-loss
decline; and the incurred number is unverifiable because **gross slippage was refused twice**
(L95, L117) while "reducing slippages" is simultaneously cited as a NIM tailwind (L117).
**Survives?** NO as an addition — A4 already states exactly this: tripwire #5 "GREEN but
mechanism discretionary… future improvement could be overlay release" (assessment 1), the
twice-deferred slippage is assessment 3 and QfM Q2/Q3, and the Asset-Quality Multiplier is
held at "provisionally Sound, do NOT upgrade." Counter is fully incorporated. No graft.

**Unverifiable-item honesty check (mandated):**
| Item | A4 treatment | Honest? |
|---|---|---|
| PCR | "ND on call (F17.1)"; tripwire #6 UNVERIFIABLE; 63.8% only as [prior-workup ref] | YES — not resolved |
| Gross slippage | "NOT REPORTED," twice-deferred (L95/L117); single cleanest Q2 metric | YES |
| Covenant resolution | "NOT MENTIONED, unraised" (F17.2); tripwire #7 UNVERIFIABLE | YES |
| Over-lending | "UNVERIFIABLE, not cleared" (F17.3); AUM/borrower & repeat share ND | YES |
| CRAR 41.3% vs 42.38% | carried to QfM Q13, "not silently reconciled" | YES |
| AUM 7,324 vs 7,384 | carried to QfM Q14 as live internal variant | YES |

All six are marked unverifiable/open rather than resolved. No tripwire is scored GREEN/RED
without a supporting A1 line: #1–#5 GREEN each carry an L8/L20/L39 cite; #6–#8 are explicitly
UNVERIFIABLE-THIS-CALL (silences), not falsely GREEN. Correct and conservative.

Adversarial verdict: **PASS** — no surviving bear counter that is both thesis-material and
absent from the review; the two positive claims with live counters already carry those
counters elsewhere in A4. Two advisory wording tightenings recommended (claim-1 QoQ/YoY label;
claim-2 IPO cross-ref), neither blocking.

---

## VERDICT: COMPLETE

- Coverage: every gated A2 row reviewed; all 16 A3 findings mapped to ≥1 management question;
  no orphan row, no missing-from-ledger row.
- Arithmetic: every derived metric ties to its A1 line within rounding; all unanchored
  implications correctly labelled.
- Adversarial: unverifiables honestly held open; no misread line; no unincorporated surviving
  bear counter.

Advisory (non-blocking, for A4 polish only, does not require a loop-back): (i) tag L53
"~780 crores" as reviewed transcription artifact; (ii) relabel the Step 2/Step 4 other-income
"understatement" as QoQ-vs-Q4, not YoY; (iii) note the ~Rs 6 Cr overlay-PAT add-back is
pre-tax; (iv) cross-reference the IPO-cash caveat at Step 2 answer 2. Only COMPLETE proceeds to
Notion save; these do not block save.

```yaml
stage: A5-adversary
company: "AYE"
quarter: "Q1 FY27"
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
