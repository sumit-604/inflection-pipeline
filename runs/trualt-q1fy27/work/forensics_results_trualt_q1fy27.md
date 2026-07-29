# A3 FORENSIC NOTES — TRUALT Q1FY27 (doctype: results)

Source (primary): `extract_results_trualt_q1fy27.txt` (10pp, Reg 33 Board Outcome + Standalone/Consolidated results + N.M. Raiji & Co. limited review).
Ledger contract: `ledger_results_trualt_q1fy27.md`. Units: Rs Lakhs (x0.01 to Cr).
Supplementary (same July 28, 2026 board meeting): `extract_pressrelease_trualt_q1fy27.txt`, `extract_chairman_trualt_q1fy27.txt`.
Ledger reconciliation: 100% — every A2 row (12 notes, 67 line items, 3 zero-standing, 1 agenda item, 11 auditor paras, 3 entities, 4 segment tables, 5 signature blocks) read verbatim at its cited line before judging.
Prior-quarter baseline: NONE (fresh coverage). Where a check needs a prior period, what is computable within this filing's 4 columns is stated and the missing baseline is flagged explicitly.

Periods across both tables: Q1FY27 (Jun 30 2026, Unaudited) | Q4FY26 (Mar 31 2026, Audited) | Q1FY26 (Jun 30 2025, Unaudited) | FY26 (Mar 31 2026, Audited).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F1 | F1 Zero-standing | Std Current Tax (534); Std/Cons Exceptional Items (531/236) | 534 | "- Current Tax" (blank all 4 periods) | FORWARD-SIGNAL | Standalone pays ZERO current tax every period while PBT is 7,331.09L; 100% of tax is deferred. The Exceptional-Items placeholder (line 531/236, blank) is the template slot for M&A gain/impairment — live given the JV/SAF build. Cash tax will step up when the depreciation shield matures. |
| F2 | F2 S-vs-C decomposition | Cons PAT (245) vs Std PAT (536) | 536 | Std Q1FY26 PBT "13.19", PAT "2.57" | AMBIGUOUS | Subsidiary PAT contribution is stable in absolute Rs (Q1FY26 469.95L → Q1FY27 426.50L) but as % of standalone PAT it collapsed from ~18,000% to 7.75% because standalone (ethanol parent) PAT exploded 2.57L → 5,500.64L. The headline "PAT rises 12x" is the parent going from breakeven to profit off a near-zero base; sequentially PAT actually FELL (Q4FY26 6,883.95L → Q1FY27 5,927.14L, -14%). Ask management for a normalised run-rate. |
| F3 | F3 Shell detection | Std vs Cons cost lines; entities (108) | 523 | "{b) Purchases of Stock-in-Trade 1,058.68" (identical to consolidated line 220) | AMBIGUOUS | Purchases of Stock-in-Trade is identical to the paisa standalone vs consolidated (1,058.68 both) → subsidiaries do zero trading. CBG segment (revenue 1,120.60L, PAT 426.55L) fully accounts for the entire subsidiary footprint = TruAlt Gas. Leafiniti Bioenergy leaves NO separable operational trace (materials gap only 129.33L, employee gap 71.76L). Question: is Leafiniti dormant / pre-operational / a holding shell? No going-concern EoM exists, so any cleanup would be balance-sheet, not operations. |
| F5 | F5 EoM scope | Cons EoM para 6 (165-170); Std EoM para 5 (473-478) | 165 | "The componentization exercise in respect of Unit 4 ... is in progress. Consequently, the updation of the fixed assets register is pending." | FORWARD-SIGNAL | First quarter carrying this EoM (Unit 4 capitalised Feb 2026, mono→dual feed). Depreciation on Unit 4 is not yet finalised → future D&A could be restated once componentisation completes. No going-concern language anywhere (confirmatory-negative on solvency). No prior quarter to verbatim-diff — baseline flagged missing. |
| F6 | F6 Forward-commitment mining | Notes + press release | 100 | "Construction continues across four CBG plants under the Company's joint venture with Sumitomo Corporation, while preparatory activities are progressing for six additional CBG plants under its partnership with GAIL" | FORWARD-SIGNAL | Dated/dateable management commitments (see Commitment Register). Filing notes themselves are boilerplate; all forward commitments sit in the EoM and the press release. These feed the Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. |
| F7 | F7 Hedge mining | Press release | 109 | "adopted a cautious and calibrated approach to expansion, consciously deferring accelerated rollout" | AMBIGUOUS | Pre-emptive cover on the fuel-retail vertical (7 of 100 outlets) — signals a FLAT retail segment next quarter, blamed on West Asia crude volatility. "actively exploring advanced biofuels and low-carbon energy solutions" (line 148) = optionality language, not commitment. |
| F8 | F8 Tax forensics | Std Current/Deferred Tax (534/535); Cons (241/243) | 535 | "- Deferred Tax (1,830.45)" with Current Tax (534) blank | FORWARD-SIGNAL | Standalone ETR ~24.97% (near statutory 25.17%) so P&L is NOT flattered — but 100% of the charge is DEFERRED (current tax = 0). Deferred tax is a persistent CHARGE (not credit) → DTL building from accelerated tax depreciation. Cash tax shield this quarter ≈ 1,830L (≈297 bps of standalone revenue). When Unit 4 / capex-cycle tax depreciation drops below book, cash tax steps up sharply. No "earlier years" tax adjustment line present. |
| F10 | F10 Share count / dilution | Paid-up (543/275); EPS (546-547) | 543 | "Paid up Equity Share Capital ... 8,575.26 ... 7,063.16" | NEUTRAL-FACT | Paid-up capital rose 1,512.10L face value YoY (Q1FY26 7,063.16L → 8,575.26L) = IPO issuance (~1.51 cr shares; "first ... results as a listed company"). Current base = 857.53 lakh shares. Basic = Diluted at every period (6.41/7.54/0.00/11.24, lines 546-547) → NO dilutive instruments (ESOP/warrant) outstanding. |
| F12 | F12 Segment forensics | Segment Assets/Liab (339/340 vs 358/359) | 339 | "Segment Assets ... 22,763.65" (CBG, Jun-26) vs 358 "6,013.63" (CBG, Jun-25) | FORWARD-SIGNAL | CBG segment assets +279% YoY (6,013.63L → 22,763.65L) on flat revenue (995.70L → 1,120.60L) = pre-commissioning capex build (the Sumitomo/GAIL plants) → future revenue ramp OR external funding need. Ethanol segment assets +38.6% (2,54,532L → 3,52,684L) with liabilities up only +9.6% → equity-funded build = IPO proceeds deployed into dual-feed capacity. No Mar-31-2026 segment balance sheet given (intermediate baseline missing). |
| F13 | F13 Board outcome beyond results | Agenda (48-53); chairman intimation | 33 (chairman doc) | "appointment of Mr. Mallikarjun Bhimappa Dyaberi ... as the Chairman of the Board for a period of one year effective from July 28, 2026" | FORWARD-SIGNAL | Results letter "has inter-alia approved" (line 48) enumerates ONLY the results (AGENDA_INCOMPLETE) — the chairman item lives in a separate filing. An Independent Director (DIN 02474471) elevated to Chairman, term 1 year to ~Jul-2027, separates Chair from MD Vijay Nirani (DIN 07413777) = governance improvement, mapped across the Unit-4/CBG commissioning window. He continues as ID afterward; "shall not constitute a second consecutive term" (chairman doc line 99). First AGM / first Annual Report as a listed company are pending → schedule a Role 6 AR Deep Dive event. |
| F14 | F14 Drafting inconsistencies | Board letter vs auditor letter/headers | 50 | "the Board has approved the Audited (Standalone and Consolidated) Financial Results" | AMBIGUOUS | Board letter says "Audited" but both auditor reports (98, 420) and every table header (208, 516) say "Unaudited" / SRE 2410 limited review — likely boilerplate carry-over, confirm intent. Cumulative drafting data points: (a) press-release table header "QoQ Growth" (press line 72) is actually YoY (Q1FY27 vs Q1FY26) — true QoQ PAT fell; (b) press EBITDA 132.76 Cr strips out Other Income (14.52 Cr) inflating the growth multiple vs a high-other-income base quarter; (c) Note 3 "The Limited Review, as required under Regulation of the SEBI" (line 314) omits the regulation number; (d) corporate-office unit no. "N-1504" (line 86) vs "N-1501" (lines 406/553/608); (e) consolidated EPS single row (279-281) vs standalone Basic/Diluted split (546-547). |
| F15 | F15 Entity list diffs | Consolidation entities (104/108) | 108 | "its subsidiaries - Leafiniti Bioenergy Private Limited and TruAlt Gas Private Limited" | AMBIGUOUS | Consolidation scope = 3 entities only (Holding + 2 subs); NO associate/JV is equity-accounted. Yet the press release cites a Sumitomo Corporation JV (line 100), a GAIL partnership (line 101) and a 100 MLPA SAF project (line 103) — none appear in the audited entity list. Consistent with pre-operational/construction stage (no equity pickup yet), but the future consolidation list will expand. No prior-quarter list to diff (baseline flagged missing). |

---

## CHECKLIST SCORECARD (all 17, no blanks — GATE A3)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 Zero-value standing items | FINDING | Standalone Current Tax zero all 4 periods (534) = 100% deferred; Exceptional-Items placeholder (531/236) is the M&A/impairment slot. |
| F2 Standalone vs consolidated | FINDING | Subsidiary PAT stable (~426L) but %-of-standalone gap collapsed 18,000%→7.75% as parent PAT went 2.57L→5,500.64L; >5pp move; 12x is off a near-zero base and PAT fell sequentially. |
| F3 Shell detection | FINDING | Identical Purchases of Stock-in-Trade (1,058.68) both bases; CBG segment fully explains all subsidiary activity → Leafiniti shows no traceable operations. |
| F4 Unaudited contribution ratio | PASS | No Other Matters paragraph in either report; N.M. Raiji reviewed the full group (holding + both subs) directly; 0% of consolidated PAT rests on component-auditor/unreviewed numbers (<10% threshold). |
| F5 Going concern / EoM scope | FINDING | EoM = Unit 4 componentisation, FA register update "pending" (165-170/473-478) → future D&A restatement risk; no going-concern language; no prior quarter to diff. |
| F6 Forward-commitment mining | FINDING | Five dated/dateable commitments (CBG x4 Sumitomo, CBG x6 GAIL, SAF 100 MLPA, retail to 100 outlets, Unit 4 componentisation) — see register. |
| F7 Hedge mining | FINDING | "consciously deferring accelerated rollout" (retail) + "actively exploring advanced biofuels" = pre-emptive cover signalling flat retail and optionality-only SAF/adv-biofuels. |
| F8 Tax forensics | FINDING | 100% deferred tax, zero standalone current tax; persistent DTL build from accelerated depreciation; cash-tax step-up risk; ETR ~25% so P&L not flattered but cash flow is. |
| F9 OCI forensics | PASS | Remeasurement amounts immaterial (<15L any quarter); no single-quarter swing exceeds full prior FY (31.01L); standalone Q1FY27 sign flip (-0.57 vs +1.52 consol) is basis-difference, immaterial. |
| F10 Share count / dilution | FINDING | Paid-up +1,512.10L YoY traces cleanly to IPO; Basic=Diluted every period → no dilutive instruments. Documented as neutral fact (current base 857.53L shares). |
| F11 Reserves / net worth tie-out | PASS | Other Equity disclosed only at FY26; net worth ~Rs 1,520.3 Cr consol / Rs 1,513.5 Cr standalone; consol-standalone gap 683.11L = NCI/consolidation (expected); no third-party anchor to trigger a >5% gap test. |
| F12 Segment forensics | FINDING | CBG assets +279% YoY on flat revenue = pre-commissioning build; Ethanol assets +38.6% vs liabilities +9.6% = equity-funded (IPO) capex. |
| F13 Board outcome beyond results | FINDING | Independent Director appointed Chairman 1yr (separate filing); results letter "inter-alia" enumerates only item 1 (AGENDA_INCOMPLETE); first AR/AGM as listco pending → AR deep-dive event. |
| F14 Note drafting inconsistencies | FINDING | "Audited" vs "Unaudited" label; "QoQ Growth" header actually YoY; EBITDA strips Other Income; Note 3 missing reg number; unit-no. N-1504/N-1501; consol vs standalone EPS format. |
| F15 Entity list diffs | FINDING | 3-entity scope, no JV/associate; Sumitomo JV / GAIL / SAF referenced in press release absent from consolidation; no prior-quarter baseline. |
| F16 Presentation-specific | N.A. | Doctype = results; per applicability rule F16 is N.A. (press-release framing quirks folded into F14). |
| F17 Concall silence audit | N.A. | No concall transcript in scope; doctype = results. |

---

## COMMITMENT REGISTER (from F6 — feeds Role 5 promise-vs-delivery + FTTCP)

| # | commitment | implied date | note/ref | status word |
|---|-----------|--------------|----------|-------------|
| 1 | Unit 4 componentisation + fixed-assets-register update | by next quarter / FY26 AR | EoM lines 165-168 / 473-476 | underway ("is in progress") |
| 2 | Four CBG plants under Sumitomo Corporation JV | under construction (undated) | press line 100 | underway ("Construction continues") |
| 3 | Six additional CBG plants under GAIL (India) partnership | pre-construction (undated) | press line 101 | initiated ("preparatory activities are progressing") |
| 4 | 100 MLPA SAF project, Andhra Pradesh; Rs 150 Cr PM JI-VAN grant | multi-year; grant already received | press lines 103-106 | underway (grant milestone completed; engineering/approvals "advancing") |
| 5 | Fuel-retail network to 100 outlets (from 7) | deferred, phased | press lines 107-111 | initiated but deferred ("expansion planned ... consciously deferring accelerated rollout") |

---

## CROSS-DOCUMENT SPIN CHECKS (audited filing vs press release)

- "PAT Rises Over 12x" (press) = consolidated 59.27 Cr vs 4.73 Cr — TRUE arithmetically but off a depressed Q1FY26 base where standalone PBT was 13.19L (breakeven) and Other Income was 22.74 Cr. Real driver: ethanol parent inflection, not a broad-based 12x.
- "QoQ Growth" column header (press line 72) mislabels a YoY comparison; true sequential (vs Q4FY26) shows PAT DOWN 14% and margin compression driven by the Q4 inventory build (Changes in Inventories Q4FY26 (24,352.36) vs Q1FY27 +4,768.81).
- Press EBITDA (132.76 Cr) = PBT + Finance + D&A − Other Income; the Other-Income exclusion widens the growth multiple against a high-other-income prior year. Not in the audited filing (no EBITDA line there).

---

```yaml
stage: A3-forensics
company: "TRUALT"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/trualt-q1fy27/work/forensics_results_trualt_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: FINDING
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1", check: "F1", line: "534", classification: "FORWARD-SIGNAL", implication: "Standalone zero current tax all periods; 100% deferred; cash tax step-up when depreciation shield matures"}
  - {id: "F2", check: "F2", line: "536", classification: "AMBIGUOUS", implication: "Consolidated 12x PAT is parent inflection off near-zero base (Q1FY26 std PAT 2.57L); PAT fell sequentially -14%"}
  - {id: "F3", check: "F3", line: "523", classification: "AMBIGUOUS", implication: "Leafiniti Bioenergy shows no separable operations; CBG segment fully explains subsidiary footprint"}
  - {id: "F5", check: "F5", line: "165", classification: "FORWARD-SIGNAL", implication: "Unit 4 componentisation pending -> future D&A restatement; no going concern; no prior baseline"}
  - {id: "F6", check: "F6", line: "100", classification: "FORWARD-SIGNAL", implication: "Five dated commitments (CBG Sumitomo/GAIL, SAF, retail) for promise-vs-delivery tracking"}
  - {id: "F7", check: "F7", line: "109", classification: "AMBIGUOUS", implication: "Retail rollout deferred -> flat retail next quarter; SAF/adv-biofuels optionality-only"}
  - {id: "F8", check: "F8", line: "535", classification: "FORWARD-SIGNAL", implication: "100% deferred tax, DTL build from accelerated depreciation; cash tax step-up risk (~297 bps shield)"}
  - {id: "F10", check: "F10", line: "543", classification: "NEUTRAL-FACT", implication: "Paid-up +1,512.10L YoY = IPO; base 857.53L shares; no basic/diluted spread (no dilutive instruments)"}
  - {id: "F12", check: "F12", line: "339", classification: "FORWARD-SIGNAL", implication: "CBG assets +279% on flat revenue = pre-commissioning build; Ethanol +38.6% equity-funded IPO capex"}
  - {id: "F13", check: "F13", line: "33", classification: "FORWARD-SIGNAL", implication: "ID elevated to Chairman 1yr (separate filing); agenda incomplete; first AR/AGM as listco pending -> AR deep dive"}
  - {id: "F14", check: "F14", line: "50", classification: "AMBIGUOUS", implication: "Audited vs Unaudited label + QoQ/YoY mislabel + EBITDA definition = cumulative governance/spin data point"}
  - {id: "F15", check: "F15", line: "108", classification: "AMBIGUOUS", implication: "Sumitomo JV/GAIL/SAF absent from 3-entity consolidation scope; future scope expansion; no baseline"}
forward_signals: ["F1", "F5", "F6", "F8", "F12", "F13"]
ambiguous: ["F2", "F3", "F7", "F14", "F15"]
commitments:
  - {commitment: "Unit 4 componentisation + fixed-assets-register update", implied_date: "next quarter / FY26 AR", ref: "EoM 165-168 / 473-476", status_word: "underway"}
  - {commitment: "Four CBG plants under Sumitomo Corporation JV", implied_date: "under construction (undated)", ref: "press line 100", status_word: "underway"}
  - {commitment: "Six additional CBG plants under GAIL partnership", implied_date: "pre-construction (undated)", ref: "press line 101", status_word: "initiated"}
  - {commitment: "100 MLPA SAF project Andhra Pradesh (Rs 150 Cr PM JI-VAN grant received)", implied_date: "multi-year; grant received", ref: "press lines 103-106", status_word: "underway"}
  - {commitment: "Fuel-retail network to 100 outlets (from 7)", implied_date: "deferred / phased", ref: "press lines 107-111", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
