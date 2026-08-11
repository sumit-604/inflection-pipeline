# A5 ADVERSARY / COMPLETENESS AUDIT — EMVDL Q1 FY27 (re-audit after prior INCOMPLETE)
# Model: claude-opus-4-8 | Fresh context: A4 review + A1 extracts + A2 ledgers only
# Re-derived independently; A4/A3 cites checked, not trusted.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run FIRST)

The MANDATORY PLAIN-LANGUAGE BRIEF (review L466-478) carries all four labelled parts, each non-empty and provenance-tagged ([this quarter filing] / [Notion memory]):

| Brief part | Heading present | Content | Status |
|---|---|---|---|
| (1) Summary narrative | L468 "1. SUMMARY NARRATIVE" | ~18-line narrative (L469): loss ₹234 Cr, presales ₹868 Cr, ₹6,000 Cr floor, debt −₹719 Cr, warrant, CIRP, other-auditor reliance, INDETERMINATE cash, H1 watch metric | PRESENT |
| (2) SECTOR intelligence | L471 | Bengaluru/MMR developer, mid-cycle, cost-of-debt headwind ~12.3-12.8%, legal overhang, NAV-accretion tailwind | PRESENT |
| (3) BUSINESS-MODEL intelligence | L474 | Three revenue modes, unit economics (~53% surplus, ~₹57k GDV), cash rhythm, hidden DM fee, warrant debt-for-equity swap, DTA non-recognition | PRESENT |
| (4) COMPETITION intelligence | L477 | Prestige/Sobha/Brigade (BLR), Lodha/Godrej/DLF (MMR), wins (brand/land bank/absorption), weaknesses (cost of debt, pledge, governance concentration) | PRESENT |

**GATE 0 = PASS.** All four parts present, real content, provenance-labelled.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledgers)

### Results filing (fresh grep + manual sweep of extract_results L418-1049)

| Category | A2 count (ledger L11-16) | My fresh count | Basis | Orphan/missing | Status |
|---|---|---|---|---|---|
| Notes | 25 | 25 | standalone notes 1-11 (11, ledger §5) + consolidated notes 1-14 (14, ledger §8) | none | MATCH |
| Line items | 57 | 57 | standalone 23 (§4 rows 1-23) + consolidated 30 (§7 rows 1-30) + Note-10 sub-table 4 (§8a) = 57 | none | MATCH |
| Zero-standing | 7 | 7 | A-4(iv) + std excep + std OCI-remeas + std other-equity + cons excep + cons OCI-remeas + cons other-equity | none | MATCH |
| Agenda items | 4 | 4 | Board outcome A/B/C/D (L22-108) | none | MATCH |
| Auditor paras | 14 | 14 | standalone review 4 + consolidated review 10 (paras 1-4 + 5-intro/5a/5b/5c/5-mgmt/5-foreign) | none | MATCH |
| Entities | 184 | 184 | Annexure 1 S.No 1-183 + 1 JV; cross-checks Note 1 "184 subsidiaries/JV" | none | MATCH |

### Presentation (fresh count vs ledger_presentation L6-16)

| Category | A2 count | My fresh count | Orphan/missing | Status |
|---|---|---|---|---|
| Slides | 33 | 33 (`^\[page N\]` 1-33) | none | MATCH |
| Table line items | 74 | 74 (11+13+13+13+7+6+11 per §2A-2G tally) | none | MATCH |
| KPI callouts | 92 | 92 (14+12+6+18+4+4+3+9+14+8) | none | MATCH |
| Chart data points | 30 | 30 (12+9+6+3) | none | MATCH |
| Cap-table points | 10 | 10 | none | MATCH |
| Footnotes | 18 | 18 | none | MATCH |
| Forward-looking | 12 | 12 | none | MATCH |
| Notes bullets | 6 | 6 | none | MATCH |
| Glossary terms | 56 | 56 | none | MATCH |

**Ledger-row → A4 citation check:** review preamble (L8-20) asserts "All reviewed," lists all 12 results A3 findings + all 11 presentation A3 findings, and both A3 files self-report reconciliation = 100%. Spot-verified that each material ledger flag surfaces in A4: CAPITAL_RAISE/CONCENTRATED_ALLOTTEE → Step 8 warrant overlay + QfM #6; OTHER_AUDITOR_RELIANCE → Step 0D auditor + Step 6B + QfM #5; LEGAL_CONTINGENCY (STPL, EEBPL) → notes table S6/C8, C9 + monitors #4/#10; SUBSEQUENT_EVENT (NCD, Spero) → notes S7/C6, C11; ENTITY_CHANGE → note S8/C7; OCR_GARBLED FX-OCI → Step 1B L105-107; ZERO_STANDING exceptional dash → Step 1 + QfM #8.

**Two ledger observations (neither an orphan / neither gates):**
- Presentation ledger flags `EXTRACT_GAP_SUSPECTED` on deck pages 22-23 (Board of Directors / Leadership Team — names/DIN not extractable). A4 does not name this deck flag, but the governance/director content it would carry is sourced instead from the results filing Annexure B (ledger_results §3; A4 Step 0C, Step 8, QfM #6/#11). Covered by substitution, not an unreviewed row.
- Presentation ledger `PRIOR_LEDGER_UNAVAILABLE` (no prior deck) — A4 carries this forward explicitly (L14, L354, L389 `PRIOR_LEDGER_UNAVAILABLE`). Reviewed.

**COVERAGE result:** no orphan rows (ledger → absent from A4); no rows my fresh pass found that the ledger lacks. **PASS.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract numbers, ₹ Cr = ₹m ×0.1)

### 2a. Tax sign check (extract_results L895-897, consolidated) — load-bearing for the bridge
- L895 Current tax Q1FY27 11.93 / Q1FY26 56.52 (both **positive = charge**)
- L896 Deferred tax Q1FY27 (9.04) / Q1FY26 (48.10) (credits)
- L897 **Total tax Q1FY27 +2.89m = +0.289 Cr (CHARGE); Q1FY26 +8.42m = +0.842 Cr (CHARGE)**
Row label is "Less: Tax expense/(credit)"; positive figure = expense. A4 Step 1B L109 and Step 4 L186/L190 sign these correctly as charges. **CORRECT.**

### 2b. Full Step-4 PAT bridge (consolidated, Q1FY27 vs Q1FY26) — re-derived end to end
| Component | My recompute (₹ Cr) | A4 value (L180-188) | Status |
|---|---|---|---|
| Gross profit (Rev−Land): 88.387 → 11.289 | −77.098 | −77.098 | MATCH |
| Employee+Other (99.149 → 141.946) | −42.797 | −42.797 | MATCH |
| D&A (6.707 → 12.982) | −6.275 | −6.275 | MATCH |
| Finance (160.421 → 118.568) | +41.853 | +41.853 | MATCH |
| Other income (13.132 → 24.527) | +11.395 | +11.395 | MATCH |
| JV share (−0.044 → 3.567) | +3.611 | +3.611 | MATCH |
| Tax (charge 0.842 → charge 0.289) | +0.553 | +0.553 | MATCH |
| Exceptional (0 → 0) | 0 | 0 | MATCH |
| **Sum** | **−68.758** | **−68.758** | MATCH |
| Actual Δ loss-after-JV (−165.644 → −234.402) | **−68.758** | −68.758 | **RECONCILES** |

Independent P&L-identity check confirms both years foot: Q1FY26 rebuilds to −165.644 (PBT −164.758, after-tax −165.600, after-JV −165.644 ✓); Q1FY27 rebuilds to −234.402 (PBT −237.680, after-tax −237.969, after-JV −234.402 ✓). The prior-loop error (−2.047 tax cell / bridge summing to −71.358) is corrected; every tax sign is right. **BRIDGE PASS.**

### 2c. Standalone-vs-consolidated PAT
Standalone PAT Q1FY27 = (902.88)m = **(90.288) Cr** (L442); Consolidated after-JV = **(234.402) Cr** (L902). 234.402 / 90.288 = **2.596 ≈ 2.6x** (A4 QfM #5, brief). **MATCH.**

### 2d. Other-auditor reliance ratios
Other-auditor subs revenue 1,645.39m / cons revenue 2,167.54m = **75.9%** (A4: 75.9% ✓). Other-auditor net loss 627.36m / cons loss-after-JV 2,344.02m = **26.77% ≈ 26.8%** (A4: 26.8% ✓). **MATCH.**

### 2e. Presales-vs-floor math
₹6,000 − ₹868 = **₹5,132 Cr** H2 requirement (A4 L172/L329 ✓); ÷3 = **₹1,711/qtr** (✓); 1,711/868 = **1.97x ≈ 2x** step-up (✓); 868×4 = **₹3,472** annualised-flat (A4 L238 ✓); H1 ≥2,400 = **40%** of floor (A4 8B/8C ✓); Citadel 328/8,414 = **3.9%** (✓); spends-to-collections 276/496 = **55.6% ≈ 56%** (✓). **ALL MATCH.**

### 2f. Derived-metric spot recomputes
| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Op EBITDA cons Q1FY27 (PBT+D+Fin−OI) | (130.657) | −237.680+12.982+118.568−24.527 = −130.657 | L891/888/887/882 | MATCH |
| Reported EBITDA cons Q1FY27 (PBT+D+Fin) | (106.13) | −237.680+12.982+118.568 = −106.130 | ditto | MATCH (= deck L702 "(106)") |
| Revenue YoY | −68.2% | (216.754−680.919)/680.919 = −68.16% | L881 | MATCH |
| Finance cost YoY | −26.1% | −26.09% | L887 | MATCH |
| Core PBT ex-OI YoY | +47.4% wider | (−262.207 vs −177.890) = 47.4% | L893/882 | MATCH |
| PAT after-JV YoY | +41.5% wider | 68.758/165.644 = 41.5% | L902 | MATCH |
| Presales +338% YoY | +338% | (868−198)/198 = 338.4% | deck L247 | MATCH |
| Presales QoQ | −67% | (868−2,632)/2,632 = −67.0% | deck L326 | MATCH |
| Net debt QoQ | −₹719 Cr | 4,082−3,363 = 719 (Q4 base [Notion memory]) | deck L266 | MATCH (base is memory, so tagged) |
| ETR cons Q1FY27 | −0.1% charge-on-loss | 0.289/−237.680 = −0.12% | L897/893 | MATCH |
| QoQ loss narrowed | 27.5% | (323.432−234.402)/323.432 = 27.5% | L902 | MATCH |

### 2g. ONE arithmetic observation (explained; not verdict-flipping)
A4 L123 cross-check states consolidated Reported EBITDA "reconciles EXACTLY … no discrepancy" listing **deck Q4FY26 (196) vs computed (192.32)**. Recompute: A4's computed (192.32) is correct as PBT+D+Fin (−344.874+12.614+139.938). But the deck's own "EBIDTA[A-B]" (Total income−land−employee−other) = −196.36, i.e. **EXCLUDES** the Q4FY26 exceptional gain of +40.38m/**+4.038 Cr** (extract L892) that PBT+D+Fin **INCLUDES**. So Q4FY26 deck (196) vs A4 computed (192.32) differ by exactly the +4.04 Cr exceptional — a definitional gap, not a computation error. The two zero-exceptional comparison quarters (Q1FY26 +2 and the load-bearing **Q1FY27 (106.13) vs deck (106)**) reconcile exactly. **Status: EXPLAINED / PASS.** The computed metric is right; only the word "EXACTLY/no discrepancy" is imprecise for the derived Q4FY26 quarter. Recommend A4 add a one-line footnote (exceptional-item definitional difference); does not gate.

**ARITHMETIC result:** every derived metric in A4's decision tables recomputes within rounding; the PAT bridge reconciles to −68.758 with all tax signs correct. No mismatch above rounding in any load-bearing figure. **PASS.**

---

## AUDIT 2.5 — Questions-for-Management traceability + count reconciliation

- **QfM rows (13, review L328-341):** every row carries a from_finding_id and each maps to a genuine AMBIGUOUS/FORWARD-SIGNAL confirmable in the extracts: coupon-not-in-filing (ledger note S7/C6, no coupon), pledge-not-in-filing (no pledge line anywhere in results extract), Citadel absorption silence (deck L403 gives only ₹328 Cr / ₹8,414 Cr, no %/PSF), DM-fee hidden (single reportable segment, Note 4/§4-cons), disposal-gain location (exceptional = dash both statements, L892/L432), DTA non-recognition (L896 small deferred credit on large loss), S-vs-C gap + other-auditor reliance (auditor para 5a-5f). All 13 trace to real findings. **PASS.**
- **Count reconciliation across docs:** notes 25 (11+14) ✓; results line items 57 (23+30+4) ✓; slides 33 ✓; entities 184 ✓. All independently reproduced above. **PASS.**

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive A4 claims → strongest bear from the SAME extract)

**Positive claim 1 (Combined Verdict L436/L225): "Net institutional debt DOWN ₹719 Cr QoQ — the clearest positive."**
Bear from same text: the ₹719 Cr rests on the Q4 base ₹4,082 Cr which is **[Notion memory], not anchored in this filing**; the deck's own cash-flow abstract shows **Net Financing cash flow +₹264 Cr** (L653) i.e. net new financing DRAWN in-quarter, and **CFO −₹285 Cr** (L643), with closing cash only +₹37 Cr — so the debt reduction cannot be reconciled to the deck's own cash flow and is not funded by operations. **Survives?** Partially, but **already incorporated**: A4 shows CFO (285)/financing +264 (Step 5 L206-209), tags the −719 as [Notion memory] (L213/L225), and the Combined Verdict L438/L424 marks "balance sheet strengthens" as **PARTIALLY CONFIRMED (debt yes; earnings/CFO no)**. No new graft required.

**Positive claim 2 (Step 2 diag 1 / brief): "Presales rose to ₹868 Cr, +338% YoY."**
Bear from same text: the ₹198 Cr base is management-declared **"not comparable"** (Presn note 6, ledger §9A note 6 / L964) and a seasonal low; the sequential print **collapsed −67% QoQ** off ₹2,632 Cr (deck L326); and ₹868 Cr sits **below the ₹1,200 Cr Q1 Red line**. **Survives?** Yes as a fact — but **already fully incorporated** (Step 3 L170, Step 6B monitor #1 RED, F16-a/b, Step 7 §7 L425 "TECHNICALLY TRUE, materially soft base"). No new graft required.

**Positive claim 3 (Step 2 diag 5 / Step 4: "Finance cost DOWN 26.1% YoY — the one genuinely improving line.")**
Bear from same text: the YoY base is the same disowned non-comparable quarter; absolute finance cost is still **₹118.6 Cr against negative EBIT → interest coverage deeply <1.2x** (monitor #6 RED, L256); and the ₹920 Cr refi's **coupon is NOT disclosed in the filing** (11% is [Notion memory] only), so the falling-cost-of-debt thesis is unproven on anchored evidence. **Survives?** Yes as a caveat — but **already incorporated**: A4 marks monitor #6 RED (L256), monitor #2 coupon-not-filing-anchored (L252), blended ~12.3-12.8% still ~230 bps above target (6D L278), and QfM #3 asks the coupon directly. No new graft required.

**ADVERSARIAL result:** the strongest bear counter to each of A4's three most-positive claims is already present and weighted in the review (this is a notably symmetric review). **No surviving bear counter requires grafting into A4.** PASS.

---

## VERDICT

**COMPLETE.** All prior-loop defects are fixed and independently reconfirmed: (1) the Step-4 PAT bridge sums to −68.758 Cr and equals the actual consolidated loss-after-JV delta, with every consolidated tax sign correct against extract L895-897 (Q1FY26 +0.842 and Q1FY27 +0.289 are both charges); (2) the results line-item count is 57 (23+30+4) matching ledger L12; (3) note 25 / slide 33 / entity 184 counts reconcile; (4) presales-vs-floor arithmetic checks; (5) the mandatory PLAIN-LANGUAGE BRIEF is present with all four provenance-labelled parts; (6) all 13 QfM rows trace to real AMBIGUOUS/FORWARD-SIGNAL findings; (7) the strongest bear counters are already incorporated. One non-gating wording note (2g): the Q4FY26 EBITDA "no discrepancy" claim glosses a +4.04 Cr exceptional-item definitional gap; A4's computed metric is correct and the load-bearing Q1FY27 reconciliation is exact — recommend a clarifying footnote, but this does not fail the gate. No orphan rows, no missing enumeration, no arithmetic mismatch above rounding in any decision metric.

```yaml
stage: A5-adversary
company: "EMVDL"
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
