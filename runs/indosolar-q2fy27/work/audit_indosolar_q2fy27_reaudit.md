# A5 ADVERSARY RE-AUDIT (correction loop 1): INDOSOLAR Q2 FY27

Company: Indosolar Limited (INDOSOLAR) | Quarter: q2fy27 (quarter ended 30-Sep-2026)
Agent: A5 adversary | Model: claude-opus-5-5 | Run date: 2026-10-23
Scope: bounded re-audit of the A4 loop-1 revision. I checked that prior findings F1, M1 and M2 are closed, confirmed the S1-S10 style fixes, re-derived every new figure, and tested the changed sections for new FACTUAL, MISSING or CONTRADICTION findings. I did not repeat the full first audit (work/audit_indosolar_q2fy27.md).
Status: COMPLETE (all four audits run, bounded). Verdict: **COMPLETE**.

Inputs read: the revised A4 review (work/review_indosolar_q2fy27.md, 642 lines), my prior audit, the A1 results and press-release fulltexts, and the A2 ledger headers. I did not open the source PDF or anything under inputs/. I did not read A3 forensics. A1 and A2 were not in the loop. Their gate lines are unchanged: results 383 of 383 IDs, orphan_ids [] (ledger_results L3, L14); press release 84 of 84, orphan_ids [] (ledger_presentation L14, L17).

Anchor key: "L" = results fulltext line. "PR L" = press-release fulltext line. "A4 L" = revised review line.

---

## AUDIT 0: DELIVERABLE COMPLETENESS (hard gate)

The brief has moved to A4 L501-559 because the revision added lines above it.

| Part | Heading (A4 line) | Status | Check |
|---|---|---|---|
| 1. Summary narrative | "1. SUMMARY NARRATIVE" (A4 L503) | PRESENT | 15 lines (A4 L504-518), inside the 10-20 line band. F1, M1 and M2 text is now in it (A4 L509, L511, L516). |
| 2. Sector intelligence | "2. SECTOR INTELLIGENCE" (A4 L520) | PRESENT | 5 bullets (A4 L521-525). |
| 3. Business-model intelligence | "3. BUSINESS-MODEL INTELLIGENCE" (A4 L527) | PRESENT | 8 bullets (A4 L528-535). |
| 4. Competition intelligence | "4. COMPETITION INTELLIGENCE" (A4 L537) | PRESENT | 6 bullets (A4 L538-543). The net-cash qualifier is now at A4 L539. |
| 5. Forward map | "5. FORWARD MAP" (A4 L545) | PRESENT | 10 catalysts (A4 L550-559), each with a bull fork and a bear fork. The M1 row now carries the method-weight and 89.94 Cr forks. |

Gate result: PASS.

---

## AUDIT 1: COVERAGE (bounded)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results structured IDs in ledger | 383 of 383 (ledger L3) | 383 (unchanged since audit 1; A1 and A2 not in loop) | none | PASS |
| Press-release structured IDs in ledger | 84 of 84 (ledger L17) | 84 (unchanged) | none | PASS |
| Numbered notes cited in A4 | 6 | 6 (A4 L58-63: R371-R376) | none | PASS |
| Footnote-type rows cited in A4 | 4 | 4 (A4 L64-67: R360, R381, R382, R383) | none | PASS |
| Rows at risk of deletion by the revision (sample: R127-R132, R139-R150, R301, R335-R337, R367) | n/a | all still cited (A4 L52, L67, L110, L468, L474) | none | PASS |

The revision only added text. No row citation was removed. The A4 preamble (A4 L33) still states 383 of 383 and 84 of 84, and it matches the ledger gate lines.

The two units that A1 did not enumerate (L287 www.sgco.co.in; the PR L109-110 CEO sentence) are unchanged. They stay STYLE (prior S6) and loop to no agent. A4 still carries PR L109-110 at A4 L522.

---

## AUDIT 2: ARITHMETIC (every figure that is new or changed in the revision)

All values re-derived from the A1 lakh values (x0.01 = Rs Cr).

| Metric (A4 line) | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Q2 FY26 gross profit; gross margin (A4 L188, L206) | 84.68; 41.81% | 20,254.79 - (11,274.75 + 511.61) = 8,468.43 lakh; 41.8095% | L78, L79, L83, L84 | PASS |
| Q2 FY27 gross profit; gross margin | 29.38; 18.89% | 15,558.63 - (23,212.20 - 10,591.83) = 2,938.26 lakh; 18.8851% | L78, L79, L83, L84 | PASS |
| Goods spread Q2 FY26 / Q2 FY27 (A4 L188, L195) | 31.15% / 17.39%; -13.76 pp | 5,331.95 / 17,118.31 = 31.1477%; 2,656.72 / 15,277.09 = 17.3902%; -13.7575 pp | L78, L83, L84 | PASS |
| Counterfactual GM at Q2 FY27 mix (A4 L194) | 32.39% | 0.018095 x 100% + 0.981905 x 31.1477% = 32.3936% | L78, L79 | PASS |
| Mix effect; share (A4 L194) | -9.42 pp; 41% | -9.4159 pp; 41.07% | as above | PASS |
| Goods-spread effect; share (A4 L195) | -13.51 pp; 59% | -13.5085 pp; 58.93% | as above | PASS |
| Total GM fall (A4 L196) | -22.92 pp (components 22.93 on rounding) | -22.9244 pp; 9.42 + 13.51 = 22.93 | as above | PASS |
| Mix and spread in Rs Cr, inside the margin effect (A4 L194-196, L211) | -14.65; -21.02; total -35.67 | 15,558.63 x -9.4159% = -1,464.98 lakh; 15,277.09 x -13.7575% = -2,101.73 lakh; 15,558.63 x -22.9244% = -3,566.71 lakh | L78, L79, L83, L84 | PASS |
| Rupee view of the GP fall (A4 L198, L487) | -55.30 = tolling -28.55 + goods volume -5.73 + goods spread -21.02 | 3,136.48 - 281.54 = 2,854.94; -1,841.22 x 31.1477% = -573.50; -2,101.73; total -5,530.17 lakh | L78, L79 | PASS |
| Bridge consistency | revenue effect -19.63 + mix -14.65 = -34.28 | tolling -28.55 + goods volume -5.73 = -34.28 | A4 L210-211 | PASS |
| Cash and bank; OCL; net of OCL (A4 L251, L263, L511) | 85.42; 89.94; about -4.52 | 8,115.51 + 426.31 = 8,541.82; 8,993.74; -451.92 lakh | L133, L134, L159 | PASS |
| OCL rise; net cash rise (A4 L251, L263, L489) | +81.99; +79.66 | 8,993.74 - 794.51 = 8,199.23; 8,541.82 - 576.27 = 7,965.55 lakh | L133, L134, L159 | PASS |
| Net cash incl. leases (A4 L252) | 2.69 / 82.23; +79.54 | 269.07 / 8,223.25; +7,954.18 lakh | L147, L153 | PASS |
| CF other-liabilities tie (A4 L263, L432) | 86.99 = 81.99 + 2.86 + 2.14 | 8,199.23 + 286.31 + (669.16 - 455.54 = 213.62) = 8,699.16 lakh = L190 | L149, L159, L176, L190, L197 | PASS |
| FY26 PAT per quarter (A4 L388, L486, L516) | 61.65 | 24,659.91 / 4 = 6,164.98 lakh | L97 | PASS |
| FY26 PAT at 25.17% statutory tax; per quarter | 175.32; 43.83 | 23,428.46 x 0.7483 = 17,531.52; / 4 = 4,382.88 lakh | L91 | PASS |
| Earnings-base spread (A4 L388, L486, L516) | 12.3x; 8.7x at statutory tax | 6,164.98 / 501.85 = 12.28x; 4,382.88 / 501.85 = 8.73x | L91, L97 | PASS |
| H2 FY26 services share (A4 L388) | 53.02% | 14,985.23 / 28,262.49 | L78, L79 | PASS |
| Grant / H1 PBT (A4 L432) | 12.35% | 669.16 / 5,418.04 | L91, L176 | PASS |
| S1: core PBT change (A4 L160) | -56.00 | 512.97 - 6,112.57 = -5,599.60 lakh | L80, L91 | PASS (fixed) |
| S1: revenue QoQ (A4 L180, L183) | +127.59% | 15,558.63 / 6,836.14 - 1 | L78, L79 | PASS (fixed) |
| S1: H1 average revenue; Op EBITDA shortfall (A4 L185) | 111.97; 31.64; 53.17% | 11,197.39; 3,164.04; 1 - 1,481.78 / 3,164.04 = 53.17% | L78-91 | PASS (fixed) |
| S9: rate effect (A4 L217) | 6.71 x 1.00 pp = -0.07 | 25.2109% - 24.2066% = 1.0043 pp; 671.02 x 1.0043% = 6.74 lakh | L91, L95 | PASS (fixed) |
| Q1 FY27 materials / revenue (A4 L184) | 10.34% (7.07 / 68.36) | 706.84 / 6,836.14 | L78-L84 | PASS |

Cite checks for M2 grafts: L222 gives the 23-Sep-2026 approval date. L56 is a waaree.com CS email, unverified on image. L71 is secretarial@waaree.com. PR L145 is investorrelations@waaree.com. PR L72 reads "a WAAREE group company". PR L118 is "Waaree's manufacturing ecosystem". All five hold.

Result: no arithmetic mismatch.

---

## PRIOR FINDING CLOSURE

| # | Type | Prior gap | Revised A4 text | Status |
|---|---|---|---|---|
| F1 | FACTUAL | "Mix shift does not explain the YoY fall" at old A4 L181, L466, L488, L595, L607 | A new decomposition table (A4 L190-198) gives three-fifths spread and two-fifths mix, plus the rupee view. Restated at Step 4 (A4 L211), Q3 (A4 L426), Q12 (A4 L435), Flag 2 (A4 L487), the brief (A4 L509), the YAML flag (A4 L627) and the analyst note (A4 L639). A grep for "does not explain", "mix artifact" and "not a mix" finds only the revision log (A4 L26) and the analyst note, which quote the old error as wrong. | CLOSED |
| M1 | MISSING | Net-cash qualifier absent at old A4 L516, L490, L403, L527 | Qualifier added at the Step 5 rows (A4 L251-252), a new qualifier bullet with two readings and the separating observation (A4 L263-266), the net-debt answer (A4 L274), 6A (A4 L332), Pillar 1 (A4 L381), 8A-W flag 4 (A4 L401), Q1 (A4 L424), Q6 (A4 L429), Flag 4 (A4 L489), the brief (A4 L511), competition (A4 L539) and the forward map M1 (A4 L550). "No debt, 85.42 Cr net cash" no longer stands alone anywhere. | CLOSED |
| M2 | MISSING | Acquisition-economics probe absent | Consideration NOT FOUND and price/PAT NOT COMPUTABLE are stated. The 12.3x / 8.7x spread, approval inside the trough quarter, transferee-group administration (L56, L71, PR L145, PR L72), two readings and the separating observation are added at the valuation-unit row (A4 L388), Flag 1 (A4 L486), 8A-W flag 2 (A4 L401), Q1 (A4 L424), the top-3 list (A4 L442), monitorable M1 (A4 L464), the forward map (A4 L550) and the brief (A4 L515-516). | CLOSED |
| S1-S5, S9 | STYLE | Rounding; "ties out"; Q1 margin wording; cash attribution; "unnumbered"; rate-effect sign | Fixed at A4 L160, L180, L183, L185, L483, L508, L512, L33, L217. | CLOSED |
| S6, S7 | STYLE | A1 unenumerated units; A2 count-test labels | Not in the A4 loop; unchanged. | CARRIED (logged) |
| S8 | STYLE | Background from memory at A4 L523, L534, L541 | Still tagged SECONDARY, PENDING LIVE VERIFICATION. The proposed Key Notes line (A4 L453) leaves them out. | CARRIED (keep out of Notion until verified) |
| S10 | STYLE | M3-M5 dated NOT FOUND | Unchanged; acceptable. | CARRIED |

---

## AUDIT 3: ADVERSARIAL READ (revised review)

I re-tested the three most positive claims in the revised text. I also tested the one new bull reading the revision adds.

### Claim 1. "Where it wins: no debt and access to the parent's ecosystem" (A4 L539)
Bear counter: the cash is not free against the 89.94 Cr line (L159). The parent ecosystem is a MGMT claim (PR L118), and it is also the channel for the transfer-pricing risk.
Survives: YES, but A4 already carries it. The qualifier sits at A4 L539 and the transfer-pricing risk at A4 L543 and Q3. No graft needed.

### Claim 2. Verdict basis "the statements foot and tie to the press release" (A4 L483)
Bear counter: the cash-flow receivable and payable lines miss the balance-sheet moves by 34.94 Cr and 37.25 Cr (L132, L155-156, L186-187).
Survives: YES, and it is already in the same paragraph (A4 L483 cites flag 4). No graft needed.

### Claim 3. H1 CFO 79.57 Cr, CFO/PAT 1.91x, FCF 74.70 Cr (A4 L239-243)
Bear counter: a 158.42 Cr receivable release (L186) and an 86.99 Cr liability inflow (L190) funded a 200.89 Cr stock build (L185). Neither repeats.
Survives: YES, and it is already in A4 at L240, L271, L382 ("Do not band on the 1.91x headline") and Flag 3. No graft needed.

### New bull reading added by the revision (A4 L388): "a normalised multi-year base and market price were weighted; the trough timing is coincidence"
Bear counter: the same row pairs it with reading two (a ratio weighted to recent earnings and set inside the group) and names the separating observation (the valuation report, M1). The readings are symmetric, and neither one is credited.
Survives: n/a. No graft needed.

### Mandatory acquisition-economics probe (Note 4 amalgamation, L222-224)
Multiple: consideration (exchange ratio) NOT FOUND / target PAT = NOT COMPUTABLE. The finding is unchanged from audit 1. Representative-year test: FY26 PAT averages 61.65 Cr a quarter (43.83 Cr at statutory tax) against Q2 FY27 PAT of 5.02 Cr, a 12.3x spread (8.7x at statutory tax). Neither year is representative. My bear reading is that the board approved the scheme inside the trough quarter, and a ratio weighted to recent earnings and set inside the group would move value from minority holders. This reading is now grafted into A4 at L388, L486 and L424. The missing evidence is still the 23-Sep-2026 Reg 30 scheme filing, which M1 routes to the operator before /fttcp.

Result: no new surviving bear counter needs a graft.

---

## VERDICT

**COMPLETE.** F1, M1 and M2 are closed. The revision added no FACTUAL, MISSING or CONTRADICTION finding. Every new figure re-derives to the lakh. The A4 protocol verdict (PROCEED WITH FLAGS) and cash-conversion class (INDETERMINATE-WITH-DIRECTION) are not under challenge. loop_back_to = "".

---

## STYLE NOTES (logged; no re-run)

New in this re-audit:
- S11. A4 L262 and A4 L264-265 number the two OCL readings in opposite orders. At L262, reading one is the customer advance and reading two is the parent. At L264-265, reading one is the parent advance and reading two is the third party. The content is the same in both places, so nothing contradicts, but the operator may misread the numbering. Use the same order in both places.
- S12. In the A4 L192-196 table, the column "Rs Cr of gross profit" totals -35.67. That figure is the margin effect only. The whole gross-profit fall is -55.30 (A4 L198). Relabel the column "Rs Cr, margin effect (Step 4)".
- S13. The brief (A4 L509) tags the three-fifths / two-fifths split [FILED, derived] but does not state that it depends on the all-materials-to-goods convention (A4 L188). The convention is well supported. Q1 FY27 materials of 706.84 lakh (L83-84) are less than goods sales of 1,397.42 lakh (L78) at any goods ratio near Q2's, so tolling carries close to zero material. Even so, add "on the materials-to-goods convention".
- S14. The about -4.52 Cr net figure (A4 L263, L511) treats the whole 89.94 Cr as a cash claim. Part of the line may be statutory dues or a current deferred-grant balance (the L190 tie shows deferred grant inside other liabilities), and that part is not a cash claim of the same kind. "About" and "free cash unproven" already carry the uncertainty, and the conclusion holds. Optional wording: "about -4.52 Cr if the whole line is a cash claim".
- S15. A4 L432 (Q9) says the 2.14 Cr drawdown inside the L190 line "confirms the non-cash reading". The tie is a reconstruction, not a filed note. Use "fits".

Carried from audit 1 (unchanged; not A4-loop items):
- S6. A1 enumeration gaps: L287 www.sgco.co.in has no ENTITY row; PR L109-110 has no FORWARD row (A4 carries it at A4 L522).
- S7. A2 count-test labels (auditor_paras includes R381-R382; signatures omits L274-282; agenda_items 0 against the one item at L40-44). No row is missing.
- S8. Memory-sourced background at A4 L523, L534, L541 stays out of any Notion payload until live-verified.
- S10. Forward-map rows M3-M5 stay NOT FOUND until the scheme filing is extracted.

---

```yaml
stage: A5-adversary
company: "INDOSOLAR"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger:
    - "results L287 www.sgco.co.in (auditor website): no ENTITY row in A1 structured; STYLE carried from audit 1 (S6), non-material, no loop"
    - "presentation PR L109-110 CEO industry-transformation sentence: no FORWARD row in A1 structured; carried in A4 L522; STYLE carried from audit 1 (S6), no loop"
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "S11: A4 L262 vs L264-265 number the two OCL readings in opposite orders (customer/parent vs parent/third party); content same; align order"
    - "S12: A4 L192-196 decomposition table column 'Rs Cr of gross profit' totals -35.67, which is the margin effect only; whole GP fall is -55.30 (A4 L198); relabel"
    - "S13: A4 L509 brief split three-fifths/two-fifths tagged [FILED, derived] without the all-materials-to-goods convention (A4 L188); add the convention"
    - "S14: A4 L263/L511 net about -4.52 Cr treats all 89.94 Cr OCL as a cash claim; part may be statutory dues or deferred grant (L190 tie); conclusion holds"
    - "S15: A4 L432 Q9 'confirms the non-cash reading' overstates a reconstruction tie; use 'fits'"
    - "S6 (carried): A1 enumeration gaps L287, PR L109-110; non-material"
    - "S7 (carried): A2 count-test category labels; no row missing"
    - "S8 (carried): memory-sourced background A4 L523, L534, L541 stays out of Notion until live-verified"
    - "S10 (carried): forward map M3-M5 NOT FOUND until scheme filing extracted"
loop_back_to: ""
gap: ""
style_notes:
  - "S11 align OCL reading order at A4 L262 and L264-265"
  - "S12 relabel A4 L192 table column as margin effect only"
  - "S13 add materials-to-goods convention to brief A4 L509"
  - "S14 optional: '-4.52 Cr if the whole line is a cash claim' at A4 L263, L511"
  - "S15 A4 L432 'confirms' to 'fits'"
  - "S6, S7, S8, S10 carried from audit 1, unchanged"
analyst_note: "Bounded re-audit after loop 1. F1, M1 and M2 are closed. F1: the new decomposition re-derives from the lakh values (L78, L79, L83, L84). Mix is -9.4159 pp, spread -13.5085 pp, and the fall -22.9244 pp. In rupees, tolling -28.55, goods volume -5.73 and spread -21.02 sum to -55.30. The bridge pieces reconcile: revenue effect -19.63 plus mix -14.65 equals tolling plus volume, -34.28. A grep finds the old wording only where it is quoted as wrong. M1: the 85.42 Cr cash, 89.94 Cr OCL and -4.52 Cr net tie to L133, L134 and L159. The 86.99 Cr L190 tie holds to the lakh. M2: 12.3x and 8.7x re-derive (6,164.98 or 4,382.88 against 501.85 lakh), and all four cites hold. Consideration is still NOT FOUND, so the multiple stays NOT COMPUTABLE; the scheme filing (M1) is the open evidence item. The revision added only STYLE items (S11-S15). Verdict COMPLETE; save may proceed."
```
