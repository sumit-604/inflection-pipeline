# STAGE 12B: VERIFIER B — RED-FLAG AUDIT (KRONOX, run 2026-08-30)

**Mode: NO-CONCALL.** KRONOX holds no earnings calls; no transcripts exist. Per
the orchestrator's NO-CONCALL rule and the Verifier B rubric adapted to it, I read
the FY26 management commentary and the two results filings myself, fresh, built my
own red-flag list, then compared it against the B05 concall analysis. B06 (peer
verification) is cross-referenced where a peer statement bears on a KRONOX flag.

Sources read in full (page-marked .txt, primary):
- AR FY26: Chairman's Letter (p.18-19), Board's Report (p.36-42), MD&A (p.58-60),
  Financial Snapshot (p.11), Notes 3/5/RPT/ratios (p.100, p.114), contingent
  liabilities (p.114). File: `work/annual-report__2f872b7a-...txt`
- FY26 audited results, 21-May-2026: `work/results__4c8de5ae-...txt`
- Q1 FY27 results, 12-Aug-2026: `work/results__03380acb-...txt`

There is no analyst Q&A, no cross-quarter tone evidence, and no
management-under-pressure material anywhere in this set. Repeated-evasion tests
(rubric rule 5 CRITICAL trigger) are structurally untestable here; no CRITICAL can
arise from a repeated-evasion miss because no Q&A source exists.

---

## PART 1: INDEPENDENT RED-FLAG LIST (from AR + results only)

Built before re-reading B05's flag list against my own.

| # | Red flag | Anchor | My severity |
|---|---|---|---|
| 1 | Dahej Unit IV "new deadlines finalized" (production in 2 years, full unit in 3) carries no capex rupee figure, no capacity, no commissioning quarter, and no balance-sheet trace: company-wide CWIP Rs 87.6 lakh (up only Rs 11.6 lakh YoY), capital commitments stated NIL. A "finalized" multi-year restart with zero capital backing on announcement day. | Chairman's Letter p.18 (l.409-418); CWIP Note 3 p.100 (l.10694, "87.6 76.0"); Contingent Liabilities/commitments NIL p.114 (l.11444-11447) | HIGH |
| 2 | Multi-year slippage: land acquired 2022, State + Central clearances obtained through 2024-2025, construction still "could not be started" as of the AR signing (12-Aug-2026); cause given only as "unforeseen circumstances," never elaborated. | Chairman's Letter p.18 (l.400-411); milestones p.4-5 (per B05); regulatory dates per COMPANY MEMORY | MEDIUM |
| 3 | ROCE fell 49.46% (FY23) to 43.15% to 38.03% to 32.22% (FY26), 17 points in four years. Disclosed as a number in the Financial Snapshot and the ratio note, but never discussed or explained anywhere in the MD&A or Board's Report. | Financial Snapshot p.11 (l.286); ratio note p.114 (l.11680: ROCE 0.32 vs 0.38, variance -16.5%) | MEDIUM |
| 4 | **Earnings quality: reported profit growth is largely non-operating.** FY26 Other Income roughly doubled (Rs 519.40 lakh vs Rs 252.60 lakh); revenue from operations grew only +1.03%. Operating PBT (PBT minus other income) was near-flat at +1.2% (Rs 3,211.9 vs Rs 3,174.5 lakh); the entire +8.6% profit growth came from treasury/other income. Q1 FY27 PAT +38.5% YoY overstates operating gain: PBT grew +16.2% and the effective tax rate fell to 25.6% from 37.5% a year earlier; revenue growth (+13.4%) is the genuine operating figure. | Board's Report p.36 (l.2992-3011: rev 10122.00, other income 519.40/252.60, PBT/PAT); FY26 results p.2 (other income 518.40 vs 252.6); Q1FY27 results p.3 (l.39-56: rev 2830.5 vs 2496.7, PBT 981.0 vs 844.1, PAT 730.3 vs 527.3) | MEDIUM |
| 5 | MD&A (p.58-60) is entirely generic macro content (world GDP 3.1%, India 6.4-6.5%, EMDE, Middle East). No company-specific financial-performance discussion, no company outlook, no sector-specific data for high-purity fine chemicals. (Company-specific risk IS covered elsewhere: Board's-Report risk paragraph and Financial Risk Management Note 38, so the MD&A gap is disclosure-quality, not a total risk-disclosure omission.) | MD&A p.58-59 (l.7413-7744); risk note l.11761+, Note 38 l.11688 | LOW-MEDIUM |
| 6 | Company took on borrowings in FY26 (proceeds from borrowings Rs 160.7 lakh; finance cost Rs 11.4 lakh; debt-equity 0.01, "NA" in FY25 = previously debt-free) while holding a large and growing >12-month fixed-deposit balance. Borrowing while cash-rich is an unexplained capital-allocation quirk; amount is small. | Cash flow proceeds from borrowings l.10859; finance cost Q1FY27 results l.47; ratio note debt-equity l.11670-11683 | LOW |
| 7 | R&D and technology-absorption disclosures are single-sentence boilerplate with no rupee figure ("incurred legitimate expenses on Research & Development"; "neither imported technology nor obtained any indigenous technology"). | Board's Report p.37 (l.3190-3200) | LOW |
| 8 | No customer, product-line, or geographic breakdown despite ~185 products; single Ind AS 108 segment; export mix rose to 32.39% with zero commentary on the driver. | Board's Report/segment Note 32 (per B05); export mix Financial Snapshot p.11 (l.296) | LOW-MEDIUM |
| 9 | Excuse framing: "tariff war from America" and "war between America and Iran" cited as making the year difficult, placed beside the unexplained internal Dahej delay, inviting the reader to infer a link the company never states. B06 finds every comparable peer grew +6% to +35% through the same shock, so the "difficult year" framing does not hold as a revenue-stall cause. | Chairman's Letter p.18 (l.391-411); B06 Q1/Q3 CONTRADICTED/PARTIALLY VERIFIED | MEDIUM |

**Not counted as a red flag (noted for the record):** the Q1 FY27 covering letter
mislabels the period as "quarter ended June 30, 2025" and calls unaudited results
"duly signed audited financial results" (l.3, l.10); the results table has heavy OCR
noise. Clerical/hygiene, not a management-credibility item.

Independent flags found: **9.**

---

## PART 2: COMPARISON AGAINST B05

| # | My flag | B05 status | Verdict |
|---|---|---|---|
| 1 | Dahej no capex/CWIP/commitment trail | B05 red_flag #1 (HIGH), Section 2A/2D | **CAUGHT** — anchors and severity match exactly |
| 2 | Multi-year slippage, "unforeseen circumstances" | B05 red_flag #2 (MEDIUM), timeline_slippages | **CAUGHT** |
| 3 | ROCE decline never discussed | B05 red_flag #3 (MEDIUM), Section 2D | **CAUGHT** — I add that the decline is numerically disclosed (snapshot + ratio note) and the FY26 variance (-16.5%) sits below the 25% mandatory-explanation threshold, so the finding is narrative silence, not a disclosure omission. Does not change the flag |
| 4 | Earnings quality: profit growth non-operating / tax-flattered | Not flagged. B05 noted the growing FD balance under ROCE and called Q1FY27 "+38.5% PAT... a genuine post-FY26 acceleration" (analyst_note) without the tax/other-income caveat | **MISSED** — thesis-relevant: trigger #2 (re-acceleration) and any forward earnings basis rest partly on profit that is treasury- and tax-driven, not operating |
| 5 | MD&A generic, no company-specific content | B05 red_flag #4 (LOW), Section 3B | **PARTIALLY CAUGHT** — B05 caught the substance but framed it only as "no sector-specific content" at LOW; I read the whole MD&A as missing company-specific financial-performance and outlook discussion. Weighting difference only |
| 6 | Borrowing while cash-rich | Not flagged | **MISSED** — MINOR; amount immaterial |
| 7 | R&D boilerplate | B05 red_flag #5 (LOW), Section 2D | **CAUGHT** |
| 8 | No customer/segment/geo breakdown | B05 Section 2D/3D | **CAUGHT** |
| 9 | External-blame excuse framing | B05 Section 2B, excuse_pattern "external-blame-heavy"; B06 contradiction | **CAUGHT** |

Caught: 6. Partially caught: 1. Missed: 2.

### B05 flags I did not independently generate — support test

All five B05 red_flags map onto flags I found independently. None is unsupported,
overstated, or invented.

| B05 red_flag | My verdict |
|---|---|
| Dahej no capex trail (HIGH) | SUPPORTED |
| Multi-year gap, unforeseen circumstances (MEDIUM) | SUPPORTED |
| ROCE decline never discussed + growing FD (MEDIUM) | SUPPORTED |
| MD&A no sector-specific content (LOW) | SUPPORTED |
| R&D boilerplate (LOW) | SUPPORTED |

`pipeline_flags_not_supported: []`

---

## PART 3: PROMISE-DELIVERY SPOT CHECKS

B05's promise-delivery tracker (Section 2A) substitutes AR-guidance-vs-results for
the missing cross-quarter transcript comparison. I re-verified four of its four rows
against source.

| # | B05 row | Direction check | Result |
|---|---|---|---|
| 1 | "Revenue maintained vs prior year" -> Delivered | Revenue from ops Rs 10,122.00 lakh vs Rs 10,019.39 lakh (+1.03%), Board's Report p.36 (l.2992); results p.2 confirm | **CONFIRMED** |
| 2 | "Dividend consistent with policy" -> Delivered | Rs 0.50/share (5%) recommended FY26, Rs 185.40 lakh absorbed, Board's Report p.37 (l.3023-3031); dividend paid Rs 185.5 lakh in the cash flow (l.166) | **CONFIRMED** |
| 3 | "Construction to follow approvals" -> Missed | "the work at Unit IV, Dahej could not be started," Chairman's Letter p.18 (l.409-411) | **CONFIRMED** |
| 4 | "New 2y/3y deadlines" -> Partial/unresolved, no capital trail | CWIP Rs 87.6 lakh (l.10694); capital commitments NIL (l.11444-11447) | **CONFIRMED** |

Checked 4, confirmed 4, wrong 0. The tracker's directions are accurate. I would add
one qualifier to row 1: revenue was maintained, but the profit line above it grew
almost entirely on non-operating income (Part 1 #4), so "delivered" understates how
flat the operating engine was.

---

## PART 4: CREDIBILITY GRADE

B05 grades management **C** (NO-CONCALL default; can rise to B only on documented
guidance-vs-delivery, which the single missed load-bearing promise blocks).

**Concur with C.** The two delivered promises are low-bar (unchanged dividend, flat
revenue framing); the one load-bearing promise (Dahej) shows a documented miss and a
restated deadline with no capital backing; and my added earnings-quality finding
(profit growth non-operating and tax-flattered) points the grade down, not up. No
case exists to move above C; the floor holds.

`credibility_grade_concur: concur`

---

## PART 5: SEVERITY AND COVERAGE

- No CRITICAL. Repeated-evasion (2+ quarter) CRITICAL is structurally untestable in
  NO-CONCALL mode; no Q&A source exists.
- One MAJOR: the missed earnings-quality flag (profit growth non-operating in FY26,
  tax-flattered in Q1 FY27), thesis-relevant to trigger #2 and the forward earnings
  basis.
- Minors: MD&A under-weighting (partially caught), the borrowing-while-cash-rich
  quirk (missed, immaterial).

**redflag_coverage: 78%** — of 9 independent red-flag-grade items, 6 fully caught
and 1 partially caught upstream (7/9). Two missed (earnings quality MAJOR; borrowing
quirk MINOR).

acceptance_rate = caught / independent flags = 6/9 = **67%** (above the 60% REWORK
floor).

---

```yaml
stage: B12b
company: "KRONOX"
run_date: "2026-08-30"
model: claude-opus-4-8
status: complete
no_concall_mode: true
independent_flags_found: 9
caught: 6
partially_caught: 1
missed:
  - {severity: "MAJOR", item: "Earnings quality not flagged: FY26 profit growth (+8.6%) is almost entirely non-operating (other income roughly doubled, Rs 519.40 vs 252.60 lakh; operating PBT +1.2%; revenue from ops +1.03%). Q1 FY27 PAT +38.5% is flattered by a tax-rate fall to 25.6% from 37.5%; operating growth is revenue +13.4% / PBT +16.2%. B05 called the Q1 figure a genuine acceleration without the caveat", anchor: "Board's Report p.36 (l.2992-3011); FY26 results p.2; Q1FY27 results p.3 (l.39-56)"}
  - {severity: "MINOR", item: "Company took on borrowings in FY26 (proceeds Rs 160.7 lakh, finance cost Rs 11.4 lakh, previously debt-free) while holding a large, growing fixed-deposit balance; unexplained capital-allocation quirk, immaterial amount", anchor: "cash flow l.10859; ratio note debt-equity l.11670-11683; Q1FY27 finance cost l.47"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 4, confirmed: 4, wrong: 0}
credibility_grade_concur: "concur — C holds; low-bar promises delivered, load-bearing Dahej promise missed with no capital backing, and the added earnings-quality finding points down not up"
redflag_coverage: 78            # (caught 6 + partially 1) / 9 independent flags, %
findings:
  - {severity: "MAJOR", location: "B05 Section 2A/2D + analyst_note (earnings quality)", note: "Missed that FY26 profit growth is non-operating (other income doubled; operating PBT +1.2%) and Q1FY27 PAT +38.5% is tax-flattered (eff. tax 25.6% vs 37.5%); thesis-relevant to trigger #2 and forward earnings basis"}
  - {severity: "MINOR", location: "B05 red_flags (capital allocation)", note: "Missed FY26 shift from debt-free to small borrowings while holding growing fixed deposits; immaterial size"}
  - {severity: "MINOR", location: "B05 red_flag #4 (MD&A)", note: "Under-weighted: MD&A lacks all company-specific financial-performance and outlook discussion, not only sector data; graded LOW, I read LOW-MEDIUM. Substance caught"}
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 67            # caught 6 / independent flags 9, %
```
