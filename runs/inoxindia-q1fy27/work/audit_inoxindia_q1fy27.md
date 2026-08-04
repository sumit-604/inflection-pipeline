# A5 ADVERSARY / COMPLETENESS AUDIT — INOX India (INOXINDIA), Q1 FY27 — FINAL

Agent: A5 ADVERSARY. Final permitted verification (no further loop). Fresh context: audited only the A4 review, the two A1 extracts (results, Lakhs x0.01; presentation, Crores x1), and the two A2 ledgers. Every number below is re-derived from the raw extract lines; A4's and A3's cites are checked, not trusted. I did not assume any prior loop's fixes are correct — I recomputed each cell from raw lines.

This supersedes the prior loop-2 audit (which returned INCOMPLETE on Standalone FY26 Operating EBITDA). That cell now reads 335.27 / margin 21.53% in table 1D; my independent recompute confirms 335.27 / 21.53% is the correct value — the fix landed. All three audits (coverage, arithmetic, adversarial) completed in one pass.

---

## 1. COVERAGE AUDIT

Fresh grep/sweep pass over both extracts, diffed against the two A2 ledgers.

### 1a. Results ledger (`ledger_results_inoxindia_q1fy27.md`)

| Category | A2 count | My fresh count | Fresh-pass anchors | Orphan rows (ledger, absent from A4) | Status |
|---|---|---|---|---|---|
| Agenda items | 2 | 2 | lines 40, 43 | none | PASS |
| Auditor paras | 10 | 10 | cons 105/112/120/135/141/160 (I,2-6); SA 374/379/386/396 (I,2-4) | none (para 5 cons, para 4 SA, para 6 Other-Matter cited in A4 0D) | PASS |
| Entities | 3 | 3 | 136/137-138/139 (a/b/c); note 9 (339-340) | none (A4 0D note 9) | PASS |
| Notes | 19 | 19 | cons 274/277/278/287/291/307/324/336/339/342 (10); SA 494/497/499/507/511/526/542/554/557 (9) | none (A4 0D notes 1-10 both) | PASS |
| Line items | 78 | 78 | cons 215-271 (44); SA 446-489 (34) | none (A4 1A/1B reproduce every data-bearing row) | PASS |
| Zero-standing | 6 | 6 | cons 233/257/260/264; SA 463/474 | none (NCI → F-01 monitorable; Captive Consumption reconciled inside Total-Expenses line 234) | PASS |
| Signature blocks | 5 | 5 | 55-68 / 178-200 / 347-355 / 405-419 / 563-580 | none (Section B 0B) | PASS |
| Press release (supplementary) | 1 | 1 | 587-688 | none (Section B) | PASS |

Notes-count OCR trap independently reproduced: consolidated notes 1/2/3/9 carry corrupted markers (note 1 unmarked at 274; 2/3/9 render as bare commas at 277/278/339). A naive digit-grep returns 6 on the consolidated block; correct sweep is 10. A2's reconciliation is sound.

### 1b. Presentation ledger (`ledger_presentation_inoxindia_q1fy27.md`)

| Section | A2 count | My fresh count | Status |
|---|---|---|---|
| Cover-letter items | 11 | 11 | PASS |
| Highlight bullets | 5 | 5 | PASS |
| Narrative statements | 7 | 7 | PASS |
| Segment-mix claims | 4 | 4 | PASS |
| Divisional development claims | 13 | 13 | PASS |
| Strategic-development bullets | 3 | 3 | PASS |
| CEO-quote items | 6 | 6 | PASS |
| Consolidated-table line items | 3 | 3 | PASS |
| Forward-looking statements | 6 | 6 (2 wrap across 96/97 and 115/116) | PASS |
| About-company statements | 5 | 5 | PASS |
| Contact block | 1 | 1 | PASS |
| **Total** | **64** | **64** | **PASS** |

Sum: 11+5+7+4+13+3+6+3+6+5+1 = 64. Every disclosure unit is engaged in A4 Section B (claims inventory 12, segment/silence tables, forward-guidance table). Boilerplate about/contact rows are reviewed-no-finding.

Cosmetic note (not a coverage failure): A4 anchors press-release cites to the RESULTS-file line numbers (595, 606, 636, 650...) rather than presentation-file numbers (85, 100, 142...). Identical PR text in both files; A4 anchored to the results-embedded copy. No row lost.

**Coverage verdict: PASS. Orphan rows: none. Rows my fresh pass found but the ledger lacks: none.**

---

## 2. ARITHMETIC AUDIT

Every 1C (consolidated) and 1D (standalone) derived cell re-derived from raw lines, all four period columns. Op EBITDA / margin / Reported EBITDA / Core PBT ex-OI computed at Cr-level (A4's stated method, note line 153); ETR computed at Lakhs-level from lines 239/240/241/237 (cons) and 469/470/471/467 (SA).

### 2a. 1C CONSOLIDATED

| Cell | A4 | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY26 | 76.13 | 80.51+7.57+0.72−12.67 = 76.13 | 235/230/229/216 | PASS |
| Op EBITDA Q4FY26 | 94.65 | 96.71+9.02+3.51−14.59 = 94.65 | 235/230/229/216 | PASS |
| Op EBITDA Q1FY27 | 75.87 | 75.59+9.50+1.59−10.81 = 75.87 | 235/230/229/216 | PASS |
| Op EBITDA FY26 | 342.85 | 345.19+33.62+9.23−45.19 = 342.85 | 235/230/229/216 | PASS |
| Op EBITDA margin Q1FY26 | 22.42% | 76.13/339.62 = 22.42% | +215 | PASS |
| Op EBITDA margin Q4FY26 | 20.55% | 94.65/460.65 = 20.55% | +215 | PASS |
| Op EBITDA margin Q1FY27 | 20.46% | 75.87/370.79 = 20.46% | +215 | PASS |
| Op EBITDA margin FY26 | 21.60% | 342.85/1587.06 = 21.60% | +215 | PASS |
| Core PBT ex-OI Q1FY26 | 67.84 | 80.51−12.67 = 67.84 | 235/216 | PASS |
| Core PBT ex-OI Q4FY26 | 82.12 | 96.71−14.59 = 82.12 | 235/216 | PASS |
| Core PBT ex-OI Q1FY27 | 64.78 | 75.59−10.81 = 64.78 | 235/216 | PASS |
| Core PBT ex-OI FY26 | 300.00 | 345.19−45.19 = 300.00 (lakhs 34518.59−4518.92 = 29999.67) | 235/216 | PASS |
| ETR Q1FY26 | 24.09% | 1939.43/8051.22 = 24.09% | 239/240/241/237 | PASS |
| ETR Q4FY26 | 24.70% | 2468.41/9992.12 = 24.70% | 239/240/241/237 | PASS |
| ETR Q1FY27 | 23.17% | 1751.36/7558.56 = 23.17% | 239/240/241/237 | PASS |
| ETR FY26 | 24.57% | 8401.84/34190.68 = 24.57% | 239/240/241/237 | PASS |

Also checked (cons): Reported EBITDA 88.80/109.24/86.68/388.04 PASS; PAT margin 18.00/16.33/15.66/16.25% PASS; Other-Income/PBT 15.74/14.60/14.30/13.22% PASS.

### 2b. 1D STANDALONE

| Cell | A4 | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY26 | 75.30 | 79.95+7.19+0.63−12.47 = 75.30 | 465/460/459/449 | PASS |
| Op EBITDA Q4FY26 | 94.33 | 96.55+7.93+3.26−13.41 = 94.33 | 465/460/459/449 | PASS |
| Op EBITDA Q1FY27 | 71.55 | 73.09+8.17+1.42−11.13 = 71.55 | 465/460/459/449 | PASS |
| **Op EBITDA FY26** | **335.27** | **340.21+30.75+8.75−44.44 = 335.27** | 465/460/459/449 | **PASS (prior-loop fix confirmed)** |
| Op EBITDA margin Q1FY26 | 23.00% | 75.30/327.39 = 23.00% | +446 | PASS |
| Op EBITDA margin Q4FY26 | 20.71% | 94.33/455.46 = 20.71% | +446 | PASS |
| Op EBITDA margin Q1FY27 | 20.04% | 71.55/357.00 = 20.04% | +446 | PASS |
| **Op EBITDA margin FY26** | **21.53%** | **335.27/1557.27 = 21.53%** | +446 | **PASS (fix confirmed)** |
| Core PBT ex-OI Q1FY26 | 67.48 | 79.95−12.47 = 67.48 | 465/449 | PASS |
| Core PBT ex-OI Q4FY26 | 83.14 | 96.55−13.41 = 83.14 | 465/449 | PASS |
| Core PBT ex-OI Q1FY27 | 61.96 | 73.09−11.13 = 61.96 | 465/449 | PASS |
| Core PBT ex-OI FY26 | 295.77 | 340.21−44.44 = 295.77 | 465/449 | PASS |
| ETR Q1FY26 | 24.46% | (1930.00+25.53)/7995.05 = 24.46% | 469/470/471/467 | PASS |
| ETR Q4FY26 | 25.53% | (2521.00+26.81−0.57)/9975.68 = 25.53% | 469/470/471/467 | PASS |
| ETR Q1FY27 | 22.88% | (1710.00+32.51−70.46)/7308.87 = 22.88% | 469/470/471/467 | PASS |
| ETR FY26 | 25.09% | (8365.00+89.48−0.57)/33693.13 = 25.09% | 469/470/471/467 | PASS |

Also checked (SA): Reported EBITDA 87.77/107.74/82.68/379.71 PASS; PAT margin 18.45/16.31/15.79/16.21% PASS.

**All named confirmations verified:** SA FY26 Op EBITDA 335.27 (margin 21.53%) ✓; ETR cons Q4FY26 24.70%, SA Q1FY26 24.46%, SA Q4FY26 25.53%, SA Q1FY27 22.88%, SA FY26 25.09% ✓; SA Op EBITDA Q4FY26 94.33 ✓; cons Core PBT ex-OI FY26 300.00 ✓. The prior loop's failing cell (SA FY26 Op EBITDA / margin) is now correct.

### 2c. Headline / bridge / gap numbers

| Metric | A4 | Recomputed | Status |
|---|---|---|---|
| Cons revenue YoY | +9.18% | 31.17/339.62 | PASS |
| Cons Op EBITDA YoY | −0.34% | −0.26/76.13 | PASS |
| Cons core PBT ex-OI YoY | −4.51% | −3.06/67.84 | PASS |
| Cons PAT YoY | −4.99% | −3.05/61.12 | PASS |
| SA revenue YoY | +9.04% | 29.61/327.39 | PASS |
| SA core PBT ex-OI YoY | −8.18% | −5.52/67.48 | PASS |
| SA PAT YoY | −6.67% | −4.03/60.40 | PASS |
| PAT bridge close | −3.05 | +21.84 −8.37 −13.72 −1.93 −0.87 −1.86 +1.88 = −3.05 | PASS |
| GP margin YoY | 60.32%→61.14% (+82bps) | 204.86/339.62 → 226.70/370.79 | PASS |
| S-vs-C PAT gap Q1FY27 | 1.70 Cr / 2.93% | 58.07−56.37 = 1.70; 1.70/58.07 | PASS |
| S-vs-C PAT gap Q4FY26 | 0.95 Cr / 1.26% | lakhs 7523.71−7428.44 = 95.27 | PASS |
| Subsidiary PAT +136% YoY | +136% | (170.38−72.27)/72.27 lakhs = +135.8% | PASS |
| Cons NW below SA | 21.07 Cr | lakhs 112052.40−109945.58 = 2106.82 | PASS |
| Brazil sub (para 6) | 1.64 Cr PAT / 13.32 Cr rev | 164.19 / 1332.00 lakh | PASS |
| Brazil % of cons PAT | 2.83% | 164.19/5807.20 | PASS |
| OCI actuarial gain Q1 | 2.11 Cr | line 247: 211.42 lakh | PASS |
| PR EBITDA vs statement | ~3.3 Cr gap | 90 − 86.68 = 3.32 | PASS |
| PR "+8.3%" base | Total Income | 381.60/352.29 = +8.32% (not Rev-from-Ops +9.18%) | PASS |
| PR "PAT Rs 61" = TCI | TCI 60.54, not PAT 58.07 | line 253 6054.12 / line 242 5807.20 | PASS |

**Minor imprecision (non-blocking):** Cons Finance-cost YoY stated +120.2% (Step 2A/Step 4). Precise recompute is +119.67% (lakhs 159.15/72.45) or +120.83% (Cr 1.59/0.72); A4's figure sits between and matches neither exactly. Denominator is Rs 0.72 Cr (A4 flags "small base"); not a 1C/1D derived cell; directionally identical (~+120%). SA Finance YoY +125.1% matches lakhs-precise (+125.13%). Recorded for transparency; changes no margin, PAT, ETR, verdict, or flag. Not a FAIL.

**Arithmetic verdict: PASS. No mismatch above rounding on any headline number or any 1C/1D derived cell. Prior-loop SA FY26 Op EBITDA error is resolved.**

---

## 3. ADVERSARIAL READ

Three most positive claims in A4's review, each with the strongest bear counter built from the SAME extracted text, and whether the counter survives (must be grafted into A4).

**Positive claim 1 — Record order book Rs 1,686 Cr / export book Rs 1,140 Cr = "strong revenue visibility" (GREEN watchlist #2; 6D ON TRACK).**
Bear counter (same text): the Rs 1,686 Cr book is undefined and unverifiable — no opening balance, no roll-forward, not in any Reg 33 statement line (PR lines 89/599; F16.2). Despite a "record" book and "highest-ever" inflow, delivered revenue grew only +9.18% YoY (215) with Op-margin −196 bps — the book is not converting into profitable growth.
Survives as a counter, but ALREADY incorporated in A4 (Step 3, 6D "margin-qualified," Q10, EBITDA-margin FLAG). No graft.

**Positive claim 2 — Gross profit +21.84 Cr, GP margin +82 bps YoY (60.32%→61.14%), "Recurring" (Step 4 bridge).**
Bear counter (same text): the gross gain is fully consumed below the gross line — Employee +24.7% (228) and Other Expenses +14.5% (231) erase GP +21.84, pushing Op EBITDA to −0.26 Cr and Op margin −196 bps; D&A +25.5% and finance +120% compound it. GP "expansion" is masked by structural operating deleverage.
Survives, but ALREADY incorporated (Step 2C diag 2/5, the bridge, 6D margin trigger WEAKENED, flags). No graft.

**Positive claim 3 — Subsidiary (Brazil) PAT +136% YoY; offshore scale-up "ON TRACK / strengthening" (6D; Section C).**
Bear counter (same text): the entire offshore delta comes from ONE subsidiary (revenue Rs 13.32 Cr, PAT Rs 1.64 Cr) FURNISHED BY MANAGEMENT and NOT independently reviewed by the principal auditor (para 6, L160-174; MGMT_FURNISHED) — low assurance. Meanwhile consolidated Other Equity is Rs 21.07 Cr BELOW standalone (271/489) — cumulative overseas equity erosion. A +136% read off a Rs 0.72→1.70 Cr base is small, low-assurance, and sits atop an eroded equity base.
Survives, but ALREADY incorporated (6D assurance caveat, Section C S-vs-C block, Q5, monitorables). No graft.

**Adversarial verdict: all three strongest bear counters are already present in A4. No surviving un-incorporated counter. Nothing to graft.**

---

## VERDICT

**COMPLETE.**

- Coverage: PASS — 78 results line items + 19 notes + 10 auditor paras + 3 entities + 2 agenda + 5 signatures + 1 PR, and 64 presentation rows, all independently re-counted and all reviewed in A4. No orphan row; nothing missing from either ledger.
- Arithmetic: PASS — every 1C/1D derived cell (Op EBITDA, margin, Core PBT ex-OI, ETR) across all four period columns, plus every headline/bridge/gap number, re-derived from raw lines with zero mismatch above rounding. The prior-loop SA FY26 Op EBITDA/margin error is confirmed fixed (335.27 / 21.53%). One immaterial small-base finance-YoY imprecision noted, non-blocking. Step 6D independently confirmed to carry the Brazil management-furnished / non-independently-reviewed assurance caveat (auditor para 6, L160-174, F-04).
- Adversarial: PASS — the three strongest bear counters are already incorporated in A4.

No loop-back to A2, A3, or A4. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "INOXINDIA"
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
