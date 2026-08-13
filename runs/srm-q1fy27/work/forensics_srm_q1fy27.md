# A3 FORENSIC NOTES — SRM Contractors Limited (SRM) — Q1 FY27 — DOCTYPE: results

Source extract: `extract_results_srm_q1fy27.txt` (10 pages, 438 lines, unit = Lakhs)
Ledger: `ledger_results_srm_q1fy27.md` (gate_a2: pass)
Prior-quarter extract: NONE (first quarterly run for SRM). QoQ verbatim diffs use the FY26
audited baselines in the Notion monitoring checklist as reference; any check strictly needing a
prior filing's line-numbered text is marked N.A. with that reason. No prior number fabricated.
Ledger reconciliation: 100% — every row in Tables 1-11 read at its cited line before judging.

---

## EXECUTIVE READ (the forward message of this document)

1. **This is a P&L-only filing. The single most thesis-critical metric — working-capital /
   receivable / creditor / contract-asset days — cannot be computed or diffed this quarter.**
   No balance sheet, no cash-flow statement. Both statements terminate at EPS (lines 196, 391).
   The FY26 baselines the thesis pivots on (gross current asset days 192, average creditor
   period 90) get zero new data points here. This is silence on a deteriorating metric =
   CONFIRMATORY-NEGATIVE; carry to the half-year / AR event. (F11)

2. **Clean review, no EoM, no going-concern, unmodified conclusion on both reports.** Thesis
   EXIT trigger #1 (audit qualification / EOM / modified conclusion) did NOT fire this quarter.
   (F5) The auditor is Rohit Kc Jain & Co (CA Ritesh Wahal, FRN 020422N) — continuity with the
   checklist's stated current auditor; no auditor change disclosed.

3. **First full consolidated quarter with MIPL, but the consolidated statement carries no
   non-controlling-interest line.** MIPL is 51% owned (49% NCI). Consolidated PAT 1,971.25 and
   EPS 8.59 appear struck on total group profit with no owner-vs-NCI split — owner EPS likely
   overstated. This is the highest-value forensic finding for A4. (F2 / FF3)

4. **Consolidated ETR falls to 18.8% on a deferred-tax CREDIT of -163.49** (only negative in the
   row) while standalone deferred tax is a +162.67 charge — a subsidiary-level DTA recognition of
   ~Rs326 lakh, ~633bps of shield below the 25.17% statutory rate. Future step-up risk. (F8)

5. **DUPLICATE_UDIN confirmed** (independently verified): identical UDIN `26517197VKSZFF5162`
   on both the standalone (line 139) and consolidated (line 339) Limited Review Reports. ICAI
   norm is one UDIN per certificate. (F14)

6. **ZERO_STANDING x10 confirmed** (independently verified): 6 standalone (lines 179, 185, 187,
   188, 189, 190) + 4 consolidated (lines 373, 382, 383, 384) = 10 nil/dash lines. (F1)

Thesis-broken trigger scan (5 triggers): #1 audit qualification/EOM — NOT fired (clean).
#2 RPT util >Rs400Cr — not disclosed in this filing (no RPT note). #3 govt delays/WC days >200 —
not derivable (no balance sheet). #4 promoter pledge/sale/block — not disclosed here (no
shareholding statement in filing). #5 ROCE <12% — not derivable (no capital-employed / balance
sheet). Four of five triggers are un-testable from a P&L-only filing; that itself is the message.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------------|----------------|---------------------|
| FF1 | F1 | T3 r12 / T7 r12 | 179, 373 | "Exceptional lteams" (no value, all periods) | FORWARD-SIGNAL | Template line sits empty during active MIPL integration; any bargain-purchase gain / restructuring cost from the Rs19 Cr final tranche (due Q2 FY27) has not yet landed — watch Q2. |
| FF2 | F2 | T3 r17 / T7 r17 | 186, 380 | std 1,593.80 vs consol 1,971.25 (Q1FY27) | NEUTRAL-FACT | S-vs-C PAT gap swung from -2.4% (Q1FY26) to +23.7% (Q1FY27), a +26pp YoY move (>5pp threshold); QoQ narrowed from +60.5% (Q4FY26). Consolidation of MIPL + project SPVs is the driver; Q1FY26 consol revenue was BELOW standalone, confirming subs were immaterial a year ago. |
| FF3 | F2 | T7 r17, r23 | 380-381, 390 | "Profit / (Loss) for the period ... 1971.25"; "Basic 8.59" | FORWARD-SIGNAL / AMBIGUOUS | No non-controlling-interest line in the consolidated statement despite 51%-owned MIPL. Consolidated PAT and EPS 8.59 appear computed on full group profit including ~49% NCI; owner EPS likely overstated (~9% on a rough MIPL-share estimate). A4 must ask: is consol PAT/EPS pre- or post-NCI? |
| FF4 | F3 | T6 r1-3 | 313-315 | "Total Revenues Rs.3,447.29 ... Net Profit After Tax Rs.11.84" | AMBIGUOUS | Reviewed-component subs show Rs11.84 lakh NPAT on Rs3,447.29 lakh revenue = 0.34% net margin. Near-zero-profit project SPVs (pass-through construction JVs); the profitable sub (MIPL) sits in the principal-auditor bucket. No per-entity split disclosed. |
| FF5 | F4 | T5 r7-10, T6 | 308, 321, 327 | "reviewed/audited by their auditors" (308) vs "unaudited/unreviewed interim financial information" (321) vs "certified by the Board of Directors" (327) | AMBIGUOUS | The same components are described three inconsistent ways. 17.6% of consolidated REVENUE (3,447.29 / 19,626.20) rests on management-certified numbers, though only 0.6% of PAT. The reassuring "reviewed/audited" phrase overstates assurance. |
| FF6 | F8 | T3 r14-15 | 183-184, 180 | current 481.33 + deferred 162.67 on PBT 1,912.46 | AMBIGUOUS | Standalone ETR 33.7% in Q1FY27 vs 25.17% statutory (+850bps), the highest of four periods, with no "income tax of previous year" line to explain it (that line is nil). Unexplained ETR spike — A4 question. |
| FF7 | F8 | T7 r15 | 378 | "(b) Deferred tax -163.49" | FORWARD-SIGNAL | Consolidated deferred tax is a CREDIT of -163.49 (only negative in the row) vs standalone +162.67 charge → subsidiary-level deferred-tax credit ~Rs326 lakh (DTA recognition, likely MIPL). Consol ETR 18.8%, ~633bps shield below statutory. DTA-driven; future ETR step-up when the shield exhausts. Verify DTA at AR. |
| FF8 | F12 | T4 r4 / T8 r5 | 227, 426 | "the Company operates in single segment" | AMBIGUOUS | Single-segment assertion (Ind AS 108) maintained into the first quarter that consolidates MIPL, a gabion / manufacturing business, alongside SRM's civil-construction business. Combining manufacturing + construction under one segment with no split is questionable — A4 question. |
| FF9 | F13 | T1 r1, T10 r1 | 30-42, 41, 57-61 | "the Board meeting commenced at 4.00 P.M. and concluded at. 4.30 P M."; signatory "16:30:23 +05'30'" | NEUTRAL-FACT / AMBIGUOUS | Sole agenda item = results approval; no AGM notice, record date, dividend, AR approval, director appointment, or capital-raise resolution. 30-minute board meeting to approve the first consolidated quarter. CS digital-signature timestamp is ~23 seconds after nominal close (benign, but a near-zero window). AGM notice for a March-FY company by mid-August is absent — expect a separate imminent Board Outcome; not schedulable as an AR Deep Dive yet. |
| FF10 | F14 | T2 / T5 sig blocks | 139, 339 | "UDIN: 26517197VKSZFF5162" (identical on both reports) | AMBIGUOUS | Same UDIN on two distinct certified documents (standalone + consolidated review reports). ICAI practice generates one UDIN per certificate. A4 question: confirm whether two UDINs were in fact generated. |
| FF11 | F14 | T6 r3, T5 r7 | 305, 315-316, 326-327 | "Total Comprehensive Loss ... Rs.11.84" (label Loss, value positive); "Our conclusion is not modified in respect of these matters" | NEUTRAL-FACT / AMBIGUOUS | Multiple drafting inconsistencies: (a) reliance-table row labelled "Loss" but value +11.84 equals the NPAT above it; (b) "not modified in respect of these matters" (plural, line 305) appears before any matters are introduced, then repeated singular at 326; (c) NO acquisition / MIPL note anywhere despite this being the first consolidation quarter. Cumulatively a governance data point. |
| FF12 | F11 | T3 / T7 tail | 196, 391 | statement ends "(2) Diluted 6.95 / 8.59" — no line follows | CONFIRMATORY-NEGATIVE | No balance sheet, no cash-flow, no equity/reserves lines. The BINDING monitoring item this quarter — WC / receivable / creditor / contract-asset days vs FY26 baseline (GCA 192, creditor 90) — is NOT derivable. Net-worth tie-out impossible. Thesis triggers #3 (WC days >200) and #5 (ROCE <12%) un-testable. Raise at half-year/AR. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING | **FINDING** | 10 ZERO_STANDING lines verified (6 std: 179,185,187,188,189,190; 4 consol: 373,382,383,384). Exceptional-items line empty during MIPL integration (FF1); OCI nil every period despite rising employee costs (note to verify at AR). |
| F2 STANDALONE vs CONSOL DECOMP | **FINDING** | PAT gap -2.4% (Q1FY26) → +23.7% (Q1FY27), +26pp YoY > 5pp threshold (FF2); no NCI line despite 51% MIPL, EPS likely on full profit (FF3). |
| F3 SHELL-ENTITY DETECTION | **FINDING** | Cost lines differ std vs consol (subs DO operate — MIPL), but reviewed-component subs show 0.34% net margin (Rs11.84 on Rs3,447.29) = near-dormant-profit project SPVs; no per-entity data, no GC EoM to reconcile (FF4). |
| F4 UNAUDITED CONTRIBUTION RATIO | **FINDING** | 0.6% of consol PAT but 17.6% of consol revenue rests on management-certified numbers; reliance para contradicts itself (reviewed/audited vs unaudited/unreviewed vs Board-certified) (FF5). No trend (first run). |
| F5 GOING CONCERN / EoM SCOPE | **PASS** | No EoM, no Other Matters heading, no going-concern language in either report (std 116-123; consol 296-305). Both conclusions unmodified. EXIT trigger #1 did NOT fire. QoQ verbatim diff not possible (no prior extract), but the trigger condition is verifiably absent this filing. |
| F6 FORWARD-COMMITMENT MINING | **PASS** | Notes (std 210-232, consol 403-429) contain no lexicon hits ("expected to", "will be", "shall be completed", "commenc", "proposes to", "board has approved", "intends to", "in the process of"). Commitment register empty. |
| F7 HEDGE PHRASE MINING | **PASS** | No hedge lexicon in notes ("no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour"). "wherever applicable" (regrouping note) not in lexicon. |
| F8 TAX FORENSICS | **FINDING** | Std ETR 33.7% Q1FY27 vs 25.17% statutory, unexplained (FF6); consol deferred-tax credit -163.49 → ~Rs326 lakh sub-level DTA, consol ETR 18.8%, ~633bps shield (FF7). Current-quarter "prior-year tax" line nil (no FINDING there). |
| F9 OCI FORENSICS | **PASS** | OCI nil in all four periods, both statements (188-190, 382-384). No single-quarter swing exceeding prior year (all zero). Note: persistent nil OCI despite rising employee costs — verify DB remeasurement at AR (not a trigger breach). |
| F10 SHARE COUNT & DILUTION | **PASS** | Basic = diluted EPS in every clean period (std 6.95/6.95, 14.66/14.66; consol 8.59/8.59, 23.58/23.58) → no dilutive instruments. Implied share count stable ~2.29 cr across periods; no corporate action. (FY26 std basic OCR-garbled "3" but diluted 37.31 and derived ~37.3, so no spread.) |
| F11 RESERVES / NET WORTH TIE-OUT | **FINDING** | No balance sheet in filing — no Other Equity, Paid-up, receivables, creditors, or contract-asset lines. Net-worth tie-out impossible AND the BINDING WC-days monitoring item is not derivable (FF12). |
| F12 SEGMENT FORENSICS | **FINDING** | "Single segment" (227, 426); no segment asset/liability tables. Assertion maintained post-MIPL consolidation despite construction + manufacturing mix (FF8). |
| F13 BOARD OUTCOME BEYOND RESULTS | **FINDING** | Sole agenda item = results approval; no AGM/AR/dividend/director/capital-raise item; 30-min board meeting; CS signature ~23s after close (FF9). Nothing schedulable as AR Deep Dive yet. |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | DUPLICATE_UDIN across two certificates (FF10); "Loss" label on +11.84 value, doubled "not modified" qualifier, no MIPL acquisition note (FF11). |
| F15 ENTITY LIST DIFFS | **N.A.** | No prior-quarter ledger to diff (first quarterly run). Table 9 (8 entities) established as baseline. YoY consolidation expansion captured under F2, but a line-numbered prior entity list does not exist to diff verbatim. |
| F16 PRESENTATION-SPECIFIC | **N.A.** | Doctype = results, not a presentation deck. |
| F17 CONCALL-SPECIFIC | **N.A.** | Doctype = results, no transcript. (Silence audit on WC-days deterioration captured under FF12 instead.) |

Status line: **F1 FINDING · F2 FINDING · F3 FINDING · F4 FINDING · F5 PASS · F6 PASS · F7 PASS · F8 FINDING · F9 PASS · F10 PASS · F11 FINDING · F12 FINDING · F13 FINDING · F14 FINDING · F15 N.A. · F16 N.A. · F17 N.A.**
(10 FINDING · 4 PASS · 3 N.A. · 0 blank — GATE A3 pass.)

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| (none) | — | — | — |

No forward-commitment lexicon hits in either notes block. NOTE for A4: the MIPL final tranche
(Rs19 Cr, due Q2 FY27) and the MPL-MIPL gabion related-party supply quantum are live checklist
commitments that this filing is SILENT on — no note, no RPT disclosure. Absence, not a stated
commitment; feeds the Role 5 promise-vs-delivery tracker as a disclosure gap.

---

## WORKING NUMBERS (for A4 audit trail)

S-vs-C PAT gap (profit for the period): Q1FY27 +377.45 (+23.7% of std) · Q4FY26 +2,036.54 (+60.5%)
· Q1FY26 -31.15 (-2.4%) · FY26 +2,543.89 (+29.7%). FY26 delta Rs25.44 Cr ties to checklist's
"~Rs25 Cr" consol-vs-std gap. Q1FY26 consol revenue (14,239.66) BELOW standalone (14,309.34) =
subs immaterial a year ago; entire Q1FY27 consol uplift is new.

Effective tax rates: Std 33.7% / 22.6% / 29.3% / 26.7% (Q1FY27/Q4FY26/Q1FY26/FY26). Consol 18.8%
/ 22.5% / 30.0% / 26.5%. Consol Q1FY27 shield vs 25.17%: ~Rs153 lakh ≈ 633bps. Sub-level deferred
tax = consol -163.49 minus std +162.67 = -326.16 lakh credit.

Reviewed-component subs (Table 6): Rs3,447.29 lakh revenue = 17.6% of consol revenue; Rs11.84
lakh NPAT = 0.6% of consol PAT = 0.34% net margin. Consol revenue uplift 4,594.66; residual
1,147.37 revenue + ~365.6 PAT sits in the principal-auditor bucket (MIPL, ~31.8% margin — the
profitable sub).

Implied share count (PAT/EPS): ~229.4 lakh (2.29 cr) shares, stable across all periods and both
statements.

---

```yaml
stage: A3-forensics
company: "SRM"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/srm-q1fy27/work/forensics_srm_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: FINDING
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FF1", check: "F1", line: "179,373", classification: "FORWARD-SIGNAL", implication: "Exceptional-items template line empty during MIPL integration; watch Q2 for final-tranche / bargain-purchase accounting."}
  - {id: "FF2", check: "F2", line: "186,380", classification: "NEUTRAL-FACT", implication: "S-vs-C PAT gap +26pp YoY (-2.4% -> +23.7%), >5pp threshold; MIPL + SPV consolidation driver."}
  - {id: "FF3", check: "F2", line: "380,390", classification: "FORWARD-SIGNAL", implication: "No NCI line despite 51% MIPL; consol EPS 8.59 appears on full group profit incl 49% NCI, owner EPS overstated."}
  - {id: "FF4", check: "F3", line: "313", classification: "AMBIGUOUS", implication: "Reviewed-component subs 0.34% net margin (11.84 on 3,447.29) = near-dormant-profit project SPVs; no per-entity data."}
  - {id: "FF5", check: "F4", line: "308,321,327", classification: "AMBIGUOUS", implication: "Reliance para self-contradicts (reviewed/audited vs unaudited/unreviewed vs Board-certified); 17.6% of consol revenue management-certified."}
  - {id: "FF6", check: "F8", line: "183,180", classification: "AMBIGUOUS", implication: "Standalone ETR 33.7% vs 25.17% statutory, unexplained (prior-year tax line nil)."}
  - {id: "FF7", check: "F8", line: "378", classification: "FORWARD-SIGNAL", implication: "Consol deferred-tax credit -163.49 (~Rs326 lakh sub-level DTA); ETR 18.8%, ~633bps shield; future step-up risk."}
  - {id: "FF8", check: "F12", line: "227,426", classification: "AMBIGUOUS", implication: "Single-segment claim maintained post-MIPL despite construction + gabion-manufacturing mix; no segment split."}
  - {id: "FF9", check: "F13", line: "41,57", classification: "AMBIGUOUS", implication: "Thin single-item board agenda; no AGM/AR/dividend; 30-min meeting; CS signature ~23s post-close; AGM notice awaited."}
  - {id: "FF10", check: "F14", line: "139,339", classification: "AMBIGUOUS", implication: "DUPLICATE_UDIN 26517197VKSZFF5162 on both review reports; ICAI norm one UDIN per certificate."}
  - {id: "FF11", check: "F14", line: "305,315", classification: "AMBIGUOUS", implication: "Drafting inconsistencies: Loss label on +11.84 value; doubled not-modified qualifier; no MIPL acquisition note."}
  - {id: "FF12", check: "F11", line: "196,391", classification: "CONFIRMATORY-NEGATIVE", implication: "P&L-only filing; binding WC/receivable/creditor/contract-asset days not derivable vs FY26 baseline; net-worth tie-out impossible; triggers #3 and #5 un-testable."}
forward_signals: ["FF1", "FF3", "FF7"]
ambiguous: ["FF4", "FF5", "FF6", "FF8", "FF9", "FF10", "FF11"]
commitments: []
gate_a3: pass
blank_checks: []
```
