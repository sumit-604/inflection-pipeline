# A2 Completeness Ledger — Paisalo Digital, Q1FY27, Results Press Release

Source: `runs/paisalo-q1fy27/work/extract_results_paisalo_q1fy27_pressrelease.txt`
Doctype note: this is a Regulation 30 press-release submission (cover letter +
6-page press release), NOT a full Regulation 33 results filing. It contains no
board outcome letter, no standalone/consolidated financial statements, no
auditor report, and no numbered notes-to-accounts. Categories in the standard
A2 "results filing" checklist that have no corresponding content in this
document (notes, agenda items, auditor paragraphs, entity list) are recorded
as N/A-DOCTYPE below and their absence is carried into the ABSENT-DISCLOSURES
section for downstream reconciliation, per task instruction.

```
=== A2 COUNT TEST ===
category: kpi_table_metrics       grep_count: 7    sweep_count: 7    match: yes
category: headline_kpi_boxes      grep_count: 4    sweep_count: 4    match: yes
category: ai_operating_metrics    grep_count: 4    sweep_count: 4    match: yes
category: key_highlight_bullets   grep_count: 16   sweep_count: 16   match: yes
category: performance_chart_nums  grep_count: 27   sweep_count: 27   match: yes
category: zero_standing_items     grep_count: 1    sweep_count: 1    match: yes
category: signature_block_fields  grep_count: 5    sweep_count: 5    match: yes
category: notes                   grep_count: 0    sweep_count: 0    match: yes  (N/A-DOCTYPE: no numbered notes section in a press release)
category: agenda_items            grep_count: 0    sweep_count: 0    match: yes  (N/A-DOCTYPE: no Board Outcome letter attached)
category: auditor_paras           grep_count: 0    sweep_count: 0    match: yes  (N/A-DOCTYPE: no auditor report attached)
category: entities                grep_count: 0    sweep_count: 0    match: yes  (N/A-DOCTYPE: no consolidation entity list attached)
category: absent_disclosure_kw    grep_count: 0    sweep_count: 0    match: yes  (confirms Standalone/Consolidated/Segment-reporting/Limited-Review/Notes-to-Accounts/Cost-to-Income/Fee-income keywords do not appear in doc)
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (run against the extract file):
- `grep -n -E "^(AUM|Disbursement|Total Income|PAT|Net Interest Margin|GNPA|NNPA) \("` → 7 KPI table rows (lines 120-126)
- `sed -n '88p' | grep -oE "Rs [0-9,]+ Mn"` → 4 headline box values (line 88); `sed -n '89p' | grep -oE "\+[0-9]+% YoY"` → 4 headline box YoY tags (line 89)
- `grep -c -E "^•"` → 16 bullets (lines 133-165)
- `sed -n '170,228p' | grep -oE "[0-9]+,[0-9]+|[0-9]+\.[0-9]+%"` → 24 comma/percent numbers, plus manual sweep of 3 bare 3-digit PAT values (722/613/472, lines 188-190) not caught by the comma/percent regex = 27 total, reconciled against manual sweep of all 9 chart series x 3 periods = 27
- `sed -n '119,126p' | grep -nE "[[:space:]]-[[:space:]]*$"` → 1 dash-valued cell (Total Income QoQ, line 122)
- `grep -n -E "Manendra Singh|MANENDRA SINGH|Company Secretary|Digitally signed by|Date: 2026\.08\.05"` → 5 signature block fields (lines 61,62,64,66,67)
- keyword sweep for absent-disclosure terms (Standalone, Consolidated, Segment, Limited Review, Notes to Accounts, Cost-to-Income, Fee/commission income) → 0 hits (one incidental match on generic word "segments" at line 135, unrelated to segment reporting, excluded)

---

## 1. Cover Letter / Regulation 30 Submission Details (page 1, lines 30-69)

| # | Item | Line | Value | Flags |
|---|------|------|-------|-------|
| 1.1 | Letter date | 30 | August 05, 2026 | |
| 1.2 | Addressee 1 | 32-36 | The Manager, Dept of Corporate Relationship, BSE Limited, 25th Floor P.J. Towers, Dalal Street, Mumbai-400 001 | |
| 1.3 | Addressee 2 | 33-36 | The Listing Department, National Stock Exchange of India Limited, Exchange Plaza, BKC, Bandra (East), Mumbai-400 051 | |
| 1.4 | Scrip code (BSE equity) | 38 | Equity-532900 | |
| 1.5 | Scrip symbol (NSE) | 38 | PAISALO | |
| 1.6 | NCD codes | 39-40 | 975107, 975202, 975251, 975329, 975437, 975640, 975865, 976752, 977004, 977097, 977278, 977279, 977358, 977371, 977643 (15 NCD codes) | |
| 1.7 | CP codes | 41 | 731429, 731434, 731455, 731624, 732088 (5 CP codes) | |
| 1.8 | Subject line | 46 | Submission under Regulation 30 of SEBI (LODR) Regulations, 2015 - Press Release | |
| 1.9 | Press release title (as quoted in cover letter) | 51-52 | "Paisalo Digital delivers AI-driven momentum with 128% YoY surge in disbursements; AUM up 28% YoY at Rs 67,074 Mn" | |
| 1.10 | Closing / valediction | 56-60 | Thanking you, Yours Faithfully, For Paisalo Digital Limited | |
| 1.11 | Enclosure line | 69 | Enclosure: Press Release | |

## 2. Headline KPI Boxes — top of press release (page 2, lines 82-90)

| # | Metric | Line(s) | Value | YoY | Flags |
|---|--------|---------|-------|-----|-------|
| 2.1 | AUM | 84,88,89 | Rs 67,074 Mn | +28% YoY | |
| 2.2 | Disbursement | 84,88,89 | Rs 17,309 Mn | +128% YoY | |
| 2.3 | Total Income | 84,88,89 | Rs 2,603 Mn | +19% YoY | |
| 2.4 | Profit After Tax | 84,88,89 | Rs 613 Mn | +30% YoY | |
| 2.5 | Orphan "GNPA (%)" label with no accompanying value in this box | 86 | (label only, no number in lines 84-90) | n/a | LAYOUT_ARTIFACT — bled through from an adjacent infographic text box; not a fifth headline metric, no value to report at this location |
| 2.6 | Sub-headline strap line | 76 | "Strengthened liability franchise drives 64 bps YoY reduction in borrowing costs" | | |

## 3. "AI Powered Scale – Q1FY27" Infographic Metrics (page 2, lines 92-113)

Extract carries an explicit [LAYOUT ARTIFACT] notice (line 93) that the four
infographic boxes below print with doubled/interleaved words from
overlapping text boxes in the source PDF; the underlying numeric values are
confirmed intact and unambiguous per the A1 extraction note.

| # | Metric box | Line(s) | Current value | Comparative | Flags |
|---|-----------|---------|---------------|-------------|-------|
| 3.1 | Customer Onboarding | 95,98,101,111 | 180k applications processed in Q1 | vs 160k in Q4FY26 | LAYOUT_ARTIFACT (doubled text in raw layout, value unambiguous) |
| 3.2 | Data Processing | 95,98,101,111 | 500k Voice Data Conversion handled | vs 350k in Q4FY26 | LAYOUT_ARTIFACT |
| 3.3 | Customer Engagement (AI Bots) | 95,98-100,106-113 | 18 Live AI Bots | vs 7 in Q4FY26 | LAYOUT_ARTIFACT |
| 3.4 | AI Calling (Promotional Calls) | 95,100-104,111-113 | 200k AI-driven outbound calls daily | vs 150K in Q4FY26 | LAYOUT_ARTIFACT |

## 4. Key Performance Indicators Table (page 2, lines 119-126)

| # | Metric | Line | Q1FY27 | Q1FY26 | YoY | Q4FY26 | QoQ | Flags |
|---|--------|------|--------|--------|-----|--------|-----|-------|
| 4.1 | AUM (Rs Mn) | 120 | 67,074 | 52,302 | +28% | 61,009 | +10% | |
| 4.2 | Disbursement (Rs Mn) | 121 | 17,309 | 7,581 | +128% | 13,440 | +29% | |
| 4.3 | Total Income (Rs Mn) | 122 | 2,603 | 2,187 | +19% | 2,609 | - | ZERO_STANDING (QoQ cell is a dash — no QoQ % computed/disclosed even though both period values are present and non-zero; the line item itself is standing, only the QoQ delta is dash-valued) |
| 4.4 | PAT (Rs Mn) | 123 | 613 | 472 | +30% | 722 | (15%) | |
| 4.5 | Net Interest Margin (%) | 124 | 6.6% | 6.5% | +4 Bps | 6.8% | (26 Bps) | |
| 4.6 | GNPA (%) | 125 | 0.70% | 0.84% | (14 Bps) | 0.76% | (6 Bps) | |
| 4.7 | NNPA (%) | 126 | 0.49% | 0.68% | (19 Bps) | 0.61% | (12 Bps) | |

## 5. Key Highlights Bullets (page 3, lines 129-165)

| # | Subsection | Line | Bullet (verbatim) | Flags |
|---|-----------|------|--------------------|-------|
| 5.1 | AUM and Disbursement | 133 | AUM grew 28% YoY to Rs 67,074 Mn, reflecting continued business momentum | |
| 5.2 | AUM and Disbursement | 134-135 | Disbursements stood at Rs 17,309 Mn in Q1FY27, surging 128% YoY on the back of steady credit demand across key segments | |
| 5.3 | Distribution | 139-140 | Strengthened last-mile presence with a network of 5,995 touchpoints, including 696 new touchpoints added during Q1 | |
| 5.4 | Distribution | 141 | Network of 424 branches to support wider reach and stronger on-ground presence | |
| 5.5 | Distribution | 142 | Customer franchise strengthened to ~18 mn, with ~1.8 Mn new additions during Q1FY27 | |
| 5.6 | Asset Quality | 146 | GNPA and NNPA improved by 14bps and 19bps YoY at 0.70% and 0.49% respectively | |
| 5.7 | Borrowings | 150 | Total borrowings stood at Rs 48,467 Mn as of June'26 | |
| 5.8 | Borrowings | 151 | Cost of borrowing improved by 64 bps YoY to 10.1%, with prudent liability management | |
| 5.9 | Profitability | 155 | Total income increased by 19% YoY to Rs 2,603 Mn | |
| 5.10 | Profitability | 156 | Net interest income increased by 16% YoY to Rs 1,447 Mn | |
| 5.11 | Profitability | 157 | NIM remained stable at 6.6% in Q1FY27 | |
| 5.12 | Profitability | 158 | AI-led efficiencies helped reduce headcount by 2% YoY to 3,018 | |
| 5.13 | Profitability | 159 | PAT stood at Rs 613 Mn, up by 30% YoY | |
| 5.14 | Profitability | 160 | Profitability remained healthy, with RoA at 3.6% and RoE at 13.4% | |
| 5.15 | Capital Adequacy | 164 | Capital Adequacy Ratio remained strong at 33.1%, with Tier 1 capital at 26.8% | |
| 5.16 | Capital Adequacy | 165 | Net Worth grew by 15% YoY to Rs 18,298 Mn | |

Section headers present with zero bullets under them: none — all six labelled
subsections (AUM & Disbursement, Distribution, Asset Quality, Borrowings,
Profitability, Capital Adequacy) carry at least one bullet.

## 6. Performance Summary Chart Numbers (page 4, lines 167-228)

Six chart-pair blocks, nine data series (Asset Quality chart carries two
series: GNPA and NNPA), three period data points each (Q1FY26 / Q4FY26 /
Q1FY27) = 27 individual chart numbers. RoA (%) and Cost of Borrowing (%) are
chart-only series with no corresponding row in the page-2 KPI table (noted in
the A1 header); the other seven series duplicate KPI-table values as bar/line
chart data labels.

| # | Series | Line | Q1FY26 | Q4FY26 | Q1FY27 | Flags |
|---|--------|------|--------|--------|--------|-------|
| 6.1 | AUM (Rs Mn) | 172-174 | 52,302 | 61,009 | 67,074 | duplicates KPI table 4.1 |
| 6.2 | Disbursement (Rs Mn) | 172,174,175 | 7,581 | 13,440 | 17,309 | duplicates KPI table 4.2 |
| 6.3 | PAT (Rs Mn) | 188-190 | 472 | 722 | 613 | duplicates KPI table 4.4 |
| 6.4 | NIM (%) | 187,190 | 6.5% | 6.8% | 6.6% | duplicates KPI table 4.5 |
| 6.5 | RoA (%) | 202 | 3.6% | 3.8% | 3.6% | chart-only series, no KPI-table row |
| 6.6 | GNPA (%) | 202-203 | 0.84% | 0.76% | 0.70% | duplicates KPI table 4.6 |
| 6.7 | NNPA (%) | 204-206 | 0.68% | 0.61% | 0.49% | duplicates KPI table 4.7 |
| 6.8 | Net Worth (Rs Mn) | 219,221 | 15,746 | 17,930 | 18,298 | chart-only series, no KPI-table row (Net Worth also cited in bullet 5.16 for Q1FY27 only) |
| 6.9 | Cost of Borrowing (%) | 219,221-222 | 10.7% | 10.2% | 10.1% | chart-only series, no KPI-table row; Q1FY27 value duplicates bullet 5.8's 10.1% |

Chart titles / axis labels (structural, not data): "Performance Summary" (168),
"Asset Under Management (Rs Mn)" (170/181), "Disbursement (Rs Mn)" (170/181),
"Profit After Tax (Rs Mn)" (185/197), "Net Interest Margin (%)" (185/197),
"Return on Assets (%)" (201/213), "Asset Quality (%)" (201/213), "Net Worth
(Rs Mn)" (217/228), "Cost of Borrowing (%)" (217/228) — 9 chart titles, one
per series, all present (no dropped chart title).

## 7. Management Quote and Concall Announcement (page 5, lines 231-265)

| # | Item | Line | Value | Flags |
|---|------|------|-------|-------|
| 7.1 | Quoted spokesperson | 231-232 | Mr. Santanu Agarwal, Deputy Managing Director | |
| 7.2 | Quote text | 234-250 | Full multi-paragraph quote on growth discipline, AI-led capabilities, funding diversification, capital position | |
| 7.3 | Concall event | 256-258 | Earnings Conference Call, Thursday, August 6, 2026 at 4:00 PM IST | |
| 7.4 | Concall context line | 259-262 | Following the Aug 5, 2026 results announcement, management will discuss performance and answer questions | |
| 7.5 | Registration link label | 264-265 | Conference Call Registration Link, "Paisalo Digital Q1FY27 Conference Call - LINK" | |

## 8. Digital Signature Block (page 1, lines 58-69)

| # | Field | Line | Value | Flags |
|---|-------|------|-------|-------|
| 8.1 | Entity attribution | 60 | For Paisalo Digital Limited | |
| 8.2 | Digital signature stamp text | 61-65 | "MANENDRA SINGH — Digitally signed by MANENDRA SINGH" | |
| 8.3 | Signature timestamp | 64-65 | Date: 2026.08.05 14:43:18 +05'30' | Same calendar date as the letter date (line 30, Aug 05, 2026) and the results-announcement date stated in the release body (line 80, "today ... quarter ended June 30, 2026"); no board-meeting conclusion time is disclosed anywhere in this document to check the timestamp against, so the standard "signature before board meeting concluded" check cannot be performed from this artifact alone — carried forward as a gap, not resolved as clean |
| 8.4 | Signatory name (printed) | 66 | (Manendra Singh) | |
| 8.5 | Signatory designation | 67 | Company Secretary | |

## 9. Boilerplate / Disclaimer / Contact Block (page 6, lines 267-299)

| # | Item | Line | Value | Flags |
|---|------|------|-------|-------|
| 9.1 | Company description | 270-277 | "About Paisalo Digital Ltd" boilerplate | |
| 9.2 | Touchpoint count (repeated) | 272 | 5,995 touch points across 22 states & UTs | duplicates bullet 5.3's 5,995 touchpoints figure; "22 states & UTs" is new information not stated in Section 5 |
| 9.3 | Disclaimer heading | 279 | Disclaimer | |
| 9.4 | Forward-looking-statement disclaimer text | 281-290 | Standard no-reliance / forward-looking-statement disclaimer | |
| 9.5 | Ticker footer | 292 | Paisalo Digital Limited (BSE:532900, NSE:PAISALO) | duplicates cover-letter scrip identifiers 1.4/1.5 |
| 9.6 | Website | 293-294 | https://paisalo.in/ | |
| 9.7 | Contact — email | 296-298 | ir@paisalo.in | |
| 9.8 | Contact — corporate office address | 296-299 | CSC, Pocket 52, CR Park, Near Police Station, New Delhi - 110019 | |

## 10. Categories checked and found N/A for this doctype (press release, not full results filing)

| Category | Finding |
|----------|---------|
| Numbered notes to accounts | Absent — no notes section anywhere in the 6-page document |
| Board Outcome letter / agenda items | Absent — this document is a Reg 30 press-release cover letter, not a Board Outcome letter; no AR approval, AGM notice, record date, dividend, director appointment, auditor change, scrutinizer, ESOP, or capital-raising resolution items are present to enumerate |
| Annexures / director profiles | Absent |
| Auditor report paragraphs (opinion, EOM, Other Matters, Going Concern, UDIN) | Absent — no auditor report attached to a press release |
| Consolidation entity list | Absent — no list of subsidiaries/associates/JVs, so no ENTITY_CHANGE check is possible against a prior-quarter list from this artifact |

---

## ABSENT-DISCLOSURES (Reg-33 items not present in this press release)

Recorded for downstream (A3/A4/A5) reconciliation against the full quarterly
filing set, since a press release is not itself the Reg-33 results filing:

1. **Standalone financial statements** — not present. Only summary KPIs (AUM,
   Disbursement, Total Income, PAT, NIM, GNPA, NNPA) and chart series (RoA,
   Net Worth, Cost of Borrowing) are disclosed; no P&L, balance sheet, or
   cash flow statement line items.
2. **Consolidated financial statements** — not present; document does not
   even state whether the KPIs shown are standalone or consolidated figures.
   This ambiguity itself should be flagged downstream (STANDALONE_VS_CONSOL
   basis undisclosed).
3. **Segment reporting** — not present; no segment-wise AUM, income, or
   profitability breakout (SME vs MSME vs micro-enterprise, or geography).
4. **Auditor limited-review report** — not present; no limited-review
   opinion, UDIN, or auditor name/firm anywhere in the document.
5. **Notes to accounts** — not present; no accounting-policy notes,
   contingent-liability notes, or related-party notes.
6. **Cost-to-Income ratio** — not present; document discloses RoA, RoE, NIM,
   Capital Adequacy, Tier 1, Cost of Borrowing, but no Cost-to-Income line
   anywhere.
7. **Fees & commission income line** — not present; Total Income and Net
   Interest Income are disclosed (bullets 5.9, 5.10) but no breakout of
   fee/commission income vs interest income vs other income.

All seven items were confirmed absent by keyword sweep (Standalone,
Consolidated, Segment, Limited Review, Notes to Accounts, Cost-to-Income,
Fee/commission income — 0 genuine hits; see grep commands above) and by
manual read of all 299 lines / 6 pages.

---

## Flags raised (roll-up)

- `LAYOUT_ARTIFACT` — items 2.5, 3.1, 3.2, 3.3, 3.4 (pdftotext column-overlap
  duplication in the page-2 infographic block, and one orphaned "GNPA (%)"
  label bleeding into the headline KPI box; underlying numeric values
  confirmed unambiguous by A1 per its extraction note)
- `ZERO_STANDING` — item 4.3 (Total Income QoQ cell is dash-valued)
- Unresolved gap (not a formal lexicon flag, carried as a note) — item 8.3,
  signature timestamp cannot be checked against a board-meeting conclusion
  time because no such time is disclosed in this document
