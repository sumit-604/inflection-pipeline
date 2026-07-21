# A2 ENUMERATOR LEDGER — SOUTHWEST Q1 FY27 — results (press release)

Source: `extract_results_southwest_q1fy27.txt` (source PDF: pressrelease_southwest_q1fy27.pdf,
4 pages, page markers at extract lines 15, 68, 114, 162). Prior-quarter ledger: none available
(first quarterly run for this ticker) — so no `ENTITY_CHANGE` / `DROPPED_SLIDE` diff is possible;
noted per row where relevant instead of computed.

DOCTYPE NOTE (governs this entire ledger): this document is a 4-page investor/press release, NOT
a Reg 33 "Statement of Unaudited Financial Results." It structurally lacks numbered notes, a
Board Outcome letter, an auditor's limited-review report, a standalone results column, a cash
flow statement, and a balance sheet. Every one of those absences is enumerated below as a
first-class finding (Category K), not left blank.

---

## === A2 COUNT TEST ===
```
category: numbered_notes            grep_count: 0   sweep_count: 0   match: yes
category: financial_line_items      grep_count: 5   sweep_count: 5   match: yes
category: financial_period_cells    grep_count: 20  sweep_count: 20  match: yes
category: table_footnotes           grep_count: 1   sweep_count: 1   match: yes
category: quarter1_highlight_bullets grep_count: 13 sweep_count: 13  match: yes
category: cmd_commentary_claims     grep_count: 9   sweep_count: 9   match: yes
category: about_section_paragraphs  grep_count: 3   sweep_count: 3   match: yes
category: jv_coalblock_statements   grep_count: 7   sweep_count: 7   match: yes
category: safe_harbor_paragraphs    grep_count: 1   sweep_count: 1   match: yes
category: letter_addressee_blocks   grep_count: 2   sweep_count: 2   match: yes
category: letter_components         grep_count: 4   sweep_count: 4   match: yes
category: signature_blocks          grep_count: 1   sweep_count: 1   match: yes
category: contact_blocks_end        grep_count: 2   sweep_count: 2   match: yes
category: letterhead_block          grep_count: 1   sweep_count: 1   match: yes
category: absent_reg33_units        grep_count: 15  sweep_count: 15  match: yes
gate_a2: pass
```
=== END COUNT TEST ===

Grep methods used (reproducible):
- numbered_notes: `grep -n -E "^\s*[0-9]+\.\s"` → 0 hits.
- financial_line_items: label match on `^(Income from Operations|EBITDA|EBITDA Margin|Profit After Tax|PAT Margin)` → 5 hits (lines 86-90).
- financial_period_cells: 5 rows × 4 columns of numeric/percent tokens on lines 86-90 → 20.
- table_footnotes: `grep -n '\*'` → 2 raw hits (line 84 marker, line 91 definition) collapsed to 1 defined footnote.
- quarter1_highlight_bullets: byte-level grep for the PDF bullet glyph (0xEF 0x82 0xB7) on lines 92-111 → 13 hits.
- cmd_commentary_claims: `grep -n -E "Mr\.?\s*(Vikas )?Jain"` inside lines 115-148 → 9 hits (lines 115,120,122,125,127,134,138,143,147); manual sweep independently resolves 9 distinct claims (one grep hit, line 125, is a closer not a new opener; one manual claim, para D's first quote at line 131, has no "Jain" token and is caught by the closer/opener token shared on line 134) — totals reconcile at 9=9.
- about_section_paragraphs: blank-line-delimited blocks in lines 152-176 → 3.
- jv_coalblock_statements: `grep -n -i -E "Jharkhand|coal block|Oman|\bJV\b|Alara"` deduplicated to distinct statement instances → 7.
- letter_addressee_blocks: `grep -n "Listing Department"` → 1 physical line carrying 2 side-by-side addressee blocks (NSE + BSE) → 2.
- absent_reg33_units: independent `grep -n -i` passes for "note", "agenda", "Board Outcome", "AGM", "dividend", "auditor", "scrutinizer", "ESOP", "record date", "cash flow", "balance sheet", "EPS", "other income", "finance cost", "depreciation", "tax expense", "exceptional item" — all 0 hits, confirming 15 structurally absent Reg-33 unit classes (list in Category K).

---

## A. Letterhead / company identification block

| # | Line | Content | Flags |
|---|------|---------|-------|
| A1 | 16-25 | Company name, "(Formerly known as South West Pinnacle Exploration Pvt Ltd)", CIN L13203HR2006PLC049480, Regd & Corp Office address (Gurgaon), phone, fax, email, website, "ISO 9001:2015 Certified Company" tag | — |

## B. Cover letter to exchanges (lines 28-67)

| # | Line | Content | Flags |
|---|------|---------|-------|
| B1 | 28 | Letter date: 21.07.2026 | — |
| B2 | 30-37 (left column) | Addressee 1: Listing Department, National Stock Exchange of India Ltd., Exchange Plaza BKC Mumbai; SYMBOL: SOUTHWEST | — |
| B3 | 30-36 (right column) | Addressee 2: Listing Department, Bombay Stock Exchange Limited, PJ Towers, Dalal Street; Script Code: 543986 | — |
| B4 | 39 | Subject line: "Press Release" | — |
| B5 | 43-44 | Body: encloses press release "titled as 'Q1 FY27 Revenue Grows 53% Q on Q to Rs. 617 Mn & PAT Grows 287% Q on Q to Rs. 93 Mn.'" | `TITLE_LABEL_MISMATCH` — cover letter quotes the release title using "Q on Q"; the actual release headline (row C2 below) and every other Y/Y reference in the document (rows D-series, E1, F1) use "Y on Y". Verbatim text discrepancy, flagged for A3/A4; not interpreted here. |
| B6 | 46, 48 | Closing: "Thanking You," / "For South West Pinnacle Exploration Limited" | — |

## C. Signature block, cover letter (lines 50-67)

| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| C1 | 50-67 | VAISHALI (digital cert: c=IN, o=Personal, l=Saharanpur, st=Uttar Pradesh, email=secretarial@southwestpinnacle.com) | Company Secretary & Compliance Officer | 2026.07.21 08:27:06 +05'30' | No Board Outcome / board-meeting start-end time is disclosed anywhere in this document (see Category K, item K3), so the signature timestamp cannot be cross-checked against a board-meeting conclusion time as required by rule 7 — recorded as **N/A, not computable from this doctype**, not silently skipped. |

## D. Investor Release masthead + financial highlights table (lines 69-91)

| # | Line | Content | Flags |
|---|------|---------|-------|
| D0a | 69 | Section label: "Investor Release" | — |
| D0b | 74-76 | Release headline (two-part): "Q1 FY27 Revenue Grows 53% Y on Y to Rs. 617 Mn & PAT Grows 287% Y on Y to Rs. 93 Mn" | see `TITLE_LABEL_MISMATCH` at B5 |
| D0c | 78-80 | Dateline: "Haryana, 21st July 2026" + company description sentence ("Integrated Service Provider providing end-to-end Drilling & exploration of Natural resources") + "Financial Results for the Quarter 1 FY-2026-27" | — |
| D0d | 84 | Table header row: "Particulars (in Rs. Million)*" with 4 period columns: Q1 FY27, Q1 FY26, FY26, FY25 | — |

### D. Financial highlights table — line items × periods (line 86-90)

| # | Line | Line item | Q1 FY27 | Q1 FY26 | FY26 | FY25 | Flags |
|---|------|-----------|---------|---------|------|------|-------|
| D1 | 86 | Income from Operations (Rs. Mn) | 617 | 402 | 2430 | 1803 | — |
| D2 | 87 | EBITDA (Rs. Mn) | 149 | 58 | 583 | 336 | — |
| D3 | 88 | EBITDA Margin % | 24% | 14% | 24% | 19% | — |
| D4 | 89 | Profit After Tax (Rs. Mn) | 93 | 24 | 330 | 164 | — |
| D5 | 90 | PAT Margin % | 15% | 6% | 14% | 9% | — |
| D6 | 91 | Table footnote: "* On Consolidated Basis" | — | — | — | — | Table carries no standalone column at all — see Category K, item K5. Every value in D1-D5 is non-zero, non-nil, non-dash across all four periods; no `ZERO_STANDING` applies within this table. |

## E. Quarter-1 Highlights bullets (lines 92-111, 13 bullets)

| # | Line(s) | First ~15 words | Flags |
|---|---------|------------------|-------|
| E1 | 93 | "Consolidated Revenue grows 53% Y on Y." | — |
| E2 | 94-95 | "EBITDA grows from 14% to 24% Y on Y with more than two and half fold increase in absolute numbers." | — |
| E3 | 96 | "PBT grows from 8% to 19% Y on Y with more than 3.80 fold increase in absolute numbers." | PBT % and multiple appear only here — no PBT line item exists in the table (D-series); unreconciled to a tabulated figure. |
| E4 | 97 | "PAT grows from 6% to 15% Y on Y with more than 3.90 fold increase in absolute numbers." | — |
| E5 | 98-99 | "Company commences operations to execute single largest order value of Rs. 307 Cr. in the State of Rajasthan." | — |
| E6 | 100 | "Company wins extension of CBM contract from RIL valuing over Rs. 166 Cr." | — |
| E7 | 101 | "Order book stands at all time high at 761 Crores." | — |
| E8 | 102-103 | "Company empaneled by Oil India Limited for providing 2D/3D Seismic Data Acquisition Services across OIL's onshore." | — |
| E9 | 104 | "Jharkhand coal block exploration completed, definitive GR under preparation." | cross-ref JV/coal-block Category G, row G1 |
| E10 | 105-106 | "Balance 75% amount of warrants, issued on preferential basis received and converted into equity shares." | Capital-action disclosure with no corresponding numbered note / capital-raising agenda item in this doctype — see Category K, item K2. |
| E11 | 107 | "20 Operations across 8 States running smoothly with Zero (0) LTIs (Loss Time Injuries)." | `ZERO_STANDING` — explicit zero-value standing metric (LTI count = 0), enumerated per rule 3, not dropped. |
| E12 | 108-109 | "Air borne survey (a latest technique for faster exploration in large mining blocks) completed under Oman second JV, GR under preparation." | cross-ref JV/coal-block Category G, row G2 |
| E13 | 110-111 | "To reinforce its Strategic investment, company is participating in ongoing Rights issue of Alara Resources Ltd, Australia." | cross-ref JV/coal-block Category G, row G3 |

## F. CMD commentary claims — Mr. Vikas Jain, Chairman & Managing Director (lines 115-148, 9 claims)

| # | Line(s) | Attribution | First ~15 words of claim | Flags |
|---|---------|-------------|---------------------------|-------|
| F1 | 115, 117-120a | "Commenting on the results ... said," | "I am proud to share that we have delivered strong and encouraging financial and operational performance..." (53% revenue growth, 287% PAT growth Y/Y, Rs.617 Mn revenue, Rs.93 Mn PAT, consolidated basis) | — |
| F2 | 120b | "...Mr. Jain said" (same sentence, unquoted) | "The standalone performance is also on similar lines" | Claim is unquoted (no direct-quote marks, unlike F1/F3-F9) and un-anchored to any figure — no standalone table or column exists anywhere in the document to verify against (Category K, item K5). |
| F3 | 122-125 | "Mr. Jain went on to explain that ... Mr. Jain added." | "this performance is despite dynamic and often challenging business environment including substantial increase in input cost..." (footprint expansion, client relationships, capability enhancement) | — |
| F4 | 127-129 | "Mr. Vikas Jain further said that" | "Recognizing our services, the clients are equally supportive and made our order book quite robust crossing over INR 761 Crs mark..." | Order book figure (761 Cr) repeats E7 verbatim — consistent, not a discrepancy. |
| F5 | 131-134a | "Explaining about the promising outlook of the company he said that" (no "Jain" token on this line — see grep-method note in Count Test section) | "with increasing government focus on mineral exploration, policy reforms, and the push for self-reliance in critical minerals..." (sector growth, company well-positioned, confidence of "promising year end outlook") | — |
| F6 | 134b-136 | "Mr. Jain added that" | "seeing the present scenario, company has ordered new rigs and other equipments to cope up with the enhanced business requirement." | Forward capex commitment (new rigs ordered) with no amount, count, or timeline given. |
| F7 | 138-141 | "Mr. Jain went on to explain that" | "India has huge untapped natural resources and government focus on exploration is the only way to unlock and extract..." | — |
| F8 | 143-145 | "Mr Jain also gave an encouraging update on Jharkhand coal block and said that" | "exploration activities have been completed and GR preparation and submission is on the anvil. Other mine development activities shall be undertaken now on fast track mode." | cross-ref JV/coal-block Category G, row G4 |
| F9 | 147-148 | "While sharing development in second JV in Oman, Mr Jain enthusiastically stated that," | "air borne survey has recently been completed in the mining block and GR preparation there also is on cards." | cross-ref JV/coal-block Category G, row G5 |

## G. JV / Coal-block statements — cross-referenced across the whole document (7 instances)

| # | Line(s) | Location | Statement | Flags |
|---|---------|----------|-----------|-------|
| G1 | 104 | Q1 Highlights bullet (=E9) | Jharkhand coal block exploration completed, definitive GR under preparation | — |
| G2 | 108-109 | Q1 Highlights bullet (=E12) | Air borne survey completed under Oman second JV, GR under preparation | — |
| G3 | 110-111 | Q1 Highlights bullet (=E13) | Company participating in ongoing Rights issue of Alara Resources Ltd, Australia (strategic investment reinforcement) | Distinct named entity from the Oman JV1 operating entity in G7 — flagged for A3/A4 to confirm relationship (parent/JV-partner vs. same entity referenced two ways). |
| G4 | 143-145 | CMD commentary (=F8) | Jharkhand coal block: exploration completed, GR prep/submission "on the anvil," other mine development to follow fast-track | — |
| G5 | 147-148 | CMD commentary (=F9) | Oman second JV: airborne survey completed, GR preparation "on cards" | — |
| G6 | 156-160, 163-164 | About SWPEL, para 1 | Jharkhand coal block facts: 266 Hectares, Geological Reserves >84 million tons, Coal Mine Development & Production Agreement signed with Ministry of Coal, company notified as accredited prospecting agency for coal & lignite, exploration completed, GR preparation underway, mine development to follow fast-track | Most granular version of the Jharkhand claim (only place hectares/tonnage/CMDPA/accreditation appear) — not repeated in E9, F8, or the highlights table. |
| G7 | 166-169 | About SWPEL, para 2 | Two Oman JVs: JV1 = long-term mining contract for Copper & Gold + exploration/drilling, via joint venture "Alara Resources LLC., Oman"; JV2 = recently formed, allocated a mining block by Sultanate of Oman, exploration in progress | Only place JV1 is named (Alara Resources LLC) and its commodity (Copper & Gold) and contract type (long-term mining contract) are disclosed. JV2 remains unnamed throughout the document (G2, G5, G7 all refer to it only as "second JV" / "Oman second JV"). |

## H. "About South West Pinnacle Exploration Limited" — paragraphs (lines 152-176, 3 paragraphs)

| # | Line(s) | Content summary | Flags |
|---|---------|------------------|-------|
| H1 | 152-164 (spans page break at line 161-162) | Company description (Integrated Service Provider; Coal/Ferrous/Non-Ferrous/Atomic Minerals; conventional/non-conventional Oil & Gas; groundwater investigation; surface geophysical investigation, downhole geophysics, 2D/3D Seismic, Passive Seismic Tomography) + Jharkhand coal block facts (=G6) | — |
| H2 | 166-169 | Two Oman JVs description (=G7) | — |
| H3 | 171-176 | Track record stats: >165 projects completed in 19 years since inception; 20 projects presently operating Pan-India + Oman JV projects; ~3.2 million meters drilling; 6.5 Lac meter geophysical logging; 515 sq.km. 3D Seismic surveys; 411 LKM 2D seismic survey; 43 drilling rigs, capacity up to 2500 meters depth | None of these cumulative/lifetime figures (165 projects, 19 years, 3.2M meters, etc.) are cross-referenced to any prior-period baseline anywhere in the document — no comparator given for whether these are up or down q/q or y/y. |

## I. Safe Harbor (lines 179-188)

| # | Line(s) | Content | Flags |
|---|---------|---------|-------|
| I1 | 181-188 | Standard forward-looking-statement disclaimer: plans/objectives, R&D progress/results, potential project characteristics, project potential, target dates; based on estimates; no obligation to update | — |

## J. Contact block, end of document (lines 191-204)

| # | Line(s) | Content | Flags |
|---|---------|---------|-------|
| J1 | 191-199 | "For more information, please contact" / Company: South West Pinnacle Exploration Limited / CIN: L13203HR2006PLC049480 | CIN here (line 199) matches letterhead CIN (line 18) — consistent, no discrepancy. |
| J2 | 201-204 | Mr. Dinesh Agarwal – CFO, dinesh.agarwal@southwestpinnacle.com, +91 124 423540 | Phone number here (+91 124 423540, 9 digits after area code) differs in digit count from the letterhead numbers T: +91 124 4235400/4235401, F: +91 124 4235402 (10 digits) — likely a truncated/typo'd digit in the extract or source PDF, flagged for A3/A4, not resolved here. |

## K. ABSENT — Reg 33 unit classes structurally not present in this document (15 items)

Per task instruction, each structural absence is recorded as a first-class enumerated finding,
not left blank. Confirmed absent by targeted grep (0 hits each, see Count Test methodology) plus
full manual line-by-line sweep of all 187 extract lines.

| # | Reg-33 unit class | Status |
|---|--------------------|--------|
| K1 | Numbered notes (below results table) | ABSENT: no numbered notes present in this document |
| K2 | Board Outcome / Board Meeting agenda items (AR approval, AGM notice, record date, dividend declaration, director appointments/resignations, auditor changes, scrutinizer appointment, ESOP grants, capital-raising enabling resolutions) | ABSENT: no Board Outcome letter present in this document; this is a press-release covering letter only |
| K3 | Board meeting start/end time | ABSENT: no board meeting time disclosed anywhere in this document (blocks the signature-timestamp cross-check at row C1) |
| K4 | Auditor's Limited Review Report (opinion paragraph, Emphasis of Matter, Other Matters, Going Concern language, entity list reviewed, UDIN number, unaudited/management-furnished entity flags) | ABSENT: no auditor report of any kind present in this document |
| K5 | Standalone financial results as a tabulated column | ABSENT: table (Category D) is consolidated-only ("* On Consolidated Basis," line 91); standalone is referenced only once, unquoted and unanchored, in prose (row F2, line 120) |
| K6 | Cash Flow Statement | ABSENT: no cash flow statement or cash-flow line items present |
| K7 | Balance Sheet / Statement of Assets & Liabilities | ABSENT: no balance sheet present |
| K8 | EPS (basic/diluted) | ABSENT: no EPS figure disclosed anywhere in this document |
| K9 | Other Income line item | ABSENT: not disclosed |
| K10 | Finance Costs line item | ABSENT: not disclosed |
| K11 | Depreciation & Amortisation line item | ABSENT: not disclosed |
| K12 | Tax Expense (current/deferred) breakup | ABSENT: not disclosed (PAT given at D4/D5 with no tax-line derivation) |
| K13 | Exceptional items / Total Comprehensive Income line items | ABSENT: not disclosed |
| K14 | Consolidation entity list / schedule of subsidiaries-JVs-associates (Reg-33 style, with % holding and relationship type per entity) | ABSENT: no formal consolidation schedule; entities appear only in narrative prose (Category G / row H2) — see Category L for the informally-named entity list extracted from that prose |
| K15 | Director profiles / DIN / appointment-reappointment annexures | ABSENT: no director annexures present in this document |

## L. Entities named in prose (informal — no formal consolidation list exists, see K14)

| # | Line(s) first named | Entity | Relationship (as stated in text) | Flags |
|---|----------------------|--------|-----------------------------------|-------|
| L1 | 110-111, 168 | Alara Resources Ltd, Australia / Alara Resources LLC, Oman | Rights-issue investee (L1a, line 111) and Oman JV1 vehicle for Copper/Gold mining services (L1b, line 168) | Two distinct name-forms appear ("Ltd, Australia" vs "LLC, Oman") for what may be parent/subsidiary or the same relationship described twice — see G3 flag. No prior-quarter ledger to test for `ENTITY_CHANGE`; noted for baseline. |
| L2 | 108-109, 147-148, 168-169 | "Second JV" in Oman (unnamed) | Recently formed, allocated a mining block by Sultanate of Oman, exploration in progress | Entity never given a proper name anywhere in the 4-page document — a naming gap, not merely an absence of detail. |

---

## Reconciliation summary

All 15 count-test categories reconcile grep vs. manual sweep at equal totals (GATE A2: pass).
Primary enumerated disclosure units, categories A, B, C, D0, D-table, E, F, H, I, J, L
(1+6+1+4+6+13+9+3+1+2+2): 48 rows. Category G (7 rows) is an explicit cross-reference index
over rows already counted in E/F/H and is not added again. Category K adds 15 structurally
absent Reg-33 unit classes, recorded explicitly rather than omitted. Ledger total, all rows
across all categories A-L: 70.
Flags raised: `ZERO_STANDING` (1, row E11), `TITLE_LABEL_MISMATCH` (1, rows B5/D0b, custom flag
for a verbatim Q-on-Q vs. Y-on-Y text discrepancy between the cover letter and the release
headline), plus per-row notes on unreconciled figures (E3 PBT%, F2 standalone claim, J2 phone
digit-count) that are enumerated as findings but not scored — that interpretation belongs to A3/A4.
