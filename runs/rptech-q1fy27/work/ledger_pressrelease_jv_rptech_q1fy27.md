# A2 ENUMERATION LEDGER — pressrelease_jv_rptech_q1fy27

Source: `extract_pressrelease_jv_rptech_q1fy27.txt` (5 pages, 212 body lines, doctype=results per task; actual content = proposed JV press release + BSE/NSE cover letter, filed alongside Q1 FY27 results, 4 Aug 2026)
No prior-quarter ledger was supplied for this doctype (first JV-press-release enumeration for RPTECH in this pipeline) — cross-check against a prior list per rule 6 is therefore N/A; all "new" designations below are based on internal evidence only (a name/entity is "new" if this is its first appearance anywhere in this document and it did not exist as a legal/operating entity before the transaction described).

```
=== A2 COUNT TEST ===
category: entities                  grep_count: 13  sweep_count: 13  match: yes
category: forward_commitment_phrases grep_count: 12  sweep_count: 12  match: yes
category: timeline_dates            grep_count: 10  sweep_count: 10  match: yes
category: equity_governance_items   grep_count: 6   sweep_count: 6   match: yes
category: target_segments           grep_count: 8   sweep_count: 8   match: yes
category: key_highlights_bullets    grep_count: 4   sweep_count: 4   match: yes
category: quotes                    grep_count: 3   sweep_count: 3   match: yes
category: boilerplate_sections      grep_count: 4   sweep_count: 4   match: yes
category: background_numeric_facts  grep_count: 6   sweep_count: 6   match: yes
category: monetary_size_figures     grep_count: 3   sweep_count: 3   match: yes
category: identifiers               grep_count: 3   sweep_count: 3   match: yes
category: digital_signature_blocks  grep_count: 1   sweep_count: 1   match: yes
category: conditions_precedent      grep_count: 0   sweep_count: 0   match: yes
category: capital_commitment_amounts grep_count: 0  sweep_count: 0   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep methodology note: all patterns run against the raw line-numbered extract; entity/phrase patterns that could split across a line-wrap (e.g. "step-down subsidiary" wraps lines 92-93) were re-verified against a newline-joined copy of the file (`tr '\n' ' '`) to avoid an undercount. Two false-positive substring matches were caught and excluded during reconciliation: (1) a naive `Rs\.` pattern matched inside "secto**rs.**", "stakeholde**rs.**", "partne**rs.**" and was corrected with a word boundary; (2) the header-metadata block (lines 1-13, the A1 extraction header, not document content) was excluded from all body counts.

---

## 1. Named entities / JV parties (13)

| # | Entity | Role | Line(s) | First 15 words / identifying text | Flags |
|---|---|---|---|---|---|
| 1 | Rashi Peripherals Limited ("RP tech") | JV Party A / filer | 24,39,67,75,76,86,87,131,133,176,186,188,225 | "Rashi Peripherals Limited (NSE: RPTECH) (BSE: 544119) ('RP tech'), one of the leading..." | — |
| 2 | Restar Corporation | JV Party B, Japanese counterparty | 32,88,89,93,94,104,122,134,150,157,161,205,207 | "Restar Corporation, a leading Japanese electronics and technology company" | ENTITY_CHANGE (first disclosure of this counterparty relationship) |
| 3 | Wholly owned subsidiary (unnamed at creation), HQ Bengaluru | Vehicle receiving RP tech's transferred semiconductor business division | 91-92 | "Rashi Peripherals will transfer its semiconductor business division into a wholly owned subsidiary headquartered in Bengaluru" | ENTITY_CHANGE — new entity created by this transaction |
| 4 | Step-down subsidiary (unnamed), HQ Singapore | Second-tier subsidiary under the Bengaluru entity | 92-93 | "...and step-down subsidiary headquartered in Singapore" | ENTITY_CHANGE — new entity created by this transaction; no further detail on its function given |
| 5 | Rashi Restar Semiconductor Solutions | Working/brand name of the JV entity | 161 | "we believe Rashi Restar Semiconductor Solutions will become a significant player in India's semiconductor distribution landscape" | ENTITY_CHANGE — first and only appearance of this name in the document; not stated whether this is the legal name of entity #3, a trade name, or a distinct entity — NOT FOUND (relationship to #3 unclarified) |
| 6 | BSE Limited | Regulatory filing recipient | 20 | "BSE Limited, Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai-400001" | — |
| 7 | National Stock Exchange of India Limited (NSE) | Regulatory filing recipient | 20-22 | "The National Stock Exchange of India Limited (NSE), 05th Floor, Exchange Plaza..." | — |
| 8 | Rajesh Goenka | Director & CEO, Rashi Peripherals — quote source | 131 | "Rajesh Goenka, Director & Chief Executive Officer - Rashi Peripherals Limited, said:" | — |
| 9 | Kapal Pansari | Managing Director, Rashi Peripherals — quote source | 145 | "Kapal Pansari - Managing Director, commented:" | — |
| 10 | Masahiro Shibata | GM Device Business Unit & VP, Executive Officer, Restar Corporation — quote source | 156-157 | "Masahiro Shibata, General Manager of Device Business Unit and Vice President, Executive Officer - Restar Corporation, said:" | — |
| 11 | Arvind Bajoria | Company Secretary and Compliance Officer, Rashi Peripherals — signatory | 39-68 | "Arvind Bajoria, Company Secretary and Compliance Officer" (digitally signed block) | — |
| 12 | Priyanka Pugaokar | Lead – Corporate Communications, Rashi Peripherals — press contact | 224-226 | "Ms Priyanka Pugaokar, Rashi Peripherals Limited, Lead – Corporate Communications" | — |
| 13 | Embedded Lab (Bengaluru) | Existing RP tech technical facility, background context | 168-169 | "including a dedicated Embedded Lab in Bengaluru that supports local design and solution development" | — (pre-existing, not new) |

## 2. Ownership / equity split & governance items (6)

| # | Item | Line | Text | Flags |
|---|---|---|---|---|
| 1 | Restar's equity stake in the subsidiary | 94 | "will subsequently acquire a 26% equity stake in the subsidiary" | forward-commitment ("will acquire") |
| 2 | RP tech shareholding in the JV | 103 | "74% shareholding with RP tech" | — |
| 3 | Restar Corporation shareholding in the JV | 103-104 | "26% with Restar Corporation" | — |
| 4 | Board size | 104 | "a 4-member Board" | — |
| 5 | RP tech board seats | 104 | "(3 RP tech and 1 Restar Corporation partner)" | — |
| 6 | Restar Corporation board seat | 104 | "(3 RP tech and 1 Restar Corporation partner)" | — |

## 3. Capital commitment amounts (0 — NOT FOUND)

| # | Item | Line | Text | Flags |
|---|---|---|---|---|
| — | Consideration / purchase price for Restar's 26% equity stake | N/A | Not stated anywhere in the release. Only the percentage (26%) and Restar's overall conglomerate size (≈US$4bn) are disclosed; no INR or USD figure is attached to the transaction itself. | ZERO_STANDING / NOT FOUND — capital commitment amount is a template item for a stake-acquisition disclosure of this type and is conspicuously absent; do not estimate |

## 4. Scope / product lines / target segments

Core scope statement (1 row):

| # | Item | Line(s) | Text | Flags |
|---|---|---|---|---|
| 1 | Product/service scope | 97-99 | "The partnership will focus on delivering advanced Image Sensing Solutions for Industrial and Automotive applications, supported by localized engineering, design, and technical services tailored to the Indian market" | forward-commitment ("will focus") |

Target segments, enumerated individually (8):

| # | Segment | Line(s) | Flags |
|---|---|---|---|
| 1 | Automotive Tier-1s | 115-116 | — |
| 2 | Industrial Robotics | 115-116 | — |
| 3 | Electronics Manufacturing Services (EMS) | 116 | — |
| 4 | Electronics Component Manufacturing Services (ECMS) | 116-117 | — |
| 5 | Enterprise Surveillance | 117 | — |
| 6 | Machine Vision Cameras | 117 | — |
| 7 | Audio Visual (AV) | 117-118 | — |
| 8 | Home Appliances | 118 | — |

## 5. Key Highlights bullets (4, distinct from the "Governance" and "Target Segments" rows above, which decompose bullets 1 and 4)

| # | Bullet heading | Line | Flags |
|---|---|---|---|
| 1 | Governance Structure | 103-104 | see section 2 for decomposed items |
| 2 | Headquarters & Reach | 106-108 | "network across 5 major-city locations to drive nationwide operations" — forward-commitment ("will leverage") |
| 3 | High-Tech Skill Transfer & Field Application Engineering Support | 110-113 | "50+ new local engineering hires over 2 years" — headcount/timeline commitment |
| 4 | Target Segments | 115-118 | see decomposed list in section 4 |

## 6. Conditions precedent (0 — flagged)

| # | Item | Line | Flags |
|---|---|---|---|
| — | None disclosed | N/A | ZERO_STANDING — searched for "subject to", "condition(s) precedent", "shareholder approval", "regulatory approval", "CCI/competition commission approval", "definitive agreement", "long form agreement", "closing condition": zero hits. No regulatory, shareholder, or board-approval condition is stated anywhere for either the business transfer, the 26% stake sale, or the October 2026 commencement date. Notable disclosure gap for a cross-border equity transaction of this type — NOT FOUND, do not assume "already satisfied" |

## 7. Timeline / dates (10)

| # | Item | Line | Text | Flags |
|---|---|---|---|---|
| 1 | Cover letter date | 16 | "August 4, 2026" | — |
| 2 | Press release date (referenced in letter body) | 31 | "press release dated August 4, 2026" | — |
| 3 | Digital signature timestamp | 48 | "Date: 2026.08.04 19:48:53 +05'30'" | signed same day as release; no board meeting time given in this document to compare against |
| 4 | Press release dateline | 85 | "Mumbai, August 04, 2026:" | — |
| 5 | JV commencement date | 95 | "the JV scheduled to officially commence operations in October 2026" | forward-commitment ("scheduled to"); ~2-month gap from announcement to commencement, no conditions precedent given to explain the gap (see section 6) |
| 6 | Engineering-hire ramp timeline | 112 | "50+ new local engineering hires over 2 years" | forward-commitment, no start date anchor given (from JV commencement, presumably, but not stated — NOT FOUND) |
| 7 | India semiconductor ecosystem target year | 164 | "$150 billion semiconductor ecosystem by 2030" | market-size framing, not a company commitment |
| 8 | RP tech's semiconductor business entry date | 166-167 | "became the first ICT distributor in India to enter the semiconductor business in 2021" | background/historical |
| 9 | RP tech incorporation date | 188 | "Incorporated in 1989, Rashi Peripherals Limited is one of India's leading distributors..." | background/historical |
| 10 | Restar Corporation founding date | 207 | "Established in 2009, Restar Corporation is a leading Japanese technology..." | background/historical |

## 8. Forward-commitment phrases (12, each occurrence)

| # | Phrase | Line | Context (first ~10 words) | Flags |
|---|---|---|---|---|
| 1 | "proposed" | 27 | "Press Release on proposed Joint Venture" (title) | — |
| 2 | "proposed" | 31 | "for the proposed Joint Venture with Restar Corporation of Japan" | — |
| 3 | "will" | 91 | "Rashi Peripherals will transfer its semiconductor business division" | — |
| 4 | "will" | 94 | "Restar Corporation...will subsequently acquire a 26% equity stake" | — |
| 5 | "scheduled to" | 95 | "the JV scheduled to officially commence operations in October 2026" | — |
| 6 | "will" | 97 | "The partnership will focus on delivering advanced Image Sensing Solutions" | — |
| 7 | "will" | 107 | "the JV will leverage a network across 5 major-city locations" | — |
| 8 | "aim to" | 126 | "the partners aim to accelerate the adoption of advanced semiconductor technologies" | — |
| 9 | "aim to" | 137 | "Together, we aim to deliver localized support" (Goenka quote) | — |
| 10 | "will" | 140 | "JV with a ≈US$4 billion Japanese conglomerate will open a host of opportunities" (Goenka quote) | — |
| 11 | "will" | 152 | "This will facilitate to setup of strong building block solutions" (Pansari quote) | — |
| 12 | "will" | 162 | "we believe Rashi Restar Semiconductor Solutions will become a significant player" (Shibata quote) | ties to ENTITY_CHANGE #5 |

No instances found of: "subject to", "expected to"/"expects to", "intends"/"intend to", "plans to". Checked and confirmed zero (see section 6 grep note).

## 9. Quotes / named speaker statements (3)

| # | Speaker | Role | Line(s) | Flags |
|---|---|---|---|---|
| 1 | Rajesh Goenka | Director & CEO, Rashi Peripherals | 131-143 | Contains forward-commitment phrases #9, #10 above |
| 2 | Kapal Pansari | Managing Director, Rashi Peripherals | 145-154 | Contains forward-commitment phrase #11 above |
| 3 | Masahiro Shibata | GM Device Business Unit & VP, Executive Officer, Restar Corporation | 156-162 | Contains forward-commitment phrase #12 and the only mention of "Rashi Restar Semiconductor Solutions" (ENTITY_CHANGE) |

## 10. Monetary size figures cited (non-capital-commitment) (3)

| # | Figure | Line | Context | Flags |
|---|---|---|---|---|
| 1 | ≈US$4 billion | 93 | "Restar Corporation - a ≈US$4 billion conglomerate" (Restar's own size, not deal value) | — |
| 2 | ≈US$4 billion | 140 | Repeated in Goenka quote: "JV with a ≈US$4 billion Japanese conglomerate" | duplicate of #1, different context (quote vs. body) |
| 3 | $150 billion | 164 | "India advances toward creating a $150 billion semiconductor ecosystem by 2030" (market TAM, not company or deal figure) | — |

## 11. Identifiers (3)

| # | Identifier | Line | Text | Flags |
|---|---|---|---|---|
| 1 | BSE Scrip Code | 24 | "Scrip Code: 544119" | — |
| 2 | NSE Symbol | 24 | "Symbol: RPTECH" | — |
| 3 | CIN | 77 | "CIN: L30007MH1989PLC051039" | — |

## 12. Digital signature block (1)

| # | Signatory | Designation | Line(s) | Timestamp | Flags |
|---|---|---|---|---|---|
| 1 | Arvind Bajoria | Company Secretary and Compliance Officer | 39-68 | 2026.08.04 19:48:53 +05'30' | No board meeting time is stated in this document to check the "signed before meeting concluded" pattern against; this is a standalone press-release cover letter, not a board outcome letter. No flag raised on that basis. |

## 13. Boilerplate / background sections (4)

| # | Section | Line | Flags |
|---|---|---|---|
| 1 | Safe Harbor Statement | 174-184 | Standard forward-looking-statement disclaimer; explicitly disclaims accuracy/completeness guarantee and undertakes no obligation to update |
| 2 | About Rashi Peripherals Limited | 186-201 | Contains 6 background numeric facts, see section 14 |
| 3 | About Restar Corporation | 205-216 | Background only; HQ Tokyo, founded 2009, no numeric facts (headcount/revenue/locations) given for Restar itself — NOT FOUND |
| 4 | Contact Information | 222-226 | Priyanka Pugaokar, Lead – Corporate Communications |

## 14. Background standing numeric facts — About Rashi Peripherals (6)

| # | Fact | Line | Flags |
|---|---|---|---|
| 1 | 700+ locations | 191-192 | — |
| 2 | 57 branches | 192 | — |
| 3 | 50 service centres | 192 | — |
| 4 | 73 warehouses | 192 | — |
| 5 | 80 global brands | 199 | — |
| 6 | 10,250 channel partners | 199 | — |

No equivalent numeric facts (headcount, revenue, branch count) are given for Restar Corporation in its "About" section (section 13, row 3) — NOT FOUND, asymmetry between the two parties' disclosed operating scale.

---

## FLAGS SUMMARY

- **ENTITY_CHANGE** (4): Restar Corporation (new counterparty relationship, row 1.2); new wholly owned subsidiary, Bengaluru (row 1.3); new step-down subsidiary, Singapore (row 1.4); "Rashi Restar Semiconductor Solutions" JV working name, first and only appearance, relationship to the Bengaluru subsidiary not clarified (row 1.5).
- **ZERO_STANDING / NOT FOUND** (2 template categories): capital commitment amount / consideration for the 26% stake (section 3) — zero disclosed; conditions precedent (section 6) — zero disclosed for a cross-border equity transaction with a ~2-month gap to stated commencement.
- **NOT FOUND** (secondary, non-template): relationship between "Rashi Restar Semiconductor Solutions" and the unnamed Bengaluru subsidiary (row 1.5); start-date anchor for the "50+ hires over 2 years" commitment (section 7, row 6); operating-scale numeric facts for Restar Corporation (section 14 note).
