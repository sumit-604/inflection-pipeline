# A5 ADVERSARY / COMPLETENESS AUDIT — GE Power India Limited (GVPIL) — Q1 FY27

Re-audit after one loop. Fresh context: A4 review, A1 extract, A2 ledger only. Every number below re-derived
from the A1 extract (Rs Cr = filing millions x0.1). A4's and A3's cites were checked, not trusted.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

Plain-Language Brief located at A4 lines 373-389. All four labelled parts present and carry real content:

| Part | Location | Present? | Content check |
|---|---|---|---|
| 1. Summary narrative | L375-377 | present | ~15-line narrative; revenue +7.7%, margin story, OI −40%, tax caveat, no-action verdict |
| 2. Sector intelligence | L379-381 | present | FGD-fade vs aftermarket bifurcation, Labour Codes, provenance-tagged |
| 3. Business-model intelligence | L383-385 | present | two revenue engines, model drift to services, dormant sub, JV collapse, provenance-tagged |
| 4. Competition intelligence | L387-389 | present | BHEL/Thermax/ISGEC/Siemens, oOEM %, backlog risk, provenance-tagged |

GATE 0 = PASS. No placeholder or empty section.

---

## AUDIT 1 — COVERAGE (fresh grep pass vs A2 ledger)

Independent re-enumeration (grep + line-by-line read) reconciled to A2's counts:

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| notes | 17 | 17 (8 std + 9 consol; consol note 1 unnumbered at L486, confirmed via "refer note 9" L426) | manual sweep + numeral grep | none | PASS |
| line_items | 94 | 94 (40 std + 44 consol + 10 embedded discontinued-ops rows) | every P&L number re-derived and matched | none | PASS |
| zero_standing | 15 | 15 (std L193,197,203,206,207,208,219; consol L447,451,457,460,461,462,470,475) | flag sweep | none | PASS |
| agenda_items | 2 | 2 (approval L51-53; noted LR L52-54) | grep | none | PASS |
| auditor_paras | 10 | 10 (std 4 + consol 6; incl. Other-Matters JV para L385-395) | grep on report headers | none | PASS |
| entities | 2 | 2 (GE Power Boilers Services subsidiary L365; NTPC GE JV L366) | grep | none | PASS |
| signature_blocks | 5 | 5 (Vipul Sharma CS L85; Vikas Khurana L150 + L403; Puneet Bhatla L301/305 + L555/560) | grep | none | PASS |
| media_release_items | 8 | 8 (headline + 5 bullets + MD quote + about/contact) | grep on page 9 | none | PASS |
| turns / slides / questions | 0 / 0 / 0 | 0 / 0 / 0 | no concall/deck supplied | none | PASS |

**Ledger-row-to-A4 traceability.** Every material A2 row is reflected in A4 or explicitly reviewed-no-finding:
- Notes 2(i)/3(i) Durgapur-JSW demerger — Step 0D, 6B#7, 6C#6, monitorables, brief. Covered.
- Notes 2(ii)/3(ii) discontinued-ops detail — Step 1 (13.44)/qtr drag, Step 4 disc row. Covered.
- Notes 3/4 Labour Codes (Rs 42.57 Cr FY26 exceptional) — Step 0D, sector intel. Covered.
- Notes 4/5 BHEL settlement (Rs 3,430.6m, ECL reversals 23.5/37.18/44.37) — Step 1C footnote, Step 3, 6B#8. Covered and quantified correctly.
- Notes 5/6 single segment — Step 0D, F12 N.A. Reviewed-no-finding.
- Notes 6/7, 7/8, 8/9 (approval, LR filing, balancing figure) — Step 0D, QoQ caution. Covered.
- Entities (subsidiary dormant, JV) — Step 1D, business-model intel (F3-01), JV reliance gate (F4). Covered.
- Signature blocks — MD-alone / no-CFO-countersignature flag surfaced (6B#9, L264). Covered.
- Media release order backlog −41.4% / EBITDA 22.5% / MD quote — Step 1C, checklist, Q1. Covered.
- Zero-standing (nil exceptionals in quarters, nil deferred tax) — Step 1 tables. Covered.
- A2 FORMATTING_GAP flags (L447, L468) and OCR_ARTIFACT flags are enumeration-quality notes; the numeric
  values A4 relied on are internally consistent with every derived total (see Audit 2). Not material gaps.

No orphan rows (nothing in the ledger absent from A4). My fresh pass surfaced no row the ledger lacks.

*Observation (not a gate failure):* A4 lists "A3-F14-01" among incorporated findings (L19, yaml L405) but the
body carries no F14 narrative. This concerns A3's finding register, which is NOT in my inputs; no A2 ledger row
is left uncovered, so it is not a coverage FAIL. Flag surfaced for the orchestrator's awareness only.

COVERAGE = PASS.

---

## AUDIT 2 — ARITHMETIC (every derived metric re-computed from raw extract)

Raw standalone (Rs Cr): Q1FY26 / Q4FY26 / Q1FY27 / FY26. All Step 1A/1B figures re-derived from L176-224 /
L428-480 and matched to the rupee. Derived metrics:

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+Fin−OI) | 44.72 | 68.82+3.27+4.51−31.88 = 44.72 | L191,186,185,177 | MATCH |
| Op EBITDA Q1FY26 | (0.07) | 44.02+3.43+5.58−53.10 = (0.07) | L191,186,185,177 | MATCH |
| Op EBITDA Q4FY26 | 106.76 | 118.85+3.01+4.37−19.47 = 106.76 | " | MATCH |
| Op EBITDA FY26 (uses PBT pre-exceptional 339.90) | 259.44 | 339.90+12.28+21.90−114.64 = 259.44 | L191,186,185,177 | MATCH |
| Op EBITDA margin Q1FY27 | 14.5% | 44.72/308.69 = 14.49% | L176 | MATCH |
| Reported EBITDA Q1FY27 | 76.60 | 68.82+3.27+4.51 = 76.60 | " | MATCH |
| Rep EBITDA margin on Total Income Q1FY27 | 22.5% | 76.60/340.57 = 22.5% (ties media release L586) | L179 | MATCH |
| Rep EBITDA margin on Total Income Q1FY26 | 15.6% | 53.03/339.83 = 15.6% (ties media release) | L179 | MATCH |
| Core PBT ex-OI Q1FY27 | 36.94 | 68.82−31.88 = 36.94 | L191,177 | MATCH |
| Core PBT ex-OI Q1FY26 | (9.08) | 44.02−53.10 = (9.08) | " | MATCH |
| Core PBT ex-OI Q4FY26 | 99.38 | 118.85−19.47 = 99.38 | " | MATCH |
| ETR Q1FY27 | 4.1% | 2.83/68.82 = 4.11% | L196,194 | MATCH |
| PAT margin Q1FY27 | 21.4% | 65.99/308.69 = 21.38% | L198,176 | MATCH |
| YoY Revenue | +7.66% | (308.69−286.73)/286.73 = +7.66% | L176 | MATCH |
| YoY Finance cost | (19.2%) | (4.51−5.58)/5.58 = −19.18% | L185 | MATCH |
| YoY Depreciation | (4.7%) | (3.27−3.43)/3.43 = −4.66% | L186 | MATCH |
| YoY Other income | (40.0%) | (31.88−53.10)/53.10 = −39.96% | L177 | MATCH |
| YoY PBT cont | +56.3% | (68.82−44.02)/44.02 = +56.3% | L194 | MATCH |
| YoY PAT cont | +49.9% | (65.99−44.02)/44.02 = +49.9% | L198 | MATCH |
| YoY Net profit | +66.2% | (52.55−31.61)/31.61 = +66.2% | L210 | MATCH |
| YoY EPS total | +66.4% | (7.82−4.70)/4.70 = +66.4% | L224 | MATCH |
| Core PBT swing | +46.02 | 36.94−(−9.08) = +46.02 | L191,177 | MATCH |
| JV % of consol PBT Q1FY27 | 1.7% | 1.18/70.00 = 1.69% | L443,445 | MATCH |
| JV PAT as % consol PAT (reliance gate) | 2.2% | 1.18/53.73 = 2.2% (<10%) | L443,464 | MATCH |
| Net worth std (Q5) | 543.8 | 476.54+67.23 = 543.77 | L219,217 | MATCH |
| Net worth consol (Q5) | 582.5 | 515.31+67.23 = 582.54 | L475,473 | MATCH |
| Q4 adj Op EBITDA (ex-ECL 44.37) | ~62.39 | 106.76−44.37 = 62.39 (margin 19.7%) | L187 note | MATCH |
| FY26 adj Op EBITDA (ex-ECL 105.05) | ~154.4 | 259.44−105.05 = 154.39 (margin 12.2%) | note 4/5 | MATCH |
| BHEL ECL total | 105.05 | 23.5+37.18+44.37 = 105.05 Cr | L277-278 | MATCH |
| Backlog YoY | −41.4% | (1545.4−2635.3)/2635.3 = −41.36% | L590-592 | MATCH |

### PAT BRIDGE (Step 4) — the prior loop-back item, re-derived from scratch

Net profit Q1FY26 = PAT cont 44.02 + discontinued (12.41) = 31.61 (L210). Q1FY27 = 65.99 + (13.44) = 52.55.
Total YoY change = 52.55 − 31.61 = **+20.94**.

A4's corrected component set (L195-200):
- Core operating PBT ex-OI (already net of D&A and finance): **+46.02**
- Other Income change: 31.88 − 53.10 = **(21.22)**
- ETR change (0 → 2.83 tax): **(2.83)**
- Exceptional: **0.00**
- Discontinued-ops change: (13.44) − (12.41) = **(1.03)**

Foot: 46.02 − 21.22 − 2.83 + 0.00 − 1.03 = **+20.94**. **MATCH.**

Cross-check by construction: continuing PBT change = 68.82 − 44.02 = 24.80 = core swing 46.02 + OI swing
(−21.22). Less tax 2.83 → PAT-cont change 21.97 = 65.99 − 44.02. Less disc drag 1.03 → +20.94 = reported net
swing. The bridge is now internally consistent from two independent directions.

**Prior-loop defect CONFIRMED FIXED.** The earlier version double-counted the YoY favourability in depreciation
(+0.16) and finance cost (+1.07) as standalone rows on top of the +46.02 core PBT row — which already embeds
both, since core PBT ex-OI is struck after D&A and finance. Adding them produced 20.94 + 0.16 + 1.07 = 22.17,
the +22.17-vs-+20.94 discrepancy the first A5 pass caught. Those two rows are now removed and the footing note
(L202) states the non-double-count rule correctly. The bridge foots to +20.94 exactly.

No arithmetic mismatch above rounding anywhere in the review. ARITHMETIC = PASS.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear counter from the same extract)

**Positive claim 1 (L159, L205):** "100%+ of the +66.2% net-profit growth is core-driven, not treasury; core
operating PBT swung +Rs 46.02 Cr while Other Income fell — the healthiest possible composition."
- **Bear counter from extract:** The +46.02 core swing is partly non-margin timing. Cost of material fell
  187.37 vs 194.97 (−7.60) and employee cost 40.61 vs 44.35 (−3.74) on higher revenue — genuine. But Changes-in-WIP
  swung from +9.11 (expense) to (3.18) (credit), a ~Rs 12.3 Cr favourable inventory/timing item (L183), i.e.
  ~27% of the "core" swing is a WIP movement, not durable margin.
- **Survives?** NO. The item is still an operating (core, non-treasury) line, so it does not defeat the specific
  claim (core vs treasury). The dominant driver (~Rs 11.3 Cr absolute cost reduction on +Rs 22 Cr revenue) is
  real margin. Not grafted. Noted for completeness only.

**Positive claim 2 (L157, L179, L367):** "Operating EBITDA margin ex-OI reached 14.5%, clean — the first
genuinely clean post-BHEL quarter, margin story validated."
- **Bear counter from extract:** On a like-for-like clean basis the sequential trajectory is DOWN, not up:
  Q4FY26 core PBT ex-OI adjusted for the Rs 44.37 Cr ECL reversal was ~Rs 55.01 Cr (L178, L182) vs Q1FY27's
  Rs 36.94 Cr — a ~33% clean QoQ decline. "One clean print is not a trend."
- **Survives?** YES as a valid caution — but it is ALREADY incorporated (Step 3 diagnostics L182, Step 8B(i)/8C
  requiring a SECOND clean quarter before crediting durability). No new graft required.

**Positive claim 3 (L155, L243, L317):** "Revenue run-rate ~Rs 1,235 Cr annualised is at/near the FY28E Rs 1,265
Cr destination; operating result at or above base path."
- **Bear counter from extract:** Order backlog collapsed −41.4% YoY to Rs 1,545.4 Cr (L590-592), with the
  services-replacement pipeline undisclosed; a book only ~1.25x annualised revenue with the FGD engine
  terminated puts forward revenue at risk, so an annualised single-quarter run-rate overstates durability.
- **Survives?** YES as a valid caution — but ALREADY incorporated (flags, checklist #2/#6, Question 1, and A4
  explicitly frames the thesis as "a MARGIN story, not a revenue-growth story," L155). No new graft required.

**Additional cross-checks for un-incorporated survivors:** ETR-flattered PAT (~Rs 14.5 Cr/qtr un-taxed) —
already in Step 4, Q2, flags. Depreciation understated by the halted Durgapur charge — already flagged (L207).
Other-Income source undisclosed — already routed to Q6/Q7. Cash conversion INDETERMINATE — verdict correctly
capped at PROCEED WITH CAVEATS with the four missing-evidence items named (L214, L231, L369), per house rule.

**No surviving bear counter is absent from A4.** Every strong counter constructible from the extract is already
present. Nothing to loop back to A4.

---

## AUDIT 4 — PROTOCOL-VERDICT CHECK

- Verdict "PROCEED WITH CAVEATS" (L367) is within the allowed set and correctly NOT a clean PROCEED: cash
  conversion is INDETERMINATE (Q1 filing, no cash-flow/BS), and the house rule forbids INDETERMINATE resolving
  silently to PROCEED — cap at CAVEATS with named missing evidence is applied (L214, L369). Consistent.
- No thesis-broken trigger fired; two (#3 receivable days, #5 RPT) correctly marked untestable and pushed to
  H1 FY27, not silently passed (L273-279). Consistent.
- Decision Status WATCHLIST / Branch 8A-W with CMP Rs 907 above the Rs 500 re-entry ceiling → no action. Sound.
- Exit-PE / destination PE HELD pending H1 BS (no ROCE input at Q1) — no round-number default introduced; no
  Section 1B breach. Consistent with NEVER rules.

VERDICT-LOGIC = PASS.

---

## VERDICT

**COMPLETE.** All four audits pass. Deliverable brief complete (4/4 parts). Coverage: fresh enumeration ties to
the A2 ledger on every category with zero orphan rows and zero rows the ledger lacks; all material rows traced
into A4. Arithmetic: every derived metric re-computed from the raw extract matches within rounding, and the
prior-loop PAT-bridge defect is confirmed FIXED — the bridge now foots to +Rs 20.94 Cr from two independent
directions with the depreciation/finance double-count removed. Adversarial: the three strongest bear counters
constructible from the extract are already incorporated in A4; none survives un-grafted. No loop-back required.
Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "GVPIL"
quarter: "Q1FY27"
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
