# A5 ADVERSARY / COMPLETENESS AUDIT (RE-AUDIT, loop 2) — Arisinfra Solutions (ARIS) Q1 FY27
### Model: claude-opus-4-8 | Fresh context: A4 review + A1 extracts + A2 ledgers only. Re-derived independently.
### This is the FINAL audit of record (overwrites prior). Verdict at end.

Scope of re-audit per task: (a) VERIFY the two loop-1 fixes landed; (b) re-run all four audits;
(c) recompute the segment sum and the annualisation logic myself, do NOT rubber-stamp.

---

## VERIFICATION OF THE TWO LOOP-1 FIXES

### Fix 2 (annualised-EPS INVALID caveat, Step 6A) — LANDED CORRECTLY. PASS.
Present at review l.421-436, symmetric to the ROCE-annualisation discount. Recomputed both legs:
- One-time slice: finance-cost reset +5.38 Cr + absence of Q1FY26 exceptional +2.88 Cr = **+8.26 Cr**;
  8.26 / 20.36 (PBT uplift, 26.67-6.31) = **40.6% ≈ ~40%** ✓.
- Deceleration: revenue -15.3% QoQ (290.81/343.36-1) ✓; diluted EPS -20.5% QoQ (2.05 vs 2.58, deck L1078) ✓.
- Annualised EPS 2.05×4 = 8.2 ✓, correctly set aside. Caveat is sound. No issue.

### Fix 1 (slide-36 Q1FY27 segment sum 3,437; 528 Mn gap vs reported) — DID NOT LAND CORRECTLY. FAIL.
The arithmetic *within* A4's chosen numbers is correct (1,302+1,774+361 = 3,437; 3,437-2,909 = 528).
BUT the premise — that 1,302/1,774/361 is the **Q1-FY27** column of slide 36 — is a period-mapping
error, contradicted by the deck's own slides and the press release:

| Stream | A4/A2 "Q1-FY27" (slide 36, l.1025) | True Q1-FY27 | Source that fixes it |
|---|---|---|---|
| CM | 1,774 | **1,540** | slide 27 L786; press release l.75-76 ("to Rs 1,540 Mn from Rs 839 Mn Q1FY26") |
| Services | 361 | **277** | press release l.78 ("grew 48% YoY to Rs 277 Mn from Rs 187 Mn") |
| B2B | 1,302 | **1,092** | slide 26 L767; slide-10 mix 37% of 2,908 = 1,076 |

Correctly mapped, slide-36 Q1-FY27 = 1,092 + 1,540 + 277 = **2,909 ≈ reported 2,908.09 (l.475)** — it
RECONCILES. The set 1,302/1,774/361 = 44.8% / 61.0% / 12.4% = **118% of revenue**, impossible for a
single quarter; those are the Q1-FY26 / Q4-FY26 / middle bars (the 1,774 CM bar is Q4-FY26, since the
press release fixes CM Q1-FY27 at 1,540). There is **no 528 Mn top-line overstatement**; slide 36 does
NOT "fail to reconcile to the reported P&L." The genuine slide-36 defect is only the Services x-axis
mislabel (Q3-FY26 vs Q4-FY26, already captured as F16-2) and general period-label ambiguity — NOT a
revenue overstatement. Fix 1 hardened a non-existent discrepancy into a stated finding, a management
question (Q8), a YAML question, and a flag.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)
PLAIN-LANGUAGE BRIEF, four labelled parts, all present and non-empty with real content:

| Part | Location | Present? | Content check |
|---|---|---|---|
| 1 Summary narrative | review l.604-629 (~24 lines) | present | Real; numbers-anchored |
| 2 Sector intelligence | review l.631-648 | present | Real; construction-credit-cycle thesis |
| 3 Business-model intelligence | review l.650-669 | present | Real; three-stream + S-vs-C |
| 4 Competition intelligence | review l.671-689 | present | Real; peer/moat bear read |

Gate 0: **PASS.**

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledgers)

Results filing (fresh grep + manual sweep of extract_results):

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| notes | 16 | 16 (SA 1-8 l.225-278; CO 1-8 l.552-604) | none | PASS |
| line_items | 77 | 77 (27+6+38+6) | none | PASS |
| zero_standing | 1 | 1 (l.493 assoc share) | none | PASS |
| agenda_items | 1 | 1 (l.37-44) | none | PASS |
| auditor_paras | 13 | 13 (SA 5 + CO 8) | none | PASS |
| entities | 8 | 8 (7 subs + 1 assoc, l.359-374) | none | PASS |
| signatures | 5 | 5 | none | PASS |
| annexures | 4 | 4 | none | PASS |

Presentation deck (fresh pass of extract_presentation):

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| slides | 42 | 42 ([page N] markers) | none | PASS |
| numbers | 211 | 211 (accepted A2 exhaustive per-line scan) | none | PASS |
| line_items | 70 | 70 (16+16+38) | none | PASS |
| zero_standing | 15 | 15 | none | PASS |
| footnotes | 10 | 10 | none | PASS |

No orphan rows (every material ledger category is cited in A4 or covered by its blanket
row-by-row preamble l.16-34). No row my fresh pass found that the ledger lacks. Coverage: **PASS.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Mn ×0.1)

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Consol revenue Q1FY27 | 290.81 | 2,908.09 Mn = 290.81 | l.475 | OK |
| Op EBITDA Q1FY27 | 30.55 | 266.67+19.02+63.62-43.83 = 305.48 Mn | l.489/484/485/476 | OK |
| Op EBITDA Q1FY26 | 18.16 | 91.90+7.57+117.38-35.26 = 181.59 | l.489/484/485/476 | OK |
| Op EBITDA margin Q1FY27 | 10.51% | 30.55/290.81 = 10.50% | derived | OK |
| Op EBITDA YoY | +68.2% | 30.55/18.16-1 = 68.2% | derived | OK |
| Margin YoY | +195 bps | 10.51-8.56 | derived | OK |
| Finance cost YoY | -45.8% | 63.62/117.38-1 | l.485 | OK |
| ETR Q1FY27 | 24.9% | 66.36/266.67 = 24.88% | l.508/502 | OK |
| ETR Q1FY26 | 19.0% | 11.97/63.09 = 18.97% | l.508/502 | OK |
| PAT YoY | +291.9% | 200.31/51.12-1 | l.510 | OK |
| PBT YoY | +322.7% | 266.67/63.09-1 | l.502 | OK |
| PAT margin Q1FY27 | 6.89% | 200.31/2,908.09 | derived | OK |
| PAT bridge PBT change | +20.36 | 12.39-1.14+5.38+0.85+2.88 | Step 4 | OK |
| PAT bridge PAT change | +14.92 | 20.36-5.44 = 14.92 (=20.03-5.11) | derived | OK |
| S-vs-C: S % of C Q1FY27 | 37.2% | 7.46/20.03 = 37.2% | l.206/510 | OK |
| Subs as % of S Q1FY27 | 168.5% | 12.57/7.46 | derived | OK |
| Unreviewed subs rev % | 55.7% | 1,620.83/2,908.09 | l.388/475 | OK |
| Unreviewed subs PAT % | 63.5% | 127.28/200.31 | l.388/510 | OK |
| Standalone rev QoQ | -37.9% | 128.73/207.36-1 | l.180 | OK |
| Standalone Op EBITDA Q1FY27 | 7.62 | 97.50+13.62+48.10-82.95 = 76.27 Mn = 7.63 | l.194/189/190/181 | rounding OK |
| Services share (#5) | 9.5% | 277/2,908 = 9.52% | l.451 | OK |
| Implied share-count rise QoQ | ~16% | 0.922/0.795-1 = 16.0% | derived | OK |
| **Slide-36 Q1FY27 segment sum** | **3,437 (overstates by 528)** | **2,909 = 1,092+1,540+277 ≈ reported 2,908; reconciles** | slide 27 L786; PR l.75-76,l.78; slide 26 L767; slide 10 L281-287 | **MISMATCH — see Fix 1** |

All P&L-derived metrics reconcile to rounding. The single arithmetic/derivation mismatch above
rounding is the slide-36 segment characterization: A4's "Q1-FY27 = 3,437, overstates reported top
line by 528 Mn" is contradicted by source lines that fix CM Q1FY27 = 1,540 (not 1,774), Services =
277 (not 361), B2B = 1,092 (not 1,302), yielding 2,909, which reconciles.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims + strongest bear from same text)

1. **"Op EBITDA margin +195 bps to 10.51%, genuine mix-shift expansion."**
   Bear counter: Q4FY26 EBITDA was struck AFTER a 4.46 Cr ECL charge and Q1FY27 after ZERO ECL
   (l.482); ex-ECL, underlying EBITDA deteriorated ~4.5 Cr QoQ, and standalone margin is only 5.92%.
   Survives — but ALREADY in A4 (Step 3 l.296, Step 1C). No graft needed.

2. **"Revenue +37.1% YoY, strong."** Bear counter: -15.3% QoQ deceleration off the Q4 peak (itself a
   note-5 balancing-figure column), and 55.7% of revenue sits in seven MSKC-unreviewed subsidiaries.
   Survives — ALREADY in A4 (Step 2C, Step 3). No graft needed.

3. **"PAT nearly 4x YoY."** Bear counter: ~40% one-time (finance-cost reset +5.38 + absence of the
   Q1FY26 exceptional +2.88 = +8.26 Cr of +20.36 Cr PBT). Survives — ALREADY in A4 (Step 4, 6A).
   No graft needed.

No NEW bull-claim bear counter survives unincorporated. However, the adversarial pass surfaces the
inverse defect: A4's OWN negative claim ("slide 36 overstates the top line by 528 Mn / does not
reconcile") does NOT survive the same extracted text (press release l.75-76/l.78; slides 26/27/10),
and must be corrected before save. This feeds A4's own disclosure-credibility bear read (Q8, Part 4
Competition), so leaving it uncorrected would encode a false ~18% revenue-overstatement claim into the
durable record.

---

## VERDICT

**INCOMPLETE.** loop_back_to: **A4.**

Gap: Fix 1 did not land correctly. A4 asserts (Step 3 l.277; Step 6/8.5 Q8 l.556; YAML question
l.723; flag l.754) that slide 36 shows Q1-FY27 segment revenue 1,302/1,774/361 = 3,437 Mn and
"overstates the top line by 528 Mn / does not reconcile to the reported P&L." This is a
period-mapping error: press release l.75-76 fixes CM Q1FY27 = 1,540 (so 1,774 is Q4-FY26), l.78 fixes
Services = 277 (so 361 is the middle bar), slide 26 L767 and slide-10 37% mix fix B2B = 1,092 (not
1,302). Correctly mapped, slide-36 Q1-FY27 = 1,092+1,540+277 = 2,909 ≈ reported 2,908.09 and RECONCILES;
1,302/1,774/361 sums to 118% of revenue and cannot be one quarter. A4 must recharacterize slide 36 as a
period-label ambiguity (the real defect is the Services Q3/Q4-FY26 x-axis mislabel, F16-2) rather than a
528 Mn top-line overstatement, and correct Q8, the corresponding YAML question, Step 3, and the flag.
Fix 2 (annualised-EPS INVALID caveat) is correct; Audits 0/1 pass; all P&L arithmetic reconciles.

```yaml
stage: A5-adversary
company: "ARIS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "Slide-36 Q1FY27 segmental revenue column / cross-slide gap"
    a4_value: "1,302/1,774/361 = 3,437 Mn; overstates reported top line by 528 Mn; does not reconcile"
    recomputed: "Q1FY27 = 1,092(B2B)/1,540(CM)/277(Services) = 2,909 Mn ~= reported 2,908.09 Mn; reconciles; 1,302/1,774/361 = 118% of revenue = Q1FY26/Q4FY26/middle bars misattributed"
    source_line: "slide 27 L786 (CM Q1FY27=1,540); press release l.75-76 (CM 1,540 from 839) and l.78 (Services 277 from 187); slide 26 L767 (B2B 1,092); slide 10 L281-287 (mix 37/53/10); results l.475 (2,908.09)"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Fix 1 wrong: slide-36 '528 Mn top-line overstatement / does not reconcile' is a period-mapping error. CM Q1FY27 is 1,540 (slide 27 L786, PR l.75-76), Services 277 (PR l.78), B2B 1,092 (slide 26 L767); Q1FY27 column = 2,909 ~= reported 2,908 and RECONCILES. A4 must recharacterize slide 36 as period-label ambiguity (Services Q3/Q4-FY26 mislabel, F16-2), not a 528 Mn overstatement, and correct Step 3, Q8, the YAML question, and the flag. Fix 2 (annualised-EPS caveat) is correct; deliverable, coverage, and all P&L arithmetic pass."
```
