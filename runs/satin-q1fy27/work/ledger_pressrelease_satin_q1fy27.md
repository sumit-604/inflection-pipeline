# A2 COMPLETENESS LEDGER — SATIN Q1 FY27 — Press Release (doctype: presentation)
Source: `extract_pressrelease_satin_q1fy27.txt` (6 pages, text-native, 304 lines)
Prior-quarter ledger: not available (no path supplied) — DROPPED_SLIDE / prior-period diff checks not performed; noted as gap, not silently skipped.

```
=== A2 COUNT TEST ===
category: bullets_narrative_and_subsidiary   grep_count: 44   sweep_count: 44   match: yes
category: table_line_items                   grep_count: 19   sweep_count: 19   match: yes
category: footnotes                          grep_count: 2    sweep_count: 2    match: yes
category: section_headings                   grep_count: 10   sweep_count: 10  match: yes
category: pages_slides                       grep_count: 6    sweep_count: 6    match: yes
category: structural_prose_items             grep_count: 20   sweep_count: 20   match: yes
category: absent_standard_disclosures        grep_count: 11   sweep_count: 11   match: yes
TOTAL DISCLOSURE UNITS ENUMERATED: 112 (44+19+2+10+6+20+11)
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation method: (1) grep pass — `grep -n "•"` for every bullet (44 hits); distinctive-keyword greps for each table row label (AUM/Disbursement/Total Revenue/PPOP/PAT/ROA/ROE x2 tables + 5 Footprints rows = 19); `grep -n "^\*ROA and ROE"` for footnotes (2); heading-regex grep for section headings (10, corrected to include "Borrowing Profile (standalone)"); `grep -n "^\[page"` for pages (6); 20 unique single-occurrence anchor strings for cover-letter/headline/closing/quote prose blocks (each confirmed count=1, sum 20); case-insensitive greps for 11 candidate standard MFI disclosures (NNPA, PAR buckets, Tier I/II, net worth, dividend, gross write-off amount, cost of funds, cost-to-income, segment AUM split, off-book/securitised AUM, consolidated credit cost — each returned 0 hits, confirming absence). (2) Manual line-by-line sweep of all 304 lines cross-checked against every grep list — no discrepancies found. GATE A2: PASS.

---

## 1. Cover Letter / Regulatory Submission (page 1)

| # | Item | Line(s) | Detail | Flags |
|---|------|---------|--------|-------|
| 1.1 | Letter date | 16 | "July 30, 2026" | |
| 1.2 | Addressee 1 | 18-19, 24 | The Manager, National Stock Exchange of India Ltd.; Symbol: SATIN | |
| 1.3 | Addressee 2 | 18-22, 24 | The Manager, BSE Limited; Scrip Code: 539404 | |
| 1.4 | Subject line | 26 | "Sub: Press Release" | |
| 1.5 | Regulatory basis + subject matter | 30-32 | Regulation 30 SEBI (LODR) Regulations 2015; Un-audited Financial Results (Standalone and Consolidated) for quarter ended June 30, 2026 | |
| 1.6 | Website availability statement | 34 | Disclosure to be made available on company website | |
| 1.7 | Digital signature block | 40-52 | Signatory: Vikas Gupta; Designation: Company Secretary & Chief Compliance Officer; Digitally signed by VIKAS GUPTA; timestamp 2026.07.30 16:44:48 +05'30' | Note: signature timestamp is same-day as press release date (30 Jul 2026); no board-meeting-conclusion time given in this doc to cross-check against (this is a press release, not the outcome letter) |
| 1.8 | Enclosure note | 53 | "Encl: A/a" | |

## 2. Headline & Framing (page 2 top)

| # | Item | Line(s) | Detail | Flags |
|---|------|---------|--------|-------|
| 2.1 | Headline | 55 | "Satin Creditcare Reports Consolidated PAT of ₹123 Crores in Q1 FY27, 172% up YoY" | |
| 2.2 | Subheadline | 56 | "20th profitable quarter in a row" | |
| 2.3 | Dateline | 58 | "30th July 2026, New Delhi" | |
| 2.4 | Intro sentence | 59-60 | Announces results for quarter ended 30th June 2026 | |

## 3. Consolidated Highlights table (page 2)

Header row: line 64 — Particulars (₹Crores) | Q1FY27 | Q1FY26 | %Change | Q4FY26 | %Change

| # | Metric | Line | Q1FY27 | Q1FY26 | %Chg YoY | Q4FY26 | %Chg QoQ | Flags |
|---|--------|------|--------|--------|----------|--------|----------|-------|
| 3.1 | Assets under Management (AUM) | 66 | 15,935 | 12,499 | 27.5% | 15,174 | 5.0% | |
| 3.2 | Disbursement | 68 | 3,495 | 2,242 | 55.9% | 4,420 | -20.9% | |
| 3.3 | Total Revenue | 70 | 827 | 680 | 21.7% | 830 | -0.3% | |
| 3.4 | Pre-Provision Operating Profit (PPOP) | 72-74 | 267 | 201 | 33.0% | 290 | -7.9% | |
| 3.5 | Profit After Tax (PAT) | 76 | 123 | 45 | 172.0% | 162 | -24.3% | |
| 3.6 | ROA* | 78 | 4.0% | 1.7% | +232bps | 5.2% | -114bps | see footnote 3.F |
| 3.7 | ROE* | 80 | 20.4% | 8.0% | +1242bps | 25.5% | -512bps | see footnote 3.F |
| 3.F | Footnote | 81 | "*ROA and ROE exclude management overlay of ₹36 Crores created as an extra buffer" | | | | | qualifies rows 3.6/3.7 |

## 4. Footprints and Outreach table (page 2)

Header row: line 85 — Particulars | Q1FY27 | Q1FY26

| # | Metric | Line | Q1FY27 | Q1FY26 | Flags |
|---|--------|------|--------|--------|-------|
| 4.1 | States & UTs | 86 | 32 | 29 | |
| 4.2 | Branches | 87 | 2,041 | 1,599 | |
| 4.3 | No. of Employees | 88 | 18,518 | 16,454 | |
| 4.4 | No. of Loan Officers | 89 | 12,511 | 11,239 | |
| 4.5 | No. of Clients (Lakhs) | 90 | 34.0 | 32.9 | |

Note: no %Change columns in this table (unlike Consolidated/Standalone Highlights) — a formatting asymmetry, not a data gap.

## 5. Standalone Highlights table (pages 2-3, spans page break)

Header row: line 95 (page 2), repeated at line 107 (page 3 continuation)

| # | Metric | Line | Q1FY27 | Q1FY26 | %Chg YoY | Q4FY26 | %Chg QoQ | Flags |
|---|--------|------|--------|--------|----------|--------|----------|-------|
| 5.1 | Assets under Management (AUM) | 97 | 13,312 | 10,956 | 21.5% | 12,853 | 3.6% | |
| 5.2 | Disbursement | 99 | 3,008 | 2,065 | 45.6% | 3,820 | -21.3% | |
| 5.3 | Total Revenue | 101 | 734 | 609 | 20.5% | 720 | 2.0% | |
| 5.4 | Pre-Provision Operating Profit (PPOP) | 109-111 | 258 | 189 | 36.4% | 256 | 0.7% | |
| 5.5 | Profit After Tax (PAT) | 112 | 120 | 43 | 182.3% | 137 | -12.2% | |
| 5.6 | ROA* | 113 | 4.3% | 1.7% | +261bps | 4.8% | -46bps | see footnote 5.F |
| 5.7 | ROE* | 115 | 18.5% | 6.8% | +1163bps | 19.9% | -148bps | see footnote 5.F |
| 5.F | Footnote | 116 | "*ROA and ROE exclude management overlay of ₹36 Crores created as an extra buffer" (identical text to 3.F) | | | | | qualifies rows 5.6/5.7 |

## 6. Narrative Metric Block: "Highlights for Q1FY27" (page 3)

Heading: line 120

| # | Line | First words / metric | Flags |
|---|------|----------------------|-------|
| 6.1 | 122-123 | PAR 1 improved to 3.0% in Q1FY27 from 3.7% in Q4FY26 (standalone) | only PAR 1 given; PAR 30/60/90 not disclosed (see §20.2) |
| 6.2 | 124-125 | Collection efficiency for the X bucket at 99.9% in Q1FY27 | |
| 6.3 | 126-128 | Credit cost reduced 177bps to 3.06% (incl. ₹36cr overlay); ex-overlay 1.97%; FY27 guidance 3-3.5% | standalone only; consolidated credit cost not given (see §20.11) |
| 6.4 | 129 | Marginal Cost of Borrowing down 37bps YoY to 10.52% (ex sub-debt) | not the same as overall Cost of Funds (see §20.7) |
| 6.5 | 130-131 | Stable/experienced management team, core leadership avg tenure 10+ years | |
| 6.6 | 132-133 | Promoters to infuse ₹100 Crores equity at ~17% premium to minimum SEBI issue price | |
| 6.7 | 134-135 | Strategic entry into Kerala (June 2026); South India build-out (TN, KA, AP, Telangana) | |
| 6.8 | 136-137 | Stable management team, 10+ yr vintage; zero attrition in field leadership (200 personnel: RM/ZM/Circle Head/Business Head) | |

## 7. Narrative Metric Block: "Capital Adequacy and Liquidity" (page 3)

Heading: line 139

| # | Line | Metric | Flags |
|---|------|--------|-------|
| 7.1 | 141 | Capital Adequacy Ratio 26.74% as on 30 Jun'26 | |
| 7.2 | 142 | Book Value per share ₹270 (consolidated basis) | absolute Net worth ₹ not given (see §20.4) |
| 7.3 | 143-144 | Balance sheet liquidity ₹2,311 Cr; undrawn sanctions ₹2,593 Cr as on 30 Jun 2026 | |

## 8. Narrative Metric Block: "Borrowing Profile (standalone)" (page 3)

Heading: line 145

| # | Line | Metric | Flags |
|---|------|--------|-------|
| 8.1 | 147 | Total on-book borrowings ₹10,216 Cr as of 30 Jun'26 | |
| 8.2 | 148 | Debt-to-equity ratio 3.15x as on 30 Jun'26 | |
| 8.3 | 149-150 | Borrowing mix: banks 70%, overseas funds 13%, DFIs 11%, NBFCs 6% (sums to 100%) | |
| 8.4 | 151-152 | 77 active lenders, incl. 4 added in Q1FY27 | |

## 9. Narrative Metric Block: "Asset Quality" (page 4)

Heading: line 159

| # | Line | Metric | Flags |
|---|------|--------|-------|
| 9.1 | 161-162 | On-book GNPA 2.18% (₹219 Cr), down from 3.74% in June'25 | NNPA not given anywhere in doc — ZERO_STANDING (see §20.1) |
| 9.2 | 163-164 | On-book provisions ₹252 Cr (2.51% of on-book portfolio); RBI-required provision ₹152 Cr | provision surplus over RBI requirement = ₹100 Cr, not stated as a explicit figure (derivable, not disclosed) |
| 9.3 | 165-166 | ₹36 Cr management overlay maintained as additional buffer | cross-references PAT/ROA/ROE footnote and Highlights bullet 6.3 — same ₹36cr cited three times in doc (lines 81, 116, 126-127, 143 n/a, 165, 235) |
| 9.4 | 167 | Stage 3 coverage ratio 84.66% as on 30 Jun'26 vs 72.85% as on 31 Mar'26 | |
| 9.5 | 168 | Overall Provision Coverage Ratio 115.07% | |
| 9.6 | 169 | Recovery against write-offs ₹8 Cr during Q1FY27 | gross write-off amount for the quarter not disclosed (see §20.6) |

## 10. Subsidiary Block: Satin Housing Finance Limited (SHFL) (page 4)

Sub-heading: line 172 — "our housing finance subsidiary"

| # | Line | Metric | Flags |
|---|------|--------|-------|
| 10.1 | 174-175 | YoY AUM growth 31.40%; total AUM ₹1,263 Cr; customer base 12,412 | |
| 10.2 | 176-177 | 34 active lenders incl. NHB refinance | |
| 10.3 | 178 | CRAR 59.79%; gearing ratio 1.79x | |
| 10.4 | 179 | PAT for Q1FY27 ₹1.5 Cr | |
| 10.5 | 180-181 | Credit rating A- (Stable) from ICRA and Infomerics | |

## 11. Subsidiary Block: Satin Finserv Limited (SFL) (page 4)

Sub-heading: line 183 — "our MSME-focused lending platform"

| # | Line | Metric | Flags |
|---|------|--------|-------|
| 11.1 | 184 | AUM ₹1,360 Cr as of Q1FY27 | |
| 11.2 | 185-186 | YoY growth 133.67% | |
| 11.3 | 187 | Green finance: 50 loans disbursed, ₹294 Cr | |
| 11.4 | 188 | CRAR 27.08%; gearing 3.21x | |
| 11.5 | 189 | PAT for Q1FY27 ₹4.9 Cr | |
| 11.6 | 190 | Credit Rating A- (Stable) from ICRA | |

## 12. Subsidiary Block: Satin Technologies Limited (STL) (pages 4-5, spans page break)

Sub-heading: line 192 — "our technology and digital transformation arm"

| # | Line | Metric | Flags |
|---|------|--------|-------|
| 12.1 | 193-195 | Enterprise tech portfolio: HRMS, Core Banking, LMS, LOS, quantum-safe cybersecurity, in-house built | no financial figures (AUM/PAT/CRAR) disclosed for STL, unlike SHFL/SFL/SGAL — ZERO_STANDING (structural: this subsidiary reports narrative only, no numeric contribution disclosed) |
| 12.2 | 196-198 | Core Banking Solution completed dev, entered customer UAT; commercial go-live targeted Sept 2026; LMS/LOS expansion for NBFCs underway | forward-commitment phrase ("targeted for") |
| 12.3 | 199-200 | QTrino Labs: first customer delivery milestone; Assessment Tool v1 complete; FIPS certification "in progress" | forward-commitment / hedge phrase ("in progress") |
| 12.4 | 201-203, 205 | Next-gen HRMS platform live in production; expanding customer base/partner network; "increasing commercial traction" (bullet spans page break, continues line 205) | |
| 12.5 | 206-207 | Strengthened execution via senior leadership additions; continued investment to accelerate commercialization/scaling | |

## 13. Subsidiary Block: Satin Growth Alternatives Limited (SGAL) (page 5)

Sub-heading: line 210 — "our alternative asset management platform"

| # | Line | Metric | Flags |
|---|------|--------|-------|
| 13.1 | 212-213 | First SEBI-approved Category II AIF (Scheme 1), target corpus ₹200 Cr | target corpus, not committed/raised corpus — forward-commitment phrase |
| 13.2 | 214 | Fund led by All-Women Board and investment team | |
| 13.3 | 216-217 | Fund aim: quasi debt/equity capital to underfunded startups/MSMEs, rural/semi-urban focus | |
| 13.4 | 218-219 | MoU signed with SBI to co-invest in startups | MoU = non-binding; no financial commitment amount disclosed |
| 13.5 | 220-222 | Leverages SCNL's Pan-India reach; RM-led on-ground audits; founder growth support | |
| 13.6 | 223-224 | "Overall Strategic Impact" framing: marks Satin's transition to diversified financial services platform | |
| 13.7 | 225-226 | Actively onboarding institutional/retail LPs; maintaining deal pipeline | no LP count, no capital raised/committed figure disclosed — ZERO_STANDING |

## 14. Chairman Quote — Dr. HP Singh, CMD (page 5)

Attribution line: 229-230

| # | Line(s) | Paragraph gist | Flags |
|---|---------|-----------------|-------|
| 14.1 | 230-232 | "Strongest opening quarter in eight years"; microfinance industry emerging from a difficult two-year period; growth returning | |
| 14.2 | 234-237 | Balance-sheet strengthening over near-term profitability; management overlay increased to ₹36 Cr; provisions "significantly above" regulatory requirement; moderated profitability/return ratios acknowledged | ties directly to §9.2/9.3 numeric disclosures |
| 14.3 | 239-241 | Institution steered through demonetisation, pandemic, recent industry stress; cushions built in good times provide resilience | |
| 14.4 | 243-246 | Optimism on housing finance, MSME, technology, alternative investment businesses; commitment to "responsible growth" and value "beyond any single quarter" | forward-commitment / hedge language, no numeric target |

## 15. About Satin Creditcare Network Limited (page 6)

Heading: line 253; paragraph: 255-268 (single paragraph, multiple embedded facts)

| # | Line | Embedded fact | Flags |
|---|------|----------------|-------|
| 15.1 | 255-256 | Presence in 27 states, 5 UTs, over 1,00,000 villages | |
| 15.2 | 260-261 | SHFL incorporated April 2017 (housing finance subsidiary) | |
| 15.3 | 262-263 | SFL — separate NBFC license Jan 2019 for MSME lending | |
| 15.4 | 263-264 | STL incorporated August 2024 (software services) | |
| 15.5 | 265-266 | SGAL incorporated August 2025 (Category II AIF manager) | |
| 15.6 | 267-268 | As on 30 June 2026: 2,041 branches, headcount 18,518, 34 lakh clients (consolidated) | restates §4.2-4.4 Footprints figures; consistent |

## 16. Disclaimer (page 6)

Heading: line 270; paragraph: 272-282

| # | Line | Content | Flags |
|---|------|---------|-------|
| 16.1 | 272-282 | Standard forward-looking-statements disclaimer; no undertaking to revise forward-looking statements | |

## 17. Corporate Footer Block (page 6)

| # | Line | Field | Flags |
|---|------|-------|-------|
| 17.1 | 286 | Company name: Satin Creditcare Network Ltd. | |
| 17.2 | 287 | CIN: L65991DL1990PLC041796 | |
| 17.3 | 288-289 | Corporate address (Gurugram) + landline | |
| 17.4 | 290-291 | Registered Office (Delhi) + email ID | |
| 17.5 | 292 | Website | |

## 18. Media/Investor Contact Block (page 6)

| # | Line | Field | Flags |
|---|------|-------|-------|
| 18.1 | 296 | Contact name: Ms. Aditi Singh | |
| 18.2 | 297 | Designation: Chief Strategy Officer | |
| 18.3 | 298 | Email | |
| 18.4 | 299 | Phone | |

## 19. Pages ("slides") — every page, content type

| Page | Line marker | Title / lead content | Content type | Flags |
|------|-------------|------------------------|--------------|-------|
| 1 | 15 | Cover letter to NSE/BSE | text | |
| 2 | 54 | Headline + Consolidated Highlights table + Footprints table + Standalone Highlights table (top) | text + 3 tables | |
| 3 | 106 | Standalone Highlights table (continuation) + Highlights bullets + Capital Adequacy + Borrowing Profile | table continuation + text (bullets) | |
| 4 | 158 | Asset Quality + Subsidiaries (SHFL, SFL, STL start) | text (bullets) | |
| 5 | 204 | STL (continuation) + SGAL + Chairman quote | text (bullets + quote) | |
| 6 | 252 | About SCNL + Disclaimer + corporate footer + media contact | text | |

## 20. Absent Standard Disclosures (flagged ZERO_STANDING — confirmed absent by case-insensitive grep, 0 hits each, cross-checked by manual sweep)

| # | Expected metric (standard for MFI/NBFC quarterly disclosure) | Anchor line (nearest related disclosure) | Flags |
|---|---|---|---|
| 20.1 | NNPA / Net NPA (%) | 161-162 (GNPA given, NNPA absent) | ZERO_STANDING |
| 20.2 | PAR 30/60/90-day buckets | 122-123 (only PAR 1 given) | ZERO_STANDING |
| 20.3 | Tier I / Tier II CRAR break-up | 141 (only blended CAR 26.74% given) | ZERO_STANDING |
| 20.4 | Net worth (absolute ₹ Cr) | 142 (only Book Value/share ₹270 given) | ZERO_STANDING |
| 20.5 | Dividend declaration | n/a — no dividend section anywhere in document | ZERO_STANDING |
| 20.6 | Gross write-off amount for the quarter | 169 (only "recovery against write-offs ₹8cr" given) | ZERO_STANDING |
| 20.7 | Overall / average Cost of Funds | 129 (only "Marginal Cost of Borrowing" 10.52% given) | ZERO_STANDING |
| 20.8 | Cost-to-Income / Opex ratio | n/a — not present in any section | ZERO_STANDING |
| 20.9 | Segment-wise / product-wise AUM split (JLG vs individual vs MSME etc.) | 66/97 (only blended AUM totals given) | ZERO_STANDING |
| 20.10 | Off-book / securitised / assigned AUM amount | 161-164 ("on-book" qualifier implies an off-book component exists but is unquantified) | ZERO_STANDING |
| 20.11 | Consolidated-level Credit Cost | 126-128 (credit cost given for standalone only) | ZERO_STANDING |

---

## Reconciliation notes / items that could not be fully closed
- No prior-quarter ledger was supplied, so `DROPPED_SLIDE` / prior-period disclosure comparison (rule 3 of the Investor Presentation enumeration) could not be run. This is a **data gap, not a mismatch** — it does not affect GATE A2, which reconciles this run's own grep vs. sweep counts only. Flagged for A3/A4 to source the prior-quarter (Q4FY26) press release if available.
- The ₹36 Cr management overlay figure recurs five times across the document (lines 81, 116, 127, 165, 235) in slightly different framings (footnote qualifier, standalone Highlights bullet, Asset Quality bullet, Chairman quote) — enumerated once per occurrence at its own location (rows 3.F, 5.F, 6.3, 9.3, 14.2) rather than collapsed, per "enumerate everything, interpret nothing."
- All 112 units reconciled; no unit was left unresolved.
