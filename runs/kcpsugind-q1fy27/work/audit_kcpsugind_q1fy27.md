# A5 ADVERSARY / COMPLETENESS AUDIT — KCPSUGIND Q1 FY27 (RESULTS)

Auditor: A5 (fresh context). Inputs seen: A4 review, A1 extract, A2 ledger only.
Unit convention re-derived independently: filing in Rs Lakhs, Cr = Lakhs ÷ 100.
Pages 3-4 are OCR'd; every number the review draws from those pages was re-checked
against the raw extract and, where possible, cross-footed to a filed subtotal.

VERDICT: **INCOMPLETE** — one arithmetic/extraction error in A4 above rounding
(FVOCI line L182). Loop back to **A4**. Everything else (deliverable, coverage,
tripwires, all other arithmetic) passes.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

Plain-Language Brief section present with all four labelled, non-empty parts:

| Part | Present? | Evidence (review line) |
|---|---|---|
| 1. Summary narrative (10-20 lines) | PRESENT | L416-422, two full paragraphs, real content |
| 2. Sector intelligence | PRESENT | L424-426, seasonality + provenance-tagged |
| 3. Business-model intelligence | PRESENT | L428-430, three-part SOTP model |
| 4. Competition intelligence | PRESENT | L432-434, provenance-tagged, Eimco pricing-power test |

Role 5 (Concall) correctly marked **N.A.** (review L15; no transcript in run; no
concall content invented). Questions routed to IR/AGM channel, not a live call. PASS.

Deliverable gate: **PASS.**

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger)

Re-ran the count by hand over the extract:

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| Agenda items (L43-106) | 5 | 5 | none | OK |
| Notes (L268-283) | 6 | 6 | none | OK |
| P&L line items (L147-200) | 37 (32 val/subtotal + 5 headers) | 37 | none | OK |
| Segment categories (L215/225/239/258) | 4 | 4 | none | OK |
| Segment sub-header (Seg Liabilities L249) | 1 | 1 | none | OK |
| Segment line items (9+13+7+7+7) | 43 | 43 | none | OK |
| Auditor paras standalone (L309-369) | 6 | 6 | none | OK |
| Auditor paras consolidated (L406-483) | 7 | 7 | none | OK |
| Entities (L516-519) | 4 | 4 | none | OK |
| Signature blocks (L110/285/373/487) | 4 | 4 | none | OK |
| **Total** | **117** | **117** | none | **OK** |

Fresh count reconciles to 117 (5+6+37+4+1+43+6+7+4+4). OCR-garbled rows I re-checked:
consolidated auditor para 3 ("J." at L423) present; Annexure entity 3 ("J." at L518,
THE EIMCO-K.C.P) present; segment sub-items "(2) un-allocable expenditure" (L234) and
"¢) Power & Fuel" capital-employed (L261) present. No row my pass found is absent from
the ledger; no ledger row is absent from the review.

Every ledger row is used or defensibly immaterial:
- All 6 notes appear in review 0D table; Note 6 (FV gain) drives the whole earnings-quality read.
- All P&L rows appear in Step 1 tables; the 8 ZERO_STANDING rows (dashes) shown as ND(nil) — defensibly immaterial.
- Segments fully carried into the segment table and Steps 5/6.
- Both LRRs discussed (seasonal-deferral para 4/5, unmodified conclusion para 6, consolidated other-matter para 7 on Quality Engineering).
- All 4 entities and 4 signatories named.
- The 5 A2 ARITHMETIC_CHECK / OCR_SUSPECT segment flags (L241/243/247/252/265) are year-ended balance figures; I independently confirmed they are OCR artifacts (e.g. Sugar std year-ended "43896.65" cannot be real: the segment-asset Total year-ended 53314.14 equals the 31.03.2026 column and only foots with Sugar = 13896.65, not 43896.65). Filing arithmetic intact; defensibly immaterial to a Q1 read. Handled.

**Orphan rows: none. Missing-from-ledger: none. COVERAGE: PASS.**

Minor note (not a gap): the review's preamble component list (L11) sums to 116 because
it does not itemise the segment sub-header the ledger counts to reach 117; the ledger's
117 is internally correct. Descriptive slip only, no unreviewed unit.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakhs, independent of A4/A3 cites)

All figures below recomputed from the extract at Lakhs÷100. Matches unless noted.

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Revenue YoY Std | +23.1% | (6813.88−5535.08)/5535.08 = 23.1% | L147 | OK |
| Revenue YoY Cons | +31.4% | (7802.66−5937.09)/5937.09 = 31.4% | L147 | OK |
| Other Income YoY Std | +109.0% | (5477.56−2620.96)/2620.96 = 109.0% | L148 | OK |
| Other Income YoY Cons | +100.4% | (5552.47−2770.25)/2770.25 = 100.4% | L148 | OK |
| PBT YoY Std | +132.7% | (5314.34−2284.05)/2284.05 = 132.7% | L163 | OK |
| PBT YoY Cons | +120.9% | (5417.54−2452.60)/2452.60 = 120.9% | L163 | OK |
| PAT YoY Std | +158.5% | (4556.47−1762.53)/1762.53 = 158.5% | L176 | OK |
| PAT YoY Cons | +141.5% | (4624.77−1915.22)/1915.22 = 141.5% | L176 | OK |
| EPS YoY Std / Cons | +159.4% / +141.4% | 2.47/1.55 / 2.39/1.69 | L193 | OK |
| Op EBITDA Std Q1FY27 | 1.71 | 53.14+0.56+2.79−54.78 = 1.71 | L147-163 | OK |
| Op EBITDA Cons Q1FY27 | 2.62 | 54.18+0.90+3.06−55.52 = 2.62 | L147-163 | OK |
| Op EBITDA Std/Cons Q1FY26 | (0.73)/(0.25) | −0.73 / −0.25 | L147-163 | OK |
| Op EBITDA margin Std/Cons | 2.5% / 3.4% | 1.71/68.14, 2.62/78.03 | derived | OK |
| Margin expansion | +380 bps both | −1.3→2.5, −0.4→3.4 | derived | OK |
| Core PBT ex-OI Std/Cons Q1FY27 | (1.64)/(1.34) | 53.14−54.78, 54.18−55.52 | L148/163 | OK |
| PBT ex-MTM Std Q1FY27/Q1FY26 | 1.92 / 0.03 | 53.14−51.22, 22.84−22.81 | L163/283 | OK |
| Other Income / PBT Std Q1FY27 | 103.1% | 54.78/53.14 | derived | OK |
| ETR Std Q1FY26 / Q1FY27 | 22.9% / 14.3% | 5.22/22.84, 7.58/53.14 | L166/163 | OK |
| ETR Cons Q1FY27 | 14.6% | 792.77/5417.54 (tax=cur26.02+def766.75) | L237/163 | OK |
| ETR Cons FY26 | 29.2% | 459.44/1572.51 | L237/163 | OK |
| PAT margin Std/Cons Q1FY27 | 66.9% / 59.3% | 45.56/68.14, 46.25/78.03 | derived | OK |
| MTM % of Std Other Income | 93.5% | 5121.91/5477.56 = 93.5% | L283/148 | OK |
| MTM % of Std PBT | 96.4% | 5121.91/5314.34 = 96.4% | L283/163 | OK |
| Seasonal deferral | Rs 10.02 Cr | 943.99+58.11 = 1002.10 L | L342-343 | OK |
| PAT bridge Std | +27.93 (1.73 core +28.57 OI −2.36 tax) | reproduces (30.30 PBT − 2.36) | L163/166 | OK |
| PAT bridge Cons | +27.10 (1.83 core +27.82 OI −2.56 tax) | reproduces (29.65 PBT − 2.56) | L163/237 | OK |
| S-vs-C PAT gap Q1FY27 | +0.68 / +1.5% | 46.25−45.56; 0.68/45.56 | L176 | OK |
| S-vs-C PAT gap Q1FY26 | +1.53 / +8.7% | 1915.22−1762.53=152.69; /1762.53 | L176 | OK |
| Eimco Cons rev Q1FY27 | 1171.13 (OCR-corr from 1174.13) | Total 7941.55 − other cons segs 6770.42 = 1171.13 | L219/222 | OK (independently reconciled) |
| **Eimco/Engineering margin** | **11.6%** | 135.28/1171.13 = 11.55% | L229/219 | OK |
| Eimco margin Q1FY26 / FY26 | 39.4% / 31.3% | 324.54/824.55, 2463.32/7863.55 | L229/219 | OK |
| Eimco rev growth / PBIT change | +42.0% / −58% | (1171.13−824.55)/824.55; (135.28−324.54)/324.54 | L219/229 | OK |
| Eimco pre-tax contrib Q1FY27/FY26 | 1.31 / 20.52 | 135.28−4.32; 2463.32−411.00 | L229 | OK |
| Sugar seg result Q1FY27 / margin | 2.14 / 5.5% | 214.42; 214.42/3874.34 | L226/216 | OK |
| Quality Eng loss % of Cons PAT | 0.12% | 5.49/4624.77 | L474/176 | OK |
| Depreciation YoY Std | (7.0%) | (56.11−60.25)/60.25 = −6.9% | L158 | MINOR (0.1pp, immaterial line ~Rs 0.04 Cr; within tolerance) |
| **FVOCI equity-instr OCI, Cons Q1FY27** | **+Rs 1.34 Cr (134.41 L)** | **434.41 L = +Rs 4.34 Cr** | **L182** | **FAIL (loop 1)** |

### The FAIL, in detail (loop 1)
A4 states the consolidated Equity-Instruments-through-OCI movement as "+Rs 1.34 Cr"
(explicitly "FVOCI +134.41 L (L182)" at review L283; repeated at L286 Step 6D bull
facts, in the business-model brief L430, and in Question A3-F9-01 L337).

Raw extract L182, consolidated 30.06.2026 column = **434.41 Lakhs = Rs 4.34 Cr**
(prior periods (116.37)/(1.77)/(148.84); standalone all dash). The A2 ledger
independently read the same value 434.41 (ledger L115). A4 alone transcribed the
leading digit as 1 instead of 4 — a **Rs 3.00 Cr misstatement**, ~224% of the stated
figure, well above rounding, repeated in four places.

Direction/qualitative claim ("sign-flip from negative to positive this quarter") is
correct and, if anything, the true Rs 4.34 Cr *strengthens* the earnings-in-OCI /
S-vs-C-divergence point. It does not change the PROCEED WITH FLAGS verdict, the two
tripwires, or any headline. But it is a hard arithmetic error on a filed line and must
be corrected before save. **Loop back to A4:** change 134.41 L / Rs 1.34 Cr → 434.41 L /
Rs 4.34 Cr in review L283, L286, L430, and QfM A3-F9-01 (L337).

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, bear counter from same text)

1. **"Revenue grew a real +23.1%/+31.4% YoY."** Bear from same text: growth did not
   reach operating profit — core PBT ex-OI still negative both books (−1.64/−1.34,
   L163/148); and standalone "Others" Q1FY26 base (4221.92, L220) is OCR-suspect,
   softening the standalone YoY base. **Counter survives but is already fully
   incorporated** (Step 2C-3, Step 1C read, L399 note). No graft needed.

2. **"Sugar swung to +Rs 2.14 Cr profit in the off-season."** Bear from same text: the
   auditor seasonal-deferral pushes Rs 1002.10 L of off-season cost (incl. sugar/cogen)
   out of Q1 into Q4 FY27 (L342-343); the sugar swing is partly a deferral artifact, and
   Note 1 warns the quarter is not an annual indicator (L268). **Counter survives but is
   already incorporated** (0D auditor para, Step 4c, flag #6, brief). No graft needed.

3. **"Investment book marked UP; FVOCI reserve sign-flipped positive (bull fact)."**
   Bear from same text: the same book posted an MTM LOSS of Rs 9.53 Cr the prior quarter
   (Q4 FY26 Other Income, L148); it is market beta, reverses together in a down market;
   and 96% of PBT rides it. **Counter survives but is already incorporated** (Step 3c,
   Step 6D symmetric read, flag #4, brief). Separately, the magnitude of this very bull
   fact is misstated — see the FVOCI FAIL above.

No surviving bear counter is *absent* from A4 — the review is already strongly symmetric.
The only defect requiring A4 action is the arithmetic error, not a missing counter.

### Tripwire firings vs primary text
- **Rs 257 Cr Eimco/Hyundai order not confirmed — SUPPORTED.** Neither "257" nor
  "Hyundai" appears anywhere in the extract. The only board-approved contract is the
  Rs 1,53,40,01,569 (Rs 153.40 Cr) supply contract with THE EIMCO-KCP Limited, the
  wholly owned subsidiary (L100-104) — a separate, intra-group item. "Not confirmed" is
  correct.
- **Eimco/Engineering margin 11.6% — SUPPORTED.** 135.28/1171.13 = 11.55% (L229/L219),
  with the OCR-corrected consolidated Engineering revenue 1171.13 independently
  reconciled to the filed consolidated segment-revenue Total 7941.55 (L222). Firing valid.

### Questions-for-Management coverage
All 10 A3 FORWARD-SIGNAL/AMBIGUOUS findings (7 FS: F2, F5, F6, F8, F9, F13-03, OI-01;
3 AMBIGUOUS: F12, F13-02, F14) each have at least one Step 8.5 row (10 rows present,
L332-341). PASS. (F13-01 is a catalyst/monitorable, not FS/AMBIGUOUS — correctly a
monitorable, not a question.)

---

## VERDICT (loop 1)

**INCOMPLETE.** Loop back to **A4**.

Gap: consolidated FVOCI Equity-Instruments-through-OCI movement is misstated as
Rs 1.34 Cr (134.41 Lakhs); the filed value at L182 is Rs 4.34 Cr (434.41 Lakhs),
independently confirmed by the A2 ledger. Error is above rounding and repeated in
review L283, L286, L430, and Question A3-F9-01 (L337). A4 must correct all four before
this review proceeds to Notion save. All other checks — deliverable (4/4 brief parts +
Role 5 N.A.), coverage (117/117, zero orphans), both tripwires, and every other derived
metric — pass.

```yaml
stage: A5-adversary
company: "kcpsugind"
quarter: "q1fy27"
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
  - metric: "Consolidated FVOCI (Equity Instruments through OCI) movement, Q1 FY27"
    a4_value: "+Rs 1.34 Cr (134.41 Lakhs)"
    recomputed: "+Rs 4.34 Cr (434.41 Lakhs)"
    source_line: "L182 (extract); confirmed by A2 ledger L115"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Cons FVOCI equity-instruments OCI misstated as Rs 1.34 Cr / 134.41 L; filed value L182 = Rs 4.34 Cr / 434.41 L (A2 ledger concurs). Above rounding, repeated at review L283, L286, L430, and QfM A3-F9-01 L337. A4 to correct all four before save."
```

---

## RE-AUDIT (loop 2) — verification of A4's single correction

A4 applied the one required fix. Re-read the corrected review fresh and verified the
three points the coordinator specified. No other change to my loop-1 findings.

### (1) All four FVOCI locations now read 434.41 L / Rs 4.34 Cr — none missed

| Location | Corrected text | Status |
|---|---|---|
| Review body, Step 6D confirming evidence (L283) | "FVOCI +434.41 L / Rs 4.34 Cr (L182)" | FIXED |
| Review body, Step 6D symmetric read (L286) | "FVOCI reserve sign-flipped positive +Rs 4.34 Cr (L182)" | FIXED |
| QfM row A3-F9-01 (L337) | "swung +Rs 4.34 Cr this quarter (L182 = 434.41 L; ... corrects an inherited A3-F9-01 OCR transcription that had reduced the filed 434.41 L to 134.41 L)" | FIXED + provenance |
| Closing YAML, QfM entry (L462) | "consolidated FVOCI reserve sign-flipped +Rs 4.34 Cr (434.41 L, L182)" | FIXED |

Confirmed against extract: L182 consolidated 30.06.2026 column = 434.41 Lakhs = Rs 4.34 Cr;
A2 ledger L115 concurs (434.41). All four locations reconcile to the filed value.
Additional (unrequired but correct) provenance notes added at preamble L5, L13, and a new
CORRECTION flag at YAML L487 — consistent, no contradiction. The business-model brief (L430)
carries no FVOCI magnitude and needed no change; the coordinator's "business-model brief"
maps to the L286 Step 6D symmetric-read location, now fixed. No stray 134.41 L / Rs 1.34 Cr
FVOCI reference remains anywhere in the review.

### (2) No unrelated 1.34 figure was wrongly changed

The legitimate consolidated **Core PBT ex-OI = (1.34)** (54.18 − 55.52) is intact and
unchanged at L107, L116, L147, L173, L199, L382. The consolidated **Q4 FY26 EPS = (1.34)**
is intact at L91-92. Both are correct filed/derived figures and were correctly left alone.
The fix touched only the FVOCI line.

### (3) Nothing else regressed

Spot-re-verified the load-bearing figures after the edit: PAT 45.56/46.25 and YoY
+158.5%/+141.5% (L176), both tripwires (Rs 257 Cr not confirmed L100; Eimco margin
135.28/1171.13 = 11.6% L229/L219), S-vs-C gap +1.5%/+8.7% (L405-406), ETRs 14.3%/14.6%
(L111-112), MTM 96.4%/93.5% (L36), PBT bridge (Step 4), the 10 QfM rows (L332-341), the
4-part plain-language brief (L416-434), Role 5 N.A. (L15), and PROCEED WITH FLAGS (L322)
— all unchanged and still reproduce. Coverage still 117/117, zero orphans. The
depreciation YoY (7.0% vs my 6.9%) remains the only residual item and stays within
rounding tolerance on a Rs 0.04 Cr line (non-blocking, as in loop 1).

### VERDICT (loop 2)

**COMPLETE.** The single flagged arithmetic mismatch is closed in all four locations
and reconciles to the filed L182 value (434.41 L / Rs 4.34 Cr); no legitimate figure was
disturbed and nothing regressed. No remaining gap. This review may proceed to Notion save.

```yaml
stage: A5-adversary
company: "kcpsugind"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
loop: 2
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
