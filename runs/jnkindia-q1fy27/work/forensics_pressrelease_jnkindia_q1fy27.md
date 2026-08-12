# A3 FORENSIC NOTES — JNK India Limited (JNKINDIA), Q1 FY27, doctype: presentation (3-page Reg 30 press release)

Source extract: `runs/jnkindia-q1fy27/work/extract_pressrelease_jnkindia_q1fy27.txt`
Reconciliation contract: `runs/jnkindia-q1fy27/work/ledger_pressrelease_jnkindia_q1fy27.md`
Prior-quarter extract: none provided (verbatim EoM / entity diffs not possible this run).
Ledger reconciliation: 100% — every row of Categories A (29 blocks), B (numeric-token lines), C (5 line items), D (3 notes), E (16 named items), F (N/A) read verbatim at its cited line before judging.

Doctype note: this is a narrative Reg-30 press release. Balance-sheet / auditor / statement-structure checks (F1–F5, F8–F12, F15) have no substrate in a 3-page release and are marked N.A. with basis. Live checks are F6 (forward commitments), F7 (hedges), F13 (board/AGM/AR), F14 (drafting inconsistencies), F16 (dropped/reframed disclosures). F17 (silence audit) is N.A. — no transcript.

Arithmetic reconciliation performed on the results table (lines 73–78), all internally consistent on the **103.0** basis:
- Total Income YoY: 186.0 / 103.0 = 1.806 → +80.6% (matches table col + quote line 84).
- EBITDA growth: 21.9 / 7.2 = 3.04x ≈ 3.1x. EBITDA margin: 21.9/186.0 = 11.8%; 7.2/103.0 = 7.0%; 111.3/838.0 = 13.3%. All tie.
- PAT margin: 9.6/186.0 = 5.2%; 1.1/103.0 = 1.1%. Ties. (PAT growth 9.6/1.1 = 8.7x vs stated 8.5x — within rounding of an unrounded ~1.13 base; noted, not a standalone finding.)
- Organic Total Income ex-Chemdist (line 79, Rs 16.5 cr): (186.0 − 16.5)/103.0 − 1 = **+64.6%** vs the +80.6% headline.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------|----------------|---------------------|
| A3-F01 | F14 | Cat B line 85 / Cat C row 1 (NUMBER_MISMATCH) | p2 L85 vs L74 | "compared to Rs. 10.30 cr in Q1FY26" (L85) vs table "103.0" (L74) | NEUTRAL-FACT | Confirmed misplaced-decimal drafting error in the Chairperson's quote: the same sentence cites "~80.6%" growth to Rs 186.0 cr, and EBITDA/PAT margins only reconcile on 103.0. Not an economic issue; a proofreading lapse in a signed Reg-30 disclosure — governance/controls data point. |
| A3-F02 | F14 | Cat E row 2 & row 10 (entity naming overlap) | p2 L79; p3 L128-130 | "Revenue of Rs 16.5 cr from JNK Chemdist Limited" (L79) vs "joint venture with the founders of Chemdist Group … JNK India holding 51% equity share capital" (L128-130) | AMBIGUOUS | A 51%-held entity is a controlled subsidiary whose full Rs 16.5 cr revenue is consolidated into Total Income, yet the release also calls it a "joint venture." Characterization inconsistency affects how much of Chemdist's current and future revenue is truly attributable vs minority-shared. → A4 question. |
| A3-F03 | F6 | Cat A blocks 20-22; Cat D row 3 (FWD_LOOKING_CAVEAT) | p2 L96-99, L101-102, L105-107 | "We are entering the off-shore, metals & minerals … focusing more on renewable energy" (L96-97); "executing the green hydrogen project and actively pursuing more opportunities" (L98-99); "this expansion will broaden our addressable market" (L101-102) | FORWARD-SIGNAL | Dateless diversification commitments into off-shore, metals & minerals, renewables and green hydrogen. Undated and unquantified — feed the Role 5 promise-vs-delivery tracker; each needs a milestone/date extracted next quarter. → A4. |
| A3-F04 | F16 | Cat D row 1 (HEADLINE_QUALIFIER); Cat C rows 2-3 | p2 L87-88; L75-76 | "we have maintained an EBITDA margin of 11.8% … maintaining a stable margin profile" (L87-88); EBITDA line labelled "(Includes Other Income)" (L75) | AMBIGUOUS | 11.8% is down ~150 bps from FY26's 13.3% and below the Notion 13% floor / 14-16% target (T2), yet framed as "stable." EBITDA "Includes Other Income," so operating-EBITDA margin is thinner still. Softened margin language over a compressing print. → A4. |
| A3-F05 | F16 | Cat A blocks 20-24; Cat E rows 3,6,7,8 | p2 L96-99; p3 L122-124; p2 L91 | "expanded its portfolio to include waste gas handling systems such as flares and incinerators, hydrogen production … solar EPC" (L122-124); "order book on June 30, 2026 is Rs 1,801 cr" (L91) | FORWARD-SIGNAL | Matches the flagged NARRATIVE-ROTATION RISK: heavy emphasis on waste-gas / renewables / green-hydrogen adjacencies while the Rs 1,801 cr order book is presented undifferentiated — no direct-vs-subcontract split, no fired-heater core OB, no JNK Global share (Notion: ~82%). Rotation toward the new-vertical story while core-heater momentum and cash conversion go undisclosed. → A4. |
| A3-F06 | F16 | Cat E rows 4-5 | p2 L91-92 | "order book … is Rs 1,801 cr" (L91); "bidding pipeline of Rs. ~6,000 cr" (L92) | AMBIGUOUS | Order book carries no definition qualifier (gross vs net of GST, executed vs pending) and no prior-period comparative; pipeline is an approximate "~6,000 cr." Definition/comparability opacity blocks QoQ order-book trend and any book decel read. → A4. |
| A3-F07 | F16 | Cat D row 2 (COMPARABILITY_CAVEAT) | p2 L79 | "Q1FY27 Total Income includes Revenue of Rs 16.5 cr from JNK Chemdist Limited which was not part of it in Q1FY26" | FORWARD-SIGNAL | Company-disclosed inorganic contribution: strip Chemdist and organic Total Income growth is +64.6% vs the +80.6% headline. Sets a lower like-for-like base rate for forward organic growth expectations. → A4. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 Zero-value standing line items | N.A. | 5-line summary table only; ledger Cat C confirms ZERO_STANDING = 0. No template statement with standing nil lines. |
| F2 Standalone vs consolidated | N.A. | Only unaudited **consolidated** figures shown (L68); no standalone column to decompose. |
| F3 Shell-entity detection | N.A. | No cost-line breakdown (no Cost of Materials / Employee Benefits / Depreciation) to compare S vs C. |
| F4 Unaudited contribution ratio | N.A. | No auditor report / "Other Matters" paragraph in a press release. |
| F5 Going concern / EoM tracking | N.A. | No auditor EoM; no prior-quarter extract for verbatim diff. |
| F6 Forward-commitment phrase mining | **FINDING** | A3-F03 — dateless entry/execution commitments into off-shore, metals & minerals, renewables, green hydrogen (L96-102). |
| F7 Hedge phrase mining | PASS | Only generic Safe Harbor "subject to numerous risks … may differ materially" (L140-142). No note-level hedge on revenue lumpiness / customer concentration; no prior quarter to establish a newly-added hedge. |
| F8 Tax forensics | N.A. | No tax line, ETR, or deferred-tax disclosure. |
| F9 OCI forensics | N.A. | No OCI / actuarial disclosure. |
| F10 Share count and dilution | N.A. | No paid-up capital, share count, or EPS in the release. |
| F11 Reserves and net worth tie-out | N.A. | No balance-sheet / net-worth figures. |
| F12 Segment forensics | N.A. | No segment assets/liabilities/revenue table. |
| F13 Board outcome beyond results | PASS | Checked: no AGM notice, record date, AR/Board's-Report approval, or director term dates. Arvind Kamath named as Chairperson & WTD (L82) with no re-appointment term. |
| F14 Note drafting inconsistencies | **FINDING** | A3-F01 (quote "10.30" vs table 103.0, L85 vs L74) and A3-F02 (JNK Chemdist "subsidiary" vs "joint venture," L79 vs L128-130). |
| F15 Entity list diffs | N.A. | No formal consolidation entity list; no prior-quarter ledger. Chemdist scope-entry captured under F07/F02 instead. |
| F16 Dropped / reframed disclosures | **FINDING** | A3-F04 (margin "stable" reframe), A3-F05 (narrative rotation + undecomposed order book), A3-F06 (order-book definition/comparative gap), A3-F07 (inorganic Chemdist in headline growth). |
| F17 Concall silence audit | N.A. | No transcript; silence audit not runnable. Notion checklist items instead frame F06/F16 above. |

Every check marked exactly one of PASS / FINDING / N.A. No blanks — GATE A3 pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/slide ref | status word |
|------------|-------------|----------------|-------------|
| Enter off-shore and metals & minerals verticals; increase renewable-energy focus | none stated | p2 L96-97 (block 20) | initiated ("are entering") |
| JNK Chemdist executing the green hydrogen project; pursuing adjacent opportunities | none stated | p2 L98-99 (block 20) | underway ("executing") |
| Expansion will broaden addressable market and enable participation in emerging investment opportunities | none stated | p2 L101-102 (block 21) | intent ("will broaden") |
| Convert the ~Rs 6,000 cr bidding pipeline into new orders | none stated | p2 L92, L105-106 (blocks 19, 22) | in process ("converting") |
| Sustain margin discipline as the business scales | none stated | p2 L88-89 (block 18) | ongoing ("remain focused on sustaining") |

All commitments are undated and unquantified — Role 5 tracker rows requiring a date/milestone at the next quarter.

---

```yaml
stage: A3-forensics
company: "JNKINDIA"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/jnkindia-q1fy27/work/forensics_pressrelease_jnkindia_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
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
  - {id: "A3-F01", check: "F14", line: "L85 vs L74", classification: "NEUTRAL-FACT", implication: "Quote 'Rs. 10.30 cr' vs table 103.0 — misplaced-decimal drafting error in signed Reg-30 release; controls/governance data point, no economic impact."}
  - {id: "A3-F02", check: "F14", line: "L79 vs L128-130", classification: "AMBIGUOUS", implication: "JNK Chemdist called both a revenue-consolidated subsidiary (51%) and a 'joint venture' — attribution of current/future Chemdist revenue unclear."}
  - {id: "A3-F03", check: "F6", line: "L96-99, L101-102", classification: "FORWARD-SIGNAL", implication: "Undated diversification commitments (off-shore, metals & minerals, renewables, green hydrogen) for promise-vs-delivery tracking."}
  - {id: "A3-F04", check: "F16", line: "L87-88, L75", classification: "AMBIGUOUS", implication: "11.8% margin (down 150bps vs FY26 13.3%, below 13% floor) framed as 'stable'; EBITDA 'Includes Other Income' so operating margin thinner."}
  - {id: "A3-F05", check: "F16", line: "L96-99, L122-124, L91", classification: "FORWARD-SIGNAL", implication: "Narrative rotation to waste-gas/renewables while Rs 1,801cr order book undecomposed (no direct-vs-subcontract, no fired-heater core, no JNK Global share)."}
  - {id: "A3-F06", check: "F16", line: "L91-92", classification: "AMBIGUOUS", implication: "Order book lacks definition qualifier and prior-period comparative; pipeline approximate — blocks QoQ order-book trend/decel read."}
  - {id: "A3-F07", check: "F16", line: "L79", classification: "FORWARD-SIGNAL", implication: "Headline +80.6% includes inorganic Rs 16.5cr Chemdist; organic growth +64.6% sets lower forward like-for-like base."}
forward_signals: ["A3-F03", "A3-F05", "A3-F07"]
ambiguous: ["A3-F02", "A3-F04", "A3-F06"]
commitments:
  - {commitment: "Enter off-shore and metals & minerals verticals; increase renewable-energy focus", implied_date: "none stated", ref: "p2 L96-97", status_word: "initiated"}
  - {commitment: "JNK Chemdist executing green hydrogen project; pursuing adjacencies", implied_date: "none stated", ref: "p2 L98-99", status_word: "underway"}
  - {commitment: "Expansion will broaden addressable market / emerging investment opportunities", implied_date: "none stated", ref: "p2 L101-102", status_word: "intent"}
  - {commitment: "Convert ~Rs 6,000cr bidding pipeline into new orders", implied_date: "none stated", ref: "p2 L92, L105-106", status_word: "in-process"}
  - {commitment: "Sustain margin discipline as business scales", implied_date: "none stated", ref: "p2 L88-89", status_word: "ongoing"}
gate_a3: pass
blank_checks: []
```
