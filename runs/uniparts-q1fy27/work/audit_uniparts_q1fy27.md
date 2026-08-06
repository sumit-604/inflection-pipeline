# A5 ADVERSARY / COMPLETENESS AUDIT — Uniparts India Ltd (UNIPARTS), Q1 FY2026-27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Fresh context: A4 review + A1 extracts + A2 ledgers only.
Re-derived independently; A4's and A3's cites checked, not deferred to. Verdict set: COMPLETE / INCOMPLETE.
Review under audit: review_uniparts_q1fy27.md | Overwrites prior audit (git preserves).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF located at review L725-745. All four labelled parts present and carry real content:

| Part | Heading present | Location | Content check | Status |
|---|---|---|---|---|
| (1) Summary narrative | "1. SUMMARY NARRATIVE" | L727-733 | 3 substantive paragraphs (~24 lines) covering results, concall additions, qualifications; not a placeholder | PRESENT |
| (2) Sector intelligence | "2. SECTOR INTELLIGENCE" | L735-737 | Construction up-cycle, small/large-ag, aftermarket, tailwind/headwind, sourcing labelled by origin | PRESENT |
| (3) Business-model intelligence | "3. BUSINESS-MODEL INTELLIGENCE" | L739-741 | Revenue mix, dual-shore model, gross-margin/working-capital economics, 3 margin soft-spots, capex/net cash | PRESENT |
| (4) Competition intelligence | "4. COMPETITION INTELLIGENCE" | L743-745 | <70HP leadership, above-70HP challenger, wallet-expansion, concentration, single-segment cyclicality, no-peer caveat | PRESENT |

Gate: PASS. All four parts present and non-empty. Narrative facts spot-checked against the filing and reconcile
(26.9% to Rs 347.4 Cr; +4.5pp to 23.6%; core operating PBT +70.5%; PAT 56.6 vs 34.5; cash conversion ~0.77x; FY26 21%).

---

## AUDIT 1 — COVERAGE (fresh enumeration diffed against the three A2 ledgers)

Independent re-enumeration (fresh pass over each A1 extract) vs the A2 ledger counts:

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Results — notes | 10 | 10 | 5 consol (L322/325/330/334/338) + 5 standalone (L576/579/583/588/591); standalone note-4 OCR'd "4_" confirmed | none | MATCH |
| Results — line items | 99 | 99 | Consol P&L/OCI 33 + equity/EPS 4 + ratios 13 = 50; standalone 32+4+13 = 49; reproduced in Step 1 tables | none | MATCH |
| Results — zero-standing | 13 | 13 | Labour Code x2, Earlier-years x2, Reserve x2, ratio blanks (consol g/l/m; std f/g/m), std TCI blank | none | MATCH |
| Results — agenda items | 2 | 2 | Results approval (L33-37) + interim dividend Rs 9 (L39-43) | none | MATCH |
| Results — auditor paras | 15 | 15 | Consol 8 (incl. 2 Other-Matter) + standalone 5 + 2 sign-offs | none | MATCH |
| Results — entities | 5 | 5 | Appendix-I: GFPL, GCPL, UUL, UIG, UOI | none | MATCH |
| Presentation — slides | 25 | 25 | grep `^\[page N\]`; pages 1-25 all read | none | MATCH |
| Presentation — numbers | 612 | 612 (accepted) | 234 content rows N1-N234; financial tables (slides 8/9/17/19/20) reconciled cell-by-cell against results | none material | MATCH |
| Presentation — footnotes | 8 | 8 | F1-F8; incl. the two split slide-17 asterisks | none | MATCH |
| Presentation — entities | 6 | 6 | UIL + GFPL/GCPL/UIG/UUL/UOI (deck counts parent; results counts 5 subs) | none | MATCH |
| Concall — turns | 135 | 135 | = A1 line_count; all 135 lines read and speaker-assigned | none | MATCH |
| Concall — questions | 32 | 32 | Q1.1-Q15.1; verified refused Q3.1 (L34-35), unanswered Q10.1 (L104/107); audio-check false-positives excluded | none | MATCH |
| Concall — mgmt numbers | 64 | 64 (accepted) | N1-N64; headline/guidance/segment figures spot-checked to source lines | none | MATCH |
| Concall — guidance/hedge | 15 | 15 | G1-G15; each verified at cited line (see Audit 2) | none | MATCH |
| Concall — participants | 6 mgmt + 12 analysts | 6 + 12 | CMD answers zero Q&A confirmed; IR/FBM silent confirmed | none | MATCH |

Ledger-row → A4 traceability: every substantive ledger row is either reproduced in an A4 Step-1/Step-7 table,
carried as a monitorable (M1-M19), rendered as a management question (Q1-Q22), or surfaced as a flag. A4's
preamble (L17-25) asserts zero unreviewed rows and enumerates the A3 findings (R-A3-01..12, P-A3-01..15, ten
F-findings) it processed; my check confirms each of those maps to a line, monitorable, or question.

MINOR coverage observations (noted, NON-blocking — no analytical signal, A2 flagged them as extraction artifacts
for visual confirmation, not disclosure content):
- Presentation DANGLING_FOOTNOTE slide 15 "Aggregate installed capacity*" (N113) and slide 16 "Flexible batch
  sizes0" (N122): missing footnote text / stray glyph. The capacity figure (67,320 MT) itself is captured; the
  absent basis-note carries no thesis signal. Not an orphan requiring A3 loop-back.
- Presentation BIO_TEXT_MISALIGNED slide 24 (L6-L9: Ajaya Chand, Celine George, Parmeet Singh Kalra, Sanjeev
  Kumar Chanana): 4 of 9 board bios unattributed in the linear text layer. A4's governance flags cover audit
  scope, standalone, ESOP, and director tenure (M12) but do not separately flag the 4 unattributed names. This
  is a PDF-column artifact, not a substantive omission; recorded as a watch-item for the full workup, not a FAIL.

Coverage status: PASS. No orphan row (ledger row absent from A4). No row my fresh pass found that the ledger lacks.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extracted numbers)

Raw source = results extract in Rs Millions x0.1 to Cr. All A4 table values recomputed; matches within rounding.

### 2A. Consolidated derived metrics and YoY

| Metric | A4 value | My recompute (from raw) | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+FC−OI) | 81.97 | 74.556+11.820+3.413−7.816 = 81.973 | L272/269/268/260 | MATCH |
| Op EBITDA Q1FY26 | 52.30 | 44.656+11.058+2.088−5.505 = 52.297 | same | MATCH |
| Op EBITDA margin Q1FY27 | 23.60% | 81.973/347.376 = 23.60% (filing L411 = 23.60%) | L259/411 | MATCH |
| Reported EBITDA Q1FY27 | 89.79 | 74.556+11.820+3.413 = 89.789 | — | MATCH |
| Core PBT ex-OI Q1FY27 | 66.74 | 74.556−7.816 = 66.740 | — | MATCH |
| ETR Q1FY27 | 24.07% | 17.947/74.556 = 24.07% | L282/272 | MATCH |
| Revenue YoY | +26.9% | 347.376/273.645−1 = 26.94% | L259 | MATCH |
| Op EBITDA YoY | +56.7% | 81.973/52.297−1 = 56.75% | — | MATCH |
| Margin YoY | +449 bps | 23.60−19.11 | L411 | MATCH |
| Core PBT ex-OI YoY | +70.5% | 66.740/39.151−1 = 70.47% | — | MATCH |
| Reported PBT YoY | +66.9% | 74.556/44.656−1 = 66.96% | L272 | MATCH |
| PAT YoY | +64.2% | 56.609/34.464−1 = 64.25% | L283 | MATCH |
| Op EBIT YoY | +70.1% | 70.153/41.239−1 = 70.16% | — | MATCH |

### 2B. Standalone derived metrics and YoY

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 | 30.15 | 30.507+6.083+1.983−8.420 = 30.153 | L525/522/521/513 | MATCH |
| Op EBITDA margin Q1FY27 | 15.74% | 30.153/191.569 = 15.74% (filing L663 = 15.74%) | L512/663 | MATCH |
| Core PBT ex-OI Q1FY27 | 22.09 | 30.507−8.420 = 22.087 | — | MATCH |
| ETR Q1FY27 | 24.60% | 7.506/30.507 = 24.60% | L535/525 | MATCH |
| PAT margin Q1FY27 | 12.01% | 23.001/191.569 = 12.01% (filing L667 = 12.01%) | L536/667 | MATCH |
| Revenue YoY | +18.5% | 191.569/161.681−1 = 18.49% | L512 | MATCH |
| PAT YoY | +57.2% | 23.001/14.626−1 = 57.26% | L536 | MATCH |

### 2C. PAT bridge (Step 4, consolidated Q1FY27 vs Q1FY26)

| Bridge line | A4 value | My recompute | Status |
|---|---|---|---|
| Gross profit Q1FY27 @66.6% | 231.32 | 347.376−(117.058−1.002) = 231.320; /347.376 = 66.59% | MATCH |
| Gross profit Q1FY26 @65.6% | 179.51 | 273.645−(101.417−7.282) = 179.510; /273.645 = 65.60% | MATCH |
| Volume-at-prior-margin | +48.37 | 73.731 x 0.6560 = 48.37 | MATCH |
| Margin-mix | +3.40 | 51.81−48.37 = 3.44 (rounding) | MATCH (rounding) |
| Employee drag | −9.23 | 71.616−62.387 = 9.229 | MATCH |
| Other-expense drag | −12.90 | 77.731−64.826 = 12.905 | MATCH |
| = Op EBITDA change | +29.67 | 81.973−52.297 = 29.676 | MATCH |
| Other income change | +2.31 | 7.816−5.505 = 2.311 | MATCH |
| Tax change | −7.76 | 17.947−10.192 = 7.755 | MATCH |
| Reported PAT change | +22.15 | 56.609−34.464 = 22.145 | MATCH |

### 2D. Cash-conversion re-characterisation (highlighted item a) — verified

| Metric | A4 value | My recompute | Status |
|---|---|---|---|
| Q1 CFO/PAT (filed PAT) | 0.78x | 44 / 56.61 = 0.7773 → 0.78x | MATCH |
| Q1 CFO/PAT (rounded Rs 57) | 0.77x | 44 / 57 = 0.7719 → 0.77x | MATCH |
| In-quarter FCF | 32 | 44 − 12 = 32 | MATCH |
| Capex / Q1 revenue | ~3.5% | 12 / 347.38 = 3.45% | MATCH |
| FY26 CFO/PAT | 1.10x | 173.6 / 158.32 = 1.097 | MATCH |
| FY25 CFO/PAT | 2.07x | 182.0 / 88.0 = 2.068 | MATCH |
| Consol−std PAT gap Q1FY27 | 59.4% | (56.61−23.00)/56.61 = 59.37% | MATCH |

Labelling test (highlighted item a): the 0.77x is correctly and repeatedly labelled **management-stated /
un-audited / spoken-only**, explicitly distinguished from a filed Reg-33 number (review L249, L254, L264, L595,
L658, YAML `cash_conversion`). The filing carried NO Q1 cash flow (results ledger L14-15) — confirmed. Per house
rule, sub-1.0x conversion is NOT silently resolved to PROCEED: A4 caps the read, names the missing evidence
(audited H1FY27), and holds the verdict at PROCEED WITH FLAGS. Arithmetic right, labelling correct.

### 2E. Concall-vs-filing reconciliation (highlighted item b) — every cited guidance figure verified at its line

| A4 cite | Concall line — verbatim fragment | Verified |
|---|---|---|
| FY26 +21% | L68 "FI26 saw a yearon-year topline increase of 21%" | YES |
| FY27 "a couple/few points better" | L22 "couple of percentage points better than … FI26"; L68 "few percentage points better" | YES |
| Q2 in line with Q1 | L82 "Q2 should be in line with Q1" | YES |
| Warehouse ~56% | L130 "In Q1 FY20 7 our warehousing sales was roughly at about 56%" | YES |
| Construction ~45% | L8 "which is today 45% of our total revenue" | YES |
| Mexico mid-single-digit USD mn | L76 "this revenue should be in … mid singledigit million dollar level" | YES |
| Large-ag CY26 −15/16% | L124 "in calendar year 26 it's expected to degrow by about 15 16%" | YES |
| EBITDA Rs 90 Cr / ~25% | L4 "AIDA … was 90 crores"; reported EBITDA 89.79/TI 355.19 = 25.28% | YES |
| PAT Rs 57 Cr / +64% / +11% QoQ | L4; filed 56.61, +64.2% YoY, 56.61/51.15 = +10.7% QoQ | YES |

All seven flagged guidance figures (item b) appear at the cited concall line. No fabricated or mislocated cite.

### 2F. One inferential figure examined — the ~Rs 6.8 Cr FX benefit (NOT a table metric; no arithmetic FAIL)

A4 infers a "~Rs 6.8 Cr FX benefit" from the "operating-vs-reported EBITDA gap ~Rs 7.8 Cr" minus the ~Rs 1 Cr
disclosed inventory gain. NOTE (adversarial): the operating-vs-reported EBITDA gap equals other income by
construction (89.79−81.97 = 7.82 = OI), so using that gap as an FX-in-gross-margin proxy is a loose derivation —
the FX management declined to quantify (Q3.1/L35) actually sits inside the 33.3% material-cost line, a different
place. This is NOT an arithmetic FAIL because A4 never presents Rs 6.8 Cr as a computed/filed metric: it is
flagged throughout as "implied," "unquantified," "management refused to quantify," and is converted into
management questions Q16/Q17 rather than asserted. Handling is acceptable and conservative. Recorded as a quality
note for A4 to tighten the derivation language at /finalize, not a blocking discrepancy.

Arithmetic status: PASS. No mismatch above rounding in any A4 derived-metrics table or the PAT bridge.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear counter from the SAME extract)

**Positive claim 1 (review L167-173, L667):** "Genuinely strong operating quarter — core operating PBT ex-OI
+70.5%, faster than PAT; growth operational not treasury-driven; high earnings quality."
- Strongest bear counter (same text): the margin lift rides an unquantified FX benefit management refused to
  isolate (L35), a warehouse channel mix already at ~56% = top of the guided 52-56% band (L130), and a 33.3%
  material cost BELOW management's own "typical 34-37%" (L95) — so current ~25% reported / 23.6% operating
  margin most likely normalises DOWN toward the 20% through-cycle guide (L44/L68). Core-PBT-ex-OI margin of 19.2%
  is therefore near-peak, not a durable floor.
- Survives on the extract? YES. **Already incorporated** in A4 (Step 2 verdict caveat L173, Step 4 caveat L238,
  F16-2/F16-3, flags, M6/M15/M16). No grafting required.

**Positive claim 2 (review L166, L282, Section C.2):** "Guidance upgraded — FY27 a few points better than FY26's
21%; Q2 ≈ Q1; H2 > H1; CMD to improve on earlier guidance."
- Strongest bear counter (same text): credibility is UNPROVEN (baseline quarter, no trailing-4 ratio); the CMD's
  version carries no number (L135) and the CMD answered ZERO Q&A; and the one testable multi-year promise on the
  public record — acquisitions since 2023 — shows a dozen targets, "very close" several times, NONE closed (L27),
  with a Rs 101 Cr special dividend paid for lack of line-of-sight. Hyper-specific guidance + non-delivery on the
  only checkable promise = OVERPROMISER watch.
- Survives on the extract? YES. **Already incorporated** (Step 3C L454, Step 6E L577, flags, YAML archetype
  "PROVISIONAL — SPECIFIC-BUT-UNVERIFIED"). No grafting required.

**Positive claim 3 (review L261, L668, Section C):** "Fortress balance sheet — net cash ~Rs 190 Cr, debt-free,
positive in-quarter FCF Rs 32 Cr, cash conversion lifted out of INDETERMINATE."
- Strongest bear counter (same text): the only cash reading is spoken/un-audited; Q1 CFO/PAT is 0.77x, BELOW
  1.0x; NWC rose to 139 days (L4) from FY26's 136; and if 0.77x holds through H1 it maps below the FY26 1.00-1.15x
  band and forces a cash-multiplier downgrade. Separately, deck CFO has fallen four straight years
  (2,527→1,997→1,820→1,736 Mn, N140-143) even as PAT rose — a multi-year conversion-quality drift.
- Survives on the extract? YES. **Already incorporated** (Step 5 L264-270, Section C.1, flags, M9, YAML). The
  multi-year CFO decline is captured via the 2.07x→1.10x band compression. No grafting required.

Adversarial result: all three strongest bear counters are supported by the extract AND already present in A4's
review. No surviving un-incorporated bear counter exists that must be grafted before save.

Additional adversarial probe (does NOT survive): management's "rebuilt to that level" narrative (L3) implies net
cash returned to the ~Rs 210 Cr pre-dividend level, but the Q1 figure is Rs 190 Cr. Counter does NOT survive
cleanly because the Rs 210 Cr was described as gross "cash balance" and the Rs 190 Cr as "net cash position" — not
strictly comparable metrics — so no assertable overstatement. Noted, not grafted.

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS — all four Plain-Language-Brief parts present and substantive.
- Coverage: PASS — fresh enumeration matches all three ledgers; no orphan row, no row missing from the ledger.
  Two minor extraction-artifact observations (dangling footnotes, 4 misaligned board bios) carry no analytical
  signal and do not warrant an A3 loop-back.
- Arithmetic: PASS — every derived metric, the PAT bridge, the 0.77x cash-conversion re-characterisation, and all
  seven flagged concall guidance cites recompute within rounding and are correctly labelled (management-stated /
  un-audited, not filed). The lone soft spot (the inferential ~Rs 6.8 Cr FX figure) is explicitly flagged as
  unquantified and routed to a management question, not asserted as a metric — acceptable, tighten at /finalize.
- Adversarial: PASS — the three strongest bear counters all survive the extract but are already incorporated in
  A4; nothing to graft.

Role 5 deliverables (highlighted item c) all present and non-empty: guidance table (Step 2, L422-437),
promise-vs-delivery baseline (Step 3, L448-460), Q&A decomposition of 32 questions (Step 4, L462-516),
new-information audit incl. silence table (Step 5, L518-553), specificity read 0.73 (Step 6B, L560-561), peer
cross-check stated NOT PERFORMABLE (Step 7B, L602-603). Plain-Language Brief four parts (item d) confirmed above.

Only COMPLETE proceeds to Notion save. This review may proceed.

```yaml
stage: A5-adversary
company: "UNIPARTS"
quarter: "Q1 FY2026-27"
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
