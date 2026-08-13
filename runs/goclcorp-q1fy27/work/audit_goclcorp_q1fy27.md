# A5 ADVERSARY / COMPLETENESS RE-AUDIT — GOCL Corporation Ltd, Q1 FY27 (loop 1, post-correction)
### Target: review_goclcorp_q1fy27.md (A4) · Evidence spine: extract_results_goclcorp_q1fy27.txt (A1 + A1-ADDENDUM + A1-ADDENDUM CORRECTION) · Ledger: ledger_results_goclcorp_q1fy27.md (A2, C14 resolved)
### Independence: re-derived from the extract lines directly; A4/A3 cites checked, not trusted. Units Rs Lakhs (x0.01 = Rs Cr).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF (review lines 484-507): all four parts present and non-empty with real content.

| Brief part | Present? | Evidence (review line) | Provenance labels present? |
|---|---|---|---|
| (1) Summary narrative (10-20 lines) | PRESENT | lines 486-487 (single dense para, ~22 lines of content) | n/a |
| (2) SECTOR intelligence | PRESENT | lines 489-493 | yes — [Notion/prior], [Filing Q1FY27] |
| (3) BUSINESS-MODEL intelligence | PRESENT | lines 495-500 | yes — [Filing Q1FY27], [Notion/prior] |
| (4) COMPETITION intelligence | PRESENT | lines 502-506 | yes — [Filing Q1FY27], [Notion/prior] |

Gate result: **PASS.** All four labelled parts present, non-empty, provenance-tagged.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledger, then A4 citation check)

Fresh manual sweep of the extract (all 12 pages + addendum) against the A2 count test:

| Category | A2 count | My fresh count | Basis / cross-check | Orphan/missing rows | Status |
|---|---|---|---|---|---|
| Notes (consol + standalone) | 18 (9+9) | 18 (9+9) | Consol N1-N9 (extract 426-608), Std N1-N9 (extract 903-1075); all 18 mapped in A4 Step 0D table (review 55-65) | none | PASS |
| Auditor paragraphs | 12 (7 consol + 5 std) | 12 (7+5) | Consol paras 1-7 (extract 117-202, incl. EoM para 6 @170-181 + Other Matter para 7 @183-202); Std paras 1-5 (extract 716-773, incl. EoM para 5 @761-773) | none | PASS |
| Both Emphasis-of-Matter + Other Matter | 3 | 3 | Consol EoM (169-181), Consol Other Matter (183-202), Std EoM (761-773); all in A4 review lines 68-69 | none | PASS |
| Segment leaf rows | 26 | 26 | Section D income 8 + results 8 + assets 5 + liabilities 5 (D2-D30 less 4 headers) | none | PASS |
| Line items (all tables) | 94 | 94 | 30 consol P&L + 26 consol segment + 5 consol disc-ops + 28 std P&L + 5 std disc-ops | none | PASS |
| Discontinued-ops sub-tables | 2 (E-D, H-D, 5 rows each) | 2 | extract 502-506 (consol), 1069-1073 (std); A4 uses in Step 1/2C/4B | none | PASS |
| Board agenda items | 1 | 1 | extract 76-78 (single combined resolution) | none | PASS |
| Entities | 2 | 2 | GOCL + HGHL Holdings UK (extract 144-146); HGHL Other-Matter carried as FND-F4/Q4 | none | PASS |
| Signatures | 5 | 5 | Satyanarayana CS (88-93), Snehal Shah consol (212-217) + std (785-790), Ravi Jain consol notes (609-619) + std notes (1076-1082) | none | PASS |

**Ledger flag-row disposition (every A2 NUMBER_DISCREPANCY / OCR_ROW_MISSING re-checked as resolved, not orphaned):**
All 9 NUMBER_DISCREPANCY cells + C14 confirmed resolved by the addendum and A4 uses the correct value in each case: C12→3,571.62 (ADDM 1); C14→1,220.09 (ADDM-CORR); C22→1,36,241.10 (ADDM 2); C34→991.45 (ADDM 3); C38→8.15 (ADDM 4); E-N5 date July-20/July-30 conflict→July 30 (ADDM 8); E-N7 advance 400/100→Rs 100 lakh (ADDM 9); G0 header→Mar-31-2026 (ADDM 10); G4→28,375.04 (ADDM 11); G10→237.70 (ADDM 12); G34→291.66 (ADDM 18). No orphan ledger row: every row is either cited in A4 or covered by the reconciliation preamble (review 15-27) / extraction-fidelity note (review 31).

**Coverage verdict: PASS — no orphan row (→A3), no row my fresh pass found that the ledger lacks (→A2).**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract lines; A4 cite verified each time)

All confirmations independent. "src" = extract line(s).

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Consol Q1FY26 exceptional item | 12.20 Cr | 1,220.09 lakh; 5,078.01+1,220.09=6,298.10=PBT; = Note 2 put-option | 435/478/1131 | CONFIRM |
| Consol Step-1 footing (PBTbx+exc=PBT), all 4 cols | ties | Q1FY27 5,272.66+351.65=5,624.31; Q4 6,359.30−209.83=6,149.47; Q1FY26 5,078.01+1,220.09=6,298.10; FY26 33,350.70+1,300.43=34,651.13 | 300-302 | CONFIRM |
| Step 2A exceptional YoY | −71.1% | (3.52−12.20)/12.20 = −71.1% | derived | CONFIRM |
| Step 4A exceptional change | (8.68) | 3.52−12.20 = −8.68 | derived | CONFIRM |
| Op EBITDA ex-OI Q1FY26 consol | (6.00) | 50.78+0.53+25.79−83.10 = −6.00 | 300/297/296/290 | CONFIRM |
| Op EBITDA ex-OI Q1FY27 consol | (5.25) | 52.73+0.86+0.004−58.84 = −5.25 | 300/297/296/290 | CONFIRM |
| Op EBITDA ex-OI Q1FY26 std | (5.33) | 41.33+0.53+0.27−47.46 = −5.33 | 872/818/817/811 | CONFIRM |
| Op EBITDA ex-OI Q1FY27 std | (5.19) | 46.50+0.86+0.004−52.55 = −5.19 | 821/818/817/811 | CONFIRM |
| Step 4A PAT bridge footing | −9.87 | +0.90−0.15−0.33+25.79−24.26=+1.95; 1.95−8.68=−6.73; −3.13 → −9.87 (=53.72→43.85) | 307/289/etc | CONFIRM |
| S-vs-C net-PAT gap Q1FY27 | +25.8% | (4,039.87−3,210.77)/3,210.77 = +25.8% (Δ829.10 ≈ HGHL PAT 829.11) | 312/831/185 | CONFIRM |
| S-vs-C gap Q4FY26 | −1.4% | (7,514.67−7,619.60)/7,619.60 = −1.4% | 312/831 | CONFIRM |
| S-vs-C gap Q1FY26 | +1.3% | (1,22,254.53−1,20,699.63)/1,20,699.63 = +1.3% | 312/831 | CONFIRM |
| S-vs-C gap FY26 | +5.3% | (1,52,194.70−1,44,584.54)/1,44,584.54 = +5.3% | 312/831 | CONFIRM |
| ETR consol Q1FY27 / Q1FY26 | 22.0% / 14.7% | 1,239.11/5,624.31=22.0%; 925.62/6,298.10=14.7% | 306/302 | CONFIRM |
| ETR std Q1FY27 / Q1FY26 | 23.5% / 20.0% | 1,094.37/4,650.47=23.5%; 825.31/4,132.77=20.0% | 825/821 | CONFIRM |
| Deferred-tax shield (this Q, consol) | ~134 bps | 75.63/5,624.31 = 1.345% = 134 bps | 305/302 | CONFIRM |
| Unallocable assets % of total | 93.8% | 3,37,109.48/3,59,411.21 = 93.8% | 408/1103 | CONFIRM |
| Unallocable assets YoY | −3.2% | (3,37,109.48−3,48,271.57)/3,48,271.57 = −3.2% | 408 | CONFIRM |
| Unallocable liabilities YoY | −60.2% | (38,877.36−97,607.13)/97,607.13 = −60.2% | 413 | CONFIRM |
| Total liabilities YoY | −64.7% | (41,254.30−1,17,024.89)/1,17,024.89 = −64.7% | 1104 | CONFIRM |
| Disc held-for-sale assets QoQ | +33.9% | (7,838.55−5,854.22)/5,854.22 = +33.9% | 409 | CONFIRM |
| Other-income/PBT consol Q1FY27 / Q1FY26 | 105% / 132% | 58.84/56.24=105%; 83.10/62.98=132% | 290/302 | CONFIRM |
| Other-income/PBT std Q1FY27 / Q1FY26 | 113% / 115% | 52.55/46.50=113%; 47.46/41.33=115% | 862/821 | CONFIRM |
| Corrected consol Q1FY26 Total income | 86.50 Cr | 339.18+8,310.45=8,649.63; 5,078.01+3,571.62=8,649.63 (refutes 8,849.63) | 289/290/1133 | CONFIRM |
| Core PBT ex-OI (all 4) | (6.11)/(32.32)/(6.05)/(6.13) | 52.73−58.84; 50.78−83.10; 46.50−52.55; 41.33−47.46 | tables | CONFIRM |
| PAT-margin-on-rev (4) | 1023/1584/829/976% | 43.85/4.29; 53.72/3.39; 35.56/4.29; 33.07/3.39 | 307/861 | CONFIRM |
| Reported-net YoY consol / std | −96.7% / −97.3% | −1,182.15/1,222.55; −1,174.88/1,206.99 | 312/831 | CONFIRM |
| 4B disc-ops share of net decline | 99.2% | −1,172.27 / −1,182.15 = 99.2% | 311 | CONFIRM |
| Kukatpally one-off in base | 1,390.77 Cr | 1,955.18 + 1,37,121.69 lakh = 19.55+1,371.22 Cr | 485-486 | CONFIRM |
| EPS internal consistency (share count) | 8.15/6.47 etc | 4,039.87 lakh / 495.725 lakh sh = 8.15; 3,210.77/495.725 = 6.47 | 312/831/321 | CONFIRM |

Every derived metric recomputes to A4's value within rounding. **No arithmetic FAIL.**

Rounding note (immaterial, not a FAIL): D&A YoY is stated +62.3% (from 2-dp Cr 0.86/0.53); from raw lakhs (86.39/53.10) it is +62.7%. A4 itself flags the line as immaterial (Rs 0.33 Cr absolute). Within Cr-rounding tolerance.

### ADVISORY fidelity notes (raw extracted cells, NOT derived metrics; non-propagating; not verdict-blocking)
Two raw-cell values are internally inconsistent in the source, resolvable, and touched by neither the A1-ADDENDUM nor A4's derived outputs. They change no ratio, bridge, footing-as-presented, narrative, flag, or verdict. Recorded for fidelity; recommend A4/A1 correct the display cells at save:

1. **Consol Q1FY26 change-in-inventories** shows 0.03 Cr (review line 91) / 3.00 lakh (ledger C7). The render-adjudicated consol Total expenses 3,571.62 (ADDM item 1) foots ONLY with 35.00 lakh: 54.26+35.00+160.71+2,578.84+53.10+689.71 = 3,571.62 (vs 3,539.62 at 3.00; delta exactly 32.00). The standalone twin is 35.00 (extract 866). Correct value = **0.35 Cr (35.00 lakh)**; the "3.00" is a cmap digit-drop of "35.00". Non-propagating because A4 anchored Total expenses and PBT-before-exceptional (50.78) to the render value, both of which are correct.
2. **Consol segment Total income Q1FY26** (ledger D5/D7) reads 6,649.63, but its own components sum to 8,649.63 (174.76+2,123.55+6,351.32) and the P&L Total income is 8,649.63. The 6,649.63 is an 8→6 misread. A4 derives nothing from segment total income, so no output is affected.

Neither meets the arithmetic-FAIL trigger (which is scoped to *derived metrics*) nor the coverage-FAIL trigger (missing/orphan *rows*). Both are resolvable from the extract (not "genuinely unresolvable"), so no conservative-bias FAIL is warranted. Flagged transparently so a wrong display cell is not carried to Notion silently.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive A4 claims; strongest bear from the same text)

| # | Most-positive A4 claim | Strongest bear counter (same extract) | Already in A4? | Survives → graft? |
|---|---|---|---|---|
| 1 | Finance-cost collapse +25.79 Cr framed "recurring/structural (post-deleverage)" — the single largest favourable bridge swing (review 242, 250, 498) | The −60% unallocable-liability fall is AMBIGUOUS (debt repay vs WC unwind); net debt is ND at Q1; and NCLAT reversal would re-import ~Rs 6,400 Cr of HNPCL debt, so "deleveraged" is conditional | YES — Step 5 Q6 (review 401), Step 4B (258), tripwire #3 AMBER (319) | Does NOT survive — fully carried |
| 2 | NCLT refusal of HNPCL merger "keeps ~Rs 6,400 Cr debt out — thesis-positive deferral" (review 381, 491) | Only a deferral, on NCLAT appeal; NCLT made unspecified "certain observations"; the silent APTEL ~Rs 2,000 Cr disallowance would still ride in via the merger | YES — Step 6D "DELAYED/WEAKENED" (343), Q3 (398), Q11 (406), tripwire #3 "not dead" (319) | Does NOT survive — fully carried |
| 3 | Continuing PAT "roughly flat"; standalone continuing PAT +7.5% (review 187, 191) | Continuing "profit" is 105-132% Other Income; Op EBITDA ex-OI negative every period both bases; ex-treasury the entity loses money — an operating profit does not exist | YES — Step 1.3 (143-153), diagnostic 3 (196), Step 4B (257) | Does NOT survive — fully carried |

No bear counter survives; each strongest bear is already surfaced in A4. Nothing to graft.

### Adversarial protocol checks (task-mandated)
- FORWARD-SIGNAL / AMBIGUOUS forensics → question rows: FND-F2 (Q5), F4 (Q4/Q13), F5 (Q1/Q2/Q10), F6 (Q8), F7 (Q10), F8 (Q9), F12 (Q6/Q7), F15 (Q3), F3 (Q13) — all covered (review 394-408). **PASS.**
- Both silent tripwires carried as questions: APTEL 743/2023 → Q11; Swiss promoter conviction → Q12 (review 406-407). **PASS.**
- Verdict vs house rules: PROCEED WITH FLAGS is in the permitted set; no STOP verdict used. INDETERMINATE cash conversion caps at PROCEED WITH CAVEATS with missing evidence named (CFO/WC/net debt, deferred to Q2FY27), then A4 goes one notch more conservative to PROCEED WITH FLAGS on governance — never silently resolved to PROCEED (review 288, 442-443). Flags propagate (14-flag YAML register). Low institutional ownership NOT treated as a risk; the 75.66%-against RPT vote is treated as a governance/transparency flag (distinct concept), not as an ownership-level penalty. **PASS.**
- "Flag, do not decide" / "informs exit framing only" / no momentum→value conversion: held throughout (review 41, 376, 378, 444). **PASS.**
- No estimated number: ND is the only fill for missing data; the two loop-1 corrections are render-adjudicated (ADDM-CORR lines 1131-1133), and Total income 8,649.63 is double-arithmetic-confirmed AND render-read, not estimated. **PASS.**

---

## VERDICT

**COMPLETE.**

- Deliverable gate: PASS (all four brief parts present, provenance-labelled).
- Coverage: PASS (18 notes, 12 auditor paras incl. both EoM + Other Matter, 26 segment rows, 2 disc-ops tables, board outcome, 2 entities, 5 signatures — no orphan, no ledger gap).
- Arithmetic: every derived metric independently recomputed and CONFIRMED, including all seven previously-disputed cells (Q1FY26 exceptional, Step-1 footing, Step 2A exceptional YoY, Step 4A exceptional change, Op EBITDA ex-OI Q1FY26, PAT-bridge footing, corrected Total income). No mismatch above rounding in any derived figure.
- Adversarial: no surviving bear counter (all three strongest bears already in A4); every FORWARD-SIGNAL/AMBIGUOUS forensic and both silent tripwires carried as questions; verdict consistent with house rules; no estimation.
- Two ADVISORY raw-cell fidelity notes (consol Q1FY26 change-in-inventories display 0.03→should be 0.35; consol segment Total income Q1FY26 6,649.63→8,649.63) are resolvable, non-propagating, and touch no derived metric or conclusion. They do NOT meet a FAIL trigger and do NOT block save. Recommended non-blocking correction: A4 fix the Step 1.1 display cell (0.35) at Notion save for internal footing consistency.

Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "goclcorp"
quarter: "q1fy27"
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
advisory_fidelity_notes:
  - {cell: "consol Q1FY26 change-in-inventories", a4_value: "0.03 Cr", correct: "0.35 Cr", basis: "render total expenses 3,571.62 foots only with 35.00 lakh; standalone twin = 35.00 (extract 866)", propagates: "none", action: "non-blocking display fix by A4"}
  - {cell: "consol segment Total income Q1FY26 (ledger D5/D7)", a4_value: "6,649.63 lakh", correct: "8,649.63 lakh", basis: "components sum 8,649.63; P&L Total income 8,649.63; 8->6 misread", propagates: "none (A4 derives nothing from it)", action: "informational"}
loop_back_to: ""
gap: ""
```
