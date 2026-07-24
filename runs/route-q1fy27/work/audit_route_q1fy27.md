# A5 ADVERSARY / COMPLETENESS AUDIT — Route Mobile Limited (ROUTE), Q1 FY27

Agent: A5 ADVERSARY (Opus 4.8) | Fresh context: A4 review + A1 extracts + A2 ledgers only.
Method: independent re-enumeration (fresh grep/sweep), independent recomputation of every derived
metric from raw extracted numbers, adversarial read on the three most positive claims.
Units re-derived at source: results Crores (x1), presentation Millions (x0.1 to Cr), pressrelease
Crores (x1). All cross-document ties re-checked under those conventions.

---

## AUDIT 1 — COVERAGE

Fresh enumeration walked each extract top-to-bottom and was diffed against the three A2 ledgers.

### 1A. Category counts (my fresh count vs A2 ledger)

| Doc | Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|---|
| results | notes (12 consol[9+3] + 10 standalone[9+1]) | 22 | 22 | none material | PASS |
| results | line_items (ConsolA 39 + SegB 21 + StdA 22 + IPOx2 10 + forex 1 + divsub 1) | 94 | 94 | none | PASS |
| results | zero_standing | 16 | 16 | none | PASS |
| results | agenda_items | 4 | 4 | none | PASS |
| results | auditor_paras (10 numbered + 4 continuation) | 14 | 14 | none | PASS |
| results | entities (subsidiary list) | 33 | 33 | none (2 renames noted, immaterial) | PASS |
| results | signature_blocks | 8 | 8 | none (Gupta/Shah/Mundra all referenced) | PASS |
| results | annexures | 2 | 2 | none | PASS |
| presentation | slides | 18 | 18 | none | PASS |
| presentation | numbers (121 semantic rows / 381 tokens) | 381 | 381 | 2 minor (see 1C) | PASS w/ note |
| presentation | zero_standing | 6 | 6 | none | PASS |
| presentation | footnotes | 10 | 10 | 2 minor (see 1C) | PASS w/ note |
| pressrelease | slides | 3 | 3 | none | PASS |
| pressrelease | slide_numbers | 33 | 33 | none | PASS |
| pressrelease | mgmt_claims_fwd_looking | 9 | 9 | none | PASS |
| pressrelease | footnotes_disclaimers | 1 | 1 | none | PASS |
| pressrelease | signatories_contacts | 2 | 2 | none | PASS |

Every A2 count reproduced token-for-token on my fresh pass. No row exists in my fresh pass that
the ledger lacks (no A2 loop-back). The A4 A2-reconciliation preamble (review L12-24) correctly
restates 22 notes / 94 line_items / 16 zero_standing / 4 agenda / 14 auditor_paras / 33 entities
and 18+3 slides; gate_a2 pass is confirmed independently.

### 1B. Material ledger rows traced into A4 (no orphans among the load-bearing rows)

- Consol P&L (all 39 rows) → Step 1.1, fully carried. Segment table (21 rows) → Step 4b (India
  -4.00, overseas 85.67, assets/liabilities incl. overseas liabilities -Rs 242 Cr YoY). Standalone
  (22 rows) → Step 1.2 / 4b.
- IPO utilisation (Rs 65 Cr unutilised) → C-4. QIP Rs 867.50 Cr → C-5. Forex note → C-6.
  Exceptional 7a/7b → C-7a/b. Dividend → C-8. Re-grouping → C-9. Dividend-from-subs Rs 4.22 → S-7.
  Cash-flow-hedge OCI (3.80) → "Consol A OCI" note. FCTR (16.27 vs 52.95) → monitorables.
- Auditor reliance (24 component-audited subs Rs 660.94 Cr / Rs 24.19 Cr; 11 foreign; 7 unreviewed
  Rs 1.12 Cr / Rs 0.02 Cr) → Auditor-opinion check + AMBER data-reliance flag. ESOP lapses
  (1,250 + 22,000) → 0C / checklist 12 / Q10. AGM, dividend record date, insider window → monitorables.
- Deck: revenue/GP/Adj-EBITDA/Adj-PAT charts, billable txns, new products, net cash Rs 1,345 Cr,
  Top-10 43%, partnerships (Truecaller/Konera/MWC), RCS "Coming Soon" → all carried (Steps 2/3/5/6,
  Section B claims inventory, monitorables).
- Press release: all 9 mgmt claims → Section B R5 Step 1 inventory (10 claims incl. 2 deck).
  NO_SAFE_HARBOR_DISCLAIMER → R5 0D / Step 7. UNSPECIFIED_MARKET_FACTORS → heavily covered.
  NO_PRIOR_MARGIN_COMPARATOR (7.94% PBT margin) → covered. ROLE_NOT_STATED (media contact) → trivial.

### 1C. Minor coverage notes (NON-BLOCKING — theme incorporated, specific datapoint not cited)

Two enumerated presentation rows carry a signal whose SUBSTANCE A4 incorporates but whose specific
figure A4 does not cite. Neither is a thesis-changing orphan, so neither blocks save; both are
recommended additions rather than FAILs:

- Slide 17 HR (ledger R118/R119): "35 New Employees joined / 60 Employees left in Q1 FY26-27"
  (net headcount -25 on a 783 base, excl. Call2Connect). A4 covers attrition via the ESOP-cessation
  lapse (checklist 12 / Q10) but does not cite the direct net-attrition datapoint. Recommend A4 add
  the 60-left/35-joined figure as corroboration of the attrition flag it already raised.
- Slide 11 footnotes (ledger R67/R68 = F2/F3): "Top 50 countries c. 86% of revenue" and "Top 150
  customers c. 92% of revenue." A4 covers concentration via Top-10 43% (GREEN) and the single
  large-account traffic drop (item 7 AMBER); the broader 86%/92% figures are not cited. See
  Audit 3, claim 3.

COVERAGE VERDICT: PASS. No material orphan rows; no rows missing from the ledger. gate_a2 confirmed.

---

## AUDIT 2 — ARITHMETIC

Every derived metric in A4's tables recomputed from raw extracted line items. Cross-document ties
recomputed under the mixed unit conventions (deck mn x0.1 to Cr). Sample of the full recheck below;
ALL A4 values reproduced within rounding.

### 2A. Consolidated derived metrics (results L304-369)

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Gross profit Q1FY27 (Rev-COGS) | 240.44 | 1,151.51-911.07 = 240.44 | L304,L309 | MATCH |
| Gross margin Q1FY27 | 20.88% | 240.44/1,151.51 = 20.88% | L304,L309 | MATCH |
| Gross margin Q1FY26 | 21.42% | 225.07/1,050.83 = 21.42% | L304,L309 | MATCH |
| Operating EBITDA Q1FY27 (PBT+D+FC-OI) | 105.48 | 91.47+23.71+1.36-11.06 = 105.48 | L317,L312,L311,L305 | MATCH |
| Op EBITDA margin Q1FY27 | 9.16% | 105.48/1,151.51 = 9.16% | — | MATCH |
| Op EBITDA Q1FY26 | 93.90 | 76.57+22.48+5.82-10.97 = 93.90 | L317,L312,L311,L305 | MATCH |
| Reported EBITDA Q1FY27 (PBT+D+FC) | 116.54 | 91.47+23.71+1.36 = 116.54 | — | MATCH |
| Core PBT ex-OI Q1FY27 | 80.41 | 91.47-11.06 = 80.41 | L317,L305 | MATCH |
| Effective tax rate Q1FY27 | 25.06% | 22.92/91.47 = 25.06% | L326,L321 | MATCH |
| ETR Q4FY26 | 17.84% | 24.84/139.27 = 17.84% | L326,L321 | MATCH |
| Current-tax-only rate Q1FY27 | 30.24% | 27.66/91.47 = 30.24% | L324,L321 | MATCH |
| PAT margin Q1FY27 | 5.95% | 68.55/1,151.51 = 5.95% | L329,L304 | MATCH |
| Other income / PBT Q1FY27 | 12.09% | 11.06/91.47 = 12.09% | L305,L321 | MATCH |

### 2B. Consolidated YoY (Step 2) and QoQ (Step 3)

| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| Revenue YoY | +9.58% | (1,151.51-1,050.83)/1,050.83 = +9.58% | MATCH |
| Gross profit YoY | +6.83% | (240.44-225.07)/225.07 = +6.83% | MATCH |
| Gross margin YoY | -54 bps | 20.88-21.42 = -0.54 pp | MATCH |
| Operating EBITDA YoY | +12.33% | (105.48-93.90)/93.90 = +12.33% | MATCH |
| Adj. EBITDA YoY (mgmt) | -5.60% | (108.93-115.39)/115.39 = -5.60% | MATCH |
| Adj. EBITDA margin YoY | -150 bps | 9.5-11.0 = -1.5 pp | MATCH |
| Finance costs YoY | -76.63% | (1.36-5.82)/5.82 = -76.63% | MATCH |
| Core operating PBT YoY | +22.58% | (80.41-65.60)/65.60 = +22.58% | MATCH |
| Reported PBT YoY | +19.46% | (91.47-76.57)/76.57 = +19.46% | MATCH |
| PAT YoY | +16.62% | (68.55-58.78)/58.78 = +16.62% | MATCH |
| EPS YoY | +17.63% | (9.94-8.45)/8.45 = +17.63% | MATCH |
| Revenue QoQ | +1.82% | (1,151.51-1,130.90)/1,130.90 = +1.82% | MATCH |
| PAT QoQ | -40.09% | (68.55-114.43)/114.43 = -40.09% | MATCH |
| GM QoQ | -246 bps | 20.88-23.34 = -2.46 pp | MATCH |

### 2C. Standalone + S-vs-C gap (Step 1.4 / Step 4b)

| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| Standalone Op EBITDA Q1FY27 | 5.57 | 20.25+3.90+0.39-18.97 = 5.57 | MATCH |
| Standalone Op EBITDA margin | 2.81% | 5.57/197.93 = 2.81% | MATCH |
| Standalone core PBT ex-OI | 1.28 | 20.25-18.97 = 1.28 | MATCH |
| Standalone OI/PBT Q1FY27 | 93.68% | 18.97/20.25 = 93.68% | MATCH |
| Standalone PAT YoY | -46.86% | (16.16-30.41)/30.41 = -46.86% | MATCH |
| Standalone Op EBITDA YoY | -65.5% | (5.57-16.14)/16.14 = -65.5% | MATCH |
| S-vs-C gap Q1FY27 (subs % of std PAT) | 324.2% | (68.55-16.16)/16.16 = 324.2% | MATCH |
| S-vs-C gap Q1FY26 | 93.3% | (58.78-30.41)/30.41 = 93.3% | MATCH |
| Standalone share of group PAT Q1FY27 | 23.6% | 16.16/68.55 = 23.6% | MATCH |
| India segment result Q1FY27 | -4.00 | L390 raw | MATCH |
| Overseas segment result YoY | +65.0% | (85.67-51.92)/51.92 = +65.0% | MATCH |

### 2D. PAT bridge (Step 4) — closes to the penny

+GP 15.37, -Employee 9.03, +Other-exp 5.24, -D&A 1.23, +Finance 4.46, +OI 0.09 = +14.90 PBT change
(= 91.47-76.57). Less tax 5.13 (22.92-17.79) = +9.77 PAT change (= 68.55-58.78). MATCH.

### 2E. Cross-document / unit-convention ties and deck non-GAAP recon

| Tie | A4 value | Recomputed | Status |
|---|---|---|---|
| Deck EBITDA 1,054.8 mn -> Cr vs results-derived Op EBITDA | 105.48 | 1,054.8 x 0.1 = 105.48 = PBT+D+FC-OI | MATCH |
| Deck GP 2,404 mn -> Cr vs Rev-COGS | 240.44 | 2,404 x 0.1 = 240.4 ~= 240.44 | MATCH (rounding) |
| Deck Adj. EBITDA recon | 1,089.3 mn | 1,054.8-28.1+49.0+13.6 = 1,089.3 | MATCH |
| Adj. EBITDA add-backs in Cr | 4.90 / 1.36 / 2.81 | 49.0/13.6/28.1 mn x0.1 | MATCH |
| Net cash 13,452 mn -> Cr | 1,345.2 | 13,452 x 0.1 | MATCH |
| New products YoY (deck chart 830/945) | 13.9% | (945-830)/830 = 13.86% | MATCH |
| New products QoQ (855/945) | 10.5% | (945-855)/855 = 10.53% | MATCH |
| New products mix Q1FY27 | 8.2% | 945/11,515 = 8.21% | MATCH |
| Billable txns YoY (39.3/45.8 bn) | +16.5% | (45.8-39.3)/39.3 = +16.54% | MATCH |
| Realization/txn change | ~-6% | 0.2514 vs 0.2674 Rs/txn = -5.98% | MATCH |
| PR PBT margin | 7.94% | 91.47/1,151.51 = 7.944% | MATCH |
| Component-auditor revenue share | 57.5% | (660.94+1.12)/1,151.51 = 57.49% | MATCH |
| Component-auditor PAT share | 35.3% | (24.19+0.02)/68.55 = 35.32% | MATCH |
| Hurdle Ratio @12% CAGR | ~1.89 | (1.12)^3 x (17.9/13.3) = 1.405 x 1.346 = 1.891 | MATCH |
| TTM EPS | ~39.4 | 37.94-8.45+9.94 = 39.43 | MATCH |

ARITHMETIC VERDICT: PASS. Zero mismatches above rounding across consolidated, standalone, YoY, QoQ,
the PAT bridge, the S-vs-C gap, deck non-GAAP reconciliation, and all mixed-unit cross-ties.

Note (not an arithmetic error): two figures A4 cites are carried from Notion/A3 memory and are NOT
in this cycle's extracts — the "~Rs 491 Cr goodwill pile (Rs 40 Cr already impaired on M.R.
Messaging)" (Q12) and the "New Products mix 11.3% in FY26" comparator. A4 attributes both to
memory/finding sources, does not present them as derived from the filing, and the current-quarter
8.2% mix that IS derived reconciles exactly. Flagged as external-provenance, not a computation FAIL.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive A4 claims, strongest bear counter from the same text)

### Claim 1 (most positive): "Revenue +9.58% YoY, above the 5-9% FY27 guide top; clears the +1.8% bull binary." (review L143, L276)
Strongest bear counter from the extract: growth is bought with price, not won on value. Billable
transactions rose +16.5% (39.3->45.8 bn, deck L392) but revenue rose only +9.58% and gross profit
only +6.83% (240.44 vs 225.07) — realization/txn fell ~6% (Rs 0.267->0.251) and gross margin
contracted -54 bps YoY / -246 bps QoQ (deck L408). QoQ revenue was only +1.82%.
SURVIVES? NO — already fully incorporated by A4 (Step 2 diagnostic 1, Step 6D, Section C: "revenue
grew slower than volume ... pricing/mix-compression tell"). No graft required.

### Claim 2: "Net cash Rs 1,345 Cr — GREEN (>= Rs 800 Cr), balance-sheet strength; no leverage concern." (review L254-255, checklist 10)
Strongest bear counter from the extract: (a) the figure is DECK-ONLY (L109) and unverifiable from
the filing — Q1 carries no Reg-33 balance sheet or cash flow; (b) net cash fell ~Rs 44 Cr QoQ with
no CFO to attribute the draw (cash conversion INDETERMINATE); (c) capital deployment is stalled —
Rs 65 Cr IPO office-premises object unutilised ~6 years (note C-4, L447) and Rs 867.50 Cr QIP parked
in FDs (C-5); (d) pending draws (Rs ~25 Cr dividend + undisclosed Heltar consideration).
SURVIVES? NO — A4 already carries every leg (Step 5 INDETERMINATE + -44 Cr draw, Step 7 "UNVERIFIABLE
from the filing," C-4 stalled deployment, C-5 parked QIP). No graft required.

### Claim 3: "Top-10 customer concentration 43% — GREEN." (review L295, checklist 6)
Strongest bear counter from the extract: the Top-10 cut understates concentration. The deck's own
footnotes (slide 11, L327/L328) show Top-50 countries = c.86% and Top-150 customers = c.92% of Q1
revenue, and a SINGLE large account's "transitory traffic reduction" (deck L412) was material enough
to move group gross margin -246 bps QoQ. A 43% Top-10 that reads GREEN sits on a revenue base that is
92%-dependent on 150 customers and demonstrably sensitive to one account.
SURVIVES? NO (substance already incorporated), but with a NON-BLOCKING completeness recommendation.
A4 already flags the single-account lumpiness (checklist item 7 AMBER) and the 35.3%-PAT /
57.5%-revenue component-auditor concentration, so the concentration-risk SUBSTANCE is in the review
and the GREEN on the specifically-defined Top-10 threshold (<=45%) is correct. The 86%/92% footnotes
(ledger R67/R68) are the specific figures A4 did not cite; recommend A4 add them as corroboration to
item 6/7. This does not change the verdict, the flag set, or the position decision, so it is a
recommended addition rather than a surviving counter that blocks save.

No bear counter survives as a thesis- or verdict-changing addition: A4's review is already
symmetrically bearish and pre-incorporates the substance of all three counters.

---

## VERDICT

**COMPLETE.**

- Coverage: every A2 ledger count reproduced independently; no material orphan rows; nothing in my
  fresh pass is missing from the ledger. Two non-blocking specific-datapoint recommendations
  (60-left/35-joined net attrition; Top-50=86% / Top-150=92% concentration footnotes) — themes
  already incorporated by A4.
- Arithmetic: zero mismatches above rounding across all consolidated/standalone/YoY/QoQ metrics, the
  PAT bridge, the S-vs-C gap, deck non-GAAP reconciliation, and all mixed-unit cross-document ties.
- Adversarial read: none of the three counters survive as verdict-changing; A4 pre-incorporates their
  substance. The one completeness recommendation (concentration footnotes) is non-blocking.

Proceeds to Notion save. Recommended (optional, non-gating) A4 additions before save: cite the
60-employees-left net-attrition datapoint (deck slide 17) and the Top-150=92% / Top-50-countries=86%
concentration footnotes (deck slide 11) as corroboration of flags A4 already raised.

```yaml
stage: A5-adversary
company: "ROUTE"
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
