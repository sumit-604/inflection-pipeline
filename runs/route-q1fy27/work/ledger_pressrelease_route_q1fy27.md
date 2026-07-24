# LEDGER — Route Mobile Limited (ROUTE), Q1 FY27, doctype: press release (enumerated under INVESTOR PRESENTATION discipline)

Source: `extract_pressrelease_route_q1fy27.txt` (A1 extract). 3-page press release, treated as 3 slide-equivalents.
Prior-quarter ledger: none available — DROPPED_SLIDE check cannot be performed; flag `PRIOR_LEDGER_UNAVAILABLE`.

```
=== A2 COUNT TEST ===
category: slides                    grep_count: 3   sweep_count: 3   match: yes
category: slide_numbers             grep_count: 33  sweep_count: 33  match: yes
category: notes (numbered)          grep_count: 0   sweep_count: 0   match: yes
category: mgmt_claims_fwd_looking   grep_count: 9   sweep_count: 9   match: yes
category: footnotes_disclaimers     grep_count: 1   sweep_count: 1   match: yes
category: signatories_contacts      grep_count: 2   sweep_count: 2   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

grep commands used:
- slides: `grep -c -E "^\[page [0-9]+\]"` → 3
- slide_numbers, financial subset: `grep -o -E "Rs\.?\s?[0-9][0-9,]*\.[0-9]+|[0-9]+\.[0-9]+%"` → 17
- slide_numbers, identifier subset: `grep -o -E "RML/2026-27/692|July 23, 2026|543228|Regulation 30|Regulations, 2015|2026\.07\.23|22:12:03|A34829|30 June, 2026|Established in 2004|5 billion|180 billion|1,000\+|96198 55711"` → 16 (17+16=33)
- notes: `grep -c -E "^\s*[0-9]+\.\s"` → 0 (no numbered notes/footnotes in this document)
- mgmt_claims_fwd_looking: sentence-split of the two quoted management paragraphs (3 + 4 = 7) plus `grep -c -E "^About "` boilerplate blocks (2) → 9
- footnotes_disclaimers: `grep -c -E "Regulation 30"` → 1
- signatories_contacts: `grep -c -E "Company Secretary|Media Contact"` → 2

---

## TABLE 1 — Slides (pages)

| Slide # | Page (source) | Line range | Title / heading | Content type | Flags |
|---|---|---|---|---|---|
| 1 | page 1 | 14-51 | Regulation 30 covering letter to BSE/NSE | text (letter, signature block) | — |
| 2 | page 2 | 53-105 | "Route Mobile Limited announces Q1 FY27 Results" (press release body, headline financials, management quotes, About Route Mobile) | text (headline metrics + narrative + boilerplate) | — |
| 3 | page 3 | 106-127 | About Proximus Global + Additional Resources + Media Contact | text (boilerplate + contact block) | — |

## TABLE 2 — Every number on every slide

| # | Slide | Line | Metric / data point | Value | Context | Flags |
|---|---|---|---|---|---|---|
| 1 | 1 | 15 | Reference number | RML/2026-27/692 | Letter ref no. | — |
| 2 | 1 | 17 | Letter date | July 23, 2026 | Letterhead date | — |
| 3 | 1 | 21 | BSE Scrip Code | 543228 | Addressee identifier | — |
| 4 | 1 | 29 | Regulatory basis | Regulation 30 | SEBI LODR citation | — |
| 5 | 1 | 30 | Regulatory basis (year) | Regulations, 2015 | SEBI LODR citation (year) | — |
| 6 | 1 | 44 | Digital signature date | 2026.07.23 | Signatory timestamp (Tejas Shah) | — |
| 7 | 1 | 45 | Digital signature time | 22:12:03 +05'30' | Signatory timestamp | — |
| 8 | 1 | 49 | ICSI Membership No. | A34829 | Signatory credential | — |
| 9 | 2 | 58 | Revenue from operations (headline) | Rs. 1,151.51 crore | Q1 FY27 headline | — |
| 10 | 2 | 58 | PAT (headline) | Rs. 68.55 crore | Q1 FY27 headline | — |
| 11 | 2 | 60 | Dateline date | July 23, 2026 | Mumbai dateline | — |
| 12 | 2 | 62 | Quarter end date | 30 June, 2026 | Period end | — |
| 13 | 2 | 66 | Revenue from operations (YoY restated) | Rs. 1,151.51 crore | Q1 FY27 vs Q1 FY26 bullet | — |
| 14 | 2 | 66 | Revenue from operations, Q1 FY26 (prior year) | Rs. 1,050.83 crore | YoY comparator | — |
| 15 | 2 | 67 | Profit Before Tax, Q1 FY27 | Rs. 91.47 crore | YoY bullet | — |
| 16 | 2 | 67 | Profit Before Tax, Q1 FY26 (prior year) | Rs. 76.57 crore | YoY comparator | — |
| 17 | 2 | 68 | Profit After Tax, Q1 FY27 (YoY restated) | Rs 68.55 crore | YoY bullet | — |
| 18 | 2 | 68 | Profit After Tax, Q1 FY26 (prior year) | Rs 58.78 crore | YoY comparator | — |
| 19 | 2 | 69 | EPS, basic | Rs. 9.94 | Q1 FY27 | — |
| 20 | 2 | 69 | EPS, diluted | Rs. 9.94 | Q1 FY27 (identical to basic) | — |
| 21 | 2 | 74-75 | Revenue from operations, Q1 FY27 (QoQ restated) | Rs. 1,151.51 crore | QoQ section | — |
| 22 | 2 | 75 | Revenue from operations, Q4 FY26 (prior quarter) | Rs. 1,130.90 crore | QoQ comparator | — |
| 23 | 2 | 77 | Profit Before Tax, Q1 FY27 (QoQ restated) | Rs. 91.47 crore | QoQ section | — |
| 24 | 2 | 77 | Profit Before Tax, Q4 FY26 (prior quarter) | Rs. 139.27 crore | QoQ comparator — PBT down 34.3% QoQ | — |
| 25 | 2 | 78 | PBT margin, Q1 FY27 | 7.94% | Stated margin; no Q4 FY26 or Q1 FY26 margin comparator given anywhere in doc | NO_PRIOR_MARGIN_COMPARATOR |
| 26 | 2 | 80 | Profit After Tax, Q1 FY27 (QoQ restated) | Rs. 68.55 crore | QoQ section | — |
| 27 | 2 | 80 | Profit After Tax, Q4 FY26 (prior quarter) | Rs. 114.43 crore | QoQ comparator — PAT down 40.1% QoQ | — |
| 28 | 2 | 96 | BSE Scrip Code (repeat) | 543228 | "About" boilerplate identifier line | — |
| 29 | 2 | 98 | Year established | 2004 | Company background | — |
| 30 | 3 | 114 | Proximus Global reach (people) | over 5 billion | Group-level boilerplate stat, not RML-specific | — |
| 31 | 3 | 115 | Proximus Global transactions secured annually | more than 180 billion | Group-level boilerplate stat, not RML-specific | — |
| 32 | 3 | 115 | Proximus Global destinations connected | 1,000+ | Group-level boilerplate stat, not RML-specific | — |
| 33 | 3 | 126 | Media contact phone number | +91 96198 55711 | Contact block | — |

Note on revenue/EPS internal consistency: no "NSE: ROUTE" numeric symbol beyond the scrip code; symbol itself is text and not enumerated as a number.

## TABLE 3 — Qualitative management claims and forward-looking statements

| # | Slide | Line | Speaker | Claim / statement (verbatim or near-verbatim) | Type | Flags |
|---|---|---|---|---|---|---|
| 1 | 2 | 82-84 | Seckin Arikan, Chairman RML & CEO Proximus Global | "Route Mobile has continued to demonstrate resilience in a challenging market environment." | Qualitative claim | — |
| 2 | 2 | 84-85 | Seckin Arikan | "The underlying demand for our solutions remains strong, resulting in healthy traffic growth and continued customer engagement." | Qualitative claim | — |
| 3 | 2 | 85-86 | Seckin Arikan | "Route Mobile remains focused on strengthening its portfolio, driving operational discipline, and leveraging its global scale to create long-term value as part of Proximus Global." | Forward-looking / strategic claim | — |
| 4 | 2 | 88-89 | Tushar Agnihotri, CEO Route Mobile | "Q1 FY27 saw continued momentum across the business, with revenue growing year-on-year and quarter-on-quarter." | Qualitative/factual claim | Note: silent on the QoQ PAT/PBT decline (rows 24, 27, 25) |
| 5 | 2 | 89-90 | Tushar Agnihotri | "Profitability was affected by a combination of market-related factors, but these are already being actively addressed through targeted actions to support margin recovery." | Qualitative claim explaining margin decline | UNSPECIFIED_MARKET_FACTORS (no factors named) |
| 6 | 2 | 90-92 | Tushar Agnihotri | "The focus remains clear: improving operational efficiency, rebuilding traffic with existing customers, expanding new customer relationships, and accelerating the adoption of higher-value solutions across the portfolio." | Forward-looking statement (priorities) | — |
| 7 | 2 | 92-94 | Tushar Agnihotri | "With these initiatives already underway, Route Mobile remains confident in its ability to strengthen margins and deliver sustainable long-term growth." | Forward-looking statement (confidence/guidance-like) | No safe-harbor / cautionary-statement disclaimer accompanies this forward-looking language anywhere in the document — see Table 4 |
| 8 | 2 | 96-104 | Corporate boilerplate (no named speaker) | "About Route Mobile Limited" — company description, portfolio, client base, global presence, Proximus Group affiliation | Descriptive/qualitative boilerplate | — |
| 9 | 3 | 107-116 | Corporate boilerplate (no named speaker) | "About Proximus Global" — group description, Telesign/BICS/Route Mobile combination, reach/scale claims (values captured in Table 2 rows 30-32) | Descriptive/qualitative boilerplate | — |

## TABLE 4 — Footnotes and disclaimers qualifying headline numbers

| # | Slide | Line | Text | Qualifies | Flags |
|---|---|---|---|---|---|
| 1 | 1 | 29-30 | "This disclosure is made in accordance with Regulation 30 of the Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015." | The disclosure/filing as a whole (not any specific headline number) | — |

Observation for downstream review (not a ledger omission — the absence is itself the enumerable fact): no footnote, asterisk, or fine print anywhere in the document qualifies, defines, or reconciles the headline revenue/PAT/PBT/EPS/margin figures in Table 2 (rows 9-27) — e.g., no note on the QoQ PBT/PAT decline (-34.3% / -40.1%) beyond the narrative quote at row 5 of Table 3, and no cautionary/safe-harbor statement accompanies the forward-looking language at Table 3 row 7. Flag: `NO_SAFE_HARBOR_DISCLAIMER`.

## TABLE 5 — Signatory and contact blocks

| # | Slide | Line | Block | Name | Designation | Timestamp | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 39-49 | Digital signature (Regulation 30 letter) | Tejas Devendra Shah | Company Secretary & Compliance Officer, ICSI Membership No. A34829 | 2026.07.23 22:12:03 +05'30' | — |
| 2 | 3 | 123-126 | Media contact | Pooja Choudhary | (role not stated) | — (email: investors@routemobile.com; phone: +91 96198 55711) | ROLE_NOT_STATED |

## TABLE 6 — Numbered notes / footnotes (RESULTS FILING style sweep)

| # | Line | Text |
|---|---|---|
| — | — | None present. No numbered note list, no asterisked footnote, no "Note:" prefixed line anywhere in this 3-page document (confirmed by grep `^\s*[0-9]+\.\s` = 0 and manual sweep). |

## TABLE 7 — Zero/nil/dash-valued standing line items

| # | Line | Item | Flags |
|---|---|---|
| — | — | Not applicable — document contains no financial table structure (narrative bullets only), so no standing line items to test for zero/nil/dash values. |

## TABLE 8 — Dropped-slide check (vs prior quarter)

| # | Result |
|---|---|
| — | Prior-quarter ledger not available (path given as "none available"). Dropped-slide comparison cannot be performed this cycle. Flag: `PRIOR_LEDGER_UNAVAILABLE`. |

---
## FLAGS SUMMARY
- `PRIOR_LEDGER_UNAVAILABLE` — Table 8, no prior-quarter ledger supplied for diff.
- `NO_PRIOR_MARGIN_COMPARATOR` — Table 2 row 25, PBT margin 7.94% stated with no prior-period margin given anywhere for comparison.
- `UNSPECIFIED_MARKET_FACTORS` — Table 3 row 5, "market-related factors" behind the margin decline are not named.
- `NO_SAFE_HARBOR_DISCLAIMER` — Table 4, forward-looking language (Table 3 rows 3, 6, 7) carries no cautionary-statement disclaimer.
- `ROLE_NOT_STATED` — Table 5 row 2, media contact designation not given.
