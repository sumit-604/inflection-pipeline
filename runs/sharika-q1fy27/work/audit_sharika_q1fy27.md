# A5 ADVERSARY / COMPLETENESS AUDIT — Sharika Enterprises Limited (SHARIKA), Q1FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Verdict:** INCOMPLETE (arithmetic FAIL, loop back to A4)
**Under audit:** `review_sharika_q1fy27.md` | **Re-derived from:** `extract_results_sharika_q1fy27.txt` (597 lines), `ledger_results_sharika_q1fy27.md`
Fresh context; A4/A3 cites were checked, not trusted. All ₹ Cr figures independently recomputed from raw ₹-lakh source lines (×0.01).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

The PLAIN-LANGUAGE BRIEF (review lines 465-483) carries all four labelled parts, each with real content:

| Part | Location | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | l.467-468 | **PRESENT** | ~18-line narrative; numbers-first; symmetric bull/bear; states AVOID maintained |
| (2) Sector intelligence | l.470-473 | **PRESENT** | Power EPC / smart-grid, copper pass-through risk, scheme tailwinds, provenance-tagged |
| (3) Business-model intelligence | l.475-478 | **PRESENT** | B2B EPC + Spintech software pivot, pre-revenue subs, no b/s buffer |
| (4) Competition intelligence | l.480-483 | **PRESENT** | Named peers (Rajesh Power, Viviana), ICR/margin/CAGR contrast, provenance-tagged |

**GATE 0: PASS.** All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

Fresh grep/manual sweep of the extract, diffed against the A2 COUNT TEST:

| Category | A2 count | My fresh count | Method / lines | Orphan rows | Status |
|---|---|---|---|---|---|
| Agenda items | 1 | 1 | Board letter l.73-75 (single approval item; no other resolution) | 0 | PASS |
| Notes | 20 | 20 | SA l.297,299,302,305,309,315,321,325,329,336 (10) + CA l.560,562,564,567,570,574,579,582,585,588 (10) | 0 | PASS |
| Line items | 61 | 61 | SA P&L l.251-293 = 26; CA P&L l.504-555 = 35 | 0 | PASS |
| Auditor paras | 28 | 28 | SA report 14 (l.119-232) + CA report 14 (l.351-477) | 0 | PASS |
| Signature blocks | 24 | 24 | 5 groups: board letter, SA auditor, SA director, CA auditor, CA director | 0 | PASS |
| Zero-standing | 8 | 8 | SA rows 12/14/16 (l.263/266/268) = 3; CA rows 13/15/17/19/29 (l.518/520/523/525/541) = 5 | 0 | PASS |
| Entities | 4 | 4 | Holding + Spintech + Smartec + Contronics (l.388-392); JV Electromeccanica excluded per Note 10 | 0 | PASS |

**Fresh count matches the ledger exactly on all seven categories. No row my pass found is missing from the ledger; no ledger row is orphaned.**

**Ledger-row → A4 traceability (every certified row cited or marked reviewed):**
- All 20 notes: covered in Step 0D structured table (notes 1-10 with SA+CA line refs). ✓
- 61 line items: reproduced in Step 1A/1C reported tables. ✓
- 28 auditor paras: Step 0D auditor-opinion check (3 BFQO counts + EOM asymmetry). ✓
- 24 signature blocks: preamble "24 signature/certification blocks (5 groups) — all reviewed"; MD signatory (Kaul l.340/593) cited in T4. FRN-illegible / UDIN-low-confidence / DIN-low-confidence data-quality flags are reviewed-no-finding (data-quality, not forensic). ✓
- 8 zero-standing: Step 1 tables mark each ND(nil, ZERO_STANDING); empty Exceptional Items line tied to Q1/F1-a. ✓
- 4 entities + JV exclusion: Step 5B + F15-a/Q10. ✓
- 1 agenda + LONG_MEETING_SINGLE_ITEM flag: F13-a/Q9 (5.5-hour single-item meeting). ✓
- SOURCE_DOCUMENT_INCONSISTENCY (514.63 vs 514.68): flags list + F14-a + Note 6 row. ✓

**COVERAGE: PASS.** No orphan rows (A3 clean); no rows missing from ledger (A2 clean).

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw lakhs)

Raw source lines confirmed: SA l.251-293, CA l.504-555. Spot-verified conversions and every derived cell in Steps 1B, 1D, 2, 4, 5B. Representative recomputations (all in ₹ Cr from raw lakh):

| Metric | A4 value | My recomputed | Source line(s) | Status |
|---|---|---|---|---|
| SA Op EBITDA Q1FY27 = PBT+D+FC−OI | 1.28 | (31.88+22.60+88.67−15.04)/100 = 1.28 | l.262/259/258/252 | PASS |
| SA Op EBITDA margin Q1FY27 | 5.77% | 128.11/2219.83 = 5.77% | l.262.. | PASS |
| SA Core PBT ex-OI Q1FY27 | 0.17 | (31.88−15.04)/100 = 0.17 | l.262/252 | PASS |
| SA ETR Q1FY27 | 28.3% | 9.02/31.88 = 28.3% | l.267/262 | PASS |
| CA Op EBITDA Q1FY27 | 1.48 | (40.97+28.89+89.49−11.56)/100 = 1.48 | l.516/513/512/505 | PASS |
| CA Op EBITDA margin Q1FY27 | 6.66% | 147.79/2220.07 = 6.66% | l.516.. | PASS |
| SA Rev YoY | +31.5% | (2219.83−1687.88)/1687.88 = 31.5% | l.251 | PASS |
| CA Rev YoY | +26.7% | (2220.07−1751.80)/1751.80 = 26.7% | l.504 | PASS |
| SA margin YoY (bps) | +978 | 5.77−(−4.01) = +9.78pp | l.262/259/258/252 | PASS |
| CA margin YoY (bps) | +1307 | 6.66−(−6.41) = +13.07pp | l.516.. | PASS |
| SA Finance cost YoY | +85.5% | (88.67−47.81)/47.81 = 85.5% | l.258 | PASS |
| SA material-cost ratio Q1FY26→Q1FY27 | 86.6%→79.8% | 1461.31/1687.88=86.6%; 1770.87/2219.83=79.8% | l.255/256/251 | PASS |
| SA gross margin Q1FY26→Q1FY27 | 13.4%→20.2% | 100−86.6=13.4; 100−79.8=20.2 | l.255/256/251 | PASS |
| SA-vs-CA gap Q1FY27 | +0.07 (+30.6%) | (29.86−22.86)/100=+0.07; 7.00/22.86=30.6% | l.527/274 | PASS |
| SA-vs-CA gap FY26 | −1.20 (15.5%) | −119.64/100=−1.20; 119.64/770.51=15.5% | l.527/274 | PASS |
| Subs incremental employee cost | +0.29 | (173.79−145.05)/100 = 0.29 | l.511/257 | PASS |
| ICR SA Q1FY27 | ~1.19x | EBIT 105.51 / FC 88.67 = 1.19 | l.262/259/258 | PASS |
| SA receivables ∆ YoY | −5.56 | 48.62−54.18(Notion) = −5.56 | l.186 | PASS |
| **Step 4 bridge: SA GP Q1FY26→Q1FY27 (memo)** | **₹2.27 → ₹4.45** | **2.27 → ₹4.49** (2219.83−1573.50−197.37=448.96 lakh) | **l.251/255/256** | **FAIL** |
| **Step 4 bridge: combined GP uplift** | **+2.18** | **+2.22** (448.96−226.57=222.39 lakh) | **l.251/255/256** | **FAIL** |
| Step 4 bridge: Depreciation change | (0.06) | (22.60−17.18)/100 = 0.0542 → (0.05) | l.259 | BORDERLINE (0.006 over rounding) |

### The arithmetic FAIL, shown

**Step 4 PAT bridge, standalone (review l.234):** `— combined gross-profit uplift (memo: GP ₹2.27→₹4.45 Cr) | +2.18`.

- Gross profit = Revenue − Cost of materials − Sub-contracting (A4's own gross-margin definition, which yields 13.4%→20.2%).
- Q1FY27 GP = 2219.83 − 1573.50 − 197.37 = **448.96 lakh = ₹4.49 Cr** (A4 wrote ₹4.45 Cr).
- Q1FY26 GP = 1687.88 − 1340.21 − 121.10 = 226.57 lakh = ₹2.27 Cr (agrees).
- Uplift = 448.96 − 226.57 = **222.39 lakh = +₹2.22 Cr** (A4 wrote +₹2.18 Cr).
- Discrepancy = **0.04 Cr (₹4 lakh), ~8× the 0.005 Cr rounding tolerance at 2-dp Cr.**

**This is not a presentation-rounding artifact — it makes A4's own bridge fail to foot.** Summing A4's stated components:
+2.18 −0.20 −0.07 −0.06 −0.41 +0.11 −0.37 +0.00 = **+1.18**, but the stated "Reported PAT YoY change" is **+1.24** (−1.01→+0.23, which is exact). A 0.06 unreconciled gap.
Using the correct GP uplift +2.22 (and dep −0.05): +2.22 −0.20 −0.07 −0.05 −0.41 +0.11 −0.37 = **+1.23 ≈ +1.24**, which foots. The corrected figure is confirmed by the independent recompute AND by the bridge closing.

Note: A4's narrative conclusion (the turn is core/recurring, PAT +₹1.24 Cr, AVOID maintained) is directionally unaffected — but the mandate is explicit: any derived-metric mismatch above rounding = FAIL. The bridge as printed does not reconcile and must be corrected before Notion save.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims + strongest bear from same text)

**Claim 1 (review l.538, 468):** "First POSITIVE operating quarter is genuine core signal movement (gross margin 13.4%→20.2%), not treasury."
- **Strongest bear (same extract):** The margin recovery is a material-cost-ratio move (86.6%→79.8%, l.255/256/251) with **no disclosed pass-through/escalation clause anywhere in the filing** — commodity-cycle luck, not a structural fix; the only positive comparator (Q4FY26) is a Note 4 **balancing figure** (l.305), and Q2/Q3FY26 are absent, so the "recovery" rests on one un-audited quarter vs a derived trough. Finance costs +85.5% (l.258) and DTA reversing (l.267) sit against it.
- **Survives?** YES as a valid bear — but **already grafted** into A4 (sector intel l.472 "reads as commodity-cycle luck"; Step 3 balancing-figure caveat; Step 6D "1 quarter, unverified durability"). No new graft required.

**Claim 2 (review l.290-292):** "Subsidiaries ADDITIVE — consolidated PAT (0.30) now exceeds parent (0.23) while NCI is a loss."
- **Strongest bear (same extract):** The consol uplift is an **accounting/elimination effect**, not a subsidiary turnaround — CA carries a ₹0.34 Cr change-in-inventories credit (l.510, no SA equivalent) and lower consol other-expenses, while subs add ₹0.29 Cr employee cost + ₹0.06 Cr depreciation on only ₹0.24 **lakh** incremental external revenue (l.504 vs l.251). Subs are pre-revenue cost centres.
- **Survives?** YES — but **already grafted** (Step 5B l.292 explicitly, F2-a/F3-a, Q2/Q3). No new graft required.

**Claim 3 (review l.167, 455):** "Revenue +31.5% SA YoY — strong growth."
- **Strongest bear (same extract):** Off a **distressed base** (Q1FY26 was the copper-spike quarter that broke the fixed-price contracts); sequentially it is only +2.2% (21.73→22.20, l.251), and Q4FY26 already annualised near the same run-rate — so YoY overstates momentum. No order book, no guidance, no scheme-linked win disclosed (l.silence).
- **Survives?** YES — but **already grafted** (Step 2C #1 "off a distressed base"; Step 3 QoQ caveat; competition intel l.482). No new graft required.

**Adversarial result:** all three strongest bear counters are supported by the extract and survive, but **A4 has already incorporated each** — no surviving bear counter is absent from the review, so none needs to be grafted. (A4's review is bear-complete on the narrative; the failure is arithmetic, not omission.)

---

## VERDICT

**INCOMPLETE.**
- **Failing agent:** A4.
- **Exact gap:** Step 4 standalone PAT bridge (review l.234) states GP ₹2.27→**₹4.45** Cr and combined GP uplift **+₹2.18** Cr; correct from raw (l.251/255/256) is GP ₹2.27→**₹4.49** Cr and uplift **+₹2.22** Cr. The error (0.04 Cr, ~8× rounding) causes A4's bridge to sum to +₹1.18 Cr against a stated Reported PAT YoY change of +₹1.24 Cr — the bridge does not foot. Correct the GP-uplift memo (and the ₹0.06→₹0.05 depreciation line) so the bridge reconciles to +₹1.24 Cr, then re-submit.

Gate 0 (deliverable brief), Coverage (A2/A3), and Adversarial-read (A4 bear-completeness) all PASS. The sole failing item is the A4 arithmetic slip above. All other derived metrics recomputed clean.

```yaml
stage: A5-adversary
company: "SHARIKA"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "Step 4 PAT bridge: SA gross profit Q1FY27 (memo)"
    a4_value: "4.45"
    recomputed: "4.49"
    source_line: "l.251/255/256 (2219.83-1573.50-197.37=448.96 lakh)"
  - metric: "Step 4 PAT bridge: combined gross-profit uplift YoY"
    a4_value: "+2.18"
    recomputed: "+2.22"
    source_line: "l.251/255/256 (448.96-226.57=222.39 lakh); bridge foots to +1.24 only at +2.22"
  - metric: "Step 4 PAT bridge: depreciation change YoY (secondary/borderline)"
    a4_value: "0.06"
    recomputed: "0.05"
    source_line: "l.259 (22.60-17.18=5.42 lakh = 0.0542 Cr)"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Step 4 SA PAT bridge arithmetic: GP 2.27->4.45 and uplift +2.18 should be 2.27->4.49 and +2.22; as printed the bridge sums to +1.18 vs stated Reported PAT YoY +1.24 (does not foot). Correct GP-uplift memo (and dep 0.06->0.05) so the bridge reconciles to +1.24, then re-submit."
```
