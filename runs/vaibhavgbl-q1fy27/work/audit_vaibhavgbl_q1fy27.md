# A5 ADVERSARY / COMPLETENESS AUDIT — Vaibhav Global Limited (VAIBHAVGBL) — Q1 FY27

Agent A5 (Adversary). Fresh context: A4 review + A1 extracts + A2 ledgers only. Re-derived independently; A4/A3 cites checked, not trusted.
Unit note applied: results filing in ₹ Lakhs (×0.01 → ₹ Cr); press release + presentation native ₹ Cr. No concall this run (Role 5 N.A.) — not faulted.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run FIRST)

The A4 review carries a PLAIN-LANGUAGE BRIEF (review L421-433) with all four labelled parts present and non-empty:

| Brief part | Location | Present? | Real content check |
|---|---|---|---|
| 1. Summary narrative (10-20 lines) | L423-424 | present | 18-line narrative; headline vs one-off/FX/QoQ adjustments, mix positive, UK/Europe + TV negatives, INDETERMINATE cash, verdict. Real. |
| 2. SECTOR intelligence | L426-427 | present | TV→digital migration, TAM $20bn vs $416mn, discretionary caution + ME conflict, tariff policy risk, ~90% FX. Real. |
| 3. BUSINESS-MODEL intelligence | L429-430 | present | Vertical integration, margin stack, 76% profit from subs, TV→digital drift, Budget Pay 38% credit gap. Real. |
| 4. COMPETITION intelligence | L432-433 | present | Own-brand/own-channel edge, sub-scale vs marketplace/TV incumbents, fixed-cost disadvantage when volume falls. Real. |

**Gate 0 result: PASS.** All four parts present and substantive.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

Fresh grep + manual sweep of each extract, diffed against the A2 count tests.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results: notes (9 consol L157/161/165/182/186/194/198/202/231 + 6 SA L291/296/300/304/308/312) | 15 | 15 | none | PASS |
| Results: line items (34 consol P&L + 20 segment + 1 note-5 + 26 SA) | 81 | 81 | none | PASS |
| Results: entities (Annexure I incl. parent) | 14 | 14 | none | PASS |
| Results: agenda items (board outcome 1-4) | 4 | 4 | none | PASS |
| Results: auditor paras (7 consol + 6 SA, numbered) | 13 | 13 | none | PASS |
| Results: annexure rows (6 ESOP + 5 EY) | 11 | 11 | none | PASS |
| Results: signature blocks | 7 | 7 | none | PASS |
| Results: zero_standing (row 22/26/28/30 consol) | 4 | 4 | none | PASS |
| Press release: disclosure units (18 sections) | 71 | 71 | none | PASS |
| Presentation: slides | 39 | 39 | none | PASS |
| Presentation: chart blocks / footnotes / entities / guidance / leadership / OCR / zero-standing | 9/15/39/11/10/6/1 | matches | none | PASS |

**Orphan-row test (ledger row present but absent from A4):** none. A4 preamble (L12-23) claims all 15 notes, all 71 press units, all 39 slides reviewed, and incorporates all 24 A3 findings (9 results + 5 press + 10 presentation) with an explicit finding→question cross-map (L362). Spot-verified that every material/flagged ledger row surfaces in A4:
- IEEPA/Section 122 (results Note 8, L202-229) → Step 0D decomposition + Step 2/4 one-off strip. Cited.
- Q4 balancing-figure caveat (Note 7) → C7, QoQ caution. Cited.
- Content/broadcasting >10% (Note 5) → Step 4 bridge (196.55 vs 165.03). Cited.
- 4 unnamed other-auditor subsidiaries (consol LRR para 7) → Q11. Cited.
- EY internal auditor vs IR advisor (results L42-43 + press L205 + deck L1159) → A3-08 / Q9. Cited.
- Net-cash conflict ₹287/296/387 (press L86 vs deck L731/L275/L1052) → FND-06 / Step 5 / Q8. Cited.
- Budget Pay 38% (deck L1148) → FND-10 / Q12. Cited.
- Meals 115mn vs 113mn (press L110 vs L190) → F14-01 Monitorables. Cited.
- Section-numbering / OCR / dual-email defects (deck) → FND-07 Monitorables. Cited.
- 0% marketplace take-rate (deck L472 ZERO_STANDING) → business-model + competition brief. Cited.
- CHART_PAGE_OFFSET (deck, 8/9 blocks) → A4 correctly anchors to RENDERED-slide values (EBITDA walk 4.2→11.1; TV/digital 444/485/484, ASP $38.8/40.5/37.1). Handled correctly.

**Missing-from-ledger test (my fresh pass found a row the ledger lacks):** none. Every numeric/entity/note I located is already enumerated.

**Coverage result: PASS.** No orphan rows (→ no A3 loop-back), no missing enumerations (→ no A2 loop-back).

Minor observation (not a gate failure, both figures ARE enumerated): the Q4 MAT-credit is printed as **₹47.2 Cr** on deck slide 18 (presentation ledger Table F #6, line 540) but **₹47.6 Cr** in the press release footnote (press ledger §9, L91); the true standalone deferred-tax credit is ₹47.53 Cr (results R:L273). A4 uses ₹47.6 Cr and ₹47.53 Cr and does not explicitly call out the 47.2-vs-47.6 deck/press rounding gap. Immaterial to any derived metric; logged for A2 visibility only, no loop-back.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakhs, ×0.01)

Every derived metric in A4's tables recomputed from the source lines. Representative recomputations (all periods checked; showing key cells):

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Operating EBITDA Q1FY27 (PBT+D+Fin−OI) | 96.73 | 70.87+26.63+4.54−5.31 = 96.73 | R:L91/88/87/80 | MATCH |
| Operating EBITDA Q4FY26 | 83.60 | 63.91+27.92+4.31−12.54 = 83.60 (uses PBT-after-exc 63.91) | R:L93/88/87/80 | MATCH |
| Op EBITDA margin Q1FY27 | 10.5% | 96.73/917.07 = 10.55% | — | MATCH |
| Op EBITDA margin Q1FY26 | 7.6% | 61.54/813.74 = 7.56% | — | MATCH |
| Op EBITDA margin +bps YoY | +297 bps | 10.548%−7.563% = 298.5 bps | — | MATCH (rounding) |
| Reported EBITDA Q1FY27 | 102.04 | 70.87+26.63+4.54 = 102.04 | — | MATCH |
| Core PBT ex-OI Q1FY27 | 65.56 | 70.87−5.31 = 65.56 | — | MATCH |
| Effective tax rate Q1FY27 | 20.4% | 14.49/70.87 = 20.44% | R:L97/91 | MATCH |
| Current-tax-only ETR Q1FY27 | 32.4% | 22.97/70.87 = 32.41% | R:L95/91 | MATCH |
| ETR Q4FY26 | −42.6% | −27.23/63.91 = −42.6% | — | MATCH |
| ETR FY26 | 5.6% | 15.72/281.85 = 5.58% | — | MATCH |
| PAT margin Q1FY27 | 6.1% | 56.38/917.07 = 6.15% | — | MATCH |
| Revenue YoY | +12.7% | 103.33/813.74 = 12.70% | R:L79 | MATCH |
| Revenue ex-IEEPA YoY | +9.6% | (891.48−813.74)/813.74 = 9.55% | R:L79, C8 −25.59 | MATCH |
| Op EBITDA ex-IEEPA YoY | +15.6% | (71.14−61.54)/61.54 = 15.6% | — | MATCH |
| Core PBT YoY | +100.2% | 32.81/32.75 = 100.2% | — | MATCH |
| Core PBT ex-IEEPA YoY | +22.1% | (39.97−32.75)/32.75 = 22.0% | — | MATCH |
| Reported PBT ex-IEEPA YoY | −1.2% (flat) | (45.28−45.82)/45.82 = −1.18% | — | MATCH |
| PAT YoY | +49.8% | 18.75/37.63 = 49.8% | R:L98 | MATCH |
| PAT QoQ | −38.1% | −34.76/91.14 = −38.1% | — | MATCH |
| PBT QoQ | +10.9% | 6.96/63.91 = 10.89% | — | MATCH |
| Current-tax-only PAT QoQ | +3.3% | (47.90−46.38)/46.38 = 3.28% | — | MATCH |
| PAT bridge: GP change | +106.05 | (91707.34−(9863.73+21692.69−4127.88))·... = Rev+103.33 − COGS(−2.72) = +106.05 | R:L79/83/84/85 | MATCH |
| PAT bridge sum → PBT | +25.05 | 106.05−3.87−67.00−1.34−1.04−7.76 = 25.04 (=70.87−45.82=25.05) | — | MATCH (rounding) |
| PAT bridge → PAT | +18.75 | 25.05−6.30 = 18.75 | — | MATCH |
| S-C PAT gap Q1FY27 | +76.4% | (56.38−13.28)/56.38 = 76.4% | R:L98/L275 | MATCH |
| S-C PAT gap Q4FY26 | −57.0% | (91.14−143.11)/91.14 = −57.0% | — | MATCH |
| UK PBIT Q1FY27 / Q1FY26 | −0.47 / +9.78 | (47.48)L→−0.47; 978.27L→9.78 | R:L140 | MATCH |
| Europe PBIT Q1FY27 / Q1FY26 | −2.89 / +12.88 | (288.50)L→−2.89; 1287.87L→12.88 | R:L142 | MATCH |
| TV volume YoY | −3.9% | (1291−1343)/1343 = −3.87% | PP:s20 | MATCH |
| TV USD ASP YoY | −4.4% | (37.1−38.8)/38.8 = −4.38% | PP:s20 | MATCH |
| IEEPA revenue booking | 25.59 | 2,559.15 L ×0.01 = 25.59 | R:L214 | MATCH |
| Section 122 unbooked | 14.26 | 1,425.73 L ×0.01 = 14.26 | R:L219 | MATCH |
| Dividend outflow | ~25.1 | 16.73 Cr sh × ₹1.50 = 25.1 | R:L117/194 | MATCH |
| Share issue 276,874 | ×₹2 = 5.53 L capital rise | 3,346.01−3,340.48 = 5.53 L | R:L117/182 | MATCH |

**Arithmetic result: PASS.** No mismatch above rounding in any derived metric across Steps 1B, 2, 3, 4, 5S. All raw-to-Cr conversions correct. No A4 loop-back on arithmetic.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims + strongest bear counter)

| # | A4's positive claim | Strongest bear counter FROM THE EXTRACT | Survives? | Already in A4? |
|---|---|---|---|---|
| 1 | Operating EBITDA margin expanded to 10.5% on genuine in-house-brand mix (57% vs 36%); gross margin +417 bps (Step 2, 6D) | ~₹25.59 Cr IEEPA refund lands in revenue at ~zero cost, inflating gross margin; and the deck's own EBITDA walk bases off 4.2% (PP:s21) which contradicts the 9% reported Q1FY26 margin — the walk is internally unreconciled (FND-09). So an unknown slice of the +297 bps is one-off, not mix. | YES | YES — Step 2 diag 2, Step 6D "killing evidence", Q8. Incorporated. |
| 2 | Reported PAT +50% YoY / "strong profitable growth" (PR headline) | Strip the ₹25.59 Cr pre-tax one-off (≈₹20.4 Cr post-tax) and it EXCEEDS the entire ₹18.75 Cr PAT increase → clean core PAT did not grow; also QoQ reported PAT is −38%, and management's +29% rebases Q4 ex-₹47.6 Cr MAT credit; constant-currency revenue "broadly flat" (PR:L127). | YES | YES — Step 2/3/4, flags ONE_OFF_IN_REVENUE / CONSTANT_CURRENCY_FLAT / QoQ_PAT_REFRAME. Incorporated. |
| 3 | High-quality structure: net cash, 24% ROCE, clean audit, ON-TRACK brand engine (Step 8) | Net cash is quoted three ways (₹287/296/387 Cr, >30% gap, FND-06); ROCE 24% is a deck FY26 annual figure on a disputed cash base and simply repeated for "Q1FY27" (PP:s29 plots 24/24); cash conversion INDETERMINATE (no Q1 cash-flow/BS); UK + Europe swung to losses; TV (largest channel) declining on volume −3.9% and USD ASP −4.4%. | YES | YES — Step 5, Step 6B/6D, flags NET_CASH_CONFLICT / CASH_CONVERSION_INDETERMINATE / SEGMENT_LOSSES / TV_STRUCTURAL_DECLINE. Incorporated. |

**Every surviving bear counter to the three most-positive claims is already carried in A4.** No un-incorporated surviving counter → no mandatory graft, no A4 loop-back.

Corroborating observation (strengthens A4's existing thesis, not a missing counter, so no graft required): USA segment PBIT rose Q1FY26 33.75 → Q1FY27 58.32 Cr (R:L139), a +24.57 Cr swing that almost exactly equals the ₹25.59 Cr IEEPA refund booked in that geography's revenue. This mechanically confirms A4's central claim that essentially all reported profit growth is the one-off; it reinforces, and does not contradict, the review.

---

## VERDICT

- Deliverable gate (four-part Plain-Language Brief): PASS.
- Coverage (independent re-enumeration vs A2): PASS — no orphan rows, no missing enumerations, all 24 A3 findings incorporated.
- Arithmetic (recomputed from raw Lakhs): PASS — every derived metric within rounding.
- Adversarial read: PASS — all three surviving bear counters already in the review.

**VERDICT: COMPLETE.** No loop-back. The A4 review may proceed to Notion save.

```yaml
stage: A5-adversary
company: "VAIBHAVGBL"
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
