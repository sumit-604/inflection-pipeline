# A5 ADVERSARY / COMPLETENESS AUDIT — DHANBANK Q1 FY27 (RE-AUDIT, LOOP 1)

Agent: A5 ADVERSARY. Fresh context: A4 review + A1 extract + A2 ledger only. Independent re-derivation; A4/A3 cites checked, not deferred to. Prior verdict: INCOMPLETE (one gap: L281 D/E and L282 Total-Debts/Assets framed as "tenor undisclosed"). This pass re-runs all three audits and re-tests that the gap is closed.

Unit basis: source Rs Lakh; /100 = Rs Cr. All recomputes done from raw extract line numbers.

---

## GATE-A5 CLOSE-OUT OF THE PRIOR (LOOP-0) FAIL

Prior FAIL: the +104% YoY borrowings jump was framed as "tenor undisclosed," ignoring the two enumerated ratio rows L281 and L282.

Fresh verification of closure:
- Footnote L223 (verbatim): "Debt represents borrowings with residual maturity of more than one year." Footnote L224: "Total debts represent total borrowings of the bank." Both confirmed by my own grep (lines 223, 224).
- L281 Debt-Equity = 0.11 / 0.12 / 0.13 / 0.12 (Q1FY27 / Q4FY26 / Q1FY26 / FY26). L282 Total-Debts/Total-Assets = 3.88% / 3.47% / 2.25% / 3.47%. Confirmed by grep (lines 281, 282).
- A4 now cites L281 and L282 in Step 1L (review L106-109), Step 2 (L135-136, L146), Step 5L (L217-218, L229), tripwire #5 (L247), growth trigger (L255, L268), monitorables (L344), Step 8.5 Q6 (L301), and the "What Changed" section (L329). No longer "tenor undisclosed."

The short-tenor conclusion is arithmetically re-derived and SOUND (see Arithmetic Audit rows I1-I5 below). GAP CLOSED.

---

## 1. COVERAGE AUDIT (fresh grep + sweep, diffed vs A2 ledger)

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Notes | 14 | 14 | Notes 1(L350),2-9(L368-402),10(L403-421),11(L422-463),12(L464),13(L465-467),14(L468-469) | none | PASS |
| Line items | 87 | 87 | P&L 22 + BS 13 + segment 36 + Note 11 16; wrapped rows collapsed | none | PASS |
| Zero-standing | 24 | 24 | 2 P&L (L258,L263) + 1 ratio (L269 GoI) + 10 segment nil + 11 Note-11 nil | none | PASS |
| Ratios 17(i)-(x) | 14 | 14 | GoI,CRAR,EPS-B,EPS-D,GNPA amt,NNPA amt,GNPA%,NNPA%,RoA,NetWorth,D/E,TD/TA,OpMgn,NPM | none | PASS |
| Segments | 4 | 4 | Treasury/Retail/Corp-Whsl/Other (reportable) | none | PASS |
| Comparative periods | 4 | 4 | 30.06.2026 / 31.03.2026 / 30.06.2025 / FY26 | none | PASS |
| Agenda items | 1 | 1 | single Reg 30/33/52 results-approval cover letter | none | PASS |
| Auditor paras | 5 | 5 | paras 1-5 (L156-219); no EOM/Other/GC | none | PASS |
| Entities | 3 | 3 | Dhanlaxmi Bank + Sagar & Assoc + Abraham & Jose | none | PASS |
| Signatures | 4 | 4 | CS + 2 audit partners + Board Order block | none | PASS |
| Footnotes | 3 | 3 | *(L222) **(L223) ***(L224) | none | PASS |

Fresh grep spot-checks run this pass: analytical-ratio roman-numeral rows, the two funding-ratio labels + their footnotes (L223/L224/L281/L282), Note-10 sub-items (i/ii/iii at L415-419). All reconcile to the ledger. No row my pass found is absent from the ledger; no ledger row is absent from A4.

Ledger-row-to-A4 citation check (specifically the two rows the prior FAIL turned on):
- 17(vii) D/E L281: CITED and correctly interpreted (>1yr-residual borrowings / equity; footnote L223). PASS.
- 17(viii) TD/TA L282: CITED and correctly interpreted (total borrowings / total assets; footnote L224). PASS.
- All A2 flags dispositioned by A4: audit-label inversion (page4 vs page5) = page-5 header typo, current quarter Unaudited (FN7); Rs 1-lakh segment-vs-BS total diff = rounding (FN8); Note-10 OCR garble recovered manually. No number impact. PASS.

COVERAGE: no orphan rows, nothing missing from ledger. PASS.

---

## 2. ARITHMETIC AUDIT (recomputed from raw extract lines)

| # | Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|---|
| A1 | NII Q1FY27 | 177.62 | 44,936-27,174 = 17,762 lakh = 177.62 | L241,L249 | PASS |
| A2 | C/I Q1FY27 | 75.79% | 16,106 / (17,762+3,489) = 16,106/21,251 = 75.789% | L250,241,249,247 | PASS |
| A3 | C/I Q1FY26 | 81.35% | 14,512/(13,910+3,930)=14,512/17,840=81.345% | L250,241,249,247 | PASS |
| A4 | C/I Q4FY26 | 55.66% | 14,267/(18,705+6,929)=14,267/25,634=55.656% | same | PASS |
| A5 | PCR ex-w/o Q1FY27 | 74.66% | 1-7,261/28,657 = 74.663% | L275-276 | PASS |
| A6 | PCR ex-w/o Q1FY26 | 65.51% | 1-13,862/40,195 = 65.513% | L275-276 | PASS |
| A7 | PCR ex-w/o Q4FY26 | 73.67% | 1-7,540/28,638 = 73.673% | L275-276 | PASS |
| A8 | RoA Q1FY27 | 0.45% | disclosed L279 = 0.45% (not derived) | L279 | PASS |
| A9 | Advances +YoY | +27.4% | 15,57,166/12,21,820-1 = +27.45% | L364 | PASS |
| A10 | Deposits +YoY | +17.1% | 19,40,405/16,56,962-1 = +17.11% | L356 | PASS |
| A11 | Borrowings +YoY | +104.5% | 85,871/41,996-1 = +104.47% | L357 | PASS |
| A12 | Borrowings abs increment | +438.75 Cr | 85,871-41,996 = 43,875 lakh | L357 | PASS |
| A13 | NII +YoY | +27.7% | 177.62/139.10-1 = +27.69% | L241,L249 | PASS |
| A14 | PPOP +YoY | +54.6% | 51.45/33.28-1 = +54.6% | L255-256 | PASS |
| A15 | PBT +YoY | +191.8% | 3,554/1,218-1 = +191.79% | L259-260 | PASS |
| A16 | PAT +YoY | +104.5% | 2,491/1,218-1 = +104.52% | L262 | PASS |
| A17 | ETR Q1FY27 | 29.9% | 1,063/3,554 = 29.91% | L261,L259 | PASS |
| A18 | ETR Q4FY26 | 44.9% | 3,547/7,896 = 44.92% | L261,L259 | PASS |
| A19 | EPS Q1FY27 | 0.63 | 2,491 lakh / (39,470/10 lakh sh) = Rs 0.631 | L262,L265 | PASS |
| A20 | Credit cost Q1FY27 (proxy) | 0.42% | 15.91x4 / avg adv 15,244.86 = 0.417% | L257,L364 | PASS |
| A21 | RoE Q1FY27 (proxy) | 7.74% | 24.91x4 / avg NW 1,286.71 = 7.74% | L262,L280 | PASS |
| A22 | Net-worth vs book-equity gap | 204.34 Cr / 13.5% | 1,513.21-1,308.87 = 204.34; /1,513.21 = 13.5% | L354-355,L280 | PASS |
| A23 | PAT bridge YoY sum | +12.73 | 38.52-4.41-15.94+5.19-10.63 = +12.73 | L241-262 | PASS |
| A24 | PAT bridge QoQ sum | -18.58 | PBT -43.42 (-9.43-34.40-18.39+18.80) + tax +24.84 = -18.58 | L241-262 | PASS |
| A25 | Operating margin 17(ix) | 10.62% | 5,145/48,425 = 10.62% | L255,248 | PASS |
| A26 | Net profit margin 17(x) | 5.14% | 2,491/48,425 = 5.14% | L262,248 | PASS |

### FN14 funding-tenor reconciliation (the revision's new arithmetic)

| # | Derived quantity | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|---|
| I1 | Implied >1yr borrowings (D/E x Net Worth) | ~143.98 / ~151.75 / ~154.44 Cr (Jun26/Mar26/Jun25) | 0.11x1,308.87=143.98; 0.12x1,264.55=151.75; 0.13x1,188.04=154.45 | L281,L280 | PASS |
| I2 | Implied short-tenor (<1yr) = total less >1yr | ~714.73 / ~584.88 / ~265.52 Cr | 858.71-143.98=714.73; 736.63-151.75=584.88; 419.96-154.44=265.52 | L357,I1 | PASS |
| I3 | Short-tenor YoY multiple | ~2.7x | 714.73/265.52 = 2.69x | I2 | PASS |
| I4 | Cross-check TD/TA definition (L224) | 3.88% | 85,871/22,12,624 = 3.881% (=total borrowings/total assets, confirms footnote) | L357,L359,L282 | PASS |
| I5 | Book-equity robustness (A4 alt base ~166 vs ~183) | ~166 / ~183 Cr | 0.11x1,513.21=166.45; 0.13x1,404.81=182.63 | L281,L354-355 | PASS |

Arithmetic soundness of the short-tenor conclusion: implied >1yr-residual borrowings are flat-to-DOWN YoY (~144 vs ~154 Cr on net worth; ~166 vs ~183 Cr on book equity) while total borrowings rose +438.75 Cr, so essentially the entire increment is <1yr residual. The conclusion holds under both equity bases and is robust to 2-decimal rounding on the D/E ratio (extreme rounding band ~137-160 Cr for >1yr, still far below the +439 Cr increment). L282 reconciles exactly to total-borrowings/total-assets (I4), independently confirming footnote L224. The two implied rows are correctly flagged in A4 as DERIVED (review L108-113), not disclosed line items. NO estimation of a disclosed number occurred. The task's stated ~Rs 144-154 Cr >1yr-reconciliation band is confirmed (I1).

ARITHMETIC: 31 of 31 checks PASS. No mismatch above rounding.

---

## 3. ADVERSARIAL READ (three most positive claims, strongest bear from the same extract)

1. CLAIM: Asset quality is the strongest leg — PCR ex-w/o 74.66% and rising, NNPA 0.47%, GNPA 1.82%, FLAG-CASH falsifier not triggered (review L226).
   BEAR: PCR ex-w/o rose partly because NNPA fell in absolute terms (7,540->7,261 lakh, L276) on a QoQ-FLAT gross NPA (28,638->28,657, L275) while the provision CHARGE fell to 15.91 Cr (L257) — coverage improved on a provision-LIGHT quarter, so the "rising coverage" optic is not fresh provisioning.
   SURVIVES? NO — already grafted as FN1 and stated repeatedly (review L227, L256, Q1 management question). No new graft required.

2. CLAIM: Core operating health genuinely positive — PPOP +54.6% YoY, NII-driven (review L141).
   BEAR: off a thin base (33.28 Cr) and PPOP HALVED QoQ (113.67->51.45, -54.7%, L159); other income FELL YoY (-11.2%) and collapsed QoQ (-49.6%), so the YoY optic flatters and the run-rate is decelerating.
   SURVIVES? NO — already grafted as FN10 and Step 3; A4 calls Q4 the outlier and the print "dragged by" not "flattered by" other income.

3. CLAIM: Growth transition ON TRACK — advances +27.4% YoY, NII +27.7% (review L255).
   BEAR: composition undisclosed (no gold/LTV/secured-unsecured split, FN13) AND the marginal funding is short-tenor wholesale, not deposits — deposits grew +17.1% while borrowings grew +104.5% and the increment is essentially all <1yr (FN14). Growth quality and funding durability both unproven.
   SURVIVES? NO — already grafted as FN13 + the revised FN14; the funding-durability flag is explicitly STRENGTHENED this revision and routed to management Q6/Q7.

Bonus check — headline PAT +104.5% YoY: already de-flattered as a nil-tax-comparator artefact (ETR 0%->29.9%, FN3). Incorporated.

No bear counter survives un-incorporated. No new gap is introduced by the revision. Every forward-signal finding (FN1,3,5,10,11,12,14) and ambiguous finding (FN4,9,13) generates at least one Step 8.5 management question; FN14 specifically is folded into Q6 (rollover ladder, repricing, NIM/CoF sensitivity, deposit-migration plan) and cross-referenced in Q7. FN2 (protective), FN6/7/8 (no-impact dispositions) correctly carry no question.

---

## VERDICT

COMPLETE. The single prior-loop gap is closed: L281 (17(vii) Debt-Equity, footnote L223) and L282 (17(viii) Total-Debts-to-Total-Assets, footnote L224) are now cited and correctly interpreted; the +104.5% YoY borrowings increment is shown to be essentially all short-tenor (<1yr residual) with an arithmetically sound reconciliation (implied >1yr borrowings ~144 vs ~154 Cr, flat-to-down); and FN14 is routed as management question Q6. Coverage: no orphan rows, nothing missing from the ledger. Arithmetic: 31/31 PASS, no mismatch above rounding. Adversarial: no surviving un-incorporated bear counter, no new gap from the revision. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "DHANBANK"
quarter: "Q1 FY27"
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
