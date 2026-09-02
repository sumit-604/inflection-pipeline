# MANINDS Corporate Presentation (01 Sep 2026) — A2 Completeness Ledger

Source: A1 structured extraction only (`extracted/maninds-presentation-2026-09-structured.md`).
Fulltext used only as count-test fallback (`extracted/maninds-presentation-2026-09-fulltext.md`).
Row IDs R001-R335 are A1's; this ledger references them, it does not re-copy verbatim values.

ids_in_structured: 335 | ids_referenced_in_ledger: 335 | orphan_ids: [] | match: yes

```
=== A2 COUNT TEST ===
category: numbers        grep_count: 223   sweep_count: 223   match: yes
category: entities        grep_count: 49    sweep_count: 49    match: yes
category: entity_summary  grep_count: 9     sweep_count: 9     match: yes
category: forward         grep_count: 20    sweep_count: 20    match: yes
category: dates           grep_count: 43    sweep_count: 43    match: yes
category: slides          grep_count: 37    sweep_count: 37    match: yes   (fulltext page-marker fallback used; structured file's own coverage note also states 37)
category: zero_standing   grep_count: 2     sweep_count: 2     match: yes
category: footnotes       grep_count: 5     sweep_count: 5     match: yes   (rows R004,R021,R153,R165,R269; grouped into 4 logical footnote units below)
gate_a2: pass
=== END COUNT TEST ===
```

ID range cross-check: NUMBER R001-R223 (223) + ENTITY R224-R272 (49) + FORWARD R273-R292 (20)
+ DATE R293-R335 (43) = 335 = TOTAL ROWS declared in A1's own COUNTS header. Contiguous, no gaps.

---
## 1. SLIDES (page-by-page ledger, 37 physical pages; all referenced IDs accounted for)

| Page | Content type | Title / summary | NUMBER ids | ENTITY ids | FORWARD ids | DATE ids | A2 flags |
|---|---|---|---|---|---|---|---|
| 1 | text | BSE/NSE Regulation-30 intimation letter (cover) | R001 | R224-R228 | - | R293-R296 | - |
| 2 | text | Corporate presentation title slide | R002 | - | - | R297 | - |
| 3 | - | [no data — section-title divider] | - | - | - | - | - |
| 4 | chart/table | Growth trajectory FY22-FY26 (Revenue/EBITDA/PAT/ROCE/ROE/Networth) | R003-R021 | - | - | R298-R299 | FOOTNOTE (R004/R021 pair) |
| 5 | text/table | Manufacturing footprint & capacity (India + KSA Dammam + Jammu) | R022-R028 | R229-R233 | R273-R276 | R300-R301 | - |
| 6 | photo/map | World map — facility/office location graphic | - | R234 (ENTITY-SUMMARY) | - | - | - |
| 7 | timeline/chart | Company history timeline 1970-2026 | R029-R048 | R235-R240 | - | R302-R315 | - |
| 8 | photo/text | Leadership: Board + KMP + senior management bios | R049-R053 | R241-R250 | - | R316 | - |
| 9 | text/table | Manufacturing facilities overview (land, capacity, ISO certs) | R054-R055 | R251-R253 (R253 ENTITY-SUMMARY) | - | - | - |
| 10 | table | LSAW product specification table | R056-R059 | R254 | - | - | - |
| 11 | table | HSAW product specification table | R060-R063 | - | - | - | - |
| 12 | table | ERW / Square-Rectangular Hollow Section spec table | R064-R070 | - | - | - | - |
| 13 | table | Internal coating & CWC (concrete weight coating) spec table | R071-R077 | - | - | - | - |
| 14 | photo/logo | Client logo roster (domestic & international) | - | R255 (ENTITY-SUMMARY) | - | - | - |
| 15 | photo/logo | Accolades & certifications roster | - | R256 (ENTITY-SUMMARY) | - | - | - |
| 16 | text | Jammu Stainless Steel Plant project update | R078-R080 | - | R277 | R317-R318 | - |
| 17 | text | Merino Shelters real-estate monetization update | R081-R085 | R257-R258 | R278-R281 | R319-R322 | - |
| 18 | text | NPC (Saudi Arabia) acquisition — section divider | - | R259 | - | - | - |
| 19 | table/text | NPC acquisition transaction overview | R086-R095 | R260-R261 | - | - | RESTATED cluster (see §4) |
| 20 | table | NPC transaction structure via MISIC (restated) | R096-R100 | R262-R263 | - | - | RESTATED cluster |
| 21 | table | NPC plant & capacity detail | R101-R109 | - | - | - | RESTATED cluster |
| 22 | text/table | NPC client relationships (Saudi Aramco + others) | R110 | R264-R265 (R265 ENTITY-SUMMARY) | - | R323 | DATA_INCONSISTENCY (see §4) |
| 23 | table/logo | NPC EPC contractor roster | - | R266 (ENTITY-SUMMARY) | - | - | - |
| 24 | table | Acquire vs Greenfield strategic comparison | R111-R116 | - | R282-R283 | R324 | RESTATED / DATA_INCONSISTENCY |
| 25 | text | NPC synergies & value-creation thesis | R117-R119 | R267 | R284-R285 | R325 | RESTATED / DATA_INCONSISTENCY |
| 26 | table | NPC financial summary, CY2025 (P&L, BS items, ratios, FX) | R120-R148 | - | - | R326-R327 | RESTATED cluster |
| 27 | - | [no data — section-title divider] | - | - | - | - | - |
| 28 | table | Standalone financial results FY26 vs FY25 | R149-R160 | - | - | R328 | FOOTNOTE_UNRESOLVED (R153) |
| 29 | table | Consolidated financial results FY26 vs FY25 | R161-R172 | - | - | R329 | FOOTNOTE_UNRESOLVED (R165) |
| 30 | table | Consolidated balance sheet FY24-FY26 | R173-R208 | - | - | R330 | ZERO_STANDING (R194, R206) |
| 31 | table | Historical financial summary FY23-FY26 | R209-R215 | - | - | R331 | - |
| 32 | chart | Quarterly trend charts Q1FY26-Q1FY27 | R216-R220 | - | R286 | R332-R334 | (R217-R219 mapping caveat carried from A1) |
| 33 | - | [no data — section-title divider] | - | - | - | - | - |
| 34 | text | Strategic goals & 5-year targets | R221-R222 | - | R287-R292 | R335 | - |
| 35 | text | Glossary of abbreviations | - | R268 (ENTITY-SUMMARY) | - | - | - |
| 36 | text | Safe-harbor / forward-looking statement disclaimer | - | R269 (ENTITY-SUMMARY) | - | - | FOOTNOTE (fine-print, deck-wide) |
| 37 | text | Contact information (Investor Relations) | R223 | R270-R272 (R272 ENTITY-SUMMARY) | - | - | RESTATED (R271 vs R228) |

Pages 3, 27, 33 carry zero structured rows — confirmed no-data section dividers per A1's own
RENDER/COVERAGE NOTES, not extraction gaps. No prior-quarter deck supplied (prior_ledger_path:
none), so DROPPED_SLIDE comparison is not applicable this run.

---
## 2. FOOTNOTES (independent sweep, cross-referenced to NUMBER/ENTITY rows above)

| Footnote unit | Marker row | Resolution row | A2 flag | Note |
|---|---|---|---|---|
| FN1 | R004 (page4, "1.6Mn+ MTPA*") | R021 (page4, "0.43Mn MTPA... NPC capacity within 1.6Mn MTPA total") | FOOTNOTE_RESOLVED | Asterisk on total API-grade capacity is resolved by the adjacent breakdown row; the 1.6Mn+ MTPA headline includes NPC's 0.43Mn MTPA post-acquisition. |
| FN2 | R153 (page28, "EBITDA* FY26 4,928...") | none found in structured file | FOOTNOTE_UNRESOLVED | No row defines what the EBITDA asterisk denotes (e.g. adjustment basis). Loop to A1/A3: check page 28 for unrendered fine print. |
| FN3 | R165 (page29, "EBITDA* FY26 4,679...") | none found in structured file | FOOTNOTE_UNRESOLVED | Same asterisk, consolidated table; same gap. |
| FN4 | R269 (page36, safe-harbor / forward-looking disclaimer) | n/a — is itself the resolution | FOOTNOTE (deck-wide) | Fine-print disclaimer qualifying all 20 FORWARD rows (R273-R292) and the 5-year targets on page 34; not itself an unresolved gap, but the qualifier every FORWARD row should be read against. |

---
## 3. ZERO_STANDING (nil/dash line items — never dropped)

| Row | Line item | Flag | Note |
|---|---|---|---|
| R194 | Intangible assets, consolidated BS, FY24 "-" (FY25 5, FY26 3) | ZERO_STANDING | Partial: only FY24 is nil; template signal that the line exists (post-NPC intangibles emerge FY25 onward). |
| R206 | Current Tax Assets, consolidated BS, FY24/FY25/FY26 all "-" | ZERO_STANDING | Nil across all three disclosed years; standing line retained regardless. |

Independent sweep of all 223 NUMBER rows for "-"/dash/nil patterns (balance-sheet and P&L tables,
pages 26/28/29/30/31) found no further zero-standing candidates beyond R194 and R206.

---
## 4. RESTATED / CROSS-REFERENCE CLUSTERS (same fact repeated across slides)

| Cluster | Row IDs | Flag | Materiality note |
|---|---|---|---|
| NPC 100% stake acquired | R039, R086, R089, R096 | RESTATED | Consistent across pages 7/19/19/20. |
| NPC total consideration USD 102 Mn | R040, R091, R097, R111 | RESTATED | Consistent across pages 7/19/20/24; R041 gives the sole INR-equivalent (~₹1,000 Cr). |
| Debt/equity financing split (USD 70 Mn debt + USD 32 Mn equity) | R092, R093, R098, R099, R111 | RESTATED | Consistent across pages 19/20/24. |
| NPC installed capacity 430,000 MT(PA) | R023, R087, R101, R104 | RESTATED | Consistent across pages 5/19/21/21. |
| Cash & liquid assets USD 83 Mn | R094, R113, R118, R139 | RESTATED | Consistent across pages 19/24/25/26. |
| Net worth USD 158.6 Mn | R095, R140 | RESTATED | Consistent, pages 19/26. |
| Order book USD 120 Mn at acquisition | R114, R119, R144 | RESTATED | Consistent across pages 24/25/26; R144 adds INR-equivalent ₹1,130-1,150 Cr. |
| IR contact — Rahul Rawat, Company Secretary | R228, R271 | RESTATED | Page 1 signing officer restated as IR contact on page 37; consistent. |
| **Saudi Aramco / NPC relationship duration** | R088 ("more than two decades"), R103 ("2+ Decades"), R324 ("since 2005"), R325 ("since 2005") **vs.** R110 ("40+ Years"), R264 ("40+ Years"), R323 ("40+ Year") | **DATA_INCONSISTENCY** | Pages 19/21/24/25 converge on ~20-21 years (since 2005) for the Aramco-approved-vendor relationship tied to the Acquire-route narrative, while page 22 states "40+ Years" for the same NPC-Aramco relationship twice (R110, R264) plus once for NPC's broader GCC client base (R323). Both cannot describe the identical relationship start date. Flag to A3/A4: verify whether "40+ years" describes NPC's founding-era relationship with Aramco (entity-level, pre-dating Man Industries' 2023/2026 acquisition) versus "2+ decades"/"since 2005" describing a narrower Aramco-approved-vendor certification date — the deck does not disambiguate, and as presented on the same NPC section (pages 19-25) it reads as an internal contradiction. |

---
## 5. NUMBER / ENTITY / FORWARD / DATE — full ID accountability (by category, contiguous ranges)

- NUMBER: R001-R223 (223 rows) — all referenced in §1 slide table above.
- ENTITY (incl. 9 ENTITY-SUMMARY grouped rows: R234, R253, R255, R256, R265, R266, R268, R269, R272): R224-R272 (49 rows) — all referenced in §1.
- FORWARD: R273-R292 (20 rows) — all referenced in §1; all 20 sit under the R269 safe-harbor qualifier (§2, FN4).
- DATE: R293-R335 (43 rows) — all referenced in §1.

No MISSING_FROM_STRUCTURED units were found: the independent page-by-page sweep (via fulltext
page markers, used only as the count-test fallback) matched A1's structured coverage note of 37
pages with data on 34 of them, dividers on 3 (pages 3/27/33), exactly.

---
## ANALYST NOTE

Two genuine downstream items: (1) FOOTNOTE_UNRESOLVED on both EBITDA* rows (R153 standalone,
R165 consolidated, pages 28-29) — the asterisk qualifies the quarter's headline profitability
metric and its definition is not captured anywhere in the structured file; A3 should check if a
fine-print line exists on those pages that A1's rendering missed. (2) DATA_INCONSISTENCY on the
Aramco/NPC relationship duration: pages 19/21/24/25 say "2+ decades"/"since 2005" (~20-21 years)
while page 22 says "40+ Years" twice for what reads as the same relationship, inside the same NPC
acquisition narrative. This matters because the "40+ Years" framing (R110, R264, R323) is stronger
evidence for NPC's Aramco-relationship durability than "2+ decades" — if the deck itself cannot
agree on the figure, A4 should not anchor an investment claim to either number without going back
to the NPC transaction document set. Both zero-standing rows (R194, R206) are ordinary nil
line-items, not concerning in isolation.
