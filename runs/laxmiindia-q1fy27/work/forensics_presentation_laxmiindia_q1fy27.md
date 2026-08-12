# A3 FORENSIC NOTES — LAXMIINDIA — Q1 FY27 — DOCTYPE: PRESENTATION

Document: `extract_presentation_laxmiindia_q1fy27.txt` (47 slides / 1433 lines)
Ledger: `ledger_presentation_laxmiindia_q1fy27.md`
Ledger reconciliation: 100% — every Section 1 slide row and every Section 2 quantified-figure
block read verbatim at its cited line before judging. Section 3 (dropped-slide) is
`PRIOR_LEDGER_UNAVAILABLE` and is carried as a completeness gap, not assumed clean.
Company-memory context: LAXMIINDIA is NEW to the pipeline — no Notion thesis, no
companies/LAXMIINDIA.md, no Decision Status, no active tripwires, no monitoring checklist.
The monitoring-checklist cross-check (F17) is therefore N.A. by construction; first-thesis
tripwire candidates are surfaced below.

---

## FINDINGS TABLE

| id | check | ledger row ref | slide / line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-a | F1 | Slide 13 "Sold to ARC" (L410-421) | S13 / L421 | "Sold to ARC   0.00  0.00  0.00  0.00 … Sold to ARC  (16.36) (9.74) (1.83) (27.93)" | AMBIGUOUS | The ARC-disposal line is a standing template item that removed ₹27.93 Cr of stressed loans in FY26 (incl. ₹1.83 Cr Stage-3). It is nil this quarter, so Q1FY27 GNPA (2.08%, L173) rose on its own with no ARC clean-up — vs 1.28% Q1FY26 (L382). Ask: was the FY26 GNPA/NNPA improvement mechanically aided by the ARC sale, and is stressed-asset formation now running ahead of resolution capacity? |
| F6-a | F6 | Slide 19 targets (L579-580, L599-600) | S19 / L579-600 | "targeted ROA of 3.50% - 3.75% and ROE of 13.50% - 14.00% … achievement of targeted ~30% AUM CAGR" | FORWARD-SIGNAL | Current RONW is 13.86% (L176/L317) — already AT the top of the 13.50-14.00% ROE target. Management is guiding a flat-to-lower ROE despite ~30% AUM CAGR, i.e. the post-IPO equity raise (net worth +79.81%, L176) leaves the book under-levered (D/E 3.10 vs 4.13 FY26, L332/L335) and ROE will be diluted until re-leveraging. ROA target 3.50-3.75% sits just above current 3.45% (L154). Tripwire candidate: ROE failing to hold 13.5% while AUM compounds 30%. |
| F6-b | F6 | Slide 27 process diagram (L800) | S27 / L800 | "E-Sign (Upcoming)" | NEUTRAL-FACT | Digital pre-disbursal E-Sign flagged as not-yet-live; minor delivery item for the Role 5 promise tracker. |
| F7-a | F7 | Slide 19 liability strategy (L580) | S19 / L580 | "exploring new funding avenues such as ECBs" | AMBIGUOUS | First mention of External Commercial Borrowings — not yet secured ("exploring"). ECB access would introduce unhedged FX / hedging-cost exposure for a domestic-rupee-asset NBFC. Ask: is an ECB in active arrangement, what tenor/size, and is the hedging cost inside the 10.66% COB math? |
| F9-a | F9 | Slide 16 OCI row (L528) | S16 / L528 | "Other Comprehensive Income  -0.14  -0.12 … -0.08  -0.09" | NEUTRAL-FACT | Single-quarter OCI of -0.14 Cr (Q1FY27) exceeds the full FY26 OCI of -0.08 Cr in magnitude — mechanically triggers the F9 assumption-change rule. Amounts trivial (gratuity actuarial), but verify discount-rate / plan-asset assumptions at the Annual Report. |
| F10-a | F10 | Slide 17 Paid-up Equity (L538) | S17 / L538 | "Paid-up Equity  26.20  20.91  25.30%  26.13  0.24%" | AMBIGUOUS | The large YoY jump (20.91→26.20) is the Aug-2025 IPO (S23, L676). But paid-up also rose ₹0.07 Cr QoQ (26.13→26.20, +0.24%) — ~14 lakh new shares at ₹5 face — with no corporate action named in the deck. No basic/diluted EPS disclosed to test the spread. Ask: what post-IPO issuance (ESOP allotment / anchor-lock release) drove the QoQ share-count creep? |
| F14-a | F14 | Slides 39/41 + cover (L15, L1132, L1199) | S39 L1132 vs S41 L1199 | "Co-founder member of LIFL" (L1132) vs "Vintage in LIFC : 4+ years" (L1199); cover ref "LIFL/SLC/2026-27/26" (L15) | NEUTRAL-FACT | The company self-abbreviates as both "LIFL" and "LIFC" within one deck; also "Laxmi India Finleasecap Pvt. Ltd." (L653) as the 2011-acquired entity. Individually immaterial; cumulatively a drafting/governance tidiness data point. |
| F16-a | F16 | Slide 12 asset-quality bifurcation (L363-393) | S12 / L363-393 | "With Up-Money Default … Without Up-Money Default" | AMBIGUOUS | The FY26 columns for Credit Cost, GNPA and NNPA are each split into "With" vs "Without Up-Money Default" (e.g. GNPA 2.13% With vs 0.80% Without, L380-384) with the "Without" (cleaner) bar placed adjacent to Q1 figures. "Up-Money Default" is defined nowhere in the deck. This is a company-authored metric window that flatters FY26 asset quality. Ask management to define "Up-Money Default", quantify the excluded pool, and state whether it recurs in FY27. |
| F16-b | F16 | Section 3 (ledger L385-388) | ledger §3 | "PRIOR_LEDGER_UNAVAILABLE — no prior-quarter LAXMIINDIA presentation ledger" | NEUTRAL-FACT | Dropped-slide / softened-guidance comparison cannot be run this quarter. Not assumed clean — flagged so A4 sources the Q4FY26 or Q1FY26 deck to backfill the diff. |
| F16-c | F16 | Slides 6/16/25/34/46 rounding (L140/L525, L778/L1014, L1384/L1408, L140) | S6 L140 vs S16 L525 | "₹ 21.91 Cr." (L142) vs "Profit Before Tax  21.90" (L525) | NEUTRAL-FACT | Cross-slide inconsistencies for A4's arithmetic pass: PBT 21.91 (S6) vs 21.90 (S16); "37% first-time borrowers" (S25 L778) vs "37.1%" (S34 L1014); Other Public 32.71% (S46 legend L1384) vs 32.70% (S46 table L1408). Separately, S6 shows a stray "71.64%" adjacent to Return-on-Net-Worth (L140-141) where the actual RONW is 13.86% (L176) — 71.64% ≈ the 71.59% PBT-YoY growth (L525): a likely OCR/label misplacement to cross-check against the source visual. |
| F16-d | F16 | Slides 20/25 lender claims (L624, L772) | S20 L624 / S25 L772 | "50+ PSU, SFB, FI & NBFC partners; zero delays / defaults" (L624); "Zero repayment delays since inception" (L772) | AMBIGUOUS | Absolute "zero" claim about the Company's own repayment record to its 47+ lenders (distinct from borrower NPAs). Hard zero-claims are A5 bait — test against any rating-rationale covenant/DPD history. Note the deck's own asset quality is deteriorating (GNPA 1.28%→2.08% YoY) even as the funding-side "zero default" claim stands. |
| F16-e | F16 | Slide 36 Vertical-Wise AUM (L1087, L1092) | S36 / L1087-1092 | "MSME  Construction & LAP  Vehicle  Wholesale  Personal Loan" with "-" cells | FORWARD-SIGNAL | Two verticals — Wholesale (on-lending, S35 L1040) and Personal Loan (Unsecured, up to ₹200 lakhs, S35 L1052-1054) — show dash/nil AUM in FY23-FY24 and are now scaled-in. A secured-MSME/vehicle lender is building an UNSECURED personal-loan and a wholesale on-lending book. Mix shift toward unsecured is a credit-cost forward signal. Tripwire candidate: unsecured (Personal Loan) share of AUM and its vintage delinquency. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 — Zero-value standing line items | FINDING | Slide 13 "Sold to ARC" all-zero this quarter (L421) vs -₹27.93 Cr FY26; Stage-1/2 write-offs nil (L423); Slide 36 dash cells for not-yet-originated verticals (L1087). See F1-a / F16-e. |
| F2 — Standalone vs consolidated decomposition | N.A. | Deck presents a single set of figures; no standalone-vs-consolidated split disclosed. Disclaimer's "Group / subsidiaries" wording (L67) is boilerplate — no subsidiary financials shown. |
| F3 — Shell-entity detection | N.A. | No S-vs-C cost lines to compare; no subsidiary cost structure in a presentation. |
| F4 — Unaudited contribution ratio | N.A. | No auditor "Other Matters" in a presentation. Note: the ENTIRE deck is management-prepared and explicitly "has not been… reviewed or approved by any statutory or regulatory authority" (L73) — treat all figures as unaudited management numbers. |
| F5 — Going concern / EoM scope | N.A. | No auditor report or Emphasis-of-Matter in an investor presentation. |
| F6 — Forward-commitment phrase mining | FINDING | Medium-term targets ROA/ROE/AUM-CAGR (L579-600); "E-Sign (Upcoming)" (L800); ECB avenue (L580). ROE target at current level = flat-ROE guidance. See F6-a / F6-b + Commitment Register. |
| F7 — Hedge phrase mining | FINDING | "exploring new funding avenues such as ECBs" (L580) — pre-emptive, unsecured funding hedge. See F7-a. (Disclaimer "no assurance" language L91 is boilerplate, not counted.) |
| F8 — Tax forensics | PASS | Implied tax rate 24.37% Q1FY27 (L527) vs 25.17% statutory = ~80bps shield, narrowing from 23.42% Q1FY26 → converging on statutory; no "earlier-year" tax items disclosed. Immaterial and normalising. |
| F9 — OCI forensics | FINDING | Q1FY27 OCI -0.14 Cr exceeds full FY26 -0.08 Cr (L528) — triggers assumption-change rule; amounts trivial; verify gratuity assumptions at AR. See F9-a. |
| F10 — Share count and dilution | FINDING | Paid-up 26.13→26.20 QoQ (+0.24%, L538), a small post-IPO issuance not named; IPO drove the YoY step; no basic/diluted EPS in deck. See F10-a. |
| F11 — Reserves and net-worth tie-out | PASS | Reserves 456.60 + Paid-up 26.20 = 482.80 ≈ Total Equity 482.79 (L538-542, 0.01 rounding); Net Worth ties across S6 (L173), S10 (L295), S17 (L542); paid-up 26.20 Cr ties to 5,23,93,078 shares × ₹5 (L411). No third-party net-worth figure to reconcile against. |
| F12 — Segment forensics | N.A. | Deck discloses Vertical-Wise AUM (S36) only — no segment assets/liabilities/revenue, so the equity-funded-build / liabilities-unwind tests cannot run. Unsecured-vertical build is carried instead in F16-e. |
| F13 — Board outcome beyond the results | N.A. | Presentation carries no board-meeting outcome, AGM notice, record date, dividend, or director appointment/term dates (director profiles S38-40 give no tenure dates). Nothing to schedule a Role 6 event from. |
| F14 — Note drafting inconsistencies | FINDING | "LIFL" (L15, L1132) vs "LIFC" (L1199) self-abbreviation; "Laxmi India Finleasecap Pvt. Ltd." (L653). Cumulative governance-tidiness note. See F14-a. |
| F15 — Entity list diffs | N.A. | No consolidation/entity list in the deck and no prior-quarter ledger to diff. |
| F16 — Dropped and reframed disclosures | FINDING | "Up-Money Default" undefined FY26 bifurcation (L363-393); PRIOR_LEDGER_UNAVAILABLE dropped-slide gap; cross-slide rounding + RONW OCR anomaly; "zero delays/defaults" absolute claim; unsecured-vertical build. See F16-a…e. |
| F17 — Concall silence audit | N.A. | Not a concall (no transcript) AND no Notion monitoring checklist exists — LAXMIINDIA is new to the pipeline. Silence audit cannot be run; first-thesis tripwire candidates surfaced in F1-a, F6-a, F16-e. |

Blank checks: none. All 17 carry exactly one status (GATE A3 pass).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide / line ref | status word |
|---|---|---|---|
| ROA of 3.50% - 3.75% | "Medium-Term" (undated) | S19 / L579 | targeted |
| ROE of 13.50% - 14.00% | "Medium-Term" (undated) | S19 / L580 | targeted |
| ~30% AUM CAGR | "Medium-Term" (undated) | S19 / L599-600 | targeted |
| New funding avenues incl. ECBs | undated | S19 / L580 | exploring |
| E-Sign in pre-disbursal flow | undated | S27 / L800 | upcoming |

All five commitments are undated ("Medium-Term Focus" header, S19 L575) — flag for A4: management questions should force a date and a baseline on each, especially the ROE target that already equals the current 13.86% actual.

---

## NOTES FOR A4 / A5

- FORWARD-SIGNAL findings (feed catalyst timeline / thesis): F6-a (flat-ROE guidance vs 30% AUM CAGR — under-levered post-IPO), F16-e (unsecured Personal-Loan + Wholesale on-lending build).
- AMBIGUOUS findings (convert to management questions): F1-a (ARC-sale dependence of FY26 asset quality), F7-a (ECB / FX exposure), F10-a (post-IPO QoQ share issuance), F16-a (define "Up-Money Default"), F16-d (verify "zero repayment delays since inception").
- Completeness gap A4 must carry: PRIOR_LEDGER_UNAVAILABLE (F16-b) — no dropped-slide / softened-guidance diff possible until a prior-quarter deck ledger is produced.
- First-thesis tripwire candidates (no prior tripwires exist): ROE holding ≥13.5% through the AUM ramp; GNPA trajectory absent ARC clean-ups; unsecured (Personal Loan) AUM share and its vintage delinquency.

---

```yaml
stage: A3-forensics
company: "LAXMIINDIA"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/laxmiindia-q1fy27/work/forensics_presentation_laxmiindia_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F1-a", check: "F1", line: "L421", classification: "AMBIGUOUS", implication: "FY26 asset quality aided by -27.93 Cr ARC sale; nil this quarter as GNPA rises 1.28%->2.08% YoY"}
  - {id: "F6-a", check: "F6", line: "L579-600", classification: "FORWARD-SIGNAL", implication: "ROE target 13.5-14.0% equals current 13.86%; flat-ROE guidance, under-levered post-IPO (D/E 3.10 vs 4.13)"}
  - {id: "F6-b", check: "F6", line: "L800", classification: "NEUTRAL-FACT", implication: "E-Sign not yet live; delivery item for promise tracker"}
  - {id: "F7-a", check: "F7", line: "L580", classification: "AMBIGUOUS", implication: "ECB funding 'exploring' — potential unhedged FX / hedging-cost exposure not in current 10.66% COB"}
  - {id: "F9-a", check: "F9", line: "L528", classification: "NEUTRAL-FACT", implication: "Q1 OCI -0.14 exceeds full FY26 -0.08; verify gratuity assumptions at AR (immaterial size)"}
  - {id: "F10-a", check: "F10", line: "L538", classification: "AMBIGUOUS", implication: "Paid-up +0.07 Cr QoQ (~14 lakh shares) post-IPO, corporate action not named; no EPS spread disclosed"}
  - {id: "F14-a", check: "F14", line: "L1132", classification: "NEUTRAL-FACT", implication: "LIFL vs LIFC self-abbreviation inconsistency (L15/L1132 vs L1199); drafting tidiness"}
  - {id: "F16-a", check: "F16", line: "L363-393", classification: "AMBIGUOUS", implication: "'Up-Money Default' undefined; FY26 'Without' GNPA 0.80% flatters vs 'With' 2.13% — force a definition"}
  - {id: "F16-b", check: "F16", line: "ledger-S3-L385", classification: "NEUTRAL-FACT", implication: "PRIOR_LEDGER_UNAVAILABLE — dropped-slide/softened-guidance diff cannot run; not assumed clean"}
  - {id: "F16-c", check: "F16", line: "L525", classification: "NEUTRAL-FACT", implication: "Cross-slide rounding (PBT 21.91/21.90; 37/37.1%; 32.71/32.70%) + stray 71.64% at RONW (L140) OCR anomaly"}
  - {id: "F16-d", check: "F16", line: "L624", classification: "AMBIGUOUS", implication: "Absolute 'zero delays/defaults since inception' lender-repayment claim to verify vs rating rationale"}
  - {id: "F16-e", check: "F16", line: "L1087", classification: "FORWARD-SIGNAL", implication: "Unsecured Personal-Loan (up to 200 lakhs) + Wholesale on-lending verticals built from nil; secured lender shifting to unsecured"}
forward_signals: ["F6-a", "F16-e"]
ambiguous: ["F1-a", "F7-a", "F10-a", "F16-a", "F16-d"]
commitments:
  - {commitment: "ROA of 3.50%-3.75%", implied_date: "medium-term (undated)", ref: "S19/L579", status_word: "targeted"}
  - {commitment: "ROE of 13.50%-14.00%", implied_date: "medium-term (undated)", ref: "S19/L580", status_word: "targeted"}
  - {commitment: "~30% AUM CAGR", implied_date: "medium-term (undated)", ref: "S19/L599-600", status_word: "targeted"}
  - {commitment: "New funding avenues incl. ECBs", implied_date: "undated", ref: "S19/L580", status_word: "exploring"}
  - {commitment: "E-Sign in pre-disbursal flow", implied_date: "undated", ref: "S27/L800", status_word: "upcoming"}
gate_a3: pass
blank_checks: []
```
