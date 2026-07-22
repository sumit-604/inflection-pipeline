# LEDGER — HFCL Q1FY27 Press Release (presentation-class, 3 pages)
Source: `extract_pressrelease_hfcl_q1fy27.txt` (166 lines, 3 pages, no OCR pages, 100% page coverage)
Enumerator: A2 | Doctype: presentation (narrative press release — enumeration discipline adapted per task instruction: every section/paragraph block is a unit, every headline metric and every stated number is a row, plus the one results table)

```
=== A2 COUNT TEST ===
category: currency_figures_rupee_symbol   grep_count: 11   sweep_count: 11   match: yes
category: percent_figures_symbol          grep_count: 20   sweep_count: 20   match: yes
category: key_highlight_bullets           grep_count: 7    sweep_count: 7    match: yes
category: financial_table_rows            grep_count: 7    sweep_count: 7    match: yes  (note: first-pass grep on bare row labels alone returned 10 — false positives from narrative sentences at lines 106/112/142 reusing the words "Revenue/PBT/PAT"; re-anchored grep to the table's fixed-column-gap format, which then matched exactly the 7 real table rows at lines 96-102)
category: section_headers                 grep_count: 6    sweep_count: 6    match: yes  (note: first-pass grep on "^Consolidated Financial Highlights" missed line 91 because of a leading space, while "Optical Connectivity" falsely matched a narrative sentence at line 154 reusing the phrase; net count coincidentally landed on 6 for the wrong six lines — re-anchored the regex to leading-whitespace + end-of-line and got the correct six: 76, 91, 115, 117, 129, 151)
category: named_entities                  grep_count: 5    sweep_count: 5    match: yes  (note: first-pass single-line grep found only 4 — missed SEBI because "Securities and Exchange" / "Board of India" wrap across lines 25/26; confirmed with a multiline-tolerant pass, count corrected to 5)
category: capacity_figures_million_fkm     grep_count: 4    sweep_count: 4    match: yes
category: standalone_paragraph_figures     grep_count: 4    sweep_count: 4    match: yes
category: business_numbers_master_list     grep_count: 43   sweep_count: 43   match: yes  (cross-check: sum of currency figures + percent figures + Bps + multiple + table absolute values + capacity figures + standalone figures, de-duplicated of unit-label-only symbol occurrences, reconciles to 43 discrete disclosed figures)
gate_a2: pass
=== END COUNT TEST ===
```

---

## TABLE 1 — Regulatory Cover Letter (Page 1, lines 15-61)

| # | Line(s) | Unit | Content | Flags |
|---|---------|------|---------|-------|
| 1.1 | 16 | Header | Letter ref "HFCL/SEC/26-27", dated July 22, 2026 | |
| 1.2 | 18-23 | Addressee | BSE Ltd., Mumbai 400001; Security Code No. 500183 | |
| 1.3 | 18-23 | Addressee | National Stock Exchange of India Ltd., Mumbai 400051; Security Code No. HFCL | |
| 1.4 | 25-26 | Regulatory citation | "RE: Intimation under Regulation 30 read with Schedule III of the Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015" | entity name (SEBI) wraps lines 25/26 |
| 1.5 | 28-30 | Subject line | Press Release on Un-audited Financial Results for 1st Quarter ended June 30, 2026, FY2026-27, Standalone and Consolidated basis | |
| 1.6 | 32 | Salutation | "Dear Sir(s)/ Madam," | |
| 1.7 | 34-37 | Body | Results approved by Audit Committee and Board of Directors at "respective meetings held on July 22, 2026" | board meeting start/end times: NOT FOUND — no times disclosed in this filing, only the date |
| 1.8 | 39-40 | Body | Request to take on record and disseminate on respective websites | |
| 1.9 | 42-46 | Closing | "Thanking you, Yours faithfully, For HFCL Limited" | |
| 1.10 | 47-53 | Signature block | Manoj Baid, President & Company Secretary; digitally signed Date: 2026.07.22, 13:48:38 +05'30' | signature timestamp recorded; cannot be checked against board-meeting conclusion time since #1.7 has no time — INDETERMINATE, not a flaggable anomaly on this evidence |
| 1.11 | 55 | Enclosure | "Encl.: Press Release" | |
| 1.12 | 60 | Footer | Regd. Office & Works: 8, Electronics Complex, Chambaghat, Solan-173213 (H.P.); Tel (01792) 230644 / 230645 / 230647; Fax (01792) 231902 | administrative, not a business disclosure figure |
| 1.13 | 61 | Footer | Corporate Identity Number: L64200HP1987PLC007466 | |

## TABLE 2 — Press Release Masthead & Headline (Page 2, lines 63-76)

| # | Line(s) | Content | Flags |
|---|---------|---------|-------|
| 2.1 | 63-64 | "Press Release / For Immediate Release" | |
| 2.2 | 67-69 | Headline: "HFCL delivers Record Quarterly Financial Performance with Highest-Ever Revenue, Profitability and Order Book" — three superlative ("highest-ever") claims bundled in one headline | superlative claim, no independently verifiable figure attached in the headline itself; figures follow in bullets |
| 2.3 | 70 | Sub-headline: "Raises FY27 Revenue Growth Aspiration to 40%" | number: 40% — first of two occurrences, see 3.5 |
| 2.4 | 72-74 | Dateline/intro: New Delhi, July 22, 2026; HFCL described as "leading technology enterprise" across Optical Fiber/OFC/Connectivity, Telecom Products, Defence & Aerospace, Digital Infrastructure; "highest ever quarterly financial results for the quarter ended June 30, 2026" | date figure: June 30, 2026 |
| 2.5 | 76 | Section header: "Key highlights during Q1FY27" | |

## TABLE 3 — Key Highlights Bullets (Page 2, lines 78-89) — 7 bullets

| # | Line(s) | Claim / Figure | Flags |
|---|---------|-----------------|-------|
| 3.1 | 78 | EBITDA Margin crossed 23% | number: 23% |
| 3.2 | 79-80 | Highest-Ever Order Book of ~₹26,665 crore, nearly 5 times of FY26 Revenue, strengthening long-term revenue visibility | numbers: ~26,665 (₹ crore); 5x — value is tilde-qualified (approximate), not exact | APPROX_VALUE |
| 3.3 | 81-82 | Export revenue ₹1063.30 crore (55.53% of revenue) Q1FY27 vs ₹209.70 crore (24.08% of revenue) Q1FY26 | numbers: 1063.30; 55.53%; 209.70; 24.08% |
| 3.4 | 83-84 | Segment revenue from product segment: 85% of total revenue Q1FY27 vs 66% Q1FY26 vs 85% Q4FY26 | numbers: 85%; 66%; 85% (Q1FY27 and Q4FY26 values coincide at 85%) | REPEAT_NUMBER (85% appears twice, different periods, coincidental match — not an error, noted for audit trail) |
| 3.5 | 85 | FY27 Revenue Growth to the best of its estimate revised to 40% | number: 40% — repeat of 2.3 | REPEAT_NUMBER (headline restated verbatim in bullet form — consistent) |
| 3.6 | 86-87 | Board approves investment of ₹215 crore in building advanced AI Data Centre Connectivity Solutions manufacturing facility | number: 215 (₹ crore) — repeated later in MD quote, see 9.3 |
| 3.7 | 88-89 | Optical Fiber and Optical Fiber Cable capacity expansion, and setting up of greenfield Preform manufacturing facility (backward integration), "progressing as planned" | qualitative, no new figure in this bullet — capacity figures given later on page 3 (Table 7) |

## TABLE 4 — Consolidated Financial Highlights Table (Page 2, lines 91-102) — 7 line items

| # | Line | Particular | Q1FY27 (₹ cr) | Q1FY26 (₹ cr) | Y-o-Y Change | Flags |
|---|------|------------|----------------|----------------|--------------|-------|
| 4.1 | 96 | Revenue | 1914.98 | 871.02 | 119.85% | |
| 4.2 | 97 | EBIDTA | 445.27 | 42.93 | 937.20% | |
| 4.3 | 98 | EBIDTA Margin (%) | 23.25% | 4.93% | 1832 Bps | |
| 4.4 | 99 | PBT | 331.52 | -44.70 | -- | ZERO_STANDING — Change cell is dash because prior-year base is negative (% change undefined), enumerated per rule, not dropped |
| 4.5 | 100 | PBT Margin (%) | 17.31% | -5.13% | -- | ZERO_STANDING (same reason as 4.4) |
| 4.6 | 101 | PAT | 245.64 | -29.30 | -- | ZERO_STANDING (same reason as 4.4) |
| 4.7 | 102 | PAT Margin (%) | 12.83% | -3.36% | -- | ZERO_STANDING (same reason as 4.4) |

Table header row (line 94): Particulars | Q1FY27 | Q1FY26 | Change; units row (line 95/81 in source numbering "₹in crore / ₹in crore / Y-o-Y %").

## TABLE 5 — Standalone Financial Highlights (Page 2, lines 105-106) — narrative-embedded, 4 figures

| # | Line | Metric | Q1FY27 value | Flags |
|---|------|--------|---------------|-------|
| 5.1 | 105 | Standalone Revenue | ₹1607.80 crore | |
| 5.2 | 105 | Standalone EBIDTA | ₹336.35 crore | |
| 5.3 | 106 | Standalone PBT | ₹240.12 crore | |
| 5.4 | 106 | Standalone PAT | ₹179.21 crore | NOT_FOUND — no Q1FY26 standalone comparison or YoY% is disclosed anywhere in the release (unlike the consolidated table, which gives full prior-year and YoY); standalone base-period figures and standalone growth rate are silent |

## TABLE 6 — Growth Drivers Narrative (Page 2, lines 108-113)

| # | Line(s) | Claim | Flags |
|---|---------|-------|-------|
| 6.1 | 108-113 | "Record quarterly financial performance reflects convergence of multiple structural growth drivers" — lists: (a) rising demand from hyperscale data centres, (b) improved product realisations, (c) operating leverage through economies of scale, (d) diversified portfolio of high-value technology products, (e) expanding export opportunities — collectively driving improvement across Revenue, EBITDA, PBT, PAT | no new numeric figures; qualitative attribution of the results in Table 4/5 to five named drivers |
| 6.2 | 112-113 | Forward-looking statement: "As these market trends continue to strengthen and our execution remains robust, we are well positioned to sustain this growth momentum" | forward-commitment / hedge-adjacent phrase ("well positioned to sustain") — no quantified commitment |

## TABLE 7 — Key Business Highlights: Optical Connectivity (Page 3, lines 115-127)

| # | Line(s) | Claim / Figure | Flags |
|---|---------|-----------------|-------|
| 7.1 | 115 | Section header: "Key Business Highlights" | |
| 7.2 | 117-121 | Subsection header "Optical Connectivity"; narrative: market expansion driven by AI-driven data centres, cloud infrastructure, next-gen telecom networks, digital infrastructure globally; "capacity expansion programme remains on track" | qualitative |
| 7.3 | 122 | Optical Fiber capacity increasing from 28 million fibre kilometres to 34 million fibre kilometres | numbers: 28; 34 (million fkm) |
| 7.4 | 123 | Optical Fiber Cable capacity expanding from 34 million fibre kilometres to 43 million fibre kilometres | numbers: 34; 43 (million fkm) — note "34" appears as both the OFC starting capacity here and the OF ending capacity in 7.3; same figure, different metric, not a duplication error |
| 7.5 | 126-127 | Backward integration into preform manufacturing "further strengthening supply chain resilience and long-term competitiveness" | qualitative, no figure; cross-references bullet 3.7's "greenfield manufacturing facility of Preform" |

## TABLE 8 — Key Business Highlights: Defence & Aerospace (Page 3, lines 129-137)

| # | Line(s) | Claim | Flags |
|---|---------|-------|-------|
| 8.1 | 129 | Subsection header: "Defence & Aerospace" | |
| 8.2 | 131-134 | HFCL scaling Defence & Aerospace business through indigenous technology development, expanding manufacturing capabilities and "proposed acquisition" | proposed acquisition referenced but not named, no counterparty, no value — NOT_FOUND (target, structure, consideration all unspecified) |
| 8.3 | 132-134 | During the quarter, Company initiated process of setting up Ammunition Manufacturing Complex in Andhra Pradesh, for Multi-mode Hand Grenade, Electronic Fuzes, other ammunition products | no figures (capacity, capex, timeline) disclosed for this new facility — NOT_FOUND |
| 8.4 | 134-136 | Simultaneously strengthening portfolio across Surveillance Radars, Thermal Imaging Sites, Tactical Communication Solutions | qualitative |
| 8.5 | 136-137 | Defence business framed as "strategic long-term growth engine," underpinned by "sustainable demand, strong policy support, and significant opportunities for value creation over the coming years" | forward-commitment phrase, no quantification |

## TABLE 9 — MD Quote: Mr. Mahendra Nahata, Managing Director (Page 3, lines 139-149)

| # | Line(s) | Content | Flags |
|---|---------|---------|-------|
| 9.1 | 139 | Speaker attribution: "Commenting on the performance, Mr. Mahendra Nahata, Managing Director, HFCL, said" | |
| 9.2 | 140-143 | "HFCL has entered a new phase of accelerated and profitable growth"; reiterates highest-ever quarterly Revenue, Profitability, Order Book; credits "strength of our execution, expanding product portfolio and growing market opportunities" | restates headline superlative claim (2.2) — no new figure |
| 9.3 | 145-149 | "Convergence of AI, digital infrastructure, optical connectivity and defence modernisation is creating significant long-term opportunities"; Board "today approved expansion of manufacturing set-up for advanced data centre connectivity products with an investment of approximately ₹215 crore"; closes "we remain well positioned to create sustainable long-term value for our stakeholders" | number: ~215 (₹ crore) — repeat of bullet 3.6, consistent | REPEAT_NUMBER (cross-referenced, consistent with 3.6) |

## TABLE 10 — About HFCL Section (Page 3, lines 151-176)

| # | Line(s) | Content | Flags |
|---|---------|---------|-------|
| 10.1 | 151 | Section header: "About HFCL" | |
| 10.2 | 153-159 | Boilerplate description: technology enterprise, Optical Fiber/OFC, Optical Connectivity Solutions, Telecom and Defence Equipment; digital networks for Telcos, Enterprises, Defence Forces; "decades of experience in Fiber optics" | no figures (decades unquantified) |
| 10.3 | 160-166 | R&D Centers located at Gurgaon, Bengaluru, Hyderabad (3 named locations), plus unnamed "invested R&D houses and other R&D collaborators" in India and abroad; product list: Optical Fiber/Cable, IP-MPLS Routers, Backhaul Radios, Wi-Fi Systems, Thermal Weapon Sights, Electronic Fuzes, High-Capacity Radio Relay, Surveillance Radars; repeats the Andhra Pradesh ammunition facility (cross-ref 8.3) | |
| 10.4 | 168-169 | Manufacturing facilities in Hyderabad, Goa, Chennai (through subsidiary HTL Ltd.), and Hosur for defence equipment | entity named: HTL Ltd. (subsidiary) |
| 10.5 | 171-173 | "Partner of choice" across India, Europe, Asia Pacific, Middle East, Africa, USA (6 geographies); commitment to quality and environmental sustainability | |
| 10.6 | 175 | Website: www.hfcl.com | |

## TABLE 11 — Signature, Contact & PR Blocks (Page 3, lines 177-183)

| # | Line(s) | Content | Flags |
|---|---------|---------|-------|
| 11.1 | 177-181 | HFCL contacts: Manoj Baid, Amit Agarwal, Alok Chander — emails manoj.baid@hfcl.com, amit.agarwal@hfcl.com, alok@hfcl.com | |
| 11.2 | 177-181 | External PR agency: Kommune PR — Ruby Sinha, Saurabh Gupta, Saurav — email hfcl@kommune.in | entity named: Kommune PR |
| 11.3 | 183 | HFCL Contact: +91 11 35209400 | administrative |
| 11.4 | 183 | Kommune PR Contact: +91 98180 75578, +91 96542 44050 | administrative |

## TABLE 12 — Master "Every Number Stated" Cross-Reference (business/disclosure figures only; excludes pure administrative identifiers already itemized in Tables 1/11) — 43 rows

| # | Line | Figure | Context | Flags |
|----|------|--------|---------|-------|
| 1 | 70 | 40% | FY27 revenue growth aspiration (headline) | REPEAT_NUMBER (=#12) |
| 2 | 78 | 23% | EBITDA margin crossed | |
| 3 | 79 | ~26,665 (₹cr) | Order Book, highest-ever | APPROX_VALUE |
| 4 | 79 | 5x | Order book vs FY26 revenue multiple | |
| 5 | 81 | 1063.30 (₹cr) | Export revenue Q1FY27 | |
| 6 | 81 | 55.53% | Export revenue % of total, Q1FY27 | |
| 7 | 81-82 | 209.70 (₹cr) | Export revenue Q1FY26 | |
| 8 | 82 | 24.08% | Export revenue % of total, Q1FY26 | |
| 9 | 83 | 85% | Product segment % of revenue, Q1FY27 | REPEAT_NUMBER (=#11) |
| 10 | 83-84 | 66% | Product segment % of revenue, Q1FY26 | |
| 11 | 84 | 85% | Product segment % of revenue, Q4FY26 | REPEAT_NUMBER (=#9) |
| 12 | 85 | 40% | FY27 revenue growth, restated | REPEAT_NUMBER (=#1) |
| 13 | 86 | 215 (₹cr) | Board-approved AI data centre connectivity investment | REPEAT_NUMBER (=#43) |
| 14 | 96 | 1914.98 (₹cr) | Consolidated Revenue Q1FY27 | |
| 15 | 96 | 871.02 (₹cr) | Consolidated Revenue Q1FY26 | |
| 16 | 96 | 119.85% | Consolidated Revenue YoY change | |
| 17 | 97 | 445.27 (₹cr) | Consolidated EBIDTA Q1FY27 | |
| 18 | 97 | 42.93 (₹cr) | Consolidated EBIDTA Q1FY26 | |
| 19 | 97 | 937.20% | Consolidated EBIDTA YoY change | |
| 20 | 98 | 23.25% | Consolidated EBIDTA margin Q1FY27 | |
| 21 | 98 | 4.93% | Consolidated EBIDTA margin Q1FY26 | |
| 22 | 98 | 1832 Bps | EBIDTA margin YoY change | |
| 23 | 99 | 331.52 (₹cr) | Consolidated PBT Q1FY27 | |
| 24 | 99 | -44.70 (₹cr) | Consolidated PBT Q1FY26 | |
| 25 | 99 | -- | PBT YoY change | ZERO_STANDING |
| 26 | 100 | 17.31% | Consolidated PBT margin Q1FY27 | |
| 27 | 100 | -5.13% | Consolidated PBT margin Q1FY26 | |
| 28 | 100 | -- | PBT margin YoY change | ZERO_STANDING |
| 29 | 101 | 245.64 (₹cr) | Consolidated PAT Q1FY27 | |
| 30 | 101 | -29.30 (₹cr) | Consolidated PAT Q1FY26 | |
| 31 | 101 | -- | PAT YoY change | ZERO_STANDING |
| 32 | 102 | 12.83% | Consolidated PAT margin Q1FY27 | |
| 33 | 102 | -3.36% | Consolidated PAT margin Q1FY26 | |
| 34 | 102 | -- | PAT margin YoY change | ZERO_STANDING |
| 35 | 105 | 1607.80 (₹cr) | Standalone Revenue Q1FY27 | NOT_FOUND (no prior-year standalone comparator anywhere) |
| 36 | 105 | 336.35 (₹cr) | Standalone EBIDTA Q1FY27 | NOT_FOUND (no prior-year standalone comparator) |
| 37 | 106 | 240.12 (₹cr) | Standalone PBT Q1FY27 | NOT_FOUND (no prior-year standalone comparator) |
| 38 | 106 | 179.21 (₹cr) | Standalone PAT Q1FY27 | NOT_FOUND (no prior-year standalone comparator) |
| 39 | 122 | 28 million fkm | Optical Fiber capacity, prior | |
| 40 | 122 | 34 million fkm | Optical Fiber capacity, current | |
| 41 | 123 | 34 million fkm | Optical Fiber Cable capacity, prior | |
| 42 | 123 | 43 million fkm | Optical Fiber Cable capacity, current | |
| 43 | 148 | ~215 (₹cr) | Investment in AI data centre connectivity facility, restated in MD quote | REPEAT_NUMBER (=#13), APPROX_VALUE |

## TABLE 13 — Named Entities (5)

| # | Line | Entity | Relationship |
|---|------|--------|---------------|
| 1 | 18 | BSE Ltd. | Regulatory filing recipient (exchange) |
| 2 | 18 | National Stock Exchange of India Ltd. | Regulatory filing recipient (exchange) |
| 3 | 25-26 | Securities and Exchange Board of India (SEBI) | Regulator, cited for LODR Regulations 2015 basis |
| 4 | 168 | HTL Ltd. | Subsidiary — manufacturing facility, Chennai (defence equipment) |
| 5 | 177 | Kommune PR | External investor relations / media agency, media contact |

No prior-quarter ledger was supplied for this run, so `ENTITY_CHANGE` / `DROPPED_SLIDE` comparisons cannot be run; this is recorded as NOT_APPLICABLE (no baseline), not a mismatch.

---

## FLAGS RAISED (summary)
- `ZERO_STANDING` — 4 instances (Table 4 rows 4.4-4.7, Change column dash cells; Table 12 rows 25/28/31/34)
- `APPROX_VALUE` — 2 instances (₹~26,665 crore order book, Table 12 #3; ₹~215 crore investment restated in MD quote, Table 12 #43 and 9.3)
- `REPEAT_NUMBER` — 40% (headline/bullet, #1/#12), 85% (Q1FY27/Q4FY26 product-segment mix, #9/#11), ₹215 crore (bullet/MD quote, #13/#43) — all internally consistent, no discrepancy found between repeats
- `NOT_FOUND` — board meeting start/end time (Table 1.7); proposed Defence acquisition target/value (Table 8.2); Ammunition Manufacturing Complex capex/capacity/timeline (Table 8.3); standalone Q1FY26 comparators and standalone YoY% (Table 5.4, Table 12 #35-38)
- `NOT_APPLICABLE` — prior-quarter ledger not supplied; ENTITY_CHANGE/DROPPED_SLIDE checks cannot be run this cycle

## GATE A2: PASS
All eight reconciliation categories (currency figures, percent figures, key-highlight bullets, financial table rows, section headers, named entities, capacity figures, standalone-paragraph figures) matched grep count to manual sweep count 1:1 after re-anchoring three regexes that initially mismatched (financial_table_rows, section_headers, named_entities — each documented above with root cause). The master business-numbers cross-reference (Table 12) independently reconciles to 43, consistent with the sum of the category-level counts. No unresolved mismatch remains.
