# A5 ADVERSARY / COMPLETENESS AUDIT — GOCL Corporation Ltd, Q1 FY27 (quarter ended Jun 30, 2026)
### Target: review_goclcorp_q1fy27.md (A4) | Independent re-derivation from A1 extract + A1-ADDENDUM and A2 ledger
### Verdict: **INCOMPLETE** — loop back to **A4** (with a secondary A2/A1-ADDENDUM enumeration gap named)

Units: filing prints Rs Lakhs (x0.01 = Rs Crores). Where a cell was cmap-corrupt I anchor to the render-adjudicated A1-ADDENDUM (extract lines 1094-1127); otherwise to OCR/clean-primary as the ledger cites. Every figure below carries a line cite; I do not defer to A4's or A3's cites.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate — run first)

The mandatory PLAIN-LANGUAGE BRIEF is present with all four labelled parts, each non-empty and provenance-tagged:

| Part | Location (review lines) | Present? | Note |
|---|---|---|---|
| (1) Summary narrative | 478-479 | PRESENT | ~1 dense para, 10-20 line equivalent; numbers-first, correct one-off framing |
| (2) SECTOR intelligence | 481-485 | PRESENT | [Notion/prior] + [Filing Q1FY27] blocks; HNPCL/APTEL/EMS/Realty |
| (3) BUSINESS-MODEL intelligence | 487-492 | PRESENT | treasury/land vehicle; HGHL shell; deleveraging ambiguity |
| (4) COMPETITION intelligence | 494-498 | PRESENT | optionality-not-franchise; execution/governance risk |

Gate: **PASS.** All three intelligence blocks are provenance-labelled; the narrative is real content, not a placeholder.

---

## 1. COVERAGE AUDIT (fresh enumeration diffed against A2 ledger)

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Notes (consol 9 + std 9) | 18 | 18 | none — all mapped in Step 0D table (review 54-65) | PASS |
| Segment leaf rows | 26 | 26 | none — EMS/Realty results, unallocable & total assets/liab, discontinued HFS all cited (Step 5, Step 6, brief) | PASS |
| Line items (leaf) | 94 | 94 | none material — all P&L/segment/discontinued rows carried into Step 1 tables | PASS |
| Board agenda items | 1 | 1 | none — single combined resolution, board Aug-13-2026 (review 22, 56) | PASS |
| Auditor paragraphs | 12 (7 consol + 5 std) | 12 | none — conclusion, both EoM, Other Matter all cited; scope/resp/standard boilerplate = reviewed-no-finding (review 67-70) | PASS |
| Entities | 2 | 2 | none — GOCL + HGHL (review 24, Q4/Q13) | PASS |
| Signatures | 5 | 5 | none — enumerated review line 25 | PASS |
| Board Outcome letter | (Section A) | matched | meeting times 03:15-05:20 not restated but immaterial boilerplate; auditor Haribhakti named; reviewed-no-finding | PASS |
| Discontinued-ops sub-tables | 2 (consol E-N3-sub, std H-N8-sub) | 2 | none — both 5-row tables reflected in discontinued PAT figures (Step 4B) | PASS |
| Both EoM + Other Matter | 3 paras | 3 | none — dual EoM (B6/F5) + Other Matter (B7) all surfaced AMBER | PASS |

**Coverage orphan finding:** none. Every A2 FINDING/flag row is cited or reviewed-no-finding.

**One row my fresh pass found that the ledger's treatment lacks (return to A2 — see Section 2, item AR-1):** ledger row **C14 Q1FY26 = 4,220.09** carries NO flag, yet it is internally contradicted by (a) the same statement's C13+C14=C15 identity and (b) Note 2's own text (1,220.09). A2 raised NUMBER_DISCREPANCY on C12/C22/C34/C38 but MISSED the C13+C14≠C15 arithmetic break on the exceptional-items row. This unflagged corruption is the seed of the A4 arithmetic failure below.

---

## 2. ARITHMETIC AUDIT (every derived figure recomputed from raw extract lines)

### 2A. Confirmations (tie exactly, within rounding)

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Corrected consol Q1FY26 Total income | 8,649.63 lakh (Rs 86.50 Cr) | 339.18 + 8,310.45 = 8,649.63; also 5,078.01 + 3,571.62 = 8,649.63; also seg 174.76+2,123.55+6,351.32 = 8,649.63 | C2/C3 289-290; ADDM 1097/1123; D2-D4 141-143 | CONFIRM (addendum bonus "8,849.63" line 1122 is a 6→8 typo; A4 correctly overrode with derived value) |
| S-vs-C net PAT gap Q1FY27 | +25.8% | (4,039.87−3,210.77)/3,210.77 = +25.8% | C25 312; ADDM item16 1113 | CONFIRM |
| S-vs-C net PAT gap Q4/Q1FY26/FY26 | −1.4% / +1.3% / +5.3% | −1.38% / +1.29% / +5.26% | C25 312; ADDM 1113 | CONFIRM |
| Continuing/discontinued split Q1FY26 std | 97.3% disc | 1,173.92/1,206.99 = 97.26% | ADDM 1111/1112/1113 | CONFIRM |
| ETR continuing (C Q1FY27 / C Q1FY26 / S Q1FY27 / S Q1FY26) | 22.0 / 14.7 / 23.5 / 20.0% | 1,239.11/5,624.31=22.03; 925.62/6,298.10=14.70; 1,094.37/4,650.47=23.53; 825.31/4,132.77=19.97 | C19/C15 306/302; ADDM 1110; G13 233 | CONFIRM |
| Deferred-tax shield bps (C Q1FY27) | ~134 bps | 75.63/5,624.31 = 1.34% | C18 305; C15 302 | CONFIRM |
| Unallocable assets = % of total assets | 93.8% | 3,37,109.48/3,59,411.21 = 93.79% | D22 408; ADDM item6 1103 | CONFIRM |
| Unallocable liab YoY | −60.2% | (388.77−976.07)/976.07 = −60.17% | D28 413 | CONFIRM |
| Total liab / total assets YoY | −64.7% / −9.5% | −64.75% / −9.52% | ADDM 1104/1103; D-rows | CONFIRM |
| Discontinued HFS assets QoQ | +33.9% | (78.39−58.54)/58.54 = +33.91% | D23 409 | CONFIRM |
| Other income / continuing PBT (4 cells) | 105 / 132 / 113 / 115% | 104.6 / 131.9 / 113.0 / 114.8% | C3/C15; G3/G13 | CONFIRM |
| Other income / revenue (std) | 12.3x | 52.55/4.29 = 12.25x | G2/G3 861-862 | CONFIRM |
| HGHL = % of consol PAT | 20.5% | 829.11/4,039.87 = 20.52% | B7 para 183-202; C25 312 | CONFIRM |
| Revenue YoY / D&A YoY / OI YoY (consol) | +26.4 / +62.3 / −29.2% | +26.5 / +62.3 / −29.2% | C2/C10/C3 | CONFIRM |
| PBT-continuing YoY / PAT-continuing YoY (consol) | −10.7% / −18.4% | −10.7% / −18.4% | C15/C20 302/307 | CONFIRM |
| Net PAT YoY (C / S) | −96.7% / −97.3% | −96.7% / −97.3% | C25; ADDM 1113 | CONFIRM |
| 4B: disc-ops = % of reported-net decline | 99.2% | 1,172.27/1,182.15 = 99.16% | C24/C25 311-312 | CONFIRM |
| Kukatpally Q1FY26 land gain | Rs 1,390.77 Cr | 19.55 + 1,371.22 = 1,390.77 | Note 3 review 58 | CONFIRM |
| Reported EBITDA row (4 cells) | 57.10/89.30/47.36/42.13 | all tie (PBT+D+Fin) | Step 1 tables | CONFIRM |
| Q4FY26 core PBT ex-OI (Step 3 note) | (12.68) | 63.59 − 76.27 = (12.68) | C13/C3 | CONFIRM |

### 2B. FAILURES (mismatch above rounding — loop to A4)

**FAIL-1 (A4 arithmetic) — Exceptional item Q1FY26 consolidated is wrong; A4's Step 1 table does not foot.**
- A4 uses **Exceptional Q1FY26 = Rs 42.20 Cr** (= 4,220.09 lakh) at review lines 57, 98, 170, 238.
- A4's own Step 1 consol table: PBT-before-exceptional 50.78 (line 97) + Exceptional 42.20 (line 98) = **92.98**, but the table's PBT continuing = **62.98** (line 99). A 30.00 Cr break, uncaught.
- True value: render-verified PBT-before-exceptional = 5,078.01 (ADDM line 1123) and PBT = 6,298.10 (C15 302, cross-confirmed at segment D16 line 155) force exceptional = 6,298.10 − 5,078.01 = **1,220.09 lakh = Rs 12.20 Cr**. This is exactly the Note 2 put-option value A4 itself quotes ("1,220.09", review line 57) but then mis-converts to 42.20 (should be 12.20). Every other period foots on this identity (Q1FY27 5,272.66+351.65=5,624.31; Q4FY26 6,359.30−209.83=6,149.47; FY26 33,350.70+1,300.43=34,651.13); only Q1FY26 was corrupt (cmap 1→4).
- Discrepancy: **A4 = Rs 42.20 Cr | recomputed = Rs 12.20 Cr | source = ADDM 1123 (5,078.01) + C15 line 302 (6,298.10) + Note 2 (1,220.09).**
- Cascade (all must be re-derived on Rs 12.20 Cr): Step 2A "Exceptional −91.7%" should be 12.20→3.52 = **−71.1%** (review line 170); Step 4A "Exceptional change (38.68)" should be 3.52−12.20 = **(8.68)** (review line 238).

**FAIL-2 (A4 arithmetic) — Operating EBITDA (ex-OI) Q1FY26 consolidated is mis-stated; the PAT bridge double-counts finance and does not foot.**
- A4's Step 1.3 states Operating EBITDA (ex-OI) Q1FY26 C = **(32.32)** (review line 141), by the stated formula "PBT-ex-exceptional + D + Fin − Other Income".
- Recompute: 50.78 + 0.53 + **25.79** + ... − 83.10 = **(6.00)**. A4 omitted the Rs 25.79 Cr finance add-back exactly where it is largest and copied in the Core-PBT-ex-OI value (32.32) instead. Standalone Q1FY26 (−5.33) and both Q1FY27 cells (−5.25 / −5.19) DO add finance and tie — only consol Q1FY26 is wrong.
- Discrepancy: **A4 = (32.32) | recomputed = (6.00) | source = C13 300 (50.78) + C10 297 (0.53) + C9 296 (25.79) − C3 290 (83.10).**
- Cascade: Step 2A "Operating EBITDA (ex-OI) (32.32)→(5.25) loss narrowed" (line 164) and Step 2 diagnostic #2 (line 191) overstate the narrowing; Step 4A's "Operating cost/other-expense change +26.17 favourable — Op EBITDA loss narrowed (32.32)→(5.25)" (line 234) is derived off the bad (32.32) and **double-counts the Rs 25.79 Cr finance-cost collapse** (also booked separately as "+25.79" on line 236). A4's stated bridge components sum to −10.41 Cr, but A4 asserts pre-tax net change (6.74) (line 239) — the bridge does not foot. Correct pre-tax bridge: PBT-before-exceptional +1.95 (50.78→52.73), exceptional (8.68) → net (6.74); the "+26.17 operating-cost" line is spurious (true ex-finance operating-expense change is ~(0.78) unfavourable).

**Note:** FAIL-1 and FAIL-2 do not overturn the top-line YoY figures (PAT continuing 53.72→43.85 = −18.4%, net −96.7%, all CONFIRMED in 2A) nor the qualitative "no core operating profit" thesis, which survives on either reading. But they are mismatches well above rounding inside A4's derived tables, and the Step 1 consolidated table visibly fails to foot — a hard FAIL under the arithmetic gate.

**AR-1 (A2 enumeration gap, secondary):** the A2 ledger carried C14 Q1FY26 = 4,220.09 with no flag despite the C13+C14≠C15 break and the Note 2 conflict; the A1-ADDENDUM did not render-adjudicate C14. On the fix loop, A2 must raise NUMBER_DISCREPANCY on C14 Q1FY26 and A1 must add the render read (1,220.09) so A4 is not re-seeded with the corrupt value.

---

## 3. ADVERSARIAL READ (three most-positive claims + strongest bear counter from the same extract)

| # | A4's positive claim | Strongest bear counter from the same extracted text | Survives? | Already in A4? |
|---|---|---|---|---|
| 1 | Finance cost collapsed −100% (Rs 25.79→0.004 Cr) = deleveraging; unallocable liab −60% (review 166, 490) | Same segment data is AMBIGUOUS: net debt is ND at Q1 (Step 5), the −60% could be WC unwind not repayment, and the HNPCL merger — merely deferred, on NCLAT appeal (ADDM item 8) — would re-import ~Rs 6,400 Cr debt if reversed. "Deleveraging" is neither confirmed nor durable. | YES | YES — Step 5 ambiguity, Q6, tripwire #3 AMBER. No new graft. |
| 2 | NCLT declined HNPCL merger Jul-30-2026 = removes ~Rs 6,400 Cr debt overhang (thesis-positive deferral) (review 336, 374, 483) | Only DEFERRED: Company is appealing to NCLAT and NCLT made unspecified "certain observations" (ADDM line 1105); the APTEL ~Rs 2,000 Cr disallowance and LPSC-contaminated economics ride in if reversed. A refusal on the operator's own scheme is also a governance signal, not only a reprieve. | YES | YES — Q3, Q11, tripwire #3, brief sector block. No new graft. |
| 3 | Continuing PAT "roughly flat"; standalone continuing PAT +7.5% YoY (review 183-184, 187) | From the same rows: continuing "profit" is 100% treasury/other income (OI 105-132% of continuing PBT), core operating PBT negative both years, and the standalone +7.5% is entirely higher Other Income (47.46→52.55) on a cash pile that depletes as land/ICD dynamics run — not operating strength. | YES | YES — FND-F2, Step 1.3 read, Q5, brief business-model block. No new graft. |

**Result:** all three bear counters survive but every one is **already incorporated** in A4's review. **No unincorporated surviving bear counter** requires grafting. The adversarial-read completeness device passes.

### Adversarial protocol checks (task-directed)
- **All FORWARD-SIGNAL / AMBIGUOUS A3 findings → ≥1 question:** YES. FND-F2→Q5; F3→Q13; F4→Q4/Q13; F5→Q1/Q2/Q10; F6→Q8; F7→Q10; F8→Q9; F12→Q6/Q7; F15→Q3. All nine mapped (review 387-401).
- **Two silent tripwires carried as questions:** YES — #1 APTEL Appeal 743/2023 → Q11; #6 Swiss promoter conviction → Q12 (review 399-400), also in Role-5 silence list (463-464).
- **Verdict consistency with house rules:** PROCEED WITH FLAGS is valid (no STOP used). INDETERMINATE cash conversion is explicitly capped at PROCEED WITH CAVEATS with missing evidence named (CFO/WC/net debt, deferred to Q2FY27) and then pushed one notch MORE conservative to FLAGS on governance — consistent (FLAGS is more conservative than CAVEATS in the set; the cap is a ceiling, not a floor). Low institutional ownership is NOT treated as a risk; the institutional-vote-against is handled as an RPT governance/disclosure gap, not an ownership penalty. Flags propagate; no halt on quality. All consistent.
- **Flag-not-decide / exit-framing-only / no momentum→value conversion:** YES — HELD (momentum, Chandelier-governed) preserved; review states "informs EXIT FRAMING only" and explicitly refuses conversion to a value position (review 41, 369, 371, 437).
- **No estimated numbers; NOT FOUND / ND is the only fill:** YES for disclosed items — ND used correctly for CFO/BS/net-debt (Q1, Reg 33 half-yearly) and for the un-passed Bear/Base/Bull grid. The one derived value (consol Q1FY26 Total income 8,649.63) is arithmetically derived from two independent render-verified checks and flagged, not estimated — acceptable. (The Rs 42.20 exceptional is not an estimate; it is a mis-read of a corrupt cell — captured as FAIL-1, not an estimation breach.)

---

## 4. VERDICT

**INCOMPLETE.**

- **Primary loop-back: A4.** Two arithmetic failures inside A4's derived tables:
  1. Exceptional item Q1FY26 consolidated must be **Rs 12.20 Cr (1,220.09 lakh)**, not Rs 42.20 Cr; A4's Step 1 consol table does not foot (50.78 + 42.20 ≠ 62.98). Re-derive Step 2A exceptional YoY (−71.1%, not −91.7%) and Step 4A exceptional change ((8.68), not (38.68)).
  2. Operating EBITDA (ex-OI) Q1FY26 consolidated must be **(6.00)**, not (32.32) (finance add-back of Rs 25.79 Cr omitted); the Step 4A PAT bridge double-counts the finance-cost collapse and does not foot to the stated (6.74) — rebuild it.
- **Secondary loop-back: A2 (with A1-ADDENDUM).** Flag C14 Q1FY26 as NUMBER_DISCREPANCY and render-adjudicate it to 1,220.09, so the fix is not re-seeded with the corrupt 4,220.09.

The DELIVERABLE gate PASSES, coverage PASSES, the adversarial read PASSES with no unincorporated survivor, and the verdict/framing discipline is sound. The single blocking issue is the arithmetic cluster above. Only COMPLETE proceeds to Notion save; this run must loop to A4 (then A2) first.

```yaml
stage: A5-adversary
company: "goclcorp"
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
  missing_from_ledger:
    - "C14 exceptional-items Q1FY26 consol = 4,220.09 carried UNFLAGGED; contradicts C13+C14=C15 identity and Note 2 (1,220.09) — A2 missed NUMBER_DISCREPANCY, A1-ADDENDUM did not adjudicate C14"
arithmetic_mismatches:
  - metric: "Exceptional items Q1FY26 consolidated (Rs Cr)"
    a4_value: "42.20"
    recomputed: "12.20"
    source_line: "ADDM 1123 (PBT-ex-exceptional 5,078.01) + C15 line 302 (PBT 6,298.10) + Note 2 review line 57 (1,220.09); A4 Step 1 table lines 97-99 do not foot (50.78+42.20 != 62.98)"
  - metric: "Operating EBITDA ex-OI Q1FY26 consolidated (Rs Cr)"
    a4_value: "(32.32)"
    recomputed: "(6.00)"
    source_line: "C13 line 300 (50.78) + C10 line 297 (0.53) + C9 line 296 (25.79) - C3 line 290 (83.10); finance add-back omitted; propagates to Step 4A bridge (double-counts finance, does not foot)"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "A4 arithmetic: (1) exceptional item Q1FY26 consol must be Rs 12.20 Cr (1,220.09 lakh) not Rs 42.20 Cr — Step 1 consol table fails to foot (50.78+42.20!=62.98); re-derive Step 2A exceptional YoY (-71.1%) and Step 4A exceptional change (8.68). (2) Operating EBITDA ex-OI Q1FY26 consol must be (6.00) not (32.32) — Rs 25.79 Cr finance add-back omitted; Step 4A PAT bridge double-counts the finance collapse and does not foot to (6.74). Secondary: A2 must flag C14 Q1FY26 as NUMBER_DISCREPANCY and A1-ADDENDUM must render-adjudicate it to 1,220.09 so the fix is not re-seeded with the corrupt 4,220.09."
```
