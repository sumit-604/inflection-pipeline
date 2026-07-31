# A5 ADVERSARY / COMPLETENESS AUDIT — Data Patterns (India) Ltd (DATAPATTNS), Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Date:** 2026-07-31
**Under audit:** `review_datapattns_q1fy27.md` (Role 4 full + Role 5 completed against the 84-turn transcript)
**Method:** fresh context. Re-derived every number from the A1 extracts at their own line/turn numbers; re-ran the A2 enumeration with an independent grep + manual sweep and diffed against each A2 ledger. Did not defer to A4's or A3's cites.

**VERDICT: INCOMPLETE.** One reproducible coverage gap: the A2 presentation ledger under-enumerates the page-24 working-capital slide by four values that my fresh pass found in the extract. Loop back to **A2**. All three audits were run in full; the arithmetic and adversarial audits PASS and every one of the four parent-flagged focus areas is substantively satisfied (details below). The failing item is mechanical and cheap to fix; the analytical substance of A4 is sound.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledger)

### 1A. Per-document / per-category count diff

| Doc | Category | A2 count | My fresh count | Diff | Status |
|---|---|---|---|---|---|
| results | numbered notes | 8 | 8 | 0 | PASS — all 8 in A4 Step 0D |
| results | line items | 27 | 27 (20 P&L rows @ l.132-169 + 7 QIP @ l.199-207) | 0 | PASS — P&L in Step 1, QIP in Step 0D/Note 4 |
| results | auditor paras | 4 | 4 (l.76,82,89,98) | 0 | PASS — unmodified conclusion + 16:34 timestamp (DP-F14a) in Step 0D |
| results | agenda items | 1 | 1 (l.34) | 0 | PASS |
| results | signature blocks | 3 | 3 | 0 | PASS |
| results | entities / annexures | 0 / 0 | 0 / 0 | 0 | PASS — Note 5 zero-subsidiary cited (Step 1/Section C) |
| acquisition | disclosure fields | 10 | 10 (S.No.1-10) | 0 | PASS — STAC covered in Step 8.5 Q7-11, flags, monitorables |
| acquisition | granular sub-items | 24 | 24 | 0 | PASS — incl. incorporation/country DISCLOSURE_GAP (Q8/Q10), turnover 157.66/442.19/416.85 L |
| acquisition | letter/header fields | 18 | 18 | 0 | PASS — approval "if any" contradiction (F1/F14) cited |
| acquisition | signature-block lines | 8 | 8 | 0 | PASS |
| concall | turns | 84 | 84 (39 Q + 28 A + 1 Moderator + 1 Closing + 15 unbracketed) | 0 | PASS — see 1B |
| concall | questions | 39 | 39 | 0 | PASS |
| concall | mgmt numbers | 66 | 66 (structure reconciled; key figures spot-verified) | 0 | PASS |
| concall | forward-commitment / hedge | 29 / 14 | 29 / 14 | 0 | PASS |
| presentation | slides | 32 | 32 (32 formfeeds) | 0 | PASS |
| presentation | P&L/margin (p14,18,28) | 340 | 340 | 0 | PASS |
| presentation | orderbook/inflow (p15-17) | 98 | 98 | 0 | PASS |
| presentation | segment/customer (p7,12,13) | 63 | 63 | 0 | PASS |
| presentation | balance/cashflow (p29,30) | 296 | 296 | 0 | PASS |
| presentation | **headline stats (13 slides, incl. p24)** | **121** | **125** | **+4** | **FAIL — see 1C** |
| presentation | zero-standing / footnotes | 43 / 9 | 43 / 9 | 0 | PASS |

### 1B. Concall turn/question reconciliation (independent grep)
Fresh grep: `[Q —` = 40 hits, `[A — Mgmt]` = 29 hits. Each count includes exactly one literal inside the A1 extraction header (line 17: "`[Q — <firm>] ... : 39`"; line 21: "`[A — Mgmt] ... : 28`"). Body-only: **39 question-turns, 28 answer-turns** → +1 Moderator (l.125) +1 Closing (l.171) +15 unbracketed operator/mgmt = **84 turns**, matching the ledger exactly. No orphan turn; no turn my pass found that the ledger lacks.

### 1C. FAIL — presentation ledger under-enumerates slide 24 (working capital)
My fresh read of the raw extract (page 24, "Working Capital", lines 820-840) finds **20** disclosed working-capital data values — five each for Debtor Days, Creditor Days, Inventory Days, and Cash Conversion Cycle:
- Debtor Days: 308, 307, 280, 287, **233** (l.823)
- Creditor Days: 45, 43, 36, 35, **30** (l.824)
- Inventory Days: **187** (l.836), 164, 155, 141, **108** (l.840)
- CCC: 427, 432, 428, 365, 329

The A2 presentation ledger (Table 6, rows at l.820/821/822/837/838/839) enumerates only **16** of these, omitting four cells: **Debtor FY22 = 233, Creditor FY22 = 30, Inventory FY25 = 187, Inventory FY26 = 108.** The ledger's stated methodology explicitly guarantees "each grouped row spells out every value it contains … No number is dropped." That guarantee is breached, and the category's "121 grep = 121 sweep" reconciliation is therefore not reproducible (true count = 125).

This is a **missing-from-ledger** condition → **loop back to A2** to re-enumerate slide 24 and re-run the count test. (Note this is peripheral to the thesis: the parent line items — Inventory Days, Debtor Days, CCC — ARE enumerated and cited; only these four historical cells are dropped, and A4 independently captured the FY26 inventory value 108 by reading the raw extract.)

### 1D. Orphan-row check (ledger rows absent from A4)
No orphan rows. Spot-verified that every thesis-relevant deck value A4 cites ties to the A2 ledger and the raw extract: revenue FY25 7,084 Mn=708.4 (l.454); other income 463 (l.912); EBITDA 314/321/1,928 (l.462); cash 4,659 Mn=465.9 (l.326); order book 9,277 Mn=927.7 (l.330); ROCE 20.8% (l.323); debtor days 307 / creditor 43 / CCC 428 (l.820/837); CFO FY26 801 Mn=80.1 (l.998); WC movement -2,114 (l.994); trade receivables 5,964→7,278 Mn=596.4→727.8 (l.964); PPE 1,606 / CWIP 132 (l.943/945); intl OB 39 Cr (l.566); Q1 inflow 1,172 Mn=117.2 Cr (l.548); planned capex 150 Cr (l.182). All present and correctly used.

**Minor A4 cite imprecision (not a coverage fail):** A4 Step 5 cites "Inventory days 108 (deck l.837, FY26)". The value 108 sits at l.840; l.837 holds 164 + the CCC values. The number is correct and real; only the line pointer is off by three.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract; ₹ Cr)

Every derived metric in A4's tables recomputes to A4's stated value within rounding. No mismatch found.

| Metric | A4 value | My recompute (source) | Status |
|---|---|---|---|
| Operating EBITDA Q1FY27 (PBT+D+FC−OI) | 31.37 | 29.48+5.92+3.28−7.31 = 31.37 (l.149/142/141/133) | PASS |
| Operating EBITDA Q1FY26 | 32.08 | 33.95+5.49+3.19−10.55 = 32.08 | PASS |
| Operating EBITDA Q4FY26 | 192.84 | 187.96+5.89+4.65−5.66 = 192.84 | PASS |
| Op EBITDA margin Q1FY27 | 27.04% | 31.37/116.03 = 27.036% | PASS |
| Op EBITDA margin Q1FY26 | 32.30% | 32.08/99.33 = 32.30% | PASS |
| Op EBITDA margin YoY | −526 bps | 27.04−32.30 = −5.26pp | PASS |
| Reported EBITDA Q1FY27 (PBT+D+FC) | 38.68 | 29.48+5.92+3.28 = 38.68 | PASS |
| Core PBT ex-OI Q1FY27 / Q1FY26 | 22.17 / 23.40 | 29.48−7.31 / 33.95−10.55 | PASS |
| Core PBT ex-OI YoY | −5.26% | (22.17−23.40)/23.40 = −5.26% | PASS |
| Effective tax rate Q1FY27 | 25.17% | 7.42/29.48 = 25.17% | PASS |
| ETR FY26 (post-exceptional) | 25.35% | 92.17/363.54 = 25.35% | PASS |
| PAT margin Q1FY27 | 19.01% | 22.06/116.03 = 19.01% | PASS |
| Revenue YoY | +16.81% | (116.03−99.33)/99.33 = 16.81% | PASS |
| Other Income YoY | −30.71% | (7.31−10.55)/10.55 = −30.71% | PASS |
| Reported PBT YoY | −13.17% | (29.48−33.95)/33.95 | PASS |
| PAT YoY | −13.49% | (22.06−25.50)/25.50 | PASS |
| Gross profit Q1FY27 (Rev−net matl) | 91.51 | 116.03−(30.73−6.21) = 91.51 (ties spoken GP l.61) | PASS |
| Gross profit Q1FY26 | 79.23 | 99.33−(57.16−37.06) = 79.23 | PASS |
| PAT bridge sum | −3.44 | +12.28−6.15−6.84−0.43−0.09−3.24+1.03 = −3.44 | PASS |
| FY26 op EBITDA vs deck 371 recon | Δ = exceptional | 373.99−371.0 = 2.99 ≈ 3.01 (Labour Code) | PASS |
| **Cash reconciliation gap** | **Rs 64 Cr** | 530.0 (concall l.61) − 465.9 (deck l.326) = 64.1 | PASS — named, not silently resolved |
| Order-book stack (deck) | 2,654.0 | 927.7 + 1,726.3 = 2,654.0 | PASS |
| Order-book stack (spoken) | Rs 8 Cr gap | 920 + 1,726 = 2,646 vs 2,654 | PASS |
| STAC total outlay | Rs 10 Cr | 1.50 (equity) + 8.50 (loan) (l.112-114) | PASS |
| STAC turnover dip FY25→FY26 | ~5.7% | (416.85−442.19)/442.19 = −5.73% | PASS |

**Role 4 numbers unchanged from the prior audited version: CONFIRMED.** Every Section A figure recomputes identically; A4's own statement that "Role 4 numbers are unchanged" holds under independent recomputation.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear from the same text)

A4 is already a comprehensively bearish document. I took its three most favourable claims and built the strongest bear counter for each from the identical extracted text; in every case the counter is already surfaced inside A4, so **no surviving counter needs grafting**.

**Positive claim 1 — "Net cash intact, Rs 465.9-530 Cr, far above the Rs 100 Cr tripwire; watchlist item 6 GREEN; net-debt-free maintained."**
Bear from same text: the two same-date cash figures do not tie (Rs 64 Cr gap, l.61 vs l.326); FY26 CFO/PAT is only 0.295x (80.1/271.37, l.998); FY26 working capital absorbed −Rs 211.4 Cr (l.994); Rs 26.25 Cr of QIP is still undeployed 3.3 yrs on (Note 4); a fresh ~Rs 2 Cr receivables provision was booked (turn 17). The "strong balance sheet" rests on a number that does not reconcile plus undeployed raised capital.
→ **Already incorporated** (A4 Step 5, Section C flags 1-4, watchlist item 6 "GREEN but Rs 64 Cr gap flagged"). Does not survive as new.

**Positive claim 2 — "Spoken P&L ties to the filing at every line (CONFIRMED); revenue +16.8% YoY growth."**
Bear from same text: +16.8% is below management's own 20-25% guide; operating EBITDA −2.2%, core operating PBT −5.3%, margin −526 bps — "confirmed" only means the soft print is real, and the growth headline masks operating deterioration.
→ **Already incorporated** (A4 Step 2 diagnostics 1-3, the stated "core signal"). Does not survive as new.

**Positive claim 3 — "Order book Rs 2,654 Cr provides healthy multi-year revenue visibility; no thesis-broken trigger fired; auditor unmodified."**
Bear from same text: only Rs 927.7 Cr is confirmed (~65% negotiated/soft); production-vs-development split REFUSED twice (turns 85/89); confirmed book flat QoQ (9,265→9,277, l.180); the Rs 1,726 Cr negotiated conversion is DELAYED (+6mo/+2mo, turn 25); the "unmodified" report was signed 16:34 vs board concluded 18:30 (DP-F14a).
→ **Already incorporated** (A4 checklist items 2/3/12, Step 6C, Section C flags 4/13/1). Does not survive as new.

**Result: no bear counter survives un-incorporated.** Adversarial completeness PASS.

---

## PARENT FOCUS-AREA CONFIRMATIONS

1. **All 18 pre-committed questions graded, each with a concall cite — SATISFIED.** The Step 8.5 Addendum grades all 18 (tally 0 ANSWERED-SPECIFICALLY / 7 PARTIAL / 2 EVADED / 9 NOT-ADDRESSED; counts verified: PARTIAL #2,3,11,12,13,14,18; EVADED #4,15; NOT-ADDRESSED #1,5,6,7,8,9,10,16,17 = 18). Each carries a turn cite; the four NOT-ADDRESSED items with no near-miss turn correctly carry "(no utterance)" as the silence cite (Q5, Q9, Q10, Q17), which is the honest anchor for a question management never spoke to.
2. **Rs 530 vs Rs 465.9 Cr cash — NAMED, not silently resolved — SATISFIED.** Carried as a Rs 64 Cr UNRECONCILED gap in Step 1, Step 5, Step 7A, Section C, a Section-8F forward question, a monitorable, and a top-level flag; deck figure anchored, spoken figure not credited. Recomputed 530−465.9 = 64.1.
3. **Every concall FORWARD-SIGNAL/AMBIGUOUS finding → a management question — SUBSTANTIALLY SATISFIED, one traceability defect.** Concall A3-02..06, 08-13, 15-17 each map to a Section-8F question or monitorable with an explicit `from_finding_id`; A3-01 (cost-drag) and A3-14 (order-book rounding) are carried as resolved signals. **Exception:** A4's line-29 contract asserts FORWARD-SIGNAL **A3-07** is "carried to 8F with an explicit from_finding_id," yet **concall-A3-07 appears nowhere in the review except lines 27/29** — no 8F row, monitorable, flag, or YAML entry references it. Its probable substance (export / counter-drone forward traction) IS covered elsewhere (monitorables, checklist item 10, Step 5A), so this is a traceability/labelling defect rather than a missed forensic; I cannot fully adjudicate it because the A3 ledger is (by design) outside my inputs. Routed to **A4** to either add the A3-07 question with its `from_finding_id` or correct the line-29 assertion. This is a secondary finding; it is **not** the basis for the INCOMPLETE verdict.
4. **Role 4 numbers unchanged — CONFIRMED** by full independent recomputation (Audit 2).

---

## VERDICT

**INCOMPLETE.**
- **Loop back to A2 (primary):** the presentation ledger's slide-24 working-capital enumeration is provably incomplete — Debtor FY22 = 233 (extract l.823), Creditor FY22 = 30 (l.824), Inventory FY25 = 187 (l.836), Inventory FY26 = 108 (l.840) are present in the extract but absent from the ledger, so the "121 headline-stats grep = sweep" reconciliation is not reproducible (true = 125) and the ledger's "no number dropped" guarantee is breached. Re-enumerate slide 24 and re-run the count test.
- **Secondary, route to A4:** reconcile the A3-07 traceability defect (line-29 claim vs no visible `from_finding_id`), and correct the Step-5 cite pointer for inventory-days 108 (l.840, not l.837).
- Arithmetic audit and adversarial audit both PASS; all four parent focus areas are substantively satisfied. Once A2 re-enumerates slide 24 (and A4 reconciles the A3-07 label), the review is clear to proceed.

```yaml
stage: A5-adversary
company: "DATAPATTNS"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger:
    - {doc: presentation, category: headline_stats_slide24, value: "Debtor Days FY22 = 233", extract_line: 823, note: "absent from A2 presentation ledger Table 6"}
    - {doc: presentation, category: headline_stats_slide24, value: "Creditor Days FY22 = 30", extract_line: 824, note: "absent from A2 presentation ledger Table 6"}
    - {doc: presentation, category: headline_stats_slide24, value: "Inventory Days FY25 = 187", extract_line: 836, note: "absent from A2 presentation ledger Table 6"}
    - {doc: presentation, category: headline_stats_slide24, value: "Inventory Days FY26 = 108", extract_line: 840, note: "absent from A2 ledger; A4 cited it as l.837 (actual l.840)"}
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: "A2"
gap: "A2 presentation ledger under-enumerates page-24 working-capital slide by 4 values (Debtor FY22=233 l.823, Creditor FY22=30 l.824, Inventory FY25=187 l.836, Inventory FY26=108 l.840); headline-stats count is 125 not the ledger's 121, so the count test is not reproducible and the 'no number dropped' guarantee is breached. Secondary (A4): concall-A3-07 asserted at line 29 as carried to Step 8F with a from_finding_id but appears in no 8F row/monitorable/flag/YAML; and Step-5 inventory-days 108 is cited to l.837 but sits at l.840."
```
