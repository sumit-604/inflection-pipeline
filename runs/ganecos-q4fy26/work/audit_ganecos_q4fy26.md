# A5 ADVERSARY / COMPLETENESS AUDIT — GANECOS Q4 FY26 (Corrigendum results)

Independent re-derivation. I read only the A4 review, the A1 extract, and the A2 ledger.
I re-ran the enumeration with my own grep pass and recomputed every derived number from the
extract's raw Lakh figures (conversion x0.01 to Cr). I did not defer to A4's or A3's cites.

Doctype: results. Ticker GANECOS. Quarter q4fy26. Unit in filing Rs Lakh (Cr = x0.01).

---

## 1. COVERAGE AUDIT

Fresh enumeration vs A2 ledger. Every ledger category traced into A4's review (cited or
reviewed-no-finding).

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Notes (numbered) | 19 | 19 (consol 1-8 = 8; standalone 1-11 = 11) | none — all in A4 0D table | PASS |
| Notes (unnumbered footnotes) | 5 | 5 (consol "#" L151; consol "/\\" ESOP L184; SA "#" L393; consol CF L335; SA CF L573-574) | none | PASS |
| Notes total | 24 | 24 | none — 0D table + corrigendum note + auditor check cover all | PASS |
| Line items total | 240 | 240 (28+42+51+26+41+49+3; per-table sums re-added) | none — all P&L/BS/CF rows captured in Steps 1 and 5 | PASS |
| Corrigendum notice items | 6 | 6 (cover-letter items 1,2,3,5,6,7; table content counted under line items) | none — 0D corrigendum note + Step 6E | PASS |
| Auditor paragraphs | 2 | 2 (consol Note 4 L158-159; SA Note 4 L400-401) | none — 0D auditor check | PASS |
| Entities named | 4 | 4 (Ecopet, Ecotech, Recycling Chain, ESOP trust) | none — notes SA6/7/8 + ESOP footnote | PASS |
| Signature blocks | 6 | 6 (1 corrigendum CS + 5 statement DIN blocks) | none — SIGNATURE_DATE_RETAINED reviewed via Q10 | PASS |
| ILLEGIBLE_VALUE flags | 4 | 4 (DPS L162, DPS L411, consol FY25 PAT L124-132, consol curr borrowings L245) | none — all four surfaced as NOT FOUND in A4 | PASS |
| ZERO_STANDING flags | 24 (summary) | **25** (grep of ledger tables: L164,165,168,184,197,199,217,231,240,258,265,266,267,268,307,308,311,323,326,340,342,360,372,380,403) | none — every nil line is enumerated in the ledger tables and reviewed collectively as no-finding | **DISCREPANCY, non-blocking** |
| Standalone coverage | full | full — both P&L, derived, BS, CF present in A4 Steps 1B/1D/5B | none | PASS |
| Consolidated coverage | full | full — both P&L, derived, BS, CF present in A4 Steps 1A/1C/5A | none | PASS |

### ZERO_STANDING discrepancy — classification

My grep over the ledger tables returns **25** `ZERO_STANDING` rows; the A2 summary (ledger
L490) and the A2 YAML (`zero_standing: 24`) both state **24**. This is an off-by-one **tally
error inside A2's summary**, not a missed enumeration: all 25 nil lines are individually present
and flagged in the ledger's own tables, and A4 reviews zero-standing rows collectively as
no-finding nil lines. No disclosure unit is orphaned, unreviewed, or absent from either the
ledger or A4; no derived number A4 used depends on this count.

Neither strict FAIL condition is triggered: there is no ledger row absent from A4 (no orphan),
and there is no row my fresh pass found that the ledger lacks (the ledger's tables contain all
25). Only the summary integer is wrong. Disposition: **non-blocking advisory to A2 — correct
the zero-standing tally from 24 to 25** (summary L490 and YAML `counts.zero_standing`). Does not
block save.

**Coverage verdict: COMPLETE.** No orphan rows. No unreviewed disclosure unit. One cosmetic A2
tally correction recommended (25, not 24).

---

## 2. ARITHMETIC AUDIT

Recomputed independently from the raw Lakh cells (x0.01). Representative and complete set of
every derived figure, margin, YoY/QoQ, bridge, and cash metric in A4. All tie within rounding.

| Metric | A4 value | My recompute | Source lines (Lakh) | Status |
|---|---|---|---|---|
| Consol Op EBITDA Q4FY26 | 52.35 | 30.94+17.16+8.79−4.54 = 52.35 | L118,114,113,104 | TIE |
| Consol Op EBITDA FY26 | 141.71 | (5,399.47+6,481.24+4,032.47−1,742.12)/100 = 141.71 | L118,114,113,104 | TIE |
| Consol Op EBITDA margin FY26 | 9.56% | 141.71/1,481.66 = 9.564% | L133/L103 | TIE |
| Consol Op EBITDA margin Q4FY26 | 12.35% | 52.35/423.94 = 12.35% | — | TIE |
| Consol Op EBITDA margin Q4FY25 | 14.84% | 51.10/344.38 = 14.84% | — | TIE |
| Consol Reported EBITDA Q4FY26 | 56.84 | (3,088.13+1,716.04+879.41)/100 = 56.84 | L120,114,113 | TIE |
| Consol Core PBT ex-OI FY26 | 36.53 | 53.95−17.42 = 36.53 | L120,104 | TIE |
| Consol ETR FY26 | 29.17% | 15.74/53.95 = 29.17% | L122+123 / L120 | TIE |
| Consol ETR Q4FY26 | 24.84% | 7.67/30.88 = 24.84% | — | TIE |
| Consol PAT margin FY26 | 2.58% | 38.21/1,481.66 = 2.58% | L124/L103 | TIE |
| Standalone Op EBITDA FY26 | 56.95 | 64.47+25.37+6.91−39.80 = 56.95 | L375,371,370,361 | TIE |
| Standalone Op EBITDA margin FY26 | 5.62% | 56.95/1,014.10 = 5.62% | — | TIE |
| Standalone ETR FY26 | 25.80% | 16.63/64.47 = 25.80% | L377+378/L375 | TIE |
| Standalone OI/PBT FY26 | 61.7% | 39.80/64.47 = 61.7% | L361/L375 | TIE |
| Revenue YoY Q4 | +23.10% | (42,394.13−34,437.99)/34,437.99 = 23.10% | L103 | TIE |
| Op EBITDA YoY Q4 | +2.45% | (52.35−51.10)/51.10 = 2.45% | — | TIE |
| Depreciation YoY Q4 | +25.02% | (1,716.04−1,372.63)/1,372.63 = 25.02% | L114 | TIE |
| Finance cost YoY Q4 | −8.86% | (879.41−964.86)/964.86 = −8.86% | L113 | TIE |
| Core PBT ex-OI YoY Q4 | −4.84% | (26.34−27.68)/27.68 = −4.84% | — | TIE |
| PAT YoY Q4 | −2.29% | (2,321.14−2,375.53)/2,375.53 = −2.29% | L124 | TIE |
| EPS Basic YoY Q4 | −7.46% | (8.68−9.38)/9.38 = −7.46% | L148 | TIE |
| Revenue YoY FY | +1.09% | (148,166.29−146,570.55)/146,570.55 = 1.09% | L103 | TIE |
| Op EBITDA YoY FY | −32.71% | (141.71−210.58)/210.58 = −32.70% | — | TIE |
| PAT YoY FY | −62.95% | (38.21−103.12)/103.12 = −62.95% | L124 (ref) | TIE |
| Revenue QoQ Q4 | +18.68% | (42,394.13−35,721.58)/35,721.58 = 18.68% | L103 | TIE |
| PAT bridge Op EBITDA | −68.87 | 141.71−210.58 = −68.87 | — | TIE |
| PAT bridge Depreciation | −9.84 | 64.81−54.97 = +9.84 drag | L114 | TIE |
| PAT bridge Finance | −2.23 | 40.32−38.09 = +2.23 drag | L113 | TIE |
| Reported PAT YoY change | −64.91 | 38.21−103.12 = −64.91 | — | TIE |
| Consol CFO/PAT FY26 | 4.47x | 170.70/38.21 = 4.468 | L303/L124 | TIE |
| Consol capex FY26 | 176.37 | (17,579.62+57.05)/100 = 176.37 | L306,307 | TIE |
| Consol FCF FY26 | −5.67 | 170.70−176.37 = −5.67 | — | TIE |
| WC inventory release FY26 | +57.81 | 5,780.68/100 = 57.81 | L297 | TIE |
| OpProfit-b4-WC vs CashGen uplift | 44.77 | 191.97−147.20 = 44.77 | L301,L293 | TIE |
| Receivable days FY26 | 48.7 | 197.75/1,481.66×365 = 48.71 | L219/L103 | TIE |
| Inventory days FY26 | 111.4 | 297.61/975.22×365 = 111.4 | L216/(L107+108+110) | TIE |
| Payable days FY26 | 32.7 | 87.31/975.22×365 = 32.7 | L247+248 | TIE |
| CCC FY26 | 127.4 | 48.7+111.4−32.7 = 127.4 | — | TIE |
| Standalone CFO/PAT FY26 | 1.31x | 62.77/47.83 = 1.31 | L546/L379 | TIE |
| Standalone net debt FY26 | ~+2.91 | 0.90+118.49−106.88−8.12−1.47 = 2.92 | L482,489,465,463,466 | TIE |
| Consol net worth gap | 21.54 below SA | 1,297.21−1,275.67 = 21.54 | L478 SA / L234 consol | TIE |
| Consol−SA PAT gap FY26 | −9.62 | 38.21−47.83 = −9.62 | L124/L379 | TIE |
| Consol−SA PAT gap FY25 | +27.64 | 103.12−75.48 = +27.64 | ref / L379 | TIE |
| Paid-up capital rise | +5.26% | 133.90/2,545.70 = 5.26% | L145 | TIE |
| FVTOCI equity loss FY26 vs FY25 | 7.60 vs 4.50 | 759.82/100 vs 450.23/100 | L137 | TIE |
| Labour-code past service (consol) | ~2.07 | (110.92+96.07)/100 = 2.07 | L179,181 | TIE |
| Consol FY25 PAT reconstruction | 103.12 (ref only) | 135.42−32.30 = 103.12; primary cell kept ND | L120,122,123 | TIE (derivation, not estimate) |
| Corrigendum reclass amount | 56.53 Lakh | 8,657.98−8,601.45 = 56.53; 130.04−56.53 = 73.51 (garbled wrong micro) | L58,56,247,248 | TIE |
| Corrigendum total unchanged | 8,731.49 | 130.04+8,601.45 = 8,731.49 | L61,247,248 | TIE |

**Arithmetic verdict: COMPLETE.** Zero mismatches above rounding across P&L extraction (both
statements, all five period columns), derived metrics, YoY/QoQ, the PAT bridge, cash-quality
ratios, working-capital days, and the corrigendum reconciliation. The consol FY25 PAT figure of
103.12 is a derivation from two legible line-anchored cells (PBT L120 minus total tax
L122+L123), not a substitution — A4 correctly keeps the primary cell ND.

---

## 3. ADVERSARIAL READ

Three most-positive claims in A4; strongest bear counter for each, built only from the extract;
does the counter survive un-incorporated (requiring a graft into A4)?

**Claim 1 — "CFO rose sharply +129.46 Cr; consolidated CFO/PAT 4.47x."**
Bear counter (same text): the 4.47x is manufactured by a depressed PAT denominator (38.21 Cr,
−63% YoY) and a one-time inventory destock of 57.81 Cr (L297); operating profit before WC
changes was only 147.20 Cr (L293) vs cash generated 191.97 Cr (L301), and FCF is negative at
−5.67 Cr after 176.37 Cr capex (L306-307).
Survives? **NO — already incorporated.** A4 marks cash conversion INDETERMINATE, states the
4.47x is "NOT a quality signal," names all three missing-evidence items, and caps the verdict
below plain PROCEED (Step 5A). No graft needed.

**Claim 2 — "Revenue grew +23.10% Q4 YoY; strong top-line."**
Bear counter (same text): core operating PBT ex-OI FELL −4.84% (27.68 to 26.34) while revenue
rose +23%, and Op EBITDA margin contracted −249 bps; the growth is volume/price-mix driven and
did not convert to core profit.
Survives? **NO — already incorporated.** A4 Step 2 diagnostics 1, 2 and 3 state exactly this.
No graft needed.

**Claim 3 — "Sequential margin recovery Q3 to Q4 (8.60% to 12.35%)" / "standalone near net-cash" / "unmodified audit opinion."**
Bear counters (same text): (a) the sequential bounce is still −249 bps below Q4FY25 14.84% and
Q3 was a labour-charge-loaded trough; (b) standalone is net-cash only because group debt sits at
the subsidiary level where consol current borrowings (L245) are illegible, and standalone OI is
61.7% of PBT (holdco/treasury: interest income 32.94 Cr L530, pref-share income L533-534); (c)
the unmodified opinion carries unknown weight because the full auditor report / Other Matters and
component-auditor coverage are not in the filing (A3-03).
Survives? **NO — all already incorporated.** A4 says "do not read the sequential bounce as
expansion" (Step 2 diag 2), reads standalone OI as structural holdco income (Step 1D, Step 5B),
and flags AUDITOR_REPORT_NOT_INCLUDED (0D caveat, Q11). No graft needed.

**Adversarial verdict: no surviving bear counter.** A4 is self-adversarial: every positive
claim already carries its bear counter from the same extracted text, and the SUMMARY states the
positives and negatives symmetrically. Nothing to graft.

### Adversarial-rigor checks demanded by the task

- **Every AMBIGUOUS/FORWARD-SIGNAL finding produces a management question:** YES. All ten A3
  findings map to at least one of the 13 Step-8.5 questions — A3-01→Q7, A3-02→Q1/Q12,
  A3-03→Q11, A3-04→Q2/Q3, A3-05→Q8, A3-06→Q9, A3-07→Q3/Q4, A3-08→Q5/Q6, A3-09→Q13, A3-10→Q10.
- **NOT FOUND values estimated anywhere:** NO. Both DPS (L162/L411), consol FY25 PAT (L124-132),
  and consol current borrowings (L245) are all kept NOT FOUND; Notion baselines (3.50 DPS,
  103.12 PAT, ~375.90 net debt) are cited explicitly and labelled non-re-verifiable, never
  silently substituted. The 103.12 reconciliation is a derivation from legible cells with the
  primary cell held ND — compliant with "NOT FOUND is the only valid fill."
- **Standalone-vs-consolidated first-class:** YES. Both statements carry full P&L, derived,
  balance-sheet and cash tables; the S-vs-C PAT inversion is the headline single metric (Step
  8C), reinforced by the net-worth gap (21.54 Cr) and ETR divergence (29.17% vs 25.80%).
- **Decision-Status change without a fired trigger:** NONE. WATCHLIST is carried unchanged and
  explicitly "flagged, not decided"; no thesis-broken condition is committed, so none fired.
- **Corrigendum reconciliation:** VERIFIED. 56.53 Lakh moved into micro/small MSME (other
  creditors 8,657.98→8,601.45; micro 73.51→130.04), total unchanged 8,731.49
  (130.04+8,601.45). A4 reconciles correctly and rightly notes the MSMED reclassification is
  "not purely clerical," raising the interest-liability/controls question (Q10).

---

## VERDICT

**COMPLETE.**

Coverage is complete: no orphan ledger row, no unreviewed disclosure unit, standalone and
consolidated both first-class. Arithmetic ties everywhere with zero mismatches above rounding.
No bear counter survives un-incorporated. No NOT FOUND value is estimated. No Decision-Status
change sneaks in. The corrigendum's single figure change reconciles.

One **non-blocking advisory to A2** (does not block save): the ledger's ZERO_STANDING summary
tally (L490) and YAML (`counts.zero_standing`) read 24, but the ledger's own tables enumerate
and flag 25 such rows (my independent grep confirms 25). Correct the summary count to 25. Every
one of the 25 nil lines is already enumerated in the ledger and reviewed by A4, so coverage is
unaffected; this is a cosmetic count correction only.

```yaml
stage: A5-adversary
company: "GANECOS"
quarter: "q4fy26"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
  advisory:
    - "A2 ZERO_STANDING summary tally reads 24 (ledger L490 / YAML counts.zero_standing) but ledger tables enumerate 25 flagged rows; fresh grep confirms 25. Non-blocking: all 25 rows are enumerated and reviewed. Correct summary to 25."
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
