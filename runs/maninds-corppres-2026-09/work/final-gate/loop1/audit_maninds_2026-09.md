# A5 ADVERSARY / COMPLETENESS AUDIT — LOOP-1 RE-AUDIT
# Man Industries (India) Ltd (MANINDS) | Corporate Presentation 01-Sep-2026 | Quarter tag 2026-09
# Inputs read: A4 review (loop1, corrected), A1 fulltext, A1 structured (R001-R335), A2 ledger.
# Source PDF and inputs/ NOT opened. Coverage re-run grepped over the A1 FULLTEXT (the spine).

---

## LOOP-1 FIX VERIFICATION (three prior findings)

| Finding | Prior defect | Corrected text in A4 | Landed? |
|---|---|---|---|
| ARI-1 | Standalone clean margin labelled "above floor by 0.3pp" (sign inverted) | 2.3 table + Read L74/L79-86: standalone clean 12.7% "BELOW 13% floor by 0.3pp"; explicit "12.7% is 0.3pp UNDER 13.0%, not over"; BOTH bases below (SA 12.7%, consol 12.3%). | YES |
| COV-2 | Acquire-route accretion guidance not grafted | 2.9 "Acquire-route EBITDA/PAT margin guidance 15-18% / 11-14% (R115/R116)"; GUIDED-ACCRETION BEAR COUNTER L203-211; flags #8; QfM Q3. | YES |
| COV-1 | Order-book "(including executed to date)" clause dropped | 2.9 ORDER-BOOK QUALIFIER L195-201, verbatim "(including executed to date)" (R144, fulltext L729-731); flag #9; QfM Q12; monitorable. | YES |
| Mandatory acq-economics probe | (new requirement) | NPC PURCHASE MULTIPLE L213-227: ~2.7x gross / ~1.9x EBITDA / ~0.5x net-of-cash, peak-year question, QfM Q11. | YES |

All three fixes plus the mandatory acquisition-economics point are present, line-anchored, and carried into flags/QfM/monitorables and the plain-language brief.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run FIRST)

| Brief part | Location | Content present? |
|---|---|---|
| 1. Summary narrative | L443-477 (~30 lines) | present, non-placeholder |
| 2. SECTOR intelligence | L479-492 | present, non-placeholder |
| 3. BUSINESS-MODEL intelligence | L494-508 | present, non-placeholder |
| 4. COMPETITION intelligence | L510-525 | present, non-placeholder |

All four labelled parts present and carry real content. GATE PASSES.

---

## AUDIT 1 — COVERAGE (independent fresh enumeration vs A2 ledger)

Fresh grep pass over the A1 fulltext (page markers, number/entity/forward/date sweeps) and the
A1 structured file, diffed against the A2 count test.

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| slides (pages) | 37 | 37 ([page 1]..[page 37]) | none | MATCH |
| NUMBER rows | 223 | 223 (R001-R223) | none | MATCH |
| ENTITY rows | 49 | 49 (R224-R272) | none | MATCH |
| FORWARD rows | 20 | 20 (R273-R292) | none | MATCH |
| DATE rows | 43 | 43 (R293-R335) | none | MATCH |
| footnotes | 10 | 10 (MF01-MF10) | none | MATCH |
| zero_standing | 3 (reconciled) | 3 (R194, R206, MF10) | none | MATCH |
| Structured IDs total | 335 | 335 (R001-R335) | orphan_ids: [] | MATCH |

ID accountability: every R001-R335 grouped in ledger §1 by slide; MF01-MF10 added as the ten
MISSING_FROM_STRUCTURED footnote/nil units. A4 STEP 1 states "All reviewed... 335/335 +
MF01-MF10 read at cited lines. No unreviewed row," and folds the material misses (MF02/MF04
EBITDA-incl-OI, MF07/MF09 Total-Income-incl-OI, MF10 Greenfield Nil order book) into the read.
The five remaining MF rows (MF01/03/05/06/08) are INR-Millions unit disclaimers with no
analytical effect. Every material financial/forward row is cited by ID in A4 (R115/R116, R144,
R149-R172, R173-R208, R209-R219, R120-R148, R220/R286/R333/R334). No orphan row. No fresh-pass
unit missing from the ledger; the ledger already caught the one A1 miss (MF10) itself.

COVERAGE: PASS.

---

## AUDIT 2 — ARITHMETIC (recompute every derived metric from raw rows)

| Metric | A4 value | Recomputed | Source rows | Status |
|---|---|---|---|---|
| Standalone clean EBITDA margin FY26 | 12.7% (below floor 0.3pp) | 4,928-531=4,397; /34,552=12.73% | R153/R150/R149 | MATCH |
| Consolidated clean EBITDA margin FY26 | 12.3% (below floor 0.7pp) | 4,679-286=4,393; /35,639=12.33% | R165/R162/R161 | MATCH |
| Standalone clean margin FY25 | 8.9% | 3,309-542=2,767; /31,182=8.87% | R153/R150 | MATCH |
| Consolidated clean margin FY25 | 9.6% | 3,563-200=3,363; /35,054=9.59% | R165/R162 | MATCH |
| Standalone EBITDA YoY | +48.9% | (4,928-3,309)/3,309=48.9% | R153 | MATCH |
| Consolidated EBITDA YoY | +31.3% | (4,679-3,563)/3,563=31.3% | R165 | MATCH |
| Consolidated revenue YoY | +1.7% | (35,639-35,054)/35,054=1.67% | R161 | MATCH |
| Standalone revenue YoY | +10.8% | (34,552-31,182)/31,182=10.81% | R149 | MATCH |
| Consolidated PAT YoY | +11.3% | (1,705-1,532)/1,532=11.29% | R171 | MATCH |
| Standalone PAT YoY | +42.8% | (1,958-1,370)/1,370=42.9% | R159 | MATCH |
| SA-vs-consol PAT gap FY26 | -253 / -12.9% | 1,705-1,958=-253; /1,958=-12.9% | R159/R171 | MATCH |
| SA-vs-consol PAT gap FY25 | +162 / +11.8% | 1,532-1,370=+162; /1,370=+11.8% | R159/R171 | MATCH |
| Subsidiary PAT swing | -415 / -21.2% of SA PAT | -253-162=-415; /1,958=-21.2% | derived | MATCH |
| Subsidiary revenue fall | ~72% | (3,872-1,087)/3,872=71.9% | R161-R149 both yrs | MATCH |
| CWIP multiple FY24->FY26 | 10.68x | 3,258/305=10.68 | R191 | MATCH |
| Inventories multiple | 2.38x | 15,350/6,456=2.38 | R199 | MATCH |
| Current receivables multiple | 2.84x | 10,098/3,551=2.84 | R201 | MATCH |
| Other fin liab multiple | 20.85x | 5,797/278=20.85 | R185 | MATCH |
| Net cash (borrowings only) | ~1,575 | 6,572-(2,402+2,595)=1,575 | R202/R176/R181 | MATCH |
| Q1FY27 Total Income YoY | +37.7% | (10,650-7,736)/7,736=37.7% | R216 | MATCH |
| Q1FY27 Total Income QoQ | -8.6% | (10,650-11,655)/11,655=-8.6% | R216 | MATCH |
| Revenue CAGR FY22-FY26 | 13.4% | (3,592/2,178)^0.25-1=13.3% | R005/R006 | MATCH (rounds to deck) |
| EBITDA CAGR FY22-FY26 | 21.0% | (468/218)^0.25-1=20.9% | R010/R011 | MATCH |
| Paid-up capital rise | +15.7% | (375-324)/324=15.7% | R173 | MATCH |
| Share premium implied | ~3,036 | 4,741-1,705=3,036 | R174/R171 | MATCH |
| GP step FY25->FY26 | +72.5%, 22.4%->38.0% | (13,639-7,905)/7,905=72.5% | R210/R211 | MATCH |
| NPC gross purchase multiple | ~2.7x PAT | 102/38.3=2.66 | R091/R134 | MATCH |
| NPC EBITDA multiple | ~1.9x | 102/52.5=1.94 | R091/R123 | MATCH |
| NPC net-of-cash multiple | ~0.5x PAT | (102-83)/38.3=0.50 | R091/R139/R134 | MATCH |
| NPC INR multiple | ~2.9x | 1,000/343.6=2.91 | R041/R148 | MATCH |
| NPC EBITDA margin CY2025 | 24.8% | 196.7/792.7=24.8% | R123/R120 | MATCH |
| NPC PAT margin CY2025 | 18.1% | 143.5/792.7=18.1% | R134/R120 | MATCH |

No mismatch above rounding. All A4-derived metrics reproduce from the anchored raw rows.

ARITHMETIC: PASS.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims + strongest bear from same text)

MANDATORY ACQUISITION-ECONOMICS PROBE executed (NPC is the acquisition in the deck).

1. CLAIM: "NPC bought cheap for a great asset" — ~2.7x gross / ~0.5x net-of-cash CY2025 PAT,
   29.5% ROCE (R142), zero debt (R284), USD 83 Mn cash (R139), Aramco-tenured.
   BEAR (same text): a debt-free 29.5%-ROCE asset at ~3x earnings is anomalously cheap; the
   deck's OWN forward accretion guide 15-18% EBITDA / 11-14% PAT (R115/R116) sits 700-900bps
   BELOW the CY2025 print (24.8%/18.1%), i.e. management is not underwriting the trailing
   margins forward. CY2025 is likely a cycle peak the seller cashed out of.
   SURVIVES? Yes — and ALREADY GRAFTED (A4 L213-227, flag #10, QfM Q11). No new graft needed.

2. CLAIM: "NPC re-rates the group at 24.8% EBITDA / 29.5% ROCE."
   BEAR (same text): the deck guides accretion at 15-18% EBITDA / 11-14% PAT (R115/R116, page-24
   "Earnings Accretive" row), not the 24.8%/18.1% print; the PAT guide (11-14%) is only ~2-3x
   the parent's thin 4.7% consol margin, not the ~4x the peak implies.
   SURVIVES? Yes — ALREADY GRAFTED (A4 L203-211, flag #8, QfM Q3, monitorable). No new graft.

3. CLAIM: "Immediate US$120 Mn order book" (slide 25, R119/R285).
   BEAR (same text): the source states "USD 120 Million ... (including executed to date)"
   (R144, fulltext L729-731); the true forward backlog converting to revenue from Q2 FY27 is
   SMALLER than the "immediate order book" framing.
   SURVIVES? Yes — ALREADY GRAFTED (A4 L195-201, flag #9, QfM Q12, monitorable). No new graft.

Secondary positive claims tested, each already countered in A4 (no un-grafted survivor):
- Standalone PAT +42.8% -> countered by consol +11.3% and subs turning loss-making (Step 4).
- Reported EBITDA 14.0%/13.0% at/above floor -> countered by clean 12.7%/12.3% (2.3, ARI-1).
- Headline ROCE 18.4% -> countered by "rides incl-OI EBIT; clean ROCE ND" (2.6, flag #7).
- "Net cash" impression -> countered by the 5,797 flip to net debt (Step 5, flag #4).
- GP margin 38.0% -> countered as likely reclassification on flat revenue (2.7, flags #6).

No surviving bear counter is absent from A4. Adversarial read produces no new correction.

ADVERSARIAL: PASS.

---

## FINDINGS BY TYPE

- FACTUAL: none.
- MISSING: none.
- CONTRADICTION: none.
- STYLE: none material. (Verdict-label note recorded in analyst_note; deemed compliant, no loop.)

---

## VERDICT

COMPLETE. All three loop-1 fixes (ARI-1, COV-1, COV-2) landed and are line-anchored; the
mandatory acquisition-economics probe is present with the multiple stated and stress-tested.
Deliverable-completeness gate passes (all four brief parts). Coverage reconciles 335/335 +
MF01-MF10 with zero orphan and zero fresh-pass miss. Arithmetic reproduces every derived metric
within rounding. Adversarial read surfaces no un-grafted surviving bear counter. No FACTUAL,
MISSING, or CONTRADICTION finding fires. Proceeds to Notion save.

## STYLE NOTES

None requiring the record. (See analyst_note for the verdict-label check.)
