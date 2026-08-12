# A5 ADVERSARY / COMPLETENESS AUDIT — IndiQube Spaces Limited (INDIQUBE) — Q1FY27
# RE-AUDIT (loop 1 of 2). Prior verdict INCOMPLETE; single blocker = deck D222 orphan.
# Fresh context: derived independently from A1 extracts + A2 ledgers; A4 cites checked, not trusted.

## PRIOR-GAP CLOSURE CHECK (the reason this re-audit exists)

**Prior blocker:** deck ledger row **D222** ("Net Impact on P&L", slide 25 / extract page 26, printed **75** vs recomputed **74**) was enumerated in the deck ledger (ARITHMETIC_VARIANCE, twin of the EBIT 96-vs-97 item) but was ABSENT from A4's review, while its identical twin (EBIT Ind AS 96-vs-97, D108/D109) was present. Asymmetry = orphan row = FAIL to A4.

**Independent recompute of D222 (deck L719-729):**
- Q1FY27: Interest on Lease Liabilities 116 (D218/L721) + Depreciation on ROU 148 (D219/L723) − Payment of Lease Liabilities 190 (D221/L727) = **74**. Slide prints **75**. ₹1 Cr QC lapse confirmed.
- Q1FY26 comparative: 100 + 113 − 140 = **73** = printed 73. Comparative column ties exactly. Confirmed.
- Cross-check: Total Ind AS 116 Impact printed 264 (=116+148 ✓) and 213 (=100+113 ✓); Net Impact = 264−190 = 74 (printed 75), 213−140 = 73 (printed 73). Consistent with above.

**Closure verification in the AMENDED review:**
- Preamble line 30: "deck A3-F14-01 EBIT 96-vs-97 and deck A3-F14-02 Net-Impact 75-vs-74 are both carried as NEUTRAL-FACT QC lapses in Step 1B." ✓
- Step 1B inconsistency list line 148: "(A3 press F14-1 / deck A3-F14-01 / deck A3-F14-02)". ✓
- Step 1B line 153: full treatment — recompute to 74, comparative ties at 73, ₹1 Cr NEUTRAL-FACT, no Question-for-Management row required (comparative foots), verdict/flags/decision unaffected. ✓
- YAML line 495 `a3_findings_incorporated` now includes "A3-F14-02(deck)". ✓

**D222 GAP: CLOSED.** The amendment placed D222 symmetrically alongside its EBIT twin. No re-derivation disagreement.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF present at review lines 463-479, all four labelled parts present and carrying real content:

| Brief part | Location | Status |
|---|---|---|
| (1) Summary narrative | L465-467 (~18 lines prose, numbers-first) | present |
| (2) SECTOR intelligence | L469-471 | present |
| (3) BUSINESS-MODEL intelligence | L473-475 | present |
| (4) COMPETITION intelligence | L477-479 | present |

Gate: **PASS.** None missing, none placeholder.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration diffed against A2 ledgers)

Fresh grep/manual re-count of each extract vs each A2 ledger:

| Category | A2 count | My fresh count | Orphan rows (ledger→absent from A4) | Status |
|---|---|---|---|---|
| results: numbered notes | 6 | 6 (extract L209,211,215,218,249,256) | none — notes table Step 0D | PASS |
| results: Note-4 footnotes | 4 | 4 (•,••,#,A at L240,241,244,245) | none — Step 0D rows | PASS |
| results: stmt line items | 29 | 29 (L166-199) | none — Step 1 table | PASS |
| results: IPO-utilisation rows | 8 | 8 (L230-239) | none — Step 0C/Q5/Q6 | PASS |
| results: auditor paras | 4 | 4 (L89,95,103,124) | none — Step 0D unmodified | PASS |
| press: reconciliation rows | 16 | 16 (L118-135) | none — Step 1B | PASS |
| press: table cells | 96 | 96 (16×6) | none | PASS |
| press: mgmt-quote numbers | 16 | 16 (L62-82) | none — Step 2B claims | PASS |
| deck: slides | 35 | 35 ([page 1..35]) | none — slide master reviewed | PASS |
| deck: data points | 234 | 234 (D001-D234) | **none — D222 now cited (was the sole prior orphan)** | PASS |
| deck: table line items | 70 | 70 | none | PASS |
| deck: ARITHMETIC_VARIANCE findings | 2 (D108/D109; D222) | 2 | **both now in Step 1B (L152, L153)** | PASS |
| monitoring: enumerated units | 155 | 155 (2 bank + 62 FD + 1 total = 65 deployment; +90 others) | none — FND-1..5/OD1 in Q5-Q7, Step 8C | PASS |
| monitoring: deployment rows | 65 | 65 (L536-606) | none (aggregated; individual FDs immaterial, ledger-flagged) | PASS |
| AGM: proceeding items | 14 | 14 (L85-176) | none — FND-01/03/05/07 in Q14-Q16 | PASS |
| AGM: resolutions | 3 | 3 (L145-154) | none — monitorable + Q15 | PASS |
| AGM: distinct persons | 7 | 7 | none | PASS |

**A3-findings incorporation:** 25 FORWARD-SIGNAL/AMBIGUOUS findings enumerated in review L24-28 (results 4 + press 8 + deck 4 + monitoring 5 + AGM 4 = 25), each routed to a Q-for-Management row (Step 8.5, Q1-Q16) and/or Monitorable (Step 8C). NEUTRAL-FACT / CONFIRMATORY-NEGATIVE items (deck A3-F14-01, deck A3-F14-02, press F16-3) handled in-line per L30 — both deck twins now present.

**Rows my fresh pass found that the ledger lacks:** none. **Orphan rows (ledger → absent from A4):** none (D222, the sole prior orphan, is now cited).

Coverage: **PASS.** No return to A2, no return to A3.

Note on YAML asymmetry (non-blocking): review YAML L495 lists "A3-F14-02(deck)" but not "A3-F14-01(deck)". This is cosmetic — A3-F14-01 (EBIT twin) is carried in the review body at L30/L148/L152 and was present in the prior version; the incorporation list simply logs the newly-added item. Both twins are substantively covered in the body. Not a coverage defect.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extracted numbers)

Units: results & monitoring Rs millions ×0.1 = Rs Cr; press release & deck native Rs Cr.

| Metric | A4 value | My recompute (raw source) | Status |
|---|---|---|---|
| Revenue Q1FY27 (Ind AS) | 422.69 | 4,226.85M ×0.1 = 422.69 (L167) | match |
| Other income Q1FY27 | 26.13 | 261.29 ×0.1 = 26.13 (L168) | match |
| Finance costs Q1FY27 | 127.22 | 1,272.19 ×0.1 (L175) | match |
| D&A Q1FY27 | 187.89 | 1,878.93 ×0.1 (L176) | match |
| PBT Q1FY27 | (30.51) | (305.10) ×0.1 (L180) | match |
| PAT Q1FY27 | (23.88) | (238.82) ×0.1 (L185) | match |
| Operating EBITDA Q1FY27 | 258.47 | (30.51)+187.89+127.22−26.13 = 258.47 | match |
| Op EBITDA margin Q1FY27 | 61.1% | 258.47/422.69 = 61.15% | match |
| Reported EBITDA Q1FY27 | 284.60 | (30.51)+187.89+127.22 = 284.60 | match |
| Core PBT ex-OI Q1FY27 | (56.64) | (30.51)−26.13 = (56.64) | match |
| Effective tax rate Q1FY27 | 21.7% | (6.63)/(30.51) = 21.73% | match |
| PAT margin Q1FY27 | (5.6%) | (23.88)/422.69 = −5.65% | match |
| Operating EBITDA Q1FY26 | 188.12 | (49.96)+142.98+109.93−14.83 = 188.12 | match |
| Op EBITDA margin Q1FY26 | 60.8% | 188.12/309.29 = 60.82% | match |
| Revenue YoY | +36.7% | 422.69/309.29 − 1 = +36.67% | match |
| Op EBITDA YoY | +37.4% | 258.47/188.12 − 1 = +37.40% | match |
| Depreciation YoY | +31.4% | 187.89/142.98 − 1 = +31.41% | match |
| Finance cost YoY | +15.7% | 127.22/109.93 − 1 = +15.73% | match |
| EBIT (operating) YoY | 45.14→70.58 +56.4% | 188.12−142.98=45.14; 258.47−187.89=70.58; +56.36% | match |
| Other income YoY | +76.2% | 26.13/14.83 − 1 = +76.20% | match |
| Reported PBT narrowed | 38.9% | (49.96−30.51)/49.96 = 38.93% | match |
| PAT narrowed | 35.0% | (36.76−23.88)/36.76 = 35.04% | match |
| QoQ revenue (Ind AS) | +5.3% | 422.69/401.45 − 1 = +5.29% | match |
| IGAAP-eq PAT YoY | +84.2% (vs mgmt +91%) | 35/19 = +84.21% (deck L286) | match — GAP correctly flagged |
| IGAAP-eq EBITDA YoY | +33.8% | 87/65 = +33.85% | match |
| IGAAP-eq EBIT YoY | +61.8% | 55/34 = +61.76% | match |
| IGAAP-eq PBT YoY | +72.0% | 43/25 = +72.0% | match |
| Adjusted Cash EBIT YoY | +44% | 75/52 = +44.2% (deck L351) | match |
| AUM YoY | +22% | 10.61/8.7 = +21.95% (deck L379) | match |
| RPA-basis occupancy | 85.97% | 6.74/7.84 = 85.97% (deck L410-412) | match |
| VAS total Q1FY27 | ₹72 Cr | 33+39 = 72 (deck L617/L619) | match |
| **EBIT Ind AS Q1FY27 (twin)** | correct = 97 | 449−27−24−188−113 = 97 (printed 96 is the lapse) | match |
| **Net Impact on P&L Q1FY27 (D222)** | recompute 74, printed 75 | 116+148−190 = 74; printed 75; ₹1 Cr lapse | match |
| **Net Impact on P&L Q1FY26 (D222 comp)** | ties at 73 | 100+113−140 = 73 = printed 73 | match |

**Arithmetic mismatches above rounding: NONE.** The amendment's added figures (D222: 74 vs printed 75; comparative 73) recompute exactly as A4 states. The ₹1 Cr items are correctly characterised as management-deck internal QC lapses, not pipeline arithmetic errors. Deck-internal ₹1 rounding on net-debt (278−343 = −65 printed −66) and Cash-EBIT expense subtotal are cited-as-source, not re-derived, and fall under the deck's own p34 rounding disclaimer — not A4 arithmetic defects.

Arithmetic: **PASS.** No return to A4.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims; strongest bear from same extract)

**Claim 1 — "Highest ever quarterly revenue ₹428 Cr, +37% YoY; PAT up 91% to ₹35 Cr; profitability strengthening across every metric" (press L55-67).**
Bear counter (same text): the ₹35 Cr PAT and +91% live only in the management-constructed IGAAP-equivalent column that no auditor reviewed (press F4-1); the statutory Ind AS result is a **₹23.88 Cr LOSS** (results L185). The +91% is arithmetically **+84.2%** (35/19), and the base is printed two ways — ₹19 Cr (deck L286) vs ₹18.5 Cr (deck L253). **Counter survives.** Already grafted: flags block, Q1, Q2, Step 1B L151, Step 2B. No new graft required.

**Claim 2 — "VAS scaling rapidly, ₹72 Cr, contribution 11%→17%" (press L78-79).**
Bear counter (same text): the rise is One-Time-driven — VAS One-Time jumped ₹7→₹39 Cr while recurring VAS was roughly flat (₹27→₹33 Cr; recurring ₹34→₹33 QoQ) (deck L617-623); management's own footnote that it is "expected to remain a recurring feature" (deck L636) is aspirational, not contracted. **Counter survives.** Already grafted: Step 8C, VAS flag, Q9, Step 6B #6. No new graft required.

**Claim 3 — "Net cash ₹66 Cr, D/E 0.05x — strong post-IPO balance sheet" (deck L196-200).**
Bear counter (same text): this is the ex-lease view that by design omits the ~₹4,700-4,900 Cr Ind AS lease liability, and the "net cash" is substantially ₹340.6 Cr of unutilised IPO proceeds parked in FDs (monitoring L606, L616), of which only ₹38.9 Cr was deployed this quarter, with capital redirected via 24-Jun-2026 postal ballot into four undescribed 0%-deployed objects (results Note 4; monitoring N2/P4-P7). **Counter survives.** Already grafted: flags block, Step 5, Step 6B #3, Q5/Q6. No new graft required.

All three bear counters survive from the extract, and **all three are already incorporated** in A4's review. No surviving bear counter is missing. No return to A4.

---

## VERDICT

**COMPLETE.**

- Deliverable-completeness gate: PASS (all four brief parts present, non-empty).
- Coverage: PASS. Prior sole orphan **D222 is now cited** (Step 1B L153 + preamble L30 + inconsistency list L148 + YAML L495), placed symmetrically with its EBIT twin. Fresh enumeration matches all five ledgers; no orphan rows, no rows the ledgers lack.
- Arithmetic: PASS. Every derived metric re-derived from raw numbers matches within rounding; the two twin ₹1 Cr deck lapses (EBIT 96-vs-97 recompute 97; Net Impact 75-vs-74 recompute 74, comparative 73) are arithmetically correct as stated. The amendment introduced no new arithmetic defect.
- Adversarial: PASS. All three surviving bear counters were already incorporated; nothing to graft.

Prior gap confirmed closed; amendment clean. This review proceeds to Notion save.
