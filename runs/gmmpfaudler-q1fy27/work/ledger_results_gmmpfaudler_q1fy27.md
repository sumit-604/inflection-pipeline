# A2 Completeness Ledger — GMM Pfaudler Limited (GMMPFAUDLR), Q1 FY27, doctype: results

Source: press_release_q1fy27.pdf (3-page earnings press release), extract at
`/home/user/inflection-pipeline/runs/gmmpfaudler-q1fy27/work/extract_results_gmmpfaudler_q1fy27.txt`.
Line numbers below refer to that extract file.

NOTE ON SCOPE: Extract lines 1-43 are A1 extraction-method metadata (header
block + the mechanical note explaining and excluding a pdftotext
contamination artifact — an orphaned ~28-slide Investor Presentation object
found only by the whole-document `-layout` pass, not part of this file's
actual 3 pages). That metadata is not filing content and is excluded from
enumeration below. The contaminated content itself never appears in the
per-page-authoritative extraction (lines 44-190) and is therefore not an
enumerable disclosure unit of this document.

This doctype (press release) does NOT contain: numbered accounting notes,
an auditor report, a Board Outcome agenda list, director/annexure profiles,
or a consolidation entity list. Each is recorded below as count 0 with a
"not present" note per task instruction, rather than omitted, so the ledger
proves completeness rather than leaving a silent gap.

---

## === A2 COUNT TEST ===
```
category: notes                          grep_count: 0   sweep_count: 0   match: yes
category: line_items (financial table)   grep_count: 8   sweep_count: 8   match: yes
category: zero_standing                  grep_count: 0   sweep_count: 0   match: yes
category: highlight_bullets              grep_count: 8   sweep_count: 8   match: yes
category: quote_paragraphs               grep_count: 3   sweep_count: 3   match: yes
category: agenda_items                   grep_count: 0   sweep_count: 0   match: yes
category: annexures_director_profiles    grep_count: 0   sweep_count: 0   match: yes
category: auditor_paras                  grep_count: 0   sweep_count: 0   match: yes
category: entities                       grep_count: 0   sweep_count: 0   match: yes
category: signature_blocks               grep_count: 1   sweep_count: 1   match: yes
category: concall_notice_items           grep_count: 6   sweep_count: 6   match: yes
category: covering_letter_elements       grep_count: 9   sweep_count: 9   match: yes
category: about_contacts_disclaimer      grep_count: 10* sweep_count: 11  match: yes**
category: page_header_id_blocks          grep_count: 2   sweep_count: 2   match: yes

* raw single-pattern grep -oE undercounts by 1: "Process Performance
  Technologies" wraps across the pdftotext -layout line break (line 163
  "...Process Performance" / line 164 "Technologies, Heavy Engineering..."),
  so a single-line regex cannot match it as one token. Manual sweep reads
  the wrapped text and recovers the 11th item (the "Process Performance
  Technologies" division name). Re-swept and reconciled -> 11 = 11.
** reconciled after accounting for the line-wrap above; see note.

gate_a2: pass
```
## === END COUNT TEST ===

Total enumerated rows (all tables below): 48.

---

## 1. Numbered notes / footnotes — NOT PRESENT (count 0)

| # | Line | Note text (first 15 words) | Flag |
|---|------|------------------------------|------|
| — | — | not present in press release (would appear in the Reg 33 tabular statement / notes to results) | — |

Grep: `grep -n -E "^\s*[0-9]+\.\s"` → 0 matches. Manual sweep of full 3 pages (lines 44-190) → 0 numbered notes, 0 asterisk/dagger/"Note:" footnotes found. Match.

---

## 2. Consolidated financial performance table — line items (8)

Table location: lines 88-97 ("Financial Performance" / "Consolidated", figures in ₹ crores except EPS, single column = Q1 FY27 only; no prior-year/prior-quarter comparative column in this summary table — YoY/QoQ deltas appear only as % text in the Highlights bullets, table 3 below).

| # | Line | Metric | Value | Flag |
|---|------|--------|-------|------|
| 1 | 97 | Revenue | ₹925 cr | |
| 2 | 97 | EBITDA | ₹94 cr | |
| 3 | 97 | EBITDA Margin | 10.1% | |
| 4 | 97 | PAT | ₹22 cr | |
| 5 | 97 | PAT Margin | 2.4% | |
| 6 | 97 | EPS | ₹5.32 | |
| 7 | 97 | Order Intake | ₹1,007 cr | |
| 8 | 97 | Backlog | ₹2,289 cr | |

Column header row cited for cross-reference: EBITDA/PAT/Order-Intake sub-labels at lines 93-96; "Revenue…EBITDA…PAT…EPS…Backlog" column order at line 94.

Grep: `grep -oE "₹[0-9,]+(\.[0-9]+)?|[0-9]+\.[0-9]+%|[0-9]+"` on line 97 → 8 tokens. Manual sweep of the 8 column headers (lines 93-96) → 8 metrics. Match.

---

## 3. Zero / nil / dash-valued standing line items — NOT PRESENT in this table (count 0)

| # | Line | Line item | Value shown | Flag |
|---|------|-----------|-------------|------|
| — | — | not present — every one of the 8 metrics in table 2 carries a populated non-zero value; this summary press-release table does not carry a tax line, exceptional-items line, minority-interest line, or other lower-frequency line that would more plausibly nil out. A full Reg 33 tabular statement would carry such lines and any zero/nil/dash value there must be enumerated with `ZERO_STANDING` | — |

Grep: `grep -nE "Nil|N/A|—|–|\b0\.00\b|\bnil\b"` on lines 90-97 → 0 matches. Manual sweep of the 8 values on line 97 → 0 zero/nil/dash values. Match. No `ZERO_STANDING` flag raised (nothing to flag).

---

## 4. Performance Highlights bullets (5)

| # | Line | Bullet (verbatim) | Flag |
|---|------|--------------------|------|
| 1 | 103 | Revenue up 16% YoY and down 2% QoQ | |
| 2 | 104 | EBITDA down 7% YoY and up 25% QoQ | |
| 3 | 105 | PAT up 118% YoY and 44% QoQ | |
| 4 | 106 | Order Intake of ₹ 1,007 Crores up 16% QoQ | |
| 5 | 107 | Backlog of ₹ 2,289 Crores up 20% YoY and 4% QoQ | |

## 5. Corporate Highlights bullets (3)

| # | Line | Bullet (verbatim, wrapped lines merged) | Flag |
|---|------|-------------------------------------------|------|
| 1 | 109-110 | Reorganization of our businesses into four distinct global divisions to drive growth, diversification and cost efficiencies. | |
| 2 | 111 | Repayment of approx. EUR 7 million of debt by the end of Q2 FY27, funded through internal accruals. | |
| 3 | 112-113 | Revision of the dividend payout frequency from semi-annual to annual, with no change in the Company's Dividend Distribution Policy. | |

Bullets 4+5 grep/sweep note: `grep -nE "^ [A-Z]"` returned 9 raw hits (lines 95, 103-107, 109, 111, 112); line 95 (" Q1" — the table's own row label, not a highlight bullet) is excluded as a false positive from the pattern, leaving 8, matching the manual sweep of 5 (table 4) + 3 (table 5) = 8. Match.

---

## 6. Management quote paragraphs (3)

| # | Line | Speaker / designation | Lead-in | First 15 words | Flag |
|---|------|------------------------|---------|------------------|------|
| 1 | 117-122 | Mr. Tarak Patel, Managing Director | "…said;" (117) | "Revenue for Q1 FY27 grew 16% year-on-year, reflecting the strength of our diversified business portfolio…" | |
| 2 | 123-127 | Mr. Tarak Patel, Managing Director (continuation) | "He further commented," (123) | "As part of our ongoing Global Transformation Programme, we have now reorganized our businesses…" | |
| 3 | 129-134 | Mr. Gregory Gelhaus, Group CEO | "…said;" (129) | "Q1 marks a positive start to the year and reflects the benefits of the strategic decisions…" | |

Numeric claims inside quotes (already reconciled to table/bullets, cited here for traceability): "grew 16% year-on-year" (118, = table 4 row 1); "increasing 20% YoY" (backlog, 121-122, = table 4 row 5). No new figures introduced in quotes 2 or 3.

Grep: `grep -nE "said;|further commented"` → 3 matches (117, 123, 129). Manual sweep of quote-mark spans (117-122, 123-127, 129-134) → 3 paragraphs. Match.

---

## 7. Board Outcome agenda items — NOT PRESENT (count 0)

| # | Line | Agenda item | Flag |
|---|------|-------------|------|
| — | — | not present in press release (would appear in the Reg 33 Board Outcome letter: AR approval, AGM notice, record date, dividend declaration, director appointments, auditor changes, scrutinizer, ESOP grants, capital-raising resolutions). Note: line 112-113 mentions a *policy-level* change to dividend payout *frequency* (semi-annual → annual) as a corporate highlight, but no board meeting agenda, start/end time, or formal resolution text is disclosed in this document. | — |

---

## 8. Annexures / director profiles — NOT PRESENT (count 0)

| # | Line | Annexure / profile | Flag |
|---|------|---------------------|------|
| — | — | not present in press release (would appear as annexures to the Reg 33 filing; this document has no director profile tables, DIN numbers, term dates, or background/relationship disclosures) | — |

---

## 9. Auditor report paragraphs — NOT PRESENT (count 0)

| # | Line | Paragraph type | Flag |
|---|------|-----------------|------|
| — | — | not present in press release (would appear in the Reg 33 auditor's Limited Review Report / Audit Report: opinion type, Emphasis of Matter, Other Matters, Going Concern, entity list reviewed, UDIN, unaudited/management-furnished entities). Note: results are self-labelled "Unaudited" throughout this press release (subject line 51, body text 86, 142, 148) — a limited-review conclusion, if any, is not disclosed here. | — |

---

## 10. Consolidation entity list — NOT PRESENT (count 0)

| # | Line | Entity | Relationship | Flag |
|---|------|--------|---------------|------|
| — | — | not present in press release (would appear in the Reg 33 statement / notes; this document reports only "Consolidated" headline figures at the group level, with no subsidiary/associate/JV entity list, so no `ENTITY_CHANGE` cross-check against a prior list is possible from this doctype) | — |

Prior-quarter ledger: none supplied for this run, so no diff was attempted in any case.

---

## 11. Digital signature block (1)

| # | Line | Signatory | Designation | Timestamp | Flag |
|---|------|-----------|-------------|-----------|------|
| 1 | 66-75 | Mittal Kartik Mehta | Company Secretary & Compliance Officer, FCS No. 7848 | 2026.08.05 18:02:37 +05'30' (line 70-71) | see note |

Note: rule 7 (signature-before-board-meeting-concluded check) is not evaluable from this document — no board meeting start/end time is disclosed anywhere in this press release (no Board Outcome letter present, table 7). Filing date on covering letter header: August 5, 2026 (line 45); results announced "Mumbai, August 05, 2026" (line 85). No same-day timing conflict is identifiable with the information available.

Grep: `grep -c "Digitally signed by"` → 1. Manual sweep → 1 signature block. Match.

---

## 12. Conference call & availability notice items (6)

| # | Line | Item | Flag |
|---|------|------|------|
| 1 | 142-143 | Statement: unaudited results available on IR section of company website (Ind AS) | |
| 2 | 147-149 | Conference call date/time: Thursday, August 06, 2026, 12:00 PM IST | |
| 3 | 150-151 | Dial-in number 1: +91 22 6280 1341 | |
| 4 | 151 | Dial-in number 2: +91 22 7115 8242 | |
| 5 | 151 | "or at weblink" — access-mode mention, no actual URL/link text given in this extract | |
| 6 | 152-153 | Statement: Q1 FY27 Earnings Presentation to be submitted to exchanges and hosted on company website | |

Grep: `grep -nE "Thursday, August 06, 2026|\+91 22 6280 1341|\+91 22 7115 8242|weblink|shall also be hosted|available in the Investor Relations"` → 6 line matches (147, 151 x2 patterns on one line counted as items 3+4+5, 152, 142) reconciled to 6 discrete items. Manual sweep → 6. Match.

---

## 13. Covering letter elements, page 1 (9)

| # | Line | Element | Flag |
|---|------|---------|------|
| 1 | 48-49 | Recipient: BSE Limited, Scrip Code 505255 | |
| 2 | 48-49 | Recipient: NSE Limited, Symbol GMMPFAUDLR | |
| 3 | 51-52 | Subject line: Press Release on Unaudited Standalone and Consolidated Financial Results for quarter ended June 30, 2026 | |
| 4 | 54 | Salutation: "Dear Sir/ Ma'am," | |
| 5 | 56-58 | Body / regulatory reference: Pursuant to SEBI (LODR) Regulations 2015, enclosing press release | |
| 6 | 60 | Closing instruction: "Kindly take the same on record." | |
| 7 | 62 | "Thanking you." | |
| 8 | 64 | "Yours faithfully," | |
| 9 | 77 | Enclosure line: "Encl.: As above" | |

Grep: `grep -nE "BSE Limited|NSE Limited|Sub\.:|Dear Sir|Pursuant to SEBI|Kindly take|Thanking you|Yours faithfully|Encl\."` on lines 44-190 (page 1 only relevant) → 9 matches (48, 48, 51, 54, 56, 60, 62, 64, 77); lines 21 and 37 also match "Sub.:" but are excluded — they sit inside the A1 extraction-method note (lines 15-42), not the actual letter. Manual sweep → 9. Match.

---

## 14. About / Contacts / Disclaimer block (11)

| # | Line | Item | Flag |
|---|------|------|------|
| 1 | 158-161 | About paragraph 1: heritage/capabilities description ("more than 140 years"; engineering capabilities, manufacturing footprint, process know-how) | |
| 2 | 162-165 | About paragraph 2: "20 manufacturing facilities across four continents"; "operates through four distinct global divisions" | |
| 3 | 166 | About paragraph 3: website reference | |
| 4 | 163 | Division name 1: Corrosion-Resistant Technologies | |
| 5 | 163-164 | Division name 2: Process Performance Technologies (name wraps across the line break) | |
| 6 | 164 | Division name 3: Heavy Engineering Technologies | |
| 7 | 164-165 | Division name 4: Process System Technologies | |
| 8 | 174, 176, 178, 180-182 | Contact — Company: Raveen Kanabar, Senior Manager Finance & Accounts, GMM Pfaudler Limited, Tel +91 22 6650 3900, Email investorrelations@gmmpfaudler.com | |
| 9 | 173, 175, 177, 179 | Contact — Investor: Ms. Neha Shroff, Strategic Growth Advisors, Tel +91 77380 73466, Email neha.shroff@sgapl.net | |
| 10 | 173-174, 176-177 | Contact — Media: Abhishek Savant, Veritas Reputation PR Private Ltd., Tel +91 8108848822, Email abhishek@veritasreputation.com | |
| 11 | 184-190 | Disclaimer paragraph: forward-looking statements caveat | |

Grep: `grep -oE "Corrosion-Resistant Technologies|Process Performance Technologies|Heavy Engineering Technologies|Process System Technologies|Raveen Kanabar|Neha Shroff|Abhishek Savant|Disclaimer:|GMM Pfaudler is a diversified|With 20 manufacturing facilities|More information is available"` → 10 raw matches; "Process Performance Technologies" (item 5) is missed by the single-line regex because pdftotext -layout wraps it across lines 163/164 ("...Process Performance" / "Technologies, Heavy Engineering..."). Re-swept manually reading the wrap → confirmed present → reconciled count 11 = 11 (see COUNT TEST note). Match after re-sweep.

---

## 15. Repeated page-header identifier block (2 occurrences)

| # | Line | Content | Flag |
|---|------|---------|------|
| 1 | 80 | "BSE: 505255 \| NSE: GMMPFAUDLR \| CIN: L29199GJ1962PLC001171 \| ISIN: INE541A01023 \| SECTOR: ENGINEERING - HEAVY" (page 2 header) | |
| 2 | 137 | identical identifier block (page 3 header) | |

Grep: `grep -nE "BSE: 505255"` → 2 matches (80, 137). Manual sweep → 2. Match.

---

## Flags summary

No `ZERO_STANDING`, `ENTITY_CHANGE`, `REPEAT_QUESTION`, `MGMT_ABSENCE`, or `DROPPED_SLIDE` conditions were found — each of those flag types requires a disclosure unit that is either zero/nil-valued, an entity-list change, a repeated analyst question, an absent promoter/CMD on a call, or a slide dropped versus a prior deck, none of which exist in this doctype/extract. This is a 3-page press release: no prior-quarter press-release ledger was supplied for a table-7/10/15 diff in any case.

One observational note (not a formal flag, since it maps to no defined lexicon code): the conference-call notice (table 12, row 5, line 151) says dial-in is available "or at weblink" but no actual URL is printed in this extract — a genuine incompleteness in the source document's text, or a hyperlink that did not survive `pdftotext -layout` extraction; flagged here for A3/A4 awareness only.
