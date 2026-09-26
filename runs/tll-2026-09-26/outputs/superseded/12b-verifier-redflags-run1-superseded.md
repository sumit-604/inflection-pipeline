# Verifier B: Communication Red Flags. TLL (Trident Lifeline Ltd), run 2026-09-26

Mode: NO-CONCALL. TLL files no earnings-call transcripts. This audit reads the company's own communication instead: four investor decks (13-Nov-2025, 20-Jan-2026, 09-May-2026, 03-Aug-2026), the FY26 and FY25 annual reports (Chairman's message, MD&A, Board's Report, Note 22, related-party note), four results sets (H1FY26 original and rectified, FY26 audited, Q1FY27 reviewed), and Reg 30 filings. The 2022 prospectus signature pages were read to settle one open question. Peer transcripts were spot-checked against B06 citations.

Order of work: independent read first, then comparison with B05 and B06. No other verifier output was read.

Model: claude-opus-5-5.

All amounts are Rs lakh unless marked Cr. Line numbers refer to the page-marked .txt beside each source PDF.

---

## 1. Independent red-flag list (graded before scoring)

### CRITICAL

**R1. The statutory auditor's former partner is now CFO and Executive Director. The link is not disclosed.**
- The 2022 IPO restated financials are signed "For, A Bafna & Associates ... CA Ashish Bafna ... Partner ... M. No. 106525", dated 29-Jul-2022 (prospectus p220, lines 18686-18713; also lines 18829-18841).
- The CFO and WTD, Mayurkumar Gajera, resigned w.e.f. 16-May-2025. The CS resigned w.e.f. 30-May-2025. Ashish Anandsingh Bafna became CFO on 17-Jul-2025 (AR FY25 p19, lines 1704-1707).
- He became Additional Executive Director on 01-Sep-2025. The Reg 30 profile says "Fellow member of ICAI ... more than two decades of experience". It does not mention his partnership in the company's statutory audit firm (Reg 30 01-Sep-2025, Annexure-A, lines 96-111). The AGM notice profile gives the same text (AR FY25 lines 13744-13755).
- A Bafna & Associates (FRN 121901W) still audits TLL. Partner Meet Prakashkumar Jain signs the FY26 audit (20260507 results, line 227) and the Q1FY27 review (20260729, line 92).
- That audit covers the FY26 cash-flow reclassification (R2) and the "Claim Income" line (R7).
- **Why CRITICAL:** auditor independence underpins every accounting-quality flag in this run. Whether he left the firm before joining, and when, is NOT FOUND in the corpus. That separating observation is for the operator.
- **Pipeline:** B05 and B06 do not mention it. B08 raises the same-surname overlap as "UNRESOLVED (NOT FOUND either way)" (08-promoter.md line 459). The prospectus in the corpus resolves it. MISSED by B05/B06.

**R2. Bank working-capital borrowings sit inside operating cash flow. The decks restate FY25 CFO without a note.**
- The Nov-2025 and Jan-2026 decks show FY25 standalone CFO at -349.31 and CFF at 747.12 (Nov deck p31, line 676; Jan deck p31, line 669).
- The May-2026 deck shows FY25 CFO at +197.07 and CFF at 200.73. No note explains the change (May deck p30, lines 644, 650).
- The FY26 audited cash-flow statement puts "Changes in Working Capital Facilities" inside operating activities: 920.49 in FY26 and 545.38 in FY25 (20260507 results p8, line 383).
- On the prior basis, FY26 standalone CFO of 793.22 is about -127.27.
- **Why CRITICAL:** cash conversion is a Pillar 2 input.
- **Pipeline:** B05 carries the B02/B03 finding and uses it to hold grade C. B05 calls it "not a deck matter", but the decks themselves show the restatement. CAUGHT.

### MAJOR

**R3. Total income is presented as "Revenue from Operations", and EBITDA includes other income. This recurs across three decks and the statutory Board's Report.**
- **Nov-2025 deck p29:** "Revenue from Operations in H1FY26 stood at Rs 4,790.17 lakh". The results show sales of 4,625.86 plus other income 164.32 (20251114 rectified results, lines 119-121).
- **Jan-2026 deck p29:** "Revenue from Operations in Q3FY26 stood at Rs 2,456.30 lakh", on the same total-income basis.
- **May-2026 deck p28:** "Revenue from Operations stood at Rs 10,607.05 lakhs". Audited revenue from operations is 10,189.95 and other income is 417.10 (20260507 p7, lines 316-318).
- **AR FY26 Board's Report:** "revenue from operations of Rs 10607.05 Lacs and EBITDA of Rs 2850.1 Lacs" (lines 1609-1614).
- The May deck says "EBITDA margins remained stable at 27%". The company's own Aug-2026 deck shows operating EBITDA margin falling from 25.8% to 23.9%, or -187 bps (Aug deck p33, line 1008).
- Consolidated EBITDA is stated two ways: 3,737.93 incl. other income in the Board's Report (line 1543) and 28.1 Cr in the MD&A.
- **Pipeline:** B05 found the May deck instance only and graded it "MINOR-to-MODERATE". B05 says it was "silently corrected" later, but the Board's Report repeats it. B05 missed the EBITDA and margin effect. PARTIALLY CAUGHT.

**R4. Promoter-interest LLPs are customers, debtors and borrowers. No investor narrative names this.**
- **Standalone sales:** Tench Life Sciences LLP 722.72 and Talon Healthcare LLP 848.91, a total of 1,571.63. That is 15.4% of revenue from operations of 10,189.95 (AR FY26 lines 7971-7981). FY25 sales were 1,155.79.
- **Receivables outstanding:** Tench 483.14 and Talon 402.21, a total of 885.35 (lines 8193-8212).
- **Loans outstanding:** Talon 149.12, Tench 217.38, Trident Texofab (a promoter textile company) 326.48, up from 40.09 in FY25 (lines 8304-8374).
- The MD&A says domestic revenue rose from 30% to 49% and credits "widening sales and marketing reach" (AR FY26 p27, lines 1260-1272). No deck or MD&A mentions the LLP sales.
- **Pipeline:** B05 2D flags only the LLP guarantees as missing from the decks. B02 and B08 hold the RPT numbers. PARTIALLY CAUGHT.

**R5. The interim figures do not reconcile, and Q4 depreciation is near zero.**
- Q4FY26 standalone D&A was 4.15, against 71.23 in Q3 (Jan deck p27, line 532) and 69.81 in Q1FY27 (20260729 results p3, line 124).
- H2 D&A was 75.38 against 110.55 in H1, while tangible assets rose from 799.58 to 1,826.55 (20260507 p6, line 276; p7, line 328).
- The May deck calls H2 PAT an "all-time high ... up 46%" (May deck p28).
- The Jan deck gives 9MFY26 PBT as 1,667.60. H1 (1,110.46, Nov deck p28) plus Q3 (592.39) is 1,702.85, a gap of 35.25. Q3 checks against the audited H2 less the Q4 column, so the 9M line is the one in error.
- The Jan deck gives 9MFY25 PAT as 916.14. H1FY25 plus Q3FY25 from the same decks is 943.19.
- **Pipeline:** B05's promise table (2A, row 3) cites the 9M figures without testing them. MISSED.

**R6. The consolidation basis is unclear, and it carries the consolidated margin story.**
- FY26 results note 8: "changed the Method of Consolidation ... from Proportionate Method to Equity Method as per AS-21 ... do not have material impact" (20260507 p16, lines 861-864).
- The Q1FY27 note still reads "consolidating above-mentioned portion of Assets and Liabilities" of the subsidiaries (20260729 p8, lines 366-369).
- The Q1FY27 consolidated review report cites "Indian Accounting Standard 34", but the company says it is exempt from Ind AS (20260729 p5, line 228; p8, line 374).
- Consolidated employee cost fell from 1,208.84 to 1,078.35 (-10.8%). Other expenses fell from 1,446.27 to 1,367.11 (-5.5%). Revenue rose 48.4% (20260507 p14, lines 701-714).
- The Chairman credits "operating leverage" for the 470 bps margin gain (AR FY26 p17). The MD&A itself shows gross margin down 690 bps.
- **Pipeline:** MISSED.

**R7. An unexplained "Claim Income" line props up consolidated PBT, and the narrative never names it.**
- Consolidated Note 22 shows Claim Income of 541.05 in FY26 and 522.17 in FY25 (AR FY26 lines 12437-12439). That is 19.9% of FY26 and 38.4% of FY25 consolidated PBT (2,719.29 and 1,361.49).
- The MD&A says "Profit before tax doubled to Rs 27.2 crore" (AR FY26 p27) without naming it.
- **Pipeline:** B05 MISSED it. B02 caught the note-level disclosure gap.

**R8. The registration thesis does not match where FY26 revenue came from.**
- The Chairman calls the registration pipeline "our clearest indicator of future revenue". Registrations by region: Africa 64%, Asia 21%, LatAm 14% (AR FY26 p17, lines 777-792).
- FY26 exports by region: Asia 57%, Africa 25%, South America 17%. Domestic sales, which need no export registration, drove growth from 30% to 49% (AR FY26 p27).
- Registered products rose by 30 in six months, from 1,061 (Sep-2025) to 1,091 (Mar-2026) (Nov deck p5; May deck p5).
- **Pipeline:** B05 1C notes the domestic shift and says the slide looks templated. It does not test the shift against the registration thesis. PARTIALLY CAUGHT.

**R9. The "stable product mix" claim contradicts the company's own numbers.**
- The Nov-2025 deck says toothpaste, mouthwash and other ointments were "36% of the revenue" (p15, lines 275-279).
- The May-2026 deck says tablets are 67%, capsules 30%, and each other category 1%. It still says "the product mix has remained fairly-stable" (p15, lines 273-288).
- The AR FY26 MD&A says the same: "stayed broadly stable" (lines 1288-1296).
- Consolidated capsules went from 6.8 to 30.6 Cr (+350%). Others went from 49.0 to 30.1 Cr (Aug deck p30).
- **Pipeline:** MISSED.

**R10. The promoter's spouse resigned for a "personal reason", then reappeared as COO.**
- On 01-Sep-2025 the board recommended Maniya Hardik Desai for reappointment (Reg 30 01-Sep-2025, line 36).
- She resigned on 21-Nov-2025, citing a "personal reason" (Reg 30 21-Nov-2025, lines 60-72 and 156).
- She appears as "Chief Operating Officer" in the Aug-2026 deck (p21, line 521) and the AR FY26 (p21, lines 992-999). No senior-management Reg 30 filing for this appears in the corpus.
- FY26 pay was 18.00, up from 9.78 (AR RPT note, lines 8035-8039).
- **Pipeline:** B05 MISSED it. B08 reads her exit as reduced family presence on the board.

**R11. "Triple consolidated business in three years" and the subsidiary peak revenues appear only in the deck.**
- Source: Aug-2026 deck p5 and p11-15. None of this is in the AR outlook filed weeks later (AR FY26 p28).
- **Pipeline:** CAUGHT (B05 1C, 2D, 4D).

**R12. The IPO registration allocation stays largely unspent.**
- Rs 51,87,506 of Rs 5,13,66,000 was used by Jun-2025 (Statement of Deviation, line 99). The figure was 75.81 by 31-Mar-2026 (AR FY26 lines 1677-1681).
- Meanwhile every deck claims a "substantial amount of capital outlay for product registrations each year".
- **Pipeline:** CAUGHT (B05 2A, 4A). B05 does not cite the Mar-2026 update.

### MINOR

| # | Item | Anchor | Pipeline |
|---|---|---|---|
| R13 | "Intrinsic value of registrations about Rs 80 Cr". "3,625 products in portfolio" counts applications; 1,091 are registered | Aug deck p17-18; May deck p14; AR FY26 SWOT | PARTIALLY (B05 has the Rs 80 Cr claim) |
| R14 | Lorem ipsum placeholder text in a filed Reg 30 deck | Aug deck p12, p14 | CAUGHT |
| R15 | Lead export market changes from South America to Asia with no explanation | Nov/Jan deck p18 vs May deck p18 | CAUGHT (B05 3D, as fact) |
| R16 | FY26 standalone EPS is stated three ways: 15.50, 15.37, 15.73 | 20260507 results line 347; AR Board's Report line 1601; MD&A line 1259 | MISSED |
| R17 | The KPI page disagrees with the ratio table: ROE 22.2% vs 0.31, ROCE 17.5% vs 0.21, net D/E 0.7 vs D/E 1.24 | AR FY26 lines 848, 908 vs 1336-1354 | MISSED |
| R18 | The FY25 Chairman's Vorinostat/NIPER promise gets no FY26 status update | AR FY25 lines 628-649; AR FY26 line 289 | MISSED by B05 (B07 tracks it) |
| R19 | Q1FY27 revenue fell against Q4: standalone 2,684.23 vs 3,197.01 (-16%), consolidated 3,371.8 vs 4,995.34 (-32%). Q4 stock-in-trade purchases spiked to 718.42. The deck shows YoY only | 20260729 lines 112, 119, 295 | MISSED |
| R20 | BSE flagged the same trade-payable bifurcation defect in H1FY25 and H1FY26 | 20241220 lines 12-19; 20251114 lines 10-18 | PARTIALLY (B05 grades the refilings Positive) |

**Totals:** 20 independent items. 12 are material (2 CRITICAL, 10 MAJOR) and 8 are MINOR.

---

## 2. Comparison table

| Item | Severity | Verdict vs B05/B06 |
|---|---|---|
| R1 Auditor ex-partner as CFO/ED | CRITICAL | MISSED (B08 left it unresolved) |
| R2 CFO reclassification and deck restatement | CRITICAL | CAUGHT |
| R3 Total income as revenue; EBITDA incl. other income | MAJOR | PARTIALLY CAUGHT |
| R4 Promoter-LLP sales, receivables, loans absent from narrative | MAJOR | PARTIALLY CAUGHT |
| R5 Q4 D&A 4.15; 9M does not reconcile | MAJOR | MISSED |
| R6 Consolidation basis and absolute cost fall | MAJOR | MISSED |
| R7 Claim Income unnamed in narrative | MAJOR | MISSED (B02 had the note gap) |
| R8 Registration thesis vs revenue source | MAJOR | PARTIALLY CAUGHT |
| R9 "Stable" product mix contradiction | MAJOR | MISSED |
| R10 Spouse resigns, returns as COO | MAJOR | MISSED |
| R11 Triple-in-3 only in deck | MAJOR | CAUGHT |
| R12 IPO registration underspend | MAJOR | CAUGHT |
| R13-R20 | MINOR | 2 CAUGHT, 2 PARTIAL, 4 MISSED |

**Pipeline flags I did not raise, assessed against the sources:**

| Pipeline flag | Verdict | Note |
|---|---|---|
| B05: revenue mislabel "silently corrected" later | OVERSTATED | The AR FY26 Board's Report repeats the Rs 10,607.05 "revenue from operations" (lines 1609-1614) |
| B05 4C: filing integrity Positive | OVERSTATED | No figure changed, but BSE flagged the same defect twice |
| B05 2A row 2: "consolidated" H1FY26 margin compression | OVERSTATED (wrong basis) | The Nov deck figures are standalone |
| B05: goodwill 10.6x, Section 197 excess, LLP guarantees (carried) | SUPPORTED | Goodwill 52.37 to 555.15 (20260507 line 665); Rs 6.37 lakh excess (AR FY26 line 14694) |
| B05 1C: 300-400/yr describes applications, not approvals | SUPPORTED | Applications 3,445 to 3,625 in six months, about 360 per year |
| B06 Q1: debtor days contradicted by CAPLIPOINT | SUPPORTED | 117/118 days (Nov-2025 line 469); 121 days (Feb-2026 line 466) verified |
| B06 Q2: injectable ramp contradicted | SUPPORTED, misdated | The 65-70% over 4-5 years quote is from INNOVACAP Nov-2025, lines 712-714, not Aug-2026. TLL states capacity on a two-shift basis; B06 does not compare the basis |
| B06 Q2: SENORES scaled down sterile injectables | SUPPORTED | SENORES Aug-2026, lines 755-759 |

No pipeline flag was found NOT SUPPORTED. No signal was invented.

---

## 3. Promise-delivery spot checks (B05 Section 2A)

| # | Promise (source) | Earlier doc contains it? | Later outcome as B05 states? | Result |
|---|---|---|---|---|
| 1 | H1FY26 deck: "outlook ... strong ... grow at both standalone and consolidated levels" | Yes, Nov deck p29, lines 597-600 | Yes. FY26 revenue from ops up 50.3% standalone and 48.4% consolidated (20260507 lines 316, 701). B05's "consolidated margin" wording is wrong; the deck is standalone | CONFIRMED (direction) |
| 2 | Q3FY26 deck: "outlook for the remaining year & coming year remains strong" | Yes, Jan deck p29, lines 589-592 | Yes, FY26 closed with growth. B05's 9M figures are unreconciled (R5) | CONFIRMED |
| 3 | Statement of Deviation: product-registration allocation | Yes, line 99: 51,87,506 of 5,13,66,000 | Yes, underdelivered. Mar-2026 figure 75.81 (AR FY26 line 1680) | CONFIRMED |
| 4 | FY25 AR outlook: "well-positioned to harness emerging opportunities" | Yes, AR FY25 lines 1184-1199 | Directional delivery, as B05 says | CONFIRMED |
| 5 | Aug-2026 deck: Parenterals revenue from FY27 | Yes, Aug deck p13, line 294 | Unresolved at run date; Q1FY27 has no subsidiary revenue line | CONFIRMED as unresolved |

**Result:** checked 5, confirmed 5, wrong 0.

**Gap in the tracker:** B05's promise table omits the FY25 Chairman's Vorinostat/NIPER commitment (R18). B05 1C says "No trigger visibly DROPPED", but it searched only across the decks.

---

## 4. Credibility grade

B05 holds grade C, the no-concall default. I would grade lower. C survives here only because the mode sets C as the default.

Five items point below C:
- The auditor-to-CFO move is undisclosed (R1).
- The income mislabel repeats in the statutory Board's Report (R3).
- The cash-flow restatement is silent (R2).
- The interim figures do not reconcile (R5).
- The "stable mix" claim is contradicted (R9).

Two readings, and what separates them:
- **Reading A:** a small SME finance function with weak drafting, and Mr Bafna left the audit firm before joining TLL.
- **Reading B:** presentation choices lift reported cash and margins under an auditor with a personal link to the CFO.
- **The separating observation:** the date he ceased to be a partner of A Bafna & Associates, and whether the firm is rotated at the FY26 AGM. Both are NOT FOUND in the corpus.

---

## 5. Score

- Material items found: 12 (2 CRITICAL, 10 MAJOR).
- Caught by B05/B06: 6. That is 3 CAUGHT and 3 PARTIALLY CAUGHT; a partial catch counts as caught because the pipeline had the item, only under-weighted.
- acceptance_rate: 6 of 12 = 50%.
- Counting full catches only gives 3 of 12 = 25%.
- The denominator is 12, which is 4 or more, so the rate is valid. It is below 60%.

```yaml
stage: B12b
company: "TLL"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: complete
no_concall_mode: true
independent_flags_found: 20
caught: 5
partially_caught: 5
missed:
  - {severity: "CRITICAL", item: "Statutory auditor's former partner is now CFO and Executive Director; firm still audits; link undisclosed in Reg 30 profile and AGM notice", anchor: "Prospectus 2022 p220 lines 18686-18713 (CA Ashish Bafna, Partner, M.No.106525, A Bafna & Associates); AR FY25 p19 lines 1704-1707 (CFO from 17-Jul-2025); Reg 30 01-Sep-2025 Annexure-A lines 96-111; FY26 audit report signed by A Bafna & Associates (20260507 results line 227)"}
  - {severity: "MAJOR", item: "Q4FY26 standalone D&A 4.15 lakh vs Q3 71.23 and Q1FY27 69.81; Jan-2026 deck 9MFY26 PBT 1,667.60 does not equal H1 1,110.46 + Q3 592.39 (gap 35.25)", anchor: "Q1FY27 results p3 line 124 (PY Q4 D&A 4.15); Jan-2026 deck p27-28 lines 532, 565; Nov-2025 deck p28 line 570; FY26 results p7 line 328"}
  - {severity: "MAJOR", item: "Consolidation basis confusion: FY26 note 8 says method changed from proportionate to equity method with no material impact; Q1FY27 note still consolidates a 'portion' of subsidiary assets; Q1FY27 review cites Ind AS 34 on an Indian GAAP filer; consolidated employee cost -10.8% and other expenses -5.5% at +48.4% revenue carry the Chairman's 470 bps margin claim", anchor: "20260507 results p16 lines 861-864; 20260729 results p8 lines 366-369, p5 line 228; FY26 results p14 lines 701-714; AR FY26 p17 lines 756-764"}
  - {severity: "MAJOR", item: "Consolidated Claim Income 541.05 lakh FY26 and 522.17 lakh FY25 (19.9% and 38.4% of consolidated PBT) never named in Chairman's message, MD&A or any deck that cites PBT doubling", anchor: "AR FY26 Note 22 consolidated lines 12437-12439; AR FY26 MD&A p27 line 1292"}
  - {severity: "MAJOR", item: "Product mix called 'broadly stable' while toothpaste/mouthwash/ointments fell from 36% of revenue to about 1% and capsules rose 6.8 to 30.6 Cr", anchor: "Nov-2025 deck p15 lines 275-285; May-2026 deck p15 lines 273-288; AR FY26 MD&A p27 lines 1288-1296; Aug-2026 deck p30 lines 818-853"}
  - {severity: "MAJOR", item: "Maniya Hardik Desai put up for reappointment 01-Sep-2025, resigned 21-Nov-2025 for 'personal reason', then shown as Chief Operating Officer with no senior-management Reg 30 filing in corpus; FY26 pay 18.00 lakh vs 9.78", anchor: "Reg 30 01-Sep-2025 line 36; Reg 30 21-Nov-2025 lines 60-72, 156; Aug-2026 deck p21 line 521; AR FY26 p21 lines 992-999; AR FY26 RPT lines 8035-8039"}
  - {severity: "MINOR", item: "FY26 standalone EPS stated three ways: 15.50, 15.37, 15.73", anchor: "20260507 results p7 line 347; AR FY26 Board's Report line 1601; AR FY26 MD&A p27 line 1259"}
  - {severity: "MINOR", item: "AR KPI page and ratio table disagree: ROE 22.2% vs 0.31, ROCE 17.5% vs 0.21, net D/E 0.7 vs D/E 1.24", anchor: "AR FY26 p18-19 lines 848, 908; AR FY26 p28 lines 1336, 1340, 1354"}
  - {severity: "MINOR", item: "FY25 AR Chairman's Vorinostat/NIPER promise gets no status update in FY26 AR or decks", anchor: "AR FY25 p13 lines 628-649; Reg 30 05-Mar-2025; AR FY26 line 289 (timeline mention only)"}
  - {severity: "MINOR", item: "Q1FY27 sequential fall not mentioned: standalone revenue 2,684.23 vs Q4 3,197.01 (-16%), consolidated 3,371.8 vs 4,995.34 (-32%); Q4 stock-in-trade purchases 718.42 spike", anchor: "20260729 results p3 lines 112, 119; p7 line 295; Aug-2026 deck p33-35 (YoY only)"}
pipeline_flags_not_supported:
  - {flag: "B05 1B/4D: standalone revenue mislabel 'silently corrected' in later documents", verdict: "OVERSTATED", anchor: "AR FY26 Board's Report lines 1609-1614 repeats 'revenue from operations of 10607.05 Lacs'"}
  - {flag: "B05 4C: filing integrity (refilings) Positive", verdict: "OVERSTATED", anchor: "BSE flagged the same trade-payable bifurcation defect in H1FY25 and H1FY26 (20241220 line 12-19; 20251114 lines 10-18)"}
  - {flag: "B05 2A row 2: consolidated EBITDA margin compressed in H1FY26", verdict: "OVERSTATED", anchor: "Nov-2025 deck p27-28 is standalone ('Note - Standalone Financials')"}
  - {flag: "B06 Part 3: INNOVACAP 65-70% utilisation ceiling attributed to Aug-2026 call", verdict: "SUPPORTED, misdated", anchor: "INNOVACAP-Concall_Nov_2025 lines 712-714; Aug-2026 line 1022 repeats 65-70% only"}
promise_delivery_spot_checks: {checked: 5, confirmed: 5, wrong: 0}
credibility_grade_concur: "lower: C holds only as the no-concall default; an undisclosed auditor-to-CFO move plus repeated income mislabelling and a silent CFO reclassification argue below C"
findings: "see block file B12b.yaml: 23 rows (2 CRITICAL, 10 MAJOR, 11 MINOR incl. 3 pipeline-accuracy rows)"
critical_count: 2
major_count: 10
minor_count: 11
material_found: 12
material_caught: 6
acceptance_rate: 50
coverage_basis: "12 material (2 CRITICAL, 10 MAJOR) of 20 independent items; 6 of 12 caught by B05/B06 (3 CAUGHT, 3 PARTIALLY CAUGHT, partial counted as caught); 6 MISSED incl. 1 CRITICAL. Counting full catches only gives 3 of 12 (25%). Plus 3 MINOR pipeline-accuracy rows. Sources read: 4 decks, FY26 and FY25 AR (Chairman, MD&A, Board's Report, notes 22 and RPT), 4 results sets, 6 Reg 30 filings, 2022 prospectus signature pages, 4 peer-transcript spot checks."
```
