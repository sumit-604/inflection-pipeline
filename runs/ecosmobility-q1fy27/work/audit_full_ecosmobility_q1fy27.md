# A5 ADVERSARY / COMPLETENESS AUDIT — ECOSMOBILITY Q1 FY27 (MERGED REVIEW) — RE-AUDIT (loop 1)
## Target: review_full_ecosmobility_q1fy27.md (Role 4 + Role 5, results + press release + investor presentation)
## Auditor context: fresh. Re-derived independently from A1 extracts + A2 ledgers + the two verified supplements. This is the loop-1 re-audit after the three loop-0 fixes were applied as deterministic text edits (orchestrator, no A4 re-run because A4's agent hit an API failure mid-rewrite).

---

## LOOP-0 → LOOP-1 FIX VERIFICATION

**Fix 1 — GATING (F16-05 management-question row): LANDED, PASS.**
- Section 6 header updated: "UPDATED QUESTIONS FOR MANAGEMENT (8 carried forward + 5 new-doc rows)" (review L381).
- New row **13 (NEW)** present (review L399), `From finding = F16-05`, Cat E/C, asking about the >5yr-customer revenue-share drift 61%(FY25)→55%(FY26)→51%(Q1FY27): denominator dilution vs churn, net revenue retention on the >5yr cohort, and whether newer clients onboard at lower realisation. Text matches the finding and the source figures (deck FY25 61% / FY26 55%; PR Q1FY27 51%).
- Re-ran the full FORWARD-SIGNAL/AMBIGUOUS → question map (both forensics files):
  - Results FS: F2-02→Q1/Q2 · F6-01→Q4/Q8 · F13-01→Q4/Q5 · F13-03→Q5 · F15-01→Q3 ✓
  - Results AMBIGUOUS: F14-01→Q6 · F15-02→Q7 ✓
  - New FS: F6-01→Q4/Q8 · F7-01→Q10 · F13-01→Q5 · F16-01→Q10 · F16-03→Q9 ✓
  - New AMBIGUOUS: F1-01→Q7/Q12 · F8-01→Q11 · F16-02→Q1 · F16-04→Q9 · **F16-05→Q13 ✓ (was the sole gap; now closed)**
  - **Every FS/AMBIGUOUS finding now carries ≥1 question row. A4's §6 contract is now true.** The gating gap is resolved.

**Fix 2 — NON-GATING (asset-light REBUTTED → MITIGATED-PENDING): LANDED, PASS.**
- `grep -i REBUT` across the whole review = **zero matches**. No "REBUTTED"/"rebuts" closed-verdict wording remains anywhere (former §2c and flag mentions are all softened).
- MITIGATED-PENDING now consistent and each instance states the 5/95 GROUP mix eases-but-does-not-close (WOS gross block still undisclosed): thesis/moat dimension table (L373), net-read paragraph (L377), monitorable row (L415), §7.5 verdict (L430), plain-language brief §8.1 narrative ("largely eased, though not fully closed", L438) and §8.3 business-model ("MITIGATES-PENDING … eased, not closed", L447), closing YAML `tripwire_resolutions.resolved_to` (L489), and flags list (L521). (No separate VRIO/moat table exists in this review; the §5 weight-of-evidence dimension table is the moat-status carrier and is updated.)

**Fix 3 — NON-GATING (protocol-verdict / cash-conversion cap): LANDED, PASS.**
- New `## 7.5 PROTOCOL VERDICT` (L424-430) present. States PROCEED WITH FLAGS; confirms cash conversion is INDETERMINATE (no cash-flow statement in filing or deck; balance-sheet cash does NOT resolve it); confirms the CLAUDE.md rule that INDETERMINATE cash conversion caps the verdict no better than PROCEED WITH CAVEATS; states PROCEED WITH FLAGS is at least as conservative as PROCEED WITH CAVEATS on the severity ordering; names the missing cash-flow evidence (resolves FY26 AR / Q2 half-yearly); and states it does not silently resolve to a clean PROCEED. Correct and complete.

---

## REGRESSION SWEEP (edits must introduce no new arithmetic or coverage defect)

**Arithmetic — UNCHANGED, re-confirmed.** The three edits are text-only (a label swap, one added question row, one added verdict paragraph); no figure was touched. Re-verified from raw deck/filing numbers, all still tie with zero mismatch above rounding:
- Net cash: 241.88+69.86+1,060.79+4.26 = 1,376.79 Mn; −1.07 borrowings = 137.57 Cr ≈ ₹137.6 Cr ✓
- Debtor days: 365×1,070.21/8,081.58 = 48.3 ≈ 48 ✓
- Fresh provisions: (73.19+21.17)−(55.54+19.03) = 19.79 Mn = +₹1.98 Cr (<₹3 Cr) ✓
- Revenue-per-trip: (1.167/1.27)−1 = −8.1%; ₹1,428 vs ₹1,554 ✓
- 6-yr EBITDA-margin series (15.2/12.3/16.5/16.2/14.1/11.6%) and ROCE series (…42.9→29.4%) ✓
- Three-doc tie: Q1FY27 EBITDA 218.47/margin 10.34%/PAT 145.50 identical across filing, PR, deck ✓
- Reported EBITDA margin Q4FY26 = 13.43% ÷rev (277.71/2,067.60) — still resets any 3-Q sub-12% run; trigger NOT FIRED holds ✓

**Coverage — UNCHANGED / improved.** All 23 forensic findings still incorporated (YAML `a3_findings_incorporated` list intact). Question table now 13 rows (8 carried + 5 new); header count matches. No ledger row orphaned; nothing missing from ledger. Plain-language brief still 4/4 (narrative, sector, business-model, competition), provenance-labelled. "What the new docs add" (§2a-2d), Role 5 grade C (§3, L479), and the Step 7A claims-vs-evidence table all intact.

**Consistency — UNCHANGED.** Role 5 grade C (Mixed) unchanged; durable Management Grade held B; Promoter TRUSTWORTHY. Thesis-break trigger carried forward UNCHANGED — MEASURE-CONDITIONAL, NOT FIRED (L365/L477) — neither silently re-fired nor silently softened; softness still flagged prominently (actuals BELOW BEAR). Tripwire resolutions still correctly scoped to FY26 year-end basis. Cash conversion still INDETERMINATE, now additionally cap-confirmed in §7.5.

**YAML — parses.** Closing block (L459-530) is well-formed; the only changed values are `tripwire_resolutions` asset-light-drift → "MITIGATED-PENDING" and the flags-list asset-light entry. No structural breakage.

No new defect introduced by the edits.

---

## STANDING AUDIT RESULT (carried from loop 0, all still PASS)

- **Deliverable-completeness (hard gate):** plain-language brief 4/4 present and non-empty; "what new docs add" present; Role 5 credibility grade present; claims-vs-evidence table present. PASS.
- **Coverage:** independent grep pass (28 slides, 20 chart panels, balance-sheet totals incl. the benign FY25 ₹0.18 Mn cross-foot) reconciles to A2; all 23 findings incorporated; every FS/AMBIGUOUS finding now has ≥1 question. PASS.
- **Arithmetic:** every derived metric re-derived from raw numbers, zero mismatch above rounding. PASS.
- **Adversarial (the six task checks):** (1) Role 5 grade C defensible — PASS; (2) asset-light now MITIGATED-PENDING (was the one overstated label) — RESOLVED; (3) trigger carried forward unchanged, not re-fired/softened — PASS; (4) tripwire resolutions scoped to FY26 basis — PASS; (5) cash conversion INDETERMINATE, not silently resolved, now cap-confirmed — PASS; (6) no FS/AMBIGUOUS finding without a question — RESOLVED (F16-05→Q13).

The three surviving bear-counter items from loop 0 are now fully incorporated: the asset-light label is corrected to MITIGATED-PENDING, and the customer-stickiness-drift leg (F16-05) now carries its own management question in addition to its narrative/monitorable treatment.

---

## VERDICT

**COMPLETE.** All three loop-0 fixes landed correctly, the gating gap (F16-05 management-question row) is closed, and the deterministic edits introduced no arithmetic or coverage regression. The merged review is cleared to proceed to Notion save.

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
