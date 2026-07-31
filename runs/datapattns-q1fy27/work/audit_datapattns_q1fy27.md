# A5 ADVERSARY / COMPLETENESS AUDIT — Data Patterns (India) Ltd (DATAPATTNS), Q1 FY27
**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Date:** 2026-07-31
**Loop:** 2 (final) | **Fresh context:** A4 review + A1 extracts + A2 ledgers only; re-derived independently, did not defer to A4's or A3's cites.

---

## PART 0 — VERIFICATION OF THE THREE LOOP-1 FIXES

| Loop-1 gap | Required fix | Verified state | Status |
|---|---|---|---|
| (a) Presentation ledger under-enumerated slide-24 WC table by 4 values (count 121 not reproducible) | Add 4 values, count → 125 | Ledger Table 6 now carries Debtor FY22=233 (l.823), Creditor FY22=30 (l.824), Inventory FY25=187 (l.836), Inventory FY26=108 (l.840); COUNT TEST `other_headline_stats` grep=125/sweep=125; grand gated total 922; A4 preamble line 18 reads "125 headline stats, incl. 20 values on slide 24" and 922 total | **FIXED** |
| (b) Step-5 inventory-days 108 mis-cited to l.837 | Re-cite to l.840 | A4 Step 5 line 201 now reads "Inventory days \| 108 (deck l.840, FY26)"; extract line 840 = 108 (line 837 = 164 + CCC 427/432/428, correctly the Inv-FY24/CCC row); CCC 428 still cited l.837, which is correct | **FIXED** |
| (c) Dangling concall-A3-07 `from_finding_id` | Resolve into the capex row in Step-8F and YAML | Step 8F row 4 (capex) `from_finding_id` = "A3-07, A3-15, DP-F6a"; YAML capex question `from_finding_id: "concall-A3-07, concall-A3-15, DP-F6a"`; A3-07 no longer orphaned; classified FORWARD-SIGNAL in preamble line 29 | **FIXED** |

All three loop-1 corrections are present and correct. No regression introduced: Table 7 dash-cell count unchanged at 43; the 4 added slide-24 values are plain disclosed figures, so no new ZERO_STANDING/NOT_FOUND flag applies.

---

## PART 1 — COVERAGE AUDIT (independent fresh enumeration vs A2 ledgers)

Fresh grep/sweep re-run over each A1 extract; diffed against the ledger COUNT TESTs; then every ledger row checked for an A4 citation or "reviewed, no finding".

| Category (doc) | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| results — notes | 8 | 8 (notes 2-7 + unnum. Note 1 l.174 + EPS footnote l.170) | none — A4 Step 0D | PASS |
| results — line_items | 27 | 27 (20 statement l.132-169 + 7 QIP l.199-207) | none — Step 1 + Note 4/DP-F6a | PASS |
| results — auditor_paras | 4 | 4 (l.76,82,89,98) | none — Step 0D | PASS |
| results — agenda_items | 1 | 1 (l.34 approval) | none — Step 0 | PASS |
| results — signature_blocks | 3 | 3 (CS l.47; auditor l.106; CMD l.219) | none — auditor timestamp → DP-F14a | PASS |
| results — entities | 0 | 0 (Note 5 zero-entity) | none — Step 0/Note 5 | PASS |
| acquisition — disclosure_fields | 10 | 10 (S.No 1-10) | none — Step 8.5 Q7-11 + Section C | PASS |
| acquisition — line_items (granular) | 24 | 24 (incl. gaps 10d incorporation, 10e country) | none — Q8 covers both | PASS |
| acquisition — quantitative_figures | 13 | 13 (Rs 10 Cr = 1.5 promoter + 8.5 loan; turnover 157.66/442.19/416.85 L; 1.3-2.0x; 3mo; 100%) | none | PASS |
| acquisition — signature_block | 8 | 8 | none | PASS |
| presentation — slides | 32 | 32 | none — preamble "all 32 reviewed" | PASS |
| presentation — pl_margin_values | 340 | 340 | none | PASS |
| presentation — orderbook_inflow | 98 | 98 | none | PASS |
| presentation — segment_customer | 63 | 63 | none | PASS |
| presentation — balance_cashflow | 296 | 296 | none | PASS |
| presentation — other_headline_stats | 125 | **125** (slide-24 re-swept = 20) | none | PASS |
| presentation — zero_standing | 43 | 43 | none | PASS |
| presentation — footnotes | 9 | 9 | none | PASS |
| concall — turns | 84 | 84 (39 Q + 28 A + 1 Mod + 1 Closing + 15 unbracketed) | none — preamble "all 84 reviewed" | PASS |
| concall — questions | 39 | 39 (28 substantive + 11 NO_NEW_QUESTION) | none — Step 4A inventory | PASS |
| concall — mgmt_numbers | 66 | 66 | none — Step 1 / Step 7A | PASS |

**Independent slide-24 re-derivation (the loop-1 locus):** Debtor Days 233/280/287/308/307 (FY22-26, l.820-823); Creditor Days 30/36/35/45/43 (FY22-26, l.820-824); Inventory Days 141/155/164/187/108 (FY22-26, l.836-840); CCC 329/365/427/432/428 (FY22-26, l.837-839). = 20 values, matching the corrected ledger exactly. No orphan, no missing-from-ledger row.

**A3-finding coverage:** all non-N.A. findings across four docs cited in A4 (results DP-F1a/F6a/F14a; acq F1/F6/F7/F11/F13/F14/F15/F17; presentation A3-F1-01…A3-F16-04; concall A3-01…A3-18). Formerly-dangling concall-A3-07 now anchored in the capex question row. No unreviewed row.

**COVERAGE RESULT: PASS** — no orphan rows (→A3), no rows my fresh pass found that the ledger lacks (→A2).

---

## PART 2 — ARITHMETIC AUDIT (recomputed from raw extracted numbers; ₹ Cr)

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+FC−OI) | 31.37 | 29.48+5.92+3.28−7.31 = 31.37 | l.149/142/141/133 | MATCH |
| Op EBITDA Q1FY26 | 32.08 | 33.95+5.49+3.19−10.55 = 32.08 | l.149/142/141/133 | MATCH |
| Op EBITDA Q4FY26 | 192.84 | 187.96+5.89+4.65−5.66 = 192.84 | l.149/142/141/133 | MATCH |
| Op EBITDA FY26 (pre-excep base) | 373.99 | 366.55+22.95+12.45−27.96 = 373.99 | l.149/142/141/133 | MATCH |
| Op EBITDA margin Q1FY27 | 27.04% | 31.37/116.03 = 27.04% | l.132 | MATCH |
| Op EBITDA margin Q1FY26 | 32.30% | 32.08/99.33 = 32.30% | l.132 | MATCH |
| Op EBITDA margin FY26 | 40.44% | 373.99/924.77 = 40.44% | l.132 | MATCH |
| Core PBT ex-OI Q1FY27 | 22.17 | 29.48−7.31 = 22.17 | l.154/133 | MATCH |
| Core PBT ex-OI Q1FY26 | 23.40 | 33.95−10.55 = 23.40 | l.154/133 | MATCH |
| Effective tax rate Q1FY27 | 25.17% | 7.42/29.48 = 25.17% | l.155/154 | MATCH |
| Effective tax rate Q1FY26 | 24.89% | 8.45/33.95 = 24.89% | l.155/154 | MATCH |
| Effective tax rate FY26 | 25.35% | 92.17/363.54 = 25.35% | l.155/154 | MATCH |
| PAT margin Q1FY27 | 19.01% | 22.06/116.03 = 19.01% | l.156/132 | MATCH |
| PAT margin Q4FY26 | 40.13% | 138.38/344.85 = 40.13% | l.156/132 | MATCH |
| YoY Revenue | +16.81% | 16.70/99.33 = +16.81% | l.132 | MATCH |
| YoY Op EBITDA | −2.21% | −0.71/32.08 = −2.21% | — | MATCH |
| YoY Op EBITDA margin | −526 bps | 27.04−32.30 = −5.26pp | — | MATCH |
| YoY Core operating PBT | −5.26% | −1.23/23.40 = −5.26% | — | MATCH |
| YoY Reported PBT | −13.17% | −4.47/33.95 = −13.17% | l.154 | MATCH |
| YoY PAT | −13.49% | −3.44/25.50 = −13.49% | l.156 | MATCH |
| YoY Other Income | −30.71% | −3.24/10.55 = −30.71% | l.133 | MATCH |
| Gross profit Q1FY27 (Rev−RM) | 91.51 | 116.03−(30.73−6.21) = 91.51 | l.132/137/139 | MATCH |
| Gross profit Q1FY26 | 79.23 | 99.33−(57.16−37.06) = 79.23 | l.132/137/139 | MATCH |
| PAT bridge (sum of components) | −3.44 | +12.28−6.15−6.84−0.43−0.09−3.24+1.03 = −3.44 | Step 4 | MATCH |
| OI-revert scenario PAT | ~24.5 | 32.72×(1−0.2517) = 24.49 | — | MATCH |
| FY26 CFO/PAT | 0.295x | 80.1/271.37 = 0.295x | deck l.998/l.156 | MATCH |
| Guidance Q2-Q4 avg needed (20% floor) | ~Rs 331/qtr | (1,109.7−116.03)/3 = 331.2 | — | MATCH |
| Order-book stack (deck) | 2,654.0 | 927.7+1,726.3 = 2,654.0 | deck l.330 | MATCH |
| Cash gap (call vs deck) | Rs 64 Cr | 530−465.9 = 64.1 | turn 11 / deck l.326 | MATCH |
| STAC turnover fall | ~5.7% | (442.19−416.85)/442.19 = 5.73% | acq l.127-128 | MATCH |
| Trade receivables Mar25→Mar26 | 596.4→727.8 | 5,964/7,278 Mn ×0.1 | deck l.964 | MATCH |

**Minor non-blocking observations (below FAIL threshold — no derived-metric error, no conclusion changes):**
1. **OI/PBT FY26 stated 7.63%** uses pre-exceptional PBT (27.96/366.55 = 7.63%); on reported PBT it would be 7.69%. The footnote-¹ cluster explicitly bases FY26 operating ratios on 366.55, so the basis is disclosed; 6 bps immaterial.
2. **Step-5 prose "CCC ~427-432 for FY23-FY25"** — the anchored cell (CCC FY26 = 428, l.837) is correct; the bars are FY24=427/FY25=432/FY26=428 (FY23=365), so the range better maps to FY24-FY25. Descriptive year-label only; every anchored figure and the structural-~430-day conclusion are sound. Not a derived-metric mismatch.

**ARITHMETIC RESULT: PASS** — no mismatch above rounding; PAT bridge closes; the concall spoken P&L (turn 11) reconciles to the filing at every line.

---

## PART 3 — ADVERSARIAL READ (strongest bear counter to the three most positive claims)

Testing whether the strongest bear counter to each top positive claim SURVIVES (supported by the extract AND absent from A4).

**Positive 1 — "Net cash intact, net-debt-free; Rs 465.9-530 Cr, far above the Rs 100 Cr tripwire (checklist #6 GREEN)."**
Bear (same text): the strength figure itself does not tie — Rs 530 Cr (call) vs Rs 465.9 Cr (deck) same-date, Rs 64 Cr unreconciled; capex RAISED to Rs 200 Cr+ against 0.30x CFO; Rs 26.25 Cr QIP undeployed 3.3 yrs; "ample flexibility" with Q1 CFO withheld.
**SURVIVES? NO** — already in A4 (Step 5 net-debt row, checklist #6 "GREEN but Rs 64 Cr gap flagged", A3-13/A3-15, Section C).

**Positive 2 — "Spoken P&L ties to the filing at every line — CONFIRMED."**
Bear (same text): the tie holds only for the P&L; the two spoken balance-sheet figures (cash Rs 530 Cr, order book Rs 920 Cr) do NOT tie to the deck — divergence exactly where no Reg-33 statement exists to check.
**SURVIVES? NO** — already in A4 Step 1 tie-out (line 104) and Step 7A.

**Positive 3 — "Order book Rs 2,654 Cr provides healthy revenue visibility; confirmed book stable."**
Bear (same text): ~65% negotiated/pending (only Rs 927.7 Cr confirmed), production-vs-development split REFUSED twice (turns 85/89), confirmed book flat (9,265→9,277), export OB Rs 39 Cr near the Rs 30 Cr tripwire, Rs 1,726 Cr conversion DELAYED from AGM.
**SURVIVES? NO** — already in A4 checklist #2/#3/#10, Step 7A, A3-F16-01/A3-08/A3-14, Section C flag 4.

**Cross-check on secondary positives** (revenue +16.8%; auditor unmodified; promoter-CMD candour; STAC accretion 1.3-2.0x): each already carries its bear counter — core-PBT −5.3% masking (Step 2), auditor 16:34-vs-board-18:30 governance flag (DP-F14a), OVERPROMISER-RISK / 0-of-18 specific answers (Step 6E/8.5), STAC turnover −5.7% + Rs 8.5 Cr liability-settlement loan + Rs 1.5 Cr not-RPT promoter payment (Q7/Q8, Section C flags 1-3). No new surviving counter.

**ADVERSARIAL RESULT: PASS** — no bear counter survives ungrafted; the review is symmetric bull-bear; nothing must be added to A4 before save.

---

## VERDICT

- Loop-1 fixes (a), (b), (c): all verified present and correct; no regression.
- Coverage: PASS (no orphan rows, no missing-from-ledger rows; slide-24 independently re-swept to 20 values / gated total 922).
- Arithmetic: PASS (all derived metrics reproduce; PAT bridge closes; two immaterial basis/label observations, neither a FAIL).
- Adversarial: PASS (all strongest bear counters already incorporated).

**VERDICT: COMPLETE.** Only COMPLETE proceeds to Notion save.

```yaml
stage: A5-adversary
company: "DATAPATTNS"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
