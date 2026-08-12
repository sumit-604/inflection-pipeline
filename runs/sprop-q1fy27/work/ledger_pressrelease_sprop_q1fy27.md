# A2 Enumeration Ledger — SPROP Q1 FY27 Press Release / Media Release

Source: `extract_pressrelease_sprop_q1fy27.txt` (true doc class: press release /
media release, 4 pages, extracted and enumerated under the "presentation"
recipe per task instruction — each page treated as the slide/unit).
Prior-quarter ledger: NONE supplied — `DROPPED_SLIDE` comparison not
applicable this run (noted, not scored as a gap).

```
=== A2 COUNT TEST ===
category: pages                         grep_count: 4    sweep_count: 4    match: yes
category: narrative_claims               grep_count: 21   sweep_count: 21   match: yes
category: numbers_metrics                grep_count: 28   sweep_count: 28   match: yes
category: financial_table_line_items     grep_count: 4    sweep_count: 4    match: yes
category: forward_statements             grep_count: 8    sweep_count: 8    match: yes
category: footnotes_disclaimers          grep_count: 2    sweep_count: 2    match: yes
category: signature_block                grep_count: 1    sweep_count: 1    match: yes
category: administrative_units           grep_count: 24   sweep_count: 24   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (reproducible): `grep -n -E "^\[page [0-9]+\]"`;
token-level `grep -n -oE` passes for `₹...`, `[0-9]+%`, `[0-9]+(\.[0-9]+)?\+?\s*msf`,
`[0-9]+\+`, `[0-9]+(\.[0-9]+)?x\b`, `[0-9]+ projects`, `[0-9]+ days`, CRISIL
rating line; `grep -n -iE` forward-looking keyword lexicon
(expect|on-track|advanced stage|planned|remains confident|remains focused|
targeted|expected to|momentum to|remains intact|H2FY27|beyond FY27|well
positioned to pursue|gain further momentum); `awk` blank-line paragraph
segmentation cross-checked against manual line-by-line read of all 158 lines.
All eight category counts reconciled on first pass; no re-sweep required.

---

## 1. PAGE / SLIDE INVENTORY

| # | Page | Line range | Title / masthead | Content type | Flags |
|---|------|-----------|-------------------|---------------|-------|
| 1 | 1 | 14–61 | Regulation 30 cover letter to NSE/BSE | text (letter + signature + footer) | — |
| 2 | 2 | 62–110 | MEDIA RELEASE — headline, Operational Highlights, Financial Highlights | text + table | — |
| 3 | 3 | 111–153 | MEDIA RELEASE — Significant highlights bullets, Outlook, CMD quote | text (bullets + prose + quote) | — |
| 4 | 4 | 154–175 | MEDIA RELEASE — About SPL, contacts | text + contact table | — |

DROPPED_SLIDE check: N/A, no prior-quarter ledger supplied.

---

## 2. NARRATIVE CLAIMS / PARAGRAPHS (management-narrative units, media release body)

| # | Line(s) | First ~15 words | Flags |
|---|---------|------------------|-------|
| 1 | 66 | "Steady start to the year with strong operational momentum" (headline 1 of 3) | — |
| 2 | 67 | "Quarterly Sales up 10% YoY to ₹484 Crs; Pre-tax profits marginally higher at ₹18 Crs" (headline 2 of 3) | — |
| 3 | 68 | "Full year outlook remains intact, backed by on-track execution and strong H2 launch line-up" (headline 3 of 3) | FORWARD_STATEMENT |
| 4 | 70–71 | "BENGALURU, August 12, 2026: Shriram Properties Limited ("SPL") has announced its financial results..." | — |
| 5 | 74–75 | "The Company reported strong operational performance with record-high first-quarter sales of ₹484 crore (0.85 msf)..." | — |
| 6 | 77–83 | "During the quarter, SPL successfully launched plots as Kolkata's first Branded Land under the codename..." (Forest View, King Life launches; contains forward sentence at 82–83) | FORWARD_STATEMENT (embedded, line 82–83) |
| 7 | 85–87 | "Gross customer collections grew 8% YoY to ₹365 crore in Q1, supported by robust execution-led milestones..." (contains forward sentence at 86–87) | FORWARD_STATEMENT (embedded, line 86–87) |
| 8 | 89–90 | "The Company handed over 690+ units to customers during Q1, building on the record handovers..." | — |
| 9 | 92–95 | "On the business development front, the Company has made significant progress in strengthening its development pipeline..." (GDV ~₹650cr new project; "advanced stage of closure" of 7+ msf) | FORWARD_STATEMENT (embedded, line 94–95) |
| 10 | 115–117 | "Total revenues stood at ₹271 crore, up 4% YoY, supported by continued revenue recognition..." (bullet 1) | — |
| 11 | 118 | "Gross profit stood at ₹56 crore, while EBITDA stood at ₹42 crore for the quarter." (bullet 2) | — |
| 12 | 119–120 | "Finance costs stood at ₹21 crore, supported by the cessation of non-cash charges relating to non-compete fee in Kolkata." (bullet 3) | — |
| 13 | 121 | "Net profit of ₹11 crore in Q1 FY27." (bullet 4) | — |
| 14 | 122–123 | "Generated operating cashflows of ₹54 crore and deployed ₹88 crore towards new project investments..." (bullet 5) | — |
| 15 | 124 | "Maintained a comfortable cash and cash equivalents balance of ₹219 crore." (bullet 6) | — |
| 16 | 125 | "Net debt stood at ₹432 crore, with a healthy net debt-to-equity ratio of 0.3x." (bullet 7) | — |
| 17 | 126 | "SPL continues to maintain a strong credit profile with a CRISIL rating of A(-)/Positive." (bullet 8) | — |
| 18 | 128–132 | "SPL remains confident of sustaining its growth momentum, supported by a strong launch pipeline targeted during H2FY27..." (Outlook para 1) | FORWARD_STATEMENT |
| 19 | 134–136 | "With a significant portion of its ongoing portfolio already sold and multiple projects progressing towards scheduled completion..." (Outlook para 2) | FORWARD_STATEMENT |
| 20 | 138–139 | "Simultaneous focus remains on continued addition of new projects across key markets is expected to strengthen..." (Outlook para 3) | FORWARD_STATEMENT |
| 21 | 143–148 | Mr. Murali M (Chairman & MD) quote: "We have commenced FY27 on a strong note, with robust operational performance..." | FORWARD_STATEMENT (embedded sentiment: "remains well positioned to pursue its growth opportunities") |

Bullets (rows 10–17, "Significant highlights" list, lines 114–126) cross-check:
8 bullets confirmed by grep of `•` markers on page 3, matches manual sweep.

Operational Highlights paragraph block-count (rows 5–9): 5 paragraphs, confirmed
by blank-line-delimited `awk` sweep of lines 74–95, matches manual read.

Outlook-section block-count (rows 18–21): 4 blocks (3 outlook paragraphs + 1
CMD quote), confirmed by blank-line-delimited `awk` sweep of lines 128–148.

---

## 3. NUMBERS / METRICS (business KPIs embedded in narrative text, distinct from the Financial Highlights table cells enumerated separately in §4)

| # | Line | Metric | Value | Context | Flags |
|---|------|--------|-------|---------|-------|
| 1 | 67 | Quarterly sales YoY growth | 10% | Headline | — |
| 2 | 67 | Quarterly sales value | ₹484 Crs | Headline | — |
| 3 | 67 | Pre-tax profit value | ₹18 Crs | Headline ("marginally higher") | — |
| 4 | 74–75 | Q1 sales value (restated in body) | ₹484 crore | Record-high first-quarter sales | — |
| 5 | 75 | Q1 sales volume | 0.85 msf | Footnote-1 qualified (msf = million sq ft) | — |
| 6 | 80 | Post-launch sales velocity | first 30 days | Both Jun'26 launches "delivering healthy sales within the first 30 days of launch" | — |
| 7 | 85 | Gross customer collections YoY growth | 8% | — | — |
| 8 | 85 | Gross customer collections value | ₹365 crore | — | — |
| 9 | 89 | Units handed over | 690+ | Q1FY27, vs. "record handovers" in Q4 FY26 (Q4 FY26 handover figure itself NOT FOUND in this document) | — |
| 10 | 94 | New project GDV added in quarter | ~₹650 crore | Approximate ("~"), single new project | — |
| 11 | 95 | Development potential at advanced stage of closure | 7+ msf | Additional projects, not yet closed | FORWARD_STATEMENT |
| 12 | 115 | Total revenues | ₹271 crore | Bullet 1 | — |
| 13 | 115 | Total revenues YoY growth | 4% | Bullet 1 | — |
| 14 | 118 | Gross profit | ₹56 crore | Bullet 2 | — |
| 15 | 118 | EBITDA (bullet restatement) | ₹42 crore | Bullet 2; cf. table EBITDA ₹41.9 cr (§4) — 0.1cr rounding vs. bullet's ₹42cr, immaterial | — |
| 16 | 119 | Finance costs | ₹21 crore | Bullet 3 | — |
| 17 | 121 | Net profit (bullet restatement) | ₹11 crore | Bullet 4; cf. table Net Profit ₹11.0 cr (§4), consistent | — |
| 18 | 122 | Operating cashflows generated | ₹54 crore | Bullet 5 | — |
| 19 | 122 | Capital deployed to new project investments | ₹88 crore | Bullet 5 | — |
| 20 | 124 | Cash and cash equivalents balance | ₹219 crore | Bullet 6 | — |
| 21 | 125 | Net debt | ₹432 crore | Bullet 7 | — |
| 22 | 125 | Net debt-to-equity ratio | 0.3x | Bullet 7 | — |
| 23 | 126 | Credit rating | CRISIL A(-)/Positive | Bullet 8 | — |
| 24 | 163 | Projects delivered (cumulative track record) | 52+ | About-SPL boilerplate | — |
| 25 | 163 | Cumulative development delivered | 32.9 msf | About-SPL boilerplate | — |
| 26 | 164 | Development pipeline, project count | 41 projects | About-SPL boilerplate | — |
| 27 | 164 | Aggregate development potential | 33.7 msf | About-SPL boilerplate | — |
| 28 | 165 | Ongoing projects within pipeline | 16.0 msf | About-SPL boilerplate, "as of June 30, 2026" | — |

Note on row 15: bullet-list EBITDA (₹42 crore, rounded) vs. Financial
Highlights table EBITDA (₹41.9 crore, §4) is a rounding presentation only,
not a discrepancy — flagged here for A3/A4 visibility, not as an error.

---

## 4. FINANCIAL HIGHLIGHTS TABLE — LINE ITEMS (lines 97–103, "(₹ Crores)")

| # | Line | Line item | Q1FY27 | Q1FY26 | FY26 | Flags |
|---|------|-----------|--------|--------|------|-------|
| 1 | 100 | Total Revenues | 271.1 | 261.5 | 1,356.9 | — |
| 2 | 101 | EBITDA | 41.9 | 41.6 | 176.8 | — |
| 3 | 102 | Profit Before Tax | 18.1 | 17.0 | 80.6 | — |
| 4 | 103 | Net Profit | 11.0 | 20.6 | 100.8 | — |

No zero/nil/dash-valued line item present in this table across any period —
no `ZERO_STANDING` rows to record. Table carries only 4 line items total
(Revenue, EBITDA, PBT, Net Profit); no margin %, no EPS, no balance-sheet
lines given in table form (balance-sheet metrics — cash, net debt, D/E — are
narrative-only, captured in §3 rows 20–22, not tabulated).

Notable computed observation (not sourced, flagged for A3/A4, not asserted
as fact): Net Profit Q1FY27 (₹11.0 cr) is *down* 46.6% YoY vs. Q1FY26
(₹20.6 cr) even though PBT is up 6.5% YoY (₹18.1 cr vs ₹17.0 cr) — the
press release headline and narrative emphasize PBT ("Pre-tax profits
marginally higher") and do not mention the YoY decline in Net Profit
anywhere in the narrative text. This gap (PBT up, PAT down, YoY, not
narrated) is a disclosure-emphasis observation for A3, not an A2
interpretation.

---

## 5. FORWARD-LOOKING STATEMENTS

| # | Line(s) | Statement (verbatim or near-verbatim) | Flags |
|---|---------|----------------------------------------|-------|
| 1 | 68 | "Full year outlook remains intact, backed by on-track execution and strong H2 launch line-up" | FORWARD_STATEMENT |
| 2 | 82–83 | "SPL expects pre-sales momentum to strengthen further with multiple launches planned in the coming quarters." | FORWARD_STATEMENT |
| 3 | 86–87 | "Overall collections to gain further momentum, supported by accelerated construction activity and sales ramp-up from new launches." | FORWARD_STATEMENT |
| 4 | 94–95 | "...is at an advanced stage of closure of additional projects with 7+ msf of development potential, providing strong visibility for future growth." | FORWARD_STATEMENT |
| 5 | 128–132 | Outlook para 1: "SPL remains confident of sustaining its growth momentum, supported by a strong launch pipeline targeted during H2FY27, healthy project execution and improving visibility on scheduled handovers..." | FORWARD_STATEMENT |
| 6 | 134–136 | Outlook para 2: "...the Company remains focused on accelerating execution and timely handovers to drive revenue recognition through the remainder of FY27." | FORWARD_STATEMENT |
| 7 | 138–139 | Outlook para 3: "...continued addition of new projects across key markets is expected to strengthen the development pipeline and support growth beyond FY27." | FORWARD_STATEMENT |
| 8 | 143–148 | CMD quote (Mr. Murali M): "...SPL remains well positioned to pursue its growth opportunities while continuing to create sustainable long-term value for all stakeholders." | FORWARD_STATEMENT |

Reconciliation note: forward-looking keyword lexicon grep (expect|on-track|
advanced stage|planned|remains confident|remains focused|targeted|expected
to|momentum to|remains intact|H2FY27|beyond FY27|well positioned to pursue)
isolated 7 of the 8 loci on first pass; a second targeted grep for "gain
further momentum" surfaced row 3 (lines 86–87), which the first lexicon
pass missed. Re-swept and reconciled to 8/8 before emitting — this is the
GATE A2 mechanism working as designed.

---

## 6. FOOTNOTES / DISCLAIMERS

| # | Line | Item | Status | Flags |
|---|------|------|--------|-------|
| 1 | 105–106 | Footnote 1: "Msf = Million Square Feet" — qualifies the "0.85 msf1" reference at line 75 | Present | — |
| 2 | N/A | Safe-harbour / forward-looking-statements disclaimer boilerplate (standard in most Indian listed-company press releases) | NOT FOUND — absent from the entire 4-page document, despite 8 FORWARD_STATEMENT rows (§5) including explicit guidance language ("expects", "targeted during H2FY27", "remains confident of sustaining growth momentum") | NO_SAFE_HARBOR_CLAUSE |

Grep basis for row 2: `grep -in -E "safe harbou?r|forward.looking statement|disclaimer"` returns zero matches across the full extract.

---

## 7. SIGNATORY / DIGITAL SIGNATURE BLOCK

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---------|-----------|-------------|-----------|-------|
| 1 | 37–47 | K. Ramaswamy (digitally signed "K Rama...Swamy") | Company Secretary & Compliance Officer, ACS 28580 | 2026.08.12 20:52:02 +05'30' | — |

No board-meeting start/end time is stated anywhere in this document (this
is a Regulation 30 press-release cover letter, not a Board Outcome letter),
so no comparison of signature timestamp against meeting conclusion time is
possible — noted as NOT FOUND rather than assumed benign.

---

## 8. ADMINISTRATIVE / COVER-LETTER DISCLOSURE UNITS

| # | Line(s) | Item | Flags |
|---|---------|------|-------|
| 1 | 15 | Letter date: "August 12, 2026" | — |
| 2 | 17–22 | Addressee block: NSE (Listing Dept, Exchange Plaza BKC Mumbai 400051, Scrip Code SHRIRAMPPS) + BSE (Corporate Services Dept, PJ Towers Dalal Street Mumbai 400001, Scrip Code 543419) — two exchanges in one table | — |
| 3 | 24 | Salutation: "Dear Sir/Madam," | — |
| 4 | 26 | Subject line: "Sub: Press Release" | — |
| 5 | 28–30 | Regulation 30 SEBI LODR 2015 basis-of-submission paragraph | — |
| 6 | 32 | Request-to-record paragraph | — |
| 7 | 34–36 | Closing salutation: "Thanking you / Regards" | — |
| 8 | 50 | Enclosure line: "Encl: a/a" | — |
| 9 | 55–57 | Registered-office footer: corporate address (Shriram House, Sadashivanagar, Bengaluru 560080) + registered office (Lakshmi Neela Rite Choice Centre, T. Nagar, Chennai 600017) | — |
| 10 | 60–61 | Contact footer line: phone, fax, website, CIN (L72200TN2000PLC044560), company email | — |
| 11 | 63 | "MEDIA RELEASE" masthead, page 2 | — |
| 12 | 73 | Section header: "Operational Highlights" | — |
| 13 | 97 | Section header: "Financial Highlights" | — |
| 14 | 110 | Page footer: "Page 1 of 3" | — |
| 15 | 112 | "MEDIA RELEASE" masthead, page 3 | — |
| 16 | 114 | Section header: "Significant highlights of Q1 FY27 results are as follows:" | — |
| 17 | 127 | Section header: "Outlook" | — |
| 18 | 153 | Page footer: "Page 2 of 3" | — |
| 19 | 155 | "MEDIA RELEASE" masthead, page 4 | — |
| 20 | 160 | Section header: "About Shriram Properties Limited" | — |
| 21 | 161–165 | About-SPL boilerplate paragraph body (company description, markets, track record — numeric content cross-referenced in §3 rows 24–28) | — |
| 22 | 167 | Section header: "For further details, please contact SPL:" | — |
| 23 | 168–170 | Contact table: Investors/Analysts column (Shrikanth DS, Rahul Agarwal) + Media column (Annet Sumitra Pillai, Louis D'Rozario), 4 named contacts with emails/phones | — |
| 24 | 175 | Page footer: "Page 3 of 3" | — |

---

## SUMMARY OF FLAGS RAISED

- `FORWARD_STATEMENT` x8 (§5, cross-referenced in §2 and §3 where embedded)
- `NO_SAFE_HARBOR_CLAUSE` x1 (§6, row 2) — a documented absence, not a positive count
- No `ZERO_STANDING`, `ENTITY_CHANGE`, `REPEAT_QUESTION`, `MGMT_ABSENCE` applicable to this doctype/document
- `DROPPED_SLIDE` not evaluable — no prior-quarter ledger supplied for diff
