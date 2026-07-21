# A5 ADVERSARY / COMPLETENESS AUDIT — SOUTHWEST — Q1 FY27 (re-audit, loop 3)

Agent A5. Fresh context: A4 review + the two A1 extracts + the two A2 ledgers only. Every number re-derived independently (Rs Mn x0.1 to Rs Cr per A1 headers). A4's and A3's cites checked, not trusted. This pass is a re-audit after A4's second loop-back, which was supposed to close the three gaps my prior audit raised: (1) orphan Oil India 2D/3D seismic empanelment row, (2) JV-recurrence bear counter, (3) ROCE label inconsistency. Each is verified below, then the review is re-attacked fresh.

---

## PRIOR-LOOP CLOSURE CHECK

| Prior gap | Where it now lives in A4 | Re-check | Verdict |
|---|---|---|---|
| Orphan OIL 2D/3D empanelment (F6.7) | 6B item 12 (L282), 6D (L305), Step 6 verdict (L325), Q18 (L402), monitorable (L454/L513), flag (L528); sourced results E8 L102-103 + pres sl.32 L1011-1012 — both confirmed in extracts | Now carried as forward enabler/monitorable/question, not banked as a booked order | **CLOSED — properly grafted** |
| JV-recurrence counter (F8.1) | Step 4 JV-normalisation flag (L195), First-Class Metric (L211), Step 2 diag-3 carve-out (L142), Q16 (L400), Caveat 7 (L439), flag (L526) | Q1 JV 13 vs FY26 14 Mn; 13/93=14.0% ✓; +333% ✓; normalise ~3.5 Mn → PAT 93→83.5 Mn=8.4 Cr (−10.2%) ✓; margin 83.5/617=13.5%≈13.6% ✓ | **CLOSED — grafted, math correct** |
| ROCE label inconsistency (F16.4) | Step 7 pillar row (L335), Q12 (L396), Caveat 8 (L440), flag (L527) | 0.5×16+7.5=15.5x ✓; 0.5×23+7.5=19x ✓ (deck 16% panel vs 23% snapshot, L1165/L1170) | **CLOSED — grafted, math correct** |

All three prior gaps are properly incorporated with correct sourcing and arithmetic. The F16.2 order-book double-count (Step 6E) was carried forward unchanged and is re-verified in Audit 3. Re-attack proceeds fresh.

---

## AUDIT 1 — COVERAGE

Independent grep/manual re-enumeration of both extracts, diffed against the two A2 ledgers.

| Category | A2 count | My fresh count | Orphan / note | Status |
|---|---|---|---|---|
| Results: numbered notes | 0 | 0 (`^\s*[0-9]+\.\s`=0; 4-page release, not Reg 33) | — | PASS |
| Results: financial line items (L86-90) | 5 | 5 | — | PASS |
| Results: financial period cells (5×4) | 20 | 20 | — | PASS |
| Results: table footnote (L91) | 1 | 1 | — | PASS |
| Results: Q1 highlight bullets (L93-111) | 13 | 13 | E8 OIL empanelment now cited in A4 (closed) | PASS |
| Results: CMD commentary claims (L115-148) | 9 | 9 | — | PASS |
| Results: JV/coal statements | 7 | 7 | — | PASS |
| Results: absent Reg-33 units (K1-K15) | 15 | 15 | carried as first-class ND in A4 0D | PASS |
| Results: letterhead/addressee/sig/about/contact | 11 | 11 | J2 phone-digit typo immaterial | PASS |
| Presentation: slides | 40 | 40 | — | PASS |
| Presentation: line items (16+16+42+6) | 80 | 80 | sl.36 42 = 22 asset + 20 eq/liab | PASS |
| Presentation: chart data points | 110 | 110 (8+8+6+11+25+6+12+32+2) | — | PASS |
| Presentation: footnotes | 7 | 7 | — | PASS |
| Presentation: ZERO_STANDING | 7 | 7 | OCI→F9.1, held-for-sale→F1.1, Curr-Tax-Liab→F1.2, CWIP→Step 5; NCI & Loans template-nil (reviewed, no finding) | PASS |
| Presentation: Ritolia DISCLOSURE_INCONSISTENCY | 1 | 1 | F14.1 / Q15 | PASS |

**No row my fresh pass found is missing from either ledger → no FAIL to A2.** No orphan ledger row is absent from A4 → no FAIL to A3.

**Ledger-flag → A4 disposition spot-check** (all cited):
- TITLE_LABEL_MISMATCH "Q on Q" vs "Y on Y" → F14-01 / Step 3 / Q14. ✓
- F2 standalone "on similar lines" → First-Class Metric / Q4. ✓
- Slide-6 Rs 307 cr HZL vs slide-32 Rs 3,070 Mn Rajasthan → F16.2 / Step 6E (A4 correctly overrides the ledger "do not conflate" note). ✓
- Slide-37 DATA_GAP (no Q1 net-worth/D-E/ROE-ROCE) → F16.1 / Q12. ✓
- OCI swing / Current Tax Liability / held-for-sale → F9.1 / F1.2 / F1.1. ✓

**Minor unaddressed cross-check (NOT elevated to FAIL):** the A2 pres-ledger slide-9 row flags a benign cross-check — the geographical map shows ~14 state labels vs "20 Operations across 8 States" (sl.32). A4 reviews slide 9 (geographical presence) but does not explicitly reconcile the count. It carries no forensic or financial content (all-time footprint map vs current-quarter operating-state count; the ledger itself supplies the benign resolution). Logged reviewed-benign; does not rise to an orphan-row FAIL.

**COVERAGE VERDICT: PASS.** 70/70 results rows and 40 slides / 80 line items / 110 data points / 7 footnotes reconcile exactly. No orphans; nothing found that the ledgers lack. All three prior loop-2 grafts confirmed present.

---

## AUDIT 2 — ARITHMETIC

Every derived cell recomputed from raw extract numbers (sl.33 L1031-63; sl.35 L1074-106; sl.36 L1112-42; sl.38 L1199-210). Load-bearing cells shown; all others reconcile to rounding.

| Metric | A4 value | My recompute | Source | Status |
|---|---|---|---|---|
| Total Income Q1FY27 (Rev+OI) | 62.1 | 61.7+0.4=62.1 | L1033/41 | OK |
| Op EBITDA Q1FY27 (Rev−TotExp) | 14.9 | 61.7−46.8=14.9 | L1033/35 | OK |
| Op EBITDA margin Q1FY27 | 24.15% | 149/617 | L1037/33 | OK |
| Op EBITDA margin Q1FY26 | 14.43% | 58/402 | L1035/33 | OK |
| Reported EBITDA Q1FY27 (PBT+D+Fin) | 16.6 | 11.9+3.0+1.7 | L1051/43/45 | OK |
| Core Op PBT ex-OI Q1FY27 | 11.5 | 11.9−0.4 | L1051/41 | OK |
| Core Op PBT ex-OI ex-JV Q1FY27 | 10.2 | 10.6−0.4 | L1047/41 | OK |
| Effective tax rate Q1FY27 (Tax/PBT) | 21.8% | 26/119=21.85% | L1053/51 | OK |
| ETR pre-JV Q1FY27 (Tax/PBSJV) | 24.5% | 26/106=24.53% | L1053/47 | OK |
| Revenue YoY | +53.5% | (617−402)/402=53.48% | L1033 | OK |
| Op EBITDA YoY | +156.9% | (149−58)/58 | L1037 | OK |
| EBITDA margin bps YoY | +972 | 2415−1443 | L1039 | OK |
| Depreciation YoY | +42.9% | (30−21)/21=42.86% | L1043 | OK |
| Finance cost YoY | −15.0% | (17−20)/20 | L1045 | OK |
| Operating EBIT YoY | +221.6% | (11.9−3.7)/3.7 | der. | OK |
| Core Op PBT ex-OI YoY | +475% | (11.5−2.0)/2.0 | der. | OK |
| Core ex-OI ex-JV YoY | +500% | (10.2−1.7)/1.7 | der. | OK |
| Reported PBT YoY | +283.9% | (119−31)/31 | L1051 | OK |
| PAT YoY | +287.5% | (93−24)/24 | L1055 | OK |
| PAT margin bps YoY | +910 | 1507−597 | L1057 | OK |
| EPS YoY | +287.3% | (3.06−0.79)/0.79 | L1063 | OK |
| PAT bridge: Op EBITDA Δ | +9.1 | 14.9−5.8 | L1037 | OK |
| PAT bridge: PBSJV Δ | +7.8 | 10.6−2.8 | L1047 | OK |
| PAT bridge: JV Δ | +1.0 | 1.3−0.3 | L1049 | OK |
| PAT bridge: = PBT change | +8.8 | 7.8+1.0; also 11.9−3.1 | L1051 | OK |
| PAT bridge: Tax Δ | −1.9 | 2.6−0.7 | L1053 | OK |
| PAT bridge: = reported PAT change | +6.9 | 8.8−1.9; also 9.3−2.4 | L1055 | OK |
| JV share of consolidated PAT | 14.0% | 13/93=13.98% | L1049/55 | OK |
| JV normalise → PAT / margin | ~8.4 / ~13.6% | 93−9.5=83.5 Mn; 83.5/617=13.5% | L1092 | OK |
| Receivable days FY25 | 154.5 | 763/1803×365 | L1132/76 | OK |
| Receivable days FY26 | 175.0 | 1166/2430×365=175.1 | L1132/76 | OK |
| Inventory days FY26 | 100.6 | 509/1847×365 | L1129/78 | OK |
| Payable days FY26 | 45.9 | 232/1847×365 | L1133/78 | OK |
| Cash conversion cycle FY26 | ~230 | 175.0+100.6−45.9=229.7 | der. | OK |
| Capex FY26 (PPE+CWIP) | 92.2 | 918+4 Mn | L1114-15 | OK |
| Cash & equiv FY25→26 | 19.4→1.3 (−93%) | 194→13, −93.3% | L1134 | OK |
| Gross borrowings FY26 (LT+ST) | 78.6 | 160+626 Mn | L1120/31 | OK |
| Net debt FY26 (gross−cash&equiv) | 77.3 | 78.6−1.3 | der. | OK |
| Order book net QoQ add | +180.1 (+31.0%) | (7613−5812)/10=180.1; /581.2=31.0% | L546 | OK |
| Survey-segment concentration | 59% | 4506/7613=59.2% | sl.17 | OK |
| CBM share of book | 29% | 2222/7613=29.2% | sl.17 | OK |
| Rev step-up FY24→25→26 | +35%/+35% | 46.9/133.4=35.2%; 62.7/180.3=34.8% | L1076 | OK |
| FY26 avg quarterly run-rate | 60.75 | 243.0/4 | der. | OK |
| Q1 annualised (×4) | 246.8 | 61.7×4 | der. | OK |
| ROCE base (0.5×ROCE+7.5) | 15.5x | 0.5×16+7.5 | L1170 | OK |

S-vs-C PAT gap: A4 records ND (both docs consolidated-only, K5) — confirmed unrecoverable from today's extracts, correctly ND not fabricated; JV-share-of-PAT (14.0%) kept distinct from the S-vs-C gap. Correct.

**ARITHMETIC VERDICT: PASS — zero mismatches above rounding.** The PAT bridge closes exactly both ways (+6.9 Cr). Note (not a FAIL; no A4 table affected): the release body's "PAT … more than 3.90 fold" (results L97) is a mild company overstatement (93/24=3.875x); A4 correctly used +287.5% and did not import 3.90. (The narrative run-rate INFERENCE issue in Step 2/3 is treated in Audit 3, not here, because A4's table numbers are all correct — the defect is in prose interpretation, not arithmetic.)

---

## AUDIT 3 — ADVERSARIAL READ

Three most-positive A4 claims, each attacked from the same extracted text.

**Positive claim 1 — "Operating income statement genuinely strong, NOT treasury-led; core ex-OI +475%, ex-JV +500%; ~100%+ of PAT growth recurring/operating" (Step 2 verdict L147; Step 4 L190).**
Strongest same-text counter: the deck-defined "EBITDA" carries no cost-line breakdown (materials/employee/other all ND, K9-K13, A4 L101); the CMD cites "substantial increase in input cost" (L123); the +972 bps margin is measured against a Q1FY26 base (14.43%) far below the FY26 full-year margin, so the expansion is undecomposable; and 14% of PAT sits in the JV line whose recurrence is unconfirmed.
**DOES NOT SURVIVE as new.** A4 already records cost lines ND (L101), carves the JV +Rs1.0 Cr out of the "recurring" claim (Step 4 flag L195), notes the margin also holds at the full-FY26 level (23.99%, recurring FY24→26), and caps the verdict at PROCEED WITH CAVEATS. Fully incorporated.

**Positive claim 2 — "Coal first-production target FY27-28 is EARLIER than the house FY29 tripwire (favourable); no thesis-broken trigger fired" (Step 6C L288; Combined verdict L423).**
Strongest same-text counter: FY27-28 is a management target stated while the GR is only "being finalised for early submission" (sl.22 L682) and mine development "shall be undertaken now" (not yet begun, L143-145). A self-declared pull-forward with the enabling filing unsubmitted is promise-not-delivery; booking it as "favourable/earlier than FY29" credits an unfulfilled promise.
**DOES NOT SURVIVE as new.** A4 logs "binary GR-slip risk" (L300), routes it to Q6 (reaffirm/deny FY27-28 vs FY29), and lists GR submission (end-Jul) and first production as dated monitorables (L450-451). The promise is flagged, not banked.

**Positive claim 3 — "Revenue +53.5% YoY; annualised Q1 (Rs 246.8 Cr) sits at/above the FY26 exit pace; no seasonal air-pocket; consistent with order-book pull-through beginning" (Step 2 diag-1 L140; Step 3 L167).**
Strongest same-text counter: the extract's own arithmetic contradicts the exit-pace / no-air-pocket characterisation. FY26 = Rs 243.0 Cr with Q1FY26 = Rs 40.2 Cr, so the FY26 non-Q1 quarters (Q2-Q4) totalled Rs 202.8 Cr, averaging **~Rs 67.6 Cr/quarter** — Q1FY26 ran at only 66% of that. On the one quarterly data point available, **Q1 is the seasonally weakest quarter.** Therefore:
- Q1FY27 at Rs 61.7 Cr is **BELOW the implied FY26 non-Q1 run-rate (~Rs 67.6 Cr)**, not "at/above the FY26 exit pace" (exit pace = Q4FY26, which is ND but implied ~Rs 67-70 Cr).
- A4's Step-3 test compares Q1FY27 (61.7) to the **blended** FY26 average (60.75) — an average dragged down by the very weak Q1FY26 it also uses for the +53.5% YoY. Comparing to the blended average manufactures "marginally above / no seasonal air-pocket."
- ×4 annualisation of a seasonally-low Q1 (246.8) is an unsound basis for asserting "exit pace." True QoQ vs Q4FY26 is ND.
**SURVIVES.** Extract-supported (pres L1033 Q1FY26 40.2 / Q1FY27 61.7; L1076 FY26 243.0). A4 affirmatively asserts the opposite ("at/above the FY26 exit pace," "no seasonal air-pocket") and this counter is nowhere in A4. A4 cannot use Q1FY26 for its YoY while ignoring what that same data point implies about seasonality; its "one quarter is one data point" caveat does not neutralise the specific unsupported exit-pace assertion. **Must be grafted into A4. → FAIL to A4.**

**Re-verification of the previously-grafted order-book counter (F16.2 / Step 6E):** properly and completely incorporated — appears in 6B item 8, 6C, 6D, 6E, Step 7 (Growth-Visibility premium explicitly NOT credited), Step 8 gate 2, Section C, Caveat 4, flags block, Questions 2 & 8. Re-attacked fresh: net QoQ add Rs 180.1 Cr < the single Rs 307 Cr order (L546); the 3,070 Mn Rajasthan order = the FY25 HZL 307 Cr award (same value, same "single largest" descriptor, same HZL-subsidiary customer, same Rajasthan location; L151-155 vs L1003-1004). Graft holds. No further action.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

- Coverage: PASS (no orphans; 70 results rows / 40 slides / 80 line items / 110 data points reconcile; all three prior loop-2 grafts confirmed present and correctly sourced).
- Arithmetic: PASS (all derived metrics reconcile within rounding; PAT bridge closes exactly).
- Adversarial: one surviving bear counter — the revenue-momentum seasonality/exit-pace counter (claim 3) — is extract-supported and absent from A4; it must be grafted before save.

**Exact gap:** A4 Step 2 diag-1 (L140) and Step 3 (L167) assert Q1FY27 is "at/above the FY26 exit pace" with "no seasonal air-pocket," which the extract's own arithmetic contradicts — FY26 non-Q1 quarters averaged ~Rs 67.6 Cr (243.0 less Q1FY26 40.2, over three quarters) vs Q1FY27's Rs 61.7 Cr, and Q1FY26 (40.2, = 66% of the non-Q1 run-rate) shows Q1 is the seasonally weakest quarter. Graft the seasonality-tempered revenue-momentum bear counter (Q1FY27 below the FY26 non-Q1/exit run-rate; ×4 annualisation overstates; true exit/QoQ pace ND) and align the Step 2 / Step 6 / Combined-verdict "pull-through beginning" language. The verdict floor (PROCEED WITH CAVEATS) is unaffected; this is a completeness graft to a momentum positive.

```yaml
stage: A5-adversary
company: "SOUTHWEST"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "Revenue +53.5% YoY; annualised Q1 (Rs 246.8 Cr) at/above the FY26 exit pace; no seasonal air-pocket; order-book pull-through beginning (A4 Step 2 L140 / Step 3 L167)"
    counter: "Extract arithmetic contradicts the exit-pace claim: FY26 Rs 243.0 Cr less Q1FY26 Rs 40.2 Cr = Rs 202.8 Cr over Q2-Q4 = ~Rs 67.6 Cr/qtr, so Q1FY26 ran at 66% of the non-Q1 run-rate (Q1 is seasonally weakest). Q1FY27 Rs 61.7 Cr is BELOW that ~Rs 67.6 Cr FY26 non-Q1/exit run-rate; A4 compares instead to the blended FY26 average (60.75) that is itself dragged down by the weak Q1FY26 used for the YoY. x4 annualisation of a seasonally-low Q1 overstates momentum; true QoQ vs Q4FY26 is ND. Graft this tempering and align the pull-through language."
    source_line: "presentation L1033 (Q1FY26 402 / Q1FY27 617), L1076 (FY26 2430); A4 L140, L167"
loop_back_to: "A4"
gap: "A4 Step 2 diag-1 (L140) and Step 3 (L167) assert Q1FY27 is 'at/above the FY26 exit pace' with 'no seasonal air-pocket'; the extract's own arithmetic (FY26 non-Q1 avg ~Rs 67.6 Cr > Q1FY27 Rs 61.7 Cr; Q1FY26 Rs 40.2 Cr = seasonally weakest quarter, 66% of non-Q1 run-rate) contradicts this. Graft the surviving seasonality/exit-pace bear counter (Q1FY27 below FY26 non-Q1/exit run-rate; x4 annualisation overstates; true exit/QoQ pace ND) and align Step 2/Step 6/Combined-verdict momentum language before save. The three prior loop-2 gaps (OIL empanelment, JV-recurrence, ROCE label) and the F16.2 order-book counter are verified correctly incorporated; no action there."
```
