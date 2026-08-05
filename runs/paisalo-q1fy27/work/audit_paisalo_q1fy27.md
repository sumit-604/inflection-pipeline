# A5 ADVERSARY / COMPLETENESS AUDIT — Paisalo Digital Ltd, Q1 FY27

Auditor: A5 (fresh context). Inputs seen: A4 review, two A1 extracts, two A2 ledgers.
Every number below re-derived independently from the A1 extracts (Rs Mn; Cr = Mn/10).
Board intimation carries no financial figures; all arithmetic is against the press release.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The PLAIN-LANGUAGE BRIEF exists (review line 340) with all four labelled parts present and carrying real content:

| Brief part | Present? | Location | Non-empty content check |
|---|---|---|---|
| (1) Summary narrative | PRESENT | review L342-350 | 4 paragraphs, numbers-first, 10-20 lines; states the QoQ dip, the untestable gates, and the WATCHLIST decision |
| (2) SECTOR intelligence | PRESENT | review L352-356 | NBFC/MSME cycle, co-lending model, RBI disclosure backdrop, disbursement-vs-book divergence risk |
| (3) BUSINESS-MODEL intelligence | PRESENT | review L358-362 | NII + fee/co-lending mechanics; three model-drift clues; bull vs bear read |
| (4) COMPETITION intelligence | PRESENT | review L364-368 | vs Muthoot/IIFL/UGRO/Satin/Aye/Northern Arc; asset-quality & capital strengths, RoE & C/I weaknesses |

**Gate result: PASS.** No placeholder text; all four are substantive.

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

Fresh grep passes run against both extracts and diffed against the A2 counts.

### Board intimation

| Category | A2 count | My fresh count | Method / note | Status |
|---|---|---|---|---|
| top_level_agenda_items | 3 | 3 | `^\s*[0-9]+\.\s+[A-Z]` = lines 38,43,48; line 72 is CC list, correctly excluded | MATCH |
| embedded_sub_disclosures | 3 | 3 | dividend L45 + director (i) L51 + director (ii) L53 | MATCH |
| annexure_table_rows | 5 | 5 | Sr No 1-5, L82-118 | MATCH |
| board_meeting_times | 2 | 2 | start 11:30 / end 12:25, L60 | MATCH |
| digital_signature_blocks | 2 | 2 | "Digitally signed by" = 2 (L64-66, L119-122) | MATCH |
| routing_recipients | 4 | 4 | BSE + NSE primary + Afrinex + India Intl Exch CC | MATCH |
| document_identifiers | 3 | 3 | equity scrip / 15 NCD / 5 CP | MATCH |
| **Total** | **22** | **22** | | **MATCH** |

### Press release

| Category | A2 count | My fresh count | Method / note | Status |
|---|---|---|---|---|
| kpi_table_metrics | 7 | 7 | AUM/Disb/TotInc/PAT/NIM/GNPA/NNPA, L120-126 | MATCH |
| headline_kpi_boxes | 4 | 4 | L84-89 (GNPA label = layout artifact, correctly not counted) | MATCH |
| ai_operating_metrics | 4 | 4 | 180k / 500k / 18 bots / 200k, L98-111 | MATCH |
| key_highlight_bullets | 16 | 16 | `^•` = 16 (L133-165) | MATCH |
| performance_chart_nums | 27 | 27 | 9 series x 3 periods, L172-226 | MATCH |
| zero_standing_items | 1 | 1 | Total Income QoQ dash, L122 | MATCH |
| signature_block_fields | 5 | 5 | L60-67 | MATCH |
| cover_letter_items | 11 | 11 | ledger §1.1-1.11 | MATCH |
| mgmt_quote/concall | 5 | 5 | ledger §7.1-7.5 | MATCH |
| boilerplate | 8 | 8 | ledger §9.1-9.8 | MATCH |
| absent_disclosures | 7 | 7 | Standalone/Consol/Segment/Limited-Review/Notes/C-to-I/Fee, all confirmed absent | MATCH |

**Orphan-row check (ledger row present but absent from A4):** none. A4's LEDGER-RECONCILIATION PREAMBLE (L28-35) claims 22/22 board rows and all press sections reviewed; I confirm every financially or governance-material row surfaces in A4 (KPI table → Step 1L; asset quality → Step 5L; borrowings → Step 5L; net worth/RoE/CAR → Steps 1L/5L; management quote / "new verticals" → FN3; DMD re-appointment → F13-b; dividend/AGM/book-closure → monitorables; the dashed Total-Income QoQ → FN1/Q11). Pure-boilerplate rows (scrip codes, CC recipients, disclaimer, contact block, AI operating counts, chart titles) are legitimately "reviewed, no finding" — none demands a forensic that A4 omitted.

**Missing-from-ledger check (my pass found, ledger lacks):** none. My independent counts equal the ledger's on every category.

**Coverage result: PASS.** No orphan rows (would loop to A3); no missed enumerations (would loop to A2).

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw Mn)

Raw (Rs Mn), press release: AUM 52,302/61,009/67,074; Disb 7,581/13,440/17,309; TotInc 2,187/2,609/2,603; PAT 472/722/613; NII Q1FY27 1,447; Net Worth 15,746/17,930/18,298; Borrowings 48,467.

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| AUM Cr (3 periods) | 5,230.2 / 6,100.9 / 6,707.4 | Mn/10 identical | L120 | MATCH |
| Disb Cr | 758.1 / 1,344.0 / 1,730.9 | identical | L121 | MATCH |
| Total Income Cr | 218.7 / 260.9 / 260.3 | identical | L122 | MATCH |
| PAT Cr | 47.2 / 72.2 / 61.3 | identical | L123 | MATCH |
| NII Q1FY27 Cr | 144.7 | 1,447/10 = 144.7 | L156 | MATCH |
| NII Q1FY26 (derived) | 124.7 | 1,447/1.16 = 1,247.4 Mn = 124.7 | L156 back-calc | MATCH |
| Net Worth Cr | 1,574.6 / 1,793.0 / 1,829.8 | identical | L165/219 | MATCH |
| Total Borrowings Cr | 4,846.7 | 48,467/10 | L150 | MATCH |
| AUM YoY | +28% | 67074/52302 = +28.2% | L120 | MATCH |
| Disbursement YoY | +128% | 17309/7581 = +128.3% | L121 | MATCH |
| Total Income YoY | +19% | 2603/2187 = +19.0% | L122 | MATCH |
| PAT YoY | +30% | 613/472 = +29.9% | L123 | MATCH |
| Net Worth YoY | +16.2% (flags stated +15%) | 18298/15746 = +16.2% | L165 | MATCH (A4 correctly flags source understatement, does not adopt it) |
| AUM QoQ | +10% | 67074/61009 = +9.9% | L120 | MATCH |
| Disbursement QoQ | +29% | 17309/13440 = +28.8% | L121 | MATCH |
| Total Income QoQ | −0.2% (dash in source) | 2603/2609 = −0.23% | L122 | MATCH |
| PAT QoQ | −15% | 613/722 = −15.1% | L123 | MATCH |
| GNPA YoY / QoQ | −14bps / −6bps | 0.70−0.84 / 0.70−0.76 | L125 | MATCH |
| NNPA YoY / QoQ | −19bps / −12bps | 0.49−0.68 / 0.49−0.61 | L126 | MATCH |
| RoA QoQ | −20bps | 3.6−3.8 | L202 | MATCH |
| Net Worth QoQ | +2.1% | 18298/17930 = +2.05% | L219 | MATCH |
| Residual "other income" Q1FY27 | 115.6 Cr; ~44% of income | 260.3−144.7 = 115.6; 115.6/260.3 = 44.4% | derived | MATCH |
| PAT bridge: NII change | +20.0 | 144.7−124.7 = +20.0 | L156 | MATCH |
| PAT bridge: reported PAT change | +14.1 | 61.3−47.2 = +14.1 | L123 | MATCH |
| PAT bridge: below-NII net drag | ~−5.9 | 20.0−14.1 = 5.9 | derived | MATCH |
| Annualised FY27 PAT | 245.2 Cr (at Base 244) | 61.3 x 4 = 245.2 | derived | MATCH |
| Q4 exit run-rate annualised | ~289 Cr | 72.2 x 4 = 288.8 | derived | MATCH |
| Q1 vs Q4 run-rate | ~−15% | 245.2/288.8 = −15.1% | derived | MATCH |
| Disbursement as % of AUM | ~26% | 1730.9/6707.4 = 25.8% | derived | MATCH |

**Source-inconsistency items — correctly handled by A4, NOT arithmetic errors:**
- NIM YoY: displayed 6.5%→6.6% implies +10bps; KPI table states "+4 Bps" (L124). A4 shows both and flags FN5. Correct treatment.
- NIM QoQ: 6.8%→6.6% implies −20bps; table states "(26 Bps)". A4 flags FN5. Correct.
- CoB YoY: chart 10.7%→10.1% implies −60bps; bullet L151 states "64 bps". A4 flags FN5. Correct.
- Net Worth: bullet L165 states "+15%", true value +16.2%. A4 uses the true value and flags. Correct.

These are source data-quality contradictions the release itself carries; A4 neither adopted the wrong figure nor estimated — it displayed the raw-derived value and routed the discrepancy to FN5. No house-rule violation, no arithmetic FAIL.

**Arithmetic result: PASS.** Zero mismatches above rounding.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims vs strongest same-text bear)

**Positive claim 1 (review L329): "PAT Rs61.3 Cr +30% YoY, annualised Rs245.2 Cr = at Notion Base FY27 (Rs244 Cr)."**
Strongest bear from the same extract: the annualised figure multiplies a quarter whose PAT fell 15% QoQ (722→613 Mn, L123) — i.e. it annualises a *declining* print and still only reaches Base, while the Q4 exit run-rate (289 Cr) has already been surrendered. Further, PAT +30% out-grew Total Income +19% (L122) and NII +16% (L156) with the driver sitting below the NII line entirely undisclosed (opex/provisions/tax/fees all ND), so the "at Base" comfort rests on an unexplained, possibly non-recurring item.
Survives? YES — but **already grafted** into A4 (QoQ softness cluster FN1 L134; earnings-quality INDETERMINATE Step 4 L153; Step 6A "flattered by nothing... should not be read as acceleration" L203). No new incorporation required.

**Positive claim 2 (review L329): "AUM +28% YoY (clears GREEN); disbursement +128% YoY."**
Strongest bear from the same extract: disbursement grew 4.6x faster than on-book AUM (+128% vs +28%); single-quarter disbursement Rs1,730.9 Cr is ~26% of the entire book, implying off-book co-lending origination or short-tenor churn not accreting to AUM — margin-dilutive and consistent with NIM staying flat despite CoB −64bps. The +128% also laps a seasonally low Q1FY26 base (7,581 Mn), so the headline overstates momentum; QoQ +29% is the fairer read.
Survives? YES — but **already grafted** (FN4 L116, L178, L288; Step 5L divergence). No new incorporation required.

**Positive claim 3 (review L329): "GNPA 0.70% / NNPA 0.49% improving; CAR 33.1% very strong."**
Strongest bear from the same extract: PCR, write-offs and credit cost are all ND (Step 5L L164-167), so improving GNPA is unverifiable — a written-off book flatters GNPA. And CAR 33.1% / Tier-1 26.8% sitting atop only 13.4% RoE (L160) is an over-capitalised, under-leveraged balance sheet: capital "strength" here partly reflects capital not earning its return, not a deployable edge.
Survives? YES — but **substantially grafted**: the write-off/PCR caveat is in Step 5L and Q7 (L290); the low-RoE-limits-capital-quality point is in Pillar 1 (L250, "ROE 13.4% is below the level that would earn a rich P/B") and the Competition brief (L366-368). No new incorporation required.

**Adversarial result: PASS.** All three strongest bear counters are supported by the extract and already present in A4. No surviving un-incorporated counter to loop back to A4.

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four brief parts present, substantive).
- Coverage: PASS (22/22 board rows, all press sections; no orphans, no missed enumerations — my fresh grep counts equal A2's on every category).
- Arithmetic: PASS (every YoY/QoQ/bps/PAT-bridge/annualisation figure re-derived; zero mismatches above rounding; the four source data-quality contradictions were correctly flagged, not adopted or estimated).
- Adversarial: PASS (three strongest same-text bear counters all already incorporated).

No loop-back required. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "PAISALO"
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
