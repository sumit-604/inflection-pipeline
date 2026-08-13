# A3 FORENSIC NOTES — GE Power India Limited (GVPIL) — Q1FY27 — DOCTYPE: results

Source extract: `runs/gvpil-q1fy27/work/extract_results_gvpil_q1fy27.txt` (621 lines, 9 pages, Rs Millions, x0.1 -> Rs Crores).
Reconciliation contract: `runs/gvpil-q1fy27/work/ledger_results_gvpil_q1fy27.md`.
Ledger rows read verbatim at cited line: 100% (all 10 A2 tables; 94 line items, 17 notes, 15 zero-standing, 10 auditor paras, 2 entities, 5 signature blocks, 8 media-release units).
Prior-quarter extract: NONE (NO_PRIOR_LEDGER) — F5 cross-quarter EoM diff and F15 entity diff cannot be run this cycle.
A2 flagged artifacts re-verified against arithmetic / source: 5 OCR_ARTIFACT, 2 FORMATTING_GAP, 1 NOTE_NUMBERING_GAP — dispositions below. None resolves to a source misstatement; all are extraction-layer. The extract remains the citation spine.

Doctype applicability: results filing -> F1-F15 apply, F16/F17 = N.A. Every check carries a status; none blank (GATE A3).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | short verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------------|----------------|---------------------|
| A3-F2-01 | F2 | Table 8 item 6 (JV share of profit) | L443 | "Share of profit of Joint Venture (net of tax) 11.8 106.0 30.0 161.7" | AMBIGUOUS | S-vs-C PAT gap collapsed from 10.3% of standalone PAT (Q4FY26) to 2.2% (Q1FY27), an 8.1pp narrowing; the entire gap is the NTPC GE JV equity pick-up, and JV profit fell 89% QoQ (106.0->11.8) and 61% YoY (30.0->11.8). JV earnings deteriorating or lumpy — A4 question. |
| A3-F3-01 | F3 | Table 8 items 4a-4f vs Table 6 items 4a-4f | L434-440 vs L182-188 | "Total expenses (4) 2,717.5" (consol) identical to standalone "Total expenses (4) 2,717.5" | NEUTRAL-FACT | Consolidated cost lines equal standalone to the rupee (materials 1,873.7=1,873.7; employees 406.1=406.1; depreciation 32.7=32.7). Subsidiary GE Power Boilers Services Ltd is a shell — zero incremental operations; consol differs from standalone only by the one-line JV equity pick-up. |
| A3-F6-01 | F6 | Table 7 note 2(i) / Table 9 note 3(i) | L238-239 / L496-497 | "The management expects the transaction to be completed within twelve months from the end of the reporting period." | FORWARD-SIGNAL | Durgapur demerger to JSW Energy is a dated commitment: completion window ~by 30 Jun 2027 (12 months from 30 Jun 2026), status "underway" (board-approved 18 Sep 2025, appointed date 1 Jul 2025, pending approvals incl. NCLT). Feeds Role 5 promise-vs-delivery and FTTCP catalyst timeline; maps to Notion trigger #6 (NCLT Durgapur). |
| A3-F8-01 | F8 | Table 6 items 7-1/7-2 (tax) | L196-197 | "1) Current tax 28.3" (against continuing PBT 688.2); "2) Deferred tax charge/ (credit) . - - -" | FORWARD-SIGNAL | Continuing-ops ETR = 28.3/688.2 = 4.1% vs 25.17% statutory (Q4FY26 1.8%, Q1FY26 0%, FY26 2.0%); deferred tax persistently NIL across all four periods. Shield ~2,100 bps / ~Rs 145m of tax deferred this quarter. Reliance on brought-forward loss set-off -> future ETR step-up risk when carryforwards exhaust; earnings quality caveat for the "clean" quarter. |
| A3-F11-01 | F11 | Table 6 items 17-18 / Table 8 items 19-20 | L217-219 / L473-475 | "Other equity as per audited balance sheet ... 4,765.4" + "Paid-up equity share capital ... 672.3" | AMBIGUOUS | Standalone net worth FY26 = 4,765.4 + 672.3 = Rs 543.77 Cr (ties Notion "Rs 544 Cr FY26 filing"); consolidated = 5,153.1 + 672.3 = Rs 582.54 Cr. Notion deck figure Rs 483 Cr is ~Rs 61 Cr / 11% below the filing — exceeds 5% gate. Candidate reconcilers: JV/subsidiary equity-method reserves (S-to-C Rs 38.8 Cr), held-for-sale reserve carve-out, or a stale/pre-audit deck date. A4 reconciliation question. |
| A3-F14-01 | F14 | Table 7 note 2(ii) footnote vs Table 9 note 3(ii) footnote; Table 9 note 1 | L264 vs L522; L486 | standalone footnote unmarked "Revenue from operations of the Durgapur undertaking..." vs consolidated "• Revenue from operations of the Durgapur undertaking..." | NEUTRAL-FACT | Cross-version drafting asymmetry: identical footnote is unmarked in the standalone but bullet-marked in the consolidated; consolidated note 1 (L486) carries no leading numeral. Individually immaterial; cumulatively a note-drafting/QC data point. Flag for verification at the source PDF; no numeric impact. |

---

## CHECKLIST SCORECARD (all 17)

| # | Status | One-line basis |
|---|--------|----------------|
| F1 | PASS | All 15 ZERO_STANDING rows are canonical annual-only template lines — exceptional items (L193/203/447/457, populated only in FY26 for labour-code provision note 3/4 and are nil in every quarter column), deferred tax (L197/207/451/461), tax-adjustments-earlier-years (L208/462), income tax on OCI (L470), other equity (L219/475). No orphan line anticipates an undisclosed transaction. The discontinued-ops exceptional line (L203/457) is the placeholder for any future Durgapur demerger disposal result — cross-ref A3-F6-01. |
| F2 | FINDING | A3-F2-01: S-vs-C PAT gap narrowed 8.1pp (10.3%->2.2% of standalone PAT) driven by JV pick-up collapse 106.0->11.8; exceeds the 5pp gate. |
| F3 | FINDING | A3-F3-01: subsidiary GE Power Boilers Services Ltd is a shell — consolidated cost lines identical to standalone to the rupee; consol-only delta is the JV equity line. Clean unmodified opinion, no going-concern EoM to reconcile against. |
| F4 | PASS | Other Matters para 6 (L385-392): JV unreviewed-by-principal-auditor contribution = Rs 11.8m PAT = 2.2% of consolidated PAT 537.3, below the 10% gate; trend is DOWN (Q4FY26 9.4%, Q1FY26 8.6%, FY26 6.4%) — no jump. |
| F5 | PASS | No going-concern or Emphasis-of-Matter paragraph in either report; standalone LR is 4 clean paras (L109-140), consolidated adds only a standard Other Matters JV-reliance para (L385-395). Nothing to track; NO_PRIOR_LEDGER prevents a diff but there is no EoM/GC language to diff. |
| F6 | FINDING | A3-F6-01: Durgapur demerger completion "within twelve months" (L238-239/L496-497) is a dateable commitment; plus completed-status items (depreciation discontinued 18 Sep 2025; BHEL obligations closed). See Commitment Register. |
| F7 | PASS | No hedge-lexicon term ("no assurance", "evaluating", "exploring", "in discussions", "endeavour") newly added in the notes; the only conditionality is the standard "post receipt of certain approvals" on the demerger (L238/L496), already captured under F6. No newly-added revenue-lumpiness or customer-concentration hedge. |
| F8 | FINDING | A3-F8-01: continuing-ops ETR ~4% vs 25.17% statutory, deferred tax persistently nil; ~2,100 bps shield, future step-up risk. Tax-adjustments-earlier-years is -0.6 in FY26 annual only (L208/L462), nil in every quarter column incl. Q1FY27 — immaterial, folded into finding. |
| F9 | PASS | Remeasurement of defined-benefit liability (L213-215/L467-471): Q1FY27 net OCI 4.0 vs prior full-year 134.3 (S) / 132.8 (C). No single-quarter swing exceeds the prior full year; no assumption-change signature. |
| F10 | PASS | Paid-up capital 672.3 in every period, standalone and consolidated (L217-218/L473-474); no corporate action. EPS labelled "Basic and diluted" throughout (L221-224/L477-480) — zero basic-vs-diluted spread, no dilutive instruments. |
| F11 | FINDING | A3-F11-01: filing net worth (std Rs 543.8 Cr / consol Rs 582.5 Cr) vs Notion deck Rs 483 Cr = ~11% gap, above the 5% gate; reconcilers listed. |
| F12 | N.A. | Single reportable operating segment per Ind AS 108 — "Power Generation equipment and related services" (note 5 L283-286 / note 6 L542-545). No segment-level asset/liability disclosure in the interim filing; no multi-segment trend to test. |
| F13 | PASS | Board meeting (L51-53, L63) approved only Q1 results and noted the LR report. A2 Table 1 row 4 confirms manual sweep: no AR approval, no AGM notice, no record date, no dividend, no director appointment/resignation, no auditor change, no capital-raising enabling resolution. No Role 6 AR event triggered by this outcome. (Note: CFO Rojal appointment w.e.f. 19-Jun-26 per Notion was a prior intimation, not in this board outcome; results are signed by MD Puneet Bhatla alone, L305/L560.) |
| F14 | FINDING | A3-F14-01: footnote-marker asymmetry (standalone unmarked L264 vs consolidated bulleted L522) and consolidated note 1 missing numeral (L486). Note text ("subjected to limited review... unmodified conclusion", L288-290/L546-548) is consistent with the auditor's Limited Review Report — no audit/LR mislabel. |
| F15 | N.A. | NO_PRIOR_LEDGER: entity add/remove/rename/relationship diff cannot be performed this cycle. Current consolidation list (Table 5): GE Power Boilers Services Ltd (subsidiary, L365/L486-487), NTPC GE Power Services Pvt Ltd (JV, L366/L487). Baseline captured for next quarter's diff. |
| F16 | N.A. | Presentation-specific; this is a results filing (no investor deck in the extract). Note for continuity: the bundled Media Release (L590-592) does carry order backlog INR 15,454m, down 41.4% YoY, "driven by termination of two FGD EP contracts, Jaypee Bina and Nigrie amounting to INR 7,749 million" — order-book/FGD data usable by A4 but no prior deck exists to diff a dropped/reframed metric. |
| F17 | N.A. | Concall-specific silence audit; no transcript in this doctype. Cross-ref for A4: the Media Release addresses Notion checklist items on order-book mix and FGD (backlog -41.4%, FGD EP contracts terminated -> Notion "FGD dead" reaffirmed, thesis-broken trigger #1 "reversion to EPC/FGD" NOT activated), but the checklist items on cash position (~Rs 880 Cr), capital allocation, receivable days, and CFO succession are not addressable from a bare results filing — these run against the Q1FY27 concall when available. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Complete demerger/transfer of Durgapur facility to JSW Energy (held-for-sale, discontinued ops) | Within 12 months of 30 Jun 2026 (~by 30 Jun 2027); appointed date 1 Jul 2025 | note 2(i) L238-239 / note 3(i) L496-497 | underway (board-approved 18 Sep 2025; "post receipt of certain approvals" incl. NCLT) |
| Discontinue depreciation on tangible assets of demerged business (Ind AS 105) | Effective 18 Sep 2025 | note 2(i) L243 / note 3(i) L501 | completed |
| BHEL settlement — receive Rs 3,400m and close all mutual obligations | FY26 (Rs 3,430.6m received incl. FX) | note 4 L273-281 / note 5 L532-540 | completed ("all obligation... stand closed... fully released and discharged") |

---

## FORENSIC NARRATIVE (compact)

1. The consolidation is standalone plus a one-line JV equity pick-up. Every consolidated cost line equals the standalone to the rupee (F3), so the subsidiary is dormant and the ONLY consolidation dynamic worth watching is the NTPC GE JV, whose contribution just fell to Rs 11.8m from Rs 106.0m last quarter (F2). Lean-bear read: watch JV order/execution; ask management whether the Q1 JV figure is timing or a step-down.

2. Earnings quality caveat for the headline "clean" quarter: continuing-ops tax is ~4% ETR on brought-forward losses with zero deferred tax (F8). The MD quote (L596-604) stresses margins came "without the aid of any exceptional or one-time items," and the P&L confirms nil exceptional in all quarter columns — but Q1FY27 other income is Rs 318.8m (9.4% of income) and Q4FY26 "Other expenses" of only 18.6 (L187/L439) was depressed by the BHEL ECL reversal (note 4/5), so QoQ margin optics are distorted by that reversal, not the current quarter.

3. Balance-sheet reconciliation open: filing net worth ~Rs 544 Cr (std) vs Notion deck Rs 483 Cr — an 11% gap A4 must resolve (F11).

4. Governance/QC: minor cross-version drafting asymmetries (F14); results signed by MD alone with no CFO countersignature amid the CFO transition (context only, not a finding).

---

```yaml
stage: A3-forensics
company: "GVPIL"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "runs/gvpil-q1fy27/work/forensics_gvpil_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: FINDING
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F2-01", check: "F2", line: "443", classification: "AMBIGUOUS", implication: "S-vs-C PAT gap narrowed 8.1pp (10.3%->2.2%); NTPC GE JV pick-up collapsed 106.0->11.8 (-89% QoQ, -61% YoY) - JV earnings deteriorating/lumpy; A4 question"}
  - {id: "A3-F3-01", check: "F3", line: "434-440", classification: "NEUTRAL-FACT", implication: "Subsidiary GE Power Boilers Services Ltd is a shell; consolidated cost lines identical to standalone; consol delta is JV equity line only"}
  - {id: "A3-F6-01", check: "F6", line: "238-239", classification: "FORWARD-SIGNAL", implication: "Durgapur demerger to JSW Energy dated to complete ~by 30 Jun 2027; NCLT/approval catalyst; feeds Role 5 tracker and FTTCP timeline (Notion trigger #6)"}
  - {id: "A3-F8-01", check: "F8", line: "196-197", classification: "FORWARD-SIGNAL", implication: "Continuing ETR ~4% vs 25.17%, deferred tax persistently nil, ~2,100 bps shield on brought-forward losses; future ETR step-up risk to reported earnings"}
  - {id: "A3-F11-01", check: "F11", line: "219", classification: "AMBIGUOUS", implication: "Filing net worth Rs 543.8 Cr (std)/Rs 582.5 Cr (consol) vs Notion deck Rs 483 Cr = 11% gap; reconcile JV reserves/HFS carve-out/deck date; A4 question"}
  - {id: "A3-F14-01", check: "F14", line: "264", classification: "NEUTRAL-FACT", implication: "Cross-version footnote-marker asymmetry (L264 unmarked vs L522 bulleted) and consolidated note 1 missing numeral (L486); immaterial QC data point, verify at source"}
forward_signals: ["A3-F6-01", "A3-F8-01"]
ambiguous: ["A3-F2-01", "A3-F11-01"]
commitments:
  - {commitment: "Complete demerger/transfer of Durgapur facility to JSW Energy", implied_date: "within 12 months of 30 Jun 2026 (~by 30 Jun 2027); appointed date 1 Jul 2025", ref: "note 2(i) L238-239 / note 3(i) L496-497", status_word: "underway"}
  - {commitment: "Discontinue depreciation on tangible assets of demerged business (Ind AS 105)", implied_date: "effective 18 Sep 2025", ref: "note 2(i) L243 / note 3(i) L501", status_word: "completed"}
  - {commitment: "BHEL settlement - receive Rs 3,400m and close all mutual obligations", implied_date: "FY26 (Rs 3,430.6m received)", ref: "note 4 L273-281 / note 5 L532-540", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
