# A5 ADVERSARY / COMPLETENESS AUDIT — TRANSRAIL LIGHTING (TRANSRAILL / 544317) — Q1 FY27

Agent A5 (ADVERSARY, Opus 4.8). Fresh context: audited ONLY the A4 review, the A1 extracts, and the A2 ledgers. Every number below re-derived independently from the raw extracts; A4/A3 cites were checked, not trusted. Re-audit after a prior INCOMPLETE on one surviving bear counter (order-book QoQ contraction). This is the final permitted loop.

Line-anchor convention: `Lxxx` = A4's inner-content line numbers (the extract's own `[page]`/cat body numbering, offset −13 from the Read-tool outer numbering). Ledger row anchors use the ledger's outer numbering. Both cross-checked.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (HARD GATE)

PLAIN-LANGUAGE BRIEF present at review L438, with all four labelled parts carrying real, non-placeholder content:

| Part | Location | Present? | Content check |
|---|---|---|---|
| 1. SUMMARY NARRATIVE | L440-442 | PRESENT | Full narrative: revenue +4% (deck 5%), 11.9% margin, PAT +3% "manufactured", core PBT ex-OI −6%, D +33%, ROCE 25.8→23.6, intake Rs1,034cr RED, order-book QoQ contraction, net debt +168%, INDETERMINATE cash, no trigger fired, rating upgrade, governance cluster, HOLD 3%. Substantive. |
| 2. SECTOR INTELLIGENCE | L444-446 | PRESENT | NEP 191,000 CKM, Rs9.15 lakh cr, 500GW/900GW, Mission 300, timing-not-structure tension, 65% fixed-price, payer mix (World Bank/AfDB/PGCIL/TBCB), named undisclosed metrics. Provenance-tagged. |
| 3. BUSINESS-MODEL INTELLIGENCE | L448-450 | PRESENT | Backward-integrated EPC economics, model-drift read (capex ahead of volume, non-operating profit quality, overseas drag, unreviewed branch PAT), SA-vs-CO PAT gap as first-class metric, named undisclosed metrics. |
| 4. COMPETITION INTELLIGENCE | L452-454 | PRESENT | Peer set (KEC/Kalpataru/L&T/Skipper/Techno), win-basis (integration, multilateral-funded Africa), weakness (scale/balance-sheet, fixed-price, governance maturity), competitive risk tied to the order-book contraction, provenance note. |

**GATE 0: PASS.** All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

Fresh grep/sweep over both extracts, diffed against the ledgers.

| Category | A2 count | My fresh count | Method / spot-check | Orphan rows in A4? | Status |
|---|---|---|---|---|---|
| Notes (results) | 31 | 31 | SA notes 1-14 (14) + CO notes 1-15 (15) + 2 "See accompanying notes" cross-refs = 31. CO=15 because note 13 has geo sub-table + note 14 entity list + note 15 regroup | No | PASS |
| Line items (results) | 90 | 90 | SA table 38 + CO table 49 + geo table 3 (In India / Outside India / Total, L951-955) = 90 | No | PASS |
| Agenda items | 4 | 4 | Results; Bagde reappt; G.M. Kapadia joint-auditor; Dilawar Singh cessation. All in A4 (Step 0/monitorables/Q11) | No | PASS |
| Auditor paras | 23 | 23 | SA LRR 7 top + 7a/b/c (3) = 10; CO LRR 8 top (incl the "S."→"5." entity list L554) + 8a-e (5) = 13; 10+13=23. EoM + Other Matters 7a/7b cited in A4 (L49, Step 8.5 Q6) | No | PASS |
| Entities | 17 | 17 | Holding 1 + subs 6 (FZE, America, Nigeria, Malaysia, Trading LLC, Gactel) + JV 9 + associate 1 (CEDEC) = 17. Gactel/Malaysia/Trading LLC all cited | No | PASS |
| Slides (presn) | 32 | 32 | `[page N]` markers 1-32; matches formfeed 32 | No | PASS |
| Data points (presn) | 221 | 221 (accepted) | DP001-DP221 sweep; material rows (financials DP075-112, order book DP021/114/117/119, balance sheet DP129-145, capacity DP171-178, RPT DP087, new-vertical DP181/192) all cited in A4. CSR/ESG/award/section-divider rows (DP194-221) carried under blanket "all 221 reviewed" (L11) = reviewed-no-finding, permissible | No material orphan | PASS |

**Orphan-row check (ledger row present, absent from A4):** none at the material level. Every forensic-bearing ledger row (EoM, Other Matters branch/subsidiary carve-outs, ZERO_STANDING deferred tax + NCI, Gactel ENTITY_CHANGE, net-debt DEFINITION_MISMATCH, order-book DPs, geo-mix, dual-CFO, capacity DATA_INCONSISTENCY, signatory mismatch, CAGR-basis footnotes) is cited in A4's Step 0D/Step 5/Step 6/Step 8.5 or the flags block. Non-material content-free rows (CSR camps, awards, section dividers) are covered by the blanket-reviewed statement, which the protocol permits as "reviewed, no finding."

**Reverse check (my fresh pass found a row the ledger lacks):** none. Re-read of L939-1145 (QIP continuation L934-938, geo table L951-955, Note 14 entity list L965-999, all three Annexures II/III/IV) surfaces nothing absent from the A2 ledgers. QIP Note 12, geo table, Gactel Ind AS 103 restatement, joint-auditor Annexure III all enumerated.

**COVERAGE: PASS** (no loop-back to A2 or A3).

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extract)

Consolidated raw (Q1FY26 / Q4FY26 / Q1FY27 / FY26): Rev 1,637.06 / 1,831.48 / 1,702.45 / 6,779.98; OI 11.40 / 10.91 / 16.63 / 49.07; PBExc&Tax(incl JV) 146.83 / 143.82 / 144.01 / 584.34; PBT 146.83 / 143.82 / 144.01 / 566.96; Tax 41.64 / 47.00 / 36.13 / 163.04; PAT 105.19 / 96.82 / 107.88 / 403.92; FC 49.55 / 54.05 / 55.72 / 218.68; D 14.62 / 19.59 / 19.49 / 66.37; JV 0.75 / −3.29 / 0.32 / 0.62.

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA consol Q1FY27 | 202.59 | 144.01+19.49+55.72−16.63 = 202.59 | L763/757/756/748 | OK |
| Op EBITDA consol Q1FY26 | 199.60 | 146.83+14.62+49.55−11.40 = 199.60 | " | OK |
| Op EBITDA consol Q4FY26 | 206.55 | 143.82+19.59+54.05−10.91 = 206.55 | " | OK |
| Op EBITDA consol FY26 | 820.32 | 584.34+66.37+218.68−49.07 = 820.32 | " | OK |
| Op EBITDA std Q1FY27 | 204.37 | 146.68+19.36+55.70−17.37 = 204.37 | L311/308/307/299 | OK |
| Op EBITDA margin (rev-from-ops) Q1FY27 | 11.90% | 202.59/1,702.45 = 11.90% | L746 | OK |
| Op EBITDA margin YoY | 12.19%→11.90% (−29bp) | 12.192%→11.899% = −29.3bp | " | OK |
| Deck-basis margin Q1FY27 | 11.67% (deck 11.7%) | 202.59/(1,702.45+33.58)=202.59/1,736.03=11.67% | L746/747 | OK |
| Reported EBITDA consol Q1FY26 | 210.99 | 146.83+14.62+49.55 = **211.00** | " | NOTE: penny rounding (−0.01); non-load-bearing, not used downstream |
| Core PBT ex-OI consol (all 4) | 135.43/132.91/127.38/517.89 | PBT−OI = 135.43/132.91/127.38/517.89 | L765/748 | OK |
| Core PBT ex-OI std Q1FY27 | 129.31 | 146.68−17.37 = 129.31 | L313/299 | OK |
| ETR consol Q1FY27 | 25.09% | 36.13/144.01 = 25.09% | L766/765 | OK |
| ETR std Q1FY27 (sub-statutory) | 24.63% | 36.13/146.68 = 24.63% (< 25.17%) | L314/313 | OK |
| ETR consol YoY | 28.36%→25.09% | 41.64/146.83=28.36%; 36.13/144.01=25.09% | " | OK |
| PAT margin consol Q1FY27 | 6.34% | 107.88/1,702.45 = 6.34% | L770/746 | OK |
| OI/PBT consol Q1FY27 | 11.55% | 16.63/144.01 = 11.55% | L748/765 | OK |
| Revenue YoY | +3.99% | 1,702.45/1,637.06−1 = +3.99% | L746 | OK |
| Op EBITDA YoY | +1.50% | 202.59/199.60−1 = +1.50% | derived | OK |
| Depreciation YoY | +33.31% | 19.49/14.62−1 = +33.31% | L757 | OK |
| Finance cost YoY | +12.45% | 55.72/49.55−1 = +12.45% | L756 | OK |
| EBIT YoY | 184.98→183.10 (−1.02%) | (199.60−14.62)→(202.59−19.49); −1.02% | derived | OK |
| Other Income YoY | +45.88% | 16.63/11.40−1 = +45.88% | L748 | OK |
| Core PBT ex-OI YoY consol | −5.94% | 127.38/135.43−1 = −5.94% | derived | OK |
| Core PBT ex-OI YoY std | −6.15% | 129.31/137.78−1 = −6.15% | derived | OK |
| Reported PAT YoY | +2.56% | 107.88/105.19−1 = +2.56% | L770 | OK |
| PAT bridge subtotal (core PBT change) | ≈−8.05 | ΔOpEBITDA+2.99 −ΔD 4.87 −ΔFC 6.17 = −8.05 (= 127.38−135.43) | Step 4 | OK (see NOTE) |
| PAT bridge → reported PBT | −2.82 | −8.05 + ΔOI 5.23 = −2.82 (146.83→144.01) | " | OK |
| PAT bridge → reported PAT | +2.69 | −2.82 + tax benefit 5.51 = +2.69 (105.19→107.88) | " | OK |
| Normalised PAT (OI+ETR revert) | ~99.3 | (144.01−5.23)×(1−0.284)=138.78×0.716=99.4 | Step 4 | OK |
| Net debt Q1FY27 | 466.42 | 716.97+58.92−228.18−81.29 = 466.42 | deck s18/L528-540 | OK |
| Net debt 31-Mar | 174.2 | 572.23+88.53−393.77−92.79 = 174.20 | " | OK |
| Net debt QoQ | +292.22 / +168% | 466.42−174.20=292.22; /174.20=+167.7% | " | OK |
| ICR (OpEBITDA/FC) | 3.64x (~3.6x) | 202.59/55.72 = 3.636x | L756 | OK |
| Book-to-bill this qtr | 0.60x | 1,034/1,702.45 = 0.607 | DP114/L746 | OK |
| Order-book reconciliation | 16,313+1,034−1,702.45 ≈ 15,645 ≈ 15,635 ex-L1 | = 15,644.55; vs 15,635 ex-L1 (16,035−400) → gap 9.55cr, immaterial (intake/rev rounding). CONTRACTION vs 16,313 confirmed either basis | DP043/114/117/119, L746 | OK |
| India rev YoY (A3-11) | +98.7% | 1,098.30/552.84−1 = +98.66% | L951 | OK |
| Outside-India rev YoY | −44.3% | 604.15/1,084.22−1 = −44.28% | L953 | OK |
| Branch PAT / SA PAT | 34.6% | 38.25/110.55 = 34.6% | L219/318 | OK |
| Niger branch net margin | 36% | 5.60/15.57 = 35.97% | L243-244 | OK |
| SA-vs-CO PAT gap Q1FY27 | −2.42% (2.67cr) | (110.55−107.88)/110.55 = 2.42% | L318/770 | OK |
| SA-vs-CO gaps Q4/Q1FY26/FY26 | −3.20% / −2.71% / −1.87% | 3.20/100.02; 2.93/108.12; 7.71/411.63 = 3.20%/2.71%/1.87% | " | OK |

**Two non-blocking observations (neither alters a load-bearing conclusion):**
1. **Reported EBITDA consol Q1FY26** printed 210.99; exact is 211.00 (penny rounding). This line is not used in any verdict, margin, or bridge. Trivial.
2. **PAT bridge JV line.** A4's Step 4 lists "Share of JV/Associate change −0.43" as a separate bridge component, but the JV share is ALREADY embedded in Op EBITDA (A4's Op EBITDA = PBExc-incl-JV + D + FC − OI). Listing it again means the four itemised deltas (+2.99 −4.87 −6.17 −0.43) sum to −8.48, whereas the stated subtotal is −8.05. The **subtotal −8.05 is the arithmetically correct core-PBT-ex-OI change** (127.38−135.43) and it reconciles cleanly to reported PBT (−2.82) and reported PAT (+2.69). So the load-bearing figures are right; the −0.43 line is a presentational double-count, not an error in any headline number. Documented, not a blocking FAIL.

**ARITHMETIC: PASS** (no mismatch above rounding in any load-bearing metric; no loop-back to A4).

---

## AUDIT 3 — ADVERSARIAL READ (A4's three most positive claims + strongest bear counter from the same extract)

**Graft-verification first (the prior loop's INCOMPLETE trigger).** The previously surviving counter — un-executed order book contracted QoQ for the first time in ~5 years — is now grafted into A4 in multiple load-bearing places:
- **Step 6D growth-trigger table (L317):** full reconciliation (16,313 + 1,034 − 1,702.45 ≈ 15,645 ≈ 15,635 ex-L1) in the Killing-Evidence column; status reset to "WEAKENED (order book now shrinking QoQ, not merely decelerating)."
- **Summary narrative (L442):** "for the first time in about five years the un-executed order book actually CONTRACTED quarter on quarter … being drawn down rather than replenished."
- Also propagated to flags (L511), Step 8.5 Q2 (L384), Step 8A (L356), 8A-W gate condition (c) (L359), 8B add-back (L363), 8C (L371), YAML flags/monitorables (L506/L511). **Graft CONFIRMED and independently re-verified as arithmetically sound.**

| # | A4's positive claim | Strongest bear counter from the SAME extract | Survives? |
|---|---|---|---|
| 1 | Credit rating UPGRADED to IND AA-/Stable; ICR ~3.6x; trigger 4 not fired (L252, L309) | Same quarter, leverage deteriorated hard: net debt +168% QoQ to 466.42 (ST borrowings +144.74, cash −165.59), two irreconcilable deck net-debt figures (466.42 vs 548), and NO cash-flow statement — the "improving profile" narrative rests on a rating action while the balance sheet moved the other way | NO — already fully incorporated (Step 5, 6B item 3 RED, 6D "WEAKENED/UNVERIFIED", flags L509) |
| 2 | Margin holds inside 11.5-12.5% band (11.9%); "ON TRACK" (L318, L165) | Margin CONTRACTED −29bp YoY to the low end; deck basis 11.7% vs 12.0%; 65% of book fixed-price/commodity-exposed; capex-absorption (D +33%) pressures forward margin as unabsorbed depreciation lands | NO — already incorporated (Step 2 diag 2, 6B item 1 AMBER, 6D "low end") |
| 3 | Deck "healthy execution, disciplined growth"; PAT +3% YoY; revenue +5% (L149, deck s12) | Revenue +4% consol lands BELOW BEAR vs any growth band, laps a +81% base, annualises to ~Rs6,944cr vs Rs8,256-8,394cr implied by guidance; PAT +3% is 100% non-operating (core PBT ex-OI −6%, rescued by OI +45.9% and sub-statutory ETR 24.63%); normalise both → run-rate PAT flat-to-down | NO — already incorporated (Step 2 diag 3/4, Step 4 bridge, Step 6A "BELOW BEAR", flags L512) |

**Bonus positive (bull optionality):** capacity doubled + Butibori commissioned (L319). Bear counter: D +33% with zero revenue lift, ROCE 25.76→23.58 — cost precedes volume. Already incorporated (6D "DELAYED").

**No NEW surviving bear counter.** The one counter that survived the prior loop (order-book QoQ contraction) is now grafted and reconciles. Every bear counter constructible from the extract against A4's top positive claims is already present in the review. Nothing further requires grafting.

---

## VERDICT

- Audit 0 (deliverable): **PASS** — all four brief parts present and substantive.
- Audit 1 (coverage): **PASS** — independent re-enumeration matches A2 (31/90/4/23/17 results; 32/221 presentation); no material orphan row; no row missing from ledger.
- Audit 2 (arithmetic): **PASS** — every load-bearing derived metric recomputes to A4's value; two documented non-blocking observations (penny EBITDA rounding; redundant-but-non-distorting JV bridge line), neither above material tolerance.
- Audit 3 (adversarial): **PASS** — the prior surviving counter (order-book QoQ contraction) is grafted into Step 6D and the summary narrative and reconciles independently; no new surviving counter.

**VERDICT: COMPLETE.** Proceeds to Notion save. No loop-back.

```yaml
stage: A5-adversary
company: "TRANSRAILL"
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
