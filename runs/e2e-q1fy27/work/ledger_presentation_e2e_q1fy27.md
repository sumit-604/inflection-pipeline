# A2 ENUMERATOR LEDGER — E2E Networks Limited (E2E) — Q1 FY27 — doctype: presentation

Source: `extract_presentation_e2e_q1fy27.txt` (A1 extract of a 2-page investor
press release: page 1 = cover letter to NSE/BSE transmitting the release,
page 2 = "E2E Networks Reports Q1 FY'27 Results" release body). Doctype was
classified `presentation` by the orchestrator; the source is not a slide
deck. This ledger applies the INVESTOR PRESENTATION enumeration rules
(slides = pages, every number on every slide, footnotes/disclaimers,
dropped-slide check) and, because the document also carries filing-letter
and press-release structure, adds adjacent categories (administrative
identifiers, highlight bullets, narrative statements, entities) so no
disclosure unit is dropped. All line numbers reference the A1 extract file
as read (source content begins at line 27; lines 1-26 are the A1 extraction
header/metadata and are not enumerated as disclosure units).

Prior-quarter ledger: not provided / not found in `runs/` — DROPPED_SLIDE
check is N/A this run (flagged `NO_PRIOR_LEDGER`).

```
=== A2 COUNT TEST ===
category: slides                grep_count: 2   sweep_count: 2   match: yes
category: kpi_metrics            grep_count: 42  sweep_count: 42  match: yes
category: admin_identifiers      grep_count: 14  sweep_count: 14  match: yes
category: highlight_bullets      grep_count: 12  sweep_count: 12  match: yes
category: narrative_statements   grep_count: 12* sweep_count: 12  match: yes
category: about_boilerplate      grep_count: 2   sweep_count: 2   match: yes
category: footnotes_disclaimers  grep_count: 3   sweep_count: 3   match: yes
category: entities                grep_count: 2  sweep_count: 2   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

`*narrative_statements` reconciliation note: the raw automated pass
(`grep -oP '(?<!\d)\.(?!\d)'` over lines 52-56, 96-99, 116-118, i.e. letter
body + Financial Performance Overview paragraph + management-commentary
quote) returns only 7 sentence-terminating periods, because two genuine
sentence endings are immediately preceded by a digit ("...ended June 30,
2026." and "...through the rest of FY'27.") and are excluded by the
digit-adjacency guard that exists to keep decimal numbers (4.3x, 75.2%,
₹0.32) from being mis-split. A manual re-sweep confirms both are real
sentence boundaries (+2 = 9), and adds three non-period structural units
the period-regex cannot see at all: the headline (line 82-83), the
subheadline (line 84), and the quote attribution line "— Management, E2E
Networks Limited" (line 120), which carries no terminal period (+3 = 12).
Corrected count 12 = manual sweep 12. Reported as match: yes on the
corrected/reconciled basis; both raw sub-counts are shown in the table
below so the arithmetic is auditable.

---

## 1. SLIDES / PAGES (2)

| # | Line | Title / heading | Content type | Flags |
|---|------|------------------|---------------|-------|
| 1 | 27 | Cover letter to NSE & BSE, "Sub: Press Release" | text (regulatory transmittal letter) | — |
| 2 | 75 | "E2E Networks Reports Q1 FY'27 Results" (press release body) | text + native KPI summary boxes (confirmed not chart images per A1 header) | — |

DROPPED_SLIDE check: no prior-quarter presentation ledger available for
comparison. Flag `NO_PRIOR_LEDGER`.

## 2. KPI / FINANCIAL & OPERATIONAL METRICS ON SLIDES (42)

Every stated number tied to a financial/operational metric, including every
restatement of the same figure at a different slide location (headline,
KPI box, bullet, quote are each a separate disclosure occurrence).

| # | Line | Slide | Metric | Value | Flags |
|---|------|-------|--------|-------|-------|
| 1 | 82 | 2 | Revenue YoY growth (headline) | 334% | — |
| 2 | 82 | 2 | Q1 FY'27 Revenue (headline) | ₹1,568 Mn | — |
| 3 | 83 | 2 | EBITDA Margin (headline) | 75.2% | — |
| 4 | 83 | 2 | Q1 PBT (headline) | ₹586 Mn | — |
| 5 | 84 | 2 | Q1 EBITDA as % of FY'26 full-year EBITDA (subheadline) | 93% | — |
| 6 | 87 | 2 | Revenue (KPI box 1) | ₹1,568 Mn | restated |
| 7 | 87 | 2 | EBITDA Margin (KPI box 2) | 75.2% | restated |
| 8 | 87 | 2 | Q1 EBITDA (KPI box 3) | ₹1,179 Mn | — |
| 9 | 87 | 2 | Q1 PBT (KPI box 4) | ₹586 Mn | restated |
| 10 | 87 | 2 | Q1 PAT (KPI box 5) | ₹439 Mn | — |
| 11 | 87 | 2 | Diluted EPS (KPI box 6) | ₹2.10 | — |
| 12 | 90 | 2 | Q1 EBITDA vs FY'26 full-year EBITDA (KPI box 3 subtext) | 93% | restated |
| 13 | 91 | 2 | Revenue growth YoY (KPI box 1 subtext) | +334.1% | — |
| 14 | 91 | 2 | Revenue growth QoQ (KPI box 1 subtext) | +63.9% | — |
| 15 | 91 | 2 | EBITDA margin QoQ change (KPI box 2 subtext) | +1,450 bps | see #26 discrepancy |
| 16 | 91 | 2 | PBT prior-quarter comparator (KPI box 4 subtext) | vs ₹86 Mn (Q4 FY'26) | — |
| 17 | 91 | 2 | PAT margin (KPI box 5 subtext) | 28.0% | — |
| 18 | 91 | 2 | EPS prior-quarter comparator (KPI box 6 subtext) | vs ₹0.32 (Q4 FY'26) | — |
| 19 | 97 | 2 | Revenue (FPO paragraph) | ₹1,568 Mn | restated |
| 20 | 97 | 2 | Revenue growth YoY (FPO paragraph, rounded) | 334% | rounded vs #13 (334.1%) |
| 21 | 97 | 2 | Revenue growth QoQ (FPO paragraph, rounded) | 64% | rounded vs #14 (63.9%) |
| 22 | 99 | 2 | Stock split ratio | 10:1 | — |
| 23 | 102 | 2 | Revenue from Operations (KFH bullet 1) | ₹1,568 Mn (+334.1% YoY; +63.9% QoQ) | restated |
| 24 | 103 | 2 | EBITDA (KFH bullet 2) | ₹1,179 Mn | restated |
| 25 | 103 | 2 | EBITDA Margin (KFH bullet 2) | 75.2% | restated |
| 26 | 103 | 2 | EBITDA margin QoQ change (KFH bullet 2) | +1,446 bps | **NUMERIC_INCONSISTENCY** vs #15 (+1,450 bps, same metric stated twice in same document) |
| 27 | 103-104 | 2 | EBITDA margin YoY change (KFH bullet 2) | +4,609 bps | — |
| 28 | 104 | 2 | GPU infrastructure scale (OH bullet 2) | ~5,100 GPUs | — |
| 29 | 105 | 2 | PBT (KFH bullet 3) | ₹586 Mn | restated |
| 30 | 105 | 2 | PBT prior-quarter comparator (KFH bullet 3) | vs ₹86 Mn (Q4 FY'26) | restated |
| 31 | 106 | 2 | PAT (KFH bullet 4) | ₹439 Mn | restated |
| 32 | 106 | 2 | PAT Margin (KFH bullet 4) | 28.0% | restated |
| 33 | 106 | 2 | PAT margin prior-quarter comparator (KFH bullet 4) | vs 6.7% (Q4 FY'26) | — |
| 34 | 107 | 2 | Diluted EPS (KFH bullet 5) | ₹2.10 per share | restated |
| 35 | 107 | 2 | EPS prior-quarter comparator (KFH bullet 5) | vs ₹0.32 (Q4 FY'26) | restated |
| 36 | 109 | 2 | Depreciation (KFH bullet 6) | ₹606 Mn | — |
| 37 | 109 | 2 | Depreciation QoQ increase (KFH bullet 6) | up ₹93 Mn | — |
| 38 | 116 | 2 | Revenue growth YoY, alt. framing (mgmt quote) | 4.3x | consistent w/ #1 (334% ≈ 4.34x) |
| 39 | 116 | 2 | EBITDA margin (mgmt quote) | 75.2% | restated |
| 40 | 117 | 2 | PBT (mgmt quote) | ₹586 Mn | restated |
| 41 | 97 | 2 | Quarter-end date referenced with revenue figure | "ended June 30, 2026" | see admin_identifiers #14 also |
| 42 | 84 | 2 | Q1 EBITDA absolute figure implied consistent with box 3 | ₹1,179 Mn (cross-check: 93% x FY26 EBITDA) | not independently disclosed as FY26 EBITDA base figure — **NOT FOUND** (FY26 full-year EBITDA absolute value never stated, only the 93% ratio) |

Flag detail: row 26 vs row 15 is a genuine within-document inconsistency —
the EBITDA-margin QoQ expansion is stated as **+1,450 bps** in the KPI
summary-box subtext (line 91) and **+1,446 bps** in the Key Financial
Highlights bullet (line 103). Both describe the same metric (EBITDA margin
QoQ change) for the same quarter. Flag: `NUMERIC_INCONSISTENCY`. Feeds Role
5 arithmetic-consistency check.

Row 42 flag: the press release states Q1 EBITDA (₹1,179 Mn) is "93% of
FY'26 full-year EBITDA" (lines 84, 90) but never states the FY'26
full-year EBITDA absolute rupee figure anywhere in this 2-page document —
flag `NOT_FOUND` (base figure for the 93% ratio is not disclosed here).

## 3. ADMINISTRATIVE / IDENTIFIER NUMBERS (14)

Every number on the slide that is not a financial/operational KPI (CIN,
address, phone, pincodes, dates, scrip/script codes, signature timestamp,
ICSI number) — required by the "every number on every slide" rule.

| # | Line | Slide | Identifier | Value | Flags |
|---|------|-------|-----------|-------|-------|
| 1 | 29 | 1 | Corporate Identification Number (CIN) | L72900DL2009PLC341980 | — |
| 2 | 31 | 1 | Registered office PIN code | 110044 | — |
| 3 | 31 | 1 | Registered office phone | +91-11-4084-4964 | — |
| 4 | 35 | 1 | Letter date | July 21, 2026 | — |
| 5 | 40 | 1 | NSE address floor | 5th Floor | — |
| 6 | 41 | 1 | BSE address plot no. | Plot No. C/1 | — |
| 7 | 42 | 1 | NSE (Mumbai) PIN code | 400 051 | — |
| 8 | 42 | 1 | BSE (Mumbai) PIN code | 400 001 | — |
| 9 | 44 | 1 | BSE Scrip Code | 544783 | — |
| 10 | 68 | 1 | Digital signature date | 2026.07.21 | — |
| 11 | 69 | 1 | Digital signature time + UTC offset | 13:54:36 +05'30' | no board meeting referenced in this document to cross-check timestamp against (rule 7 N/A here — flag `NO_MEETING_REFERENCE`) |
| 12 | 73 | 1 | Signatory ICSI membership number | A59215 | — |
| 13 | 80 | 2 | Press-release dateline date | July 21, 2026 | restated (same calendar date as letter, #4) |
| 14 | 96-97 | 2 | Quarter-end date | June 30, 2026 | — |

Note: BSE ticker "Script Symbol: E2E" / "Scrip Code: 544783" appear as a
matched pair (line 44) — NSE side uses "Script Symbol" (non-standard
spelling of "Scrip Symbol"), BSE side uses "Scrip Code"; recorded as-is,
not normalized.

## 4. HIGHLIGHT BULLETS (12) — Key Financial Highlights (6) + Other Highlights (6)

| # | Line | Column | Bullet text (verbatim lead) | Flags |
|---|------|--------|------------------------------|-------|
| 1 | 102 | Key Financial Highlights | "₹1,568 Mn Revenue from Operations (+334.1% YoY; +63.9% QoQ)" | — |
| 2 | 103-104 | Key Financial Highlights | "EBITDA: ₹1,179 Mn \| Margin: 75.2% (+1,446 bps QoQ; +4,609 bps YoY)" | see NUMERIC_INCONSISTENCY above |
| 3 | 105 | Key Financial Highlights | "PBT: ₹586 Mn vs ₹86 Mn in Q4 FY'26" | — |
| 4 | 106 | Key Financial Highlights | "PAT: ₹439 Mn \| PAT Margin: 28.0% (vs 6.7% in Q4 FY'26)" | — |
| 5 | 107 | Key Financial Highlights | "Diluted EPS: ₹2.10 per share (vs ₹0.32 in Q4 FY'26)" | — |
| 6 | 109 | Key Financial Highlights | "Depreciation: ₹606 Mn, up ₹93 Mn QoQ on new GPU capex" | — |
| 7 | 102-104 | Other Highlights | "B200 cluster successfully deployed on the TIR platform, contributing to revenue within its first quarter" | — |
| 8 | 104 | Other Highlights | "GPU infrastructure scaled to approximately 5,100 GPUs" | — |
| 9 | 105-106 | Other Highlights | "Incorporated Sovcloud Technologies Limited, a wholly owned subsidiary" | `ENTITY_CHANGE` — new entity, first appearance, no prior-quarter list to check against |
| 10 | 107-108 | Other Highlights | "Operating large GPU clusters on the TIR platform, targeting industry benchmarks for NCCL and Model FLOPs Utilization (MFU)" | forward-looking / targets stated, not yet achieved — `FORWARD_LOOKING` |
| 11 | 110 | Other Highlights | "Investing in Organisational Capability through strengthening of teams" | no headcount / quantum disclosed — qualitative only |
| 12 | 111-112 | Other Highlights | "Cluster performance driven through meticulous, full stack optimisations across multiple layers" | qualitative only, no metric attached |

## 5. NARRATIVE STATEMENTS (12) — letter body, FPO paragraph, management quote

| # | Line | Slide | Statement (unit) | Flags |
|---|------|-------|-------------------|-------|
| 1 | 52-53 | 1 | Letter body sentence 1: transmittal of press release "E2E Networks Reports Q1 FY'27 Results" to Exchange | — |
| 2 | 53-54 | 1 | Letter body sentence 2: "for the information of the Exchange and the members" | — |
| 3 | 56 | 1 | Letter body sentence 3: "Kindly take this on record" | — |
| 4 | 82-83 | 2 | Headline (title, no terminal period): revenue/EBITDA margin/PBT summary | — |
| 5 | 84 | 2 | Subheadline (no terminal period): B200 live + Q1 EBITDA 93% of FY26 full year | — |
| 6 | 96-97 | 2 | FPO sentence 1: unaudited Q1 FY'27 results announced, quarter ended June 30, 2026 | ends "...2026." — flags unaudited status, cross-ref footnote #3 |
| 7 | 97-98 | 2 | FPO sentence 2: revenue driven by B200 go-live, GPU utilisation improvement, TIR platform scale-up | attributions/causal claims, not independently evidenced in this doc |
| 8 | 98-99 | 2 | FPO sentence 3: 10:1 stock split + direct BSE Mainboard listing as capital-markets milestone | — |
| 9 | 116-117 | 2 | Mgmt quote sentence 1: revenue grew 4.3x YoY, EBITDA margin to 75.2%, PBT ₹586 Mn | — |
| 10 | 117-118 | 2 | Mgmt quote sentence 2: GPU fleet utilisation "remains strong," "robust demand from AI ecosystem" | qualitative, unquantified |
| 11 | 118 | 2 | Mgmt quote sentence 3: "remain focused on aggressive and judicious capacity expansion through the rest of FY'27" | `FORWARD_LOOKING` — guidance-adjacent, no number attached |
| 12 | 120 | 2 | Quote attribution: "— Management, E2E Networks Limited" (no terminal period) | `UNATTRIBUTED_QUOTE` — no named executive (no CEO/CFO/MD name or designation given for the commentary) |

## 6. ABOUT / BOILERPLATE (2)

| # | Line | Slide | Statement | Flags |
|---|------|-------|-----------|-------|
| 1 | 122 | 2 | Company description: "India's leading AI-First Cloud GPU Platform, listed on the NSE and BSE" | — |
| 2 | 122-123 | 2 | Product/infra description: GPU series (B200, H200, H100, legacy) + Linux/Windows/Storage/Managed Cloud; data centres in Noida and Chennai | — |

## 7. FOOTNOTES / FINE-PRINT DISCLAIMERS (3)

Every footnote/disclaimer qualifying a headline number, per rule 4 of the
INVESTOR PRESENTATION enumeration.

| # | Line | Slide | Disclaimer | Qualifies | Flags |
|---|------|-------|-----------|-----------|-------|
| 1 | 124 | 2 | "This press release may contain forward-looking statements based on current expectations and assumptions." | all forward-looking language (rows 5, 10, 11 above) | — |
| 2 | 124 | 2 | "Actual results may differ materially." | same as #1 | — |
| 3 | 124-125 | 2 | "All financial figures for Q1 FY'27 are unaudited and subject to limited review by the Statutory Auditors." | **every headline KPI on the slide** — revenue, EBITDA, margin, PBT, PAT, EPS, depreciation are all unaudited/limited-review figures | material qualifier on all of section 2 (KPI metrics) — `UNAUDITED_FIGURES` |

## 8. ENTITIES MENTIONED (2)

| # | Line | Entity | Relationship | Flags |
|---|------|--------|---------------|-------|
| 1 | 28 (and throughout) | E2E Networks Limited | Reporting/filing entity (CIN L72900DL2009PLC341980) | — |
| 2 | 105-106 | Sovcloud Technologies Limited | Newly incorporated wholly owned subsidiary, first mention this quarter, no prior-period entity list to diff against | `ENTITY_CHANGE`, `NO_PRIOR_LEDGER` |

## 9. LETTER SIGNATORY / SIGNATURE BLOCK (page 1)

| # | Line | Element | Detail | Flags |
|---|------|---------|--------|-------|
| 1 | 64 | Company signoff | "For E2E Networks Limited" | — |
| 2 | 65-69 | Digital signature graphic | "Digitally signed by RONIT, Date: 2026.07.21 13:54:36 +05'30'" | timestamp same calendar date as letter date (line 35); no board meeting start/end time disclosed in this document to benchmark against — `NO_MEETING_REFERENCE` |
| 3 | 71-73 | Signatory identity | Ronit, Company Secretary & Compliance Officer, ICSI M. No. A59215 | single signatory; no additional director/officer signature on this letter |

## ZERO_STANDING CHECK

No table with explicit zero/nil/dash line items is present in this 2-page
press release (no annexed financial statement tables were extracted — only
narrative KPI callouts and highlight bullets, all of which carry non-zero
values in this quarter). No `ZERO_STANDING` rows apply to this document.
This is recorded explicitly (not silently dropped): the absence of a
tabular P&L/balance-sheet breakout in the source itself is worth noting for
A3/A4 — flag `NO_DETAILED_TABLE` (KPI figures are release-level summary
only; segment/table-level detail, if any, would be in a separate filing not
covered by this extract).

## SUMMARY FLAGS RAISED (unique)

NUMERIC_INCONSISTENCY, NOT_FOUND, ENTITY_CHANGE, FORWARD_LOOKING,
UNATTRIBUTED_QUOTE, UNAUDITED_FIGURES, NO_PRIOR_LEDGER, NO_MEETING_REFERENCE,
NO_DETAILED_TABLE
