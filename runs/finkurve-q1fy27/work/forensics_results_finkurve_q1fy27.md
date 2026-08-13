# A3 FORENSIC NOTES — Finkurve Financial Services Ltd (Arvog) — Q1 FY27 — DOCTYPE: results (Reg 33 unaudited results + Board Outcome + Limited Review Report + Security Cover Certificate + Annexures 3/4), STANDALONE-ONLY

Model: claude-opus-4-8 | Ledger reconciled: 100% (all 176 enumerated rows read at their cited file line in `extract_results_finkurve_q1fy27.txt` before judging).
Line cites below are **file (outer) line numbers** of the extract, matching the A2 ledger convention (file_line = embedded_line + 84).

NBFC adaptation (per A3 task directive "F4, F5, F12 run in full — asset quality, ECL/provisioning, related-party"): F4 hosts asset-quality forensics, F5 hosts ECL/provisioning forensics, F12 hosts related-party forensics. Standard consolidation checks (F2/F3/F15) are N.A. because a full-text sweep confirms no "consolidated / subsidiary / standalone" token anywhere and Note 6 (L348) declares a single reportable segment.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| F4-1 | F4 | §6 q(ia)/q(ib), q(iia)/q(iib) | L380-383 | "Gross NPA (INR in lacs) 665.65 … Gross NPA ratio (%) 0.54% … Net NPA … 596.11 … 0.48%" | FORWARD-SIGNAL | GNPA 0.54% is ~6x the Notion baseline of 0.09%. Still under the 1.5% tripwire but the trajectory on a 72% LTV gold book is the single asset-quality watch item; Stage-1/2/3 movement is not disclosed to size it. |
| F4-2 | F4 | §3 items 1 & 7; §6 (b)/(c) | L288, L295, L361-362 | "Finance costs 2,672.31 … 707.82"; "Interest Service Coverage Ratio 1.38"; "Debt service coverage Ratio 0.41" | FORWARD-SIGNAL | Finance cost +278% YoY (707.82→2,672.31) outran interest income +181% (2,659.83→7,478.68) → spread compression as leverage builds, exactly the Notion NIM/cost-of-funds risk. DSCR 0.41 and ISCR 1.38 are thin. |
| F5-1 | F5 | §3 item 10; §6 q(iii) | L298, L384 | "impairment/ (Reversal of Impairment) on financial instruments 20.38"; "Provision Coverage Ratio (%) 10.45%" | FORWARD-SIGNAL | Impairment charge collapsed to 20.38 lakhs vs FY26 run-rate ~554/qtr (2,217.18/4). Normalising to run-rate would cut PBT (1,120.52, L303) by ~48%. PCR only 10.45% on a rising GNPA; no Stage-wise ECL table exists (Ind AS 109 completeness gap). Earnings quality flag. |
| F10-1 | F10 | §3 rows 22-23 | L313-314 | "Basic (INR) 0.50 … Diluted (INR) 0.58" (Q1FY27 column) | AMBIGUOUS | Diluted EPS (0.58) exceeds Basic EPS (0.50) — arithmetically impossible under Ind AS 33 (anti-dilutive instruments are ignored). Either a transposition/typo or a computation error; must be resolved before EPS is trusted. |
| F10-2 | F10 | §3 row 20; Annexure 3 row 15 | L310, L697-711 | "Paid up equity share capital 1,401.28 … 1,400.50 … 1,400.19"; "Rs. 30cr being 75% of the share warrants subscription amount yet to be received" | FORWARD-SIGNAL | Paid-up rose +0.78 lakh (warrant/pref conversion). Rs 30 cr (75% of warrant money) is still uncalled = pending cash inflow AND pending dilution. Notion tripwire: dilutive raise below Rs 40. |
| F12-1 | F12 | Board Outcome items 5,6,7 | L127, L131, L135 | "Material Related Party Transactions pertaining to … to/from M/s. Augmont Goldtech Private Limited … Service Fees, Commission … Brand Usage and Tech Support … subject to shareholders approval" | FORWARD-SIGNAL | Omnibus related-party framework (grant of loans to RP, acceptance of loans from RP, Augmont fee/brand/tech) put to AGM-42→43 (2027). Confirms Augmont dependency; no rupee quantum disclosed here — a governance/concentration exposure to size. |
| F12-2 | F12 | §3 rows 2 & 8; Note 8 | L289, L296, L387 | "Fees and commission income 58.4 … 1,323.51 … 101.72"; "Fees and commission expenses 1,363.74"; "Previous periods' figures have been regrouped/ rearranged" | FORWARD-SIGNAL | Fee INCOME collapsed: Q1FY26 1,323.51 → FY26 net 101.72 (implying ~-1,222 of reversals across FY26) → Q1FY27 ~5.84 (printed "58.4" is a decimal artifact; subtotal 7,510.30 = 7,478.68+5.84+25.79 confirms). This is the Notion "watch reclassification" risk made visible via Note 8 regrouping. Fee EXPENSE 1,363.74/qtr (6,972.62 FY26) is the Augmont pass-through. |
| F13-1 | F13 | Board Outcome items 8,9,10 | L148, L152, L156 | "power to borrow funds … not exceeding X 5000 Crore … subject to shareholders approval"; "issue of Non – Convertible Debentures on Private Placement Basis" | FORWARD-SIGNAL | Enabling resolutions for Rs 5,000 Cr borrowing headroom (vs current D/E 2.88), Sec 186 threshold hike, and fresh private-placement NCDs foreshadow a large debt scale-up and the D/E ramp toward 4-4.5x. Funding-round precursor. |
| F13-2 | F13 | Board Outcome item 11 | L159 | "continuation of Directorship of Mr. Himadri Bhattacharya (DIN: 02331474), as Non-Executive Independent Director … Post Attaining the Age of 75 … subject to shareholders approval" | NEUTRAL-FACT | Independent director being *continued* (not dropped) past 75 by special resolution — a retention/governance signal, not a red flag; note in the governance register. |
| F14-1 | F14 | §3 rows 22-23 vs §6 h-i/h-ii | L313-314, L368-369 | Statement "Basic 0.50 … Diluted 0.58" vs Ratios "Basic EPS 0.60 … Diluted EPS 0.59" | AMBIGUOUS | Same-document EPS mismatch across two tables (Basic 0.50 vs 0.60; Diluted 0.58 vs 0.59). The Ratios table has the correct direction (diluted ≤ basic); the Statement table looks mis-keyed. Data-integrity/control question. |
| F14-2 | F14 | Annexure 3 rows 6-7 vs Annexure 4 rows 6-7 | L673-674, L735-736 | Annexure 3 "Monitoring Agency Applicable … CRISIL Rating Limited"; Annexure 4 "Monitoring Agency Not Applicable" | AMBIGUOUS | A Rs 199 Cr NCD raise (Annexure 4) is marked "Monitoring Agency Not Applicable" while the smaller Rs 141.50 Cr equity raise carries CRISIL. Inconsistent treatment — a compliance/disclosure question for management. |
| F14-3 | F14 | Annexure 4 rows 8 & 15 | L737, L758 | "Is there a Deviation / Variation in use of funds raised — No"; deviation row "For lending business … 135 … 199 … NA" | AMBIGUOUS | Funds utilised (Rs 199 Cr) exceed original allocation (Rs 135 Cr) yet the deviation flag reads "No". Amount-utilised-vs-disclosed is a defined deviation type (b); the "No" and the 199>135 arithmetic are in tension. |
| F14-4 | F14 | Review Report para 5 | L253-256 | "the quarter ended 30th June 2025 … were reviewed by predecessor auditor whose report dated 13th August, 2025 expressed an unmodified conclusion" | NEUTRAL-FACT | AUDITOR_CHANGE: Q1FY26 comparative rests on a predecessor auditor; current auditor (Ladha Singhal & Associates) is unmodified but takes no direct responsibility for the comparative. First full cycle under the new firm — watch for comparative restatement at the Annual Report. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINE ITEMS | PASS | All ZERO_STANDING lines explained as template/not-applicable: "Net loss on fair value changes" nil all 4 periods (L297, mirror of the net-gain line L290); CLA "Write Off" (L338) and "default loss guarantee Nil" (L340); Appendix I zero lines — CWIP/Goodwill/Intangibles-under-dev/Inventories/Cash/Bank (L524-534). Goodwill = nil (L526) corroborates standalone/no-acquisition. Cash shows Col J "-" only because the cover table scopes charged assets, not unrestricted cash. No template line signals an unexpected future transaction class. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | No consolidated statement exists (full-text sweep finds no consolidated/subsidiary token); single reportable segment "financial services" (L348); Goodwill nil (L526). No subsidiary or JV appears — Augmont is an RPT counterparty, not a consolidated entity; the 2 CLAs are co-lending partners, not group entities. Confirmed no S-vs-C gap to compute. |
| F3 SHELL-ENTITY DETECTION | N.A. | No subsidiaries/consolidated cost lines to compare. |
| F4 ASSET QUALITY (NBFC) | FINDING | GNPA 0.54%/665.65 lakhs, NNPA 0.48%/596.11 (L380-383) up ~6x vs 0.09% baseline; spread compression as finance cost outruns interest income (L288/L295); DSCR 0.41, ISCR 1.38 (L361-362). CRAR 26.63% (L385) and D/E 2.88 (L360) remain healthy — headroom, noted. See F4-1, F4-2. |
| F5 ECL / PROVISIONING (NBFC) | FINDING | Impairment charge 20.38 lakhs (L298) vs FY26 run-rate ~554/qtr; PCR only 10.45% (L384); no Stage-1/2/3 ECL table in the filing. Under-provisioning/earnings-quality signal. See F5-1. |
| F6 FORWARD-COMMITMENT PHRASE MINING | PASS | Hits logged to the Commitment Register (below): "will be uploaded" (L112), "to be held in the Year 2027" (L127-135), "subject to shareholders approval" (items 5-11), "yet to be received" (L697-711). All routine enabling/approval language; the material ones (borrowing power, NCD, warrants) are escalated under F13/F10. No anomalous or status-changed commitment. |
| F7 HEDGE PHRASE MINING | PASS | No pre-emptive hedge newly added in the Notes about revenue lumpiness, gold-price, or customer/sector concentration. "subject to" instances are AGM-approval conditions, not risk hedges. Note 8 "wherever necessary" (L387) is standard regrouping boilerplate. |
| F8 TAX FORENSICS | PASS | ETR: Q1FY27 24.7% (276.71/1,120.52), Q4FY26 22.8%, Q1FY26 25.5%, FY26 24.8% — all near statutory 25.17% (L303-304). No "tax adjustments relating to earlier years" line present; net DTL 2,325.74 in cover table (L550), no period movement disclosed. No shield anomaly. |
| F9 OCI FORENSICS | PASS | Q1FY27 OCI is effectively nil: TCI 843.81 = PAT 843.81 (L305, L307); the illegible glyph at L306 resolves to ~nil. FY26 OCI 37.49 all fell in Q4. No single-quarter swing exceeding prior year → no assumption-change signal. |
| F10 SHARE COUNT & DILUTION | FINDING | Anti-dilutive EPS anomaly (Basic 0.50 < Diluted 0.58, L313-314) and pending Rs 30 Cr warrant call / paid-up creep to 1,401.28 (L310, L697-711). See F10-1, F10-2. |
| F11 RESERVES & NET WORTH TIE-OUT | PASS | Paid-up 1,401.28 + Other Equity 33,089.57 (Mar-26, L310-311) + Q1 profit 843.81 ≈ 35,334.66 vs Ratios Net Worth 35,436.80 (L365). Gap ~102 lakhs / 0.3% (securities premium on warrant conversion) — well under the 5% threshold. |
| F12 RELATED-PARTY (NBFC) | FINDING | Omnibus RP loan grant/acceptance + Augmont fee/brand/tech framework to AGM (L127/131/135); fee-and-commission income reclassification via Note 8 (L289/296/387). See F12-1, F12-2. |
| F13 BOARD OUTCOME BEYOND RESULTS | FINDING | 11 agenda items assessed. Beyond item 1: Rs 5,000 Cr borrowing power (L148), Sec 186 hike (L152), private-placement NCD (L156), two deviation statements (Annexures 3/4), three RPT approvals (L127/131/135), IND-director continuation post-75 (L159). 42nd AGM referenced → Annual Report imminent (schedule Role 6 AR Deep Dive). See F13-1, F13-2. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | EPS cross-table mismatch (L313-314 vs L368-369), monitoring-agency inconsistency (L673-674 vs L735-736), Annexure 4 deviation tension 199>135/"No" (L737/L758), predecessor-auditor change (L253-256). Plus immaterial artifacts: "has been has been" typo Note 3 (L322), firm name "Ladha Singhal & Associates" vs sign-off "Ladha Singhal Associates" (L192 vs L177/440). See F14-1..F14-4. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list exists in a standalone filing; nothing to diff. (Auditor change captured under F14-4, not an entity-list item.) |
| F16 DROPPED/REFRAMED DISCLOSURES | N.A. | Presentation-only check; doctype is a results filing. |
| F17 CONCALL SILENCE AUDIT | N.A. | Concall-only check; no transcript in this document. |

Status counts: **PASS 6** (F1,F6,F7,F8,F9,F11) · **FINDING 6** (F4,F5,F10,F12,F13,F14) · **N.A. 5** (F2,F3,F15,F16,F17). No blank checks — GATE A3 satisfied.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|------------|--------------|-----|-------------|
| Grant of loans to Related Parties (material RPT) | 42nd AGM → 43rd AGM, 2027 | L127 | board has approved (pending shareholder approval) |
| Acceptance of loans from Related Parties (material RPT) | 42nd AGM → 43rd AGM, 2027 | L131 | board has approved (pending shareholder approval) |
| Augmont Goldtech payments — Service Fees, Commission, Brand Usage, Tech Support | 42nd AGM → 43rd AGM, 2027 | L135 | board has approved (pending shareholder approval) |
| Borrowing power up to Rs 5,000 Cr (Sec 180) | on AGM approval | L148 | board has approved (pending shareholder approval) |
| Increase Sec 186 loan/guarantee/investment threshold | on AGM approval | L152 | board has approved (pending shareholder approval) |
| Issue of NCDs on private placement basis | forthcoming | L156 | board has approved (pending shareholder approval) |
| Continuation of directorship (Himadri Bhattacharya) post-75 | on AGM approval | L159 | board has approved (pending shareholder approval) |
| Warrant balance Rs 30 Cr (75% subscription) to be received | within warrant exercise window (issued May 2025) | L697-711 | underway / yet to be received |
| Results upload to company website | immediate | L112 | will be uploaded |

---

## ADJUDICATION OF A2 LEADS (confirm/dismiss with cites)

1. **Diluted EPS mismatch 0.58 vs 0.59** — CONFIRMED. Statement L314 = 0.58; Ratios L369 = 0.59. → F14-1 (AMBIGUOUS).
2. **Basic 0.50 < Diluted 0.58 (anti-dilutive)** — CONFIRMED at L313-314; arithmetically impossible. → F10-1 (AMBIGUOUS).
3. **Annexure 4 funds utilised ~Rs 199 Cr > allocation ~Rs 135 Cr, deviation "No"** — CONFIRMED. Row L758 (135/199), flag L737. → F14-3 (AMBIGUOUS).
4. **Monitoring Agency inconsistency (CRISIL vs Not Applicable)** — CONFIRMED. Annexure 3 L673-674 (Applicable/CRISIL) vs Annexure 4 L735-736 (Not Applicable). → F14-2 (AMBIGUOUS).
5. **Predecessor-auditor reference (AUDITOR_CHANGE)** — CONFIRMED at L253-256. → F14-4 (NEUTRAL-FACT).
6. **NOT_FOUND values** — CONFIRMED as data-quality gaps, not findings against management: CLA "Fees charged/paid" illegible (L333), CLA "Outstanding*" footnote referent missing (L337), Appendix I "Others" liability value illegible (L551), "Cover on Book Value" illegible (L554), footnote (vi) truncated (L654). Flagged for source re-check; none alters a forensic conclusion.

Additional adjudication — **Fees income "58.4" magnitude**: the printed 58.4 (L289) is a decimal artifact; the Q1FY27 revenue subtotal 7,510.30 (L291) = 7,478.68 + 5.84 + 25.79, so the true value is ~5.84 lakhs. This does not create a subtotal break; it is folded into the fee-reclassification finding F12-2.

Notion checklist tests: standalone-vs-consolidated gap = none (F2, no subsidiary appears); GNPA 0.54%/NNPA 0.48% vs 0.09% baseline (F4-1, below 1.5% tripwire); Stage-wise ECL = NOT FOUND (F5-1); CRAR 26.63% healthy (L385); cost-of-funds/spread compression confirmed (F4-2); Augmont RPT dependency confirmed (F12-1); warrant cash inflow Rs 30 Cr pending (F10-2). ROE and the Rs 30 buy-trigger are price/return items for A4, not document-testable here.

---

## HANDOFF TO A4 (convert to management questions)

FORWARD-SIGNAL: F4-1 (GNPA 6x baseline), F4-2 (spread compression), F5-1 (impairment collapse / low PCR / no Stage-ECL), F10-2 (Rs 30 Cr warrant call pending), F12-1 (Augmont/RPT omnibus), F12-2 (fee-income reclassification), F13-1 (Rs 5,000 Cr borrowing + NCD enabling resolutions).

AMBIGUOUS: F10-1 (Basic < Diluted EPS), F14-1 (EPS cross-table mismatch), F14-2 (monitoring-agency inconsistency on Rs 199 Cr NCD), F14-3 (Annexure 4 199>135 flagged "No").

```yaml
stage: A3-forensics
company: "finkurve"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/finkurve-q1fy27/work/forensics_results_finkurve_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: FINDING
  F5: FINDING
  F6: PASS
  F7: PASS
  F8: PASS
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F4-1", check: "F4", line: "L380-383", classification: "FORWARD-SIGNAL", implication: "GNPA 0.54%/NNPA 0.48% up ~6x from 0.09% baseline on a 72% LTV gold book; below 1.5% tripwire but the trend is the asset-quality watch item"}
  - {id: "F4-2", check: "F4", line: "L288, L295, L361-362", classification: "FORWARD-SIGNAL", implication: "Finance cost +278% YoY outran interest income +181% -> spread compression; DSCR 0.41, ISCR 1.38 thin"}
  - {id: "F5-1", check: "F5", line: "L298, L384", classification: "FORWARD-SIGNAL", implication: "Impairment charge 20.38L vs FY26 run-rate ~554/qtr; PCR only 10.45%; no Stage-wise ECL disclosed; normalising provisions would cut PBT ~48%"}
  - {id: "F10-1", check: "F10", line: "L313-314", classification: "AMBIGUOUS", implication: "Diluted EPS 0.58 > Basic 0.50 is impossible under Ind AS 33 -> typo or computation error, resolve before trusting EPS"}
  - {id: "F10-2", check: "F10", line: "L310, L697-711", classification: "FORWARD-SIGNAL", implication: "Rs 30 Cr (75% of warrant money) uncalled = pending cash inflow plus pending dilution; Notion tripwire dilutive raise <Rs 40"}
  - {id: "F12-1", check: "F12", line: "L127, L131, L135", classification: "FORWARD-SIGNAL", implication: "Omnibus RP loan grant/acceptance + Augmont fee/brand/tech framework to AGM43(2027); confirms Augmont dependency, no rupee quantum disclosed"}
  - {id: "F12-2", check: "F12", line: "L289, L296, L387", classification: "FORWARD-SIGNAL", implication: "Fee income Q1FY26 1,323.51 -> FY26 101.72 -> Q1FY27 ~5.84 via Note 8 regrouping; the Notion fee reclassification risk made visible; expense side 1,363.74/qtr is Augmont pass-through"}
  - {id: "F13-1", check: "F13", line: "L148, L152, L156", classification: "FORWARD-SIGNAL", implication: "Rs 5,000 Cr borrowing power + Sec 186 hike + private-placement NCD enabling resolutions foreshadow large debt scale-up / D/E ramp to 4-4.5x"}
  - {id: "F13-2", check: "F13", line: "L159", classification: "NEUTRAL-FACT", implication: "Independent director continued (not dropped) past 75 by special resolution -> retention/governance signal"}
  - {id: "F14-1", check: "F14", line: "L313-314, L368-369", classification: "AMBIGUOUS", implication: "EPS differs across two tables in the same document (Basic 0.50 vs 0.60; Diluted 0.58 vs 0.59) -> data-integrity/control question"}
  - {id: "F14-2", check: "F14", line: "L673-674, L735-736", classification: "AMBIGUOUS", implication: "Rs 199 Cr NCD marked Monitoring Agency Not Applicable while Rs 141.50 Cr equity carries CRISIL -> compliance/disclosure question"}
  - {id: "F14-3", check: "F14", line: "L737, L758", classification: "AMBIGUOUS", implication: "Funds utilised Rs 199 Cr exceed original allocation Rs 135 Cr yet deviation flag = No -> arithmetic/narrative tension"}
  - {id: "F14-4", check: "F14", line: "L253-256", classification: "NEUTRAL-FACT", implication: "AUDITOR_CHANGE: Q1FY26 comparative reviewed by predecessor auditor; first full cycle under Ladha Singhal & Associates, watch for comparative restatement at AR"}
forward_signals: ["F4-1", "F4-2", "F5-1", "F10-2", "F12-1", "F12-2", "F13-1"]
ambiguous: ["F10-1", "F14-1", "F14-2", "F14-3"]
commitments:
  - {commitment: "Grant of loans to Related Parties (material RPT)", implied_date: "AGM42->AGM43, 2027", ref: "L127", status_word: "approved-pending"}
  - {commitment: "Acceptance of loans from Related Parties (material RPT)", implied_date: "AGM42->AGM43, 2027", ref: "L131", status_word: "approved-pending"}
  - {commitment: "Augmont Goldtech payments (fees/commission/brand/tech)", implied_date: "AGM42->AGM43, 2027", ref: "L135", status_word: "approved-pending"}
  - {commitment: "Borrowing power up to Rs 5,000 Cr (Sec 180)", implied_date: "on AGM approval", ref: "L148", status_word: "approved-pending"}
  - {commitment: "Increase Sec 186 threshold", implied_date: "on AGM approval", ref: "L152", status_word: "approved-pending"}
  - {commitment: "Issue of NCDs on private placement", implied_date: "forthcoming", ref: "L156", status_word: "approved-pending"}
  - {commitment: "Continuation of directorship (Himadri Bhattacharya) post-75", implied_date: "on AGM approval", ref: "L159", status_word: "approved-pending"}
  - {commitment: "Warrant balance Rs 30 Cr (75%) to be received", implied_date: "within warrant exercise window (issued May 2025)", ref: "L697-711", status_word: "underway"}
  - {commitment: "Results upload to company website", implied_date: "immediate", ref: "L112", status_word: "will be uploaded"}
gate_a3: pass
blank_checks: []
```
