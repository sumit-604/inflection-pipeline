# A3 FORENSIC NOTES — Balaji Amines Limited (BALAMINES), Q1 FY27 — doctype: presentation (Investor Release / Press Release)

Source extract: `extract_presentation_balamines_q1fy27.txt` (pressrelease_balamines_q1fy27.pdf, 5 pages)
A2 ledger: `ledger_presentation_balamines_q1fy27.md`
Prior-quarter baseline: none (first coverage; no prior deck to diff)
Notion monitoring checklist: none (new-coverage ticker)
Ledger reconciliation: 100% — every row in ledger §1 (rows 1-48), §2 (1-3), §3 (1-2), §4 (1-32), §5 (F1-F2), §7 (1-14) read verbatim at its cited line before judging.

Doctype applicability (per task + prompt rule): F16 applies, plus the F6/F10/F11 numbers the release carries, plus F7/F14 phrase/drafting checks. Balance-sheet-heavy checks F1-F5, F8, F9, F12, F15 are N.A. (no balance sheet, no auditor letter, no segment assets/liabilities, no entity list in this doctype). F13 N.A. (no board resolution / AGM / director / AR content in a Reg 30 press release). F17 N.A. (no concall).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | short verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------------|----------------|---------------------|
| F6-01 | F6 | §4 rows 12,14,15,16,18,19,20,30,32 | L115-148, L165-180 | "targeted for commissioning during FY27"; "expected to be commissioned during FY27" | FORWARD-SIGNAL | Four distinct FY27 commissioning commitments (NMM, ACN, BSC Unit-I brownfield, BSC Unit-II greenfield HCN/NaCN/EDTA) all dated only "during FY27" with no month/quarter granularity — dense, undifferentiated H2FY27 catalyst cluster; slip risk. DME 100k TPA already logged "completed." Feeds Role 5 promise-vs-delivery tracker + FTTCP timeline. |
| F7-01 | F7 | §4 row 24 | L156-157 | "maintaining sustainable performance in the adverse scenarios of West Asia's crisis" | AMBIGUOUS | Sole macro/geopolitical acknowledgment in the release, unquantified. For an amines/specialty exporter this hints at feedstock (methanol/ammonia), logistics or export-demand exposure to the Middle East. A4 question: which channel and what magnitude. |
| F10-01 | F10 | §3 rows 1-2 | L108-109 | "Diluted EPS for Q1FY27 stood at ₹ 23.13 per equity share as against ₹ 19.99 in Q4FY26" | AMBIGUOUS | No basic EPS, no paid-up capital, no Q1FY26 comparator disclosed — basic-vs-diluted spread not computable here. Diluted EPS QoQ +15.7% tracks STANDALONE PAT QoQ +16.1% (62→72), not consolidated PAT +20% (65→78) — implies EPS is standalone-basis (release does not state it). Cross-check share count, spread and basis against the Reg 33 filing. |
| F11-01 | F11 | §1 rows 7-12, 19-24 | L76, L78 | "EBITDA (Rs. Cr) ... 64 ... 64" (Std vs Consol Q1FY26) | FORWARD-SIGNAL | Consol-minus-standalone (Balaji Speciality Chemicals + other non-standalone) contribution swinging positive: PAT contribution −3 (Q1FY26: consol 37 < std 40) → +3 (Q4FY26: 65 vs 62) → +6 (Q1FY27: 78 vs 72); EBITDA contribution 0 (64 vs 64) → +8 (102 vs 94) → +11 (121 vs 110). BSC turning EBITDA-accretive and PAT-positive, consistent with the expansion narrative. Confirm at consolidated Reg 33. |
| F11-02 | F11 | §1 row 40; §5 F1 | L81, L84 | "*Cash PAT is PAT + Depreciation + Deferred tax" | NEUTRAL-FACT | Cash PAT is a company-defined non-GAAP metric with no reconciliation to the cash-flow statement in the release; implied (Dep+Deferred tax) add-back = 17/13/13 (Std Q1FY27/Q1FY26/Q4FY26) and 19/14/16 (Consol) — tie-out deferred to the filing. Internal slip: Consolidated Cash PAT Margin Q1FY27 shown "20%" but 97/461 = 21.0% (rounds to 21%); every other margin cell rounds correctly. |
| F14-01 | F14 | §4 row 21 | L150 | "Mr. D. Ram Reddy, Managing Director, commented, [NS1]" | NEUTRAL-FACT | Stray tracked-change/comment marker "[NS1]" left inline in a filed, digitally-signed public disclosure — proofing/governance data point. "NS" plausibly the IR advisor's fingerprint (Nikunj Seth, MUFG Intime, L228). Individually immaterial; a marker of the release-drafting control environment. |
| F16-01 | F16 | §4 rows 4,5,6; §1 rows 46-47 | L88-93 | "Volumes were maintained at similar levels last year" | FORWARD-SIGNAL | Directly contradicts disclosed data: consolidated Sales Volume 27,570 MT (Q1FY26) → 21,587 MT (Q1FY27) = −21.7% YoY (and −21.0% QoQ vs 27,341); standalone 24,847 → 20,619 = −17.0% YoY. Framing is MISLEADING (not merely softened). "Stable operational performance" (L88) is pinned to the favorable QoQ revenue frame (461 vs 403) while the YoY/QoQ volume contraction goes uncharacterized. A4 question: is the shrunken volume base structural (lost tonnage / deliberate mix shift), and reconcile with "maintained at similar levels." |
| F16-02 | F16 | §1 rows 4-6, 46-47 | L75, L82, L89-91 | "supported by stable commodity prices" | FORWARD-SIGNAL | Revenue +25.6% YoY (367→461) on volume −21.7% ⇒ realization ~₹2.14 lakh/MT vs ~₹1.33 lakh/MT = ~+60% YoY per-MT; QoQ revenue +14.4% on volume −21.0% ⇒ realization ~+45% QoQ. Growth is price/mix-led, not volume-led — the "stable commodity prices" claim sits against a large realization step-up. Earnings-quality / durability risk if realizations normalize. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | No balance sheet / line-item template in a press release; ledger ZERO_STANDING count = 0. |
| F2 STANDALONE vs CONSOLIDATED DECOMP | N.A. | No JV/associate/subsidiary/elimination detail in this doctype; the S-vs-C contribution swing that *is* computable from the highlight table is surfaced under F11-01. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone-vs-consolidated cost lines (materials, employee, depreciation) disclosed. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other Matters / component-auditor disclosure (unaudited results, no auditor letter attached). |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No Going Concern / Emphasis-of-Matter paragraph; no auditor letter; first coverage (no prior EoM to diff). |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | F6-01: DME (completed) + four "during FY27" commissioning commitments + BSC ₹750cr programme + undated electronic-grade/EV-battery aspiration. |
| F7 HEDGE PHRASE MINING | **FINDING** | F7-01: sole substantive hedge is the unquantified West Asia crisis reference; remaining hits ("subject to numerous risks," L213; "endeavors," L180) are boilerplate Safe Harbor; no prior deck to diff for newly-added hedges. |
| F8 TAX FORENSICS | N.A. | No tax line / ETR / deferred-tax breakdown disclosed (deferred tax appears only inside the Cash PAT definition, not as a statement line). |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure in a press release. |
| F10 SHARE COUNT & DILUTION | **FINDING** | F10-01: diluted EPS 23.13 vs 19.99 recorded; no basic EPS / paid-up capital / Q1FY26 comparator — spread not computable, EPS basis unstated (evidence points standalone); cross-check at filing. |
| F11 RESERVES / NET-WORTH TIE-OUT (repurposed: Cash PAT + highlight-table reconciliation) | **FINDING** | F11-01 subsidiary contribution swing (BSC turning accretive); F11-02 Cash PAT non-GAAP + Consol Cash PAT Margin Q1FY27 rounding slip (20% shown vs 21.0% computed). |
| F12 SEGMENT FORENSICS | N.A. | Only segment *volumes* disclosed (§2); no segment assets/liabilities/results to trend. |
| F13 BOARD OUTCOME BEYOND RESULTS | N.A. | Reg 30 press release carries no board resolution / AGM notice / director appointment / AR-approval content; board outcomes (if any) sit in the Reg 33 filing, not this document. |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | F14-01: stray "[NS1]" editorial marker left inline in the filed, digitally-signed release (L150). |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list in this doctype; first coverage (no prior list to diff). |
| F16 DROPPED / REFRAMED DISCLOSURES | **FINDING** | F16-01 "volumes maintained at similar levels" vs −21.7% YoY volume decline (misleading framing); F16-02 price/mix-led growth vs "stable commodity prices." No prior-quarter release baseline available for dropped-metric / axis diffs. |
| F17 CONCALL SILENCE AUDIT | N.A. | No concall transcript for this document (task confirms F17 N.A.). |

---

## COMMITMENT REGISTER (from F6)

| Commitment | Implied date | Ref | Status word |
|-----------|--------------|-----|-------------|
| DME 100,000 TPA plant (India's first commercial-scale) | Q1FY27 (achieved) | L115-117 / L159-161 (§4 rows 12, 25) | "successful commissioning" — COMPLETED |
| N-Methyl Morpholine (NMM) commissioning | during FY27 | L122-124 / L165-167 (§4 rows 14, 27) | "next phase … includes the commissioning" — UNDERWAY/PLANNED |
| Acetonitrile (ACN) capacity expansion | during FY27 | L122-124 (§4 row 14) | "capacity expansion during FY27" — UNDERWAY/PLANNED |
| Balaji Speciality Chemicals ₹750 cr phased expansion programme | multi-quarter ("over the coming quarters") | L128-130 / L166-168 (§4 rows 15, 28) | "continues to advance" / "progressing as planned" — UNDERWAY |
| BSC Unit-I brownfield (EDA-based downstream products) | during FY27 | L144-145 (§4 row 19) | "expected to be commissioned" — UNDERWAY |
| BSC Unit-II greenfield, MIDC Chincholi (HCN, NaCN, EDTA, EDTA-2Na) | during FY27 | L147-148 (§4 row 20) | "under execution … targeted for commissioning" — UNDER EXECUTION |
| Electronic-grade products / EV battery chemicals expansion | unspecified (no date) | L172-175 (§4 row 30) | "remain focused on expanding" — ASPIRATIONAL (undated) |
| Order pipeline | unspecified | L177-180 (§4 row 32) | "healthy order pipeline" — ASSERTED, UNQUANTIFIED |

Commitment-register note for Role 5: four commissioning promises (NMM, ACN, Unit-I, Unit-II) share an identical, undifferentiated "during FY27" deadline. Track each as a separate promise-vs-delivery row; a single missed line reads as a slip. DME is the one delivered milestone this quarter.

---

## FOR A4 (management questions to build)
- F16-01 / F16-02 (FORWARD-SIGNAL): reconcile "volumes maintained at similar levels" with the −21.7% YoY / −21.0% QoQ consolidated volume decline; is the shrunken tonnage base structural or a deliberate mix shift, and how durable is the ~60% YoY realization step-up that is carrying revenue growth.
- F6-01 (FORWARD-SIGNAL): which of NMM / ACN / Unit-I / Unit-II lands in which FY27 quarter, and what capex-spent-to-date and % completion sit behind "progressing as planned."
- F7-01 (AMBIGUOUS): West Asia crisis exposure channel (feedstock, logistics, export demand) and magnitude.
- F10-01 (AMBIGUOUS): confirm diluted EPS basis (standalone vs consolidated), basic-vs-diluted spread, and share count against the Reg 33 filing.
- F11-01 (FORWARD-SIGNAL, data cross-check): confirm the BSC/non-standalone PAT and EBITDA contribution turnaround at consolidated Reg 33.

---

```yaml
stage: A3-forensics
company: "BALAMINES"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/balamines-q1fy27/work/forensics_presentation_balamines_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F6-01", check: "F6", line: "L115-148,L165-180", classification: "FORWARD-SIGNAL", implication: "Four undated 'during FY27' commissioning commitments (NMM, ACN, BSC Unit-I, BSC Unit-II) cluster H2FY27 catalysts; DME logged completed"}
  - {id: "F7-01", check: "F7", line: "L156-157", classification: "AMBIGUOUS", implication: "Unquantified West Asia crisis exposure; A4 to probe feedstock/logistics/export channel"}
  - {id: "F10-01", check: "F10", line: "L108-109", classification: "AMBIGUOUS", implication: "No basic EPS/paid-up/Q1FY26 comparator; EPS basis unstated (evidence=standalone); cross-check spread at filing"}
  - {id: "F11-01", check: "F11", line: "L76,L78", classification: "FORWARD-SIGNAL", implication: "Consol-minus-standalone PAT contribution -3->+3->+6 and EBITDA 0->+8->+11: BSC turning accretive"}
  - {id: "F11-02", check: "F11", line: "L81,L84", classification: "NEUTRAL-FACT", implication: "Cash PAT non-GAAP, no CF reconciliation; Consol Cash PAT Margin Q1FY27 shown 20% vs 21.0% computed"}
  - {id: "F14-01", check: "F14", line: "L150", classification: "NEUTRAL-FACT", implication: "Stray '[NS1]' editorial marker left in a filed, signed release; drafting-control/governance data point"}
  - {id: "F16-01", check: "F16", line: "L88-93", classification: "FORWARD-SIGNAL", implication: "'Volumes maintained at similar levels' vs -21.7% YoY consolidated volume decline = misleading framing"}
  - {id: "F16-02", check: "F16", line: "L75,L82,L89-91", classification: "FORWARD-SIGNAL", implication: "Revenue +25.6% YoY on volume -21.7% => realization ~+60%/MT; growth price/mix-led, durability risk"}
forward_signals: ["F6-01", "F11-01", "F16-01", "F16-02"]
ambiguous: ["F7-01", "F10-01"]
commitments:
  - {commitment: "DME 100,000 TPA plant", implied_date: "Q1FY27 (achieved)", ref: "L115-117/L159-161", status_word: "completed"}
  - {commitment: "NMM commissioning", implied_date: "FY27", ref: "L122-124/L165-167", status_word: "underway"}
  - {commitment: "ACN capacity expansion", implied_date: "FY27", ref: "L122-124", status_word: "underway"}
  - {commitment: "BSC Rs 750 cr phased expansion", implied_date: "multi-quarter", ref: "L128-130/L166-168", status_word: "underway"}
  - {commitment: "BSC Unit-I brownfield (EDA downstream)", implied_date: "FY27", ref: "L144-145", status_word: "underway"}
  - {commitment: "BSC Unit-II greenfield MIDC Chincholi (HCN/NaCN/EDTA/EDTA-2Na)", implied_date: "FY27", ref: "L147-148", status_word: "under execution"}
  - {commitment: "Electronic-grade / EV battery chemicals expansion", implied_date: "unspecified", ref: "L172-175", status_word: "aspirational"}
  - {commitment: "Order pipeline", implied_date: "unspecified", ref: "L177-180", status_word: "asserted"}
gate_a3: pass
blank_checks: []
```
