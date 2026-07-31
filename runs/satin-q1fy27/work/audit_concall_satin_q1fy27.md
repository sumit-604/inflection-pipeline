# A5 ADVERSARY / COMPLETENESS AUDIT — SATIN Q1 FY27 CONCALL (ROLE 5)
# RE-AUDIT v2 — dated 2026-07-31
# Auditor: A5 (Opus 4.8), fresh context. Independence: re-derived from A1 extract +
# A2 ledger + A3 forensics only. Target: review_concall_satin_q1fy27.md (corrected).
# Prior audit returned INCOMPLETE for exactly two gaps; both re-verified below, then a
# full three-audit re-sweep to confirm no new error was introduced.

Target: `runs/satin-q1fy27/work/review_concall_satin_q1fy27.md`
Spine: `extract_concall_satin_q1fy27.txt` (333 ln) · `ledger_concall_satin_q1fy27.md`
       · `forensics_concall_satin_q1fy27.md`

---

## PART 0 — VERIFICATION OF THE TWO PRIOR-INCOMPLETE GAPS

### GAP 1 — Assam 44,000 vs 40,000 surfaced as flagged-unreconciled alongside A3-03 and A3-04

Independent grep confirms the raw fact: "44,000 borrowers" at A1 ln 133 (opening, Turn 2)
vs "40,000 odd customers" at A1 ln 248 (Q&A, Turn 6). Same Assam fact, same call, two counts
= A3-07 (NEUTRAL-FACT, forensics §2).

The corrected review now surfaces it in THREE places and — critically — *alongside* the two
ratio inconsistencies, as required:

- **Step 1, "Internal contradictions in the opening" (review ln 152-159):** lists all three
  as one flagged-not-resolved cluster — adjusted ROA **4.34% (ln135) vs 4.28% (ln193)** = A3-03;
  NIM **14.66% (ln122) vs 14.36% (ln282)** = A3-04; Assam **44,000 (ln133) vs 40,000 (ln248)**
  = A3-07. Verbatim: "All three are flagged-not-resolved (same treatment)."
- **Step 6D (review ln 480):** "note the 44,000 vs 40,000 count inconsistency, A3-07, immaterial
  to the ~1% net read but logged."
- **Step 7A table (review ln 517):** row "Assam borrowers '44,000' (opening) vs '40,000' (Q&A)
  ... UNRECONCILED, immaterial (net ~1% either way; A3-07)."
- **YAML flags (review ln 885):** explicit flag carrying both counts, both line cites,
  "unreconciled", and the immaterial-but-logged treatment.

Cross-check against my independent line cites: 4.34%→ln135, 4.28%→ln193, 14.66%→ln122,
14.36%→ln282, 44,000→ln133, 40,000→ln248 — every cite exact. All three treated identically as
flagged-unreconciled (not silently resolved). **GAP 1 = FIXED.**

### GAP 2 — Answered-vs-open tally reconciles to 13 with Q11 counted once

Step 3E-detail table (review ln 269-289) assigns one status per Role-4 question Q1-Q13.
Independent re-tally of the table rows:

| Status | Questions | Count |
|---|---|---|
| ANSWERED | Q2, Q8 | 2 |
| PARTIAL | Q1, Q3, Q4, Q6, Q10 | 5 |
| EVADED | Q5 | 1 |
| NOT ADDRESSED | Q7, Q9, Q11, Q12, Q13 | 5 |
| **Total** | | **13** |

2 + 5 + 1 + 5 = 13, matching the 13 Role-4 questions. Q11 (consol ROE) appears exactly once —
NOT ADDRESSED — with rationale stated (ln 286-289): "consol ROE was neither asked nor
volunteered." No double-count (the prior fault was Q11 tallied twice). Prose summary (ln 285-289),
YAML `answered_vs_open_summary`, and `tally_check: "answered 2 + partial 5 + evaded 1 +
not_addressed 5 = 13"` (review ln 847-852) all match the table and each other. **GAP 2 = FIXED.**

---

## PART 1 — COVERAGE AUDIT (fresh grep vs A2, then A2/A3 → A4)

| Category | A2 count | My fresh count | Method / evidence | Orphan | Status |
|---|---|---|---|---|---|
| Speaker turns | 12 | 12 | T1 op(95), T2 CMD(102), T3 op(175), T4-10 = 7 analyst turns, T11 close(321), T12 end(332) | none | PASS |
| Analyst turns | 7 | 7 | grep "question from the line of" = ln 177,220,244,256,275,291,298 (exactly 7) | none | PASS |
| Participants | 11 | 11 | 2 mgmt (HP Singh, Aditi Singh) + Pratik Mudkar + Operator + 7 analysts; A2 re-sweep 10→11 documented, carried | none | PASS |
| Analyst questions | 20 | 20 (accepted) | A2 C.1-C.20 dual-method; my read finds no 21st, no dropped sub-question | none | PASS |
| Spoken numbers | 194 | 194 (accepted) | 120 Turn-2 + 74 Q&A; A2 re-sweep 186→194 (3 wrap-split + word-form) documented | none | PASS |
| Guidance-fwd | 15 | 15 | Section E G.1-G.15 → Step 2L / A3 register | none | PASS |
| A3 findings | 19 | 19 | A3-01…A3-19 all incorporated (review ln 39-41) | none | PASS |

**Ledger-row → A4 traceability.** Every A2/A3 row is cited in the review or carried as reviewed.
High-load rows spot-verified against A1 lines (all exact): consol PAT 123/+172% (ln121), std PAT
120/+182% (ln121-122), consol AUM 15,935/+27% (ln118), GNPA 2.2%/2.18% (ln125-126), credit cost
3.06% + overlay 36 + ex-overlay 1.97% (ln128-129), ROA 3.55%/ROE 15.10% (ln125,135), slippage
49/write-off 127 (ln228), Q4 slippage 90 (ln315), ECB 1,573/100% hedged/net -3 (ln301-306), DA
94/20-22% (ln221-223), CRAR 26.74%←25.39% (ln155), promoter 100 Cr @17% (ln157), on-book prov
250 vs 152 (ln138), 2030 AUM 32,000 (ln163), consol ROA 3.3% (ln229), steady NIM 14.35-14.50%
(ln283), stable credit cost 2.5-3.0% (ln204), guidance 20-25%/18,200-18,900 (ln159), CGFMU
pre-tied GNPA 3.5-4% (ln293-294).

Both A2 NOT-FOUND items carried unresolved in the preamble (review ln 43-46): yr-ago NNPA "9%"
(ln126, A3-06) and new-branch breakeven unit "91" (ln289) — not asserted as fact.

**Peer cross-check omission disclosed?** YES — Step 7B (review ln 526-534): "No peer NBFC-MFI
concall was supplied ... within the +/-4-week window ... deferred and stated explicitly," flagged
to the orchestrator; mirrored in YAML flags (ln 887). Complies with the protocol rule.

**COVERAGE: PASS. orphan_rows: none. missing_from_ledger: none.**

---

## PART 2 — ARITHMETIC / FIDELITY AUDIT (recompute every derived figure)

Concall layer; Role-4 filing metrics (EBITDA, ETR, PAT bridge) correctly not re-litigated
(cross-referenced to the A5-COMPLETE Role 4). Derived quantities inside Role 5, recomputed raw:

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| 3E status tally | 2+5+1+5 = 13 | 2+5+1+5 = 13 | Step 3E table | PASS |
| Response-quality tally | A9/B8/C2/D1/E0 = 20 | A9 (C.20 A/B→A), B8, C2 (C.10,C.15), D1 (C.1), E0 = 20 | Step 4A | PASS |
| Specificity ratio | ~10/16 ≈ 0.63 | 10/16 = 0.625 ≈ 0.63 | Step 6B | PASS |
| Defensive-language count | ~7 (>5 hedge-heavy) | 7 distinct (conservative-refrain = 1) | Step 6C | PASS |
| Consol PAT over standalone | Rs 3 Cr | 123 − 120 = 3 | ln121-122 | PASS |
| Consol−standalone income gap | Rs 93 Cr | 827 − 734 = 93 | ln121 | PASS |
| Write-off vs slippage | 127 > 49 | 127 > 49 | ln228 | PASS |
| Single-quarter delivery | 5.0/5 = 100% | 5 in-band, consol-ROE excluded (no commitment) | Step 3A/3B | PASS |
| Reported vs ex-overlay credit cost | 3.06% vs 1.97% | both spoken, overlay 36 Cr | ln128-129 | PASS |

**Fidelity.** (i) Every cited concall number ties to an A1 line via the garble ledger — verified
by independent grep for 4.34/4.28/14.66/14.36/127K/49K/1573cr (all at cited lines). (ii) No garble
asserted as fact: "38 cr"→Rs 3,008 Cr, "127 K"→Rs 127 Cr, yr-ago NNPA "9%" and breakeven-unit
"91" carried as garble/NOT-FOUND, not truth (review ln 47-51, 43-46). (iii) Internal
inconsistencies (A3-03 ROA, A3-04 NIM, A3-05 overlay 20 vs 21, A3-07 Assam count) flagged-not-
resolved, never silently reconciled.

One observation (NOT a fail): management's spoken "20-25% implying 18,200-18,900 Cr" (ln159) does
not arithmetically close off the Rs 15,935 Cr consol base (20% → ~19,122). The review faithfully
quotes it as management's *own* implied band ("implies", Step 2L), does not adopt it as an
A4-derived figure, and does not assert the math is correct. Correct conservative handling — a
management inconsistency appropriately transcribed, not an A4 arithmetic error.

**ARITHMETIC: PASS. arithmetic_mismatches: none above rounding.**

---

## PART 3 — ADVERSARIAL READ (three most positive claims, strongest bear from same text)

**Claim 1 — "100% within-band delivery; credibility Grade B; COMMITTED & CREDIBLE archetype."**
Bear (same text): 100% only on the metrics management *chose* to guide; consol ROE, overlay
ceiling, Stage-2, GNPA trajectory withheld — "guide-what-you-can-beat." *Already incorporated:*
Step 3 caveat (ln 235-240), 3C (ln 242-246), 6E boundary watch-items, YAML flags. **Does not
survive as new — already grafted.**

**Claim 2 — "Slippages halved 90→49; genuine asset-quality improvement; strongest Q1 in 8 years."**
Bear (same text): the Rs 127 Cr write-off (> Rs 49 Cr slippage) mechanically drove the 90 bps
GNPA fall by management's own words (ln 317); part of the "improvement" is loans removed, not
recovered; reported credit cost/ROA stay overlay-discretionary (number declined, ln 183).
*Already incorporated:* Step 8.5 cap re-test ("PARTIALLY LIFTS but HOLDS"), 7A narrative-vs-
mechanism tension (ln 519-524), plain-language "the catch," YAML flags. **Does not survive as
new — already grafted.**

**Claim 3 — "ECB Rs 1,573 Cr 100% hedged, net −Rs 3 Cr — FX risk resolved GREEN."**
Bear (same text): "100% hedged" is a single-management-voice assertion (no CFO; flag
SINGLE_MGMT_VOICE) with no hedge-documentation note; the MTM-in-income vs forex-in-finance-cost
period mismatch keeps the P&L line volatile quarter to quarter even if the net is small; R4 FND-04
flagged the hedge claim as footnote-asserted with no note. *Already incorporated:* review logs it
as concall-only (ln 513), notes the period mismatch (Step 3E Q8, ln 278), carries SINGLE_MGMT_VOICE
(Step 0B) and the deferred external cross-check (7C). **Does not survive as new — already grafted.**

No surviving bear counter requires grafting into A4. **ADVERSARIAL: PASS.**

---

## PART 4 — ADVERSARIAL CHECKS ON THE VERDICT ITSELF (not manufacturing a gap)

- Credibility Grade **B** — defensible: 17/20 Q&A at A/B, promoter fields all Q&A, one hard
  evasion (overlay number), provisional (first tracked call). Supported by the extract.
- INDETERMINATE cap **HOLDS** — correct per CLAUDE.md ("never let INDETERMINATE cash conversion
  silently resolve to PROCEED"); the two decisive items (ARC-vs-organic split of Rs 127 Cr,
  Stage-2 book) stay undisclosed, so the cap cannot clear. Properly conservative.
- Verdict **PROCEED WITH CAVEATS** — in the permitted set; no STOP invented; HELD, unchanged.
- Decision Status **flagged-not-decided** — WATCHLIST/BUY unchanged, "A4 flags, human decides,"
  no pre-committed trigger fired. Correct.
- Plain-language summary (10-12 lines, rounded numbers, one-line verdict) and SECTOR KNOWLEDGE
  (append to sectors/NBFC-MFI.md) — both present and compliant.

Nothing here forces a re-open. Both prior gaps are genuinely closed and the re-sweep introduced
no new coverage, arithmetic, or fidelity error; I am not manufacturing a gap to avoid closing.

---

## VERDICT

**COMPLETE.** Both prior-INCOMPLETE gaps are fixed (Assam 44,000/40,000 now flagged-unreconciled
alongside A3-03 and A3-04; answered-vs-open tally reconciles to 13 with Q11 counted once). The
full re-audit passes on all three axes — coverage (12 turns / 20 questions / 194 numbers / 7
analysts all accounted, peer omission disclosed), arithmetic/fidelity (every cited number ties to
an A1 line, no garble asserted as fact, inconsistencies flagged not resolved), and adversarial
(all three bear counters already incorporated; Grade B, cap-HOLDS, PROCEED-set verdict, Decision
Status flagged, plain-language + sector blocks present). No orphan rows, no arithmetic mismatch,
no surviving un-grafted bear counter. Cleared to proceed to Notion save.

```yaml
stage: A5-adversary
company: "SATIN"
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
