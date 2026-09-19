# Stage 0 — Input validation: RAPPID (Rappid Valves (India) Ltd), run 2026-09-19

Run by the orchestrator inline (no subagent). Block: outputs/blocks/B00-inputs.yaml (governs).

## Spear gate
companies/RAPPID.md carries `Spear: OVERRIDE 2026-09-19 (operator standing ruling 2026-09-05: Step-1 intake replaces the web spear)`. Gate PASSES. The four load-bearing facts in B00.spear_gate are the first verification priority for every stage.

## Manifest
company Rappid Valves (India) Ltd; ticker RAPPID; cmp 365.9; market_cap_cr 189.97; listed 2024-09-30 (NSE Emerge SME); run_type full; concalls_available false (NO-CONCALL MODE). cmp and market cap are non-zero: the standalone screener page was used (the consolidated page carries no figures).

## Sector cap row
Cables / Industrial products (25x), per section-1b chunk 05. Evidence and phase-3 flag in B00.sector_cap_row_evidence.

## Reporting units
Results, FY26 AR and RHP in INR Lakhs. FY25 AR (other/) in INR Thousands. The 12-May-2025 original FY25 filing shows statements in Rupees. Screener and business updates in INR Cr. Convert once, at stage 10.

## Freshness pair check
All four pairs PASS. Verdict: FRESHNESS PAIRS OK. Detail in B00.freshness_pairs.

## Collector defect gate
1. collector_warnings copied verbatim into B00.input_gaps.
2. Screening CSVs opened: screener-Data_Sheet.csv, KSB-, QUESTFLOW-, ATAM-Data_Sheet.csv each carry numbers (FY22-FY26 P&L, balance sheet, cash flow for RAPPID). P&L/BS/CF/Quarters sheets were empty exports and were not written.
3. announcements/ (42) and shareholding/ (5 XBRL) are populated from the NSE SME API at /step1.
4. cmp and market_cap_cr non-zero. No halt.

## Empty folders
rating/ and research/ are empty. EMPTY-FOLDER CONFIRMATION suppressed by the /step1 autonomy contract; standing answer "proceed with the gaps". Degradation: stage 10 marks rating_wc_quote unresolved; research has no effect on anchored evidence.

## Corpus manifest (document identity check, page 1 read for every PDF)

| path | issuer | document type | page-1 subject / period | matches folder |
|---|---|---|---|---|
| inputs/announcements/01Feb2025_RAPPID_01022025120242_RappidQIA.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation under Regulation 30 of SEBI (Listing Obligations and Disclosure Requirements) | yes |
| inputs/announcements/01Jun2026_RAPPID_01062026184958_Rappid_ACVC_RecordingSigned.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Audio/Video Recording of the Earnings Call held on 01 June 2026. | yes |
| inputs/announcements/01Mar2025_RAPPID_01032025162400_CS_Reg.pdf | Rappid Valves (India) Ltd | Reg 30 filing | InƟmaƟon of ResignaƟon of Company Secretary and Compliance Oﬃcer of the Company | yes |
| inputs/announcements/01Sep2025_RAPPID_01092025164803_Board_Meeting_Outcome.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Outcome of the Board meeting held on 01st September, 2025. | yes |
| inputs/announcements/01Sep2026_RAPPID_01092026200937_Intimation_Notice_of_AGM_Signed.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Notice of 24th Annual General Meeting to be held on Thursday, September 24, 2026 | yes |
| inputs/announcements/02Sep2025_RAPPID_02092025232559_Intimation_Notice.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Notice of 23rd Annual General Meeting pursuant to Regulation 30 of the SEBI (Listing | yes |
| inputs/announcements/03Dec2024_RAPPID_03122024161834_PODisclosure.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation of receipt of Purchase Orders amounting Rs 4,03,90,000 /- from Vinpa | yes |
| inputs/announcements/03Jul2025_RAPPID_03072025172357_SD_General_Business_Update_Rappid.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation under Regulation 30 of SEBI (Listing Obligations and Disclosure | yes |
| inputs/announcements/04Jun2025_RAPPID_04062025121355_Rappid_Disclosure_Sd.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Disclosure as per Regulation 7(2) of SEBI (Prohibition of Insider Trading) Regulations, 2015 | yes |
| inputs/announcements/07Jan2025_RAPPID_07012025152409_Change_in_RTA_Rappid.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation regarding change in name of Registrar and Transfer Agent (RTA) of | yes |
| inputs/announcements/07Mar2026_RAPPID_07032026121657_IRAppt.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation of Appointment of Investor Relations (IR) Agency. | yes |
| inputs/announcements/07Mar2026_RAPPID_07032026152649_Board_Meeting_Outcome_Signed.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Outcome of the Board meeting held on 07th March 2026. | yes |
| inputs/announcements/08Jun2026_RAPPID_08062026151443_Work_Order_Shree_.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Disclosure under Regulations 30 of SEBI (Listing Obligations and Disclosure Requirements) | yes |
| inputs/announcements/09Jul2026_RAPPID_09072026161031_General_Business_Update_Rappid_signed.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation of Business Update for the Quarter Ended June 30, 2026 (Q1/2026-27) | yes |
| inputs/announcements/10Jul2026_RAPPID_10072026150526_GBU_Rappid_Signed.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation of revision in Business Update for the Quarter Ended June 30, 2026 | yes |
| inputs/announcements/10Mar2025_RAPPID_10032025153940_Outcome_of_BM.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Outcome of the Board meeƟng held on March 10, 2025 | yes |
| inputs/announcements/13Aug2026_RAPPID_13082026191053_Workorder.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Disclosure under Regulations 30 of SEBI (Listing Obligations and Disclosure Requirements) | yes |
| inputs/announcements/14Jan2025_RAPPID_19122024172640_NSEReply.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Queries Raise Segment Details | yes |
| inputs/announcements/14May2025_RAPPID_14052025151842_Rappid_PO_order_disclosure.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Bagging of Letter of Intent for supply of valves amounting to INR 2.58 Crores from  Larsen | yes |
| inputs/announcements/14Nov2024_RAPPID_14112024230617_statement_of_deviation.pdf | Rappid Valves (India) Ltd | Reg 30 filing | (image-only; identity from NSE feed metadata: statement of deviation, IPO proceeds, H1FY25) | yes |
| inputs/announcements/15Jun2026_RAPPID_15062026102327_Work_Order.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Disclosure under Regulations 30 of SEBI (Listing Obligations and Disclosure Requirements) | yes |
| inputs/announcements/16Jan2026_RAPPID_16012026141145_Clarification_Letter.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Clarification w.r.t disclosure made under Regulation 7 of SEBI (Prohibition of Insider Trading) | yes |
| inputs/announcements/16Oct2025_RAPPID_16102025150349_General_Information_Business_update.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation under Regulation 30 of SEBI (Listing Obligations and Disclosure Requirements) | yes |
| inputs/announcements/18Jul2025_RAPPID_18072025165114_SignedBoard_Meeting_Outcome.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Outcome of the Board meeting held on 18th July,2025 | yes |
| inputs/announcements/19Jan2026_RAPPID_19012026164650_Clarification_Letter_Signed.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Clarification on Financial Results for the Quarter Ended September 30, 2025 | yes |
| inputs/announcements/20Mar2025_RAPPID_20032025152024_Rappid_Disclosure.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Disclosure as per Regulation 7(2) of SEBI (Prohibition of Insider Trading) Regulations, 2015 | yes |
| inputs/announcements/21Mar2026_RAPPID_21032026151115_Board_Meeting_OutcomeSd.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Outcome of the Board meeting held on 21st March 2026. | yes |
| inputs/announcements/24Mar2026_RAPPID_24032026155948_Intimation_Sd.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation of Completion of Dispatch of Notice of Extra Ordinary General Meeting | yes |
| inputs/announcements/25May2026_team_sandeshc_29042026124914_40.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Declaration under Regulation 31(4) of the SEBI (Substantial Acquisition of Shares and | yes |
| inputs/announcements/26May2026_RAPPID_26052026192553_Signed_Intimation_of_EC.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation of Earnings Conference Call scheduled to be held on Monday, 01st June 2026. | yes |
| inputs/announcements/27Mar2025_RAPPID_27032025132136_Rappid_Disclosure_signed.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Disclosure as per Regulation 7(2) of SEBI (Prohibition of Insider Trading) Regulations, 2015 | yes |
| inputs/announcements/27Sep2025_RAPPID_27092025175941_AGM_Proceedings_SD.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Proceedings of the 23rd Annual General Meeting held on Saturday, 27th Day of September 2025 | yes |
| inputs/announcements/28Feb2026_RAPPID_28022026144345_CS_Resignation.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation of Resignation of Company Secretary and Compliance Officer of the | yes |
| inputs/announcements/28May2026_RAPPID_28052026195951_Rappid_Press_Release_Intimation_signed.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Submission of Press Release pertaining to audited financial results for the half year and | yes |
| inputs/announcements/28Nov2024_RAPPID_28112024175140_Rappid_Investor_Meet_Public_Announcement_signed.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation of Schedule of Analyst/Institutional Investor Meeting under | yes |
| inputs/announcements/29May2026_RAPPID_29052026173059_Work_Order.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Disclosure under Regulations 30 of SEBI (Listing Obligations and Disclosure Requirements) | yes |
| inputs/announcements/29Sep2025_RAPPID_29092025180910_Voting_Result_and_Scrutinizer_Report_final.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Declaration of Voting Results and Scrutinizers Report with respect to the 23rd Annual General | yes |
| inputs/announcements/30Apr2026_RAPPID_30042026174853_Scrutinizersreport.pdf | Rappid Valves (India) Ltd | Reg 30 filing | DeclaraƟon of VoƟng Results and ScruƟnizers Report for the Postal Ballot. | yes |
| inputs/announcements/30Jan2025_RAPPID_30012025170006_RappidInvestormeet.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Intimation of Schedule of Analyst/Institutional Investor Meeting under | yes |
| inputs/announcements/30Jun2025_RAPPID_25062025164758_Claritifcationletterrappidsd.pdf | Rappid Valves (India) Ltd | Reg 30 filing | DeclaraƟon pursuant to RegulaƟon 33(3)(d) of the SEBI (LisƟng ObligaƟons and | yes |
| inputs/announcements/30Jun2025_team_sandeshc_15052025134311_14.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Declaration under Regulation 31(4) of the SEBI (Substantial Acquisition of Shares and | yes |
| inputs/announcements/30Mar2026_RAPPID_30032026155315_Corigendum_Rappid_Sd.pdf | Rappid Valves (India) Ltd | Reg 30 filing | Corrigendum to the Postal Ballot Notice of Rappid Valves (India) Limited | yes |
| inputs/annual-report/Annual_Report_2026.pdf | Rappid Valves (India) Ltd | Annual report FY26 (y/e 31-Mar-2026) | 24th Annual Report of the Company for the Financial Year 2025-26. | yes |
| inputs/concalls/Concall_Jun_2026_Transcript.pdf | Rappid Valves (India) Ltd | Earnings call transcript, FY26 results, 01-Jun-2026 | Intimation of Transcript for Earnings Conference Call held on Monday, June 01, 2026. | yes |
| inputs/other/Annual_Report_2025.pdf | Rappid Valves (India) Ltd | Annual report FY25 (y/e 31-Mar-2025) | 23rd Annual Report of the Company for the Financial Year 2024-25. | yes |
| inputs/peer-concalls/ATAM-Concall_Apr_2024_Transcript.pdf | Atam Valves Ltd | Earnings call transcript | Transcript of Earnings Call for the Quarter and Financial year ended March 31, 2024 | yes |
| inputs/peer-concalls/ATAM-Concall_Jul_2024_Transcript.pdf | Atam Valves Ltd | Earnings call transcript | Transcript of Earnings Call for the Quarter ended June 30, 2024 | yes |
| inputs/peer-concalls/ATAM-Concall_Nov_2023_Transcript.pdf | Atam Valves Ltd | Earnings call transcript | Transcript of Earnings Call for the Quarter and Half year ended September 30th, 2023 | yes |
| inputs/peer-concalls/KSB-Concall_Aug_2026_Transcript.pdf | KSB Ltd | Earnings call transcript | Transcript for the Institutional Investors Meet. | yes |
| inputs/peer-concalls/KSB-Concall_Mar_2026_Transcript.pdf | KSB Ltd | Earnings call transcript | Transcript for the Institutional Investors Meet. | yes |
| inputs/peer-concalls/KSB-Concall_Nov_2025_Transcript.pdf | KSB Ltd | Earnings call transcript | Transcript for the Institutional Investors Meet. | yes |
| inputs/peer-concalls/KSB-Concall_Sep_2025_Transcript.pdf | KSB Ltd | Earnings call transcript | Transcript for the Institutional Investors Meet. | yes |
| inputs/peer-concalls/QUESTFLOW-Concall_Jun_2024_Transcript.pdf | Quest Flow Controls Ltd | Earnings call transcript | Transcript for Audio Recording of Earnings Conference Call pertaining to H2 | yes |
| inputs/presentation/09Mar2026_RAPPID_09032026122042_Signed_BU.pdf | Rappid Valves (India) Ltd | Investor presentation | Investor Presentation of Rappid Valves (India) Limited | yes |
| inputs/presentation/Investor_Presentation_1.pdf | Rappid Valves (India) Ltd | Investor presentation | Intimation of Investor presentation for Earnings Conference Call scheduled to be held on | yes |
| inputs/prospectus/Rappid_Valves_RHP_Sep2024.pdf | Rappid Valves (India) Ltd | Red Herring Prospectus, Sep-2024 | - | yes |
| inputs/results/12May2025_RAPPID_12052025192339_Rappid_Outcome.pdf | Rappid Valves (India) Ltd | Board outcome with financial results | Outcome of the Board meeting held on May 12th, 2025 | yes |
| inputs/results/13Nov2025_RAPPID_13112025153621_Outcome_Final.pdf | Rappid Valves (India) Ltd | Board outcome with financial results | Outcome of the meeting of the Board of Directors of the company held on 13 | yes |
| inputs/results/14May2025_RAPPID_14052025082209_Rappid_Final_Outcome_Signed.pdf | Rappid Valves (India) Ltd | Board outcome with financial results | Outcome of the Board meeting held on May 12th, 2025 | yes |
| inputs/results/14Nov2024_Final_Outcome_3_14112024182104.pdf | Rappid Valves (India) Ltd | Board outcome with financial results | Outcome of the Board meeting held on November 14th, 2024 | yes |
| inputs/results/27May2026_RAPPID_27052026180012_BM_Outcome.pdf | Rappid Valves (India) Ltd | Board outcome with financial results | Outcome of the Board Meeting held on 27th May 2026. | yes |

Moves made at stage 0: inputs/announcements/09Mar2026_RAPPID_09032026122042_Signed_BU.pdf (+ .txt) moved to inputs/presentation/ (page 1 cover letter: "Investor Presentation of Rappid Valves (India) Limited"). inputs/peer-concalls/ATAM-Concall_Apr_2024_Transcript_2.pdf removed: the same 18-Apr-2024 Q4FY24 call as ATAM-Concall_Apr_2024_Transcript.pdf without its cover letter. No document UNIDENTIFIED. The 14-Nov-2024 statement of deviation has no text layer; its identity is from the NSE feed and its rendered pages (work/raster/deviation_14Nov2024_p1-3.png).

## Tooling
PyMuPDF text extraction for every PDF, pypdf open test for every PDF: no failures. Stages read the page-marked .txt beside each PDF; image-only pages are in work/raster/ as PNG.
