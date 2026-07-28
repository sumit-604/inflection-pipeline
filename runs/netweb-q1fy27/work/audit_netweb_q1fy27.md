# A5 ADVERSARY / COMPLETENESS AUDIT — Netweb Technologies India Limited (NETWEB), Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Fresh context (A4 review + A1 extracts + A2 ledgers only).
Quarter: Q1 FY27 (ended 30-Jun-2026). Units: filing in Rs Millions (extract L186), converted x0.1 to Rs Cr.
No concall supplied this quarter (Role 5 N.A.) — verified A4 fabricated no concall content (see Audit 3, note C).

Method: I re-ran the enumeration with my own pass over each A1 extract and diffed against the A2 ledgers;
I recomputed every derived metric in A4's tables from the raw reconciled Millions figures (results extract
lines 288-326), independent of A4's and A3's cites. Values used are the A1 footed/reconciled cells, but every
arithmetic operation below is my own.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledgers vs A4 citation)

### 1A. RESULTS ledger (`ledger_results_netweb_q1fy27.md`)

| Category | A2 count | My fresh count | Basis of my count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|---|
| Notes (page 5) | 6 | 6 | Numbered items L373/382/386/391/394/412 | none — all 6 in A4 Step 0D note table | PASS |
| Line items (reconciled P&L) | 26 | 26 | Rows L288-326, less 2 header lines | see 1C (OCI rows) | PASS (with note) |
| Zero-standing | 1 | 1 | Exceptional items L302 dash x4 | none — A4 F1 (nil all periods) | PASS |
| Agenda items | 4 | 4 | Financial Results / Dividend / AGM / Cost Auditor L66-95 | none — A4 monitorables cover all 4 | PASS |
| Auditor paras | 4 | 4 | Numbered paras L135/142/149/157 | none — A4 0D cites para 4 clean conclusion | PASS |
| Entities | 2 | 2 | Netweb Tech (L46) + Netweb Foundation (L386) | none — A4 F2 / sc_gap note | PASS |
| Annexure items | 4 | 4 | Cost-auditor Annexure-2 rows L433-438 | none — A4 monitorables (cost auditor) | PASS |
| Signature blocks | 3 | 3 | Lohit Chhabra (CS) / Jalaj Soni (auditor) / Sanjay Lodha (MD) | none material — covered by blanket "all rows reviewed"; administrative, no forensic | PASS |

### 1B. PRESENTATION ledger (`ledger_presentation_netweb_q1fy27.md`)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides (pages) | 3 | 3 | none | PASS |
| P&L line items | 7 | 7 | none — all in A4 Step 1 / Step 6A | PASS |
| Zero-standing | 0 | 0 | n/a | PASS |
| Footnotes | 3 | 3 | none — non-std EBITDA def + margin denominator both handled by A4 F16-4 | PASS |
| Slide numbers | 72 | 72 (spot-checked key figures) | none — Net Debt 1,999.00, Order Book 25,069.35, AI 5,105.70, HPC 1,252.94, PC 1,353.46, L1 8,480.47 all consumed by A4 | PASS |
| Admin identifiers | 16 | 16 | none (administrative, out of financial scope) | PASS |
| CMD sentences | 11 | 11 | none — CMD macro/forward claims in A4 6D | PASS |
| CMD qualitative | 9 | 9 | none | PASS |

All presentation ledger flags are represented in A4: SEGMENT_DISCLOSURE_ASYMMETRY (F16-3),
MARGIN_DENOMINATOR_NOTE + NONSTANDARD_EBITDA_DEFINITION (F16-4), NEW_DISCLOSURE HPC/PC/L1 (Q7/order book),
OCR_ECHO / OCR_RECOVERED_LABEL (methodological), SUPERLATIVE/FORWARD/HEDGE (6D demand-pillar). No orphan.

### 1C. The only coverage item worth flagging (resolved PASS, not a FAIL)

The four OCI-region rows in the results ledger — Re-measurement gains/(losses) on defined benefit plans
(L315, Rs 0.86 Cr net), Income tax on OCI (L316), Total OCI (L317), Total comprehensive income (L319) — do
**not** appear as line items in A4's Step 1 data table. A3 raised **no** finding on any of them and A4's
LEDGER-RECONCILIATION PREAMBLE states explicitly "All rows reviewed... No ledger row is unreviewed." The OCI
remeasurement is Rs 0.86 Cr (immaterial, standard defined-benefit accrual, consistent across all four period
columns) and carries no thesis relevance. This qualifies as "reviewed, no finding," not an orphan. **No loop-back.**

### 1D. Fresh-pass rows the ledgers LACK

My independent sweep of both extracts found **no** disclosure unit (note, line item, agenda item, entity,
annexure row, footnote, CMD sentence, or slide number) that the A2 ledgers failed to enumerate. No FAIL to A2.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract, not from A4)

Raw source = reconciled Millions table (results extract L288-326); press-release headline figures (L117-131).
All A1 footing checks (Total income, Total expenses, Total tax, PAT, OCI, TCI across all 4 columns) independently
re-verified as internally consistent before recomputation.

| Metric | A4 value | My recomputed value | Source line(s) | Status |
|---|---|---|---|---|
| Revenue Cr (Q1FY27/Q4FY26/Q1FY26/FY26) | 819.69/773.70/301.21/2183.56 | 819.686/773.702/301.212/2183.563 | L288 | MATCH |
| Op EBITDA Q1FY27 (PBT+Dep+Fin−OI) | 120.52 | 114.14+3.33+11.52−8.47=120.52 | L303/297/296/289 | MATCH |
| Op EBITDA Q4FY26 | 96.57 | 94.822+3.834+8.153−10.235=96.574 | L303/297/296/289 | MATCH |
| Op EBITDA Q1FY26 / FY26 | 44.80 / 284.84 | 44.802 / 284.842 | same | MATCH |
| Op EBITDA margin (4 cols) | 14.70/12.48/14.87/13.04% | 14.703/12.482/14.873/13.045% | derived | MATCH |
| Core PBT ex-OI (4 cols) | 105.67/84.58/40.50/257.68 | 105.67/84.58/40.50/257.68 | L303−L289 | MATCH |
| Effective tax rate (4 cols) | 25.25/25.55/26.74/25.57% | 25.25/25.55/26.744/25.57% | L309/L303 | MATCH |
| PAT margin on Rev (Q1FY27) | 10.41% | 85.32/819.69=10.410% | L311/L288 | MATCH |
| PAT margin on Total Income (4 cols) | 10.30/9.00/10.08/9.35% | 10.30/9.00/10.08/9.345% | L311/L290 | MATCH |
| Revenue YoY | +172.1% | (819.69−301.21)/301.21=172.13% | L288 | MATCH |
| Op EBITDA YoY | +169.0% | 75.72/44.80=169.0% | derived | MATCH |
| Finance cost YoY | +1078.3% (11.8x) | 11.524/0.978=11.783x → +1078.3% | L296 | MATCH |
| Core operating PBT YoY | +160.9% | (105.666−40.507)/40.507=160.86% | derived | MATCH |
| PAT YoY / EPS YoY | +179.9% / +178.4% | 179.94% / 178.44% | L311/L325 | MATCH |
| Revenue QoQ | +5.9% | (819.69−773.70)/773.70=5.94% | L288 | MATCH |
| PAT bridge sum | +54.84 | 75.72−0.01−10.54+7.36−17.69=54.84 = 85.32−30.48 | Step 4 | MATCH |
| Recurring core engine | +65.17 | 75.72−0.01−10.54=65.17 | derived | MATCH |
| Deferred-tax credit share of PAT change | ~6.5% | 3.59/54.84=6.55% | L308 | MATCH |
| Other income share of PAT change | 13.4% | 7.36/54.84=13.42% | L289 | MATCH |
| Net-debt swing | −283.2 Cr | 83.3+199.90=283.2 | press L102 + Notion | MATCH |
| Order book / L1 | 2,506.9 / 848.0 Cr | 25,069.35/8,480.47 Mn x0.1 | press L106/L153 | MATCH |
| AI Systems rev / % of rev | 510.57 Cr / 62.29% | 5,105.70 Mn; 510.57/819.69=62.29% | press L108 | MATCH |
| HPC / Private Cloud Cr | 125.3 / 135.3 | 1,252.94 / 1,353.46 Mn x0.1 | press L152 | MATCH |
| Residual non-AI/HPC/PC share | ~5.9% | 100−62.29−15.29−16.51=5.91% | derived | MATCH |
| 285k share issuance | 285,000 | (113.88−113.31)Mn/2 = 0.285 Cr shares | L321 | MATCH |
| EPS internal check | 14.98 | 85.32Cr/(5.694 Cr sh)=14.98 | L311/L321 | MATCH |
| Finance Q1 as % of FY26 finance | ~89% | 11.52/12.95=88.97% | L296 | MATCH |
| PAT ex deferred-tax credit | ~81.73 | 85.32−3.59=81.73 | L311/L308 | MATCH |

**Zero arithmetic mismatches above rounding.** Every derived metric in A4's tables reconciles to the raw
reconciled extract. The press-release Op EBITDA quartet (1,205.15 / 965.74 / 448.02 / 2,848.42 Mn) also foots
exactly to PBT+Dep+Fin−OI in each column, independently confirming A1's non-standard EBITDA reconstruction.

---

## AUDIT 3 — ADVERSARIAL READ (strongest bear for A4's 3 most positive claims, from the same extract)

**Claim 1 — "Headline growth is real and operating-led: core operating PBT +160.9%, ~80%+ of the PAT
increase recurring" (A4 Step 2 diag 3, Step 4).**
Strongest bear from the extract: the flat-to-up margin and PBT are cushioned by two credits that reduced the
expense/tax lines this quarter — a Rs 97.04 Cr WIP BUILD (Change in inventories (970.39) Mn, L294, a credit to
expense, 12.3x the Q4FY26 (78.72) and sign-flipped from the +194.37 Q1FY26 draw) and a Rs 3.59 Cr deferred-tax
CREDIT (L308, sign-flipped from prior charges). Cost of materials consumed is 90.7% of revenue (743.28/819.69)
vs 67.9% a year ago — a raw gross-margin compression consistent with thin-value-add GPU pass-through.
**Survives?** NO. A4 already incorporates all three: the WIP build as a normal accrual that "will unwind as WIP
delivers" (L138, L142, L166-167, S1), the deferred-tax credit (F8, L168, Q9), and gross-margin compression /
"few large GPU deals" (L107, L253, Q4). Not grafted — already present.

**Claim 2 — "Op EBITDA margin 14.70%, top of the 13-14% guide, held flat YoY / +222 bps QoQ; margin durable"
(A4 Step 2 diag 2, 6D).**
Strongest bear: the flat margin is only held because opex leverage (Other expenses 3.4% of rev vs 5.4%;
Employee 3.0% vs 5.3%) offsets a real gross-margin compression, AND the QoQ base (Q4FY26) is a Note-2 BALANCING
FIGURE (L382) — derived, not independently reported — so the +222 bps "recovery" is measured against a soft base.
**Survives?** NO. A4 flags the Note-2 balancing-figure caveat explicitly (L137, L142) and tags margin durability
"ON TRACK (watch mix)" (L253). Already present.

**Claim 3 — "No thesis-broken trigger fired; net-debt swing is growth-induced; thesis MAINTAINED, HOLD"
(A4 Section C).**
Strongest bear: the net position swung Rs 283.2 Cr into net debt (absorbing 3.3x the Rs 85.32 Cr PAT), finance
cost jumped 11.8x to Rs 11.52 Cr (89% of ALL FY26 finance cost in one quarter) with NO borrowings/WCDL note in
the reviewed filing, and the reviewed statement carries NO cash flow, NO balance sheet, and NO
receivables/inventory/payables split. The Rs 199.90 Cr net-debt figure itself is sourced only to the UNREVIEWED
press release (L102), not the limited-reviewed results. So "growth-induced, not structural" is unverifiable from
the extract.
**Survives?** NO. This is precisely what A4 caps the verdict on: cash conversion INDETERMINATE, "structural-vs-
growth cannot be confirmed at Q1" (L194), verdict held at PROCEED WITH CAVEATS with the missing evidence named
(H1 cash flow + balance sheet, receivable/inventory/payable split, strategic-order revenue split). This bear IS
the verdict driver, not an omission.

**No surviving bear counter requires grafting into A4.** All three strongest counters are already incorporated.

### Cross-checks on the two contested calls in the task brief

**(A) INDETERMINATE cash-conversion call.** A4 does NOT resolve it to PROCEED; it caps at PROCEED WITH CAVEATS
and names the missing evidence (H1 FY27 cash flow statement + balance sheet). This is the exact behaviour the
CLAUDE.md NEVER rule mandates. Correct. A Q1 standalone Reg-33 filing carrying only a P&L (no BS/CFS) is
consistent with the extract — the results extract (6 pp) indeed contains no cash flow or balance sheet, so "no
Q1 cash flow exists" is a fact, not an evasion. Correct call.

**(B) PROCEED WITH CAVEATS verdict.** Verdict is inside the allowed set (CLAUDE.md). Rationale (strong quarter,
no trigger fired, but cash conversion unconfirmable) is supported by the extract and correctly bounded. No
downgrade or over-claim. Correct.

**(C) No fabricated concall content.** Section B declares Role 5 N.A. and produces no claims inventory / Q&A /
guidance table of its own. Where A4 cites "35-40% organic CAGR," "~35% AI normalisation," "CCC 90-110 days,"
"ST borrowing to fall" it attributes them to the FY26 **Q4** concall / Notion memory used as a PRIOR-period
yardstick — not to a Q1 FY27 call. The presentation ledger has 0 concall turns; A4 reports 0 turns. Consistent.
No fabrication. (Notion-sourced figures — avg cost, re-entry zone, destination PE 38x, ROCE 37.5%, FY26 CFO/PAT
83.3%, CCC 84 days, order book Mar-26 2,097 Cr, promoter 66.98% — are memory inputs outside the A1 extracts and
are correctly labelled as such; they are not re-derivable from the extract and are not treated as a gap.)

---

## VERDICT

**COMPLETE.**

- Coverage: both A2 gates independently reproduced; every ledger row cited in A4 or covered by the blanket
  "reviewed, no finding" statement (immaterial OCI rows resolved PASS). No orphan row; no fresh-pass row the
  ledger lacks.
- Arithmetic: zero mismatches above rounding across every derived metric in A4's tables.
- Adversarial: the three strongest bear counters are all already incorporated in A4; none survives to be grafted.
- The INDETERMINATE cash-conversion call and the PROCEED WITH CAVEATS verdict are correctly applied per the
  CLAUDE.md NEVER rule; no concall content fabricated.

Only COMPLETE proceeds to Notion save.

```yaml
stage: A5-adversary
company: "NETWEB"
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
