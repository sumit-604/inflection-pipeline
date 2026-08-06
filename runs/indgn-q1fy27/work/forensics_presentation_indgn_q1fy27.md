# A3 FORENSIC NOTES — PRESENTATION — INDGN Q1 FY27

Doctype: **PRESENTATION** (Indegene Q1 FY27 investor deck + fact sheet, 22 slides)
Source extract: `work/extract_presentation_indgn_q1fy27.txt` (749 lines, ocr_pages [2,12,15,20])
Ledger reconciled: `work/ledger_presentation_indgn_q1fy27.md` — **100%** (all 6 tables, all 22 slides read at cited lines)
Cross-reference for deck-only calls: `work/extract_results_indgn_q1fy27.txt` (Reg 33 filing, per A2)
Model: claude-opus-4-8 | Run: 2026-08-06

Doctype scope note: per the A3 spec, on a PRESENTATION F16 applies plus any F6/F10/F11
numbers the deck carries; audited-filing / balance-sheet / auditor checks (F2-F5, F9-F13,
F15) and the concall silence audit (F17) are N.A. and marked so. F1 fires because the deck's
P&L (slide 13) carries a genuine ZERO_STANDING row; F8 fires because the deck carries an ETR
disclosure; F14 fires on an internal cross-table inconsistency. OCR slides (2, 12, 15, 20) are
content-thin title/divider pages with no numeric KPI at stake; every quantified finding below
sits on a non-OCR slide, so OCR confidence does not gate any finding.

---

## FINDINGS TABLE

| id | check | ledger row ref | slide / line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F1 | Table 4; T2 slide 13 L404 | s13 / L404, fn L410 | "Exceptional items(1) — 203 —" ; "One-time provision towards the estimated cost of settlement of lawsuit alleging breach of Telephone Consumer Protection Act." | AMBIGUOUS | TCPA settlement is an *estimate* and (per filing) not yet executed at 30-Jun-26; the standing row can be re-populated with a true-up. Nil this quarter is "no incremental charge," not "closed." |
| FND-02 | F6 | T2 slide 8 L128; slide 10 | s8 / L261-262 ; s10 / L340-341, L325-326 | "we expect operating leverage to improve further and profitability to strengthen in the second half of the year" ; "revenue from Q3 improving profitability" ; GenAI offerings "moved from concept to revenue-generating engagements" | FORWARD-SIGNAL | Dated management promises: H2-FY27 margin lift, a Q3-FY27 outcome-based-deal profitability step. Feeds Role 5 promise-vs-delivery tracker; verifiable next 1-2 quarters. |
| FND-03 | F8 | T2 slide 13 fn L412 (DECK_ONLY) | s13 / L412 ; L405-406 | "Increased tax cost estimated basis Effective Tax Rate (ETR) of 23.9% for Q1'FY27 and 24.2% for Q4'FY26" | FORWARD-SIGNAL | ETR 23.9% sits ~127 bps below statutory 25.17% (shield ~₹19M on PBT 1,527). The *rate* is deck-only (0 hits in filing) — deck volunteers a favorable tax optic the filing omits; normalization toward statutory is a small future PAT headwind. |
| FND-04 | F14 | T2 slide 4 L87; slide 13 L162; slide 21 L231 | s4 / L127 vs s13 / L407 vs s21 / L645 | s4: "0.2% YoY" (unsigned, no arrow) ; s13 & s21: "-0.2%" | NEUTRAL-FACT | Same metric (PAT YoY) rendered with opposite/absent sign across three tables in one deck. Individually immaterial, a data-consistency / governance datapoint; the headline card is the flattering rendering. |
| FND-05 | F16 | T2 slide 4 L87-88 (DIRECTION_UNCLEAR) | s4 / L127 ; title L107 | "0.2% YoY ▲ 45.9% QoQ" (PAT) ; "4 days YoY ▲ 4 days QoQ" (DSO) ; "A Quarter of significant growth at scale" | AMBIGUOUS | Headline KPI card strips the sign/arrow from the two YoY moves that are NOT clean positives: PAT declined -0.2% YoY yet reads as bare "0.2%"; DSO's YoY glyph is absent while its QoQ up-arrow (worse) is shown. Optics of a down-PAT quarter under a "significant growth" banner. → A4 question. |
| FND-06 | F16 | T2 slide 5 L94-96; slide 13 L155,L162 | s5 / L135 title ; margins L149-153 ; s13 L400, L408 | "Revenue Re-Acceleration with Resilient Margins" ; EBITDA margin 20.2%→16.9%, PAT margin 15.3%→10.9% | AMBIGUOUS | "Resilient" framing over EBITDA margin -330 bps YoY and PAT margin -440 bps YoY. Sequential uptick (Q4 16.4%→Q1 16.9% EBITDA; 7.9%→10.9% PAT) is real but the YoY compression is reframed away. → A4 question. |
| FND-07 | F16 | T2 slide 4 L84-85; slide 13 L151 | s4 / L117-119 ; title L107 | "INR 10,631 M ▲39.7% YoY ... USD 112.5 M ▲26.5% YoY" ; "significant growth at scale" | FORWARD-SIGNAL | Deck leads with INR 39.7% YoY; USD is 26.5% (≈13 pt currency gap) and QoQ USD is only 2.5%. No organic / constant-currency / ex-M&A split anywhere in the deck (Notion #2). Headline overstates underlying momentum. → A4 question: organic cc ex-M&A growth. |
| FND-08 | F16 | T2 slide 22 L285-286 (DECK_ONLY) | s22 / L740, L743 ; L742, L744 ; s4 L127 | Net DSO 67/63/71, def "(1) Billed + Unbilled – Unearned" ; "Cash and Cash Equivalents 14,602/15,385/17,280", def "(2) Includes ... Current Investments, Bank balances and Non-Current Bank Deposits" | AMBIGUOUS | Two cash-conversion optics: DSO uses a non-standard formula folding unbilled revenue in as a receivable-equivalent (deflates the day-count); "Cash and Cash Equivalents" is a broadened liquidity aggregate. Even on the broadened basis, cash fell 17,280→14,602 (-15.5% YoY, -5.1% QoQ) while revenue rose — a cash drain the framing softens. Both deck-only. → A4 question. |
| FND-09 | F16 | T2 slide 17 L190-206 (DECK_ONLY, UNSOURCED_TAM) | s17 / L495, L491-511, L486 | "$135 B+ Our Market Opportunity" ; verticals $55B/$24B/$21B/$36B/$21B ; "~9-14% CAGR (2022-2026)" ; "Expanding our TAM" | AMBIGUOUS | TAM figures carry no external source cite; the five verticals sum to $157B ≠ the $135B+ headline (undisclosed overlap/subset). "Expanding our TAM" reframes the addressable market upward. Treat as management estimate. → A4 question. |

---

## CHECKLIST SCORECARD (all 17, one status each)

| # | Check | Status | One-line basis |
|---|---|---|---|
| F1 | Zero-value standing line items | **FINDING** | Slide 13 L404 Exceptional items dash/203/dash; TCPA settlement "estimated" and (per filing) not yet executed — FND-01. |
| F2 | Standalone vs consolidated decomposition | **N.A.** | Deck presents consolidated only; no standalone column exists to decompose. |
| F3 | Shell-entity detection | **N.A.** | No standalone-vs-consolidated cost lines in a presentation. |
| F4 | Unaudited contribution ratio | **N.A.** | No auditor Other-Matters paragraph in a deck. |
| F5 | Going concern / EoM scope | **N.A.** | No auditor EoM / going-concern language in a deck. |
| F6 | Forward-commitment phrase mining | **FINDING** | "we expect ... profitability to strengthen in the second half" (s8 L261-262); "revenue from Q3 improving profitability" (s10 L340-341); GenAI "concept to revenue-generating" (s10 L325-326) — FND-02, see Commitment Register. |
| F7 | Hedge phrase mining | **PASS** | Only boilerplate forward-looking disclaimer (s3 L86-96: "may lead to a material difference", "does not assume an obligation to update"). No newly-added note-level hedge on lumpiness/concentration. "Estimated settlement" hedge captured under F1. |
| F8 | Tax forensics | **FINDING** | ETR 23.9% (L412) vs statutory 25.17% = ~127 bps shield; the rate is deck-only (absent from filing); no "earlier-years" tax adjustment present — FND-03. |
| F9 | OCI forensics | **N.A.** | No OCI / actuarial disclosure in a deck. |
| F10 | Share count & dilution | **N.A.** | Deck carries no share count, paid-up capital, or EPS. |
| F11 | Reserves & net worth tie-out | **N.A.** | No net worth / other-equity figure in the deck (broadened cash figure handled under F16/FND-08). |
| F12 | Segment forensics | **N.A.** | Deck gives revenue mix % only; no segment assets/liabilities to trend. |
| F13 | Board outcome beyond results | **N.A.** | Presentation, not a Board Outcome; no AR/AGM/record-date/director-term content. |
| F14 | Note-drafting inconsistencies | **FINDING** | PAT YoY rendered "0.2%" unsigned on slide 4 (L127) vs "-0.2%" on slides 13 (L407) & 21 (L645) — cross-table sign inconsistency — FND-04. |
| F15 | Entity list diffs | **N.A.** | No consolidation/entity list in a deck; no prior-quarter deck ledger supplied. |
| F16 | Presentation-specific: dropped & reframed disclosures | **FINDING** | FND-05 (slide-4 PAT/DSO direction optics), FND-06 ("Resilient Margins" over -330/-440 bps), FND-07 (headline INR vs no organic/ccy split), FND-08 (non-standard DSO + broadened cash), FND-09 (unsourced/expanding TAM). Dropped-metric comparison limited — no prior-quarter deck ledger supplied (A2 Table 1 note). |
| F17 | Concall-specific: silence audit | **N.A.** | No transcript in scope; concall-specific. Notion-checklist coverage folded into F16: deck addresses margins (#1), DSO/cash (#3, non-standard), RPE/cohorts/attrition/headcount (#4), TAM (#5); the one item the deck does NOT address is organic ex-M&A/constant-currency growth (#2) — carried as FND-07. |

**Roll-up:** FINDING ×5 (F1, F6, F8, F14, F16) · PASS ×1 (F7) · N.A. ×11 · blanks 0 → **GATE A3: PASS.**

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide / line ref | status word |
|---|---|---|---|
| Operating leverage to improve and profitability to strengthen | H2 FY27 | s8 / L261-262 | expect (guidance / underway) |
| Restore margins to historical levels progressively as ahead-of-curve investments convert | through FY27 | s10 / L338-341 | underway |
| Outcome-based deal revenue improving profitability | from Q3 FY27 | s10 / L340-341 | committed (dated) |
| GenAI offerings moved concept → revenue-generating engagements | achieved this quarter | s10 / L325-326 | completed (status-change; scale = ongoing) |
| Overseas third-party-payroll contractors transitioned to direct employment | "currently" / ongoing | s7 / L246 ; s22 / L731 | in the process of (underway) |

---

## NOTES FOR A4

- **Forward-signals to convert to management questions:** FND-02 (H2/Q3 margin & profitability promises — pin the delivery quarter and the magnitude), FND-03 (why is the sub-statutory ETR disclosed in the deck but not the filing, and is 23.9% sustainable), FND-07 (state organic constant-currency ex-M&A growth vs the 39.7% INR headline).
- **Ambiguous → questions:** FND-01 (is the TCPA provision final or subject to true-up; settlement executed?), FND-05 (why no sign/arrow on the two YoY moves that are not clean positives), FND-06 (reconcile "Resilient Margins" with -330/-440 bps YoY), FND-08 (standard-basis DSO and true cash-equivalents; explain the 15.5% YoY cash decline), FND-09 (source the TAM figures; reconcile $157B of verticals to the $135B+ headline).
- **Confidence:** all quantified findings sit on non-OCR slides (4, 5, 8, 10, 13, 17, 22); OCR slides 2/12/15/20 contributed no numeric evidence. Slide-6 "Growing accounts by revenue tier" chart (CHART_LAYOUT_AMBIGUOUS in A2) was NOT relied on for any finding — tier-level counts to be confirmed against the source image before A4 cites them.
- **Dropped-disclosure gap:** no prior-quarter (Q4 FY26) deck ledger was supplied, so F16's "metrics present last quarter, absent now" and "changed chart baselines" limbs are unverified. A4 should source the Q4 FY26 deck if a quarter-over-quarter reframing check is wanted.

```yaml
stage: A3-forensics
company: "INDGN"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/indgn-q1fy27/work/forensics_presentation_indgn_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FND-01", check: "F1", line: "s13/L404,L410", classification: "AMBIGUOUS", implication: "TCPA settlement is an estimate not yet executed; standing row can re-populate with a true-up"}
  - {id: "FND-02", check: "F6", line: "s8/L261-262; s10/L340-341,L325-326", classification: "FORWARD-SIGNAL", implication: "Dated H2-FY27 margin-lift and Q3-FY27 outcome-deal profitability promises; feeds promise-vs-delivery tracker"}
  - {id: "FND-03", check: "F8", line: "s13/L412; L405-406", classification: "FORWARD-SIGNAL", implication: "ETR 23.9% ~127bps below statutory and deck-only; normalization is a small future PAT headwind"}
  - {id: "FND-04", check: "F14", line: "s4/L127 vs s13/L407 vs s21/L645", classification: "NEUTRAL-FACT", implication: "PAT YoY sign inconsistent across three tables; headline card is the flattering rendering"}
  - {id: "FND-05", check: "F16", line: "s4/L127,L107", classification: "AMBIGUOUS", implication: "Declining/unclear YoY moves (PAT -0.2%, DSO) shown unsigned/arrowless under a growth banner"}
  - {id: "FND-06", check: "F16", line: "s5/L135,L149-153; s13/L400,L408", classification: "AMBIGUOUS", implication: "'Resilient Margins' framing over EBITDA -330bps and PAT -440bps YoY"}
  - {id: "FND-07", check: "F16", line: "s4/L117-119,L107", classification: "FORWARD-SIGNAL", implication: "Headline 39.7% INR vs 26.5% USD; no organic/constant-currency/ex-M&A split disclosed"}
  - {id: "FND-08", check: "F16", line: "s22/L740,L743,L742,L744", classification: "AMBIGUOUS", implication: "Non-standard DSO (Billed+Unbilled-Unearned) and broadened cash def soften a 15.5% YoY cash decline"}
  - {id: "FND-09", check: "F16", line: "s17/L495,L491-511,L486", classification: "AMBIGUOUS", implication: "TAM unsourced; verticals sum $157B != $135B+ headline; 'Expanding our TAM'"}
forward_signals: ["FND-02", "FND-03", "FND-07"]
ambiguous: ["FND-01", "FND-05", "FND-06", "FND-08", "FND-09"]
commitments:
  - {commitment: "Operating leverage improves, profitability strengthens", implied_date: "H2 FY27", ref: "s8/L261-262", status_word: "expect"}
  - {commitment: "Restore margins to historical levels progressively", implied_date: "through FY27", ref: "s10/L338-341", status_word: "underway"}
  - {commitment: "Outcome-based deal revenue improving profitability", implied_date: "from Q3 FY27", ref: "s10/L340-341", status_word: "committed"}
  - {commitment: "GenAI offerings concept -> revenue-generating", implied_date: "achieved this quarter", ref: "s10/L325-326", status_word: "completed"}
  - {commitment: "Third-party-payroll contractors -> direct employment", implied_date: "ongoing", ref: "s7/L246; s22/L731", status_word: "in the process of"}
gate_a3: pass
blank_checks: []
```
