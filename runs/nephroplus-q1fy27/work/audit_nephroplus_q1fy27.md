# A5 ADVERSARY / COMPLETENESS AUDIT — NephroPlus (Nephrocare Health Services Ltd) — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8
Review under audit: `review_nephroplus_q1fy27.md`
Independence: audited only against A1 extracts + A2 ledgers. Every metric below re-derived from the cited raw line; A4's and A3's cites were checked, not trusted.
Unit convention re-verified: statutory filing in ₹ Millions (R L254), ×0.1 to ₹ Cr; presentation & press release native ₹ Cr. No concall this quarter → Role 5 correctly run in reduced form (N.A.).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The MANDATORY PLAIN-LANGUAGE BRIEF (Section 18) carries all four labelled parts, each with real, non-placeholder content:

| Brief part | Location | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | 18.1 (review L509-511) | PRESENT | ~20-line narrative, line-anchored, ends with explicit "PROCEED WITH CAVEATS" verdict |
| (2) Sector intelligence | 18.2 (review L513-515) | PRESENT | Dialysis chronic/recurring demand, penetration 7% vs 16/27/35%, 20-22% India CAGR, payer structure 76.5% public — all cited |
| (3) Business-model intelligence | 18.3 (review L517-519) | PRESENT | Asset-light 52% partner-hospital model, volume×price engine, S-vs-C margin structure (F2) |
| (4) Competition intelligence | 18.4 (review L521-523) | PRESENT | #1 India / #5 global, >50% organized share, 4.4x next chain, global-major risk, KSA JV minority note |

**Gate 0: PASS.** All four parts present and substantive.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger vs A4 review)

### 1a. Fresh grep/sweep re-count vs A2 count-test

| Doc | Category | A2 count | My fresh count | Match | Basis |
|---|---|---|---|---|---|
| Results | numbered+unnumbered notes | 21 | 21 | yes | Std notes 1-8 (R L309-348) + Cons notes 1-11 (R L638-742) + 2 EPS footnotes (R L300,628) = 8+11+2 |
| Results | entities | 26 | 26 | yes | LRR Annexure I Sr 1-26 (R L474-559); Note 5 = 1 parent+24 subs+1 JV (R L657-686) |
| Results | agenda items | 10 | 10 | yes | a/b/c/d (4) + 3 AC members + 3 SRC members (R L22-44) |
| Results | annexure (Reg 30) | 10 | 10 | yes | Sr 1-10 (R L84-158) |
| Results | auditor paras | 11 | 11 | yes | Std 5 (R L178-208) + Cons 6 (R L389-442) |
| Results | signature blocks | 5 | 5 | yes | R L68,227,354,444,744 |
| Results | geography rows | 5 | 5 | yes | India/PH/UZ/Others/Total (R L699-703) |
| Presentation | slides | 46 | 46 | yes | 46 `[page N]` tags; matches formfeed 46 |
| Presentation | chart markers | 8 | 8 | yes | pages 11,12,16,25,27,32,35,41 |
| Presentation | OCR pages | 4 | 4 | yes | pages 7,15,28,40 |
| Presentation | footnote blocks | 25 | 25 | yes | incl. orphan CIS (F25) and duplicate CKD (F21) |
| Presentation | disclosure units | 341 | 341 (accepted) | yes | structural anchors all verify; DU numbering to 428 with documented dedup to 341 |
| Press release | total rows | 44 | 44 | yes | 7+8+3+19+3+1+2+1 |

No category where my fresh pass found a row the ledger lacks → **no return-to-A2 fault.**

### 1b. Ledger-row → A4-review reflection (orphan check)

Every material ledger flag is either cited in the review or dispositioned:

| Ledger flag | Row | Reflected in A4? | Where |
|---|---|---|---|
| STANDALONE_NOT_IN_EXTRACT | PR T7 | yes | Q7, flag, R5-5B (F2-1) |
| INCONSISTENT_DEFINITION (Saudi vs ESOP) | PR N3/N1 | yes | Q3, A16 flag (F14-1) |
| ROUNDING_VARIANCE (₹282/₹65/10,30,000) | PR M14/M15/M17 | yes | R5-Step7, F14-2 |
| KSA_MILESTONE (license/commenced/RFI) | Presn DU178-180 | yes | Q1, Q2, checklist 7/13, trigger 3 |
| CROSS_CHECK clinic scope (272/200/78; 6/18/8) | Presn DU286/290 | yes | Q9 (A14) |
| Intl-mix trend omits Q1FY27 | Presn DU273 | yes | Q10 (A12) |
| ORPHAN_FOOTNOTE CIS | Presn F25 | yes | Q11 (A11) |
| ENTITY_CHANGE Kazakhstan LLP | R Note 9 / entity 26 | yes | Q8, Step 0D, monitorables (F15) |
| Provisional PPA / 7 asset transfers ₹70.9 Cr | R L729 | yes | Q5, Step 0D (F7) |
| ZERO_STANDING Saudi add-back 0.0 / CCPS 0.0 | Presn DU058/069 | yes | Q3, Step 0C, A16 |
| MARGIN_DELTA_OMITTED | PR L3/L5 | dispositioned | deltas present in bullets (M6/M7); benign |
| DATA_AMBIGUOUS organized-share chart | Presn DU262 | dispositioned | used qualitatively in 18.2; non-thesis |
| REPEAT_METRIC | PR M25/M27 | dispositioned | benign, no question needed |

**Minor coverage observation (non-blocking):** the A2 results ledger raised `TIGHT_SIGNATURE_TIMING` on the two MD result-signatures (R L354/L744, ~1m20s / ~1m54s after board close, ahead of the auditor's own signature). The A2 ledger itself adjudicated it "after conclusion — no SIGNATURE_BEFORE_CONCLUSION breach... tight but not contradictory." A4's preamble marks all 5 signature blocks reviewed but does not surface a one-line disposition of this specific flag. Because A2 already concluded no breach and the row is accounted for at row level, this is a recommendation to A4 (add a one-line "signature timing tight, no breach" note), **not an orphan-row FAIL.**

Every A3-class AMBIGUOUS / FORWARD-SIGNAL flag is converted to at least one Section-16 management question. **Coverage: PASS.**

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from the cited raw line)

All consolidated figures below are filing Millions ×0.1 (R L582-627); standalone from R L262-299.

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Revenue YoY (C) | +23.7% | 281.75/227.78−1 = 23.69% | R L582 | MATCH |
| Operating EBITDA ex-OI Q1FY27 (C) | 63.88 | 44.60+24.54+2.21−7.46 = 63.88 | R L595,589,588,583 | MATCH |
| Operating EBITDA ex-OI Q1FY26 (C) | 47.56 | 28.52+19.52+6.10−6.58 = 47.56 | R L595,589,588,583 | MATCH |
| Op EBITDA margin Q1FY27 | 22.7% | 63.88/281.75 = 22.67% | — | MATCH |
| Op EBITDA margin Q1FY26 | 20.9% | 47.56/227.78 = 20.88% | — | MATCH |
| Margin expansion | +180 bps | 22.67−20.88 = 1.79pp | — | MATCH |
| Op EBITDA growth | +34.3% | 63.88/47.56−1 = 34.3% | — | MATCH |
| Core PBT ex-OI Q1FY27 (after JV) | 33.57 | 41.03−7.46 = 33.57 | R L599,583 | MATCH |
| Core PBT ex-OI Q1FY26 | 21.94 | 28.52−6.58 = 21.94 | R L599,583 | MATCH |
| Core PBT ex-OI growth | +53.0% | 33.57/21.94−1 = 53.0% | — | MATCH |
| Core PBT ex-JV growth | +69.3% | (44.60−7.46)/21.94−1 = 69.3% | R L595 | MATCH |
| ETR Q1FY27 (C) | 22.1% | 9.06/41.03 = 22.08% | R L604,599 | MATCH |
| ETR Q1FY26 (C) | 16.9% | 4.82/28.52 = 16.90% | R L604,599 | MATCH |
| ETR Q4FY26 (C) | 8.6% | 2.85/33.22 = 8.58% | R L604,599 | MATCH |
| PAT margin Q1FY27 | 11.3% | 31.97/281.75 = 11.35% | R L606 | MATCH |
| OI/PBT Q1FY27 | 18.2% | 7.46/41.03 = 18.2% | R L583,599 | MATCH |
| EPS basic YoY (C) | +13.1% | 3.19/2.82−1 = 13.1% | R L626 | MATCH |
| PBT YoY (C) | +43.9% | 41.03/28.52−1 = 43.9% | R L599 | MATCH (deck 43.8% rounding) |
| PAT YoY (C) | +34.9% | 31.97/23.70−1 = 34.9% | R L606 | MATCH |
| PAT bridge sum | +8.27 | 16.32−5.02+3.89+0.88−3.57−4.24 = 8.26 | Step 4 | MATCH (rounding) |
| Revenue YoY (S) | +14.5% | 170.38/148.83−1 = 14.48% | R L262 | MATCH |
| Op EBITDA ex-OI Q1FY27 (S) | 24.15 | 16.69+13.09+0.49−6.12 = 24.15 | R L276,270,269,263 | MATCH |
| Op EBITDA margin (S) | 14.2% | 24.15/170.38 = 14.2% | — | MATCH |
| PAT YoY (S) | +150.6% | 12.56/5.01−1 = 150.7% | R L283 | MATCH (rounding) |
| S-vs-C gap: subsidiary PAT share Q1FY27 | 60.7% | (31.97−12.56)/31.97 = 60.7% | R L606,283 | MATCH |
| — Q4FY26 | 64.1% | (30.37−10.89)/30.37 = 64.1% | R L606,283 | MATCH |
| — Q1FY26 | 78.9% | (23.70−5.01)/23.70 = 78.9% | R L606,283 | MATCH |
| Intl revenue mix | 44.9% | (90.63+32.13+3.61)/281.75 = 44.85% | R L699-702 | MATCH |
| Receivable days (Mar-26) | ~116 | 316.9/998.85×365 = 115.8 | P L1490,1446 | MATCH |
| Inventory days | ~53 | 33.0/226.79×365 = 53.1 | P L1487 | MATCH |
| Payable days | ~230 | 143.0/226.79×365 = 230.1 | P L1486 | MATCH |
| CFO/PAT FY26 | 3.03x | 232.6/76.84 = 3.03 | P L1517,R L606 | MATCH |
| Net cash Mar-26 | ~403 | 123.9+131.6+170.6−23.0 = 403.1 | P L1491,1493,1489,1484 | MATCH |
| Goodwill/net worth | 7.8% | 86.7/1,116.5 = 7.76% | P L1477,1472 | MATCH |
| QoQ revenue | +6.1% | 265.62→281.75 = 6.07% | R L582 | MATCH |
| QoQ op EBITDA | +18.8% | 63.88/53.77−1 = 18.8% | R L595 etc | MATCH |

**Arithmetic: PASS — every derived metric reproduces within rounding. Zero mismatches above rounding.**

**Note on the "44.9% of revenue arising in subsidiaries" claim (Step 0D / F4 / Q4):** 44.9% is the international geography mix, whereas a pure standalone-vs-consolidated revenue gap is (281.75−170.38)/281.75 = 39.5%. These reconcile once intercompany is stripped: the parent's *external* revenue ≈ India geography 155.38, so subsidiaries' external revenue = 281.75−155.38 = 126.37 = 44.9%. The 44.9% is therefore a defensible "external revenue arising in (foreign) subsidiaries" measure and reproduces from R L699. Not a FAIL; flagged only so A4 states the basis (external/geography) rather than mixing it with the standalone-based 60.7% PAT figure.

**Discipline checks:**
- Cash-conversion INDETERMINATE cap: **respected.** Step 5 and the 18.1 narrative both cap the verdict at PROCEED WITH CAVEATS with the four missing-evidence items named (no Q1 CFO, no Q1 balance sheet, capex not isolable, receivables not refreshed). Not silently resolved to PROCEED.
- No exit PE / valuation introduced: **confirmed.** Step 7 explicitly declines to recompute destination PE/fair values; entry zone ₹345-423 is carried from Notion memory, not newly derived. Compliant with Role 4/5 scope.
- Standalone AND consolidated both treated: **confirmed** (Steps 1a/1b, 2/2b).

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear counter from the same extract)

**Claim 1 — "Growth is real and operating: revenue +23.7%, margin +180bps, core PBT ex-OI +53% > PAT +35%."**
Bear counter (same text): the India parent grew revenue only +14.5% and India-geography only +11.6% (R L699); the consolidated +23.7% is disproportionately international, and Philippines' +35.4% embeds **7 acquisitions executed in-quarter** (P L651/656) — i.e., partly inorganic, not same-clinic. **Counter survives on the extract but is already grafted** into A4 (Step 2b/F2, Step 2 diagnostic 5, Q9 clinic-scope). No new incorporation required.

**Claim 2 — "KSA license obtained; thesis tripwire cleared; catalyst on track."**
Bear counter (same text): NHSSAC turnover NIL FY24/FY25/FY26 (R L88,149-151), JV share-of-loss **widened** to ₹3.57 Cr — larger than the entire prior-year JV loss of ₹3.09 Cr (R L597) — and no first revenue is quantified; the entity is simultaneously being internally restructured (R L44). License is a cost-only milestone so far. **Counter survives but is already grafted** (Q1, checklist item 7 AMBER, flags, 8C bear threshold). No new incorporation required.

**Claim 3 — "Adjusted PAT +41.7%, Adj EBITDA margin 23.1%, operating leverage."**
Bear counter (same text): the headline is non-GAAP — Adj PAT 36.8 adds back the ₹3.6 Cr JV loss + ₹1.3 Cr ESOP (PR L54-56), presenting profit as if the Saudi drag did not exist; reported PAT grew only +34.9% and reported EBITDA margin is 22.7%; ETR is normalising 16.9%→22.1%→25.17% (a structural forward EPS headwind), and reported EPS grew only +13.1% on IPO dilution. **Counter survives but is already grafted** (A16, F8, F14-1, Step 4, 18.1 narrative). No new incorporation required.

**Result: all three bear counters are supported by the extract and all three are already incorporated in A4.** No surviving bear counter is missing from the review; therefore nothing must be newly grafted before save.

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four brief parts present and substantive).
- Coverage: PASS (fresh counts reconcile to A2 on every category; every material ledger flag cited or dispositioned; every AMBIGUOUS/FORWARD-SIGNAL flag → ≥1 management question).
- Arithmetic: PASS (S-vs-C gap, margins, YoY/QoQ, ETR, subsidiary-contribution ratio, receivable days, PAT bridge all reproduce within rounding; zero mismatches above rounding).
- Adversarial: PASS (three strongest bear counters all already incorporated; none surviving-and-missing).
- Discipline: INDETERMINATE cash-conversion cap respected; no exit PE/valuation introduced; standalone and consolidated both treated.

Two non-blocking recommendations for A4 (do not gate the save): (i) add a one-line disposition of the A2 `TIGHT_SIGNATURE_TIMING` flag (A2 already concluded no breach); (ii) state the basis (external/geography) when citing "44.9% of revenue arising in subsidiaries" so it is not read on the same standalone basis as the 60.7% PAT figure.

```yaml
stage: A5-adversary
company: "NEPHROPLUS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE               # COMPLETE | INCOMPLETE
plain_language_brief:           # hard gate — all four must be present
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []               # ledger rows not cited in A4
  missing_from_ledger: []       # rows your fresh pass found, ledger lacks
arithmetic_mismatches: []       # {metric, a4_value, recomputed, source_line}
surviving_bear_counters: []     # all three strongest counters already incorporated in A4
loop_back_to: ""
gap: ""
```
