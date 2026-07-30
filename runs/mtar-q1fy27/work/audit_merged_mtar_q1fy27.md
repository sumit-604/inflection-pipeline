# A5 ADVERSARY / COMPLETENESS AUDIT — MTAR Technologies Limited (MTAR), Q1 FY27

**Agent:** A5 ADVERSARY | **Fresh context:** A4 merged review + 3 A1 extracts + 3 A2 ledgers only.
**Re-derived independently** (own grep/sweep + own arithmetic from raw INR-M / Rs-Cr figures). A4/A3 cites were checked, not trusted.
**Audited file:** review_merged_mtar_q1fy27.md | **Date:** 2026-07-30

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledgers, then A4 citation check)

### Results filing (extract 585 lines / 9 pages)
| Category | A2 count | My fresh count | Method | Orphans (in ledger, absent from A4) | Status |
|---|---|---|---|---|---|
| Notes | 11 | 11 | consol 1-6 (L429/431/435/437/439/440) + standalone [1]-[5] (L359/363/365/367/368) | none — all in Step 0D table | PASS |
| Line items | 68 | 68 | standalone 34 (L321-355) + consolidated 34 (L392-425) | none — Step 1a/1b carry all | PASS |
| Zero-standing | 8 | 8 | 4 std + 4 consol (excep item, prior-period tax adj, OCI x2 each) | none — F8-a/F14-c cover | PASS |
| Agenda items | 7 | 7 | L105-120 items 1-7 | items 3,4,7 (director re-appts, scrutinizer) not individually cited; blanket reviewed-no-finding acceptable (administrative) | PASS |
| Auditor paras | 26 | 26 | standalone 10 (L459-547) + consol 16 (L557-692) | none — clean opinion + F14-a/F14-b logged | PASS |
| Entities | 3 | 3 | MTAR + Gee Pee + Magnatar (L429-430) | none — F6-a | PASS |

### Press release (extract 143 lines / 4 pages)
| Category | A2 count | My fresh count | Method | Orphans | Status |
|---|---|---|---|---|---|
| Financial numbers | 26 | 26 | Rs. values 16 + % 10 (L77-109); all tie to filing Table 1 | none | PASS |
| Segment claims | 5 | 5 | SG1-5 (highest-ever, sector lists x2, leading-mfr, 4-decade) | none — "highest ever" + inflection framing cited (Q&A 12) | PASS |
| MD sentences | 3 | 3 | MD1-3 (L112-116) | none — A3-F6-01 (guidance in-line), inflection point Q&A 12 | PASS |
| Footnotes/disclaimer | 5 | 5 | FD1-5 (L134-144) | none — forward-looking blanket, reviewed-no-finding | PASS |
| Admin | 14 | 14 | AD1-13 + split signature block | none — administrative, reviewed-no-finding | PASS |
| (operational metric) | 1 | 1 | OM1 "sixteen mfg units" (L119) | none | PASS |

### Presentation (extract 823 lines / 32 slides)
| Category | A2 count | My fresh count | Method | Orphans | Status |
|---|---|---|---|---|---|
| Slides | 32 | 32 | 1:1 form-feed markers | none — all referenced or narrative-reviewed | PASS |
| Numbers | 535 | 535 | per-slide checksum re-summed = 535 (536 raw − 1 footnote restatement booked to F2) | S22-1 (SLB Rs 45 Cr) not individually cited; reviewed-no-finding acceptable | PASS |
| Footnotes | 7 | 7 | F1-F7 (safe-harbor, excep, restated-OB, #30Jun, RoCE/RoE/CapEmp defs) | none — F3 drives F-10 def-watch | PASS |
| Zero-standing | 9 | 9 | S12r14, S25r14, S26r5/r11/r15, S27r3/r5/r7/r11 | none | PASS |

**Orphan rows (ledger row not cited AND not reviewed-no-finding by A4): NONE.**
**Rows my fresh pass found that a ledger lacks: NONE.** The three ledgers reconcile exactly to my independent enumeration. No FAIL to A2, no orphan FAIL to A3.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw; results INR M x0.1, deck/PR Rs Cr x1)

All Table-1 conversions verified cell-by-cell against filing p6 (consolidated) and p5 (standalone); every A4 figure ties within rounding. Derived-metric and requested spot-checks:

| Metric | A4 value | My recomputation (raw) | Source line | Status |
|---|---|---|---|---|
| Operating EBITDA Q1FY27 (PBT+D+FC−OI) | 85.05 | 67.402+9.692+15.847−7.887 = 85.05 | L410/404/403/397 | PASS |
| Reported EBITDA Q1FY27 (PBT+D+FC) | 92.94 | 67.40+9.69+15.85 = 92.94 | same | PASS |
| Op EBITDA margin Q1FY27 | 23.6% | 85.05/360.72 = 23.58% | L396 | PASS |
| +550 bps YoY | +550 bps | 23.58%−18.13% = 5.45pp ≈ 550 bps | — | PASS |
| Core PBT ex-OI Q1FY27 | 59.51 | 67.40−7.89 = 59.51 | L410/397 | PASS |
| ETR Q1FY27 / FY26 | 25.5% / 25.5% | 17.175/67.402=25.5%; 32.12/126.15=25.5% | L415/410 | PASS |
| YoY: Rev +130.4% / core PBT +319.1% / PAT +364.5% | as stated | 204.14/156.58=130.4%; 45.31/14.20=319.1%; 39.414/10.813=364.5% | Step 2 | PASS |
| QoQ: Rev +17.9% / OpEBITDA +37.6% / core PBT +37.9% | as stated | 54.65/306.07=17.86%; 23.25/61.80=37.6%; 16.37/43.14=37.9% | Step 3 | PASS |
| S-vs-C PAT gap (S−C)/S all 4 periods | 0.53/3.74/0.14/1.35% | 0.27/50.50; 0.42/11.23; 0.06/44.34; 1.29/95.32 = 0.53/3.74/0.14/1.35% | YAML | PASS |
| **(a) Order-book waterfall** | 5,143.3 | 2,581.9+2,895.1−333.7 = 5,143.3 (exact) | S13-5/6/7/8 | PASS |
| (a) FY26 inflow 2,453.3 as distinct FLOW | flow, not contradiction | Correct: stock (opening/closing book) vs flow (annual inflow) are different measures; 2,895.1>2,453.3 valid flow-vs-flow | S13-15 | PASS |
| **(b) Guidance** 80% base 876.2→1,577; Q1=22.9%; Q2-Q4 avg 405.5 | as stated | 876.2×1.8=1,577.2; 360.7/1,577=22.9%; (1,577.2−360.7)/3=405.5; flat run-rate 360.7×4=1,442.8=+64.7% | S4-1/S25 | PASS |
| **(c) Segment split** sums to consol rev | CE 220.8/61% etc | 220.8+3.2+36.4+100.4 = 360.8 vs 360.7 (Δ0.1 round); 61+1+10+28=100% | S7-10/S9-10/S8-10/S10-10 | PASS |
| **(d) WC days** 274→59; adv-funding OCL +210.4 to 254.9 | 274→59; +210 to 254.9 | S14-3=274, S14-12=59 (−215); OCL 254.9−44.5=+210.4 | S14/S26-16 | PASS |
| **(e) D/E** 0.24→0.45; gross debt 369.3 | 0.24→0.45; 369.3 | S30-11/12; 147.7+221.6=369.3; 369.3/822.6=0.449 | S26/S30 | PASS |
| **(f) Promoter tripwire — FIRED status** | NOT FIRED (29.35% > 25%) | Correct | S31-20 | PASS |
| **(f) Promoter decline PACE "~1.02pp/quarter"** | ~1.02 pp/qtr | **NOT REPRODUCIBLE.** Steps: −0.82/−0.15/−1.09. Series avg = (31.41−29.35)/3 = **0.687 pp/qtr**; OLS slope = 0.63; latest qtr = 1.09. None = 1.02. | S31-8..20 | **FAIL → A4** |
| **(f) "~4 quarters to <25%"** | ~4 quarters (≈Q1 FY28) | Holds ONLY at latest-qtr pace 1.09 (4.35/1.09=4.0). At the **series-average 0.687 pp/qtr → 4.35/0.687 = 6.3 quarters.** A4 bridged to "4 quarters" via the unsupported 1.02 avg. | Section (d) | **FAIL → A4** |
| **(e) Net Debt Mar-26 "≈₹389 Cr"** | ≈389 | **NOT REPRODUCIBLE and contradicts A4's own anchor.** Same basis A4 used for Mar-25 (=~160: gross−cash−bank) applied to Mar-26 = 369.3−1.0−20.2 = 348.1; +leases 7.3 = **355** (MF excluded), or **140** (MF as cash). A4's anchor text itself says "140 / 355." The cell value 389 matches neither. | Step 5 net-debt row | **FAIL → A4** |
| PAT bridge closes (GP effect + opex + D&A + FC + OI + tax) | +39.42 | GP +79.3 (vol +110.7, margin −31.4); −opex 22.64; −D&A 1.32; −FC 10.03; +OI 7.28; −tax 13.18 → PAT +39.42 | Step 4 | PASS |
| GP% Q1FY27 / Q1FY26 | 45.5% / 54.2% | 164.22/360.72=45.5%; 84.90/156.58=54.2% (−8.7pp YoY) | L396/400/401 | PASS (feeds Adversarial C) |
| FY25 PAT 52.9 vs 53.4 discrepancy | flagged F-08, ±0.5 immaterial | Confirmed: S25=52.9, S29=53.4; filing has no FY25 to arbitrate; correctly held | S25/S29-13 | PASS |
| Slide-12 header mislabel "Q4 FY25" for Q1 FY26 values | flagged F-07 | Confirmed: extract L333 header vs L308 Slide-11 labels same 156.6 as Q1FY26 | S12 | PASS |
| Deck EBITDA excludes Other Income | 85.05 = rev−(mat+Δinv+emp+other) | 360.72−(204.32−7.82+46.52+32.64)=85.06; incl OI would be ~92.9 | A3-F14-01 | PASS |

**Load-bearing arithmetic (all YoY/QoQ, margins, ETR, order-book waterfall, guidance, segment split, WC, D/E, PAT bridge, S-vs-C, tripwire fired-status): ALL PASS.**
**Three non-load-bearing figures FAIL to A4** (net-debt Mar-26 label; promoter avg-decline pace; the "~4 quarters" projection that rests on it). None changes the PROCEED WITH CAVEATS verdict, Decision Status, any gate, or any fired/not-fired trigger — but all three are above-rounding, non-reproducible numbers that would enter Notion institutional memory if saved. Per discipline (any above-rounding mismatch = FAIL) they must be corrected first.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims; strongest same-text bear counter)

**Claim 1 — Order book ~2x / Rs 5,143.3 Cr (highest-ever inflow Rs 2,895.1 Cr).**
Bear counter (same text): (i) closing book is on a **"restated" basis** — net of forex/price-escalation/scrap (F3); gross-vs-net-GST and executed-vs-pending undisclosed, so quantum is not like-for-like with the Rs 2,582 Cr Q3 FY26 baseline; (ii) the "**Diversified** Order Book" label is undercut by its own segment mix — **66.7% sits in one vertical** (Clean Energy Rs 3,431 Cr), i.e. concentration in the Bloom/fuel-cell relationship (A3-F16-01); (iii) the book is **not converting** — civil-nuclear revenue Rs 3.2 Cr (1%) despite the Rs 504 Cr Kaiga order (F-04). **Survives? NO — already grafted:** Section (c) holds quantum at DEFINITION_WATCH, F-04 flags non-conversion, Bloom concentration is Q&A #12, and 66.7%=CE is stated. The only mild addition is naming the "diversified" claim as internally contradicted by the 66.7% concentration; already implied.

**Claim 2 — Guidance raised to 80% revenue growth (+ 24% margin pulled into FY27).**
Bear counter (same text): Q1 Rs 360.7 Cr is only **22.9%** of the Rs 1,577 Cr target; the +130.4% YoY is **base-inflated** (Q1 FY26 = softest quarter, 17.9% of FY26); flat run-rate annualizes to only **+64.7%** (9pp below 80%); the 80% needs H2 to average **Rs 405.5 Cr/qtr (+12%)** off catalysts that are themselves slipping (Weatherford → Q3 FY27; nuclear not converting). The MD only says "in line with guidance" — reaffirmation, not delivery. **Survives? NO — fully grafted** in Section (b) (back-half-dependent, "not validated by Q1 alone," all four figures present).

**Claim 3 — Op EBITDA margin 23.6%, +550 bps YoY, GREEN.**
Bear counter (same text): the +550 bps EBITDA-margin expansion coincides with a **GROSS-margin DECLINE of 8.7pp (54.2% → 45.5%)** — so the margin gain is pure **operating-leverage on ~2x revenue, not product-mix/pricing improvement**, and it **reverses if growth stalls**; the mix even worked against GP as **Products & Others jumped to 28% from 15%** (lower-value import-substitutes, durability unknown, F-05); it is **one clean quarter**, and 23.6% is **below the 24% guide midpoint**. **Survives? PARTIALLY — a one-line graft recommended.** The substance is already in the review (Step 4 quantifies GP% 54.2→45.5, −Rs 31.4 Cr margin effect, Products-mix F-05; Growth-trigger notes "one clean quarter only"). But the +550 bps GREEN verdict lines (Step 2 diagnostic #2; Section (a); monitorable #4) call it "genuine expansion" **without adjacently flagging that gross margin fell 870 bps**. A4 should add one clause at the margin-GREEN verdict: *"+550 bps EBITDA-margin expansion is operating-leverage-driven and coincides with a −8.7pp gross-margin decline (Products-mix dilution); fragile if revenue growth decelerates."*

**Net adversarial result:** No wholly new bear counter survives that is absent from the review; the order-book and guidance counters are already grafted. One cross-reference graft is warranted (Claim 3 margin fragility) — folded into the A4 loop-back below.

**Cross-document consistency stresses (all correctly handled by A4, no positive claim undercut beyond what is disclosed):** 4-vertical voluntary split vs single Ind AS 108 segment (F-12, flagged unaudited); FY25 PAT 52.9 vs 53.4 (F-08, immaterial, un-arbitrable); Slide-12 "Q4 FY25" mislabel (F-07); "restated" order book (F-10). None introduces an unhandled contradiction.

---

## VERDICT

**INCOMPLETE — loop back to A4.**

Coverage: PASS (zero orphans, zero missing-from-ledger; all three A2 ledgers reconcile to independent enumeration). Load-bearing arithmetic: PASS (order-book waterfall, guidance, segment split, WC, D/E, YoY/QoQ, margins, ETR, PAT bridge, S-vs-C, tripwire fired-status all recomputed clean). Adversarial: three positive claims stress-tested; two counters already grafted, one one-line graft required.

**Gap (three A4 corrections required before Notion save):**
1. **Net Debt Mar-26 "≈Rs 389 Cr"** is not reproducible and contradicts A4's own anchor — correct to **Rs 355 Cr** (MF excluded, consistent with the Rs 160 Cr Mar-25 basis) or **Rs 140 Cr** (MF as cash); do not leave 389.
2. **Promoter decline rate "~1.02pp/quarter"** is unsourceable — the series average is **0.687 pp/qtr** (OLS 0.63; only the latest quarter fell 1.09). Correct the stated pace.
3. **"~4 quarters to <25% (≈Q1 FY28)"** holds only at the accelerated latest-quarter pace (1.09pp); at the series-average pace it is **~6 quarters**. Either restate to ~6 quarters or explicitly flag that "4 quarters" assumes the latest-quarter acceleration continues.
4. (Graft) Add the **gross-margin fragility clause** to the +550 bps EBITDA-margin GREEN verdict (Claim 3 above).

All corrections are quick edits; none disturbs the PROCEED WITH CAVEATS verdict or the WATCHLIST — AVOID Decision Status. On A4 re-emission with these fixed, this audit's coverage and load-bearing arithmetic already clear it for save.

```yaml
stage: A5-adversary
company: "MTAR"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Net Debt Mar-26", a4_value: "approx Rs 389 Cr", recomputed: "Rs 355 Cr (MF excluded, same basis as Mar-25 ~160) or Rs 140 Cr (MF as cash)", source_line: "Step 5 net-debt row; S26 borrowings 147.7+221.6=369.3, leases 7.3, cash 1.0, bank 20.2, MF 215.3"}
  - {metric: "Promoter stake avg decline pace", a4_value: "~1.02 pp/quarter", recomputed: "0.687 pp/qtr series avg (steps -0.82/-0.15/-1.09; OLS 0.63; latest qtr 1.09)", source_line: "S31-8=31.41 ... S31-20=29.35"}
  - {metric: "Quarters to promoter <25% tripwire", a4_value: "~4 quarters (Q1 FY28)", recomputed: "~6.3 quarters at 0.687 pp/qtr avg (4.35/0.687); '4 quarters' only holds at latest-qtr 1.09 pace", source_line: "Section (d); 29.35-25=4.35pp"}
surviving_bear_counters:
  - {claim: "Op EBITDA margin 23.6% / +550 bps YoY GREEN", counter: "+550 bps EBITDA-margin expansion is operating-leverage-driven and coincides with an -8.7pp GROSS-margin decline (54.2%->45.5%) plus Products&Others mix spike to 28%; fragile if revenue growth decelerates. Substance is in Step 4/F-05 but not cross-referenced at the margin-GREEN verdict lines.", source_line: "S11-7/8/9 GP% 54.2/44.2/45.5; S10-10 Products 28%; L396/400/401"}
loop_back_to: "A4"
gap: "Three non-reproducible figures in A4 tables must be corrected before save: (1) Net Debt Mar-26 'approx 389' -> 355 (MF excl) or 140 (MF as cash); (2) promoter decline '~1.02pp/qtr' -> 0.687pp/qtr avg; (3) '~4 quarters to <25%' -> ~6 quarters at avg pace (or flag it assumes latest-qtr acceleration). Plus graft the gross-margin fragility clause onto the +550 bps EBITDA-margin GREEN verdict. Coverage and all load-bearing arithmetic PASS."
```
