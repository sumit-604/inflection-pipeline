# A5 ADVERSARY — RE-AUDIT (loop 1 of 2) — LAXMIINDIA Q1 FY27

Independent re-audit of the re-saved A4 merged review. Fresh context; re-derived
from A1 extracts and A2 ledgers. No deference to A3/A4 cites.

---

## PRIMARY-FIX VERIFICATION (the single prior-loop FAIL)

Prior INCOMPLETE: Step 3 QoQ table, derived "Q2+Q3 FY26" PPOP cell read 40.00,
should be 36.00.

- **Re-grep for `40.00` across the review:** ZERO hits (Grep, whole file). The
  stale value is gone.
- **PPOP cell now reads 36.00** (review L153). Independent recompute from raw
  Slide-16 anchors (pres L517): FY26 PPOP 80.10 − Q1FY26 14.48 − Q4FY26 29.62 =
  **36.00**. MATCH.
- **Sibling derived cells on the same row re-derived independently:**
  - NII 75.81 = 161.78 − 33.86 − 52.11 = 75.81 (pres L507). MATCH.
  - PBT 26.21 = 66.05 − 12.76 − 27.08 = 26.21 (pres L525). MATCH.
  - PAT 19.45 = 49.68 − 9.65 − 20.58 = 19.45 (pres L529). MATCH.
- **No cell moved except the target; no downstream dependency touched.** The row's
  only derived downstream is the "avg ~37.9 NII/qtr" run-rate label (75.81/2 =
  37.905 ≈ 37.9), which is NII-based and does NOT touch PPOP. L160's "~24%" claim
  = 47.06/37.9 = +24.2%, still holds. No total or average anywhere sums the PPOP
  36.00 cell. Fix is isolated and introduced no new inconsistency.

Fix CONFIRMED. Proceeding to full re-audit (not a rubber-stamp).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF present (review L346-366), all four labelled parts non-empty:

| Part | Heading | Line | Status |
|---|---|---|---|
| 1 Summary narrative | "### 1. Summary narrative" | L348 | present (3 real paragraphs) |
| 2 Sector intelligence | "### 2. Sector intelligence" | L356 | present (real content) |
| 3 Business-model intelligence | "### 3. Business-model intelligence" | L360 | present (real content) |
| 4 Competition intelligence | "### 4. Competition intelligence" | L364 | present (real content) |

Gate: PASS.

---

## AUDIT 1 — COVERAGE (fresh enumeration diffed vs A2 ledger)

| Category | A2 count | My fresh count | Orphan/missing | Status |
|---|---|---|---|---|
| Slides (presentation) | 47 | 47 (fresh grep `^\[page [0-9]+\]` = 47) | none | PASS |
| Footnotes (presentation) | 5 | 5 (ledger §4, reconciled non-anchored) | none | PASS |
| Notes to results | 16 | 16 (12 main + 8.1-8.4) | none | PASS |
| Board agenda items | 2 | 2 (results approval; AGM notice) | none | PASS |
| Board sub-enclosures | 4 | 4 | none | PASS |
| LRR paragraphs | 5 | 5 | none | PASS |
| Asset-cover cert paras | 13 | 13 | none | PASS |
| P&L line items | 29 | 29 | none | PASS |
| Reg 52(4) disclosures | 23 | 23 | none | PASS |
| Annexure-I fields | 20 | 20 | none | PASS |
| Annexure-A units | 12 | 12 | none | PASS |
| Appendix-1 line items | 17 | 17 | none | PASS |
| Signature blocks | 9 | 9 | none | PASS |

A4 preamble (L12-16) restates every count identically; ledger row disposition:
"All rows reviewed." A3 findings incorporated: 12 results (A3-01..A3-12) + 12
presentation (F1-a, F6-a, F6-b, F7-a, F9-a, F10-a, F14-a, F16-a..e) = 24, all
appearing in the review body and/or Step 8.5 question map / flags block. No orphan
ledger row (in ledger, absent from A4); no row my fresh pass found that the ledger
lacks. COVERAGE: PASS.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Slide-16 / statutory figures)

| Metric | A4 value | Recomputed | Source | Status |
|---|---|---|---|---|
| Q2+Q3 NII (derived) | 75.81 | 161.78−33.86−52.11 = 75.81 | pres L507 | PASS |
| Q2+Q3 PPOP (derived) | 36.00 | 80.10−14.48−29.62 = 36.00 | pres L517 | PASS (fixed) |
| Q2+Q3 PBT (derived) | 26.21 | 66.05−12.76−27.08 = 26.21 | pres L525 | PASS |
| Q2+Q3 PAT (derived) | 19.45 | 49.68−9.65−20.58 = 19.45 | pres L529 | PASS |
| Q2+Q3 avg NII/qtr | ~37.9 | 75.81/2 = 37.905 | derived | PASS |
| NII YoY | +38.97% | 13.20/33.86 = 38.98% (disclosed 38.97%) | pres L507 | PASS |
| PPOP YoY | +76.82% | 11.12/14.48 = 76.80% (disclosed 76.82%) | pres L517 | PASS |
| PBT YoY | +71.59% | 9.14/12.76 = 71.63% (disclosed 71.59%) | pres L525 | PASS |
| PAT incl OCI YoY | +70.17% | 6.78/9.65 = 70.26% (disclosed 70.17%) | pres L529 | PASS |
| Provisions YoY | +115.79% | 1.98/1.71 = 115.79% | pres L522 | PASS |
| Finance cost YoY | +15.48% | 5.15/33.23 = 15.50% (disclosed 15.48%) | pres L506 | PASS |
| Cost-to-Income Q1FY27 | 53.9% | 29.94/55.54 = 53.91% | Step 1L | PASS |
| Cost-to-Income Q1FY26 | 60.7% | 22.37/36.84 = 60.72% | Step 1L | PASS |
| Cost-to-Income Q4FY26 | 48.2% | 27.59/57.21 = 48.23% | Step 1L | PASS |
| ETR Q1FY27 | 24.37% | 5.34/21.90 = 24.38% (disclosed 24.37%) | pres L527 | PASS |
| ETR Q1FY26 | 23.42% | 2.99/12.76 = 23.43% (disclosed 23.42%) | pres L527 | PASS |
| Other-Inc share Q1FY27 | 15.3% | 8.48/55.54 = 15.27% | Step 2 dx6 | PASS |
| QoQ NII | −9.69% | −5.05/52.11 = −9.69% | pres L507 | PASS |
| QoQ PPOP | −13.58% | −4.02/29.62 = −13.57% (disclosed −13.58%) | pres L517 | PASS |
| QoQ ECL | +96.7% | 1.48/1.53 = 96.73% | pres L520 | PASS |
| PAT bridge closes | +6.78 | 13.20+5.50−7.57−1.98−2.35−0.02 = 6.78 | Step 4 | PASS |
| PPOP-change bridge | +11.12 | 25.60−14.48 = 11.12 | Step 4 | PASS |
| AUM YoY | +27.91% | 375.69/1346.05 = 27.91% | pres L143/146 | PASS |
| Own-book YoY | +31.74% | 392.01/1234.89 = 31.74% | pres L152 | PASS |
| Net worth YoY | +79.81% | 214.29/268.50 = 79.81% | pres L542 | PASS |
| CRAR change | +504bps | 25.32−20.28 = 5.04pp | pres L349 | PASS |
| COB change | −67bps | 11.33−10.66 = 0.67pp | pres L152 | PASS |
| GNPA / NNPA / credit-cost Δ | +80/+26/+37bps | 0.80/0.26/0.37pp | pres S12 | PASS |
| Stage-3 gross Δ | +1.46 | 33.49−32.03 = 1.46 | pres L425 | PASS |
| EPS Basic YoY | +31.2% / +35.5% | 0.73/2.34, 0.83/2.34 | res L685/L1066 | PASS |

Every A4 percentage is either exactly reproduced or matches the presentation's
own disclosed figure (which is computed off unrounded sub-cent underlying); all
gaps are strictly within rounding. No mismatch above rounding. ARITHMETIC: PASS.

Note (carried, not a new FAIL): the EPS 3.07-vs-3.17 within-filing conflict and
the Diluted-3.16 > Basic-3.07 anomaly are correctly surfaced (A3-05, Step 1L L86,
Q1 in Step 8.5). Slide-6 PBT 21.91 vs Slide-16 21.90 (0.01 rounding) is
acknowledged. Disbursement 166/232 carries the COLUMN_MISALIGN caveat. S-vs-C PAT
gap = ND every period (standalone-only filing) — reported as gap, not "clean."

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest bear from same text)

1. **Claim: "NII +39% with genuine spread expansion, not just volume" (L133).**
   Bear from same extract: NII grew 39% while AUM grew only 27.9% partly because
   the book is under-levered post-IPO — cheap equity (net worth +79.81%, D/E 3.10
   vs FY26 4.13) is temporarily depressing cost of borrowing (10.66%) and
   flattering spread/NIM; as the book re-levers toward ~4x, COB and spread
   normalise and the "expansion" partly unwinds. **Survives?** YES — but it is
   ALREADY IN the review (F6-a under-leverage story, Step 2 diagnostic 5 L137,
   Q5). No new graft required.

2. **Claim: "PPOP +77%; headline growth is real, not treasury-driven" (L119/L135).**
   Bear from same extract: Other/fee income jumped +184% (2.98→8.48) to 15.3% of
   net income with source/recurrence undisclosed; strip it to the prior 2.98 and
   PBT growth falls to ~29% (L138/L186). **Survives?** YES — already IN the review
   (Step 2 diagnostic 6, Step 4 revert-case, Q2/Q4). No new graft required.

3. **Claim: "GNPA/asset quality; RoA 3.45%, CRAR 25.32%, rating upgraded to A"
   as promotion rationale (L263).** Bear from same extract: FY26 asset quality was
   ARC-aided (Rs 27.93 Cr sale, incl Rs 1.83 Cr Stage-3, pres L421); Q1 FY27 had
   NIL ARC and GNPA rose 1.28%→2.08%, NNPA→0.93%, ECL +96.7% QoQ, absolute Stage-3
   +1.46 Cr — the "improving asset quality" read may invert. **Survives?** YES —
   already IN the review as the single-most-important trajectory caveat (F1-a,
   Step 3 L159, Step 5L, tripwire T2, Step 8C, Q3, and named the "single cleanest
   metric"). No new graft required.

All three strongest bear counters are already incorporated in the A4 review. No
surviving un-incorporated counter. ADVERSARIAL: PASS.

---

## VERDICT

**COMPLETE.** The prior-loop arithmetic FAIL (Step 3 PPOP 40.00→36.00) is fixed,
independently re-derived to 36.00, and the fix is isolated — no other cell moved,
no total/average or downstream claim depends on it, and re-grep confirms `40.00`
is gone. Full re-audit passes on all four gates: deliverable-completeness (four
brief parts present), coverage (13 results categories + 47 slides + 5 footnotes,
fresh counts match ledger, no orphan/missing rows), arithmetic (every derived
metric within rounding), and adversarial (the three strongest bear counters are
already in the review). Cleared to proceed to Notion save.

```yaml
stage: A5-adversary
company: "LAXMIINDIA"
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
