# QUARTERLY PIPELINE A5 — ADVERSARY / COMPLETENESS AUDIT
# GEE Limited (GEE) — Q1 FY27 — RE-AUDIT (post A4 arithmetic-loop correction)

Fresh context. Re-derived independently from the A1 extract and A2 ledger; A4 cites
checked, not trusted. This is a re-audit after an A4 correction loop; the current
review is audited from scratch on its merits.

Anchor convention: extract line numbers are `cat -n` numbers of
`extract_results_gee_q1fy27.txt`. Filing unit = Rs Lakhs (line 69); Cr = Lakhs x 0.01.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

The MANDATORY PLAIN-LANGUAGE BRIEF (review lines 363-385) carries all four labelled
parts, each with real, non-placeholder content:

| Part | Heading present | Location | Non-empty | Status |
|---|---|---|---|---|
| (1) Summary narrative | yes ("### 1. SUMMARY NARRATIVE") | review L367-373 | 3 substantive paras, ~24 lines, line-anchored | PRESENT |
| (2) Sector intelligence | yes ("### 2. SECTOR INTELLIGENCE") | review L375-377 | real content (single-segment welding consumables, RM cost 64.7%, cyclicality) | PRESENT |
| (3) Business-model intelligence | yes ("### 3. BUSINESS-MODEL INTELLIGENCE") | review L379-381 | real content (trading-mix drift, asset-sale cash reliance) | PRESENT |
| (4) Competition intelligence | yes ("### 4. COMPETITION INTELLIGENCE") | review L383-385 | real content (EM 30, no pricing power, pledge/warrant profile) | PRESENT |

GATE 0: PASS. All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh grep enumeration diffed against A2 ledger)

Independent re-enumeration of the extract:

| Category | A2 count | My fresh count | Method | Orphan/missing | Status |
|---|---|---|---|---|---|
| Notes (fin results) | 6 | 6 | grep numbered notes L112-127: 1,2,3,4,5,6 (note 6 "6.The results", no space, still caught) | none | MATCH |
| Line items (table) | 28 | 28 | manual sweep L73-110, wraps (81, 104-105) and bare roman markers excluded | none | MATCH |
| Zero-standing rows | 4 | 4 | L89 (Q1FY26 dash), L95 & L96 (dash Q1FY27/Q1FY26), L106 (blank 3 cols) | none | MATCH |
| Agenda items | 5 | 5 | Board-outcome bullets L34-46 | none | MATCH |
| Auditor paras | 5 | 5 | L158,163,170,181 numbered + L188 unnumbered conclusion | none | MATCH |
| Signature blocks | 3 | 3 | grep "Digitally signed by" -> L54 (More), L130 (Agarwal) + auditor L190-201 (no digital metadata) | none | MATCH |
| Consolidation entities | 0 | 0 | standalone filing, no subsidiary list | none | MATCH |

No row my fresh pass found is absent from the ledger. No ledger row is absent from my pass.

Every ledger row cited in A4 or explicitly reviewed:
- All 6 notes: Step 0D notes table (review L40-45).
- All 28 line items: Step 1 data table (review L61-83) + derived table.
- 4 zero-standing rows: Step 1 note (review L85) plus exceptional/tax handling.
- 5 agenda items: Monitorables (review L350-354) + Step 6 trigger checks.
- 5 auditor paras: opinion check (review L47), unmodified conclusion cited (L188).
- 3 signature blocks: More (procedural), Agarwal (F14.1 date inconsistency, Q3 to mgmt), auditor (SAPD unchanged, trigger #2 not fired).
- SCOPE_LIMITATION (Board's/Corp Gov Report annexures absent upstream): explicitly carried as an UNREVIEWED flag to Role 6 (review L441). Correctly handled, not silently dropped.

COVERAGE: PASS. Zero orphan rows, zero rows missing from ledger.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw Lakhs)

| Metric | A4 value | Recomputed (from raw Lakhs) | Source lines | Status |
|---|---|---|---|---|
| Revenue YoY | +29.9% | 23.68/79.18 = 29.91% | 73 | OK |
| Revenue QoQ | -8.3% | -9.30/112.16 = -8.29% | 73 | OK |
| Op EBITDA Q1FY27 | 8.00 | 545.25+100.74+184.82-30.89 = 799.92 L | 88,84,83,74 | OK |
| Op EBITDA Q1FY26 | 4.54 | 130.41+101.55+224.49-2.27 = 454.18 L | 88,84,83,74 | OK |
| Op EBITDA Q4FY26 | 11.13 | 966.47+76.64+182.12-112.49 = 1112.74 L | 88,84,83,74 | OK |
| Op EBITDA FY26 | 33.40 | 2230.30+383.08+846.07-119.75 = 3339.70 L | 88,84,83,74 | OK |
| Op EBITDA margin Q1FY27 | 7.78% | 799.92/10285.66 = 7.78% | 88/73 | OK |
| Op EBITDA margin Q1FY26 | 5.74% | 454.18/7917.70 = 5.74% | 88/73 | OK |
| Op EBITDA margin YoY | +204 bps | 7.78 - 5.74 = +2.04 pp | derived | OK |
| Core PBT ex-OI Q1FY27 | 5.14 | 545.25-30.89 = 514.36 L | 88,74 | OK |
| Core PBT ex-OI Q1FY26 | 1.28 | 130.41-2.27 = 128.14 L | 88,74 | OK |
| Core PBT ex-OI YoY | +301.4% | 514.36/128.14 - 1 = 301.4% | derived | OK |
| ETR Q1FY27 | 25.17% | 230.24/914.79 = 25.17% | 97/90 | OK |
| ETR Q1FY26 | 25.17% | 32.82/130.41 = 25.17% | 97/90 | OK |
| ETR Q4FY26 | 44.03% | 278.59/632.70 = 44.03% | 97/90 | OK |
| ETR FY26 | 31.46% | 596.67/1896.53 = 31.46% | 97/90 | OK |
| PAT margin Q1FY27 | 6.66% | 684.55/10285.66 = 6.66% | 99/73 | OK |
| Finance cost YoY | -17.7% | -39.67/224.49 = -17.67% | 83 | OK |
| Depreciation YoY | -0.8% | -0.81/101.55 = -0.80% | 84 | OK |
| EBIT operating YoY | +98.3% | 699.18/352.63 - 1 = 98.3% | derived | OK |
| Reported PBT-after-exc YoY | +601.5% | 784.38/130.41 = 601.5% | 90 | OK |
| PAT YoY | +601.5% | 586.96/97.59 = 601.5% | 99 | OK |
| EPS YoY (share-adj) | +594.7% | 1.13/0.19 = 594.7% | 109 | OK |
| Exceptional as % PBT-after-exc | 40.4% | 369.55/914.79 = 40.40% | 89/90 | OK |
| RM cost / revenue Q1FY27 | 64.7% | 6649.85/10285.66 = 64.65% | 78/73 | OK |
| Warrant dilution | ~9.8% | 51/(1039.54/2)=51/519.77 = 9.81% | 103 | OK |
| EPS bonus-adjust check | 0.19 reported | 97.59/519.77 = 0.188 (bonus base); pre-bonus 97.59/259.885 = 0.375 | 99,103,109 | OK |

### Step-4 PAT bridge (the flagged prior-loop error — re-verified)

Reported PAT change denominator: 684.55 - 97.59 = **586.96 L = +Rs 5.87 Cr** (line 99).
The prior-loop +Rs 6.87 Cr Crore-conversion slip is CORRECTED to +Rs 5.87 Cr (review L9, L160). Confirmed correct.

| Bridge component | A4 (L) | Recomputed (L) | Basis | Status |
|---|---|---|---|---|
| Volume @ prior 5.74% margin | +135.83 | 2367.96 x 0.057365 = +135.84 | rev delta x prior margin | OK (rounding) |
| Margin change on Q1FY27 rev | +209.91 | (0.077766-0.057365) x 10285.66 = +209.83 | margin delta x rev | OK (rounding; vol+margin tie to Op EBITDA delta 345.74 L) |
| Depreciation change | +0.81 | 101.55-100.74 = +0.81 | line 84 | OK |
| Finance cost change | +39.67 | 224.49-184.82 = +39.67 | line 83 | OK |
| Other Income change | +28.62 | 30.89-2.27 = +28.62 | line 74 | OK |
| Exceptional (property sale) | +369.55 | line 89 / Note 4 | line 89,122 | OK |
| Tax change | -197.42 | 32.82-230.24 = -197.42 | line 97 | OK |
| **Sum** | **+586.96** | 135.83+209.91+0.81+39.67+28.62+369.55-197.42 = +586.97 | — | OK (ties to 586.96 within rounding) |

### Step-4 recurring / non-recurring split (denominator 586.96 L)

| Bucket | A4 % | Recomputed | Status |
|---|---|---|---|
| Core operating (135.83+209.91+0.81+39.67 = 386.22 L) | 65.8% | 386.22/586.96 = 65.80% | OK |
| Other Income (28.62 L) | 4.9% | 28.62/586.96 = 4.88% | OK |
| Exceptional property-sale gain (369.55 L, NON-RECURRING) | 63.0% | 369.55/586.96 = 62.96% | OK |
| Tax drag (-197.42 L) | -33.6% | -197.42/586.96 = -33.63% | OK |
| Sum | ~100% | 65.8+4.9+63.0-33.6 = 100.1% | OK |

The "~63% one-off" framing (review L9, L131, L184) is arithmetically correct against
the corrected 586.96 L denominator. The earlier "half one-off" framing is gone.

ARITHMETIC: PASS. No mismatch above rounding. The prior-loop error is fully repaired and
the dependent split percentages were recomputed against the correct denominator.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear from same text)

**Positive claim 1 (review L118, L129):** "Core operating PBT ex-OI grew +301.4% YoY
(4.0x), independent of Other Income and the exceptional gain — the single most honest
signal in the filing."
- Bear counter (from extract): the +301% is off a near-nil Rs 1.28 Cr base (line 88),
  and the "core operating" bucket embeds a Rs 0.40 Cr finance-cost saving (line 83) and
  a Rs 0.01 Cr depreciation benefit (line 84), i.e. part of the improvement is
  below-operating, not gross operating leverage. Sequentially, core PBT ex-OI fell from
  Rs 8.54 Cr (Q4) to Rs 5.14 Cr (Q1), down ~40% QoQ (line 88).
- Survives? NO — already grafted. Review L153 states ex-exceptional PBT fell 43.5% QoQ;
  Step 3 (L149) shows core PBT down QoQ; the finance/D&A components are itemised in the
  Step-4 bridge (L166-167). Counter is fully incorporated.

**Positive claim 2 (review L111, L125, L244):** "Revenue +29.9% YoY clears monitoring
trigger #2 (>=Rs 95 Cr) — GREEN, fired favourably."
- Bear counter (from extract): revenue is DOWN 8.3% QoQ from the Q4 peak of Rs 112.16 Cr
  (line 73), it is one print with Q2/Q3 FY26 absent (ND) so seasonality is untestable, and
  purchase of stock-in-trade jumped to Rs 13.61 Cr from Rs 0.06 Cr (line 79) — a trading
  overlay that inflates revenue at thinner margin.
- Survives? NO — already grafted. Review L125 warns "do not annualise a single print";
  L152 quantifies the -8.3% QoQ; L381 (Business-Model brief) flags the trading-mix drift.
  Counter is fully incorporated.

**Positive claim 3 (review L113, L127):** "Operating EBITDA margin expanded +204 bps YoY
to 7.78% — genuine margin expansion."
- Bear counter (from extract): 7.78% remains BELOW the FY26 full-year 9.05% (derived) and
  compressed 214 bps QoQ from Q4's 9.92% (line 88/73); combined material cost
  (RM + stock-in-trade + inventory change) is roughly flat YoY at ~77% of revenue
  (Q1FY26 77.5% vs Q1FY27 77.1%, lines 78-80,73), so the expansion is opex/finance
  leverage on a soft QoQ base, not pricing power (no disclosed price action).
- Survives? NO — already grafted. Review L127 states "still below FY26 9.05% and far
  below the 13% target"; L152 shows the 214 bps QoQ compression; L377 notes margin
  expansion "came without any disclosed pricing action." Counter is fully incorporated.

No surviving bear counter requires new grafting. All three strongest counters are already
present in the review with matching line anchors.

---

## VERDICT

**COMPLETE.**

- Gate 0 (plain-language brief, 4 parts): PASS.
- Coverage (fresh enumeration vs ledger; every row cited): PASS, zero orphans.
- Arithmetic (every derived metric incl. the Step-4 PAT bridge and its split): PASS.
  The prior loop's +Rs 6.87 Cr Crore-conversion error is correctly repaired to +Rs 5.87 Cr,
  and the recurring/non-recurring split (~63% one-off) is recomputed against the correct
  586.96 L denominator.
- Adversarial read: all three strongest bear counters already grafted; nothing to loop back.

Cleared to proceed to Notion save.

```yaml
stage: A5-adversary
company: "GEE"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
