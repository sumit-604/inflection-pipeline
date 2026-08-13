# A3 FORENSIC NOTES — Fujiyama Power Systems Ltd (UTLSOLAR / BSE 544613)
Doctype: results | Quarter: Q1 FY27 (quarter ended 30 June 2026)
Source extract: /home/user/inflection-pipeline/runs/utlsolar-q1fy27/work/extract_results_utlsolar_q1fy27.txt
Ledger: /home/user/inflection-pipeline/runs/utlsolar-q1fy27/work/ledger_results_utlsolar_q1fy27.md
Model: claude-opus-4-8
Units: source Rs million; x0.1 -> Rs Crores (EPS/face value not converted).

RECONCILIATION: 100%. All 29 P&L line-item rows (A2 sec 1, lines 450-522), the
PAT-gap metric (sec 2, lines 474/476/497-498), all 4 agenda items (lines 70-89),
all 8 notes (lines 541-601), all 13 auditor paragraphs (lines 159-323), all 12
annexure rows, all 3 consolidation entities (lines 270-272) and all 8 signoff
blocks were read verbatim at their cited lines before judging. No unread row.

Data-quality posture: page-7 figures are taken from A1's VERIFIED 300dpi
transcription block (lines 438-523), not the garbled raw OCR layer (lines
343-416). Zero-value ("-") cells are treated as DATA. The one A1-resolved cell
(consol FY26 Current tax = 885.52m, line 479-491) is treated as reconciled-but-
not-visually-confirmed and independently re-checked below under F8.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | class | forward implication |
|----|-------|----------------|------|----------------|-------|---------------------|
| A3-01 | F1 | sec1 row 13, 15 | 468-470, 474 | "Loss due to fire in Bawal Plant (refer note 3)" ... "Share in loss of associates ... (0.01)" | FORWARD-SIGNAL | Template now carries a specifically-captioned fire-loss exceptional line (live until insurance resolves) and a now-permanent associate-share line; both will recur next quarter. |
| A3-02 | F2 | sec2 (PAT gap) | 474, 476, 497-498 | "Profit before tax ... 776.61 ... 776.60" (std vs consol) | FORWARD-SIGNAL | S-vs-C PAT gap is Rs 0.01m (0.002% of PAT) this quarter — under the 5pp trigger — but it is structurally new; every consolidated comparative cell is standalone data relabelled, so no like-for-like trend exists and the gap widens as the 31% associates scale. |
| A3-03 | F5 | sec5 para5 / sec6 para6 | 188-193, 281-286 | "a major fire broke out on 06 May 2026 in one of the Company's production facilities located in Bawal ... Rs. 1,435.81 million ... recognised as an exceptional item ... Our conclusion is not modified" | CONFIRMATORY-NEGATIVE | First appearance of a Bawal-fire Emphasis-of-Matter in BOTH review reports; ties to the company-memory Bawal tripwire. Not a qualification (conclusion unmodified) but a standing EoM until the insurance/recovery is settled. |
| A3-04 | F6 | note 3 / note 4 / agenda 4 | 560, 557, 568, 86 | "management expect to recover the loss of net carrying value in due course"; "filed its submission with BIS and awaiting further response" | FORWARD-SIGNAL | Three dateable open commitments: insurance recovery of Rs 1,435.81m (undated), BIS submission response (undated), and shareholder ratification of the 5-yr secretarial-auditor term at the ensuing AGM. Feed the promise-vs-delivery tracker. |
| A3-05 | F7 | note 3 | 557-558 | "recovery of loss could not be ascertained" ; "The assessment of the loss is currently in progress" | AMBIGUOUS | Pre-emptive hedge: no insurance recovery is recognised and none is quantified. Next quarter may still carry an unrecovered Rs 143.581 Cr hole if the surveyor assessment drags; direction is bear until a claim number lands. |
| A3-06 | F8 | sec1 row 18 | 492-493 | "Income tax relating to earlier period   -   -   1.04   1.04" | NEUTRAL-FACT | Non-zero prior-period tax adjustment (Rs 1.04m) in FY26 columns triggers the F8 rule; immaterial. Separately, current tax of Rs 198.04m = 25.5% of post-fire PBT, i.e. the Rs 1,435.81m fire loss appears fully tax-deducted this quarter — any future insurance recovery will be taxable. |
| A3-07 | F9 | sec1 row 22 | 500-503, 508-509 | "Remeasurement gain / (loss) of defined benefit obligation plans   (2.47) ... (2.42)" | AMBIGUOUS | Single-quarter actuarial loss (Rs 2.47m, Q1FY27) EXCEEDS the entire prior full year (Rs 2.42m, FY26) — F9 assumption-change trigger. Verify discount-rate / plan-asset assumptions at the Annual Report. |
| A3-08 | F10 | sec1 row 26, 28-29 | 514-516, 520-522 | "Paid up equity share capital ... 306.90 ... 306.42"; Diluted "1.88 ... 2.40" | AMBIGUOUS | Paid-up capital rose Rs 0.48m (approx 4.8 lakh Re-1 shares) QoQ (306.42m -> 306.90m) with no corporate-action note in the filing; simultaneously the basic-vs-diluted EPS spread collapsed to nil (was 0.01-0.03 in prior periods). Suggests an instrument conversion/allotment not disclosed here. |
| A3-09 | F13 | sec3 item 4 / Annexure D | 84-89, 724-728 | "for a term of five (5) consecutive financial years ... subject to approval of shareholders in the ensuring AGM" | FORWARD-SIGNAL | An ensuing AGM is foreshadowed (secretarial-auditor 5-yr term needs ratification). Watch for the AGM notice / record date and any special or capital-raising resolutions riding with it. No AR/Board's-Report/MD&A/dividend/director item present. |
| A3-10 | F14 | note 3 vs EoM x2 | 554 vs 189/282 | note 3: "On 06 May 2025. a mayor fire broke out"; EoM: "06 May 2026" | AMBIGUOUS | Internal date inconsistency: note 3 body dates the fire "06 May 2025" while both auditor EoM paragraphs and the quarter context say "06 May 2026." Near-certain typo/OCR, but an uncorrected drafting inconsistency on a material exceptional item — governance data point. |
| A3-11 | F15 | sec7 entity list / note 5 | 270-272, 572-581 | "Zayo Cables Private Limited ... Associate Company w.e.f 25 April 2026"; "acquired 3,100 equity shares of face value 210 each, representing 31%" | FORWARD-SIGNAL | First-ever consolidation: two 31% associates (Zayo Cables, Zayo Energy) added w.e.f. 25 Apr 2026. Acquisition CONSIDERATION is not disclosed (only 3,100 shares each at Rs 10 face); related-party / promoter-link status is not disclosed. New off-balance-sheet exposure to two "energy"/"cables" investees. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING | FINDING | 4 ZERO_STANDING rows read (13,15,18,27); Reserves (518) + prior-period tax (493) are interim boilerplate, but the pre-captioned "Loss due to fire in Bawal Plant" line (468) and the now-live "Share in loss of associates" line (474) are forward-relevant -> A3-01. |
| F2 STANDALONE vs CONSOL | FINDING | Gap = Rs 0.01m on PAT (std 57.795 vs consol 57.794 Cr, lines 497-498), driven 100% by associate-loss share (line 474); under 5pp mechanically but structurally new + comparatives are relabelled standalone -> A3-02. |
| F3 SHELL-ENTITY | PASS | All standalone and consolidated cost lines are identical (lines 455-462) because the two additions are 31% associates carried by equity method (Ind AS 28), NOT line-consolidated subsidiaries; no subsidiary, no Going Concern EoM -> no shell to reconcile. |
| F4 UNAUDITED CONTRIBUTION | PASS | Associate share of net loss = Rs 0.01m, ~0.002% of consol PAT (line 474) — far below the 10% trigger; consolidated auditor reviewed the Holding Co "and its share of the net loss ... of its associates" (lines 244-245), no separate component-auditor/unreviewed block. |
| F5 GOING CONCERN / EoM | FINDING | Bawal-fire EoM present in both reports (lines 188-193 / 281-286); no prior-quarter extract supplied so verbatim cross-quarter diff is impossible, but this is the fire's first reporting quarter = new EoM -> A3-03. Standalone says "the Company's", consolidated says "the holding company's"; Rs amount and scope identical. |
| F6 FORWARD-COMMITMENT | FINDING | Lexicon hits: "expect to recover ... in due course" (560), "in progress" (557), "awaiting further response" (568), "subject to approval of shareholders" (86) -> A3-04, commitment register below. |
| F7 HEDGE PHRASE | FINDING | Notes carry pre-emptive hedges: "recovery of loss could not be ascertained" (557-558) and "subject to approval" (86); the insurance-recovery hedge signals continued non-recognition -> A3-05. |
| F8 TAX FORENSICS | FINDING | ETR unremarkable (Q1FY27 25.5%, Q1FY26 24.9%, Q4FY26 26.2%, FY26 25.5% vs 25.17% statutory); non-zero "Income tax relating to earlier period" Rs 1.04m (line 493) triggers rule; fire loss appears fully tax-deducted -> A3-06. Deferred tax negligible (0.62m, line 494). Consol FY26 current tax reconciles to 885.52m only (885.52+1.04+152.48=1,039.04), independently confirming A1's cell resolution. |
| F9 OCI FORENSICS | FINDING | Q1FY27 actuarial remeasurement loss Rs 2.47m > full-year FY26 loss Rs 2.42m (lines 503) = single-quarter swing exceeds prior year -> assumption-change flag A3-07. |
| F10 SHARE COUNT / DILUTION | FINDING | Paid-up +Rs 0.48m QoQ unexplained (306.42m->306.90m, line 516); basic-vs-diluted EPS spread collapsed to nil in Q1FY27 (lines 520-522) -> A3-08. IPO-scale jump 280.10m->306.42m sits across the FY26 columns (comparatives from IPO-restated info). |
| F11 RESERVES / NET WORTH | PASS | Net worth ties: Reserves 12,427.14m + Paid-up 306.42m = 12,733.56m at 31-Mar-26 (lines 516, 518); interim columns show Reserves as "-" per convention; no third-party (rating/slide) figure in this filing to reconcile against. |
| F12 SEGMENT | PASS | Note 8 (lines 600-601): single reportable segment (SPGS), predominantly India; no segment-wise asset/liability/revenue table exists in the filing, nothing anomalous to trend. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Items 2-4 are re-appointments (internal auditor Rohit Garg, an employee; cost auditor Chandra Bhushan Kumar & Co.; secretarial auditor Raghav Bansal & Assoc.); item 4's 5-yr term needs AGM ratification, foreshadowing an AGM -> A3-09. No AR/dividend/director/capital-raise item. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Fire date "06 May 2025" (note 3, line 554) vs "06 May 2026" (both EoMs, 189/282) -> A3-10; note 5 "face value 210" (line 572) is OCR for Rs 10; "Fujlyama"/"INR 4/-" are raw-OCR artifacts (A1-verified corrects to Fujiyama / INR 1/-), not document inconsistencies. |
| F15 ENTITY LIST DIFFS | FINDING | Two entities added: Zayo Cables Pvt Ltd, Zayo Energy Pvt Ltd, 31% associates w.e.f. 25 Apr 2026 (lines 271-272, 572-581); first consolidation so no prior list to diff; consideration and related-party status undisclosed -> A3-11. |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype = results, not a presentation deck. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype = results, not a concall transcript. |

Tally: FINDING = 11 (F1,F2,F5,F6,F7,F8,F9,F10,F13,F14,F15) | PASS = 4 (F3,F4,F11,F12) | N.A. = 2 (F16,F17). Total 17, no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Recover insurance claim on Rs 1,435.81m fire-damaged carrying value | "in due course" (undated) | note 3, line 560 | underway (claim lodged, surveyor assessment in progress) |
| Insurance loss assessment / quantification | ongoing | note 3, line 557 | underway |
| BIS non-compliance dispute (Rs 24.50m + Rs 19m goods seized) — company submission | undated | note 4, lines 565-568 | underway (submission filed, awaiting BIS response) |
| Secretarial-auditor 5-yr appointment (FY27-FY31) ratification | ensuing AGM (FY27) | agenda item 4 line 86 / Annexure D lines 724-728 | proposed (pending shareholder approval) |

---

## MONITORING-CHECKLIST TEST (Notion, tested only where the filing can speak)

| # | Signal | Reading this filing | Verdict |
|---|--------|---------------------|---------|
| 1 | Revenue growth YoY (green >25% / red <15%) | Q1FY27 Rs 1,345.693 Cr vs Q1FY26 Rs 597.349 Cr = +125.3% (lines 450) | GREEN — no red |
| 2 | EBITDA margin (green >18% / red <15% x2) | PBEIT&tax 221.242 + Dep 25.017 + Finance 10.901 = 257.16 Cr; approx 19.1% of total income / 18.9% of revenue (lines 450-467). Fire loss sits BELOW this line. | GREEN — no red |
| 3 | CFO/PAT (annual) | No cash-flow statement in a results filing | N.A. in filing |
| 4 | Inventory days | No inventory balance disclosed; "Changes in inventories" (100.895) Cr = large inventory BUILD this quarter (line 456) but days not computable | N.A. (build noted) |
| 5-7 | Dadri DCR / on-grid mix / Ratlam ramp | Concall items | N.A. in filing |
| 8 | Net debt (red >600 / broken >700 Cr) | No borrowings/balance-sheet figure; finance cost Rs 10.901 Cr/qtr only (line 459) | N.A. in filing |
| 9 | CFO / senior-mgmt stability | No C-suite departure disclosed; results signed by JMD&CEO Yogesh Dua (line 611) and CS Mayuri Gupta; CFO Prashant Gupta neither confirmed nor exited | GREEN (no departure signal); note CFO did not sign |
| 10 | CRISIL credit-watch (Bawal fire) | Not referenced in filing | N.A. in filing |

THESIS-BROKEN TESTS: none fire. EBITDA margin ~19% (not <15%); no audit qualification (both conclusions unmodified — the fire is an EoM, not a qualification); no CFO exit disclosed; Bawal insurance claim NOT rejected (assessment in progress); DCR/CFO/inventory-2yr conditions not testable from a results filing. NO red monitoring trigger and NO thesis-broken condition fires on this document.

Standing watch items handed to A4 (not triggers, but pressure points): (a) fire exceptional Rs 143.581 Cr masked a strong operating quarter — PAT fell to Rs 57.795 Cr / EPS 1.88 from Rs 106.323 Cr / 3.58 in Q4FY26 despite +125% YoY revenue; (b) insurance recovery unrecognised and unquantified; (c) large inventory build Rs 100.895 Cr; (d) BIS seizures unquantified beyond seized-goods value; (e) undisclosed Zayo acquisition consideration and related-party status.

```yaml
stage: A3-forensics
company: "UTLSOLAR"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/utlsolar-q1fy27/work/forensics_results_utlsolar_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: FINDING
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: PASS
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "468-470,474", classification: "FORWARD-SIGNAL", implication: "Pre-captioned fire-loss exceptional line and now-permanent associate-share line will recur."}
  - {id: "A3-02", check: "F2", line: "474,476,497-498", classification: "FORWARD-SIGNAL", implication: "S-vs-C PAT gap immaterial now but structurally new; comparatives are relabelled standalone, gap widens as associates scale."}
  - {id: "A3-03", check: "F5", line: "188-193,281-286", classification: "CONFIRMATORY-NEGATIVE", implication: "First-appearance Bawal-fire EoM in both reports; standing until insurance/recovery settled."}
  - {id: "A3-04", check: "F6", line: "560,557,568,86", classification: "FORWARD-SIGNAL", implication: "Three dateable open commitments (insurance recovery, BIS response, AGM ratification)."}
  - {id: "A3-05", check: "F7", line: "557-558", classification: "AMBIGUOUS", implication: "Insurance recovery unrecognised/unquantified; next quarter may still carry the Rs 143.581 Cr hole."}
  - {id: "A3-06", check: "F8", line: "492-493", classification: "NEUTRAL-FACT", implication: "Rs 1.04m prior-period tax adjustment; fire loss fully tax-deducted so future insurance recovery is taxable."}
  - {id: "A3-07", check: "F9", line: "500-503", classification: "AMBIGUOUS", implication: "Single-quarter actuarial loss exceeds full prior year = assumption change; verify at Annual Report."}
  - {id: "A3-08", check: "F10", line: "514-516,520-522", classification: "AMBIGUOUS", implication: "Paid-up +Rs 0.48m QoQ unexplained and EPS spread collapsed to nil; possible undisclosed instrument conversion."}
  - {id: "A3-09", check: "F13", line: "84-89,724-728", classification: "FORWARD-SIGNAL", implication: "Ensuing AGM foreshadowed; watch AGM notice/record date and any special/capital-raise resolutions."}
  - {id: "A3-10", check: "F14", line: "554", classification: "AMBIGUOUS", implication: "Fire date 06 May 2025 (note 3) contradicts 06 May 2026 (both EoMs) — uncorrected drafting inconsistency on a material item."}
  - {id: "A3-11", check: "F15", line: "270-272,572-581", classification: "FORWARD-SIGNAL", implication: "First consolidation adds two 31% associates (Zayo Cables/Energy); acquisition consideration and related-party status undisclosed."}
forward_signals: ["A3-01","A3-02","A3-04","A3-09","A3-11"]
ambiguous: ["A3-05","A3-07","A3-08","A3-10"]
commitments:
  - {commitment: "Recover insurance claim on Rs 1,435.81m fire-damaged assets", implied_date: "in due course (undated)", ref: "note 3 line 560", status_word: "underway"}
  - {commitment: "Insurance loss assessment/quantification with surveyor", implied_date: "ongoing", ref: "note 3 line 557", status_word: "underway"}
  - {commitment: "BIS non-compliance dispute submission/response", implied_date: "undated", ref: "note 4 line 568", status_word: "underway"}
  - {commitment: "Secretarial-auditor 5-yr term ratification", implied_date: "ensuing AGM FY27", ref: "agenda item 4 line 86 / Annexure D line 724-728", status_word: "proposed"}
gate_a3: pass
blank_checks: []
```
