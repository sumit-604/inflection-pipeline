# A2 ENUMERATION LEDGER — Balaji Amines Limited (BALAMINES), Q1 FY27, Press Release / Investor Release

Source: `extract_presentation_balamines_q1fy27.txt` (pressrelease_balamines_q1fy27.pdf, 5 pages, unit convention: Crores, x1)
Prior-quarter ledger: none (first coverage for this pipeline — no DROPPED_SLIDE check possible)
Doctype note: document is a press-release-style Investor Release, not a slide deck. "Slide" unit below = page.

```
=== A2 COUNT TEST ===
category: pages                    grep_count: 5    sweep_count: 5    match: yes
category: financial_highlights_cells grep_count: 48  sweep_count: 48   match: yes
category: segment_volumes          grep_count: 3    sweep_count: 3    match: yes
category: diluted_eps              grep_count: 2    sweep_count: 2    match: yes
category: mgmt_forward_statements  grep_count: 32   sweep_count: 32   match: yes  (see reconciliation note)
category: footnotes_disclaimers    grep_count: 2    sweep_count: 2    match: yes
category: other_identifiers        grep_count: 14   sweep_count: 14   match: yes
category: zero_standing_items      grep_count: 0    sweep_count: 0    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

**Reconciliation note on mgmt_forward_statements:** first-pass automated keyword grep
(`FY27|commission|expansion|DME|NMM|ACN|HCN|NaCN|EDTA|zero-debt|progressing as
planned|Mega Project|...`) on lines 61-180 returned 23 merged line-blocks — a mismatch
against an initial manual topical grouping of 25 claims. Re-swept: the keyword grep
missed the sentence at lines 136-138 (import-substitution/cyanide-chemistry rationale —
no exact keyword match) and over-merged the three-line headline (61-63, one metric per
line) into a single block. Resolution: re-ran both passes at **sentence-level**
granularity (period/semicolon boundaries, abbreviation-safe splitting of "Mr.", "D.",
"viz."), independently, over the same nine text spans (headline, performance-highlights
narrative, EBITDA/PAT/margin/EPS narrative, zero-debt line, New Projects section,
Balaji Speciality Chemicals section, execution-status section, MD attribution line, MD
quote paragraphs). Both passes converged on **32 discrete sentences/claims**. That is
the count used below. Table-cell figures (category 1) and segment-volume /diluted-EPS
figures (categories 2-3) are excluded from this count even where a sentence restates
them, to avoid double-counting across categories — cross-references are noted in the
flags column instead.

---

## 1. Key Financial Highlights table — one row per metric per column (line 73-82)

Header: line 73 "Particulars (₹ Cr.) | Standalone | Consolidated"; line 74 sub-header
"Q1FY27 | Q1FY26 | Q4FY26 | Q1FY27 | Q1FY26 | Q4FY26".

| # | Line | Metric | Book | Period | Value | Flags |
|---|------|--------|------|--------|-------|-------|
| 1 | 75 | Total Revenue (Rs. Cr) | Standalone | Q1FY27 | 429 | |
| 2 | 75 | Total Revenue (Rs. Cr) | Standalone | Q1FY26 | 327 | |
| 3 | 75 | Total Revenue (Rs. Cr) | Standalone | Q4FY26 | 370 | |
| 4 | 75 | Total Revenue (Rs. Cr) | Consolidated | Q1FY27 | 461 | cross-ref headline L61 |
| 5 | 75 | Total Revenue (Rs. Cr) | Consolidated | Q1FY26 | 367 | |
| 6 | 75 | Total Revenue (Rs. Cr) | Consolidated | Q4FY26 | 403 | cross-ref L88 |
| 7 | 76 | EBITDA (Rs. Cr) | Standalone | Q1FY27 | 110 | |
| 8 | 76 | EBITDA (Rs. Cr) | Standalone | Q1FY26 | 64 | |
| 9 | 76 | EBITDA (Rs. Cr) | Standalone | Q4FY26 | 94 | |
| 10 | 76 | EBITDA (Rs. Cr) | Consolidated | Q1FY27 | 121 | cross-ref headline L62, L102 |
| 11 | 76 | EBITDA (Rs. Cr) | Consolidated | Q1FY26 | 64 | note: identical to Standalone Q1FY26 (64) — coincidence, not an extraction error; verify at A3 |
| 12 | 76 | EBITDA (Rs. Cr) | Consolidated | Q4FY26 | 102 | cross-ref L102 |
| 13 | 77 | EBITDA Margin (%) | Standalone | Q1FY27 | 26% | |
| 14 | 77 | EBITDA Margin (%) | Standalone | Q1FY26 | 20% | |
| 15 | 77 | EBITDA Margin (%) | Standalone | Q4FY26 | 26% | |
| 16 | 77 | EBITDA Margin (%) | Consolidated | Q1FY27 | 26% | cross-ref L105 |
| 17 | 77 | EBITDA Margin (%) | Consolidated | Q1FY26 | 17% | cross-ref L105-106 |
| 18 | 77 | EBITDA Margin (%) | Consolidated | Q4FY26 | 25% | cross-ref L105 |
| 19 | 78 | PAT (Rs. Cr) | Standalone | Q1FY27 | 72 | |
| 20 | 78 | PAT (Rs. Cr) | Standalone | Q1FY26 | 40 | |
| 21 | 78 | PAT (Rs. Cr) | Standalone | Q4FY26 | 62 | |
| 22 | 78 | PAT (Rs. Cr) | Consolidated | Q1FY27 | 78 | cross-ref headline L63, L108 |
| 23 | 78 | PAT (Rs. Cr) | Consolidated | Q1FY26 | 37 | |
| 24 | 78 | PAT (Rs. Cr) | Consolidated | Q4FY26 | 65 | cross-ref L108 |
| 25 | 79 | PAT Margin (%) | Standalone | Q1FY27 | 17% | |
| 26 | 79 | PAT Margin (%) | Standalone | Q1FY26 | 12% | |
| 27 | 79 | PAT Margin (%) | Standalone | Q4FY26 | 17% | |
| 28 | 79 | PAT Margin (%) | Consolidated | Q1FY27 | 17% | |
| 29 | 79 | PAT Margin (%) | Consolidated | Q1FY26 | 10% | |
| 30 | 79 | PAT Margin (%) | Consolidated | Q4FY26 | 16% | |
| 31 | 80 | Cash PAT* (Rs. Cr) | Standalone | Q1FY27 | 89 | footnoted, see Footnote F1 |
| 32 | 80 | Cash PAT* (Rs. Cr) | Standalone | Q1FY26 | 53 | footnoted |
| 33 | 80 | Cash PAT* (Rs. Cr) | Standalone | Q4FY26 | 75 | footnoted |
| 34 | 80 | Cash PAT* (Rs. Cr) | Consolidated | Q1FY27 | 97 | footnoted |
| 35 | 80 | Cash PAT* (Rs. Cr) | Consolidated | Q1FY26 | 51 | footnoted |
| 36 | 80 | Cash PAT* (Rs. Cr) | Consolidated | Q4FY26 | 81 | footnoted |
| 37 | 81 | Cash PAT Margin (%) | Standalone | Q1FY27 | 21% | |
| 38 | 81 | Cash PAT Margin (%) | Standalone | Q1FY26 | 16% | |
| 39 | 81 | Cash PAT Margin (%) | Standalone | Q4FY26 | 20% | |
| 40 | 81 | Cash PAT Margin (%) | Consolidated | Q1FY27 | 20% | |
| 41 | 81 | Cash PAT Margin (%) | Consolidated | Q1FY26 | 14% | |
| 42 | 81 | Cash PAT Margin (%) | Consolidated | Q4FY26 | 20% | |
| 43 | 82 | Sales Volume (in MT) | Standalone | Q1FY27 | 20,619 | no segment split disclosed for standalone |
| 44 | 82 | Sales Volume (in MT) | Standalone | Q1FY26 | 24,847 | |
| 45 | 82 | Sales Volume (in MT) | Standalone | Q4FY26 | 25,394 | |
| 46 | 82 | Sales Volume (in MT) | Consolidated | Q1FY27 | 21,587 | cross-ref L93; segment sum (see §2) ties out |
| 47 | 82 | Sales Volume (in MT) | Consolidated | Q1FY26 | 27,570 | cross-ref L93 |
| 48 | 82 | Sales Volume (in MT) | Consolidated | Q4FY26 | 27,341 | |

No zero/nil/dash values present in this table in any period/column — `ZERO_STANDING` count = 0 for this table.

---

## 2. Segment volume breakdown — Q1FY27 (line 97-100)

| # | Line | Segment | Value | Flags |
|---|------|---------|-------|-------|
| 1 | 98 | Amines volumes | 6,248.57 MT | |
| 2 | 99 | Amines Derivatives volumes | 8,205.11 MT | |
| 3 | 100 | Specialty Chemicals volumes | 7,132.92 MT | |

Sum check: 6,248.57 + 8,205.11 + 7,132.92 = 21,586.60 MT ≈ 21,587 MT — ties to the
Consolidated Sales Volume Q1FY27 cell (row 46 above) and to the L93 narrative restatement,
not to the Standalone figure (20,619 MT, row 43). The source text does not itself label
this breakdown "Consolidated" — `SCOPE_INFERRED` (basis inferred from the arithmetic
tie-out; A3/A4 should confirm against the standalone segment split, which this release
does not disclose — `NOT_DISCLOSED`).

---

## 3. Diluted EPS figures (line 108-109)

| # | Line | Metric | Period | Value | Flags |
|---|------|--------|--------|-------|-------|
| 1 | 108-109 | Diluted EPS | Q1FY27 | ₹ 23.13 per equity share | basis (standalone/consolidated) not stated in text; immediately follows Consolidated PAT sentence — `SCOPE_AMBIGUOUS` |
| 2 | 109 | Diluted EPS | Q4FY26 | ₹ 19.99 per equity share | same scope ambiguity |

No Q1FY26 diluted EPS given — only a sequential (Q4FY26) comparison is disclosed, unlike
every other headline metric in this release which gets both YoY and QoQ comparisons.
`NOT_DISCLOSED` / `PARTIAL_COMPARISON`.

---

## 4. Management / forward statements and project-update claims (32 sentences, lines 61-180)

Named items called out in the task brief are marked in the **Named-item** column.

| # | Line(s) | Type | First ~15 words | Named-item | Flags |
|---|---------|------|------------------|------------|-------|
| 1 | 61 | FINANCIAL_RESTATEMENT (headline) | "Consolidated Q1FY27 Revenue stood at ₹ 461 Crore;" | | cross-ref table row 4 |
| 2 | 62 | FINANCIAL_RESTATEMENT (headline) | "EBITDA stood at ₹ 121 Crore;" | | cross-ref table row 10 |
| 3 | 63 | FINANCIAL_RESTATEMENT (headline) | "Net Profit stood at ₹ 78 Crore" | | cross-ref table row 22 |
| 4 | 88 | FINANCIAL_RESTATEMENT | "Revenue from Operations for Q1FY27 stood at ₹ 461 crore, as compared to ₹ 403 crore in Q4FY26, indicating stable operational performance" | | qualitative gloss "stable operational performance" attached to a sequential (not YoY) comparison |
| 5 | 89-91 | MGMT_CLAIM | "Volumes were maintained at similar levels last year, supported by stable commodity prices and consistent demand..." | | `NARRATIVE_VS_DATA_CHECK`: consolidated volume fell from 27,570 MT (Q1FY26) to 21,587 MT (Q1FY27), a 21.7% YoY decline (table rows 46/47); standalone volume fell 17.0% YoY (rows 43/44). "Maintained at similar levels" merits A3/A4 review against these figures. |
| 6 | 93 | FINANCIAL_RESTATEMENT | "Total volumes stood at 21,587 MT for Q1 FY27 as against 27,570 MT in Q1 FY26" | | cross-ref table rows 46/47; same volume figures as flag in row 5 above |
| 7 | 102-103 | FINANCIAL_RESTATEMENT | "EBITDA for Q1FY27 was ₹ 121 crore, as compared to ₹ 102 crore in Q4FY26 and ₹ 64 crore in Q1FY26" | | |
| 8 | 105-106 | FINANCIAL_RESTATEMENT | "EBITDA margin for Q1FY27 stood at 26%, as against 25% in Q4FY26 and 17% in Q1FY26" | | |
| 9 | 108 | FINANCIAL_RESTATEMENT | "PAT for Q1FY27 was ₹ 78 crore as compared to ₹ 65 crore in Q4FY26" | | |
| 10 | 108-109 | FINANCIAL_RESTATEMENT | "Diluted EPS for Q1FY27 stood at ₹ 23.13 per equity share as against ₹ 19.99 in Q4FY26" | | cross-ref §3 |
| 11 | 111 | MGMT_CLAIM | "On a standalone basis, we are a zero-debt company" | zero-debt standalone | no supporting balance-sheet figures (debt/cash) in this release — assertion only, `NOT_DISCLOSED` (supporting figures) |
| 12 | 115-117 | PROJECT_UPDATE | "Following the successful commissioning of its 100,000 TPA Dimethyl Ether (DME) plant - India's first commercial-scale DME manufacturing facility..." | DME 100,000 TPA commissioning | |
| 13 | 118-120 | PROJECT_UPDATE | "The DME plant marks the Company's strategic entry into alternate fuel applications, catering to LPG blending and aerosol propellant markets..." | DME 100,000 TPA commissioning | |
| 14 | 122-124 | FORWARD_GUIDANCE | "The Company's next phase of expansion includes the commissioning of N-Methyl Morpholine (NMM) and the Acetonitrile (ACN) capacity expansion during FY27..." | NMM, ACN | timeline: "during FY27" — no month/quarter granularity |
| 15 | 128-130 | PROJECT_UPDATE | "Balaji Speciality Chemicals Limited continues to advance its ₹750 crore phased expansion programme, which has been accorded Mega Project Status..." | Balaji Speciality Chemicals Rs 750 cr phased expansion | Mega Project Status under Maharashtra PSI 2019 cited but no incentive quantum disclosed — `NOT_DISCLOSED` |
| 16 | 131-134 | PROJECT_UPDATE | "The expansion is aimed at establishing an integrated specialty chemicals platform with the manufacture of high-value products including Hydrogen Cyanide (HCN)..." | Balaji Speciality Chemicals — product scope (HCN, NaCN, EDTA, EDTA-2Na, DETA, TETA, PIP, AEEA, AEP) | |
| 17 | 136-138 | MGMT_CLAIM | "The project represents a significant step in building indigenous capabilities in cyanide chemistry, enabling domestic production of critical intermediates..." | | import-substitution rationale (pharma, agrochemical, mining end-markets) — the sentence the first-pass keyword grep missed (see reconciliation note) |
| 18 | 142 | FORWARD_GUIDANCE | "Execution of the expansion is progressing as planned" | | no % completion or capex-spent-to-date disclosed — `NOT_DISCLOSED` |
| 19 | 144-145 | FORWARD_GUIDANCE | "a) The brownfield Unit-I expansion for EDA-based downstream products is expected to be commissioned during FY27" | Unit-I brownfield FY27 | |
| 20 | 147-148 | FORWARD_GUIDANCE | "b) The greenfield Unit-II facility at MIDC Chincholi is under execution, with plants for HCN, NaCN, EDTA and EDTA-2Na targeted for commissioning during FY27" | Unit-II greenfield MIDC Chincholi HCN/NaCN/EDTA FY27 | |
| 21 | 150 | ATTRIBUTION | "On the performance, Mr. D. Ram Reddy, Managing Director, commented, [NS1]" | | `DOC_ARTIFACT`: stray editorial/tracked-change marker "[NS1]" left inline in a filed, digitally-signed public disclosure — proofing lapse, worth flagging upstream |
| 22 | 152-154 | MD_QUOTE | "We have commenced FY27 on a strong note, delivering healthy operational and financial performance supported by improved demand..." | | |
| 23 | 154-156 | MD_QUOTE | "Our diversified product portfolio, integrated manufacturing capabilities and strong customer relationships enabled us to effectively capitalize on operational efficiencies" | | |
| 24 | 156-157 | MD_QUOTE | "This has been the leveraging point with improving market conditions while maintaining sustainable performance in the adverse scenarios of West Asia's crisis" | | only reference to geopolitical/macro risk in the document; not quantified |
| 25 | 159-161 | MD_QUOTE | "During the quarter, we achieved a significant milestone with the successful commissioning of India's first commercial-scale 100,000 TPA Dimethyl Ether (DME) plant" | DME 100,000 TPA commissioning (restated) | duplicate of claim #12 |
| 26 | 160-163 | MD_QUOTE | "This marks an important milestone in BAL's strategic vision to diversify into new-age chemicals and alternate fuel applications, while reinforcing our commitment towards import substitution..." | | |
| 27 | 165-167 | MD_QUOTE | "We continue to make steady progress on our growth pipeline with the Expansion Projects viz N-Methyl Morpholine (NMM), Acetonitrile (ACN) projects" | NMM, ACN (restated) | duplicate of claim #14; "steady progress" not quantified |
| 28 | 166-168 | MD_QUOTE | "Further, the expansion plans of Balaji Speciality Chemicals Limited are progressing as planned and are expected to further strengthen our group's product portfolio..." | Balaji Speciality Chemicals (restated) | duplicate of claim #15/#18 |
| 29 | 170-172 | MD_QUOTE | "Our integrated manufacturing platform continues to be a key competitive advantage, providing operational flexibility, supply chain reliability and cost efficiencies..." | | |
| 30 | 172-175 | MD_QUOTE / FORWARD_GUIDANCE | "At the same time, we remain focused on expanding our presence in high-value specialty chemicals and electronic-grade products, positioning the Company to benefit from structural growth opportunities in pharmaceuticals, agrochemicals, alternate fuels and the evolving EV battery chemicals ecosystem" | | new claims not elsewhere in the document: "electronic-grade products" and "EV battery chemicals ecosystem" — no product/project/capex specifics attached; `NOT_DISCLOSED` (detail) |
| 31 | 177 | MD_QUOTE / FORWARD_GUIDANCE | "Looking ahead, we remain confident in our growth outlook" | | |
| 32 | 177-180 | MD_QUOTE / FORWARD_GUIDANCE | "Backed by a healthy order pipeline, improving demand environment, ongoing capacity additions and a disciplined approach to execution..." | | "healthy order pipeline" asserted, not quantified anywhere in the release — `NOT_DISCLOSED` |

Note: claims #25/#12, #27/#14, and #28/#15 are deliberate near-duplicates (MD quote
restates the business-update section). Both instances are ledgered separately per the
"enumerate everything" rule; A3/A4 should treat them as one underlying disclosure with
two occurrences, not two independent claims.

---

## 5. Footnotes / disclaimers

| # | Line | Item | Text (verbatim or full) | Flags |
|---|------|------|--------------------------|-------|
| F1 | 84 | Cash PAT definition footnote | "*Cash PAT is PAT + Depreciation + Deferred tax" | qualifies all 12 Cash PAT / Cash PAT Margin cells in §1 (rows 31-42); non-standard/company-defined metric, no reconciliation to cash flow statement provided in this release |
| F2 | 208-216 | Safe Harbor Statement | "Statements in this document relating to future status, events, or circumstances... The company assumes no obligation to update forward-looking statements to reflect actual results, changed assumptions or other factors." | standard boilerplate; qualifies all FORWARD_GUIDANCE / PROJECT_UPDATE rows in §4 (items 14, 15, 18, 19, 20, 30, 31, 32 in particular) |

---

## 6. Page-level index (5 pages, first coverage — no prior deck to diff for DROPPED_SLIDE)

| Page | Lines | Title / Section | Content type |
|------|-------|------------------|--------------|
| 1 | 15-56 | Covering letter to BSE/NSE (Reg. 30 filing transmittal), digitally signed | text |
| 2 | 57-94 | Investor Release masthead + headline figures + Key Financial Highlights table + Consolidated Performance Highlights narrative | text + table |
| 3 | 95-138 | Segment volume breakdown, EBITDA/PAT/margin/EPS commentary, zero-debt line, New Projects update (DME/NMM/ACN), Balaji Speciality Chemicals expansion | text |
| 4 | 140-187 | Execution status (Unit-I/Unit-II), MD quote (D. Ram Reddy), About BAL (opening) | text |
| 5 | 188-233 | About BAL (continued), Safe Harbor Statement, Company/IR Advisor contact block | text |

---

## 7. Other page identifiers / administrative facts (supplementary — base-rule "every number on every page")

| # | Line(s) | Item | Value | Flags |
|---|---------|------|-------|-------|
| 1 | 17 | Letter date | 27th July, 2026 | |
| 2 | 26 | BSE Scrip Code | 530999 | |
| 3 | 26 | NSE Symbol | BALAMINES | |
| 4 | 30-31, 35 | Quarter ended (regulatory filing reference) | 30th June, 2026 (= Q1FY27) | |
| 5 | 33 | Regulatory basis cited | Regulation 30, SEBI (LODR) Regulations, 2015 | |
| 6 | 47-53 | Digital signature block | Abhijeet Kothadiya, Company Secretary & Compliance Officer; signed 2026.07.27 19:16:57 +05'30' | signature timestamp (27 Jul, 19:16:57) is the day after the press-release dateline (27 Jul) is same-day — consistent, no timing flag |
| 7 | 65 | Press-release dateline | Solapur, July 27, 2026 | |
| 8 | 185 | Company founding year | 1988 | |
| 9 | 192 | MMA manufacturing commencement year | 1990 | |
| 10 | 198-199 | Manufacturing footprint | four sites — three near Solapur, one near Hyderabad | |
| 11 | 203 | Ancillary business | 5-star hotel in Solapur (Balaji Sarovar), managed via Sarovar Group tie-up | out-of-segment business, not reflected in the segment volume breakdown (§2) — informational only |
| 12 | 226 | CIN | L24132MH1988PLC049387 | |
| 13 | 228-229 | IR Advisor contact 1 | Nikunj Seth, MUFG Intime India Pvt Ltd, +91 9773397958 | |
| 14 | 231-232 | IR Advisor contact 2 | Sakshi Mehta, MUFG Intime India Pvt Ltd, +91 9833212052 | |

---

## Flags summary

- `DOC_ARTIFACT` — line 150, stray "[NS1]" tracked-change/comment marker left inline in the filed, signed press release.
- `NARRATIVE_VS_DATA_CHECK` — lines 89-91 / 93, "volumes maintained at similar levels last year" narrative versus a disclosed 21.7% YoY consolidated volume decline (27,570 MT to 21,587 MT) and 17.0% standalone decline (24,847 MT to 20,619 MT).
- `SCOPE_INFERRED` — segment volume breakdown (§2, lines 98-100) is not explicitly labeled Standalone or Consolidated; inferred Consolidated by arithmetic tie-out to line 82/93.
- `SCOPE_AMBIGUOUS` — Diluted EPS (§3, lines 108-109) basis (standalone vs consolidated) not stated.
- `NOT_DISCLOSED` — multiple instances: standalone segment volume split, zero-debt supporting balance-sheet figures, PSI 2019 incentive quantum, % completion / capex-spent on BSC expansion, order-pipeline quantification, EV battery chemicals / electronic-grade products project specifics, Q1FY26 diluted EPS comparator.
- `ZERO_STANDING` — none found in this document; all disclosed line items carry non-zero values across all periods.
- `ENTITY_CHANGE` — not applicable (no consolidation entity list in this doctype).
- `MGMT_ABSENCE` — not applicable (press release, not a concall transcript).
- `DROPPED_SLIDE` — not applicable, no prior-quarter ledger provided (first coverage).
