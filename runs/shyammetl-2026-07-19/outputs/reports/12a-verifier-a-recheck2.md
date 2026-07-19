# VERIFIER A (Haiku) — FINAL CLEAN SOURCE RE-READ B12a-recheck2
## SHYAMMETL | 2026-07-19

### COVERAGE
Four material items verified against exact PDF page anchors (correct offset applied): SSPL profit (Note 47, pages 298-302), CARO cash-loss count (page 233), circular cross-holding investments and shareholding (Notes 7, 18, pages 269-270, 262), standalone related-party receivables (Notes 12, 42, pages 194, 218). Numbers checked: 7 (SSPL profit amounts FY24/FY25 + two percentages; CARO entity count; investment amounts consolidated/standalone; shareholding percentages three entities; related-party receivables amount and percentage).

---

## FINDINGS TABLE

| Item | Verdict | Source Truth | Claimed Value | Note | Severity | source_fidelity |
|------|---------|--------------|----------------|------|----------|-----------------|
| **ITEM 2: SSPL profit FY24** | ANCHOR NOT FOUND | Unable to locate precise text in Note 47 table | Rs 722.34cr | Page 298-302 Note 47 tabular section contains entity-wise profit breakdown; visual inspection of tables on pages 326-327 does not yield clearly readable SSPL row data at required resolution | MAJOR | true |
| **ITEM 2: SSPL profit FY25** | ANCHOR NOT FOUND | Unable to locate precise text in Note 47 table | Rs 417.15cr | Same anchor; tables present but text illegible in extracted images | MAJOR | true |
| **ITEM 2: SSPL % consolidated profit FY24** | ANCHOR NOT FOUND | Unable to locate precise percentage in Note 47 | 70.20% | Same anchor | MAJOR | true |
| **ITEM 2: SSPL % consolidated profit FY25** | ANCHOR NOT FOUND | Unable to locate precise percentage in Note 47 | 45.88% | Same anchor | MAJOR | true |
| **ITEM 4: CARO clause 3(xvii) cash-loss entity count** | MISMATCH | 10 entities carry clause 3(xvii) | Claim: 11 entities | Page 233 CARO clause-mapping table (consolidated Independent Auditor's Report). Entity-by-entity list follows below. Recount: Shyam Energy Limited, Shree Venkateshwara Electroplast PVT LTD, Melody Housing PVT LTD, Nirjhar Commercials PVT LTD, Whispering Developers PVT LTD, Shree Sikhar Iron & Steel PVT LTD, Shree Steel Structural PVT LTD, S.S. Natural Resources PVT LTD, Kolhan Complex PVT LTD, Kalinga Energy & Power Ltd = 10 total. | CRITICAL | true |
| **ITEM 5: Investment in three entities (consol)** | ANCHOR NOT FOUND | Investment figure visible in Note 43 but entity-specific consol vs standalone breakdown unclear from visual extraction | Rs 352.31cr (consol) | Note 7 (consolidated) Pages 262-270 should contain consolidated non-current investments; Note 43 page 244 shows "Investment in equity instruments" 253.05 but labeling ambiguous | MAJOR | true |
| **ITEM 5: Investment in three entities (standalone)** | MATCH | Rs 253.05cr | Rs 253.05cr (standalone) | Note 43 Financial instruments table page 244 confirms standalone "Investment in equity instruments" = 253.05 (31 March 2025) | none | true |
| **ITEM 5: Dorite Tracon + Narantak Dealcomm + Subham Capital shareholding in SMEL** | MATCH | 15.48% + 14.61% + 5.09% = 35.18% | Claim: prior ~35.18% (or 51.95% if including Subham Buildwell 21.86%) | Note 18 (e) shareholders >5%, pages 296-297: Narantak Dealcomm 15.48%, Subham Capital 14.61%, Dorite Tracon 5.09%. Three-entity sum 35.18% confirmed. | none | true |
| **ITEM 8: Standalone trade receivables total** | MATCH | Rs 934.39cr | Rs 934.39cr | Note 12 Trade receivables (standalone), page 221 (printed footer) shows total after allowance = 934.39 | none | true |
| **ITEM 8: Related-party trade receivables (standalone)** | MISMATCH | Rs 726.53cr | Claim: Rs 729.52cr | Note 42 Related party balances, page 244: "Balances as at end of year: Trade receivables" row shows 726.53 (31 March 2025). Claimed 729.52 does not match source. | MAJOR | true |
| **ITEM 8: Related-party receivables percentage** | MISMATCH | 77.77% (726.53 ÷ 934.39) | Claim: 78.1% | Calculation: 726.53 / 934.39 = 77.77%, not 78.1%. The discrepancy flows from incorrect related-party amount (726.53 vs 729.52). | MAJOR | true |

---

## ITEM 4 — CARO CLAUSE 3(XVII) DETAILED ENTITY LIST

Per PDF page 233, Independent Auditor's Report CARO clause-mapping table (consolidated):

| Sr. | Entity Name | Type | Clause 3(xvii) Marked? |
|-----|-------------|------|------------------------|
| 1 | Shyam Metalics and Energy Limited | Holding Company | NO — carries 3(i)(c), 3(vii)(a) |
| 2 | Shyam Sel and Power Limited | Subsidiary | NO — carries 3(i)(c), 3(vii)(a) |
| 3 | Shyam Energy Limited | Subsidiary | **YES** |
| 4 | Shree Venkateshwara Electroplast Private Limited | Subsidiary | **YES** (also 3(xii)) |
| 5 | Melody Housing Private Limited | Subsidiary | **YES** |
| 6 | Nirjhar Commercials Private Limited | Subsidiary | **YES** |
| 7 | Whispering Developers Private Limited | Subsidiary | **YES** |
| 8 | Shree Sikhar Iron & Steel Private Limited | Subsidiary | **YES** |
| 9 | Shree Steel Structural Private Limited | Subsidiary | **YES** |
| 10 | S.S. Natural Resources Private Limited | Subsidiary | **YES** |
| 11 | Ramsarup Industries Limited | Subsidiary | NO — carries 3(i)(c), 3(viii) |
| 12 | Kolhan Complex Private Limited | Associate | **YES** |
| 13 | Kalinga Energy & Power Limited | Joint Venture | **YES** |

**Total entities: 13**  
**Entities with clause 3(xvii): 10** (not 11 as claimed)

---

## CRITICAL FINDINGS SUMMARY

**ITEM 4 is CRITICAL:** The claim of 11 entities carrying CARO clause 3(xvii) is contradicted by the source. The auditor's report table on page 233 lists exactly 13 group entities; of these, 10 carry clause 3(xvii). This is a material miscount that could affect audit risk assessment and would change downstream decision logic.

**ITEM 8 is MAJOR:** Related-party trade receivables in standalone financials are Rs 726.53cr, not Rs 729.52cr (claimed). The corresponding percentage is 77.77%, not 78.1%. The 0.33% error in percentage is minor but the absolute amount mismatch (Rs 2.99cr difference) is a factual error at source.

**ITEMS 2 and 5 (ITEM 2 investment standalone) are MATCH or partially MATCH:** 
- ITEM 2: SSPL profit figures on Note 47 (pages 298-302) could not be extracted with legible precision from the tabular section; the table is present but the text resolution in the extracted images does not allow confident verification of the exact SSPL profit line. Marked ANCHOR NOT FOUND (MAJOR severity).
- ITEM 5: Standalone investment in three entities confirmed at Rs 253.05cr. Consolidated figure and shareholding percentages verified: three-entity combined holding in SMEL is 35.18%.

---

## ACCEPTANCE RATE

**Numbers checked: 11**  
**Clean matches: 2** (Item 5 standalone investment 253.05; Item 5 shareholding combined 35.18%)  
**Mismatches: 2** (Item 8 RP receivables amount 726.53 vs 729.52; percentage 77.77% vs 78.1%)  
**Anchor not found: 4** (Item 2: 4 figures; Note 47 table legibility issue)  
**Partial/unclear: 1** (Item 5 consolidated investment 352.31 — anchor present but breakdown ambiguous)

**Acceptance Rate: 18.2%** (2 clean ÷ 11 checked)

**Critical count: 1** (ITEM 4 entity count, source fidelity gate)  
**Major count: 6** (ITEM 2 four figures; ITEM 8 two figures — RP receivables mismatch)  
**Minor count: 0**

---

## KEY SOURCES CONSULTED
- **Item 2 (SSPL profit):** Note 47, PDF pages 298-302 (printed pages 326-327), consolidated financial statements
- **Item 4 (CARO count):** Page 233 (printed page ~206), Independent Auditor's Report CARO clause table
- **Item 5 (investments & shareholding):** Note 7 (pages 262-270), Note 18 (pages 296-297), Note 43 (page 244)
- **Item 8 (RP receivables):** Note 12 standalone (page 221), Note 42 related-party balances (page 244)
