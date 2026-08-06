# A3 FORENSIC NOTES — RateGain Travel Technologies Limited (RATEGAIN), Q1 FY27, Doctype: RESULTS

Source extract: /home/user/inflection-pipeline/runs/rategain-q1fy27/work/extract_results_rategain_q1fy27.txt
Source ledger: /home/user/inflection-pipeline/runs/rategain-q1fy27/work/ledger_results_rategain_q1fy27.md
Unit convention: figures printed in Rs million; x0.1 = Rs crore. Statutory tax 25.17%.
Coverage: 100% of A2 ledger rows read verbatim at cited lines before judging (Board 2 + standing 8; Annexure B 4; signatures 5; auditor paras 5+6; entities 18; standalone P&L 24; consolidated P&L 33; PPA 7; standalone notes 10; consolidated notes 12).
Prior-quarter context: NONE in repo (first-time coverage, no companies/RATEGAIN.md, no prior ledger). All EoM/entity/guidance diffs are flagged where a prior-quarter baseline is REQUIRED but UNAVAILABLE.
Doctype applicability: F1-F15 apply; F16 (presentation) and F17 (concall) = N.A.

This is a transformative-acquisition quarter: Sojern Inc. and its 9-entity foreign chain (acquired 06 Nov 2025, Rs 22,220.83 mn / USD 250.92 mn) consolidated for the full period. Consolidated results are NOT comparable to prior periods (management's own caveat, line 617-618). Read every consolidated YoY number through that lens.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------------|----------------|---------------------|
| A3-F1 | F1 | §7 row 10 / §8 rows 10,24,26,28 | 201, 506, 535 | "Exceptional items (Refer Note 9/10) — " (nil all Q); NCI "-" | FORWARD-SIGNAL | Exceptional-items line is LIVE (FY26 carried 47.94 std / 346.18 consol for Sojern deal + Labour Code costs). Nil this quarter, but Sojern integration ongoing and the HK-subsidiary liquidation (10 Jul 2026) can re-activate it. NCI lines nil in every period = no minority structure today; any future partial stake would surface here. |
| A3-F2 | F2 | §7 row 15 vs §8 row 15 | 209, 515 | Std PAT "42.09" vs Consol PAT "949.10" (Q1FY27) | FORWARD-SIGNAL | Consolidated PAT is 22.5x standalone; standalone PAT is only 4.4% of consolidated. Standalone PAT COLLAPSED YoY 180.55 -> 42.09 (-77%) while consolidated DOUBLED 469.32 -> 949.10 (+102%). Group profit is now almost entirely subsidiary/Sojern-sourced. Gap-to-standalone-PAT widened from ~160% (Q1FY26) to ~2,155% (Q1FY27) — far beyond the 5pp threshold. Parent-level earnings power is thin and shrinking. |
| A3-F6 | F6 | §1 row 2 / §11 Note 9 | 42-43, 693-696, 649 | "will issue a corporate guarantee for an amount of upto USD 65.00 million"; "credit facility to be availed by"; "would provide for these developments appropriately" | FORWARD-SIGNAL | Two dateable commitments: (1) new bank debt at RateGain UK + Sojern to be drawn from HSBC/JP Morgan/CITI, parent to guarantee USD 65M — subsidiary leverage rising near-term; (2) Labour Code cost provisioning still open-ended and undated. |
| A3-F7 | F7 | §2 row 4 / §11 Note 5 | 699-703, 617-618 | "The Company does not foresee any impact of such guarantee"; "not comparable with the other corresponding period" | AMBIGUOUS | Pre-emptive legal cover on a USD 65M contingent liability, plus a comparability disclaimer that pre-frames consolidated growth as acquisition-driven, not organic. Reassurance language usually precedes the risk it disclaims. Question for A4. |
| A3-F8 | F8 | §8 rows 11-14 / §9 row 6 | 508-513, 607 | Consol tax "256.45" on PBT "1,205.55" = 21.27% ETR; PPA "Deferred tax liability on intangible assets recognised 1,307.89" | AMBIGUOUS | Consolidated ETR 21.27% is ~390 bps below statutory 25.17%; Q1FY27 shows a deferred-tax CHARGE (54.07) at Group vs a persistent deferred-tax CREDIT standalone (2.68). The PPA created a Rs 1,307.89 mn (Rs 130.79 cr) DTL on intangibles that reverses over 6-7 yrs (customer rel. 7y, trademarks 7y, software 6y) — a future ETR variable and amortisation drag. ETR trajectory ambiguous (foreign mix vs DTL reversal). |
| A3-F9 | F9 | §8 rows 19-21 | 524-527 | "Exchange differences on translation of foreign operations 116.17" (FY26: 1,245.83; Q4FY26 alone: 745.66) | FORWARD-SIGNAL | Actuarial remeasurement is benign (2.23 vs FY26 8.92, no assumption-change swing). But post-Sojern the consolidated OCI is now DOMINATED by FX translation: Rs 116.17 mn this quarter, Rs 1,245.83 mn in FY26, Rs 745.66 mn in a single prior quarter. Comprehensive income is now materially currency-driven; USD/INR moves will swing book equity. |
| A3-F10 | F10 | §7 row 20 / §10-11 Notes 6/7 & 4/5 | 218, 545, 258-260 | Paid-up flat "118.36 / 118.10 / 118.01"; yet "money raised by the way of Qualified Institutional Placement... amounting to 11,151.20 million" | AMBIGUOUS | EPS basic/diluted spread is narrow and stable (consol 8.03/8.02) and the +0.26 mn paid-up rise traces cleanly to 260,133 ESOP shares (18 Jun 2026). BUT a referenced Rs 11,151.20 mn (Rs 1,115 cr) "QIP/internal funds" leaves NO visible footprint in paid-up capital across periods spanning the Nov-2025 acquisition (+0.09 mn only). Reconcile whether QIP was equity at parent (and pre-dates shown periods) or was substantively "internal funds." Question for A4. |
| A3-F13 | F13 | §1 row 2 (Board agenda item 2) / Annexure B | 40-48, 693-696 | "the Company has also approved issuance of Corporate Guarantee of up to USD 65.00 million" | FORWARD-SIGNAL | Board action BEYOND the results: parent to guarantee USD 65M of new bank facilities for RateGain UK + Sojern. Signals fresh subsidiary debt (possible refinancing of the USD 125M Sojern acquisition loan) and rising contingent leverage. No AR/AGM/dividend/director item this quarter — no Role 6 AR event triggered. |
| A3-F14 | F14 | §5 (consol auditor) para 6 vs para 4 | 370, 393-403 | Para 4 "includes the results of the entities listed in Annexure A"; para 6 carves out ONLY the Trust ("total revenue of NIL... net loss 0.004 million") | AMBIGUOUS | The consolidated review report provides NO component-auditor Other Matter for the 9 newly-acquired foreign Sojern entities (US, Mexico, Singapore, MENA/UAE, HK, Germany, Nrejos SARL); the sole carve-out is the Rs 0.004 mn Trust. Unusual for a just-acquired foreign group. Did Deloitte review all Sojern subs directly, or is component-auditor reliance undisclosed? Prior-quarter auditor-para diff UNAVAILABLE (first coverage). Question for A4. |
| A3-F15 | F15 | §6 rows 4,7,15,16 / §11 Note 12 | 437-438, 443-445, 461-462, 463-464, 660-661 | "Sojern Hong Kong Limited (Liquidated w.e.f. July 10, 2026)"; "Nrejos SARL"; "Formerly Known As MyHotelShop / Sojern MENA DMCC"; "BCV Social LLC merged into RateGain Adara Inc." | FORWARD-SIGNAL | Five entity changes: 2 renames (MyHotelShop->RateGain Germany; Sojern MENA DMCC->FZCO), 1 merger (BCV Social, w.e.f. 1 Apr 2025), 1 post-quarter liquidation (Sojern HK, 10 Jul 2026 — a liquidation gain/loss may hit a future period), and note the reverse-named "Nrejos SARL" (= "Sojern" spelled backwards) — verify function/substance. Prior-quarter entity ledger UNAVAILABLE (first coverage); additions/deletions cannot be asserted, only in-document self-disclosures. |

Checks with no finding: F3, F4, F5, F11, F12 = PASS (bases below). F16, F17 = N.A.

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINES | FINDING | Exceptional-items line live in FY26 (47.94 std / 346.18 consol), nil this Q but re-activatable via Sojern integration + HK liquidation; 3 NCI lines nil every period = no minority structure (lines 201, 506, 535). |
| F2 STANDALONE vs CONSOLIDATED | FINDING | Consol PAT 949.10 = 22.5x standalone 42.09; gap-to-standalone-PAT widened 160% -> 2,155% YoY; standalone PAT -77% while consol +102% (lines 209, 515). |
| F3 SHELL-ENTITY DETECTION | PASS | Cost lines differ massively standalone vs consol (employee 518.88 vs 2,947.60; D&A 12.69 vs 375.18) — subsidiaries have real operations, no cost-identity shell signal; entity-level financials not in this filing; no Going Concern EoM (lines 194-500). |
| F4 UNAUDITED CONTRIBUTION | PASS | Only un-reviewed-by-Deloitte item is the Trust: revenue NIL, net loss Rs 0.004 mn = 0.0004% of consol PAT, far below 10% (lines 393-403). (Component-auditor absence on foreign subs raised under F14.) |
| F5 GOING CONCERN / EoM | PASS | No Going Concern para, no Emphasis of Matter; sole Other Matter is Trust carve-out (unmodified conclusion). Prior-quarter verbatim diff UNAVAILABLE (first coverage) — flagged, not asserted (lines 121-151, 372-403). |
| F6 FORWARD-COMMITMENT MINING | FINDING | "will issue a corporate guarantee... USD 65.00 million" (693); "to be availed by" (43); "would provide for these developments appropriately" (649). |
| F7 HEDGE PHRASE MINING | FINDING | "does not foresee any impact of such guarantee" (699); "not comparable with the other corresponding period" (617) — pre-emptive cover + comparability disclaimer. |
| F8 TAX FORENSICS | FINDING | Consol ETR 21.27% vs 25.17% (~390 bps shield); persistent std deferred-tax credits vs consol charge; PPA DTL Rs 1,307.89 mn reverses over 6-7 yrs. No "earlier-years" tax adjustment line present (lines 508-513, 607). |
| F9 OCI FORENSICS | FINDING | Actuarial benign (2.23 vs FY26 8.92); FX-translation OCI now dominant (Q1FY27 116.17; Q4FY26 745.66; FY26 1,245.83) — post-Sojern currency exposure (lines 519-527). |
| F10 SHARE COUNT & DILUTION | FINDING | Paid-up +0.26 mn traces to 260,133 ESOP shares; EPS spread narrow/stable; BUT referenced Rs 11,151.20 mn QIP has no visible paid-up footprint — reconcile (lines 218, 258-260, 545). |
| F11 RESERVES / NET WORTH | PASS | Std other equity 14,148.01 + paid-up 118.10; consol 19,940.45 + 118.10; other equity blank in Q columns (standard). No third-party net-worth number in this filing to tie a >5% gap against (lines 219, 546). |
| F12 SEGMENT FORENSICS | PASS | Single reported segment (Ind AS 108) per std Note 5 / consol Note 6; no segment asset/liability disclosure to trend (lines 267, 625). |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | Agenda item 2 = approval of USD 65M corporate guarantee for new RateGain UK + Sojern bank facilities; no AR/AGM/dividend/director item this Q (lines 40-48). |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Consol review report gives no component-auditor Other Matter for 9 foreign Sojern subs — only Rs 0.004 mn Trust carved out (lines 370, 393-403). (OCR "s"/UDIN garbles are extraction artifacts, excluded.) |
| F15 ENTITY LIST DIFFS | FINDING | 2 renames, 1 merger, 1 post-quarter liquidation (Sojern HK), reverse-named Nrejos SARL; prior-quarter entity baseline UNAVAILABLE (lines 437-464, 660-661). |
| F16 PRESENTATION-SPECIFIC | N.A. | Doctype = results, not a presentation deck. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype = results, not a concall transcript; no Notion checklist (first coverage). |

GATE A3: pass (17/17 marked, no blanks).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Issue corporate guarantee up to USD 65M to HSBC/JP Morgan/CITI for RateGain UK + Sojern facilities | Near-term (post board approval 06 Aug 2026) | Board letter line 42-43; Annexure B line 693-696 | initiated (board-approved) |
| Draw new bank credit facilities at RateGain UK + Sojern | Future ("to be availed") | line 43, 696 | initiated |
| Provide for further Labour Code developments "appropriately" | Undated / open | consol Note 9 line 649 (std Note 8 line 298) | underway (monitoring) |
| Sojern Inc. acquisition (100% equity) | Completed 06 Nov 2025 | std Note 4 line 256 / consol Note 5 line 588 | completed |
| Finalise Sojern working-capital adjustment (-Rs 6.36 mn consideration/goodwill) | This quarter | line 261 / 592 | completed |
| Liquidate Sojern Hong Kong Limited | Completed w.e.f. 10 Jul 2026 (subsequent) | consol Note 12 line 660-661; Annexure A row 16 line 463 | completed |
| Issue 37,453 ESOP shares | Completed 28 Jul 2026 (subsequent) | Note 6/7 line 276, 634 | completed |

---

## PRIOR-QUARTER GAPS FLAGGED (baseline required, UNAVAILABLE this run)
- F5: no prior EoM/Going-Concern paragraph to verbatim-diff.
- F14: no prior auditor Other-Matter paragraph to diff (component-auditor question stands open).
- F15: no prior entity ledger; only in-document self-disclosed changes captured. Recommend A4 request FY26 Q4 filing + FY26 Annual Report to establish the Sojern-chain baseline and confirm the component-auditor structure.

## SOUTHWEST-CLASS SWEEP (task-directed items, all accounted)
- Zero-value profit-on-sale line: no dedicated line; exceptional-items line is the catch-all (F1). Sojern HK liquidation may generate a future gain/loss there.
- Standalone-vs-consolidated PAT gap: F2 (22.5x, widening).
- Shell/new subsidiary: F3 (no cost-identity shell), F15 (Nrejos SARL reverse-name, 9-entity Sojern chain).
- Board agenda beyond item 1: F13 (USD 65M guarantee).
- Forward-commitment phrases in notes: F6.
- OCI/actuarial swings: F9 (FX translation dominance; actuarial benign).
- Deferred-tax movements: F8 (Rs 1,307.89 mn DTL; 390 bps ETR shield).
- USD 65M corporate guarantee: F6 / F13.
- Exceptional-items line: F1.
