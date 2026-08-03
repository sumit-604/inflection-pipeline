# A3 FORENSIC NOTES — SAMHI Hotels Limited (SAMHI), Q1 FY27 — DOCTYPE: presentation (sub-class: press release, 4 pp.)

Source extract: `extract_pressrelease_samhi_q1fy27.txt` (234 lines, 4 pages, unit Millions, x0.1 to Rs Crore)
Ledger: `ledger_pressrelease_samhi_q1fy27.md` — every row read verbatim at its cited line; reconciliation 100%.
Prior-quarter extract: NONE supplied. Notion monitoring checklist: EMPTY (new company, no companies/SAMHI.md). No tripwires fabricated.

Doctype applicability note: this is a 4-page Reg 30 press release, not a full results filing and not a concall. It carries only two summary tables (consolidated financial highlights + debt profile), a management quote, and boilerplate. There is no standalone table, no auditor report, no notes to accounts, no OCI, no segment data, no share-count/EPS, no balance sheet. Accordingly F2, F3, F4, F5, F9, F10, F11, F12, F15, F17 are marked N.A. with reason. F1, F6, F7, F8, F13, F14 are run on the numbers the release does carry; F16 (presentation reframing) applies.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------|----------------|---------------------|
| A3-01 | F1 | §5 rows 5,6 (PARTIAL_DASH) | 118, 119 | "Exceptional Items — — 1,075" ; "Profit/(Loss) from discontinued ops — (28) (55)" | AMBIGUOUS | Template carries live Exceptional Items and Discontinued Ops lines. FY26 exceptional of Rs 1,075 Mn (likely GIC-transaction related) and the Caspia Delhi discontinued op (note 5, line 129) inflate the FY26 base; both anticipate recurrence at asset churn / GIC events. A4 to ask nature and recurrence of the FY26 Rs 1,075 Mn exceptional. |
| A3-02 | F8 | §5 rows 7,8 | 120, 121 | "PBT 327 231 ... 2,671" ; "PAT 249 192 ... 5,665" | FORWARD-SIGNAL | FY26 PAT (5,665) EXCEEDS FY26 PBT (2,671) by Rs 2,994 Mn — i.e. a net tax CREDIT of ~Rs 2,994 Mn (DTA recognition / carryforward or MAT-credit pickup). Reported FY26 PAT is structurally inflated; run-rate PAT bears full ~25% tax. Q1FY27 ETR = 78/327 = 23.9%, Q1FY26 = 39/231 = 16.9%. Future ETR step-up risk once the shield exhausts; the FY26 PAT of 5,665 is NOT a valuation anchor. |
| A3-03 | F14 | §7 mgmt_number 11 vs §4 bullet 6 / §6 row 3 | 188 vs 106 & 146 | "Net Debt to EBITDA at a comfortable ~3.0x" (line 188) vs "Net Debt to EBITDA is at ~3.2x" (line 106) vs table "3.2x" (line 146) | AMBIGUOUS | Verified NUMBER_DISCREPANCY. Table is arithmetically correct: 14,928 / 4,664 = 3.20x. The CEO's "~3.0x" is unsupported by any disclosed figure (not 3.2x, not the 2.4x growth-adjusted line). Either optimistic rounding or a drafting error in the headline quote. A4 to ask which leverage figure management stands behind. |
| A3-04 | F14 | §11 TEXT_ARTIFACT rows 1,2; §5/§6 rounding | 28/78/138/200; 145; 147; 74; 122; 222 | "IMART HOTEL INVESTMENTS—" / "—SNART HOTEL INVESTMENTS——"; "4,6642"/"4,7212"; "240"/"3.9¢"; "SAMHI Hotels Lid"; "Put. Ltd." | NEUTRAL-FACT | Verified TEXT_ARTIFACTs: garbled logo tagline (4 pages), footnote-digit fused onto TTM EBITDA (4,664/4,721) and growth-adjusted leverage cells (2.4x rendered "240", 3.9x as "3.9¢"), plus typos "Lid"/"Put.". Also a Rs 1 Mn foot: SAMHI 183 + Minority 67 = 250 vs PAT stated 249 (line 122-123 vs 121). Individually immaterial; cumulatively a proof-reading/governance data point on a single-purpose 4-page release. No numeric disclosure materially affected. |
| A3-05 | F6 | §7 quote paras 3-7 | 174-175, 178, 179-181, 185, 188-189 | "expected to increase the share of upscale inventory from ~41% to ~60% by FY2030" | FORWARD-SIGNAL | Six dated/dateable management commitments extracted (see Commitment Register). FY2030 upscale-mix ramp, proposed Marriott distribution partnership, RARE succession-capital investments, ~40% margin target, stable interest outflows. These seed the Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline; no prior deck exists to diff status transitions, so this establishes the baseline. |
| A3-06 | F7 | §7 quote para 2 | 169-170 | "The quarter witnessed some disruption to international travel due to the Middle East conflict" | AMBIGUOUS | Management newly surfaces an external demand hedge (geopolitical / international-travel softness), framed as offset by domestic resilience. On a press release this is pre-emptive narrative cover. No prior deck to confirm it is new. A4 to ask the RevPAR/occupancy exposure to international vs domestic mix and whether Q2 carries the same caveat. |
| A3-07 | F16 | §4 bullets 3,4; §5 row 3; §7 para 1; §6 columns | 100, 102, 116, 165-166, 142 | "up 10.8% YoY Comparable? and +7.3% YoY Reported" ; "up 12.1% YoY Comparable?, down 4.1% YoY Reported" ; margin "improved to 36.0% (excluding the GST impact)" | AMBIGUOUS | Reframing: the headline leads with favorable "Comparable"/"excluding GST" numbers while REPORTED EBITDA is down 4.1% (1,013 vs 1,056) and REPORTED EBITDA margin fell to 32.9% from 36.8% (line 116). "Comparable" excludes GIC one-timers and the ~Rs 92 Mn Q1FY27 GST ITC hit (note 4, line 128). Debt-profile columns skip to a Sep 30 2023 (IPO-era) baseline to frame the 5.3x -> 3.2x deleveraging (line 142/146), a favorable-baseline choice. No prior deck supplied, so dropped-metric diffing is a GAP, not clean. A4 to reconcile reported vs comparable bridges and confirm the GST ITC drag is one-time. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1  | FINDING | No strict all-period ZERO_STANDING row (A2 = 0), but the Exceptional Items and Discontinued-Ops PARTIAL_DASH lines (118/119) anticipate transaction classes; A3-01. |
| F2  | N.A. | Release discloses consolidated figures only; no standalone table despite the letter approving both — S-vs-C gap cannot be computed. |
| F3  | N.A. | No standalone vs consolidated cost lines (no cost breakup at all); shell detection impossible from a press release. |
| F4  | N.A. | No auditor report / Other Matters paragraph in a press release; component-auditor unaudited ratio undisclosed. |
| F5  | N.A. | No auditor Emphasis of Matter / Going Concern paragraph; nothing to verbatim-diff (and no prior quarter). |
| F6  | FINDING | Six forward commitments mined from the CEO quote (FY2030 upscale mix, Marriott, RARE, ~40% margin, stable interest); A3-05 + Commitment Register. |
| F7  | FINDING | Newly surfaced geopolitical/international-travel demand hedge (line 169) beyond standard safe-harbor boilerplate; A3-06. |
| F8  | FINDING | FY26 PAT (5,665) > PBT (2,671) => ~Rs 2,994 Mn net tax credit; quarterly ETRs 23.9% / 16.9% below statutory; future step-up risk; A3-02. |
| F9  | N.A. | No OCI / actuarial disclosure in a press release. |
| F10 | N.A. | No paid-up capital, share count, or basic/diluted EPS disclosed. |
| F11 | N.A. | No Other Equity / net-worth figures; only net debt disclosed. |
| F12 | N.A. | No segment assets/liabilities/revenue tables. |
| F13 | PASS | Reg 30 letter checked (lines 44-49): single-purpose results approval only; no AR/AGM/record date/dividend/director/auditor/ESOP item — consistent with doctype, nothing beyond results. |
| F14 | FINDING | Net Debt:EBITDA ~3.0x (line 188) vs 3.2x (lines 106/146) drafting inconsistency, plus TEXT_ARTIFACTs and Rs 1 Mn attributable-PAT foot; A3-03 + A3-04. |
| F15 | N.A. | No consolidation entity list in the release and no prior-quarter ledger to diff. |
| F16 | FINDING | Comparable/"excluding GST" reframing masks reported EBITDA -4.1% and margin fall to 32.9%; favorable Sep-2023 debt baseline; A3-07 (dropped-metric diff a noted GAP). |
| F17 | N.A. | Not a concall; no transcript. Monitoring checklist empty, so no silence audit possible/needed. |

Scorecard tally: FINDING x6 (F1, F6, F7, F8, F14, F16), PASS x1 (F13), N.A. x10 (F2, F3, F4, F5, F9, F10, F11, F12, F15, F17). No blank checks — GATE A3 pass.

---

## COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Note/line ref | Status word |
|---|------------|--------------|---------------|-------------|
| 1 | Increase upscale inventory share from ~41% to ~60% | FY2030 | line 174-175 ("expected to increase") | underway |
| 2 | Growth pipeline: ongoing hotel additions, rebranding, renovation | rolling / to FY2030 | line 174 ("remains on track, with ongoing") | underway |
| 3 | Proposed Marriott distribution partnership | undated (not yet executed) | line 178 ("the proposed Marriott distribution partnership") | initiated |
| 4 | Provide succession capital via small tactical investments in RARE leisure assets | undated | line 179-181 ("we intend to provide succession capital") | initiated |
| 5 | Support operating EBITDA margin of ~40% (via upscale mix, GST-unaffected) | medium-term, tied to #1 | line 185 ("is expected to support operating EBITDA margins of approximately 40%") | target |
| 6 | Interest outflows to remain stable; strengthen FCF | forward | line 188-189 ("interest outflows expected to remain stable") | target |

Baseline established for Role 5 tracker; no prior deck exists to score status transitions this run.

---

## RECONCILIATION & GAP NOTES
- Ledger rows read: all sections §1-§11, all table rows, all 11 mgmt_numbers, all 10 footnotes, both TEXT_ARTIFACT rows, all three PARTIAL_DASH rows — 100%.
- A2-surfaced items verified and line-cited: NUMBER_DISCREPANCY 3.0x/3.2x (A3-03), three PARTIAL_DASH rows (A3-01 covers exceptional/discontinued; growth-adjusted-leverage dash noted under A3-04 artifact/§6), TEXT_ARTIFACT garbled digits + logo (A3-04).
- GAPS (not defects, flagged for the file): (a) no prior-quarter deck => F16 dropped-metric and F15 entity diffs cannot be performed; (b) no standalone table => F2/F3 blocked; (c) no board-meeting start/end time => signature-timestamp cross-check (21:09:01 IST) cannot be assessed, per A2 §2.

---

```yaml
stage: A3-forensics
company: "SAMHI"
quarter: "Q1 FY27"
doctype: "presentation (press release)"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/samhi-q1fy27/work/forensics_pressrelease_samhi_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "118,119", classification: "AMBIGUOUS", implication: "FY26 exceptional Rs 1,075 Mn + Caspia Delhi discontinued op inflate the base; recurrence at asset churn/GIC events"}
  - {id: "A3-02", check: "F8", line: "120,121", classification: "FORWARD-SIGNAL", implication: "FY26 PAT 5,665 > PBT 2,671 = ~Rs 2,994 Mn net tax credit; run-rate PAT bears full tax; future ETR step-up; FY26 PAT not a valuation anchor"}
  - {id: "A3-03", check: "F14", line: "188", classification: "AMBIGUOUS", implication: "CEO ~3.0x leverage unsupported vs disclosed 3.2x (14,928/4,664); optimistic rounding or drafting error"}
  - {id: "A3-04", check: "F14", line: "145,147,74,122", classification: "NEUTRAL-FACT", implication: "TEXT_ARTIFACTs (logo, fused footnote digits), typos, Rs 1 Mn attributable-PAT foot; proof-reading/governance data point, no numeric disclosure impaired"}
  - {id: "A3-05", check: "F6", line: "174", classification: "FORWARD-SIGNAL", implication: "Six dated commitments seed Role 5 tracker/FTTCP timeline; FY2030 upscale ramp and ~40% margin target the key catalysts"}
  - {id: "A3-06", check: "F7", line: "169", classification: "AMBIGUOUS", implication: "Newly surfaced geopolitical/international-travel demand hedge; ask Q2 carry-forward and intl vs domestic exposure"}
  - {id: "A3-07", check: "F16", line: "102,116", classification: "AMBIGUOUS", implication: "Comparable/ex-GST reframing masks reported EBITDA -4.1% and margin 32.9% (vs 36.8%); favorable Sep-2023 debt baseline; reconcile bridges and confirm GST ITC one-time"}
forward_signals: ["A3-02", "A3-05"]
ambiguous: ["A3-01", "A3-03", "A3-06", "A3-07"]
commitments:
  - {commitment: "Upscale inventory share ~41% -> ~60%", implied_date: "FY2030", ref: "line 174-175", status_word: "underway"}
  - {commitment: "Growth pipeline: hotel additions, rebranding, renovation", implied_date: "rolling to FY2030", ref: "line 174", status_word: "underway"}
  - {commitment: "Proposed Marriott distribution partnership", implied_date: "undated", ref: "line 178", status_word: "initiated"}
  - {commitment: "Succession capital / tactical investments in RARE leisure assets", implied_date: "undated", ref: "line 179-181", status_word: "initiated"}
  - {commitment: "Operating EBITDA margin ~40%", implied_date: "medium-term", ref: "line 185", status_word: "target"}
  - {commitment: "Interest outflows stable; strengthen FCF", implied_date: "forward", ref: "line 188-189", status_word: "target"}
gate_a3: pass
blank_checks: []
```
