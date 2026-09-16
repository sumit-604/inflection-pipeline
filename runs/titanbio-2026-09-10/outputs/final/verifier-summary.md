# VERIFIER SUMMARY — TITANBIO, phase 1, 2026-09-16

Run: runs/titanbio-2026-09-10. Scope: phase 1 verifiers A, B, D in full, and the
Gate 0 and Emerging Moat portion of C. Verifier C's valuation, expectation ledger and
business understanding narrative sections were NOT RUN in phase 1 and are deferred to
phase 3.

## Phase 1 confidence delta

| Component | Score | Verifier | Acceptance basis |
|---|---|---|---|
| Numerical acceptance | 95.2 | B12a (claude-haiku-4-5) | 42 material numbers checked of 87 counted (48.3 percent coverage), 40 clean, 0 CRITICAL, 2 MAJOR, 0 false positives struck |
| Red flag coverage | 50 | B12b (claude-opus-5) | 29 independent flags found, 14 material (2 CRITICAL + 12 MAJOR), 3 fully caught upstream, 4 partially caught, 7 missed; partials counted as caught |
| Framework adherence | 85 | B12c (claude-opus-5) | 73 of 86 rules passed; gate0 41/46 (89 percent), emoat 32/40 (80 percent). Measured before the stage 1 and stage 7 corrections, which have since closed all 14 findings |
| Peer utilisation | 100 | B12d (claude-sonnet-5) | 11 of 11 peer transcripts confirmed SUBSTANTIVE, all claims addressed, no verdict discipline fails. B12d's own internal acceptance rate is 64, computed on citation accuracy, not on transcript utilisation |
| **Overall** | **50** | min of four | Below 60. Forced REWORK per prompts/00-orchestrator.md Section 5 |

Finding counts: 2 CRITICAL, 24 MAJOR, 15 MINOR across the four verifiers. Three
findings were disputed and resolved; full rows in
outputs/final/verifier-disagreement-log.md.

## CRITICAL

| Verifier | Location anchor | Finding | Status |
|---|---|---|---|
| B | B05 Sections 2A and 2D. AR FY2026 MD&A p.104; 30-May-2026 results standalone cash flow p.10; AR FY2024 p.105; AR FY2025 p.100 | MD&A cash flow Table A reports pre tax operating cash of Rs 3,896.91 lakh as CFO against audited net CFO of Rs 3,042.08 lakh, omits the Rs 854.83 lakh tax line and does not reconcile to its own closing cash of 147.77; the same unlabelled basis switch recurs for FY24 between AR FY2024 (2,114.63) and AR FY2025 (2,901.66). Cash conversion is a Section 1B pillar input | OPEN. In the named stage 5 rerun scope |
| C | C-01. B01 Block B, B4 and the working capital days table | Payable Days computed with revenue converted lakh to crore at 10 times instead of 100 times; all five rows 10 times too high. FY25's 121.68 days implies payables of Rs 52.15 cr against the report's own FY25 total current liabilities of Rs 17.74 cr. B4 5 to 3, core 81 to 79, classification GOOD plus to GOOD | CLOSED. Stage 1 re-ran, confirmed, re-emitted |

## MAJOR

| Verifier | Location anchor | Finding | Status |
|---|---|---|---|
| A | B04 bizmodel related party section; task addendum item 5. AR FY26 Note 41(a) | Related party purchases stated as Rs 3,683.61 lakh and 37.1 percent of cost of materials consumed; the audited note itemises Peptech 44.79 + Phoenix 2,574.32 + Stalwart 986.20 + Titan Animal 78.30 = Rs 3,877.14 lakh, which is 39.1 percent of Rs 9,916.35 lakh. source_fidelity true | CLOSED. Audited figure carried in every phase 1 final artifact with the Note 41(a) anchor; the stage figure it replaces is named |
| A | B01 gate0 and B02 notes, MD&A versus cash flow statement. AR FY26 p.116 standalone, p.162 consolidated; MD&A p.104 | MD&A states an investing outflow of Rs 3,441.49 lakh; the audited cash flow statement shows Rs 3,254.59 lakh on both bases. Gap Rs 186.90 lakh, source of the discrepancy NOT FOUND in the provided extracts. source_fidelity true | OPEN as a company disclosure inconsistency. The audited figure is the one the stages used and it is correct |
| B | B05 Sections 2D and 3D. AR FY2024 line 2920; AR FY2025 line 3967; AR FY2026 line 4044 | Stage 5 recorded the FY26 growth mechanism as unexplained; foreign exchange earned is disclosed in all three Directors' Reports (Rs 5,208.41 / 5,295.20 / 8,897.37 lakh), implying exports supplied about 72 percent of the FY26 revenue increment and moved from 31.4 to 43.2 percent of revenue | OPEN. In the stage 5 rerun scope |
| B | B05, AR FY2026 MD&A p.105 versus AR FY2025 MD&A p.100 | FY25 ROE restated to 10.70 percent by dividing FY25 PAT of 1,827.11 by FY26 closing equity of 17,084.15; AR FY2025 reported the same year at 12.59 percent. Inflates the published FY25 to FY26 ROE improvement from 3.47 points to 6.62 points. Not caught upstream | OPEN. In the stage 5 rerun scope |
| B | B05, AR FY2025 p.100 versus AR FY2024 p.106 and AR FY2026 p.105 | AR FY2025 blanks the Change percent column for all eight ratios in the one year every ratio deteriorated; the other two annual reports populate it. Not caught upstream | OPEN. In the stage 5 rerun scope |
| B | B05 Section 2A row 5. AR FY2026 MD&A p.103; AR FY2025 MD&A p.98 | Selling and distribution rose 3 percent to Rs 1,152.78 lakh on revenue up 31.8 percent with promotion, travel, advertisement and commission cut; FY25 did the inverse, up 27.74 percent on revenue down 5.7 percent. Stage 5 tested the marketing claim qualitatively when the numbers to test it sat in the prose it quoted | OPEN. In the stage 5 rerun scope |
| B | B05. AR FY2024 p.105; AR FY2025 p.100; AR FY2026 p.104 | Headcount does not reconcile across three annual reports: 449 (FY24), 424 with a claimed rise of 7.07 percent (FY25, implying a base of 396), 527 with a claimed rise of 15.09 percent (FY26, implying a base of 458). Headcount is the only scale proxy disclosed | OPEN. In the stage 5 rerun scope |
| B | B05 and B06. 30-May-2026 results p.7 versus 12-Feb-2026 results p.4 | Q4 FY26 revenue fell 13.6 percent quarter on quarter to Rs 4,883.35 lakh and PAT fell 16.7 percent to Rs 655.57 lakh, with the Q4 effective tax rate at 36.2 percent against 25.5 percent in Q3. No commentary in any filing. Relevant to whether the FY26 exit rate supports the FY27 base | OPEN. In the stage 5 rerun scope |
| B | B05 red flag table, B06 Section 2C and Claim 6. 30-May-2026 consolidated cash flow p.18 | Held that the consolidated investing outflow is Rs 3,441.49 lakh, that Rs 3,254.59 lakh does not appear, and recomputed the portfolio share as 73.1 percent against stage 5's 77 percent | RESOLVED AGAINST B12b. Verifier A's rerun found Rs 3,254.59 lakh on both bases at AR FY26 p.116 and p.162. The 77 percent share stands |
| B | B06 Section 2B, Section 2E, Claim 4, Part 4 | Held that exports of Rs 80.33 cr, 39 percent of revenue and 49 percent FY26 export growth were NOT FOUND in the AR sections read, and offered the Directors' Report foreign exchange earned series instead | RESOLVED AGAINST B12b. Verifier A's rerun verified the export figures clean at source. Both measures exist and differ: exported goods Rs 8,033.20 lakh in the AR note, foreign exchange earned Rs 8,897.37 lakh in the Directors' Report annexure |
| C | C-02. B01 Block F, M12 | Inherits the payable days unit error; the corrected working capital days series exceeds 45 days in all four years, so M12 falls 1 to 0 and the moat score 15 to 14, moat class MODERATE unchanged | CLOSED by the stage 1 correction |
| C | C-03. B01 block_b_trend and analyst_note | Asserts a working capital release the corrected series does not show; propagated into B07 category G2 | CLOSED by the stage 1 and stage 7 corrections |
| C | C-04. B07 Section 6D and combined_assessment | Returns the coined label "GOOD, NOT TRANSITIONING" instead of one of the eight matrix values; re-derived value is GOOD. The prompt names the eight labels but omits the mapping table | CLOSED. Stage 7 re-emitted combined_assessment as GOOD and named the missing mapping table as a gap |
| C | C-05. B07 block active_categories | G2 is graded Weak in the body and still listed in a Strong or Moderate only field, while B2, also Weak, is correctly excluded. No score effect at the time of the finding | CLOSED. G2 now scores 0 and has left the active list |
| D | B06 peer_coverage_map row, ADVENZYMES Feb-04-2026 | Row credits the call with EFSA approval timelines; the Feb-04-2026 transcript contains no EFSA content, which sits in the Aug-12-2026 transcript. Per call attribution error, peer still SUBSTANTIVE on other genuine content | OPEN. Citation date correction recorded |
| D | B06 peer_coverage_map row, ADVENZYMES May-12-2026 | Row credits the call with Nutrazyme and Wellfa disclosed revenue; neither name appears in the May-12-2026 transcript. Content is in the Nov-13-2025 transcript | OPEN. Citation date correction recorded |
| D | B06 peer_coverage_map row, FERMENTA Aug-17-2021 | Row credits the call with the formula priced input contract; no formula pricing language in that transcript. The wool grease formula quote is in the Nov-17-2021 transcript | OPEN. Citation date correction recorded |
| D | B06 peer_coverage_map row, FERMENTA Jun-01-2022 | Row credits the call with the key account margin trade off pattern; "key account" does not appear in that transcript. Content is in the Nov-17-2021 transcript | OPEN. Citation date correction recorded |
| D | B06 report Part 2A | "let's not get into the QoQ... some quarters here and there" cited to Mukund Kabra on the Feb-04-2026 call; the quote is verbatim in the Aug-12-2026 transcript. Underlying point independently supported elsewhere | OPEN. Citation date correction recorded |
| D | B06 report Part 1 Claim 4 | "still waiting from 2014" EFSA quote cited to the Feb-04-2026 call; it is verbatim in the Aug-12-2026 transcript | OPEN. Citation date correction recorded |
| D | B06 report Part 1 Claim 2, VIDHIING Jun-12-2024 | Naphthalene raw material substitution quote attributed to Mihir Manek; spoken by Mitesh Manek, CFO. Mihir Manek asks the preceding question. Call and content correct, speaker wrong | OPEN. Speaker correction recorded |
| D | B06 report Part 1 Claim 2, VIDHIING May-14-2026 | "inflationary trends and volatile freight markets" attributed to Bipin Manek; spoken by Mitesh Manek in the financial highlights section. Call correct, speaker wrong | OPEN. Speaker correction recorded |
| D | B06 report Part 2B, ADVENZYMES Nov-13-2025 | "we have not reduced a penny on our pricing" attributed to Mihir Manek; spoken by Mitesh Manek answering Lala Ram's question. Call correct, speaker wrong | OPEN. Speaker correction recorded |
| D | B06-peers.yaml, contradicted[1].quote_anchor, VIDHIING May-14-2026 | 18 month commissioning and the Rs 75 cr to 85 cr capex with Rs 125 cr to 150 cr expected revenue attributed to Mihir Manek as one statement; the commissioning answer came from Bipin Manek and Mitesh Manek in one exchange and the figures from Mihir Manek in a separate later exchange. Figures correct, two speakers merged | OPEN. Correction carried into the contradicted claims list in outputs/final/gate-recommendation.md |

## MINOR

| Verifier | Location anchor | Finding | Status |
|---|---|---|---|
| B | B05 flag 3, cautionary statement basis mislabel | Graded MEDIUM; identical boilerplate runs across all three annual reports, the MD&A labels its own tables by basis and standalone and consolidated revenue are the same number. Over called by one severity band, belongs at LOW | OPEN |
| B | B05 Section 2D and trigger 1, like for like growth | "~28.06 percent like for like ex freight" is a stage 2 derivation; no company filing quantifies the freight amount, yet the figure is carried to two decimals in the trigger table as if measured | OPEN |
| B | B05 trigger 3 and Section 2D, FVTPL portfolio return | Portfolio described as having an undisclosed return profile; AR FY2026 p.105 discloses return on investment of 3.64 percent (FY26) against 7.04 percent (FY25) and ROCE of 24.09 percent. The strongest evidence on the allocation, cited by neither report | OPEN |
| B | B05 Section 2D and trigger 4, Titan Media stake | Reg 30 dated 28-Feb-2025 raised voting rights in Titan Media Limited to 48.44 percent from 32.29 percent in five lines with no consideration, valuation or rationale, against a full Annexure-A for a Rs 10.62 lakh arbitration. Disclosure asymmetry not cited | OPEN |
| C | C-06. B01 M12 | Band reached via a median of four years test the rubric does not contain | CLOSED by the stage 1 correction |
| C | C-07. B01 M5 and M7 | "PEER DATA NEEDED" marker required by the Block F instruction not used; substance captured in input_gaps | CLOSED. Marker applied on re-emission |
| C | C-08. B01 Block A and data_years | Return blocks run on FY23 to FY26 while the block reports data_years 10; the exclusion of FY17 to FY20 from A1 and A2 is not tested or flagged. Not recomputable, the corpus holds no FY17 to FY22 balance sheet detail | CLOSED as a stated data note; the gap itself stands and is named |
| C | C-09. B07 optionality register scope | B2 qualification lock in omitted though inference only; two registered rows, FVTPL composition and the Peptech reconciliation, are verification items rather than forward advantages | CLOSED. Both rows moved to input_gaps, B2 added to the register |
| C | C-10. B07 block schema | data_years and fy_range emitted outside the prompt's block schema | CLOSED |
| C | C-11. B07 evidence_mix | Counts only scored active rows; the body anchors documented evidence in five categories | CLOSED. Recount restated at the 22 category level |
| C | C-12. B07 catalysts_12m | Two rows carry evidence_type "DOCUMENTED (pending)" for events that have not occurred; this field feeds Pillar 3 catalyst proximity at stage 11 and must not read as documented | CLOSED. Re-labelled |
| C | C-13. B07 Section 3 recount prose | Body sentence says "2 categories ... three categories" in one sentence; the emitted block states 3 correctly | CLOSED |
| C | C-14. B07 Section 2C | Fixed asset turnover 4.02 times standalone against B01 M3's 3.25 times consolidated for the same ratio; implied embedded growth 3.4 percent against 2.7 percent. Conclusion unaffected | CLOSED. Basis stated |
| D | B06 report Part 1 Claim 1 | "mixed... some flat" attributed jointly to Beni Rauka and Mukund Kabra on the Feb-04-2026 call; the line is solely Mukund Kabra's scripted opening remarks. Imprecise joint attribution | OPEN |
| D | Corpus: ADVENZYMES-Concall_Nov_2025_Transcript.txt and ADVENZYMES-Concall_Feb_2026_Transcript.txt | Claimed an identical Ravi Purohit, Nutrazyme and Wellfa Q&A block appears verbatim in both extracted files, suggesting a page duplication artifact | STRUCK on corpus evidence. The four ADVENZYMES PDFs carry four distinct md5 hashes, four call dates and four page counts (20, 24, 22, 23); the block appears 3 times in the Feb-2026 file and 0 times in the Nov-2025 file. B12d's misattribution findings above stand; only the duplication claim is struck |

## Withdrawn on rerun

| Verifier | Location anchor | Finding | Status |
|---|---|---|---|
| A (first pass) | B09 market sizing, India microbiology culture media TAM | Claimed USD 194.4 million at Rs 96 per dollar converts to Rs 18.66 crore against the stage's Rs 1,866 crore, graded MAJOR with source_fidelity true | WITHDRAWN. USD 194.4 million times 96 is Rs 1,866 crore; the verifier's own conversion carried a million versus crore slip, and its internal cross check carried the same slip. The orchestrator re-invoked Verifier A once with the severity semantics and coverage addendum; the rerun withdrew the finding, verified the market sizing conversions clean and raised two different MAJORs, both real |
