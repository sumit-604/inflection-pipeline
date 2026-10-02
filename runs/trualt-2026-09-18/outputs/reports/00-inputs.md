# Stage 0 — Input validation (TRUALT, 2026-09-18)

Orchestrator-run inventory. The YAML block below is the handoff; the corpus manifest lists every document with its identity read off page 1.

```yaml
stage: B00-inputs
company: TRUALT
run_date: '2026-09-18'
model: orchestrator
status: complete
spear_gate:
  form: OVERRIDE
  date: '2026-09-18'
  source: companies/TRUALT.md
  note: 'operator standing ruling 2026-09-05: Step-1 intake replaces the web spear'
  load_bearing_facts:
  - 'Utilisation and grain economics, guidance vs delivery: Q1FY27 claim 60% utilisation now, 80-85% target, grain
    ethanol margin compressed from Rs 15-16 to Rs 6-7 per litre, 44 cr litres FY27 OMC orders. Score the four concalls
    (Q2FY26 to Q1FY27) against what printed.'
  - 'Cash conversion and IPO money: FY26 CFO Rs -296 cr, inventory Rs 210 cr to Rs 528 cr, borrowings Rs 1,557 cr
    to Rs 1,652 cr in the year of a Rs 751 cr fresh issue (screener Data_Sheet). Trace the Rs 425 cr working-capital
    tranche through the three monitoring agency reports (inputs/announcements/20260210-*, 20260515-*, 20260803-*)
    and the FY26 AR notes.'
  - 'Promoter pledge and related parties: Jun-2026 SHP shows 2,22,95,674 of 6,04,98,650 promoter shares pledged
    (36.85%) (inputs/shareholding/TRUALT-SHP-June-2026.txt). Read prospectus and FY26 AR related-party notes for
    feedstock bought from Nirani-group sugar mills. Identify Onkar Agro Sugars & Energy Pvt Ltd, buyer of Unit 5
    (Badami) by Rs 171 cr slump sale (inputs/announcements/20260804-*).'
  - 'Governance churn: 28-Oct-2025 cessation citing a ''management decision''; company secretary appointments 09-Jan-2026
    and 03-Feb-2026; chairman change and director cessation 28-Jul-2026; NSE and BSE fines Rs 4.55 lakh each for
    board composition (25-Aug-2026); GST demand order 20-Aug-2026.'
company_memory: companies/TRUALT.md (Step-1 draft) + runs/trualt-2026-09-18/step1-business-brief.md (web-sourced).
  Memory to weigh, never anchored evidence.
text_route: 'Every inputs/ PDF has a page-marked .txt beside it ([page N] markers). Stages and verifiers read the
  .txt; the PDF stays the source of record and page numbers match. Image-only pages carry an [OCR: ...] marker.'
inventory:
  prospectus: 1
  annual-report: 1
  results: 3
  rating: 1
  concalls: 4
  peer-concalls: 12
  announcements: 35
  shareholding: 2
  research: 0
  screening: 4
  presentation: 2
  other: 0
input_gaps:
- 'collector_warning (verbatim): sector_cap_row_guess Pharma / CDMO is the collector default and is wrong; Step
  1 set Sugar / agri-commodity.'
- 'collector_warning (verbatim): peer RENUKA (Shree Renuka Sugars) collected but has held no concall since Jun-2022;
  replaced by TRIVENI, collected separately with screener_collect.py. RENUKA Data_Sheet removed.'
- 'collector_warning (verbatim): announcements: collector downloaded 5 of 102 BSE rows; Step 1 fetched the material
  Reg 30 filings by hand (41 files, 6 duplicates of other folders removed). Routine filings (trading window, Reg
  74(5), newspaper ads, SDD) skipped.'
- 'collector_warning (verbatim): results, rating, prospectus and shareholding were empty after the collector; Step
  1 filled them from BSE (results Q3FY26, Q4FY26, Q1FY27; Ind-Ra rating with full rationale), the NSE archive (final
  prospectus 01-Oct-2025) and the BSE XBRL SHP (Mar and Jun 2026, converted to text).'
- 'collector_warning (verbatim): Q4FY26 audited results PDF is a scan (16 of 20 pages image-only); the .txt beside
  it carries RapidOCR text marked per page. OCR also filled 4 image pages in each deck and 10 in the prospectus.'
- 'collector_warning (verbatim): concall filenames: collector names by month; BALRAMCHIN May_2026 is dated 30-Apr-2026
  and Jun_2026 is dated 22-May-2026 on page 1.'
- 'collector_warning (verbatim): screener export sheets came out EMPTY (formulas with no cached values), so no CSV
  was written for them: screener:Profit & Loss, screener:Quarters, screener:Balance Sheet, screener:Cash Flow, screener:Customization,
  GULPOLY:Profit & Loss, GULPOLY:Quarters, GULPOLY:Balance Sheet, GULPOLY:Cash Flow, GULPOLY:Customization, BALRAMCHIN:Profit
  & Loss, BALRAMCHIN:Quarters, BALRAMCHIN:Balance Sheet, BALRAMCHIN:Cash Flow, BALRAMCHIN:Customization, TRIVENI:Profit
  & Loss, TRIVENI:Quarters, TRIVENI:Balance Sheet, TRIVENI:Cash Flow, TRIVENI:Customization (every Data_Sheet.csv
  is populated and carries P&L, quarters, balance sheet and cash flow). Open Financials.xlsx once in Excel or LibreOffice,
  save it, then run --push-again.'
- 'research: NONE. No broker notes collected. No effect on anchored evidence.'
- 'other: NONE (folder empty, never consumed).'
- 'screening: only <TICKER>-Data_Sheet.csv exists for TRUALT and each peer; the Profit & Loss / Balance Sheet /
  Cash Flow / Quarters sheets exported empty and were not written. Data_Sheet carries FY23-FY26 annual P&L, balance
  sheet, cash flow and nine quarters (Jun-2024 to Jun-2026), so the gap is cosmetic. TRUALT screener history starts
  FY23 (company incorporated 2021): Gate 0 data_years is at most 4 audited years; the prospectus restated FY23-FY25
  is the backward baseline.'
- 'concalls: FOUR transcripts present (Q2FY26 to Q1FY27). The contract uses the 3 most recent (Q3FY26, Q4FY26, Q1FY27);
  the Q2FY26 (Nov-2025) transcript is passed to stage 5 as the promise baseline for the multi-feed shutdown, because
  the load-bearing guidance-vs-delivery fact needs the first post-listing promise. Deliberate deviation, recorded
  here.'
- 'prospectus: PRESENT (final prospectus 01-Oct-2025). Listed 03-Oct-2025, inside the ~3 year window, so it is foundational:
  promoter/group history, group-company map, restated FY23-FY25.'
- 'results: the Q4FY26 audited results PDF is a scan; its financial tables come from OCR text (RapidOCR). Stages
  cross-check any OCR figure against the FY26 AR (text-native) and anchor to the AR where both carry the figure.'
- 'results: Q2FY26 and Q1FY26 results are not in results/ (contract keeps 3 most recent). The Q2FY26 results sit
  inside inputs/announcements/20251111-d6d62c30-*.pdf (board outcome); Q1FY26 (BSE, 19-Oct-2025) was not downloaded.'
- 'sector_cap_row: Step 1 set ''Sugar / agri-commodity'' (18x). That row is Section 1B v3.11 Amendment 27.4 (16-Sep-2026),
  present on branch framework/group-3-promotions and NOT yet merged to main; this run branch is cut from main, whose
  cap table lacks the row. Nearest row on main: ''Agri processing'' 20x. Flagged for phase-3 operator confirmation
  before stage 11.'
freshness_pairs:
- pair: RESULTS to CONCALL
  trigger_doc: inputs/results/20260728-0be1ab5a-0d18-4e49-bee4-59b1c1bad6e3.pdf (Q1FY27)
  mate_expected: Q1FY27 transcript
  status: PASS
  missing_doc: ''
  mate_found: inputs/concalls/Concall_Aug_2026_Transcript.pdf (quarter ended 30-Jun-2026)
- pair: RATING BULLETIN to RATIONALE
  trigger_doc: inputs/rating/20260428-d45123bf-acc7-4fae-a013-0416f795d2d5.pdf
  mate_expected: full Ind-Ra rationale
  status: PASS
  missing_doc: ''
  mate_found: same file pp.2-8 carries the full Ind-Ra press release with detailed rationale
- pair: SEBI ORDER to ORDER TEXT
  trigger_doc: none
  mate_expected: n/a
  status: PASS
  missing_doc: ''
  mate_found: no SEBI order referenced in the corpus; the 25-Aug-2026 fines are exchange notices (inputs/announcements/20260826-*)
- pair: AR to LATEST AUDITED ANNUAL RESULTS
  trigger_doc: inputs/results/20260522-f5247716-e67c-4a23-aa42-626d5c3c9e0b.pdf (FY26 audited)
  mate_expected: FY26 AR
  status: PASS
  missing_doc: ''
  mate_found: inputs/annual-report/Annual_Report_2026.pdf (FY2025-26)
freshness_verdict: FRESHNESS PAIRS OK
reporting_units:
  results: INR lakh
  annual_report: INR lakh
  prospectus: INR lakh
  rating: INR million
  screener: INR Cr
  presentation: read off each slide
sector_cap_row:
  row: Sugar / agri-commodity
  cap: 18x
  evidence: 'Revenue is fuel ethanol sold to OMCs at administered prices; row boundary text: revenue dominated by
    one commodity with regulated or exchange-traded pricing.'
  cite: section-1b chunk 05 (A27.4) and frameworks/Section_1B_v3_11_Amendments.md Amendment 27.4, both on branch
    framework/group-3-promotions
  status: 'PROVISIONAL: row not on main; confirm at phase 3'
listed_date: '2025-10-03'
concall_map:
  inputs/concalls/Concall_Nov_2025_Transcript.pdf: Q2FY26
  inputs/concalls/Concall_Feb_2026_Transcript.pdf: Q3FY26
  inputs/concalls/Concall_May_2026_Transcript.pdf: Q4FY26
  inputs/concalls/Concall_Aug_2026_Transcript.pdf: Q1FY27
peers:
  GULPOLY: grain-ethanol comp (maize/rice distillery to OMCs)
  BALRAMCHIN: scale integrated sugar + cane/grain distillery
  TRIVENI: dual-feed cane-juice + grain distillery; replaced RENUKA (no concall since Jun-2022)
corpus_manifest:
- path: inputs/announcements/20251006-678cac7b-9ab0-4249-9118-7724b03aa5b4.pdf
  text: inputs/announcements/20251006-678cac7b-9ab0-4249-9118-7724b03aa5b4.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Disclosure Under Regulation 30(5) Of SEBI (LODR) Regulation, 2015'
  period: '2025-10-06'
  folder_match: true
- path: inputs/announcements/20251019-d4284e6c-df6d-47b2-8a09-42d1f07cc25f.pdf
  text: inputs/announcements/20251019-d4284e6c-df6d-47b2-8a09-42d1f07cc25f.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Acquisition'
  period: '2025-10-19'
  folder_match: true
- path: inputs/announcements/20251028-02847e6d-b315-45ed-8f84-31fea22e8a41.pdf
  text: inputs/announcements/20251028-02847e6d-b315-45ed-8f84-31fea22e8a41.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Cessation'
  period: '2025-10-28'
  folder_match: true
- path: inputs/announcements/20251028-0ede2eb1-3122-4a15-b728-ee5f05fc21e7.pdf
  text: inputs/announcements/20251028-0ede2eb1-3122-4a15-b728-ee5f05fc21e7.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Additional Investment In The Equity Shares Of Trualt Gas Private Limited, A Subsidiary Of
    The Company.'
  period: '2025-10-28'
  folder_match: true
- path: inputs/announcements/20251028-6aa06f36-10db-4224-a6bb-263bde21a4c6.pdf
  text: inputs/announcements/20251028-6aa06f36-10db-4224-a6bb-263bde21a4c6.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Board Meeting Outcome for Outcome Of The Board Meeting Held On October 29, 2025.'
  period: '2025-10-28'
  folder_match: true
- path: inputs/announcements/20251111-2c0f49d1-199d-496d-b526-a03bef2a6204.pdf
  text: inputs/announcements/20251111-2c0f49d1-199d-496d-b526-a03bef2a6204.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Memorandum of Understanding /Agreements'
  period: '2025-11-11'
  folder_match: true
- path: inputs/announcements/20251111-d6d62c30-2987-4d14-a3e3-ab916991fdf5.pdf
  text: inputs/announcements/20251111-d6d62c30-2987-4d14-a3e3-ab916991fdf5.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Board Meeting Outcome for Outcome Of The Board Meeting Held On November 11, 2025'
  period: '2025-11-11'
  folder_match: true
- path: inputs/announcements/20251112-14ed093e-682b-4be4-9579-926cccc1a287.pdf
  text: inputs/announcements/20251112-14ed093e-682b-4be4-9579-926cccc1a287.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Press Release / Media Release'
  period: '2025-11-12'
  folder_match: true
- path: inputs/announcements/20251113-1527b507-cbcf-4830-88a2-43fb06feb4fa.pdf
  text: inputs/announcements/20251113-1527b507-cbcf-4830-88a2-43fb06feb4fa.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Analyst / Investor Meet - Outcome'
  period: '2025-11-13'
  folder_match: true
- path: inputs/announcements/20251115-81ab5769-1650-486c-bbe7-279ba406789d.pdf
  text: inputs/announcements/20251115-81ab5769-1650-486c-bbe7-279ba406789d.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Memorandum of Understanding /Agreements'
  period: '2025-11-15'
  folder_match: true
- path: inputs/announcements/20251115-deb06aae-b3e2-40d8-bb4e-bc7525e86f7a.pdf
  text: inputs/announcements/20251115-deb06aae-b3e2-40d8-bb4e-bc7525e86f7a.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Press Release / Media Release'
  period: '2025-11-15'
  folder_match: true
- path: inputs/announcements/20260109-a81b4f85-e8b9-46f2-b3da-beec0bee1719.pdf
  text: inputs/announcements/20260109-a81b4f85-e8b9-46f2-b3da-beec0bee1719.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Board Meeting Outcome for Outcome Of Board Meeting'
  period: '2026-01-09'
  folder_match: true
- path: inputs/announcements/20260204-9e2321b0-b598-4e63-a3aa-32d51a4a607d.pdf
  text: inputs/announcements/20260204-9e2321b0-b598-4e63-a3aa-32d51a4a607d.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Press Release / Media Release'
  period: '2026-02-04'
  folder_match: true
- path: inputs/announcements/20260206-fb6a6ed0-7028-4649-9c3c-09f7680e956c.pdf
  text: inputs/announcements/20260206-fb6a6ed0-7028-4649-9c3c-09f7680e956c.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Disclosure Under Regulation 30 Of The Securities And Exchange Board Of India (Listing Obligations
    And Disclosure Requirements) Regulations, 2015'
  period: '2026-02-06'
  folder_match: true
- path: inputs/announcements/20260209-e149c802-673e-46f2-bbb2-7cb458c5df12.pdf
  text: inputs/announcements/20260209-e149c802-673e-46f2-bbb2-7cb458c5df12.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Analyst / Investor Meet - Outcome'
  period: '2026-02-09'
  folder_match: true
- path: inputs/announcements/20260210-c6b6f62f-d4d2-4ba0-add9-dc5c3eed9dbe.pdf
  text: inputs/announcements/20260210-c6b6f62f-d4d2-4ba0-add9-dc5c3eed9dbe.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Monitoring Agency Report'
  period: '2026-02-10'
  folder_match: true
- path: inputs/announcements/20260319-a40a58dc-d74f-4d99-ad10-e84f2d61bbe1.pdf
  text: inputs/announcements/20260319-a40a58dc-d74f-4d99-ad10-e84f2d61bbe1.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Press Release / Media Release'
  period: '2026-03-19'
  folder_match: true
- path: inputs/announcements/20260330-b112b5a7-e0ce-4c2f-a4be-1bd919c5328c.pdf
  text: inputs/announcements/20260330-b112b5a7-e0ce-4c2f-a4be-1bd919c5328c.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Disclosure Under Regulation 30(5) Of SEBI (LODR) Regulation, 2015'
  period: '2026-03-30'
  folder_match: true
- path: inputs/announcements/20260515-770462ed-0f51-4b70-bccb-7cecaa508809.pdf
  text: inputs/announcements/20260515-770462ed-0f51-4b70-bccb-7cecaa508809.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Monitoring Agency Report'
  period: '2026-05-15'
  folder_match: true
- path: inputs/announcements/20260522-00273a4a-f863-493b-8293-2350a4b28925.pdf
  text: inputs/announcements/20260522-00273a4a-f863-493b-8293-2350a4b28925.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Analyst / Investor Meet - Outcome'
  period: '2026-05-22'
  folder_match: true
- path: inputs/announcements/20260618-5fbbc5d6-c9fe-4b13-8492-ccd301523eab.pdf
  text: inputs/announcements/20260618-5fbbc5d6-c9fe-4b13-8492-ccd301523eab.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Press Release / Media Release'
  period: '2026-06-18'
  folder_match: true
- path: inputs/announcements/20260618-81dcb00a-2695-4ccf-9471-78612f6ddb39.pdf
  text: inputs/announcements/20260618-81dcb00a-2695-4ccf-9471-78612f6ddb39.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Press Release / Media Release (Revised)'
  period: '2026-06-18'
  folder_match: true
- path: inputs/announcements/20260728-dbc835b6-c55c-45ba-bcf3-746041928f4c.pdf
  text: inputs/announcements/20260728-dbc835b6-c55c-45ba-bcf3-746041928f4c.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Cessation'
  period: '2026-07-28'
  folder_match: true
- path: inputs/announcements/20260728-dc772654-a845-4905-ae17-80b0fd8d7430.pdf
  text: inputs/announcements/20260728-dc772654-a845-4905-ae17-80b0fd8d7430.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Press Release / Media Release'
  period: '2026-07-28'
  folder_match: true
- path: inputs/announcements/20260728-f298c590-66fd-4370-b478-3761a3611fc3.pdf
  text: inputs/announcements/20260728-f298c590-66fd-4370-b478-3761a3611fc3.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Change in Management'
  period: '2026-07-28'
  folder_match: true
- path: inputs/announcements/20260729-2ccb5b86-ae88-4c12-a556-475ee4c53764.pdf
  text: inputs/announcements/20260729-2ccb5b86-ae88-4c12-a556-475ee4c53764.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Analyst / Investor Meet - Outcome'
  period: '2026-07-29'
  folder_match: true
- path: inputs/announcements/20260803-2ea4073d-47c4-4ad8-b2aa-f73682f1d4f2.pdf
  text: inputs/announcements/20260803-2ea4073d-47c4-4ad8-b2aa-f73682f1d4f2.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Monitoring Agency Report'
  period: '2026-08-03'
  folder_match: true
- path: inputs/announcements/20260804-8aee3e5f-1c5c-4fe0-8892-e6bedce687c0.pdf
  text: inputs/announcements/20260804-8aee3e5f-1c5c-4fe0-8892-e6bedce687c0.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Announcement under Regulation 30 (LODR)-Diversification / Disinvestment'
  period: '2026-08-04'
  folder_match: true
- path: inputs/announcements/20260821-c043b2c0-a6af-4567-99b3-1d1e1d9b817a.pdf
  text: inputs/announcements/20260821-c043b2c0-a6af-4567-99b3-1d1e1d9b817a.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Disclosure Under Regulation 30 Of SEBI (Listing Obligations And Disclosure Requirements)
    Regulations, 2015'
  period: '2026-08-21'
  folder_match: true
- path: inputs/announcements/20260826-e98e197e-d139-4235-8f4c-dfd6749050f0.pdf
  text: inputs/announcements/20260826-e98e197e-d139-4235-8f4c-dfd6749050f0.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Disclosure Under Regulation 30 Of SEBI (Listing Obligations And Disclosure Requirements)
    Regulations, 2015'
  period: '2026-08-26'
  folder_match: true
- path: inputs/announcements/20260831-72bbee7a-6d80-4282-bde3-d557c3394b74.pdf
  text: inputs/announcements/20260831-72bbee7a-6d80-4282-bde3-d557c3394b74.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Shareholder Meeting / Postal Ballot-Outcome of AGM'
  period: '2026-08-31'
  folder_match: true
- path: inputs/announcements/20260901-5fe9ab1b-bfec-4527-a11b-57d8c43ae475.pdf
  text: inputs/announcements/20260901-5fe9ab1b-bfec-4527-a11b-57d8c43ae475.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Shareholder Meeting / Postal Ballot-Scrutinizer''''s Report'
  period: '2026-09-01'
  folder_match: true
- path: inputs/announcements/20260915-ba753534-1074-4a25-8acc-1a033e4ae62b.pdf
  text: inputs/announcements/20260915-ba753534-1074-4a25-8acc-1a033e4ae62b.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Structural Digital Database'
  period: '2026-09-15'
  folder_match: true
- path: inputs/announcements/20260916-10f2ed82-32d2-4120-845b-5be5206e82d8.pdf
  text: inputs/announcements/20260916-10f2ed82-32d2-4120-845b-5be5206e82d8.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Structural Digital Database'
  period: '2026-09-16'
  folder_match: true
- path: inputs/announcements/20260917-d3166e77-963f-4175-82f8-f5ce65a59ee7.pdf
  text: inputs/announcements/20260917-d3166e77-963f-4175-82f8-f5ce65a59ee7.txt
  issuer: TruAlt Bioenergy Ltd
  type: 'Reg 30 filing: Structural Digital Database'
  period: '2026-09-17'
  folder_match: true
- path: inputs/annual-report/Annual_Report_2026.pdf
  text: inputs/annual-report/Annual_Report_2026.txt
  issuer: TruAlt Bioenergy Ltd
  type: Annual report FY26 (filed with AGM notice 06-Aug-2026), Rs lakh
  period: FY2025-26
  folder_match: true
- path: inputs/concalls/Concall_Aug_2026_Transcript.pdf
  text: inputs/concalls/Concall_Aug_2026_Transcript.txt
  issuer: TruAlt Bioenergy Ltd
  type: Earnings call transcript (filed 04-Aug-2026)
  period: Q1FY27
  folder_match: true
- path: inputs/concalls/Concall_Feb_2026_Transcript.pdf
  text: inputs/concalls/Concall_Feb_2026_Transcript.txt
  issuer: TruAlt Bioenergy Ltd
  type: Earnings call transcript (filed 13-Feb-2026)
  period: Q3FY26
  folder_match: true
- path: inputs/concalls/Concall_May_2026_Transcript.pdf
  text: inputs/concalls/Concall_May_2026_Transcript.txt
  issuer: TruAlt Bioenergy Ltd
  type: Earnings call transcript (filed 28-May-2026)
  period: Q4FY26 / FY26
  folder_match: true
- path: inputs/concalls/Concall_Nov_2025_Transcript.pdf
  text: inputs/concalls/Concall_Nov_2025_Transcript.txt
  issuer: TruAlt Bioenergy Ltd
  type: Earnings call transcript (filed 19-Nov-2025)
  period: Q2FY26
  folder_match: true
- path: inputs/peer-concalls/BALRAMCHIN-Concall_Aug_2026_Transcript.pdf
  text: inputs/peer-concalls/BALRAMCHIN-Concall_Aug_2026_Transcript.txt
  issuer: Balrampur Chini Mills Ltd
  type: Peer earnings call transcript
  period: Q1FY27
  folder_match: true
- path: inputs/peer-concalls/BALRAMCHIN-Concall_Feb_2026_Transcript.pdf
  text: inputs/peer-concalls/BALRAMCHIN-Concall_Feb_2026_Transcript.txt
  issuer: Balrampur Chini Mills Ltd
  type: Peer earnings call transcript
  period: Q3FY26
  folder_match: true
- path: inputs/peer-concalls/BALRAMCHIN-Concall_Jun_2026_Transcript.pdf
  text: inputs/peer-concalls/BALRAMCHIN-Concall_Jun_2026_Transcript.txt
  issuer: Balrampur Chini Mills Ltd
  type: Peer earnings call transcript
  period: Q4FY26 (filed 22-May-2026; filename month is the collector label)
  folder_match: true
- path: inputs/peer-concalls/BALRAMCHIN-Concall_May_2026_Transcript.pdf
  text: inputs/peer-concalls/BALRAMCHIN-Concall_May_2026_Transcript.txt
  issuer: Balrampur Chini Mills Ltd
  type: Peer earnings call transcript
  period: filed 30-Apr-2026; quarter to be read from the transcript (filename month is the collector label)
  folder_match: true
- path: inputs/peer-concalls/GULPOLY-Concall_Aug_2026_Transcript.pdf
  text: inputs/peer-concalls/GULPOLY-Concall_Aug_2026_Transcript.txt
  issuer: Gulshan Polyols Ltd
  type: Peer earnings call transcript
  period: Q1FY27
  folder_match: true
- path: inputs/peer-concalls/GULPOLY-Concall_Feb_2026_Transcript.pdf
  text: inputs/peer-concalls/GULPOLY-Concall_Feb_2026_Transcript.txt
  issuer: Gulshan Polyols Ltd
  type: Peer earnings call transcript
  period: Q3FY26
  folder_match: true
- path: inputs/peer-concalls/GULPOLY-Concall_May_2026_Transcript.pdf
  text: inputs/peer-concalls/GULPOLY-Concall_May_2026_Transcript.txt
  issuer: Gulshan Polyols Ltd
  type: Peer earnings call transcript
  period: Q4FY26
  folder_match: true
- path: inputs/peer-concalls/GULPOLY-Concall_Nov_2025_Transcript.pdf
  text: inputs/peer-concalls/GULPOLY-Concall_Nov_2025_Transcript.txt
  issuer: Gulshan Polyols Ltd
  type: Peer earnings call transcript
  period: Q2FY26
  folder_match: true
- path: inputs/peer-concalls/TRIVENI-Concall_Aug_2026_Transcript.pdf
  text: inputs/peer-concalls/TRIVENI-Concall_Aug_2026_Transcript.txt
  issuer: Triveni Engineering & Industries Ltd
  type: Peer earnings call transcript
  period: Q1FY27
  folder_match: true
- path: inputs/peer-concalls/TRIVENI-Concall_Feb_2026_Transcript.pdf
  text: inputs/peer-concalls/TRIVENI-Concall_Feb_2026_Transcript.txt
  issuer: Triveni Engineering & Industries Ltd
  type: Peer earnings call transcript
  period: Q3FY26
  folder_match: true
- path: inputs/peer-concalls/TRIVENI-Concall_Jun_2026_Transcript.pdf
  text: inputs/peer-concalls/TRIVENI-Concall_Jun_2026_Transcript.txt
  issuer: Triveni Engineering & Industries Ltd
  type: Peer earnings call transcript
  period: Q4FY26 (filename month is the collector label; read period from transcript)
  folder_match: true
- path: inputs/peer-concalls/TRIVENI-Concall_Nov_2025_Transcript.pdf
  text: inputs/peer-concalls/TRIVENI-Concall_Nov_2025_Transcript.txt
  issuer: Triveni Engineering & Industries Ltd
  type: Peer earnings call transcript
  period: Q2FY26
  folder_match: true
- path: inputs/presentation/20260522-2464a867-08cc-4a4a-8267-001ced7bce0f.pdf
  text: inputs/presentation/20260522-2464a867-08cc-4a4a-8267-001ced7bce0f.txt
  issuer: TruAlt Bioenergy Ltd
  type: Investor presentation (filed 22-May-2026)
  period: Q4FY26 / FY26
  folder_match: true
- path: inputs/presentation/Investor_Presentation_1.pdf
  text: inputs/presentation/Investor_Presentation_1.txt
  issuer: TruAlt Bioenergy Ltd
  type: Investor presentation (filed 28-Jul-2026)
  period: Q1FY27
  folder_match: true
- path: inputs/prospectus/TRUALT-Prospectus-01OCT2025.pdf
  text: inputs/prospectus/TRUALT-Prospectus-01OCT2025.txt
  issuer: TruAlt Bioenergy Ltd
  type: Final prospectus (IPO), 678 pp, Rs lakh; NSE archive FP_INE0MWH01014_01OCT2025
  period: Restated FY23-FY25 + stub period
  folder_match: true
- path: inputs/rating/20260428-d45123bf-acc7-4fae-a013-0416f795d2d5.pdf
  text: inputs/rating/20260428-d45123bf-acc7-4fae-a013-0416f795d2d5.txt
  issuer: TruAlt Bioenergy Ltd / India Ratings
  type: Reg 30 intimation + full Ind-Ra rating rationale (27-Apr-2026), IND A-/Stable/IND A2+ on INR 17,660 mn bank
    facilities
  period: Apr-2026
  folder_match: true
- path: inputs/results/20260203-7ed30bcf-6620-4b8d-b17e-b2497a804aa6.pdf
  text: inputs/results/20260203-7ed30bcf-6620-4b8d-b17e-b2497a804aa6.txt
  issuer: TruAlt Bioenergy Ltd
  type: Unaudited results, standalone + consolidated, Rs lakh
  period: Q3FY26 / 9MFY26
  folder_match: true
- path: inputs/results/20260522-f5247716-e67c-4a23-aa42-626d5c3c9e0b.pdf
  text: inputs/results/20260522-f5247716-e67c-4a23-aa42-626d5c3c9e0b.txt
  issuer: TruAlt Bioenergy Ltd
  type: Audited results + board outcome, standalone + consolidated, Rs lakh; SCANNED, 16/20 pages OCR text
  period: Q4FY26 / FY26
  folder_match: true
- path: inputs/results/20260728-0be1ab5a-0d18-4e49-bee4-59b1c1bad6e3.pdf
  text: inputs/results/20260728-0be1ab5a-0d18-4e49-bee4-59b1c1bad6e3.txt
  issuer: TruAlt Bioenergy Ltd
  type: Unaudited results (limited review), standalone + consolidated, Rs lakh
  period: Q1FY27
  folder_match: true
- path: inputs/shareholding/TRUALT-SHP-June-2026.html
  text: inputs/shareholding/TRUALT-SHP-June-2026.txt
  issuer: TruAlt Bioenergy Ltd (BSE XBRL)
  type: Shareholding pattern Reg 31
  period: quarter ended 30-Jun-2026 (filed 17-Jul-2026)
  folder_match: true
- path: inputs/shareholding/TRUALT-SHP-March-2026.html
  text: inputs/shareholding/TRUALT-SHP-March-2026.txt
  issuer: TruAlt Bioenergy Ltd (BSE XBRL)
  type: Shareholding pattern Reg 31
  period: quarter ended 31-Mar-2026
  folder_match: true
flags: []
analyst_note: 'Corpus is complete for a phase 1 read. Two soft spots: the scanned Q4FY26 results (OCR) and the provisional
  sector cap row that exists only on an unmerged framework branch.'

```