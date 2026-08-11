# A5 ADVERSARY / COMPLETENESS AUDIT — DIVGI TORQTRANSFER, Q1 FY27
# Model: Opus 4.8 | Fresh context: A4 review + A1 extracts + A2 ledgers only.
# Independent re-derivation. I do not defer to A3/A4 cites; I check them.
# Two passes: PASS 1 (initial audit) found one arithmetic mismatch; PASS 2 (re-audit
# after A4 remediation) confirms the fix and issues the final verdict.

Review under audit: `review_divgi_q1fy27.md`
Evidence spine: `extract_results_*`, `extract_presentation_*`, `ledger_results_*`, `ledger_presentation_*`.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF present as a labelled final section (review lines 364-396). All four parts present, non-placeholder:

| Brief part | Location | Present? |
|---|---|---|
| 1. Summary narrative | L366-370 | PRESENT (~15 lines, numbers-first, bull + three tempering items) |
| 2. SECTOR intelligence | L372-378 | PRESENT (provenance-labelled) |
| 3. BUSINESS-MODEL intelligence | L380-387 | PRESENT (provenance-labelled) |
| 4. COMPETITION intelligence | L389-396 | PRESENT (provenance-labelled) |

Gate 0 result: PASS.

---

## AUDIT 1 — COVERAGE (fresh grep pass diffed against A2 ledgers)

| Category | A2 count | My fresh count | Orphan/missing | Status |
|---|---|---|---|---|
| Results notes | 7 | 7 | none | PASS |
| Board agenda items | 5 | 5 | none | PASS |
| Annexure I rows | 4 | 4 | none | PASS |
| Auditor paras | 4 | 4 | none | PASS |
| P&L line-item rows | 29 | 29 | none | PASS |
| Entities | 2 | 2 | none | PASS |
| Signatory blocks | 4 | 4 | none | PASS |
| Zero-standing (results) | 1 | 1 | none | PASS |
| Presentation slides | 41 | 41 | none | PASS |

Every ledgered disclosure unit addressed in A4 (7 notes individually in Step 0D; 5 agenda items — 1/2/4/5 individually, 3 Scrutinizer carried as routine no-finding by the 5-item reconciliation; 4 annexure rows; 4 auditor paras with affirmative absence of EoM/Other-Matters/Going-Concern; 29 P&L rows incl. acknowledged zero-standing Other-equity; 2 entities + Note 7; all 41 slides, quantitative ones cited, descriptive ones carried by the 41-slide reconciliation). No orphan rows; nothing my fresh pass found is missing from the ledger.

STANDALONE-ONLY stated plainly (L30), `sc_gap_pat_pct = ND` — no invented gap. FIRST-COVERAGE stated plainly (L7/L40/L255) — no invented prior Decision Status. Correct.

COVERAGE result: PASS.

---

## AUDIT 2 — ARITHMETIC (independent re-foot from raw extract line values)

Units: results filing ₹ million (L248) ×0.1 → Cr; presentation ₹ Cr ×1.

### Headline P&L + derived metrics — all re-foot exactly
Revenue Q1FY27 137.14 (1,371.42m); PBT 33.75 (337.51m); PAT 25.24 (252.40m); EPS 8.25.
Op EBITDA 37.02, margin 27.0% (37.02/137.14=26.99%); Rep EBITDA 41.64; core PBT ex-OI 29.13; OI/PBT 13.7%; ETR 25.2% (8.51/33.75); PAT margin 18.4%.
YoY: revenue +91.3% (65.46/71.68); Op EBITDA margin +746 bps (26.99−19.53; review's 745 within rounding band); core PBT ex-OI +316.7%; PBT +179.4%; PAT +182.6%; EPS +182.5%.
QoQ: revenue +27.4%; core PBT ex-OI +107.6%; PAT +63.0%.
PAT bridge closes: +22.14 − 0.47 − 5.36 = +16.31 = 25.24−8.93. PASS.
Cash: CFO/PAT FY26 0.88x (41.1/46.9); inventory +51.9%; receivables +42.9%; payables +49.1%; net cash 232.6; IPO capex 60.7% (915.27/1,507.07); dividend ₹10.0 Cr (3.27×30.582m sh). PASS.

### A3 corrections — all applied and independently verified
FY26 Δ-inventories (80.76) not (807.60): footing 1,448.73−80.76+415.41+3.10+292.37+1,045.37 = 3,124.22m = printed total (L268). EPS Mar-26 5.06. Deferred-tax series −0.65/−17.43/4.11/−1.21. Slide 35 PAT (ties slide-38 table), slide 37 cash-reserve reorder, slide 11 mix (TC 53/Comp 24/Others 18/EGD 4) — all applied. PASS.

### PASS-1 mismatch — NOW REMEDIATED (re-audit)
PASS 1 flagged: Step 7 "ROCE base" cell stated RoCE FY24 = 12.5%, whereas slide 37 (extract L1176-1185, RoCE FY21-FY26 = 17.8/18.3/12.5/9.3/5.6/9.9) gives FY24 = 9.3% (12.5% is FY23). 3.2 pp mismatch above rounding. Loop-back to A4.

RE-AUDIT of the remediated review (review L243):
> "RoCE trajectory FY23 12.5% → FY24 9.3% → FY25 5.6% → FY26 9.9% (recovering off a trough) | slide 37 L1178-1185"

Verification against extract slide 37 (L1176-1185): FY23 12.5% ✓, FY24 9.3% ✓, FY25 5.6% ✓ (trough), FY26 9.9% ✓. Source citation updated to L1178-1185, correct. The corrected cell now matches the source exactly. MISMATCH CLEARED.

Surgical-edit confirmation (no side effects):
- Only the Step 7 "ROCE base" cell (L243) changed. The only other "12.5%" in the file is the unrelated Q1FY26 PAT-margin cell (L104, intact); "9.3%" now appears only at the corrected cell (the three "−9.3%" Other-Income items at L120/L129/L167 are unrelated and unchanged).
- Derived-metrics table (L92-104) unchanged and re-foots identically to PASS 1.
- Questions-for-management table (Step 8.5) and Coverage Map (L400-418) unchanged: 13/13 findings still mapped (A3-F2→Q2, A3-F6a→Q2, A3-F6b→Q5, A3-F13a→Q11, A3-F13b→Q12, A3-F15→Q1/Q13, A3-01→Q4, A3-02→Q8/Q9/Q10, A3-03→Q8, A3-04→Q4, A3-05→Q1/Q3, A3-06→Q6, A3-07→Q7).
- Standalone-only + first-coverage framing (L7/L30/L40/L255), sc_gap_pat_pct = ND (L439), protocol_verdict PROCEED WITH CAVEATS (L435), and the four plain-language-brief headers (L366/372/380/389) all intact.
- Closing A4 YAML block unchanged.

ARITHMETIC result: PASS. All headline P&L, margins, tax rate, YoY/QoQ, PAT bridge, and cash metrics re-foot exactly; all A3 corrections applied; the sole PASS-1 mismatch is remediated and verified; the fix was surgical with no collateral change.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear counter from the SAME extract)

Findings-to-questions: 13/13 AMBIGUOUS/FORWARD-SIGNAL findings map to ≥1 existing question (Coverage Map + Step 8.5 verified). PASS.

1. "Revenue +91.3% YoY, Op EBITDA margin +745 bps, growth operational not treasury." Bear: low single-quarter Q1FY26 base + Note-6 balancing QoQ base + 27.0% is a single-quarter margin high. SURVIVES? No — review flags the balancing caveat, fresh-baseline low-base, and sets the Q2 ≥₹137 Cr / ≥27% plateau test. Incorporated.
2. "Net cash ₹232.6 Cr, zero leverage, funds EV/US without debt." Bear: BS is Mar-26 not Jun-26; FY26 CFO/PAT fell to 0.88x on a ₹20.8 Cr WC build; cash pile about to be drawn by US remittance + ₹591.8m undeployed capex. SURVIVES? No — review flags INDETERMINATE Q1 conversion (caps verdict), WC drag, staleness, US outflow. Incorporated.
3. "Core operating PBT +316.7%, ~100% recurring." Bear: TC engine leans on the single Indonesia program; EV −20% on a slipped flagship; "Others +229%" off a tiny base; future D&A from undeployed capex + US build will compress the celebrated margin. SURVIVES? No — review flags single-program EV risk, undeployed capex, and explicitly warns steady-state D&A will rise. Incorporated.

ADVERSARIAL result: no surviving bear counter requiring graft. Review is symmetric; bear side carried in its five named caveats.

---

## FINAL VERDICT

COMPLETE.

The single PASS-1 gap (Step 7 RoCE FY-column mislabel) is remediated: review L243 now reads FY23 12.5% → FY24 9.3% → FY25 5.6% → FY26 9.9%, matching slide 37 (extract L1176-1185) exactly, with the source citation corrected to L1178-1185. The edit was surgical — no other cell, table, number, the questions-for-management table, the coverage map, or the closing YAML changed. All previously-passing items remain intact: deliverable gate (four provenance-labelled brief blocks), coverage (no orphan rows), headline P&L / margins / YoY-QoQ / PAT-bridge / cash arithmetic (all re-foot exactly, all A3 corrections applied), 13/13 finding-to-question mapping, standalone-only + first-coverage framing, and no surviving bear counter. The review is save-ready. Proceed to Notion.

```yaml
stage: A5-adversary
company: "divgi"
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
