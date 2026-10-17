# A3 FORENSIC NOTES: presentation, KARNIKA, h1fy27 (Q2 FY27 / H1 FY27, period ended 30-Sep-2026)

Agent: A3 forensic notes (claude-opus-5-5). Run date 2026-10-17.
Inputs read: A1 structured `extracted/karnika-presentation-h1fy27-structured.md` (R001-R553), A1 fulltext `extracted/karnika-presentation-h1fy27-fulltext.md` (lines 1-610, all 32 pages), A2 ledger `work/ledger_presentation_karnika_h1fy27.md`.
Not available: prior-quarter fulltext; Notion monitoring checklist; companies/KARNIKA.md. This is a PRE-THESIS READ with no spear on record. No source PDF and nothing under inputs/ was opened.
Slide convention (per A2): slide = page minus 1. Cites give fulltext line (lNNN) and slide (SNN).
Rounding: the deck prints most figures in whole INR Cr. Derived numbers below use the printed margin percentages to recover one decimal where possible. Every derived figure is labelled "derived" and shows its inputs.

## 0. LEDGER RECONCILIATION

- Structured IDs in the ledger: 553 (R001-R553). IDs read at their cited fulltext line: 553. Reconciled: 100%.
- ZERO_STANDING rows: 42 of 42 read (sections 2 and 3 of the ledger agree).
- Line-cite drift (A1 cite, carried by A2). The value exists verbatim at an adjacent line. The value is correct and only the line number is off. This is a pipeline data-quality note, not a document finding:

| Row | Value | Cited line | Actual line |
|---|---|---|---|
| R006 | 35% | l94 | l93 |
| R018 | 49% | l159 | l160 |
| R052 | 7.9% | l225 | l226 |
| R065 | 70 | l271 | l274 |
| R073 | 13 | l276 | l275 |
| R205 | 101 | l331 | l321 |
| R207 | 28 | l327 | l329 |
| R208 | 36 | l327 | l328 |
| R212 | 90%+ | l324 | l325 |
| R256 | 0.8x | l522 | l523 |
| R257 | 0.8x | l522 | l523 |

- A2 flag rulings:
  - RESTATED (R055-R064 and R248-R253): **not upheld.** The FY24, FY25 and FY26 value pairs are identical on S10 (l217-226) and S27 (l518-521): (17.5, 19.0), (21.8, 25.5) and (25.5, 29.0). Only the legend order differs: "ROE ROCE" at l230 and "ROCE ROE" at l525.
  - SERIES_UNRESOLVED and SERIES_BY_POSITION on ROE/ROCE: **resolved by computation from S29/S30.**
    - FY26 ROCE = EBIT (PBT 39 + interest 5) / (equity 98 + debt 76) = 25.3%, so ROCE = 25.5%. ROE = 28/98 = 28.6%, so ROE = 29.0%.
    - FY25 ROCE = 28/131 = 21.4%, so 21.8% is ROCE and 25.5% is ROE (18/71 = 25.4%).
    - FY24 ROCE = 19/105 = 18.1%, so 17.5% is ROCE and 19.0% is ROE (10/53 = 18.9%).
    - FY23 45.6% is ROE (8/18 = 44%).
  - HEADER_LABEL_MISMATCH (R516, R518, R543, R544): **resolved. The "Q1FY26" column holds Q1 FY27 data.** See A3-12.
  - MAPPING_UNRESOLVED (S8 category mix, S9 segmentation): stays unresolved. It is used only conditionally in A3-21.
  - YEAR_BY_X_POSITION (FATR): the mapping is plausible against PPE on an average-PPE basis for FY25 and FY26. The H1FY27 value is not reproducible. See A3-26.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R141-R148; R260-R261, R470 | l297 S14; l540-544 S28 | "(0.2) 0 - 0 - 0 0 -" | AMBIGUOUS | The associate line has its first non-zero value in Q2FY27, a loss of Rs 0.2 Cr. The associate is Elementa Lifespaces, 40% acquired "for Rs. 2 crore" (l542-544). One quarter's loss equals about 10% of the Rs 2 Cr cost. The H1FY27 cell prints 0, but Q1 is 0 and Q2 is (0.2), so the half-year should read (0.2). The table is internally inconsistent. Ask what Elementa does, what its run-rate loss is, and why the H1 cell prints 0. |
| A3-02 | F1 | R354-R357, R374-R377 | l588, l594 S30 | "Long term provisions 0 0 0 0" / "Short term provisions 0 0 0 0" | AMBIGUOUS | Provisions are zero in all four years. Yet the company runs 4 plants (l101) and employee cost was Rs 8 Cr in FY26 (l560). The template line exists for employee benefits (gratuity, leave) and tax. Readings: the gratuity scheme is fully funded through an insurer; amounts are below Rs 0.5 Cr; or no provision is made under AS 15. Check the AR notes on employee benefits. |
| A3-03 | F1 | R394-R397; R469, R258 | l583 S30; l530-531 S28 | "Goodwill 0 0 0 0" | AMBIGUOUS | Goodwill is zero in every year despite "Acquired a 75% controlling stake in Kidcity" (l530-531). Either the purchase was at or below book value, or the consideration was small. The deck discloses no consideration for Kidcity. Ask for the consideration, the net assets acquired, and any capital reserve. |
| A3-04 | F1 | R422-R425; R432-R433, R365 | l591, l593 S30 | "Cash and bank balances 2 12 0 0" | AMBIGUOUS | Cash rounds to zero at FY25 and FY26. Over the same span, other financial assets went from 1 to 22 (l593) and short-term borrowings reached 75 (l591). Either liquidity sits in "other financial assets" (deposits or margin money), or the company runs on fully drawn working-capital lines. Ask what the Rs 22 Cr comprises and whether any of it is restricted. |
| A3-05 | F6 | R474, R016 | l139-140 S7 | "Kiosks: Targeting 55+ on airports, high end streets" | FORWARD-SIGNAL | This is a numeric target with no date and no current count. Ask for the count at H1FY27, the target date, capex per kiosk, and whether the kiosks are owned or franchised. Add it to the Role 5 promise tracker. |
| A3-06 | F6 | R501, R549, R522 | l448, l460 S24 | "2028: Accelerating the Next Growth Phase" | FORWARD-SIGNAL | The chart sets 2028 on the axis but prints no 2028 value. Management signals a target without stating it. Ask for the 2028 revenue and PBT figures, and whether "2028" means FY28 or CY28. This is the deck's only dated forward horizon. |
| A3-07 | F6 | R492 | l413 S22 | "Strengthens brand visibility with EBO and KIOSK expansion." | FORWARD-SIGNAL | Exclusive brand outlets (EBOs) appear only here. The omnichannel slide (l126-148) lists no EBOs and the deck gives no count. Ask for the current EBO count, the plan, and the capex per store. A new owned-retail format changes capital intensity. |
| A3-08 | F10 | R197-R204, R322-R329, R330-R333 | l305 S14; l571-572 S29; l580 S30 | "EPS Diluted (INR) 2.01 3.29 (38.9%)" | AMBIGUOUS | **EPS is not restated for the bonus issue.** Implied weighted shares (derived as PAT / EPS): FY25 18/14.54 = 1.24 Cr, which matches capital of 12 Cr at Rs 10 face value. FY26: 28/6.72 = 4.2 Cr. Q2FY26: 9.45/3.29 = 2.9 Cr. H1FY26: 12.5/6.07 = 2.1 Cr. Q1FY27: about 6.4 Cr. These step changes fit a 5x bonus allotted around Aug-2025 and then time-weighted, not adjusted retrospectively as AS 20 and Ind AS 33 require. The printed EPS falls of (38.9%) and (43.2%) are artefacts. On a bonus-adjusted basis, Q2 EPS rose about 30%. Check the filed results' comparative EPS: a deck-only error is a drafting issue, while an error in the filing is an accounting-compliance issue. |
| A3-09 | F10 | R197, R200, R202; R189, R192, R194 | l305, l304 S14 | "2.01 ... 1.44 ... 3.45" | AMBIGUOUS | Implied diluted shares, derived from PAT margin x revenue, divided by EPS: Q1FY27 = 9.2/1.44 = about 6.3-6.5 Cr. Q2FY27 = 14.2/2.01 = about 7.0-7.1 Cr, up about 10-12% QoQ. FY26 paid-up capital is 62 Cr, about 6.2 Cr shares. H1 is consistent: 23.4/3.45 = 6.8 Cr. The deck does not show basic EPS by quarter. Readings: a preferential issue, warrants or ESOPs in Q2FY27; or attributable PAT differs from consolidated PAT through the 25% minority interest in Kidcity. Check the shareholding pattern and any allotment filings for Jul-Sep 2026. |
| A3-10 | F11 | R255, R363, R423, R343, R347 | l522 S27; l586, l591 S30 | "1.0x" (FY24 Net Debt / Equity) | NEUTRAL-FACT | FY24 computed on a net basis: (2 + 50 - 12)/53 = 0.75x. The printed figure is 1.0x, which equals gross debt over equity (0.98x), a gap of more than 5%. FY23 at 2.8x matches the net basis ((52 - 2)/18 = 2.78x). The definition is therefore inconsistent across years. Possible reconciling item: the FY24 cash of 12 Cr was restricted (IPO escrow or margin money). The "sharp reduction" story is overstated for FY24 only in definition, not in direction. |
| A3-11 | F11 | R398-R401, R426-R433, R362-R365, R294-R297 | l584, l592-593, l591 S30; l564 S29 | "Non-Current Investments 0 0 9 20" / "Other financial assets 0 0 1 22" | AMBIGUOUS | Investments plus short-term loans and advances plus other financial assets: FY24 = 1, FY25 = 19 (27% of equity), FY26 = 57 (20 + 15 + 22, 58% of equity of 98). Over the same period, short-term borrowings rose 59 to 75 and other income rose 4 to 9. Elementa (Rs 2 Cr) explains little of the Rs 20 Cr of investments. Lean bear: capital is leaving the operating business, partly funded by debt. Ask for counterparties, related-party status, interest rates and the nature of each item. |
| A3-12 | F14 | R516, R518, R543, R544, R096-R200 (Q1 column) | l268, l278 S13; l289-290 S14 | "Q1 FY26" / "Q2FY27 Q2FY26 Y-o-Y (%) Q1FY26 Q-o-Q (%)" | NEUTRAL-FACT | The "Q1FY26" column holds Q1 FY27 data. Proof: H1FY27 180 = Q2FY27 106 + 74. Actual Q1FY26 = H1FY26 103 - Q2FY26 70 = 33. The Q1 EPS of 1.44 implies about 6.4 Cr shares, which is the post-bonus count. The panel headers "Q1 FY26" (l268) and "H1 FY26" (l278) are also mislabelled. Implications: Q1FY27 grew about 124% YoY (74 vs 33), and quarterly revenue is strongly seasonal. |
| A3-13 | F14 | R259, R529, R330-R333 | l536-537 S28; l580 S30 | "completed a bonus share in the ratio of 1:4" | AMBIGUOUS | Equity capital went 12 to 62 (l580), a factor of 5.2. "1:4" in standard notation means 1 bonus share for 4 held, which would give a factor of 1.25. The arithmetic fits 4 bonus shares for 1 held. Either the ratio is misprinted, or capital also rose for another reason. A fresh issue would have to be about 47 Cr at face value. Confirm from the record-date filing. |
| A3-14 | F14 | R238, R265, R226 | l496 S27 vs l556 S29, l456 S24 | "24915.0%" (249 concatenated with 15.0%) | NEUTRAL-FACT | FY26 revenue prints as 249 on S27 and as 248 on S24 and S29. The difference is immaterial alone. It adds to the deck's cumulative drafting record with A3-12 and A3-13. |
| A3-15 | F14 | R544, R551, R552 | l289 S14; l554-555 S29; l576-577 S30 | "Particulars (INR Cr)" | AMBIGUOUS | The deck never says "Consolidated" or "Standalone". The minority interest (l583) and associate (l297) lines imply consolidated figures. The tables use the Indian GAAP Schedule III Division I format (Reserves & Surplus, Short term provisions). F2 and F3 cannot be run. Ask which basis is used, and get the standalone figures from the results filing. |
| A3-16 | F15 | R461, R469, R528, R338-R341 | l421 S23; l529-533 S28; l583 S30 | "Karnika + KidCity Acquisition Rationale" / "Non Controlling Interest 0 0 0 2" | AMBIGUOUS | The minority interest is 0 for FY23-FY25 and 2 at FY26, so Kidcity enters the consolidation only in FY26. A1 maps the acquisition to 2024 by chart x-position, but the text position falls nearer the 2025 column. The H1FY27 deck still carries an "Acquisition Rationale" slide for a deal described as done. Readings: a carried-over slide; or a further step is planned (the remaining 25%, or a merger). Ask for the acquisition date and consideration, and whether more steps are planned. |
| A3-17 | F15 | R470, R260, R261, R530 | l539-544 S28 | "Elementa Lifespaces: 40% stake acquired for Rs. 2 crore." | AMBIGUOUS | A new associate was added in 2026, and its loss appears first in Q2FY27 (A3-01). The deck does not describe Elementa's business or its fit with kidswear. Ask about its business, its related-party status, and any further capital commitment. Prior-quarter entity diff: not runnable, because there is no prior extract. |
| A3-18 | F15 | R468, R525 | l532-533 S28 | "Operations restructured under Karni International" | AMBIGUOUS | The 2017 restructuring entity is not named in the deck's group structure. Its current relationship is not stated (subsidiary, merged, partnership or related party). Ask whether Karni International still exists and whether it trades with Karnika. |
| A3-19 | F16 | R054, R290-R297, R306-R309 | l233-235 S10; l563-564 S29 | "Healthy PAT margins reflecting strong operating discipline and efficient" | AMBIGUOUS | FY26 PAT margin rose 100 bps (10.4% to 11.4%) while EBITDA margin fell 10 bps (15.1% to 15.0%). Other income rose 4 to 9, which is 23% of FY26 PBT of 39. Derived: FY26 other income 9 minus H1FY26 other income 1 leaves about 7-9 Cr in H2FY26, about 36% of H2FY26 PBT of about 22. The margin expansion is non-operating. It links to the financial assets in A3-11. Ask what made up FY26 other income. |
| A3-20 | F16 | R081, R082, R115, R289, R293 | l280 S13; l562-563 S29 | "Margins 18.9% 18.2%" (H1 EBITDA) | FORWARD-SIGNAL | H1FY26 EBITDA margin was 18.9%; FY26 full year was 15.0%. Derived H2FY26: EBITDA 37 - 19.5 = 17.5 on revenue 248 - 103 = 145, a 12.1% margin. Margins are strongly seasonal, with H1 high and H2 low. H1FY27 at 18.2% should not be annualised, and a lower H2FY27 margin is the base expectation. Ask what drives the H2 margin dip. |
| A3-21 | F16 | R045-R049, R266-R293; R029-R036 | l217-218 S10; l557-563 S29; l172, l175 S8 | "Our Gross Margins reflect product mix transition and input cost" | AMBIGUOUS | Gross margin fell from 50.4% to 33.6% (FY23-FY26), yet EBITDA margin rose from 12.2% to 15.0%. Other operating expenses fell from 41 to 39 while revenue grew 98%. In FY25-FY26 alone, COGS rose from 55.4% to 66.5% of revenue and other opex fell from 26.0% to 15.7%. About 10 points moved between the two lines in one year. "Mix and input cost" does not explain falling opex. Readings: costs were reclassified (for example, job-work charges moved into COGS), or the mix shifted to low-margin traded goods or fabric. In the S8 chart, stack position 4 goes 9% (FY25) to 28% (FY26) to 7% (H1FY27); the legend mapping is not in the text, but if that position is "Fabric", it fits. The separating observation is category revenue in Rs and the cost-line definitions. |
| A3-22 | F16 | R480, R484, R485, R212, R386-R393 | l209-211 S10; l325-330 S16; l580-582 S30 | "Return Ratios Adjusting with Capacity & Capital Expansion" vs "SCALABLE CAPACITY WITHOUT ADDITIONAL CAPEX ON" | AMBIGUOUS | One slide is titled "Investment-Led Transition Phase" and cites capacity expansion. Another claims growth needs no plant capex, at 90%+ utilisation of all plants. PPE fell from 7 to 6 and capital work in progress is 1. The investment visible on the balance sheet is financial (A3-11), not capacity. Return ratios also rose rather than "adjusted". Ask: what is being invested in, and how does growth continue at 90%+ utilisation without capex? |
| A3-23 | F16 | R254-R257, R362-R365 | l516 S27; l591 S30; l535 S28 | "Sharp Reduction in Leverage Levels" | NEUTRAL-FACT | Short-term borrowings rose from 52 (FY23) to 75 (FY26), up 44%. The ratio fell because equity grew through the IPO and retained earnings, not because debt fell. The IPO slide says "Funds utilized for debt reduction" (l535), but absolute debt is higher. Debt still funds working capital and the financial assets in A3-11. |
| A3-24 | F16 | R472, R486, R220, R221, R527 | l351 S18; l356-357 S18; l546 S28 | "Expanding Global Footprint." vs "<1% Revenue from Exports (H1FY27)" | CONFIRMATORY-NEGATIVE | Exports were "initiated" in 2023 (l546) and are below 1% of revenue three years later. The headline framing ("Expanding Global Footprint") runs ahead of delivery. Give the export optionality no weight until a revenue figure is disclosed. |
| A3-25 | F16 | R010, R210, R548, R252, R012 | l101-102 S5; l316 S16; l519 S27; l104-106 S5 | "32% ROCE (H1FY27)" / "26%" | AMBIGUOUS | One deck gives three ROCE figures: 32% (H1FY27, l101-102), 26% with no period (l316), and 25.5% (FY26, l519). FY26 ROCE (derived, 25.3%) counts other income of 9 within EBIT of 44. Excluding other income it is about 20%. The H1FY27 ROCE and the 0.6x net debt/equity (l104-106) cannot be checked, because the deck has no H1FY27 balance sheet or cash flow. Ask for the definition and the H1 balance sheet, or pull them from the results filing. |
| A3-26 | F16 | R209, R205-R208, R546-R547, R414-R421 | l90-92 S5; l324, l333 S16; l589-590 S30 | "Asset-Light Model Delivering Superior Capital Efficiency" | AMBIGUOUS | Trade receivables are 88 Cr, about 130 days of FY26 revenue (158 days in FY25, 117 in FY23). Inventories are 58 Cr, about 128 days of COGS. Together that is 146 Cr against PPE of 6. FATR excludes working capital. The H1FY27 FATR of 75x annualised implies average PPE of about 4.8 Cr, which FY26 PPE of 6 and H1 depreciation of 0.4 do not reproduce. Capital intensity sits in working capital. Ask for receivable days at H1FY27 and the FATR denominator. |
| A3-27 | F16 | R472 (positioning), R002 | l87-88 S5 | "India’s largest Integrated Kidswear Platform at Scale" | AMBIGUOUS | A superlative at Rs 248 Cr revenue, with no source given. Ask for the comparison basis and the peers counted. Treat it as tone evidence, not as a fact. |

Checks F2, F3, F4, F5, F9, F12, F13 and F17 are N.A. F7 and F8 are PASS. Bases are in the scorecard.

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 42 ZERO_STANDING rows read. Four carry a forward question: the associate line activated (A3-01), provisions zero (A3-02), goodwill zero despite Kidcity (A3-03), cash zero (A3-04). FY23 depreciation 0, deferred tax liability 0 and capital work in progress 0 for FY23-FY25 are rounding or consistent with an asset-light model. |
| F2 Standalone vs consolidated | N.A. | The deck shows one basis, unlabelled; consolidated is inferred from the minority interest and associate lines (A3-15). No S-vs-C gap can be computed. |
| F3 Shell-entity detection | N.A. | No standalone cost lines to compare. |
| F4 Unaudited contribution ratio | N.A. | No auditor report in the deck. The cover says "Un-Audited Financial Results" (l29). |
| F5 Going concern / EoM tracking | N.A. | No emphasis-of-matter text in the deck, and no prior-quarter extract. |
| F6 Forward-commitment mining | FINDING | Lexicon hits in the body: "initiated" (l546) and "completed" (l536). "will be" appears only in the disclaimer (l53). Non-lexicon dateable targets: kiosks 55+ (A3-05), 2028 phase (A3-06), EBO expansion (A3-07). Register in section 3. |
| F7 Hedge-phrase mining | PASS | Lexicon hits ("subject to" l54, "could cause" l60) sit only in the standard safe-harbour paragraph (l53-64). The deck body has no hedges, and there is no prior deck to diff. |
| F8 Tax forensics | PASS | Effective tax rate, derived from margin-recovered figures: Q2FY27 26.0%, Q1FY27 28.3%, H1FY27 27.4%, H1FY26 26.2%. Printed annual figures: FY26 25.6%, FY25 25.0%, FY24 21.4%, FY23 27%. All sit near the statutory 25.17%, and the H1FY27 gap of about 2 points fits a non-deductible associate loss. Deferred tax asset of 1 at FY26 only, immaterial. No earlier-year tax line. |
| F9 OCI forensics | N.A. | The deck has no OCI line. |
| F10 Share count and dilution | FINDING | Capital went 12 to 62 in FY26. EPS is not bonus-adjusted (A3-08). Implied diluted shares rose about 11% QoQ in Q2FY27 (A3-09). Basic EPS equals diluted EPS in every annual year (l571-572); basic EPS is absent for the quarters. |
| F11 Reserves and net worth tie-out | FINDING | Equity ties: FY23 9+9+0 = 18; FY24 12+41+0 = 53; FY25 12+58+0 = 70 vs 71 (rounding); FY26 62+34+2 = 98. FY26 reserves: 58 + 28 - 50 (bonus capitalised) = 36 vs 34, a gap of about 2 (dividend, minority share or rounding). Balance sheets foot within 1. Net D/E definition inconsistent for FY24 (A3-10). Financial assets reach 58% of net worth (A3-11). |
| F12 Segment forensics | N.A. | No segment assets or liabilities. The category mix is shown in % only, with an unresolved legend mapping (used in A3-21). |
| F13 Board outcome beyond results | N.A. | The deck reports no board outcome. The director roster (l470-486) shows 3 executive directors, 1 non-executive and 2 independent directors, with no term dates. |
| F14 Drafting inconsistencies | FINDING | Mislabelled Q1 column and panel headers (A3-12). Bonus ratio vs capital (A3-13). Revenue 249 vs 248 (A3-14). Basis unlabelled (A3-15). |
| F15 Entity list diffs | FINDING | No prior list exists, so no quarter-over-quarter diff was possible. Within the deck: Kidcity enters the consolidation in FY26 while the timeline says 2024 (A3-16); the Elementa associate was added in 2026 (A3-17); Karni International's relationship is unstated (A3-18). |
| F16 Dropped / reframed disclosures | FINDING | No prior deck, so dropped-metric diffs were not assessed. In-deck reframings: A3-19 to A3-27. The H1 balance sheet and cash flow are absent although the deck quotes H1 ratios (A3-25). |
| F17 Silence audit | N.A. | Concall-specific check; this document is a presentation. No Notion checklist and no companies/KARNIKA.md exist (pre-thesis read). |

## 3. COMMITMENT REGISTER (F6)

| # | Commitment | Implied date | Ref | Status word |
|---|---|---|---|---|
| C1 | Kiosks: "Targeting 55+ on airports, high end streets" | none stated | S7 l139-140 (R474) | targeted (no baseline count) |
| C2 | Shop-in-shop expansion "within leading retail destinations"; "SIS: 85+ (as of H1FY27)" | none stated | S7 l141-148 (R475, R017) | underway |
| C3 | "EBO and KIOSK expansion" | none stated | S22 l413 (R492) | stated (no baseline) |
| C4 | "2028: Accelerating the Next Growth Phase": brand amplification, distribution expansion, operational efficiencies | 2028 (FY or CY not stated) | S24 l448-460 (R501, R549) | stated (no figure) |
| C5 | "expanding export presence" | none stated | S5 l95; S18 l356-357; S28 l546 | initiated (2023); below 1% of revenue in H1FY27 |
| C6 | "superior ROCE and ROE trajectory over the medium term" | medium term | S10 l232-234 (R480) | stated |
| C7 | "SCALABLE CAPACITY WITHOUT ADDITIONAL CAPEX ON PLANT" | none stated | S16 l328-330 (R484, R485) | stated (testable via PPE and capital work in progress) |
| C8 | "Forward integration into retail"; reach "across Tier 2 & Tier 3 markets" | none stated | S22 l407, l411 (R487, R490) | stated |
| C9 | "Going forward, our focus remains on expanding market reach, strengthening brand equity ... maintaining profitability and financial discipline" | none stated | S12 l257-261 (R482) | stated |
| C10 | "Acquired a 75% controlling stake in Kidcity" | 2024 per timeline position; the minority interest suggests FY26 | S28 l529-533 (R469, R258) | completed |
| C11 | "Bonus Issue Successfully completed a bonus share in the ratio of 1:4" | 2025 (FY26) | S28 l535-537 (R259) | completed |
| C12 | "Elementa Lifespaces: 40% stake acquired for Rs. 2 crore" | 2026 | S28 l539-544 (R470, R261) | completed |
| C13 | IPO "Funds utilized for debt reduction, working capital support, and modernization initiatives" | 2022-23 | S28 l532-537 | completed (utilized) |
| C14 | "Installed automated machinery, implemented ERP systems, and initiated export operations" | 2023 | S28 l539-548 | implemented / initiated |

## 4. FLAGS FOR A4 (management questions)

- FORWARD-SIGNAL: A3-05, A3-06, A3-07, A3-20.
- AMBIGUOUS: A3-01, A3-02, A3-03, A3-04, A3-08, A3-09, A3-11, A3-13, A3-15, A3-16, A3-17, A3-18, A3-19, A3-21, A3-22, A3-25, A3-26, A3-27.
- Priority order for A4:
  1. A3-11 + A3-19: 57 Cr of financial assets alongside rising other income and debt.
  2. A3-08 + A3-09 + A3-13: bonus-adjusted share count, and the possible Q2 dilution.
  3. A3-20: H2 margin seasonality.
  4. A3-21: gross margin collapse versus falling opex.
  5. A3-16 + A3-17: Kidcity and Elementa.
  6. A3-06: the 2028 figure.

## 5. YAML BLOCK

```yaml
stage: A3-forensics
company: "KARNIKA"
quarter: "h1fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/karnika-h1fy27/work/forensics_presentation_karnika_h1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: PASS
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "l297 S14; l540-544 S28", classification: "AMBIGUOUS", implication: "Associate line first non-zero in Q2FY27 at (0.2) Cr, about 10% of the Rs 2 Cr Elementa cost in one quarter; H1FY27 cell prints 0, inconsistent with Q1 0 + Q2 (0.2)"}
  - {id: "A3-02", check: "F1", line: "l588, l594 S30", classification: "AMBIGUOUS", implication: "Long- and short-term provisions zero in all four years despite 4 plants and Rs 8 Cr employee cost; gratuity funded, below rounding, or not provided (AS 15)"}
  - {id: "A3-03", check: "F1", line: "l583 S30; l530-531 S28", classification: "AMBIGUOUS", implication: "Goodwill zero in all years despite the 75% Kidcity stake; consideration undisclosed"}
  - {id: "A3-04", check: "F1", line: "l591, l593 S30", classification: "AMBIGUOUS", implication: "Cash zero at FY25 and FY26 while other financial assets reach 22 and ST borrowings 75; liquidity location and restriction unknown"}
  - {id: "A3-05", check: "F6", line: "l139-140 S7", classification: "FORWARD-SIGNAL", implication: "Kiosk target 55+ with no date or baseline; Role 5 tracker item"}
  - {id: "A3-06", check: "F6", line: "l448, l460 S24", classification: "FORWARD-SIGNAL", implication: "2028 growth-phase slide with 2028 axis unvalued; undisclosed target, ask for the figure and FY/CY"}
  - {id: "A3-07", check: "F6", line: "l413 S22", classification: "FORWARD-SIGNAL", implication: "EBO expansion named only here, no count; new owned-retail format changes capital intensity"}
  - {id: "A3-08", check: "F10", line: "l305 S14; l571-572 S29; l580 S30", classification: "AMBIGUOUS", implication: "EPS not bonus-adjusted (implied shares 1.24/2.1/2.9/4.2/6.4 Cr); printed EPS falls (38.9%)/(43.2%) are artefacts; adjusted Q2 EPS up about 30%; check filed results for AS 20 compliance"}
  - {id: "A3-09", check: "F10", line: "l304-305 S14", classification: "AMBIGUOUS", implication: "Implied diluted shares about 6.4 Cr in Q1FY27 rising to about 7.06 Cr in Q2FY27, up about 11% QoQ vs 6.2 Cr paid-up; possible allotment, warrants or minority-interest effect"}
  - {id: "A3-10", check: "F11", line: "l522 S27; l591 S30", classification: "NEUTRAL-FACT", implication: "FY24 net D/E printed 1.0x vs 0.75x computed net (gross basis 0.98x); definition inconsistent with FY23 2.8x"}
  - {id: "A3-11", check: "F11", line: "l584, l591-593 S30; l564 S29", classification: "AMBIGUOUS", implication: "Investments + loans + other financial assets went 1 (FY24) to 19 (FY25) to 57 Cr (FY26), 58% of net worth, while ST debt rose 59 to 75; capital leaving operations, debt-funded; counterparties unknown"}
  - {id: "A3-12", check: "F14", line: "l268, l278 S13; l289-290 S14", classification: "NEUTRAL-FACT", implication: "Q1FY26 column is Q1FY27 data (180 = 106 + 74; actual Q1FY26 = 33); Q1FY27 YoY about +124%; strong seasonality"}
  - {id: "A3-13", check: "F14", line: "l536-537 S28; l580 S30", classification: "AMBIGUOUS", implication: "Bonus printed 1:4 but capital rose 12 to 62 (5.2x), which fits 4 bonus for 1 held; confirm from record-date filing"}
  - {id: "A3-14", check: "F14", line: "l496 S27; l456 S24; l556 S29", classification: "NEUTRAL-FACT", implication: "FY26 revenue 249 vs 248 across slides; cumulative drafting record"}
  - {id: "A3-15", check: "F14", line: "l289 S14; l554-555 S29; l576-577 S30", classification: "AMBIGUOUS", implication: "Deck never states consolidated vs standalone; minority-interest and associate lines imply consolidated; F2/F3 not runnable from the deck"}
  - {id: "A3-16", check: "F15", line: "l421 S23; l529-533 S28; l583 S30", classification: "AMBIGUOUS", implication: "Kidcity minority interest first appears FY26 vs timeline 2024; Acquisition Rationale slide still in H1FY27 deck; possible further step (remaining 25%/merger)"}
  - {id: "A3-17", check: "F15", line: "l539-544 S28", classification: "AMBIGUOUS", implication: "Elementa Lifespaces 40% associate added 2026; business and related-party status undisclosed; first loss in Q2FY27"}
  - {id: "A3-18", check: "F15", line: "l532-533 S28", classification: "AMBIGUOUS", implication: "Karni International (2017 restructuring entity) current relationship unstated"}
  - {id: "A3-19", check: "F16", line: "l233-235 S10; l563-564 S29", classification: "AMBIGUOUS", implication: "FY26 PAT margin +100 bps on flat EBITDA margin; other income 4 to 9 Cr (23% of PBT), about 7-9 Cr of it in H2FY26 (about 36% of H2 PBT); margin expansion is non-operating"}
  - {id: "A3-20", check: "F16", line: "l280 S13; l562-563 S29", classification: "FORWARD-SIGNAL", implication: "H1FY26 EBITDA margin 18.9% vs FY26 15.0%; implied H2FY26 about 12.1%; do not annualise H1FY27 18.2%, expect lower H2"}
  - {id: "A3-21", check: "F16", line: "l217-218 S10; l557-563 S29; l172, l175 S8", classification: "AMBIGUOUS", implication: "Gross margin 50.4% to 33.6% while EBITDA margin rose and opex fell 41 to 39 on +98% revenue; about 10 pts moved COGS vs opex in FY26; reclassification or low-margin fabric/trading mix"}
  - {id: "A3-22", check: "F16", line: "l209-211 S10; l325-330 S16; l580-582 S30", classification: "AMBIGUOUS", implication: "Investment-Led/capacity expansion title vs no-capex claim at 90%+ utilisation; PPE 7 to 6, CWIP 1; the investment is financial not capacity"}
  - {id: "A3-23", check: "F16", line: "l516 S27; l591 S30; l535 S28", classification: "NEUTRAL-FACT", implication: "Leverage ratio fell on equity growth; ST borrowings rose 52 to 75 (+44%) despite IPO debt-reduction claim"}
  - {id: "A3-24", check: "F16", line: "l351, l356-357 S18; l546 S28", classification: "CONFIRMATORY-NEGATIVE", implication: "Exports below 1% of H1FY27 revenue three years after initiation; Expanding Global Footprint framing unearned"}
  - {id: "A3-25", check: "F16", line: "l101-102, l104-106 S5; l316 S16; l519 S27", classification: "AMBIGUOUS", implication: "ROCE shown as 32%/26%/25.5%; FY26 ROCE includes 9 Cr other income (about 20% ex other income); no H1 balance sheet or cash flow to verify H1 ratios"}
  - {id: "A3-26", check: "F16", line: "l90-92 S5; l324, l333 S16; l589-590 S30", classification: "AMBIGUOUS", implication: "Asset-light claim vs receivables about 130 days and inventory about 128 days (146 Cr vs PPE 6); H1FY27 FATR 75x not reproducible"}
  - {id: "A3-27", check: "F16", line: "l87-88 S5", classification: "AMBIGUOUS", implication: "Unsourced India's largest integrated kidswear platform claim at Rs 248 Cr revenue; tone evidence only"}
forward_signals: ["A3-05", "A3-06", "A3-07", "A3-20"]
ambiguous: ["A3-01", "A3-02", "A3-03", "A3-04", "A3-08", "A3-09", "A3-11", "A3-13", "A3-15", "A3-16", "A3-17", "A3-18", "A3-19", "A3-21", "A3-22", "A3-25", "A3-26", "A3-27"]
commitments:
  - {commitment: "Kiosks targeting 55+ on airports, high end streets", implied_date: "none stated", ref: "S7 l139-140", status_word: "targeted"}
  - {commitment: "SIS expansion; 85+ as of H1FY27", implied_date: "none stated", ref: "S7 l141-148", status_word: "underway"}
  - {commitment: "EBO and kiosk expansion", implied_date: "none stated", ref: "S22 l413", status_word: "stated"}
  - {commitment: "2028 next growth phase (brand, distribution, efficiencies); no figure", implied_date: "2028", ref: "S24 l448-460", status_word: "stated"}
  - {commitment: "Expanding export presence (<1% of H1FY27 revenue)", implied_date: "none stated", ref: "S5 l95; S18 l356-357; S28 l546", status_word: "initiated"}
  - {commitment: "Superior ROCE/ROE trajectory over the medium term", implied_date: "medium term", ref: "S10 l232-234", status_word: "stated"}
  - {commitment: "Scalable capacity without additional plant capex", implied_date: "none stated", ref: "S16 l328-330", status_word: "stated"}
  - {commitment: "Forward integration into retail; Tier 2/3 reach", implied_date: "none stated", ref: "S22 l407, l411", status_word: "stated"}
  - {commitment: "Kidcity 75% controlling stake", implied_date: "2024 per timeline; FY26 per minority interest", ref: "S28 l529-533", status_word: "completed"}
  - {commitment: "Bonus issue printed 1:4", implied_date: "2025 (FY26)", ref: "S28 l535-537", status_word: "completed"}
  - {commitment: "Elementa Lifespaces 40% for Rs 2 crore", implied_date: "2026", ref: "S28 l539-544", status_word: "completed"}
  - {commitment: "IPO funds utilized for debt reduction, WC, modernization", implied_date: "2022-23", ref: "S28 l532-537", status_word: "completed"}
  - {commitment: "Automation, ERP, export operations", implied_date: "2023", ref: "S28 l539-548", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis read; no prior deck, so diffs ran within the deck only. Three threads matter. (1) Earnings quality: FY26 PAT margin rose 100 bps on a flat EBITDA margin. Other income rose 4 to 9 Cr, about 7-9 Cr of it in H2FY26. Investments, loans and other financial assets rose from 1 Cr (FY24) to 57 Cr (FY26), 58% of net worth, while short-term debt rose to 75 Cr. Get the counterparties and the related-party schedule from the results filing or the AR. (2) Seasonality: H1 EBITDA margins run near 18-19%; the implied H2FY26 margin was about 12%. Do not annualise H1FY27. (3) Share count: deck EPS is not bonus-adjusted, so the printed EPS declines are artefacts. Separately, implied diluted shares rose about 11% QoQ in Q2FY27; check for an allotment or warrants. The column labelled Q1FY26 holds Q1FY27 data. Pipeline notes: A1 line cites drift by 1-10 lines on 11 rows; the values were verified at adjacent lines. The A2 RESTATED flag on ROE/ROCE is not upheld: values match across the two slides, and the series were resolved by computation."
```
