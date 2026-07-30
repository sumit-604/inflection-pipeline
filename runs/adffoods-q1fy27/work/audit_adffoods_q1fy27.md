# A5 ADVERSARY / COMPLETENESS AUDIT — ADF Foods Limited (ADFFOODS) — Q1 FY27

Independent re-derivation from A1 extracts and A2 ledgers only. Units: results filing Lakhs (x0.01 to Cr); press release / presentation already Rs Cr. Every line reference is my own re-check, not a deference to A4's or A3's cites.

Run-limitation facts accounted for (judged, not counted as my own gaps): no concall transcript (press release stands in as management-commentary source; A4 ran Role 5 in pre-positioning mode with Q&A / tone-vs-prior / credibility ratio marked ND-with-reason and master gate held OPEN — handled correctly); no prior-quarter ledger (deck-to-deck and entity-list verbatim diffs not runnable — A4 flagged this in the YAML, correct); Q1 Reg 33 filing carries no cash-flow statement (CFO / CFO-PAT ND, cash-conversion INDETERMINATE — handled correctly, see Cash-Conversion Check).

---

## 1. COVERAGE AUDIT

Fresh grep + manual sweep over each A1 extract, diffed against the A2 ledger COUNT TESTs.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results — numbered notes | 8 | 8 (L456,460,463,467,474,478,486,489) | none — all 8 tabled in Step 0D | PASS |
| Results — auditor paragraphs | 12 (4 S + 8 C) | 12 (S paras L90-119; C paras L157-282) | none — opinion + paras 6/7/8 in Step 0D + Q6 | PASS |
| Results — consolidation entities | 8 (7 table + 1 excluded) | 8 (L189-201 + Power Brands L277) | none — entity list + Ireland step-down covered (Q5) | PASS |
| Results — statement/segment line items | 76 (45 + 30 + 1 FX) | 76 (main 45 L322-431; segment 30 L512-545; Note-4 FX 1 L471) | none — all financial rows re-extracted into Step 1 tables | PASS |
| Results — signature blocks | 5 | 5 (L53-61,121-134,284-298,494-501,548-558) | administrative — covered by "all reviewed" preamble | PASS |
| Results — board-letter items | 6 | 6 (L15-71) | INTER_ALIA_UNDISCLOSED → Q14; rest reviewed-no-finding | PASS |
| Presentation — slides | 50 | 50 ([page 1]..[page 50]) | none | PASS |
| Presentation — quantified metrics | 285 | 285 (reconciled to ledger Table 2 running total; spot-verified slides 10/11/12/13/14/48/49) | material metrics (seg p14, dividend p49, 5yr p48, guidance p19) all surfaced | PASS |
| Presentation — footnotes | 5 | 5 (F1-F5, L123-148/1315-1317/1349) | reviewed | PASS |
| Presentation — director bios | 8 | 8 (slide 43 D1-D8) | reviewed-no-finding (DIN/term dates NOT FOUND, correct) | PASS |
| Presentation — admin facts | 6 | 6 (Table 1a) | reviewed-no-finding | PASS |
| Press release — disclosure units | 57 | 57 (11+3+4+10+7+14+2+5+1) | ZERO_STANDING 0-bps margin (4.3) → A3-01; all quote units mapped | PASS |

Missing-from-ledger (rows my fresh pass found that the ledger lacks): **none.** All fresh counts equal the A2 COUNT TESTs.

Orphan ledger rows (ledger rows with no A4 citation and no "reviewed, no finding"): **none.** Every flagged ledger row (ZERO_STANDING x9 results + x1 press, AUDITOR_RELIANCE, UNAUDITED_MGMT_FURNISHED, EXCLUDED_ENTITY, INTER_ALIA_UNDISCLOSED, AMBIGUOUS_CHART_MAPPING x2, AMBIGUOUS_DIRECTION, UNIT_CAUTION, QUALITATIVE_APPROX, NO_PRIOR_LEDGER) is either cited substantively or correctly disposed as reviewed-no-finding.

FORWARD-SIGNAL / AMBIGUOUS -> Question coverage: every finding ID A4 classifies as FWD or AMB at review line 358 maps to at least one Step 8.5 question row. Re-checked each: F2→Q5, F6→Q5/Q8, F13→Q5/Q14, F15→Q5/Q14, F1→Q12, F4→Q6, F7→Q8, F8→Q7, F12→Q4, F2-1→Q5, F6-1→Q2, F7-1→Q1/Q9, F12-1→Q4, F16-1→Q1, F16-2→Q2, F16-4→Q10, F16-6→Q1, F16-7→Q3, F16-10→Q5, F16-3→Q10, F16-5→Q11, F16-9→Q13, A3-01→Q3, A3-03→Q2, A3-04→Q1/Q8/Q9, A3-06→Q1, A3-02→Q5. **All discharged.**

Coverage observation (non-blocking, logged for A4 hygiene, not a FAIL): four IDs A4 declares "incorporated (all)" — A3-F3, F14-1, F16-8, A3-05 — appear ONLY in the roster (review L20 / YAML L560) and nowhere in the review body or question table. They are correctly outside A4's own FWD/AMB set (L358), so they require no question. A3's findings file is out of my context by design, so I cannot confirm their type; A4 should mark them explicitly "reviewed, no separate finding" rather than leave them roster-only. Does not rise to an orphan-row FAIL.

---

## 2. ARITHMETIC AUDIT

Recomputed from raw Lakhs (results) / raw Rs Cr (press, deck). Standalone and consolidated, every period. Full sweep performed; only cells with any deviation or load-bearing status shown.

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Standalone Q1FY26 PBT (OCR trap) | 22.85 (flagged L340 misreads 2,784.58; true 2,284.58) | 2,284.58 L → 22.85 (PBT−tax check: 2,284.58−585.39=1,699.19=PAT L363) | L338/L340/L342/L359 | PASS — A4 caught and corrected the OCR error correctly |
| Consol Op EBITDA ex-OI Q1FY27 (PBT+D+FC−OI) | 29.65 | 23.49+6.57+0.69−1.10 = 29.65 | L338/335/334/324 | PASS |
| Consol Op EBITDA ex-OI Q1FY26 | 23.53 | 21.11+4.89+0.58−3.05 = 23.53 | L338/335/334/324 | PASS |
| Consol Op EBITDA margin Q1FY27 / Q1FY26 | 17.72% / 17.71% (+1 bps) | 29.65/167.29=17.72%; 23.53/132.88=17.71% | L323 | PASS |
| Consol revenue YoY | +25.9% | (167.29−132.88)/132.88 = 25.9% | L323 | PASS |
| Consol EBITDA YoY | +26.0% | (29.65−23.53)/23.53 = 26.0% | derived | PASS |
| Consol revenue QoQ | (15.0)% | (167.29−196.73)/196.73 = −15.0% | L323 | PASS |
| Consol effective tax rate Q1FY27 | 26.4% | 6.20/23.49 = 26.4% | L361/338 | PASS |
| Consol current-tax-only ETR Q1FY27 | 37.0% | 8.70/23.49 = 37.0% (869.62/2,348.71) | L342/338 | PASS |
| PAT bridge (consol YoY) | +6.12 / (1.68) / (1.95) / (0.11) / (0.34) = +2.05 | 6.12 / 1.68 / 1.95 / 0.11 / 0.34; ties to 17.29−15.24=+2.05 | L363 etc. | PASS |
| S−C PAT drag % (Q1FY26/Q4FY26/Q1FY27/FY26) | 10.28 / 13.89 / 5.44 / 7.47 | 174.71/1699.19; 417.83/3009.08; 99.37/1827.89; 726.02/9718.43 | L363-408 | PASS |
| Distribution seg margin Q1FY27 / Q1FY26 (~590 bps) | 11.5% / 17.4% | 266.52/2324.36=11.5%; 358.93/2066.33=17.4% | L513/520 | PASS |
| Distribution seg results YoY | (25.7)% | (266.52−358.93)/358.93 = −25.7% | L520 | PASS |
| Processed-foods Q1FY27 revenue (deck 165.0 flag) | 144.05 (filing wins; deck transposed w/ Q4 165.04) | 14,404.53 L → 144.05; Q4FY26 16,504.45 L → 165.04 | L514 | PASS — transposition catch correct |
| Non-MSKA revenue / PAT exposure | 50.5% rev / 11.17% PAT | 8,440.93/16,728.89=50.5%; (77.20+115.82)/1,728.52=11.17% | L227/266/323/363 | PASS |
| US tariff refund split | 3.12+7.29+9.28 = 19.69 | 3.12+7.29+9.28 = 19.69 (USD 2.08mn) | L479-481 | PASS |
| Q4FY26 consol deferred+earlier tax | (0.86) | Total−Current = 1,056.06−1,143.87 = −87.81 L → **(0.88)** | L361/342 | MINOR MISMATCH 0.02 Cr — A4 summed OCR component lines (13.63+72.18=85.81) instead of the authoritative Total−Current residual (87.81). Non-propagating: does not enter any ETR, YoY, or the PAT bridge (all Q1-based). Not verdict-changing. |
| Note-4 standalone FY26 FX gain | +14.26 | 1,425.41 L → 14.25 | L472 | MINOR 0.01 Cr rounding, immaterial |
| **Ex-Note-6-credit consol Op EBITDA YoY (A4 prose, Step 4 / verdict)** | **"roughly flat to modestly positive"** | **29.65−7.29 = 22.36 vs 23.53 = −1.17 Cr = −5.0% DECLINE** | L481 (7.29 credit) / derived | **FAIL — see Adversarial counter 1; the tariff credit (7.29) EXCEEDS the entire YoY EBITDA increase (+6.12), so underlying EBITDA declined, it is not flat-to-positive** |

Every load-bearing derived metric in A4's Step 1.3, Step 2, Step 3, Step 4 and Section C tables ties out to my independent recompute within rounding. Two immaterial residual/rounding blips noted for transparency. The one substantive arithmetic defect is the ex-credit EBITDA characterization, developed below.

---

## 3. ADVERSARIAL READ — three most positive A4 claims, strongest bear counter from the same extract

### Positive claim 1 (A4 Step 2.3 #3 / verdict #1, L162/L499): "core operating PBT ex-OI +24.0% and operating EBITDA +26.0% — the headline growth is REAL, not treasury-flattered."
Bear counter (same extract, Note 6 L481): the Rs 7.29 Cr tariff-refund credit to cost of materials is **larger than the entire YoY operating-EBITDA increase of +6.12 Cr**. Strip it and consolidated operating EBITDA is 29.65 − 7.29 = **22.36 vs 23.53 prior = −1.17 Cr, a ~5.0% YoY DECLINE**. Reported +26% EBITDA growth is therefore not "real operating growth diluted below the line" — it is entirely a Note-6 one-off, and the underlying operating line contracted YoY. The flat 0-bps consolidated margin corroborates the absence of true operating leverage.
**Counter SURVIVES.** A4 flags the tariff credit prominently and states reported PAT "would have declined YoY," but in Step 4 (L204) A4 characterizes ex-credit EBITDA as "roughly flat to modestly positive," which is arithmetically wrong and too generous. Because 7.29 > 6.12, the extract forces a decline. This must be grafted into A4 before save: the ex-credit consolidated operating EBITDA **declined ~5% YoY (22.36 vs 23.53)**, replacing "flat to modestly positive," and the "growth is REAL" framing must be qualified to "reported growth is a tariff-credit artefact; underlying operating EBITDA declined."

### Positive claim 2 (A4 Section C, L496): the overseas subsidiary PAT drag is "narrowing 10.28% -> 5.44% of standalone PAT — a genuine positive" (checklist 11 GREEN, tripwire 9 improving).
Bear counter (same extract, Note 6 L478 "the Company's wholly owned subsidiary received a refund"): the Rs 7.29 Cr credit and the broader Rs 19.69 Cr refund originate at a subsidiary and land in Q1FY27 profitability; the drag-% (S−C)/S narrows mechanically when a one-off boosts the period's PAT. The auditor's own para 7 still shows the unreviewed subs at a net loss of Rs (1.16) Cr this quarter — the cluster remains loss-making. So the single-quarter narrowing to 5.44% is at least partly a one-off tariff artefact, not evidence of structural subsidiary improvement.
**Counter PARTIALLY incorporated.** A4 already asks whether the narrowing is "structural or seasonal" (Q5) and notes the revenue gap WIDENED to 38.3%. But the specific mechanism — the Note-6 tariff one-off flattering the Q1FY27 drag reading — is not named in Section C's "genuine positive" line. Graft recommended: qualify the "genuine positive" with the Note-6 tariff flatter so the 5.44% is not read as clean structural narrowing. Secondary to counter 1.

### Positive claim 3 (A4 R5 Step 3, L426): "2.0 / 2 = 100% on hard milestones" (Surat commercial start + AEO-T3 delivered).
Bear counter (same extract): both are binary presence/absence items; Surat is only "initial container shipments" with no utilisation % and the prior Rs 40-50 Cr FY27 contribution guidance dropped, and the AEO-T3 working-capital benefit is unquantified. A 100% score on two soft-binary items is not a credibility signal.
**Counter does NOT survive as un-incorporated.** A4 explicitly states "on a base of only two binary items; NOT a credibility ratio," flags Surat as "nascent, needs a number," and holds the ramp trigger at ON TRACK (early). Fully surfaced.

---

## 4. CASH-CONVERSION / PROTOCOL-VERDICT CHECK (house rule)

CLAUDE.md: INDETERMINATE cash conversion may never silently resolve to PROCEED; it caps the verdict at PROCEED WITH CAVEATS with the missing evidence named. A4 marked CFO / CFO-PAT as ND (Q1 Reg 33 files no cash-flow statement), declared cash conversion INDETERMINATE, named the missing evidence (H1 FY27 cash-flow at Q2 as the next Pillar-2 reading), and stated the PROCEED-WITH-CAVEATS cap explicitly (L227, L519). The assigned verdict PROCEED WITH FLAGS sits at or above that severity floor (flags > caveats in the PROCEED/CAVEATS/FLAGS/REWORK/INSUFFICIENT ordering) and is not a silent PROCEED. **Cash-conversion handling is correct.** No pillar was re-set on Q1 data; entry/MoS held pending the August master gate — consistent with the no-round-number / master-gate rules.

---

## 5. VERDICT

**INCOMPLETE.** Loop back to **A4.**

Gap: A4's ex-Note-6-credit reading of underlying consolidated operating EBITDA — stated as "roughly flat to modestly positive" (Step 4, L204) — is arithmetically a **~5.0% YoY DECLINE** (29.65 − 7.29 = 22.36 vs Q1FY26 23.53 = −1.17 Cr), because the Rs 7.29 Cr tariff credit (Note 6, L481) exceeds the entire +6.12 Cr YoY EBITDA increase. This is a surviving bear counter that A4 states too favourably and must be grafted before save: the reported +26% consolidated EBITDA growth is entirely a tariff-credit artefact and underlying operating EBITDA contracted YoY; the "growth is REAL" framing (L162/L499) must be qualified accordingly. Secondary graft: qualify the Section C "genuine positive" subsidiary-drag narrowing (10.28%->5.44%) with the same Note-6 tariff flatter, since the one-off lands in Q1FY27 PAT. All coverage, all other arithmetic, the FWD/AMB->question mapping, and the INDETERMINATE-cash-conversion handling PASS.

```yaml
stage: A5-adversary
company: "ADFFOODS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Ex-Note6-credit consolidated operating EBITDA YoY (Step 4 / verdict prose)", a4_value: "roughly flat to modestly positive", recomputed: "-5.0% YoY decline (29.65-7.29=22.36 vs 23.53=-1.17 Cr)", source_line: "review L204/L499; extract L481 (7.29 credit), L338/335/334/324/323"}
  - {metric: "Q4FY26 consolidated deferred+earlier tax (Step 1.2 display cell, non-propagating)", a4_value: "(0.86)", recomputed: "(0.88) via Total-Current = 1056.06-1143.87 = -87.81 L", source_line: "extract L361/L342"}
surviving_bear_counters:
  - {claim: "Consolidated operating EBITDA +26.0% and core PBT ex-OI +24.0% — headline growth is REAL, not treasury-flattered", counter: "Rs 7.29 Cr Note-6 tariff credit (>+6.12 Cr total EBITDA increase); ex-credit consolidated operating EBITDA DECLINED ~5% YoY (22.36 vs 23.53). Reported growth is a one-off artefact; A4's 'roughly flat to modestly positive' is arithmetically a decline and must be corrected", source_line: "review L162/L204/L499; extract L481/L338/L323"}
  - {claim: "Overseas subsidiary PAT drag narrowing 10.28%->5.44% is a genuine positive (checklist 11 GREEN, tripwire 9 improving)", counter: "Note-6 refund originates at a WOS and lands in Q1FY27 PAT, mechanically flattering the (S-C)/S drag %; auditor para 7 still shows unreviewed subs at Rs (1.16) Cr net loss. Qualify the 5.44% as one-off-flattered, not clean structural narrowing", source_line: "review L496; extract L478/L266"}
loop_back_to: "A4"
gap: "A4 Step 4/verdict states ex-Note-6-credit underlying consolidated operating EBITDA as 'roughly flat to modestly positive'; it is a ~5.0% YoY DECLINE (29.65-7.29=22.36 vs 23.53) because the Rs 7.29 Cr tariff credit exceeds the entire +6.12 Cr YoY EBITDA increase. Graft the corrected read (reported +26% EBITDA is entirely a tariff-credit artefact; underlying operating EBITDA declined YoY) and qualify the 'growth is REAL' framing; secondarily qualify the Section C subsidiary-drag-narrowing 'genuine positive' with the same Note-6 one-off flatter."
```
