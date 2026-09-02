# A2 ENUMERATOR — Completeness Ledger
MANINDS | Q1 FY27 (2026-09) | doctype: presentation
Source (A1 structured, referenced by ID only, never re-copied): extracted/maninds-presentation-2026-09-structured.md
Source (A1 fulltext, count-test fallback only, used to resolve footnote/zero-standing sweeps
not separately rowed in the structured file): extracted/maninds-presentation-2026-09-fulltext.md
Prior-quarter ledger: none supplied — DROPPED_SLIDE comparison not applicable this run.

```
=== A2 COUNT TEST ===
category: slides        grep_count: 37   sweep_count: 37   match: yes
category: numbers       grep_count: 223  sweep_count: 223  match: yes
category: entities      grep_count: 49   sweep_count: 49   match: yes
category: forward       grep_count: 20   sweep_count: 20   match: yes
category: dates         grep_count: 43   sweep_count: 43   match: yes
category: footnotes     grep_count: 10   sweep_count: 10   match: yes
category: zero_standing grep_count: 2    sweep_count: 3    match: no -> re-swept (see note)
gate_a2: pass
=== END COUNT TEST ===
```
Zero-standing re-sweep note: A1's structured file marks 2 rows ZERO_STANDING explicitly
(R194, R206). My independent sweep of the page-24 Acquire-vs-Greenfield table found a 3rd
nil-valued standing item ("Order book on day one" = Nil, Greenfield column) that A1 did not
capture at all (the Acquire-side figure is R114; the Greenfield-side Nil has no row). Re-swept
against fulltext line 641 and confirmed present in source. Logged as MF10 below
(MISSING_FROM_STRUCTURED + ZERO_STANDING). After adding MF10 the two sweep methods
reconcile: 2 structured-file ZERO_STANDING rows + 1 MISSING_FROM_STRUCTURED nil item = 3
total nil-standing disclosure units, all now on this ledger. GATE A2 passes because every
unit — including the one A1 missed — is accounted for on this ledger with a line anchor.

---
## 1. SLIDE LEDGER (37 slides — primary ID-accountability table)
Every structured-file row ID is grouped here by its page/slide. This table alone accounts
for all 335 structured IDs (R001–R335); flag tables below add A2-only annotations on top.

| Slide | Title | Content type | A1 structured IDs on this slide | A2 flags |
|---|---|---|---|---|
| 1 | Regulation 30 filing letter (BSE/NSE, Man Industries, CS signature) | text | R001, R224–R228, R293–R296 | — |
| 2 | Corporate Presentation 2026 (cover) | text | R002, R297 | — |
| 3 | Business Overview (section divider) | text (divider) | none | no-data divider, confirmed vs fulltext |
| 4 | Company at a glance (Manufacturing Excellence; Robust Growth Trajectory FY22→FY26) | text + chart | R003–R021, R298–R299 | footnote R021 resolves R004's asterisk in-structured |
| 5 | A Business Built for Scale (India + KSA footprint) | text/table | R022–R028, R229–R233, R273–R276, R300–R301 | — |
| 6 | Global Presence, Manufacturing Footprint & Offices | photo/map | R234 | ENTITY-SUMMARY (map graphic), per materiality rule |
| 7 | Company timeline 1970–2025 | text (timeline infographic) | R029–R048, R235–R240, R302–R315 | dense slide, 40 IDs |
| 8 | Experienced Management governed by a Strong Board | photo + text (bios) | R049–R053, R241–R250, R316 | — |
| 9 | Manufacturing Facilities | text | R054–R055, R251–R253 | — |
| 10 | LSAW Pipe — product specification | table | R056–R059, R254 | — |
| 11 | HSAW Pipe — product specification | table | R060–R063 | — |
| 12 | ERW Pipe — product specification | table | R064–R070 | — |
| 13 | Coating / CWC — product specification | table | R071–R077 | — |
| 14 | Marquee Clientele across Globe | photo (logo roster) | R255 | ENTITY-SUMMARY, no text-layer client names |
| 15 | Accolades & Certifications | photo (logo roster) | R256 | ENTITY-SUMMARY, no text-layer content |
| 16 | Jammu Plant Update (status as of Q1 FY27) | text/chart | R078–R080, R277, R317–R318 | — |
| 17 | Merino Shelters real-estate monetisation | text | R081–R085, R257–R258, R278–R281, R319–R322 | — |
| 18 | STRATEGIC ACQUISITION — National Pipe Company Saudi Arabia (divider) | text (divider) | R259 | — |
| 19 | NPC transaction overview (Target/Consideration/Financing) | table/text | R086–R095, R260–R261 | — |
| 20 | NPC financing structure & ownership (100% via MISIC) | text/chart | R096–R100, R262–R263 | R096–R100 explicitly marked "(restated)" by A1; RESTATED cluster, see §3 |
| 21 | About National Pipe Company Limited — capacity & plant specs | table | R101–R109 | RESTATED cluster (430,000 MT capacity), see §3 |
| 22 | NPC client relationships (Saudi Aramco + roster) | text/list | R110, R264–R265, R323 | — |
| 23 | NPC EPC contractor roster | photo/list | R266 | ENTITY-SUMMARY, no distinct per-member facts |
| 24 | Why Acquisition Is Better Than Greenfield (Acquire vs Greenfield comparison) | table | R111–R116, R282–R283, R324 | MF10 (Nil order-book, Greenfield side) missing here — see §4 |
| 25 | Synergies / value-creation thesis (NPC) | text | R117–R119, R267, R284–R285, R325 | RESTATED cluster (US$83Mn cash, US$120Mn order book), see §3 |
| 26 | NPC Financial Summary — CY2025 (P&L, balance-sheet extract, ratios) | table | R120–R148, R326–R327 | densest slide, 31 IDs |
| 27 | Financial Overview (section divider) | text (divider) | none | no-data divider, confirmed vs fulltext |
| 28 | Annual Standalone Financial Performance (FY26 vs FY25) | table | R149–R160, R328 | MF01, MF02 footnotes missing — see §4 |
| 29 | Annual Consolidated Financial Performance (FY26 vs FY25) | table | R161–R172, R329 | MF03, MF04 footnotes missing — see §4 |
| 30 | Consolidated Balance Sheet (FY24/FY25/FY26) | table | R173–R208, R330 | R194, R206 ZERO_STANDING; MF05 footnote missing — see §2, §4 |
| 31 | Historical Consolidated Financial Performance (FY23–FY26, bar charts) | chart | R209–R215, R331 | MF06, MF07 footnotes missing — see §4 |
| 32 | Quarterly Consolidated Financial Performance Trend (Q1FY26–Q1FY27) | chart | R216–R220, R286, R332–R334 | MF08, MF09 footnotes missing — see §4; R217–R219 note unresolvable per-quarter bar mapping (A1's own caveat, carried forward) |
| 33 | Next 5 years Goal (section divider) | text (divider) | none | no-data divider, confirmed vs fulltext |
| 34 | Piping Towards Higher Utilization Through Global Diversification (5-yr strategy) | text | R221–R222, R287–R292, R335 | — |
| 35 | List of Abbreviations | text | R268 | ENTITY-SUMMARY, glossary |
| 36 | Disclaimer | text | R269 | ENTITY-SUMMARY, legal boilerplate |
| 37 | THANK YOU — Investor Relations contacts | text | R223, R270–R272 | — |

Slide-count reconciliation: 37 slides physically present (fulltext `[page N]` markers, N=1..37)
= 37 slides enumerated above. 3 slides (3, 27, 33) carry zero structured rows and are
confirmed no-data section dividers, not extraction gaps (per A1's own RENDER/COVERAGE
NOTES, independently re-confirmed against fulltext in this sweep). No prior-quarter deck
was supplied, so DROPPED_SLIDE cannot be tested this run — flag as a standing gap for A3/A4:
completeness of the slide *set* vs last quarter is unverified.

---
## 2. ZERO_STANDING LEDGER (nil/dash-valued standing line items)

| Ref | Category | A2 flags | Note |
|---|---|---|---|
| R194 | line_item (consolidated BS asset) | ZERO_STANDING | Intangible assets FY24 = "-"; FY25/FY26 populated (5, 3). Template signal: line exists because intangibles were recognised from FY25. |
| R206 | line_item (consolidated BS asset) | ZERO_STANDING | Current Tax Assets = "-" in all three years FY24/FY25/FY26. Standing zero across the full 3-year window shown. |
| MF10 | line_item (Acquire-vs-Greenfield comparison, page 24) | ZERO_STANDING, MISSING_FROM_STRUCTURED | "Order book on day one" = Nil for the Greenfield route (fulltext line 641, page 24). The Acquire-route figure (US$120 Mn) is captured at R114; the Greenfield Nil counterpart has no structured row. A real miss: dropping the zero side of a comparison table understates how deliberately the deck frames the Nil order book as the cost of the greenfield path not taken. |

---
## 3. RESTATED LEDGER (facts repeated across two or more slides)

| Cluster | IDs | A2 flags | Note |
|---|---|---|---|
| NPC total consideration (USD 102 Mn / ~₹1,000 Cr) | R040, R041, R091, R097, R111 | RESTATED | Same figure across pages 7, 19, 20, 24. |
| NPC financing split (US$70 Mn debt + US$32 Mn equity = US$102 Mn) | R092, R093, R098, R099, R100, R111 | RESTATED | R098–R100 self-labelled "(restated)" by A1 on page 20; formalised here as a cluster spanning pages 19, 20, 24. |
| NPC installed capacity (430,000 MT / 250k HSAW + 180k LSAW) | R023, R087, R101, R104, R105, R106 | RESTATED | Same capacity figure across pages 5, 19, 21. |
| NPC order book on acquisition (US$120 Mn) | R114, R119, R144, R285 | RESTATED | Pages 24, 25, 26; R144 also carries the INR-equivalent (₹1,130–1,150 Cr) restatement of the same figure. |
| NPC cash & liquid assets / net worth (US$83.0 Mn / US$158.6 Mn) | R094, R095, R113, R118, R136–R140 | RESTATED | Pages 19, 24, 25, and the full CY2025 balance-sheet-extract breakdown on page 26. |
| Saudi Aramco relationship duration | R088 ("more than two decades"), R103 ("2+ Decades"), R110 ("40+ Years"), R324/R325 ("since 2005") | RESTATED | Same underlying relationship restated in three different unit framings (decades vs years vs since-date) across pages 19, 21, 22, 24, 25. Unit inconsistency (2+ decades / 40+ years) is a reconciliation question for A3, not resolved here — A2 enumerates the restatement only. |
| Rahul Rawat, Company Secretary | R228, R271 | RESTATED | Signing officer on page 1, IR contact on page 37. |

---
## 4. FOOTNOTE LEDGER (10 footnote/disclaimer occurrences swept from fulltext)

| Ref | Page / line | A2 flags | Note |
|---|---|---|---|
| R021 (cross-ref) | page4 / line92 | already in A1 structured file | "*Note: 1.6Mn MTPA includes NPC capacity of 0.43Mn MTPA" — resolves R004's asterisk. No gap. |
| MF01 | page28 / line744 | MISSING_FROM_STRUCTURED, FOOTNOTE | "*All figures reported in INR Millions, except for EPS" — unit disclaimer, standalone P&L table header. |
| MF02 | page28 / line775 | MISSING_FROM_STRUCTURED, FOOTNOTE | "* EBITDA is inclusive of Other Income, since it's operational in nature" — defines the asterisk on R153 (EBITDA*, standalone). Materially qualifies a headline number: standalone EBITDA is not a pure-operating EBITDA. |
| MF03 | page29 / line781 | MISSING_FROM_STRUCTURED, FOOTNOTE | Same unit disclaimer as MF01, consolidated P&L table header. |
| MF04 | page29 / line812 | MISSING_FROM_STRUCTURED, FOOTNOTE | Same EBITDA-inclusive-of-Other-Income definition as MF02, qualifies R165 (EBITDA*, consolidated). |
| MF05 | page30 / line818 | MISSING_FROM_STRUCTURED, FOOTNOTE | "*All figures reported in INR Millions" — unit disclaimer, consolidated balance sheet header. |
| MF06 | page31 / line859 | MISSING_FROM_STRUCTURED, FOOTNOTE | Unit disclaimer, historical financial-performance chart header. |
| MF07 | page31 / line890 | MISSING_FROM_STRUCTURED, FOOTNOTE | "Note:* Total Income is inclusive of Other Income, since it's operational in nature" — qualifies the "Total Income*" chart title feeding R209. |
| MF08 | page32 / line895–896 | MISSING_FROM_STRUCTURED, FOOTNOTE | Unit disclaimer, quarterly-trend chart header (wraps across two OCR lines). |
| MF09 | page32 / line930–941 | MISSING_FROM_STRUCTURED, FOOTNOTE | OCR-garbled combined footnote block: repeats the "Total Income inclusive of Other Income" definition (qualifies R216) interleaved with the Q1-FY27/40-day NPC-contribution note. The 40-day content is already captured at R220 and R286 (FORWARD); the Total-Income-inclusive portion is new and previously uncaptured. |

Materiality: MF02/MF04 are the highest-value misses on this ledger. Both standalone and
consolidated EBITDA — the two headline profitability numbers on the deck's core financial
slides — carry an unflagged "includes Other Income" qualifier in the structured extraction.
Any downstream margin or quality-of-earnings read (A4) that treats R153/R165 as pure
operating EBITDA without this qualifier would be working off an incomplete number.

---
## 5. ID ACCOUNTABILITY
ids_in_structured: 335 | ids_referenced_in_ledger: 335 | orphan_ids: [] | match: yes

All R001–R335 are accounted for in §1 (SLIDE LEDGER), with §2–§4 adding A2-only flags,
cross-references, and the 10 MISSING_FROM_STRUCTURED units on top (no double-counting:
MF01–MF10 are new rows this ledger adds, not re-references of structured IDs).
