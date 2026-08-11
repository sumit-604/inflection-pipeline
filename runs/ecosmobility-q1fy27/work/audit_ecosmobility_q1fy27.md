# A5 ADVERSARY / COMPLETENESS AUDIT — ECOSMOBILITY Q1 FY27 (RE-AUDIT, loop 1)
## Target: review_ecosmobility_q1fy27.md (A4 ANALYST, revised in place) | Auditor: A5, fresh context
## Inputs: A4 review (revised), A1 extract spine, A2 ledger, VERIFIED FIGURES SUPPLEMENT. A3 reasoning NOT seen — all cites re-derived.

This re-audit tests ONLY whether the single INCOMPLETE finding from loop 0 is resolved, plus a defect-scan of the revision. The loop-0 coverage sweep (no orphan rows, no missing-from-ledger), arithmetic sweep (every derived metric within rounding), deliverable gate (all four brief parts present), and adversarial checks (profitless-growth bridge supported; INDETERMINATE cash cap correctly applied; no zero-lines/board-items dropped) all PASSED and are not re-run except where the revision touched them.

---

## LOOP-0 FINDING (the one INCOMPLETE)
A4's prominent verdict "Pre-committed thesis-break trigger FORMALLY FIRED" + 8A-W "WATCHLIST → AVOID" mapping was **not defensible on the trigger's pre-committed measure** (consolidated REPORTED EBITDA margin sub-12% for 3 consecutive quarters), because Q4 FY26 reported EBITDA margin (13.43% ÷rev / 13.20% ÷total income) is above 12% and breaks any 3-quarter run, so Q1 FY27 is at most a single borderline sub-12% quarter (11.90% total-income only; 12.11% rev-from-ops above 12%). Loop back → A4.

---

## VERIFICATION OF THE SEVEN CLAIMED FIXES (checked against the file, not A4's word)

| # | Claimed fix | File evidence | Internally consistent? | Verdict |
|---|-------------|---------------|------------------------|---------|
| 1 | Trigger restated MEASURE-CONDITIONAL, headline "NOT FIRED on literal reported measure" | Step 6C heading L327; table FIRED? = "NO on the literal measure" L325; L342 "(a) … has NOT formally fired"; Step 1C reported-margin rows shaded/flagged L109, L119-121, L133 | Q4 FY26 reported 13.43%/13.20% in L120-121 matches the 13.43%/13.20% cited in the 6C verdict table L334 | RESOLVED |
| 2 | "Already crossed at Q4 FY26" framing withdrawn | L337 verbatim: "The earlier draft's framing that the threshold was 'already crossed at Q4 FY26' is withdrawn — it is contradicted by the Q4 FY26 reported EBITDA margin in this review's own Step 1 table." | Yes | RESOLVED |
| 3 | Operating-EBITDA reading kept as flagged possibility on unverifiable Q2/Q3 baselines | L339: operating 10.34% "WOULD be consistent with 'fired' — BUT … requires Q2/Q3 FY26 operating baselines that are NOT in this filing … a possibility, not a verified fact." | Consistent with Step 3 Q2/Q3 rows = ND (L194-195) | RESOLVED |
| 4 | Decision Status held WATCHLIST/HOLD-NOT-ADD; no AVOID asserted | L345, Step 8 L385 ("This branch does NOT apply. No AVOID reclassification is forced"), L387; YAML decision_status L499, thesis_break_trigger L501, flags L527 | 8A-W first branch correctly gated OFF; below-bear branch (separate rule) still fires the projection-downgrade only | RESOLVED |
| 5 | QfM row added on reported-vs-operating basis | New Q2 at L412 (from F2-02): asks REPORTED vs OPERATING basis and rev-from-ops vs total-income denominator; table now 8 rows; top-3 re-ranked (L420-424); "all eight questions" L426; YAML L509 | Row maps to a real finding (F2-02) and to the exact ambiguity that gates the decision | RESOLVED |
| 6 | "60 Cr shares" → 6 Cr | L39 "6.00 Cr shares", L50 "~₹14.28 Cr on 6 Cr shares", L57 "(6 Cr shares)", L441, YAML L522 | ₹14.28 Cr = ₹2.38 × 6 Cr ✓ (120 mn ÷ ₹2 FV = 60 mn = 6 Cr shares) | RESOLVED |
| 7 | Sign-flipped "S–C PAT gap" label corrected | L247 defines "Consolidated minus Standalone (positive = consolidated above standalone)"; L253 row relabeled "Consol − Standalone PAT gap"; L258 narrative aligned | Values unchanged (+0.023 / −0.244 / +0.151 / +0.372) and now match the stated sign convention | RESOLVED |

**All seven fixes verified present and internally consistent with the review's own figures.** The core correction — the headline no longer asserts the trigger fired, the literal reported measure is shown NOT to meet the 3-quarter condition (Q4 FY26 13.43% resets the run), and the operating reading is explicitly labelled unverifiable — is exactly the graft the loop-0 audit required. Crucially, margin weakness is preserved and stated plainly (L343 "MARGINS ARE GENUINELY SOFT"), so the correction narrows only the FORMAL trigger status, not the bear read.

---

## DEFECT-SCAN OF THE REVISION (did the edit introduce a new arithmetic or coverage error?)

| Revision touchpoint | Check | Status |
|---------------------|-------|--------|
| New Step 2B row: reported EBITDA margin YoY 13.65%→12.11% = −154 bps (L162) | 13.65 − 12.11 = 1.54 pp | CORRECT |
| Step 2C dx2 reported margin −154 bps (L175) | matches above | CORRECT |
| Step 1C reported-margin rows unchanged (L119-121): consol 13.65 / 13.43 / 12.11 (÷rev); 13.44 / 13.20 / 11.90 (÷total inc) | 27.771/206.760=13.43%; 27.771/210.378=13.20%; 25.596/215.120=11.90%; 25.596/211.372=12.11% | CORRECT |
| Step 3 trajectory adds reported-margin column 13.65 / 13.43 / 12.11 (L193-197) | matches Step 1C | CONSISTENT |
| Watchlist item 1 now AMBER, red threshold "reported <12% ×3Q", reading notes Q4 FY26 13.43% resets run (L313) | consistent with 6C | CONSISTENT |
| Step 6D margin-recovery trigger "BROKEN-AS-WRITTEN … formal break-trigger NOT fired on literal reported measure" (L351) | consistent | CONSISTENT |
| Step 8C single cleanest metric switched to REPORTED EBITDA margin with operating shown alongside (L397-399) | aligns with trigger being written on reported | CONSISTENT |
| Coverage: QfM 7→8 rows; all 11 A3 findings still incorporated (YAML L496); board-outcome items 1-5, annexures, notes, zero-lines all still present | no rows dropped; the added row is additive | NO COVERAGE REGRESSION |
| Deliverable gate: PLAIN-LANGUAGE BRIEF (L460) narrative rewritten to two-part honest read; sector/business-model/competition blocks intact and provenance-labelled (L466-480) | all four parts present, non-empty | GATE STILL PASS |
| INDETERMINATE cash cap unchanged (L284, Flag 3) | still named, not silently PROCEED; verdict PROCEED WITH FLAGS honors the CAVEATS ceiling | STILL COMPLIANT |

No new arithmetic mismatch, no coverage regression, no deliverable-gate breakage. The two cosmetic loop-0 notes are both fixed.

---

## VERDICT

**COMPLETE.**

The single loop-0 INCOMPLETE finding is fully resolved. A4's headline trigger verdict now reads NOT-FIRED-on-the-literal-reported-measure, is internally consistent with the review's own Q4 FY26 reported EBITDA margin (13.43% ÷rev / 13.20% ÷total income) that breaks the 3-quarter run, keeps the operating-EBITDA "fired" reading only as an explicitly unverifiable possibility, holds Decision Status at WATCHLIST / HOLD-NOT-ADD with no AVOID asserted, adds a Questions-for-Management row on the reported-vs-operating basis, and corrects both cosmetic errors (6 Cr shares; Consol−Standalone gap label). Margin softness is preserved as a prominent, separately stated flag. The revision introduced no new arithmetic or coverage defect. This review proceeds to Notion save.

```yaml
stage: A5-adversary
company: "ECOSMOBILITY"
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
