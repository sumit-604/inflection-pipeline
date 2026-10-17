# A3 FORENSIC NOTES - Aurum PropTech Ltd (AURUM) - Q2 FY27 - doctype: PRESENTATION

Inputs read: A1 structured (R001-R367), A1 fulltext (lines 1-1081, all 38 pdf pages), A2 ledger (367 rows).
Prior-quarter fulltext: not available. Prior-quarter context comes only from the task message (Notion record of the Q1 FY27 deck).
Source PDF and inputs/ were not opened.
Slide convention: deck slide N = pdf page N+1. Line numbers below are A1 fulltext lines.

## 0. Reconciliation against the A2 ledger

- Ledger rows: 367. Rows read at the cited fulltext line: 367. Reconciled: 100%.
- A2 count test: gate_a2 pass. ZERO_STANDING rows: 0. Orphan IDs: none.
- A2 VALUE_CONFLICT R020/R269: resolved on arithmetic below (FN-01). The deck's own build-up supports 3.1%, not -3.2%.
- A1 pointer defects (pipeline data quality, not company findings):
  - R078 and R079 say "text at line 149". The slide 5 footnote text is at line 187.
  - R151 says "text at line 344". The slide 12 footnote text is at line 382.
  - These pointers do not change any value. A4 should cite lines 187 and 382.

Applicability rule used. A check runs when the deck carries its subject matter. A check is N.A. when the deck has no such content (no statutory P&L, no notes, no auditor letter, no balance sheet). This follows the doctype line "F16 applies plus any F6/F10/F11 numbers the deck carries". On that basis F6, F7, F12, F14, F15 and F16 run. The deck carries no share-capital, EPS or net-worth numbers, so F10 and F11 are N.A.

## 1. Arithmetic tie-out of slide 29 (pdf p30, lines 816-840)

| Line item (Rs Cr) | Q2 FY26 | Q2 FY27 | Check |
|---|---|---|---|
| Adjusted Income TIr (L823) | 84.80 | 134.81 | |
| + RoU other income (L824) | 2.86 | 2.50 | |
| Total Income TI (L826) | 87.66 | 137.31 | ties |
| - Employee benefits & other expenses (L827) | 61.25 | 96.33 | |
| EBITDA (L828) | 26.41 | 40.98 | ties |
| EBITDA/TI (L817) | 30.1% | 29.8% | ties (30.13%, 29.84%) |
| + ESOP (L831), - RoU OI (L832), - lease payments (L834) | 0.38 / 2.86 / 21.28 | 1.21 / 2.50 / 24.25 | |
| Adjusted EBITDA (L835) | 2.65 | 15.44 | ties |
| Adj EBITDA / TIr computed | 3.125% | 11.45% | L818 shows -3.2% for Q2 FY26: does NOT tie |
| - ESOP, - finance, - depreciation, - Ind AS impact (L836-839) | 0.38 / 1.24 / 5.73 / 2.27 | 1.21 / 0.01 / 6.44 / 1.19 | |
| PBT before exceptional items (L840) | -6.96 | 6.60 | ties (-6.97, 6.59 on rounding) |
| PBT/TI (L816) | -7.9% | 4.8% | ties |
| Total income growth | | 56.6% | ties to "57% YoY" (L92) |

Adjusted EBITDA margin bridge (share of TIr, Q2 FY26 to Q2 FY27, computed from L823-835):
- EBITDA/TIr: 31.14% to 30.40% = -75 bps
- ESOP add-back: 0.45% to 0.90% = +45 bps
- RoU other income deduction: 3.37% to 1.85% = +152 bps
- Long-term lease payments: 25.09% to 17.99% = +711 bps
- Total: +833 bps (deck: "+840 bps", L95, on rounded 11.5% less 3.1%)

PBT swing +13.56 Cr: Adjusted EBITDA +12.79, finance cost +1.23, Ind AS impact +1.08, ESOP -0.83, depreciation -0.71.

Segment tie-out (slide 4, lines 118-150):
- Segment revenue: 56 + 70 + 4 = 130 Cr (each rounded; range 128.5-131.5).
- Total income 137.31 (L826) less 130 = 7.31 Cr implied other income (range 5.81-8.81). It includes RoU other income 2.50 (L824). The deck has no other-income line: NOT FOUND as a disclosed figure.
- Slide 3 "Others" 11 Cr (L108) = Capital 4 Cr (L121) + about 7 Cr other income. Slide 3 presents other income inside the revenue mix.
- Segment profit: 0.93 + 11 + 0.45 = 12.38 Cr (range 11.88-12.88). Less unallocable 5.95 (L150) = 6.43 (range 5.93-6.93). PBT 6.60 (L840) sits inside that range.
- Result: segment profits less 5.95 already equal PBT. The 7.31 Cr other income has no separate place in the bridge (see FN-05).
- PBT ex other income, derived: 6.60 - 7.31 = -0.71 Cr (range -2.21 to +0.79 on segment rounding). The sign cannot be fixed from the deck.

## 2. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F14 | R020, R269, R287, R271, R022 | L97 (slide 3) vs L818 (slide 29) | slide 3 "3.1%"; slide 29 "Adjusted EBITDA / Adjusted Income (%) ... -3.2%" | AMBIGUOUS | The same metric and period carry two values. The build-up rows (L835 2.65 / L823 84.80 = 3.1%) and the "+840 bps" claim (L95) support 3.1%. If -3.2% is the figure the Q2 FY26 deck published, the base period was restated upward. A4 question: which value is correct, and was Q2 FY26 Adjusted EBITDA restated from the figure first published? |
| FN-02 | F14 | R302, R275, R276, R277, R278, R121 | L820-822, L827 (slide 29); L247 (slide 7) | "the business has demonstrated improving Expense to Total Income ratios from Q2FY26 to Q2FY27" | FORWARD-SIGNAL | The deck's own expense line contradicts the claim. Employee + other expenses / TI = 61.25/87.66 = 69.9% to 96.33/137.31 = 70.2%, so 28 bps worse. Expenses grew 57.3% against income growth of 56.6%. This also contradicts "Automation lets volumes scale without proportional growth" (L247). The claim holds only if lease payments count as expense, and that is a mix effect (FN-03). No operating leverage shows on the reported cost base. |
| FN-03 | F16 | R021, R022, R054, R267, R268, R285, R286, R304 | L817, L818, L834 (slide 29); L91-97 (slide 3) | "EBITDA / Total Income (%) 30.1 % 29.8 %"; "Less: Long term lease payments 21.28 24.25" | FORWARD-SIGNAL | The headline metric is Adjusted EBITDA margin, +840 bps. Reported EBITDA margin fell 30 bps. The bridge shows +711 bps from lease payments falling as a share of income and +152 bps from a lower RoU other-income deduction, against -75 bps on underlying EBITDA. The margin gain comes from a mix shift away from leased co-living, not from scale. Housing.com joins the mix next quarter, so the next margin print measures mix, not efficiency. |
| FN-04 | F16 | R286, R285, R058, R059 | L834 (slide 29); L169 (slide 5) | "Less: Long term lease payments 21.28 24.25"; "16,502 (-14%) ... No. of Beds under Management" | AMBIGUOUS | Lease payments rose 14.0% YoY while co-living beds fell 14%. If lease payments track co-living beds, lease outgo per bed rose about 32% (Rs 1.11 lakh to Rs 1.47 lakh per quarter). The deck does not split co-living leases from office or other leases. A4 question: lease payments by business (HelloWorld, Nestaway, offices); whether exits from 5-7 year landlord agreements (L595-598) carry exit or overlap costs. |
| FN-05 | F12 | R049, R050, R051, R038, R039, R040, R035, R036, R037, R276, R298 | L150, L126 (slide 4); L826, L840 (slide 29) | "Other income excluded from segmental income. Finance cost & other un-allocable expense of ₹5.95 crores removed from segmental breakup." | AMBIGUOUS | Segment profit 12.38 less 5.95 = 6.43, which equals PBT 6.60 within rounding. About 7.31 Cr of implied other income then has no separate place. Reading A: other income (including 2.50 Cr RoU other income) sits inside segment profit. Rental's "₹93 Lakhs" profit (L126) could then rest on RoU other income: 0.93 - 2.50 = -1.57 Cr ex other income, against checklist item 5. Reading B: the 5.95 is net of other income, so gross unallocable cost is about 13 Cr. The results filing's segment note separates the two. Segment assets and liabilities: NOT FOUND in the deck. |
| FN-06 | F16 | R026, R306, R298, R016, R019, R037, R276 | L87 (slide 3); L840 (slide 29); L108 (slide 3) | "Continued growth, improving margins, and a sustained profitable quarter"; "PBT (before Exceptional Items) ... 6.60" | AMBIGUOUS | The Q1 FY27 deck headline counted quarters ("third consecutive profitable quarter", Notion record). That claim rested on continuing-ops PAT of -0.34 Cr. This headline drops the count. "Profitable" rests on PBT before exceptional items, which includes about 7.31 Cr implied other income. Derived PBT ex other income is -0.71 Cr (range -2.21 to +0.79). The deck shows no tax, PAT or exceptional-item line. Lean bear: checklist item 1 may be at strike two (red). The results filing's other-income and exceptional lines settle it. |
| FN-07 | F16 | R080, R081, R056, R057, R058, R059, R086, R089, R227 | L201-203 (slide 6) vs L169 (slide 5) | "Scaled platform to 8,500+ rentable units across 4,300 houses" vs "8,866 (-25%) Number of Signed Units" | FORWARD-SIGNAL | "Scaled" describes a metric that fell 25% YoY. Against the Q1 FY27 deck (Notion: signed units -28%, beds -8% YoY), signed units still decline and the co-living bed decline sped up from -8% to -14%. Rental revenue of Rs 56 Cr (L121) has no YoY figure in the deck. Rental volume is still shrinking, which pressures checklist item 5 (Rental breakeven in FY27). |
| FN-08 | F16 | R064, R065, R066, R069, R070, R071-R075, R085, R106, R169, R186, R035-R040 | L169-177 (slide 5); L212 (slide 6); L121-126 (slide 4); L435-438 (slide 15) | "816" (no change shown); "Achieved 7.6x QoQ growth in bookings" | AMBIGUOUS | YoY figures appear only where they suit the slide. Transactions (816), rent GMV (Rs 35 Cr), occupancy (82%), CRM gross margin (62%), value of homes sold (Rs 838 Cr), all revenue-per-member figures and all segment revenue and profit carry no prior period. "7.6x QoQ" has no base number. No organic ex-PropTiger split is given (checklist item 2). The PropTiger date on the timeline is ambiguous: "September 2025" (L435) and "July 2025" (L438) sit by position only (R186). That date decides whether the Q2 FY26 base includes PropTiger. A4 question: segment revenue and profit for Q2 FY26, and PropTiger revenue in both quarters. |
| FN-09 | F16 | R125-R153, R028, R029, R166 | L372-382 (slide 12); L112 (slide 3); L434 (slide 15) | "+28 % 5Y CAGR in Core Business Collections2 ... (2) FY21 to FY26"; "Housing.com figures to be integrated from next quarter." | FORWARD-SIGNAL | Four slides cover Housing.com (pdf p10-13) but give no revenue, EBITDA, loss or collections figure. The growth metrics are a 5-year CAGR that ends in FY26 and enquiry growth (+10%). The REA share swap (1,97,93,309 shares, Notion item 9) appears only as "Joined forces with REA Group". The deck gives no consideration, share count, REA stake or nominee director (the board list at L907-968 names none). The Q3 FY27 consolidated P&L will absorb a business of undisclosed profitability, and checklist items 1, 6 and 7 change basis. A4 question: Housing.com FY26 and H1 FY27 revenue and EBITDA; purchase consideration and goodwill; post-swap share count and REA stake; REA board rights. |
| FN-10 | F15 | R165, R166, R167, R186, R168-R185 | L432-435 (slide 15) | "September 2026 ... Housing.com Joined forces with REA Group to bring Housing.com into Aurum’s integrated PropTech ecosystem" | FORWARD-SIGNAL | New entity added to the group in September 2026. Every other entity on the slide carries its legal name (e.g. L437 "PropTiger Marketing Services Private Limited", L446 "NestAway Technologies Private Limited"). The Housing.com legal entity is NOT FOUND in the deck. The deal closed 29-Sep (Notion item 9), so the 30-Sep balance sheet may already consolidate Housing.com goodwill while the P&L excludes it. A4 question: legal entity acquired; does the 30-Sep-2026 balance sheet consolidate it; provisional goodwill amount against the 174.25 Cr carried (checklist item 7). |
| FN-11 | F16 | R170, R171, R172, R046, R037, R040, R258-R263 | L441-443 (slide 15); L776-805 (slide 27); L121, L126 (slide 4) | "AMSA SM - REIT ... June 2023 ... Received SM-REIT registration from SEBI" | CONFIRMATORY-NEGATIVE | The Capital slide gives market size only ("₹50,000 Cr.+ SM REIT-able supply", L798). It names no scheme, no AUM, no filing date and no launch commitment, about 40 months after registration. Capital segment: Rs 4 Cr revenue, Rs 45 lakh profit, with no split between SM-REIT and lending. This supports the red path on checklist item 3. The concall A3 counts the silence. |
| FN-12 | F16 | R292, R291, R295, R296, R307 | L837, L839, L844 (slide 29) | "Less: Finance costs 1.24 0.01"; "Less: Impact of IND AS 2.27 1.19"; "The costs here are net of all such considerations." | AMBIGUOUS | Finance cost fell from 1.24 Cr to 0.01 Cr. The Ind AS 116 effect is one net plug line. Together they give +2.31 Cr of the +13.56 Cr PBT swing. Two readings: debt repaid (possibly from the July 2026 AREDL warrant money, checklist item 9 "productive use" test), or lease interest moved into the plug. A4 question: borrowings at 30-Sep-2026 against 30-Jun-2026, and what the Ind AS impact line contains. |
| FN-13 | F7 | R012 | L78-80 (slide 2, OCR) | "shall not constitute a solicitation of a proxy, consent or authorisation with respect to any securities or in respect of the business combination" | AMBIGUOUS | The safe-harbour text refers to a specific "business combination". No lexicon-exact hedge hits. The deck is dated 16-Oct-2026, after the Housing.com swap closed 29-Sep. Prior deck not available to diff, so this may be standing text. A4 question, low priority: does "the business combination" refer to Housing.com/REA or to another pending transaction? |
| FN-14 | F6 | R029, R052, R201, R028, R048, R200 | L112 (slide 3); L149 (slide 4); L507 (slide 16) | "Housing.com figures to be integrated from next quarter." | FORWARD-SIGNAL | This is a dated commitment: consolidation in Q3 FY27 (quarter ending 31-Dec-2026), repeated on three slides. Q3 FY27 YoY and QoQ comparisons lose like-for-like meaning. Role 5 tracker: check delivery in the Q3 FY27 results and ask for a pro-forma or ex-Housing.com bridge. |
| FN-15 | F6 | R111, R115, R118, R103, R113, R116 | L223, L235, L242 (slide 7); L212-216 (slide 6) | "AI Transformation underway"; "AI-first core re-architecture progressing"; "Last quarter        Now        Now · in progress" | NEUTRAL-FACT | Status words for the tracker: two items "underway"/"progressing", the rest stated as done. The stage legend (PILOTED to AI-NATIVE) uses colour markers that A1 could not extract (R118), so no stage change can be verified from this extract. No revenue figure is attached to the new "pay-per-use revenue stream". |
| FN-16 | F14 | R336, R355, R335, R354 | L928 (slide 33) vs L1024 (slide 36) | "With 18 years of multisectoral experience" vs "15 years of multisectoral experience" | NEUTRAL-FACT | Same director, two experience figures in one deck. Immaterial alone. It adds to the deck-quality count with FN-01 and FN-02. |

Flagged for A4 (FORWARD-SIGNAL + AMBIGUOUS): FN-01, FN-02, FN-03, FN-04, FN-05, FN-06, FN-07, FN-08, FN-09, FN-10, FN-12, FN-13, FN-14.

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Presentation; A2 found 0 ZERO_STANDING rows; no statutory template. Pointer for results A3: label "PBT (before Exceptional Items)" (L840, R306) implies an exceptional line exists. |
| F2 Standalone vs consolidated | N.A. | Deck carries consolidated figures only ("Consolidated", L156). |
| F3 Shell-entity detection | N.A. | No standalone cost lines in deck. |
| F4 Unaudited contribution ratio | N.A. | No auditor report in deck. |
| F5 Going concern / EoM scope | N.A. | No auditor EoM in deck. |
| F6 Forward-commitment mining | FINDING | FN-14, FN-15; register in section 4. |
| F7 Hedge phrase mining | FINDING | No lexicon-exact hits; safe-harbour "business combination" clause, FN-13. |
| F8 Tax forensics | N.A. | Deck carries no tax line, no ETR, no PAT. |
| F9 OCI forensics | N.A. | Deck carries no OCI. |
| F10 Share count and dilution | N.A. | Deck carries no paid-up capital or EPS. The share swap is not quantified (handled in FN-09). |
| F11 Reserves / net worth tie-out | N.A. | Deck carries no net worth or reserves figure. |
| F12 Segment forensics | FINDING | FN-05: segment profit less unallocable equals PBT and leaves implied other income unplaced. Segment assets and liabilities NOT FOUND. |
| F13 Board outcome beyond results | N.A. | Deck is not a board outcome. Board list (L907-968) shows no term dates and no REA nominee (noted in FN-09). |
| F14 Drafting inconsistencies | FINDING | FN-01 (3.1% vs -3.2%), FN-02 (expense-ratio claim contradicted by own numbers), FN-16 (18 vs 15 years). |
| F15 Entity list diffs | FINDING | FN-10: Housing.com added September 2026, legal entity NOT FOUND. No prior entity list available for a full diff. |
| F16 Dropped / reframed disclosures | FINDING | FN-03, FN-04, FN-06, FN-07, FN-08, FN-09, FN-11, FN-12. Prior deck fulltext not available. No dropped metric found among the two Q1 metrics known from Notion (both still shown). |
| F17 Silence audit | N.A. | Concall-specific. Deck-level checklist cross-reference below is non-scored input for the concall A3. |

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | note/slide ref | status word |
|---|---|---|---|
| Housing.com figures integrated into consolidated reporting | Q3 FY27 (quarter to 31-Dec-2026) | L112 s3, L149 s4, L507 s16 (R029, R052, R201) | initiated |
| Housing.com brought into Aurum via REA Group transaction | September 2026 | L432-435 s15 (R165, R166) | completed |
| AI transformation across platforms | undated | L223 s7 (R111) | underway |
| AI-first core re-architecture of sales CRM, lead scoring in core | undated | L235-236 s7 (R115) | underway ("progressing") |
| AI-led Lead Enrichment, new pay-per-use revenue stream | Q2 FY27 | L212-216 s6 (R103) | completed ("Introduced"); revenue NOT FOUND |
| AI voice agents/chatbot default first touch; auto-triage to vendor network | Q2 FY27 | L229-230 s7 (R113) | completed ("now the default") |
| AI agents qualifying buyers; AI-powered CMS extended across booking | Q2 FY27 | L238-239 s7 (R116) | completed ("extended") |
| Aurum Qonvo WhatsApp AI platform scaled; 3 developers onboarded | Q2 FY27 | L211-213 s6 (R096, R097) | completed |
| AMSA SM-REIT registration from SEBI | June 2023 | L441-443 s15 (R170, R171) | completed (registration only); first scheme: no commitment, NOT FOUND |

## 5. NOTION CHECKLIST CROSS-REFERENCE (non-scored; F17 is N.A. on a deck)

Silence count across quarters: NOT TESTABLE from this run (prior deck fulltext not available).

| # | Checklist item | Deck addresses? | Deck evidence / gap |
|---|---|---|---|
| 1 | Operating profit ex one-times | Partly | PBT before exceptional 6.60 (L840) includes about 7.31 Cr implied other income; derived ex-OI -0.71 Cr (range -2.21/+0.79). Other income line NOT FOUND. FN-06. |
| 2 | Organic revenue ex-PropTiger YoY | No | No PropTiger split; PropTiger date ambiguous (R186). FN-08. |
| 3 | SM-REIT first scheme with AUM | No | Registration June 2023 only; no scheme, AUM or date. FN-11. |
| 4 | Receivables >1yr buckets | No | No balance-sheet data in deck. |
| 5 | Rental segment breakeven | Partly | Rental segment profit "₹93 Lakhs" (L126) on Rs 56 Cr revenue; may rest on RoU other income (FN-05); volumes falling (FN-07). |
| 6 | Distribution EBITDA margin >=12% | Partly | Segment profit 11/70 = 15.7% (range 14.9-16.5%). This is segment profit, not EBITDA. No prior quarter to test "declining". |
| 7 | Goodwill 174.25 Cr not impaired | No | No goodwill figure; Housing.com goodwill arrives with consolidation (FN-10). |
| 8 | Audit / RPT / AREDL loan-advance test | No | Deck names "Aurum RealEstate (engaged in real estate development in the MMR region)" (L914) as group company. ED Onkar Shetye lists "Aurum RealEstate Developers" as a previous organisation (L1025). Suggested question: is AREDL among the 15 active mandates (L202-203) or 280+ projects (L201), and is there any loan or advance to AREDL? |
| 9 | July-2026 fund-raise | No | AREDL warrants absent; swap framed as "Joined forces" (L434), no share count (FN-09). Finance cost fell to 0.01 Cr (FN-12), a possible use-of-proceeds signal. |

```yaml
stage: A3-forensics
company: "AURUM"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\q2fy27\\runs\\aurum-q2fy27\\work\\forensics_presentation_aurum_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: FINDING
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN-01", check: "F14", line: "L97 vs L818 (slide 3 vs slide 29); R020/R269", classification: "AMBIGUOUS", implication: "Q2 FY26 Adj EBITDA margin 3.1% vs -3.2%; build-up 2.65/84.80 and +840 bps support 3.1%; ask if base was restated from published figure"}
  - {id: "FN-02", check: "F14", line: "L820-822, L827 (slide 29); L247 (slide 7)", classification: "FORWARD-SIGNAL", implication: "'improving Expense to Total Income ratios' contradicted: 69.9% to 70.2%; expenses +57.3% vs income +56.6%; no operating leverage on reported cost base"}
  - {id: "FN-03", check: "F16", line: "L817, L818, L834 (slide 29)", classification: "FORWARD-SIGNAL", implication: "+840 bps adj margin = +711 bps lease share +152 bps RoU OI +45 ESOP -75 underlying; reported EBITDA margin fell 30.1% to 29.8%; gain is mix shift from leased co-living"}
  - {id: "FN-04", check: "F16", line: "L834 (slide 29); L169 (slide 5)", classification: "AMBIGUOUS", implication: "lease payments +14% while beds -14%; ~+32% per bed if co-living driven; ask lease split by business and exit costs"}
  - {id: "FN-05", check: "F12", line: "L150, L126 (slide 4); L826, L840 (slide 29)", classification: "AMBIGUOUS", implication: "segment profit 12.38 - 5.95 = PBT 6.60 leaves ~7.31 Cr implied other income unplaced; Rental Rs 93 lakh may rest on 2.50 Cr RoU other income (checklist 5)"}
  - {id: "FN-06", check: "F16", line: "L87, L108 (slide 3); L840 (slide 29)", classification: "AMBIGUOUS", implication: "headline dropped consecutive count; profit is PBT pre-exceptional incl ~7.31 Cr OI; derived ex-OI -0.71 Cr (range -2.21/+0.79); checklist 1 strike-two risk; no PAT/tax/exceptional shown"}
  - {id: "FN-07", check: "F16", line: "L201-203 (slide 6) vs L169 (slide 5)", classification: "FORWARD-SIGNAL", implication: "'Scaled platform' on signed units -25%; beds decline sped up -8% (Q1) to -14%; rental revenue shrinking, checklist 5 pressured"}
  - {id: "FN-08", check: "F16", line: "L169-177 (slide 5); L212 (slide 6); L121-126 (slide 4); L435-438 (slide 15)", classification: "AMBIGUOUS", implication: "YoY shown selectively; no segment prior period; no organic ex-PropTiger split; PropTiger date ambiguous (R186) decides Q2 FY26 base"}
  - {id: "FN-09", check: "F16", line: "L372-382 (slide 12); L112 (slide 3); L434 (slide 15)", classification: "FORWARD-SIGNAL", implication: "Housing.com: no revenue/EBITDA/loss in 4 slides; swap shown as 'Joined forces', no shares/stake/nominee; Q3 P&L absorbs undisclosed profitability"}
  - {id: "FN-10", check: "F15", line: "L432-435 (slide 15)", classification: "FORWARD-SIGNAL", implication: "Housing.com added Sep 2026, legal entity NOT FOUND; closed 29-Sep so 30-Sep balance sheet may carry goodwill while P&L excludes it (checklist 7)"}
  - {id: "FN-11", check: "F16", line: "L441-443 (slide 15); L776-805 (slide 27)", classification: "CONFIRMATORY-NEGATIVE", implication: "SM-REIT ~40 months post-registration, no scheme/AUM/date; Capital Rs 4 Cr revenue; checklist 3 red path"}
  - {id: "FN-12", check: "F16", line: "L837, L839, L844 (slide 29)", classification: "AMBIGUOUS", implication: "finance cost 1.24 to 0.01 and net Ind AS plug add +2.31 Cr of +13.56 Cr PBT swing; debt repaid (warrant money? checklist 9) or reclassified"}
  - {id: "FN-13", check: "F7", line: "L78-80 (slide 2, OCR)", classification: "AMBIGUOUS", implication: "disclaimer cites 'the business combination'; ask whether it is Housing.com/REA or another pending transaction"}
  - {id: "FN-14", check: "F6", line: "L112 (slide 3); L149 (slide 4); L507 (slide 16)", classification: "FORWARD-SIGNAL", implication: "Housing.com consolidation dated Q3 FY27; like-for-like comparisons break; track delivery and request ex-Housing.com bridge"}
  - {id: "FN-15", check: "F6", line: "L223, L235, L242 (slide 7); L212-216 (slide 6)", classification: "NEUTRAL-FACT", implication: "AI status words underway/progressing; stage markers not extractable (R118); new pay-per-use stream unquantified"}
  - {id: "FN-16", check: "F14", line: "L928 (slide 33) vs L1024 (slide 36)", classification: "NEUTRAL-FACT", implication: "Onkar Shetye 18 vs 15 years experience; deck-quality data point with FN-01, FN-02"}
forward_signals: ["FN-02", "FN-03", "FN-07", "FN-09", "FN-10", "FN-14"]
ambiguous: ["FN-01", "FN-04", "FN-05", "FN-06", "FN-08", "FN-12", "FN-13"]
commitments:
  - {commitment: "Housing.com figures integrated into consolidated reporting", implied_date: "Q3 FY27 (to 31-Dec-2026)", ref: "L112/L149/L507; R029, R052, R201", status_word: "initiated"}
  - {commitment: "Housing.com brought into Aurum via REA Group transaction", implied_date: "September 2026", ref: "L432-435; R165, R166", status_word: "completed"}
  - {commitment: "AI transformation across platforms", implied_date: "undated", ref: "L223; R111", status_word: "underway"}
  - {commitment: "AI-first core re-architecture of sales CRM", implied_date: "undated", ref: "L235; R115", status_word: "underway"}
  - {commitment: "AI-led Lead Enrichment pay-per-use revenue stream", implied_date: "Q2 FY27", ref: "L212-216; R103", status_word: "completed"}
  - {commitment: "AI voice agents/chatbot default first touch; auto-triage to vendors", implied_date: "Q2 FY27", ref: "L229-230; R113", status_word: "completed"}
  - {commitment: "AI buyer qualification; AI CMS extended across booking", implied_date: "Q2 FY27", ref: "L238-239; R116", status_word: "completed"}
  - {commitment: "Aurum Qonvo scaled; 3 developers onboarded", implied_date: "Q2 FY27", ref: "L211-213; R096, R097", status_word: "completed"}
  - {commitment: "AMSA SM-REIT SEBI registration (first scheme: no commitment, NOT FOUND)", implied_date: "June 2023", ref: "L441-443; R170, R171", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The deck's margin story is mix, not efficiency. Reported EBITDA margin fell (30.1% to 29.8%) and the expense ratio worsened (69.9% to 70.2%), against the deck's own claim. The +840 bps adjusted gain comes from lease payments (+711 bps) and RoU other income (+152 bps) falling as a share of income, while co-living shrinks (beds -14%, faster than Q1's -8%). 'Profitable' is PBT before exceptional items. That PBT holds about 7.3 Cr of other income the deck never shows as a line; slide 3 folds it into 'Others 11'. PBT ex other income derives to about -0.7 Cr, but segment rounding leaves the sign open, so checklist 1 strike two is likely, not proven. The results filing settles it from the other-income and exceptional lines. Segment profit less 5.95 already equals PBT, so Rental's 93 lakh profit may depend on RoU other income. Housing.com gets four slides and no financials. Consolidation next quarter resets Q3 comparisons and brings goodwill. The 3.1% vs -3.2% conflict resolves to 3.1% on arithmetic; ask whether the base was restated. Prior deck unavailable: dropped-slide and silence counts untested."
```
