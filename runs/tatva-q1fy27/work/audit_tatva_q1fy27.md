# A5 ADVERSARY / COMPLETENESS AUDIT — TATVA, Q1 FY27 (RE-AUDIT, post one loop)

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Fresh context (A4 review + A1 extracts + A2 ledgers only; re-derived independently).
Prior loop: INCOMPLETE on ONE narrative-fidelity point — narrative asserted "management talked for over an hour" while the review marks call duration ND (no transcript timestamps). Coverage / arithmetic / adversarial passed clean last round. This run re-verifies all four, proportionate on the three that passed, forensic on the narrative fix.

---

## 1. COVERAGE AUDIT (spot-check; passed clean last round)

Fresh grep/sweep over `extract_concall_tatva_q1fy27.txt` (lines 21-138) diffed against `ledger_concall_tatva_q1fy27.md`, plus results and presentation ledger citation-coverage.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Concall participants | 13 | 13 (3 mgmt/IR + host + operator + 8 analysts) | none | PASS |
| Concall turns (lines 21-138) | 118 | 118 (138−21+1; zero blanks in range) | none | PASS |
| Concall analyst questions | 32 | 32 (Q1-Q32; Shlok 2 + part 1 + Raman 8 + Nirani 5 + Gor 2 + Sam 2 + Rohit 8 + Ketan 4 = 32) | none — all 32 graded in Step 4A | PASS |
| Concall mgmt/analyst numbers | 56 | 56 (N1-N56; 52 MGMT/IR + 4 ANALYST_CITED) | none | PASS |
| Concall fwd-commit + hedge phrases | 34 | 34 (23 FC + 11 H) | none | PASS |
| Concall zero-standing | 5 | 5 (Z1-Z5; all in Step 5A/8B) | none | PASS |
| Concall A3 findings A3-F01..A3-F18 | 18 | 18 — every id cited in review body (Step 5A/5B silence audit, Step 6, Step 8A-8F, flags), not just the Section B preamble list | none | PASS |
| Results A3 findings (F1-a..F14-b) | 13 | 13 — cited Step 0-8.5 / YAML | none | PASS |
| Presentation A3 findings (A3-01..A3-13) | 13 | 13 — cited Step 6/8.5 / YAML | none | PASS |

Fresh-pass rows the ledger lacks: none. No orphan rows (every ledger row cited or reviewed-no-finding). Coverage holds. **COVERAGE PASS.**

---

## 2. ARITHMETIC AUDIT (spot-check; passed clean last round)

Recomputed from raw extracted numbers.

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Concall revenue Rs 1,671 mn -> Rs Cr | Rs 167.06 Cr (ties to filing) | 1,671 mn x 0.1 = 167.1 Cr; filing 1,670.55 mn = 167.06 Cr | extract L22 / filing L286 | PASS (rounding) |
| Operating EBITDA Rs 323 mn -> Rs Cr | Rs 32.30 Cr | 323 x 0.1 = 32.30; 22.43 PBTbe + 10.57 D + 2.08 Fin − 2.78 OI = 32.30 | L22 / filing L296-300 | PASS (exact) |
| Segment split (mn) | PTC 428 / ESS 63 / PASC 584 / SDA 578 | 428+63+584+578 = 1,653 mn; 1,670.55 − 1,653 = 17.55 mn unallocated (present in deck too) | L22 | PASS (residual disclosed both sources) |
| Revenue +42.9% YoY | +42.9% (call "+43%") | 167.06/116.86 − 1 = +42.95% | Step 2 | PASS |
| Revenue +24.5% QoQ | +24.5% (call "+25%") | 167.06/134.14 − 1 = +24.5% | Step 3 | PASS |
| EBITDA +86.3% YoY | +86.3% (call "+86%") | 32.30/17.33 − 1 = +86.4% | Step 1C | PASS |
| EBITDA QoQ | +14.8% (call "+15%") | 32.30/28.13 − 1 = +14.8% | Step 7A | PASS |
| ESS −52% QoQ | −52% | 63 mn Q1 vs implied ~131 mn Q4 (analyst "six crores") | L22/L50 | PASS |
| Credibility ratio | 62.5% (Grade B) | 2.5 points ÷ (5 total − 1 UNCLEAR = 4) = 0.625 | Step 3B | PASS |

No mismatch above rounding. **ARITHMETIC PASS.**

---

## 3. ADVERSARIAL READ (no rubber-stamp; re-run)

Three most-positive claims in the review, each with strongest bear counter from the same extracted text, and whether the counter is NEW-and-surviving (must be grafted) or already-disclosed-and-flagged (COMPLETE per materiality bar).

**Claim 1 — "Strong operating quarter: revenue +43%, EBITDA +86%, PAT +140%, all tie to the filing."**
Bear counter (from extract): only ~36% of the +Rs 9.33 Cr PAT growth is durably-recurring parent core; ~28.5% is a one-off parent Other Income (L485, plus nil standalone current tax L502); ~43.1% is subsidiary-sourced from two ~zero-cost foreign WOS with no audit carve-out; margin faded QoQ 21.0%->19.3%.
Verdict: ALREADY FLAGGED — Step 4A/4B/4D, Section C, flags list, narrative para 2. No new surviving counter.

**Claim 2 — "Semiconductor first-dispatch catalyst FIRED (delivered AND qualified)."**
Bear counter (from extract): only "few tons" delivered; 3-4 more plant-scale trials over two years; management explicit that large-volume revenue is "not before Q4 of 2028" (L45/L46/L68); no semiconductor capex now (Z3).
Verdict: ALREADY FLAGGED — Step 8A ("large-volume revenue >=Q4 CY2028"), narrative ("meaningful semiconductor revenue unlikely before late 2028"). No new surviving counter.

**Claim 3 — "Management COMMITTED & CREDIBLE; reaffirmed FY27 25-30% growth and 20-22% margin; credibility 62.5% Grade B."**
Bear counter (from extract): reaffirmations are back-end-loaded off weak bases (20-22% off a 19.3% Q1, L72; ESS Rs 40-50 Cr off Rs 6.3 Cr / −52% QoQ, L51); management named NO execution risk when asked (L36, Grade D); offtake informal-only (L119); trailing-1 is single-quarter noise.
Verdict: ALREADY FLAGGED — Step 6E OVERPROMISER-boundary flag, Step 3C, Section C, flags list, narrative para 6. No new surviving counter.

No NEW surviving bear counter beyond what the review already flags. Per the stated materiality bar (already-disclosed-and-flagged is COMPLETE, not a gap), nothing must be grafted into A4. **ADVERSARIAL PASS.**

---

## 4. NARRATIVE FIDELITY (forensic — the looped item)

**(a) Narrative present in both places?** YES. Standalone `narrative_tatva_q1fy27.md` (40 lines) AND review final section "PLAIN-LANGUAGE NARRATIVE (operator brief)" at review lines 1066-1107. Both carry the headline "TATVA Q1 FY27: a loud beat, quiet on the catch."

**(b) Is "over an hour" / any call-duration claim GONE from BOTH copies?** YES. Fresh grep for `hour|over an hour|talked for|an hour` returns ZERO matches in `review_tatva_q1fy27.md`; grep for `hour` returns ZERO matches in `narrative_tatva_q1fy27.md`. The prior INCOMPLETE cause is fully removed from both, consistent with the review's own ND on call duration (Section B Step 0C: "Call duration / Q&A-duration % / exact clock time: ND").

**(c) Are the two copies identical?** Body text IDENTICAL (headline, "What unfolded this quarter", "What the next 10 to 11 months will decide", "Bottom line" — all match word-for-word). ONE benign, expected divergence in the second sentence of the preamble paragraph:
- Standalone (L3): "It translates the combined Role 4 + Role 5 review and adds no new number; every figure here already appears in a table in the review with its source."
- Review-embedded (L1070): "It translates the review above and adds no new number; every figure here already appears in a table with its source."
This is a self-locating pointer that MUST differ by context (a standalone file cannot say "the review above"). It introduces no number, no claim, no verdict, and contradicts nothing. NOT a fidelity gap; reported for transparency, not a FAIL.

**(d) Every number/claim in the narrative supported in the review tables?** YES — spot-verified end to end:
- Revenue +43% / Rs 167 Cr / highest in disclosed set (Step 2, Step 3); PAT +140% / Rs 16 Cr (Step 2); "EBITDA up 86%" led by deck and call (Step 1C, Section B claim 2); numbers tie to filing (Step 7A).
- Rs 9.3 Cr growth split: ~1/3 (Rs 3.3 Cr) parent core, ~28% one-off parent OI + near-nil parent cash tax, ~43% two USA/Europe WOS with ~zero staff/plant/equipment booking a third of group PAT, no auditor comment (Step 4B/4D, F4-a).
- 8 analysts / 32 questions / overseas arms asked by none (Section B Step 4B, Step 5B, A3-F15).
- Asset turn "roughly halved, ~3x to ~1.5x", same ROC claimed (Step 4C Exch.1, N45/N46/N47, A3-F06); moat "copyable by any determined competitor" (Q24, A3-F09); monoglime withdrawn, China price crash >half in 30 days, equipment repurposed (Q29, N48-N53, A3-F12).
- Margin 21%->19%, below 20-22%, reaffirmed with "lost one quarter with a little lesser margin" (Step 3, L72); ESS Rs 40-50 Cr target vs Rs 6 Cr / −52% QoQ / two months lost to war-driven shortage (Step 8A, N30, L51-53).
- Finance costs 5x, borrowing ceiling >3x to Rs 1,000 Cr, debt/earnings above thesis level, call silent on debt/cash/collections (Step 5, F6-b, A3-F17).
- Rs 200 Cr plant, GB 20-Jul-2026, 18-21 mo (N19/N20/N33/N34); semiconductor shipment delivered+accepted, revenue unlikely before late 2028 (L46/L68); first pharma molecule into production (L22).
- No Q1 cash-flow statement by rule; call added nothing on cash (Step 5).
- Forward forks: Q2 H1 (~Oct 2026) cash-flow read + rec days >185 tripwire (Step 6C, 8C); GB 20-Jul-2026 / Dahej-III naming (A3-F14); ESS ramp + margin recovery (8A); hybrid battery Oct/Nov 2026 -> late 2027 (N39/N40); overseas-arms durability open (5B).
- Bottom line: CMP ~Rs 1,194 ~10x the Rs 97-121 zone (~9.87x entry max), WATCHLIST/AVOID unchanged (Step 0A, Step 8, Section C).
No invented figure; no new claim; no new verdict.

**(e) Contradicts flags or verified Decision Status?** NO. Narrative reaffirms WATCHLIST / AVOID (on-valuation; Hurdle STOP) and every flag (thin recurrence, subsidiary concentration, leverage, margin fade, catalyst timing, cash-conversion INDETERMINATE, replicable moat, asset-turn downshift).

**NARRATIVE FIDELITY PASS.** The single looped defect is fixed in both copies; no new defect introduced.

---

## VERDICT

**COMPLETE.** The prior INCOMPLETE cause ("over an hour" call-duration claim) is removed from BOTH narrative copies, consistent with the review's ND on call duration. Coverage (no orphan rows; all 18 concall A3 findings + all results/presentation findings cited), arithmetic (concall-vs-filing ties and the 62.5% credibility ratio all reconcile within rounding), and adversarial read (no new surviving bear counter beyond what is already flagged) all hold on re-run. Narrative numbers/claims are all supported and non-contradictory. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "TATVA"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
narrative_ok: true
narrative_issues: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
