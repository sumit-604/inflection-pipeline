# A5 ADVERSARY / COMPLETENESS AUDIT — Data Patterns (India) Ltd (DATAPATTNS), Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Date:** 2026-07-31
**Under audit:** review_datapattns_q1fy27.md (A4 ANALYST)
**Method:** fresh independent grep/read pass over the three A1 extracts; every A4 derived number recomputed from raw source lines; A4 cites checked, not trusted.

---

## AUDIT 1 — COVERAGE

Fresh enumeration re-run against each extract, diffed to the A2 ledgers, then every ledger category checked for citation or explicit "reviewed, no finding" in A4.

| Doc | Category | A2 count | Fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|---|
| results | agenda_items | 1 | 1 (l.34 approval) | none — cited (0D Note 1 / preamble) | PASS |
| results | auditor_paras | 4 | 4 (l.76,82,89,98) | none — cited (0D unmodified) | PASS |
| results | line_items | 27 | 27 (20 stmt l.132-168 + 7 QIP l.199-207) | none — Step 1 + Note 4 | PASS |
| results | notes | 8 | 8 (Notes 1-7 + EPS footnote l.170) | none — 0D table lists all 8 | PASS |
| results | entities | 0 | 0 (Note 5 l.209) | none — S-vs-C = structural 0 | PASS |
| results | signature_blocks | 3 | 3 (CS l.47, auditor l.106-119, CMD l.219) | none — auditor cited (DP-F14a) | PASS |
| results | annexures | 0 | 0 | n/a | PASS |
| acquisition | disclosure_fields | 10 | 10 (S.No 1-10) | none — all 10 mapped to Q7-Q11 (F1,F6,F7,F11,F13,F14,F15,F17) | PASS |
| acquisition | line_items (granular) | 24 | 24 | none — incl. DISCLOSURE_GAP (incorp date/country) via Q8 | PASS |
| acquisition | letter_and_header_fields | 18 | 18 | none — approval caveat "if any" cited (acq F1/F14, Q10) | PASS |
| acquisition | signature_block_lines | 8 | 8 | none — timestamp-absent noted | PASS |
| presentation | slides | 32 | 32 ([page 1]..[page 32]) | none — preamble 32/32 | PASS |
| presentation | pl_margin_values | 340 | 340 | reconciled in aggregate; material rows cited Step 1/2/4 | PASS |
| presentation | orderbook_inflow_values | 98 | 98 | material rows cited (2,654 / 927.7 / 1,172 / 39) | PASS |
| presentation | segment_customer_mix | 63 | 63 | cited 6B items 3/11 | PASS |
| presentation | balance_cashflow_values | 296 | 296 | material rows cited Step 5 | PASS |
| presentation | other_headline_stats | 121 | 121 | material rows cited | PASS |
| presentation | zero_standing (dash) | 43 | 43 | reviewed (Exceptional-line silence → Q5/A3-F1-01) | PASS |
| presentation | footnotes | 9 | 9 | dual-order-book qualifier cited (A3-F16-01); TTM basis noted Step 5 | PASS |

**Gated preamble reconciliation:** A4 states 340+98+63+296+121 = **918** gated values, 43 zero-standing, 9 footnotes — matches the presentation ledger exactly. Acquisition preamble (10+24+18+8) and results preamble (8+27+1+4+3+0+0) match their ledgers exactly.

**Specific A2-flagged items requiring A3/A4 attention — all carried into A4:**
- Rs-1-Mn cross-slide mismatches (Slide 22 FY23 rev 4,534 vs Slide 28 4,535; FY22 3,108 vs 3,109) → A4 flag "Rs-1-Mn cross-slide drafting mismatches" (A3-F14-01). Cited.
- Slide 30 FY25 closing cash 376 vs Slide 29 Mar-25 cash 377 → same Rs-1-Mn umbrella flag. Cited.
- Mislabeled "Total equity and liabilities" subtotal (BS l.946 carries Total-Equity values) → A4 flag "mislabeled Total-Equity". Cited.
- "Navel System" typo (l.561) → A4 "'Navel/Naval'". Cited.
- SIGNATURE_BEFORE_BOARD_CONCLUSION (auditor 16:34:57 vs board 18:30) → DP-F14a, prominent flag + Q16. Cited.
- DISCLOSURE_GAP (STAC incorporation date, country) → Q8. Cited.
- OCI +Rs 0.6 Cr FY26 after 5-yr loss streak → A3-F9-01, Q17. Cited.

**Fresh rows found that the ledger lacks:** none.
**Orphan rows (ledger present, A4 absent):** none.

**Coverage note (not a FAIL):** the Slide-16 diversified order-book segment split A4 reports as "Services 30.0%, EW 31.9%, Radar 20.9%" (6B item 3 / 5B) sits on a chart the A2 ledger explicitly flagged `LAYOUT_AMBIGUOUS` (segment-to-value mapping not resolvable from layout text). A4 presents the reading without repeating the ambiguity caveat. The three values (30.0+31.9+20.9 = 82.8%, remainder 17.2% across six small segments summing to ~100%) are internally consistent and the item is non-arithmetic; carried as a caution for the Q2 visual cross-check, not a coverage failure.

**COVERAGE VERDICT: PASS.** Fresh counts equal ledger counts in every category; no orphan rows; no missing-from-ledger rows.

---

## AUDIT 2 — ARITHMETIC

Every A4 derived metric recomputed from raw extract lines (₹ Cr; results filing x1). Raw inputs: results l.132-168; deck cross-checks l.454-487.

| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+FC−OI) | 31.37 | 29.48+5.92+3.28−7.31 = 31.37 | l.142/141/154/133 | MATCH |
| Op EBITDA Q1FY26 | 32.08 | 33.95+5.49+3.19−10.55 = 32.08 | l.154/142/141/133 | MATCH |
| Op EBITDA Q4FY26 | 192.84 | 187.96+5.89+4.65−5.66 = 192.84 | l.154/142/141/133 | MATCH |
| Op EBITDA FY26 (ex-exceptional) | 373.99 | 366.55+22.95+12.45−27.96 = 373.99 | l.149/142/141/133 | MATCH |
| Op EBITDA margin Q1FY27 | 27.04% | 31.37/116.03 = 27.04% | l.132 | MATCH |
| Op EBITDA margin Q1FY26 | 32.30% | 32.08/99.33 = 32.30% | l.132 | MATCH |
| Op EBITDA margin FY26 | 40.44% | 373.99/924.77 = 40.44% | l.132 | MATCH |
| Op EBITDA margin YoY | −526 bps | 27.036 − 32.297 = −526 bps | l.132/484 | MATCH |
| Reported EBITDA Q1FY27 (PBT+D+FC) | 38.68 | 29.48+5.92+3.28 = 38.68 | l.154/142/141 | MATCH |
| Core PBT ex-OI Q1FY27 | 22.17 | 29.48−7.31 = 22.17 | l.154/133 | MATCH |
| Core PBT ex-OI Q1FY26 | 23.40 | 33.95−10.55 = 23.40 | l.154/133 | MATCH |
| Core PBT ex-OI YoY | −5.26% | −1.23/23.40 = −5.26% | derived | MATCH |
| Effective Tax Rate Q1FY27 | 25.17% | 7.42/29.48 = 25.17% | l.155/154 | MATCH |
| Effective Tax Rate Q1FY26 | 24.89% | 8.45/33.95 = 24.89% | l.155/154 | MATCH |
| Effective Tax Rate FY26 | 25.35% | 92.17/363.54 = 25.35% (post-exceptional PBT) | l.155/154 | MATCH |
| PAT margin Q1FY27 | 19.01% | 22.06/116.03 = 19.01% | l.156/132 | MATCH |
| Revenue YoY | +16.81% | 16.70/99.33 = 16.81% | l.132 | MATCH |
| Op EBITDA YoY | −2.21% | −0.71/32.08 = −2.21% | derived | MATCH |
| Other Income YoY | −30.71% | −3.24/10.55 = −30.71% | l.133 | MATCH |
| Reported PBT YoY | −13.17% | −4.47/33.95 = −13.17% | l.154 | MATCH |
| PAT YoY | −13.49% | −3.44/25.50 = −13.49% | l.156 | MATCH |
| EPS YoY | −13.41% | −0.61/4.55 = −13.41% | l.168 | MATCH |
| QoQ revenue | −66.4% | 116.03/344.85 − 1 = −66.4% | l.132/454 | MATCH |
| PAT bridge: Gross profit Δ | +12.28 (79.23→91.51) | 91.51−79.23 = +12.28 | l.132/137/139 | MATCH |
| PAT bridge: Employee Δ | −6.15 (+16.9%) | 42.53−36.38 = 6.15; /36.38 = 16.9% | l.140 | MATCH |
| PAT bridge: Other exp Δ | −6.84 (+63.5%) | 17.61−10.77 = 6.84; /10.77 = 63.5% | l.143 | MATCH |
| PAT bridge closes | −3.44 | +12.28−6.15−6.84−0.43−0.09−3.24+1.03 = −3.44 | derived | MATCH |
| OI-revert scenario PAT | ~24.5 | 32.72×(1−0.2517) = 24.49 | derived | MATCH |
| S-vs-C PAT gap (all periods) | 0.0% | no consolidated entity (Note 5 l.209) | l.209 | MATCH |
| Deck EBITDA = Op EBITDA tie | 314/321/1,928 Mn | 31.4/32.1/192.8 Cr vs filing 31.37/32.08/192.84 | l.462 | MATCH |
| FY26 deck EBITDA 371.0 vs filing 373.99 | Δ = exceptional | 373.99−3.01 = 370.98 ≈ 371.0 | l.462/153 | MATCH |
| CFO/PAT FY26 | 0.295x | 80.1/271.37 = 0.295x | l.998/156 | MATCH |
| Net cash Jun-26 | 465.9 | 4,659 Mn × 0.1 = 465.9 | l.326 | MATCH |
| Order-book soft share | ~65% | (2,654−927.7)/2,654 = 65.05% | l.286/330 | MATCH |
| Order waterfall tie | 9,277 | 9,265+1,172−1,160 = 9,277 | l.548-551 | MATCH |
| STAC true outlay | Rs 10 Cr | 1.50+8.50 = 10.0 | acq l.112-115 | MATCH |
| STAC FY26 turnover decline | ~5.7% | (416.85−442.19)/442.19 = −5.73% | acq l.127-128 | MATCH |
| Customer conc. BrahMos+Export | ~49% | 26.7+22.1 = 48.8% | l.444 | MATCH |
| Implied Q2-Q4 avg for 20% floor | ~331 | (1,109.7−116.03)/3 = 331.2 | l.132/262 | MATCH |

**ARITHMETIC VERDICT: PASS.** Every derived metric in A4's tables recomputes to A4's stated value within rounding. No mismatch found. The FY26 EBITDA basis switch (pre-exceptional 366.55 for operating EBITDA / operating metrics; post-exceptional 363.54 for the FY26 ETR) is internally disclosed by A4 in footnotes ¹ and ² and both reconcile to the deck.

---

## AUDIT 3 — ADVERSARIAL READ

Three most positive claims in A4, each attacked with the strongest bear counter buildable **from the same extracted text**, then tested for survival (i.e., supported by extract AND not already incorporated by A4).

**Positive claim 1 — "Net cash ~Rs 465.9 Cr; net-debt-free maintained; GREEN, far above the Rs 100 Cr tripwire" (Step 5 / checklist item 6).**
Bear counter: the Rs 465.9 Cr (deck l.326) is an undecomposed Jun-26 "Cash, Bank & Investment" aggregate; the Mar-26 balance sheet shows only Rs 56.9 Cr in pure cash & equivalents (l.966, 569 Mn), with the bulk in current investments Rs 328.9 Cr (l.962) and other bank balances Rs 37.0 Cr (l.968), against receivables ballooning to Rs 727.8 Cr (l.964) and chronic WC absorption of −Rs 211.4 Cr in FY26 (l.994). Plus Rs 26.25 Cr QIP undeployed, a Rs 150 cr capex plan, and a Rs 8.5 Cr STAC bailout loan drawing on the cushion.
Survives? **NO.** A4 already carries every load-bearing element: WC drag as structural (Step 5), receivables 727.8, QIP undeployed (DP-F6a), Rs 150 cr capex vs 0.30x CFO (Q15), STAC Rs 10 Cr immaterial to cushion. The only un-stated nuance (cash-vs-investment composition of the Jun-26 figure) does not alter the net-debt-free reading — investments are liquid and total debt is 0.0 (l.932). Not a required addition.

**Positive claim 2 — "No thesis-broken trigger has FIRED" (Step 6C).**
Bear counter: Trigger 1 (margin+export double-fail) already has one leg tripped — Q1 operating EBITDA 27.0% is below the 33% line — and the second leg sits Rs 9 Cr from firing (export OB Rs 39 Cr vs Rs 30 Cr threshold, l.566), with A4's own checklist item 10 rating the export book RED ("confirms decline"). "None fired" understates how close Trigger 1 is.
Survives? **NO.** A4 states this explicitly: Trigger 1 is "AMBER — half the margin leg tripped; export OB Rs 39 Cr sits just above the Rs 30 Cr line" and names it "the one to watch." Fully incorporated.

**Positive claim 3 — "Auditor expressed an unmodified conclusion; clean; no going-concern; thesis-broken trigger 5 = NO" (Step 0D / Step 6C).**
Bear counter: the unmodified conclusion is undercut at the governance level — the auditor's digital signature is timestamped 16:34:57 IST (l.113), ~1h56m before the Board's stated 18:30 conclusion (l.41), while the report asserts the Statement was "approved by the Company's Board of Directors" (l.82).
Survives? **NO.** A4 raises exactly this as DP-F14a, an AMBER governance flag, a propagated combined-verdict flag, and Q16. Fully incorporated.

**Additional positive claims tested (Revenue +16.8% YoY; STAC 1.3-2.0x accretion; order-book "visibility" Rs 2,654 Cr):** each is self-countered inside A4 — core operating PBT −5.3% strips the revenue headline (Step 2 diag 3); STAC accretion flagged unquantified with thin/negative net worth (Q7/Q9); order book flagged ~65% soft with Q1 inflow only Rs 117 Cr (A3-F16-01, Q2/Q14). None survives.

**SURVIVING BEAR COUNTERS REQUIRING GRAFT INTO A4: none.**

---

## VERDICT

**COMPLETE.**

- Coverage: fresh enumeration equals every A2 ledger count; no orphan rows; no missing-from-ledger rows; every material ledger row and every A2 flag is cited or reviewed in A4.
- Arithmetic: all A4 derived metrics recompute to A4's values within rounding; no discrepancy above rounding.
- Adversarial: the three (plus three secondary) most-positive claims are already bear-countered inside A4 from the same extract; no surviving counter needs grafting.

No loop-back to A2, A3, or A4 required. A4 proceeds to Notion save.

```yaml
stage: A5-adversary
company: "DATAPATTNS"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
