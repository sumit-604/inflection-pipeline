# A5 ADVERSARY / COMPLETENESS AUDIT — PNGSREVA — Q1 FY27 (re-audit)

Scope: standalone-only results filing (no consolidated, no concall, no presentation this run).
Units INR Million; conversion INR Million x0.1 = Rs Crore. Fresh context: A4 review, A1
extract, A2 ledger only. All counts and metrics re-derived independently; A4/A3 cites checked,
not deferred to. This is a re-audit after one A4 correction loop — all three audits re-run afresh.

---

## AUDIT 1 — COVERAGE (fresh grep + manual sweep vs A2 ledger)

Independent re-enumeration of the A1 extract, diffed against the A2 ledger, then checked that
every ledger row is either cited in A4 or blanket-marked reviewed in A4's preamble (lines 13-17).

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Agenda items | 1 | 1 (l.15-46, single "approved" hit) | none | PASS |
| Auditor paragraphs | 4 | 4 (l.82, 88, 97, 125) | none | PASS |
| P&L value-bearing rows | 24 | 24 (manual sweep l.177-223) | none | PASS |
| P&L structural/header rows | 6 | 6 (l.177,182,194,205,206,221) | none | PASS |
| Notes | 7 | 7 (grep l.242,246,251,257,259,261,281) | none | PASS |
| IPO utilisation lines | 4 | 4 (l.273,274,277,278) | none | PASS |
| IPO utilisation footnote | 1 | 1 (l.279) | none | PASS |
| Management-comment items | 4 | 4 (l.309,333,338,342) | none | PASS |
| Revenue sub-table rows | 3 | 3 (l.318,319,320) | none | PASS |
| Entities in scope | 1 | 1 (standalone, no subs) | none | PASS |
| Signature blocks | 4 | 4 (l.36,135,288,350) | none | PASS |
| ZERO_STANDING items | 2 | 2 (Earlier-year-taxes l.200; Other equity l.219) | none | PASS |
| Turns | 0 | 0 (N.A. — results filing) | N.A. | PASS |
| Slides | 0 | 0 (N.A. — results filing) | N.A. | PASS |

Fresh count ties the ledger on every category. No row my pass found is missing from the ledger
(nothing to loop back to A2). No orphan row (nothing to loop back to A3).

Row-level coverage of A4 (individually cited vs blanket "reviewed, no finding"):
- Individually cited/analysed: revenue, other income, total income, purchases, change-in-inv,
  employee, finance, depreciation, other expenses, total expenses, PBT, income-tax charge,
  deferred tax, earlier-year-taxes (FN4), total tax, PAT, paid-up capital, basic/diluted EPS,
  all 7 notes, all 4 IPO rows + footnote, store-count comment (FN8), diamond-studded revenue
  sub-row, UDIN garble + Gadgil designation mismatch (FN5), Note 4/5 comparability caveats.
- Reviewed-no-finding under the preamble blanket, and I confirm each is immaterial:
  OCI trio (re-measurement (0.16), tax effect 0.04, total OCI (0.12) — l.208-210), total
  comprehensive income (l.213-215), Other equity Rs483.502 Cr FY-end-only (l.219), website
  comment (l.333), and advance tax Rs30.00M (Rs3.00 Cr, l.342-343). None is verdict-bearing.
- OBSERVATION (not a FAIL): advance tax Rs30.00M (l.342-343) is the sole forward cash-outflow
  datum in a filing where A4 marks CFO entirely ND. It does not change the INDETERMINATE cash
  classification (it is not CFO), so blanket coverage is acceptable, but it is the one enumerated
  management-comment item A4 does not surface in body text. Logged, immaterial.

COVERAGE VERDICT: PASS. No orphan rows; no rows missing from ledger.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw INR Million, x0.1 to Rs Cr)

Raw source lines (INR Million): Rev l.178, OI l.179, TotInc l.180, Purchases l.183, ChgInv l.184,
Employee l.185, Finance l.186, Deprec l.187, OtherExp l.188, TotExp l.189, PBT l.195, IncomeTax
l.198, DeferredTax l.199, EarlierYr l.200, TotTax l.201, PAT l.203, EPS l.222-223. Every derived
figure below recomputed from these; A4 cite checked.

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Cost of Materials Q1FY27 | 76.141 | 106.619+(30.478)=76.141 | l.183+184 | PASS |
| Operating EBITDA Q1FY27 (PBT+D+Fin-OI) | 33.927 | 36.398+0.357+2.748-5.576=33.927 | l.195,187,186,179 | PASS |
| Operating EBITDA Q1FY26 | 11.583 | 9.847+0.038+1.985-0.287=11.583 | l.195,187,186,179 | PASS |
| Op EBITDA margin Q1FY27 | 28.76% | 33.927/117.973=28.76% | derived | PASS |
| Op EBITDA margin Q1FY26 | 21.55% | 11.583/53.749=21.55% | derived | PASS |
| Reported EBITDA Q1FY27 | 39.503 | 36.398+0.357+2.748=39.503 | l.195,187,186 | PASS |
| Reported EBITDA margin Q1FY27 | 33.49% | 39.503/117.973=33.49% | derived | PASS |
| Gross Profit Q1FY27 | 41.832 | 117.973-76.141=41.832 | derived | PASS |
| Gross Margin Q1FY27 | 35.46% | 41.832/117.973=35.46% | derived | PASS |
| Gross Margin Q1FY26 | 31.48% | 16.918/53.749=31.48% | derived | PASS |
| Core PBT ex-OI Q1FY27 | 30.822 | 36.398-5.576=30.822 | l.195,179 | PASS |
| Other Income / PBT Q1FY27 | 15.32% | 5.576/36.398=15.32% | l.179,195 | PASS |
| Effective Tax Rate Q1FY27 | 25.24% | 9.188/36.398=25.24% | l.201,195 | PASS |
| Effective Tax Rate Q1FY26 | 24.36% | 2.399/9.847=24.36% | l.201,195 | PASS |
| PAT Margin Q1FY27 | 23.06% | 27.210/117.973=23.06% | l.203 | PASS |
| Revenue YoY | +119.49% | (117.973-53.749)/53.749=119.49% | l.178 | PASS |
| Operating EBITDA YoY | +192.90% | 22.344/11.583=192.90% | derived | PASS |
| Op EBITDA margin YoY | +721 bps | 28.76-21.55=7.21pp | derived | PASS |
| Depreciation YoY | +839.47% | 0.319/0.038=839.47% | l.187 | PASS |
| Finance cost YoY | +38.44% | 0.763/1.985=38.44% | l.186 | PASS |
| Other Income YoY | +1842.86% | 5.289/0.287=1842.86% | l.179 | PASS |
| Core operating PBT YoY | +222.41% | 21.262/9.560=222.41% | derived | PASS |
| Reported PBT YoY | +269.64% | 26.551/9.847=269.64% | l.195 | PASS |
| PAT YoY | +265.33% | 19.762/7.448=265.33% | l.203 | PASS |
| EPS YoY | +151.61% | (8.58-3.41)/3.41=151.61% | l.222 | PASS |
| Revenue QoQ | -14.59% | (117.973-138.126)/138.126=-14.59% | l.178 | PASS |
| Core PBT ex-OI QoQ | +13.23% | (30.822-27.220)/27.220=13.23% | derived | PASS |
| PAT QoQ | +27.10% | (27.210-21.409)/21.409=27.10% | l.203 | PASS |
| PAT bridge: GP delta | +24.914 | 41.832-16.918=24.914 | derived | PASS |
| PAT bridge: volume @31.48% | +20.218 | 64.224*0.3148=20.218 | derived | PASS |
| PAT bridge: mix @+3.98pp | +4.695 | 117.973*0.0398=4.695 | derived | PASS |
| PAT bridge: OI delta | +5.289 | 5.576-0.287=5.289 | l.179 | PASS |
| PAT bridge: tax delta | +6.789 | 9.188-2.399=6.789 | l.201 | PASS |
| Reconciliation to PBT change | +26.551 | 24.914-0.821-0.319-0.763+5.289-1.749=26.551 | derived | PASS (ties l.195 delta) |
| OI after-tax contribution | ~3.95 | 5.289*(1-0.2524)=3.954 | derived | PASS |
| OI % of PAT increase | ~20.0% | 3.954/19.762=20.0% | derived | PASS |
| Normalized PBT ex-OI-spike | 31.109 | 36.398-5.289=31.109 | derived | PASS |
| Normalized PAT | 23.257 | 31.109*0.7476=23.257 | derived | PASS |
| Normalized PAT YoY | +212% | 15.809/7.448=212.3% | derived | PASS |
| Q1 rev as % FY26 rev | 26.9% | 117.973/439.028=26.87% | l.178 | PASS |
| Q1 PAT as % FY26 PAT | 42.1% | 27.210/64.655=42.09% | l.203 | PASS |
| Q1 EPS as % FY26 EPS | 30.2% | 8.58/28.41=30.20% | l.222 | PASS |
| IPO total deployed | 18.5% | 645.60/3491.23=18.49% | l.278 | PASS |
| IPO store object deployed | 14.1% | 404.88/2865.64=14.13% | l.273 | PASS |
| IPO marketing deployed | 1.3% | 4.61/354.00=1.30% | l.275 | PASS |
| IPO GCP deployed | 86.9% | 236.11/271.59=86.94% | l.277 | PASS |
| Net IPO undeployed | Rs284.56 Cr / 81.5% | 2845.63M=Rs284.563 Cr; 2845.63/3491.23=81.5% | l.278 | PASS |
| Trailing PE | 13.19x | 374.8/28.41=13.19 | l.222 + brief | PASS |
| Dest/Current PE | 1.44x | 19/13.19=1.44 | derived | PASS |
| HR growth-leg threshold | ~10.7% | (1.953/1.44)^(1/3)-1=10.7% | derived | PASS |
| Share count YoY add | ~9.83M | (316.98-218.66)/10=9.832M | l.218 | PASS |
| Diamond-studded mix Q1FY27 | Rs115.987 Cr | 1159.87/10=115.987 | l.318 | PASS |

Notes on external inputs (out of extract scope, not recomputable, correctly flagged by A4 as
"brief"/"Notion"): CMP Rs374.8, entry zone Rs276-345, Dest PE 19x, bull FY27 rev Rs571 Cr,
FY26 KAM Rs335.55 Cr, FY26 ROCE 14.16%. A5 cannot verify these from the extract; A4 does not
treat any as extract-anchored. No arithmetic dependency error introduced.

ARITHMETIC VERDICT: PASS. Every derived metric in A4's tables ties to the raw extract within
rounding. The Step 4 PAT bridge reconciles exactly (+24.914-0.821-0.319-0.763+5.289-1.749 =
+26.551 PBT change, less Rs6.789 tax = +Rs19.762 PAT change = 27.210-7.448). No mismatch above
rounding.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear from same extract)

**Claim 1 (A4 l.110/121/171): "Core operating PBT +222.41%; ~80% of PAT growth is recurring
core, not treasury; the operating core stands on its own."**
Strongest bear from extract: the "recurring core" leans on the +721bps margin lift. Of the
+Rs24.914 Cr GP gain, Rs4.695 Cr (~19%) is mix/margin that A4 itself calls unverified (FN7),
and QoQ the core rose only +13.23% while revenue FELL -14.59% off the Q4 base. If margin reverts
to the 22% band, the "80% recurring" claim shrinks materially.
Survives? NO NEW GRAFT NEEDED — already in A4: FN7 flagged AMBIGUOUS (l.105,119,278), and the
QoQ revenue dip plus the "flattered headline" caveat are in Step 3 (l.144) and Step 2 (l.110,
121,127).

**Claim 2 (A4 l.377/Step 6A): "Op EBITDA margin 28.76% (+721bps), PAT already 42.1% of FY26 PAT
in one quarter, actuals at/above base-bull on every metric."**
Strongest bear from extract: mix is Rs115.987 Cr diamond-studded of Rs117.973 Cr = 98.3% vs FY26
~87% (gold Rs56.927 Cr / Rs439.028 Cr = 13% in FY26 vs 1.7% now, l.319/320); Q1 (Akshaya
Tritiya) skews to high-value diamond, so through-cycle margin plausibly reverts toward Q4 FY26's
22.14% / FY26's 21.63%. Also tested: does the Rs30.478 Cr FG build (l.184) mechanically inflate
GM? Checked and REJECTED — the negative change-in-inventory is proper accrual matching (goods not
sold are correctly excluded from COGS); it does not fabricate margin, so that specific counter is
not extract-supported.
Survives? NO NEW GRAFT NEEDED — the mix-sustainability/seasonality bear is already A4's FN7 with
an explicit "normalizes to ~22%" bear answer (l.338) and the Step 6A caveat (l.236).

**Claim 3 (A4 l.117: "Revenue tracking bull path Rs571 Cr, not base").**
Strongest bear from extract: from the FILING ALONE, Q1 x4 = Rs471.9 Cr — below the Rs571 Cr bull
and only base-ish; revenue DECLINED -14.59% QoQ; and to reach Rs571 Cr the remaining nine months
must average ~Rs151 Cr/qtr, i.e. ABOVE even the derived Q4 FY26 peak of Rs138.126 Cr (itself a
balancing figure, Note 4). The "tracking bull" label rests on an external pre-results note, not
on the filing.
Survives? NO NEW GRAFT NEEDED — A4 shows the Q1 x4 = Rs471.9 Cr math and labels the bull read
"directional" (l.117), and Step 3 (l.147) states the ~Rs151 Cr/qtr step-up requirement and the
Q4-is-derived caveat. The bear is derivable from A4's own disclosed numbers.

ADVERSARIAL VERDICT: PASS. The three strongest bear counters are each already incorporated in
A4; none survives as an un-incorporated counter requiring graft. The one candidate counter that
would have been new (FG build inflating margin) is not extract-supported and is correctly absent.

---

## VERDICT

**COMPLETE.**

- Coverage: fresh enumeration ties the A2 ledger on all 14 categories; zero orphan rows; zero
  rows missing from the ledger; every material/flagged row individually cited in A4, immaterial
  rows blanket-reviewed. No loop-back to A2 or A3.
- Arithmetic: every derived metric in A4's tables recomputed from raw INR Million extract lines;
  all tie within rounding; the PAT bridge reconciles exactly. No loop-back to A4.
- Adversarial: the three most-positive claims each have a live bear counter, but all are already
  present in A4 (FN6/FN7, QoQ dip, seasonality, transient Other Income, Q1 x4 math). No surviving
  counter to graft. No loop-back to A4.

Only COMPLETE proceeds to Notion save; this review is cleared.

```yaml
stage: A5-adversary
company: "PNGSREVA"
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
