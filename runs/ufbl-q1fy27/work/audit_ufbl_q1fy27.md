# A5 ADVERSARY / COMPLETENESS AUDIT — UFBL Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Date:** 2026-08-12
**Under audit:** `review_ufbl_q1fy27.md` (A4)
**Re-derived from:** `extract_presentation_ufbl_q1fy27.txt` (A1), `ledger_presentation_ufbl_q1fy27.md` (A2)
**Scope confirmed:** single investor PRESENTATION, 39 slides, 0 Reg-33 filing, 0 concall. Independence held: I did not read A3's notes; every finding below is re-derived from the extract and ledger only.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF present at review lines 333-358, all four labelled parts non-empty with real content:

| Part | Location | Present? | Content check |
|---|---|---|---|
| 1. Summary narrative | l335-339 | **present** | ~15 lines, two paragraphs, numbers-anchored, balanced bull/bear |
| 2. Sector intelligence | l341-346 | **present** | industry size, structural drivers, cycle, International — provenance-tagged |
| 3. Business-model intelligence | l348-352 | **present** | revenue mechanics, unit economics with A10 caveat, model drift |
| 4. Competition intelligence | l354-358 | **present** | named peers, structural-weakness read, competitive tell |

GATE 0: **PASS.** No missing or placeholder part.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger)

Fresh grep `^\[page [0-9]+\]` over the extract → 39 hits, N=1..39 contiguous, no gaps/repeats. My counts reproduce the ledger exactly:

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides (`[page N]`) | 39 | 39 | none | MATCH |
| Slide numbers | 39 | 39 | none | MATCH |
| P&L line items (sl31) | 17 | 17 | none | MATCH |
| Balance-sheet line items (sl32) | 37 | 37 | none | MATCH |
| Footnotes / disclaimers | 11 | 11 | none | MATCH |
| Zero/nil/dash standing items | 8 | 8 | none | MATCH |
| OCR-only no-data slides (2,17,18,19,21,22,23) | 7 | 7 | none | MATCH |

**Ledger-flag → A4-disposition trace (every flagged row resolves to a review finding or an explicit reviewed-no-finding):**
- `UNIT_LABEL_ANOMALY` sl12 "Cumulative App Downloads (IN ₹ MN)" (l314) → A7 / Q9 ✓
- `DATA_LABEL_ODDITY` sl31 PAT YoY "190 mn" (l994) → Step 2 note + brief ✓
- `ZERO_STANDING` Investments Mar-26 nil (l1022) → A1 / Q5 ✓
- `ZERO_STANDING` GSI score withheld (sl16) → A2 / Q6 ✓
- `ZERO_STANDING` Deferred-tax-liability Mar-25 dash + margin-row YoY blanks → immaterial, correctly not a finding ✓
- `SIGNATURE_BLOCK` sl1 CS digital signature → Role 5 Step 0 (l219) ✓
- `ROUNDING_DELTA` sl37 shareholding (34.6/9.3/27.8/28.3 vs pie 35/9/28/28) → Jubilant 9.3% carried in brief; low-institutional not treated as risk (correct per CLAUDE.md) ✓
- `NO_PRIOR_LEDGER` (Table 5) → carried as open item (Step 8 gate, monitorables) ✓
- `TEXT_ANOMALY` sl38 stray "2/3/5" digits (l1186/1191/1197) → extraction-residue, no disclosure signal; A4 uses sl38 l1197 for the operating-leverage claim but does not flag the stray digits. **Not an orphan-FAIL:** the flag is an OCR artifact carrying no company-disclosure content, and A2 itself passed it as "not resolved by A2, flagged for A3."

**A4 preamble (l14) declares all 39 slides + both tabular statements + 11 footnotes + 8 zero-standing rows reviewed.** Qualitative governance slides 33/34/35/36 (bios, board, awards, ESG) carry no A3 finding and no individual citation but fall under the blanket reviewed-no-finding declaration; none carries a disclosure signal A4 dropped.

COVERAGE: **PASS.** No orphan rows (ledger→A4). No rows my fresh pass found that the ledger lacks (A2 complete).

---

## AUDIT 2 — ARITHMETIC (recomputed from raw ₹ Mn extract; Cr = Mn × 0.1)

Every derived figure in A4 re-derived from slide 31/32/24/25/26/29/30 raw numbers. All tie within ₹0.1 Cr rounding.

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Revenue Q1FY27 (Cr) | 425.9 | 4,259 ×0.1 = 425.9 | l983 | MATCH |
| Revenue Q1FY26 (Cr) | 297.0 | 2,970 ×0.1 = 297.0 | l983 | MATCH |
| Revenue YoY | +43.4% | 4,259/2,970−1 = 43.40% | l983 | MATCH |
| Total Income Q1FY27 | 427.1 | 425.9+1.2 = 427.1 | derived | MATCH |
| Total Expenses Q1FY27 | 424.7 | 145.7+87.0+22.9+45.7+123.4 = 424.7 | derived | MATCH |
| PBT Q1FY27 | 2.4 | 24 ×0.1 = 2.4 | l992 | MATCH |
| PAT Q1FY27 | 2.3 | 23 ×0.1 = 2.3 | l994 | MATCH |
| PAT swing YoY | +19.0 | 2.3−(−16.7) = 19.0 (deck "190 mn") | l994 | MATCH |
| Operating EBITDA Q1FY27 | 69.9 | PBT+D+Fin−OI = 2.4+45.7+22.9−1.2 = 69.8; deck 699→69.9 | l987 | MATCH (0.1 deck rounding) |
| Operating EBITDA Q1FY26 | 46.0 | −17.0+44.9+20.0−1.9 = 46.0 (deck 460) | l987 | MATCH |
| Op EBITDA margin exp. | +90 bps | 16.4%−15.5% = 0.9 pp | l988 | MATCH |
| Reported EBITDA Q1FY27 | 71.0 | 2.4+45.7+22.9 = 71.0 | derived | MATCH |
| Core PBT ex-OI Q1FY27 | 1.2 | 2.4−1.2 = 1.2 | derived | MATCH |
| Core PBT ex-OI Q1FY26 | (18.9) | −17.0−1.9 = −18.9 | derived | MATCH |
| Core-PBT swing | +20.1 | 1.2−(−18.9) = 20.1 | derived | MATCH |
| Effective Tax Rate Q1FY27 | 4.2% | 0.1/2.4 = 4.17% | l993/992 | MATCH |
| Other Income/PBT Q1FY27 | 50.0% | 1.2/2.4 = 50.0% | derived | MATCH |
| Adjusted Op EBITDA Q1FY27 | 34.3 | 343 ×0.1 = 34.3 | l999 | MATCH |
| Adjusted PAT Q1FY27 | 8.7 | 87 ×0.1 = 8.7 | l1001 | MATCH |
| **PAT bridge — Gross profit chg** | +79.2 | 2,802−2,010 = 792 →79.2 | l792/l984 | MATCH |
| Employee chg | (14.1) | 870−729 = 141 →14.1 | l985 | MATCH |
| Occupancy chg | (41.3) | 1,234−821 = 413 →41.3 | l986 | MATCH |
| Op EBITDA chg | +23.9 | components 79.2−14.1−41.3 = 23.8; deck 699−460 = 239→23.9 | l987 | MATCH (0.1 deck rounding) |
| Depreciation chg | (0.8) | 457−449 = 8 →0.8 | l991 | MATCH |
| Finance-cost chg | (2.9) | 229−200 = 29 →2.9 | l990 | MATCH |
| Other-income chg | (0.7) | 12−19 = −7 →0.7 | l989 | MATCH |
| PBT chg | +19.4 | 2.4−(−17.0) = 19.4 | l992 | MATCH |
| Tax chg | (0.4) | 1−(−3) = 4 →0.4 charge | l993 | MATCH |
| Reported PAT chg | +19.0 | 19.4−0.4 = 19.0 | l994 | MATCH |
| Net debt ex-leases Mar-26 | 106.7 | (772+572)−(256+21) = 1,067 →106.7 | l1021/1030/1032/1033 | MATCH |
| Net debt ex-leases Mar-25 | 52.4 | (462+233)−(169+2) = 524 →52.4 | same | MATCH |
| Net-debt change | +54.3 | 106.7−52.4 = 54.3 | derived | MATCH |
| Lease liabilities Mar-26 | 750.8 | 6,665+843 = 7,508 →750.8 | l1022/1031 | MATCH |
| Lease liabilities Mar-25 | 688.0 | 6,150+730 = 6,880 →688.0 | l1022/1031 | MATCH |
| Total equity change | (49.6) | 321.3−370.9 = −49.6 (3,213 vs 3,709) | l1018 | MATCH |
| DTA (net) | 59.6 | 596 ×0.1 = 59.6 | l1025 | MATCH |
| Segment sum vs consol | ties ±3 Mn | 3,284+385+587 = 4,256 vs 4,259 | l845/909/948 | MATCH |
| Annualised revenue | 17,036 | 4,259 ×4 = 17,036 vs FY26 13,387 | l983/l144 | MATCH |
| Gross margin drift YoY | −190 bps | 65.8%−67.7% = −1.9 pp | l802 | MATCH |
| Delivery share | 14.9%→16.8% | l828 | l828 | MATCH |

**Two descriptive imprecisions (not gate-failing, within rounding / order-of-magnitude):**
- EBIT low-base swing: A4 says "+21x"; 24.2/1.1 = 22.0x. Explicitly labelled "large low-base swing" — a descriptor of a near-zero base, not a load-bearing metric. No FAIL.
- Deck-internal only (not an A4 error): BBQ India annualised ₹13,148 Mn vs quarterly 3,284×4 = 13,136 (12 Mn / 0.09% deck inconsistency). A4 quoted the deck figure faithfully; immaterial.

ARITHMETIC: **PASS.** No mismatch above rounding.

---

## AUDIT 3 — ADVERSARIAL READ (3 most-positive claims, strongest bear from the SAME extract)

**Claim 1 (Step 4, l142):** "PAT swing ~100% operating, not treasury/tax — the single best fact in the deck."
- **Bear from extract:** The turn rests on a ₹2.4 Cr PBT (l992) off the *weakest* base quarter (Q1FY26 SSSG −3.4%, l786). Of the three big cost lines, CoF&B grew +51.8% and Occupancy +50.3% — both *faster* than revenue +43.4% (l984/986/983); only employee cost (+19.3%) delivered leverage. Gross margin fell 190 bps YoY. So "operating leverage" is narrow and the profit is razor-thin.
- **Survives?** NO — already incorporated. A4 states gross margin down 190 bps (Step 3, l121), flags the trough base (A8/A9, Step 3 l120), and Step 2 labels EBIT a "low-base swing." Bear tempering is present.

**Claim 2 (Step 2, l88 / summary l337):** "Operating EBITDA margin genuinely expanded 90 bps YoY to 16.4%."
- **Bear from extract:** 16.4% is post-IND-AS-116 (rent capitalised out of opex). The deck's own Adjusted Operating EBITDA % (rent as cash cost, l1000) is only 8.1% — roughly half. And the full-year trend is DOWN: FY26 14.4% vs FY25 17.1% (l988). The YoY quarterly expansion sits against a declining annual margin.
- **Survives?** NO — already incorporated. A4's derived table shows Adjusted 8.1% vs 4.6% (l76) and FY26 14.4% vs FY25 17.1% (l64), and the reading note (l80) states adjusted EBITDA is ~half the IND-AS figure.

**Claim 3 (summary l337 / Step 2 l99):** "Revenue +43.4% YoY, strong; three growth engines (+43.4/+46.6/+36.2%)."
- **Bear from extract:** The headline "SSSG 28.7%" (l133/786) contradicts the company's own 12-year chart placing Q1FY27 at 4.7% (l748); the ₹17,036 Mn "scale" is the peak quarter ×4 vs FY26 actual 13,387 (l983); International +46.6% carries a 320 bps GCC gross-margin hit pre-labelled "temporary" (l919).
- **Survives?** NO — already incorporated as A8 (SSSG contradiction), A9 (annualisation), A5 (GCC), all in flags, questions, and the summary narrative.

**Result: 0 surviving bear counters.** All three strongest bears are already grafted into A4's review. Nothing to loop back for.

---

## CROSS-CHECKS ON SCOPE-SPECIFIC RULES
- **Cash-conversion INDETERMINATE cap:** deck carries no cash-flow statement (confirmed — no CFO line anywhere in slides 31/32); CFO = ND correctly forces INDETERMINATE and caps at PROCEED WITH CAVEATS with the missing evidence (H1 FY27 CFO) named. Consistent (l23, l149).
- **PROCEED WITH CAVEATS verdict:** consistent with a management-authored, un-cross-examined deck (no audit, no Q&A). No interpretation exceeds what the deck supports; entity-ROCE, destination PE, and entry zone are all correctly deferred (Step 7/8), NEVER-rule on exit multiple respected.
- **Questions-for-Management trace:** all 10 rows map to a real extract-grounded issue (A1 investments l1022; A2 GSI sl16; A3 store target l122; A4 operating leverage l1197; A5 GCC l900/275; A6 DTA l1025 + ETR l992/993; A7 mislabel l314 + misspelling l998; A8 SSSG l748 vs l786; A9 annualisation l144 vs l983; A10 mixed basis l274/275). No fabricated finding; no orphan question.

---

## VERDICT

**COMPLETE.** All four deliverable-brief parts present; fresh enumeration reproduces the A2 ledger with zero orphan rows and zero missing rows; every derived metric re-computes within ₹0.1 Cr rounding; all three strongest bear counters are already incorporated in A4. Scope-specific caps (cash INDETERMINATE → PROCEED WITH CAVEATS) are correct for a presentation-only run. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "UFBL"
quarter: "Q1FY27"
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
