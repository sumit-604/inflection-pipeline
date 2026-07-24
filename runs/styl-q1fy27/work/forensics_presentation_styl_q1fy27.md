# A3 FORENSIC NOTES — presentation_styl_q1fy27 (Investor Presentation Q1FY27)
Company: Seshaasai Technologies Ltd (STYL) | Quarter: Q1FY27 | Doctype: presentation (32 slides, INR Million)
Source extract: /home/user/inflection-pipeline/runs/styl-q1fy27/work/extract_presentation_styl_q1fy27.txt
Ledger reconciled: 100% (Table 1 all 32 slides, Table 2 rows S6-01..S6-12, Table 3 L1..L11 slides 17/18, Table 4 IPO objects 1-4 + Total, all 8 flags read verbatim at cited lines)

Doctype lens: this is a deck, not a filing or transcript. Balance-sheet / auditor / entity-list / OCI / share-count checks (F2,F3,F4,F5,F9,F10,F11,F12,F13,F15) are N.A. because the deck carries none of that data. The active lenses are F16 (dropped/reframed disclosure, chart base games, non-GAAP bridges), F6/F7 (forward phrase and hedge mining), F8 (tax, computable from slides 17/18), F1 (the ZERO_STANDING IPO row), F14 (drafting inconsistencies). F17 concall silence is deferred; the thesis silence audit is delivered as the MONITORING OVERLAY table below (the task's stated priority overlay).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1 | F1 | Table 4 row 2 / ZERO_STANDING | line 935 (slide 31) | "Repayment of Borrowings 3,000.0 3,000.0 - 3,000.0 -" | NEUTRAL-FACT | ₹3,000mn IPO tranche for debt repayment is 100% deployed (B=B+C=3,000; unutilized 0). Explains Finance Cost collapse to ₹18.4mn (-76.2% YoY, line 524). The deleveraging tailwind is now EXHAUSTED — the ~₹59mn/yr YoY finance-cost benefit will not repeat in FY28 comparisons. |
| F6 | F6 | Table 1 slides 12/13/14 | lines 332, 330, 367, 397 | "Commenced payment card exports to Europe & Africa." | FORWARD-SIGNAL | New export revenue stream initiated Q1FY27; three multi-year tenders won (1 Payments line 330, 2 PSU-bank CFS line 367) = forward backlog; largest-retailer RFID "ramped up and stabilized" (line 397). Feeds Role 5 promise-vs-delivery tracker. |
| F8 | F8 | Table 3 L10/L11 slides 17/18 | lines 529-532 | "The lower margin in Q1FY26 was primarily due to higher tax provisioning" | AMBIGUOUS | ETR: Q1FY26 33.0% (181.4/549.7) -> Q1FY27 26.3% (215.0/817.9) -> Q4FY26 26.8%. The headline PAT +63.8% YoY is materially flattered by tax normalisation off an abnormally high Q1FY26 base; underlying pre-tax growth is +48.8% (PBT). Current 26.3% ETR still ~110bps above statutory 25.17%. |
| F14 | F14 | S6-05 vs S6-11 (NUMBER_INCONSISTENCY) | lines 163, 185 | "₹ 873.1 mn" (YoY block) vs "₹ 873.13 mn" (QoQ block) | NEUTRAL-FACT | Same metric (Q1FY27 Operating EBITDA), two precisions. Also L4 QoQ delta "51.17" two-decimal outlier (line 555) and "OPERTATING" typo (lines 162,184). Governance-hygiene, immaterial; reconcile the exact Operating-EBITDA figure against the results filing. |
| F16a | F16 | slide 10 chart vs slide 16 stack (ORDER_INFERRED / COLUMN_ALIGNMENT_UNCERTAIN) | lines 299-308 vs 466-478 | slide 10: "15,583 ... 14,632 14,411 ... FY24 FY25 FY26" | AMBIGUOUS (lean bear) | Slide 10 presents FY-revenue ASCENDING to a FY26 peak of 15,583 (₹1,558 Cr). But slide 16's segment stack sums FY24=15,583 / FY25≈14,631 / FY26≈14,395, i.e. DESCENDING, and Notion's FY26 base ₹1,441 Cr = 14,410 Mn matches slide 16's FY26, NOT slide 10's FY26. Either slide 10's year labels are reversed (3-yr revenue is flat-to-declining, dressed as growth) or a column-alignment artifact. Verify against source PDF layout + results filing before trusting the FY26 total. |
| F16b | F16 | S6-03/S6-04/S6-05 + L2 (non-GAAP bridge) | lines 154, 164, 509 | "EBITDA MARGIN 25.1% ↑135 bps YoY" vs "OPERATING EBITDA ... 23.2% ↑22 bps YoY" | FORWARD-SIGNAL | EBITDA ₹944.1mn = Operating EBITDA ₹873.1mn + Other Income ₹71.0mn (Other Income +203% YoY, line 509). Headline EBITDA-margin expansion of +135bps is almost entirely non-operating; the clean operating margin rose only +22bps YoY and is 23.2%. Numerator also mixes other income with a revenue-from-ops denominator (overstates vs 24.6% on total income). Other-income sustainability is a live question. |
| F16c | F16 | slide 15 (LABEL_AMBIGUITY) | lines 435-438 vs 154 | "Gross Margin (%) ... YOY +13.3%" | AMBIGUOUS | Under a "Gross Margin (%)" header the deck prints "YOY +13.3%", which is gross-PROFIT rupee growth (1,384->1,568). Actual gross MARGIN FELL 286bps YoY (44.5%->41.7%, line 154) and 527bps QoQ. The label invites reading margin as improving when it deteriorated. |
| F16d | F16 | slide 18 QoQ remark (seasonality framing) | line 550 | "Q4 has historically been the Company's strongest quarter in terms of revenue." | FORWARD-SIGNAL | Pre-emptive framing of the -6.9% QoQ revenue and -573bps QoQ EBITDA-margin drop as seasonal. Implies Q1/Q2 are structurally softer and Q4-loaded; sets a low internal bar for H1FY27. Confirm the seasonality claim against the FY26 quarterly revenue path (slides 12-14 do not show a clean Q1-trough pattern). |

---

## CHECKLIST SCORECARD (all 17, one status each — GATE A3)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING | FINDING | Slide 31 Repayment-of-Borrowings dash row = ₹3,000mn IPO tranche fully deployed; finance-cost tailwind now exhausted (line 935). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Deck shows Consolidated only (slides 17/18); no standalone column to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | Requires standalone-vs-consol cost lines; deck carries a single consolidated P&L. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor Other-Matters paragraph in a deck. |
| F5 GOING CONCERN / EoM | N.A. | No auditor report / EoM in a presentation. |
| F6 FORWARD-COMMITMENT MINING | FINDING | "Commenced" exports to Europe & Africa (line 332); 3 multi-year tenders won (lines 330,367); retailer volumes "stabilized" (line 397). |
| F7 HEDGE PHRASE MINING | PASS | Only generic forward-looking disclaimer boilerplate ("subject to known and unknown risks", line 109); no newly-added operational hedge on lumpiness/concentration detectable (NO_PRIOR_LEDGER limits diff). Seasonality framing captured under F16d. |
| F8 TAX FORENSICS | FINDING | ETR 33.0% (Q1FY26) -> 26.3% (Q1FY27); PAT +63.8% YoY flattered by tax normalisation, deck admits it (lines 529-532). |
| F9 OCI FORENSICS | N.A. | Deck discloses no OCI / actuarial lines. |
| F10 SHARE COUNT / DILUTION | N.A. | No paid-up capital, share count, or basic/diluted EPS in the deck. |
| F11 RESERVES / NET WORTH | N.A. | No other-equity / net-worth figure; deck gives only cash ₹3,690mn (line 951), nothing to tie out. |
| F12 SEGMENT FORENSICS | N.A. | Segment REVENUE disclosed (slides 12-14/16) but no segment assets/liabilities to trend. |
| F13 BOARD OUTCOME | N.A. | Investor deck, not a board-outcome filing; no AGM notice / resolutions / director term dates. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Operating EBITDA ₹873.1 vs ₹873.13 (lines 163/185); "51.17" precision outlier (line 555); "OPERTATING" typo (lines 162/184). |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list in deck; no prior ledger (NO_PRIOR_LEDGER). |
| F16 DROPPED / REFRAMED DISCLOSURES | FINDING | Four items: F16a slide10-vs-16 revenue base game; F16b EBITDA-vs-Operating-EBITDA non-GAAP bridge; F16c slide15 gross-margin label; F16d QoQ seasonality framing. |
| F17 CONCALL SILENCE AUDIT | N.A. | No transcript; thesis silence audit delivered in MONITORING OVERLAY below. Dropped-slide diff blocked by NO_PRIOR_LEDGER. |

Scorecard tally: PASS = 1 (F7); FINDING = 5 checks (F1, F6, F8, F14, F16 — F16 carries 4 sub-findings); N.A. = 11. No blanks. GATE A3 = pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide/line ref | status word |
|---|---|---|---|
| Payment card exports to Europe & Africa | Q1FY27 (in-quarter) | slide 12, line 332 | commenced (initiated) |
| 1 multi-year tender won — Payment cards | Q1FY27 | slide 12, line 330 | won |
| 2 multi-year tenders won — CFS, from PSU banks | Q1FY27 | slide 13, line 367 | won |
| Largest Indian retailer RFID volumes (Reliance-Retail candidate) | Q1FY27 | slide 14, line 397 | "ramped up and stabilized" |
| SIM card volume contribution to revenue | ongoing, undated | slide 14, lines 404-405 | "continue to build up" |

---

## MONITORING OVERLAY — Notion HELD-position checklist vs what the DECK discloses
(This is the pre-committed decision-gate overlay. Status = CONFIRM / CONTRADICT-BREACH / PARTIAL / SILENT, with slide/line cite.)

| # | Monitoring trigger | Deck status | Cite | Note |
|---|---|---|---|---|
| 1 | Revenue YoY >+10% | CONFIRM (+21.1%) | line 154, 507 | ₹3,764.7 vs ₹3,108.7mn. Caveat: off a "relatively subdued Q1FY26 base" (line 508); growth is IoT-led (see #14). |
| 2 | EBITDA margin sustain >27% | CONTRADICT / BREACH | lines 153, 163, 180 | 25.1% reported (23.2% Operating); below 27% trigger and down from 30.8% QoQ (-573bps). Gross margin -286bps YoY on West Asia conflict / RM / FX / logistics (lines 511-512). |
| 3 | IoT revenue >₹55 Cr | CONFIRM (₹67.4 Cr) | slide 14, line 395 | 674 Mn = ₹67.4 Cr; +144% YoY. (ORDER_INFERRED — verify bar-to-label mapping vs filing.) |
| 4 | SIM utilization >40% (vs 30%) | SILENT | lines 404-405 | Only "SIM card volumes continue to build up"; no utilization %. |
| 5 | Inventory days <80 (vs 86) | SILENT | line 516 | Only qualitative "strategic inventory management"; no days metric. |
| 6 | Receivable days stable / <80 | SILENT | — | No receivable-days or DSO figure anywhere in deck. |
| 7 | FY27 guidance (specific rev/margin) | SILENT / ABSENT | line 114 | No numeric FY27 guidance; disclaimer states "assumes no obligation to update any forward-looking information." Notable at a decision gate. |
| 8 | eSIM commercial launch (first rev / Q2FY27 date) | SILENT | line 421 | Only "eSIM has cross-industry potential" (aspirational); no launch date or first revenue. |
| 9 | Reliance Retail RFID volume disclosed | PARTIAL | line 397 | "one of the largest Indian retailer has ramped up and stabilized" — retailer unnamed, no volume/₹. |
| 10 | Promoter lock-in (no OFS near Sep 30 2026) | SILENT | — | No shareholding / lock-in / OFS disclosure in deck. |
| 11 | Promoter pledge stays 0% | SILENT | — | No pledge disclosure in deck. |
| 12 | Receivables factoring announced | SILENT | — | Not mentioned. |
| 13 | Gautam Jain concall participation | SILENT (deck cannot confirm) | slide 28, line 840 | Named Whole-time Director; participation is a transcript matter. |
| 14 | Payments QoQ — no 2 consecutive declines | CONTRADICT / BREACH | slide 12, line 325 | 1,984(Q3)->1,919(Q4)->1,582(Q1FY27) = TWO consecutive QoQ declines. Payments only +5.6% YoY (1,582 vs 1,498) — the laggard; total +21% is IoT-driven. (ORDER_INFERRED — confirm sequence vs filing.) |
| 15 | Cash-transition WC initiative addressed | PARTIAL / SILENT | lines 515-516 | Only generic "supply-chain agility through diversified sourcing" / "strategic inventory management"; no named cash-transition WC program. |

Headline vs Notion FY26 base cross-check:
- FY26 Rev ₹1,441 Cr: slide 16 stack FY26 ≈ 14,395 Mn (₹1,440 Cr) MATCHES; slide 10 labels FY26 = 15,583 Mn (₹1,558 Cr) which DOES NOT — see F16a (labeling/base inconsistency, lean bear).
- FY26 EBITDA 27.4%: slide 10 shows 27% (line 300) — consistent.
- FY26 PAT ₹240 Cr: slide 10 PAT margin 17% (line 299) x ~14,410 Mn ≈ ₹245 Cr — consistent.
- Mix Payments ~48% / CFS ~40% / IoT ~12%: Q1FY27 = Payments 42.3% / CFS 39.7% / IoT 18.0% (1,582 / 1,488 / 674 of 3,744) — mix shifting toward IoT, away from Payments; corroborates #14 Payments weakness.

MONITORING-TRIGGER RESULT: 2 CONFIRM (rev growth #1, IoT scale #3), 2 hard BREACHES (EBITDA margin <27% #2; Payments two consecutive QoQ declines #14), 2 PARTIAL (#9, #15), 9 SILENT — including four thesis-critical silences at a decision gate: FY27 guidance (#7), eSIM launch date (#8), SIM utilization (#4), and both working-capital-days metrics (#5,#6). The +21% headline is IoT-led and masks a declining, low-growth Payments core and a sub-threshold margin.

---

## HANDOFF TO A4 (findings to convert into management questions)
FORWARD-SIGNAL: F6 (export/tender/retailer commitments — delivery timeline), F16b (Other Income +203% sustainability behind the EBITDA-margin headline), F16d (seasonality claim — verify FY26 quarterly path).
AMBIGUOUS (lean bear): F8 (PAT growth quality ex-tax normalisation), F16a (FY26 revenue label/base reversal — is 3-yr revenue actually flat-to-declining?), F16c (gross-margin label vs actual -286bps).
Plus the silence rows (#4,5,6,7,8,10,11,12,15) and the two breaches (#2,#14) are A4/A5 concall-question material.

---

```yaml
stage: A3-forensics
company: "STYL"
quarter: "q1fy27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/styl-q1fy27/work/forensics_presentation_styl_q1fy27.md"
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
  - {id: "F1", check: "F1", line: "935", classification: "NEUTRAL-FACT", implication: "IPO debt-repayment tranche 100% deployed; finance-cost tailwind (-76.2% YoY) now exhausted, will not repeat."}
  - {id: "F6", check: "F6", line: "332", classification: "FORWARD-SIGNAL", implication: "Europe/Africa card exports commenced + 3 multi-year tenders won + retailer RFID stabilized = forward backlog."}
  - {id: "F8", check: "F8", line: "529", classification: "AMBIGUOUS", implication: "PAT +63.8% YoY flattered by ETR normalising 33.0%->26.3%; underlying PBT growth +48.8%."}
  - {id: "F14", check: "F14", line: "163", classification: "NEUTRAL-FACT", implication: "Operating EBITDA 873.1 vs 873.13 and precision/typo inconsistencies; reconcile exact figure vs filing."}
  - {id: "F16a", check: "F16", line: "299", classification: "AMBIGUOUS", implication: "Slide10 FY26=15,583 contradicts slide16 stack + Notion FY26 ₹1,441 Cr; possible reversed year labels hiding flat/declining revenue."}
  - {id: "F16b", check: "F16", line: "164", classification: "FORWARD-SIGNAL", implication: "Headline EBITDA margin +135bps is other-income driven (Other Income +203%); clean operating margin +22bps to 23.2%."}
  - {id: "F16c", check: "F16", line: "438", classification: "AMBIGUOUS", implication: "Slide15 gross-margin header shows +13.3% (rupee growth) while gross margin fell 286bps YoY."}
  - {id: "F16d", check: "F16", line: "550", classification: "FORWARD-SIGNAL", implication: "QoQ decline pre-framed as Q4-seasonality; implies structurally soft H1FY27."}
forward_signals: ["F6", "F16b", "F16d"]
ambiguous: ["F8", "F16a", "F16c"]
commitments:
  - {commitment: "Payment card exports to Europe & Africa", implied_date: "Q1FY27", ref: "slide12 line332", status_word: "commenced"}
  - {commitment: "1 multi-year tender won (Payments)", implied_date: "Q1FY27", ref: "slide12 line330", status_word: "won"}
  - {commitment: "2 multi-year tenders won (CFS, PSU banks)", implied_date: "Q1FY27", ref: "slide13 line367", status_word: "won"}
  - {commitment: "Largest Indian retailer RFID volumes", implied_date: "Q1FY27", ref: "slide14 line397", status_word: "stabilized"}
  - {commitment: "SIM card revenue contribution", implied_date: "undated", ref: "slide14 line404", status_word: "building"}
gate_a3: pass
blank_checks: []
```
