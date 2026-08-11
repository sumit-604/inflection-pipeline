# A2 ENUMERATION LEDGER — Exicom Tele-Systems Limited (EXICOM), Q1 FY27, Press Release
Source: extract_pressrelease_exicom_q1fy27.txt (4 pages, 146 body lines + 13-line header, line numbers below refer to the extract file's absolute line numbers)
Doctype branch applied: INVESTOR PRESENTATION (per task routing — headline-number + management-claim disclosure), cross-checked with RESULTS FILING rules #2 (table line items) and #7 (signature block) since this document embeds both a covering letter and a summary financial table.
Prior-quarter ledger: NONE supplied (first run for this doctype/ticker pairing). DROPPED_SLIDE check is therefore N/A this run — flagged `FIRST_RUN_NO_PRIOR_LEDGER`.

```
=== A2 COUNT TEST ===
category: pages                 grep_count: 4    sweep_count: 4    match: yes
category: quantified_claims     grep_count: 26   sweep_count: 26   match: yes
category: financial_line_items  grep_count: 4    sweep_count: 4    match: yes
category: zero_standing         grep_count: 0    sweep_count: 0    match: yes
category: named_entities        grep_count: 14   sweep_count: 14   match: yes
category: quotes                grep_count: 1    sweep_count: 1    match: yes
category: footnotes             grep_count: 3    sweep_count: 3    match: yes
category: signature_blocks      grep_count: 1    sweep_count: 1    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep methodology notes (for A3/A4 audit trail):
- pages: `grep -c "^\[page" extract...txt` = 4. Sweep: read each `[page N]` marker in situ, confirmed 4 distinct page units (lines 15, 56, 100, 151).
- quantified_claims: sum of token-level greps — percent tokens `~?[0-9]+\.?[0-9]*%` (18 raw hits, minus 1 header `page_coverage: 100%` metadata line, minus 6 financial-table `EBITDA %` row values counted separately under financial_line_items = 11 narrative tokens mapping to 9 distinct claims, one claim — gross margin 31.7% vs 39.4% — carrying 2 tokens, one — Consol EBITDA loss "narrowing to ~22cr from ~39cr" — carrying 2 rupee tokens); rupee-crore tokens (6, mapping to 5 distinct claims, one claim carrying 2 tokens); USD-million tokens (2); kW/kWh tokens (3, one embedded inside the BESS claim already counted via its rupee token); comma-grouped large numbers 80,000 / 200,000 (2); bare count nouns "180 DC chargers" / "508 charger sales" / "14 customers" (3, "14 customers" embedded inside the BESS claim already counted); spelled-out numbers "fifteen" / "ten new" (2). Cross-referenced against a full manual line-by-line sweep of pages 2-4 body text (page 1 covering letter carries no business-metric quantified claims, only identifiers) — both methods land on 26 distinct claims. See QC1-QC26 below.
- financial_line_items: `grep -n -E "^\s*(Revenue|EBITDA %|EBITDA|PAT)\s" ` on lines 135-146 = 4 (Revenue, EBITDA, EBITDA %, PAT), each carrying 6 period values (SA Q1FY27/Q4FY26/Q1FY26, Consol Q1FY27/Q4FY26/Q1FY26).
- named_entities: manual sweep of every named/specifically-referenced product, program, or counterparty (named or descriptively unnamed but distinctly referenced), 14 total, cross-checked against no separate automatable grep pattern (proper-noun sweep is inherently manual); listed individually below with line numbers for A3/A4 spot-check.
- quotes: `grep -n "said:"` = 1 (Anant Nahata). No second attributed quote block exists in this document.
- footnotes: manual sweep, 3 (forward-looking-statement disclaimer, ₹ Crore unit label on the summary table, media-contact footer line) — grep-verified via `grep -n -E "forward-looking|Media Contact|₹ Crore"` = 3 lines.
- signature_blocks: `grep -n "Digitally signed"` = 1 (Sangeeta Karnatak).

---

## 1. PAGES (page = disclosure unit, per INVESTOR PRESENTATION rule 1)

| # | Page | Line range | Content type | Summary | Flags |
|---|------|-----------|---------------|---------|-------|
| P1 | 1 | 15-55 | text (regulatory covering letter) | Reg. 30 cover letter to BSE/NSE enclosing the press release; states results "approved by the Audit Committee and the Board of Directors... at their respective meetings held today" (line 38-39); no board meeting start/end time given; digitally signed by Sangeeta Karnatak, Company Secretary & Compliance Officer | `BOARD_MEETING_TIME_NOT_FOUND` |
| P2 | 2 | 56-99 | text (press release body, headline + 2 highlight bullets + 3 narrative sections: overview, margin commentary, EV Charging) | Headline "Exicom Opens FY27 with Order Wins..."; SA/Consol headline numbers; gross margin YoY compression; EV Charging section incl. AC/DC/India-EV growth and 2 bullets (carmaker win, CPO/DC charger orders) continuing onto P3 | none |
| P3 | 3 | 100-150 | text (continuation of EV Charging bullets, Tritium section, Critical Power section, CEO quote, summary financial table) | Slim DC chargers + export bullets; Tritium USD revenue/orders/product milestones; Critical Power YoY growth, BESS, export mix; Anant Nahata quote; 4-line-item x 6-period financial table; start of "About Exicom" boilerplate | none |
| P4 | 4 | 151-161 | text (boilerplate + footer + disclaimer) | "About Exicom" continuation (incl. 200,000-charger cumulative claim); media contact line; forward-looking-statements disclaimer | none |

`DROPPED_SLIDE` check: N/A — no prior-quarter press-release ledger supplied. Flag `FIRST_RUN_NO_PRIOR_LEDGER`.

---

## 2. QUANTIFIED CLAIMS (every numeric/directional business-metric statement, narrative text only; formal table figures are in Section 3)

| # | Line(s) | Claim (verbatim gist) | Precision | Flags |
|---|---------|------------------------|-----------|-------|
| QC1 | 62 | Headline bullet: Standalone revenue up ~57% YoY | precise % | `HEADLINE_RESTATED_AT_QC4` |
| QC2 | 62 | Headline bullet: SA "EBITDA more than doubles" | qualitative multiplier, no exact figure in bullet | `QUALITATIVE_ONLY` |
| QC3 | 63 | Headline bullet: Consolidated EBITDA loss narrower YoY; margin under pressure | qualitative, no figure in bullet | `QUALITATIVE_ONLY` |
| QC4 | 69 | Standalone revenue rose ~57% YoY to ₹237 crore | precise | `XCHECK_CONCALL` (compare to concall-stated SA revenue growth %/₹) |
| QC5 | 69-70 | SA EBITDA "more than doubled" to ~₹21 crore | approximate (~) | `XCHECK_CONCALL` |
| QC6 | 70 | SA EBITDA margin Q1 FY27 = 8.8% | precise | matches Section 3 table exactly — cross-checked, consistent |
| QC7 | 70-71 | Consolidated revenue grew 61% to ₹331 crore | precise | `XCHECK_CONCALL` |
| QC8 | 71 | Consolidated EBITDA loss narrowing to ~₹22 crore from ~₹39 crore last year | approximate (~), two-period comparison in one claim | `XCHECK_CONCALL` — table (Sec.3) shows exact (21.9) vs (38.6); ~22/~39 are rounded restatements, note rounding direction |
| QC9 | 77 | Consolidated gross margin 31.7% against 39.4% a year ago | precise, two-period comparison | `XCHECK_CONCALL` (explicit task-flagged metric) |
| QC10 | 85 | India EV market crossed 80,000 electric four-wheeler sales this quarter (market-level, not company-specific) | precise count | `MARKET_LEVEL_NOT_COMPANY` |
| QC11 | 87-88 | AC charging: Exicom recorded YoY growth of 35% in Q1 FY27 | precise % | `XCHECK_CONCALL` — task explicitly flags possible concall variance ("AC may have grown by 30%") |
| QC12 | 89 | India EV business grew revenue 15% YoY | precise % | `XCHECK_CONCALL` |
| QC13 | 92 | Sole supplier of 7.4 kW AC units to "a leading carmaker" (unnamed) | precise spec, customer unnamed | `CUSTOMER_UNNAMED` |
| QC14 | 96 | "Working towards doubling its AC line capacity starting Q3" | qualitative multiplier + forward timing | `FORWARD_GUIDANCE`, `QUALITATIVE_ONLY` |
| QC15 | 97-99 | Brought on fifteen (15) new charge point operators; orders for over 180 DC chargers with Bus/Truck OEMs and Charging Network operators till October 2026 | precise counts + forward delivery window | `XCHECK_CONCALL` (order-book figure) |
| QC16 | 101 | Slim DC chargers: sub-100 kW DC charging spec | precise spec (upper bound) | none |
| QC17 | 104 | Orders from ten (10) new export countries | precise count | `XCHECK_CONCALL` |
| QC18 | 111 | Tritium revenue USD 10.3 million (current quarter) | precise | `XCHECK_CONCALL` (task explicitly names Tritium US$ figures) |
| QC19 | 111 | Tritium 508 charger sales (current quarter) | precise | `XCHECK_CONCALL` |
| QC20 | 112-113 | Tritium booked USD 20.8 million in orders, "roughly double the previous quarter" | precise $ figure + approximate QoQ multiplier | `XCHECK_CONCALL` (order-book figure) |
| QC21 | 117 | Tritium guided to EBITDA breakeven in Q4 FY27 | forward guidance, no $ figure, timeline only | `FORWARD_GUIDANCE`, `XCHECK_CONCALL` |
| QC22 | 121 | Critical Power revenue grew 80% YoY | precise % | `XCHECK_CONCALL` |
| QC23 | 122 | Bharat Net Phase 3: Exicom holds "over 60%" wallet share | precise floor % | `XCHECK_CONCALL` |
| QC24 | 123-124 | BESS: solutions up to 300 kWh (home + C&I); added 14 customers; close to ₹20 crore bookings in Q1 | 3 sub-figures in one claim (spec, count, approx ₹) | `XCHECK_CONCALL` |
| QC25 | 125 | Africa + Middle East export markets contributing 8% of revenues | precise % (scope of "revenues" — segment or total — not specified) | `SCOPE_AMBIGUOUS` |
| QC26 | 154 | "Over 200,000 chargers sold worldwide" (cumulative, About Exicom boilerplate) | precise floor, cumulative/lifetime not quarterly | `BOILERPLATE_CUMULATIVE_NOT_QUARTERLY` |

---

## 3. FINANCIAL TABLE LINE ITEMS (page 3, lines 135-146; ₹ Crore, Standalone + Consolidated x 3 periods each)

| # | Line item | Line | Q1 FY27 SA | Q4 FY26 SA | Q1 FY26 SA | Q1 FY27 Consol | Q4 FY26 Consol | Q1 FY26 Consol | Flags |
|---|-----------|------|-----------|-----------|-----------|----------------|----------------|----------------|-------|
| LI1 | Revenue | 139 | 236.8 | 282.1 | 150.7 | 331.0 | 387.9 | 205.3 | matches prior_context.md prior-quarter reference figures (Q4 FY26 SA 282.07≈282.1; Consol 387.95≈387.9) — consistent |
| LI2 | EBITDA | 141 | 20.9 | 29.9 | 8.8 | (21.9) | 0.27 | (38.6) | Consol Q4 FY26 +0.27 matches prior_context.md "+0.3" (rounding); this quarter's Consol EBITDA (21.9) confirms prior_context.md's pre-committed BEAR outcome (~-Rs22 Cr) |
| LI3 | EBITDA % | 143 | 8.8% | 10.6% | 5.8% | (6.6%) | 0.1% | (18.8%) | derived/consistent with LI1÷LI2 to rounding |
| LI4 | PAT | 145 | 4.9 | 11.9 | (7.7) | (73.5) | (54.3) | (83.1) | Consol PAT loss (73.5) this quarter vs (54.3) prior quarter — loss widened sequentially despite EBITDA-loss narrowing YoY; no note in this document explains the below-EBITDA delta (D&A, finance cost, exceptional items, tax) — `PAT_EBITDA_GAP_UNEXPLAINED`, flag for A3/A4 |

`ZERO_STANDING` check: none of the 4 line items carry a zero, nil, or dash value in any of the 6 periods shown. zero_standing count = 0.

---

## 4. NAMED ENTITIES / PRODUCTS / PROGRAMS / COUNTERPARTIES

| # | Line | Entity | Type | Named or descriptive-unnamed | Flags |
|---|------|--------|------|-------------------------------|-------|
| NE1 | 93 | Spin Air | Product (flagship AC charging portfolio) | Named | none |
| NE2 | 93 | SpinWise | Product (AI chatbot, new launch) | Named | `NEW_LAUNCH_THIS_QUARTER` |
| NE3 | 94 | Spin Control app (new generation, public-charger discoverability + real-time tracking) | Product | Named | `NEW_LAUNCH_THIS_QUARTER` |
| NE4 | 92 | "a leading carmaker" (sole 7.4 kW AC supply win) | Customer | Unnamed | `CUSTOMER_UNNAMED` |
| NE5 | 101 | Slim DC chargers (incl. Ring Topology inter-charger power sharing) | Product | Named | `NEW_LAUNCH_THIS_QUARTER` |
| NE6 | 103 | Ring Topology | Technology feature | Named | none |
| NE7 | 99 | "a leading e-trucking company" (renewed long-term partnership) | Customer | Unnamed | `CUSTOMER_UNNAMED` |
| NE8 | 114 | TRI-FLEX (Tritium high-power charging system, under lab validation) | Product | Named | `FORWARD_GUIDANCE` (in validation, not yet revenue) |
| NE9 | 114 | "the largest open public charging network in the US" | Customer/counterparty (Tritium TRI-FLEX validation partner) | Unnamed | `CUSTOMER_UNNAMED` |
| NE10 | 115 | GRID-FLEX (Tritium power-side system, first unit live June 2026) | Product | Named | none |
| NE11 | 115 | "a hyperscale customer" (GRID-FLEX first live site) | Customer | Unnamed | `CUSTOMER_UNNAMED` |
| NE12 | 123 | BESS (Battery Energy Storage Systems) portfolio | Product line | Named (acronym) | none |
| NE13 | 122 | Bharat Net Phase 3 | Government/telecom program | Named | none |
| NE14 | 121 | "leading telcos" (5G site expansion driver) | Customer segment | Unnamed (generic) | `CUSTOMER_UNNAMED` |

---

## 5. MANAGEMENT QUOTES

| # | Line(s) | Speaker | Designation | Gist | Flags |
|---|---------|---------|-------------|------|-------|
| MQ1 | 127-132 | Anant Nahata | Managing Director and CEO, Exicom | "Against the same quarter last year this is a stronger business... cost pressure took more out of margins than what we anticipated... confident about the year ahead..." — acknowledges margin miss vs internal expectation, no hard numeric guidance in the quote itself | `MGMT_ACKNOWLEDGES_MARGIN_MISS` (verbatim: "cost pressure took more out of margins than what we anticipated") |

No second management quote present in this document. Task brief names both Anant Nahata and Shiraz Khanna as expected quote sources; Shiraz Khanna does not appear anywhere in this press release (name absent from full-text sweep). Flag `SHIRAZ_KHANNA_QUOTE_NOT_PRESENT` — likely appears only in the concall transcript (separate doctype), not a defect of this document, but noted for A3/A4 cross-source completeness check.

---

## 6. FOOTNOTES / DISCLAIMERS / UNIT LABELS

| # | Line(s) | Item | Qualifies which headline number(s) | Flags |
|---|---------|------|--------------------------------------|-------|
| FN1 | 135 | "₹ Crore" unit label heading the summary table | All 4 table line items (Section 3) | none |
| FN2 | 157 | Media Contact / Investor Relations footer (khushboo.chawla@exicom.in / investors@exicom.in) | administrative, does not qualify a number | `ADMINISTRATIVE_NOT_A_DISCLAIMER` |
| FN3 | 159-160 | Forward-looking-statements disclaimer ("actual results may differ materially...") | Qualifies all forward-looking / guidance language in the release, incl. QC14, QC15 (Oct-2026 delivery window), QC20 (order intake), QC21 (Tritium Q4 FY27 breakeven guidance) | none |

---

## 7. SIGNATURE BLOCK

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---------|-----------|-------------|-----------|-------|
| SB1 | 46-53 | Sangeeta Karnatak | Company Secretary & Compliance Officer | 2026.08.10 14:37:12 +05'30' | Board/Audit Committee approval stated as "today, i.e., August 10, 2026" (line 38-39) with no meeting start/end time disclosed anywhere in the document, so the signature-vs-meeting-conclusion timing check cannot be performed. Flag `BOARD_MEETING_TIME_NOT_FOUND` (cannot confirm signature postdates meeting conclusion). |

---

## FLAGS SUMMARY (all flags raised across this ledger)

- `FIRST_RUN_NO_PRIOR_LEDGER` — no prior-quarter press-release ledger to diff for DROPPED_SLIDE.
- `BOARD_MEETING_TIME_NOT_FOUND` — no start/end time for the board meeting; signature timestamp cannot be checked against meeting conclusion.
- `HEADLINE_RESTATED_AT_QC4` — QC1 bullet duplicates QC4 body claim (same underlying metric, two line locations).
- `QUALITATIVE_ONLY` — QC2, QC3, QC14 carry directional/multiplier language without a precise figure in that specific line.
- `XCHECK_CONCALL` — QC4, QC5, QC7, QC8, QC9, QC11, QC12, QC15, QC17, QC18, QC19, QC20, QC21, QC22, QC23, QC24: every headline/segment metric that plausibly recurs in the concall transcript and must be reconciled by A3/A4 for cross-source variance (explicit task example: AC charging +35% YoY here vs a reportedly lower concall figure).
- `MARKET_LEVEL_NOT_COMPANY` — QC10 (80,000 four-wheeler sales) is an India-market statistic, not an Exicom company metric; do not conflate with company revenue/order figures downstream.
- `CUSTOMER_UNNAMED` — QC13, NE4, NE7, NE9, NE11, NE14: every counterparty referenced only by generic descriptor ("a leading carmaker," "a leading e-trucking company," "the largest open public charging network in the US," "a hyperscale customer," "leading telcos"). Five distinct unnamed-counterparty instances for A3/A4 to note as a disclosure-specificity pattern.
- `FORWARD_GUIDANCE` — QC14, QC15 (Oct-2026 window), QC21, NE8: statements about future timing/capacity/breakeven not yet realized.
- `SCOPE_AMBIGUOUS` — QC25: "8% of revenues" does not specify whether this is 8% of Critical Power segment revenue or total consolidated revenue.
- `BOILERPLATE_CUMULATIVE_NOT_QUARTERLY` — QC26: 200,000 chargers is a lifetime/cumulative figure embedded in company-description boilerplate, not a Q1 FY27 operating metric; must not be read as quarterly.
- `PAT_EBITDA_GAP_UNEXPLAINED` — LI4: Consolidated PAT loss widened sequentially (Rs73.5 Cr vs Rs54.3 Cr) even as consolidated EBITDA loss narrowed both YoY and roughly flat QoQ-comparable; press release gives no note explaining the below-EBITDA delta (D&A, finance costs, exceptional items, tax, minority interest).
- `NEW_LAUNCH_THIS_QUARTER` — NE2, NE3, NE5: SpinWise, new-gen Spin Control app, Slim DC chargers all introduced/launched this quarter per the release's own language.
- `MGMT_ACKNOWLEDGES_MARGIN_MISS` — MQ1: CEO quote explicitly states cost pressure exceeded internal expectations.
- `SHIRAZ_KHANNA_QUOTE_NOT_PRESENT` — task brief names Shiraz Khanna as an expected quote source; absent from this document entirely (likely concall-only).
- `ADMINISTRATIVE_NOT_A_DISCLAIMER` — FN2 is a contact footer, included for completeness, not a number-qualifying footnote.

## PRIOR-CONTEXT CROSS-NOTES (memory only, not anchored evidence — for A3/A4 framing, per prior_context.md)
- LI2 Consol EBITDA (21.9) confirms the pre-committed Q1 FY27 BEAR decision-metric outcome from prior_context.md (bull >=0, bear < -Rs20 Cr; actual ~-Rs22 Cr) — Trigger T1 (2nd consecutive consol EBITDA breakeven quarter) did NOT confirm, reversing from the Q4 FY26 +Rs0.27 Cr print.
- QC12 (India EV +15% YoY) vs prior_context.md T3 note "was FIRING +60% YoY" as of the Q4 FY26/Delhi-policy review — this is a sharp deceleration if both figures use the same India-EV-business base; flag for A3/A4 to verify definitional consistency (same segment scope) before treating as a trend break.
- QC15 order-book language (15 new CPOs, 180+ DC chargers) should be reconciled against prior_context.md T4 (Critical Power FY27 order book Rs1,016 Cr at Q4 FY26) and any consolidated order-book figure given in the concall — this press release does not state a single consolidated order-book Rs figure, only segment-level narrative counts.
- No note in this document addresses prior_context.md's 11 carried monitoring questions (net-debt ceiling, Note 5 foreign holder, Tritium backlog reconciliation, hyperscaler FAT date, WC funding durability, SA margin sustainability, Corporate Promoter loan status, Delhi EV policy order impact, Tritium India Delhi DCFC positioning, Hyderabad manufacturing capacity, EVSE India FY27 guidance revision) — expected, since a 4-page press release is not the venue for concall-level Q&A; flag `SILENCE_EXPECTED_WRONG_DOCTYPE` only if A3's concall ledger also shows these unaddressed.
