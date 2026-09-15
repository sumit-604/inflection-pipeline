# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 3 (PATTERN PASS + CONSOLIDATION)
Company: Syngene International Ltd (SYNGENE) | Run date: 2026-09-15
Source: Annual_Report_2026.pdf (page numbers = PDF page in the "===== PAGE n =====" markers).
Comparator: Annual_Report_2025.txt, cited only where used. All amounts in INR Million unless
converted to Rs Cr for readability. Tagged [STANDALONE] / [CONSOLIDATED]. This report
consolidates Pass 1 (full extraction), Pass 2 (what was missed), and Pass 3 (pattern re-read).

---

## PASS 3 — PATTERN RE-READ

Approach: read for contradictions between notes, numbers that do not tie to the main
statements, notes that are vague relative to the detail given elsewhere, prior-year
restatements, post-balance-sheet events, and going-concern language, rather than
note-by-note sequentially (which Passes 1 and 2 already covered).

### New finding: selective ratio-variance disclosure (Note 38, standalone p.286-287)

Note 38's own disclosure rule is to explain "variance more than 25%" in any financial
ratio. Applying that rule to FY26 (all standalone, Note 38, p.286-287):
- Net profit ratio: 11% vs 13% FY25 = **-14.5%** variance — under the 25% threshold,
  NOT explained.
- Return on equity: 8% vs 10% FY25 = **-18%** variance — under the 25% threshold, NOT
  explained.
- Return on capital employed: 10.78% vs 13.24% FY25 = **-19%** variance — under the
  25% threshold, NOT explained.
- By contrast, ratios that improved and cleared 25% — debt-equity (-100%, i.e. debt
  fully repaid), net capital turnover (+27%), inventory turnover (+26%) — each get an
  explicit one-line explanation in the "Explanation for variance" block (p.287:
  "Improvement in debt equity ratio is due to repayment of borrowings..." etc).
- 🔴 Net effect: the three ratios that most directly reflect the ~35% PAT decline
  (profitability, ROE, ROCE) all sit just under the mandatory-explanation line and are
  left unexplained in the notes, while every ratio that improved is explained in
  detail. This is a genuine disclosure-asymmetry pattern — not a numbers error, but a
  choice of what gets narrated. It compounds Pass 1's exceptional-item and Note 43
  classification findings (Section 12, Pass 1) into a broader pattern: FY26 disclosure
  consistently frames the deterioration story through mechanisms (threshold rules,
  "exceptional" classification) that keep the worst-looking numbers out of the
  explained/narrated sections of the notes.

### Confirmatory pattern checks (no new numbers, closes out the pattern search)

- 🟢 **Zoetis is named only in narrative Business Review text** ("...multinationals
  such as BMS, GSK, Zoetis, and..." — Business Review section, and again in a client
  list), never inside the audited Notes to Financial Statements. This confirms Pass
  1's finding that Note 32/33 customer concentration disclosure (35.6%/37.2%
  two-customer revenue) is anonymised per Ind AS 108 and cannot itself be tied to
  Zoetis/Librela from the financial notes — the company-memory LBF2 linkage remains an
  inference from narrative text plus the concentration percentage, not a note-level
  fact. Stage 3 should treat "customers = Zoetis" as PENDING LIVE VERIFICATION, not a
  notes-confirmed fact.
- 🟢 **Going concern language re-confirmed clean on full-text search**: "going
  concern" appears only in the standard Ind AS/SA 570 boilerplate (Note 1.2(a)
  standalone p.218 / consolidated p.306; Independent Auditor's Report responsibility
  paragraphs, both reports) — no material uncertainty paragraph, no emphasis of matter,
  in either the standalone or consolidated Independent Auditor's Report. Confirms Pass
  1's Section 12 finding; no new information.
- 🟢 **No prior-period restatement found** — Pass 2's targeted search (Finding G) is
  re-confirmed on this pass's independent full-text sweep; no additional instance
  found.
- No new post-balance-sheet event beyond the two already flagged (FY26 final dividend
  recommendation, Note 44/45 standalone/consolidated; the unresolved SSS dividend
  figure, Note 45(c) consolidated) — both already carried in Passes 1-2.

No further material new findings beyond the ratio-disclosure item above. Proceeding
to consolidation.

---

═══════════════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS RANKED BY INVESTOR IMPORTANCE

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Cash flow hedge reserve deteriorated >20x YoY: Rs -3,027mn pre-tax / Rs -2,275mn net-of-tax OCI loss FY26 (standalone) vs Rs -143mn/-100mn FY25; consolidated Rs -3,082mn pre-tax / Rs -2,316mn net-of-tax vs Rs -146mn/-102mn FY25. Corroborated independently by the derivative fair-value book flipping from a +Rs 2,155mn net asset (FY25) to a -Rs 1,191mn net liability (FY26), standalone. | Note 30(b), Note 28 (standalone p.276/270-271; consolidated p.365/339) | 🔴 | Live, ongoing forward-earnings risk (unrealised losses reclassify into P&L over the life of hedged transactions); far larger than, and explains, the Rs 50cr Q1FY27 EBITDA hedge hit in company memory. First finding for FTTCP/Role 1 to model as a multi-quarter earnings drag, not a one-off. |
| 2 | PAT and EPS fell ~35-36% YoY: standalone PAT Rs 4,680mn to Rs 3,049mn, EPS Rs 11.64 to Rs 7.58; consolidated PAT Rs 4,962mn to Rs 3,167mn, EPS Rs 12.34 to Rs 7.87. | Note 37/38 (p.286/373) | 🔴 | Driven by exceptional-item swing (Rs 320mn gain FY25 to Rs 733mn expense FY26), a Rs 277mn ordinary-expense FX write-off, and margin/hedge pressure; the base-year earnings this pipeline's projections will key off is a depressed year, not a clean run-rate. |
| 3 | Two-customer revenue concentration remains above 35% of total revenue both years: Rs 12,196mn/34,238mn = 35.6% standalone FY26 (40.4% FY25); Rs 13,926mn/37,387mn = 37.2% consolidated FY26 (41.1% FY25). Customers not named in the notes (Ind AS 108 does not require it); Zoetis appears only in narrative text, never in the audited notes. | Note 32 (standalone p.278), Note 33 (consolidated p.365) | 🔴 | **LBF2 status: FOUND, but not confirmable to Zoetis from notes alone.** The concentration is real and material; the specific counterparty link to Zoetis/Librela is a narrative-plus-inference, not a note-level fact — flag PENDING LIVE VERIFICATION for Stage 3/claude.ai. No take-or-pay disclosure found anywhere (confirms Pass 1 gap). |
| 4 | Non-standalone (predominantly Syngene USA/Bayview) CWIP estimated at ~Rs 5,044mn at 31-Mar-2026 (consolidated CWIP Rs 10,404mn less standalone CWIP Rs 5,360mn) — now roughly as large as the Company's entire standalone CWIP book, and growing while standalone CWIP fell 38.8%. | Note 3(a) (standalone p.242-243, consolidated p.324) | 🟡 | **LBF3 status: FOUND (derived by subtraction, not directly disclosed).** Quantifies the scale of non-revenue-generating US capital sunk relative to the domestic capex programme — a key input for Stage 3's capital-intensity read on the Bayview transition. |
| 5 | Rs 277mn "unrecoverable receivables due to cumulative FX movements" write-off (Rs 202mn after tax) classified as an ordinary Other Expense, NOT as an Exceptional Item, despite being of comparable size to the Rs 304mn termination benefit that WAS classified exceptional. Unusual causal claim (FX movements causing credit unrecoverability); no counterparty or currency disclosed. | Note 43 standalone (p.289) / Note 44 consolidated (p.374); Note 25 (p.255-256) | 🔴 | Earnings-optics classification choice: keeps a discrete, disclosed one-off inside "core" operating expense rather than the explicitly excluded exceptional-items line, inflating the apparent core-earnings decline's ordinariness. Cross-refers to Finding 11 (ratio-disclosure asymmetry) below. |
| 6 | Income tax contingent liability Rs 5,181mn standalone (Rs 5,184mn consolidated) = 97.6% of total contingent liabilities and = **11.0% of standalone net worth** (Rs 47,038mn) / 10.7% consolidated — a single item above the 10%-of-net-worth threshold, spanning 6 assessment years (FY09, FY13-19, FY21, FY22). | Note 31 (p.277-278 standalone, p.362 consolidated); Note 29 (p.274, net worth) | 🔴 | Long-running, unresolved dispute pattern rather than a single event; trend is improving (Rs 6,285mn to Rs 5,308mn standalone, partly Vivad se Vishwas settlement) but the absolute exposure remains above the material threshold. |
| 7 | Syngene USA Inc. (holds Bayview) swung to a Rs 77mn consolidated-note loss in FY26 from a Rs 38mn profit FY25, while accumulating further CWIP (Rs 785mn additional pre-operating cost). Separately, the Board's Report narrative states a USD 1.4mn loss (~Rs 124-131mn) for the same entity/year — a ~40% gap versus the audited Rs 77mn figure, unreconciled anywhere in the AR. | Note 32(b)/33(b) consolidated (p.364/368); Board's Report p.65 | 🟡 | **LBF3 status: FOUND, with an internal disclosure inconsistency.** Capital is being deployed into a now-loss-making subsidiary; the scale of the loss itself is ambiguous by ~40% between two disclosures in the same AR, both of which should tie. |
| 8 | No CGU-specific impairment test disclosed for Bayview USA or Unit 3 Bengaluru biologics facility despite the scale of non-revenue-generating capital sunk in both (no quantified discount rate, growth rate, or sensitivity anywhere in Notes 2-4). Structurally explained (not excused) by Syngene's single-operating-segment status under Ind AS 108, which removes any obligation to show segment/CGU-level data. | Note 2(g)/2(i) policy (p.228-229/319-320); Note 32/33 segment note (p.278/365) | 🟡 | **LBF3 status: FOUND — impairment test is NOT FOUND IN DOCUMENT.** An investor cannot independently test Bayview or Unit 3 for impairment risk from the notes; the single-segment structure is the stated reason, not a defect unique to Syngene, but it does not reduce the substantive information gap given a loss-making subsidiary sitting on this capital. |
| 9 | "Other related parties" sale-of-services jumped 155% (Rs 820mn to Rs 2,091mn = 6.1% of standalone revenue), with a matching receivable build from Rs 5mn to Rs 314mn — neither broken down by counterparty nor explained in the note. | Note 26 (standalone p.259/269-270, consolidated p.345-346) | 🔴 | Single largest YoY swing in the RPT table; the "other related parties" bucket includes several director-linked entities added mid-year (Bicara, Puretech, Abergy, Third Arc, Therapoma) — a management question on which entity/entities drove it and on collectability of the new receivable. |
| 10 | Selective ratio-variance disclosure: the three ratios most directly reflecting the PAT decline (net profit ratio -14.5%, ROE -18%, ROCE -19%) all sit just under Note 38's own 25%-variance explanation threshold and are left unexplained, while every ratio that improved and cleared 25% (debt-equity, net capital turnover, inventory turnover) is explained in a dedicated paragraph. | Note 38 (standalone p.286-287) | 🔴 | Pass 3 pattern finding. Not a numbers error, a narration choice: the notes explain good news in detail and are silent, by threshold technicality, on the year's central profitability deterioration. Reinforces Finding 5's classification-choice pattern. |
| 11 | Syngene Scientific Solutions Ltd (SSS) subsidiary event-after-reporting-date discloses a final dividend of Rs 3,15,000 (315,000) per Rs 10 equity share — numerically implausible against SSS's disclosed 84,000,000-share base and Rs 287mn FY26 PBT (implied aggregate payout ~Rs 26.46 lakh crore, ~56x Syngene's own consolidated revenue). Re-verified verbatim in Pass 2; not an extraction artefact. | Note 45(c) consolidated (p.375) | 🔴 | Unresolved from the document; reads as an as-filed drafting error (e.g., an intended Rs 3.15 or Rs 31.50/share) but cannot be corrected without management confirmation — carried as a standing verification item, not assumed to be real. |
| 12 | Probable USD-vs-Rs-Mn unit mislabel in the outstanding FX forward/option notional-contract table: disclosed notional (Rs 393mn/Rs 167mn FY26 standalone; Rs 404mn/Rs 170mn consolidated) is implausibly small against the Rs 3,027-3,082mn pre-tax hedge fair-value swing on the same book and against ~USD 238mn of USA-derived annual services revenue; read as USD million the notional would sit at an internally consistent 1.7-2.3x annual USD revenue over the table's own multi-year buckets. Same apparent error appears in both standalone and consolidated versions (inherited template, not independently made twice). | Note 28 (standalone p.273, consolidated p.339 series) | 🟡 | Second independent documentation/proofing gap in the same note set as Finding 11 below; flagged for management verification, not restated as fact, but bears on how much weight to place on any other single figure in Note 28. |
| 13 | CWIP schedule slippage recurs: a different project is overdue each year (FY26: "S20B Infra warm shell," Rs 407mn total overdue, revised cap. date 30-Sep-2026; FY25: "Project 3/IOT," Rs 81-89mn, expected cap. date 31-Jan-2026, a date now passed without the project reappearing as overdue or capitalised under either name in FY26). No project has exceeded its original COST budget in either year. | Note 3(a) (standalone p.242, consolidated p.329) | 🟡 | Schedule risk, not cost risk, in ongoing capex — worth tracking whether the pattern of "a different overdue project every year" continues, since it suggests a persistent execution-timing gap rather than a one-off delay. |
| 14 | Flat dividend of Rs 1.25/share recommended for FY26 (same as FY25) despite the ~35% standalone PAT decline — implying a materially higher payout ratio this year than last. | Note 44 standalone (p.289) / Note 45 consolidated (p.375) | 🟡 | A capital-allocation signal: management chose not to cut the dividend even as core earnings fell sharply, which the notes do not explain (no payout-ratio policy statement found in this note). |
| 15 | Standalone Note 43 is mislabelled as "Business Combination" in the Judgements cross-reference index (actual content is the FX receivables write-off; the true business-combination note is standalone Note 42). The equivalent consolidated cross-reference is correctly labelled. | Note 1.2(e) (p.219 standalone; correct version p.311 consolidated) | 🟡 | Minor on its own, but the third documentation-quality gap identified across the three passes (alongside Findings 11 and 12) — a consistent signal that the standalone notes were not fully proofed against their own cross-reference index before filing. |

## B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 6 | Point-in-time recognition mix rose to 86.4% (FY25: 81.4%); auditor's Key Audit Matter names "bill and hold" arrangements as a tested fraud-risk area (not an identified misstatement); two-customer concentration properly disclosed at aggregate level under Ind AS 108, no take-or-pay terms disclosed. |
| Expense capitalisation honesty | 6 | Bayview asset-acquisition accounting (Ind AS 103 concentration test, no goodwill) is a defensible election; CWIP schedule slippage recurs yearly (no cost overrun); no capitalisation-threshold Rupee figure disclosed; no impairment test disclosed against Bayview/Unit 3 CWIP. |
| Provisioning adequacy | 8 | ECL allowance shrank in step with receivables; inventory obsolescence flat as % of average inventory; gratuity funding jump well explained (Labour Codes wage-definition change) with stable actuarial assumptions and modest sensitivity. |
| RPT fairness | 6 | Land/rent/facility dependency on holding company is structural but consistently disclosed year to year; the 155% "other related parties" sale-of-services jump and matching receivable build are disclosed in aggregate but not broken down by counterparty or explained. |
| Disclosure transparency | 4 | Multiple gaps across the three passes: no capitalisation threshold, no impairment sensitivity for Bayview/Unit 3, unbroken-out RPT jump, an exceptional-item classification choice that keeps a comparable-sized write-off out of the exceptional line, a probable unit-mislabel in the derivatives notional table, a standalone cross-reference proofing error, an unresolved implausible SSS dividend figure, and a selective (threshold-driven) silence on the year's three worst-moving ratios. |
| Consistency with prior years | 8 | No policy changes with quantified P&L impact; no restatements or reclassifications found on two independent targeted searches; useful lives and actuarial/discount-rate assumptions stable YoY. |
| **OVERALL** | **6** | Provisioning and year-on-year policy consistency are clean. Disclosure transparency is the weak dimension: several proofing-quality gaps plus a discernible pattern of framing the worst-moving numbers (exceptional-item exclusion, sub-threshold ratio silence) more favourably than the underlying deterioration warrants. The single largest substantive risk (FX hedge book) is fully disclosed, not hidden — it lowers the outlook, not the accounting-quality score. |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| FX hedge book unrealised loss (Rs -2,275mn/-2,316mn net-of-tax OCI, standalone/consolidated) reclassifying into P&L over the life of hedged transactions | HIGH | Quarterly hedge-reserve reclassification into P&L; derivative asset/liability balance; USD/INR rate | Ongoing through FY27-28; Q1FY27 EBITDA hit (company memory) is the first tranche, not the last |
| Two-customer revenue concentration >35%, LBF2 link to Zoetis/Librela unconfirmed at note level | HIGH | Any customer-level disclosure change, contract renewal/loss news via live verification (Zoetis appears only in narrative text) | Any contract renegotiation or loss, immediate on occurrence |
| Non-standalone (Bayview) CWIP ~Rs 5.0bn not yet earning; Syngene USA loss-making; no impairment test disclosed (LBF3) | MEDIUM-HIGH | Bayview commissioning timeline vs 30-Sep-2026 revised date; Syngene USA quarterly results; any impairment indicator disclosed | Commissioning delay or cost overrun, FY27-28 |
| Income tax contingent liability = 11.0% of net worth, unresolved across 6 assessment years | MEDIUM | Appellate/tribunal outcomes; any provision booked in future ARs | Uncertain timing, multi-year litigation |
| Earnings-optics classification and disclosure-framing pattern (Note 43 exceptional-item exclusion; sub-threshold silence on profitability-ratio decline) | MEDIUM | Whether similar exclusions/silences recur next year; any change in what gets classified "exceptional" | Each quarterly/annual close |
| Documentation/proofing quality (unresolved SSS dividend figure; probable derivatives-table unit mislabel; standalone cross-reference error) | LOW-MEDIUM | Correction or clarification in the next annual report or via management Q&A | Next AR filing cycle |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. What drove the 155% jump in "other related parties" sale of services (Rs 820mn to Rs 2,091mn, Note 26) and the matching receivable build (Rs 5mn to Rs 314mn)? Which counterparties, and what is the collectability assessment on the new receivable?
2. Why is the Rs 277mn "unrecoverable receivables due to cumulative foreign exchange movements" write-off (Note 43/44) excluded from Exceptional Items when the Rs 304mn termination benefit of comparable size was included? What is the counterparty and currency behind this write-off?
3. What explains the ~40% gap between the Board's Report disclosure of Syngene USA Inc.'s FY26 loss (USD 1.4mn, approximately Rs 124-131mn) and the audited consolidated Note 33(b) figure of Rs 77mn for the same entity and year?
4. Given the scale of capital sunk in Bayview USA (approximately Rs 5.0bn of non-standalone CWIP, per Note 3(a) subtraction) and Unit 3 Bengaluru, with Syngene USA now loss-making, why has no CGU-specific impairment test or indicator assessment been disclosed?
5. Can management confirm two apparent documentation issues: (a) whether the FX forward/option notional amounts in Note 28 (Rs 393mn/Rs 167mn standalone) should be read in USD million rather than Rupees million, given the multi-billion-rupee scale of the FY26 hedge fair-value swing; and (b) the correct per-share dividend figure for Syngene Scientific Solutions Ltd (Note 45(c) states Rs 3,15,000 per Rs 10 share against an 84,000,000-share base, an implausible aggregate payout)?

## E. NOTES-BASED RED FLAGS

- **Selective ratio-variance disclosure**: the three ratios most directly reflecting the ~35% PAT decline (net profit ratio -14.5%, ROE -18%, ROCE -19%) sit just under Note 38's own 25%-variance explanation threshold and are left unexplained, while every ratio that improved and cleared 25% is explained in a dedicated paragraph. A narration choice, not a numbers error, but it shapes how the year's core deterioration reads.
- **Exceptional-item classification choice**: the Rs 277mn FX receivables write-off is kept out of "Exceptional Items" despite being disclosed as a discrete, one-off event of comparable size to items that were classified exceptional — an earnings-optics-shaping choice on which line absorbs a bad number.
- **Recurring documentation/proofing gaps in the standalone notes**: three independent instances found across the three passes — the Note 1.2(e) cross-reference misidentification, the probable Rs-Mn/USD-Mn unit mislabel in the derivatives notional table (Note 28), and the numerically implausible, unresolved SSS Rs 3,15,000/share dividend figure (Note 45(c)). None individually rises to fraud-risk, but together they are an evidence-quality caution on every other standalone figure extracted this pass.
- **Undisclosed impairment-test risk indicator**: no CGU-specific impairment test exists for Bayview or Unit 3 Bengaluru despite a loss-making subsidiary (Syngene USA) sitting on the growing non-standalone CWIP — structurally explained by single-segment reporting, not disclosed as tested.

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices, marked by classification choices that flatter the P&L narrative. Key concern: the Rs 2.3bn net-of-tax hedge-book loss reclassifying into future earnings, compounded by an unexplained profitability-ratio decline and an exceptional-item exclusion that both understate how the year actually deteriorated. Key strength: conservative ECL and inventory provisioning, and policies unchanged and consistent year on year. Overall accounting quality: 6/10.

---

## LBF STATUS SUMMARY (for Stage 3 / Halt 1 dossier)

- **LBF2 (Zoetis/Librela concentration, contract protection, biologics-asset impairment)**: Customer concentration FOUND at note level (35.6% standalone / 37.2% consolidated, two customers, Note 32/33) but customers are NOT named in the notes; Zoetis appears only in narrative Business Review text, never in the audited financial notes — the Zoetis/Librela link is PENDING LIVE VERIFICATION, not a notes-confirmed fact. Take-or-pay disclosure: NOT FOUND IN DOCUMENT. Quantified impairment test for biologics assets: NOT FOUND IN DOCUMENT (see LBF3 also).
- **LBF3 (CWIP, capitalisation, Bayview accounting, depreciation step-up)**: FOUND and quantified across passes — Bayview CWIP accumulated as an Ind AS 103 asset acquisition (Note 42/43); non-standalone CWIP estimated at ~Rs 5,044mn (derived, not directly stated); Syngene USA Inc. swung to a loss (Rs 77mn per audited note, vs an unreconciled USD 1.4mn/~Rs 124-131mn per Board's Report narrative); no CGU-specific impairment test disclosed for Bayview or Unit 3 Bengaluru (structurally explained by single-segment Ind AS 108 reporting, not tested). Depreciation step-up from Bayview commissioning: NOT FOUND IN DOCUMENT this year (asset remains in CWIP, not yet depreciating).
