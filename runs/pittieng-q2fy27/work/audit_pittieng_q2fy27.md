# A5 ADVERSARY AUDIT: PITTIENG (Pitti Engineering Limited), Q2 FY27

Agent: A5 adversary | Model: claude-opus-5-5 | Date: 2026-10-23
Instruction file: prompts/quarterly-a5-adversary.md
Inputs read: work/review_pittieng_q2fy27.md (A4); extracted/pittieng-results-q2fy27-fulltext.md and -structured.md; extracted/pittieng-presentation-q2fy27-fulltext.md and -structured.md; work/ledger_results_pittieng_q2fy27.md; work/ledger_presentation_pittieng_q2fy27.md.
Not read: source PDFs, anything under inputs/, A3 forensic notes, orchestrator commentary.
Cite convention: review:L### = line in the A4 review. results:L### and presentation:L### = A1 fulltext lines. R### = A1 structured row IDs (they restart per document). All Rs figures are crores unless marked lakh.
Note: sections 0-6 below are the iteration-1 audit, kept as written; review:L### there refer to the pre-revision review. The ITERATION 2 and ITERATION 3 re-audit sections follow. The ITERATION 3 RE-AUDIT section at the end holds the final verdict and the governing YAML block.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Location in review | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | review:L610-L626 | 16 lines (limit 10-20), real content, tiered | present |
| 2. Sector intelligence | review:L628-L633 | 5 bullets: demand, mix by sector, trade policy, regulation, gaps | present |
| 3. Business-model intelligence | review:L635-L642 | 7 bullets: process, two-business model, mix, per-tonne, scrap, capital drift, gaps | present |
| 4. Competition intelligence | review:L644-L650 | 6 bullets: claimed position, wins, weakness, peers NOT FOUND, in-house stamping risk, export share | present |
| 5. Forward map | review:L652-L664 | make-or-break reading plus 8 dated catalysts, each with a bull fork and a bear fork | present |

Gate result: PASS. All five parts are present and carry content.

---

## 1. COVERAGE AUDIT

### 1A. Fresh enumeration vs A2 ledger

| Doc | Category | A2 count | Fresh count | Fresh method (spine = A1 fulltext) | Orphan rows | Status |
|---|---|---|---|---|---|---|
| results | notes | 7 | 7 | grep "^[1-9] (The\|Figures)" hits L337, L340, L342, L345, L382, L388, L402 | none | PASS |
| results | line items | 126 | 126 | grep "\| [(\d-]" on pp5-9: P&L L187-L224 = 32, BS L233-L280 = 37, CF L288-L330 = 40, recon L358-L380 = 11, segment L394-L400 = 6 | none | PASS |
| results | zero-standing tags | 35 | 35 | grep "ZERO_STANDING]" in structured file | none | PASS |
| results | agenda items | 6 | 6 | Board letter items L37, L42, L44, L51, L55, L59 (L419 and L573 are annexure headings, not agenda) | none | PASS |
| results | auditor paragraphs | 5 | 5 | L112, L118, L126, L138 ("4," OCR), L155 (EoM) | none | PASS |
| results | entities | 42 | 42 | grep "\| ENTITY \|" | none | PASS |
| results | all A1 IDs (NUMBER 501, ENTITY 42, FORWARD 20, DATE 35, QUALIFIER 45) | 643 | 643 | per-type grep, total 643 | none | PASS |
| presentation | slides | 32 | 32 | grep "^\[page \d+\]" = 32 | none | PASS |
| presentation | numbers | 743 | 743 | grep "\| NUMBER \|" | none | PASS |
| presentation | entities | 67 | 67 | grep "\| ENTITY \|" | none | PASS |
| presentation | forward | 24 | 24 | grep "\| FORWARD \|" | none | PASS |
| presentation | dates | 81 | 81 | grep "\| DATE \|" | none | PASS |
| presentation | qualifiers / footnotes | 76 | 76 | grep "\| QUALIFIER \|" | none | PASS |
| presentation | zero-standing | 18 | 18 | grep "ZERO_STANDING" | none | PASS |
| presentation | all A1 IDs | 991 | 991 | sum of types | none | PASS |

Fulltext-to-structured sweep (the spine check). I read every numeric and named token on results pp1-4 and pp10-15 and on all 32 slides, and matched each to an A1 row. No unit is missing from the structured files. Spot proofs on scrambled slides: slide 7 tonnages re-add (4,786 + 1,350 + 14,476 = 20,612; + 1,059 = 21,671; H1 38,865 and 40,889 also tie). Slide 9 YoY labels re-derive from the mapped values (for example GP 224.3 / 188.0 = +19.3%). Slide 28 Mar-25 non-current assets foot to 1,149.2 only with goodwill 136.1 at R522. Slide 31 ROE FY24 and FY25 re-derive (89.7 / 403.45 = 22.2%; 122.3 / 685.8 = 17.8%), which confirms the positional order. Slide footers (page numbers) are not captured, which is per A1's capture note and carries no data.

### 1B. Ledger rows vs A4 citations
- A4 review:L15 marks every ID reviewed: results 643 of 643 and presentation 991 of 991, "No ledger row is unreviewed". I accept this as the explicit "reviewed, no finding" marking for rows A4 does not cite one by one.
- Spot test of material rows. Every note (0D), every agenda item (0D, K3-K16), all five filing tables (Step 1, Step 5, 5A, Point 5) and every A2 flag are cited: ENTITY_CHANGE R053/R054, FOOTNOTE_UNRESOLVED R502, ARITH_CHECK ANX1 (Q11), TITLE_MISMATCH R839 (Flag 8), PIE_ORDER (T3, 5.5C), CHART_ASSIGNMENT (52% flagged positional).
- The blanket mark covers the rows that A4 does not cite: divider slides 4, 12, 18, 24 and 26; slides 14, 17 and 21; results R033-R034 (A2 flag: 40-minute Board meeting for six items including the Rs 450 Cr capex); and R062 (auditor report day unreadable). None of these changes a conclusion.
- orphan_rows: none. missing_from_ledger: none.

Coverage result: PASS.

---

## 2. ARITHMETIC AUDIT

I converted the raw lakh values to crores (x0.01). I recomputed every derived metric that A4 prints. The table lists the load-bearing metrics. Each one carries its A4 value, my recomputed value and the source line. Rows I recomputed but do not list all tie within 0.01 Cr or 0.01 pp: Step 1 derived rows, Step 3 Q1 FY26 and H2 FY26 rows, 5.5A rupee splits, 6A targets, Q6, Q11, Q13, Q22, Q23, Q24, Q31.

| # | Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|---|
| 1 | Operating EBITDA (PBT + D + Fin - OI): Q2 FY27 / Q1 FY27 / Q2 FY26 | 88.88 / 86.37 / 77.66 | 88.876 / 86.373 / 77.658 | results:L188, L195, L196, L203 | PASS |
| 2 | Operating EBITDA H1 FY27 / H1 FY26 / FY26 | 175.25 / 153.00 / 315.54 | 175.249 / 152.999 / 315.536 | same | PASS |
| 3 | Operating EBITDA margin Q2 FY27 / Q2 FY26 / change | 15.36% / 16.26% / -89 bps | 15.365% / 16.256% / -89.1 bps | results:L187 | PASS |
| 4 | Gross margin Q2 FY27 / Q2 FY26 / H1 FY27 / FY26 | 38.78% / 39.36% / 39.05% / 39.37% | 38.780% / 39.357% / 39.054% / 39.372% | results:L187, L191-L193 | PASS |
| 5 | ETR Q2 FY27 / Q1 FY27 / H1 FY27 / FY26 | 25.13% / 18.55% / 22.20% / 29.70% | 25.129% / 18.550% / 22.205% / 29.701% | results:L203, L208 | PASS |
| 6 | ETR before earlier-years credit Q2 FY27 / Q2 FY26 | 27.07% / 27.55% | 27.075% / 27.550% | results:L206, L208 | PASS |
| 7 | Revenue YoY / PAT YoY / EPS YoY (Q2) | +21.08% / -15.48% / -14.84% | +21.081% / -15.484% / -14.842% | results:L187, L209, L223 | PASS |
| 8 | Core PBT (PBT - OI) Q2 YoY | +32.62% | 4,315.73 / 3,254.33 lakh = +32.615% | results:L188, L203 | PASS |
| 9 | Core PBT ex OI and ex FX, Q2 YoY | +23.3% | 41.36 / 33.54 = +23.3% | results:L188, L203; presentation:L255 (R198, R199) | PASS |
| 10 | PAT bridge YoY (rev, margin, D&A, fin, OI, tax x2) | +16.37, -5.15, -3.64, +3.04, -19.22, +2.20, +0.20 = -6.21 | +16.371, -5.153, -3.641, +3.037, -19.222, +2.201, +0.199 = -6.208 | results:L187-L209 | PASS |
| 11 | QoQ PBT bridge | +2.50, -1.01, +6.30, +1.25 = +9.04 | +2.503, -1.013, +6.297, +1.251 = +9.038 | results:L188-L203 | PASS |
| 12 | FX share of QoQ finance-cost fall / PBT rise | 78% / 54% | 4.9 / 6.30 = 77.8%; 4.9 / 9.04 = 54.2% | presentation:L254-L255; results:L195, L203 | PASS |
| 13 | Standalone-vs-consolidated gap, Q1 FY27 (of restated / of old PEL) | 29.4% / 41.6% | 8.660 / 29.502 = 29.36%; 8.660 / 20.842 = 41.55% | results:L360 (R445-R447) | PASS |
| 14 | Gap FY26 / H1 FY26 / Q2 FY26 / Q1 FY26 derived | 17.2/20.8; 15.6/18.5; 11.3/12.7; 23.2/30.2 | 17.22/20.80; 15.60/18.48; 11.25/12.68; 23.22/30.24 | results:L360, L367 | PASS |
| 15 | Former-subsidiary PBT margin Q1 FY27 vs old PEL; YoY PBT | 13.1% vs 5.6%; old PEL -15.7%, subs +59.7% | 11.469 / 87.357 = 13.13% vs 24.752 / 442.589 = 5.59%; -15.70%, +59.65% | results:L358-L359, L365-L366 | PASS |
| 16 | CFO/PAT H1 FY27 / H1 FY26 | 5.10x / 1.51x | 5.096x / 1.515x | results:L307, L209 | PASS |
| 17 | FCF (CFO - capex) / FCF after finance charges and lease interest | 66.19 / 23.32 | 66.194 / 23.324 | results:L307, L310, L317, L319 | PASS |
| 18 | Day counts: receivable / inventory / payable / CCC | 39.4 to 35.8; 124.3 to 129.8; 76.6 to 128.7; 87.1 to 36.9 | 39.36 to 35.84; 124.29 to 129.78; 76.57 to 128.72; 87.08 to 36.90 | results:L244, L247, L273-L274; L187-L193 | PASS |
| 19 | Net debt ex leases Mar-26 / Sep-26 | 552.11 / 538.68 | 552.107 / 538.676 | results:L246-L249, L262, L270 | PASS (definition caveat: finding A5-M2) |
| 20 | Net debt / TTM operating EBITDA | 1.59x on 337.79 | 538.68 / 337.787 = 1.595x | derived from rows 2, 19 | PASS |
| 21 | TTM EPS / TTM PE / market value | 32.02 / 29.9x / Rs 3,605 Cr | 32.02 / 29.89x / Rs 3,605.0 Cr | results:L223, L220, L493 | PASS |
| 22 | Qualified tier share / adjusted EBITDA per tonne / sales per tonne | 29.8% vs 26.8% / Rs 36.9k vs 39.9k (-7.5%) / -1.4% | 29.77% vs 26.77% / Rs 36,878 vs 39,889 (-7.55%) / -1.42% | presentation:L184-L195, L244 | PASS |
| 23 | Castings: implied Q1 FY27 / H2 need per quarter | 2,968 MT / 5,473 MT (+77.3%) | 2,968 / 5,473 (+77.35%) | presentation:L195 (R076, R079) | PASS |
| 24 | FY26 ROE reproduction on goodwill-inclusive equity | 12.5% (117.8 / 942.8) | 12.49%; on printed restated equity 13.47% | presentation:L760, L780-L781, L868 | PASS |
| 25 | **ROE/ROCE mechanical lift from goodwill removal** (review:L112, L430) | "about 14% relative (136.1 / 986.9)" | 13.8% is the cut in equity, not the ratio lift. ROE lift = 986.9 / 850.8 - 1 = **+16.0%**. ROCE lift on equity + gross borrowings = 1,685.75 / 1,549.65 - 1 = **+8.8%** (with leases +8.2%) | presentation:L785 (R522), L780 (R577); results:L258, L262, L270 | **FAIL (A5-F3)** |
| 26 | **Q2 margin walk vs narrative cause** (review:L615) | "slipped 0.9 points ... because staff costs grew faster than sales" | Gross margin -57.7 bps = 65% of the -89.1 bps slip. Employee cost/revenue +26.1 bps. Other expenses/revenue +5.3 bps. A4's own walk at review:L211 shows the same | results:L187, L191-L194, L197 | **FAIL (A5-F1)** |
| 27 | **"FCF without supplier credit"** (review:L618; L285 verdict cell) | minus Rs 98.6 Cr | -98.65 is FCF before all working-capital movement (WC release +164.84). The supplier credit alone is +231.52 (payables), which exceeds the total release. FCF ex the payables rise = 66.19 - 231.52 = **-165.33** (other WC items absorbed 66.68) [derived, BS-delta proxy] | results:L304, L307, L310, L273-L274 | **FAIL (A5-F2)** |
| 28 | **Lease-principal sign: direction of the CFO effect** (Q16, review:L491) | "CFO may be overstated by Rs 11.56 Cr"; bear answer "CFO restated lower" | The financing total -12,020.21 lakh foots only with +578.15 (the same holds for H1 FY26: +146.42 foots with +653.41). Closing cash 5,907.64 lakh ties to the BS (L248). A sign fix that keeps the cash tie raises CFO, or cuts the investing outflow, by Rs 11.56 Cr. This error cannot make CFO overstated | results:L307, L315, L317-L330, L248 | **FAIL (A5-F4)** |
| 29 | H1 operating margin change | -56 bps | -55.2 bps (16.376% to 15.823%) | results:L187 | STYLE (rounding on rounded inputs) |
| 30 | Employee cost / revenue change, Q2 | +27 bps | +26.1 bps | results:L187, L194 | STYLE |
| 31 | Core PBT change, Q2 YoY | +10.62 | +10.614 | results:L188, L203 | STYLE |
| 32 | Pre-WC after-tax cash H1 FY27; FCF ex WC; net debt incl leases | 158.19; -98.64; 663.85 / 652.60 | 158.183; -98.648; 663.844 / 652.592 | results:L303, L306; L263, L271 | STYLE (0.01 drift) |

Arithmetic result: FAIL. Four derived claims differ from the recomputed values by more than rounding (rows 25-28). Every table total, margin, ETR, bridge, day count and gap ties.

---

## 3. ADVERSARIAL READ

### Claim 1 (most positive): "The headline decline is not an operating decline ... The whole PAT decline comes from the non-recurring base. Core operations added profit." (review:L212, L253 tags the -19.22 OI change NON-RECURRING, L264, narrative L613 "The fall came from one line")
Strongest bear counter from the extract:
- Other income was a recurring line for three years. The deck history shows Rs 48.5 Cr in FY24, Rs 38.8 Cr in FY25 and Rs 40.1 Cr in FY26 (presentation:L741-L742; R411, R410, R409). That is 2.1% to 3.9% of revenue every year.
- Outside the Q2 FY26 spike, FY26 still carried a baseline. Q1 FY26 had Rs 7.40 Cr (H1 28.73 less Q2 21.32). H2 FY26 had Rs 11.38 Cr, or Rs 5.69 Cr a quarter (FY 40.11 less H1 28.73) [derived, results:L188].
- FY27 runs Rs 0.85 Cr (Q1) and Rs 2.10 Cr (Q2) (results:L188). About Rs 3.6 to 5.3 Cr a quarter, pre-tax, of the -19.22 is a lost baseline and not the spike.
- Effect on A4's bridge: the recurring core pre-tax gain falls from +7.8 to about +2.5 to +4.2 Cr. The annualised loss of about Rs 34 Cr pre-tax (FY26 Rs 40.1 Cr vs FY27 run-rate of about Rs 6 Cr) is close to 21% of FY26 PAT after tax. The source of the OI is NOT FOUND (A4's own Q8). So the NON-RECURRING tag on the full -19.22 is not evidenced.
- What survives of A4's claim: core operations still added profit, and most of the YoY fall is still the Q2 FY26 spike.
- Verdict: **the counter SURVIVES as a qualifier (MISSING, A4).** Graft it into Step 2 diagnostic 6, the Step 4 bridge (split the OI row: spike about -15.6, baseline about -3.6) and mandatory Q1, and into the narrative line at L613. Raise Q8's bear answer to the main reading until the source is named.

### Claim 2: "Exports rose to Rs 154.3 Cr and broke a five-quarter plateau." (narrative L624; 6D L413 ON TRACK; GV-b L436 "Positive")
Strongest bear counter from the extract:
- H1 outside-India revenue grew only +6.3% (Rs 291.78 Cr vs Rs 274.49 Cr, results:L395), against company revenue +18.5%.
- Export share fell in Q2 (26.7% vs 28.3%) and in H1 (26.3% vs 29.4%) (results:L394-L396).
- Outside-India segment assets fell 54.8% YoY (results:L399).
- The railway share of the pie fell from 32% to 27% (presentation:L437-L447, order unverified).
- Verdict: **the counter is supported, but A4 already carries it**: share fall at L413, segment assets at Q13 (L488), railway at T3 (L344) and the M2 contradiction at L526. No graft needed.

### Claim 3: capacity commissioning passes, and castings tonnage "tests whether the Rs 290 Cr programme fills its capacity before the Rs 450 Cr follows" (review:L238, L463; T2 thesis element L343 "Castings capacity fill under the Rs 290 Cr programme")
Strongest bear counter from the extract:
- Slide 5 labels the left column "Capacity before capex announcement of Rs 290 Crores" (presentation:L125; R919). Castings in that column is 24,600 MT (L133; R006).
- Current castings capacity is also 24,600 MT (slide 6, L163; R033). Only machining carries a "current" footnote showing growth past the pre-programme level (7,20,000 to 8,13,600 hours, L136, L149).
- So the castings plant running at 52% is **pre-programme capacity**. The castings step that the Rs 290 Cr + Rs 450 Cr programme funds, to 36,000 MT by FY31 (+46%, L133; R007), has not landed yet. A4's own Q10 (L485, memory "36,000 MT by Q1 FY29") points the same way and contradicts the 8C framing.
- At Q2's implied output run-rate (52% x 24,600 = 12,792 MT a year, positional R021), 36,000 MT of capacity would run at about 35.5%.
- Verdict: **the counter SURVIVES (FACTUAL, A4).** Reword 8C (L463) and the T2 reading (L343). Add the 35.5% at-target utilisation to the castings bear case. Log a memory difference N10: memory frames the castings fill under the Rs 290 Cr programme, and deck slide 5 places 24,600 MT before that programme.

### Mandatory acquisition-economics probe
- What the documents describe: a no-consideration common-control merger of two wholly-owned subsidiaries, "dissolved without winding up" (results:L351; R429). They also refer back to the FY25 acquisition behind it: goodwill was nil at Mar-24 and Rs 136.1 Cr at Mar-25 (presentation:L785-L786; R522). The new COO M&G is described as "turned senior leader post-acquisition" (presentation:L627-L633; R792).
- Purchase consideration: NOT FOUND in either document.
- Multiple: consideration is at least the goodwill, so the floor is **about Rs 136.1 Cr / Rs 20.28 Cr FY26 PAT contribution of the merged entities = 6.7x** (results:L367; R474, net of eliminations). On the Q1 FY27 contribution annualised (8.66 x 4 = 34.64, results:L360; R446) the floor is 3.9x. The full price/PAT is NOT FOUND.
- Quality markers: Q1 FY27 PBT margin 13.1% vs old PEL 5.6%, and PBT +59.7% YoY (row 15 above). Debt, ROCE, cash and customer tenure of the targets: NOT FOUND.
- Representativeness: the contribution rose from Rs 5.31 Cr (Q1 FY26) to Rs 8.66 Cr (Q1 FY27). One quarter cannot separate a growth step from a peak, and the merger now removes the series (A4 5A, Q17).
- Bear reading: the acquisition cost left the equity base through a reserve entry and never through ROE. A4 already carries this (Point 3, P1-a, Flag 4, Q4). Neither document makes a cheap-acquisition claim.
- Result: **no graft needed.** The floor multiple is recorded here for the operator.

---

## 4. FINDINGS REGISTER (every finding tagged)

| ID | Type | Fix agent | Finding | Anchor |
|---|---|---|---|---|
| A5-F1 | FACTUAL | A4 | Narrative blames staff costs for the margin slip. Gross margin is 65% of it (-57.7 of -89.1 bps); staff cost is +26.1 bps. Rewrite L615 | review:L615, L211; results:L187, L191-L194, L197 |
| A5-F2 | FACTUAL | A4 | "Without that supplier credit, FCF was minus Rs 98.6 Cr" mislabels FCF before all working capital. FCF ex the payables rise is about -165.3 Cr. Relabel L618 and the L285 verdict cell, or state both figures | review:L618, L285; results:L304, L307, L310, L273-L274 |
| A5-F3 | FACTUAL | A4 | Goodwill-removal lift stated as "about 14% relative" for ROE and ROCE. It is +16.0% for ROE and about +8.8% for ROCE. Fix Point 3 item 2 and P1-a | review:L112, L430; presentation:L780, L785; results:L258, L262, L270 |
| A5-F4 | FACTUAL | A4 (A3-25 origin; A3 note may need the same fix) | Q16 says the lease-sign error may overstate CFO by Rs 11.56 Cr. Given the cash tie, a fix can only raise CFO or cut the investing outflow. Restate the "why it matters" text and the bear answer | review:L491; results:L317-L330, L248 |
| A5-F5 | FACTUAL | A4 | 8C frames Q3 castings tonnage as the fill test of the Rs 290 Cr programme. Slide 5 puts 24,600 MT before that programme, so the +46% castings step is still ahead (about 35.5% utilisation at Q2 run-rate). Reword L463 and L343, add memory difference N10 | review:L463, L343, L485; presentation:L125, L133, L149, L155, L163 |
| A5-M1 | MISSING | A4 | Surviving bear counter 1: OI was Rs 38.8-48.5 Cr a year FY24-FY26 with a Rs 5.7-7.4 Cr quarterly baseline, which FY27 lacks. The NON-RECURRING tag on the full -19.22 is unevidenced. Recurring core pre-tax gain is about +2.5 to +4.2, not +7.8 | review:L212, L253, L264, L613; presentation:L741-L742; results:L188 |
| A5-M2 | MISSING | A4 | Net-debt (T1) basis caveat absent. Other bank balances rose from Rs 27.27 Cr to Rs 42.65 Cr, and the Rs 15.28 Cr placement is classified under FINANCING activities (L324). That is consistent with margin money against LCs or borrowings [INFERENCE]. If lien-marked, net debt ex leases is up to Rs 581.33 Cr at Sep-26 and Rs 579.38 Cr at Mar-26: H1 change +1.95 (rising), not -13.43. Add as T1 caveat (e) and extend Q1 | review:L300, L342, L348, L476; results:L249, L324 |
| A5-S1 | STYLE | none | Rounding drift on rounded inputs: H1 margin -56 vs -55 bps; employee +27 vs +26 bps; core PBT +10.62 vs +10.61; 158.19 vs 158.18; -98.64 vs -98.65; 663.85/652.60 vs 663.84/652.59 | arithmetic rows 29-32 |
| A5-S2 | STYLE | none | Q9 (L484) says the rest of the finance-cost fall "is unexplained". Point 1 (L90) explains the Rs 1.3 Cr as interest moving with debt. Align the wording; the question stands | review:L90, L484 |
| A5-S3 | STYLE | none | The protocol verdict PROCEED WITH FLAGS appears only in the Step 9 Key Notes (L567), the YAML (L681) and the analyst note. There is no verdict line in the body | review:L567, L681 |
| A5-S4 | STYLE | none | Flag 7 puts "81% of net worth" after "Rs 450 Cr new capex". The 81% is the Rs 740 Cr total (Q6 L481) | review:L599, L481 |
| A5-S5 | STYLE | none (A2) | Ledger L5 says 35 zero-standing tags sit "across 13 line items". 32 sit on 13 line items; 3 (R593, R594, R596) sit on the ANX2v vesting schedule. The count is correct | ledger_results L5, L198 |

Counts: FACTUAL 5, MISSING 2, CONTRADICTION 0, STYLE 5.

---

## 5. VERDICT

**INCOMPLETE.** Failing agent: **A4**. Finding types: FACTUAL (A5-F1 to F5) and MISSING (A5-M1, M2). No CONTRADICTION.

Exact gap for the A4 rework (one pass, no new extraction needed):
1. L615: margin slip cause is gross margin (-58 bps of -89), not staff cost.
2. L618 and L285: -98.6 is FCF before all working capital. FCF ex supplier credit is about -165.3.
3. L112 and L430: the goodwill lift is ROE +16.0% and ROCE about +8.8%, not "about 14%".
4. Q16 L491: the lease-sign fix raises CFO. Drop "overstated" and "CFO restated lower".
5. L463 and L343: 24,600 MT castings is pre-Rs 290 Cr capacity. The step to 36,000 MT is still ahead (about 35.5% at Q2 run-rate). Add memory difference N10.
6. Graft the OI baseline counter: Rs 38.8-48.5 Cr a year FY24-FY26, a Rs 3.6-5.3 Cr a quarter lost baseline, recurring core +2.5 to +4.2 not +7.8.
7. T1 caveat (e): Rs 42.65 Cr other bank balances, funded through financing (results:L324), may be margin money. Net debt would then be up to Rs 581.33 Cr and rising in H1.

Coverage (PASS) and the brief gate (PASS) need no re-run of A2 or A3. A3 may mirror fix 4 in its note A3-25. That is not a gate.

## 6. STYLE NOTES (logged, no loop)
- A5-S1 rounding drift (rows 29-32).
- A5-S2 Q9 vs Point 1 wording.
- A5-S3 no body verdict line.
- A5-S4 Flag 7 referent.
- A5-S5 A2 zero-standing description.

---

```yaml
# ITERATION 1 BLOCK (superseded by the ITERATION 3 block at the end of this file)
stage: A5-adversary
company: "PITTIENG"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "ROE/ROCE mechanical lift from goodwill removal (review L112, L430)"
    a4_value: "about 14% relative (136.1/986.9)"
    recomputed: "ROE +16.0% (986.9/850.8); ROCE +8.8% (1,685.75/1,549.65 on equity + gross borrowings); 13.8% is the equity cut, not the ratio lift"
    source_line: "presentation:L780, L785 (R577, R522); results:L258, L262, L270"
  - metric: "Q2 operating margin slip cause (narrative L615)"
    a4_value: "because staff costs grew faster than sales"
    recomputed: "gross margin -57.7 bps of -89.1 bps (65%); employee +26.1 bps; other expenses +5.3 bps"
    source_line: "results:L187, L191-L194, L197"
  - metric: "FCF without supplier credit, H1 FY27 (narrative L618; Step 5 L285)"
    a4_value: "-98.6"
    recomputed: "-98.65 is FCF before all working capital; FCF ex payables rise (+231.52) = -165.33"
    source_line: "results:L304, L307, L310, L273-L274"
  - metric: "Lease-principal sign, direction of CFO effect (Q16 L491)"
    a4_value: "CFO may be overstated by Rs 11.56 Cr"
    recomputed: "financing total foots only with +578.15 and closing cash ties to BS; a fix keeping the tie raises CFO or cuts investing outflow by 11.56; CFO cannot be overstated by this"
    source_line: "results:L317-L330, L248"
surviving_bear_counters:
  - claim: "PAT fall is not operating; whole decline is the non-recurring OI base (review L212, L253, L264, L613)"
    counter: "OI ran Rs 38.8-48.5 Cr a year FY24-FY26 and Rs 5.7-7.4 Cr a quarter outside the Q2 FY26 spike; FY27 runs 0.85 and 2.10. About Rs 3.6-5.3 Cr a quarter is a lost baseline; recurring core pre-tax gain is about +2.5 to +4.2, not +7.8"
    source_line: "presentation:L741-L742 (R409-R411); results:L188"
    type: MISSING
  - claim: "Castings tonnage tests fill of the Rs 290 Cr programme; commissioning test passes (review L238, L463, L343)"
    counter: "Slide 5 places 24,600 MT castings capacity before the Rs 290 Cr announcement and it has not moved; the step to 36,000 MT (+46%) is still ahead; Q2 implied output 12,792 MT a year is about 35.5% of 36,000 MT"
    source_line: "presentation:L125, L133, L149, L155, L163 (R006, R007, R919, R021, R033)"
    type: FACTUAL
findings_by_type:
  factual:
    - "A5-F1 (A4): narrative L615 blames staff costs; gross margin is 65% of the -89 bps slip"
    - "A5-F2 (A4): L618/L285 label -98.6 as FCF without supplier credit; it is FCF before all WC; ex payables it is about -165.3"
    - "A5-F3 (A4): L112/L430 goodwill lift 'about 14%'; ROE +16.0%, ROCE about +8.8%"
    - "A5-F4 (A4; origin A3-25): Q16 L491 says lease-sign fix may lower CFO; with the cash tie it can only raise CFO"
    - "A5-F5 (A4): L463/L343 frame castings fill as the Rs 290 Cr programme; slide 5 shows 24,600 MT is pre-programme, +46% still ahead"
  missing:
    - "A5-M1 (A4): OI recurring baseline (Rs 38.8-48.5 Cr a year FY24-FY26) absent; NON-RECURRING tag on full -19.22 unevidenced"
    - "A5-M2 (A4): T1 net-debt caveat absent; Rs 42.65 Cr other bank balances funded through financing (results:L324) may be margin money; net debt up to Rs 581.33 Cr and rising in H1"
  contradiction: []
  style:
    - "A5-S1: rounding drift on rounded inputs (H1 -56 vs -55 bps; +27 vs +26 bps; 10.62 vs 10.61; 158.19 vs 158.18; -98.64 vs -98.65; 663.85/652.60 vs 663.84/652.59)"
    - "A5-S2: Q9 L484 'rest is unexplained' vs Point 1 L90 'interest moved in line with debt'"
    - "A5-S3: protocol verdict only in Step 9 Key Notes, YAML and analyst note; no body verdict line"
    - "A5-S4: Flag 7 L599 '81% of net worth' refers to Rs 740 Cr, not Rs 450 Cr"
    - "A5-S5 (A2): ledger L5 '13 line items' wording; 3 of 35 zero-standing tags sit on the vesting schedule"
loop_back_to: "A4"
gap: "A4 rework, 7 items: (1) L615 margin cause is gross margin -58 of -89 bps, not staff cost; (2) L618/L285 -98.6 is FCF before all WC, ex supplier credit about -165.3; (3) L112/L430 goodwill lift ROE +16.0%, ROCE about +8.8%, not 14%; (4) Q16 L491 lease-sign fix raises CFO, drop 'overstated'; (5) L463/L343 castings 24,600 MT is pre-Rs 290 Cr capacity, step to 36,000 MT still ahead (about 35.5% at Q2 run-rate), add memory difference N10; (6) graft OI baseline counter, recurring core +2.5 to +4.2 not +7.8; (7) T1 caveat: Rs 42.65 Cr other bank balances funded via financing (results:L324) may be margin money, net debt up to 581.33 and rising in H1"
style_notes:
  - "A5-S1 rounding drift"
  - "A5-S2 Q9 vs Point 1 wording"
  - "A5-S3 no body verdict line"
  - "A5-S4 Flag 7 referent"
  - "A5-S5 A2 zero-standing description"
analyst_note: "Brief gate and coverage pass: counts match A2 on both documents, and the fulltext sweep found no unit missing from the structured files. Every table total, margin, ETR, bridge, day count and gap ties. The failures are in derived claims and the narrative, which the operator reads first, and all seven fit in one A4 pass. Two fixes change the bear case most. First, castings at 52% is pre-programme capacity, so the funded step to 36,000 MT would run near 35% at today's output. Second, other income was a recurring line of about Rs 40 Cr a year, so part of its fall is a lost baseline and the recurring core gain is smaller than A4 states. The net-debt caveat on deposits placed through financing is an inference; if those deposits are lien-marked, H1 net debt rose. Acquisition probe: no price is disclosed; goodwill alone is 6.7x the merged entities' FY26 PAT contribution; A4 already carries the goodwill bear."
```

---

## ITERATION 2 RE-AUDIT (2026-10-23)

Trigger: coordinator re-audit, correction loop iteration 1 of 1. A4 revised work/review_pittieng_q2fy27.md in place (revision line review:L4; CORRECTION LOG review:L581-L592).
Scope: (a) re-check each FACTUAL and MISSING finding against the A1 fulltexts; (b) scan every changed passage for new errors; (c) re-run the brief gate and the coverage check on the revised file.
Line numbers in this section (review:L###) refer to the iteration-1 REVISED review (before the loop-2 edits).
Passages scanned: L4, L7; Point 3 L113; Step 2 L202-L216; Step 3 L232-L239; Step 4 L254-L268; Step 5 L288-L318; 5.5A-B L348-L361; 6A-6D L383-L421; Steps 6.5/7 L436-L442; Step 8 L462-L470; Q8-Q10, Q16, Q32 L490-L514; top-3 and channel L516-L521; M5 note L542; K1, K6-K8 L550-L557; Key Notes and tracker payload L575-L576; correction log L581-L592; N10 L609; Flags L615-L622; Brief L634-L689; YAML L699-L791.

### R1. Iteration-1 findings re-checked against the extract

| ID | Type | Fix in revised review | Re-check against A1 fulltext | Status |
|---|---|---|---|---|
| A5-F1 | FACTUAL | L212 and narrative L639: gross margin named as the main cause (-58 bps, about two-thirds); staff cost +26 bps second | 39.357% to 38.780% = -57.7 bps; employee 8.324% to 8.585% = +26.1 bps; other 14.777% to 14.830% = +5.3 bps (results:L187, L191-L194, L197) | CLOSED |
| A5-F2 | FACTUAL | L288 relabelled "FCF before all working-capital change" (-98.64); new row L289 FCF ex payables rise -165.33; narrative L642; P2-a L439; Flag 3 L617 | 66.194 - 231.517 = -165.32; other WC items absorbed 66.68 (results:L307, L310, L304, L273-L274). H1 FY26 left ND because Sep-25 BS is not filed: correct | CLOSED |
| A5-F3 | FACTUAL | Point 3 item 2 L113; P1-a L436; Flag 4 L618 | ROE 986.91 / 850.81 - 1 = +16.0%; ROCE 1,685.76 / 1,549.66 - 1 = +8.8%; with leases 111.74 added +8.2% (results:L258, L262-L263, L270-L271; presentation:L785 R522) | CLOSED |
| A5-F4 | FACTUAL | Q16 L498 reworded; bear answer now "built to a plug" | Financing total (12,020.21) lakh at L327 foots with +578.15 at L318; closing cash 5,907.64 at L330 = BS L248. Bear answer is a fair question, not a claim | CLOSED |
| A5-F5 | FACTUAL | L239, L317, T2 L349, 5.5B L360, 6D L421, 8A-W L462, 8C L470, Q10 L492, N10 L609, Flag 2 L616, Brief L645, L665, L672, L686 | Slide 5 "Capacity before capex announcement of Rs 290 Crores" castings 24,600 (presentation:L125, L133; R919, R006); current 24,600 (L163; R033); 36,000 / 24,600 = +46.3%; 0.52 x 24,600 = 12,792; 12,792 / 36,000 = 35.5% | CLOSED |
| A5-M1 | MISSING | L202, L216, bridge split L254-L256, L267-L268, E-a L441, Q8 L490, Flag 5 L619, Brief L636-L637, L666, L682 | FY24-FY26 48.5 / 38.8 / 40.1 (presentation:L741-L742; R411, R410, R409); Q1 FY26 7.40 and H2 FY26 5.69 a quarter (results:L188); spike 21.32 - 5.69 = 15.63; baseline 5.69 - 2.10 = 3.59 (or 7.40 - 2.10 = 5.30); rows sum to -19.22 | CLOSED as a graft. The graft created new finding A5-C1 (below) |
| A5-M2 | MISSING | Step 5 rows L304, L306; Q4 L318; T1 L348 and caveat (e) L354; 6A L383; 6B L401; P2-b L440; Q32 L514; K7 L556; Brief L643, L682, L687 | Other bank balances 2,727.44 to 4,265.48 lakh = +15.38 (results:L249; R286-R287); placement (1,528.20) lakh sits in the financing total at L324 (R403); 552.11 + 27.27 = 579.38; 538.68 + 42.65 = 581.33; change +1.95. [INFERENCE] label carried on every use | CLOSED |

### R2. New-error scan of the changed passages

**A5-C1 | CONTRADICTION | fix agent A4 | new in iteration 2.** The review uses "baseline" for two quantities that do not reconcile.
- Reading A sits in the bridge (L254-L255), Step 2 diagnostic 6 (L216) and Step 4 mandatory Q1 (L267). The Q2 FY26 item above Rs 5.69 Cr is NON-RECURRING (-15.63). The lost baseline is Rs 3.6-5.3 Cr a quarter, about Rs 14-21 Cr a year. The recurring pre-tax gain is +2.5 to +4.2.
- Reading B sits in E-a (L441), Q8 (L490: "a lost baseline of about Rs 34 Cr a year pre-tax"), Flag 5 (L619), the YAML flag (L779) and the analyst note (L791). These call the full Rs 38.8-48.5 Cr a year a baseline. Rs 34 Cr is the full-line change: FY26 Rs 40.11 Cr vs an FY27 run-rate of (0.85 + 2.10) x 2 = Rs 5.90 Cr (results:L188). It includes the Q2 FY26 item that the bridge calls non-recurring.
- Flag 5 and the analyst note pair Reading B's baseline with Reading A's gain. Those do not compute together. On a Rs 38.8-48.5 Cr a year level (Rs 9.70-12.13 Cr a quarter), Q2's lost baseline is Rs 7.60-10.03 Cr. The recurring pre-tax change is then +0.2 to -2.2, not +2.5 to +4.2. If the Q2 FY26 item recurs every Q2, the change is 7.78 - 19.22 = -11.4. Under Reading B, "core operations still added profit" (L267) holds for the operating rows only, not for the recurring earnings base.
- Same issue, minor part: L216 pairs a spike of -15.6 with a baseline of up to -5.3. At the Rs 7.40 Cr baseline the spike is -13.92, and the two rows still have to sum to -19.22.
- Why it matters: Flag 5 and the analyst note are what Notion and the operator read. The sign of the recurring pre-tax change depends on which reading holds, and the documents do not settle it (source NOT FOUND, Q8).
- Note: my iteration-1 text (section 3, Claim 1) placed the Rs 34 Cr annualised figure next to the quarterly split without labelling the two readings. That seeded the mix-up.
- Fix, with exact replacement text ready to apply. At L216, L268, L441, L490, L619, L779 and L791, replace the single "baseline" wording with two labelled readings. Two observations separate them: the Q8 answer (source of the Q2 FY26 Rs 21.32 Cr) and Q2 FY25 other income, which is not in these documents.
  - "Reading A (Q2 FY26 item one-off): lost other-income baseline Rs 3.6-5.3 Cr a quarter, about Rs 14-21 Cr a year; recurring pre-tax change in Q2 +2.5 to +4.2."
  - "Reading B (the item recurs yearly; FY24-FY26 totals were stable at Rs 38.8-48.5 Cr): lost recurring other income about Rs 34 Cr a year; recurring pre-tax change in Q2 between about -2 (level spread evenly) and -11.4 (item seasonal to Q2)."
  - Flag 5, Q8 and the analyst note then quote both ranges and drop the bare "baseline Rs 38.8-48.5 Cr ... recurring gain +2.5 to +4.2" pairing.

No other new error was found. I recomputed every new number in the changed passages and each one ties to the extract: 1,685.76 / 1,549.66; 1,797.49 / 1,661.39; -165.33; 66.7; 15.38; 579.38; 581.33; +1.95; -15.63; -3.59; -5.30; -39.0%; -9.0%; -12.8; Rs 34 Cr as a line change; 12,792 MT; 35.5%; +46%; -55 bps; +26 bps; +10.61.

### R3. Gates on the revised file
- Brief gate: PASS. Narrative L634-L650 is 17 lines (limit 10-20). Sector L652-L657, business model L659-L667, competition L669-L675 and forward map L677-L689 are all present. The forward map still has 8 dated rows, each with a bull and a bear fork.
- Coverage: PASS, unchanged. A4 added no new row IDs. Q32 and the new Step 5 rows cite results:L249 and L324, which are R286-R287 (ledger LI046) and R403-R404 (ledger LI103). orphan_rows: none. missing_from_ledger: none.
- STYLE status: A5-S2 fixed (Q9 L491). A5-S1 partly fixed: -55 bps, +26 bps and +10.61 are corrected; 158.19, -98.64 and 663.85/652.60 still show 0.01 drift. A5-S3, A5-S4 and A5-S5 remain open. All are logged only.

### R4. Iteration 2 verdict
**INCOMPLETE.**
- Open: 1 CONTRADICTION, A5-C1, fix agent A4.
- Closed: 5 FACTUAL (A5-F1 to F5) and 2 MISSING (A5-M1, M2).
- The fix is wording only: the exact text is above. It needs no new extraction and no re-run of A2 or A3.
- This was loop 1 of 1. The orchestrator decides whether A5-C1 goes to Halt 1 as an open item, or takes the replacement text with operator approval.

```yaml
# ITERATION 2 BLOCK (superseded by the ITERATION 3 block at the end of this file)
stage: A5-adversary
company: "PITTIENG"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
re_audit: true
iteration: 2
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "Recurring pre-tax change paired with the 'Rs 38.8-48.5 Cr a year baseline' (Flag 5 L619; YAML flag L779; analyst note L791)"
    a4_value: "baseline Rs 38.8-48.5 Cr a year gone, so recurring pre-tax gain +2.5 to +4.2"
    recomputed: "+2.5 to +4.2 holds only on the FY26 ex-spike baseline (Rs 5.69-7.40 a quarter). On a Rs 38.8-48.5 Cr a year level the Q2 change is +0.2 to -2.2; if the Q2 FY26 item recurs each Q2 it is -11.4"
    source_line: "presentation:L741-L742 (R409-R411); results:L188"
surviving_bear_counters: []  # both iteration-1 counters (A5-M1 other income, A5-F5 castings) grafted into A4 and re-checked
findings_by_type:
  factual: []
  missing: []
  contradiction:
    - "A5-C1 (A4, new in iteration 2): 'baseline' used for two quantities. Bridge/diag 6/mandatory Q1 (L216, L254-L255, L267) use the FY26 ex-spike baseline (Rs 3.6-5.3 Cr a quarter, gain +2.5 to +4.2); E-a L441, Q8 L490, Flag 5 L619, YAML L779 and analyst note L791 call the full Rs 38.8-48.5 Cr a year baseline and a Rs 34 Cr a year loss, yet keep the +2.5 to +4.2 gain. On that level the Q2 recurring change is +0.2 to -2.2 (or -11.4 if the item is seasonal to Q2)"
  style:
    - "A5-S1 (partial): 0.01 drift remains on 158.19, -98.64, 663.85/652.60"
    - "A5-S3: protocol verdict only in Step 9 Key Notes, YAML and analyst note; no body verdict line"
    - "A5-S4: Flag 8 L622 '81% of net worth' refers to Rs 740 Cr, not Rs 450 Cr"
    - "A5-S5 (A2): ledger L5 '13 line items' wording; 3 of 35 zero-standing tags sit on the vesting schedule"
closed_findings: [A5-F1, A5-F2, A5-F3, A5-F4, A5-F5, A5-M1, A5-M2, A5-S2]
loop_back_to: "A4"
gap: "A5-C1: at L216, L268, L441, L490, L619, L779, L791 replace the single 'baseline' wording with two labelled readings separated by the Q8 answer and Q2 FY25 other income. Reading A (Q2 FY26 item one-off): lost baseline Rs 3.6-5.3 Cr a quarter, about Rs 14-21 Cr a year; Q2 recurring pre-tax change +2.5 to +4.2. Reading B (item recurs yearly; FY24-FY26 totals Rs 38.8-48.5 Cr): lost recurring other income about Rs 34 Cr a year; Q2 recurring pre-tax change about -2 (even spread) to -11.4 (seasonal to Q2). Also pair spike -13.92 with the Rs 7.40 Cr baseline at L216. Loop 1 of 1 used: orchestrator routes to Halt 1 or applies this text with operator approval"
style_notes:
  - "A5-S1 partial rounding drift"
  - "A5-S3 no body verdict line"
  - "A5-S4 Flag 8 referent"
  - "A5-S5 A2 zero-standing description"
analyst_note: "Iteration 2. All seven iteration-1 findings are fixed and re-check clean against the A1 fulltexts: margin cause, FCF labels, goodwill lift, lease-sign direction, castings pre-programme capacity, the other-income graft and the deposits caveat. Coverage and the brief gate still pass. The other-income graft introduced one contradiction. The bridge treats the Q2 FY26 item as one-off and finds a lost baseline of Rs 3.6-5.3 Cr a quarter, giving a recurring pre-tax gain of +2.5 to +4.2. Q8, E-a, Flag 5 and the analyst note instead call the full Rs 38.8-48.5 Cr a year a baseline and quote a Rs 34 Cr a year loss, while keeping the +2.5 to +4.2 gain. Those do not compute together: on the annual-level reading the Q2 recurring change is about 0 to -2, or -11.4 if the item is seasonal to Q2. The fix is wording, not new evidence: name both readings and the observation that separates them (the Q8 answer and Q2 FY25 other income). This was loop 1 of 1, so the orchestrator decides whether C1 goes to Halt 1 or takes the exact replacement text in the audit."
```

---

## ITERATION 3 RE-AUDIT (loop 2) (2026-10-24)

Trigger: coordinator re-audit, correction loop iteration 2 (operator-approved 2026-10-24; the last permitted). A4 revised work/review_pittieng_q2fy27.md in place for A5-C1 and applied STYLE A5-S3 and A5-S4 (revision line review:L4; CORRECTION LOG review:L587-L601, A5-C1 row L597).
Scope: (a) check A5-C1 against the A1 fulltexts; (b) scan every changed passage for new errors; (c) re-run the brief gate and coverage on the revised file.
Line numbers in this section (review:L###) refer to the loop-2 REVISED review.
Passages scanned: L4; Step 2 table L202 and diagnostic 6 L216-L219; Step 4 table L257-L259, check L265, mandatory Q1-Q2 L270-L271; E-a L444; Step 8 verdict line L458 and 8A-W L467; Q8 L495; K17 L571; Key Notes L581; correction log L587-L601; Flags L622-L636 (Flag 5 L628, Flag 8 L631); Brief L643-L698 (L646, L675, L691); YAML L708-L804 (fixes L717-L719, Q8 L746, K17 L781, flag L792, analyst_note L804).
Residual-wording check: grep "baseline" in the revised review hits only the correction-log row L595, which describes the old wording. grep "+2.5 to +4.2" hits only lines that label it Reading A (L217, L270, L495, L628, L792, L804, and the logs L597, L717).

### S1. A5-C1 re-checked against the extract

| Location | Revised text (summary) | Re-check against A1 fulltext | Result |
|---|---|---|---|
| Diag 6 L216 | FY27 run-rate (0.85 + 2.10) x 2 = Rs 5.90 Cr vs FY26 Rs 40.11 Cr: line change about Rs 34.2 Cr | results:L188: 2.95 x 2 = 5.90; 40.11 - 5.90 = 34.21 | ties |
| Reading A L217 | level Rs 5.69-7.40 Cr a quarter; pairs -15.63/-3.59 and -13.92/-5.30; lost Rs 3.6-5.3 Cr a quarter, about Rs 14-21 Cr a year; Q2 recurring change +2.5 to +4.2 | 21.32 - 5.69 = 15.63; 5.69 - 2.10 = 3.59; 21.32 - 7.40 = 13.92; 7.40 - 2.10 = 5.30; each pair sums to 19.22; 3.59 x 4 = 14.4, 5.30 x 4 = 21.2; 7.78 - 5.30 = 2.48, 7.78 - 3.59 = 4.19 (results:L188; Q1 FY26 = H1 28.73 - Q2 21.32; H2 = (40.11 - 28.73) / 2) | ties; the minor pairing defect from iteration 2 is fixed |
| Reading B L218 | lost about Rs 34 Cr a year; Q2 change +0.2 to -2.2 (even spread, Rs 9.70-12.13 a quarter, Q2 lost Rs 7.60-10.03) or -11.4 (seasonal) | 38.8 / 4 = 9.70; 48.5 / 4 = 12.13 (presentation:L741-L742; R410, R411); 9.70 - 2.10 = 7.60; 12.13 - 2.10 = 10.03; 7.78 - 7.60 = +0.18; 7.78 - 10.03 = -2.25; 7.78 - 19.22 = -11.44 | ties |
| Separating observations L219, K17 L571, L781 | Q8 answer and Q2 FY25 other income (ND here); neither reading preferred | Q2 FY25 is not in either document: confirmed (results columns L185 start at Q2 FY26; deck history is annual only, L739) | correct ND handling |
| Bridge L257-L259, check L265 | Reading A split rows labelled; total row carries Reading B split | as above; -15.63 / 40.09 = -39.0%; -3.59 / 40.09 = -9.0% | ties |
| Mandatory Q1 L270 | operating rows +7.8 under both readings; A: +2.5 to +4.2, spike -15.6 to -13.9; B: +0.2 to -2.2 or -11.4, recurring base flat to down | as above | consistent |
| Mandatory Q2 L271 | A: Rs 14-21 Cr a year recurring gone, rest of the Rs 34 Cr line change one-off; B: about Rs 34 Cr a year gone | as above | consistent |
| E-a L444; 8A-W L467; Key Notes L581; Flag 5 L628; YAML flag L792; analyst note L804 | both readings named, each with its own loss and change; no Reading B level paired with Reading A gain | as above | consistent |
| Q8 L495 | A: Rs 14-21 Cr a year, +2.5 to +4.2; B: Rs 34 Cr a year, "about -2 (even spread) to -11.4" | even-spread range is +0.2 to -2.2; Q8 rounds it to "about -2" (this wording came from my own iteration-2 replacement text) | STYLE only, new note A5-S6 |
| Brief L646, L675; forward map L691 | two readings stated in plain words with Rs 14-21 Cr and Rs 34 Cr a year | as above | consistent |

A5-C1: **CLOSED.**

### S2. STYLE items applied in loop 2
- A5-S3: CLOSED. Step 8 L458 now carries the body verdict line: "Protocol verdict: PROCEED WITH FLAGS". This matches the YAML L727.
- A5-S4: CLOSED. Flag 8 L631 now ties the 81% to the Rs 740 Cr programme: 740 / 911.7 = 81.2% (presentation:L278; R268).

### S3. New-error scan
- No new FACTUAL, MISSING or CONTRADICTION finding.
- Every new number ties to the extract, as shown in the S1 table.
- The other changed passages agree with each other and with Step 2 diagnostic 6: Step 2 table L202, 8A-W L467, K17 and the YAML question L746.
- New STYLE note A5-S6. Q8 (L495) writes Reading B's even-spread change as "about -2". Diagnostic 6, mandatory Q1 and Flag 5 give the full range, +0.2 to -2.2. This is cosmetic, it changes no conclusion, and it repeats my own iteration-2 replacement text.

### S4. Gates on the revised file
- Brief gate: PASS. Narrative L643-L659 is 17 lines (limit 10-20). Sector L661-L666, business model L668-L676, competition L678-L684 and forward map L686-L698 are all present. The forward map has 8 dated rows, each with a bull and a bear fork.
- Coverage: PASS, unchanged. Loop 2 added no new row IDs. K17 points outside the corpus and is marked ND. orphan_rows: none. missing_from_ledger: none.

### S5. Final verdict
**COMPLETE with style notes.**
- Every FACTUAL, MISSING and CONTRADICTION finding is closed. That is 5 FACTUAL (A5-F1 to F5), 2 MISSING (A5-M1, M2) and 1 CONTRADICTION (A5-C1).
- STYLE notes still open, logged only and never re-run:
  - A5-S1 (partial): 0.01 drift on 158.19, -98.64 and 663.85/652.60.
  - A5-S5: wording in the A2 ledger.
  - A5-S6: the Q8 rounding.
- The review may proceed to the Notion save gate. The save still needs the operator's approval of the printed payload.

```yaml
stage: A5-adversary
company: "PITTIENG"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
re_audit: true
iteration: 3
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []  # iteration-1 counters (A5-M1 other income, A5-F5 castings) grafted and re-checked; A5-C1 two-reading fix re-checked
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "A5-S1 (partial): 0.01 drift remains on 158.19, -98.64, 663.85/652.60"
    - "A5-S5 (A2): ledger L5 '13 line items' wording; 3 of 35 zero-standing tags sit on the vesting schedule"
    - "A5-S6 (new): Q8 L495 rounds Reading B's even-spread change to 'about -2'; the full range elsewhere is +0.2 to -2.2 (wording from A5's own iteration-2 replacement text)"
closed_findings: [A5-F1, A5-F2, A5-F3, A5-F4, A5-F5, A5-M1, A5-M2, A5-C1, A5-S2, A5-S3, A5-S4]
loop_back_to: ""
gap: ""
style_notes:
  - "A5-S1 partial rounding drift (0.01)"
  - "A5-S5 A2 zero-standing description"
  - "A5-S6 Q8 Reading B range rounded to 'about -2'"
analyst_note: "Iteration 3, loop 2, the last permitted. A5-C1 is closed. Other income now carries two labelled readings everywhere it appears, and every figure re-derives from the A1 fulltexts. Reading A (Q2 FY26 item one-off): Rs 3.6-5.3 Cr a quarter lost, Q2 recurring pre-tax change +2.5 to +4.2. Reading B (item recurs yearly): about Rs 34 Cr a year lost, change +0.2 to -2.2, or -11.4 if seasonal. The Q8 answer and Q2 FY25 other income separate them; Q2 FY25 is outside this corpus and correctly marked ND (K17). Grep confirms no residual pairing of one reading's level with the other's gain. STYLE S3 and S4 are applied. No new non-STYLE error was found in the changed passages. Remaining notes are cosmetic: 0.01 rounding drift, A2 ledger wording and a rounded range in Q8 that came from A5's own replacement text. Across three passes A5 raised 8 non-STYLE findings and all 8 closed. The brief gate and coverage passed at every pass."
```
