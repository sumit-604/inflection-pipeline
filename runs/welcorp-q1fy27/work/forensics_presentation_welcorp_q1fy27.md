# A3 FORENSIC NOTES — Welspun Corp Limited (WELCORP) — Q1FY27 (quarter ended 30 June 2026) — DOCTYPE: PRESENTATION

Source extract: `extract_presentation_welcorp_q1fy27.txt` (477 lines, 19 pages, 100% coverage, page 2 OCR-duplicated).
Ledger: `ledger_presentation_welcorp_q1fy27.md` (Tables 1-17, gate_a2 pass).
Ledger reconciliation: **100%** — every ledger row read verbatim at its cited line before judging.
Prior-quarter ledger: **none** (`NO_PRIOR_LEDGER`) — cross-deck DROPPED_SLIDE / ENTITY_CHANGE diffs run within-deck only, flagged where evidence is single-deck.

Doctype applicability (per prompt line 128-131): on a presentation, F16 applies plus any F6/F10/F11 numbers the deck carries; balance-sheet / auditor checks are N.A. F17 silence audit is run against the deck per the explicit task direction (deck-vs-Notion-checklist, in place of a transcript).

---

## FINDINGS TABLE

| id | check | ledger row ref | slide / line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F1 | T10 r9/r10/r12 (`ZERO_STANDING` x4) | Sl.10 / L272-278 | "Exceptional Items* 548 - - 0 -" ; "* One time gain on partial stake sale in ... EPIC ... KSA" | NEUTRAL-FACT | Headline PAT 1,046 (+199% YoY) and EPS 39.7 (+198%) are inflated by a one-off 548cr gain; the dormant Exceptional line (dash/dash/0/dash in all comparison cells) was activated solely by EPIC. Run-rate PAT = 499 (+42%). Strip 548 for any forward multiple. |
| FND-02 | F6 | T5 r3; T6 r-DI; T11 r4/r11; T14 | Sl.5 / L137 | "strategic expansions in the USA and KSA are on track for commissioning within FY27" | FORWARD-SIGNAL | Full commitment register below. FY27E revenue 20,000cr requires a ~30% H2 volume ramp that is explicitly contingent on USA+KSA commissioning; the whole guidance rests on these two dateable commitments. |
| FND-03 | F7 | T13B Sl.15 | Sl.15 / L377 | "Prevailing geopolitical uncertainties and tariffs are currently impacting the export sentiment, however, long-term potential remains intact" | FORWARD-SIGNAL | Pre-emptive hedge that reconciles with the observed Stainless Steel Bars & Pipes volume -24% YoY (8.3->6.3 KMT, T7 r3); management is signalling continued SS export weakness into the next quarter. |
| FND-04 | F7 | T13B Sl.14 India | Sl.14 / L362-364 | "Jal Jeevan Mission, Amrut 2.0: Funding constraints persist and could continue for a longer time frame" | FORWARD-SIGNAL | A caution listed under "Key Drivers," not a tailwind. Corroborates Notion "JJM receivables — DELAYED"; management is pre-warning that domestic DI demand/collection headwinds extend beyond this quarter. |
| FND-05 | F14 | T4 r5; Sl.12 title | Sl.12 / L307 ; Sl.4 / L126 | "GURADRAILS/ ORDER BOOK" (misspelling) ; agenda item "5. PROJECT UPDATE" | NEUTRAL-FACT | Individually immaterial drafting artifacts (title typo; agenda promises a "Project Update" section with no corresponding titled slide) — cumulatively a low-grade governance/QC data point; the missing Project Update slide is material in its own right, see FND-07. |
| FND-06 | F15 | T17 r2 (EPIC) | Sl.10 / L278 ; Sl.8 / L234 | "One time gain on partial stake sale in East Pipes Integrated Company for Industry (EPIC), KSA" | FORWARD-SIGNAL | Economic interest in associate EPIC was reduced this quarter. Ties to Notion #10 (EPIC contribution Rs50+cr/q deteriorating, stake ~22%): a smaller stake mechanically lowers future "Share of profit from Associates & JVs" (73cr this quarter, T10 r8). Deck discloses the sale gain but NOT the post-sale stake % — see FND-10. |
| FND-07 | F16 | T4 r5 (`POSSIBLE_DROPPED_CONTENT`); T5 r3 | Sl.4 / L126 ; Sl.5 / L137 | agenda "5. PROJECT UPDATE" (no slide) ; "on track for commissioning within FY27" | FORWARD-SIGNAL | Notion #1 expected KSA first production BY Q1FY27 (this quarter, AMBER). The deck neither confirms nor denies first production; it reframes to a full-year "within FY27" window and carries NO Project Update slide, NO capacity, NO % completion, NO date. DI is still "launching in KSA" (T6, L166, present tense = not launched). Softening / slippage signal on the primary catalyst. |
| FND-08 | F16 | T11 r4/r11/r12; T10 r4 | Sl.11 / L284,296 ; Sl.10 / L267 | "2,850 ... 756 (Q1)" ; Q1 EBITDA Margin "18.5%" | AMBIGUOUS | FY27E EBITDA guidance 2,850cr implies a full-year margin of 14.25% (2,850/20,000) vs Q1 actual 18.5%, and sits below the Q1 annualised run-rate of 3,024 (756x4). Implied 9M EBITDA 2,094 = ~13% margin. Either conservatism or a guided ~550bps H2 margin compression (KSA/US ramp mix). Convert to A4 question. |
| FND-09 | F16 | T12 r3/r4/r5 | Sl.12 / L320,329 | "24,750 CRORE" ; "* Based on execution upto 30th June and new orders upto 22nd July" | AMBIGUOUS | Order book given as an absolute figure with a cutoff date but NO executability window in months. Against FY27E revenue 20,000, cover is ~1.24x — below the ~1.4x Notion #2 carried, and the >=18-month visibility claim is asserted qualitatively ("medium- to long-term") not quantified. Deck omits the coverage-months metric that would test executability. Convert to A4 question. |
| FND-10 | F17 | T12; T14; T17; Notion #10/#11 | Sl.16-17 / L408-432 ; L278 | "SINTEX: CHANNEL EXPANSION UNDERWAY" (channel counts only, no Sintex P&L) | CONFIRMATORY-NEGATIVE | Silence audit table below. The deck highlights Sintex distributor/retailer/plumber counts (1.5x/2x/21x) while disclosing zero Sintex revenue/EBITDA (Sintex is Notion RED); is silent on ongoing EPIC quarterly contribution and post-sale stake; silent on RPT sales % (Notion #11 AMBER 33.44%); and silent on JJM receivables. Sustained silence on deteriorating metrics = confirmatory negative per Role 5. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING | **FINDING** | T10 Exceptional Items row: `ZERO_STANDING` x4 in comparison cells, activated by 548cr EPIC one-off inflating PAT/EPS (FND-01). |
| F2 STANDALONE vs CONSOLIDATED | **N.A.** | Deck carries consolidated figures only (PAT "after Minorities, Associates & JVs"); no standalone column exists to decompose. |
| F3 SHELL-ENTITY DETECTION | **N.A.** | No standalone-vs-consolidated cost lines in a presentation; Cost of Materials / Employee Benefits not disclosed. |
| F4 UNAUDITED CONTRIBUTION RATIO | **N.A.** | No auditor report / Other Matters paragraph in a presentation doctype. |
| F5 GOING CONCERN / EoM SCOPE | **N.A.** | No auditor EoM / going-concern paragraph in a deck, and `NO_PRIOR_LEDGER` for any diff. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | Lexicon hits: "on track for ... commissioning within FY27" (L137), "launching in KSA" (L166), "underway" (L408); commitment register below (FND-02). |
| F7 HEDGE PHRASE MINING | **FINDING** | New/pre-emptive hedges on SS export sentiment (L377) and JJM/Amrut funding constraints (L362) presage continued segment weakness (FND-03, FND-04). |
| F8 TAX FORENSICS | **N.A.** | P&L snapshot omits the current-tax line; ETR not computable (note: implied tax+minority ~161 on ~1,207 pre-tax reflects a near-untaxed KSA stake-sale gain — observation only, not a computable ETR). |
| F9 OCI FORENSICS | **N.A.** | No OCI / actuarial disclosure in a presentation. |
| F10 SHARE COUNT & DILUTION | **PASS** | Implied share count stable at ~26.3-26.4cr across all periods (1,046/39.7; 350/13.3; 370/14.0) — no corporate action; deck carries a single EPS series (no basic/diluted spread to widen). |
| F11 RESERVES / NET WORTH TIE-OUT | **N.A.** | Deck carries no Other Equity / Paid-up / net-worth figure (only Net Debt/(Cash) and ROCE); nothing to tie out. |
| F12 SEGMENT FORENSICS | **N.A.** | No segment assets/liabilities disclosed; deck carries segment volumes only (the SS -24% volume decline is captured under F7/F16, not here). |
| F13 BOARD OUTCOME BEYOND RESULTS | **N.A.** | This is a Reg. 30 investor-presentation submission, not a Board Outcome; no AR/AGM/record-date/director-appointment content (T2 cover-letter note confirms). |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | No notes/auditor to cross-check, but within-deck: "GURADRAILS" title typo (L307) + agenda item 5 with no matching slide (L126); immaterial individually, cumulative QC data point (FND-05). |
| F15 ENTITY LIST DIFFS | **FINDING** | No prior list, but the deck itself discloses a relationship change: EPIC partial stake sale = reduced economic interest in the associate (FND-06). |
| F16 DROPPED / REFRAMED DISCLOSURES | **FINDING** | Missing Project Update slide + KSA commissioning reframed to full-year (FND-07); EBITDA guidance below Q1 run-rate / margin (FND-08); order book with no executability window (FND-09). |
| F17 SILENCE AUDIT | **FINDING** | Deck-vs-Notion silence table: conspicuous omission of Sintex P&L, ongoing EPIC economics/post-sale stake, RPT %, JJM receivables (FND-10). |

Gate A3: **pass** — every check marked exactly one of PASS / FINDING / N.A.; no blanks.

---

## COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Slide / line ref | Status word | Note |
|---|---|---|---|---|---|
| C1 | USA + KSA strategic expansions commissioning | Within FY27 | Sl.5 / L137 | on track / underway | No capacity, no specific date; reframes Notion #1's "first production by Q1FY27" to a full-year window. |
| C2 | Ductile Iron Pipes launch in KSA | Not dated (present-progressive) | Sl.6 / L166 | launching / initiated | "launching in KSA" = not yet launched; DI-KSA still pre-commissioning. |
| C3 | FY27E Revenue guidance INR 20,000cr | FY27 full year | Sl.11 / L285,304 | guidance | vs Notion base case 19,550 (+2.3%, corroborates, slightly above). Requires ~30% H2 volume ramp over Q1 run-rate (4,081x4=16,324). |
| C4 | FY27E EBITDA guidance INR 2,850cr | FY27 full year | Sl.11 / L284 | guidance | Implies 14.25% full-year margin vs 18.5% Q1 actual; below Q1 annualised 3,024. See FND-08. |
| C5 | Sintex channel expansion | Ongoing | Sl.17 / L408 | underway | Channel counts up (distributors 1.5x, retailers 2x, plumbers 21x over 2yr); no Sintex financials disclosed. |
| C6 | ROCE sustained >20%; Net Debt/EBITDA <1x | Ongoing guardrails | Sl.12 / L317-324 | commitment | Q1 ROCE 23.1% (annualised), net cash position — currently satisfied. |
| C7 | Water Neutrality by 2040; Carbon Neutrality by 2040 | 2040 | Sl.18 / L457 | target | 14-year horizon; low near-term forensic weight. |

---

## WHAT WAS NOT DISCUSSED (F17 SILENCE AUDIT — deck vs Notion monitoring checklist)

| Monitoring item | Notion status | Addressed in deck? | Consecutive-quarter silence | Verdict |
|---|---|---|---|---|
| #1 KSA LSAW+DI commissioning / first production (expected Q1FY27) | AMBER | Partial — "within FY27" (L137), "launching in KSA" (L166); NO first-production confirmation, NO Project Update slide (L126) | 1 (baseline; `NO_PRIOR_LEDGER`) | Conspicuous omission of a specifics slide the agenda promised. FORWARD-SIGNAL (FND-07). |
| #2 US order-book visibility >=18 months (~1.4x cover) | GREEN | Partial — global order book 24,750cr (L320), qualitative "medium- to long-term"; NO months, NO US-specific figure | 1 (baseline) | Coverage-months metric omitted; implied ~1.24x on FY27E. AMBIGUOUS (FND-09). |
| #10 EPIC ongoing contribution Rs50+cr/q; stake ~22% | Deteriorating | Silent on ongoing contribution and post-sale stake %; only the 548cr sale gain shown (L278) | 1 (baseline) | Discloses the exit gain, hides the run-rate. CONFIRMATORY-NEGATIVE (FND-10). |
| #11 RPT sales % (FY26 33.44%) | AMBER | Silent — no related-party disclosure anywhere in deck | 1 (baseline) | Expected absence in a deck, but AMBER metric left untested. CONFIRMATORY-NEGATIVE. |
| Sintex subsidiary financials | RED | Silent on revenue/EBITDA; channel counts highlighted instead (Sl.16-17) | 1 (baseline) | Highlights channel growth, omits P&L for a RED subsidiary. CONFIRMATORY-NEGATIVE (FND-10). |
| JJM receivables | DELAYED | Silent on receivables; JJM cited as demand driver (L352) and funding caution (L362) | 1 (baseline) | Demand narrative present, collection/receivables silent. CONFIRMATORY-NEGATIVE (FND-04 linkage). |
| India DI commissioning | FIRED | Addressed — DI volumes 65->69 KMT (Sl.7), "Significant player in India" (L165) | n/a | Not silent. |
| FY28 base case revenue (22,975) | n/a | Silent — deck guides FY27 only | 1 (baseline) | FY28 outer-year visibility not offered. NEUTRAL. |

---

## CROSS-LINKED FORWARD NARRATIVE (for A4)

The FY27E revenue guidance of 20,000cr (C3) is not supportable on the Q1 run-rate (4,081 x 4 = 16,324); it requires a ~30% step-up in H2 that the deck explicitly ties to USA+KSA commissioning (C1). Yet the single most important catalyst — KSA first production, which Notion expected BY this quarter — is neither confirmed nor given a Project Update slide, and DI-KSA is still "launching" (FND-07). Simultaneously the FY27E EBITDA guidance implies a full-year margin (14.25%) well below the 18.5% just delivered (FND-08). Net read: management is holding a top-line number that depends on an unconfirmed, apparently slipping commissioning, while quietly guiding margin down. These are the two questions A4 should put to management. Headline PAT growth (+199%) is one-off-driven (FND-01); the associate engine behind part of the story (EPIC) was just partially sold (FND-06) with its ongoing economics undisclosed (FND-10).

---

```yaml
stage: A3-forensics
company: "WELCORP"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/welcorp-q1fy27/work/forensics_presentation_welcorp_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: PASS
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "FND-01", check: "F1", line: "L272-278", classification: "NEUTRAL-FACT", implication: "Headline PAT 1,046/+199% and EPS 39.7 inflated by 548cr one-off EPIC gain; run-rate PAT 499/+42%."}
  - {id: "FND-02", check: "F6", line: "L137", classification: "FORWARD-SIGNAL", implication: "FY27E 20,000cr revenue rests on USA+KSA commissioning 'within FY27'; dateable primary catalyst."}
  - {id: "FND-03", check: "F7", line: "L377", classification: "FORWARD-SIGNAL", implication: "New hedge on SS export sentiment matches SS volume -24% YoY; signals continued segment weakness."}
  - {id: "FND-04", check: "F7", line: "L362-364", classification: "FORWARD-SIGNAL", implication: "JJM/Amrut 'funding constraints persist' caution corroborates delayed JJM receivables; domestic DI headwind extends."}
  - {id: "FND-05", check: "F14", line: "L307,L126", classification: "NEUTRAL-FACT", implication: "'GURADRAILS' typo + agenda Project Update with no slide; low-grade QC/governance data point."}
  - {id: "FND-06", check: "F15", line: "L278", classification: "FORWARD-SIGNAL", implication: "EPIC partial stake sale reduces associate economic interest; lowers future Share-of-JV income; post-sale stake undisclosed."}
  - {id: "FND-07", check: "F16", line: "L126,L137", classification: "FORWARD-SIGNAL", implication: "KSA first production (expected Q1FY27) reframed to 'within FY27'; no Project Update slide, no capacity/date; slippage signal."}
  - {id: "FND-08", check: "F16", line: "L284,L296", classification: "AMBIGUOUS", implication: "FY27E EBITDA 2,850 implies 14.25% margin vs 18.5% Q1 and below run-rate 3,024; conservatism or ~550bps H2 compression."}
  - {id: "FND-09", check: "F16", line: "L320,L329", classification: "AMBIGUOUS", implication: "Order book 24,750cr given without executability months; ~1.24x FY27E cover, below Notion ~1.4x; window untested."}
  - {id: "FND-10", check: "F17", line: "L408-432,L278", classification: "CONFIRMATORY-NEGATIVE", implication: "Sintex P&L, ongoing EPIC economics/post-sale stake, RPT %, JJM receivables all silent while channel counts highlighted."}
forward_signals: ["FND-02", "FND-03", "FND-04", "FND-06", "FND-07"]
ambiguous: ["FND-08", "FND-09"]
commitments:
  - {commitment: "USA + KSA expansions commissioning", implied_date: "within FY27", ref: "Sl.5/L137", status_word: "underway"}
  - {commitment: "Ductile Iron Pipes launch in KSA", implied_date: "undated", ref: "Sl.6/L166", status_word: "launching"}
  - {commitment: "FY27E Revenue guidance INR 20,000 cr", implied_date: "FY27", ref: "Sl.11/L285", status_word: "guidance"}
  - {commitment: "FY27E EBITDA guidance INR 2,850 cr", implied_date: "FY27", ref: "Sl.11/L284", status_word: "guidance"}
  - {commitment: "Sintex channel expansion", implied_date: "ongoing", ref: "Sl.17/L408", status_word: "underway"}
  - {commitment: "ROCE >20% / Net Debt-EBITDA <1x guardrails", implied_date: "ongoing", ref: "Sl.12/L317-324", status_word: "commitment"}
  - {commitment: "Water & Carbon Neutrality", implied_date: "2040", ref: "Sl.18/L457", status_word: "target"}
gate_a3: pass
blank_checks: []
```
