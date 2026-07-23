# A5 ADVERSARY / COMPLETENESS AUDIT (RE-AUDIT R2) — Ksolves India Limited — Q1 FY27

Artifact under audit: `review_ksolves_q1fy27.md` (A4 ANALYST, revised in place 2026-07-23)
Independent evidence: `extract_concall_ksolves_q1fy27.txt` (A1), `ledger_concall_ksolves_q1fy27.md` (A2)
Auditor: A5 (Opus 4.8). Fresh context; A3 reasoning not consulted; all grafts re-verified against the A1 extract, not against the revision's own claims.

Prior verdict (R1): INCOMPLETE -> A4, two blocking gaps. This R2 re-audit confirms closure and checks for regression.

---

## 1. RE-VERIFICATION OF THE TWO R1 BLOCKING GAPS

### Gap 1 — Margin-durability caveat. CLOSED.
A4 added a dedicated caveat (review L64) and threaded it through every place the 30.3% / +389bps margin is framed: Step 1 item 5, Step 2 margin row, Step 3A, 5A, 6A ("MAINTAINED (qualified)"), 7A, 8A ("FIRED but QUALIFIED"), 8B item 1 ("GREEN (quality-flagged)"), 8C floor note, 8D pillar note, the 8C-metric, and the Combined Verdict.

Cite audit against the raw extract (re-derived, not trusted):
- **L245** — extract reads "the impact was largely offset through operating efficiencies and the trimming of discretionary spends." A4's "cost-out / discretionary-spend cuts" is faithful. OK
- **L388** — extract reads "Margins will not be impacted. The reason is that we are not hiring... largely, we are hiring only on a requirement basis." Supports "not operating leverage." OK
- **L516-520** — extract: "when people are leaving, we are not stopping them, until and unless they have exceptional quality." Supports "non-replacement of exits." OK
- **L155** — revenue "sequentially moderated by 3.7%" supports "flat-to-down revenue." OK
- Filing-unverifiability: Section 7A now explicitly extends UNVERIFIABLE to the EBITDA/margin line. OK

Bull-bear symmetry now present: the Combined Verdict (review L422-424) carries an explicit split Bull list and Bear list, with the cost-out margin sitting in the Bear column. Monitorables now include a dedicated "Margin QUALITY (cost-out vs operating leverage)" row (review L399, L483) and Q-18 tests it directly. The caveat is reflected in symmetry and monitorables as required. **Gap 1 genuinely closed against the evidence spine.**

### Gap 2 — "Explicitly and early" contradiction. CLOSED.
The word "early" is removed from Step 3B. The revised Step 3B (review L165) states the withdrawal was in prepared remarks (L181-183) but the quantified downgrade "was NOT proactively stated there... emerged only late in Q&A under analyst pushing on trajectory (turns 62-64, L694-716; L744-745)," grading it "SOFT / tempered B... candid-when-pushed, not proactively transparent." Step 1(c), 6D, 6E (now "boundary-adjacent to EVASIVE"), and the Concall Verdict block are all consistent with this.

Cite audit against the raw extract:
- **L181-183** — prepared remarks read only "it would not be prudent for us to reaffirm the revenue guidance for the current financial year at this stage" — NO number attached. A4's "withdrawal flagged, magnitude not stated proactively" is correct. OK
- **Turns 62/64 = L694 / L715** — the 18-20% magnitude appears at L694-698 ("As I said in the last con call, we will try to maintain, year on year, 18% to 20%") and L715-716 ("my plan was that this year, again, I would give 18% to 20%. In the last call, I said so"). Both are in Q&A/closing, after opening remarks ended (~L282). OK
- **L744-745** — "+4-5% ... maximum" is in the closing summary (turn 70), not prepared remarks. OK

The credibility read is now internally consistent (Step 3B no longer contradicts Step 1c) and no longer more confident than the evidence allows. **Gap 2 genuinely closed against the evidence spine.**

---

## 2. REGRESSION CHECK — nothing that previously passed has broken

**Coverage (74 / 17 / 34):** Preamble (review L15-20) unchanged: 74 turns, 17 questions, 34 rows, roster 5, hedges 10 — matches my R1 independent grep pass (per-speaker sum 30+16+9+5+5+5+4+0 = 74; 17 questions on turns 7/14/16/18/22/24/28/32/34/36/38/40/43/47/50/57/65). Q&A inventory (Step 4A) still lists exactly Q1-Q17. No ledger row dropped; no orphan introduced. PASS.

**Every forward-signal / ambiguous finding still carries a management question:** re-mapped the FN->Q table (review L367-386). FN-01->Q-03, FN-02->Q-04, FN-04->Q-07, FN-05->Q-08, FN-06->Q-06, FN-07->Q-11, FN-10->Q-10, FN-12->Q-05, FN-13->Q-01, FN-14->Q-02 (forward); FN-08->Q-12, FN-09->Q-09, FN-11->Q-13, FN-16->Q-14 (ambiguous); FN-15->Q-15/16/17. All 14 + FN-15 still covered; the new Q-18 (margin-durability, A5 graft) is an addition, not a substitution. No question removed. PASS.

**Arithmetic:** the A1 table (review L40-62) and derived-priors block (L66) are byte-identical to R1 — all previously reconciled cells (EBITDA margin 12.56/41.4=30.34%; PAT margin 9.21/41.4=22.25%; EPS 3.88/2.71=+43.2%; implied priors 37.6/43.0/9.95/6.43 and their 26.4%/17.1% cross-checks) still hold. The revision's NEW numbers all reconcile:

| New metric (dividend quant, review L68/L249) | A4 value | My recompute | Status |
|---|---|---|---|
| Implied shares | ~2.37 cr | 9.21 / 3.88 = 2.374 cr | RECONCILES |
| Interim dividend outflow | ~Rs9.5 cr | 4 x 2.374 = 9.50 cr | RECONCILES |
| Payout vs Q1 EPS | ~103% | 4.00 / 3.88 = 103.1% | RECONCILES |
| Payout vs cash | ~56% | 9.5 / 17 = 55.9% | RECONCILES |
| Annualised payout | ~26% | 9.5 / (9.21x4=36.84) = 25.8% | RECONCILES |

No arithmetic mismatch above rounding; no new arithmetic error introduced. A4 correctly downgraded the dividend to "routine ~26% payout" — consistent with my R1 finding that the dividend bear counter does not survive once annualised. PASS.

**INDETERMINATE cash cap:** Section A5 (review L84) unchanged; Combined Verdict (L428, L430) still caps at no better than PROCEED WITH CAVEATS with the five missing evidence items named (CFO, CFO/PAT, DSO, CCC, promoter pledge); protocol verdict PROCEED WITH FLAGS honours the cap. PASS.

**Tripwire logic:** Step 8C (review L338-347) intact — tripwire (a) NOT FIRED (Q2 unavailable), (b) NOT FIRED (2 of 3), full-exit promoter-sale/DSO NOT FIRED but UNVERIFIED (silence cannot clear a full-exit trigger), margin floor NOT FIRED (30.3% vs 28%). The added note that the 28% cushion is cost-out-dependent is a conservative refinement, not a logic change. No tripwire fired; Decision Status unchanged (HELD 2.5%, branch 8A). PASS.

**Advisory (A2 anecdote L529-531):** A4 logged it in the preamble (L25) and flags (L512) as an unremediated A2/A3 enumeration note with no thesis impact. Correctly routed as advisory, non-blocking. Carried forward, not a gate item.

---

## 3. ADVERSARIAL RE-READ (R2)

The two R1 surviving counters are now grafted (Gap 1, Gap 2 above) with bull-bear symmetry restored in the Combined Verdict. The third R1 candidate (dividend) was assessed non-surviving in R1 and A4 has now quantified and correctly framed it as routine — no residual one-sidedness. Re-scanning the revised review for any newly introduced over-confidence: none found. The margin is now consistently a QUALIFIED positive; credibility is SOFT B / boundary-adjacent; the catalyst remains unquantified; every headline positive carries its bear counter. No new surviving bear counter.

---

## 4. VERDICT

**COMPLETE.** Both R1 blocking gaps are closed against the primary evidence spine (Gap 1 margin-durability caveat: cites L245/L388/L516-520 verified, reflected in bull-bear symmetry and monitorables; Gap 2 "early" removed and made consistent with L181-183 prepared-remarks silence vs turns 62-64 / L694-716 late-Q&A disclosure). No regression: coverage 74/17/34 intact, all forward-signal/ambiguous findings still carry a management question (Q-18 added, none removed), all arithmetic reconciles including the new dividend math, the INDETERMINATE cash-conversion cap is honoured, and the tripwire logic is sound with no tripwire fired. Cleared to proceed to Notion save.

```yaml
stage: A5-adversary
company: "ksolves"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger:
    - "L529-531 spoken anecdote numbers (~9-month estimate; team ~14-15) absent from A2 §5; non-thesis, logged advisory to A2, non-blocking"
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
