# A5 ADVERSARY / COMPLETENESS AUDIT — GE Power India (GVPIL) — Q1 FY27

Fresh context: audited against the A4 review, the A1 extract, and the A2 ledger only.
Every metric below re-derived from raw extract lines; A4/A3 cites were checked, not trusted.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The A4 review carries a "PLAIN-LANGUAGE BRIEF (mandatory standing deliverable)" block (review L373-389)
with all four labelled parts present and carrying real content:

| Part | Heading present | Non-empty / real content | Status |
|---|---|---|---|
| 1. Summary narrative (10-20 lines) | Yes (L375-377) | Yes — full narrative, revenue/margin/PAT, cautions, price vs re-entry | PRESENT |
| 2. Sector intelligence | Yes (L379-381) | Yes — thermal-equipment bifurcation, FGD exit, Labour Codes, provenance-tagged | PRESENT |
| 3. Business-model intelligence | Yes (L383-385) | Yes — two revenue engines, model drift to services, tax/cash caveats | PRESENT |
| 4. Competition intelligence | Yes (L387-389) | Yes — BHEL/Thermax/ISGEC/Siemens, aftermarket moat, oOEM% gap | PRESENT |

GATE 0 = PASS. All four brief parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh grep/manual re-enumeration vs A2 ledger)

Re-enumerated each category independently off the extract (621 lines, 9 pages).

| Category | A2 count | My fresh count | Basis | Orphan / extra | Status |
|---|---|---|---|---|---|
| notes | 17 | 17 | Standalone 8 (L230,234,247,266,273,283,288,292,296) + Consolidated 9 (L486,489,492,505,525,532,542,546,549,552) | none | MATCH |
| line_items | 94 | 94 | Standalone P&L 40 + Consolidated P&L 44 + 2 embedded discontinued-ops tables (5+5) | none | MATCH |
| zero_standing | 15 | 15 | 7 standalone (L193,197,203,206,207,208,219) + 8 consolidated (L447,451,457,460,461,462,470,475) | none | MATCH |
| agenda_items | 2 | 2 | approval of results (L51-53) + noting LRR (L52-54) | none | MATCH |
| auditor_paras | 10 | 10 | Standalone LR 4 + Consolidated LR 6 (incl Other-Matters para L385-395) | none | MATCH |
| entities | 2 | 2 | GE Power Boilers Services (subsidiary, L365/486) + NTPC GE JV (L366/487) | none | MATCH |
| signature_blocks | 5 | 5 | Vipul Sharma CS (L69-85); Khurana standalone (L143-155) + consolidated (L398-408); Bhatla standalone (L301-308) + consolidated (L555-562) | none | MATCH |
| media_release_items | 8 | 8 | headline + 4 financial bullets + backlog bullet + MD quote + about/contact (L570-621) | none | MATCH |
| turns / questions / slides | 0 | 0 | no concall / no deck supplied — Role 5 not run | none | MATCH |

Ledger-row → A4 citation check: every A2 table row is either cited in A4 or subsumed under a
"reviewed" statement. The material notes (2(i)/3(i) Durgapur-JSW demerger, 3 Labour Codes, 4/5 BHEL,
5/6 single segment, 8/9 balancing figure) are each carried into A4 Step 0D and downstream. Signature
blocks (MD-alone signature, absent CFO countersignature, two distinct UDINs), both entities, both
agenda items, the 15 zero-standing rows (exceptional nil, deferred tax nil), and all 8 media units
(backlog -41.4%, EBITDA 22.5%/15.6%) are cited. The two FORMATTING_GAP flags (L447, L468) are OCR
artifacts on nil rows, not findings; no citation owed.

**No orphan rows. No rows my fresh pass found that the ledger lacks. COVERAGE = PASS.**

---

## AUDIT 2 — ARITHMETIC (recompute every derived metric from raw extract)

Raw (Rs Cr = filing millions x0.1). Standalone continuing ops unless noted.

### 2A. Data-extraction tables (Step 1) — all tie to raw lines
Spot-recompute of the load-bearing conversions: Revenue Q1FY27 3,086.9m=308.69 (L176); Other income
318.8m=31.88 (L177); PBT-cont 688.2m=68.82 (L191/194); Current tax 28.3m=2.83 (L196); PAT-cont
659.9m=65.99 (L198); Net profit 525.5m=52.55 (L210). Consolidated Q1FY26 revenue 2,868.5m=286.85 (L428
vs standalone 286.73 L176 — A4 correctly distinguishes). JV share 11.8m=1.18 (L443). All Step 1A/1B
cells verified against L176-224 / L428-480. **No mismatch.**

### 2C/2D. Derived metrics — recomputed
| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+Fin-OI) | 44.72 | 68.82+3.27+4.51-31.88 = 44.72 | L191,186,185,177 | OK |
| Op EBITDA Q4FY26 | 106.76 | 118.85+3.01+4.37-19.47 = 106.76 | L191,186,185,177 | OK |
| Op EBITDA Q1FY26 | (0.07) | 44.02+3.43+5.58-53.10 = (0.07) | L191,186,185,177 | OK |
| Op EBITDA FY26 (uses PBT pre-except 339.90) | 259.44 | 339.90+12.28+21.90-114.64 = 259.44 | L191,186,185,177 | OK |
| Op EBITDA margin Q1FY27 | 14.5% | 44.72/308.69 = 14.49% | — | OK |
| Reported EBITDA margin on Total Income Q1FY27 | 22.5% | 76.60/340.57 = 22.49% (=media release 22.5% L586) | — | OK |
| Reported EBITDA margin on Total Income Q1FY26 | 15.6% | 53.03/339.83 = 15.60% (=media release 15.6% L586) | — | OK |
| Core PBT ex-OI Q1FY27 | 36.94 | 68.82-31.88 = 36.94 | — | OK |
| Effective tax rate Q1FY27 | 4.1% | 2.83/68.82 = 4.11% | — | OK |
| PAT margin Q1FY27 | 21.4% | 65.99/308.69 = 21.38% | — | OK |
| BHEL reversals FY26 total | 105.05 | 23.5+37.18+44.37 (L277-278) | — | OK |
| Adj Q4 Op EBITDA / adj FY26 Op EBITDA | 62.39 / 154.4 | 106.76-44.37 / 259.44-105.05 = 62.39 / 154.39 | — | OK |
| YoY Revenue | +7.66% | (308.69-286.73)/286.73 = +7.66% | — | OK |
| YoY Finance / Dep / OI | -19.2% / -4.7% / -40.0% | -19.18% / -4.66% / -39.96% | — | OK |
| YoY Net Profit / EPS-total | +66.2% / +66.4% | 20.94/31.61=66.24% ; 3.12/4.70=66.4% | L210, L223 | OK |
| S-vs-C PAT gap % (of standalone) | 2.2/10.3/9.8/6.9 | 1.18/52.55=2.2; 10.57/102.64=10.3; 3.11/31.61=9.8; 16.25/236.36=6.9 | — | OK |
| JV % of consol PBT | 1.7/8.2/6.4/4.5 | 1.18/70.00; 10.60/129.42; 3.00/47.13; 16.17/356.15 | — | OK |
| NTPC JV QoQ / YoY | -89% / -61% | (1.18-10.60)/10.60=-88.9%; (1.18-3.00)/3.00=-60.7% | L443 | OK |
| Un-taxed PAT/qtr @25.17% | ~14.5 | 68.82x0.2517 - 2.83 = 14.49 | — | OK |
| Backlog decline | -41.4% | (1545.4-2635.3)/2635.3 = -41.4% | L590-592 | OK |

### 2E. PAT BRIDGE (Step 4) — **FAILS TO FOOT**
A4 Step 4 table (review L193-202) lists these YoY-change components summing to a stated total of +20.94:

| Component | A4 (Rs Cr) |
|---|---|
| Core operating PBT (ex-OI) | +46.02 |
| Depreciation change | +0.16 |
| Finance cost change | +1.07 |
| Other Income change | (21.22) |
| Effective tax rate change | (2.83) |
| Exceptional items | 0.00 |
| Discontinued ops change | (1.03) |
| **Stated Reported Net Profit change** | **+20.94** |

Sum of the seven components = 46.02 + 0.16 + 1.07 − 21.22 − 2.83 + 0.00 − 1.03 = **+22.17**, not +20.94.
The bridge over-adds by exactly **+1.23 Cr = the +0.16 depreciation + +1.07 finance rows counted twice.**

Root cause (mechanical, not a rounding issue): A4's "Core operating PBT (ex-OI)" row uses +46.02, which
is the PBT−OI swing and therefore ALREADY embeds the depreciation reduction (+0.16) and finance-cost
reduction (+1.07). Listing dep and finance again as separate positive rows double-counts them. A4's own
Step 2 diagnostic 4 (review L161) states the correct identity: "Net continuing-PBT change +Rs 24.80 Cr =
core +46.02 less OI 21.22" — i.e. 46.02 already nets dep and finance, leaving no room for the two extra
rows. Step 4 therefore contradicts Step 2.

Correct bridge (either fix foots to +20.94):
- Option A — restate row 1 as the operating-EBITDA swing +44.79 (= 44.72 − (−0.07)); then
  44.79 + 0.16 + 1.07 − 21.22 − 2.83 + 0 − 1.03 = **+20.94** ✓
- Option B — keep core PBT +46.02 and DELETE the dep and finance rows; then
  46.02 − 21.22 − 2.83 + 0 − 1.03 = **+20.94** ✓

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Step 4 PAT bridge foot | components sum +22.17 vs stated total +20.94 | must sum to +20.94 (row1 = +44.79, or drop dep+finance rows) | review L193-202; raw L176-210 | **FAIL** |

Note: the +20.94 total itself is correct (52.55 − 31.61, L210), and every individual component value is
correct in isolation; the defect is the double-count that breaks the bridge identity. Above rounding
(123x the 0.01 Cr precision of the table). Loop back to A4.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims; strongest bear from the same extract)

**Claim 1 (review L157/375):** Operating EBITDA margin expanded ~1,450 bps YoY to 14.5%; core operations
"genuinely turned positive," not narrative.
Bear from extract: the margin gain rests on cost-of-material/erection falling to 60.7% of revenue
(187.37/308.69) from 68.0% (194.97/286.73) in a single quarter, against an order backlog that collapsed
−41.4% YoY to Rs 1,545 Cr (L590-592); one clean print off a depressed Q1FY26 base is not a trend and the
mix that drove it may not persist as backlog shrinks.
Survives? NO — already incorporated. A4 marks this "one clean quarter; needs a second" (L285), sets the
≥12% second-quarter gate (Step 8C), and flags backlog −41.4% prominently (checklist #2, Question 1).

**Claim 2 (review L159/205):** "More than 100%" of the +66.2% PAT growth is recurring core, with Other
Income a drag — "healthiest possible composition."
Bear from extract: reported PAT is flattered by a 4.1% ETR vs 25.17% statutory (~Rs 14.5 Cr/qtr un-taxed,
L208), and Other Income at Rs 31.88 Cr is still 46.3% of PBT with its source undisclosed — for a
cash-rich company a chunk is likely recurring interest, so labelling all OI "non-recurring" understates
core reliance and overstates quality.
Survives? NO — already incorporated. A4 flags ETR 4.1% / ~Rs 14.5 Cr un-taxed (Step 4, Question 2,
Step 6A "normalise for tax") and routes OI source to Questions Q6/Q7 with the 46.3%-of-PBT caveat (L165).

**Claim 3 (review L317/367):** Operating result lands at/above the Notion base path; no thesis-broken
trigger fired → PROCEED WITH CAVEATS; revenue run-rate "already near the destination."
Bear from extract: backlog fell to Rs 1,545 Cr (~1.25x annual revenue) and −41.4% YoY; annualising one
quarter to ~Rs 1,235 Cr and calling revenue "near destination" ignores that backlog leads revenue, and
the extract shows NO services order intake replacing the terminated FGD work — the run-rate A4
extrapolates is the thing most at risk.
Survives? NO — already incorporated. A4 surfaces the backlog collapse as a top flag, marks checklist
#2/#6 AMBER/UNKNOWN, makes Question 1 the #1 thesis-changing question, and explicitly warns the pivot is
"dangerous if peers are taking the services share" (L389).

**No surviving bear counter requires grafting into A4** — each of the three positive claims already
carries its strongest same-text counter.

---

## AUDIT 4 — PROTOCOL-VERDICT CHECK

A4's protocol verdict PROCEED WITH CAVEATS is internally consistent with the CLAUDE.md house rule: cash
conversion is INDETERMINATE on a Q1 filing (no cash-flow / no balance sheet per Reg 33 half-yearly), and
A4 correctly caps at CAVEATS (not clean PROCEED) with the four missing-evidence items named (CFO/PAT,
balance-sheet cash, receivable days, RPT/LM-Wind balances). No thesis-broken trigger fired; Branch 8A-W
(watchlist, fully exited) correctly governs; no re-entry at CMP Rs 907 vs Rs 500 ceiling. The exit-PE
authority is untouched (destination PE held pending H1 BS). The verdict LOGIC is sound. However, the
verdict rests on a Step 4 PAT bridge that does not foot; the arithmetic defect must be corrected before
save even though it does not change the CAVEATS conclusion.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

Gap: the Step 4 PAT bridge (review L193-202) does not foot — its seven components sum to +Rs 22.17 Cr but
the stated Reported Net Profit YoY change is +Rs 20.94 Cr. The "Core operating PBT (ex-OI) +46.02" row
already embeds the depreciation (+0.16) and finance-cost (+1.07) reductions, which are then listed a
second time as separate rows, double-counting +Rs 1.23 Cr. This contradicts A4's own Step 2 diagnostic 4
(review L161: "+24.80 = core +46.02 less OI 21.22"). Fix: restate row 1 as the operating-EBITDA swing
+44.79, OR delete the depreciation and finance rows; either makes the bridge foot to +20.94. Coverage
(all counts match, no orphan rows), the plain-language brief (all four parts present), every other
derived metric, and the adversarial read (no surviving un-incorporated bear counter) all PASS.

```yaml
stage: A5-adversary
company: "GVPIL"
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
  - metric: "Step 4 PAT bridge (does not foot)"
    a4_value: "components sum +22.17 vs stated total +20.94"
    recomputed: "+20.94 (row1 should be operating-EBITDA swing +44.79, or drop the +0.16 dep and +1.07 finance rows)"
    source_line: "review L193-202; raw extract L176-210"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Step 4 PAT bridge double-counts depreciation (+0.16) and finance (+1.07) already embedded in the Core operating PBT (ex-OI) +46.02 row; components sum to +22.17 vs the correct +20.94 (contradicts Step 2 diagnostic 4, review L161). Restate row1 as operating-EBITDA swing +44.79 or delete the dep and finance rows so the bridge foots to +20.94."
```
