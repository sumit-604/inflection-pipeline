# Stage 0: input validation, EMUDHRA 2026-09-19

Orchestrator stage. Block: outputs/blocks/B00-inputs.yaml.

- Spear gate: OVERRIDE 2026-09-19 (companies/EMUDHRA.md). Four load-bearing facts carried to every stage.
- Sector cap row: Platform / SaaS / IT services (flag for phase-3 confirmation).
- Units: filings INR Million; screener INR Cr.
- Freshness verdict: **CORPUS GAPPED-FRESHNESS** (rating bulletin without its June-2026 ICRA rationale).
- Tooling: pypdf 6.14.2 and pdftotext present; every PDF opened and was extracted to page-marked .txt.
- Empty-folder confirmation: suppressed by the /step1 autonomy contract; standing answer "proceed with the gaps".

## Inventory
- prospectus: 0
- annual-report: 1
- results: 3
- rating: 3
- concalls: 3
- peer-concalls: 12
- announcements: 30
- shareholding: 2
- research: 0
- screening: 4
- presentation: 2
- other: 1

## Corpus manifest (document identity from page 1)

| path | issuer | type | period | folder match |
|---|---|---|---|---|
| inputs/announcements/20260202-4117a834.pdf | eMudhra | Reg 30 filing: Intimation under Regulation 30 of the Securities and Exchange Board of India (Listing | 20260202 | yes |
| inputs/announcements/20260202-43419e27.pdf | eMudhra | Reg 30 filing: Press Release on the unaudited financial results of the company for the quarter ended | 20260202 | yes |
| inputs/announcements/20260202-d761e5b6.pdf | eMudhra | Reg 30 filing: Additional update to the outcome of the Board Meeting held on February 02,2026 | 20260202 | yes |
| inputs/announcements/20260204-d507034d.pdf | eMudhra | Reg 30 filing: Disclosure under Regulation 30 of SEBI (Listing Obligations & Disclosure Requirements) | 20260204 | yes |
| inputs/announcements/20260209-3i-Infotech-Investor-Call-Transcript.pdf | eMudhra | Special investor call transcript, 3i Infotech allegations | 06-Feb-2026 | yes |
| inputs/announcements/20260209-8e37cf4b.pdf | eMudhra | Reg 30 filing: Press Release | 20260209 | yes |
| inputs/announcements/20260209-a7e3e2bf.pdf | eMudhra | Reg 30 filing: Postal Ballot notice | 20260209 | yes |
| inputs/announcements/20260212-944815c1.pdf | eMudhra | Reg 30 filing: Press Release | 20260212 | yes |
| inputs/announcements/20260216-c36e3206.pdf | eMudhra | Reg 30 filing: Press Release | 20260216 | yes |
| inputs/announcements/20260220-6892c79f.pdf | eMudhra | Reg 30 filing: Press Release | 20260220 | yes |
| inputs/announcements/20260223-01b04755.pdf | eMudhra | Reg 30 filing: Press Release | 20260223 | yes |
| inputs/announcements/20260226-9bdb4713.pdf | eMudhra | Reg 30 filing: Press Release | 20260226 | yes |
| inputs/announcements/20260226-f1c9958a.pdf | eMudhra | Reg 30 filing: Intimation under Regulation 30 read with Schedule III of the Securities and Exchange | 20260226 | yes |
| inputs/announcements/20260305-54f8cefb.pdf | eMudhra | Reg 30 filing: Press Release | 20260305 | yes |
| inputs/announcements/20260311-d29b888b.pdf | eMudhra | Reg 30 filing: Press Release | 20260311 | yes |
| inputs/announcements/20260318-43e41643.pdf | eMudhra | Reg 30 filing: Press Release | 20260318 | yes |
| inputs/announcements/20260325-9a426058.pdf | eMudhra | Reg 30 filing: Press Release | 20260325 | yes |
| inputs/announcements/20260410-e38f5fbe.pdf | eMudhra | Reg 30 filing: Increase in Volume | 20260410 | yes |
| inputs/announcements/20260417-42cf4e2a.pdf | eMudhra | Reg 30 filing: Revised Submission – Press Release | 20260417 | yes |
| inputs/announcements/20260417-8f60da77.pdf | eMudhra | Reg 30 filing: Press Release | 20260417 | yes |
| inputs/announcements/20260506-451e6012.pdf | eMudhra | Reg 30 filing: Press Release on the audited financial results of the company for the quarter and year ended | 20260506 | yes |
| inputs/announcements/20260506-4b40af1a.pdf | eMudhra | Reg 30 filing: Disclosure under Regulation 30 of Securities and Exchange Board of India (Listing Obligation | 20260506 | yes |
| inputs/announcements/20260506-b6f24b33.pdf | eMudhra | Reg 30 filing: Disclosure under Regulation 30 of Securities and Exchange Board of India (Listing Obligation | 20260506 | yes |
| inputs/announcements/20260629-17e01867.pdf | eMudhra | Reg 30 filing: Intimation under Regulation 30 read with Schedule III of the Securities and Exchange | 20260629 | yes |
| inputs/announcements/20260706-b78300f5.pdf | eMudhra | Reg 30 filing: Intimation under Regulation 30 read with Schedule III of the Securities and Exchange | 20260706 | yes |
| inputs/announcements/20260729-3678b793.pdf | eMudhra | Reg 30 filing: Press Release on the unaudited financial results of the company for the quarter ended June 30, 2026. | 20260729 | yes |
| inputs/announcements/20260818-7509d90d.pdf | eMudhra | Reg 30 filing: Disclosure under Regulation 30 of SEBI (Listing Obligations & Disclosure Requirements) | 20260818 | yes |
| inputs/announcements/20260828-e662e06d-f94a-4202-88ef-431bac624cdb.pdf | eMudhra | Reg 30 filing: Schedule of Analyst/ Institutional Investor Meeting | 20260828 | yes |
| inputs/announcements/20260913-8955c07b-c4c4-4086-b403-f13cce603cd0.pdf | eMudhra | Reg 30 filing: Press Release | 20260913 | yes |
| inputs/announcements/20260918-dafb9797-d359-46c4-842c-591a5b2df335.pdf | eMudhra | Reg 30 filing: Schedule of Analyst/ Institutional Investor Meeting | 20260918 | yes |
| inputs/annual-report/Annual_Report_2026.pdf | eMudhra | Annual Report FY2025-26 | FY26 | yes |
| inputs/concalls/Concall_Aug_2026_Transcript.pdf | eMudhra | Earnings call transcript | Q1FY27 | yes |
| inputs/concalls/Concall_Feb_2026_Q3FY26_Transcript.pdf | eMudhra | Earnings call transcript | Q3FY26 | yes |
| inputs/concalls/Concall_May_2026_Transcript.pdf | eMudhra | Earnings call transcript | Q4FY26 | yes |
| inputs/other/Annual_Report_2025.pdf | eMudhra | Annual Report FY2024-25 (not consumed) | FY25 | yes |
| inputs/peer-concalls/NEWGEN-Concall_Jan_2026_Transcript.pdf | Newgen Software | Peer call transcript | Q3FY26 | yes |
| inputs/peer-concalls/NEWGEN-Concall_Jul_2026_Transcript.pdf | Newgen Software | Peer call transcript | Q1FY27 | yes |
| inputs/peer-concalls/NEWGEN-Concall_May_2026_Transcript.pdf | Newgen Software | Peer call transcript | Q4FY26 | yes |
| inputs/peer-concalls/NEWGEN-Concall_Nov_2025_Transcript.pdf | Newgen Software | Peer call transcript | Q2FY26 | yes |
| inputs/peer-concalls/PROTEAN-Concall_Aug_2026_Transcript.pdf | Protean eGov | Peer call transcript | Q1FY27 | yes |
| inputs/peer-concalls/PROTEAN-Concall_Dec_2025_Transcript.pdf | Protean eGov | Peer call transcript | business update 22-Dec-2025 | yes |
| inputs/peer-concalls/PROTEAN-Concall_Feb_2026_Transcript.pdf | Protean eGov | Peer call transcript | Q3FY26 | yes |
| inputs/peer-concalls/PROTEAN-Concall_May_2026_Transcript.pdf | Protean eGov | Peer call transcript | Q4FY26 | yes |
| inputs/peer-concalls/QUICKHEAL-Concall_Aug_2025_Transcript.pdf | Quick Heal | Peer call transcript | Q1FY26 | yes |
| inputs/peer-concalls/QUICKHEAL-Concall_Feb_2025_Transcript.pdf | Quick Heal | Peer call transcript | Q3FY25 | yes |
| inputs/peer-concalls/QUICKHEAL-Concall_May_2026_Transcript.pdf | Quick Heal | Peer call transcript | Q4FY26 | yes |
| inputs/peer-concalls/QUICKHEAL-Concall_Oct_2025_Transcript.pdf | Quick Heal | Peer call transcript | Q2FY26 | yes |
| inputs/presentation/20260507_Investor_Presentation_Q4FY26.pdf | eMudhra | Investor presentation | Q4FY26 | yes |
| inputs/presentation/20260730_Investor_Presentation_Q1FY27.pdf | eMudhra | Investor presentation | Q1FY27 | yes |
| inputs/rating/20250602_ICRA_Rationale_Upgrade_A_Stable.pdf | ICRA | Rating rationale | 02-Jun-2025 | yes |
| inputs/rating/20250708_ICRA_Update_Material_Event.pdf | ICRA | Rating material-event update | 08-Jul-2025 | yes |
| inputs/rating/20260629_Credit_Rating_Intimation.pdf | eMudhra/ICRA | Rating letter, no rationale | 29-Jun-2026 | yes |
| inputs/results/FY26-Q3_Results_31Dec2025.pdf | eMudhra | Unaudited results SA+consol | Q3FY26 | yes |
| inputs/results/FY26_Audited_Results_31Mar2026.pdf | eMudhra | Audited results SA+consol | FY26 | yes |
| inputs/results/FY27-Q1_Results_30Jun2026.pdf | eMudhra | Unaudited results SA+consol | Q1FY27 | yes |

## Freshness pairs

- RESULTS to CONCALL: PASS. 
- RATING BULLETIN to RATIONALE: FAIL. ICRA rationale for eMudhra Limited, June 2026 surveillance (icra.in; not reachable by script, bot wall). Latest full rationale held is 02-Jun-2025 (inputs/rating/20250602_ICRA_Rationale_Upgrade_A_Stable.pdf) plus the 08-Jul-2025 material-event update.
- SEBI ORDER to ORDER TEXT: PASS. 
- AR to LATEST AUDITED ANNUAL RESULTS: PASS. 

## Input gaps

- FRESHNESS FAIL: ICRA June-2026 rating rationale absent; only the reaffirmation letter is held. Gate recommendation caps at PROCEED WITH CAVEATS. Operator: download from icra.in and push to inputs/rating/.
- collector_warning (verbatim): shareholding/ is empty: no source is automated yet. Push the latest quarterly shareholding pattern by hand; it closes the FII+DII UA qualifier and the promoter pledge trend. [REPAIRED at Step 1: BSE Reg 31 summaries Jun-2026 and Mar-2026 fetched; they show promoter 54.40% and no pledge but not the FII/DII split, which is on screener only.]
- collector_warning (verbatim): screener export sheets came out EMPTY (formulas with no cached values), so no CSV was written for them: screener:Profit & Loss, screener:Quarters, screener:Balance Sheet, screener:Cash Flow, screener:Customization, NEWGEN:Profit & Loss, NEWGEN:Quarters, NEWGEN:Balance Sheet, NEWGEN:Cash Flow, NEWGEN:Customization, QUICKHEAL:Profit & Loss, QUICKHEAL:Quarters, QUICKHEAL:Balance Sheet, QUICKHEAL:Cash Flow, QUICKHEAL:Customization, PROTEAN:Profit & Loss, PROTEAN:Quarters, PROTEAN:Balance Sheet, PROTEAN:Cash Flow, PROTEAN:Customization. Open Financials.xlsx once in Excel or LibreOffice, save it, then run --push-again. [Every Data_Sheet.csv is populated: FY19-FY26 annual P&L, balance sheet, cash flow and recent quarters. Gap is cosmetic.]
- collector_warning (verbatim): no results PDFs yet (screener has none): add later on github or locally + --push-again [REPAIRED: Q3FY26, FY26 audited, Q1FY27 fetched from BSE.]
- collector_warning (verbatim): no rating PDF yet: add later the same way [PARTLY REPAIRED: ICRA letter 29-Jun-2026 plus the 2025 rationale and material-event update; the 2026 rationale is the freshness gap above.]
- announcements: collector downloaded 4 of 126 BSE rows; Step 1 fetched 29 material Reg 30 filings by hand, removed 3 board-outcome copies byte-identical to results/ and 1 copy of the Q1FY27 transcript. Routine filings (trading window, investor-meet intimations, Reg 74(5), newspaper ads) skipped.
- concalls: collector filed the 06-Feb-2026 special investor call on the 3i Infotech allegations as a concall; moved to announcements/ (it is not an earnings call). Three earnings transcripts remain.
- annual-report: collector took FY25 and FY26 ARs; contract is 0-1, so FY25 moved to other/ (preserved, not consumed). Stage 3 backward depth relies on the FY26 AR comparatives and screener Data_Sheet.
- prospectus: NONE; not a gap (listed June 2022, >3y).
- research: NONE. No broker notes. No effect on anchored evidence.
- shareholding: FII/DII split not in the BSE summary text held; screener shows FII 3.92% + DII 10.55% = 14.47% at Jun-2026 (non-anchored). UA institutional-absence qualifier (<3%) is not met on either reading.
- peer-concalls: PROTEAN Dec-2025 file is a business-update call (NSDL Payments Bank stake), not an earnings call; QUICKHEAL has no Q3FY26 or Q1FY27 transcript on screener, so its set spans Feb-2025 to May-2026.
- EMPTY-FOLDER CONFIRMATION suppressed by /step1 autonomy contract: prospectus (not a gap) and research are empty; standing answer "proceed with the gaps"; run degrades per the DEGRADATION MAP.
