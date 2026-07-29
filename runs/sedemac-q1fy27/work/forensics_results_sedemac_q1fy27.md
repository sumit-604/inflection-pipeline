# A3 FORENSIC NOTES — SEDEMAC Mechatronics Ltd — Q1 FY27 — DOCTYPE: results

Inputs read: extract_results_sedemac_q1fy27.txt (312 lines), ledger_results_sedemac_q1fy27.md (Tables 1-7).
Ledger reconciliation: 100% — every row in A2 Tables 1-7 read verbatim at its cited line in the A1 extract before judging.
Applicability (per instruction, results filing): F1-F15 apply; F16 and F17 are N.A.

Standing thesis context carried inline (not evidence): Decision Status AVOID/EXCLUDED at CMP ~Rs1,971 (~84x FY26 EPS); entry zone Rs720-920; destination PE 28-32x. THIS FILING IS MASTER GATE #2 — cash-conversion leg previously flagged DETERIORATING; FTTCP DEEP WATCH.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F8 | F8 Tax | Table 3 / Note 3 (line 192, 285-286) | 285-286 | "Income tax expense for the quarter ended 30 June 2026 includes a reversal of excess tax provision pertaining to earlier years amounting to INR 2.98 crores" | FORWARD-SIGNAL | Reported ETR 19.4% (8.03/41.34) sits ~580bps below statutory 25.17% only because a one-off Rs2.98cr prior-year reversal is buried in current tax. Ex-reversal ETR ~26.6%. The reversal adds ~2.98cr = ~9% of the 33.31cr PAT. YoY "PAT +95%" (17.07→33.31) is substantially a tax-rate artifact: Q1FY26 ETR was 43.4% (deferred tax 8.10 on PBT 30.17) vs 19.4% now. Underlying PBT grew only +37% (30.17→41.34). ETR normalises up next quarter → EPS quality this quarter overstated. |
| F9 | F9 OCI | Table 3 (line 200) | 200 | "Remeasurements of defined benefit obligations (1.58)" | AMBIGUOUS | Single-quarter actuarial remeasurement loss of 1.58cr exceeds the entire FY26 remeasurement of (0.39cr) — triggers the F9 assumption-change test. Q1FY26 was also large ((1.69)) and Q4FY26 positive (0.76), so this may be Q1 discount-rate seasonality rather than a one-way assumption reset. Immaterial in size (1.58 on 33.31 PAT) but verify discount-rate / plan-asset assumptions at the Annual Report. |
| F10 | F10 Dilution | Table 3 (line 210-212, 218-219) | 210-212 | "Paid-up equity share capital ... 44.17 | 44.16" | FORWARD-SIGNAL | Paid-up rose 44.16→44.17cr (+0.01cr ≈ ~10k shares of Rs10 face) during Q1FY27 with NO corporate-action note explaining it — signature of an ESOP exercise/allotment. Basic>diluted in every period (Q1FY27 7.54 vs 7.49) confirms live dilutive instruments (options) outstanding. Ongoing ESOP dilution overhang; A4 to size the option pool vs the thesis share count. |
| F11 | F11 Net worth | Table 3 (line 214) + Table 4 (line 253, 259) | 214 | "Other equity ... 405.04" | AMBIGUOUS | Segment tie is exact at FY26 (813.70−364.50 = 449.20 = 405.04+44.16). Rolling that forward: 449.20 + Q1FY27 TCI 32.13 + paid-up 0.01 = 481.34, but Q1FY27 segment-derived equity is 943.06−449.76 = 493.30 → ~11.96cr of equity growth NOT explained by comprehensive income or the tiny allotment, and no note discloses it. Candidate reconciling items: securities premium on allotment, a reserve/transition adjustment, or a fresh premium-bearing issue. A4 to request the balance sheet / equity movement. |
| F12a | F12 Segment | Table 4 (line 250, 237) | 250 | "Segment assets -Mobility 835.56 ... 654.05" | FORWARD-SIGNAL | Mobility segment assets +181.51cr QoQ (654.05→835.56, +27.7%) while Mobility revenue grew only +8.8% QoQ (258.39→281.04). Asset intensity rising far faster than sales = working-capital/capex absorption. This is the direct balance-sheet confirmation of the DETERIORATING cash-conversion leg (Master Gate #2). |
| F12b | F12 Segment | Table 4 (line 252, 258) | 252 | "-Unallocable 28.55 ... 85.40" (assets); "-Unallocable 122.49 ... 68.74" (liab) | FORWARD-SIGNAL | Unallocable (cash/investment-like) assets fell −56.85cr QoQ (85.40→28.55) and unallocable (borrowing/provision-like) liabilities rose +53.75cr QoQ (68.74→122.49). Cash reserves drawn down AND liabilities levered up to fund the Mobility asset build. Total assets +129.36cr QoQ vs quarterly TCI of only 32.13cr = growth is NOT self-funding. |
| F12c | F12 Segment | Table 4 (line 238, 243) | 238 | "-Industrial 28.73 | 29.32 | 34.10" | FORWARD-SIGNAL | Industrial segment revenue −15.7% YoY (34.10→28.73) and segment result −18.2% YoY (4.84→3.96), assets roughly flat. The non-Mobility leg is contracting while the whole story leans on Mobility (91% of revenue). Concentration + a shrinking second leg. |

---

## CHECKLIST SCORECARD (all 17, one status each)

| # | Check | Status | Basis |
|---|-------|--------|-------|
| F1 | Zero-value standing lines | PASS | Only ZERO_STANDING row is "Other equity" (line 214), blank in the 3 quarter columns and populated only in the year-ended column — standard SEBI quarterly format, not a transaction-class placeholder. No exceptional-items / profit-on-sale / discontinued-ops template line stands at zero; the one one-off (tax reversal) is correctly inside current tax, not a suppressed exceptional line. |
| F2 | Standalone vs consolidated | N.A. | Note 5 (line 291): "The Company has no subsidiary, associate or joint venture companies as on 30 June 2026." No consolidated statement exists. Verified no investment-income or related-party lines suggest hidden entities — Other income is only 0.86cr and "Unallocable" is an internal segment residual, not an entity. |
| F3 | Shell-entity detection | N.A. | No subsidiaries to compare cost lines against (Note 5, line 291). No Going Concern EoM present. |
| F4 | Unaudited contribution ratio | N.A. | No "Other Matters" paragraph in the Limited Review Report; no component auditors, JVs or associates. 0% of PAT rests on unreviewed numbers — the whole statement is reviewed by B S R & Co. LLP. |
| F5 | Going concern / EoM scope | PASS | No Going Concern paragraph. Review para 4 (lines 113-116) verbatim-diffed: "Attention is drawn to the fact that the figures for the three months ended 31 March 2026 ... are the balancing figures ...". Assessed = boilerplate. This is the universal Q1 balancing-figure disclosure (cross-refs Note 4, line 288-289), EoM-style phrasing but purely about derivation of the March comparative, not a substantive matter about the Company. The A2 UNLABELED_EOM_LANGUAGE flag is a labelling observation, not a substantive EoM; no scope, entity or amount to trend (no prior-quarter extract supplied). |
| F6 | Forward-commitment mining | PASS | Lexicon sweep of notes/letter: only hits are "commenced" (line 48, board meeting timing — neutral), "approved" (line 39-40, 263 — approval of these results, not a forward promise), and "has completed" (Note 2, line 271, IPO already done/listed 11-Mar-2026 = completed, historical). No live "expected to / will be / underway / proposes to / intends to / in the process of". No open dated management commitments to track. |
| F7 | Hedge-phrase mining | PASS | Lexicon sweep ("no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour", "may"): no pre-emptive hedge language added anywhere in the notes. No newly-added revenue-lumpiness or customer-concentration hedge. |
| F8 | Tax forensics | FINDING | Note 3 prior-year reversal Rs2.98cr (line 285-286) = explicit "tax adjustments relating to earlier years", non-zero → FINDING. ETR 19.4%/23.5%/43.4%/31.0% (Q1FY27/Q4FY26/Q1FY26/FY26) vs statutory 25.17%. Deferred tax is a consistent charge (3.31/2.61/8.10/21.95), not a credit shield. See finding F8. |
| F9 | OCI forensics | FINDING | Q1FY27 actuarial remeasurement (1.58) exceeds full FY26 (0.39) — F9 trigger met. See finding F9. |
| F10 | Share count & dilution | FINDING | In-quarter paid-up rise 44.16→44.17 with no explanatory note; persistent basic>diluted spread = live options. See finding F10. |
| F11 | Reserves / net-worth tie-out | FINDING | FY26 segment-vs-equity tie is exact (449.20); Q1FY27 roll-forward leaves ~11.96cr of equity growth unexplained by TCI. No third-party (rating/slide) number available for the 5% external-gap test, so this is an internal roll-forward anomaly. See finding F11. |
| F12 | Segment forensics | FINDING | Mobility assets +181.5cr QoQ vs +8.8% revenue; unallocable cash drawn down −56.85cr and unallocable liabilities +53.75cr; Industrial revenue/result contracting YoY. See findings F12a/F12b/F12c. |
| F13 | Board outcome beyond results | PASS | Single agenda item confirmed — line 42: "1. Unaudited Financial Results ... along with the Limited Review Report", and line 45-46 attaches only that. No AR/Board's-Report/MD&A approval, no AGM notice or record date, no dividend, no director appointment/resignation with term dates, no auditor change, no capital-raising enabling resolution. No Role-6 AR event or funding-round foreshadow to schedule this quarter. (Note: no dividend, consistent with a WC-heavy growth stage retaining cash.) |
| F14 | Note-drafting inconsistencies | PASS | Note 1 (line 268-269) "limited review ... unqualified review conclusion" matches the auditor letter (limited review, unmodified, lines 105-112/117-138). Entity name "SEDEMAC Mechatronics Limited (Formerly ... Private Limited)" consistent across all tables. Note 4 (line 288-289, "nine months ... 31 December 2025") reconciles with review para 4 ("third quarter", lines 113-116). Only defect is an immaterial typo "agrregating" (line 275) — single, non-cumulative, no governance weight. |
| F15 | Entity-list diffs | N.A. | No consolidation list (standalone-only per Note 5); no prior-quarter ledger supplied (A2 flag NO_PRIOR_LEDGER_FOR_ENTITY_DIFF). Nothing to diff. |
| F16 | Presentation-specific | N.A. | Doctype is a results filing, not an investor presentation. |
| F17 | Concall silence audit | N.A. | Doctype is a results filing, not a transcript. (F6 register carries no open commitments; monitoring-checklist silence is audited by A4/A5 against the concall doctype when it lands.) |

Status tally: PASS = 6 (F1, F5, F6, F7, F13, F14); FINDING = 5 (F8, F9, F10, F11, F12); N.A. = 6 (F2, F3, F4, F15, F16, F17). Total = 17, no blanks. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/turn ref | status word |
|------------|--------------|---------------|-------------|
| Initial Public Offering (offer-for-sale, 80,43,300 shares, Rs1,087.45cr; no fresh capital to Company) | listed 11 March 2026 | Note 2, lines 271-276 | completed |

No open / forward-dated management commitments in this filing. No "initiated → underway → completed" transition to carry to the FTTCP catalyst timeline this quarter.

---

## CASH-CONVERSION & EARNINGS-QUALITY SYNTHESIS (Master Gate #2)

Addressing the monitoring checklist directly:
- Revenue vs +37% unit-growth claim: reported revenue +42.5% YoY (217.36→309.77), Mobility +53.4% YoY. Revenue outgrows the cited +37% units → positive price/mix, NOT ASP erosion. Underlying PBT +37% YoY (30.17→41.34); the headline PAT +95% is a tax-rate artifact (F8).
- Cash conversion (LEG UNDER TEST): CONFIRMS DETERIORATING. Balance sheet expanded +129.36cr QoQ (assets 813.70→943.06) against only 32.13cr of quarterly comprehensive income. Mobility assets +181.5cr QoQ vs +8.8% revenue (F12a). Funded by liabilities +85.26cr and a −56.85cr drawdown of unallocable (cash-like) assets (F12b). Depreciation +25% YoY (13.09→16.37) signals a capex/RoU ramp. Growth is liability- and cash-funded, not self-funding.
- Other-income composition: Other income only 0.86cr = 2.1% of PBT (Q1FY26 was 2.60cr = 8.6%). Operating PBT this quarter is actually HIGH quality (not propped by other income) — a confirmatory negative-to-neutral: the earnings miss on quality comes from tax (F8), not other income.
- EPS quality: 7.54 basic is flattered ~9% by the Rs2.98cr tax reversal; ex-reversal EPS ~6.87. Diluted<basic confirms option overhang (F10).

Net forensic read: the filing quietly confirms the thesis concern — high-quality operating line, but a working-capital/capex-heavy balance sheet consuming cash, and a PAT line flattered by a non-recurring tax reversal. Supports AVOID / cash-conversion DETERIORATING.

---

```yaml
stage: A3-forensics
company: "SEDEMAC"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/sedemac-q1fy27/work/forensics_results_sedemac_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: PASS
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F8", check: "F8-tax", line: "285-286", classification: "FORWARD-SIGNAL", implication: "Rs2.98cr prior-year tax reversal in current tax; ETR 19.4% vs 25.17%; YoY PAT +95% is a tax-rate artifact, underlying PBT +37%; ETR normalises up next quarter"}
  - {id: "F9", check: "F9-oci", line: "200", classification: "AMBIGUOUS", implication: "Q1 actuarial loss 1.58cr exceeds full FY26 0.39cr; possible discount-rate assumption change vs Q1 seasonality; verify at Annual Report"}
  - {id: "F10", check: "F10-dilution", line: "210-212", classification: "FORWARD-SIGNAL", implication: "Paid-up 44.16->44.17 in-quarter with no note (likely ESOP exercise); persistent basic>diluted spread = live option overhang / ongoing dilution"}
  - {id: "F11", check: "F11-networth", line: "214", classification: "AMBIGUOUS", implication: "Q1FY27 segment-derived equity 493.30 exceeds FY26 close rolled forward for TCI by ~11.96cr, unexplained by any note; request balance sheet / equity movement"}
  - {id: "F12", check: "F12-segment", line: "250", classification: "FORWARD-SIGNAL", implication: "Mobility assets +181.5cr QoQ vs +8.8% revenue; unallocable cash -56.85cr and liabilities +53.75cr; Industrial revenue/result contracting YoY = cash-conversion DETERIORATING confirmed"}
forward_signals: ["F8", "F10", "F12"]
ambiguous: ["F9", "F11"]
commitments:
  - {commitment: "IPO (offer-for-sale, 80,43,300 shares, Rs1,087.45cr, no fresh capital to Company)", implied_date: "2026-03-11 listed", ref: "Note 2 lines 271-276", status_word: "completed"}
gate_a3: pass
blank_checks: []
```
