# A2 COMPLETENESS LEDGER — Sammaan Capital Limited (SAMMAANCAP) — Q1FY27 — doctype: presentation

Source: `extract_presentation_sammaancap_q1fy27.txt` (155 numbered source lines, 4 pages).
Document is a 4-page company Press Release + covering letter (no slide deck, no financial
statement tables, no board outcome agenda, no auditor report, no concall transcript). Each
PDF page is treated as the coverage unit in place of a "slide." Line numbers below are the
A1 extract's own source-line numbers (1-155), matching the numbers printed in the left
column of the extract file.

No prior-quarter ledger was supplied and no prior SAMMAANCAP run folder exists in
`runs/`. This is the first quarterly-pipeline pass on this ticker, so `DROPPED_SLIDE` /
prior-period diffing is **not assessable** — noted explicitly rather than silently skipped.

---

=== A2 COUNT TEST ===
```
category: pages                 grep_count: 4    sweep_count: 4    match: yes
category: highlight_bullets     grep_count: 16   sweep_count: 16   match: yes
category: mgmt_numbers          grep_count: 22   sweep_count: 22   match: yes
category: forward_guidance      grep_count: 6    sweep_count: 6    match: yes
category: administrative_numbers grep_count: 16  sweep_count: 16   match: yes
category: narrative_units       grep_count: 8    sweep_count: 8    match: yes
category: zero_standing         grep_count: 0    sweep_count: 0    match: yes (n/a — no financial table present, see note below)
category: agenda_items          grep_count: 0    sweep_count: 0    match: yes (n/a — not a board outcome letter)
category: auditor_paras         grep_count: 0    sweep_count: 0    match: yes (n/a — no auditor report in this document)
category: entities               grep_count: 0    sweep_count: 0    match: yes (n/a — no consolidation entity list in this document)
gate_a2: pass
```
=== END COUNT TEST ===

**Reconciliation method.** For each numeric category, grep_count was produced with a
targeted regex pass over `extract_presentation_sammaancap_q1fy27.txt` (commands recorded
below each table); sweep_count was produced by an independent manual line-by-line read of
the extract. First-pass grep regexes under-matched `mgmt_numbers` (21 vs sweep's 22 — the
regex initially missed the `FY27-28` token on line 88) and were refined to add an
`FY[0-9]{2}-[0-9]{2}` pattern and a `0\.[0-9]+%` / `20\.1%` pattern (percent tokens were
being truncated by an overly greedy prior regex). After the re-sweep, both methods agree on
22. All other categories matched on the first pass.

---

## TABLE 1 — Pages (slide-equivalent units)

| # | Line | Page header text | Content type | Notes |
|---|------|-------------------|---------------|-------|
| 1 | 1 | `[page 1]` — covering letter to BSE/NSE | text | Transmittal letter, addressed to BSE & NSE, CC to India INX / NSE IX |
| 2 | 39 | `[page 2]` — Press Release, "Key Highlights" | text | 11 bullet highlights, headline framing "First Full Quarter Under IHC" |
| 3 | 87 | `[page 3]` — "Consolidated Financial Highlights", CEO quote, About, IR contact | text | 5 bullet financial highlights + CEO quote paragraph + boilerplate |
| 4 | 131 | `[page 4]` — Media Contacts, Safe Harbor | text | Media contact + full Safe Harbor disclaimer paragraph |

grep: `grep -n -E "\[page [0-9]+\]"` → 4 hits (lines 1, 39, 87, 131). sweep: 4 pages read
manually. Match: yes.

---

## TABLE 2 — Highlight bullets (every bulleted disclosure unit)

### Page 2 — "Key Highlights" (11 bullets)

| # | Line | First ~12 words | Numeric? | Flags |
|---|------|-------------------|----------|-------|
| 1 | 51 | "AUM grew to ₹ 56,239 Crore from ₹53,160 crore in Q4FY26" | yes | |
| 2 | 53-54 | "Disbursed ₹ 3,875 crore in Q1FY27 across five products, driving diversified growth without concentration" | yes | |
| 3 | 56 | "97% of the disbursements were secured, while 3% were unsecured" | yes | no per-product breakdown given — see TABLE 3 note |
| 4 | 58-59 | "Gross recoveries: ₹ 424 Crores; Net recoveries after taking into account provisions and other credit costs: ₹240 Crore" | yes | |
| 5 | 61-62 | "Maintained a growth-focused approach within prudent risk guardrails, while actively pursuing both organic and inorganic growth opportunities" | no | FORWARD_GUIDANCE (M&A optionality language) |
| 6 | 64-65 | "Credit ratings upgraded to AA+ (Stable) by CRISIL, CARE and ICRA; international rating upgraded to BB- (Stable) by S&P Global within 90 days" | yes | |
| 7 | 67-68 | "Steady reduction in stock borrowing cost — ~85 bps reduction from Q2FY26 to Q1FY27, with further ~75 bps reduction expected by end of FY27" | yes | FORWARD_GUIDANCE (forward ~75bps component) |
| 8 | 70-71 | "Strengthening leadership team with key senior hires across functions to support new product launches" | no | |
| 9 | 73 | "Identified 53 AI use cases for phased implementation across FY27-28" | yes | FORWARD_GUIDANCE |
| 10 | 75-78 | "AI-ready infrastructure initiated during the quarter — unified loan origination platform, unified HR life cycle platform..." | no | |
| 11 | 80 | "Strengthening cross functional integration with IHC across Risk, Finance and IT functions" | no | |

### Page 3 — "Consolidated Financial Highlights — Q1FY27" (5 bullets)

| # | Line | First ~12 words | Numeric? | Flags |
|---|------|-------------------|----------|-------|
| 12 | 93 | "Consolidated PAT stood at ₹243 Crore in Q1FY27" | yes | |
| 13 | 94 | "Disbursements at ₹ 3,875 Crore" | yes | REPEAT_METRIC (duplicate of bullet #2, line 53) |
| 14 | 95 | "Gearing ratio at 1.8x" | yes | |
| 15 | 96 | "Net NPA at 0.15%" | yes | |
| 16 | 97 | "Capital adequacy at 20.1%" | yes | |

grep: `grep -n "•"` → 16 bullet-marker lines (66,68,71,73,76,79,82,85,88,90,95,108,109,110,111,112
in the raw file-line numbering, corresponding to source lines 51,53,56,58,61,64,67,70,73,75,80,
93,94,95,96,97). sweep: 16 bullets read and transcribed manually (11 + 5). Match: yes.

---

## TABLE 3 — Management-stated numeric metrics (every number cited)

| # | Line | Metric | Value | Type | Flags |
|---|------|--------|-------|------|-------|
| 1 | 51 | AUM (current, as of Jun 30 2026) | ₹56,239 Crore | stock/balance | |
| 2 | 51 | AUM (prior quarter, Q4FY26) | ₹53,160 Crore | stock/balance, comparative | |
| 3 | 53 | Disbursements (Q1FY27) | ₹3,875 Crore | flow | REPEAT_METRIC (also line 94) |
| 4 | 53 | Number of products disbursed across | five (5) | count | no per-product ₹/% breakdown disclosed |
| 5 | 56 | Secured disbursement share | 97% | mix % | |
| 6 | 56 | Unsecured disbursement share | 3% | mix % | |
| 7 | 58 | Gross recoveries | ₹424 Crore | flow | |
| 8 | 59 | Net recoveries (post provisions/credit costs) | ₹240 Crore | flow | |
| 9 | 64 | Domestic credit rating | AA+ (Stable), CRISIL/CARE/ICRA | rating | |
| 10 | 65 | International rating | BB- (Stable), S&P Global | rating | |
| 11 | 65 | Rating-upgrade timeframe | within 90 days of IHC's investment | duration | |
| 12 | 67 | Stock borrowing cost reduction, actual (Q2FY26 to Q1FY27) | ~85 bps | delta, realized | |
| 13 | 68 | Stock borrowing cost reduction, forward guidance (by end FY27) | ~75 bps | delta, guidance | FORWARD_GUIDANCE |
| 14 | 73 | AI use cases identified | 53 | count | |
| 15 | 73 | AI use case rollout window | FY27-28 (phased) | timeline | FORWARD_GUIDANCE |
| 16 | 93 | Consolidated PAT (Q1FY27) | ₹243 Crore | P&L | |
| 17 | 94 | Disbursements (repeat statement) | ₹3,875 Crore | flow | REPEAT_METRIC (duplicate of #3) |
| 18 | 95 | Gearing ratio | 1.8x | ratio | |
| 19 | 96 | Net NPA | 0.15% | asset quality | |
| 20 | 97 | Capital adequacy | 20.1% | ratio | |
| 21 | 114 | Branch network | 200+ branches | count | boilerplate "About" section, not flagged as results metric |
| 22 | 114 | Channel partner network | 8,000+ channel partners | count | boilerplate "About" section, not flagged as results metric |

grep (refined pass): `grep -n -oE "₹[ ]?[0-9,]+|[0-9]+%|0\.[0-9]+%|20\.1%|[0-9]+ bps|~[0-9]+
bps|[0-9]\.[0-9]x|AA\+|BB-|[0-9,]+\+ (branches|channel partners)|[0-9]+ AI use cases|
FY[0-9]{2}-[0-9]{2}|[0-9]+ days|five products"` → 22 tokens across lines 66,68,71,73,74,79,
80,82,83,88,108,109,110,111,112,129 (file-line numbers; source lines 51,53,56,58,59,64,65,
67,68,73,93,94,95,96,97,114). sweep: 22 rows above. Match: yes (after regex refinement noted
above — first pass under-matched at 21 because it lacked an `FY[0-9]{2}-[0-9]{2}` pattern
for the line-73 rollout window and truncated the two-decimal percent values).

No PAT margin, NII, spread/NIM, cost-to-income, ROE/ROA, opex, AUM growth %, or product-wise
(mortgage/LAP/MSME/etc.) disbursement value is stated anywhere in this document — those are
absences, not omissions from this ledger; flagged for A3/A4 as **data not disclosed in this
doctype** (may be covered in the results/investor-deck doctype extracts for the same
quarter).

---

## TABLE 4 — Forward-looking / guidance / hedge phrases

| # | Line(s) | Phrase (paraphrase within ledger; verbatim in extract) | Type | Flag |
|---|---------|----------------------------------------------------------|------|------|
| 1 | 61-62 | "actively pursuing both organic and inorganic growth opportunities" | qualitative forward stance (M&A optionality) | FORWARD_GUIDANCE |
| 2 | 67-68 | "further ~75 bps reduction expected by end of FY27" | quantified guidance | FORWARD_GUIDANCE |
| 3 | 73 | "53 AI use cases for phased implementation across FY27-28" | quantified roadmap | FORWARD_GUIDANCE |
| 4 | 103-105 | CEO quote: "...well positioned to move decisively onto its next phase of growth... growth-oriented disbursals within clearly defined risk guardrails, ensuring that growth is both calibrated and sustainable" | qualitative forward framing | FORWARD_GUIDANCE |
| 5 | 108-110 | CEO quote: "As we look ahead, our priorities are clear — accelerate growth responsibly, strengthen earnings, progressively reduce our cost of funds, leverage the capabilities of our parent, deepen our technology-led distribution platform and maintain disciplined risk management" | 5-item forward priority list (unquantified) | FORWARD_GUIDANCE |
| 6 | 140-149 | Safe Harbor paragraph in full: forward-looking statements are assumption-based, not guaranteed, subject to risks/uncertainties, company undertakes no obligation to update | standard hedge/disclaimer | HEDGE_LANGUAGE |

grep: `grep -n -iE "expected|forward-looking|look ahead|does not undertake|guarantee|risks
and uncertainties|phased implementation|actively pursuing|priorities are clear|well
positioned|next phase"` → hits on lines 61,68,73,103,108,140,141,147,148, which group into
6 distinct logical statements (Safe Harbor paragraph, lines 140-149, is one unit despite
multiple keyword hits within it). sweep: 6 units read manually. Match: yes.

---

## TABLE 5 — Administrative / identifying numbers (non-business, for completeness)

| # | Line | Item | Value |
|---|------|------|-------|
| 1 | 2 | Letter date | August 13, 2026 |
| 2 | 4 | BSE scrip code | 535789 |
| 3 | 4 | BSE scrip code (2nd) | 890192 |
| 4 | 8 | Mumbai postal code (BSE) | 400 001 |
| 5 | 8 | Mumbai postal code (NSE) | 400 051 |
| 6 | 22 | Digital signature date | 2026.08.13 |
| 7 | 23 | Digital signature time | 17:38:37 +05'30' |
| 8 | 34 | CIN | L65922DL2005PLC136029 |
| 9 | 35 | Corp office postal code | 122 004 |
| 10 | 35 | Corp office phone | +91 1246048213 |
| 11 | 35 | Corp office fax | +91 1246048214 |
| 12 | 36 | Regd office postal code | 110 024 |
| 13 | 36 | Regd office phone | +91 1148147506 |
| 14 | 36 | Regd office fax | +91 1148147501 |
| 15 | 45 | Press-release dateline | August 13, 2026 |
| 16 | 46 | Quarter-end date restated in lead paragraph | June 30, 2026 |

grep: targeted regex for scrip codes / PIN codes / CIN / phone patterns / dates → 16 hits
after excluding 2 header/footer metadata false-positives (source-file header line and the
closing A1 YAML block, neither of which is document content). sweep: 16 rows above. Match:
yes.

---

## TABLE 6 — Narrative / structural units (non-bulleted prose blocks)

| # | Line(s) | Unit | Notes |
|---|---------|------|-------|
| 1 | 10-16 | Cover letter body (Sub / salutation / transmittal sentence / closing) | Purely administrative, no claims |
| 2 | 19-25 | Cover-letter signature block | Signatory: Amit Kumar Jain, Company Secretary; digitally signed 2026.08.13 17:38:37 +05'30'. Same-day as letter date (line 2) and press-release dateline (line 45) — no timing anomaly detectable from this document alone (this is not a board-outcome letter, so no board meeting start/end time is stated to check the signature against) |
| 3 | 43-44 | Headline | "Sammaan Capital Marks First Full Quarter Under IHC with AUM Gaining Momentum" |
| 4 | 45-46 | Dateline / lead paragraph | Mumbai, Aug 13 2026; reports results for quarter ended Jun 30 2026 |
| 5 | 49 | Standalone framing line | "First quarter as part of the IHC Group, marking a transformational phase for Sammaan Capital" — thematic anchor repeated at lines 65, 100-103, 112-113 |
| 6 | 100-110 | CEO (Gagan Banga, MD & CEO) quote paragraph | See TABLE 4 rows 4-5 for forward content within it |
| 7 | 112-118 | "About Sammaan Capital Limited" boilerplate | Contains branch/channel-partner counts (TABLE 3 rows 21-22); identifies IHC (Abu Dhabi) as parent |
| 8 | 138-149 | Safe Harbor disclaimer | See TABLE 4 row 6 |

grep: `grep -n -E "^[0-9]+\t[A-Z]"` style manual identification of paragraph-opening lines
cross-checked against page breaks → 8 distinct prose units. sweep: 8 units read manually.
Match: yes.

---

## TABLE 7 — Zero / nil / dash standing items (rule 2, RESULTS FILING enumerate list)

**Not applicable.** This document contains no financial statement table (no P&L, balance
sheet, or line-item schedule) — every disclosed number is a standalone narrative bullet
metric (TABLE 3). There is therefore no "line item present with a zero/nil/dash value in
one or more periods" to enumerate. This is stated explicitly per the operating rule
("never drop a nil row") rather than silently omitted: zero_standing count = 0, and that
zero is a documented finding, not an unchecked gap. If the results/investor-deck doctype
extracts for this same quarter contain financial tables, those must carry their own
zero-standing sweep independently — this ledger covers the presentation/press-release
doctype only.

## TABLE 8 — Board agenda items, auditor report paragraphs, consolidation entity list

**Not applicable to this document.** This is a covering letter transmitting a Press
Release (Reg. 30 type intimation), not a Board Outcome letter, audited financial result,
or auditor's report. No agenda items, no auditor opinion/EOM/Other Matters paragraphs, and
no consolidation entity list appear in this doctype. Noted explicitly so A3/A4 do not
mistake the absence for a missed enumeration — these categories should be checked against
the results-doctype extract for the same quarter (`extract_results_sammaancap_q1fy27.txt`
exists in the work folder per directory listing, but is out of scope for this
presentation-doctype ledger).

---

## FLAG SUMMARY

- `REPEAT_METRIC` — Disbursements ₹3,875 Crore stated twice, verbatim, at line 53 (Key
  Highlights) and line 94 (Consolidated Financial Highlights). Not a discrepancy (same
  number both times) but a structural repeat worth noting for A3.
- `FORWARD_GUIDANCE` — 6 instances (TABLE 4): quantified (~75bps by end FY27; 53 AI use
  cases across FY27-28) and qualitative (organic/inorganic growth pursuit; CEO forward
  priorities list).
- `HEDGE_LANGUAGE` — Safe Harbor paragraph (line 140-149), standard disclaimer.
- Incomplete breakdown (not a formal flag code, noted for A3/A4): "five products" driving
  disbursements (line 53) and 97%/3% secured/unsecured split (line 56) are given only in
  aggregate; no per-product ₹ Crore or % breakdown is disclosed in this document.
- No `ZERO_STANDING`, `ENTITY_CHANGE`, `MGMT_ABSENCE`, or `REPEAT_QUESTION` conditions
  apply — this doctype has no financial tables, no entity list, and no concall content.
- `DROPPED_SLIDE` / prior-period page comparison — not assessable; no prior SAMMAANCAP
  run exists in `runs/` and no prior ledger path was supplied.
