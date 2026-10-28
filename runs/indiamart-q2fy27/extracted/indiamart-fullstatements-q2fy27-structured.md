=== A1 STRUCTURED EXTRACTION (targeted notes) ===
company: INDIAMART | quarter: q2fy27 | source: Indiamart_Q2FY27_Results_Full_Statements.pdf (62 pages)
fulltext: runs/indiamart-q2fy27/extracted/indiamart-fullstatements-q2fy27-fulltext.md (line numbers below refer to that file, header included)
unit: INR million (x0.1 to Rs Crores); values verbatim, not converted
ROW ID RANGE: R001-R3165
COUNTS: NUMBER 2272 | ENTITY 358 | FORWARD 5 | DATE 94 | QUALIFIER 436
ROW FORMAT: R### | page N | line L | TYPE | verbatim value | [item] context | flag
ITEM TAGS: [I1] Other income note 20 (cons p24, stand p53) | [I2] Investments: note 7, note 8 (investments, loans, other financial assets), note 28 fair value (cons p17-20, p27; stand p46-49, p56-57) | [I3] Note 30 related parties (cons p29-31; stand p58-60) | [I4] Other non-current assets = note 9 Other assets non-current (cons p20) and note 11 Other assets non-current (stand p49) | [I5] Independent Auditor's Reports (cons p2-5; stand p33-35)
PAGES ROWED (full or partial): 2, 3, 4, 5, 17, 18, 19, 20, 24, 27, 29, 30, 31, 33, 34, 35, 46, 47, 48, 49, 53, 56, 57, 58, 59, 60
  partial pages: p20 (rowed note 8c, 8d, note 9; NOT notes 10, 11); p24 (rowed note 20 only; NOT notes 19, 21, 22); p27 (rowed note 28 only; NOT note 27 gratuity); p49 (rowed note 8 loans/other financial assets and note 11 other assets; NOT notes 9, 10); p53 (rowed note 20 only; NOT notes 21-24); p2 and p33 (letterhead block rowed as one paragraph).
PAGES NOT ROWED (fulltext only): 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 21, 22, 23, 25, 26, 28, 32, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 50, 51, 52, 54, 55, 61, 62
SCOPE FACTS (mechanical):
  - Consolidated note 7 shows IB Monotaro Private Limited reclassified to Investment in other entities at FVTPL, fair value loss INR 71.49 (cons note 7(iv), p17); standalone fair value loss INR 200.00 (stand note 7(vii), p46/p47).
  - IndiaMart Finance Limited: standalone note 7 and note 7(iii) show 1,20,50,000 equity shares, INR 120.50 (p46, p47); consolidated statements contain no line for it (a subsidiary).
  - Standalone auditor report text contains no paragraph headed "Other Matters". The consolidated report Other Matters (a) and (b) are on p4-5.
  - Notes 7 and 8 in standalone are numbered note 7 (subsidiaries and associates) and note 8; standalone note 11 is Other assets (note 9 is Trade receivables). Consolidated Other assets is note 9.
TABLE CHECK LOG (text vs pdftoppm render):
  - Viewed and matched: p17, p18, p19, p20, p24, p27, p46, p47, p48, p53. p27 reconciliation columns taken from the render. p17 restored one missing label from the render.
  - Not viewed (pdftotext -raw order read; totals cross-footed in text): p29, p30, p31, p49, p56, p57, p58, p59, p60. Cross-foot spot checks: cons other assets non-current 139.43 + 35.98 + 0 = 175.41; stand 22.75 + 0 = 22.75 and current 9.79 + 7.09 + 38.29 = 55.17; cons other income Q2 FY27 total (76.23), 6M 990.84.
  - Layout caveat: where -layout shares one fulltext line between two rows, the line anchor of the second row may repeat the first row's line (page is always right).
  - Row granularity: each (metric x period) is its own row. Face value and issue premium inside share-class labels are their own NUMBER rows. Fund, bond and G-sec holdings are ENTITY rows. Auditor paragraphs are QUALIFIER rows, one per paragraph (page-split paragraphs give one row per page fragment).
=== END STRUCTURED HEADER ===

## NUMBER TABLE (2272 rows)

R001 | page 4 | line 203 | NUMBER | five | [I5] subsidiaries not audited by BSR (audited by other auditors), other matter (a)
R002 | page 4 | line 205 | NUMBER | Rs. 2,160.49 million | [I5] five subsidiaries total assets before consolidation adjustments at 30 Sep 2026
R003 | page 4 | line 205 | NUMBER | Rs. 31.76 million | [I5] five subsidiaries total revenue before consol adj, quarter ended 30 Sep 2026
R004 | page 4 | line 206 | NUMBER | Rs. 59.01 million | [I5] five subsidiaries total revenue before consol adj, YTD ended 30 Sep 2026
R005 | page 4 | line 208 | NUMBER | Rs. 41.44 million | [I5] five subsidiaries net cash inflows before consol adj, YTD 30 Sep 2026
R006 | page 4 | line 216 | NUMBER | Rs. 153.60 million | [I5] group share of net loss, seven associates (unaudited), quarter ended 30 Sep 2026
R007 | page 4 | line 217 | NUMBER | Rs. 281.44 million | [I5] group share of net loss, seven associates (unaudited), YTD ended 30 Sep 2026
R008 | page 4 | line 218 | NUMBER | seven | [I5] associates with unaudited financial information, other matter (b)
R009 | page 4 | line 220 | NUMBER | Rs. 17.69 million | [I5] group share of net loss, one associate (unaudited), 1 Apr 2026 to 29 May 2026
R010 | page 4 | line 221 | NUMBER | one | [I5] associate with unaudited information for 1 Apr-29 May 2026
R011 | page 5 | line 249 | NUMBER | 098113 | [I5] partner membership number, consolidated report
R012 | page 35 | line 2481 | NUMBER | 098113 | [I5] partner membership number, standalone report
R013 | page 2 | line 106 | NUMBER | BA61223 | [I5] BSR & Co. registration number (footer)
R014 | page 2 | line 107 | NUMBER | AAB-8181 | [I5] BSR & Co. LLP registration number (footer)
R015 | page 2 | line 65 | NUMBER | 122 002 | [I5] Gurugram postal code (letterhead)
R016 | page 33 | line 2405 | NUMBER | BA61223 | [I5] BSR & Co. registration number (footer)
R017 | page 33 | line 2406 | NUMBER | AAB-8181 | [I5] BSR & Co. LLP registration number (footer)
R018 | page 5 | line 237 | NUMBER | 101248W/W-100022 | [I5] firm registration number, consolidated
R019 | page 35 | line 2476 | NUMBER | 101248W/W-100022 | [I5] firm registration number, standalone
R020 | page 24 | line 1721 | NUMBER | (110.71) | [I1] cons note 20 other income: funds, bonds, debentures and investment trust, qtr Sep 2026
R021 | page 24 | line 1721 | NUMBER | 74.34 | [I1] cons note 20 other income: funds, bonds, debentures and investment trust, qtr Sep 2025
R022 | page 24 | line 1721 | NUMBER | 976.01 | [I1] cons note 20 other income: funds, bonds, debentures and investment trust, 6M Sep 2026
R023 | page 24 | line 1721 | NUMBER | 949.87 | [I1] cons note 20 other income: funds, bonds, debentures and investment trust, 6M Sep 2025
R024 | page 24 | line 1722 | NUMBER | - | [I1] cons note 20 other income: -Fair value gain on measurement of Investment, qtr Sep 2026 | ZERO_STANDING
R025 | page 24 | line 1722 | NUMBER | - | [I1] cons note 20 other income: -Fair value gain on measurement of Investment, qtr Sep 2025 | ZERO_STANDING
R026 | page 24 | line 1722 | NUMBER | (71.49) | [I1] cons note 20 other income: -Fair value gain on measurement of Investment, 6M Sep 2026
R027 | page 24 | line 1722 | NUMBER | - | [I1] cons note 20 other income: -Fair value gain on measurement of Investment, 6M Sep 2025 | ZERO_STANDING
R028 | page 24 | line 1724 | NUMBER | 15.96 | [I1] cons note 20 other income: - on bank deposits, qtr Sep 2026
R029 | page 24 | line 1724 | NUMBER | 6.70 | [I1] cons note 20 other income: - on bank deposits, qtr Sep 2025
R030 | page 24 | line 1724 | NUMBER | 31.40 | [I1] cons note 20 other income: - on bank deposits, 6M Sep 2026
R031 | page 24 | line 1724 | NUMBER | 9.08 | [I1] cons note 20 other income: - on bank deposits, 6M Sep 2025
R032 | page 24 | line 1725 | NUMBER | 17.73 | [I1] cons note 20 other income: - on corporate deposits and loans, qtr Sep 2026
R033 | page 24 | line 1725 | NUMBER | 17.67 | [I1] cons note 20 other income: - on corporate deposits and loans, qtr Sep 2025
R034 | page 24 | line 1725 | NUMBER | 34.78 | [I1] cons note 20 other income: - on corporate deposits and loans, 6M Sep 2026
R035 | page 24 | line 1725 | NUMBER | 23.35 | [I1] cons note 20 other income: - on corporate deposits and loans, 6M Sep 2025
R036 | page 24 | line 1726 | NUMBER | 0.68 | [I1] cons note 20 other income: - on security deposits, qtr Sep 2026
R037 | page 24 | line 1726 | NUMBER | 0.81 | [I1] cons note 20 other income: - on security deposits, qtr Sep 2025
R038 | page 24 | line 1726 | NUMBER | 1.37 | [I1] cons note 20 other income: - on security deposits, 6M Sep 2026
R039 | page 24 | line 1726 | NUMBER | 1.60 | [I1] cons note 20 other income: - on security deposits, 6M Sep 2025
R040 | page 24 | line 1727 | NUMBER | 0.19 | [I1] cons note 20 other income: Other interest income, qtr Sep 2026
R041 | page 24 | line 1727 | NUMBER | 0.51 | [I1] cons note 20 other income: Other interest income, qtr Sep 2025
R042 | page 24 | line 1727 | NUMBER | 0.19 | [I1] cons note 20 other income: Other interest income, 6M Sep 2026
R043 | page 24 | line 1727 | NUMBER | 0.83 | [I1] cons note 20 other income: Other interest income, 6M Sep 2025
R044 | page 24 | line 1728 | NUMBER | - | [I1] cons note 20 other income: Gain on de-recognition of lease liability, qtr Sep 2026 | ZERO_STANDING
R045 | page 24 | line 1728 | NUMBER | - | [I1] cons note 20 other income: Gain on de-recognition of lease liability, qtr Sep 2025 | ZERO_STANDING
R046 | page 24 | line 1728 | NUMBER | - | [I1] cons note 20 other income: Gain on de-recognition of lease liability, 6M Sep 2026 | ZERO_STANDING
R047 | page 24 | line 1728 | NUMBER | 0.01 | [I1] cons note 20 other income: Gain on de-recognition of lease liability, 6M Sep 2025
R048 | page 24 | line 1729 | NUMBER | 0.10 | [I1] cons note 20 other income: Liabilities and provisions no longer required, qtr Sep 2026
R049 | page 24 | line 1729 | NUMBER | 0.04 | [I1] cons note 20 other income: Liabilities and provisions no longer required, qtr Sep 2025
R050 | page 24 | line 1729 | NUMBER | 15.48 | [I1] cons note 20 other income: Liabilities and provisions no longer required, 6M Sep 2026
R051 | page 24 | line 1729 | NUMBER | 39.79 | [I1] cons note 20 other income: Liabilities and provisions no longer required, 6M Sep 2025
R052 | page 24 | line 1730 | NUMBER | (0.19) | [I1] cons note 20 other income: Net gain on disposal of property, plant and e, qtr Sep 2026
R053 | page 24 | line 1730 | NUMBER | 0.19 | [I1] cons note 20 other income: Net gain on disposal of property, plant and e, qtr Sep 2025
R054 | page 24 | line 1730 | NUMBER | 3.00 | [I1] cons note 20 other income: Net gain on disposal of property, plant and e, 6M Sep 2026
R055 | page 24 | line 1730 | NUMBER | 0.26 | [I1] cons note 20 other income: Net gain on disposal of property, plant and e, 6M Sep 2025
R056 | page 24 | line 1731 | NUMBER | 0.01 | [I1] cons note 20 other income: Miscellaneous income, qtr Sep 2026
R057 | page 24 | line 1731 | NUMBER | 0.66 | [I1] cons note 20 other income: Miscellaneous income, qtr Sep 2025
R058 | page 24 | line 1731 | NUMBER | 0.10 | [I1] cons note 20 other income: Miscellaneous income, 6M Sep 2026
R059 | page 24 | line 1731 | NUMBER | 0.72 | [I1] cons note 20 other income: Miscellaneous income, 6M Sep 2025
R060 | page 24 | line 1732 | NUMBER | (76.23) | [I1] cons note 20 other income: Total, qtr Sep 2026
R061 | page 24 | line 1732 | NUMBER | 100.92 | [I1] cons note 20 other income: Total, qtr Sep 2025
R062 | page 24 | line 1732 | NUMBER | 990.84 | [I1] cons note 20 other income: Total, 6M Sep 2026
R063 | page 24 | line 1732 | NUMBER | 1,025.51 | [I1] cons note 20 other income: Total, 6M Sep 2025
R064 | page 53 | line 3751 | NUMBER | (115.09) | [I1] stand note 20 other income: funds, bonds, debentures and investment trust, qtr Sep 2026
R065 | page 53 | line 3751 | NUMBER | 56.39 | [I1] stand note 20 other income: funds, bonds, debentures and investment trust, qtr Sep 2025
R066 | page 53 | line 3751 | NUMBER | 918.58 | [I1] stand note 20 other income: funds, bonds, debentures and investment trust, 6M Sep 2026
R067 | page 53 | line 3751 | NUMBER | 894.69 | [I1] stand note 20 other income: funds, bonds, debentures and investment trust, 6M Sep 2025
R068 | page 53 | line 3752 | NUMBER | - | [I1] stand note 20 other income: -Fair value loss on measurement of Investment, qtr Sep 2026 | ZERO_STANDING
R069 | page 53 | line 3752 | NUMBER | - | [I1] stand note 20 other income: -Fair value loss on measurement of Investment, qtr Sep 2025 | ZERO_STANDING
R070 | page 53 | line 3752 | NUMBER | (200.00) | [I1] stand note 20 other income: -Fair value loss on measurement of Investment, 6M Sep 2026
R071 | page 53 | line 3752 | NUMBER | - | [I1] stand note 20 other income: -Fair value loss on measurement of Investment, 6M Sep 2025 | ZERO_STANDING
R072 | page 53 | line 3754 | NUMBER | 12.38 | [I1] stand note 20 other income: - on bank deposits, qtr Sep 2026
R073 | page 53 | line 3754 | NUMBER | 5.74 | [I1] stand note 20 other income: - on bank deposits, qtr Sep 2025
R074 | page 53 | line 3754 | NUMBER | 24.48 | [I1] stand note 20 other income: - on bank deposits, 6M Sep 2026
R075 | page 53 | line 3754 | NUMBER | 6.56 | [I1] stand note 20 other income: - on bank deposits, 6M Sep 2025
R076 | page 53 | line 3755 | NUMBER | 14.47 | [I1] stand note 20 other income: - on corporate deposits and loans, qtr Sep 2026
R077 | page 53 | line 3755 | NUMBER | 13.98 | [I1] stand note 20 other income: - on corporate deposits and loans, qtr Sep 2025
R078 | page 53 | line 3755 | NUMBER | 28.66 | [I1] stand note 20 other income: - on corporate deposits and loans, 6M Sep 2026
R079 | page 53 | line 3755 | NUMBER | 16.40 | [I1] stand note 20 other income: - on corporate deposits and loans, 6M Sep 2025
R080 | page 53 | line 3756 | NUMBER | 0.68 | [I1] stand note 20 other income: - on security deposits, qtr Sep 2026
R081 | page 53 | line 3756 | NUMBER | 0.81 | [I1] stand note 20 other income: - on security deposits, qtr Sep 2025
R082 | page 53 | line 3756 | NUMBER | 1.37 | [I1] stand note 20 other income: - on security deposits, 6M Sep 2026
R083 | page 53 | line 3756 | NUMBER | 1.60 | [I1] stand note 20 other income: - on security deposits, 6M Sep 2025
R084 | page 53 | line 3757 | NUMBER | - | [I1] stand note 20 other income: Gain on de-recognition of lease liability, qtr Sep 2026 | ZERO_STANDING
R085 | page 53 | line 3757 | NUMBER | - | [I1] stand note 20 other income: Gain on de-recognition of lease liability, qtr Sep 2025 | ZERO_STANDING
R086 | page 53 | line 3757 | NUMBER | - | [I1] stand note 20 other income: Gain on de-recognition of lease liability, 6M Sep 2026 | ZERO_STANDING
R087 | page 53 | line 3757 | NUMBER | 0.01 | [I1] stand note 20 other income: Gain on de-recognition of lease liability, 6M Sep 2025
R088 | page 53 | line 3758 | NUMBER | - | [I1] stand note 20 other income: Liabilities and provisions no longer required, qtr Sep 2026 | ZERO_STANDING
R089 | page 53 | line 3758 | NUMBER | - | [I1] stand note 20 other income: Liabilities and provisions no longer required, qtr Sep 2025 | ZERO_STANDING
R090 | page 53 | line 3758 | NUMBER | 15.38 | [I1] stand note 20 other income: Liabilities and provisions no longer required, 6M Sep 2026
R091 | page 53 | line 3758 | NUMBER | - | [I1] stand note 20 other income: Liabilities and provisions no longer required, 6M Sep 2025 | ZERO_STANDING
R092 | page 53 | line 3759 | NUMBER | (0.01) | [I1] stand note 20 other income: Net gain on disposal of property, plant and e, qtr Sep 2026
R093 | page 53 | line 3759 | NUMBER | 0.22 | [I1] stand note 20 other income: Net gain on disposal of property, plant and e, qtr Sep 2025
R094 | page 53 | line 3759 | NUMBER | 2.86 | [I1] stand note 20 other income: Net gain on disposal of property, plant and e, 6M Sep 2026
R095 | page 53 | line 3759 | NUMBER | 0.35 | [I1] stand note 20 other income: Net gain on disposal of property, plant and e, 6M Sep 2025
R096 | page 53 | line 3760 | NUMBER | 1.60 | [I1] stand note 20 other income: Miscellaneous income, qtr Sep 2026
R097 | page 53 | line 3760 | NUMBER | 2.15 | [I1] stand note 20 other income: Miscellaneous income, qtr Sep 2025
R098 | page 53 | line 3760 | NUMBER | 3.96 | [I1] stand note 20 other income: Miscellaneous income, 6M Sep 2026
R099 | page 53 | line 3760 | NUMBER | 4.08 | [I1] stand note 20 other income: Miscellaneous income, 6M Sep 2025
R100 | page 53 | line 3761 | NUMBER | (85.97) | [I1] stand note 20 other income: Total, qtr Sep 2026
R101 | page 53 | line 3761 | NUMBER | 79.29 | [I1] stand note 20 other income: Total, qtr Sep 2025
R102 | page 53 | line 3761 | NUMBER | 795.29 | [I1] stand note 20 other income: Total, 6M Sep 2026
R103 | page 53 | line 3761 | NUMBER | 923.69 | [I1] stand note 20 other income: Total, 6M Sep 2025
R104 | page 17 | line 1096 | NUMBER | 5,954 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R105 | page 17 | line 1096 | NUMBER | 311.50 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R106 | page 17 | line 1096 | NUMBER | 5,954 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R107 | page 17 | line 1096 | NUMBER | 311.50 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R108 | page 17 | line 1096 | NUMBER | INR 100 | [I2] face value per unit, Compulsory convertible preference shares of I
R109 | page 17 | line 1096 | NUMBER | INR 52,217.90 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R110 | page 17 | line 1097 | NUMBER | 1,13,126 | [I2] cons note 7 associates: Bonus shares received on above Compulsory con, units at 30 Sep 2026
R111 | page 17 | line 1097 | NUMBER | - | [I2] cons note 7 associates: Bonus shares received on above Compulsory con, amount at 30 Sep 2026 | ZERO_STANDING
R112 | page 17 | line 1097 | NUMBER | 1,13,126 | [I2] cons note 7 associates: Bonus shares received on above Compulsory con, units at 31 Mar 2026
R113 | page 17 | line 1097 | NUMBER | - | [I2] cons note 7 associates: Bonus shares received on above Compulsory con, amount at 31 Mar 2026 | ZERO_STANDING
R114 | page 17 | line 1098 | NUMBER | 10 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R115 | page 17 | line 1098 | NUMBER | 0.52 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R116 | page 17 | line 1098 | NUMBER | 10 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R117 | page 17 | line 1098 | NUMBER | 0.52 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R118 | page 17 | line 1098 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R119 | page 17 | line 1098 | NUMBER | INR 52,307.90 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R120 | page 17 | line 1099 | NUMBER | 190 | [I2] cons note 7 associates: Bonus shares received on above Equity shares, units at 30 Sep 2026
R121 | page 17 | line 1099 | NUMBER | - | [I2] cons note 7 associates: Bonus shares received on above Equity shares, amount at 30 Sep 2026 | ZERO_STANDING
R122 | page 17 | line 1099 | NUMBER | 190 | [I2] cons note 7 associates: Bonus shares received on above Equity shares, units at 31 Mar 2026
R123 | page 17 | line 1099 | NUMBER | - | [I2] cons note 7 associates: Bonus shares received on above Equity shares, amount at 31 Mar 2026 | ZERO_STANDING
R124 | page 17 | line 1097 | NUMBER | 1,809 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R125 | page 17 | line 1097 | NUMBER | 525.26 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R126 | page 17 | line 1097 | NUMBER | 1,809 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R127 | page 17 | line 1097 | NUMBER | 525.26 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R128 | page 17 | line 1097 | NUMBER | INR 100 | [I2] face value per unit, Compulsory convertible preference shares of I
R129 | page 17 | line 1097 | NUMBER | INR 2,90,261 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R130 | page 17 | line 1101 | NUMBER | 34,371 | [I2] cons note 7 associates: Bonus shares received on above Compulsory con, units at 30 Sep 2026
R131 | page 17 | line 1101 | NUMBER | - | [I2] cons note 7 associates: Bonus shares received on above Compulsory con, amount at 30 Sep 2026 | ZERO_STANDING
R132 | page 17 | line 1101 | NUMBER | 34,371 | [I2] cons note 7 associates: Bonus shares received on above Compulsory con, units at 31 Mar 2026
R133 | page 17 | line 1101 | NUMBER | - | [I2] cons note 7 associates: Bonus shares received on above Compulsory con, amount at 31 Mar 2026 | ZERO_STANDING
R134 | page 17 | line 1102 | NUMBER | 444 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R135 | page 17 | line 1102 | NUMBER | 90.24 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R136 | page 17 | line 1102 | NUMBER | 444 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R137 | page 17 | line 1102 | NUMBER | 90.24 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R138 | page 17 | line 1102 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R139 | page 17 | line 1102 | NUMBER | INR 2,03,242 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R140 | page 17 | line 1103 | NUMBER | 8,436 | [I2] cons note 7 associates: Bonus shares received on above Equity shares, units at 30 Sep 2026
R141 | page 17 | line 1103 | NUMBER | - | [I2] cons note 7 associates: Bonus shares received on above Equity shares, amount at 30 Sep 2026 | ZERO_STANDING
R142 | page 17 | line 1103 | NUMBER | 8,436 | [I2] cons note 7 associates: Bonus shares received on above Equity shares, units at 31 Mar 2026
R143 | page 17 | line 1103 | NUMBER | - | [I2] cons note 7 associates: Bonus shares received on above Equity shares, amount at 31 Mar 2026 | ZERO_STANDING
R144 | page 17 | line 1104 | NUMBER | 137 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R145 | page 17 | line 1104 | NUMBER | 39.78 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R146 | page 17 | line 1104 | NUMBER | 137 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R147 | page 17 | line 1104 | NUMBER | 39.78 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R148 | page 17 | line 1104 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R149 | page 17 | line 1104 | NUMBER | INR 2,90,351 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R150 | page 17 | line 1105 | NUMBER | 2,603 | [I2] cons note 7 associates: Bonus shares received on above Equity shares, units at 30 Sep 2026
R151 | page 17 | line 1105 | NUMBER | - | [I2] cons note 7 associates: Bonus shares received on above Equity shares, amount at 30 Sep 2026 | ZERO_STANDING
R152 | page 17 | line 1105 | NUMBER | 2,603 | [I2] cons note 7 associates: Bonus shares received on above Equity shares, units at 31 Mar 2026
R153 | page 17 | line 1105 | NUMBER | - | [I2] cons note 7 associates: Bonus shares received on above Equity shares, amount at 31 Mar 2026 | ZERO_STANDING
R154 | page 17 | line 1100 | NUMBER | 2,750 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R155 | page 17 | line 1100 | NUMBER | 57.45 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R156 | page 17 | line 1100 | NUMBER | 2,750 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R157 | page 17 | line 1100 | NUMBER | 57.45 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R158 | page 17 | line 1100 | NUMBER | INR 100 | [I2] face value per unit, Compulsory convertible preference shares of I
R159 | page 17 | line 1100 | NUMBER | INR 20,789.66 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R160 | page 17 | line 1101 | NUMBER | 2,814 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R161 | page 17 | line 1101 | NUMBER | 40.85 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R162 | page 17 | line 1101 | NUMBER | 2,814 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R163 | page 17 | line 1101 | NUMBER | 40.85 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R164 | page 17 | line 1101 | NUMBER | INR 100 | [I2] face value per unit, Compulsory convertible preference shares of I
R165 | page 17 | line 1101 | NUMBER | INR 14,417.80 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R166 | page 17 | line 1108 | NUMBER | 935 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R167 | page 17 | line 1108 | NUMBER | 13.57 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R168 | page 17 | line 1108 | NUMBER | 1,079.17 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, subtotal at 30 Sep 2026
R169 | page 17 | line 1108 | NUMBER | 935 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R170 | page 17 | line 1108 | NUMBER | 13.57 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R171 | page 17 | line 1108 | NUMBER | 1,079.17 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, subtotal at 31 Mar 2026
R172 | page 17 | line 1108 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R173 | page 17 | line 1108 | NUMBER | INR 14,507.80 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R174 | page 17 | line 1109 | NUMBER | (965.21) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 30 Sep 2026
R175 | page 17 | line 1109 | NUMBER | (862.73) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 31 Mar 2026
R176 | page 17 | line 1106 | NUMBER | 1,28,593 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R177 | page 17 | line 1106 | NUMBER | 99.92 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R178 | page 17 | line 1106 | NUMBER | 1,28,593 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R179 | page 17 | line 1106 | NUMBER | 99.92 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R180 | page 17 | line 1106 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R181 | page 17 | line 1106 | NUMBER | INR 776 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R182 | page 17 | line 1113 | NUMBER | 100 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R183 | page 17 | line 1113 | NUMBER | 0.07 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R184 | page 17 | line 1113 | NUMBER | 100 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R185 | page 17 | line 1113 | NUMBER | 0.07 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R186 | page 17 | line 1113 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R187 | page 17 | line 1113 | NUMBER | INR 776 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R188 | page 17 | line 1107 | NUMBER | 1,19,474 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R189 | page 17 | line 1107 | NUMBER | 100.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R190 | page 17 | line 1107 | NUMBER | 1,19,474 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R191 | page 17 | line 1107 | NUMBER | 100.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R192 | page 17 | line 1107 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R193 | page 17 | line 1107 | NUMBER | INR 836 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R194 | page 17 | line 1112 | NUMBER | 1,05,607 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R195 | page 17 | line 1112 | NUMBER | 129.20 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R196 | page 17 | line 1112 | NUMBER | 1,05,607 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R197 | page 17 | line 1112 | NUMBER | 129.20 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R198 | page 17 | line 1112 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R199 | page 17 | line 1112 | NUMBER | INR 1,222 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R200 | page 17 | line 1116 | NUMBER | 17,750 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R201 | page 17 | line 1116 | NUMBER | 14.86 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R202 | page 17 | line 1116 | NUMBER | 17,750 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R203 | page 17 | line 1116 | NUMBER | 14.86 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R204 | page 17 | line 1116 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R205 | page 17 | line 1116 | NUMBER | INR 837 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R206 | page 17 | line 1117 | NUMBER | 17,963 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R207 | page 17 | line 1117 | NUMBER | 21.98 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R208 | page 17 | line 1117 | NUMBER | 17,963 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R209 | page 17 | line 1117 | NUMBER | 21.98 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R210 | page 17 | line 1117 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R211 | page 17 | line 1117 | NUMBER | INR 1,222 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R212 | page 17 | line 1114 | NUMBER | 45,407 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R213 | page 17 | line 1114 | NUMBER | 80.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R214 | page 17 | line 1114 | NUMBER | 45,407 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R215 | page 17 | line 1114 | NUMBER | 80.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R216 | page 17 | line 1114 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R217 | page 17 | line 1114 | NUMBER | INR 1,760.83 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R218 | page 17 | line 1115 | NUMBER | 42,697 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R219 | page 17 | line 1115 | NUMBER | 80.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R220 | page 17 | line 1115 | NUMBER | 42,697 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R221 | page 17 | line 1115 | NUMBER | 80.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R222 | page 17 | line 1115 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R223 | page 17 | line 1115 | NUMBER | INR 1,872.68 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R224 | page 17 | line 1120 | NUMBER | 100 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R225 | page 17 | line 1120 | NUMBER | 0.16 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R226 | page 17 | line 1120 | NUMBER | 100 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R227 | page 17 | line 1120 | NUMBER | 0.16 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R228 | page 17 | line 1120 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R229 | page 17 | line 1120 | NUMBER | INR 1,552.74 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R230 | page 17 | line 1121 | NUMBER | 21,811 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R231 | page 17 | line 1121 | NUMBER | 51.30 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R232 | page 17 | line 1121 | NUMBER | 21,811 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R233 | page 17 | line 1121 | NUMBER | 51.30 | [I2] cons note 7 associates: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R234 | page 17 | line 1121 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R235 | page 17 | line 1121 | NUMBER | INR 2352 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R236 | page 17 | line 1118 | NUMBER | 91,804 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R237 | page 17 | line 1118 | NUMBER | 142.64 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R238 | page 17 | line 1118 | NUMBER | 720.13 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, subtotal at 30 Sep 2026
R239 | page 17 | line 1118 | NUMBER | 91,804 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R240 | page 17 | line 1118 | NUMBER | 142.64 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R241 | page 17 | line 1118 | NUMBER | 720.13 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, subtotal at 31 Mar 2026
R242 | page 17 | line 1118 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R243 | page 17 | line 1118 | NUMBER | INR 1552.74 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R244 | page 17 | line 1123 | NUMBER | 97.87 | [I2] cons note 7 associates: Fair value gain recognised through profit and, amount at 30 Sep 2026
R245 | page 17 | line 1123 | NUMBER | 97.87 | [I2] cons note 7 associates: Fair value gain recognised through profit and, amount at 31 Mar 2026
R246 | page 17 | line 1124 | NUMBER | (168.24) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 30 Sep 2026
R247 | page 17 | line 1124 | NUMBER | (132.97) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 31 Mar 2026
R248 | page 17 | line 1119 | NUMBER | 12,846 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R249 | page 17 | line 1119 | NUMBER | 96.05 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R250 | page 17 | line 1119 | NUMBER | 12,846 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R251 | page 17 | line 1119 | NUMBER | 96.05 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R252 | page 17 | line 1119 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R253 | page 17 | line 1119 | NUMBER | INR 7,467 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R254 | page 17 | line 1122 | NUMBER | 5,248 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R255 | page 17 | line 1122 | NUMBER | 75.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R256 | page 17 | line 1122 | NUMBER | 5,248 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R257 | page 17 | line 1122 | NUMBER | 75.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R258 | page 17 | line 1122 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R259 | page 17 | line 1122 | NUMBER | INR 14,282 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R260 | page 17 | line 1127 | NUMBER | 1,969 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R261 | page 17 | line 1127 | NUMBER | 30.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R262 | page 17 | line 1127 | NUMBER | 1,969 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R263 | page 17 | line 1127 | NUMBER | 30.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R264 | page 17 | line 1127 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R265 | page 17 | line 1127 | NUMBER | INR 15,226 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R266 | page 17 | line 1130 | NUMBER | 1,879 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R267 | page 17 | line 1130 | NUMBER | 14.05 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R268 | page 17 | line 1130 | NUMBER | 1,879 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R269 | page 17 | line 1130 | NUMBER | 14.05 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R270 | page 17 | line 1130 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R271 | page 17 | line 1130 | NUMBER | INR 7,467 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R272 | page 17 | line 1128 | NUMBER | 3,939 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R273 | page 17 | line 1128 | NUMBER | 60.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R274 | page 17 | line 1128 | NUMBER | 3,939 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R275 | page 17 | line 1128 | NUMBER | 60.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R276 | page 17 | line 1128 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R277 | page 17 | line 1128 | NUMBER | INR 15,222 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R278 | page 17 | line 1129 | NUMBER | 6,565 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R279 | page 17 | line 1129 | NUMBER | 100.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R280 | page 17 | line 1129 | NUMBER | 375.10 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, subtotal at 30 Sep 2026
R281 | page 17 | line 1129 | NUMBER | 6,565 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R282 | page 17 | line 1129 | NUMBER | 100.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R283 | page 17 | line 1129 | NUMBER | 375.10 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, subtotal at 31 Mar 2026
R284 | page 17 | line 1129 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R285 | page 17 | line 1129 | NUMBER | INR 15,222 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R286 | page 17 | line 1133 | NUMBER | (167.82) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 30 Sep 2026
R287 | page 17 | line 1133 | NUMBER | (148.83) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 31 Mar 2026
R288 | page 17 | line 1131 | NUMBER | 2,694 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R289 | page 17 | line 1131 | NUMBER | 162.50 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R290 | page 17 | line 1131 | NUMBER | 2,694 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R291 | page 17 | line 1131 | NUMBER | 162.50 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R292 | page 17 | line 1131 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R293 | page 17 | line 1131 | NUMBER | INR 60,311 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R294 | page 17 | line 1137 | NUMBER | 2,241 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R295 | page 17 | line 1137 | NUMBER | 97.50 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R296 | page 17 | line 1137 | NUMBER | 260.00 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, subtotal at 30 Sep 2026
R297 | page 17 | line 1137 | NUMBER | 2,241 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R298 | page 17 | line 1137 | NUMBER | 97.50 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R299 | page 17 | line 1137 | NUMBER | 260.00 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, subtotal at 31 Mar 2026
R300 | page 17 | line 1137 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R301 | page 17 | line 1137 | NUMBER | INR 43,497 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R302 | page 17 | line 1138 | NUMBER | (42.04) | [I2] cons note 7 associates: Less: Impairment allowance for investment in , amount at 30 Sep 2026
R303 | page 17 | line 1138 | NUMBER | (42.04) | [I2] cons note 7 associates: Less: Impairment allowance for investment in , amount at 31 Mar 2026
R304 | page 17 | line 1139 | NUMBER | (84.35) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 30 Sep 2026
R305 | page 17 | line 1139 | NUMBER | (64.23) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 31 Mar 2026
R306 | page 17 | line 1142 | NUMBER | 4,784 | [I2] cons note 7 associates: Compulsory Convertible Preference Shares of I, units at 30 Sep 2026
R307 | page 17 | line 1142 | NUMBER | 130.72 | [I2] cons note 7 associates: Compulsory Convertible Preference Shares of I, amount at 30 Sep 2026
R308 | page 17 | line 1142 | NUMBER | 4,784 | [I2] cons note 7 associates: Compulsory Convertible Preference Shares of I, units at 31 Mar 2026
R309 | page 17 | line 1142 | NUMBER | 130.72 | [I2] cons note 7 associates: Compulsory Convertible Preference Shares of I, amount at 31 Mar 2026
R310 | page 17 | line 1142 | NUMBER | INR 10 | [I2] face value per unit, Compulsory Convertible Preference Shares of I
R311 | page 17 | line 1142 | NUMBER | INR 27,314 | [I2] issue premium per unit, Compulsory Convertible Preference Shares of I
R312 | page 17 | line 1143 | NUMBER | 0.001% | [I2] stated in note text: 0.001% Compulsory Convertible Preference
R313 | page 17 | line 1143 | NUMBER | INR 10 | [I2] stated in note text: 0.001% Compulsory Convertible Preference
R314 | page 17 | line 1143 | NUMBER | INR 1,49,914 | [I2] stated in note text: 0.001% Compulsory Convertible Preference
R315 | page 17 | line 1144 | NUMBER | 333 | [I2] cons note 7 associates: emium of INR 1,49,914 each) (refer note (ii)), units at 30 Sep 2026
R316 | page 17 | line 1144 | NUMBER | 49.93 | [I2] cons note 7 associates: emium of INR 1,49,914 each) (refer note (ii)), amount at 30 Sep 2026
R317 | page 17 | line 1144 | NUMBER | - | [I2] cons note 7 associates: emium of INR 1,49,914 each) (refer note (ii)), units at 31 Mar 2026 | ZERO_STANDING
R318 | page 17 | line 1144 | NUMBER | - | [I2] cons note 7 associates: emium of INR 1,49,914 each) (refer note (ii)), amount at 31 Mar 2026 | ZERO_STANDING
R319 | page 17 | line 1145 | NUMBER | 100 | [I2] cons note 7 associates: Equity Shares of INR 10 each (at premium of I, units at 30 Sep 2026
R320 | page 17 | line 1145 | NUMBER | 2.73 | [I2] cons note 7 associates: Equity Shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R321 | page 17 | line 1145 | NUMBER | 183.38 | [I2] cons note 7 associates: Equity Shares of INR 10 each (at premium of I, subtotal at 30 Sep 2026
R322 | page 17 | line 1145 | NUMBER | 100 | [I2] cons note 7 associates: Equity Shares of INR 10 each (at premium of I, units at 31 Mar 2026
R323 | page 17 | line 1145 | NUMBER | 2.73 | [I2] cons note 7 associates: Equity Shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R324 | page 17 | line 1145 | NUMBER | 133.45 | [I2] cons note 7 associates: Equity Shares of INR 10 each (at premium of I, subtotal at 31 Mar 2026
R325 | page 17 | line 1145 | NUMBER | INR 10 | [I2] face value per unit, Equity Shares of INR 10 each (at premium of I
R326 | page 17 | line 1145 | NUMBER | INR 27,314 | [I2] issue premium per unit, Equity Shares of INR 10 each (at premium of I
R327 | page 17 | line 1146 | NUMBER | (52.19) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 30 Sep 2026
R328 | page 17 | line 1146 | NUMBER | (44.69) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 31 Mar 2026
R329 | page 17 | line 1149 | NUMBER | - | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026 | ZERO_STANDING
R330 | page 17 | line 1149 | NUMBER | - | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026 | ZERO_STANDING
R331 | page 17 | line 1149 | NUMBER | 8,11,250 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R332 | page 17 | line 1149 | NUMBER | 1,041.77 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R333 | page 17 | line 1149 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R334 | page 17 | line 1149 | NUMBER | INR 1,274.15 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R335 | page 17 | line 1150 | NUMBER | - | [I2] cons note 7 associates: Investment in Equity shares of INR 10 each (a, units at 30 Sep 2026 | ZERO_STANDING
R336 | page 17 | line 1150 | NUMBER | - | [I2] cons note 7 associates: Investment in Equity shares of INR 10 each (a, amount at 30 Sep 2026 | ZERO_STANDING
R337 | page 17 | line 1150 | NUMBER | - | [I2] cons note 7 associates: Investment in Equity shares of INR 10 each (a, subtotal at 30 Sep 2026 | ZERO_STANDING
R338 | page 17 | line 1150 | NUMBER | 1,06,876 | [I2] cons note 7 associates: Investment in Equity shares of INR 10 each (a, units at 31 Mar 2026
R339 | page 17 | line 1150 | NUMBER | 137.36 | [I2] cons note 7 associates: Investment in Equity shares of INR 10 each (a, amount at 31 Mar 2026
R340 | page 17 | line 1150 | NUMBER | 1,179.13 | [I2] cons note 7 associates: Investment in Equity shares of INR 10 each (a, subtotal at 31 Mar 2026
R341 | page 17 | line 1150 | NUMBER | INR 10 | [I2] face value per unit, Investment in Equity shares of INR 10 each (a
R342 | page 17 | line 1150 | NUMBER | INR 1,275.24 | [I2] issue premium per unit, Investment in Equity shares of INR 10 each (a
R343 | page 17 | line 1151 | NUMBER | - | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 30 Sep 2026 | ZERO_STANDING
R344 | page 17 | line 1151 | NUMBER | (503.62) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 31 Mar 2026
R345 | page 17 | line 1154 | NUMBER | 20 | [I2] cons note 7 associates: Equity shares of INR 1000 each (at premium of, units at 30 Sep 2026
R346 | page 17 | line 1154 | NUMBER | 20.60 | [I2] cons note 7 associates: Equity shares of INR 1000 each (at premium of, amount at 30 Sep 2026
R347 | page 17 | line 1154 | NUMBER | 20 | [I2] cons note 7 associates: Equity shares of INR 1000 each (at premium of, units at 31 Mar 2026
R348 | page 17 | line 1154 | NUMBER | 20.60 | [I2] cons note 7 associates: Equity shares of INR 1000 each (at premium of, amount at 31 Mar 2026
R349 | page 17 | line 1154 | NUMBER | INR 1000 | [I2] face value per unit, Equity shares of INR 1000 each (at premium of
R350 | page 17 | line 1154 | NUMBER | INR 10,28,411.76 | [I2] issue premium per unit, Equity shares of INR 1000 each (at premium of
R351 | page 17 | line 1143 | NUMBER | 7,950 | [I2] cons note 7 associates: Compulsory Convertible Preference shares of I, units at 30 Sep 2026
R352 | page 17 | line 1143 | NUMBER | 116.90 | [I2] cons note 7 associates: Compulsory Convertible Preference shares of I, amount at 30 Sep 2026
R353 | page 17 | line 1143 | NUMBER | 137.50 | [I2] cons note 7 associates: Compulsory Convertible Preference shares of I, subtotal at 30 Sep 2026
R354 | page 17 | line 1143 | NUMBER | 7,950 | [I2] cons note 7 associates: Compulsory Convertible Preference shares of I, units at 31 Mar 2026
R355 | page 17 | line 1143 | NUMBER | 116.90 | [I2] cons note 7 associates: Compulsory Convertible Preference shares of I, amount at 31 Mar 2026
R356 | page 17 | line 1143 | NUMBER | 137.50 | [I2] cons note 7 associates: Compulsory Convertible Preference shares of I, subtotal at 31 Mar 2026
R357 | page 17 | line 1143 | NUMBER | INR 10 | [I2] face value per unit, Compulsory Convertible Preference shares of I
R358 | page 17 | line 1143 | NUMBER | INR 14,696 | [I2] issue premium per unit, Compulsory Convertible Preference shares of I
R359 | page 17 | line 1156 | NUMBER | (30.72) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 30 Sep 2026
R360 | page 17 | line 1156 | NUMBER | (26.67) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 31 Mar 2026
R361 | page 17 | line 1132 | NUMBER | 10,323 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R362 | page 17 | line 1132 | NUMBER | 696.08 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R363 | page 17 | line 1132 | NUMBER | 10,323 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R364 | page 17 | line 1132 | NUMBER | 696.08 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R365 | page 17 | line 1132 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R366 | page 17 | line 1132 | NUMBER | INR 67,420 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R367 | page 17 | line 1150 | NUMBER | 3,805 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R368 | page 17 | line 1150 | NUMBER | 218.12 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R369 | page 17 | line 1150 | NUMBER | 3,805 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R370 | page 17 | line 1150 | NUMBER | 218.12 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R371 | page 17 | line 1150 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R372 | page 17 | line 1150 | NUMBER | INR 57,315 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R373 | page 17 | line 1136 | NUMBER | 2,226 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R374 | page 17 | line 1136 | NUMBER | 208.30 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R375 | page 17 | line 1136 | NUMBER | 2,226 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R376 | page 17 | line 1136 | NUMBER | 208.30 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R377 | page 17 | line 1136 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R378 | page 17 | line 1136 | NUMBER | INR 93,565 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R379 | page 17 | line 1160 | NUMBER | 808 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R380 | page 17 | line 1160 | NUMBER | 75.61 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R381 | page 17 | line 1160 | NUMBER | 808 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R382 | page 17 | line 1160 | NUMBER | 75.61 | [I2] cons note 7 associates: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R383 | page 17 | line 1160 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R384 | page 17 | line 1160 | NUMBER | INR 93,565 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R385 | page 17 | line 1159 | NUMBER | 2,921 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 30 Sep 2026
R386 | page 17 | line 1159 | NUMBER | 410.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R387 | page 17 | line 1159 | NUMBER | 2,921 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, units at 31 Mar 2026
R388 | page 17 | line 1159 | NUMBER | 410.00 | [I2] cons note 7 associates: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R389 | page 17 | line 1159 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R390 | page 17 | line 1159 | NUMBER | INR 140,352 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R391 | page 17 | line 1161 | NUMBER | INR 10 | [I2] stated in note text: Compulsory convertible preference shares
R392 | page 17 | line 1161 | NUMBER | INR 140,352 | [I2] stated in note text: Compulsory convertible preference shares
R393 | page 17 | line 1165 | NUMBER | 4,630 | [I2] cons note 7 associates: emium of INR 140,352/- each) (refer note (i)), units at 30 Sep 2026
R394 | page 17 | line 1165 | NUMBER | 649.88 | [I2] cons note 7 associates: emium of INR 140,352/- each) (refer note (i)), amount at 30 Sep 2026
R395 | page 17 | line 1165 | NUMBER | - | [I2] cons note 7 associates: emium of INR 140,352/- each) (refer note (i)), units at 31 Mar 2026 | ZERO_STANDING
R396 | page 17 | line 1165 | NUMBER | - | [I2] cons note 7 associates: emium of INR 140,352/- each) (refer note (i)), amount at 31 Mar 2026 | ZERO_STANDING
R397 | page 17 | line 1166 | NUMBER | - | [I2] cons note 7 associates: Fair value gain recognised through profit and, units at 30 Sep 2026 | ZERO_STANDING
R398 | page 17 | line 1166 | NUMBER | (68.99) | [I2] cons note 7 associates: Fair value gain recognised through profit and, amount at 30 Sep 2026
R399 | page 17 | line 1166 | NUMBER | 2,189.00 | [I2] cons note 7 associates: Fair value gain recognised through profit and, subtotal at 30 Sep 2026
R400 | page 17 | line 1166 | NUMBER | - | [I2] cons note 7 associates: Fair value gain recognised through profit and, units at 31 Mar 2026 | ZERO_STANDING
R401 | page 17 | line 1166 | NUMBER | (68.99) | [I2] cons note 7 associates: Fair value gain recognised through profit and, amount at 31 Mar 2026
R402 | page 17 | line 1166 | NUMBER | 1,539.12 | [I2] cons note 7 associates: Fair value gain recognised through profit and, subtotal at 31 Mar 2026
R403 | page 17 | line 1167 | NUMBER | (238.48) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 30 Sep 2026
R404 | page 17 | line 1167 | NUMBER | (145.45) | [I2] cons note 7 associates: Less: Share of loss of associate, amount at 31 Mar 2026
R405 | page 17 | line 1169 | NUMBER | 172.47 | [I2] cons note 7 associates: Advance pending share transfer (refer note (i, amount at 30 Sep 2026
R406 | page 17 | line 1169 | NUMBER | - | [I2] cons note 7 associates: Advance pending share transfer (refer note (i, amount at 31 Mar 2026 | ZERO_STANDING
R407 | page 17 | line 1169 | NUMBER | 3,465.57 | [I2] cons note 7 associates: nding share transfer (refer note (iii) below), amount at 30 Sep 2026
R408 | page 17 | line 1169 | NUMBER | 3,550.24 | [I2] cons note 7 associates: nding share transfer (refer note (iii) below), amount at 31 Mar 2026
R409 | page 17 | line 1174 | NUMBER | 649.88 | [I2] stated in note text: (i) During the period the Group had inve
R410 | page 17 | line 1174 | NUMBER | INR 10 | [I2] stated in note text: (i) During the period the Group had inve
R411 | page 17 | line 1174 | NUMBER | INR 140,352 | [I2] stated in note text: (i) During the period the Group had inve
R412 | page 17 | line 1178 | NUMBER | INR 10 | [I2] stated in note text: Value INR 10/- each at a premium of INR 
R413 | page 17 | line 1178 | NUMBER | INR 149,914 | [I2] stated in note text: Value INR 10/- each at a premium of INR 
R414 | page 17 | line 1178 | NUMBER | INR 49.93 | [I2] stated in note text: Value INR 10/- each at a premium of INR 
R415 | page 17 | line 1180 | NUMBER | INR 172.47 | [I2] stated in note text: (iii) During the period the Group has gi
R416 | page 17 | line 1181 | NUMBER | 26.94% | [I2] stated in note text: Group thereby increasing its equity owne
R417 | page 17 | line 1183 | NUMBER | INR 71.49 | [I2] stated in note text: (iv) During the period ended 30 Septembe
R418 | page 18 | line 1197 | NUMBER | 4,615.38 | [I2] cons note 8a non-current inv: i) Investment in other entities at FVTPL, amount at 30 Sep 2026
R419 | page 18 | line 1197 | NUMBER | 4,029.05 | [I2] cons note 8a non-current inv: i) Investment in other entities at FVTPL, amount at 31 Mar 2026
R420 | page 18 | line 1198 | NUMBER | - | [I2] cons note 8a non-current inv: ii) Investment in debt instruments of associa, amount at 30 Sep 2026 | ZERO_STANDING
R421 | page 18 | line 1198 | NUMBER | 50.00 | [I2] cons note 8a non-current inv: ii) Investment in debt instruments of associa, amount at 31 Mar 2026
R422 | page 18 | line 1265 | NUMBER | 4,615.38 | [I2] cons note 8a non-current inv: nt in debt instruments of associates at FVTPL, amount at 30 Sep 2026
R423 | page 18 | line 1265 | NUMBER | 4,079.05 | [I2] cons note 8a non-current inv: nt in debt instruments of associates at FVTPL, amount at 31 Mar 2026
R424 | page 18 | line 1201 | NUMBER | 19,298.81 | [I2] cons note 8a non-current inv: Investment in mutual funds and exchange trade, amount at 30 Sep 2026
R425 | page 18 | line 1201 | NUMBER | 20,845.16 | [I2] cons note 8a non-current inv: Investment in mutual funds and exchange trade, amount at 31 Mar 2026
R426 | page 18 | line 1202 | NUMBER | 7,070.13 | [I2] cons note 8a non-current inv: Investment in bonds and debentures at FVTPL, amount at 30 Sep 2026
R427 | page 18 | line 1202 | NUMBER | 5,974.53 | [I2] cons note 8a non-current inv: Investment in bonds and debentures at FVTPL, amount at 31 Mar 2026
R428 | page 18 | line 1203 | NUMBER | 3,626.13 | [I2] cons note 8a non-current inv: Investment in Government Securities- Quoted (, amount at 30 Sep 2026
R429 | page 18 | line 1203 | NUMBER | 3,474.36 | [I2] cons note 8a non-current inv: Investment in Government Securities- Quoted (, amount at 31 Mar 2026
R430 | page 18 | line 1204 | NUMBER | 91.99 | [I2] cons note 8a non-current inv: Invesment in TREPS (measured at amortised cos, amount at 30 Sep 2026
R431 | page 18 | line 1204 | NUMBER | - | [I2] cons note 8a non-current inv: Invesment in TREPS (measured at amortised cos, amount at 31 Mar 2026 | ZERO_STANDING
R432 | page 18 | line 1204 | NUMBER | 30,087.06 | [I2] cons note 8a non-current inv: vesment in TREPS (measured at amortised cost), amount at 30 Sep 2026
R433 | page 18 | line 1204 | NUMBER | 30,294.05 | [I2] cons note 8a non-current inv: vesment in TREPS (measured at amortised cost), amount at 31 Mar 2026
R434 | page 18 | line 1214 | NUMBER | 10 | [I2] cons note 8a non-current inv: Equity shares held of INR 10 each (at premium, units at 30 Sep 2026
R435 | page 18 | line 1214 | NUMBER | - | [I2] cons note 8a non-current inv: Equity shares held of INR 10 each (at premium, amount at 30 Sep 2026 | ZERO_STANDING
R436 | page 18 | line 1214 | NUMBER | 10 | [I2] cons note 8a non-current inv: Equity shares held of INR 10 each (at premium, units at 31 Mar 2026
R437 | page 18 | line 1214 | NUMBER | - | [I2] cons note 8a non-current inv: Equity shares held of INR 10 each (at premium, amount at 31 Mar 2026 | ZERO_STANDING
R438 | page 18 | line 1214 | NUMBER | INR 899 | [I2] issue premium per unit, Equity shares held of INR 10 each (at premium
R439 | page 18 | line 1215 | NUMBER | 16,200 | [I2] cons note 8a non-current inv: 0.001% Compulsorily convertible preference sh, units at 30 Sep 2026
R440 | page 18 | line 1215 | NUMBER | 13.50 | [I2] cons note 8a non-current inv: 0.001% Compulsorily convertible preference sh, amount at 30 Sep 2026
R441 | page 18 | line 1215 | NUMBER | 16,200 | [I2] cons note 8a non-current inv: 0.001% Compulsorily convertible preference sh, units at 31 Mar 2026
R442 | page 18 | line 1215 | NUMBER | 13.50 | [I2] cons note 8a non-current inv: 0.001% Compulsorily convertible preference sh, amount at 31 Mar 2026
R443 | page 18 | line 1215 | NUMBER | 0.001% | [I2] instrument coupon, 0.001% Compulsorily convertible preference sh
R444 | page 18 | line 1216 | NUMBER | 717.46 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, amount at 30 Sep 2026
R445 | page 18 | line 1216 | NUMBER | 730.96 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, carrying total at 30 Sep 2026
R446 | page 18 | line 1216 | NUMBER | 717.46 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, amount at 31 Mar 2026
R447 | page 18 | line 1216 | NUMBER | 730.96 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, carrying total at 31 Mar 2026
R448 | page 18 | line 1219 | NUMBER | 1,146 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 30 Sep 2026
R449 | page 18 | line 1219 | NUMBER | 5.89 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R450 | page 18 | line 1219 | NUMBER | 1,146 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 31 Mar 2026
R451 | page 18 | line 1219 | NUMBER | 5.89 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R452 | page 18 | line 1219 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R453 | page 18 | line 1219 | NUMBER | INR 5,132.68 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R454 | page 18 | line 1220 | NUMBER | 1,580 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 30 Sep 2026
R455 | page 18 | line 1220 | NUMBER | 6.50 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R456 | page 18 | line 1220 | NUMBER | 1,580 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 31 Mar 2026
R457 | page 18 | line 1220 | NUMBER | 6.50 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R458 | page 18 | line 1220 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R459 | page 18 | line 1220 | NUMBER | INR 4,104.14 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R460 | page 18 | line 1221 | NUMBER | 1,290 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 30 Sep 2026
R461 | page 18 | line 1221 | NUMBER | 75.00 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R462 | page 18 | line 1221 | NUMBER | 1,290 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 31 Mar 2026
R463 | page 18 | line 1221 | NUMBER | 75.00 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R464 | page 18 | line 1221 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R465 | page 18 | line 1221 | NUMBER | INR 58,120.00 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R466 | page 18 | line 1222 | NUMBER | 100 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R467 | page 18 | line 1222 | NUMBER | 0.51 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R468 | page 18 | line 1222 | NUMBER | 100 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R469 | page 18 | line 1222 | NUMBER | 0.51 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R470 | page 18 | line 1222 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R471 | page 18 | line 1222 | NUMBER | INR 5,132.68 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R472 | page 18 | line 1223 | NUMBER | (33.00) | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, amount at 30 Sep 2026
R473 | page 18 | line 1223 | NUMBER | 54.90 | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, carrying total at 30 Sep 2026
R474 | page 18 | line 1223 | NUMBER | (33.00) | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, amount at 31 Mar 2026
R475 | page 18 | line 1223 | NUMBER | 54.90 | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, carrying total at 31 Mar 2026
R476 | page 18 | line 1227 | NUMBER | 24,74,637 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R477 | page 18 | line 1227 | NUMBER | 240.56 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R478 | page 18 | line 1227 | NUMBER | 24,74,637 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R479 | page 18 | line 1227 | NUMBER | 240.56 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R480 | page 18 | line 1227 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R481 | page 18 | line 1227 | NUMBER | INR 87.21 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R482 | page 18 | line 1228 | NUMBER | 1,80,000 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R483 | page 18 | line 1228 | NUMBER | 22.95 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R484 | page 18 | line 1228 | NUMBER | 1,80,000 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R485 | page 18 | line 1228 | NUMBER | 22.95 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R486 | page 18 | line 1228 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R487 | page 18 | line 1228 | NUMBER | INR 117.46 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R488 | page 18 | line 1229 | NUMBER | 55,526 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R489 | page 18 | line 1229 | NUMBER | 25.64 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R490 | page 18 | line 1229 | NUMBER | 55,526 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R491 | page 18 | line 1229 | NUMBER | 25.64 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R492 | page 18 | line 1229 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R493 | page 18 | line 1229 | NUMBER | INR 451.8 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R494 | page 18 | line 1230 | NUMBER | 15,10,656 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 30 Sep 2026
R495 | page 18 | line 1230 | NUMBER | 240.68 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R496 | page 18 | line 1230 | NUMBER | 15,10,656 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 31 Mar 2026
R497 | page 18 | line 1230 | NUMBER | 240.68 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R498 | page 18 | line 1230 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R499 | page 18 | line 1230 | NUMBER | INR 149.32 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R500 | page 18 | line 1231 | NUMBER | 689.97 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, amount at 30 Sep 2026
R501 | page 18 | line 1231 | NUMBER | 1,219.80 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, carrying total at 30 Sep 2026
R502 | page 18 | line 1231 | NUMBER | 689.97 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, amount at 31 Mar 2026
R503 | page 18 | line 1231 | NUMBER | 1,219.80 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, carrying total at 31 Mar 2026
R504 | page 18 | line 1235 | NUMBER | 1,870 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 30 Sep 2026
R505 | page 18 | line 1235 | NUMBER | 161.41 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R506 | page 18 | line 1235 | NUMBER | 1,870 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 31 Mar 2026
R507 | page 18 | line 1235 | NUMBER | 161.41 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R508 | page 18 | line 1235 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R509 | page 18 | line 1235 | NUMBER | INR 86,306.32 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R510 | page 18 | line 1237 | NUMBER | 100 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R511 | page 18 | line 1237 | NUMBER | 8.63 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R512 | page 18 | line 1237 | NUMBER | 100 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R513 | page 18 | line 1237 | NUMBER | 8.63 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R514 | page 18 | line 1237 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R515 | page 18 | line 1237 | NUMBER | INR 86,306.32 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R516 | page 18 | line 1238 | NUMBER | (95.56) | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, amount at 30 Sep 2026
R517 | page 18 | line 1238 | NUMBER | 74.48 | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, carrying total at 30 Sep 2026
R518 | page 18 | line 1238 | NUMBER | (95.56) | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, amount at 31 Mar 2026
R519 | page 18 | line 1238 | NUMBER | 74.48 | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, carrying total at 31 Mar 2026
R520 | page 18 | line 1241 | NUMBER | 6,95,922 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R521 | page 18 | line 1241 | NUMBER | 252.78 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R522 | page 18 | line 1241 | NUMBER | 6,95,922 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R523 | page 18 | line 1241 | NUMBER | 252.78 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R524 | page 18 | line 1241 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R525 | page 18 | line 1241 | NUMBER | INR 362.22 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R526 | page 18 | line 1242 | NUMBER | 3,54,619 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 30 Sep 2026
R527 | page 18 | line 1242 | NUMBER | 644.02 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R528 | page 18 | line 1242 | NUMBER | 3,54,619 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 31 Mar 2026
R529 | page 18 | line 1242 | NUMBER | 644.02 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R530 | page 18 | line 1242 | NUMBER | INR 5 | [I2] face value per unit, Compulsory convertible preference shares of I
R531 | page 18 | line 1242 | NUMBER | INR 1,811.10 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R532 | page 18 | line 1243 | NUMBER | 400 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 30 Sep 2026
R533 | page 18 | line 1243 | NUMBER | 0.15 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R534 | page 18 | line 1243 | NUMBER | 400 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, units at 31 Mar 2026
R535 | page 18 | line 1243 | NUMBER | 0.15 | [I2] cons note 8a non-current inv: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R536 | page 18 | line 1243 | NUMBER | INR 5 | [I2] face value per unit, Compulsory convertible preference shares of I
R537 | page 18 | line 1243 | NUMBER | INR 358.22 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R538 | page 18 | line 1244 | NUMBER | 1,995 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R539 | page 18 | line 1244 | NUMBER | 1.39 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R540 | page 18 | line 1244 | NUMBER | 1,995 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R541 | page 18 | line 1244 | NUMBER | 1.39 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R542 | page 18 | line 1244 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R543 | page 18 | line 1244 | NUMBER | INR 695.72 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R544 | page 18 | line 1245 | NUMBER | 17,647 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R545 | page 18 | line 1245 | NUMBER | 10.13 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R546 | page 18 | line 1245 | NUMBER | 17,647 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R547 | page 18 | line 1245 | NUMBER | 10.13 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R548 | page 18 | line 1245 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R549 | page 18 | line 1245 | NUMBER | INR 572.80 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R550 | page 18 | line 1246 | NUMBER | 14,414 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R551 | page 18 | line 1246 | NUMBER | 10.93 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R552 | page 18 | line 1246 | NUMBER | 14,414 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R553 | page 18 | line 1246 | NUMBER | 10.93 | [I2] cons note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R554 | page 18 | line 1246 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R555 | page 18 | line 1246 | NUMBER | INR 757.19 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R556 | page 18 | line 1247 | NUMBER | 35,840 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, units at 30 Sep 2026
R557 | page 18 | line 1247 | NUMBER | 124.85 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 30 Sep 2026
R558 | page 18 | line 1247 | NUMBER | 35,840 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, units at 31 Mar 2026
R559 | page 18 | line 1247 | NUMBER | 124.85 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 31 Mar 2026
R560 | page 18 | line 1247 | NUMBER | INR 5 | [I2] face value per unit, Compulsory convertible Preference shares of I
R561 | page 18 | line 1247 | NUMBER | INR 3,478.60 | [I2] issue premium per unit, Compulsory convertible Preference shares of I
R562 | page 18 | line 1248 | NUMBER | 2,186 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, units at 30 Sep 2026
R563 | page 18 | line 1248 | NUMBER | 1.52 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 30 Sep 2026
R564 | page 18 | line 1248 | NUMBER | 2,186 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, units at 31 Mar 2026
R565 | page 18 | line 1248 | NUMBER | 1.52 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 31 Mar 2026
R566 | page 18 | line 1248 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible Preference shares of I
R567 | page 18 | line 1248 | NUMBER | INR 686.72 | [I2] issue premium per unit, Compulsory convertible Preference shares of I
R568 | page 18 | line 1249 | NUMBER | 415 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, units at 30 Sep 2026
R569 | page 18 | line 1249 | NUMBER | 1.57 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 30 Sep 2026
R570 | page 18 | line 1249 | NUMBER | 415 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, units at 31 Mar 2026
R571 | page 18 | line 1249 | NUMBER | 1.57 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 31 Mar 2026
R572 | page 18 | line 1249 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible Preference shares of I
R573 | page 18 | line 1249 | NUMBER | INR 3,789.95 | [I2] issue premium per unit, Compulsory convertible Preference shares of I
R574 | page 18 | line 1250 | NUMBER | 86,548 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, units at 30 Sep 2026
R575 | page 18 | line 1250 | NUMBER | 78.04 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 30 Sep 2026
R576 | page 18 | line 1250 | NUMBER | 86548 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, units at 31 Mar 2026
R577 | page 18 | line 1250 | NUMBER | 78.04 | [I2] cons note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 31 Mar 2026
R578 | page 18 | line 1250 | NUMBER | INR 5 | [I2] face value per unit, Compulsory convertible Preference shares of I
R579 | page 18 | line 1250 | NUMBER | INR 896.70 | [I2] issue premium per unit, Compulsory convertible Preference shares of I
R580 | page 18 | line 1251 | NUMBER | 823.53 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, amount at 30 Sep 2026
R581 | page 18 | line 1251 | NUMBER | 1,948.91 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, carrying total at 30 Sep 2026
R582 | page 18 | line 1251 | NUMBER | 823.53 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, amount at 31 Mar 2026
R583 | page 18 | line 1251 | NUMBER | 1,948.91 | [I2] cons note 8a non-current inv: Fair value gain recognised through profit and, carrying total at 31 Mar 2026
R584 | page 18 | line 1256 | NUMBER | 8,11,250 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R585 | page 18 | line 1256 | NUMBER | 1,041.77 | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R586 | page 18 | line 1256 | NUMBER | - | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026 | ZERO_STANDING
R587 | page 18 | line 1256 | NUMBER | - | [I2] cons note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026 | ZERO_STANDING
R588 | page 18 | line 1256 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R589 | page 18 | line 1256 | NUMBER | INR 1,274.15 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R590 | page 18 | line 1257 | NUMBER | 1,06,876 | [I2] cons note 8a non-current inv: Investment in Equity shares of INR 10 each (a, units at 30 Sep 2026
R591 | page 18 | line 1257 | NUMBER | 137.36 | [I2] cons note 8a non-current inv: Investment in Equity shares of INR 10 each (a, amount at 30 Sep 2026
R592 | page 18 | line 1257 | NUMBER | - | [I2] cons note 8a non-current inv: Investment in Equity shares of INR 10 each (a, units at 31 Mar 2026 | ZERO_STANDING
R593 | page 18 | line 1257 | NUMBER | - | [I2] cons note 8a non-current inv: Investment in Equity shares of INR 10 each (a, amount at 31 Mar 2026 | ZERO_STANDING
R594 | page 18 | line 1257 | NUMBER | INR 10 | [I2] face value per unit, Investment in Equity shares of INR 10 each (a
R595 | page 18 | line 1257 | NUMBER | INR 1,275.24 | [I2] issue premium per unit, Investment in Equity shares of INR 10 each (a
R596 | page 18 | line 1258 | NUMBER | (521.31) | [I2] cons note 8a non-current inv: Less: Share of loss of associate till the dat, amount at 30 Sep 2026
R597 | page 18 | line 1258 | NUMBER | - | [I2] cons note 8a non-current inv: Less: Share of loss of associate till the dat, amount at 31 Mar 2026 | ZERO_STANDING
R598 | page 18 | line 1259 | NUMBER | (71.49) | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, amount at 30 Sep 2026
R599 | page 18 | line 1259 | NUMBER | 586.33 | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, carrying total at 30 Sep 2026
R600 | page 18 | line 1259 | NUMBER | - | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, amount at 31 Mar 2026 | ZERO_STANDING
R601 | page 18 | line 1259 | NUMBER | - | [I2] cons note 8a non-current inv: Fair value loss recognised through profit and, carrying total at 31 Mar 2026 | ZERO_STANDING
R602 | page 18 | line 1223 | NUMBER | 4,615.38 | [I2] cons note 8a non-current inv: value loss recognised through profit and loss, amount at 30 Sep 2026
R603 | page 18 | line 1223 | NUMBER | 4,029.05 | [I2] cons note 8a non-current inv: value loss recognised through profit and loss, amount at 31 Mar 2026
R604 | page 18 | line 1270 | NUMBER | INR 1000 | [I2] stated in note text: Investment in Compulsory convertible deb
R605 | page 18 | line 1274 | NUMBER | 50,000 | [I2] cons note 8a non-current inv: Opening, units at 30 Sep 2026
R606 | page 18 | line 1274 | NUMBER | 50.00 | [I2] cons note 8a non-current inv: Opening, amount at 30 Sep 2026
R607 | page 18 | line 1274 | NUMBER | - | [I2] cons note 8a non-current inv: Opening, units at 31 Mar 2026 | ZERO_STANDING
R608 | page 18 | line 1274 | NUMBER | - | [I2] cons note 8a non-current inv: Opening, amount at 31 Mar 2026 | ZERO_STANDING
R609 | page 18 | line 1276 | NUMBER | - | [I2] cons note 8a non-current inv: Addition during the year, units at 30 Sep 2026 | ZERO_STANDING
R610 | page 18 | line 1276 | NUMBER | - | [I2] cons note 8a non-current inv: Addition during the year, amount at 30 Sep 2026 | ZERO_STANDING
R611 | page 18 | line 1276 | NUMBER | 50000 | [I2] cons note 8a non-current inv: Addition during the year, units at 31 Mar 2026
R612 | page 18 | line 1276 | NUMBER | 50.00 | [I2] cons note 8a non-current inv: Addition during the year, amount at 31 Mar 2026
R613 | page 18 | line 1278 | NUMBER | (50,000) | [I2] cons note 8a non-current inv: Conversion during the period (refer note 7(ii, units at 30 Sep 2026
R614 | page 18 | line 1278 | NUMBER | (50.00) | [I2] cons note 8a non-current inv: Conversion during the period (refer note 7(ii, amount at 30 Sep 2026
R615 | page 18 | line 1278 | NUMBER | - | [I2] cons note 8a non-current inv: Conversion during the period (refer note 7(ii, subtotal at 30 Sep 2026 | ZERO_STANDING
R616 | page 18 | line 1278 | NUMBER | - | [I2] cons note 8a non-current inv: Conversion during the period (refer note 7(ii, units at 31 Mar 2026 | ZERO_STANDING
R617 | page 18 | line 1278 | NUMBER | - | [I2] cons note 8a non-current inv: Conversion during the period (refer note 7(ii, amount at 31 Mar 2026 | ZERO_STANDING
R618 | page 18 | line 1278 | NUMBER | 50.00 | [I2] cons note 8a non-current inv: Conversion during the period (refer note 7(ii, subtotal at 31 Mar 2026
R619 | page 18 | line 1280 | NUMBER | 4,615.38 | [I2] cons note 8a non-current inv: Total non-current investments (i+ii), amount at 30 Sep 2026
R620 | page 18 | line 1280 | NUMBER | 4,079.05 | [I2] cons note 8a non-current inv: Total non-current investments (i+ii), amount at 31 Mar 2026
R621 | page 19 | line 1299 | NUMBER | - | [I2] cons note 8b current inv: Aditya Birla Sun Life Arbitrage Fund, units at 30 Sep 2026 | ZERO_STANDING
R622 | page 19 | line 1299 | NUMBER | - | [I2] cons note 8b current inv: Aditya Birla Sun Life Arbitrage Fund, amount at 30 Sep 2026 | ZERO_STANDING
R623 | page 19 | line 1299 | NUMBER | 1,69,00,751 | [I2] cons note 8b current inv: Aditya Birla Sun Life Arbitrage Fund, units at 31 Mar 2026
R624 | page 19 | line 1299 | NUMBER | 507.83 | [I2] cons note 8b current inv: Aditya Birla Sun Life Arbitrage Fund, amount at 31 Mar 2026
R625 | page 19 | line 1300 | NUMBER | 1,23,62,268 | [I2] cons note 8b current inv: Aditya Birla Sun Life Corporate Bond Fund, units at 30 Sep 2026
R626 | page 19 | line 1300 | NUMBER | 1,501.85 | [I2] cons note 8b current inv: Aditya Birla Sun Life Corporate Bond Fund, amount at 30 Sep 2026
R627 | page 19 | line 1300 | NUMBER | 1,23,62,268 | [I2] cons note 8b current inv: Aditya Birla Sun Life Corporate Bond Fund, units at 31 Mar 2026
R628 | page 19 | line 1300 | NUMBER | 1,457.83 | [I2] cons note 8b current inv: Aditya Birla Sun Life Corporate Bond Fund, amount at 31 Mar 2026
R629 | page 19 | line 1301 | NUMBER | 4,40,73,459 | [I2] cons note 8b current inv: Aditya Birla Sun Life Nifty SDL Apr 2027 Inde, units at 30 Sep 2026
R630 | page 19 | line 1301 | NUMBER | 589.24 | [I2] cons note 8b current inv: Aditya Birla Sun Life Nifty SDL Apr 2027 Inde, amount at 30 Sep 2026
R631 | page 19 | line 1301 | NUMBER | 4,40,73,459 | [I2] cons note 8b current inv: Aditya Birla Sun Life Nifty SDL Apr 2027 Inde, units at 31 Mar 2026
R632 | page 19 | line 1301 | NUMBER | 573.08 | [I2] cons note 8b current inv: Aditya Birla Sun Life Nifty SDL Apr 2027 Inde, amount at 31 Mar 2026
R633 | page 19 | line 1302 | NUMBER | 87,77,620 | [I2] cons note 8b current inv: Axis Corporate Bond Fund, units at 30 Sep 2026
R634 | page 19 | line 1302 | NUMBER | 170.01 | [I2] cons note 8b current inv: Axis Corporate Bond Fund, amount at 30 Sep 2026
R635 | page 19 | line 1302 | NUMBER | 87,77,620 | [I2] cons note 8b current inv: Axis Corporate Bond Fund, units at 31 Mar 2026
R636 | page 19 | line 1302 | NUMBER | 164.64 | [I2] cons note 8b current inv: Axis Corporate Bond Fund, amount at 31 Mar 2026
R637 | page 19 | line 1303 | NUMBER | - | [I2] cons note 8b current inv: Axis Liquid Fund, units at 30 Sep 2026 | ZERO_STANDING
R638 | page 19 | line 1303 | NUMBER | - | [I2] cons note 8b current inv: Axis Liquid Fund, amount at 30 Sep 2026 | ZERO_STANDING
R639 | page 19 | line 1303 | NUMBER | 22,871 | [I2] cons note 8b current inv: Axis Liquid Fund, units at 31 Mar 2026
R640 | page 19 | line 1303 | NUMBER | 70.09 | [I2] cons note 8b current inv: Axis Liquid Fund, amount at 31 Mar 2026
R641 | page 19 | line 1304 | NUMBER | - | [I2] cons note 8b current inv: Axis Money Market Fund, units at 30 Sep 2026 | ZERO_STANDING
R642 | page 19 | line 1304 | NUMBER | - | [I2] cons note 8b current inv: Axis Money Market Fund, amount at 30 Sep 2026 | ZERO_STANDING
R643 | page 19 | line 1304 | NUMBER | 4,733 | [I2] cons note 8b current inv: Axis Money Market Fund, units at 31 Mar 2026
R644 | page 19 | line 1304 | NUMBER | 7.16 | [I2] cons note 8b current inv: Axis Money Market Fund, amount at 31 Mar 2026
R645 | page 19 | line 1305 | NUMBER | 18,909 | [I2] cons note 8b current inv: Bajaj Finserve Liquid Fund, units at 30 Sep 2026
R646 | page 19 | line 1305 | NUMBER | 23.51 | [I2] cons note 8b current inv: Bajaj Finserve Liquid Fund, amount at 30 Sep 2026
R647 | page 19 | line 1305 | NUMBER | - | [I2] cons note 8b current inv: Bajaj Finserve Liquid Fund, units at 31 Mar 2026 | ZERO_STANDING
R648 | page 19 | line 1305 | NUMBER | - | [I2] cons note 8b current inv: Bajaj Finserve Liquid Fund, amount at 31 Mar 2026 | ZERO_STANDING
R649 | page 19 | line 1306 | NUMBER | 7,11,756 | [I2] cons note 8b current inv: BHARAT Bond ETF - April 2030, units at 30 Sep 2026
R650 | page 19 | line 1306 | NUMBER | 1,145.39 | [I2] cons note 8b current inv: BHARAT Bond ETF - April 2030, amount at 30 Sep 2026
R651 | page 19 | line 1306 | NUMBER | 7,11,756 | [I2] cons note 8b current inv: BHARAT Bond ETF - April 2030, units at 31 Mar 2026
R652 | page 19 | line 1306 | NUMBER | 1,111.61 | [I2] cons note 8b current inv: BHARAT Bond ETF - April 2030, amount at 31 Mar 2026
R653 | page 19 | line 1307 | NUMBER | 7,17,70,352 | [I2] cons note 8b current inv: Edelweiss CRISIL IBX 50:50 Gilt Plus SDL Apri, units at 30 Sep 2026
R654 | page 19 | line 1307 | NUMBER | 956.79 | [I2] cons note 8b current inv: Edelweiss CRISIL IBX 50:50 Gilt Plus SDL Apri, amount at 30 Sep 2026
R655 | page 19 | line 1307 | NUMBER | 7,17,70,352 | [I2] cons note 8b current inv: Edelweiss CRISIL IBX 50:50 Gilt Plus SDL Apri, units at 31 Mar 2026
R656 | page 19 | line 1307 | NUMBER | 930.37 | [I2] cons note 8b current inv: Edelweiss CRISIL IBX 50:50 Gilt Plus SDL Apri, amount at 31 Mar 2026
R657 | page 19 | line 1308 | NUMBER | - | [I2] cons note 8b current inv: Edelweiss NIFTY PSU Bond Plus SDL Apr 2026 50, units at 30 Sep 2026 | ZERO_STANDING
R658 | page 19 | line 1308 | NUMBER | - | [I2] cons note 8b current inv: Edelweiss NIFTY PSU Bond Plus SDL Apr 2026 50, amount at 30 Sep 2026 | ZERO_STANDING
R659 | page 19 | line 1308 | NUMBER | 4,74,76,047 | [I2] cons note 8b current inv: Edelweiss NIFTY PSU Bond Plus SDL Apr 2026 50, units at 31 Mar 2026
R660 | page 19 | line 1308 | NUMBER | 648.09 | [I2] cons note 8b current inv: Edelweiss NIFTY PSU Bond Plus SDL Apr 2026 50, amount at 31 Mar 2026
R661 | page 19 | line 1309 | NUMBER | 25,80,662 | [I2] cons note 8b current inv: Edelweiss Arbitrage Fund, units at 30 Sep 2026
R662 | page 19 | line 1309 | NUMBER | 58.09 | [I2] cons note 8b current inv: Edelweiss Arbitrage Fund, amount at 30 Sep 2026
R663 | page 19 | line 1309 | NUMBER | 1,55,50,911 | [I2] cons note 8b current inv: Edelweiss Arbitrage Fund, units at 31 Mar 2026
R664 | page 19 | line 1309 | NUMBER | 339.31 | [I2] cons note 8b current inv: Edelweiss Arbitrage Fund, amount at 31 Mar 2026
R665 | page 19 | line 1310 | NUMBER | 5,78,43,679 | [I2] cons note 8b current inv: Edelweiss Nifty Midcap150 Momentum 50 Index F, units at 30 Sep 2026
R666 | page 19 | line 1310 | NUMBER | 1,038.61 | [I2] cons note 8b current inv: Edelweiss Nifty Midcap150 Momentum 50 Index F, amount at 30 Sep 2026
R667 | page 19 | line 1310 | NUMBER | 4,60,74,718 | [I2] cons note 8b current inv: Edelweiss Nifty Midcap150 Momentum 50 Index F, units at 31 Mar 2026
R668 | page 19 | line 1310 | NUMBER | 739.32 | [I2] cons note 8b current inv: Edelweiss Nifty Midcap150 Momentum 50 Index F, amount at 31 Mar 2026
R669 | page 19 | line 1311 | NUMBER | 1,54,29,585 | [I2] cons note 8b current inv: HDFC Ultra Short to Short Term Fund, units at 30 Sep 2026
R670 | page 19 | line 1311 | NUMBER | 1,044.24 | [I2] cons note 8b current inv: HDFC Ultra Short to Short Term Fund, amount at 30 Sep 2026
R671 | page 19 | line 1311 | NUMBER | 1,54,29,585 | [I2] cons note 8b current inv: HDFC Ultra Short to Short Term Fund, units at 31 Mar 2026
R672 | page 19 | line 1311 | NUMBER | 1,011.19 | [I2] cons note 8b current inv: HDFC Ultra Short to Short Term Fund, amount at 31 Mar 2026
R673 | page 19 | line 1312 | NUMBER | 47,38,647 | [I2] cons note 8b current inv: HDFC Corporate Bond Fund, units at 30 Sep 2026
R674 | page 19 | line 1312 | NUMBER | 166.53 | [I2] cons note 8b current inv: HDFC Corporate Bond Fund, amount at 30 Sep 2026
R675 | page 19 | line 1312 | NUMBER | 47,38,647 | [I2] cons note 8b current inv: HDFC Corporate Bond Fund, units at 31 Mar 2026
R676 | page 19 | line 1312 | NUMBER | 161.75 | [I2] cons note 8b current inv: HDFC Corporate Bond Fund, amount at 31 Mar 2026
R677 | page 19 | line 1313 | NUMBER | 14,74,179 | [I2] cons note 8b current inv: ICICI Prudential Ultra Short to Short Term Fu, units at 30 Sep 2026
R678 | page 19 | line 1313 | NUMBER | 879.56 | [I2] cons note 8b current inv: ICICI Prudential Ultra Short to Short Term Fu, amount at 30 Sep 2026
R679 | page 19 | line 1313 | NUMBER | 14,74,179 | [I2] cons note 8b current inv: ICICI Prudential Ultra Short to Short Term Fu, units at 31 Mar 2026
R680 | page 19 | line 1313 | NUMBER | 851.11 | [I2] cons note 8b current inv: ICICI Prudential Ultra Short to Short Term Fu, amount at 31 Mar 2026
R681 | page 19 | line 1314 | NUMBER | - | [I2] cons note 8b current inv: ICICI Prudential Money Market Fund, units at 30 Sep 2026 | ZERO_STANDING
R682 | page 19 | line 1314 | NUMBER | - | [I2] cons note 8b current inv: ICICI Prudential Money Market Fund, amount at 30 Sep 2026 | ZERO_STANDING
R683 | page 19 | line 1314 | NUMBER | 6,12,903 | [I2] cons note 8b current inv: ICICI Prudential Money Market Fund, units at 31 Mar 2026
R684 | page 19 | line 1314 | NUMBER | 246.40 | [I2] cons note 8b current inv: ICICI Prudential Money Market Fund, amount at 31 Mar 2026
R685 | page 19 | line 1315 | NUMBER | - | [I2] cons note 8b current inv: ICICI Prudential Liquid Fund, units at 30 Sep 2026 | ZERO_STANDING
R686 | page 19 | line 1315 | NUMBER | - | [I2] cons note 8b current inv: ICICI Prudential Liquid Fund, amount at 30 Sep 2026 | ZERO_STANDING
R687 | page 19 | line 1315 | NUMBER | 1,12,625 | [I2] cons note 8b current inv: ICICI Prudential Liquid Fund, units at 31 Mar 2026
R688 | page 19 | line 1315 | NUMBER | 45.92 | [I2] cons note 8b current inv: ICICI Prudential Liquid Fund, amount at 31 Mar 2026
R689 | page 19 | line 1316 | NUMBER | 2,06,88,321 | [I2] cons note 8b current inv: ICICI Prudential Corporate Bond Fund, units at 30 Sep 2026
R690 | page 19 | line 1316 | NUMBER | 693.40 | [I2] cons note 8b current inv: ICICI Prudential Corporate Bond Fund, amount at 30 Sep 2026
R691 | page 19 | line 1316 | NUMBER | 2,06,88,321 | [I2] cons note 8b current inv: ICICI Prudential Corporate Bond Fund, units at 31 Mar 2026
R692 | page 19 | line 1316 | NUMBER | 671.52 | [I2] cons note 8b current inv: ICICI Prudential Corporate Bond Fund, amount at 31 Mar 2026
R693 | page 19 | line 1317 | NUMBER | 4,82,19,177 | [I2] cons note 8b current inv: ICICI Prudential Nifty SDL Dec 2028 Index Fun, units at 30 Sep 2026
R694 | page 19 | line 1317 | NUMBER | 646.27 | [I2] cons note 8b current inv: ICICI Prudential Nifty SDL Dec 2028 Index Fun, amount at 30 Sep 2026
R695 | page 19 | line 1317 | NUMBER | 4,82,19,177 | [I2] cons note 8b current inv: ICICI Prudential Nifty SDL Dec 2028 Index Fun, units at 31 Mar 2026
R696 | page 19 | line 1317 | NUMBER | 631.26 | [I2] cons note 8b current inv: ICICI Prudential Nifty SDL Dec 2028 Index Fun, amount at 31 Mar 2026
R697 | page 19 | line 1318 | NUMBER | 1,84,82,974 | [I2] cons note 8b current inv: ICICI Prudential Nifty Alpha Low Volatility 3, units at 30 Sep 2026
R698 | page 19 | line 1318 | NUMBER | 482.84 | [I2] cons note 8b current inv: ICICI Prudential Nifty Alpha Low Volatility 3, amount at 30 Sep 2026
R699 | page 19 | line 1318 | NUMBER | 2,01,61,336 | [I2] cons note 8b current inv: ICICI Prudential Nifty Alpha Low Volatility 3, units at 31 Mar 2026
R700 | page 19 | line 1318 | NUMBER | 498.20 | [I2] cons note 8b current inv: ICICI Prudential Nifty Alpha Low Volatility 3, amount at 31 Mar 2026
R701 | page 19 | line 1319 | NUMBER | 2,05,79,467 | [I2] cons note 8b current inv: ICICI Prudential Nifty 200 Quality 30 ETF, units at 30 Sep 2026
R702 | page 19 | line 1319 | NUMBER | 405.27 | [I2] cons note 8b current inv: ICICI Prudential Nifty 200 Quality 30 ETF, amount at 30 Sep 2026
R703 | page 19 | line 1319 | NUMBER | 2,05,79,467 | [I2] cons note 8b current inv: ICICI Prudential Nifty 200 Quality 30 ETF, units at 31 Mar 2026
R704 | page 19 | line 1319 | NUMBER | 386.69 | [I2] cons note 8b current inv: ICICI Prudential Nifty 200 Quality 30 ETF, amount at 31 Mar 2026
R705 | page 19 | line 1320 | NUMBER | 81,07,015 | [I2] cons note 8b current inv: Invesco India Arbitrage Fund, units at 30 Sep 2026
R706 | page 19 | line 1320 | NUMBER | 303.18 | [I2] cons note 8b current inv: Invesco India Arbitrage Fund, amount at 30 Sep 2026
R707 | page 19 | line 1320 | NUMBER | 2,03,34,137 | [I2] cons note 8b current inv: Invesco India Arbitrage Fund, units at 31 Mar 2026
R708 | page 19 | line 1320 | NUMBER | 736.72 | [I2] cons note 8b current inv: Invesco India Arbitrage Fund, amount at 31 Mar 2026
R709 | page 19 | line 1321 | NUMBER | 2,37,186 | [I2] cons note 8b current inv: Kotak Corporate Bond Fund, units at 30 Sep 2026
R710 | page 19 | line 1321 | NUMBER | 996.49 | [I2] cons note 8b current inv: Kotak Corporate Bond Fund, amount at 30 Sep 2026
R711 | page 19 | line 1321 | NUMBER | 2,37,186 | [I2] cons note 8b current inv: Kotak Corporate Bond Fund, units at 31 Mar 2026
R712 | page 19 | line 1321 | NUMBER | 967.94 | [I2] cons note 8b current inv: Kotak Corporate Bond Fund, amount at 31 Mar 2026
R713 | page 19 | line 1322 | NUMBER | 1,03,99,286 | [I2] cons note 8b current inv: Kotak Arbitrage Fund, units at 30 Sep 2026
R714 | page 19 | line 1322 | NUMBER | 450.90 | [I2] cons note 8b current inv: Kotak Arbitrage Fund, amount at 30 Sep 2026
R715 | page 19 | line 1322 | NUMBER | 2,06,50,108 | [I2] cons note 8b current inv: Kotak Arbitrage Fund, units at 31 Mar 2026
R716 | page 19 | line 1322 | NUMBER | 867.91 | [I2] cons note 8b current inv: Kotak Arbitrage Fund, amount at 31 Mar 2026
R717 | page 19 | line 1323 | NUMBER | 4,97,90,091 | [I2] cons note 8b current inv: Kotak Nifty SDL Apr 2027 Top 12 Equal Weight , units at 30 Sep 2026
R718 | page 19 | line 1323 | NUMBER | 661.41 | [I2] cons note 8b current inv: Kotak Nifty SDL Apr 2027 Top 12 Equal Weight , amount at 30 Sep 2026
R719 | page 19 | line 1323 | NUMBER | 4,97,90,091 | [I2] cons note 8b current inv: Kotak Nifty SDL Apr 2027 Top 12 Equal Weight , units at 31 Mar 2026
R720 | page 19 | line 1323 | NUMBER | 643.13 | [I2] cons note 8b current inv: Kotak Nifty SDL Apr 2027 Top 12 Equal Weight , amount at 31 Mar 2026
R721 | page 19 | line 1324 | NUMBER | 9,46,02,577 | [I2] cons note 8b current inv: Kotak Nifty SDL Apr 2032 Top 12 Equal Weight , units at 30 Sep 2026
R722 | page 19 | line 1324 | NUMBER | 1,270.05 | [I2] cons note 8b current inv: Kotak Nifty SDL Apr 2032 Top 12 Equal Weight , amount at 30 Sep 2026
R723 | page 19 | line 1324 | NUMBER | 9,46,02,577 | [I2] cons note 8b current inv: Kotak Nifty SDL Apr 2032 Top 12 Equal Weight , units at 31 Mar 2026
R724 | page 19 | line 1324 | NUMBER | 1,233.69 | [I2] cons note 8b current inv: Kotak Nifty SDL Apr 2032 Top 12 Equal Weight , amount at 31 Mar 2026
R725 | page 19 | line 1325 | NUMBER | 2,49,40,628 | [I2] cons note 8b current inv: Nippon India Dynamic Term Fund, units at 30 Sep 2026
R726 | page 19 | line 1325 | NUMBER | 1,054.73 | [I2] cons note 8b current inv: Nippon India Dynamic Term Fund, amount at 30 Sep 2026
R727 | page 19 | line 1325 | NUMBER | 2,49,40,628 | [I2] cons note 8b current inv: Nippon India Dynamic Term Fund, units at 31 Mar 2026
R728 | page 19 | line 1325 | NUMBER | 1,026.31 | [I2] cons note 8b current inv: Nippon India Dynamic Term Fund, amount at 31 Mar 2026
R729 | page 19 | line 1326 | NUMBER | 45,42,601 | [I2] cons note 8b current inv: SBI Corporate Bond Fund, units at 30 Sep 2026
R730 | page 19 | line 1326 | NUMBER | 77.31 | [I2] cons note 8b current inv: SBI Corporate Bond Fund, amount at 30 Sep 2026
R731 | page 19 | line 1326 | NUMBER | 45,42,601 | [I2] cons note 8b current inv: SBI Corporate Bond Fund, units at 31 Mar 2026
R732 | page 19 | line 1326 | NUMBER | 74.98 | [I2] cons note 8b current inv: SBI Corporate Bond Fund, amount at 31 Mar 2026
R733 | page 19 | line 1327 | NUMBER | - | [I2] cons note 8b current inv: Tata Money Market Fund, units at 30 Sep 2026 | ZERO_STANDING
R734 | page 19 | line 1327 | NUMBER | - | [I2] cons note 8b current inv: Tata Money Market Fund, amount at 30 Sep 2026 | ZERO_STANDING
R735 | page 19 | line 1327 | NUMBER | 6,90,894 | [I2] cons note 8b current inv: Tata Money Market Fund, units at 31 Mar 2026
R736 | page 19 | line 1327 | NUMBER | 238.88 | [I2] cons note 8b current inv: Tata Money Market Fund, amount at 31 Mar 2026
R737 | page 19 | line 1328 | NUMBER | 2,11,86,189 | [I2] cons note 8b current inv: Nippon India Nivesh Lakshya Long Term Fund, units at 30 Sep 2026
R738 | page 19 | line 1328 | NUMBER | 390.77 | [I2] cons note 8b current inv: Nippon India Nivesh Lakshya Long Term Fund, amount at 30 Sep 2026
R739 | page 19 | line 1328 | NUMBER | 2,11,86,189 | [I2] cons note 8b current inv: Nippon India Nivesh Lakshya Long Term Fund, units at 31 Mar 2026
R740 | page 19 | line 1328 | NUMBER | 377.78 | [I2] cons note 8b current inv: Nippon India Nivesh Lakshya Long Term Fund, amount at 31 Mar 2026
R741 | page 19 | line 1329 | NUMBER | 7,66,63,436 | [I2] cons note 8b current inv: Nippon India Nifty Alpha Low Volatility 30 In, units at 30 Sep 2026
R742 | page 19 | line 1329 | NUMBER | 1,167.83 | [I2] cons note 8b current inv: Nippon India Nifty Alpha Low Volatility 30 In, amount at 30 Sep 2026
R743 | page 19 | line 1329 | NUMBER | 5,34,71,886 | [I2] cons note 8b current inv: Nippon India Nifty Alpha Low Volatility 30 In, units at 31 Mar 2026
R744 | page 19 | line 1329 | NUMBER | 770.31 | [I2] cons note 8b current inv: Nippon India Nifty Alpha Low Volatility 30 In, amount at 31 Mar 2026
R745 | page 19 | line 1330 | NUMBER | 48,15,796 | [I2] cons note 8b current inv: Tata Arbitrage Fund, units at 30 Sep 2026
R746 | page 19 | line 1330 | NUMBER | 78.88 | [I2] cons note 8b current inv: Tata Arbitrage Fund, amount at 30 Sep 2026
R747 | page 19 | line 1330 | NUMBER | 3,42,53,192 | [I2] cons note 8b current inv: Tata Arbitrage Fund, units at 31 Mar 2026
R748 | page 19 | line 1330 | NUMBER | 543.71 | [I2] cons note 8b current inv: Tata Arbitrage Fund, amount at 31 Mar 2026
R749 | page 19 | line 1331 | NUMBER | 9,52,470 | [I2] cons note 8b current inv: SBI Nifty 200 Quality 30 ETF, units at 30 Sep 2026
R750 | page 19 | line 1331 | NUMBER | 197.45 | [I2] cons note 8b current inv: SBI Nifty 200 Quality 30 ETF, amount at 30 Sep 2026
R751 | page 19 | line 1331 | NUMBER | 8,00,932 | [I2] cons note 8b current inv: SBI Nifty 200 Quality 30 ETF, units at 31 Mar 2026
R752 | page 19 | line 1331 | NUMBER | 157.97 | [I2] cons note 8b current inv: SBI Nifty 200 Quality 30 ETF, amount at 31 Mar 2026
R753 | page 19 | line 1332 | NUMBER | - | [I2] cons note 8b current inv: UTI Money Market Fund, units at 30 Sep 2026 | ZERO_STANDING
R754 | page 19 | line 1332 | NUMBER | - | [I2] cons note 8b current inv: UTI Money Market Fund, amount at 30 Sep 2026 | ZERO_STANDING
R755 | page 19 | line 1332 | NUMBER | 42,990 | [I2] cons note 8b current inv: UTI Money Market Fund, units at 31 Mar 2026
R756 | page 19 | line 1332 | NUMBER | 140.42 | [I2] cons note 8b current inv: UTI Money Market Fund, amount at 31 Mar 2026
R757 | page 19 | line 1333 | NUMBER | 7,43,75,147 | [I2] cons note 8b current inv: UTI Nifty200 Quality 30 Index Fund, units at 30 Sep 2026
R758 | page 19 | line 1333 | NUMBER | 621.10 | [I2] cons note 8b current inv: UTI Nifty200 Quality 30 Index Fund, amount at 30 Sep 2026
R759 | page 19 | line 1333 | NUMBER | 7,43,75,147 | [I2] cons note 8b current inv: UTI Nifty200 Quality 30 Index Fund, units at 31 Mar 2026
R760 | page 19 | line 1333 | NUMBER | 592.77 | [I2] cons note 8b current inv: UTI Nifty200 Quality 30 Index Fund, amount at 31 Mar 2026
R761 | page 19 | line 1334 | NUMBER | - | [I2] cons note 8b current inv: Bajaj Finserv Liquid Fund, units at 30 Sep 2026 | ZERO_STANDING
R762 | page 19 | line 1334 | NUMBER | - | [I2] cons note 8b current inv: Bajaj Finserv Liquid Fund, amount at 30 Sep 2026 | ZERO_STANDING
R763 | page 19 | line 1334 | NUMBER | 6,302 | [I2] cons note 8b current inv: Bajaj Finserv Liquid Fund, units at 31 Mar 2026
R764 | page 19 | line 1334 | NUMBER | 7.58 | [I2] cons note 8b current inv: Bajaj Finserv Liquid Fund, amount at 31 Mar 2026
R765 | page 19 | line 1335 | NUMBER | - | [I2] cons note 8b current inv: Kotak Money Market Fund, units at 30 Sep 2026 | ZERO_STANDING
R766 | page 19 | line 1335 | NUMBER | - | [I2] cons note 8b current inv: Kotak Money Market Fund, amount at 30 Sep 2026 | ZERO_STANDING
R767 | page 19 | line 1335 | NUMBER | 43,333 | [I2] cons note 8b current inv: Kotak Money Market Fund, units at 31 Mar 2026
R768 | page 19 | line 1335 | NUMBER | 205.60 | [I2] cons note 8b current inv: Kotak Money Market Fund, amount at 31 Mar 2026
R769 | page 19 | line 1336 | NUMBER | - | [I2] cons note 8b current inv: UTI Liquid Fund, units at 30 Sep 2026 | ZERO_STANDING
R770 | page 19 | line 1336 | NUMBER | - | [I2] cons note 8b current inv: UTI Liquid Fund, amount at 30 Sep 2026 | ZERO_STANDING
R771 | page 19 | line 1336 | NUMBER | 14,530 | [I2] cons note 8b current inv: UTI Liquid Fund, units at 31 Mar 2026
R772 | page 19 | line 1336 | NUMBER | 65.63 | [I2] cons note 8b current inv: UTI Liquid Fund, amount at 31 Mar 2026
R773 | page 19 | line 1337 | NUMBER | 5,58,962 | [I2] cons note 8b current inv: Bandhan Money Market Fund, units at 30 Sep 2026
R774 | page 19 | line 1337 | NUMBER | 26.48 | [I2] cons note 8b current inv: Bandhan Money Market Fund, amount at 30 Sep 2026
R775 | page 19 | line 1337 | NUMBER | 63,93,002 | [I2] cons note 8b current inv: Bandhan Money Market Fund, units at 31 Mar 2026
R776 | page 19 | line 1337 | NUMBER | 314.55 | [I2] cons note 8b current inv: Bandhan Money Market Fund, amount at 31 Mar 2026
R777 | page 19 | line 1338 | NUMBER | 45,22,509 | [I2] cons note 8b current inv: Altiva Hybrid Long Short Fund, units at 30 Sep 2026
R778 | page 19 | line 1338 | NUMBER | 49.96 | [I2] cons note 8b current inv: Altiva Hybrid Long Short Fund, amount at 30 Sep 2026
R779 | page 19 | line 1338 | NUMBER | 21,91,794 | [I2] cons note 8b current inv: Altiva Hybrid Long Short Fund, units at 31 Mar 2026
R780 | page 19 | line 1338 | NUMBER | 22.40 | [I2] cons note 8b current inv: Altiva Hybrid Long Short Fund, amount at 31 Mar 2026
R781 | page 19 | line 1339 | NUMBER | 91,91,798 | [I2] cons note 8b current inv: SBI 10 YEAR CONSTANT MATURITY GILT FUND, units at 30 Sep 2026
R782 | page 19 | line 1339 | NUMBER | 630.71 | [I2] cons note 8b current inv: SBI 10 YEAR CONSTANT MATURITY GILT FUND, amount at 30 Sep 2026
R783 | page 19 | line 1339 | NUMBER | 91,91,798 | [I2] cons note 8b current inv: SBI 10 YEAR CONSTANT MATURITY GILT FUND, units at 31 Mar 2026
R784 | page 19 | line 1339 | NUMBER | 614.81 | [I2] cons note 8b current inv: SBI 10 YEAR CONSTANT MATURITY GILT FUND, amount at 31 Mar 2026
R785 | page 19 | line 1340 | NUMBER | 31,23,085 | [I2] cons note 8b current inv: Magnum Hybrid Long Short Fund, units at 30 Sep 2026
R786 | page 19 | line 1340 | NUMBER | 32.41 | [I2] cons note 8b current inv: Magnum Hybrid Long Short Fund, amount at 30 Sep 2026
R787 | page 19 | line 1340 | NUMBER | 17,18,197 | [I2] cons note 8b current inv: Magnum Hybrid Long Short Fund, units at 31 Mar 2026
R788 | page 19 | line 1340 | NUMBER | 17.17 | [I2] cons note 8b current inv: Magnum Hybrid Long Short Fund, amount at 31 Mar 2026
R789 | page 19 | line 1341 | NUMBER | 5,61,12,534 | [I2] cons note 8b current inv: SBI Nifty200 Quality 30 Index Fund, units at 30 Sep 2026
R790 | page 19 | line 1341 | NUMBER | 525.57 | [I2] cons note 8b current inv: SBI Nifty200 Quality 30 Index Fund, amount at 30 Sep 2026
R791 | page 19 | line 1341 | NUMBER | 1,91,80,261 | [I2] cons note 8b current inv: SBI Nifty200 Quality 30 Index Fund, units at 31 Mar 2026
R792 | page 19 | line 1341 | NUMBER | 171.53 | [I2] cons note 8b current inv: SBI Nifty200 Quality 30 Index Fund, amount at 31 Mar 2026
R793 | page 19 | line 1342 | NUMBER | 25,85,641 | [I2] cons note 8b current inv: ICICI Alpha Low Volatility 30 ETF, units at 30 Sep 2026
R794 | page 19 | line 1342 | NUMBER | 67.74 | [I2] cons note 8b current inv: ICICI Alpha Low Volatility 30 ETF, amount at 30 Sep 2026
R795 | page 19 | line 1342 | NUMBER | - | [I2] cons note 8b current inv: ICICI Alpha Low Volatility 30 ETF, units at 31 Mar 2026 | ZERO_STANDING
R796 | page 19 | line 1342 | NUMBER | - | [I2] cons note 8b current inv: ICICI Alpha Low Volatility 30 ETF, amount at 31 Mar 2026 | ZERO_STANDING
R797 | page 19 | line 1343 | NUMBER | 8,180 | [I2] cons note 8b current inv: Edelweiss Liquid Fund, units at 30 Sep 2026
R798 | page 19 | line 1343 | NUMBER | 30.00 | [I2] cons note 8b current inv: Edelweiss Liquid Fund, amount at 30 Sep 2026
R799 | page 19 | line 1343 | NUMBER | - | [I2] cons note 8b current inv: Edelweiss Liquid Fund, units at 31 Mar 2026 | ZERO_STANDING
R800 | page 19 | line 1343 | NUMBER | - | [I2] cons note 8b current inv: Edelweiss Liquid Fund, amount at 31 Mar 2026 | ZERO_STANDING
R801 | page 19 | line 1344 | NUMBER | 2,46,52,417 | [I2] cons note 8b current inv: Edelweiss Banking and PSU Debt Fund, units at 30 Sep 2026
R802 | page 19 | line 1344 | NUMBER | 668.63 | [I2] cons note 8b current inv: Edelweiss Banking and PSU Debt Fund, amount at 30 Sep 2026
R803 | page 19 | line 1344 | NUMBER | - | [I2] cons note 8b current inv: Edelweiss Banking and PSU Debt Fund, units at 31 Mar 2026 | ZERO_STANDING
R804 | page 19 | line 1344 | NUMBER | - | [I2] cons note 8b current inv: Edelweiss Banking and PSU Debt Fund, amount at 31 Mar 2026 | ZERO_STANDING
R805 | page 19 | line 1345 | NUMBER | 14,653 | [I2] cons note 8b current inv: Tata Overnight Fund, units at 30 Sep 2026
R806 | page 19 | line 1345 | NUMBER | 21.37 | [I2] cons note 8b current inv: Tata Overnight Fund, amount at 30 Sep 2026
R807 | page 19 | line 1345 | NUMBER | - | [I2] cons note 8b current inv: Tata Overnight Fund, units at 31 Mar 2026 | ZERO_STANDING
R808 | page 19 | line 1345 | NUMBER | - | [I2] cons note 8b current inv: Tata Overnight Fund, amount at 31 Mar 2026 | ZERO_STANDING
R809 | page 19 | line 1346 | NUMBER | 1,89,55,981 | [I2] cons note 8b current inv: Kotak Nifty Midcap 150 Momentum 50 Index Fund, units at 30 Sep 2026
R810 | page 19 | line 1346 | NUMBER | 174.24 | [I2] cons note 8b current inv: Kotak Nifty Midcap 150 Momentum 50 Index Fund, amount at 30 Sep 2026
R811 | page 19 | line 1346 | NUMBER | - | [I2] cons note 8b current inv: Kotak Nifty Midcap 150 Momentum 50 Index Fund, units at 31 Mar 2026 | ZERO_STANDING
R812 | page 19 | line 1346 | NUMBER | - | [I2] cons note 8b current inv: Kotak Nifty Midcap 150 Momentum 50 Index Fund, amount at 31 Mar 2026 | ZERO_STANDING
R813 | page 19 | line 1347 | NUMBER | 19,298.81 | [I2] cons note 8b current inv: Total, amount at 30 Sep 2026
R814 | page 19 | line 1347 | NUMBER | 20,845.16 | [I2] cons note 8b current inv: Total, amount at 31 Mar 2026
R815 | page 19 | line 1351 | NUMBER | 7,500 | [I2] cons note 8b current inv: Bajaj Finance Ltd. Bond, units at 30 Sep 2026
R816 | page 19 | line 1351 | NUMBER | 789.74 | [I2] cons note 8b current inv: Bajaj Finance Ltd. Bond, amount at 30 Sep 2026
R817 | page 19 | line 1351 | NUMBER | 5,000 | [I2] cons note 8b current inv: Bajaj Finance Ltd. Bond, units at 31 Mar 2026
R818 | page 19 | line 1351 | NUMBER | 515.59 | [I2] cons note 8b current inv: Bajaj Finance Ltd. Bond, amount at 31 Mar 2026
R819 | page 19 | line 1352 | NUMBER | 3,000 | [I2] cons note 8b current inv: Axis Finance Ltd. Bond, units at 30 Sep 2026
R820 | page 19 | line 1352 | NUMBER | 313.48 | [I2] cons note 8b current inv: Axis Finance Ltd. Bond, amount at 30 Sep 2026
R821 | page 19 | line 1352 | NUMBER | 3,000 | [I2] cons note 8b current inv: Axis Finance Ltd. Bond, units at 31 Mar 2026
R822 | page 19 | line 1352 | NUMBER | 305.60 | [I2] cons note 8b current inv: Axis Finance Ltd. Bond, amount at 31 Mar 2026
R823 | page 19 | line 1353 | NUMBER | 30 | [I2] cons note 8b current inv: HDFC Bank Perpetual Bond, units at 30 Sep 2026
R824 | page 19 | line 1353 | NUMBER | 305.88 | [I2] cons note 8b current inv: HDFC Bank Perpetual Bond, amount at 30 Sep 2026
R825 | page 19 | line 1353 | NUMBER | 30 | [I2] cons note 8b current inv: HDFC Bank Perpetual Bond, units at 31 Mar 2026
R826 | page 19 | line 1353 | NUMBER | 313.33 | [I2] cons note 8b current inv: HDFC Bank Perpetual Bond, amount at 31 Mar 2026
R827 | page 19 | line 1354 | NUMBER | 5,275 | [I2] cons note 8b current inv: HDFC Bank Bond, units at 30 Sep 2026
R828 | page 19 | line 1354 | NUMBER | 1,037.95 | [I2] cons note 8b current inv: HDFC Bank Bond, amount at 30 Sep 2026
R829 | page 19 | line 1354 | NUMBER | 2,775 | [I2] cons note 8b current inv: HDFC Bank Bond, units at 31 Mar 2026
R830 | page 19 | line 1354 | NUMBER | 766.56 | [I2] cons note 8b current inv: HDFC Bank Bond, amount at 31 Mar 2026
R831 | page 19 | line 1355 | NUMBER | 7,050 | [I2] cons note 8b current inv: HDB Financial Services Ltd Bond, units at 30 Sep 2026
R832 | page 19 | line 1355 | NUMBER | 727.57 | [I2] cons note 8b current inv: HDB Financial Services Ltd Bond, amount at 30 Sep 2026
R833 | page 19 | line 1355 | NUMBER | 6,000 | [I2] cons note 8b current inv: HDB Financial Services Ltd Bond, units at 31 Mar 2026
R834 | page 19 | line 1355 | NUMBER | 627.98 | [I2] cons note 8b current inv: HDB Financial Services Ltd Bond, amount at 31 Mar 2026
R835 | page 19 | line 1356 | NUMBER | 25 | [I2] cons note 8b current inv: ICICI Bank Bond, units at 30 Sep 2026
R836 | page 19 | line 1356 | NUMBER | 249.43 | [I2] cons note 8b current inv: ICICI Bank Bond, amount at 30 Sep 2026
R837 | page 19 | line 1356 | NUMBER | - | [I2] cons note 8b current inv: ICICI Bank Bond, units at 31 Mar 2026 | ZERO_STANDING
R838 | page 19 | line 1356 | NUMBER | - | [I2] cons note 8b current inv: ICICI Bank Bond, amount at 31 Mar 2026 | ZERO_STANDING
R839 | page 19 | line 1357 | NUMBER | 1,370 | [I2] cons note 8b current inv: Kotak Mahindra Prime Ltd. Bond, units at 30 Sep 2026
R840 | page 19 | line 1357 | NUMBER | 139.48 | [I2] cons note 8b current inv: Kotak Mahindra Prime Ltd. Bond, amount at 30 Sep 2026
R841 | page 19 | line 1357 | NUMBER | - | [I2] cons note 8b current inv: Kotak Mahindra Prime Ltd. Bond, units at 31 Mar 2026 | ZERO_STANDING
R842 | page 19 | line 1357 | NUMBER | - | [I2] cons note 8b current inv: Kotak Mahindra Prime Ltd. Bond, amount at 31 Mar 2026 | ZERO_STANDING
R843 | page 19 | line 1358 | NUMBER | 100 | [I2] cons note 8b current inv: India Infradebt Ltd Bond, units at 30 Sep 2026
R844 | page 19 | line 1358 | NUMBER | 104.13 | [I2] cons note 8b current inv: India Infradebt Ltd Bond, amount at 30 Sep 2026
R845 | page 19 | line 1358 | NUMBER | 100 | [I2] cons note 8b current inv: India Infradebt Ltd Bond, units at 31 Mar 2026
R846 | page 19 | line 1358 | NUMBER | 100.15 | [I2] cons note 8b current inv: India Infradebt Ltd Bond, amount at 31 Mar 2026
R847 | page 19 | line 1359 | NUMBER | 1,250 | [I2] cons note 8b current inv: LIC Housing Finance Ltd Bond, units at 30 Sep 2026
R848 | page 19 | line 1359 | NUMBER | 349.02 | [I2] cons note 8b current inv: LIC Housing Finance Ltd Bond, amount at 30 Sep 2026
R849 | page 19 | line 1359 | NUMBER | 100 | [I2] cons note 8b current inv: LIC Housing Finance Ltd Bond, units at 31 Mar 2026
R850 | page 19 | line 1359 | NUMBER | 106.71 | [I2] cons note 8b current inv: LIC Housing Finance Ltd Bond, amount at 31 Mar 2026
R851 | page 19 | line 1360 | NUMBER | 7,500 | [I2] cons note 8b current inv: Mahindra & Mahindra Financial Services Ltd. B, units at 30 Sep 2026
R852 | page 19 | line 1360 | NUMBER | 788.84 | [I2] cons note 8b current inv: Mahindra & Mahindra Financial Services Ltd. B, amount at 30 Sep 2026
R853 | page 19 | line 1360 | NUMBER | 7,500 | [I2] cons note 8b current inv: Mahindra & Mahindra Financial Services Ltd. B, units at 31 Mar 2026
R854 | page 19 | line 1360 | NUMBER | 761.15 | [I2] cons note 8b current inv: Mahindra & Mahindra Financial Services Ltd. B, amount at 31 Mar 2026
R855 | page 19 | line 1361 | NUMBER | 10 | [I2] cons note 8b current inv: Punjab National Bank Perpetual Bond, units at 30 Sep 2026
R856 | page 19 | line 1361 | NUMBER | 106.18 | [I2] cons note 8b current inv: Punjab National Bank Perpetual Bond, amount at 30 Sep 2026
R857 | page 19 | line 1361 | NUMBER | 10 | [I2] cons note 8b current inv: Punjab National Bank Perpetual Bond, units at 31 Mar 2026
R858 | page 19 | line 1361 | NUMBER | 102.32 | [I2] cons note 8b current inv: Punjab National Bank Perpetual Bond, amount at 31 Mar 2026
R859 | page 19 | line 1362 | NUMBER | 10,000 | [I2] cons note 8b current inv: REC Zero Coupon Bond, units at 30 Sep 2026
R860 | page 19 | line 1362 | NUMBER | 568.50 | [I2] cons note 8b current inv: REC Zero Coupon Bond, amount at 30 Sep 2026
R861 | page 19 | line 1362 | NUMBER | 10,000 | [I2] cons note 8b current inv: REC Zero Coupon Bond, units at 31 Mar 2026
R862 | page 19 | line 1362 | NUMBER | 561.84 | [I2] cons note 8b current inv: REC Zero Coupon Bond, amount at 31 Mar 2026
R863 | page 19 | line 1363 | NUMBER | 70 | [I2] cons note 8b current inv: State Bank of India Perpetual Bond, units at 30 Sep 2026
R864 | page 19 | line 1363 | NUMBER | 709.85 | [I2] cons note 8b current inv: State Bank of India Perpetual Bond, amount at 30 Sep 2026
R865 | page 19 | line 1363 | NUMBER | 100 | [I2] cons note 8b current inv: State Bank of India Perpetual Bond, units at 31 Mar 2026
R866 | page 19 | line 1363 | NUMBER | 1,039.24 | [I2] cons note 8b current inv: State Bank of India Perpetual Bond, amount at 31 Mar 2026
R867 | page 19 | line 1364 | NUMBER | 15 | [I2] cons note 8b current inv: State Bank of India Tier-II Bond, units at 30 Sep 2026
R868 | page 19 | line 1364 | NUMBER | 150.22 | [I2] cons note 8b current inv: State Bank of India Tier-II Bond, amount at 30 Sep 2026
R869 | page 19 | line 1364 | NUMBER | 15 | [I2] cons note 8b current inv: State Bank of India Tier-II Bond, units at 31 Mar 2026
R870 | page 19 | line 1364 | NUMBER | 156.81 | [I2] cons note 8b current inv: State Bank of India Tier-II Bond, amount at 31 Mar 2026
R871 | page 19 | line 1365 | NUMBER | 1,000 | [I2] cons note 8b current inv: LIC Housing Finance Limited Bond, units at 30 Sep 2026
R872 | page 19 | line 1365 | NUMBER | 100.49 | [I2] cons note 8b current inv: LIC Housing Finance Limited Bond, amount at 30 Sep 2026
R873 | page 19 | line 1365 | NUMBER | 1,000 | [I2] cons note 8b current inv: LIC Housing Finance Limited Bond, units at 31 Mar 2026
R874 | page 19 | line 1365 | NUMBER | 106.31 | [I2] cons note 8b current inv: LIC Housing Finance Limited Bond, amount at 31 Mar 2026
R875 | page 19 | line 1366 | NUMBER | 250 | [I2] cons note 8b current inv: Tata Capital Limited Bond, units at 30 Sep 2026
R876 | page 19 | line 1366 | NUMBER | 268.80 | [I2] cons note 8b current inv: Tata Capital Limited Bond, amount at 30 Sep 2026
R877 | page 19 | line 1366 | NUMBER | 250 | [I2] cons note 8b current inv: Tata Capital Limited Bond, units at 31 Mar 2026
R878 | page 19 | line 1366 | NUMBER | 259.63 | [I2] cons note 8b current inv: Tata Capital Limited Bond, amount at 31 Mar 2026
R879 | page 19 | line 1367 | NUMBER | 1,000 | [I2] cons note 8b current inv: Club with Mahindra & Mahindra Financial Servi, units at 30 Sep 2026
R880 | page 19 | line 1367 | NUMBER | 102.43 | [I2] cons note 8b current inv: Club with Mahindra & Mahindra Financial Servi, amount at 30 Sep 2026
R881 | page 19 | line 1367 | NUMBER | - | [I2] cons note 8b current inv: Club with Mahindra & Mahindra Financial Servi, units at 31 Mar 2026 | ZERO_STANDING
R882 | page 19 | line 1367 | NUMBER | - | [I2] cons note 8b current inv: Club with Mahindra & Mahindra Financial Servi, amount at 31 Mar 2026 | ZERO_STANDING
R883 | page 19 | line 1368 | NUMBER | 15 | [I2] cons note 8b current inv: Union Bank of India Perpetual Bond, units at 30 Sep 2026
R884 | page 19 | line 1368 | NUMBER | 157.62 | [I2] cons note 8b current inv: Union Bank of India Perpetual Bond, amount at 30 Sep 2026
R885 | page 19 | line 1368 | NUMBER | 15 | [I2] cons note 8b current inv: Union Bank of India Perpetual Bond, units at 31 Mar 2026
R886 | page 19 | line 1368 | NUMBER | 152.13 | [I2] cons note 8b current inv: Union Bank of India Perpetual Bond, amount at 31 Mar 2026
R887 | page 19 | line 1369 | NUMBER | 1,942 | [I2] cons note 8b current inv: Power Finance Corporation Zero Coupon Bond, units at 30 Sep 2026
R888 | page 19 | line 1369 | NUMBER | 100.52 | [I2] cons note 8b current inv: Power Finance Corporation Zero Coupon Bond, amount at 30 Sep 2026
R889 | page 19 | line 1369 | NUMBER | 1,942 | [I2] cons note 8b current inv: Power Finance Corporation Zero Coupon Bond, units at 31 Mar 2026
R890 | page 19 | line 1369 | NUMBER | 99.18 | [I2] cons note 8b current inv: Power Finance Corporation Zero Coupon Bond, amount at 31 Mar 2026
R891 | page 19 | line 1370 | NUMBER | 7,070.13 | [I2] cons note 8b current inv: Total, amount at 30 Sep 2026
R892 | page 19 | line 1370 | NUMBER | 5,974.53 | [I2] cons note 8b current inv: Total, amount at 31 Mar 2026
R893 | page 19 | line 1373 | NUMBER | 1,00,00,000 | [I2] cons note 8b current inv: 7.18% Government of India 2037, units at 30 Sep 2026
R894 | page 19 | line 1373 | NUMBER | 1,009.66 | [I2] cons note 8b current inv: 7.18% Government of India 2037, amount at 30 Sep 2026
R895 | page 19 | line 1373 | NUMBER | 1,25,00,000 | [I2] cons note 8b current inv: 7.18% Government of India 2037, units at 31 Mar 2026
R896 | page 19 | line 1373 | NUMBER | 1,265.15 | [I2] cons note 8b current inv: 7.18% Government of India 2037, amount at 31 Mar 2026
R897 | page 19 | line 1374 | NUMBER | 10,00,000 | [I2] cons note 8b current inv: 7.44% Government of Karnataka SGS 2034, units at 30 Sep 2026
R898 | page 19 | line 1374 | NUMBER | 98.98 | [I2] cons note 8b current inv: 7.44% Government of Karnataka SGS 2034, amount at 30 Sep 2026
R899 | page 19 | line 1374 | NUMBER | 10,00,000 | [I2] cons note 8b current inv: 7.44% Government of Karnataka SGS 2034, units at 31 Mar 2026
R900 | page 19 | line 1374 | NUMBER | 100.18 | [I2] cons note 8b current inv: 7.44% Government of Karnataka SGS 2034, amount at 31 Mar 2026
R901 | page 19 | line 1375 | NUMBER | 35,00,000 | [I2] cons note 8b current inv: 7.42% Government of Karnataka SGS 2035, units at 30 Sep 2026
R902 | page 19 | line 1375 | NUMBER | 343.18 | [I2] cons note 8b current inv: 7.42% Government of Karnataka SGS 2035, amount at 30 Sep 2026
R903 | page 19 | line 1375 | NUMBER | 35,00,000 | [I2] cons note 8b current inv: 7.42% Government of Karnataka SGS 2035, units at 31 Mar 2026
R904 | page 19 | line 1375 | NUMBER | 347.67 | [I2] cons note 8b current inv: 7.42% Government of Karnataka SGS 2035, amount at 31 Mar 2026
R905 | page 19 | line 1376 | NUMBER | 25,00,000 | [I2] cons note 8b current inv: 7.45% Government of Karnataka SGS 2037, units at 30 Sep 2026
R906 | page 19 | line 1376 | NUMBER | 243.11 | [I2] cons note 8b current inv: 7.45% Government of Karnataka SGS 2037, amount at 30 Sep 2026
R907 | page 19 | line 1376 | NUMBER | 25,00,000 | [I2] cons note 8b current inv: 7.45% Government of Karnataka SGS 2037, units at 31 Mar 2026
R908 | page 19 | line 1376 | NUMBER | 245.75 | [I2] cons note 8b current inv: 7.45% Government of Karnataka SGS 2037, amount at 31 Mar 2026
R909 | page 19 | line 1377 | NUMBER | 20,00,000 | [I2] cons note 8b current inv: 7.43% Government of Tamil Nadu SGS 2034, units at 30 Sep 2026
R910 | page 19 | line 1377 | NUMBER | 196.65 | [I2] cons note 8b current inv: 7.43% Government of Tamil Nadu SGS 2034, amount at 30 Sep 2026
R911 | page 19 | line 1377 | NUMBER | 20,00,000 | [I2] cons note 8b current inv: 7.43% Government of Tamil Nadu SGS 2034, units at 31 Mar 2026
R912 | page 19 | line 1377 | NUMBER | 199.05 | [I2] cons note 8b current inv: 7.43% Government of Tamil Nadu SGS 2034, amount at 31 Mar 2026
R913 | page 19 | line 1378 | NUMBER | 25,00,000 | [I2] cons note 8b current inv: 7.38% Government of Tamil Nadu SGS 2034, units at 30 Sep 2026
R914 | page 19 | line 1378 | NUMBER | 251.03 | [I2] cons note 8b current inv: 7.38% Government of Tamil Nadu SGS 2034, amount at 30 Sep 2026
R915 | page 19 | line 1378 | NUMBER | 25,00,000 | [I2] cons note 8b current inv: 7.38% Government of Tamil Nadu SGS 2034, units at 31 Mar 2026
R916 | page 19 | line 1378 | NUMBER | 254.06 | [I2] cons note 8b current inv: 7.38% Government of Tamil Nadu SGS 2034, amount at 31 Mar 2026
R917 | page 19 | line 1379 | NUMBER | 20,00,000 | [I2] cons note 8b current inv: 7.34% Government of Tamil Nadu SGS 2034, units at 30 Sep 2026
R918 | page 19 | line 1379 | NUMBER | 198.03 | [I2] cons note 8b current inv: 7.34% Government of Tamil Nadu SGS 2034, amount at 30 Sep 2026
R919 | page 19 | line 1379 | NUMBER | 20,00,000 | [I2] cons note 8b current inv: 7.34% Government of Tamil Nadu SGS 2034, units at 31 Mar 2026
R920 | page 19 | line 1379 | NUMBER | 200.50 | [I2] cons note 8b current inv: 7.34% Government of Tamil Nadu SGS 2034, amount at 31 Mar 2026
R921 | page 19 | line 1380 | NUMBER | 25,00,000 | [I2] cons note 8b current inv: 7.72% Government of Maharashtra SGS 2035, units at 30 Sep 2026
R922 | page 19 | line 1380 | NUMBER | 252.74 | [I2] cons note 8b current inv: 7.72% Government of Maharashtra SGS 2035, amount at 30 Sep 2026
R923 | page 19 | line 1380 | NUMBER | 25,00,000 | [I2] cons note 8b current inv: 7.72% Government of Maharashtra SGS 2035, units at 31 Mar 2026
R924 | page 19 | line 1380 | NUMBER | 256.14 | [I2] cons note 8b current inv: 7.72% Government of Maharashtra SGS 2035, amount at 31 Mar 2026
R925 | page 19 | line 1381 | NUMBER | 25,00,000 | [I2] cons note 8b current inv: 7.40% Government of Maharashtra SGS 2035, units at 30 Sep 2026
R926 | page 19 | line 1381 | NUMBER | 244.82 | [I2] cons note 8b current inv: 7.40% Government of Maharashtra SGS 2035, amount at 30 Sep 2026
R927 | page 19 | line 1381 | NUMBER | 25,00,000 | [I2] cons note 8b current inv: 7.40% Government of Maharashtra SGS 2035, units at 31 Mar 2026
R928 | page 19 | line 1381 | NUMBER | 248.01 | [I2] cons note 8b current inv: 7.40% Government of Maharashtra SGS 2035, amount at 31 Mar 2026
R929 | page 19 | line 1382 | NUMBER | 35,00,000 | [I2] cons note 8b current inv: 7.73% Government of Maharashtra SGS 2036, units at 30 Sep 2026
R930 | page 19 | line 1382 | NUMBER | 353.22 | [I2] cons note 8b current inv: 7.73% Government of Maharashtra SGS 2036, amount at 30 Sep 2026
R931 | page 19 | line 1382 | NUMBER | 35,00,000 | [I2] cons note 8b current inv: 7.73% Government of Maharashtra SGS 2036, units at 31 Mar 2026
R932 | page 19 | line 1382 | NUMBER | 357.85 | [I2] cons note 8b current inv: 7.73% Government of Maharashtra SGS 2036, amount at 31 Mar 2026
R933 | page 19 | line 1383 | NUMBER | 10,00,000 | [I2] cons note 8b current inv: 6.48% Government of India 2035, units at 30 Sep 2026
R934 | page 19 | line 1383 | NUMBER | 98.65 | [I2] cons note 8b current inv: 6.48% Government of India 2035, amount at 30 Sep 2026
R935 | page 19 | line 1383 | NUMBER | - | [I2] cons note 8b current inv: 6.48% Government of India 2035, units at 31 Mar 2026 | ZERO_STANDING
R936 | page 19 | line 1383 | NUMBER | - | [I2] cons note 8b current inv: 6.48% Government of India 2035, amount at 31 Mar 2026 | ZERO_STANDING
R937 | page 19 | line 1384 | NUMBER | 35,00,000 | [I2] cons note 8b current inv: 6.68% Government of India 2040, units at 30 Sep 2026
R938 | page 19 | line 1384 | NUMBER | 336.06 | [I2] cons note 8b current inv: 6.68% Government of India 2040, amount at 30 Sep 2026
R939 | page 19 | line 1384 | NUMBER | - | [I2] cons note 8b current inv: 6.68% Government of India 2040, units at 31 Mar 2026 | ZERO_STANDING
R940 | page 19 | line 1384 | NUMBER | - | [I2] cons note 8b current inv: 6.68% Government of India 2040, amount at 31 Mar 2026 | ZERO_STANDING
R941 | page 19 | line 1385 | NUMBER | 3,626.13 | [I2] cons note 8b current inv: Total, amount at 30 Sep 2026
R942 | page 19 | line 1385 | NUMBER | 3,474.36 | [I2] cons note 8b current inv: Total, amount at 31 Mar 2026
R943 | page 19 | line 1388 | NUMBER | 91.99 | [I2] cons note 8b current inv: TREPS Lending, amount at 30 Sep 2026
R944 | page 19 | line 1388 | NUMBER | - | [I2] cons note 8b current inv: TREPS Lending, amount at 31 Mar 2026 | ZERO_STANDING
R945 | page 19 | line 1390 | NUMBER | 30,087.06 | [I2] cons note 8b current inv: Total current investments, amount at 30 Sep 2026
R946 | page 19 | line 1390 | NUMBER | 30,294.05 | [I2] cons note 8b current inv: Total current investments, amount at 31 Mar 2026
R947 | page 19 | line 1392 | NUMBER | 29,995.07 | [I2] cons note 8b current inv: Aggregate book value of quoted investments, amount at 30 Sep 2026
R948 | page 19 | line 1392 | NUMBER | 30,294.05 | [I2] cons note 8b current inv: Aggregate book value of quoted investments, amount at 31 Mar 2026
R949 | page 19 | line 1393 | NUMBER | 29,995.07 | [I2] cons note 8b current inv: Aggregate market value of quoted investments, amount at 30 Sep 2026
R950 | page 19 | line 1393 | NUMBER | 30,294.05 | [I2] cons note 8b current inv: Aggregate market value of quoted investments, amount at 31 Mar 2026
R951 | page 19 | line 1394 | NUMBER | 4,707.37 | [I2] cons note 8b current inv: Aggregate carrying value of unquoted investme, amount at 30 Sep 2026
R952 | page 19 | line 1394 | NUMBER | 4,079.05 | [I2] cons note 8b current inv: Aggregate carrying value of unquoted investme, amount at 31 Mar 2026
R953 | page 20 | line 1458 | NUMBER | 544.91 | [I2] cons note 8c/d loans, other fin assets: - PNB Housing Finance Limited ^, at 30 Sep 2026
R954 | page 20 | line 1458 | NUMBER | 525.66 | [I2] cons note 8c/d loans, other fin assets: - PNB Housing Finance Limited ^, at 31 Mar 2026
R955 | page 20 | line 1459 | NUMBER | 218.10 | [I2] cons note 8c/d loans, other fin assets: - LIC ^, at 30 Sep 2026
R956 | page 20 | line 1459 | NUMBER | 210.41 | [I2] cons note 8c/d loans, other fin assets: - LIC ^, at 31 Mar 2026
R957 | page 20 | line 1460 | NUMBER | 165.27 | [I2] cons note 8c/d loans, other fin assets: - Bajaj Finance Limited ^, at 30 Sep 2026
R958 | page 20 | line 1460 | NUMBER | 159.77 | [I2] cons note 8c/d loans, other fin assets: - Bajaj Finance Limited ^, at 31 Mar 2026
R959 | page 20 | line 1461 | NUMBER | 0.36 | [I2] cons note 8c/d loans, other fin assets: Loans to employees**, at 30 Sep 2026
R960 | page 20 | line 1461 | NUMBER | 1.21 | [I2] cons note 8c/d loans, other fin assets: Loans to employees**, at 31 Mar 2026
R961 | page 20 | line 1461 | NUMBER | 928.64 | [I2] cons note 8c/d loans, other fin assets: Loans to employees**, at 30 Sep 2026
R962 | page 20 | line 1461 | NUMBER | 897.05 | [I2] cons note 8c/d loans, other fin assets: Loans to employees**, at 31 Mar 2026
R963 | page 20 | line 1465 | NUMBER | 6.07 | [I2] cons note 8c/d loans, other fin assets: Loans to employees **, at 30 Sep 2026
R964 | page 20 | line 1465 | NUMBER | 6.28 | [I2] cons note 8c/d loans, other fin assets: Loans to employees **, at 31 Mar 2026
R965 | page 20 | line 1467 | NUMBER | 934.71 | [I2] cons note 8c/d loans, other fin assets: Total loans, at 30 Sep 2026
R966 | page 20 | line 1467 | NUMBER | 903.33 | [I2] cons note 8c/d loans, other fin assets: Total loans, at 31 Mar 2026
R967 | page 20 | line 1480 | NUMBER | 42.26 | [I2] cons note 8c/d loans, other fin assets: Security deposits, at 30 Sep 2026
R968 | page 20 | line 1480 | NUMBER | 36.64 | [I2] cons note 8c/d loans, other fin assets: Security deposits, at 31 Mar 2026
R969 | page 20 | line 1481 | NUMBER | 723.51 | [I2] cons note 8c/d loans, other fin assets: Deposits with remaining maturity for more tha, at 30 Sep 2026
R970 | page 20 | line 1481 | NUMBER | 700.31 | [I2] cons note 8c/d loans, other fin assets: Deposits with remaining maturity for more tha, at 31 Mar 2026
R971 | page 20 | line 1482 | NUMBER | 765.77 | [I2] cons note 8c/d loans, other fin assets: Total, at 30 Sep 2026
R972 | page 20 | line 1482 | NUMBER | 736.95 | [I2] cons note 8c/d loans, other fin assets: Total, at 31 Mar 2026
R973 | page 20 | line 1485 | NUMBER | 45.33 | [I2] cons note 8c/d loans, other fin assets: Security deposits, at 30 Sep 2026
R974 | page 20 | line 1485 | NUMBER | 44.55 | [I2] cons note 8c/d loans, other fin assets: Security deposits, at 31 Mar 2026
R975 | page 20 | line 1486 | NUMBER | 65.98 | [I2] cons note 8c/d loans, other fin assets: Amount recoverable from payment gateway, at 30 Sep 2026
R976 | page 20 | line 1486 | NUMBER | 218.03 | [I2] cons note 8c/d loans, other fin assets: Amount recoverable from payment gateway, at 31 Mar 2026
R977 | page 20 | line 1487 | NUMBER | 0.07 | [I2] cons note 8c/d loans, other fin assets: Other receivables, at 30 Sep 2026
R978 | page 20 | line 1487 | NUMBER | - | [I2] cons note 8c/d loans, other fin assets: Other receivables, at 31 Mar 2026 | ZERO_STANDING
R979 | page 20 | line 1488 | NUMBER | 111.38 | [I2] cons note 8c/d loans, other fin assets: Total, at 30 Sep 2026
R980 | page 20 | line 1488 | NUMBER | 262.58 | [I2] cons note 8c/d loans, other fin assets: Total, at 31 Mar 2026
R981 | page 20 | line 1491 | NUMBER | 3 to 9 years | [I2] stated in note text: Security deposits are non-interest beari
R982 | page 27 | line 1876 | NUMBER | 22,924.94 | [I2] cons note 28 fair value: Level1, at 30 Sep 2026
R983 | page 27 | line 1876 | NUMBER | 24,319.52 | [I2] cons note 28 fair value: Level1, at 31 Mar 2026
R984 | page 27 | line 1906 | NUMBER | 7,070.13 | [I2] cons note 28 fair value: - Investment in bonds & debentures (Refer Not, at 30 Sep 2026
R985 | page 27 | line 1906 | NUMBER | 5,974.53 | [I2] cons note 28 fair value: - Investment in bonds & debentures (Refer Not, at 31 Mar 2026
R986 | page 27 | line 1876 | NUMBER | 4,615.38 | [I2] cons note 28 fair value: Level3, at 30 Sep 2026
R987 | page 27 | line 1876 | NUMBER | 4,029.05 | [I2] cons note 28 fair value: Level3, at 31 Mar 2026
R988 | page 27 | line 1876 | NUMBER | - | [I2] cons note 28 fair value: Level3, at 30 Sep 2026 | ZERO_STANDING
R989 | page 27 | line 1876 | NUMBER | 50.00 | [I2] cons note 28 fair value: Level3, at 31 Mar 2026
R990 | page 27 | line 1876 | NUMBER | 34,610.45 | [I2] cons note 28 fair value: Level3, at 30 Sep 2026
R991 | page 27 | line 1876 | NUMBER | 34,373.10 | [I2] cons note 28 fair value: Level3, at 31 Mar 2026
R992 | page 27 | line 1912 | NUMBER | 91.99 | [I2] cons note 28 fair value: - Investment in TREPS, at 30 Sep 2026
R993 | page 27 | line 1912 | NUMBER | - | [I2] cons note 28 fair value: - Investment in TREPS, at 31 Mar 2026 | ZERO_STANDING
R994 | page 27 | line 1913 | NUMBER | 42.16 | [I2] cons note 28 fair value: - Trade receivables, at 30 Sep 2026
R995 | page 27 | line 1913 | NUMBER | 54.95 | [I2] cons note 28 fair value: - Trade receivables, at 31 Mar 2026
R996 | page 27 | line 1914 | NUMBER | 380.61 | [I2] cons note 28 fair value: - Cash and cash equivalents, at 30 Sep 2026
R997 | page 27 | line 1914 | NUMBER | 804.13 | [I2] cons note 28 fair value: - Cash and cash equivalents, at 31 Mar 2026
R998 | page 27 | line 1915 | NUMBER | 6.43 | [I2] cons note 28 fair value: - Loans to employees, at 30 Sep 2026
R999 | page 27 | line 1915 | NUMBER | 7.49 | [I2] cons note 28 fair value: - Loans to employees, at 31 Mar 2026
R1000 | page 27 | line 1916 | NUMBER | 928.28 | [I2] cons note 28 fair value: - Inter-corporate deposits and Loans, at 30 Sep 2026
R1001 | page 27 | line 1916 | NUMBER | 895.84 | [I2] cons note 28 fair value: - Inter-corporate deposits and Loans, at 31 Mar 2026
R1002 | page 27 | line 1917 | NUMBER | 87.59 | [I2] cons note 28 fair value: - Security deposits, at 30 Sep 2026
R1003 | page 27 | line 1917 | NUMBER | 81.19 | [I2] cons note 28 fair value: - Security deposits, at 31 Mar 2026
R1004 | page 27 | line 1918 | NUMBER | 939.95 | [I2] cons note 28 fair value: - Deposits with Banks, at 30 Sep 2026
R1005 | page 27 | line 1918 | NUMBER | 808.17 | [I2] cons note 28 fair value: - Deposits with Banks, at 31 Mar 2026
R1006 | page 27 | line 1919 | NUMBER | 66.05 | [I2] cons note 28 fair value: - Other financial assets, at 30 Sep 2026
R1007 | page 27 | line 1919 | NUMBER | 218.03 | [I2] cons note 28 fair value: - Other financial assets, at 31 Mar 2026
R1008 | page 27 | line 1919 | NUMBER | 2,543.06 | [I2] cons note 28 fair value: - Other financial assets, at 30 Sep 2026
R1009 | page 27 | line 1919 | NUMBER | 2,869.80 | [I2] cons note 28 fair value: - Other financial assets, at 31 Mar 2026
R1010 | page 27 | line 1921 | NUMBER | 37,153.51 | [I2] cons note 28 fair value: Total financial assets (a+b), at 30 Sep 2026
R1011 | page 27 | line 1921 | NUMBER | 37,242.90 | [I2] cons note 28 fair value: Total financial assets (a+b), at 31 Mar 2026
R1012 | page 27 | line 1927 | NUMBER | 368.69 | [I2] cons note 28 fair value: - Trade payables, at 30 Sep 2026
R1013 | page 27 | line 1927 | NUMBER | 319.81 | [I2] cons note 28 fair value: - Trade payables, at 31 Mar 2026
R1014 | page 27 | line 1928 | NUMBER | 189.85 | [I2] cons note 28 fair value: - Other financial liabilities, at 30 Sep 2026
R1015 | page 27 | line 1928 | NUMBER | 246.61 | [I2] cons note 28 fair value: - Other financial liabilities, at 31 Mar 2026
R1016 | page 27 | line 1929 | NUMBER | 201.09 | [I2] cons note 28 fair value: - Lease liabilities, at 30 Sep 2026
R1017 | page 27 | line 1929 | NUMBER | 231.02 | [I2] cons note 28 fair value: - Lease liabilities, at 31 Mar 2026
R1018 | page 27 | line 1930 | NUMBER | 759.63 | [I2] cons note 28 fair value: Total financial liabilities, at 30 Sep 2026
R1019 | page 27 | line 1930 | NUMBER | 797.44 | [I2] cons note 28 fair value: Total financial liabilities, at 31 Mar 2026
R1020 | page 27 | line 1962 | NUMBER | 4,665.38 | [I2] cons note 28d Level 3 reconciliation: Opening balance, qtr Sep 2026 (columns fixed from page render)
R1021 | page 27 | line 1962 | NUMBER | 3,073.59 | [I2] cons note 28d Level 3 reconciliation: Opening balance, qtr Sep 2025 (columns fixed from page render)
R1022 | page 27 | line 1962 | NUMBER | 4,079.05 | [I2] cons note 28d Level 3 reconciliation: Opening balance, 6M Sep 2026 (columns fixed from page render)
R1023 | page 27 | line 1962 | NUMBER | 4,201.96 | [I2] cons note 28d Level 3 reconciliation: Opening balance, 6M Sep 2025 (columns fixed from page render)
R1024 | page 27 | line 1963 | NUMBER | - | [I2] cons note 28d Level 3 reconciliation: Fair value gain/(loss) recognised in profit or loss (net), qtr Sep 2026 (columns fixed from page render) | ZERO_STANDING
R1025 | page 27 | line 1963 | NUMBER | - | [I2] cons note 28d Level 3 reconciliation: Fair value gain/(loss) recognised in profit or loss (net), qtr Sep 2025 (columns fixed from page render) | ZERO_STANDING
R1026 | page 27 | line 1963 | NUMBER | (71.49) | [I2] cons note 28d Level 3 reconciliation: Fair value gain/(loss) recognised in profit or loss (net), 6M Sep 2026 (columns fixed from page render)
R1027 | page 27 | line 1963 | NUMBER | - | [I2] cons note 28d Level 3 reconciliation: Fair value gain/(loss) recognised in profit or loss (net), 6M Sep 2025 (columns fixed from page render) | ZERO_STANDING
R1028 | page 27 | line 1964 | NUMBER | - | [I2] cons note 28d Level 3 reconciliation: Change in status of investment to Other entity, qtr Sep 2026 (columns fixed from page render) | ZERO_STANDING
R1029 | page 27 | line 1964 | NUMBER | - | [I2] cons note 28d Level 3 reconciliation: Change in status of investment to Other entity, qtr Sep 2025 (columns fixed from page render) | ZERO_STANDING
R1030 | page 27 | line 1964 | NUMBER | 657.82 | [I2] cons note 28d Level 3 reconciliation: Change in status of investment to Other entity, 6M Sep 2026 (columns fixed from page render)
R1031 | page 27 | line 1964 | NUMBER | - | [I2] cons note 28d Level 3 reconciliation: Change in status of investment to Other entity, 6M Sep 2025 (columns fixed from page render) | ZERO_STANDING
R1032 | page 27 | line 1965 | NUMBER | - | [I2] cons note 28d Level 3 reconciliation: Change in status of investment to Associate, qtr Sep 2026 (columns fixed from page render) | ZERO_STANDING
R1033 | page 27 | line 1965 | NUMBER | - | [I2] cons note 28d Level 3 reconciliation: Change in status of investment to Associate, qtr Sep 2025 (columns fixed from page render) | ZERO_STANDING
R1034 | page 27 | line 1965 | NUMBER | - | [I2] cons note 28d Level 3 reconciliation: Change in status of investment to Associate, 6M Sep 2026 (columns fixed from page render) | ZERO_STANDING
R1035 | page 27 | line 1965 | NUMBER | (1,128.37) | [I2] cons note 28d Level 3 reconciliation: Change in status of investment to Associate, 6M Sep 2025 (columns fixed from page render)
R1036 | page 27 | line 1966 | NUMBER | (50.00) | [I2] cons note 28d Level 3 reconciliation: Conversion (refer note 7), qtr Sep 2026 (columns fixed from page render)
R1037 | page 27 | line 1966 | NUMBER | - | [I2] cons note 28d Level 3 reconciliation: Conversion (refer note 7), qtr Sep 2025 (columns fixed from page render) | ZERO_STANDING
R1038 | page 27 | line 1966 | NUMBER | (50.00) | [I2] cons note 28d Level 3 reconciliation: Conversion (refer note 7), 6M Sep 2026 (columns fixed from page render)
R1039 | page 27 | line 1966 | NUMBER | - | [I2] cons note 28d Level 3 reconciliation: Conversion (refer note 7), 6M Sep 2025 (columns fixed from page render) | ZERO_STANDING
R1040 | page 27 | line 1967 | NUMBER | 4,615.38 | [I2] cons note 28d Level 3 reconciliation: Closing balance, qtr Sep 2026 (columns fixed from page render)
R1041 | page 27 | line 1967 | NUMBER | 3,073.59 | [I2] cons note 28d Level 3 reconciliation: Closing balance, qtr Sep 2025 (columns fixed from page render)
R1042 | page 27 | line 1967 | NUMBER | 4,615.38 | [I2] cons note 28d Level 3 reconciliation: Closing balance, 6M Sep 2026 (columns fixed from page render)
R1043 | page 27 | line 1967 | NUMBER | 3,073.59 | [I2] cons note 28d Level 3 reconciliation: Closing balance, 6M Sep 2025 (columns fixed from page render)
R1044 | page 46 | line 3169 | NUMBER | 1,10,000 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, units at 30 Sep 2026
R1045 | page 46 | line 3169 | NUMBER | 1.10 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, amount at 30 Sep 2026
R1046 | page 46 | line 3169 | NUMBER | 1,10,000 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, units at 31 Mar 2026
R1047 | page 46 | line 3169 | NUMBER | 1.10 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, amount at 31 Mar 2026
R1048 | page 46 | line 3169 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each
R1049 | page 46 | line 3170 | NUMBER | 78,70,000 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (refer note (v) , units at 30 Sep 2026
R1050 | page 46 | line 3170 | NUMBER | 128.06 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (refer note (v) , amount at 30 Sep 2026
R1051 | page 46 | line 3170 | NUMBER | - | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (refer note (v) , units at 31 Mar 2026 | ZERO_STANDING
R1052 | page 46 | line 3170 | NUMBER | - | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (refer note (v) , amount at 31 Mar 2026 | ZERO_STANDING
R1053 | page 46 | line 3170 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (refer note (v) 
R1054 | page 46 | line 3171 | NUMBER | 93,25,000 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Debentures of INR 10, units at 30 Sep 2026
R1055 | page 46 | line 3171 | NUMBER | 932.50 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Debentures of INR 10, amount at 30 Sep 2026
R1056 | page 46 | line 3171 | NUMBER | 93,25,000 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Debentures of INR 10, units at 31 Mar 2026
R1057 | page 46 | line 3171 | NUMBER | 932.50 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Debentures of INR 10, amount at 31 Mar 2026
R1058 | page 46 | line 3171 | NUMBER | INR 100 | [I2] face value per unit, Compulsorily Convertible Debentures of INR 10
R1059 | page 46 | line 3172 | NUMBER | 76,00,000 | [I2] stand note 7 subs+assoc: Optionally Convertible Debentures of INR 10 e, units at 30 Sep 2026
R1060 | page 46 | line 3172 | NUMBER | 190.00 | [I2] stand note 7 subs+assoc: Optionally Convertible Debentures of INR 10 e, amount at 30 Sep 2026
R1061 | page 46 | line 3172 | NUMBER | - | [I2] stand note 7 subs+assoc: Optionally Convertible Debentures of INR 10 e, units at 31 Mar 2026 | ZERO_STANDING
R1062 | page 46 | line 3172 | NUMBER | - | [I2] stand note 7 subs+assoc: Optionally Convertible Debentures of INR 10 e, amount at 31 Mar 2026 | ZERO_STANDING
R1063 | page 46 | line 3172 | NUMBER | INR 10 | [I2] face value per unit, Optionally Convertible Debentures of INR 10 e
R1064 | page 46 | line 3172 | NUMBER | INR 15 | [I2] issue premium per unit, Optionally Convertible Debentures of INR 10 e
R1065 | page 46 | line 3173 | NUMBER | 6,00,000 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Debentures of INR 10, units at 30 Sep 2026
R1066 | page 46 | line 3173 | NUMBER | 60.00 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Debentures of INR 10, amount at 30 Sep 2026
R1067 | page 46 | line 3173 | NUMBER | 1,311.66 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Debentures of INR 10, subtotal at 30 Sep 2026
R1068 | page 46 | line 3173 | NUMBER | 6,00,000 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Debentures of INR 10, units at 31 Mar 2026
R1069 | page 46 | line 3173 | NUMBER | 60.00 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Debentures of INR 10, amount at 31 Mar 2026
R1070 | page 46 | line 3173 | NUMBER | 993.60 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Debentures of INR 10, subtotal at 31 Mar 2026
R1071 | page 46 | line 3173 | NUMBER | INR 100 | [I2] face value per unit, Compulsorily Convertible Debentures of INR 10
R1072 | page 46 | line 3170 | NUMBER | 2,95,83,125 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, units at 30 Sep 2026
R1073 | page 46 | line 3170 | NUMBER | 5,070.62 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, amount at 30 Sep 2026
R1074 | page 46 | line 3170 | NUMBER | 2,95,83,125 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, units at 31 Mar 2026
R1075 | page 46 | line 3170 | NUMBER | 5,070.62 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, amount at 31 Mar 2026
R1076 | page 46 | line 3170 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each
R1077 | page 46 | line 3177 | NUMBER | 22.19 | [I2] stand note 7 subs+assoc: Add: Deemed investment (refer note (vi) below, amount at 30 Sep 2026
R1078 | page 46 | line 3177 | NUMBER | 5,092.81 | [I2] stand note 7 subs+assoc: Add: Deemed investment (refer note (vi) below, subtotal at 30 Sep 2026
R1079 | page 46 | line 3177 | NUMBER | - | [I2] stand note 7 subs+assoc: Add: Deemed investment (refer note (vi) below, units at 31 Mar 2026 | ZERO_STANDING
R1080 | page 46 | line 3177 | NUMBER | 16.56 | [I2] stand note 7 subs+assoc: Add: Deemed investment (refer note (vi) below, amount at 31 Mar 2026
R1081 | page 46 | line 3177 | NUMBER | 5,087.18 | [I2] stand note 7 subs+assoc: Add: Deemed investment (refer note (vi) below, subtotal at 31 Mar 2026
R1082 | page 46 | line 3176 | NUMBER | 1,00,000 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, units at 30 Sep 2026
R1083 | page 46 | line 3176 | NUMBER | 1.00 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, amount at 30 Sep 2026
R1084 | page 46 | line 3176 | NUMBER | 1.00 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, subtotal at 30 Sep 2026
R1085 | page 46 | line 3176 | NUMBER | 1,00,000 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, units at 31 Mar 2026
R1086 | page 46 | line 3176 | NUMBER | 1.00 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, amount at 31 Mar 2026
R1087 | page 46 | line 3176 | NUMBER | 1.00 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, subtotal at 31 Mar 2026
R1088 | page 46 | line 3176 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each
R1089 | page 46 | line 3185 | NUMBER | 1,20,50,000 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (refer note (iii, units at 30 Sep 2026
R1090 | page 46 | line 3185 | NUMBER | 120.50 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (refer note (iii, amount at 30 Sep 2026
R1091 | page 46 | line 3185 | NUMBER | 120.50 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (refer note (iii, subtotal at 30 Sep 2026
R1092 | page 46 | line 3185 | NUMBER | - | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (refer note (iii, units at 31 Mar 2026 | ZERO_STANDING
R1093 | page 46 | line 3185 | NUMBER | - | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (refer note (iii, amount at 31 Mar 2026 | ZERO_STANDING
R1094 | page 46 | line 3185 | NUMBER | - | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (refer note (iii, subtotal at 31 Mar 2026 | ZERO_STANDING
R1095 | page 46 | line 3185 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (refer note (iii
R1096 | page 46 | line 3188 | NUMBER | 6,843 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Preference Shares of, units at 30 Sep 2026
R1097 | page 46 | line 3188 | NUMBER | 350.01 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Preference Shares of, amount at 30 Sep 2026
R1098 | page 46 | line 3188 | NUMBER | 6,843 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Preference Shares of, units at 31 Mar 2026
R1099 | page 46 | line 3188 | NUMBER | 350.01 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Preference Shares of, amount at 31 Mar 2026
R1100 | page 46 | line 3188 | NUMBER | INR 10 | [I2] face value per unit, Compulsorily Convertible Preference Shares of
R1101 | page 46 | line 3188 | NUMBER | INR 51,138 | [I2] issue premium per unit, Compulsorily Convertible Preference Shares of
R1102 | page 46 | line 3189 | NUMBER | 2,147 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1103 | page 46 | line 3189 | NUMBER | 109.81 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1104 | page 46 | line 3189 | NUMBER | 2,147 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1105 | page 46 | line 3189 | NUMBER | 109.81 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1106 | page 46 | line 3189 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1107 | page 46 | line 3189 | NUMBER | INR 51,138 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1108 | page 46 | line 3190 | NUMBER | 7,853 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1109 | page 46 | line 3190 | NUMBER | 403.57 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1110 | page 46 | line 3190 | NUMBER | 7,853 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1111 | page 46 | line 3190 | NUMBER | 403.57 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1112 | page 46 | line 3190 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1113 | page 46 | line 3190 | NUMBER | INR 51,135 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1114 | page 46 | line 3191 | NUMBER | 1,759 | [I2] stand note 7 subs+assoc: 0.001% Optionally Convertible Debentures of I, units at 30 Sep 2026
R1115 | page 46 | line 3191 | NUMBER | 90.00 | [I2] stand note 7 subs+assoc: 0.001% Optionally Convertible Debentures of I, amount at 30 Sep 2026
R1116 | page 46 | line 3191 | NUMBER | 1,759 | [I2] stand note 7 subs+assoc: 0.001% Optionally Convertible Debentures of I, units at 31 Mar 2026
R1117 | page 46 | line 3191 | NUMBER | 90.00 | [I2] stand note 7 subs+assoc: 0.001% Optionally Convertible Debentures of I, amount at 31 Mar 2026
R1118 | page 46 | line 3191 | NUMBER | INR 10 | [I2] face value per unit, 0.001% Optionally Convertible Debentures of I
R1119 | page 46 | line 3191 | NUMBER | INR 51,157 | [I2] issue premium per unit, 0.001% Optionally Convertible Debentures of I
R1120 | page 46 | line 3191 | NUMBER | 0.001% | [I2] instrument coupon, 0.001% Optionally Convertible Debentures of I
R1121 | page 46 | line 3192 | NUMBER | 1,172 | [I2] stand note 7 subs+assoc: 0.001% Optionally Convertible Debentures of I, units at 30 Sep 2026
R1122 | page 46 | line 3192 | NUMBER | 59.97 | [I2] stand note 7 subs+assoc: 0.001% Optionally Convertible Debentures of I, amount at 30 Sep 2026
R1123 | page 46 | line 3192 | NUMBER | - | [I2] stand note 7 subs+assoc: 0.001% Optionally Convertible Debentures of I, units at 31 Mar 2026 | ZERO_STANDING
R1124 | page 46 | line 3192 | NUMBER | - | [I2] stand note 7 subs+assoc: 0.001% Optionally Convertible Debentures of I, amount at 31 Mar 2026 | ZERO_STANDING
R1125 | page 46 | line 3192 | NUMBER | INR 10 | [I2] face value per unit, 0.001% Optionally Convertible Debentures of I
R1126 | page 46 | line 3192 | NUMBER | INR 51,157 | [I2] issue premium per unit, 0.001% Optionally Convertible Debentures of I
R1127 | page 46 | line 3192 | NUMBER | 0.001% | [I2] instrument coupon, 0.001% Optionally Convertible Debentures of I
R1128 | page 46 | line 3193 | NUMBER | - | [I2] stand note 7 subs+assoc: Add: Deemed investment (refer note (vi) below, units at 30 Sep 2026 | ZERO_STANDING
R1129 | page 46 | line 3193 | NUMBER | 12.48 | [I2] stand note 7 subs+assoc: Add: Deemed investment (refer note (vi) below, amount at 30 Sep 2026
R1130 | page 46 | line 3193 | NUMBER | - | [I2] stand note 7 subs+assoc: Add: Deemed investment (refer note (vi) below, units at 31 Mar 2026 | ZERO_STANDING
R1131 | page 46 | line 3193 | NUMBER | 10.40 | [I2] stand note 7 subs+assoc: Add: Deemed investment (refer note (vi) below, amount at 31 Mar 2026
R1132 | page 46 | line 3194 | NUMBER | (52.61) | [I2] stand note 7 subs+assoc: Less: Impairment allowance, amount at 30 Sep 2026
R1133 | page 46 | line 3194 | NUMBER | 973.23 | [I2] stand note 7 subs+assoc: Less: Impairment allowance, carrying total at 30 Sep 2026
R1134 | page 46 | line 3194 | NUMBER | (52.61) | [I2] stand note 7 subs+assoc: Less: Impairment allowance, amount at 31 Mar 2026
R1135 | page 46 | line 3194 | NUMBER | 911.18 | [I2] stand note 7 subs+assoc: Less: Impairment allowance, carrying total at 31 Mar 2026
R1136 | page 46 | line 3181 | NUMBER | 1,00,000 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, units at 30 Sep 2026
R1137 | page 46 | line 3181 | NUMBER | 1.00 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, amount at 30 Sep 2026
R1138 | page 46 | line 3181 | NUMBER | 1,00,000 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, units at 31 Mar 2026
R1139 | page 46 | line 3181 | NUMBER | 1.00 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each, amount at 31 Mar 2026
R1140 | page 46 | line 3181 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each
R1141 | page 46 | line 3198 | NUMBER | 7,50,000 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Preference Shares of, units at 30 Sep 2026
R1142 | page 46 | line 3198 | NUMBER | 7.50 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Preference Shares of, amount at 30 Sep 2026
R1143 | page 46 | line 3198 | NUMBER | 7,50,000 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Preference Shares of, units at 31 Mar 2026
R1144 | page 46 | line 3198 | NUMBER | 7.50 | [I2] stand note 7 subs+assoc: Compulsorily Convertible Preference Shares of, amount at 31 Mar 2026
R1145 | page 46 | line 3198 | NUMBER | INR 10 | [I2] face value per unit, Compulsorily Convertible Preference Shares of
R1146 | page 46 | line 3199 | NUMBER | 24,00,000 | [I2] stand note 7 subs+assoc: 0.001% optionally convertible Debentures of I, units at 30 Sep 2026
R1147 | page 46 | line 3199 | NUMBER | 60.00 | [I2] stand note 7 subs+assoc: 0.001% optionally convertible Debentures of I, amount at 30 Sep 2026
R1148 | page 46 | line 3199 | NUMBER | 24,00,000 | [I2] stand note 7 subs+assoc: 0.001% optionally convertible Debentures of I, units at 31 Mar 2026
R1149 | page 46 | line 3199 | NUMBER | 60.00 | [I2] stand note 7 subs+assoc: 0.001% optionally convertible Debentures of I, amount at 31 Mar 2026
R1150 | page 46 | line 3199 | NUMBER | INR 10 | [I2] face value per unit, 0.001% optionally convertible Debentures of I
R1151 | page 46 | line 3199 | NUMBER | INR 15 | [I2] issue premium per unit, 0.001% optionally convertible Debentures of I
R1152 | page 46 | line 3199 | NUMBER | 0.001% | [I2] instrument coupon, 0.001% optionally convertible Debentures of I
R1153 | page 46 | line 3201 | NUMBER | 25,00,000 | [I2] stand note 7 subs+assoc: Compulsory Convertible Debentures (CCD) of Rs, units at 30 Sep 2026
R1154 | page 46 | line 3201 | NUMBER | 25.00 | [I2] stand note 7 subs+assoc: Compulsory Convertible Debentures (CCD) of Rs, amount at 30 Sep 2026
R1155 | page 46 | line 3201 | NUMBER | 93.50 | [I2] stand note 7 subs+assoc: Compulsory Convertible Debentures (CCD) of Rs, subtotal at 30 Sep 2026
R1156 | page 46 | line 3201 | NUMBER | 25,00,000 | [I2] stand note 7 subs+assoc: Compulsory Convertible Debentures (CCD) of Rs, units at 31 Mar 2026
R1157 | page 46 | line 3201 | NUMBER | 25.00 | [I2] stand note 7 subs+assoc: Compulsory Convertible Debentures (CCD) of Rs, amount at 31 Mar 2026
R1158 | page 46 | line 3201 | NUMBER | 93.50 | [I2] stand note 7 subs+assoc: Compulsory Convertible Debentures (CCD) of Rs, subtotal at 31 Mar 2026
R1159 | page 46 | line 3201 | NUMBER | INR 10 | [I2] face value per unit, Compulsory Convertible Debentures (CCD) of Rs
R1160 | page 46 | line 3201 | NUMBER | 7,592.70 | [I2] stand note 7 subs+assoc: y Convertible Debentures (CCD) of Rs 10/-each, amount at 30 Sep 2026
R1161 | page 46 | line 3201 | NUMBER | 7,086.46 | [I2] stand note 7 subs+assoc: y Convertible Debentures (CCD) of Rs 10/-each, amount at 31 Mar 2026
R1162 | page 46 | line 3207 | NUMBER | 5,954 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1163 | page 46 | line 3207 | NUMBER | 311.50 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1164 | page 46 | line 3207 | NUMBER | 5,954 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1165 | page 46 | line 3207 | NUMBER | 311.50 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1166 | page 46 | line 3207 | NUMBER | INR 100 | [I2] face value per unit, Compulsory convertible preference shares of I
R1167 | page 46 | line 3207 | NUMBER | INR 52,217.90 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1168 | page 46 | line 3209 | NUMBER | 1,13,126 | [I2] stand note 7 subs+assoc: Bonus shares received on above Compulsory con, units at 30 Sep 2026
R1169 | page 46 | line 3209 | NUMBER | - | [I2] stand note 7 subs+assoc: Bonus shares received on above Compulsory con, amount at 30 Sep 2026 | ZERO_STANDING
R1170 | page 46 | line 3209 | NUMBER | 1,13,126 | [I2] stand note 7 subs+assoc: Bonus shares received on above Compulsory con, units at 31 Mar 2026
R1171 | page 46 | line 3209 | NUMBER | - | [I2] stand note 7 subs+assoc: Bonus shares received on above Compulsory con, amount at 31 Mar 2026 | ZERO_STANDING
R1172 | page 46 | line 3210 | NUMBER | 10 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1173 | page 46 | line 3210 | NUMBER | 0.52 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1174 | page 46 | line 3210 | NUMBER | 10 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1175 | page 46 | line 3210 | NUMBER | 0.52 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1176 | page 46 | line 3210 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1177 | page 46 | line 3210 | NUMBER | INR 52,307.90 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1178 | page 46 | line 3211 | NUMBER | 190 | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, units at 30 Sep 2026
R1179 | page 46 | line 3211 | NUMBER | - | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, amount at 30 Sep 2026 | ZERO_STANDING
R1180 | page 46 | line 3211 | NUMBER | 190 | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, units at 31 Mar 2026
R1181 | page 46 | line 3211 | NUMBER | - | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, amount at 31 Mar 2026 | ZERO_STANDING
R1182 | page 46 | line 3209 | NUMBER | 1,809 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1183 | page 46 | line 3209 | NUMBER | 525.26 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1184 | page 46 | line 3209 | NUMBER | 1,809 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1185 | page 46 | line 3209 | NUMBER | 525.26 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1186 | page 46 | line 3209 | NUMBER | INR 100 | [I2] face value per unit, Compulsory convertible preference shares of I
R1187 | page 46 | line 3209 | NUMBER | INR 290,261 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1188 | page 46 | line 3214 | NUMBER | 34,371 | [I2] stand note 7 subs+assoc: Bonus shares received on above Compulsory con, units at 30 Sep 2026
R1189 | page 46 | line 3214 | NUMBER | - | [I2] stand note 7 subs+assoc: Bonus shares received on above Compulsory con, amount at 30 Sep 2026 | ZERO_STANDING
R1190 | page 46 | line 3214 | NUMBER | 34,371 | [I2] stand note 7 subs+assoc: Bonus shares received on above Compulsory con, units at 31 Mar 2026
R1191 | page 46 | line 3214 | NUMBER | - | [I2] stand note 7 subs+assoc: Bonus shares received on above Compulsory con, amount at 31 Mar 2026 | ZERO_STANDING
R1192 | page 46 | line 3215 | NUMBER | 444 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1193 | page 46 | line 3215 | NUMBER | 90.24 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1194 | page 46 | line 3215 | NUMBER | 444 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1195 | page 46 | line 3215 | NUMBER | 90.24 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1196 | page 46 | line 3215 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1197 | page 46 | line 3215 | NUMBER | INR 203,242 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1198 | page 46 | line 3216 | NUMBER | 8,436 | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, units at 30 Sep 2026
R1199 | page 46 | line 3216 | NUMBER | - | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, amount at 30 Sep 2026 | ZERO_STANDING
R1200 | page 46 | line 3216 | NUMBER | 8,436 | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, units at 31 Mar 2026
R1201 | page 46 | line 3216 | NUMBER | - | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, amount at 31 Mar 2026 | ZERO_STANDING
R1202 | page 46 | line 3217 | NUMBER | 137 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1203 | page 46 | line 3217 | NUMBER | 39.78 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1204 | page 46 | line 3217 | NUMBER | 137 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1205 | page 46 | line 3217 | NUMBER | 39.78 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1206 | page 46 | line 3217 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1207 | page 46 | line 3217 | NUMBER | INR 290,351 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1208 | page 46 | line 3218 | NUMBER | 2,603 | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, units at 30 Sep 2026
R1209 | page 46 | line 3218 | NUMBER | - | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, amount at 30 Sep 2026 | ZERO_STANDING
R1210 | page 46 | line 3218 | NUMBER | 2,603 | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, units at 31 Mar 2026
R1211 | page 46 | line 3218 | NUMBER | - | [I2] stand note 7 subs+assoc: Bonus shares received on above Equity shares, amount at 31 Mar 2026 | ZERO_STANDING
R1212 | page 46 | line 3212 | NUMBER | 2,750 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1213 | page 46 | line 3212 | NUMBER | 57.45 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1214 | page 46 | line 3212 | NUMBER | 2,750 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1215 | page 46 | line 3212 | NUMBER | 57.45 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1216 | page 46 | line 3212 | NUMBER | INR 100 | [I2] face value per unit, Compulsory convertible preference shares of I
R1217 | page 46 | line 3212 | NUMBER | INR 20,789.66 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1218 | page 46 | line 3214 | NUMBER | 2,814 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1219 | page 46 | line 3214 | NUMBER | 40.85 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1220 | page 46 | line 3214 | NUMBER | 2,814 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1221 | page 46 | line 3214 | NUMBER | 40.85 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1222 | page 46 | line 3214 | NUMBER | INR 100 | [I2] face value per unit, Compulsory convertible preference shares of I
R1223 | page 46 | line 3214 | NUMBER | INR 14,417.80 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1224 | page 46 | line 3223 | NUMBER | 935 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1225 | page 46 | line 3223 | NUMBER | 13.57 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1226 | page 46 | line 3223 | NUMBER | 1,079.17 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, subtotal at 30 Sep 2026
R1227 | page 46 | line 3223 | NUMBER | 935 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1228 | page 46 | line 3223 | NUMBER | 13.57 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1229 | page 46 | line 3223 | NUMBER | 1,079.17 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, subtotal at 31 Mar 2026
R1230 | page 46 | line 3223 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1231 | page 46 | line 3223 | NUMBER | INR 14,507.80 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1232 | page 46 | line 3219 | NUMBER | 1,28,593 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1233 | page 46 | line 3219 | NUMBER | 99.92 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1234 | page 46 | line 3219 | NUMBER | 1,28,593 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1235 | page 46 | line 3219 | NUMBER | 99.92 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1236 | page 46 | line 3219 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R1237 | page 46 | line 3219 | NUMBER | INR 776 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1238 | page 46 | line 3227 | NUMBER | 100 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R1239 | page 46 | line 3227 | NUMBER | 0.07 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R1240 | page 46 | line 3227 | NUMBER | 100 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R1241 | page 46 | line 3227 | NUMBER | 0.07 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R1242 | page 46 | line 3227 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R1243 | page 46 | line 3227 | NUMBER | INR 776 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R1244 | page 46 | line 3221 | NUMBER | 1,19,474 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1245 | page 46 | line 3221 | NUMBER | 100.00 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1246 | page 46 | line 3221 | NUMBER | 1,19,474 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1247 | page 46 | line 3221 | NUMBER | 100.00 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1248 | page 46 | line 3221 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R1249 | page 46 | line 3221 | NUMBER | INR 836 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1250 | page 46 | line 3226 | NUMBER | 1,05,607 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1251 | page 46 | line 3226 | NUMBER | 129.20 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1252 | page 46 | line 3226 | NUMBER | 1,05,607 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1253 | page 46 | line 3226 | NUMBER | 129.20 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1254 | page 46 | line 3226 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R1255 | page 46 | line 3226 | NUMBER | INR 1,222 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1256 | page 46 | line 3230 | NUMBER | 17,750 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R1257 | page 46 | line 3230 | NUMBER | 14.86 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R1258 | page 46 | line 3230 | NUMBER | 17,750 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R1259 | page 46 | line 3230 | NUMBER | 14.86 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R1260 | page 46 | line 3230 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R1261 | page 46 | line 3230 | NUMBER | INR 837 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R1262 | page 46 | line 3231 | NUMBER | 17,963 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R1263 | page 46 | line 3231 | NUMBER | 21.98 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R1264 | page 46 | line 3231 | NUMBER | 17,963 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R1265 | page 46 | line 3231 | NUMBER | 21.98 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R1266 | page 46 | line 3231 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R1267 | page 46 | line 3231 | NUMBER | INR 1,222 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R1268 | page 46 | line 3228 | NUMBER | 45,407 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1269 | page 46 | line 3228 | NUMBER | 80.00 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1270 | page 46 | line 3228 | NUMBER | 45,407 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1271 | page 46 | line 3228 | NUMBER | 80.00 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1272 | page 46 | line 3228 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R1273 | page 46 | line 3228 | NUMBER | INR 1,760.83 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1274 | page 46 | line 3229 | NUMBER | 42,697 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1275 | page 46 | line 3229 | NUMBER | 80.00 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1276 | page 46 | line 3229 | NUMBER | 42,697 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1277 | page 46 | line 3229 | NUMBER | 80.00 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1278 | page 46 | line 3229 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R1279 | page 46 | line 3229 | NUMBER | INR 1,872.68 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1280 | page 46 | line 3236 | NUMBER | 100 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R1281 | page 46 | line 3236 | NUMBER | 0.16 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R1282 | page 46 | line 3236 | NUMBER | 100 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R1283 | page 46 | line 3236 | NUMBER | 0.16 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R1284 | page 46 | line 3236 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R1285 | page 46 | line 3236 | NUMBER | INR 1,552.74 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R1286 | page 46 | line 3237 | NUMBER | 21,811 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R1287 | page 46 | line 3237 | NUMBER | 51.30 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R1288 | page 46 | line 3237 | NUMBER | 21,811 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R1289 | page 46 | line 3237 | NUMBER | 51.30 | [I2] stand note 7 subs+assoc: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R1290 | page 46 | line 3237 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R1291 | page 46 | line 3237 | NUMBER | INR 2,352 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R1292 | page 46 | line 3232 | NUMBER | 91,804 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1293 | page 46 | line 3232 | NUMBER | 142.64 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1294 | page 46 | line 3232 | NUMBER | 91,804 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1295 | page 46 | line 3232 | NUMBER | 142.64 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1296 | page 46 | line 3232 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible preference shares of I
R1297 | page 46 | line 3232 | NUMBER | INR 1552.74 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1298 | page 46 | line 3240 | NUMBER | - | [I2] stand note 7 subs+assoc: Fair value gain recognised through profit and, units at 30 Sep 2026 | ZERO_STANDING
R1299 | page 46 | line 3240 | NUMBER | 97.87 | [I2] stand note 7 subs+assoc: Fair value gain recognised through profit and, amount at 30 Sep 2026
R1300 | page 46 | line 3240 | NUMBER | 818.00 | [I2] stand note 7 subs+assoc: Fair value gain recognised through profit and, subtotal at 30 Sep 2026
R1301 | page 46 | line 3240 | NUMBER | - | [I2] stand note 7 subs+assoc: Fair value gain recognised through profit and, units at 31 Mar 2026 | ZERO_STANDING
R1302 | page 46 | line 3240 | NUMBER | 97.87 | [I2] stand note 7 subs+assoc: Fair value gain recognised through profit and, amount at 31 Mar 2026
R1303 | page 46 | line 3240 | NUMBER | 818.00 | [I2] stand note 7 subs+assoc: Fair value gain recognised through profit and, subtotal at 31 Mar 2026
R1304 | page 46 | line 3243 | NUMBER | - | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026 | ZERO_STANDING
R1305 | page 46 | line 3243 | NUMBER | - | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026 | ZERO_STANDING
R1306 | page 46 | line 3243 | NUMBER | 8,11,250 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1307 | page 46 | line 3243 | NUMBER | 1,041.77 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1308 | page 46 | line 3243 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1309 | page 46 | line 3243 | NUMBER | INR 1,274.15 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1310 | page 46 | line 3244 | NUMBER | - | [I2] stand note 7 subs+assoc: Investment in Equity shares of INR 10 each (a, units at 30 Sep 2026 | ZERO_STANDING
R1311 | page 46 | line 3244 | NUMBER | - | [I2] stand note 7 subs+assoc: Investment in Equity shares of INR 10 each (a, amount at 30 Sep 2026 | ZERO_STANDING
R1312 | page 46 | line 3244 | NUMBER | 1,06,876 | [I2] stand note 7 subs+assoc: Investment in Equity shares of INR 10 each (a, units at 31 Mar 2026
R1313 | page 46 | line 3244 | NUMBER | 137.36 | [I2] stand note 7 subs+assoc: Investment in Equity shares of INR 10 each (a, amount at 31 Mar 2026
R1314 | page 46 | line 3244 | NUMBER | INR 10 | [I2] face value per unit, Investment in Equity shares of INR 10 each (a
R1315 | page 46 | line 3244 | NUMBER | INR 1,275.24 | [I2] issue premium per unit, Investment in Equity shares of INR 10 each (a
R1316 | page 46 | line 3245 | NUMBER | - | [I2] stand note 7 subs+assoc: Less: Impairment allowance, amount at 30 Sep 2026 | ZERO_STANDING
R1317 | page 46 | line 3245 | NUMBER | - | [I2] stand note 7 subs+assoc: Less: Impairment allowance, carrying total at 30 Sep 2026 | ZERO_STANDING
R1318 | page 46 | line 3245 | NUMBER | (392.80) | [I2] stand note 7 subs+assoc: Less: Impairment allowance, amount at 31 Mar 2026
R1319 | page 46 | line 3245 | NUMBER | 786.33 | [I2] stand note 7 subs+assoc: Less: Impairment allowance, carrying total at 31 Mar 2026
R1320 | page 46 | line 3234 | NUMBER | 10,323 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1321 | page 46 | line 3234 | NUMBER | 696.08 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1322 | page 46 | line 3234 | NUMBER | 10,323 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1323 | page 46 | line 3234 | NUMBER | 696.08 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1324 | page 46 | line 3234 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R1325 | page 46 | line 3234 | NUMBER | INR 67,420 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1326 | page 46 | line 3244 | NUMBER | 3,805 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1327 | page 46 | line 3244 | NUMBER | 218.12 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1328 | page 46 | line 3244 | NUMBER | 3,805 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1329 | page 46 | line 3244 | NUMBER | 218.12 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1330 | page 46 | line 3244 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1331 | page 46 | line 3244 | NUMBER | INR 57,315 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1332 | page 46 | line 3238 | NUMBER | 2,226 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1333 | page 46 | line 3238 | NUMBER | 208.30 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1334 | page 46 | line 3238 | NUMBER | 2,226 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1335 | page 46 | line 3238 | NUMBER | 208.30 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1336 | page 46 | line 3238 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R1337 | page 46 | line 3238 | NUMBER | INR 93,565 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1338 | page 46 | line 3248 | NUMBER | 2,921 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1339 | page 46 | line 3248 | NUMBER | 410.00 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1340 | page 46 | line 3248 | NUMBER | 2,921 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1341 | page 46 | line 3248 | NUMBER | 410.00 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1342 | page 46 | line 3248 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R1343 | page 46 | line 3248 | NUMBER | INR 140,352 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1344 | page 46 | line 3249 | NUMBER | 808 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1345 | page 46 | line 3249 | NUMBER | 75.61 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1346 | page 46 | line 3249 | NUMBER | 808 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1347 | page 46 | line 3249 | NUMBER | 75.61 | [I2] stand note 7 subs+assoc: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1348 | page 46 | line 3249 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1349 | page 46 | line 3249 | NUMBER | INR 93,565 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1350 | page 46 | line 3250 | NUMBER | 4,630 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1351 | page 46 | line 3250 | NUMBER | 649.88 | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1352 | page 46 | line 3250 | NUMBER | - | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, units at 31 Mar 2026 | ZERO_STANDING
R1353 | page 46 | line 3250 | NUMBER | - | [I2] stand note 7 subs+assoc: Compulsory convertible preference shares of I, amount at 31 Mar 2026 | ZERO_STANDING
R1354 | page 46 | line 3250 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R1355 | page 46 | line 3250 | NUMBER | INR 140,352 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1356 | page 46 | line 3254 | NUMBER | - | [I2] stand note 7 subs+assoc: Fair value loss recognised through profit and, units at 30 Sep 2026 | ZERO_STANDING
R1357 | page 46 | line 3254 | NUMBER | (68.99) | [I2] stand note 7 subs+assoc: Fair value loss recognised through profit and, amount at 30 Sep 2026
R1358 | page 46 | line 3254 | NUMBER | 2,189.00 | [I2] stand note 7 subs+assoc: Fair value loss recognised through profit and, subtotal at 30 Sep 2026
R1359 | page 46 | line 3254 | NUMBER | - | [I2] stand note 7 subs+assoc: Fair value loss recognised through profit and, units at 31 Mar 2026 | ZERO_STANDING
R1360 | page 46 | line 3254 | NUMBER | (68.99) | [I2] stand note 7 subs+assoc: Fair value loss recognised through profit and, amount at 31 Mar 2026
R1361 | page 46 | line 3254 | NUMBER | 1,539.12 | [I2] stand note 7 subs+assoc: Fair value loss recognised through profit and, subtotal at 31 Mar 2026
R1362 | page 46 | line 3254 | NUMBER | 4,086.17 | [I2] stand note 7 subs+assoc:  till the date entity has become an associate, amount at 30 Sep 2026
R1363 | page 46 | line 3254 | NUMBER | 4,222.62 | [I2] stand note 7 subs+assoc:  till the date entity has become an associate, amount at 31 Mar 2026
R1364 | page 46 | line 3256 | NUMBER | 11,678.87 | [I2] stand note 7 subs+assoc: Total Investment in subsidiaries and associat, amount at 30 Sep 2026
R1365 | page 46 | line 3256 | NUMBER | 11,309.08 | [I2] stand note 7 subs+assoc: Total Investment in subsidiaries and associat, amount at 31 Mar 2026
R1366 | page 46 | line 3258 | NUMBER | 11,678.87 | [I2] stand note 7 subs+assoc: Aggregate carrying value of unquoted investme, amount at 30 Sep 2026
R1367 | page 46 | line 3258 | NUMBER | 11,309.08 | [I2] stand note 7 subs+assoc: Aggregate carrying value of unquoted investme, amount at 31 Mar 2026
R1368 | page 46 | line 3259 | NUMBER | 52.61 | [I2] stand note 7 subs+assoc: Aggregate impairment in value of investments, amount at 30 Sep 2026
R1369 | page 46 | line 3259 | NUMBER | 445.41 | [I2] stand note 7 subs+assoc: Aggregate impairment in value of investments, amount at 31 Mar 2026
R1370 | page 47 | line 3284 | NUMBER | 55.50 | [I2] stand note 8a non-current inv: a) Investment in subsidiaries at FVTPL, amount at 30 Sep 2026
R1371 | page 47 | line 3284 | NUMBER | 183.56 | [I2] stand note 8a non-current inv: a) Investment in subsidiaries at FVTPL, amount at 31 Mar 2026
R1372 | page 47 | line 3285 | NUMBER | 3,829.52 | [I2] stand note 8a non-current inv: b) Investment in other entities at FVTPL, amount at 30 Sep 2026
R1373 | page 47 | line 3285 | NUMBER | 3,243.19 | [I2] stand note 8a non-current inv: b) Investment in other entities at FVTPL, amount at 31 Mar 2026
R1374 | page 47 | line 3308 | NUMBER | 3,885.02 | [I2] stand note 8a non-current inv: b) Investment in other entities at FVTPL, amount at 30 Sep 2026
R1375 | page 47 | line 3308 | NUMBER | 3,426.75 | [I2] stand note 8a non-current inv: b) Investment in other entities at FVTPL, amount at 31 Mar 2026
R1376 | page 47 | line 3288 | NUMBER | 18,107.35 | [I2] stand note 8a non-current inv: Investment in mutual funds and exchange trade, amount at 30 Sep 2026
R1377 | page 47 | line 3288 | NUMBER | 19,809.24 | [I2] stand note 8a non-current inv: Investment in mutual funds and exchange trade, amount at 31 Mar 2026
R1378 | page 47 | line 3289 | NUMBER | 6,149.56 | [I2] stand note 8a non-current inv: Investment in bonds and debentures at FVTPL, amount at 30 Sep 2026
R1379 | page 47 | line 3289 | NUMBER | 5,242.25 | [I2] stand note 8a non-current inv: Investment in bonds and debentures at FVTPL, amount at 31 Mar 2026
R1380 | page 47 | line 3290 | NUMBER | 3,626.13 | [I2] stand note 8a non-current inv: Investment in Government Securities- Quoted (, amount at 30 Sep 2026
R1381 | page 47 | line 3290 | NUMBER | 3,474.36 | [I2] stand note 8a non-current inv: Investment in Government Securities- Quoted (, amount at 31 Mar 2026
R1382 | page 47 | line 3291 | NUMBER | 91.99 | [I2] stand note 8a non-current inv: Invesments in TREPS (Measured at Amortised Co, amount at 30 Sep 2026
R1383 | page 47 | line 3291 | NUMBER | - | [I2] stand note 8a non-current inv: Invesments in TREPS (Measured at Amortised Co, amount at 31 Mar 2026 | ZERO_STANDING
R1384 | page 47 | line 3291 | NUMBER | 27,975.03 | [I2] stand note 8a non-current inv: esments in TREPS (Measured at Amortised Cost), amount at 30 Sep 2026
R1385 | page 47 | line 3291 | NUMBER | 28,525.85 | [I2] stand note 8a non-current inv: esments in TREPS (Measured at Amortised Cost), amount at 31 Mar 2026
R1386 | page 47 | line 3302 | NUMBER | 78,70,000 | [I2] stand note 8a non-current inv: Opening balance, units at 30 Sep 2026
R1387 | page 47 | line 3302 | NUMBER | 128.06 | [I2] stand note 8a non-current inv: Opening balance, amount at 30 Sep 2026
R1388 | page 47 | line 3302 | NUMBER | 78,70,000 | [I2] stand note 8a non-current inv: Opening balance, units at 31 Mar 2026
R1389 | page 47 | line 3302 | NUMBER | 128.06 | [I2] stand note 8a non-current inv: Opening balance, amount at 31 Mar 2026
R1390 | page 47 | line 3303 | NUMBER | (78,70,000) | [I2] stand note 8a non-current inv: Conversion during the period (refer note 7(v), units at 30 Sep 2026
R1391 | page 47 | line 3303 | NUMBER | (128.06) | [I2] stand note 8a non-current inv: Conversion during the period (refer note 7(v), amount at 30 Sep 2026
R1392 | page 47 | line 3303 | NUMBER | - | [I2] stand note 8a non-current inv: Conversion during the period (refer note 7(v), subtotal at 30 Sep 2026 | ZERO_STANDING
R1393 | page 47 | line 3303 | NUMBER | - | [I2] stand note 8a non-current inv: Conversion during the period (refer note 7(v), units at 31 Mar 2026 | ZERO_STANDING
R1394 | page 47 | line 3303 | NUMBER | - | [I2] stand note 8a non-current inv: Conversion during the period (refer note 7(v), amount at 31 Mar 2026 | ZERO_STANDING
R1395 | page 47 | line 3303 | NUMBER | 128.06 | [I2] stand note 8a non-current inv: Conversion during the period (refer note 7(v), subtotal at 31 Mar 2026
R1396 | page 47 | line 3305 | NUMBER | 27,75,000 | [I2] stand note 8a non-current inv: estment in Pay With Indiamart Private Limited, units at 30 Sep 2026
R1397 | page 47 | line 3305 | NUMBER | 55.50 | [I2] stand note 8a non-current inv: estment in Pay With Indiamart Private Limited, amount at 30 Sep 2026
R1398 | page 47 | line 3305 | NUMBER | 55.50 | [I2] stand note 8a non-current inv: estment in Pay With Indiamart Private Limited, subtotal at 30 Sep 2026
R1399 | page 47 | line 3305 | NUMBER | 27,75,000 | [I2] stand note 8a non-current inv: estment in Pay With Indiamart Private Limited, units at 31 Mar 2026
R1400 | page 47 | line 3305 | NUMBER | 55.50 | [I2] stand note 8a non-current inv: estment in Pay With Indiamart Private Limited, amount at 31 Mar 2026
R1401 | page 47 | line 3305 | NUMBER | 55.50 | [I2] stand note 8a non-current inv: estment in Pay With Indiamart Private Limited, subtotal at 31 Mar 2026
R1402 | page 47 | line 3305 | NUMBER | 183.56 | [I2] stand note 8a non-current inv: estment in Pay With Indiamart Private Limited, amount at 31 Mar 2026
R1403 | page 47 | line 3311 | NUMBER | 24,74,637 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1404 | page 47 | line 3311 | NUMBER | 240.56 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1405 | page 47 | line 3311 | NUMBER | 24,74,637 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1406 | page 47 | line 3311 | NUMBER | 240.56 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1407 | page 47 | line 3311 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1408 | page 47 | line 3311 | NUMBER | INR 87.21 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1409 | page 47 | line 3312 | NUMBER | 1,80,000 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1410 | page 47 | line 3312 | NUMBER | 22.95 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1411 | page 47 | line 3312 | NUMBER | 1,80,000 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1412 | page 47 | line 3312 | NUMBER | 22.95 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1413 | page 47 | line 3312 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1414 | page 47 | line 3312 | NUMBER | INR 117.50 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1415 | page 47 | line 3313 | NUMBER | 55,526 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1416 | page 47 | line 3313 | NUMBER | 25.64 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1417 | page 47 | line 3313 | NUMBER | 55,526 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1418 | page 47 | line 3313 | NUMBER | 25.64 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1419 | page 47 | line 3313 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1420 | page 47 | line 3313 | NUMBER | INR 451.80 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1421 | page 47 | line 3314 | NUMBER | 15,10,656 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1422 | page 47 | line 3314 | NUMBER | 240.68 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1423 | page 47 | line 3314 | NUMBER | 15,10,656 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1424 | page 47 | line 3314 | NUMBER | 240.68 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1425 | page 47 | line 3314 | NUMBER | INR 40 | [I2] face value per unit, Compulsory convertible preference shares of I
R1426 | page 47 | line 3314 | NUMBER | INR 119.32 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1427 | page 47 | line 3316 | NUMBER | 689.97 | [I2] stand note 8a non-current inv: Fair value gain recognised through profit and, amount at 30 Sep 2026
R1428 | page 47 | line 3316 | NUMBER | 1,219.80 | [I2] stand note 8a non-current inv: Fair value gain recognised through profit and, carrying total at 30 Sep 2026
R1429 | page 47 | line 3316 | NUMBER | 689.97 | [I2] stand note 8a non-current inv: Fair value gain recognised through profit and, amount at 31 Mar 2026
R1430 | page 47 | line 3316 | NUMBER | 1,219.80 | [I2] stand note 8a non-current inv: Fair value gain recognised through profit and, carrying total at 31 Mar 2026
R1431 | page 47 | line 3319 | NUMBER | 1,870 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1432 | page 47 | line 3319 | NUMBER | 161.41 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1433 | page 47 | line 3319 | NUMBER | 1,870 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1434 | page 47 | line 3319 | NUMBER | 161.41 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1435 | page 47 | line 3319 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible preference shares of I
R1436 | page 47 | line 3319 | NUMBER | INR 86,306.32 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1437 | page 47 | line 3320 | NUMBER | 100 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1438 | page 47 | line 3320 | NUMBER | 8.63 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1439 | page 47 | line 3320 | NUMBER | 100 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026
R1440 | page 47 | line 3320 | NUMBER | 8.63 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026
R1441 | page 47 | line 3320 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1442 | page 47 | line 3320 | NUMBER | INR 86,306.32 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1443 | page 47 | line 3321 | NUMBER | (95.56) | [I2] stand note 8a non-current inv: Fair value loss recognised through profit and, amount at 30 Sep 2026
R1444 | page 47 | line 3321 | NUMBER | 74.48 | [I2] stand note 8a non-current inv: Fair value loss recognised through profit and, carrying total at 30 Sep 2026
R1445 | page 47 | line 3321 | NUMBER | (95.56) | [I2] stand note 8a non-current inv: Fair value loss recognised through profit and, amount at 31 Mar 2026
R1446 | page 47 | line 3321 | NUMBER | 74.48 | [I2] stand note 8a non-current inv: Fair value loss recognised through profit and, carrying total at 31 Mar 2026
R1447 | page 47 | line 3324 | NUMBER | 6,95,922 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R1448 | page 47 | line 3324 | NUMBER | 252.78 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R1449 | page 47 | line 3324 | NUMBER | 6,95,922 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R1450 | page 47 | line 3324 | NUMBER | 252.78 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R1451 | page 47 | line 3324 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R1452 | page 47 | line 3324 | NUMBER | INR 362.22 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R1453 | page 47 | line 3325 | NUMBER | 3,54,619 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1454 | page 47 | line 3325 | NUMBER | 644.02 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1455 | page 47 | line 3325 | NUMBER | 3,54,619 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1456 | page 47 | line 3325 | NUMBER | 644.02 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1457 | page 47 | line 3325 | NUMBER | INR 5 | [I2] face value per unit, Compulsory convertible preference shares of I
R1458 | page 47 | line 3325 | NUMBER | INR 1,811.10 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1459 | page 47 | line 3326 | NUMBER | 400 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, units at 30 Sep 2026
R1460 | page 47 | line 3326 | NUMBER | 0.15 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, amount at 30 Sep 2026
R1461 | page 47 | line 3326 | NUMBER | 400 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, units at 31 Mar 2026
R1462 | page 47 | line 3326 | NUMBER | 0.15 | [I2] stand note 8a non-current inv: Compulsory convertible preference shares of I, amount at 31 Mar 2026
R1463 | page 47 | line 3326 | NUMBER | INR 5 | [I2] face value per unit, Compulsory convertible preference shares of I
R1464 | page 47 | line 3326 | NUMBER | INR 358.22 | [I2] issue premium per unit, Compulsory convertible preference shares of I
R1465 | page 47 | line 3327 | NUMBER | 1,995 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R1466 | page 47 | line 3327 | NUMBER | 1.39 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R1467 | page 47 | line 3327 | NUMBER | 1,995 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R1468 | page 47 | line 3327 | NUMBER | 1.39 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R1469 | page 47 | line 3327 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R1470 | page 47 | line 3327 | NUMBER | INR 695.72 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R1471 | page 47 | line 3328 | NUMBER | 17,647 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R1472 | page 47 | line 3328 | NUMBER | 10.13 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R1473 | page 47 | line 3328 | NUMBER | 17,647 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R1474 | page 47 | line 3328 | NUMBER | 10.13 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R1475 | page 47 | line 3328 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R1476 | page 47 | line 3328 | NUMBER | INR 572.80 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R1477 | page 47 | line 3329 | NUMBER | 14,414 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 30 Sep 2026
R1478 | page 47 | line 3329 | NUMBER | 10.93 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 30 Sep 2026
R1479 | page 47 | line 3329 | NUMBER | 14,414 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, units at 31 Mar 2026
R1480 | page 47 | line 3329 | NUMBER | 10.93 | [I2] stand note 8a non-current inv: Equity shares of INR 1 each (at premium of IN, amount at 31 Mar 2026
R1481 | page 47 | line 3329 | NUMBER | INR 1 | [I2] face value per unit, Equity shares of INR 1 each (at premium of IN
R1482 | page 47 | line 3329 | NUMBER | INR 757.19 | [I2] issue premium per unit, Equity shares of INR 1 each (at premium of IN
R1483 | page 47 | line 3330 | NUMBER | 35,840 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, units at 30 Sep 2026
R1484 | page 47 | line 3330 | NUMBER | 124.85 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 30 Sep 2026
R1485 | page 47 | line 3330 | NUMBER | 35,840 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, units at 31 Mar 2026
R1486 | page 47 | line 3330 | NUMBER | 124.85 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 31 Mar 2026
R1487 | page 47 | line 3330 | NUMBER | INR 5 | [I2] face value per unit, Compulsory convertible Preference shares of I
R1488 | page 47 | line 3330 | NUMBER | INR 3478.60 | [I2] issue premium per unit, Compulsory convertible Preference shares of I
R1489 | page 47 | line 3331 | NUMBER | 2,186 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, units at 30 Sep 2026
R1490 | page 47 | line 3331 | NUMBER | 1.52 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 30 Sep 2026
R1491 | page 47 | line 3331 | NUMBER | 2,186 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, units at 31 Mar 2026
R1492 | page 47 | line 3331 | NUMBER | 1.52 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 31 Mar 2026
R1493 | page 47 | line 3331 | NUMBER | INR 10 | [I2] face value per unit, Compulsory convertible Preference shares of I
R1494 | page 47 | line 3331 | NUMBER | INR 686.72 | [I2] issue premium per unit, Compulsory convertible Preference shares of I
R1495 | page 47 | line 3332 | NUMBER | 415 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, units at 30 Sep 2026
R1496 | page 47 | line 3332 | NUMBER | 1.57 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 30 Sep 2026
R1497 | page 47 | line 3332 | NUMBER | 415 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, units at 31 Mar 2026
R1498 | page 47 | line 3332 | NUMBER | 1.57 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 31 Mar 2026
R1499 | page 47 | line 3332 | NUMBER | INR 1 | [I2] face value per unit, Compulsory convertible Preference shares of I
R1500 | page 47 | line 3332 | NUMBER | INR 3789.95 | [I2] issue premium per unit, Compulsory convertible Preference shares of I
R1501 | page 47 | line 3334 | NUMBER | 86,548 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, units at 30 Sep 2026
R1502 | page 47 | line 3334 | NUMBER | 78.04 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 30 Sep 2026
R1503 | page 47 | line 3334 | NUMBER | 86,548 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, units at 31 Mar 2026
R1504 | page 47 | line 3334 | NUMBER | 78.04 | [I2] stand note 8a non-current inv: Compulsory convertible Preference shares of I, amount at 31 Mar 2026
R1505 | page 47 | line 3334 | NUMBER | INR 5 | [I2] face value per unit, Compulsory convertible Preference shares of I
R1506 | page 47 | line 3334 | NUMBER | INR 896.70 | [I2] issue premium per unit, Compulsory convertible Preference shares of I
R1507 | page 47 | line 3336 | NUMBER | 823.53 | [I2] stand note 8a non-current inv: Fair value gain recognised through profit and, amount at 30 Sep 2026
R1508 | page 47 | line 3336 | NUMBER | 1,948.91 | [I2] stand note 8a non-current inv: Fair value gain recognised through profit and, carrying total at 30 Sep 2026
R1509 | page 47 | line 3336 | NUMBER | 823.53 | [I2] stand note 8a non-current inv: Fair value gain recognised through profit and, amount at 31 Mar 2026
R1510 | page 47 | line 3336 | NUMBER | 1,948.91 | [I2] stand note 8a non-current inv: Fair value gain recognised through profit and, carrying total at 31 Mar 2026
R1511 | page 47 | line 3340 | NUMBER | 8,11,250 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 30 Sep 2026
R1512 | page 47 | line 3340 | NUMBER | 1041.77 | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 30 Sep 2026
R1513 | page 47 | line 3340 | NUMBER | - | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, units at 31 Mar 2026 | ZERO_STANDING
R1514 | page 47 | line 3340 | NUMBER | - | [I2] stand note 8a non-current inv: Equity shares of INR 10 each (at premium of I, amount at 31 Mar 2026 | ZERO_STANDING
R1515 | page 47 | line 3340 | NUMBER | INR 10 | [I2] face value per unit, Equity shares of INR 10 each (at premium of I
R1516 | page 47 | line 3340 | NUMBER | INR 1,274.15 | [I2] issue premium per unit, Equity shares of INR 10 each (at premium of I
R1517 | page 47 | line 3341 | NUMBER | 1,06,876 | [I2] stand note 8a non-current inv: Investment in Equity shares of INR 10 each (a, units at 30 Sep 2026
R1518 | page 47 | line 3341 | NUMBER | 137.36 | [I2] stand note 8a non-current inv: Investment in Equity shares of INR 10 each (a, amount at 30 Sep 2026
R1519 | page 47 | line 3341 | NUMBER | - | [I2] stand note 8a non-current inv: Investment in Equity shares of INR 10 each (a, units at 31 Mar 2026 | ZERO_STANDING
R1520 | page 47 | line 3341 | NUMBER | - | [I2] stand note 8a non-current inv: Investment in Equity shares of INR 10 each (a, amount at 31 Mar 2026 | ZERO_STANDING
R1521 | page 47 | line 3341 | NUMBER | INR 10 | [I2] face value per unit, Investment in Equity shares of INR 10 each (a
R1522 | page 47 | line 3341 | NUMBER | INR 1,275.24 | [I2] issue premium per unit, Investment in Equity shares of INR 10 each (a
R1523 | page 47 | line 3342 | NUMBER | (392.80) | [I2] stand note 8a non-current inv: Less: Impairment allowance recognised through, amount at 30 Sep 2026
R1524 | page 47 | line 3342 | NUMBER | - | [I2] stand note 8a non-current inv: Less: Impairment allowance recognised through, amount at 31 Mar 2026 | ZERO_STANDING
R1525 | page 47 | line 3343 | NUMBER | (200.00) | [I2] stand note 8a non-current inv: Fair value loss recognised through profit and, amount at 30 Sep 2026
R1526 | page 47 | line 3343 | NUMBER | 586.33 | [I2] stand note 8a non-current inv: Fair value loss recognised through profit and, carrying total at 30 Sep 2026
R1527 | page 47 | line 3343 | NUMBER | - | [I2] stand note 8a non-current inv: Fair value loss recognised through profit and, amount at 31 Mar 2026 | ZERO_STANDING
R1528 | page 47 | line 3343 | NUMBER | - | [I2] stand note 8a non-current inv: Fair value loss recognised through profit and, carrying total at 31 Mar 2026 | ZERO_STANDING
R1529 | page 47 | line 3321 | NUMBER | 3,829.52 | [I2] stand note 8a non-current inv: value loss recognised through profit and loss, amount at 30 Sep 2026
R1530 | page 47 | line 3321 | NUMBER | 3,243.19 | [I2] stand note 8a non-current inv: value loss recognised through profit and loss, amount at 31 Mar 2026
R1531 | page 47 | line 3349 | NUMBER | 3,885.02 | [I2] stand note 8a non-current inv: Total non-current investments (a+b+c), amount at 30 Sep 2026
R1532 | page 47 | line 3349 | NUMBER | 3,426.75 | [I2] stand note 8a non-current inv: Total non-current investments (a+b+c), amount at 31 Mar 2026
R1533 | page 47 | line 3274 | NUMBER | INR 10 | [I2] stated in note text: Optionally Convertible Cumulative Redeem
R1534 | page 47 | line 3268 | NUMBER | 7,600,000 | [I2] stated in note text: ii) During the period ended 30 September
R1535 | page 47 | line 3268 | NUMBER | 0.001% | [I2] stated in note text: ii) During the period ended 30 September
R1536 | page 47 | line 3268 | NUMBER | INR 10 | [I2] stated in note text: ii) During the period ended 30 September
R1537 | page 47 | line 3268 | NUMBER | INR 15 | [I2] stated in note text: ii) During the period ended 30 September
R1538 | page 47 | line 3301 | NUMBER | INR 10 | [I2] stated in note text: Optionally Convertible Cumulative Redeem
R1539 | page 47 | line 3274 | NUMBER | 7,870,000 | [I2] stated in note text: v). The Company had invested in 7,870,00
R1540 | page 47 | line 3274 | NUMBER | 0.01% | [I2] stated in note text: v). The Company had invested in 7,870,00
R1541 | page 47 | line 3277 | NUMBER | INR 200 | [I2] stated in note text: vii) During the period ended 30 Septembe
R1542 | page 47 | line 3270 | NUMBER | 12,050,000 | [I2] stated in note text: business users. During the period, the C
R1543 | page 47 | line 3270 | NUMBER | INR 10 | [I2] stated in note text: business users. During the period, the C
R1544 | page 47 | line 3271 | NUMBER | INR 649.88 | [I2] stated in note text: iv) During the period ended 30 September
R1545 | page 47 | line 3271 | NUMBER | INR 10 | [I2] stated in note text: iv) During the period ended 30 September
R1546 | page 47 | line 3271 | NUMBER | INR 1,40,352 | [I2] stated in note text: iv) During the period ended 30 September
R1547 | page 47 | line 3272 | NUMBER | 22.25% | [I2] stated in note text: share thereby increasing the shareholdin
R1548 | page 47 | line 3272 | NUMBER | 25.80% | [I2] stated in note text: share thereby increasing the shareholdin
R1549 | page 47 | line 3267 | NUMBER | 1,172 | [I2] stated in note text: i) During the period ended 30 September 
R1550 | page 47 | line 3267 | NUMBER | 0.001% | [I2] stated in note text: i) During the period ended 30 September 
R1551 | page 47 | line 3267 | NUMBER | INR 10 | [I2] stated in note text: i) During the period ended 30 September 
R1552 | page 47 | line 3267 | NUMBER | INR 51,157 | [I2] stated in note text: i) During the period ended 30 September 
R1553 | page 48 | line 3367 | NUMBER | - | [I2] stand note 8b current inv: Aditya Birla Sun Life Arbitrage Fund, units at 30 Sep 2026 | ZERO_STANDING
R1554 | page 48 | line 3367 | NUMBER | - | [I2] stand note 8b current inv: Aditya Birla Sun Life Arbitrage Fund, amount at 30 Sep 2026 | ZERO_STANDING
R1555 | page 48 | line 3367 | NUMBER | 1,69,00,751 | [I2] stand note 8b current inv: Aditya Birla Sun Life Arbitrage Fund, units at 31 Mar 2026
R1556 | page 48 | line 3367 | NUMBER | 507.83 | [I2] stand note 8b current inv: Aditya Birla Sun Life Arbitrage Fund, amount at 31 Mar 2026
R1557 | page 48 | line 3368 | NUMBER | 1,16,44,141 | [I2] stand note 8b current inv: Aditya Birla Sun Life Corporate Bond Fund, units at 30 Sep 2026
R1558 | page 48 | line 3368 | NUMBER | 1,414.61 | [I2] stand note 8b current inv: Aditya Birla Sun Life Corporate Bond Fund, amount at 30 Sep 2026
R1559 | page 48 | line 3368 | NUMBER | 1,16,44,141 | [I2] stand note 8b current inv: Aditya Birla Sun Life Corporate Bond Fund, units at 31 Mar 2026
R1560 | page 48 | line 3368 | NUMBER | 1,373.14 | [I2] stand note 8b current inv: Aditya Birla Sun Life Corporate Bond Fund, amount at 31 Mar 2026
R1561 | page 48 | line 3369 | NUMBER | 3,91,18,998 | [I2] stand note 8b current inv: Aditya Birla Sun Life Nifty SDL Apr 2027 Inde, units at 30 Sep 2026
R1562 | page 48 | line 3369 | NUMBER | 523.00 | [I2] stand note 8b current inv: Aditya Birla Sun Life Nifty SDL Apr 2027 Inde, amount at 30 Sep 2026
R1563 | page 48 | line 3369 | NUMBER | 3,91,18,998 | [I2] stand note 8b current inv: Aditya Birla Sun Life Nifty SDL Apr 2027 Inde, units at 31 Mar 2026
R1564 | page 48 | line 3369 | NUMBER | 508.66 | [I2] stand note 8b current inv: Aditya Birla Sun Life Nifty SDL Apr 2027 Inde, amount at 31 Mar 2026
R1565 | page 48 | line 3370 | NUMBER | 87,77,620 | [I2] stand note 8b current inv: Axis Corporate Bond Fund, units at 30 Sep 2026
R1566 | page 48 | line 3370 | NUMBER | 170.01 | [I2] stand note 8b current inv: Axis Corporate Bond Fund, amount at 30 Sep 2026
R1567 | page 48 | line 3370 | NUMBER | 87,77,620 | [I2] stand note 8b current inv: Axis Corporate Bond Fund, units at 31 Mar 2026
R1568 | page 48 | line 3370 | NUMBER | 164.64 | [I2] stand note 8b current inv: Axis Corporate Bond Fund, amount at 31 Mar 2026
R1569 | page 48 | line 3371 | NUMBER | - | [I2] stand note 8b current inv: Axis Liquid Fund, units at 30 Sep 2026 | ZERO_STANDING
R1570 | page 48 | line 3371 | NUMBER | - | [I2] stand note 8b current inv: Axis Liquid Fund, amount at 30 Sep 2026 | ZERO_STANDING
R1571 | page 48 | line 3371 | NUMBER | 22,871 | [I2] stand note 8b current inv: Axis Liquid Fund, units at 31 Mar 2026
R1572 | page 48 | line 3371 | NUMBER | 70.09 | [I2] stand note 8b current inv: Axis Liquid Fund, amount at 31 Mar 2026
R1573 | page 48 | line 3372 | NUMBER | 7,11,756 | [I2] stand note 8b current inv: BHARAT Bond ETF - April 2030, units at 30 Sep 2026
R1574 | page 48 | line 3372 | NUMBER | 1,145.39 | [I2] stand note 8b current inv: BHARAT Bond ETF - April 2030, amount at 30 Sep 2026
R1575 | page 48 | line 3372 | NUMBER | 7,11,756 | [I2] stand note 8b current inv: BHARAT Bond ETF - April 2030, units at 31 Mar 2026
R1576 | page 48 | line 3372 | NUMBER | 1,111.61 | [I2] stand note 8b current inv: BHARAT Bond ETF - April 2030, amount at 31 Mar 2026
R1577 | page 48 | line 3373 | NUMBER | (0) | [I2] stand note 8b current inv: Bandhan Money Market Fund, units at 30 Sep 2026 | ZERO_STANDING
R1578 | page 48 | line 3373 | NUMBER | - | [I2] stand note 8b current inv: Bandhan Money Market Fund, amount at 30 Sep 2026 | ZERO_STANDING
R1579 | page 48 | line 3373 | NUMBER | 63,86,224 | [I2] stand note 8b current inv: Bandhan Money Market Fund, units at 31 Mar 2026
R1580 | page 48 | line 3373 | NUMBER | 292.00 | [I2] stand note 8b current inv: Bandhan Money Market Fund, amount at 31 Mar 2026
R1581 | page 48 | line 3374 | NUMBER | - | [I2] stand note 8b current inv: Edelweiss NIFTY PSU Bond Plus SDL Apr 2026 50, units at 30 Sep 2026 | ZERO_STANDING
R1582 | page 48 | line 3374 | NUMBER | - | [I2] stand note 8b current inv: Edelweiss NIFTY PSU Bond Plus SDL Apr 2026 50, amount at 30 Sep 2026 | ZERO_STANDING
R1583 | page 48 | line 3374 | NUMBER | 4,74,76,047 | [I2] stand note 8b current inv: Edelweiss NIFTY PSU Bond Plus SDL Apr 2026 50, units at 31 Mar 2026
R1584 | page 48 | line 3374 | NUMBER | 648.09 | [I2] stand note 8b current inv: Edelweiss NIFTY PSU Bond Plus SDL Apr 2026 50, amount at 31 Mar 2026
R1585 | page 48 | line 3375 | NUMBER | 8,180 | [I2] stand note 8b current inv: Edelweiss Liquid Fund, units at 30 Sep 2026
R1586 | page 48 | line 3375 | NUMBER | 30.00 | [I2] stand note 8b current inv: Edelweiss Liquid Fund, amount at 30 Sep 2026
R1587 | page 48 | line 3375 | NUMBER | - | [I2] stand note 8b current inv: Edelweiss Liquid Fund, units at 31 Mar 2026 | ZERO_STANDING
R1588 | page 48 | line 3375 | NUMBER | - | [I2] stand note 8b current inv: Edelweiss Liquid Fund, amount at 31 Mar 2026 | ZERO_STANDING
R1589 | page 48 | line 3376 | NUMBER | 6,94,63,060 | [I2] stand note 8b current inv: Edelweiss CRISIL IBX 50:50 Gilt Plus SDL Apri, units at 30 Sep 2026
R1590 | page 48 | line 3376 | NUMBER | 926.03 | [I2] stand note 8b current inv: Edelweiss CRISIL IBX 50:50 Gilt Plus SDL Apri, amount at 30 Sep 2026
R1591 | page 48 | line 3376 | NUMBER | 6,94,63,060 | [I2] stand note 8b current inv: Edelweiss CRISIL IBX 50:50 Gilt Plus SDL Apri, units at 31 Mar 2026
R1592 | page 48 | line 3376 | NUMBER | 900.46 | [I2] stand note 8b current inv: Edelweiss CRISIL IBX 50:50 Gilt Plus SDL Apri, amount at 31 Mar 2026
R1593 | page 48 | line 3377 | NUMBER | (0) | [I2] stand note 8b current inv: Edelweiss Arbitrage Fund, units at 30 Sep 2026 | ZERO_STANDING
R1594 | page 48 | line 3377 | NUMBER | - | [I2] stand note 8b current inv: Edelweiss Arbitrage Fund, amount at 30 Sep 2026 | ZERO_STANDING
R1595 | page 48 | line 3377 | NUMBER | 1,31,97,587 | [I2] stand note 8b current inv: Edelweiss Arbitrage Fund, units at 31 Mar 2026
R1596 | page 48 | line 3377 | NUMBER | 287.96 | [I2] stand note 8b current inv: Edelweiss Arbitrage Fund, amount at 31 Mar 2026
R1597 | page 48 | line 3378 | NUMBER | 5,42,13,089 | [I2] stand note 8b current inv: Edelweiss Nifty Midcap150 Momentum 50 Index F, units at 30 Sep 2026
R1598 | page 48 | line 3378 | NUMBER | 973.42 | [I2] stand note 8b current inv: Edelweiss Nifty Midcap150 Momentum 50 Index F, amount at 30 Sep 2026
R1599 | page 48 | line 3378 | NUMBER | 4,43,12,353 | [I2] stand note 8b current inv: Edelweiss Nifty Midcap150 Momentum 50 Index F, units at 31 Mar 2026
R1600 | page 48 | line 3378 | NUMBER | 711.04 | [I2] stand note 8b current inv: Edelweiss Nifty Midcap150 Momentum 50 Index F, amount at 31 Mar 2026
R1601 | page 48 | line 3379 | NUMBER | 1,54,29,585 | [I2] stand note 8b current inv: HDFC Ultra Short to Short Term Fund, units at 30 Sep 2026
R1602 | page 48 | line 3379 | NUMBER | 1,044.24 | [I2] stand note 8b current inv: HDFC Ultra Short to Short Term Fund, amount at 30 Sep 2026
R1603 | page 48 | line 3379 | NUMBER | 1,54,29,585 | [I2] stand note 8b current inv: HDFC Ultra Short to Short Term Fund, units at 31 Mar 2026
R1604 | page 48 | line 3379 | NUMBER | 1,011.19 | [I2] stand note 8b current inv: HDFC Ultra Short to Short Term Fund, amount at 31 Mar 2026
R1605 | page 48 | line 3380 | NUMBER | 47,38,647 | [I2] stand note 8b current inv: HDFC Corporate Bond Fund, units at 30 Sep 2026
R1606 | page 48 | line 3380 | NUMBER | 166.53 | [I2] stand note 8b current inv: HDFC Corporate Bond Fund, amount at 30 Sep 2026
R1607 | page 48 | line 3380 | NUMBER | 47,38,647 | [I2] stand note 8b current inv: HDFC Corporate Bond Fund, units at 31 Mar 2026
R1608 | page 48 | line 3380 | NUMBER | 161.75 | [I2] stand note 8b current inv: HDFC Corporate Bond Fund, amount at 31 Mar 2026
R1609 | page 48 | line 3381 | NUMBER | 14,43,254 | [I2] stand note 8b current inv: ICICI Prudential Ultra Short to Short Term Fu, units at 30 Sep 2026
R1610 | page 48 | line 3381 | NUMBER | 861.11 | [I2] stand note 8b current inv: ICICI Prudential Ultra Short to Short Term Fu, amount at 30 Sep 2026
R1611 | page 48 | line 3381 | NUMBER | 14,43,254 | [I2] stand note 8b current inv: ICICI Prudential Ultra Short to Short Term Fu, units at 31 Mar 2026
R1612 | page 48 | line 3381 | NUMBER | 833.26 | [I2] stand note 8b current inv: ICICI Prudential Ultra Short to Short Term Fu, amount at 31 Mar 2026
R1613 | page 48 | line 3382 | NUMBER | 0 | [I2] stand note 8b current inv: ICICI Prudential Money Market Fund, units at 30 Sep 2026 | ZERO_STANDING
R1614 | page 48 | line 3382 | NUMBER | - | [I2] stand note 8b current inv: ICICI Prudential Money Market Fund, amount at 30 Sep 2026 | ZERO_STANDING
R1615 | page 48 | line 3382 | NUMBER | 6,12,903 | [I2] stand note 8b current inv: ICICI Prudential Money Market Fund, units at 31 Mar 2026
R1616 | page 48 | line 3382 | NUMBER | 246.40 | [I2] stand note 8b current inv: ICICI Prudential Money Market Fund, amount at 31 Mar 2026
R1617 | page 48 | line 3383 | NUMBER | - | [I2] stand note 8b current inv: ICICI Prudential Liquid Fund, units at 30 Sep 2026 | ZERO_STANDING
R1618 | page 48 | line 3383 | NUMBER | - | [I2] stand note 8b current inv: ICICI Prudential Liquid Fund, amount at 30 Sep 2026 | ZERO_STANDING
R1619 | page 48 | line 3383 | NUMBER | 1,12,625 | [I2] stand note 8b current inv: ICICI Prudential Liquid Fund, units at 31 Mar 2026
R1620 | page 48 | line 3383 | NUMBER | 45.92 | [I2] stand note 8b current inv: ICICI Prudential Liquid Fund, amount at 31 Mar 2026
R1621 | page 48 | line 3384 | NUMBER | 2,06,88,321 | [I2] stand note 8b current inv: ICICI Prudential Corporate Bond Fund, units at 30 Sep 2026
R1622 | page 48 | line 3384 | NUMBER | 693.40 | [I2] stand note 8b current inv: ICICI Prudential Corporate Bond Fund, amount at 30 Sep 2026
R1623 | page 48 | line 3384 | NUMBER | 2,06,88,321 | [I2] stand note 8b current inv: ICICI Prudential Corporate Bond Fund, units at 31 Mar 2026
R1624 | page 48 | line 3384 | NUMBER | 671.52 | [I2] stand note 8b current inv: ICICI Prudential Corporate Bond Fund, amount at 31 Mar 2026
R1625 | page 48 | line 3385 | NUMBER | 4,82,19,177 | [I2] stand note 8b current inv: ICICI Prudential Nifty SDL Dec 2028 Index Fun, units at 30 Sep 2026
R1626 | page 48 | line 3385 | NUMBER | 646.27 | [I2] stand note 8b current inv: ICICI Prudential Nifty SDL Dec 2028 Index Fun, amount at 30 Sep 2026
R1627 | page 48 | line 3385 | NUMBER | 4,82,19,177 | [I2] stand note 8b current inv: ICICI Prudential Nifty SDL Dec 2028 Index Fun, units at 31 Mar 2026
R1628 | page 48 | line 3385 | NUMBER | 631.26 | [I2] stand note 8b current inv: ICICI Prudential Nifty SDL Dec 2028 Index Fun, amount at 31 Mar 2026
R1629 | page 48 | line 3386 | NUMBER | 2,46,52,417 | [I2] stand note 8b current inv: Edelweiss Banking and PSU Debt Fund, units at 30 Sep 2026
R1630 | page 48 | line 3386 | NUMBER | 668.63 | [I2] stand note 8b current inv: Edelweiss Banking and PSU Debt Fund, amount at 30 Sep 2026
R1631 | page 48 | line 3386 | NUMBER | - | [I2] stand note 8b current inv: Edelweiss Banking and PSU Debt Fund, units at 31 Mar 2026 | ZERO_STANDING
R1632 | page 48 | line 3386 | NUMBER | - | [I2] stand note 8b current inv: Edelweiss Banking and PSU Debt Fund, amount at 31 Mar 2026 | ZERO_STANDING
R1633 | page 48 | line 3387 | NUMBER | 1,84,82,974 | [I2] stand note 8b current inv: ICICI Prudential Nifty Alpha Low Volatility 3, units at 30 Sep 2026
R1634 | page 48 | line 3387 | NUMBER | 482.84 | [I2] stand note 8b current inv: ICICI Prudential Nifty Alpha Low Volatility 3, amount at 30 Sep 2026
R1635 | page 48 | line 3387 | NUMBER | 1,84,82,974 | [I2] stand note 8b current inv: ICICI Prudential Nifty Alpha Low Volatility 3, units at 31 Mar 2026
R1636 | page 48 | line 3387 | NUMBER | 456.74 | [I2] stand note 8b current inv: ICICI Prudential Nifty Alpha Low Volatility 3, amount at 31 Mar 2026
R1637 | page 48 | line 3388 | NUMBER | 2,05,79,467 | [I2] stand note 8b current inv: ICICI Prudential Nifty 200 Quality 30 ETF, units at 30 Sep 2026
R1638 | page 48 | line 3388 | NUMBER | 405.27 | [I2] stand note 8b current inv: ICICI Prudential Nifty 200 Quality 30 ETF, amount at 30 Sep 2026
R1639 | page 48 | line 3388 | NUMBER | 2,05,79,467 | [I2] stand note 8b current inv: ICICI Prudential Nifty 200 Quality 30 ETF, units at 31 Mar 2026
R1640 | page 48 | line 3388 | NUMBER | 386.69 | [I2] stand note 8b current inv: ICICI Prudential Nifty 200 Quality 30 ETF, amount at 31 Mar 2026
R1641 | page 48 | line 3389 | NUMBER | 42,25,814 | [I2] stand note 8b current inv: Invesco India Arbitrage Fund, units at 30 Sep 2026
R1642 | page 48 | line 3389 | NUMBER | 158.03 | [I2] stand note 8b current inv: Invesco India Arbitrage Fund, amount at 30 Sep 2026
R1643 | page 48 | line 3389 | NUMBER | 1,64,52,936 | [I2] stand note 8b current inv: Invesco India Arbitrage Fund, units at 31 Mar 2026
R1644 | page 48 | line 3389 | NUMBER | 596.10 | [I2] stand note 8b current inv: Invesco India Arbitrage Fund, amount at 31 Mar 2026
R1645 | page 48 | line 3390 | NUMBER | 2,16,768 | [I2] stand note 8b current inv: Kotak Corporate Bond Fund, units at 30 Sep 2026
R1646 | page 48 | line 3390 | NUMBER | 910.71 | [I2] stand note 8b current inv: Kotak Corporate Bond Fund, amount at 30 Sep 2026
R1647 | page 48 | line 3390 | NUMBER | 2,16,768 | [I2] stand note 8b current inv: Kotak Corporate Bond Fund, units at 31 Mar 2026
R1648 | page 48 | line 3390 | NUMBER | 884.62 | [I2] stand note 8b current inv: Kotak Corporate Bond Fund, amount at 31 Mar 2026
R1649 | page 48 | line 3391 | NUMBER | 76,29,346 | [I2] stand note 8b current inv: Kotak Arbitrage Fund, units at 30 Sep 2026
R1650 | page 48 | line 3391 | NUMBER | 330.80 | [I2] stand note 8b current inv: Kotak Arbitrage Fund, amount at 30 Sep 2026
R1651 | page 48 | line 3391 | NUMBER | 1,78,80,168 | [I2] stand note 8b current inv: Kotak Arbitrage Fund, units at 31 Mar 2026
R1652 | page 48 | line 3391 | NUMBER | 751.49 | [I2] stand note 8b current inv: Kotak Arbitrage Fund, amount at 31 Mar 2026
R1653 | page 48 | line 3392 | NUMBER | (0) | [I2] stand note 8b current inv: Kotak Money Market Fund, units at 30 Sep 2026 | ZERO_STANDING
R1654 | page 48 | line 3392 | NUMBER | - | [I2] stand note 8b current inv: Kotak Money Market Fund, amount at 30 Sep 2026 | ZERO_STANDING
R1655 | page 48 | line 3392 | NUMBER | 43,333 | [I2] stand note 8b current inv: Kotak Money Market Fund, units at 31 Mar 2026
R1656 | page 48 | line 3392 | NUMBER | 205.60 | [I2] stand note 8b current inv: Kotak Money Market Fund, amount at 31 Mar 2026
R1657 | page 48 | line 3393 | NUMBER | 4,48,35,182 | [I2] stand note 8b current inv: Kotak Nifty SDL Apr 2027 Top 12 Equal Weight , units at 30 Sep 2026
R1658 | page 48 | line 3393 | NUMBER | 595.59 | [I2] stand note 8b current inv: Kotak Nifty SDL Apr 2027 Top 12 Equal Weight , amount at 30 Sep 2026
R1659 | page 48 | line 3393 | NUMBER | 4,48,35,182 | [I2] stand note 8b current inv: Kotak Nifty SDL Apr 2027 Top 12 Equal Weight , units at 31 Mar 2026
R1660 | page 48 | line 3393 | NUMBER | 579.13 | [I2] stand note 8b current inv: Kotak Nifty SDL Apr 2027 Top 12 Equal Weight , amount at 31 Mar 2026
R1661 | page 48 | line 3394 | NUMBER | 9,46,02,577 | [I2] stand note 8b current inv: Kotak Nifty SDL Apr 2032 Top 12 Equal Weight , units at 30 Sep 2026
R1662 | page 48 | line 3394 | NUMBER | 1,270.05 | [I2] stand note 8b current inv: Kotak Nifty SDL Apr 2032 Top 12 Equal Weight , amount at 30 Sep 2026
R1663 | page 48 | line 3394 | NUMBER | 9,46,02,577 | [I2] stand note 8b current inv: Kotak Nifty SDL Apr 2032 Top 12 Equal Weight , units at 31 Mar 2026
R1664 | page 48 | line 3394 | NUMBER | 1,233.69 | [I2] stand note 8b current inv: Kotak Nifty SDL Apr 2032 Top 12 Equal Weight , amount at 31 Mar 2026
R1665 | page 48 | line 3395 | NUMBER | 1,89,55,981 | [I2] stand note 8b current inv: Kotak Nifty Midcap 150 Momentum 50 Index Fund, units at 30 Sep 2026
R1666 | page 48 | line 3395 | NUMBER | 174.24 | [I2] stand note 8b current inv: Kotak Nifty Midcap 150 Momentum 50 Index Fund, amount at 30 Sep 2026
R1667 | page 48 | line 3395 | NUMBER | - | [I2] stand note 8b current inv: Kotak Nifty Midcap 150 Momentum 50 Index Fund, units at 31 Mar 2026 | ZERO_STANDING
R1668 | page 48 | line 3395 | NUMBER | - | [I2] stand note 8b current inv: Kotak Nifty Midcap 150 Momentum 50 Index Fund, amount at 31 Mar 2026 | ZERO_STANDING
R1669 | page 48 | line 3396 | NUMBER | 2,49,40,628 | [I2] stand note 8b current inv: Nippon India Dynamic Term Fund, units at 30 Sep 2026
R1670 | page 48 | line 3396 | NUMBER | 1,054.73 | [I2] stand note 8b current inv: Nippon India Dynamic Term Fund, amount at 30 Sep 2026
R1671 | page 48 | line 3396 | NUMBER | 2,49,40,628 | [I2] stand note 8b current inv: Nippon India Dynamic Term Fund, units at 31 Mar 2026
R1672 | page 48 | line 3396 | NUMBER | 1,026.31 | [I2] stand note 8b current inv: Nippon India Dynamic Term Fund, amount at 31 Mar 2026
R1673 | page 48 | line 3397 | NUMBER | (0) | [I2] stand note 8b current inv: Tata Money Market Fund, units at 30 Sep 2026 | ZERO_STANDING
R1674 | page 48 | line 3397 | NUMBER | - | [I2] stand note 8b current inv: Tata Money Market Fund, amount at 30 Sep 2026 | ZERO_STANDING
R1675 | page 48 | line 3397 | NUMBER | 40,093 | [I2] stand note 8b current inv: Tata Money Market Fund, units at 31 Mar 2026
R1676 | page 48 | line 3397 | NUMBER | 202.03 | [I2] stand note 8b current inv: Tata Money Market Fund, amount at 31 Mar 2026
R1677 | page 48 | line 3398 | NUMBER | 1,93,81,965 | [I2] stand note 8b current inv: Nippon India Nivesh Lakshya Long Term Fund, units at 30 Sep 2026
R1678 | page 48 | line 3398 | NUMBER | 357.48 | [I2] stand note 8b current inv: Nippon India Nivesh Lakshya Long Term Fund, amount at 30 Sep 2026
R1679 | page 48 | line 3398 | NUMBER | 1,93,81,965 | [I2] stand note 8b current inv: Nippon India Nivesh Lakshya Long Term Fund, units at 31 Mar 2026
R1680 | page 48 | line 3398 | NUMBER | 345.61 | [I2] stand note 8b current inv: Nippon India Nivesh Lakshya Long Term Fund, amount at 31 Mar 2026
R1681 | page 48 | line 3399 | NUMBER | 7,63,46,346 | [I2] stand note 8b current inv: Nippon India Nifty Alpha Low Volatility 30 In, units at 30 Sep 2026
R1682 | page 48 | line 3399 | NUMBER | 1,163.00 | [I2] stand note 8b current inv: Nippon India Nifty Alpha Low Volatility 30 In, amount at 30 Sep 2026
R1683 | page 48 | line 3399 | NUMBER | 5,34,71,886 | [I2] stand note 8b current inv: Nippon India Nifty Alpha Low Volatility 30 In, units at 31 Mar 2026
R1684 | page 48 | line 3399 | NUMBER | 770.31 | [I2] stand note 8b current inv: Nippon India Nifty Alpha Low Volatility 30 In, amount at 31 Mar 2026
R1685 | page 48 | line 3400 | NUMBER | 91,91,798 | [I2] stand note 8b current inv: SBI 10 Year Constant Maturity Gilt Fund, units at 30 Sep 2026
R1686 | page 48 | line 3400 | NUMBER | 630.71 | [I2] stand note 8b current inv: SBI 10 Year Constant Maturity Gilt Fund, amount at 30 Sep 2026
R1687 | page 48 | line 3400 | NUMBER | 91,91,798 | [I2] stand note 8b current inv: SBI 10 Year Constant Maturity Gilt Fund, units at 31 Mar 2026
R1688 | page 48 | line 3400 | NUMBER | 614.81 | [I2] stand note 8b current inv: SBI 10 Year Constant Maturity Gilt Fund, amount at 31 Mar 2026
R1689 | page 48 | line 3401 | NUMBER | 5,55,95,999 | [I2] stand note 8b current inv: SBI Nifty200 Quality 30 Index Fund, units at 30 Sep 2026
R1690 | page 48 | line 3401 | NUMBER | 520.73 | [I2] stand note 8b current inv: SBI Nifty200 Quality 30 Index Fund, amount at 30 Sep 2026
R1691 | page 48 | line 3401 | NUMBER | 1,91,80,261 | [I2] stand note 8b current inv: SBI Nifty200 Quality 30 Index Fund, units at 31 Mar 2026
R1692 | page 48 | line 3401 | NUMBER | 171.53 | [I2] stand note 8b current inv: SBI Nifty200 Quality 30 Index Fund, amount at 31 Mar 2026
R1693 | page 48 | line 3402 | NUMBER | 5,90,671 | [I2] stand note 8b current inv: SBI Nifty 200 Quality 30 ETF, units at 30 Sep 2026
R1694 | page 48 | line 3402 | NUMBER | 122.30 | [I2] stand note 8b current inv: SBI Nifty 200 Quality 30 ETF, amount at 30 Sep 2026
R1695 | page 48 | line 3402 | NUMBER | 5,90,671 | [I2] stand note 8b current inv: SBI Nifty 200 Quality 30 ETF, units at 31 Mar 2026
R1696 | page 48 | line 3402 | NUMBER | 116.71 | [I2] stand note 8b current inv: SBI Nifty 200 Quality 30 ETF, amount at 31 Mar 2026
R1697 | page 48 | line 3403 | NUMBER | 15,72,519 | [I2] stand note 8b current inv: Tata Arbitrage Fund, units at 30 Sep 2026
R1698 | page 48 | line 3403 | NUMBER | 25.76 | [I2] stand note 8b current inv: Tata Arbitrage Fund, amount at 30 Sep 2026
R1699 | page 48 | line 3403 | NUMBER | 3,10,09,914 | [I2] stand note 8b current inv: Tata Arbitrage Fund, units at 31 Mar 2026
R1700 | page 48 | line 3403 | NUMBER | 492.23 | [I2] stand note 8b current inv: Tata Arbitrage Fund, amount at 31 Mar 2026
R1701 | page 48 | line 3404 | NUMBER | - | [I2] stand note 8b current inv: UTI Money Market Fund, units at 30 Sep 2026 | ZERO_STANDING
R1702 | page 48 | line 3404 | NUMBER | - | [I2] stand note 8b current inv: UTI Money Market Fund, amount at 30 Sep 2026 | ZERO_STANDING
R1703 | page 48 | line 3404 | NUMBER | 42,990 | [I2] stand note 8b current inv: UTI Money Market Fund, units at 31 Mar 2026
R1704 | page 48 | line 3404 | NUMBER | 140.42 | [I2] stand note 8b current inv: UTI Money Market Fund, amount at 31 Mar 2026
R1705 | page 48 | line 3405 | NUMBER | 14,653 | [I2] stand note 8b current inv: Tata Overnight Fund, units at 30 Sep 2026
R1706 | page 48 | line 3405 | NUMBER | 21.37 | [I2] stand note 8b current inv: Tata Overnight Fund, amount at 30 Sep 2026
R1707 | page 48 | line 3405 | NUMBER | - | [I2] stand note 8b current inv: Tata Overnight Fund, units at 31 Mar 2026 | ZERO_STANDING
R1708 | page 48 | line 3405 | NUMBER | - | [I2] stand note 8b current inv: Tata Overnight Fund, amount at 31 Mar 2026 | ZERO_STANDING
R1709 | page 48 | line 3406 | NUMBER | 7,43,75,147 | [I2] stand note 8b current inv: UTI Nifty200 Quality 30 Index Fund, units at 30 Sep 2026
R1710 | page 48 | line 3406 | NUMBER | 621.10 | [I2] stand note 8b current inv: UTI Nifty200 Quality 30 Index Fund, amount at 30 Sep 2026
R1711 | page 48 | line 3406 | NUMBER | 7,43,75,147 | [I2] stand note 8b current inv: UTI Nifty200 Quality 30 Index Fund, units at 31 Mar 2026
R1712 | page 48 | line 3406 | NUMBER | 592.77 | [I2] stand note 8b current inv: UTI Nifty200 Quality 30 Index Fund, amount at 31 Mar 2026
R1713 | page 48 | line 3407 | NUMBER | - | [I2] stand note 8b current inv: UTI Liquid Fund, units at 30 Sep 2026 | ZERO_STANDING
R1714 | page 48 | line 3407 | NUMBER | - | [I2] stand note 8b current inv: UTI Liquid Fund, amount at 30 Sep 2026 | ZERO_STANDING
R1715 | page 48 | line 3407 | NUMBER | 14,530 | [I2] stand note 8b current inv: UTI Liquid Fund, units at 31 Mar 2026
R1716 | page 48 | line 3407 | NUMBER | 65.63 | [I2] stand note 8b current inv: UTI Liquid Fund, amount at 31 Mar 2026
R1717 | page 48 | line 3408 | NUMBER | 18,107.35 | [I2] stand note 8b current inv: Total, amount at 30 Sep 2026
R1718 | page 48 | line 3408 | NUMBER | 19,809.24 | [I2] stand note 8b current inv: Total, amount at 31 Mar 2026
R1719 | page 48 | line 3411 | NUMBER | 7,500 | [I2] stand note 8b current inv: Bajaj Finance Ltd. Bond, units at 30 Sep 2026
R1720 | page 48 | line 3411 | NUMBER | 789.74 | [I2] stand note 8b current inv: Bajaj Finance Ltd. Bond, amount at 30 Sep 2026
R1721 | page 48 | line 3411 | NUMBER | 5,000 | [I2] stand note 8b current inv: Bajaj Finance Ltd. Bond, units at 31 Mar 2026
R1722 | page 48 | line 3411 | NUMBER | 515.59 | [I2] stand note 8b current inv: Bajaj Finance Ltd. Bond, amount at 31 Mar 2026
R1723 | page 48 | line 3412 | NUMBER | 25 | [I2] stand note 8b current inv: ICICI Bank Bond, units at 30 Sep 2026
R1724 | page 48 | line 3412 | NUMBER | 249.43 | [I2] stand note 8b current inv: ICICI Bank Bond, amount at 30 Sep 2026
R1725 | page 48 | line 3412 | NUMBER | - | [I2] stand note 8b current inv: ICICI Bank Bond, units at 31 Mar 2026 | ZERO_STANDING
R1726 | page 48 | line 3412 | NUMBER | - | [I2] stand note 8b current inv: ICICI Bank Bond, amount at 31 Mar 2026 | ZERO_STANDING
R1727 | page 48 | line 3413 | NUMBER | 2,500 | [I2] stand note 8b current inv: Axis Finance Ltd. Bond, units at 30 Sep 2026
R1728 | page 48 | line 3413 | NUMBER | 262.88 | [I2] stand note 8b current inv: Axis Finance Ltd. Bond, amount at 30 Sep 2026
R1729 | page 48 | line 3413 | NUMBER | 2,500 | [I2] stand note 8b current inv: Axis Finance Ltd. Bond, units at 31 Mar 2026
R1730 | page 48 | line 3413 | NUMBER | 252.84 | [I2] stand note 8b current inv: Axis Finance Ltd. Bond, amount at 31 Mar 2026
R1731 | page 48 | line 3414 | NUMBER | 20 | [I2] stand note 8b current inv: HDFC Bank Perpetual Bond, units at 30 Sep 2026
R1732 | page 48 | line 3414 | NUMBER | 200.49 | [I2] stand note 8b current inv: HDFC Bank Perpetual Bond, amount at 30 Sep 2026
R1733 | page 48 | line 3414 | NUMBER | 20 | [I2] stand note 8b current inv: HDFC Bank Perpetual Bond, units at 31 Mar 2026
R1734 | page 48 | line 3414 | NUMBER | 210.51 | [I2] stand note 8b current inv: HDFC Bank Perpetual Bond, amount at 31 Mar 2026
R1735 | page 48 | line 3415 | NUMBER | 5,275 | [I2] stand note 8b current inv: HDFC Bank Bond, units at 30 Sep 2026
R1736 | page 48 | line 3415 | NUMBER | 1,037.95 | [I2] stand note 8b current inv: HDFC Bank Bond, amount at 30 Sep 2026
R1737 | page 48 | line 3415 | NUMBER | 2,775 | [I2] stand note 8b current inv: HDFC Bank Bond, units at 31 Mar 2026
R1738 | page 48 | line 3415 | NUMBER | 766.56 | [I2] stand note 8b current inv: HDFC Bank Bond, amount at 31 Mar 2026
R1739 | page 48 | line 3416 | NUMBER | 5,000 | [I2] stand note 8b current inv: HDB Financial Services Ltd Bond, units at 30 Sep 2026
R1740 | page 48 | line 3416 | NUMBER | 517.55 | [I2] stand note 8b current inv: HDB Financial Services Ltd Bond, amount at 30 Sep 2026
R1741 | page 48 | line 3416 | NUMBER | 5,000 | [I2] stand note 8b current inv: HDB Financial Services Ltd Bond, units at 31 Mar 2026
R1742 | page 48 | line 3416 | NUMBER | 520.29 | [I2] stand note 8b current inv: HDB Financial Services Ltd Bond, amount at 31 Mar 2026
R1743 | page 48 | line 3417 | NUMBER | 100 | [I2] stand note 8b current inv: India Infradebt Ltd Bond, units at 30 Sep 2026
R1744 | page 48 | line 3417 | NUMBER | 104.13 | [I2] stand note 8b current inv: India Infradebt Ltd Bond, amount at 30 Sep 2026
R1745 | page 48 | line 3417 | NUMBER | 100 | [I2] stand note 8b current inv: India Infradebt Ltd Bond, units at 31 Mar 2026
R1746 | page 48 | line 3417 | NUMBER | 100.15 | [I2] stand note 8b current inv: India Infradebt Ltd Bond, amount at 31 Mar 2026
R1747 | page 48 | line 3418 | NUMBER | 1,370 | [I2] stand note 8b current inv: Kotak Mahindra Prime Ltd. Bond, units at 30 Sep 2026
R1748 | page 48 | line 3418 | NUMBER | 139.48 | [I2] stand note 8b current inv: Kotak Mahindra Prime Ltd. Bond, amount at 30 Sep 2026
R1749 | page 48 | line 3418 | NUMBER | - | [I2] stand note 8b current inv: Kotak Mahindra Prime Ltd. Bond, units at 31 Mar 2026 | ZERO_STANDING
R1750 | page 48 | line 3418 | NUMBER | - | [I2] stand note 8b current inv: Kotak Mahindra Prime Ltd. Bond, amount at 31 Mar 2026 | ZERO_STANDING
R1751 | page 48 | line 3419 | NUMBER | 250 | [I2] stand note 8b current inv: LIC Housing Finance Bond, units at 30 Sep 2026
R1752 | page 48 | line 3419 | NUMBER | 248.12 | [I2] stand note 8b current inv: LIC Housing Finance Bond, amount at 30 Sep 2026
R1753 | page 48 | line 3419 | NUMBER | - | [I2] stand note 8b current inv: LIC Housing Finance Bond, units at 31 Mar 2026 | ZERO_STANDING
R1754 | page 48 | line 3419 | NUMBER | - | [I2] stand note 8b current inv: LIC Housing Finance Bond, amount at 31 Mar 2026 | ZERO_STANDING
R1755 | page 48 | line 3420 | NUMBER | 7,500 | [I2] stand note 8b current inv: Mahindra & Mahindra Financial Services Ltd. B, units at 30 Sep 2026
R1756 | page 48 | line 3420 | NUMBER | 788.84 | [I2] stand note 8b current inv: Mahindra & Mahindra Financial Services Ltd. B, amount at 30 Sep 2026
R1757 | page 48 | line 3420 | NUMBER | 7,500 | [I2] stand note 8b current inv: Mahindra & Mahindra Financial Services Ltd. B, units at 31 Mar 2026
R1758 | page 48 | line 3420 | NUMBER | 761.15 | [I2] stand note 8b current inv: Mahindra & Mahindra Financial Services Ltd. B, amount at 31 Mar 2026
R1759 | page 48 | line 3421 | NUMBER | 10 | [I2] stand note 8b current inv: Punjab National Bank Perpetual Bond, units at 30 Sep 2026
R1760 | page 48 | line 3421 | NUMBER | 106.18 | [I2] stand note 8b current inv: Punjab National Bank Perpetual Bond, amount at 30 Sep 2026
R1761 | page 48 | line 3421 | NUMBER | 10 | [I2] stand note 8b current inv: Punjab National Bank Perpetual Bond, units at 31 Mar 2026
R1762 | page 48 | line 3421 | NUMBER | 102.32 | [I2] stand note 8b current inv: Punjab National Bank Perpetual Bond, amount at 31 Mar 2026
R1763 | page 48 | line 3422 | NUMBER | 10,000 | [I2] stand note 8b current inv: REC Zero Coupon Bond, units at 30 Sep 2026
R1764 | page 48 | line 3422 | NUMBER | 568.50 | [I2] stand note 8b current inv: REC Zero Coupon Bond, amount at 30 Sep 2026
R1765 | page 48 | line 3422 | NUMBER | 10,000 | [I2] stand note 8b current inv: REC Zero Coupon Bond, units at 31 Mar 2026
R1766 | page 48 | line 3422 | NUMBER | 561.84 | [I2] stand note 8b current inv: REC Zero Coupon Bond, amount at 31 Mar 2026
R1767 | page 48 | line 3423 | NUMBER | 250 | [I2] stand note 8b current inv: TATA Capital Limited Bond, units at 30 Sep 2026
R1768 | page 48 | line 3423 | NUMBER | 268.80 | [I2] stand note 8b current inv: TATA Capital Limited Bond, amount at 30 Sep 2026
R1769 | page 48 | line 3423 | NUMBER | 250 | [I2] stand note 8b current inv: TATA Capital Limited Bond, units at 31 Mar 2026
R1770 | page 48 | line 3423 | NUMBER | 259.63 | [I2] stand note 8b current inv: TATA Capital Limited Bond, amount at 31 Mar 2026
R1771 | page 48 | line 3424 | NUMBER | 70 | [I2] stand note 8b current inv: State Bank of India Perpetual Bond, units at 30 Sep 2026
R1772 | page 48 | line 3424 | NUMBER | 709.85 | [I2] stand note 8b current inv: State Bank of India Perpetual Bond, amount at 30 Sep 2026
R1773 | page 48 | line 3424 | NUMBER | 100 | [I2] stand note 8b current inv: State Bank of India Perpetual Bond, units at 31 Mar 2026
R1774 | page 48 | line 3424 | NUMBER | 1,039.24 | [I2] stand note 8b current inv: State Bank of India Perpetual Bond, amount at 31 Mar 2026
R1775 | page 48 | line 3425 | NUMBER | 15 | [I2] stand note 8b current inv: Union Bank of India Perpetual Bond, units at 30 Sep 2026
R1776 | page 48 | line 3425 | NUMBER | 157.62 | [I2] stand note 8b current inv: Union Bank of India Perpetual Bond, amount at 30 Sep 2026
R1777 | page 48 | line 3425 | NUMBER | 15 | [I2] stand note 8b current inv: Union Bank of India Perpetual Bond, units at 31 Mar 2026
R1778 | page 48 | line 3425 | NUMBER | 152.13 | [I2] stand note 8b current inv: Union Bank of India Perpetual Bond, amount at 31 Mar 2026
R1779 | page 48 | line 3426 | NUMBER | 6,149.56 | [I2] stand note 8b current inv: Total, amount at 30 Sep 2026
R1780 | page 48 | line 3426 | NUMBER | 5,242.25 | [I2] stand note 8b current inv: Total, amount at 31 Mar 2026
R1781 | page 48 | line 3429 | NUMBER | 1,00,00,000 | [I2] stand note 8b current inv: 7.18% Government of India 2037, units at 30 Sep 2026
R1782 | page 48 | line 3429 | NUMBER | 1,009.66 | [I2] stand note 8b current inv: 7.18% Government of India 2037, amount at 30 Sep 2026
R1783 | page 48 | line 3429 | NUMBER | 1,25,00,000 | [I2] stand note 8b current inv: 7.18% Government of India 2037, units at 31 Mar 2026
R1784 | page 48 | line 3429 | NUMBER | 1,265.15 | [I2] stand note 8b current inv: 7.18% Government of India 2037, amount at 31 Mar 2026
R1785 | page 48 | line 3430 | NUMBER | 10,00,000 | [I2] stand note 8b current inv: 7.44% Government of Karnataka SGS 2034, units at 30 Sep 2026
R1786 | page 48 | line 3430 | NUMBER | 98.98 | [I2] stand note 8b current inv: 7.44% Government of Karnataka SGS 2034, amount at 30 Sep 2026
R1787 | page 48 | line 3430 | NUMBER | 10,00,000 | [I2] stand note 8b current inv: 7.44% Government of Karnataka SGS 2034, units at 31 Mar 2026
R1788 | page 48 | line 3430 | NUMBER | 100.18 | [I2] stand note 8b current inv: 7.44% Government of Karnataka SGS 2034, amount at 31 Mar 2026
R1789 | page 48 | line 3431 | NUMBER | 35,00,000 | [I2] stand note 8b current inv: 7.42% Government of Karnataka SGS 2035, units at 30 Sep 2026
R1790 | page 48 | line 3431 | NUMBER | 343.18 | [I2] stand note 8b current inv: 7.42% Government of Karnataka SGS 2035, amount at 30 Sep 2026
R1791 | page 48 | line 3431 | NUMBER | 35,00,000 | [I2] stand note 8b current inv: 7.42% Government of Karnataka SGS 2035, units at 31 Mar 2026
R1792 | page 48 | line 3431 | NUMBER | 347.67 | [I2] stand note 8b current inv: 7.42% Government of Karnataka SGS 2035, amount at 31 Mar 2026
R1793 | page 48 | line 3432 | NUMBER | 25,00,000 | [I2] stand note 8b current inv: 7.45% Government of Karnataka SGS 2037, units at 30 Sep 2026
R1794 | page 48 | line 3432 | NUMBER | 243.11 | [I2] stand note 8b current inv: 7.45% Government of Karnataka SGS 2037, amount at 30 Sep 2026
R1795 | page 48 | line 3432 | NUMBER | 25,00,000 | [I2] stand note 8b current inv: 7.45% Government of Karnataka SGS 2037, units at 31 Mar 2026
R1796 | page 48 | line 3432 | NUMBER | 245.75 | [I2] stand note 8b current inv: 7.45% Government of Karnataka SGS 2037, amount at 31 Mar 2026
R1797 | page 48 | line 3433 | NUMBER | 20,00,000 | [I2] stand note 8b current inv: 7.43% Government of Tamil Nadu SGS 2034, units at 30 Sep 2026
R1798 | page 48 | line 3433 | NUMBER | 196.65 | [I2] stand note 8b current inv: 7.43% Government of Tamil Nadu SGS 2034, amount at 30 Sep 2026
R1799 | page 48 | line 3433 | NUMBER | 20,00,000 | [I2] stand note 8b current inv: 7.43% Government of Tamil Nadu SGS 2034, units at 31 Mar 2026
R1800 | page 48 | line 3433 | NUMBER | 199.05 | [I2] stand note 8b current inv: 7.43% Government of Tamil Nadu SGS 2034, amount at 31 Mar 2026
R1801 | page 48 | line 3434 | NUMBER | 25,00,000 | [I2] stand note 8b current inv: 7.72% Government of Maharashtra SGS 2035, units at 30 Sep 2026
R1802 | page 48 | line 3434 | NUMBER | 252.74 | [I2] stand note 8b current inv: 7.72% Government of Maharashtra SGS 2035, amount at 30 Sep 2026
R1803 | page 48 | line 3434 | NUMBER | 25,00,000 | [I2] stand note 8b current inv: 7.72% Government of Maharashtra SGS 2035, units at 31 Mar 2026
R1804 | page 48 | line 3434 | NUMBER | 256.14 | [I2] stand note 8b current inv: 7.72% Government of Maharashtra SGS 2035, amount at 31 Mar 2026
R1805 | page 48 | line 3435 | NUMBER | 25,00,000 | [I2] stand note 8b current inv: 7.40% Government of Maharashtra SGS 2035, units at 30 Sep 2026
R1806 | page 48 | line 3435 | NUMBER | 244.82 | [I2] stand note 8b current inv: 7.40% Government of Maharashtra SGS 2035, amount at 30 Sep 2026
R1807 | page 48 | line 3435 | NUMBER | 25,00,000 | [I2] stand note 8b current inv: 7.40% Government of Maharashtra SGS 2035, units at 31 Mar 2026
R1808 | page 48 | line 3435 | NUMBER | 248.01 | [I2] stand note 8b current inv: 7.40% Government of Maharashtra SGS 2035, amount at 31 Mar 2026
R1809 | page 48 | line 3436 | NUMBER | 35,00,000 | [I2] stand note 8b current inv: 7.73% Government of Maharashtra SGS 2036, units at 30 Sep 2026
R1810 | page 48 | line 3436 | NUMBER | 353.22 | [I2] stand note 8b current inv: 7.73% Government of Maharashtra SGS 2036, amount at 30 Sep 2026
R1811 | page 48 | line 3436 | NUMBER | 35,00,000 | [I2] stand note 8b current inv: 7.73% Government of Maharashtra SGS 2036, units at 31 Mar 2026
R1812 | page 48 | line 3436 | NUMBER | 357.85 | [I2] stand note 8b current inv: 7.73% Government of Maharashtra SGS 2036, amount at 31 Mar 2026
R1813 | page 48 | line 3437 | NUMBER | 10,00,000 | [I2] stand note 8b current inv: 6.48% Government of India 2035, units at 30 Sep 2026
R1814 | page 48 | line 3437 | NUMBER | 98.65 | [I2] stand note 8b current inv: 6.48% Government of India 2035, amount at 30 Sep 2026
R1815 | page 48 | line 3437 | NUMBER | - | [I2] stand note 8b current inv: 6.48% Government of India 2035, units at 31 Mar 2026 | ZERO_STANDING
R1816 | page 48 | line 3437 | NUMBER | - | [I2] stand note 8b current inv: 6.48% Government of India 2035, amount at 31 Mar 2026 | ZERO_STANDING
R1817 | page 48 | line 3438 | NUMBER | 25,00,000 | [I2] stand note 8b current inv: 7.38% Government of Tamil Nadu SGS 2034, units at 30 Sep 2026
R1818 | page 48 | line 3438 | NUMBER | 251.03 | [I2] stand note 8b current inv: 7.38% Government of Tamil Nadu SGS 2034, amount at 30 Sep 2026
R1819 | page 48 | line 3438 | NUMBER | 25,00,000 | [I2] stand note 8b current inv: 7.38% Government of Tamil Nadu SGS 2034, units at 31 Mar 2026
R1820 | page 48 | line 3438 | NUMBER | 254.06 | [I2] stand note 8b current inv: 7.38% Government of Tamil Nadu SGS 2034, amount at 31 Mar 2026
R1821 | page 48 | line 3439 | NUMBER | 20,00,000 | [I2] stand note 8b current inv: 7.34% Government of Tamil Nadu SGS 2034, units at 30 Sep 2026
R1822 | page 48 | line 3439 | NUMBER | 198.03 | [I2] stand note 8b current inv: 7.34% Government of Tamil Nadu SGS 2034, amount at 30 Sep 2026
R1823 | page 48 | line 3439 | NUMBER | 20,00,000 | [I2] stand note 8b current inv: 7.34% Government of Tamil Nadu SGS 2034, units at 31 Mar 2026
R1824 | page 48 | line 3439 | NUMBER | 200.50 | [I2] stand note 8b current inv: 7.34% Government of Tamil Nadu SGS 2034, amount at 31 Mar 2026
R1825 | page 48 | line 3440 | NUMBER | 35,00,000 | [I2] stand note 8b current inv: 6.68% Government of India 2040, units at 30 Sep 2026
R1826 | page 48 | line 3440 | NUMBER | 336.06 | [I2] stand note 8b current inv: 6.68% Government of India 2040, amount at 30 Sep 2026
R1827 | page 48 | line 3440 | NUMBER | - | [I2] stand note 8b current inv: 6.68% Government of India 2040, units at 31 Mar 2026 | ZERO_STANDING
R1828 | page 48 | line 3440 | NUMBER | - | [I2] stand note 8b current inv: 6.68% Government of India 2040, amount at 31 Mar 2026 | ZERO_STANDING
R1829 | page 48 | line 3441 | NUMBER | 3,626.13 | [I2] stand note 8b current inv: Total, amount at 30 Sep 2026
R1830 | page 48 | line 3441 | NUMBER | 3,474.36 | [I2] stand note 8b current inv: Total, amount at 31 Mar 2026
R1831 | page 48 | line 3444 | NUMBER | - | [I2] stand note 8b current inv: TREPS Lending, units at 30 Sep 2026 | ZERO_STANDING
R1832 | page 48 | line 3444 | NUMBER | 91.99 | [I2] stand note 8b current inv: TREPS Lending, amount at 30 Sep 2026
R1833 | page 48 | line 3444 | NUMBER | - | [I2] stand note 8b current inv: TREPS Lending, units at 31 Mar 2026 | ZERO_STANDING
R1834 | page 48 | line 3444 | NUMBER | - | [I2] stand note 8b current inv: TREPS Lending, amount at 31 Mar 2026 | ZERO_STANDING
R1835 | page 48 | line 3446 | NUMBER | 91.99 | [I2] stand note 8b current inv: Total, amount at 30 Sep 2026
R1836 | page 48 | line 3446 | NUMBER | - | [I2] stand note 8b current inv: Total, amount at 31 Mar 2026 | ZERO_STANDING
R1837 | page 48 | line 3448 | NUMBER | 27,883.04 | [I2] stand note 8b current inv: Aggregate book value of quoted investments, amount at 30 Sep 2026
R1838 | page 48 | line 3448 | NUMBER | 28,525.85 | [I2] stand note 8b current inv: Aggregate book value of quoted investments, amount at 31 Mar 2026
R1839 | page 48 | line 3449 | NUMBER | 27,883.04 | [I2] stand note 8b current inv: Aggregate market value of quoted investments, amount at 30 Sep 2026
R1840 | page 48 | line 3449 | NUMBER | 28,525.85 | [I2] stand note 8b current inv: Aggregate market value of quoted investments, amount at 31 Mar 2026
R1841 | page 48 | line 3450 | NUMBER | 3,977.01 | [I2] stand note 8b current inv: Aggregate carrying value of unquoted investme, amount at 30 Sep 2026
R1842 | page 48 | line 3450 | NUMBER | 3,426.75 | [I2] stand note 8b current inv: Aggregate carrying value of unquoted investme, amount at 31 Mar 2026
R1843 | page 49 | line 3472 | NUMBER | 218.10 | [I2] stand note 8 loans, other fin assets: -LIC^, at 30 Sep 2026
R1844 | page 49 | line 3472 | NUMBER | 210.40 | [I2] stand note 8 loans, other fin assets: -LIC^, at 31 Mar 2026
R1845 | page 49 | line 3473 | NUMBER | 544.91 | [I2] stand note 8 loans, other fin assets: -PNB Housing Finance Ltd.^, at 30 Sep 2026
R1846 | page 49 | line 3473 | NUMBER | 525.66 | [I2] stand note 8 loans, other fin assets: -PNB Housing Finance Ltd.^, at 31 Mar 2026
R1847 | page 49 | line 3475 | NUMBER | 0.36 | [I2] stand note 8 loans, other fin assets: Loans to employees*, at 30 Sep 2026
R1848 | page 49 | line 3475 | NUMBER | 1.19 | [I2] stand note 8 loans, other fin assets: Loans to employees*, at 31 Mar 2026
R1849 | page 49 | line 3480 | NUMBER | 763.37 | [I2] stand note 8 loans, other fin assets: Loans to employees*, at 30 Sep 2026
R1850 | page 49 | line 3480 | NUMBER | 737.25 | [I2] stand note 8 loans, other fin assets: Loans to employees*, at 31 Mar 2026
R1851 | page 49 | line 3475 | NUMBER | 6.07 | [I2] stand note 8 loans, other fin assets: Loans to employees*, at 30 Sep 2026
R1852 | page 49 | line 3475 | NUMBER | 6.05 | [I2] stand note 8 loans, other fin assets: Loans to employees*, at 31 Mar 2026
R1853 | page 49 | line 3490 | NUMBER | 42.26 | [I2] stand note 8 loans, other fin assets: Security deposits, at 30 Sep 2026
R1854 | page 49 | line 3490 | NUMBER | 36.64 | [I2] stand note 8 loans, other fin assets: Security deposits, at 31 Mar 2026
R1855 | page 49 | line 3492 | NUMBER | 645.39 | [I2] stand note 8 loans, other fin assets: - Deposits with maturity of more than twelve , at 30 Sep 2026
R1856 | page 49 | line 3492 | NUMBER | 623.33 | [I2] stand note 8 loans, other fin assets: - Deposits with maturity of more than twelve , at 31 Mar 2026
R1857 | page 49 | line 3492 | NUMBER | 687.65 | [I2] stand note 8 loans, other fin assets: ts with maturity of more than twelve months**, at 30 Sep 2026
R1858 | page 49 | line 3492 | NUMBER | 659.97 | [I2] stand note 8 loans, other fin assets: ts with maturity of more than twelve months**, at 31 Mar 2026
R1859 | page 49 | line 3495 | NUMBER | 40.76 | [I2] stand note 8 loans, other fin assets: Security deposits, at 30 Sep 2026
R1860 | page 49 | line 3495 | NUMBER | 40.43 | [I2] stand note 8 loans, other fin assets: Security deposits, at 31 Mar 2026
R1861 | page 49 | line 3496 | NUMBER | 54.34 | [I2] stand note 8 loans, other fin assets: Amount recoverable from payment gateway, at 30 Sep 2026
R1862 | page 49 | line 3496 | NUMBER | 191.78 | [I2] stand note 8 loans, other fin assets: Amount recoverable from payment gateway, at 31 Mar 2026
R1863 | page 49 | line 3497 | NUMBER | 11.86 | [I2] stand note 8 loans, other fin assets: Other receivables *, at 30 Sep 2026
R1864 | page 49 | line 3497 | NUMBER | 0.10 | [I2] stand note 8 loans, other fin assets: Other receivables *, at 31 Mar 2026
R1865 | page 49 | line 3497 | NUMBER | 106.96 | [I2] stand note 8 loans, other fin assets: Other receivables *, at 30 Sep 2026
R1866 | page 49 | line 3497 | NUMBER | 232.31 | [I2] stand note 8 loans, other fin assets: Other receivables *, at 31 Mar 2026
R1867 | page 49 | line 3500 | NUMBER | 3 to 9 years | [I2] stated in note text: Security deposits are non-interest beari
R1868 | page 49 | line 3483 | NUMBER | 24 monthly instalments | [I2] stated in note text: *Represent interest free loans to employ
R1869 | page 56 | line 3908 | NUMBER | 21,733.48 | [I2] stand note 28 fair value: Level1, at 30 Sep 2026
R1870 | page 56 | line 3908 | NUMBER | 23,283.60 | [I2] stand note 28 fair value: Level1, at 31 Mar 2026
R1871 | page 56 | line 3924 | NUMBER | 6,149.56 | [I2] stand note 28 fair value: - Investment in bonds & debentures (Refer Not, at 30 Sep 2026
R1872 | page 56 | line 3924 | NUMBER | 5,242.25 | [I2] stand note 28 fair value: - Investment in bonds & debentures (Refer Not, at 31 Mar 2026
R1873 | page 56 | line 3925 | NUMBER | 3,885.02 | [I2] stand note 28 fair value: - Investment in equity/preference instruments, at 30 Sep 2026
R1874 | page 56 | line 3925 | NUMBER | 3,426.75 | [I2] stand note 28 fair value: - Investment in equity/preference instruments, at 31 Mar 2026
R1875 | page 56 | line 3925 | NUMBER | 31,768.06 | [I2] stand note 28 fair value: eference instruments of other entities Level3, at 30 Sep 2026
R1876 | page 56 | line 3925 | NUMBER | 31,952.60 | [I2] stand note 28 fair value: eference instruments of other entities Level3, at 31 Mar 2026
R1877 | page 56 | line 3929 | NUMBER | 91.99 | [I2] stand note 28 fair value: - Investment in TREPS, at 30 Sep 2026
R1878 | page 56 | line 3929 | NUMBER | - | [I2] stand note 28 fair value: - Investment in TREPS, at 31 Mar 2026 | ZERO_STANDING
R1879 | page 56 | line 3930 | NUMBER | 10.44 | [I2] stand note 28 fair value: - Trade receivables, at 30 Sep 2026
R1880 | page 56 | line 3930 | NUMBER | 11.24 | [I2] stand note 28 fair value: - Trade receivables, at 31 Mar 2026
R1881 | page 56 | line 3931 | NUMBER | 314.37 | [I2] stand note 28 fair value: - Cash and cash equivalents, at 30 Sep 2026
R1882 | page 56 | line 3931 | NUMBER | 770.54 | [I2] stand note 28 fair value: - Cash and cash equivalents, at 31 Mar 2026
R1883 | page 56 | line 3932 | NUMBER | 763.01 | [I2] stand note 28 fair value: - Intercorporate deposits with financial inst, at 30 Sep 2026
R1884 | page 56 | line 3932 | NUMBER | 736.06 | [I2] stand note 28 fair value: - Intercorporate deposits with financial inst, at 31 Mar 2026
R1885 | page 56 | line 3933 | NUMBER | 6.43 | [I2] stand note 28 fair value: - Loans to employees, at 30 Sep 2026
R1886 | page 56 | line 3933 | NUMBER | 7.24 | [I2] stand note 28 fair value: - Loans to employees, at 31 Mar 2026
R1887 | page 56 | line 3934 | NUMBER | 83.02 | [I2] stand note 28 fair value: - Security deposits, at 30 Sep 2026
R1888 | page 56 | line 3934 | NUMBER | 77.07 | [I2] stand note 28 fair value: - Security deposits, at 31 Mar 2026
R1889 | page 56 | line 3935 | NUMBER | 650.16 | [I2] stand note 28 fair value: - Deposits with Banks, at 30 Sep 2026
R1890 | page 56 | line 3935 | NUMBER | 626.63 | [I2] stand note 28 fair value: - Deposits with Banks, at 31 Mar 2026
R1891 | page 56 | line 3936 | NUMBER | 66.20 | [I2] stand note 28 fair value: - Other financial assets, at 30 Sep 2026
R1892 | page 56 | line 3936 | NUMBER | 191.88 | [I2] stand note 28 fair value: - Other financial assets, at 31 Mar 2026
R1893 | page 56 | line 3936 | NUMBER | 1,985.62 | [I2] stand note 28 fair value: - Other financial assets, at 30 Sep 2026
R1894 | page 56 | line 3936 | NUMBER | 2,420.66 | [I2] stand note 28 fair value: - Other financial assets, at 31 Mar 2026
R1895 | page 56 | line 3938 | NUMBER | 33,753.68 | [I2] stand note 28 fair value: Total (a+b), at 30 Sep 2026
R1896 | page 56 | line 3938 | NUMBER | 34,373.26 | [I2] stand note 28 fair value: Total (a+b), at 31 Mar 2026
R1897 | page 56 | line 3942 | NUMBER | 329.79 | [I2] stand note 28 fair value: - Trade payables, at 30 Sep 2026
R1898 | page 56 | line 3942 | NUMBER | 259.21 | [I2] stand note 28 fair value: - Trade payables, at 31 Mar 2026
R1899 | page 56 | line 3943 | NUMBER | 166.24 | [I2] stand note 28 fair value: - Other financial liabilities, at 30 Sep 2026
R1900 | page 56 | line 3943 | NUMBER | 213.45 | [I2] stand note 28 fair value: - Other financial liabilities, at 31 Mar 2026
R1901 | page 56 | line 3944 | NUMBER | 201.09 | [I2] stand note 28 fair value: - Lease liabilities, at 30 Sep 2026
R1902 | page 56 | line 3944 | NUMBER | 231.02 | [I2] stand note 28 fair value: - Lease liabilities, at 31 Mar 2026
R1903 | page 56 | line 3945 | NUMBER | 697.12 | [I2] stand note 28 fair value: Total, at 30 Sep 2026
R1904 | page 56 | line 3945 | NUMBER | 703.68 | [I2] stand note 28 fair value: Total, at 31 Mar 2026
R1905 | page 57 | line 3997 | NUMBER | 55.50 | [I2] stand note 28 fair value level 3: Opening balance, qtr Sep 2026
R1906 | page 57 | line 3997 | NUMBER | 183.56 | [I2] stand note 28 fair value level 3: Opening balance, qtr Sep 2025
R1907 | page 57 | line 3997 | NUMBER | 183.56 | [I2] stand note 28 fair value level 3: Opening balance, 6M Sep 2026
R1908 | page 57 | line 3997 | NUMBER | 183.56 | [I2] stand note 28 fair value level 3: Opening balance, 6M Sep 2025
R1909 | page 57 | line 3998 | NUMBER | - | [I2] stand note 28 fair value level 3: Conversion of preference shares into equity s, qtr Sep 2026 | ZERO_STANDING
R1910 | page 57 | line 3998 | NUMBER | - | [I2] stand note 28 fair value level 3: Conversion of preference shares into equity s, qtr Sep 2025 | ZERO_STANDING
R1911 | page 57 | line 3998 | NUMBER | (128.06) | [I2] stand note 28 fair value level 3: Conversion of preference shares into equity s, 6M Sep 2026
R1912 | page 57 | line 3998 | NUMBER | - | [I2] stand note 28 fair value level 3: Conversion of preference shares into equity s, 6M Sep 2025 | ZERO_STANDING
R1913 | page 57 | line 4000 | NUMBER | 55.50 | [I2] stand note 28 fair value level 3: Closing balance, qtr Sep 2026
R1914 | page 57 | line 4000 | NUMBER | 183.56 | [I2] stand note 28 fair value level 3: Closing balance, qtr Sep 2025
R1915 | page 57 | line 4000 | NUMBER | 55.50 | [I2] stand note 28 fair value level 3: Closing balance, 6M Sep 2026
R1916 | page 57 | line 4000 | NUMBER | 183.56 | [I2] stand note 28 fair value level 3: Closing balance, 6M Sep 2025
R1917 | page 57 | line 4008 | NUMBER | 3,829.52 | [I2] stand note 28 fair value level 3: Opening balance, qtr Sep 2026
R1918 | page 57 | line 4008 | NUMBER | 2,237.73 | [I2] stand note 28 fair value level 3: Opening balance, qtr Sep 2025
R1919 | page 57 | line 4008 | NUMBER | 3,243.19 | [I2] stand note 28 fair value level 3: Opening balance, 6M Sep 2026
R1920 | page 57 | line 4008 | NUMBER | 3,366.10 | [I2] stand note 28 fair value level 3: Opening balance, 6M Sep 2025
R1921 | page 57 | line 4009 | NUMBER | - | [I2] stand note 28 fair value level 3: Fair value change recognised in profit or los, qtr Sep 2026 | ZERO_STANDING
R1922 | page 57 | line 4009 | NUMBER | - | [I2] stand note 28 fair value level 3: Fair value change recognised in profit or los, qtr Sep 2025 | ZERO_STANDING
R1923 | page 57 | line 4009 | NUMBER | (200.00) | [I2] stand note 28 fair value level 3: Fair value change recognised in profit or los, 6M Sep 2026
R1924 | page 57 | line 4009 | NUMBER | - | [I2] stand note 28 fair value level 3: Fair value change recognised in profit or los, 6M Sep 2025 | ZERO_STANDING
R1925 | page 57 | line 4010 | NUMBER | - | [I2] stand note 28 fair value level 3: Change in status of investment to Other entit, qtr Sep 2026 | ZERO_STANDING
R1926 | page 57 | line 4010 | NUMBER | - | [I2] stand note 28 fair value level 3: Change in status of investment to Other entit, qtr Sep 2025 | ZERO_STANDING
R1927 | page 57 | line 4010 | NUMBER | 786.33 | [I2] stand note 28 fair value level 3: Change in status of investment to Other entit, 6M Sep 2026
R1928 | page 57 | line 4010 | NUMBER | - | [I2] stand note 28 fair value level 3: Change in status of investment to Other entit, 6M Sep 2025 | ZERO_STANDING
R1929 | page 57 | line 4011 | NUMBER | - | [I2] stand note 28 fair value level 3: Change in status of investment to Associate, qtr Sep 2026 | ZERO_STANDING
R1930 | page 57 | line 4011 | NUMBER | - | [I2] stand note 28 fair value level 3: Change in status of investment to Associate, qtr Sep 2025 | ZERO_STANDING
R1931 | page 57 | line 4011 | NUMBER | - | [I2] stand note 28 fair value level 3: Change in status of investment to Associate, 6M Sep 2026 | ZERO_STANDING
R1932 | page 57 | line 4011 | NUMBER | (1,128.37) | [I2] stand note 28 fair value level 3: Change in status of investment to Associate, 6M Sep 2025
R1933 | page 57 | line 4012 | NUMBER | 3,829.52 | [I2] stand note 28 fair value level 3: Closing balance, qtr Sep 2026
R1934 | page 57 | line 4012 | NUMBER | 2,237.73 | [I2] stand note 28 fair value level 3: Closing balance, qtr Sep 2025
R1935 | page 57 | line 4012 | NUMBER | 3,829.52 | [I2] stand note 28 fair value level 3: Closing balance, 6M Sep 2026
R1936 | page 57 | line 4012 | NUMBER | 2,237.73 | [I2] stand note 28 fair value level 3: Closing balance, 6M Sep 2025
R1937 | page 57 | line 4018 | NUMBER | - | [I2] stand note 28 fair value level 3: Opening balance, qtr Sep 2026 | ZERO_STANDING
R1938 | page 57 | line 4018 | NUMBER | - | [I2] stand note 28 fair value level 3: Opening balance, qtr Sep 2025 | ZERO_STANDING
R1939 | page 57 | line 4018 | NUMBER | - | [I2] stand note 28 fair value level 3: Opening balance, 6M Sep 2026 | ZERO_STANDING
R1940 | page 57 | line 4018 | NUMBER | 21.10 | [I2] stand note 28 fair value level 3: Opening balance, 6M Sep 2025
R1941 | page 57 | line 3998 | NUMBER | - | [I2] stand note 28 fair value level 3: Conversion, qtr Sep 2026 | ZERO_STANDING
R1942 | page 57 | line 3998 | NUMBER | - | [I2] stand note 28 fair value level 3: Conversion, qtr Sep 2025 | ZERO_STANDING
R1943 | page 57 | line 3998 | NUMBER | - | [I2] stand note 28 fair value level 3: Conversion, 6M Sep 2026 | ZERO_STANDING
R1944 | page 57 | line 3998 | NUMBER | (21.10) | [I2] stand note 28 fair value level 3: Conversion, 6M Sep 2025
R1945 | page 57 | line 4020 | NUMBER | - | [I2] stand note 28 fair value level 3: Closing balance, qtr Sep 2026 | ZERO_STANDING
R1946 | page 57 | line 4020 | NUMBER | - | [I2] stand note 28 fair value level 3: Closing balance, qtr Sep 2025 | ZERO_STANDING
R1947 | page 57 | line 4020 | NUMBER | - | [I2] stand note 28 fair value level 3: Closing balance, 6M Sep 2026 | ZERO_STANDING
R1948 | page 57 | line 4020 | NUMBER | - | [I2] stand note 28 fair value level 3: Closing balance, 6M Sep 2025 | ZERO_STANDING
R1949 | page 29 | line 2165 | NUMBER | 47.81 | [I3] cons note 30 RPT list: Short-term employee benefits, qtr Sep 2026
R1950 | page 29 | line 2165 | NUMBER | 46.14 | [I3] cons note 30 RPT list: Short-term employee benefits, qtr Sep 2025
R1951 | page 29 | line 2165 | NUMBER | 97.13 | [I3] cons note 30 RPT list: Short-term employee benefits, 6M Sep 2026
R1952 | page 29 | line 2165 | NUMBER | 92.15 | [I3] cons note 30 RPT list: Short-term employee benefits, 6M Sep 2025
R1953 | page 29 | line 2166 | NUMBER | (0.02) | [I3] cons note 30 RPT list: Post-employment benefits, qtr Sep 2026
R1954 | page 29 | line 2166 | NUMBER | 0.02 | [I3] cons note 30 RPT list: Post-employment benefits, qtr Sep 2025
R1955 | page 29 | line 2166 | NUMBER | 0.14 | [I3] cons note 30 RPT list: Post-employment benefits, 6M Sep 2026
R1956 | page 29 | line 2166 | NUMBER | 0.87 | [I3] cons note 30 RPT list: Post-employment benefits, 6M Sep 2025
R1957 | page 29 | line 2167 | NUMBER | 0.05 | [I3] cons note 30 RPT list: Other long-term employee benefits, qtr Sep 2026
R1958 | page 29 | line 2167 | NUMBER | 0.65 | [I3] cons note 30 RPT list: Other long-term employee benefits, qtr Sep 2025
R1959 | page 29 | line 2167 | NUMBER | 1.29 | [I3] cons note 30 RPT list: Other long-term employee benefits, 6M Sep 2026
R1960 | page 29 | line 2167 | NUMBER | 1.83 | [I3] cons note 30 RPT list: Other long-term employee benefits, 6M Sep 2025
R1961 | page 29 | line 2168 | NUMBER | 3.31 | [I3] cons note 30 RPT list: Employee share based payment, qtr Sep 2026
R1962 | page 29 | line 2168 | NUMBER | 5.03 | [I3] cons note 30 RPT list: Employee share based payment, qtr Sep 2025
R1963 | page 29 | line 2168 | NUMBER | 7.10 | [I3] cons note 30 RPT list: Employee share based payment, 6M Sep 2026
R1964 | page 29 | line 2168 | NUMBER | 7.10 | [I3] cons note 30 RPT list: Employee share based payment, 6M Sep 2025
R1965 | page 29 | line 2168 | NUMBER | 51.15 | [I3] cons note 30 RPT list: Employee share based payment, qtr Sep 2026
R1966 | page 29 | line 2168 | NUMBER | 51.84 | [I3] cons note 30 RPT list: Employee share based payment, qtr Sep 2025
R1967 | page 29 | line 2168 | NUMBER | 105.66 | [I3] cons note 30 RPT list: Employee share based payment, 6M Sep 2026
R1968 | page 29 | line 2168 | NUMBER | 101.95 | [I3] cons note 30 RPT list: Employee share based payment, 6M Sep 2025
R1969 | page 30 | line 2187 | NUMBER | 1.72 | [I3] cons note 30 RPT transactions: Mansa Enterprises Private Limited, qtr Sep 2026
R1970 | page 30 | line 2187 | NUMBER | 1.58 | [I3] cons note 30 RPT transactions: Mansa Enterprises Private Limited, qtr Sep 2025
R1971 | page 30 | line 2187 | NUMBER | 3.42 | [I3] cons note 30 RPT transactions: Mansa Enterprises Private Limited, 6M Sep 2026
R1972 | page 30 | line 2187 | NUMBER | 3.19 | [I3] cons note 30 RPT transactions: Mansa Enterprises Private Limited, 6M Sep 2025
R1973 | page 30 | line 2190 | NUMBER | - | [I3] cons note 30 RPT transactions: S R Dinodia & Co LLP, qtr Sep 2026 | ZERO_STANDING
R1974 | page 30 | line 2190 | NUMBER | 0.74 | [I3] cons note 30 RPT transactions: S R Dinodia & Co LLP, qtr Sep 2025
R1975 | page 30 | line 2190 | NUMBER | 0.13 | [I3] cons note 30 RPT transactions: S R Dinodia & Co LLP, 6M Sep 2026
R1976 | page 30 | line 2190 | NUMBER | 1.08 | [I3] cons note 30 RPT transactions: S R Dinodia & Co LLP, 6M Sep 2025
R1977 | page 30 | line 2194 | NUMBER | - | [I3] cons note 30 RPT transactions: Key management personnel, qtr Sep 2026 | ZERO_STANDING
R1978 | page 30 | line 2194 | NUMBER | 0.75 | [I3] cons note 30 RPT transactions: Key management personnel, qtr Sep 2025
R1979 | page 30 | line 2194 | NUMBER | 0.83 | [I3] cons note 30 RPT transactions: Key management personnel, 6M Sep 2026
R1980 | page 30 | line 2194 | NUMBER | 1.50 | [I3] cons note 30 RPT transactions: Key management personnel, 6M Sep 2025
R1981 | page 30 | line 2197 | NUMBER | 1,694.77 | [I3] cons note 30 RPT transactions: Key management personnel, qtr Sep 2026
R1982 | page 30 | line 2197 | NUMBER | - | [I3] cons note 30 RPT transactions: Key management personnel, qtr Sep 2025 | ZERO_STANDING
R1983 | page 30 | line 2197 | NUMBER | 1,694.77 | [I3] cons note 30 RPT transactions: Key management personnel, 6M Sep 2026
R1984 | page 30 | line 2197 | NUMBER | 1,413.43 | [I3] cons note 30 RPT transactions: Key management personnel, 6M Sep 2025
R1985 | page 30 | line 2198 | NUMBER | 66.36 | [I3] cons note 30 RPT transactions: Relatives of Key Management Personnel, qtr Sep 2026
R1986 | page 30 | line 2198 | NUMBER | - | [I3] cons note 30 RPT transactions: Relatives of Key Management Personnel, qtr Sep 2025 | ZERO_STANDING
R1987 | page 30 | line 2198 | NUMBER | 66.36 | [I3] cons note 30 RPT transactions: Relatives of Key Management Personnel, 6M Sep 2026
R1988 | page 30 | line 2198 | NUMBER | 55.70 | [I3] cons note 30 RPT transactions: Relatives of Key Management Personnel, 6M Sep 2025
R1989 | page 30 | line 2199 | NUMBER | 7.09 | [I3] cons note 30 RPT transactions: Entities where Key Management Personnel exerc, qtr Sep 2026
R1990 | page 30 | line 2199 | NUMBER | - | [I3] cons note 30 RPT transactions: Entities where Key Management Personnel exerc, qtr Sep 2025 | ZERO_STANDING
R1991 | page 30 | line 2199 | NUMBER | 7.09 | [I3] cons note 30 RPT transactions: Entities where Key Management Personnel exerc, 6M Sep 2026
R1992 | page 30 | line 2199 | NUMBER | 6.49 | [I3] cons note 30 RPT transactions: Entities where Key Management Personnel exerc, 6M Sep 2025
R1993 | page 30 | line 2202 | NUMBER | 4.15 | [I3] cons note 30 RPT transactions: Relatives of Key Management Personnel, qtr Sep 2026
R1994 | page 30 | line 2202 | NUMBER | 1.69 | [I3] cons note 30 RPT transactions: Relatives of Key Management Personnel, qtr Sep 2025
R1995 | page 30 | line 2202 | NUMBER | 8.42 | [I3] cons note 30 RPT transactions: Relatives of Key Management Personnel, 6M Sep 2026
R1996 | page 30 | line 2202 | NUMBER | 3.42 | [I3] cons note 30 RPT transactions: Relatives of Key Management Personnel, 6M Sep 2025
R1997 | page 30 | line 2204 | NUMBER | 1.10 | [I3] cons note 30 RPT transactions: Director's sitting fees, qtr Sep 2026
R1998 | page 30 | line 2204 | NUMBER | 1.80 | [I3] cons note 30 RPT transactions: Director's sitting fees, qtr Sep 2025
R1999 | page 30 | line 2204 | NUMBER | 3.40 | [I3] cons note 30 RPT transactions: Director's sitting fees, 6M Sep 2026
R2000 | page 30 | line 2204 | NUMBER | 3.50 | [I3] cons note 30 RPT transactions: Director's sitting fees, 6M Sep 2025
R2001 | page 30 | line 2206 | NUMBER | 1.50 | [I3] cons note 30 RPT transactions: Loans to KMP, qtr Sep 2026
R2002 | page 30 | line 2206 | NUMBER | - | [I3] cons note 30 RPT transactions: Loans to KMP, qtr Sep 2025 | ZERO_STANDING
R2003 | page 30 | line 2206 | NUMBER | 1.50 | [I3] cons note 30 RPT transactions: Loans to KMP, 6M Sep 2026
R2004 | page 30 | line 2206 | NUMBER | - | [I3] cons note 30 RPT transactions: Loans to KMP, 6M Sep 2025 | ZERO_STANDING
R2005 | page 30 | line 2210 | NUMBER | 649.88 | [I3] cons note 30 RPT transactions: Fleetex Technologies Private Limited, qtr Sep 2026
R2006 | page 30 | line 2210 | NUMBER | - | [I3] cons note 30 RPT transactions: Fleetex Technologies Private Limited, qtr Sep 2025 | ZERO_STANDING
R2007 | page 30 | line 2210 | NUMBER | 649.88 | [I3] cons note 30 RPT transactions: Fleetex Technologies Private Limited, 6M Sep 2026
R2008 | page 30 | line 2210 | NUMBER | 410.00 | [I3] cons note 30 RPT transactions: Fleetex Technologies Private Limited, 6M Sep 2025
R2009 | page 30 | line 2213 | NUMBER | 172.47 | [I3] cons note 30 RPT transactions: Agillos E-Commerce Private Limited, qtr Sep 2026
R2010 | page 30 | line 2213 | NUMBER | - | [I3] cons note 30 RPT transactions: Agillos E-Commerce Private Limited, qtr Sep 2025 | ZERO_STANDING
R2011 | page 30 | line 2213 | NUMBER | 172.47 | [I3] cons note 30 RPT transactions: Agillos E-Commerce Private Limited, 6M Sep 2026
R2012 | page 30 | line 2213 | NUMBER | - | [I3] cons note 30 RPT transactions: Agillos E-Commerce Private Limited, 6M Sep 2025 | ZERO_STANDING
R2013 | page 30 | line 2216 | NUMBER | 1.71 | [I3] cons note 30 RPT transactions: Simply Vyapar Apps Private Limited, qtr Sep 2026
R2014 | page 30 | line 2216 | NUMBER | 1.56 | [I3] cons note 30 RPT transactions: Simply Vyapar Apps Private Limited, qtr Sep 2025
R2015 | page 30 | line 2216 | NUMBER | 3.22 | [I3] cons note 30 RPT transactions: Simply Vyapar Apps Private Limited, 6M Sep 2026
R2016 | page 30 | line 2216 | NUMBER | 2.86 | [I3] cons note 30 RPT transactions: Simply Vyapar Apps Private Limited, 6M Sep 2025
R2017 | page 30 | line 2217 | NUMBER | - | [I3] cons note 30 RPT transactions: IB Monotaro Private Limited, qtr Sep 2026 | ZERO_STANDING
R2018 | page 30 | line 2217 | NUMBER | 0.50 | [I3] cons note 30 RPT transactions: IB Monotaro Private Limited, qtr Sep 2025
R2019 | page 30 | line 2217 | NUMBER | 0.28 | [I3] cons note 30 RPT transactions: IB Monotaro Private Limited, 6M Sep 2026
R2020 | page 30 | line 2217 | NUMBER | 0.99 | [I3] cons note 30 RPT transactions: IB Monotaro Private Limited, 6M Sep 2025
R2021 | page 30 | line 2219 | NUMBER | 1.50 | [I3] cons note 30 RPT transactions: Repayment of Loan by KMP, qtr Sep 2026
R2022 | page 30 | line 2219 | NUMBER | - | [I3] cons note 30 RPT transactions: Repayment of Loan by KMP, qtr Sep 2025 | ZERO_STANDING
R2023 | page 30 | line 2219 | NUMBER | 1.50 | [I3] cons note 30 RPT transactions: Repayment of Loan by KMP, 6M Sep 2026
R2024 | page 30 | line 2219 | NUMBER | - | [I3] cons note 30 RPT transactions: Repayment of Loan by KMP, 6M Sep 2025 | ZERO_STANDING
R2025 | page 30 | line 2222 | NUMBER | 0.58 | [I3] cons note 30 RPT transactions: Dividend paid, qtr Sep 2026
R2026 | page 30 | line 2222 | NUMBER | - | [I3] cons note 30 RPT transactions: Dividend paid, qtr Sep 2025 | ZERO_STANDING
R2027 | page 30 | line 2222 | NUMBER | 0.58 | [I3] cons note 30 RPT transactions: Dividend paid, 6M Sep 2026
R2028 | page 30 | line 2222 | NUMBER | 1.12 | [I3] cons note 30 RPT transactions: Dividend paid, 6M Sep 2025
R2029 | page 31 | line 2241 | NUMBER | 1,079.17 | [I3] cons note 30 RPT balances: Simply Vyapar Apps Private Limited, at 30 Sep 2026
R2030 | page 31 | line 2241 | NUMBER | 1,079.17 | [I3] cons note 30 RPT balances: Simply Vyapar Apps Private Limited, at 31 Mar 2026
R2031 | page 31 | line 2242 | NUMBER | 375.10 | [I3] cons note 30 RPT balances: Truckhall Private Limited, at 30 Sep 2026
R2032 | page 31 | line 2242 | NUMBER | 375.10 | [I3] cons note 30 RPT balances: Truckhall Private Limited, at 31 Mar 2026
R2033 | page 31 | line 2243 | NUMBER | 260.00 | [I3] cons note 30 RPT balances: Agillos E-Commerce Private Limited, at 30 Sep 2026
R2034 | page 31 | line 2243 | NUMBER | 260.00 | [I3] cons note 30 RPT balances: Agillos E-Commerce Private Limited, at 31 Mar 2026
R2035 | page 31 | line 2244 | NUMBER | 183.38 | [I3] cons note 30 RPT balances: Edgewise Technologies Private Limited, at 30 Sep 2026
R2036 | page 31 | line 2244 | NUMBER | 133.45 | [I3] cons note 30 RPT balances: Edgewise Technologies Private Limited, at 31 Mar 2026
R2037 | page 31 | line 2245 | NUMBER | - | [I3] cons note 30 RPT balances: IB Monotaro Private Limited (refer note 7 (iv, at 30 Sep 2026 | ZERO_STANDING
R2038 | page 31 | line 2245 | NUMBER | 1,179.13 | [I3] cons note 30 RPT balances: IB Monotaro Private Limited (refer note 7 (iv, at 31 Mar 2026
R2039 | page 31 | line 2246 | NUMBER | 137.50 | [I3] cons note 30 RPT balances: Adansa Solutions Private Limited, at 30 Sep 2026
R2040 | page 31 | line 2246 | NUMBER | 137.50 | [I3] cons note 30 RPT balances: Adansa Solutions Private Limited, at 31 Mar 2026
R2041 | page 31 | line 2247 | NUMBER | 818.00 | [I3] cons note 30 RPT balances: Mobisy Technologies Private Limited, at 30 Sep 2026
R2042 | page 31 | line 2247 | NUMBER | 818.00 | [I3] cons note 30 RPT balances: Mobisy Technologies Private Limited, at 31 Mar 2026
R2043 | page 31 | line 2248 | NUMBER | 2,189.00 | [I3] cons note 30 RPT balances: Fleetx Technologies Private Limited, at 30 Sep 2026
R2044 | page 31 | line 2248 | NUMBER | 1,539.12 | [I3] cons note 30 RPT balances: Fleetx Technologies Private Limited, at 31 Mar 2026
R2045 | page 31 | line 2251 | NUMBER | 172.47 | [I3] cons note 30 RPT balances: Agillos E-Commerce Private Limited, at 30 Sep 2026
R2046 | page 31 | line 2251 | NUMBER | - | [I3] cons note 30 RPT balances: Agillos E-Commerce Private Limited, at 31 Mar 2026 | ZERO_STANDING
R2047 | page 31 | line 2254 | NUMBER | - | [I3] cons note 30 RPT balances: Edgewise Technologies Private Limited, at 30 Sep 2026 | ZERO_STANDING
R2048 | page 31 | line 2254 | NUMBER | 50.00 | [I3] cons note 30 RPT balances: Edgewise Technologies Private Limited, at 31 Mar 2026
R2049 | page 31 | line 2257 | NUMBER | 0.88 | [I3] cons note 30 RPT balances: Simply Vyapar Apps Private Limited, at 30 Sep 2026
R2050 | page 31 | line 2257 | NUMBER | 0.22 | [I3] cons note 30 RPT balances: Simply Vyapar Apps Private Limited, at 31 Mar 2026
R2051 | page 31 | line 2260 | NUMBER | 0.90 | [I3] cons note 30 RPT balances: S R Dinodia & Co LLP, at 30 Sep 2026
R2052 | page 31 | line 2260 | NUMBER | 0.90 | [I3] cons note 30 RPT balances: S R Dinodia & Co LLP, at 31 Mar 2026
R2053 | page 31 | line 2261 | NUMBER | 0.33 | [I3] cons note 30 RPT balances: Mansa Enterprises Private Limited, at 30 Sep 2026
R2054 | page 31 | line 2261 | NUMBER | 0.11 | [I3] cons note 30 RPT balances: Mansa Enterprises Private Limited, at 31 Mar 2026
R2055 | page 31 | line 2264 | NUMBER | - | [I3] cons note 30 RPT balances: Simply Vyapar Apps Private Limited, at 30 Sep 2026 | ZERO_STANDING
R2056 | page 31 | line 2264 | NUMBER | 0.02 | [I3] cons note 30 RPT balances: Simply Vyapar Apps Private Limited, at 31 Mar 2026
R2057 | page 31 | line 2245 | NUMBER | - | [I3] cons note 30 RPT balances: IB Monotaro Private Limited, at 30 Sep 2026 | ZERO_STANDING
R2058 | page 31 | line 2245 | NUMBER | 1.28 | [I3] cons note 30 RPT balances: IB Monotaro Private Limited, at 31 Mar 2026
R2059 | page 58 | line 4093 | NUMBER | 47.81 | [I3] stand note 30 RPT list: Short-term employee benefits, qtr Sep 2026
R2060 | page 58 | line 4093 | NUMBER | 46.14 | [I3] stand note 30 RPT list: Short-term employee benefits, qtr Sep 2025
R2061 | page 58 | line 4093 | NUMBER | 97.13 | [I3] stand note 30 RPT list: Short-term employee benefits, 6M Sep 2026
R2062 | page 58 | line 4093 | NUMBER | 92.15 | [I3] stand note 30 RPT list: Short-term employee benefits, 6M Sep 2025
R2063 | page 58 | line 4094 | NUMBER | (0.02) | [I3] stand note 30 RPT list: Post- employment benefits, qtr Sep 2026
R2064 | page 58 | line 4094 | NUMBER | 0.02 | [I3] stand note 30 RPT list: Post- employment benefits, qtr Sep 2025
R2065 | page 58 | line 4094 | NUMBER | 0.14 | [I3] stand note 30 RPT list: Post- employment benefits, 6M Sep 2026
R2066 | page 58 | line 4094 | NUMBER | 0.87 | [I3] stand note 30 RPT list: Post- employment benefits, 6M Sep 2025
R2067 | page 58 | line 4095 | NUMBER | 0.05 | [I3] stand note 30 RPT list: Other long-term employee benefits, qtr Sep 2026
R2068 | page 58 | line 4095 | NUMBER | 0.65 | [I3] stand note 30 RPT list: Other long-term employee benefits, qtr Sep 2025
R2069 | page 58 | line 4095 | NUMBER | 1.29 | [I3] stand note 30 RPT list: Other long-term employee benefits, 6M Sep 2026
R2070 | page 58 | line 4095 | NUMBER | 1.83 | [I3] stand note 30 RPT list: Other long-term employee benefits, 6M Sep 2025
R2071 | page 58 | line 4096 | NUMBER | 3.31 | [I3] stand note 30 RPT list: Employee share based payment, qtr Sep 2026
R2072 | page 58 | line 4096 | NUMBER | 5.03 | [I3] stand note 30 RPT list: Employee share based payment, qtr Sep 2025
R2073 | page 58 | line 4096 | NUMBER | 7.10 | [I3] stand note 30 RPT list: Employee share based payment, 6M Sep 2026
R2074 | page 58 | line 4096 | NUMBER | 7.10 | [I3] stand note 30 RPT list: Employee share based payment, 6M Sep 2025
R2075 | page 58 | line 4096 | NUMBER | 51.15 | [I3] stand note 30 RPT list: Employee share based payment, qtr Sep 2026
R2076 | page 58 | line 4096 | NUMBER | 51.84 | [I3] stand note 30 RPT list: Employee share based payment, qtr Sep 2025
R2077 | page 58 | line 4096 | NUMBER | 105.66 | [I3] stand note 30 RPT list: Employee share based payment, 6M Sep 2026
R2078 | page 58 | line 4096 | NUMBER | 101.95 | [I3] stand note 30 RPT list: Employee share based payment, 6M Sep 2025
R2079 | page 59 | line 4111 | NUMBER | 1.72 | [I3] stand note 30 RPT transactions: Mansa Enterprises Private Limited, qtr Sep 2026
R2080 | page 59 | line 4111 | NUMBER | 1.58 | [I3] stand note 30 RPT transactions: Mansa Enterprises Private Limited, qtr Sep 2025
R2081 | page 59 | line 4111 | NUMBER | 3.42 | [I3] stand note 30 RPT transactions: Mansa Enterprises Private Limited, 6M Sep 2026
R2082 | page 59 | line 4111 | NUMBER | 3.19 | [I3] stand note 30 RPT transactions: Mansa Enterprises Private Limited, 6M Sep 2025
R2083 | page 59 | line 4114 | NUMBER | - | [I3] stand note 30 RPT transactions: S R Dinodia & Co LLP, qtr Sep 2026 | ZERO_STANDING
R2084 | page 59 | line 4114 | NUMBER | 0.74 | [I3] stand note 30 RPT transactions: S R Dinodia & Co LLP, qtr Sep 2025
R2085 | page 59 | line 4114 | NUMBER | 0.13 | [I3] stand note 30 RPT transactions: S R Dinodia & Co LLP, 6M Sep 2026
R2086 | page 59 | line 4114 | NUMBER | 1.08 | [I3] stand note 30 RPT transactions: S R Dinodia & Co LLP, 6M Sep 2025
R2087 | page 59 | line 4119 | NUMBER | - | [I3] stand note 30 RPT transactions: Key management personnel, qtr Sep 2026 | ZERO_STANDING
R2088 | page 59 | line 4119 | NUMBER | 0.75 | [I3] stand note 30 RPT transactions: Key management personnel, qtr Sep 2025
R2089 | page 59 | line 4119 | NUMBER | 0.83 | [I3] stand note 30 RPT transactions: Key management personnel, 6M Sep 2026
R2090 | page 59 | line 4119 | NUMBER | 1.50 | [I3] stand note 30 RPT transactions: Key management personnel, 6M Sep 2025
R2091 | page 59 | line 4122 | NUMBER | 1,694.77 | [I3] stand note 30 RPT transactions: Key management personnel, qtr Sep 2026
R2092 | page 59 | line 4122 | NUMBER | - | [I3] stand note 30 RPT transactions: Key management personnel, qtr Sep 2025 | ZERO_STANDING
R2093 | page 59 | line 4122 | NUMBER | 1,694.77 | [I3] stand note 30 RPT transactions: Key management personnel, 6M Sep 2026
R2094 | page 59 | line 4122 | NUMBER | 1,413.43 | [I3] stand note 30 RPT transactions: Key management personnel, 6M Sep 2025
R2095 | page 59 | line 4123 | NUMBER | 66.36 | [I3] stand note 30 RPT transactions: Relatives of Key Management Personnel, qtr Sep 2026
R2096 | page 59 | line 4123 | NUMBER | - | [I3] stand note 30 RPT transactions: Relatives of Key Management Personnel, qtr Sep 2025 | ZERO_STANDING
R2097 | page 59 | line 4123 | NUMBER | 66.36 | [I3] stand note 30 RPT transactions: Relatives of Key Management Personnel, 6M Sep 2026
R2098 | page 59 | line 4123 | NUMBER | 55.70 | [I3] stand note 30 RPT transactions: Relatives of Key Management Personnel, 6M Sep 2025
R2099 | page 59 | line 4124 | NUMBER | 7.09 | [I3] stand note 30 RPT transactions: Entities where Key Management Personnel exerc, qtr Sep 2026
R2100 | page 59 | line 4124 | NUMBER | - | [I3] stand note 30 RPT transactions: Entities where Key Management Personnel exerc, qtr Sep 2025 | ZERO_STANDING
R2101 | page 59 | line 4124 | NUMBER | 7.09 | [I3] stand note 30 RPT transactions: Entities where Key Management Personnel exerc, 6M Sep 2026
R2102 | page 59 | line 4124 | NUMBER | 6.49 | [I3] stand note 30 RPT transactions: Entities where Key Management Personnel exerc, 6M Sep 2025
R2103 | page 59 | line 4128 | NUMBER | - | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, qtr Sep 2026 | ZERO_STANDING
R2104 | page 59 | line 4128 | NUMBER | 25.00 | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, qtr Sep 2025
R2105 | page 59 | line 4128 | NUMBER | - | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, 6M Sep 2026 | ZERO_STANDING
R2106 | page 59 | line 4128 | NUMBER | 25.00 | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, 6M Sep 2025
R2107 | page 59 | line 4129 | NUMBER | 190.00 | [I3] stand note 30 RPT transactions: Tradezeal Online Private Limited, qtr Sep 2026
R2108 | page 59 | line 4129 | NUMBER | 60.00 | [I3] stand note 30 RPT transactions: Tradezeal Online Private Limited, qtr Sep 2025
R2109 | page 59 | line 4129 | NUMBER | 190.00 | [I3] stand note 30 RPT transactions: Tradezeal Online Private Limited, 6M Sep 2026
R2110 | page 59 | line 4129 | NUMBER | 60.00 | [I3] stand note 30 RPT transactions: Tradezeal Online Private Limited, 6M Sep 2025
R2111 | page 59 | line 4130 | NUMBER | - | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, qtr Sep 2026 | ZERO_STANDING
R2112 | page 59 | line 4130 | NUMBER | - | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, qtr Sep 2025 | ZERO_STANDING
R2113 | page 59 | line 4130 | NUMBER | 59.97 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, 6M Sep 2026
R2114 | page 59 | line 4130 | NUMBER | - | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, 6M Sep 2025 | ZERO_STANDING
R2115 | page 59 | line 4131 | NUMBER | 120.50 | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, qtr Sep 2026
R2116 | page 59 | line 4131 | NUMBER | - | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, qtr Sep 2025 | ZERO_STANDING
R2117 | page 59 | line 4131 | NUMBER | 120.50 | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, 6M Sep 2026
R2118 | page 59 | line 4131 | NUMBER | - | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, 6M Sep 2025 | ZERO_STANDING
R2119 | page 59 | line 4134 | NUMBER | 649.88 | [I3] stand note 30 RPT transactions: Fleetx Technologies Private Limited, qtr Sep 2026
R2120 | page 59 | line 4134 | NUMBER | - | [I3] stand note 30 RPT transactions: Fleetx Technologies Private Limited, qtr Sep 2025 | ZERO_STANDING
R2121 | page 59 | line 4134 | NUMBER | 649.88 | [I3] stand note 30 RPT transactions: Fleetx Technologies Private Limited, 6M Sep 2026
R2122 | page 59 | line 4134 | NUMBER | 410.00 | [I3] stand note 30 RPT transactions: Fleetx Technologies Private Limited, 6M Sep 2025
R2123 | page 59 | line 4137 | NUMBER | 4.15 | [I3] stand note 30 RPT transactions: Relatives of Key Management Personnel, qtr Sep 2026
R2124 | page 59 | line 4137 | NUMBER | 1.69 | [I3] stand note 30 RPT transactions: Relatives of Key Management Personnel, qtr Sep 2025
R2125 | page 59 | line 4137 | NUMBER | 8.42 | [I3] stand note 30 RPT transactions: Relatives of Key Management Personnel, 6M Sep 2026
R2126 | page 59 | line 4137 | NUMBER | 3.42 | [I3] stand note 30 RPT transactions: Relatives of Key Management Personnel, 6M Sep 2025
R2127 | page 59 | line 4139 | NUMBER | 1.10 | [I3] stand note 30 RPT transactions: Director's sitting fees, qtr Sep 2026
R2128 | page 59 | line 4139 | NUMBER | 1.80 | [I3] stand note 30 RPT transactions: Director's sitting fees, qtr Sep 2025
R2129 | page 59 | line 4139 | NUMBER | 3.40 | [I3] stand note 30 RPT transactions: Director's sitting fees, 6M Sep 2026
R2130 | page 59 | line 4139 | NUMBER | 3.50 | [I3] stand note 30 RPT transactions: Director's sitting fees, 6M Sep 2025
R2131 | page 59 | line 4141 | NUMBER | 1.50 | [I3] stand note 30 RPT transactions: Loans to KMP, qtr Sep 2026
R2132 | page 59 | line 4141 | NUMBER | - | [I3] stand note 30 RPT transactions: Loans to KMP, qtr Sep 2025 | ZERO_STANDING
R2133 | page 59 | line 4141 | NUMBER | 1.50 | [I3] stand note 30 RPT transactions: Loans to KMP, 6M Sep 2026
R2134 | page 59 | line 4141 | NUMBER | - | [I3] stand note 30 RPT transactions: Loans to KMP, 6M Sep 2025 | ZERO_STANDING
R2135 | page 59 | line 4144 | NUMBER | 1.71 | [I3] stand note 30 RPT transactions: Simply Vyapar Apps Private Limited, qtr Sep 2026
R2136 | page 59 | line 4144 | NUMBER | 1.56 | [I3] stand note 30 RPT transactions: Simply Vyapar Apps Private Limited, qtr Sep 2025
R2137 | page 59 | line 4144 | NUMBER | 3.22 | [I3] stand note 30 RPT transactions: Simply Vyapar Apps Private Limited, 6M Sep 2026
R2138 | page 59 | line 4144 | NUMBER | 2.86 | [I3] stand note 30 RPT transactions: Simply Vyapar Apps Private Limited, 6M Sep 2025
R2139 | page 59 | line 4145 | NUMBER | - | [I3] stand note 30 RPT transactions: IB Monotaro Private Limited, qtr Sep 2026 | ZERO_STANDING
R2140 | page 59 | line 4145 | NUMBER | 0.50 | [I3] stand note 30 RPT transactions: IB Monotaro Private Limited, qtr Sep 2025
R2141 | page 59 | line 4145 | NUMBER | 0.28 | [I3] stand note 30 RPT transactions: IB Monotaro Private Limited, 6M Sep 2026
R2142 | page 59 | line 4145 | NUMBER | 0.99 | [I3] stand note 30 RPT transactions: IB Monotaro Private Limited, 6M Sep 2025
R2143 | page 59 | line 4146 | NUMBER | 2.62 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, qtr Sep 2026
R2144 | page 59 | line 4146 | NUMBER | 0.15 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, qtr Sep 2025
R2145 | page 59 | line 4146 | NUMBER | 3.01 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, 6M Sep 2026
R2146 | page 59 | line 4146 | NUMBER | 0.26 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, 6M Sep 2025
R2147 | page 59 | line 4147 | NUMBER | 0.01 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, qtr Sep 2026
R2148 | page 59 | line 4147 | NUMBER | 0.01 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, qtr Sep 2025
R2149 | page 59 | line 4147 | NUMBER | 0.02 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, 6M Sep 2026
R2150 | page 59 | line 4147 | NUMBER | 0.05 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, 6M Sep 2025
R2151 | page 59 | line 4150 | NUMBER | 0.94 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, qtr Sep 2026
R2152 | page 59 | line 4150 | NUMBER | 1.41 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, qtr Sep 2025
R2153 | page 59 | line 4150 | NUMBER | 2.71 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, 6M Sep 2026
R2154 | page 59 | line 4150 | NUMBER | 2.83 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, 6M Sep 2025
R2155 | page 59 | line 4151 | NUMBER | 0.09 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, qtr Sep 2026
R2156 | page 59 | line 4151 | NUMBER | 0.09 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, qtr Sep 2025
R2157 | page 59 | line 4151 | NUMBER | 0.18 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, 6M Sep 2026
R2158 | page 59 | line 4151 | NUMBER | 0.19 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, 6M Sep 2025
R2159 | page 59 | line 4152 | NUMBER | 0.56 | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, qtr Sep 2026
R2160 | page 59 | line 4152 | NUMBER | 0.45 | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, qtr Sep 2025
R2161 | page 59 | line 4152 | NUMBER | 1.02 | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, 6M Sep 2026
R2162 | page 59 | line 4152 | NUMBER | 0.81 | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, 6M Sep 2025
R2163 | page 59 | line 4153 | NUMBER | 0.01 | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, qtr Sep 2026
R2164 | page 59 | line 4153 | NUMBER | - | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, qtr Sep 2025 | ZERO_STANDING
R2165 | page 59 | line 4153 | NUMBER | 0.01 | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, 6M Sep 2026
R2166 | page 59 | line 4153 | NUMBER | - | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, 6M Sep 2025 | ZERO_STANDING
R2167 | page 59 | line 4160 | NUMBER | 2.62 | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, qtr Sep 2026
R2168 | page 59 | line 4160 | NUMBER | - | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, qtr Sep 2025 | ZERO_STANDING
R2169 | page 59 | line 4160 | NUMBER | 4.16 | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, 6M Sep 2026
R2170 | page 59 | line 4160 | NUMBER | - | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, 6M Sep 2025 | ZERO_STANDING
R2171 | page 59 | line 4162 | NUMBER | 1.50 | [I3] stand note 30 RPT transactions: Repayment of Loan by KMP, qtr Sep 2026
R2172 | page 59 | line 4162 | NUMBER | - | [I3] stand note 30 RPT transactions: Repayment of Loan by KMP, qtr Sep 2025 | ZERO_STANDING
R2173 | page 59 | line 4162 | NUMBER | 1.50 | [I3] stand note 30 RPT transactions: Repayment of Loan by KMP, 6M Sep 2026
R2174 | page 59 | line 4162 | NUMBER | - | [I3] stand note 30 RPT transactions: Repayment of Loan by KMP, 6M Sep 2025 | ZERO_STANDING
R2175 | page 59 | line 4165 | NUMBER | - | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, qtr Sep 2026 | ZERO_STANDING
R2176 | page 59 | line 4165 | NUMBER | 0.05 | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, qtr Sep 2025
R2177 | page 59 | line 4165 | NUMBER | - | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, 6M Sep 2026 | ZERO_STANDING
R2178 | page 59 | line 4165 | NUMBER | 0.21 | [I3] stand note 30 RPT transactions: IIL Digital Private Limited, 6M Sep 2025
R2179 | page 59 | line 4168 | NUMBER | 2.86 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, qtr Sep 2026
R2180 | page 59 | line 4168 | NUMBER | 2.12 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, qtr Sep 2025
R2181 | page 59 | line 4168 | NUMBER | 5.63 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, 6M Sep 2026
R2182 | page 59 | line 4168 | NUMBER | 5.06 | [I3] stand note 30 RPT transactions: Busy Infotech Private Limited (Formerly known, 6M Sep 2025
R2183 | page 59 | line 4169 | NUMBER | 0.26 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, qtr Sep 2026
R2184 | page 59 | line 4169 | NUMBER | 2.22 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, qtr Sep 2025
R2185 | page 59 | line 4169 | NUMBER | 2.08 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, 6M Sep 2026
R2186 | page 59 | line 4169 | NUMBER | 3.90 | [I3] stand note 30 RPT transactions: Livekeeping Technologies Private Limited, 6M Sep 2025
R2187 | page 59 | line 4172 | NUMBER | 2.11 | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, qtr Sep 2026
R2188 | page 59 | line 4172 | NUMBER | - | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, qtr Sep 2025 | ZERO_STANDING
R2189 | page 59 | line 4172 | NUMBER | 2.11 | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, 6M Sep 2026
R2190 | page 59 | line 4172 | NUMBER | - | [I3] stand note 30 RPT transactions: IndiaMart Finance Limited, 6M Sep 2025 | ZERO_STANDING
R2191 | page 59 | line 4121 | NUMBER | 0.58 | [I3] stand note 30 RPT transactions: Dividend paid, qtr Sep 2026
R2192 | page 59 | line 4121 | NUMBER | - | [I3] stand note 30 RPT transactions: Dividend paid, qtr Sep 2025 | ZERO_STANDING
R2193 | page 59 | line 4121 | NUMBER | 0.58 | [I3] stand note 30 RPT transactions: Dividend paid, 6M Sep 2026
R2194 | page 59 | line 4121 | NUMBER | 1.12 | [I3] stand note 30 RPT transactions: Dividend paid, 6M Sep 2025
R2195 | page 60 | line 4190 | NUMBER | - | [I3] stand note 30 RPT balances: Tradezeal Online Private Limited, at 30 Sep 2026 | ZERO_STANDING
R2196 | page 60 | line 4190 | NUMBER | 128.06 | [I3] stand note 30 RPT balances: Tradezeal Online Private Limited, at 31 Mar 2026
R2197 | page 60 | line 4191 | NUMBER | 55.50 | [I3] stand note 30 RPT balances: Pay With Indiamart Private Limited, at 30 Sep 2026
R2198 | page 60 | line 4191 | NUMBER | 55.50 | [I3] stand note 30 RPT balances: Pay With Indiamart Private Limited, at 31 Mar 2026
R2199 | page 60 | line 4196 | NUMBER | 5,092.81 | [I3] stand note 30 RPT balances: Busy Infotech Private Limited (Formerly Known, at 30 Sep 2026
R2200 | page 60 | line 4196 | NUMBER | 5,087.18 | [I3] stand note 30 RPT balances: Busy Infotech Private Limited (Formerly Known, at 31 Mar 2026
R2201 | page 60 | line 4197 | NUMBER | 1,311.66 | [I3] stand note 30 RPT balances: Tradezeal Online Private Limited, at 30 Sep 2026
R2202 | page 60 | line 4197 | NUMBER | 993.60 | [I3] stand note 30 RPT balances: Tradezeal Online Private Limited, at 31 Mar 2026
R2203 | page 60 | line 4198 | NUMBER | 1.00 | [I3] stand note 30 RPT balances: Pay With Indiamart Private Limited, at 30 Sep 2026
R2204 | page 60 | line 4198 | NUMBER | 1.00 | [I3] stand note 30 RPT balances: Pay With Indiamart Private Limited, at 31 Mar 2026
R2205 | page 60 | line 4199 | NUMBER | 1,025.84 | [I3] stand note 30 RPT balances: Livekeeping Technologies Private Limited ^*, at 30 Sep 2026
R2206 | page 60 | line 4199 | NUMBER | 963.79 | [I3] stand note 30 RPT balances: Livekeeping Technologies Private Limited ^*, at 31 Mar 2026
R2207 | page 60 | line 4200 | NUMBER | 93.50 | [I3] stand note 30 RPT balances: IIL Digital Private Limited, at 30 Sep 2026
R2208 | page 60 | line 4200 | NUMBER | 93.50 | [I3] stand note 30 RPT balances: IIL Digital Private Limited, at 31 Mar 2026
R2209 | page 60 | line 4201 | NUMBER | 120.50 | [I3] stand note 30 RPT balances: IndiaMart Finance Limited (incorporated on 04, at 30 Sep 2026
R2210 | page 60 | line 4201 | NUMBER | - | [I3] stand note 30 RPT balances: IndiaMart Finance Limited (incorporated on 04, at 31 Mar 2026 | ZERO_STANDING
R2211 | page 60 | line 4204 | NUMBER | 1,079.17 | [I3] stand note 30 RPT balances: Simply Vyapar Apps Private Limited, at 30 Sep 2026
R2212 | page 60 | line 4204 | NUMBER | 1,079.17 | [I3] stand note 30 RPT balances: Simply Vyapar Apps Private Limited, at 31 Mar 2026
R2213 | page 60 | line 4205 | NUMBER | - | [I3] stand note 30 RPT balances: IB Monotaro Private Limited(refer note 7 (vii, at 30 Sep 2026 | ZERO_STANDING
R2214 | page 60 | line 4205 | NUMBER | 1,179.13 | [I3] stand note 30 RPT balances: IB Monotaro Private Limited(refer note 7 (vii, at 31 Mar 2026
R2215 | page 60 | line 4206 | NUMBER | 818.00 | [I3] stand note 30 RPT balances: Mobisy Technologies Private Limited, at 30 Sep 2026
R2216 | page 60 | line 4206 | NUMBER | 818.00 | [I3] stand note 30 RPT balances: Mobisy Technologies Private Limited, at 31 Mar 2026
R2217 | page 60 | line 4207 | NUMBER | 2,189.00 | [I3] stand note 30 RPT balances: Fleetx Technologies Private Limited, at 30 Sep 2026
R2218 | page 60 | line 4207 | NUMBER | 1,539.12 | [I3] stand note 30 RPT balances: Fleetx Technologies Private Limited, at 31 Mar 2026
R2219 | page 60 | line 4210 | NUMBER | 0.88 | [I3] stand note 30 RPT balances: Simply Vyapar Apps Private Limited, at 30 Sep 2026
R2220 | page 60 | line 4210 | NUMBER | 0.22 | [I3] stand note 30 RPT balances: Simply Vyapar Apps Private Limited, at 31 Mar 2026
R2221 | page 60 | line 4211 | NUMBER | 2.85 | [I3] stand note 30 RPT balances: Livekeeping Technologies Private Limited, at 30 Sep 2026
R2222 | page 60 | line 4211 | NUMBER | 0.02 | [I3] stand note 30 RPT balances: Livekeeping Technologies Private Limited, at 31 Mar 2026
R2223 | page 60 | line 4214 | NUMBER | 0.03 | [I3] stand note 30 RPT balances: Busy Infotech Private Limited ( Formerly Know, at 30 Sep 2026
R2224 | page 60 | line 4214 | NUMBER | 0.03 | [I3] stand note 30 RPT balances: Busy Infotech Private Limited ( Formerly Know, at 31 Mar 2026
R2225 | page 60 | line 4215 | NUMBER | 9.30 | [I3] stand note 30 RPT balances: Livekeeping Technologies Private Limited, at 30 Sep 2026
R2226 | page 60 | line 4215 | NUMBER | - | [I3] stand note 30 RPT balances: Livekeeping Technologies Private Limited, at 31 Mar 2026 | ZERO_STANDING
R2227 | page 60 | line 4216 | NUMBER | 0.41 | [I3] stand note 30 RPT balances: IIL Digital Private Limited, at 30 Sep 2026
R2228 | page 60 | line 4216 | NUMBER | 0.07 | [I3] stand note 30 RPT balances: IIL Digital Private Limited, at 31 Mar 2026
R2229 | page 60 | line 4201 | NUMBER | 2.12 | [I3] stand note 30 RPT balances: IndiaMart Finance Limited, at 30 Sep 2026
R2230 | page 60 | line 4201 | NUMBER | - | [I3] stand note 30 RPT balances: IndiaMart Finance Limited, at 31 Mar 2026 | ZERO_STANDING
R2231 | page 60 | line 4220 | NUMBER | 0.90 | [I3] stand note 30 RPT balances: S R Dinodia & Co LLP, at 30 Sep 2026
R2232 | page 60 | line 4220 | NUMBER | 0.90 | [I3] stand note 30 RPT balances: S R Dinodia & Co LLP, at 31 Mar 2026
R2233 | page 60 | line 4221 | NUMBER | 0.33 | [I3] stand note 30 RPT balances: Mansa Enterprises Private Limited, at 30 Sep 2026
R2234 | page 60 | line 4221 | NUMBER | 0.11 | [I3] stand note 30 RPT balances: Mansa Enterprises Private Limited, at 31 Mar 2026
R2235 | page 60 | line 4222 | NUMBER | 0.95 | [I3] stand note 30 RPT balances: IIL Digital Private Limited, at 30 Sep 2026
R2236 | page 60 | line 4222 | NUMBER | - | [I3] stand note 30 RPT balances: IIL Digital Private Limited, at 31 Mar 2026 | ZERO_STANDING
R2237 | page 60 | line 4226 | NUMBER | 0.05 | [I3] stand note 30 RPT balances: Busy Infotech Private Limited(Formerly Known , at 30 Sep 2026
R2238 | page 60 | line 4226 | NUMBER | 0.07 | [I3] stand note 30 RPT balances: Busy Infotech Private Limited(Formerly Known , at 31 Mar 2026
R2239 | page 60 | line 4205 | NUMBER | - | [I3] stand note 30 RPT balances: IB Monotaro Private Limited, at 30 Sep 2026 | ZERO_STANDING
R2240 | page 60 | line 4205 | NUMBER | 1.28 | [I3] stand note 30 RPT balances: IB Monotaro Private Limited, at 31 Mar 2026
R2241 | page 60 | line 4228 | NUMBER | - | [I3] stand note 30 RPT balances: Simply Vyapar Apps Private Limited, at 30 Sep 2026 | ZERO_STANDING
R2242 | page 60 | line 4228 | NUMBER | 0.02 | [I3] stand note 30 RPT balances: Simply Vyapar Apps Private Limited, at 31 Mar 2026
R2243 | page 20 | line 1497 | NUMBER | 139.43 | [I4] cons note 9 other assets: Prepaid expenses, at 30 Sep 2026
R2244 | page 20 | line 1497 | NUMBER | 0.16 | [I4] cons note 9 other assets: Prepaid expenses, at 31 Mar 2026
R2245 | page 20 | line 1498 | NUMBER | 35.98 | [I4] cons note 9 other assets: Indirect taxes recoverable, at 30 Sep 2026
R2246 | page 20 | line 1498 | NUMBER | 26.13 | [I4] cons note 9 other assets: Indirect taxes recoverable, at 31 Mar 2026
R2247 | page 20 | line 1499 | NUMBER | - | [I4] cons note 9 other assets: Capital advance, at 30 Sep 2026 | ZERO_STANDING
R2248 | page 20 | line 1499 | NUMBER | 1.40 | [I4] cons note 9 other assets: Capital advance, at 31 Mar 2026
R2249 | page 20 | line 1500 | NUMBER | 175.41 | [I4] cons note 9 other assets: Total, at 30 Sep 2026
R2250 | page 20 | line 1500 | NUMBER | 27.69 | [I4] cons note 9 other assets: Total, at 31 Mar 2026
R2251 | page 20 | line 1503 | NUMBER | 15.68 | [I4] cons note 9 other assets: Advances recoverable, at 30 Sep 2026
R2252 | page 20 | line 1503 | NUMBER | 13.69 | [I4] cons note 9 other assets: Advances recoverable, at 31 Mar 2026
R2253 | page 20 | line 1504 | NUMBER | 35.60 | [I4] cons note 9 other assets: Indirect taxes recoverable, at 30 Sep 2026
R2254 | page 20 | line 1504 | NUMBER | 35.60 | [I4] cons note 9 other assets: Indirect taxes recoverable, at 31 Mar 2026
R2255 | page 20 | line 1505 | NUMBER | 311.03 | [I4] cons note 9 other assets: Prepaid expenses, at 30 Sep 2026
R2256 | page 20 | line 1505 | NUMBER | 356.71 | [I4] cons note 9 other assets: Prepaid expenses, at 31 Mar 2026
R2257 | page 20 | line 1506 | NUMBER | 362.31 | [I4] cons note 9 other assets: Total, at 30 Sep 2026
R2258 | page 20 | line 1506 | NUMBER | 406.00 | [I4] cons note 9 other assets: Total, at 31 Mar 2026
R2259 | page 49 | line 3542 | NUMBER | - | [I4] stand note 11 other assets: Capital advance, at 30 Sep 2026 | ZERO_STANDING
R2260 | page 49 | line 3542 | NUMBER | 1.40 | [I4] stand note 11 other assets: Capital advance, at 31 Mar 2026
R2261 | page 49 | line 3543 | NUMBER | 22.75 | [I4] stand note 11 other assets: Indirect taxes recoverable (Refer Note 32 (a), at 30 Sep 2026
R2262 | page 49 | line 3543 | NUMBER | 12.56 | [I4] stand note 11 other assets: Indirect taxes recoverable (Refer Note 32 (a), at 31 Mar 2026
R2263 | page 49 | line 3544 | NUMBER | 22.75 | [I4] stand note 11 other assets: Total, at 30 Sep 2026
R2264 | page 49 | line 3544 | NUMBER | 13.96 | [I4] stand note 11 other assets: Total, at 31 Mar 2026
R2265 | page 49 | line 3547 | NUMBER | 9.79 | [I4] stand note 11 other assets: Advances recoverable, at 30 Sep 2026
R2266 | page 49 | line 3547 | NUMBER | 8.44 | [I4] stand note 11 other assets: Advances recoverable, at 31 Mar 2026
R2267 | page 49 | line 3543 | NUMBER | 7.09 | [I4] stand note 11 other assets: Indirect taxes recoverable, at 30 Sep 2026
R2268 | page 49 | line 3543 | NUMBER | 9.47 | [I4] stand note 11 other assets: Indirect taxes recoverable, at 31 Mar 2026
R2269 | page 49 | line 3549 | NUMBER | 38.29 | [I4] stand note 11 other assets: Prepaid expenses, at 30 Sep 2026
R2270 | page 49 | line 3549 | NUMBER | 48.19 | [I4] stand note 11 other assets: Prepaid expenses, at 31 Mar 2026
R2271 | page 49 | line 3550 | NUMBER | 55.17 | [I4] stand note 11 other assets: Total, at 30 Sep 2026
R2272 | page 49 | line 3550 | NUMBER | 66.10 | [I4] stand note 11 other assets: Total, at 31 Mar 2026

## ENTITY TABLE (358 rows)

R2273 | page 2 | line 62 | ENTITY | B S R & Co. LLP, Chartered Accountants (statutory auditor, Gurugram office) | [I5] consolidated report auditor
R2274 | page 2 | line 71 | ENTITY | IndiaMART InterMESH Limited ("Holding Company") | [I5] addressee of consolidated report
R2275 | page 5 | line 237 | ENTITY | Firm's Registration No. 101248W/W-100022 | [I5] consolidated report signature block
R2276 | page 5 | line 241 | ENTITY | David Jones, Partner, Membership No. 098113 | [I5] consolidated report signatory
R2277 | page 5 | line 250 | ENTITY | UDIN: 26098113SRBTOZ2829 | [I5] consolidated report UDIN
R2278 | page 33 | line 2355 | ENTITY | B S R & Co. LLP, Chartered Accountants (statutory auditor, Gurugram office) | [I5] standalone report auditor
R2279 | page 33 | line 2364 | ENTITY | IndiaMART InterMESH Limited ("the Company") | [I5] addressee of standalone report
R2280 | page 35 | line 2476 | ENTITY | Firm's Registration No. 101248W/W-100022 | [I5] standalone report signature block
R2281 | page 35 | line 2478 | ENTITY | David Jones, Partner, Membership No. 098113 | [I5] standalone report signatory
R2282 | page 35 | line 2482 | ENTITY | UDIN: 26098113AYOEGP5632 | [I5] standalone report UDIN
R2283 | page 4 | line 203 | ENTITY | other auditors (unnamed) of five subsidiaries | [I5] consolidated other matter (a)
R2284 | page 4 | line 218 | ENTITY | seven associates, financial information not audited by any auditor (unnamed) | [I5] consolidated other matter (b)
R2285 | page 4 | line 221 | ENTITY | one associate (period 1 April 2026 to 29 May 2026), not audited by any auditor (unnamed) | [I5] consolidated other matter (b)
R2286 | page 17 | line 1095 | ENTITY | Simply Vyapar Apps Private Limited | [I2] named entity, cons note 7 associates
R2287 | page 17 | line 1111 | ENTITY | Mobisy Technologies Private Limited | [I2] named entity, cons note 7 associates
R2288 | page 17 | line 1126 | ENTITY | Truckhall Private Limited | [I2] named entity, cons note 7 associates
R2289 | page 17 | line 1135 | ENTITY | Agillos E-Commerce Private Limited | [I2] named entity, cons note 7 associates
R2290 | page 17 | line 1141 | ENTITY | Edgewise Technologies Private Limited | [I2] named entity, cons note 7 associates
R2291 | page 17 | line 1153 | ENTITY | Adansa Solutions Private Limited | [I2] named entity, cons note 7 associates
R2292 | page 17 | line 1158 | ENTITY | Fleetx Technologies Private Limited | [I2] named entity, cons note 7 associates
R2293 | page 18 | line 1213 | ENTITY | Instant Procurement Services Private Limited | [I2] named entity, cons note 8a non-current inv
R2294 | page 18 | line 1218 | ENTITY | Legistify Services Private Limited | [I2] named entity, cons note 8a non-current inv
R2295 | page 18 | line 1226 | ENTITY | Mynd Solutions Private Limited | [I2] named entity, cons note 8a non-current inv
R2296 | page 18 | line 1234 | ENTITY | Zimyo Consulting Private Limited | [I2] named entity, cons note 8a non-current inv
R2297 | page 18 | line 1240 | ENTITY | Baldor Technologies Private Limited | [I2] named entity, cons note 8a non-current inv
R2298 | page 18 | line 1268 | ENTITY | Edgewise Technologies Private Limited | [I2] named entity, cons note 8a non-current inv
R2299 | page 18 | line 1272 | ENTITY | Private Ltd | [I2] named entity, cons note 8a non-current inv
R2300 | page 19 | line 1299 | ENTITY | Aditya Birla Sun Life Arbitrage Fund | [I2] holding listed, cons note 8b current inv
R2301 | page 19 | line 1300 | ENTITY | Aditya Birla Sun Life Corporate Bond Fund | [I2] holding listed, cons note 8b current inv
R2302 | page 19 | line 1301 | ENTITY | Aditya Birla Sun Life Nifty SDL Apr 2027 Index Fund | [I2] holding listed, cons note 8b current inv
R2303 | page 19 | line 1302 | ENTITY | Axis Corporate Bond Fund | [I2] holding listed, cons note 8b current inv
R2304 | page 19 | line 1303 | ENTITY | Axis Liquid Fund | [I2] holding listed, cons note 8b current inv
R2305 | page 19 | line 1304 | ENTITY | Axis Money Market Fund | [I2] holding listed, cons note 8b current inv
R2306 | page 19 | line 1305 | ENTITY | Bajaj Finserve Liquid Fund | [I2] holding listed, cons note 8b current inv
R2307 | page 19 | line 1306 | ENTITY | BHARAT Bond ETF - April 2030 | [I2] holding listed, cons note 8b current inv
R2308 | page 19 | line 1307 | ENTITY | Edelweiss CRISIL IBX 50:50 Gilt Plus SDL April 2037 Index Fund | [I2] holding listed, cons note 8b current inv
R2309 | page 19 | line 1308 | ENTITY | Edelweiss NIFTY PSU Bond Plus SDL Apr 2026 50:50 Index Fund | [I2] holding listed, cons note 8b current inv
R2310 | page 19 | line 1309 | ENTITY | Edelweiss Arbitrage Fund | [I2] holding listed, cons note 8b current inv
R2311 | page 19 | line 1310 | ENTITY | Edelweiss Nifty Midcap150 Momentum 50 Index Fund | [I2] holding listed, cons note 8b current inv
R2312 | page 19 | line 1311 | ENTITY | HDFC Ultra Short to Short Term Fund | [I2] holding listed, cons note 8b current inv
R2313 | page 19 | line 1312 | ENTITY | HDFC Corporate Bond Fund | [I2] holding listed, cons note 8b current inv
R2314 | page 19 | line 1313 | ENTITY | ICICI Prudential Ultra Short to Short Term Fund | [I2] holding listed, cons note 8b current inv
R2315 | page 19 | line 1314 | ENTITY | ICICI Prudential Money Market Fund | [I2] holding listed, cons note 8b current inv
R2316 | page 19 | line 1315 | ENTITY | ICICI Prudential Liquid Fund | [I2] holding listed, cons note 8b current inv
R2317 | page 19 | line 1316 | ENTITY | ICICI Prudential Corporate Bond Fund | [I2] holding listed, cons note 8b current inv
R2318 | page 19 | line 1317 | ENTITY | ICICI Prudential Nifty SDL Dec 2028 Index Fund | [I2] holding listed, cons note 8b current inv
R2319 | page 19 | line 1318 | ENTITY | ICICI Prudential Nifty Alpha Low Volatility 30 ETF | [I2] holding listed, cons note 8b current inv
R2320 | page 19 | line 1319 | ENTITY | ICICI Prudential Nifty 200 Quality 30 ETF | [I2] holding listed, cons note 8b current inv
R2321 | page 19 | line 1320 | ENTITY | Invesco India Arbitrage Fund | [I2] holding listed, cons note 8b current inv
R2322 | page 19 | line 1321 | ENTITY | Kotak Corporate Bond Fund | [I2] holding listed, cons note 8b current inv
R2323 | page 19 | line 1322 | ENTITY | Kotak Arbitrage Fund | [I2] holding listed, cons note 8b current inv
R2324 | page 19 | line 1323 | ENTITY | Kotak Nifty SDL Apr 2027 Top 12 Equal Weight Index Fund | [I2] holding listed, cons note 8b current inv
R2325 | page 19 | line 1324 | ENTITY | Kotak Nifty SDL Apr 2032 Top 12 Equal Weight Index Fund | [I2] holding listed, cons note 8b current inv
R2326 | page 19 | line 1325 | ENTITY | Nippon India Dynamic Term Fund | [I2] holding listed, cons note 8b current inv
R2327 | page 19 | line 1326 | ENTITY | SBI Corporate Bond Fund | [I2] holding listed, cons note 8b current inv
R2328 | page 19 | line 1327 | ENTITY | Tata Money Market Fund | [I2] holding listed, cons note 8b current inv
R2329 | page 19 | line 1328 | ENTITY | Nippon India Nivesh Lakshya Long Term Fund | [I2] holding listed, cons note 8b current inv
R2330 | page 19 | line 1329 | ENTITY | Nippon India Nifty Alpha Low Volatility 30 Index Fund | [I2] holding listed, cons note 8b current inv
R2331 | page 19 | line 1330 | ENTITY | Tata Arbitrage Fund | [I2] holding listed, cons note 8b current inv
R2332 | page 19 | line 1331 | ENTITY | SBI Nifty 200 Quality 30 ETF | [I2] holding listed, cons note 8b current inv
R2333 | page 19 | line 1332 | ENTITY | UTI Money Market Fund | [I2] holding listed, cons note 8b current inv
R2334 | page 19 | line 1333 | ENTITY | UTI Nifty200 Quality 30 Index Fund | [I2] holding listed, cons note 8b current inv
R2335 | page 19 | line 1334 | ENTITY | Bajaj Finserv Liquid Fund | [I2] holding listed, cons note 8b current inv
R2336 | page 19 | line 1335 | ENTITY | Kotak Money Market Fund | [I2] holding listed, cons note 8b current inv
R2337 | page 19 | line 1336 | ENTITY | UTI Liquid Fund | [I2] holding listed, cons note 8b current inv
R2338 | page 19 | line 1337 | ENTITY | Bandhan Money Market Fund | [I2] holding listed, cons note 8b current inv
R2339 | page 19 | line 1338 | ENTITY | Altiva Hybrid Long Short Fund | [I2] holding listed, cons note 8b current inv
R2340 | page 19 | line 1339 | ENTITY | SBI 10 YEAR CONSTANT MATURITY GILT FUND | [I2] holding listed, cons note 8b current inv
R2341 | page 19 | line 1340 | ENTITY | Magnum Hybrid Long Short Fund | [I2] holding listed, cons note 8b current inv
R2342 | page 19 | line 1341 | ENTITY | SBI Nifty200 Quality 30 Index Fund | [I2] holding listed, cons note 8b current inv
R2343 | page 19 | line 1342 | ENTITY | ICICI Alpha Low Volatility 30 ETF | [I2] holding listed, cons note 8b current inv
R2344 | page 19 | line 1343 | ENTITY | Edelweiss Liquid Fund | [I2] holding listed, cons note 8b current inv
R2345 | page 19 | line 1344 | ENTITY | Edelweiss Banking and PSU Debt Fund | [I2] holding listed, cons note 8b current inv
R2346 | page 19 | line 1345 | ENTITY | Tata Overnight Fund | [I2] holding listed, cons note 8b current inv
R2347 | page 19 | line 1346 | ENTITY | Kotak Nifty Midcap 150 Momentum 50 Index Fund | [I2] holding listed, cons note 8b current inv
R2348 | page 19 | line 1351 | ENTITY | Bajaj Finance Ltd. Bond | [I2] holding listed, cons note 8b current inv
R2349 | page 19 | line 1352 | ENTITY | Axis Finance Ltd. Bond | [I2] holding listed, cons note 8b current inv
R2350 | page 19 | line 1353 | ENTITY | HDFC Bank Perpetual Bond | [I2] holding listed, cons note 8b current inv
R2351 | page 19 | line 1354 | ENTITY | HDFC Bank Bond | [I2] holding listed, cons note 8b current inv
R2352 | page 19 | line 1355 | ENTITY | HDB Financial Services Ltd Bond | [I2] holding listed, cons note 8b current inv
R2353 | page 19 | line 1356 | ENTITY | ICICI Bank Bond | [I2] holding listed, cons note 8b current inv
R2354 | page 19 | line 1357 | ENTITY | Kotak Mahindra Prime Ltd. Bond | [I2] holding listed, cons note 8b current inv
R2355 | page 19 | line 1358 | ENTITY | India Infradebt Ltd Bond | [I2] holding listed, cons note 8b current inv
R2356 | page 19 | line 1359 | ENTITY | LIC Housing Finance Ltd Bond | [I2] holding listed, cons note 8b current inv
R2357 | page 19 | line 1360 | ENTITY | Mahindra & Mahindra Financial Services Ltd. Bond | [I2] holding listed, cons note 8b current inv
R2358 | page 19 | line 1361 | ENTITY | Punjab National Bank Perpetual Bond | [I2] holding listed, cons note 8b current inv
R2359 | page 19 | line 1362 | ENTITY | REC Zero Coupon Bond | [I2] holding listed, cons note 8b current inv
R2360 | page 19 | line 1363 | ENTITY | State Bank of India Perpetual Bond | [I2] holding listed, cons note 8b current inv
R2361 | page 19 | line 1364 | ENTITY | State Bank of India Tier-II Bond | [I2] holding listed, cons note 8b current inv
R2362 | page 19 | line 1365 | ENTITY | LIC Housing Finance Limited Bond | [I2] holding listed, cons note 8b current inv
R2363 | page 19 | line 1366 | ENTITY | Tata Capital Limited Bond | [I2] holding listed, cons note 8b current inv
R2364 | page 19 | line 1367 | ENTITY | Club with Mahindra & Mahindra Financial Services Ltd. Bond | [I2] holding listed, cons note 8b current inv
R2365 | page 19 | line 1368 | ENTITY | Union Bank of India Perpetual Bond | [I2] holding listed, cons note 8b current inv
R2366 | page 19 | line 1369 | ENTITY | Power Finance Corporation Zero Coupon Bond | [I2] holding listed, cons note 8b current inv
R2367 | page 19 | line 1373 | ENTITY | 7.18% Government of India 2037 | [I2] holding listed, cons note 8b current inv
R2368 | page 19 | line 1374 | ENTITY | 7.44% Government of Karnataka SGS 2034 | [I2] holding listed, cons note 8b current inv
R2369 | page 19 | line 1375 | ENTITY | 7.42% Government of Karnataka SGS 2035 | [I2] holding listed, cons note 8b current inv
R2370 | page 19 | line 1376 | ENTITY | 7.45% Government of Karnataka SGS 2037 | [I2] holding listed, cons note 8b current inv
R2371 | page 19 | line 1377 | ENTITY | 7.43% Government of Tamil Nadu SGS 2034 | [I2] holding listed, cons note 8b current inv
R2372 | page 19 | line 1378 | ENTITY | 7.38% Government of Tamil Nadu SGS 2034 | [I2] holding listed, cons note 8b current inv
R2373 | page 19 | line 1379 | ENTITY | 7.34% Government of Tamil Nadu SGS 2034 | [I2] holding listed, cons note 8b current inv
R2374 | page 19 | line 1380 | ENTITY | 7.72% Government of Maharashtra SGS 2035 | [I2] holding listed, cons note 8b current inv
R2375 | page 19 | line 1381 | ENTITY | 7.40% Government of Maharashtra SGS 2035 | [I2] holding listed, cons note 8b current inv
R2376 | page 19 | line 1382 | ENTITY | 7.73% Government of Maharashtra SGS 2036 | [I2] holding listed, cons note 8b current inv
R2377 | page 19 | line 1383 | ENTITY | 6.48% Government of India 2035 | [I2] holding listed, cons note 8b current inv
R2378 | page 19 | line 1384 | ENTITY | 6.68% Government of India 2040 | [I2] holding listed, cons note 8b current inv
R2379 | page 20 | line 1458 | ENTITY | - PNB Housing Finance Limited ^ | [I2] named entity with figures, cons note 8c/d loans, other fin assets
R2380 | page 20 | line 1460 | ENTITY | - Bajaj Finance Limited ^ | [I2] named entity with figures, cons note 8c/d loans, other fin assets
R2381 | page 27 | line 1952 | ENTITY | Legistify Services Private Limited, Mynd Solutions Private | [I2] named entity, cons note 28 fair value
R2382 | page 27 | line 1953 | ENTITY | Limited, Zimyo Consulting Private Limited, Instant Procurement | [I2] named entity, cons note 28 fair value
R2383 | page 27 | line 1954 | ENTITY | Services Private Limited and Baldor Technologies Private Limited, | [I2] named entity, cons note 28 fair value
R2384 | page 46 | line 3168 | ENTITY | Tradezeal Online Private Limited | [I2] named entity, stand note 7 subs+assoc
R2385 | page 46 | line 3175 | ENTITY | Busy Infotech Private Limited (formerly Tolexo Online Private Limited) | [I2] named entity, stand note 7 subs+assoc
R2386 | page 46 | line 3179 | ENTITY | Pay With Indiamart Private Limited | [I2] named entity, stand note 7 subs+assoc
R2387 | page 46 | line 3183 | ENTITY | Indiamart Finance Limited | [I2] named entity, stand note 7 subs+assoc
R2388 | page 46 | line 3187 | ENTITY | Livekeeping Technologies Private Limited | [I2] named entity, stand note 7 subs+assoc
R2389 | page 46 | line 3196 | ENTITY | IIL Digital Private Limited | [I2] named entity, stand note 7 subs+assoc
R2390 | page 46 | line 3206 | ENTITY | Simply Vyapar Apps Private Limited | [I2] named entity, stand note 7 subs+assoc
R2391 | page 46 | line 3225 | ENTITY | Mobisy Technologies Private Limited | [I2] named entity, stand note 7 subs+assoc
R2392 | page 46 | line 3247 | ENTITY | Fleetx Technologies Private Limited | [I2] named entity, stand note 7 subs+assoc
R2393 | page 47 | line 3300 | ENTITY | Tradezeal Online Private Limited | [I2] named entity, stand note 8a non-current inv
R2394 | page 47 | line 3305 | ENTITY | Pay With Indiamart Private Limited | [I2] named entity, stand note 8a non-current inv
R2395 | page 47 | line 3310 | ENTITY | Mynd Solutions Private Limited | [I2] named entity, stand note 8a non-current inv
R2396 | page 47 | line 3318 | ENTITY | Zimyo consulting Private Limited | [I2] named entity, stand note 8a non-current inv
R2397 | page 47 | line 3323 | ENTITY | Baldor Technologies Private Limited | [I2] named entity, stand note 8a non-current inv
R2398 | page 48 | line 3367 | ENTITY | Aditya Birla Sun Life Arbitrage Fund | [I2] holding listed, stand note 8b current inv
R2399 | page 48 | line 3368 | ENTITY | Aditya Birla Sun Life Corporate Bond Fund | [I2] holding listed, stand note 8b current inv
R2400 | page 48 | line 3369 | ENTITY | Aditya Birla Sun Life Nifty SDL Apr 2027 Index Fund | [I2] holding listed, stand note 8b current inv
R2401 | page 48 | line 3370 | ENTITY | Axis Corporate Bond Fund | [I2] holding listed, stand note 8b current inv
R2402 | page 48 | line 3371 | ENTITY | Axis Liquid Fund | [I2] holding listed, stand note 8b current inv
R2403 | page 48 | line 3372 | ENTITY | BHARAT Bond ETF - April 2030 | [I2] holding listed, stand note 8b current inv
R2404 | page 48 | line 3373 | ENTITY | Bandhan Money Market Fund | [I2] holding listed, stand note 8b current inv
R2405 | page 48 | line 3374 | ENTITY | Edelweiss NIFTY PSU Bond Plus SDL Apr 2026 50:50 Index Fund | [I2] holding listed, stand note 8b current inv
R2406 | page 48 | line 3375 | ENTITY | Edelweiss Liquid Fund | [I2] holding listed, stand note 8b current inv
R2407 | page 48 | line 3376 | ENTITY | Edelweiss CRISIL IBX 50:50 Gilt Plus SDL April 2037 index fund | [I2] holding listed, stand note 8b current inv
R2408 | page 48 | line 3377 | ENTITY | Edelweiss Arbitrage Fund | [I2] holding listed, stand note 8b current inv
R2409 | page 48 | line 3378 | ENTITY | Edelweiss Nifty Midcap150 Momentum 50 Index Fund | [I2] holding listed, stand note 8b current inv
R2410 | page 48 | line 3379 | ENTITY | HDFC Ultra Short to Short Term Fund | [I2] holding listed, stand note 8b current inv
R2411 | page 48 | line 3380 | ENTITY | HDFC Corporate Bond Fund | [I2] holding listed, stand note 8b current inv
R2412 | page 48 | line 3381 | ENTITY | ICICI Prudential Ultra Short to Short Term Fund | [I2] holding listed, stand note 8b current inv
R2413 | page 48 | line 3382 | ENTITY | ICICI Prudential Money Market Fund | [I2] holding listed, stand note 8b current inv
R2414 | page 48 | line 3383 | ENTITY | ICICI Prudential Liquid Fund | [I2] holding listed, stand note 8b current inv
R2415 | page 48 | line 3384 | ENTITY | ICICI Prudential Corporate Bond Fund | [I2] holding listed, stand note 8b current inv
R2416 | page 48 | line 3385 | ENTITY | ICICI Prudential Nifty SDL Dec 2028 Index Fund | [I2] holding listed, stand note 8b current inv
R2417 | page 48 | line 3386 | ENTITY | Edelweiss Banking and PSU Debt Fund | [I2] holding listed, stand note 8b current inv
R2418 | page 48 | line 3387 | ENTITY | ICICI Prudential Nifty Alpha Low Volatility 30 ETF | [I2] holding listed, stand note 8b current inv
R2419 | page 48 | line 3388 | ENTITY | ICICI Prudential Nifty 200 Quality 30 ETF | [I2] holding listed, stand note 8b current inv
R2420 | page 48 | line 3389 | ENTITY | Invesco India Arbitrage Fund | [I2] holding listed, stand note 8b current inv
R2421 | page 48 | line 3390 | ENTITY | Kotak Corporate Bond Fund | [I2] holding listed, stand note 8b current inv
R2422 | page 48 | line 3391 | ENTITY | Kotak Arbitrage Fund | [I2] holding listed, stand note 8b current inv
R2423 | page 48 | line 3392 | ENTITY | Kotak Money Market Fund | [I2] holding listed, stand note 8b current inv
R2424 | page 48 | line 3393 | ENTITY | Kotak Nifty SDL Apr 2027 Top 12 Equal Weight Index Fund | [I2] holding listed, stand note 8b current inv
R2425 | page 48 | line 3394 | ENTITY | Kotak Nifty SDL Apr 2032 Top 12 Equal Weight Index Fund | [I2] holding listed, stand note 8b current inv
R2426 | page 48 | line 3395 | ENTITY | Kotak Nifty Midcap 150 Momentum 50 Index Fund | [I2] holding listed, stand note 8b current inv
R2427 | page 48 | line 3396 | ENTITY | Nippon India Dynamic Term Fund | [I2] holding listed, stand note 8b current inv
R2428 | page 48 | line 3397 | ENTITY | Tata Money Market Fund | [I2] holding listed, stand note 8b current inv
R2429 | page 48 | line 3398 | ENTITY | Nippon India Nivesh Lakshya Long Term Fund | [I2] holding listed, stand note 8b current inv
R2430 | page 48 | line 3399 | ENTITY | Nippon India Nifty Alpha Low Volatility 30 Index Fund | [I2] holding listed, stand note 8b current inv
R2431 | page 48 | line 3400 | ENTITY | SBI 10 Year Constant Maturity Gilt Fund | [I2] holding listed, stand note 8b current inv
R2432 | page 48 | line 3401 | ENTITY | SBI Nifty200 Quality 30 Index Fund | [I2] holding listed, stand note 8b current inv
R2433 | page 48 | line 3402 | ENTITY | SBI Nifty 200 Quality 30 ETF | [I2] holding listed, stand note 8b current inv
R2434 | page 48 | line 3403 | ENTITY | Tata Arbitrage Fund | [I2] holding listed, stand note 8b current inv
R2435 | page 48 | line 3404 | ENTITY | UTI Money Market Fund | [I2] holding listed, stand note 8b current inv
R2436 | page 48 | line 3405 | ENTITY | Tata Overnight Fund | [I2] holding listed, stand note 8b current inv
R2437 | page 48 | line 3406 | ENTITY | UTI Nifty200 Quality 30 Index Fund | [I2] holding listed, stand note 8b current inv
R2438 | page 48 | line 3407 | ENTITY | UTI Liquid Fund | [I2] holding listed, stand note 8b current inv
R2439 | page 48 | line 3411 | ENTITY | Bajaj Finance Ltd. Bond | [I2] holding listed, stand note 8b current inv
R2440 | page 48 | line 3412 | ENTITY | ICICI Bank Bond | [I2] holding listed, stand note 8b current inv
R2441 | page 48 | line 3413 | ENTITY | Axis Finance Ltd. Bond | [I2] holding listed, stand note 8b current inv
R2442 | page 48 | line 3414 | ENTITY | HDFC Bank Perpetual Bond | [I2] holding listed, stand note 8b current inv
R2443 | page 48 | line 3415 | ENTITY | HDFC Bank Bond | [I2] holding listed, stand note 8b current inv
R2444 | page 48 | line 3416 | ENTITY | HDB Financial Services Ltd Bond | [I2] holding listed, stand note 8b current inv
R2445 | page 48 | line 3417 | ENTITY | India Infradebt Ltd Bond | [I2] holding listed, stand note 8b current inv
R2446 | page 48 | line 3418 | ENTITY | Kotak Mahindra Prime Ltd. Bond | [I2] holding listed, stand note 8b current inv
R2447 | page 48 | line 3419 | ENTITY | LIC Housing Finance Bond | [I2] holding listed, stand note 8b current inv
R2448 | page 48 | line 3420 | ENTITY | Mahindra & Mahindra Financial Services Ltd. Bond | [I2] holding listed, stand note 8b current inv
R2449 | page 48 | line 3421 | ENTITY | Punjab National Bank Perpetual Bond | [I2] holding listed, stand note 8b current inv
R2450 | page 48 | line 3422 | ENTITY | REC Zero Coupon Bond | [I2] holding listed, stand note 8b current inv
R2451 | page 48 | line 3423 | ENTITY | TATA Capital Limited Bond | [I2] holding listed, stand note 8b current inv
R2452 | page 48 | line 3424 | ENTITY | State Bank of India Perpetual Bond | [I2] holding listed, stand note 8b current inv
R2453 | page 48 | line 3425 | ENTITY | Union Bank of India Perpetual Bond | [I2] holding listed, stand note 8b current inv
R2454 | page 48 | line 3429 | ENTITY | 7.18% Government of India 2037 | [I2] holding listed, stand note 8b current inv
R2455 | page 48 | line 3430 | ENTITY | 7.44% Government of Karnataka SGS 2034 | [I2] holding listed, stand note 8b current inv
R2456 | page 48 | line 3431 | ENTITY | 7.42% Government of Karnataka SGS 2035 | [I2] holding listed, stand note 8b current inv
R2457 | page 48 | line 3432 | ENTITY | 7.45% Government of Karnataka SGS 2037 | [I2] holding listed, stand note 8b current inv
R2458 | page 48 | line 3433 | ENTITY | 7.43% Government of Tamil Nadu SGS 2034 | [I2] holding listed, stand note 8b current inv
R2459 | page 48 | line 3434 | ENTITY | 7.72% Government of Maharashtra SGS 2035 | [I2] holding listed, stand note 8b current inv
R2460 | page 48 | line 3435 | ENTITY | 7.40% Government of Maharashtra SGS 2035 | [I2] holding listed, stand note 8b current inv
R2461 | page 48 | line 3436 | ENTITY | 7.73% Government of Maharashtra SGS 2036 | [I2] holding listed, stand note 8b current inv
R2462 | page 48 | line 3437 | ENTITY | 6.48% Government of India 2035 | [I2] holding listed, stand note 8b current inv
R2463 | page 48 | line 3438 | ENTITY | 7.38% Government of Tamil Nadu SGS 2034 | [I2] holding listed, stand note 8b current inv
R2464 | page 48 | line 3439 | ENTITY | 7.34% Government of Tamil Nadu SGS 2034 | [I2] holding listed, stand note 8b current inv
R2465 | page 48 | line 3440 | ENTITY | 6.68% Government of India 2040 | [I2] holding listed, stand note 8b current inv
R2466 | page 49 | line 3473 | ENTITY | -PNB Housing Finance Ltd.^ | [I2] named entity with figures, stand note 8 loans, other fin assets
R2467 | page 57 | line 3975 | ENTITY | Zimyo Consulting Private Limited, Mynd Solutions Private Limited, Fleetx | [I2] named entity, stand note 28 fair value level 3
R2468 | page 29 | line 2099 | ENTITY | 30 Related party transactions | [I3] named entity, cons note 30 RPT list
R2469 | page 29 | line 2100 | ENTITY | i) Names of related parties and related party relationship: | [I3] named entity, cons note 30 RPT list
R2470 | page 29 | line 2102 | ENTITY | a) Entity's subsidiaries & associates Subsidiaries | [I3] named entity, cons note 30 RPT list
R2471 | page 29 | line 2109 | ENTITY | Associates | [I3] named entity, cons note 30 RPT list
R2472 | page 29 | line 2118 | ENTITY | b) Key Management | [I3] named entity, cons note 30 RPT list
R2473 | page 29 | line 2094 | ENTITY | Name Designation | [I3] named entity, cons note 30 RPT list
R2474 | page 29 | line 2120 | ENTITY | Dinesh Chandra Agarwal Managing Director & CEO | [I3] named entity, cons note 30 RPT list
R2475 | page 29 | line 2121 | ENTITY | Brijesh Kumar Agrawal Whole Time Director | [I3] named entity, cons note 30 RPT list
R2476 | page 29 | line 2094 | ENTITY | Jitin Diwan Chief Financial Officer | [I3] named entity, cons note 30 RPT list
R2477 | page 29 | line 2123 | ENTITY | Manoj Bhargava Company Secretary & Whole time director | [I3] named entity, cons note 30 RPT list
R2478 | page 29 | line 2126 | ENTITY | Vivek Narayan Gour Independent Director | [I3] named entity, cons note 30 RPT list
R2479 | page 29 | line 2127 | ENTITY | Pallavi Dinodia Gupta Independent Director | [I3] named entity, cons note 30 RPT list
R2480 | page 29 | line 2094 | ENTITY | Manish Vij Independent Director | [I3] named entity, cons note 30 RPT list
R2481 | page 29 | line 2129 | ENTITY | Vasudha Bagri Compliance Officer | [I3] named entity, cons note 30 RPT list
R2482 | page 29 | line 2130 | ENTITY | Sandeep Barasiya Independent Director (with effect from 29 April 2025) | [I3] named entity, cons note 30 RPT list
R2483 | page 29 | line 2131 | ENTITY | Vasuta Agarwal Independent Director (with effect from 18 July 2025 ) | [I3] named entity, cons note 30 RPT list
R2484 | page 29 | line 2133 | ENTITY | c) Relatives of Key Management Personnel (KMP)* | [I3] named entity, cons note 30 RPT list
R2485 | page 29 | line 2134 | ENTITY | Bharat Agarwal | [I3] named entity, cons note 30 RPT list
R2486 | page 29 | line 2135 | ENTITY | Chetna Agarwal | [I3] named entity, cons note 30 RPT list
R2487 | page 29 | line 2136 | ENTITY | Gunjan Agarwal | [I3] named entity, cons note 30 RPT list
R2488 | page 29 | line 2137 | ENTITY | Anand Kumar Agrawal | [I3] named entity, cons note 30 RPT list
R2489 | page 29 | line 2138 | ENTITY | Meena Agrawal | [I3] named entity, cons note 30 RPT list
R2490 | page 29 | line 2139 | ENTITY | Pankaj Agarwal | [I3] named entity, cons note 30 RPT list
R2491 | page 29 | line 2140 | ENTITY | Naresh Chandra Agrawal | [I3] named entity, cons note 30 RPT list
R2492 | page 29 | line 2141 | ENTITY | Prakash Chandra Agrawal | [I3] named entity, cons note 30 RPT list
R2493 | page 29 | line 2142 | ENTITY | Shravani Prakash | [I3] named entity, cons note 30 RPT list
R2494 | page 29 | line 2143 | ENTITY | Anjani Prakash | [I3] named entity, cons note 30 RPT list
R2495 | page 29 | line 2144 | ENTITY | Pradeep Dinodia | [I3] named entity, cons note 30 RPT list
R2496 | page 29 | line 2145 | ENTITY | Amit Agarwal ^ | [I3] named entity, cons note 30 RPT list
R2497 | page 29 | line 2147 | ENTITY | d) Entities where Key Management Personnel (KMP) exercise significant influence.* | [I3] named entity, cons note 30 RPT list
R2498 | page 29 | line 2148 | ENTITY | Mansa Enterprises Private Limited | [I3] named entity, cons note 30 RPT list
R2499 | page 29 | line 2149 | ENTITY | S R Dinodia & Co LLP | [I3] named entity, cons note 30 RPT list
R2500 | page 29 | line 2150 | ENTITY | Dinesh Chandra Agarwal HUF | [I3] named entity, cons note 30 RPT list
R2501 | page 29 | line 2151 | ENTITY | Nanpara Family Trust | [I3] named entity, cons note 30 RPT list
R2502 | page 29 | line 2152 | ENTITY | Nanpara Business Trust | [I3] named entity, cons note 30 RPT list
R2503 | page 29 | line 2153 | ENTITY | Hamirwasia Business Trust | [I3] named entity, cons note 30 RPT list
R2504 | page 29 | line 2154 | ENTITY | Hamirwasia Family Trust | [I3] named entity, cons note 30 RPT list
R2505 | page 29 | line 2156 | ENTITY | e) Other related parties* | [I3] named entity, cons note 30 RPT list
R2506 | page 29 | line 2163 | ENTITY | ii) Key management personnel compensation | [I3] named entity, cons note 30 RPT list
R2507 | page 29 | line 2102 | ENTITY | Tradezeal Online Private Limited | [I3] named entity, cons note 30 RPT list
R2508 | page 29 | line 2103 | ENTITY | Busy Infotech Private Limited (Formerly Tolexo Online Private Limited) | [I3] named entity, cons note 30 RPT list
R2509 | page 29 | line 2104 | ENTITY | Pay With Indiamart Private Limited | [I3] named entity, cons note 30 RPT list
R2510 | page 29 | line 2105 | ENTITY | Livekeeping Technologies Private Limited | [I3] named entity, cons note 30 RPT list
R2511 | page 29 | line 2109 | ENTITY | Simply Vyapar Apps Private Limited | [I3] named entity, cons note 30 RPT list
R2512 | page 29 | line 2115 | ENTITY | Adansa Solutions Private Limited | [I3] named entity, cons note 30 RPT list
R2513 | page 29 | line 2116 | ENTITY | Mobisy Technologies Private Limited | [I3] named entity, cons note 30 RPT list
R2514 | page 29 | line 2110 | ENTITY | Truckhall Private Limited | [I3] named entity, cons note 30 RPT list
R2515 | page 29 | line 2111 | ENTITY | Fleetx Technologies Private Limited (with effect from 11 April 2025) | [I3] named entity, cons note 30 RPT list
R2516 | page 29 | line 2112 | ENTITY | Agillos E-Commerce Private Limited | [I3] named entity, cons note 30 RPT list
R2517 | page 29 | line 2113 | ENTITY | Edgewise Technologies Private Limited | [I3] named entity, cons note 30 RPT list
R2518 | page 30 | line 2187 | ENTITY | Mansa Enterprises Private Limited | [I3] named entity with figures, cons note 30 RPT transactions
R2519 | page 30 | line 2190 | ENTITY | S R Dinodia & Co LLP | [I3] named entity with figures, cons note 30 RPT transactions
R2520 | page 30 | line 2210 | ENTITY | Fleetex Technologies Private Limited | [I3] named entity with figures, cons note 30 RPT transactions
R2521 | page 30 | line 2213 | ENTITY | Agillos E-Commerce Private Limited | [I3] named entity with figures, cons note 30 RPT transactions
R2522 | page 30 | line 2216 | ENTITY | Simply Vyapar Apps Private Limited | [I3] named entity with figures, cons note 30 RPT transactions
R2523 | page 30 | line 2217 | ENTITY | IB Monotaro Private Limited | [I3] named entity with figures, cons note 30 RPT transactions
R2524 | page 30 | line 2221 | ENTITY | Indiamart Employee Benefit Trust | [I3] named entity, cons note 30 RPT transactions
R2525 | page 31 | line 2241 | ENTITY | Simply Vyapar Apps Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2526 | page 31 | line 2242 | ENTITY | Truckhall Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2527 | page 31 | line 2243 | ENTITY | Agillos E-Commerce Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2528 | page 31 | line 2244 | ENTITY | Edgewise Technologies Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2529 | page 31 | line 2245 | ENTITY | IB Monotaro Private Limited (refer note 7 (iv)) | [I3] named entity with figures, cons note 30 RPT balances
R2530 | page 31 | line 2246 | ENTITY | Adansa Solutions Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2531 | page 31 | line 2247 | ENTITY | Mobisy Technologies Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2532 | page 31 | line 2248 | ENTITY | Fleetx Technologies Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2533 | page 31 | line 2251 | ENTITY | Agillos E-Commerce Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2534 | page 31 | line 2254 | ENTITY | Edgewise Technologies Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2535 | page 31 | line 2257 | ENTITY | Simply Vyapar Apps Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2536 | page 31 | line 2260 | ENTITY | S R Dinodia & Co LLP | [I3] named entity with figures, cons note 30 RPT balances
R2537 | page 31 | line 2261 | ENTITY | Mansa Enterprises Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2538 | page 31 | line 2264 | ENTITY | Simply Vyapar Apps Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2539 | page 31 | line 2245 | ENTITY | IB Monotaro Private Limited | [I3] named entity with figures, cons note 30 RPT balances
R2540 | page 58 | line 4030 | ENTITY | 29 Segment information | [I3] named entity, stand note 30 RPT list
R2541 | page 58 | line 4033 | ENTITY | 30 Related party transactions | [I3] named entity, stand note 30 RPT list
R2542 | page 58 | line 4034 | ENTITY | i) Names of related parties and related party relationship: | [I3] named entity, stand note 30 RPT list
R2543 | page 58 | line 4036 | ENTITY | a) Entity's subsidiaries & associates Subsidiaries Tradezeal Online Private Limited | [I3] named entity, stand note 30 RPT list
R2544 | page 58 | line 4037 | ENTITY | Busy Infotech Private Limited (Formerly Tolexo Online Private Limited) | [I3] named entity, stand note 30 RPT list
R2545 | page 58 | line 4038 | ENTITY | Pay With Indiamart Private Limited | [I3] named entity, stand note 30 RPT list
R2546 | page 58 | line 4039 | ENTITY | Livekeeping Technologies Private Limited | [I3] named entity, stand note 30 RPT list
R2547 | page 58 | line 4040 | ENTITY | IIL Digital Private Limited | [I3] named entity, stand note 30 RPT list
R2548 | page 58 | line 4043 | ENTITY | Associates Simply Vyapar Apps Private Limited | [I3] named entity, stand note 30 RPT list
R2549 | page 58 | line 4045 | ENTITY | Mobisy Technologies Private Limited | [I3] named entity, stand note 30 RPT list
R2550 | page 58 | line 4046 | ENTITY | Fleetx Technologies Private Limited (with effect from 11 April 2025) | [I3] named entity, stand note 30 RPT list
R2551 | page 58 | line 4025 | ENTITY | Name Designation | [I3] named entity, stand note 30 RPT list
R2552 | page 58 | line 4047 | ENTITY | Dinesh Chandra Agarwal Managing Director & CEO | [I3] named entity, stand note 30 RPT list
R2553 | page 58 | line 4048 | ENTITY | Brijesh Kumar Agrawal Whole Time Director | [I3] named entity, stand note 30 RPT list
R2554 | page 58 | line 4025 | ENTITY | Jitin Diwan Chief Financial Officer | [I3] named entity, stand note 30 RPT list
R2555 | page 58 | line 4050 | ENTITY | Manoj Bhargava Company Secretary & Whole time director | [I3] named entity, stand note 30 RPT list
R2556 | page 58 | line 4053 | ENTITY | Vivek Narayan Gour Independent Director | [I3] named entity, stand note 30 RPT list
R2557 | page 58 | line 4054 | ENTITY | Pallavi Dinodia Gupta Independent Director | [I3] named entity, stand note 30 RPT list
R2558 | page 58 | line 4055 | ENTITY | Manish Vij Independent Director | [I3] named entity, stand note 30 RPT list
R2559 | page 58 | line 4056 | ENTITY | Vasudha Bagri Compliance Officer | [I3] named entity, stand note 30 RPT list
R2560 | page 58 | line 4057 | ENTITY | Sandeep Barasiya Independent Director (with effect from 29 April 2025) | [I3] named entity, stand note 30 RPT list
R2561 | page 58 | line 4058 | ENTITY | Vasuta Agarwal Independent Director (with effect from 18 July 2025) | [I3] named entity, stand note 30 RPT list
R2562 | page 58 | line 4063 | ENTITY | Bharat Agarwal | [I3] named entity, stand note 30 RPT list
R2563 | page 58 | line 4064 | ENTITY | Chetna Agarwal | [I3] named entity, stand note 30 RPT list
R2564 | page 58 | line 4065 | ENTITY | Gunjan Agarwal | [I3] named entity, stand note 30 RPT list
R2565 | page 58 | line 4066 | ENTITY | Anand Kumar Agrawal | [I3] named entity, stand note 30 RPT list
R2566 | page 58 | line 4067 | ENTITY | Meena Agrawal | [I3] named entity, stand note 30 RPT list
R2567 | page 58 | line 4068 | ENTITY | Pankaj Agarwal | [I3] named entity, stand note 30 RPT list
R2568 | page 58 | line 4069 | ENTITY | Naresh Chandra Agrawal | [I3] named entity, stand note 30 RPT list
R2569 | page 58 | line 4070 | ENTITY | Prakash Chandra Agrawal | [I3] named entity, stand note 30 RPT list
R2570 | page 58 | line 4071 | ENTITY | Shravani Prakash | [I3] named entity, stand note 30 RPT list
R2571 | page 58 | line 4072 | ENTITY | Anjani Prakash | [I3] named entity, stand note 30 RPT list
R2572 | page 58 | line 4073 | ENTITY | Pradeep Dinodia | [I3] named entity, stand note 30 RPT list
R2573 | page 58 | line 4077 | ENTITY | Mansa Enterprises Private Limited | [I3] named entity, stand note 30 RPT list
R2574 | page 58 | line 4078 | ENTITY | S R Dinodia & Co LLP | [I3] named entity, stand note 30 RPT list
R2575 | page 58 | line 4079 | ENTITY | Dinesh Chandra Agarwal HUF | [I3] named entity, stand note 30 RPT list
R2576 | page 58 | line 4080 | ENTITY | Nanpara Family Trust | [I3] named entity, stand note 30 RPT list
R2577 | page 58 | line 4081 | ENTITY | Nanpara Business Trust | [I3] named entity, stand note 30 RPT list
R2578 | page 58 | line 4082 | ENTITY | Hamirwasia Business Trust | [I3] named entity, stand note 30 RPT list
R2579 | page 58 | line 4083 | ENTITY | Hamirwasia Family Trust | [I3] named entity, stand note 30 RPT list
R2580 | page 58 | line 4085 | ENTITY | e) Other related parties* | [I3] named entity, stand note 30 RPT list
R2581 | page 58 | line 4091 | ENTITY | ii) Key management personnel compensation | [I3] named entity, stand note 30 RPT list
R2582 | page 58 | line 4076 | ENTITY | d) Entities where Key Management Personnel (KMP) exercise significant influence* | [I3] named entity, stand note 30 RPT list
R2583 | page 58 | line 4045 | ENTITY | b) Key Management Personnel (KMP) | [I3] named entity, stand note 30 RPT list
R2584 | page 58 | line 4062 | ENTITY | c) Relatives of Key Management Personnel (KMPs)* | [I3] named entity, stand note 30 RPT list
R2585 | page 58 | line 4074 | ENTITY | Amit Agarwal^ | [I3] named entity, stand note 30 RPT list
R2586 | page 59 | line 4111 | ENTITY | Mansa Enterprises Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2587 | page 59 | line 4114 | ENTITY | S R Dinodia & Co LLP | [I3] named entity with figures, stand note 30 RPT transactions
R2588 | page 59 | line 4128 | ENTITY | IIL Digital Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2589 | page 59 | line 4129 | ENTITY | Tradezeal Online Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2590 | page 59 | line 4130 | ENTITY | Livekeeping Technologies Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2591 | page 59 | line 4131 | ENTITY | IndiaMart Finance Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2592 | page 59 | line 4134 | ENTITY | Fleetx Technologies Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2593 | page 59 | line 4144 | ENTITY | Simply Vyapar Apps Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2594 | page 59 | line 4145 | ENTITY | IB Monotaro Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2595 | page 59 | line 4146 | ENTITY | Livekeeping Technologies Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2596 | page 59 | line 4147 | ENTITY | Busy Infotech Private Limited (Formerly known as Tolexo) | [I3] named entity with figures, stand note 30 RPT transactions
R2597 | page 59 | line 4150 | ENTITY | Livekeeping Technologies Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2598 | page 59 | line 4151 | ENTITY | Busy Infotech Private Limited (Formerly known as Tolexo) | [I3] named entity with figures, stand note 30 RPT transactions
R2599 | page 59 | line 4152 | ENTITY | IIL Digital Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2600 | page 59 | line 4153 | ENTITY | IndiaMart Finance Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2601 | page 59 | line 4160 | ENTITY | IIL Digital Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2602 | page 59 | line 4165 | ENTITY | IIL Digital Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2603 | page 59 | line 4168 | ENTITY | Busy Infotech Private Limited (Formerly known as Tolexo) | [I3] named entity with figures, stand note 30 RPT transactions
R2604 | page 59 | line 4169 | ENTITY | Livekeeping Technologies Private Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2605 | page 59 | line 4172 | ENTITY | IndiaMart Finance Limited | [I3] named entity with figures, stand note 30 RPT transactions
R2606 | page 59 | line 4174 | ENTITY | Indiamart Employee Benefit Trust | [I3] named entity, stand note 30 RPT transactions
R2607 | page 60 | line 4190 | ENTITY | Tradezeal Online Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2608 | page 60 | line 4191 | ENTITY | Pay With Indiamart Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2609 | page 60 | line 4196 | ENTITY | Busy Infotech Private Limited (Formerly Known as Tolexo) ^ | [I3] named entity with figures, stand note 30 RPT balances
R2610 | page 60 | line 4197 | ENTITY | Tradezeal Online Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2611 | page 60 | line 4198 | ENTITY | Pay With Indiamart Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2612 | page 60 | line 4199 | ENTITY | Livekeeping Technologies Private Limited ^* | [I3] named entity with figures, stand note 30 RPT balances
R2613 | page 60 | line 4200 | ENTITY | IIL Digital Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2614 | page 60 | line 4201 | ENTITY | IndiaMart Finance Limited (incorporated on 04 August 2026) | [I3] named entity with figures, stand note 30 RPT balances
R2615 | page 60 | line 4204 | ENTITY | Simply Vyapar Apps Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2616 | page 60 | line 4205 | ENTITY | IB Monotaro Private Limited(refer note 7 (vii))* | [I3] named entity with figures, stand note 30 RPT balances
R2617 | page 60 | line 4206 | ENTITY | Mobisy Technologies Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2618 | page 60 | line 4207 | ENTITY | Fleetx Technologies Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2619 | page 60 | line 4210 | ENTITY | Simply Vyapar Apps Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2620 | page 60 | line 4211 | ENTITY | Livekeeping Technologies Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2621 | page 60 | line 4214 | ENTITY | Busy Infotech Private Limited ( Formerly Known as Tolexo) | [I3] named entity with figures, stand note 30 RPT balances
R2622 | page 60 | line 4215 | ENTITY | Livekeeping Technologies Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2623 | page 60 | line 4216 | ENTITY | IIL Digital Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2624 | page 60 | line 4201 | ENTITY | IndiaMart Finance Limited | [I3] named entity with figures, stand note 30 RPT balances
R2625 | page 60 | line 4220 | ENTITY | S R Dinodia & Co LLP | [I3] named entity with figures, stand note 30 RPT balances
R2626 | page 60 | line 4221 | ENTITY | Mansa Enterprises Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2627 | page 60 | line 4222 | ENTITY | IIL Digital Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2628 | page 60 | line 4226 | ENTITY | Busy Infotech Private Limited(Formerly Known as Tolexo) | [I3] named entity with figures, stand note 30 RPT balances
R2629 | page 60 | line 4205 | ENTITY | IB Monotaro Private Limited | [I3] named entity with figures, stand note 30 RPT balances
R2630 | page 60 | line 4228 | ENTITY | Simply Vyapar Apps Private Limited | [I3] named entity with figures, stand note 30 RPT balances

## FORWARD TABLE (5 rows)

R2631 | page 4 | line 166 | FORWARD | future events or conditions may cause the Group and its associates to cease to continue as a going concern | [I5] consolidated auditor responsibility text
R2632 | page 34 | line 2458 | FORWARD | future events or conditions may cause the Company to cease to continue as a going concern | [I5] standalone auditor responsibility text
R2633 | page 17 | line 1180 | FORWARD | (iii) During the period the Group has given INR 172.47 to various shareholders of Agillos E-Commerce Pvt. Ltd. for transfer of its equity shares. Subsequently on 5 October 2026, such shares have been transferred in the name of the | [I2] cons note 7 associates statement
R2634 | page 27 | line 1937 | FORWARD | iii) Fair value of quoted mutual funds, exchange traded fund, investment trust and government securities is based on quoted market prices at the reporting date. We do not expect material volatility in these financial assets. | [I2] cons note 28 fair value statement
R2635 | page 56 | line 3954 | FORWARD | iii) Fair value of quoted mutual funds, exchange traded funds, investment trust and government securities is based on quoted market prices at the reporting date. We do not expect material volatility in these | [I2] stand note 28 fair value statement

## DATE TABLE (94 rows)

R2636 | page 2 | line 77 | DATE | 30 September 2026 | [I5] in consolidated auditor para
R2637 | page 2 | line 106 | DATE | October 14, 2013 | [I5] in consolidated auditor para
R2638 | page 4 | line 203 | DATE | 30 September 2026 | [I5] in consolidated auditor para
R2639 | page 4 | line 215 | DATE | 30 September 2026 | [I5] in consolidated auditor para
R2640 | page 4 | line 215 | DATE | 1 April 2026 | [I5] in consolidated auditor para
R2641 | page 4 | line 215 | DATE | 29 May 2026 | [I5] in consolidated auditor para
R2642 | page 5 | line 246 | DATE | 27 October 2026 | [I5] in consolidated auditor para
R2643 | page 33 | line 2370 | DATE | 30 September 2026 | [I5] in standalone auditor para
R2644 | page 33 | line 2405 | DATE | October 14, 2013 | [I5] in standalone auditor para
R2645 | page 35 | line 2478 | DATE | 27 October 2026 | [I5] in standalone auditor para
R2646 | page 24 | line 1691 | DATE | 30 September 2026 | [I1] period column header, cons note 20 other income
R2647 | page 24 | line 1691 | DATE | 30 September 2025 | [I1] period column header, cons note 20 other income
R2648 | page 53 | line 3742 | DATE | 30 September 2026 | [I1] period column header, stand note 20 other income
R2649 | page 53 | line 3747 | DATE | 30 September 2025 | [I1] period column header, stand note 20 other income
R2650 | page 53 | line 3747 | DATE | September 2025 | [I1] period column header, stand note 20 other income
R2651 | page 17 | line 1087 | DATE | 30 September 2026 | [I2] period column header, cons note 7 associates
R2652 | page 17 | line 1087 | DATE | 31 March 2026 | [I2] period column header, cons note 7 associates
R2653 | page 17 | line 1180 | DATE | 5 October 2026 | [I2] in: (iii) During the period the Group has gi
R2654 | page 17 | line 1183 | DATE | 30 September 2026 | [I2] in: (iv) During the period ended 30 Septembe
R2655 | page 18 | line 1187 | DATE | 30 September 2026 | [I2] period column header, cons note 8a non-current inv
R2656 | page 18 | line 1193 | DATE | 31 March 2026 | [I2] period column header, cons note 8a non-current inv
R2657 | page 19 | line 1287 | DATE | 30 September 2026 | [I2] period column header, cons note 8b current inv
R2658 | page 19 | line 1296 | DATE | 31 March 2026 | [I2] period column header, cons note 8b current inv
R2659 | page 20 | line 1445 | DATE | 30 September 2026 | [I2] period column header, cons note 8c/d loans, other fin assets
R2660 | page 20 | line 1453 | DATE | 31 March 2026 | [I2] period column header, cons note 8c/d loans, other fin assets
R2661 | page 27 | line 1878 | DATE | 30 September 2026 | [I2] period column header, cons note 28 fair value
R2662 | page 27 | line 1887 | DATE | 31 March 2026 | [I2] period column header, cons note 28 fair value
R2663 | page 27 | line 1955 | DATE | 11 April 2025 | [I2] in: Fleetx Technologies Private Limited (til
R2664 | page 27 | line 1956 | DATE | 29 May 2026 | [I2] in: Monotaro Private Ltd. (w.e.f 29 May 2026
R2665 | page 27 | line 1963 | DATE | 30 September 2025 | [I2] period column header, cons note 28 fair value
R2666 | page 27 | line 1971 | DATE | 30 September 2025 | [I2] in: During the period ended 30 September 202
R2667 | page 27 | line 1971 | DATE | 30 September 2026 | [I2] in: During the period ended 30 September 202
R2668 | page 27 | line 1958 | DATE | 30 September 2026 | [I2] in: Considering the nature of investments, t
R2669 | page 27 | line 1945 | DATE | 30 September 2026 | [I2] in: Following table describes the valuation 
R2670 | page 46 | line 3162 | DATE | 31 March 2026 | [I2] period column header, stand note 7 subs+assoc
R2671 | page 46 | line 3156 | DATE | 30 September 2026 | [I2] period column header, stand note 7 subs+assoc
R2672 | page 47 | line 3263 | DATE | 30 September 2026 | [I2] period column header, stand note 8a non-current inv
R2673 | page 47 | line 3281 | DATE | 31 March 2026 | [I2] period column header, stand note 8a non-current inv
R2674 | page 47 | line 3268 | DATE | 30 September 2026 | [I2] in: ii) During the period ended 30 September
R2675 | page 47 | line 3274 | DATE | 30 September 2026 | [I2] in: v). The Company had invested in 7,870,00
R2676 | page 47 | line 3277 | DATE | 30 September 2026 | [I2] in: vii) During the period ended 30 Septembe
R2677 | page 47 | line 3269 | DATE | 30 September 2026 | [I2] in: iii) During the period ended 30 Septembe
R2678 | page 47 | line 3269 | DATE | 4 August 2026 | [I2] in: iii) During the period ended 30 Septembe
R2679 | page 47 | line 3271 | DATE | 30 September 2026 | [I2] in: iv) During the period ended 30 September
R2680 | page 47 | line 3267 | DATE | 30 September 2026 | [I2] in: i) During the period ended 30 September 
R2681 | page 48 | line 3359 | DATE | 30 September 2026 | [I2] period column header, stand note 8b current inv
R2682 | page 48 | line 3359 | DATE | 31 March 2026 | [I2] period column header, stand note 8b current inv
R2683 | page 49 | line 3461 | DATE | 30 September 2026 | [I2] period column header, stand note 8 loans, other fin assets
R2684 | page 49 | line 3461 | DATE | 31 March 2026 | [I2] period column header, stand note 8 loans, other fin assets
R2685 | page 49 | line 3485 | DATE | 31 March 2026 | [I2] in: ^ Includes interest accrued of INR 63.01
R2686 | page 49 | line 3502 | DATE | 31 March 2026 | [I2] in: **Includes interest accrued of INR 45.39
R2687 | page 56 | line 3910 | DATE | 30 September 2026 | [I2] period column header, stand note 28 fair value
R2688 | page 56 | line 3918 | DATE | 31 March 2026 | [I2] period column header, stand note 28 fair value
R2689 | page 57 | line 3976 | DATE | 11 April 2025 | [I2] in: Technologies Private Limited (till 11 Ap
R2690 | page 57 | line 3977 | DATE | 29 May 2026 | [I2] in: (w.e.f 29 May 2026) and Baldor Technolog
R2691 | page 57 | line 3963 | DATE | 30 September 2026 | [I2] period column header, stand note 28 fair value level 3
R2692 | page 57 | line 3998 | DATE | 30 September 2025 | [I2] period column header, stand note 28 fair value level 3
R2693 | page 57 | line 4024 | DATE | 30 September 2026 | [I2] in: During the period ended 30 September 202
R2694 | page 57 | line 4024 | DATE | 30 September 2025 | [I2] in: During the period ended 30 September 202
R2695 | page 57 | line 3968 | DATE | 30 September 2026 | [I2] in: Following table describes the valuation 
R2696 | page 29 | line 2124 | DATE | 29 June 2026 | [I3] in: Dhruv Prakash Non-Executive Director (up
R2697 | page 29 | line 2125 | DATE | 23 September 2025 | [I3] in: Rajesh Sawhney Independent Director (upt
R2698 | page 29 | line 2130 | DATE | 29 April 2025 | [I3] in: Sandeep Barasiya Independent Director (w
R2699 | page 29 | line 2131 | DATE | 18 July 2025 | [I3] in: Vasuta Agarwal Independent Director (wit
R2700 | page 29 | line 2096 | DATE | 30 September 2026 | [I3] period column header, cons note 30 RPT list
R2701 | page 29 | line 2164 | DATE | 30 September 2025 | [I3] period column header, cons note 30 RPT list
R2702 | page 29 | line 2107 | DATE | 04 August 2026 | [I3] in: Indiamart Finance Limited (incorporated 
R2703 | page 29 | line 2106 | DATE | 27 August 2024 | [I3] in: IIL Digital Private Limited (incorporate
R2704 | page 29 | line 2161 | DATE | 01 November 2025 | [I3] in: ^ Transactions from 01 November 2025
R2705 | page 29 | line 2111 | DATE | 11 April 2025 | [I3] in: Fleetx Technologies Private Limited (wit
R2706 | page 29 | line 2114 | DATE | 29 May 2026 | [I3] in: IB Monotaro Private Limited (upto 29 May
R2707 | page 30 | line 2174 | DATE | 30 September 2026 | [I3] period column header, cons note 30 RPT transactions
R2708 | page 30 | line 2182 | DATE | 30 September 2025 | [I3] period column header, cons note 30 RPT transactions
R2709 | page 31 | line 2230 | DATE | 30 September 2026 | [I3] period column header, cons note 30 RPT balances
R2710 | page 31 | line 2237 | DATE | 31 March 2026 | [I3] period column header, cons note 30 RPT balances
R2711 | page 58 | line 4041 | DATE | 04 August 2026 | [I3] in: IndiaMart Finance Limited (incorporated 
R2712 | page 58 | line 4044 | DATE | 29 May 2026 | [I3] in: IB Monotaro Private Limited (till 29 May
R2713 | page 58 | line 4046 | DATE | 11 April 2025 | [I3] in: Fleetx Technologies Private Limited (wit
R2714 | page 58 | line 4051 | DATE | 29 June 2026 | [I3] in: Dhruv Prakash Non-Executive Director (Up
R2715 | page 58 | line 4052 | DATE | 23 September 2025 | [I3] in: Rajesh Sawhney Independent Director (Upt
R2716 | page 58 | line 4057 | DATE | 29 April 2025 | [I3] in: Sandeep Barasiya Independent Director (w
R2717 | page 58 | line 4058 | DATE | 18 July 2025 | [I3] in: Vasuta Agarwal Independent Director (wit
R2718 | page 58 | line 4027 | DATE | 30 September 2026 | [I3] period column header, stand note 30 RPT list
R2719 | page 58 | line 4092 | DATE | 30 September 2025 | [I3] period column header, stand note 30 RPT list
R2720 | page 58 | line 4089 | DATE | 01 November 2025 | [I3] in: ^ Transactions from 01 November 2025
R2721 | page 59 | line 4100 | DATE | 30 September 2026 | [I3] period column header, stand note 30 RPT transactions
R2722 | page 59 | line 4107 | DATE | 30 September 2025 | [I3] period column header, stand note 30 RPT transactions
R2723 | page 60 | line 4178 | DATE | 30 September 2026 | [I3] period column header, stand note 30 RPT balances
R2724 | page 60 | line 4185 | DATE | 31 March 2026 | [I3] period column header, stand note 30 RPT balances
R2725 | page 60 | line 4201 | DATE | 04 August 2026 | [I3] in: IndiaMart Finance Limited (incorporated 
R2726 | page 20 | line 1453 | DATE | 30 September 2026 | [I4] period column header, cons note 9 other assets
R2727 | page 20 | line 1476 | DATE | 31 March 2026 | [I4] period column header, cons note 9 other assets
R2728 | page 49 | line 3473 | DATE | 30 September 2026 | [I4] period column header, stand note 11 other assets
R2729 | page 49 | line 3473 | DATE | 31 March 2026 | [I4] period column header, stand note 11 other assets

## QUALIFIER TABLE (436 rows)

R2730 | page 2 | line 62 | QUALIFIER | B S R & Co. LLP Building No. 10, 12th Floor, Tower-C DLF Cyber Chartered Accountants City, Phase - II Gurugram - 122 002, India Tel: +91 124 719 1000 Fax: +91 124 719 8613 | [I5] consolidated auditor report paragraph (lines 62-67)
R2731 | page 2 | line 69 | QUALIFIER | Independent Auditor's Report | [I5] consolidated auditor report paragraph (lines 69-69)
R2732 | page 2 | line 71 | QUALIFIER | To the Board of Directors of IndiaMART InterMESH Limited | [I5] consolidated auditor report paragraph (lines 71-71)
R2733 | page 2 | line 73 | QUALIFIER | Report on the Audit of the Condensed Consolidated Interim Financial Statements | [I5] consolidated auditor report paragraph (lines 73-73)
R2734 | page 2 | line 75 | QUALIFIER | Opinion | [I5] consolidated auditor report paragraph (lines 75-75)
R2735 | page 2 | line 77 | QUALIFIER | We have audited the condensed consolidated interim financial statements of IndiaMART InterMESH Limited (hereinafter referred to as the "Holding Company") and its subsidiaries (Holding Company and its subsidiaries together referred to as "the Group"), and its associates, which comprise the condensed consolidated interim Balance Sheet as at 30 September 2026, condensed consolidated interim statement of Profit and Loss (including other comprehensive income) for the quarter and year-to-date period then ended, condensed consolidated interim statement of changes in equity, condensed consolidated interim statement of cash flows for the year-to-date period then ended, and notes to the condensed consolidated interim financial statements, including material accounting policies and other explanatory information as required by Indian Accounting Standard (Ind AS) 34 "Interim Financial Reporting" and other accounting principles generally accepted in India (hereinafter referred to as "the condensed consolidated interim financial statements"). | [I5] consolidated auditor report paragraph (lines 77-87)
R2736 | page 2 | line 89 | QUALIFIER | In our opinion and to the best of our information and according to the explanations given to us, the aforesaid condensed consolidated interim financial statements are prepared, in all material respects, in accordance with Ind AS 34 and other accounting principles generally accepted in India. | [I5] consolidated auditor report paragraph (lines 89-91)
R2737 | page 2 | line 93 | QUALIFIER | Basis for Opinion | [I5] consolidated auditor report paragraph (lines 93-93)
R2738 | page 2 | line 95 | QUALIFIER | We conducted our audit in accordance with the Standards on Auditing (SAs) specified under section 143(10) of the Companies Act, 2013 ("Act"). Our responsibilities under those Standards are further described in the Auditor's Responsibilities for the Audit of the Condensed Consolidated Interim Financial Statements section of our report. We are independent of the Group, and its associates in accordance with the ethical requirements that are relevant to our audit of the condensed consolidated interim financial statements in terms of the Code of Ethics issued by the Institute of Chartered Accountants of India and the relevant provisions of the Act, and we have fulfilled our other ethical responsibilities in accordance with these requirements. We believe that the audit evidence obtained by us along with the consideration of reports of other auditors referred to in paragraph (a) of the "Other Matters" section below, is sufficient and appropriate to provide a basis for our opinion on the condensed consolidated interim financial statements. | [I5] consolidated auditor report paragraph (lines 95-104)
R2739 | page 2 | line 106 | QUALIFIER | B S R & Co. (a partnership firm with Registration No. BA61223) converted into B S R & Co. LLP Registered Office: (a Limited Liability Partnership with LLP Registration No. AAB-8181) with effect from October 14, 2013 14th Floor, Central B Wing and North C Wing, Nesco IT Park 4, Nesco Center, Western Express Highway, Goregaon (East), Mumbai - 400063 | [I5] consolidated auditor report paragraph (lines 106-110)
R2740 | page 3 | line 112 | QUALIFIER | B S R & Co. LLP | [I5] consolidated auditor report page header (firm name)
R2741 | page 3 | line 114 | QUALIFIER | Management's and Board of Directors' Responsibilities for the Condensed Consolidated Interim Financial Statements | [I5] consolidated auditor report paragraph (lines 114-115)
R2742 | page 3 | line 117 | QUALIFIER | The Holding Company's Management and Board of Directors are responsible for the preparation and presentation of these condensed consolidated interim financial statements in accordance with Ind AS 34 prescribed under section 133 of the Act and other accounting principles generally accepted in India. The respective Management and Board of Directors of the companies included in the Group and of its associates are responsible for maintenance of adequate accounting records in accordance with the provisions of the Act for safeguarding of the assets of each company and for preventing and detecting frauds and other irregularities; the selection and application of appropriate accounting policies; making judgments and estimates that are reasonable and prudent; and the design, implementation and maintenance of adequate internal financial controls, that were operating effectively for ensuring accuracy and completeness of the accounting records, relevant to the preparation and presentation of the condensed consolidated interim financial statements that are free from material misstatement, whether due to fraud or error, which have been used for the purpose of preparation of the condensed consolidated interim financial statements by the Management and Board of Directors of the Holding Company, as aforesaid. | [I5] consolidated auditor report paragraph (lines 117-129)
R2743 | page 3 | line 131 | QUALIFIER | In preparing the condensed consolidated interim financial statements, the respective Management and Board of Directors of the companies included in the Group and of its associates, are responsible for assessing the ability of each company to continue as a going concern, disclosing, as applicable, matters related to going concern and using the going concern basis of accounting unless the respective Board of Directors either intends to liquidate the Company or to cease operations, or has no realistic alternative but to do so. | [I5] consolidated auditor report paragraph (lines 131-135)
R2744 | page 3 | line 137 | QUALIFIER | The respective Board of Directors of the companies included in the Group and of its associates are responsible for overseeing the financial reporting process of each company. | [I5] consolidated auditor report paragraph (lines 137-138)
R2745 | page 3 | line 140 | QUALIFIER | Auditor's Responsibilities for the Audit of the Condensed Consolidated Interim Financial Statements | [I5] consolidated auditor report paragraph (lines 140-140)
R2746 | page 3 | line 142 | QUALIFIER | Our objectives are to obtain reasonable assurance about whether the condensed consolidated interim financial statements as a whole are free from material misstatement, whether due to fraud or error, and to issue an auditor's report that includes our opinion. Reasonable assurance is a high level of assurance, but is not a guarantee that an audit conducted in accordance with SAs will always detect a material misstatement when it exists. Misstatements can arise from fraud or error and are considered material if, individually or in the aggregate, they could reasonably be expected to influence the economic decisions of users taken on the basis of these condensed consolidated interim financial statements. | [I5] consolidated auditor report paragraph (lines 142-148)
R2747 | page 3 | line 150 | QUALIFIER | As part of an audit in accordance with SAs, we exercise professional judgment and maintain professional skepticism throughout the audit. We also: | [I5] consolidated auditor report paragraph (lines 150-151)
R2748 | page 3 | line 153 | QUALIFIER | x Identify and assess the risks of material misstatement of the condensed consolidated interim financial statements, whether due to fraud or error, design and perform audit procedures responsive to those risks, and obtain audit evidence that is sufficient and appropriate to provide a basis for our opinion. The risk of not detecting a material misstatement resulting from fraud is higher than for one resulting from error, as fraud may involve collusion, forgery, intentional omissions, misrepresentations, or the override of internal control. | [I5] consolidated auditor report paragraph (lines 153-158)
R2749 | page 3 | line 160 | QUALIFIER | x Obtain an understanding of internal control relevant to the audit in order to design audit procedures that are appropriate in the circumstances, but not for the purpose of expressing opinion on the effectiveness of the Group's internal control. | [I5] consolidated auditor report paragraph (lines 160-162)
R2750 | page 3 | line 164 | QUALIFIER | x Evaluate the appropriateness of accounting policies used and the reasonableness of accounting estimates and related disclosures made by the Management and Board of Directors. | [I5] consolidated auditor report paragraph (lines 164-165)
R2751 | page 4 | line 167 | QUALIFIER | B S R & Co. LLP | [I5] consolidated auditor report page header (firm name)
R2752 | page 4 | line 169 | QUALIFIER | x Conclude on the appropriateness of the Management and Board of Directors use of the going concern basis of accounting in preparation of condensed consolidated interim financial statements and, based on the audit evidence obtained, whether a material uncertainty exists related to events or conditions that may cast significant doubt on appropriateness of this assumption. If we conclude that a material uncertainty exists, we are required to draw attention in our auditor's report to the related disclosures in the condensed consolidated interim financial statements or, if such disclosures are inadequate, to modify our opinion. Our conclusions are based on the audit evidence obtained up to the date of our auditor's report. However, future events or conditions may cause the Group and its associates to cease to continue as a going concern. | [I5] consolidated auditor report paragraph (lines 169-176)
R2753 | page 4 | line 178 | QUALIFIER | x Evaluate the overall presentation, structure and content of the condensed consolidated interim financial statements, including the disclosures, and whether the condensed consolidated interim financial statements represent the underlying transactions and events in a manner that is in accordance with Ind AS 34. | [I5] consolidated auditor report paragraph (lines 178-180)
R2754 | page 4 | line 182 | QUALIFIER | x Obtain sufficient appropriate audit evidence regarding the condensed consolidated interim financial statements of such entities or business activities within the Group and its associates to express an opinion on the condensed consolidated interim financial statements. We are responsible for the direction, supervision and performance of the audit of condensed consolidated interim financial statements of such entities included in the condensed consolidated interim financial statements of which we are the independent auditors. For the other entities included in the condensed consolidated interim financial statements, which have been audited by other auditors, such other auditors remain responsible for the direction, supervision and performance of the audits carried out by them. We remain solely responsible for our audit opinion. Our responsibilities in this regard are further described in para (a) of the section titled `Other Matters' in this audit report. | [I5] consolidated auditor report paragraph (lines 182-191)
R2755 | page 4 | line 193 | QUALIFIER | We communicate with those charged with governance of the Holding Company regarding, among other matters, the planned scope and timing of the audit and significant audit findings, including any significant deficiencies in internal control that we identify during our audit. | [I5] consolidated auditor report paragraph (lines 193-195)
R2756 | page 4 | line 197 | QUALIFIER | We also provide those charged with governance with a statement that we have complied with relevant ethical requirements regarding independence, and to communicate with them all relationships and other matters that may reasonably be thought to bear on our independence, and where applicable, related safeguards. | [I5] consolidated auditor report paragraph (lines 197-199)
R2757 | page 4 | line 201 | QUALIFIER | Other Matters | [I5] consolidated auditor report paragraph (lines 201-201)
R2758 | page 4 | line 203 | QUALIFIER | (a) We did not audit the condensed interim financial statements of five subsidiaries, whose condensed interim financial statements reflect total assets (before consolidation adjustments) of Rs. 2,160.49 million as at 30 September 2026, total revenue (before consolidation adjustments) of Rs. 31.76 million and Rs. 59.01 million, for the quarter ended 30 September 2026 and year-to-date period ended 30 September 2026 respectively, and net cash inflows (before consolidation adjustments) of Rs. 41.44 million for the year-to-date period ended 30 September 2026, as considered in the condensed consolidated interim financial. These condensed interim financial statements have been audited by other auditors whose reports have been furnished to us by the Management and our opinion on the condensed consolidated interim financial statements, in so far as it relates to the amounts and disclosures included in respect of these subsidiaries is based solely on the reports of the other auditors. | [I5] consolidated auditor report paragraph (lines 203-213)
R2759 | page 4 | line 215 | QUALIFIER | (b) The condensed consolidated interim financial statements also include the Group's share of net loss of Rs. 153.60 million and Rs. 281.44 million for the quarter and year-to-date period ended 30 September 2026, respectively, as considered in the condensed consolidated interim financial statements, in respect of seven associates, whose condensed interim financial information has not been audited either by us or by other auditors. Further, the condensed consolidated interim financial statements include the Group's share of net loss of Rs. 17.69 million for the period from 1 April 2026 to 29 May 2026, in respect of one associate, whose financial information has not been audited either by us or other auditors. These unaudited condensed interim financial information have been furnished to us by the Management and our opinion on the condensed consolidated interim financial statements, insofar as it relates to the amounts and disclosures included in respect of these associates, | [I5] consolidated auditor report paragraph (lines 215-224)
R2760 | page 5 | line 226 | QUALIFIER | B S R & Co. LLP is based solely on such unaudited condensed interim financial information. In our opinion and according to the information and explanations given to us by the Management, these unaudited condensed interim financial information are not material to the Group. | [I5] consolidated auditor report paragraph (lines 226-229)
R2761 | page 5 | line 231 | QUALIFIER | Our opinion on the condensed consolidated interim financial statements is not modified in respect of the above matters with respect to our reliance on the work done and the reports of the other auditors and the condensed interim financial information certified by the Management. | [I5] consolidated auditor report paragraph (lines 231-233)
R2762 | page 5 | line 235 | QUALIFIER | For B S R & Co. LLP Chartered Accountants Firm's Registration No. 101248W/W-100022 | [I5] consolidated auditor report paragraph (lines 235-237)
R2763 | page 5 | line 239 | QUALIFIER | Digitally signed by | [I5] consolidated auditor report paragraph (lines 239-239)
R2764 | page 5 | line 241 | QUALIFIER | DAVID JULIAN DAVID JULIAN JONES | [I5] consolidated auditor report paragraph (lines 241-241)
R2765 | page 5 | line 243 | QUALIFIER | JONES Date: 2026.10.27 13:13:17 +05'30' | [I5] consolidated auditor report paragraph (lines 243-244)
R2766 | page 5 | line 246 | QUALIFIER | Place: Gurugram David Jones Date: 27 October 2026 Partner | [I5] consolidated auditor report paragraph (lines 246-247)
R2767 | page 5 | line 249 | QUALIFIER | Membership No. 098113 UDIN: 26098113SRBTOZ2829 | [I5] consolidated auditor report paragraph (lines 249-250)
R2768 | page 33 | line 2355 | QUALIFIER | B S R & Co. LLP Building No. 10, 12th Floor, Tower-C DLF Cyber City, Chartered Accountants Phase - II Gurugram - 122 002, India Tel: +91 124 719 1000 Fax: +91 124 719 8613 | [I5] standalone auditor report paragraph (lines 2355-2360)
R2769 | page 33 | line 2362 | QUALIFIER | Independent Auditors Report | [I5] standalone auditor report paragraph (lines 2362-2362)
R2770 | page 33 | line 2364 | QUALIFIER | To the Board of Directors of IndiaMART InterMESH Limited | [I5] standalone auditor report paragraph (lines 2364-2364)
R2771 | page 33 | line 2366 | QUALIFIER | Report on the Audit of the Condensed Standalone Interim Financial Statements | [I5] standalone auditor report paragraph (lines 2366-2366)
R2772 | page 33 | line 2368 | QUALIFIER | Opinion | [I5] standalone auditor report paragraph (lines 2368-2368)
R2773 | page 33 | line 2370 | QUALIFIER | We have audited the condensed standalone interim financial statements of IndiaMART InterMESH Limited (the Company), which comprise the condensed standalone interim balance sheet as at 30 September 2026, the condensed standalone interim statement of profit and loss (including other comprehensive income) for the quarter and year to date period then ended, the condensed standalone interim statement of changes in equity and the condensed standalone interim statement of cash flows for the year-to-date then ended, and notes to the condensed standalone interim financial statements, including material accounting policies and other explanatory information, as required by Indian Accounting Standard (Ind AS) 34 Interim Financial Reporting and other accounting principles generally accepted in India. | [I5] standalone auditor report paragraph (lines 2370-2377)
R2774 | page 33 | line 2379 | QUALIFIER | In our opinion and to the best of our information and according to the explanations given to us, the aforesaid condensed standalone interim financial statements are prepared, in all material respects, in accordance with Ind AS 34 and other accounting principles generally accepted in India. | [I5] standalone auditor report paragraph (lines 2379-2381)
R2775 | page 33 | line 2383 | QUALIFIER | Basis for Opinion | [I5] standalone auditor report paragraph (lines 2383-2383)
R2776 | page 33 | line 2385 | QUALIFIER | We conducted our audit in accordance with the Standards on Auditing (SAs) specified under Section 143(10) of the Companies Act, 2013 (Act). Our responsibilities under those SAs are further described in the Auditors Responsibilities for the Audit of the Condensed Standalone Interim Financial Statements section of our report. We are independent of the Company in accordance with the Code of Ethics issued by the Institute of Chartered Accountants of India together with the ethical requirements that are relevant to our audit of the condensed standalone interim financial statements under the provisions of the Act, and the Rules thereunder, and we have fulfilled our other ethical responsibilities in accordance with these requirements and the Code of Ethics. We believe that the audit evidence obtained by us, is sufficient and appropriate to provide a basis for our opinion on the condensed standalone interim financial statements. | [I5] standalone auditor report paragraph (lines 2385-2393)
R2777 | page 33 | line 2395 | QUALIFIER | Management's and Board of Directors Responsibilities for the Condensed Standalone Interim Financial Statements | [I5] standalone auditor report paragraph (lines 2395-2396)
R2778 | page 33 | line 2398 | QUALIFIER | The Companys Management and Board of Directors are responsible for the preparation and presentation of these condensed standalone interim financial statements in accordance with Ind AS 34 prescribed under section 133 of the Act and other accounting principles generally accepted in India. This responsibility also includes maintenance of adequate accounting records in accordance with the provisions of the Act for safeguarding of the assets of the Company and for preventing and detecting frauds and other irregularities; selection and application of appropriate accounting policies; making judgments and estimates that are | [I5] standalone auditor report paragraph (lines 2398-2403)
R2779 | page 33 | line 2405 | QUALIFIER | B S R & Co. (a partnership firm with Registration No. BA61223) converted into B S R & Co. LLP Registered Office: (a Limited Liability Partnership with LLP Registration No. AAB-8181) with effect from October 14, 2013 14th Floor, Central B Wing and North C Wing, Nesco IT Park 4, Nesco Center, Western Express 1 Highway, Goregaon (East), Mumbai - 400063 | [I5] standalone auditor report paragraph (lines 2405-2409)
R2780 | page 34 | line 2411 | QUALIFIER | B S R & Co. LLP | [I5] standalone auditor report page header (firm name)
R2781 | page 34 | line 2413 | QUALIFIER | reasonable and prudent; and design, implementation and maintenance of adequate internal financial controls that were operating effectively for ensuring the accuracy and completeness of the accounting records, relevant to the preparation and presentation of the condensed standalone interim financial statements, which are free from material misstatement, whether due to fraud or error. | [I5] standalone auditor report paragraph (lines 2413-2416)
R2782 | page 34 | line 2418 | QUALIFIER | In preparing the condensed standalone interim financial statements, the Management and Board of Directors are responsible for assessing the Companys ability to continue as a going concern, disclosing, as applicable, matters related to going concern and using the going concern basis of accounting unless the Board of Directors either intends to liquidate the Company or to cease operations, or has no realistic alternative but to do so. | [I5] standalone auditor report paragraph (lines 2418-2421)
R2783 | page 34 | line 2423 | QUALIFIER | The Board of Directors is also responsible for overseeing the Companys financial reporting process. | [I5] standalone auditor report paragraph (lines 2423-2423)
R2784 | page 34 | line 2425 | QUALIFIER | Auditors Responsibilities for the Audit of the Condensed Standalone Interim Financial Statements | [I5] standalone auditor report paragraph (lines 2425-2425)
R2785 | page 34 | line 2427 | QUALIFIER | Our objectives are to obtain reasonable assurance about whether the condensed standalone interim financial statements as a whole are free from material misstatement, whether due to fraud or error, and to issue an auditors report that includes our opinion. Reasonable assurance is a high level of assurance, but is not a guarantee that an audit conducted in accordance with SAs will always detect a material misstatement when it exists. Misstatements can arise from fraud or error and are considered material if, individually or in the aggregate, they could reasonably be expected to influence the economic decisions of users taken on the basis of these condensed standalone interim financial statements. As part of an audit in accordance with SAs, we exercise professional judgment and maintain professional skepticism throughout the audit. We also: | [I5] standalone auditor report paragraph (lines 2427-2435)
R2786 | page 34 | line 2437 | QUALIFIER | Identify and assess the risks of material misstatement of the condensed standalone interim financial statements, whether due to fraud or error, design and perform audit procedures responsive to those risks, and obtain audit evidence that is sufficient and appropriate to provide a basis for our opinion. The risk of not detecting a material misstatement resulting from fraud is higher than for one resulting from error, as fraud may involve collusion, forgery, intentional omissions, misrepresentations, or the override of internal control. | [I5] standalone auditor report paragraph (lines 2437-2442)
R2787 | page 34 | line 2444 | QUALIFIER | Obtain an understanding of internal control relevant to the audit in order to design audit procedures that are appropriate in the circumstances, but not for the purpose of expressing opinion on the effectiveness of the entitys internal control. | [I5] standalone auditor report paragraph (lines 2444-2446)
R2788 | page 34 | line 2448 | QUALIFIER | Evaluate the appropriateness of accounting policies used and the reasonableness of accounting estimates and related disclosures made by the Management and Board of Directors. | [I5] standalone auditor report paragraph (lines 2448-2449)
R2789 | page 34 | line 2451 | QUALIFIER | Conclude on the appropriateness of the Management and Board of Directors use of the going concern basis of accounting in the preparation of condensed standalone interim financial statements and, based on the audit evidence obtained, whether a material uncertainty exists related to events or conditions that may cast significant doubt on the Companys ability to continue as a going concern. If we conclude that a material uncertainty exists, we are required to draw attention in our auditors report to the related disclosures in the condensed standalone interim financial statements or, if such disclosures are inadequate, to modify our opinion. Our conclusions are based on the audit evidence obtained up to the date of our auditors report. However, future events or conditions may cause the Company to cease to continue as a going concern. | [I5] standalone auditor report paragraph (lines 2451-2458)
R2790 | page 34 | line 2460 | QUALIFIER | Evaluate the overall presentation, structure and content of the condensed standalone interim financial statements, including the disclosures, and whether the condensed standalone interim financial statements represent the underlying transactions and events in a manner that is in accordance with Ind AS 34. | [I5] standalone auditor report paragraph (lines 2460-2462)
R2791 | page 35 | line 2464 | QUALIFIER | B S R & Co. LLP | [I5] standalone auditor report page header (firm name)
R2792 | page 35 | line 2466 | QUALIFIER | We communicate with those charged with governance regarding, among other matters, the planned scope and timing of the audit and significant audit findings, including any significant deficiencies in internal control that we identify during our audit. | [I5] standalone auditor report paragraph (lines 2466-2468)
R2793 | page 35 | line 2470 | QUALIFIER | We also provide those charged with governance with a statement that we have complied with relevant ethical requirements regarding independence, and to communicate with them all relationships and other matters that may reasonably be thought to bear on our independence, and where applicable, related safeguards. | [I5] standalone auditor report paragraph (lines 2470-2472)
R2794 | page 35 | line 2474 | QUALIFIER | For B S R & Co. LLP Chartered Accountants Firm's Registration No. 101248W/W-100022 | [I5] standalone auditor report paragraph (lines 2474-2476)
R2795 | page 35 | line 2478 | QUALIFIER | Place: Gurugram David Jones Date: 27 October 2026 Partner | [I5] standalone auditor report paragraph (lines 2478-2479)
R2796 | page 35 | line 2481 | QUALIFIER | Membership No. 098113 UDIN: 26098113AYOEGP5632 | [I5] standalone auditor report paragraph (lines 2481-2482)
R2797 | page 5 | line 229 | QUALIFIER | unaudited associate information: "In our opinion ... not material to the Group" | [I5] consolidated other matter (b) qualifier; mgmt-furnished, unaudited
R2798 | page 5 | line 231 | QUALIFIER | opinion "is not modified" in respect of other-auditor reliance and management-certified information | [I5] consolidated other matter closing
R2799 | page 4 | line 203 | QUALIFIER | opinion on these subsidiaries "based solely on the reports of the other auditors" | [I5] consolidated other matter (a) reliance
R2800 | page 33 | line 2366 | QUALIFIER | standalone report contains no paragraph headed "Other Matters" in the extracted text (grep check of lines 2330-2560) | [I5] mechanical check, standalone
R2801 | page 24 | line 1716 | QUALIFIER | 20 Other income | [I1] cons note 20 other income heading/qualifier
R2802 | page 24 | line 1718 | QUALIFIER | Fair value gain/(loss) on measurement and income from sale of financial assets | [I1] cons note 20 other income note/text
R2803 | page 24 | line 1719 | QUALIFIER | -Fair value gain/(loss) (net) on measurement, interest and income | [I1] cons note 20 other income heading/qualifier
R2804 | page 24 | line 1720 | QUALIFIER | from sale of mutual funds, exchange traded funds, bonds, | [I1] cons note 20 other income heading/qualifier
R2805 | page 24 | line 1721 | QUALIFIER | debentures and investment trust | [I1] cons note 20 other income heading/qualifier
R2806 | page 24 | line 1723 | QUALIFIER | Interest income from financial assets measured at amortised cost | [I1] cons note 20 other income heading/qualifier
R2807 | page 53 | line 3746 | QUALIFIER | 20 Other income | [I1] stand note 20 other income heading/qualifier
R2808 | page 53 | line 3749 | QUALIFIER | Fair value gain/(loss) on measurement and income from sale of financial assets | [I1] stand note 20 other income note/text
R2809 | page 53 | line 3750 | QUALIFIER | -Fair value gain/(loss) (net) on measurement, interest and income from sale of | [I1] stand note 20 other income note/text
R2810 | page 53 | line 3751 | QUALIFIER | mutual funds, exchange traded funds, bonds, debentures and investment trust | [I1] stand note 20 other income note/text
R2811 | page 53 | line 3752 | QUALIFIER | (refer note 7(iv)) | [I1] cross-reference in: -Fair value loss on measurement of Inves
R2812 | page 53 | line 3753 | QUALIFIER | Interest income from financial assets measured at amortised cost | [I1] stand note 20 other income heading/qualifier
R2813 | page 53 | line 3758 | QUALIFIER | (refer note 16) | [I1] cross-reference in: Liabilities and provisions no longer req
R2814 | page 17 | line 1090 | QUALIFIER | 7 Investment in associates- Unquoted* | [I2] cons note 7 associates heading/qualifier
R2815 | page 17 | line 1092 | QUALIFIER | (Accounted under equity method) No. of units Amount No. of units Amount | [I2] cons note 7 associates note/text
R2816 | page 17 | line 1093 | QUALIFIER | Fully paid up - at cost | [I2] cons note 7 associates heading/qualifier
R2817 | page 17 | line 1143 | QUALIFIER | 0.001% Compulsory Convertible Preference Shares of INR 10 each (at premium of INR 1,49,914 | [I2] cons note 7 associates note/text
R2818 | page 17 | line 1144 | QUALIFIER | each) (refer note (ii)) | [I2] cons note 7 associates heading/qualifier
R2819 | page 17 | line 1148 | QUALIFIER | Investments in IB Monotaro Private Limited (refer note (iv) below) | [I2] cons note 7 associates heading/qualifier
R2820 | page 17 | line 1161 | QUALIFIER | Compulsory convertible preference shares of INR 10 each (at premium of INR 140,352/- each) | [I2] cons note 7 associates note/text
R2821 | page 17 | line 1165 | QUALIFIER | (refer note (i)) | [I2] cons note 7 associates heading/qualifier
R2822 | page 17 | line 1169 | QUALIFIER | (refer note (iii) | [I2] cross-reference in: Advance pending share transfer (refer no
R2823 | page 17 | line 1173 | QUALIFIER | Notes: | [I2] cons note 7 associates heading/qualifier
R2824 | page 17 | line 1174 | QUALIFIER | (i) During the period the Group had invested in 649.88 in the Compulsory Convertible Preference Shares (CCPS) of Fleetx Technologies Private Limited of INR 10 face value at a premium of INR 140,352 per share thereby increasing the | [I2] cons note 7 associates note/text
R2825 | page 17 | line 1175 | QUALIFIER | shareholding on fully diluted basis from 22.25% to 25.80%. | [I2] cons note 7 associates heading/qualifier
R2826 | page 17 | line 1177 | QUALIFIER | (ii) During the period the Group's existing investment in Compulsorily Convertible Debentures (CCDs) of Edgewise Technologies Private Limited was converted into 333 Compulsorily Convertible Preference Shares (CCPS) of Face | [I2] cons note 7 associates note/text
R2827 | page 17 | line 1178 | QUALIFIER | Value INR 10/- each at a premium of INR 149,914/- per share, aggregating to INR 49.93 Consequently, the investment has been reclassified from CCDs to CCPS under Non-Current Investments carrying at cost. | [I2] cons note 7 associates note/text
R2828 | page 17 | line 1181 | QUALIFIER | Group thereby increasing its equity ownership on fully converted and diluted basis to 26.94% | [I2] cons note 7 associates note/text
R2829 | page 17 | line 1183 | QUALIFIER | (iv) During the period ended 30 September 2026, the investment in IB Monotaro Private Limited is reclassified to 'Investment in other entities" measured at Fair Value Through Profit or Loss (FVTPL), and a fair value loss of INR 71.49 | [I2] cons note 7 associates note/text
R2830 | page 17 | line 1184 | QUALIFIER | was recognised on the date of reclassification in accordance with Ind AS 109 - Financial Instruments. | [I2] cons note 7 associates note/text
R2831 | page 18 | line 1190 | QUALIFIER | 8 Financial assets | [I2] cons note 8a non-current inv heading/qualifier
R2832 | page 18 | line 1195 | QUALIFIER | i) Investments | [I2] cons note 8a non-current inv heading/qualifier
R2833 | page 18 | line 1196 | QUALIFIER | Non-current | [I2] cons note 8a non-current inv heading/qualifier
R2834 | page 18 | line 1200 | QUALIFIER | Current | [I2] cons note 8a non-current inv heading/qualifier
R2835 | page 18 | line 1209 | QUALIFIER | a) Non-current investments No. of units Amount No. of units Amount | [I2] cons note 8a non-current inv heading/qualifier
R2836 | page 18 | line 1210 | QUALIFIER | (i) Investment in others entities | [I2] cons note 8a non-current inv heading/qualifier
R2837 | page 18 | line 1211 | QUALIFIER | Unquoted (measured at FVTPL) (Refer note 1 below) | [I2] cons note 8a non-current inv heading/qualifier
R2838 | page 18 | line 1255 | QUALIFIER | Investment in IB Monotaro Private Limited (refer note 7(iv)) | [I2] cons note 8a non-current inv heading/qualifier
R2839 | page 18 | line 1265 | QUALIFIER | (ii) Investment in debt instruments of associates at FVTPL | [I2] cons note 8a non-current inv heading/qualifier
R2840 | page 18 | line 1211 | QUALIFIER | Unquoted (measured at FVTPL) | [I2] cons note 8a non-current inv heading/qualifier
R2841 | page 18 | line 1270 | QUALIFIER | Investment in Compulsory convertible debentures of INR 1000 each in Edgewise Technologies | [I2] cons note 8a non-current inv note/text
R2842 | page 18 | line 1278 | QUALIFIER | (refer note 7(ii)) | [I2] cross-reference in: Conversion during the period (refer note
R2843 | page 18 | line 1282 | QUALIFIER | Notes: | [I2] cons note 8a non-current inv heading/qualifier
R2844 | page 18 | line 1284 | QUALIFIER | 1. The Group has invested in equity, convertible preference, and convertible debt instruments of other entities and associates, based on the terms of these instruments they are measured at fair value through profit and loss. | [I2] cons note 8a non-current inv note/text
R2845 | page 19 | line 1290 | QUALIFIER | 8 Financial assets (Cont'd) | [I2] cons note 8b current inv heading/qualifier
R2846 | page 19 | line 1292 | QUALIFIER | b) Current investments | [I2] cons note 8b current inv heading/qualifier
R2847 | page 19 | line 1298 | QUALIFIER | Investment in mutual funds and exchange traded funds - Quoted (measured at FVTPL) No. of units Amount No. of units Amount | [I2] cons note 8b current inv note/text
R2848 | page 19 | line 1349 | QUALIFIER | Investment in bonds and debentures- Quoted (measured at FVTPL) | [I2] cons note 8b current inv heading/qualifier
R2849 | page 19 | line 1372 | QUALIFIER | Investment in Government Securities- Quoted (measured at FVTPL) | [I2] cons note 8b current inv heading/qualifier
R2850 | page 19 | line 1387 | QUALIFIER | Invesments in Tri-Party Repo Settlement (measured at amortised cost) | [I2] cons note 8b current inv heading/qualifier
R2851 | page 20 | line 1448 | QUALIFIER | 8 Financial assets (Cont'd) | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2852 | page 20 | line 1450 | QUALIFIER | c) Loans (measured at amortised cost) | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2853 | page 20 | line 1455 | QUALIFIER | (i) Loans | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2854 | page 20 | line 1456 | QUALIFIER | Non-current (unsecured, considered good unless stated otherwise) | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2855 | page 20 | line 1457 | QUALIFIER | Inter-corporate deposits* | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2856 | page 20 | line 1458 | QUALIFIER | ^ | [I2] marker on: - PNB Housing Finance Limited ^ | FOOTNOTE_MARKER
R2857 | page 20 | line 1459 | QUALIFIER | ^ | [I2] marker on: - LIC ^ | FOOTNOTE_MARKER
R2858 | page 20 | line 1460 | QUALIFIER | ^ | [I2] marker on: - Bajaj Finance Limited ^ | FOOTNOTE_MARKER
R2859 | page 20 | line 1461 | QUALIFIER | ** | [I2] marker on: Loans to employees** | FOOTNOTE_MARKER
R2860 | page 20 | line 1463 | QUALIFIER | Current (unsecured, considered good unless stated otherwise) | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2861 | page 20 | line 1464 | QUALIFIER | Inter-corporate deposits* | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2862 | page 20 | line 1465 | QUALIFIER | ** | [I2] marker on: Loans to employees ** | FOOTNOTE_MARKER
R2863 | page 20 | line 1469 | QUALIFIER | Notes: | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2864 | page 20 | line 1470 | QUALIFIER | * Inter-corporate deposits placed with financial institutions yield fixed interest rate. | [I2] cons note 8c/d loans, other fin assets note/text
R2865 | page 20 | line 1471 | QUALIFIER | ** Represent interest free loans to employees, which are generally recoverable within 24 monthly | [I2] cons note 8c/d loans, other fin assets note/text
R2866 | page 20 | line 1472 | QUALIFIER | instalments. | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2867 | page 20 | line 1473 | QUALIFIER | ^ Includes interest accrued | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2868 | page 20 | line 1478 | QUALIFIER | d) Other financial assets (measured at amortised cost) | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2869 | page 20 | line 1479 | QUALIFIER | Non-current (unsecured, considered good unless stated otherwise) | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2870 | page 20 | line 1481 | QUALIFIER | (Refer Note 11(b)) | [I2] cross-reference in: Deposits with remaining maturity for mor
R2871 | page 20 | line 1481 | QUALIFIER | ** | [I2] marker on: Deposits with remaining maturity for mor | FOOTNOTE_MARKER
R2872 | page 20 | line 1484 | QUALIFIER | Current (unsecured, considered good unless stated otherwise) | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2873 | page 20 | line 1490 | QUALIFIER | Notes: | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2874 | page 20 | line 1491 | QUALIFIER | Security deposits are non-interest bearing and are generally on term of 3 to 9 years. | [I2] cons note 8c/d loans, other fin assets note/text
R2875 | page 20 | line 1492 | QUALIFIER | ** Includes interest accrued | [I2] cons note 8c/d loans, other fin assets heading/qualifier
R2876 | page 27 | line 1899 | QUALIFIER | 28 Fair value measurements | [I2] cons note 28 fair value heading/qualifier
R2877 | page 27 | line 1901 | QUALIFIER | a) | [I2] cons note 28 fair value heading/qualifier
R2878 | page 27 | line 1901 | QUALIFIER | Level | [I2] cons note 28 fair value heading/qualifier
R2879 | page 27 | line 1903 | QUALIFIER | Financial assets | [I2] cons note 28 fair value heading/qualifier
R2880 | page 27 | line 1904 | QUALIFIER | a) Measured at fair value through profit or loss (FVTPL) | [I2] cons note 28 fair value heading/qualifier
R2881 | page 27 | line 1906 | QUALIFIER | (Refer Note b(v) | [I2] cross-reference in: - Investment in bonds & debentures (Refe
R2882 | page 27 | line 1911 | QUALIFIER | b) Measured at amortised cost (refer note (b)(i) and (ii) below) | [I2] cons note 28 fair value heading/qualifier
R2883 | page 27 | line 1925 | QUALIFIER | Financial liabilities | [I2] cons note 28 fair value heading/qualifier
R2884 | page 27 | line 1926 | QUALIFIER | a) Measured at amortised cost (refer note (b)(i) and (ii)) | [I2] cons note 28 fair value heading/qualifier
R2885 | page 27 | line 1932 | QUALIFIER | b) The following methods / assumptions were used to estimate the fair values: | [I2] cons note 28 fair value note/text
R2886 | page 27 | line 1945 | QUALIFIER | c) | [I2] cons note 28 fair value heading/qualifier
R2887 | page 27 | line 1947 | QUALIFIER | Financial assets | [I2] cons note 28 fair value heading/qualifier
R2888 | page 27 | line 1947 | QUALIFIER | Valuation | [I2] cons note 28 fair value heading/qualifier
R2889 | page 27 | line 1948 | QUALIFIER | technique(s) | [I2] cons note 28 fair value heading/qualifier
R2890 | page 27 | line 1947 | QUALIFIER | Significant Unobservable | [I2] cons note 28 fair value heading/qualifier
R2891 | page 27 | line 1948 | QUALIFIER | inputs | [I2] cons note 28 fair value heading/qualifier
R2892 | page 27 | line 1907 | QUALIFIER | Investment in equity/preference instruments of other entities | [I2] cons note 28 fair value heading/qualifier
R2893 | page 27 | line 1955 | QUALIFIER | Fleetx Technologies Private Limited (till 11 April 2025), IB | [I2] cons note 28 fair value heading/qualifier
R2894 | page 27 | line 1956 | QUALIFIER | Monotaro Private Ltd. (w.e.f 29 May 2026) | [I2] cons note 28 fair value heading/qualifier
R2895 | page 27 | line 1952 | QUALIFIER | Market multiple | [I2] cons note 28 fair value heading/qualifier
R2896 | page 27 | line 1953 | QUALIFIER | and Discounted | [I2] cons note 28 fair value heading/qualifier
R2897 | page 27 | line 1954 | QUALIFIER | cashflow approach | [I2] cons note 28 fair value heading/qualifier
R2898 | page 27 | line 1952 | QUALIFIER | i) Discount rate | [I2] cons note 28 fair value heading/qualifier
R2899 | page 27 | line 1953 | QUALIFIER | ii) Terminal growth rate | [I2] cons note 28 fair value heading/qualifier
R2900 | page 27 | line 1954 | QUALIFIER | iii) Market multiples | [I2] cons note 28 fair value heading/qualifier
R2901 | page 27 | line 1955 | QUALIFIER | (Comparable Companies) | [I2] cons note 28 fair value heading/qualifier
R2902 | page 27 | line 1956 | QUALIFIER | iv) Revenue growth rate | [I2] cons note 28 fair value heading/qualifier
R2903 | page 27 | line 1960 | QUALIFIER | d) Reconciliation of level 3 fair value measurements | [I2] cons note 28 fair value heading/qualifier
R2904 | page 27 | line 1971 | QUALIFIER | During the period ended 30 September 2025 and 30 September 2026, there were no transfers due to re-classification into and out of Level 3 fair value measurements. | [I2] cons note 28 fair value note/text
R2905 | page 27 | line 1901 | QUALIFIER | Category wise details as to carrying value, fair value and the level of fair value measurement hierarchy of the Group's financial instruments are as follows: | [I2] cons note 28 fair value note/text
R2906 | page 27 | line 1950 | QUALIFIER | Investment in equity/preference instruments of other entities/investment in debt instruments of associates | [I2] cons note 28 fair value note/text
R2907 | page 27 | line 1958 | QUALIFIER | Considering the nature of investments, there is no material change in the significant unobservable inputs for investment in debt instruments of associates as at 30 September 2026. | [I2] cons note 28 fair value note/text
R2908 | page 27 | line 1945 | QUALIFIER | Following table describes the valuation techniques used and key inputs thereto for the level 3 financial assets for the period ended 30 September 2026 | [I2] cons note 28 fair value note/text
R2909 | page 27 | line 1947 | QUALIFIER | Inter-relationship between significant unobservable input and fair value measurement | [I2] cons note 28 fair value note/text
R2910 | page 27 | line 1952 | QUALIFIER | The estimated fair value of Investment in Other entities will Increase/ (decrease) if the Terminal growth rate and Market multiple | [I2] cons note 28 fair value note/text
R2911 | page 27 | line 1953 | QUALIFIER | is higher/ (lower). | [I2] cons note 28 fair value heading/qualifier
R2912 | page 27 | line 1954 | QUALIFIER | The estimated fair value of Investment in Other entities will Increase/ (decrease) if the Discount rate is higher/ (lower). | [I2] cons note 28 fair value note/text
R2913 | page 27 | line 1883 | QUALIFIER | The Group has a defined benefit gratuity plan. Every employee who has completed statutory defined period of service gets a gratuity on departure in accordance with Payment of Gratuity Act, 1972. The scheme is funded with insurance company in form of | [I2] cons note 28 fair value note/text
R2914 | page 27 | line 1884 | QUALIFIER | qualifying insurance policy. This defined benefit plans exposes the Group to actuarial risks, such as longevity risk, interest rate risk and salary risk. | [I2] cons note 28 fair value note/text
R2915 | page 27 | line 1943 | QUALIFIER | vi) Fair value of the quoted bonds and debentures is determined using observable market's inputs and is classified as Level 2. | [I2] cons note 28 fair value note/text
R2916 | page 27 | line 1939 | QUALIFIER | iv) Fair value of investment in equity/preference/ and debenture instruments of other entities is estimated based on discounted cash flows / market multiple valuation technique using the cash flow projections, discount rate and credit risk and are classified as | [I2] cons note 28 fair value note/text
R2917 | page 27 | line 1876 | QUALIFIER | Level 3. | [I2] cons note 28 fair value heading/qualifier
R2918 | page 27 | line 1907 | QUALIFIER | - Investment in equity/preference instruments of other entities (Refer Note b(iv) below) | [I2] cons note 28 fair value note/text
R2919 | page 27 | line 1941 | QUALIFIER | v) Fair value of Investment in debt instruments of associates is estimated based on discounted cash flows / market multiple valuation technique using the cash flow projections, discount rate and credit risk and are classified as Level 3. | [I2] cons note 28 fair value note/text
R2920 | page 27 | line 1933 | QUALIFIER | i) The carrying value of deposits with Banks, Inter-corporate deposits with Financial institutions, trade receivables, loans to employees, cash and cash equivalents, trade payables, security deposits, lease liabilities and other financial assets and other financial | [I2] cons note 28 fair value note/text
R2921 | page 27 | line 1934 | QUALIFIER | liabilities measured at amortised cost approximate their fair value due to the short-term maturities of these instruments. These have been assessed basis counterparty credit risk. | [I2] cons note 28 fair value note/text
R2922 | page 27 | line 1935 | QUALIFIER | ii) The fair value of non-current financial assets and financial liabilities measured are determined by discounting future cash flows using current rates of instruments with similar terms and credit risk. The current rates used does not reflect significant changes | [I2] cons note 28 fair value note/text
R2923 | page 27 | line 1936 | QUALIFIER | from the discount rates used initially. Therefore, the carrying value of these instruments measured at amortised cost approximate their fair value. | [I2] cons note 28 fair value note/text
R2924 | page 27 | line 1908 | QUALIFIER | - Investment in debt instruments of associates (Refer Note b(v) below) | [I2] cons note 28 fair value note/text
R2925 | page 27 | line 1886 | QUALIFIER | The amount included in the balance sheet arising from the Group's obligation in respect of its gratuity plan and leave encashment is as follows: | [I2] cons note 28 fair value note/text
R2926 | page 27 | line 1905 | QUALIFIER | - Investment in mutual funds, exchange traded funds and government securities (Refer Note b(iii) below) | [I2] cons note 28 fair value note/text
R2927 | page 27 | line 1960 | QUALIFIER | Reconciliation table columns resolved from pdftoppm render of page 27; text layer scrambled the row order | [I2] A1 extraction log
R2928 | page 46 | line 3159 | QUALIFIER | 7 Investment in subsidiaries and associates* | [I2] stand note 7 subs+assoc heading/qualifier
R2929 | page 46 | line 3164 | QUALIFIER | No. of shares Amount No. of shares Amount | [I2] stand note 7 subs+assoc heading/qualifier
R2930 | page 46 | line 3166 | QUALIFIER | Investment in subsidiaries - Unquoted | [I2] stand note 7 subs+assoc heading/qualifier
R2931 | page 46 | line 3167 | QUALIFIER | Fully paid up - at cost | [I2] stand note 7 subs+assoc heading/qualifier
R2932 | page 46 | line 3170 | QUALIFIER | (refer note (v) | [I2] cross-reference in: Equity shares of INR 10 each (refer note
R2933 | page 46 | line 3172 | QUALIFIER | (refer note (ii) | [I2] cross-reference in: Optionally Convertible Debentures of INR
R2934 | page 46 | line 3177 | QUALIFIER | (refer note (vi) | [I2] cross-reference in: Add: Deemed investment (refer note (vi) 
R2935 | page 46 | line 3185 | QUALIFIER | (refer note (iii) | [I2] cross-reference in: Equity shares of INR 10 each (refer note
R2936 | page 46 | line 3192 | QUALIFIER | (refer note (i) | [I2] cross-reference in: 0.001% Optionally Convertible Debentures
R2937 | page 46 | line 3193 | QUALIFIER | (refer note (vi) | [I2] cross-reference in: Add: Deemed investment (refer note (vi) 
R2938 | page 46 | line 3203 | QUALIFIER | Investment in associates - Unquoted | [I2] stand note 7 subs+assoc heading/qualifier
R2939 | page 46 | line 3204 | QUALIFIER | Fully paid up - at cost | [I2] stand note 7 subs+assoc heading/qualifier
R2940 | page 46 | line 3242 | QUALIFIER | Investment in IB Monotaro Private Limited (refer note (vii) below) | [I2] stand note 7 subs+assoc heading/qualifier
R2941 | page 46 | line 3250 | QUALIFIER | (refer note iv below) | [I2] cross-reference in: Compulsory convertible preference shares
R2942 | page 46 | line 3260 | QUALIFIER | *Refer note 30 for transactions and outstanding balances pertaining to related parties. | [I2] stand note 7 subs+assoc note/text
R2943 | page 47 | line 3266 | QUALIFIER | Notes: | [I2] stand note 8a non-current inv heading/qualifier
R2944 | page 47 | line 3280 | QUALIFIER | 8 Financial assets | [I2] stand note 8a non-current inv heading/qualifier
R2945 | page 47 | line 3282 | QUALIFIER | i) Investments | [I2] stand note 8a non-current inv heading/qualifier
R2946 | page 47 | line 3283 | QUALIFIER | Non-current* | [I2] stand note 8a non-current inv heading/qualifier
R2947 | page 47 | line 3287 | QUALIFIER | Current | [I2] stand note 8a non-current inv heading/qualifier
R2948 | page 47 | line 3293 | QUALIFIER | *Refer note 30 for transactions and outstanding balances pertaining to related parties. | [I2] stand note 8a non-current inv note/text
R2949 | page 47 | line 3295 | QUALIFIER | Non-current investments | [I2] stand note 8a non-current inv heading/qualifier
R2950 | page 47 | line 3296 | QUALIFIER | a) Investment in instruments of subsidiaries at FVTPL (fully paid-up) (Refer note (i) below) | [I2] stand note 8a non-current inv note/text
R2951 | page 47 | line 3298 | QUALIFIER | Unquoted (measured at FVTPL) No. of shares Amount No. of shares Amount | [I2] stand note 8a non-current inv note/text
R2952 | page 47 | line 3303 | QUALIFIER | (refer note 7(v)) | [I2] cross-reference in: Conversion during the period (refer note
R2953 | page 47 | line 3285 | QUALIFIER | b) Investment in other entities (fully paid up ) | [I2] stand note 8a non-current inv heading/qualifier
R2954 | page 47 | line 3309 | QUALIFIER | Unquoted (measured at FVTPL) (Refer note (ii) below) | [I2] stand note 8a non-current inv heading/qualifier
R2955 | page 47 | line 3339 | QUALIFIER | Investment in IB Monotaro Private Limited (refer note 7 (vii)) | [I2] stand note 8a non-current inv heading/qualifier
R2956 | page 47 | line 3351 | QUALIFIER | Notes: | [I2] stand note 8a non-current inv heading/qualifier
R2957 | page 47 | line 3274 | QUALIFIER | Optionally Convertible Cumulative Redeemable Preference Shares of INR 10 each (at premium of INR 10 each) | [I2] stand note 8a non-current inv note/text
R2958 | page 47 | line 3356 | QUALIFIER | ii). The Company has investment in compulsory convertible preference shares and equity shares of other entities, based on the terms of these instruments they are being measured at fair value through profit and loss. | [I2] stand note 8a non-current inv note/text
R2959 | page 47 | line 3352 | QUALIFIER | i). The Company had invested in optionally convertible cumulative redeemable preference shares ('OCCRPS') of its subsidiaries. Based on the terms of OCCRPS, these have been classified as financial instruments in the nature of financial assets | [I2] stand note 8a non-current inv note/text
R2960 | page 47 | line 3353 | QUALIFIER | to be measured at fair value. Fair value of these instruments has been determined based on market multiples / replacement cost method / discounted cash flow valuation technique using cash flow projections and discount rate. Gain/loss on | [I2] stand note 8a non-current inv note/text
R2961 | page 47 | line 3354 | QUALIFIER | subsequent re-measurement is recognised through Statement of Profit and Loss. | [I2] stand note 8a non-current inv note/text
R2962 | page 47 | line 3268 | QUALIFIER | ii) During the period ended 30 September 2026, the Company has invested in the 7,600,000, 0.001% Optionally Convertible Debentures of Tradezeal Online Private Limited of INR 10/-each at premium of INR 15. | [I2] stand note 8a non-current inv note/text
R2963 | page 47 | line 3301 | QUALIFIER | Optionally Convertible Cumulative Redeemable Preference Shares of INR 10 each | [I2] stand note 8a non-current inv note/text
R2964 | page 47 | line 3274 | QUALIFIER | v). The Company had invested in 7,870,000 0.01% Optionally Convertible Cumulative Redeemable Preference Shares (OCCRPS) of Tradezeal Online Private Limited. During the period ended 30 September 2026, these OCCRPS were | [I2] stand note 8a non-current inv note/text
R2965 | page 47 | line 3275 | QUALIFIER | converted into equity shares on a 1:1 basis in accordance with the terms of the agreement. | [I2] stand note 8a non-current inv note/text
R2966 | page 47 | line 3276 | QUALIFIER | vi) Deemed investment is towards cost of stock options allocated to employees of subsidiary companies. | [I2] stand note 8a non-current inv note/text
R2967 | page 47 | line 3277 | QUALIFIER | vii) During the period ended 30 September 2026, the investment in IB Monotaro Private Limited is reclassified to 'Investment in other entities" measured at Fair Value Through Profit or Loss (FVTPL), and a fair value loss of INR 200 was | [I2] stand note 8a non-current inv note/text
R2968 | page 47 | line 3278 | QUALIFIER | recognised on the date of reclassification in accordance with Ind AS 109 - Financial Instruments. | [I2] stand note 8a non-current inv note/text
R2969 | page 47 | line 3269 | QUALIFIER | iii) During the period ended 30 September 2026, the Company incorporated a wholly owned subsidiary, "IndiaMart Finance Limited", on 4 August 2026, primarily to facilitate the short-term working capital and financing requirements of | [I2] stand note 8a non-current inv note/text
R2970 | page 47 | line 3270 | QUALIFIER | business users. During the period, the Company invested in 12,050,000 equity shares of the subsidiary, having a face value of INR 10 each. | [I2] stand note 8a non-current inv note/text
R2971 | page 47 | line 3271 | QUALIFIER | iv) During the period ended 30 September 2026, the Company has invested INR 649.88 in the Compulsory Convertible Preference Shares (CCPS) of Fleetx Technologies Private Limited of INR 10 face value at a premium of INR 1,40,352 per | [I2] stand note 8a non-current inv note/text
R2972 | page 47 | line 3272 | QUALIFIER | share thereby increasing the shareholding on fully diluted basis from 22.25% to 25.80%. | [I2] stand note 8a non-current inv note/text
R2973 | page 47 | line 3267 | QUALIFIER | i) During the period ended 30 September 2026, the Company has invested in the 1,172, 0.001% Optionally Convertible Debentures of Livekeeping Technologies Private Limited of INR 10/-each at premium of INR 51,157. | [I2] stand note 8a non-current inv note/text
R2974 | page 48 | line 3363 | QUALIFIER | 8 Financial assets (Cont'd) | [I2] stand note 8b current inv heading/qualifier
R2975 | page 48 | line 3362 | QUALIFIER | No. of units Amount No. of units Amount | [I2] stand note 8b current inv heading/qualifier
R2976 | page 48 | line 3365 | QUALIFIER | Current investments | [I2] stand note 8b current inv heading/qualifier
R2977 | page 48 | line 3366 | QUALIFIER | Investment in mutual funds and exchange traded funds - Quoted (measured at FVTPL) | [I2] stand note 8b current inv note/text
R2978 | page 48 | line 3410 | QUALIFIER | Investment in bonds and debentures- Quoted (measured at FVTPL) | [I2] stand note 8b current inv heading/qualifier
R2979 | page 48 | line 3428 | QUALIFIER | Investment in Government Securities- Quoted (measured at FVTPL) | [I2] stand note 8b current inv heading/qualifier
R2980 | page 48 | line 3443 | QUALIFIER | Invesments in Tri-Party Repo Settlement-Unquoted (measured at amortised cost) | [I2] stand note 8b current inv note/text
R2981 | page 49 | line 3464 | QUALIFIER | 8 Financial assets (Cont'd) | [I2] stand note 8 loans, other fin assets heading/qualifier
R2982 | page 49 | line 3466 | QUALIFIER | ii) Loans (measured at amortised cost) As at | [I2] stand note 8 loans, other fin assets heading/qualifier
R2983 | page 49 | line 3468 | QUALIFIER | Non current | [I2] stand note 8 loans, other fin assets heading/qualifier
R2984 | page 49 | line 3469 | QUALIFIER | Considered good- Unsecured | [I2] stand note 8 loans, other fin assets heading/qualifier
R2985 | page 49 | line 3471 | QUALIFIER | Inter-corporate deposits** | [I2] stand note 8 loans, other fin assets heading/qualifier
R2986 | page 49 | line 3472 | QUALIFIER | ^ | [I2] marker on: -LIC^ | FOOTNOTE_MARKER
R2987 | page 49 | line 3473 | QUALIFIER | ^ | [I2] marker on: -PNB Housing Finance Ltd.^ | FOOTNOTE_MARKER
R2988 | page 49 | line 3475 | QUALIFIER | * | [I2] marker on: Loans to employees* | FOOTNOTE_MARKER
R2989 | page 49 | line 3494 | QUALIFIER | Current | [I2] stand note 8 loans, other fin assets heading/qualifier
R2990 | page 49 | line 3478 | QUALIFIER | Considered good- Unsecured | [I2] stand note 8 loans, other fin assets heading/qualifier
R2991 | page 49 | line 3482 | QUALIFIER | Notes: | [I2] stand note 8 loans, other fin assets heading/qualifier
R2992 | page 49 | line 3485 | QUALIFIER | ^ Includes interest accrued of INR 63.01 (31 March 2026 : INR 36.06). | [I2] stand note 8 loans, other fin assets heading/qualifier
R2993 | page 49 | line 3487 | QUALIFIER | iii) Other financial assets (measured at amortised cost) As at | [I2] stand note 8 loans, other fin assets heading/qualifier
R2994 | page 49 | line 3489 | QUALIFIER | Non-current (unsecured, considered good unless stated otherwise) | [I2] stand note 8 loans, other fin assets heading/qualifier
R2995 | page 49 | line 3491 | QUALIFIER | Deposits with banks | [I2] stand note 8 loans, other fin assets heading/qualifier
R2996 | page 49 | line 3492 | QUALIFIER | ** | [I2] marker on: - Deposits with maturity of more than tw | FOOTNOTE_MARKER
R2997 | page 49 | line 3494 | QUALIFIER | Current (unsecured, considered good unless stated otherwise) | [I2] stand note 8 loans, other fin assets heading/qualifier
R2998 | page 49 | line 3497 | QUALIFIER | * | [I2] marker on: Other receivables * | FOOTNOTE_MARKER
R2999 | page 49 | line 3499 | QUALIFIER | Notes: | [I2] stand note 8 loans, other fin assets heading/qualifier
R3000 | page 49 | line 3500 | QUALIFIER | Security deposits are non-interest bearing and are generally on term of 3 to 9 years. | [I2] stand note 8 loans, other fin assets note/text
R3001 | page 49 | line 3501 | QUALIFIER | * Refer Note 30 for outstanding balances pertaining to related parties. | [I2] stand note 8 loans, other fin assets note/text
R3002 | page 49 | line 3502 | QUALIFIER | **Includes interest accrued of INR 45.39 (31 March 2026 : INR 23.33). | [I2] stand note 8 loans, other fin assets heading/qualifier
R3003 | page 49 | line 3484 | QUALIFIER | ** Intercorporate deposits placed with financial institutions yield fixed interest rates. | [I2] stand note 8 loans, other fin assets note/text
R3004 | page 49 | line 3483 | QUALIFIER | *Represent interest free loans to employees, which are generally recoverable within 24 monthly instalments. | [I2] stand note 8 loans, other fin assets note/text
R3005 | page 56 | line 3913 | QUALIFIER | 28 Fair value measurements | [I2] stand note 28 fair value heading/qualifier
R3006 | page 56 | line 3915 | QUALIFIER | a) | [I2] stand note 28 fair value heading/qualifier
R3007 | page 56 | line 3917 | QUALIFIER | Level As at | [I2] stand note 28 fair value heading/qualifier
R3008 | page 56 | line 3920 | QUALIFIER | Financial assets | [I2] stand note 28 fair value heading/qualifier
R3009 | page 56 | line 3921 | QUALIFIER | a) Measured at fair value through profit or loss (FVTPL) | [I2] stand note 28 fair value heading/qualifier
R3010 | page 56 | line 3922 | QUALIFIER | - Investment in mutual funds, exchange traded funds and government securities | [I2] stand note 28 fair value note/text
R3011 | page 56 | line 3923 | QUALIFIER | (Refer Note b(iii) below) | [I2] stand note 28 fair value heading/qualifier
R3012 | page 56 | line 3924 | QUALIFIER | (Refer Note b(v) | [I2] cross-reference in: - Investment in bonds & debentures (Refe
R3013 | page 56 | line 3927 | QUALIFIER | b) Measured at amortised cost (Refer Note b(i) and (ii) below) | [I2] stand note 28 fair value heading/qualifier
R3014 | page 56 | line 3940 | QUALIFIER | Financial liabilities | [I2] stand note 28 fair value heading/qualifier
R3015 | page 56 | line 3941 | QUALIFIER | a) Measured at amortised cost (Refer Note b(i) and (ii) below) Level 3 | [I2] stand note 28 fair value note/text
R3016 | page 56 | line 3947 | QUALIFIER | b) The following methods / assumptions were used to estimate the fair values: | [I2] stand note 28 fair value note/text
R3017 | page 56 | line 3915 | QUALIFIER | Category wise details as to carrying value, fair value and the level of fair value measurement hierarchy of the Company's financial instruments are as follows: | [I2] stand note 28 fair value note/text
R3018 | page 56 | line 3948 | QUALIFIER | i) The carrying value of deposits with banks, investment in TREPS, trade receivables, cash and cash equivalents, loans to employees, trade payables, security deposits, lease liabilities and other financial assets | [I2] stand note 28 fair value note/text
R3019 | page 56 | line 3949 | QUALIFIER | and other financial liabilities measured at amortised cost approximate their fair value due to the short-term maturities of these instruments. These have been assessed basis credit risk. | [I2] stand note 28 fair value note/text
R3020 | page 56 | line 3951 | QUALIFIER | ii) The fair value of non-current financial assets and financial liabilities are determined by discounting future cash flows using current rates of instruments with similar terms and credit risk. The current rates | [I2] stand note 28 fair value note/text
R3021 | page 56 | line 3952 | QUALIFIER | used do not reflect significant changes from the discount rates used initially. Therefore, the carrying value of these instruments measured at amortised cost approximate their fair value. | [I2] stand note 28 fair value note/text
R3022 | page 56 | line 3956 | QUALIFIER | iv) Fair value of debt instruments of subsidiaries, equity/preference instruments of other entities is estimated based on replacement cost method / discounted cash flows / market multiple valuation technique | [I2] stand note 28 fair value note/text
R3023 | page 56 | line 3957 | QUALIFIER | using cash flow projections, discount rate and credit risk and are classified as Level 3. | [I2] stand note 28 fair value note/text
R3024 | page 56 | line 3955 | QUALIFIER | financial assets. | [I2] stand note 28 fair value heading/qualifier
R3025 | page 56 | line 3958 | QUALIFIER | v) Fair value of the quoted bonds and debentures is determined using observable market's inputs and is classified as Level 2. | [I2] stand note 28 fair value note/text
R3026 | page 56 | line 3959 | QUALIFIER | vi) Fair value of debt instruments of associates is estimated based on replacement cost method / discounted cash flows / market multiple valuation technique using cash flow projections, discount rate and | [I2] stand note 28 fair value note/text
R3027 | page 56 | line 3957 | QUALIFIER | credit risk and are classified as Level 3. | [I2] stand note 28 fair value heading/qualifier
R3028 | page 57 | line 3966 | QUALIFIER | 28 Fair value measurements (Cont'd) | [I2] stand note 28 fair value level 3 heading/qualifier
R3029 | page 57 | line 3968 | QUALIFIER | c) | [I2] stand note 28 fair value level 3 heading/qualifier
R3030 | page 57 | line 3970 | QUALIFIER | Financial assets Valuation technique(s) Significant Unobservable | [I2] stand note 28 fair value level 3 heading/qualifier
R3031 | page 57 | line 3971 | QUALIFIER | input | [I2] stand note 28 fair value level 3 heading/qualifier
R3032 | page 57 | line 3970 | QUALIFIER | Inter-relationship between | [I2] stand note 28 fair value level 3 heading/qualifier
R3033 | page 57 | line 3971 | QUALIFIER | significant unobservable | [I2] stand note 28 fair value level 3 heading/qualifier
R3034 | page 57 | line 3971 | QUALIFIER | Investment in debt instruments of subsidiaries and equity/preference | [I2] stand note 28 fair value level 3 heading/qualifier
R3035 | page 57 | line 3972 | QUALIFIER | instruments of other entities | [I2] stand note 28 fair value level 3 heading/qualifier
R3036 | page 57 | line 3973 | QUALIFIER | Pay With Indiamart Private Limited Replacement cost method Replacement cost method The estimated fair value of | [I2] stand note 28 fair value level 3 note/text
R3037 | page 57 | line 3974 | QUALIFIER | investment in subsidiaries | [I2] stand note 28 fair value level 3 heading/qualifier
R3038 | page 57 | line 3975 | QUALIFIER | will Increase/ (decrease) if | [I2] stand note 28 fair value level 3 heading/qualifier
R3039 | page 57 | line 3976 | QUALIFIER | the Replacement cost is | [I2] stand note 28 fair value level 3 heading/qualifier
R3040 | page 57 | line 3977 | QUALIFIER | higher/ (lower) | [I2] stand note 28 fair value level 3 heading/qualifier
R3041 | page 57 | line 3976 | QUALIFIER | Technologies Private Limited (till 11 April 2025), IB Monotaro Private Limited | [I2] stand note 28 fair value level 3 note/text
R3042 | page 57 | line 3977 | QUALIFIER | (w.e.f 29 May 2026) and Baldor Technologies Private Limited | [I2] stand note 28 fair value level 3 heading/qualifier
R3043 | page 57 | line 3975 | QUALIFIER | Market multiple approach | [I2] stand note 28 fair value level 3 heading/qualifier
R3044 | page 57 | line 3976 | QUALIFIER | and discounted cash flow | [I2] stand note 28 fair value level 3 heading/qualifier
R3045 | page 57 | line 3975 | QUALIFIER | approach | [I2] stand note 28 fair value level 3 heading/qualifier
R3046 | page 57 | line 3975 | QUALIFIER | i) Discount rate | [I2] stand note 28 fair value level 3 heading/qualifier
R3047 | page 57 | line 3976 | QUALIFIER | ii) Terminal growth rate | [I2] stand note 28 fair value level 3 heading/qualifier
R3048 | page 57 | line 3977 | QUALIFIER | iii) Market multiples | [I2] stand note 28 fair value level 3 heading/qualifier
R3049 | page 57 | line 3978 | QUALIFIER | (Comparable Companies) | [I2] stand note 28 fair value level 3 heading/qualifier
R3050 | page 57 | line 3979 | QUALIFIER | iv) Revenue growth rate | [I2] stand note 28 fair value level 3 heading/qualifier
R3051 | page 57 | line 3973 | QUALIFIER | The estimated fair value of | [I2] stand note 28 fair value level 3 heading/qualifier
R3052 | page 57 | line 3979 | QUALIFIER | investment in other entities | [I2] stand note 28 fair value level 3 heading/qualifier
R3053 | page 57 | line 3980 | QUALIFIER | will Increase/ (decrease) if | [I2] stand note 28 fair value level 3 heading/qualifier
R3054 | page 57 | line 3981 | QUALIFIER | the terminal growth rate, | [I2] stand note 28 fair value level 3 heading/qualifier
R3055 | page 57 | line 3982 | QUALIFIER | Market multiple and revenue | [I2] stand note 28 fair value level 3 heading/qualifier
R3056 | page 57 | line 3983 | QUALIFIER | growth rate is higher/ (lower). | [I2] stand note 28 fair value level 3 heading/qualifier
R3057 | page 57 | line 3978 | QUALIFIER | The estimated fair value of | [I2] stand note 28 fair value level 3 heading/qualifier
R3058 | page 57 | line 3985 | QUALIFIER | investment in other entities | [I2] stand note 28 fair value level 3 heading/qualifier
R3059 | page 57 | line 3986 | QUALIFIER | will Increase/ (decrease) if | [I2] stand note 28 fair value level 3 heading/qualifier
R3060 | page 57 | line 3987 | QUALIFIER | the Discount Rate is | [I2] stand note 28 fair value level 3 heading/qualifier
R3061 | page 57 | line 3988 | QUALIFIER | (lower)/higher. | [I2] stand note 28 fair value level 3 heading/qualifier
R3062 | page 57 | line 3993 | QUALIFIER | d) Reconciliation of level 3 fair value measurements | [I2] stand note 28 fair value level 3 heading/qualifier
R3063 | page 57 | line 3998 | QUALIFIER | (refer note 7) | [I2] cross-reference in: Conversion of preference shares into equ
R3064 | page 57 | line 4010 | QUALIFIER | (refer note 7) | [I2] cross-reference in: Change in status of investment to Other 
R3065 | page 57 | line 4024 | QUALIFIER | During the period ended 30 September 2026 and 30 September 2025, there were no transfers due to re-classification into and out of Level 3 fair value measurements. | [I2] stand note 28 fair value level 3 note/text
R3066 | page 57 | line 3990 | QUALIFIER | Considering the nature of investments, there is no material change in the significant unobservable inputs and sensitivity for investment made in other entities, debt instruments of associates as at 30 September | [I2] stand note 28 fair value level 3 note/text
R3067 | page 57 | line 3991 | QUALIFIER | 2026. | [I2] stand note 28 fair value level 3 heading/qualifier
R3068 | page 57 | line 3995 | QUALIFIER | Investment in Optionally Convertible Cumulative Redeemable Preference instruments of subsidiaries | [I2] stand note 28 fair value level 3 note/text
R3069 | page 57 | line 4005 | QUALIFIER | Investment in equity/preference instruments/debt instrument of other entities/investment in debt instruments of | [I2] stand note 28 fair value level 3 note/text
R3070 | page 57 | line 3990 | QUALIFIER | associates | [I2] stand note 28 fair value level 3 heading/qualifier
R3071 | page 57 | line 4016 | QUALIFIER | Derivative contract Liability | [I2] stand note 28 fair value level 3 heading/qualifier
R3072 | page 57 | line 3968 | QUALIFIER | Following table describes the valuation techniques used and key inputs thereto for the level 3 financial assets as of 30 September 2026 | [I2] stand note 28 fair value level 3 note/text
R3073 | page 29 | line 2124 | QUALIFIER | Dhruv Prakash Non-Executive Director (upto 29 June 2026) | [I3] cons note 30 RPT list heading/qualifier
R3074 | page 29 | line 2125 | QUALIFIER | Rajesh Sawhney Independent Director (upto 23 September 2025) | [I3] cons note 30 RPT list heading/qualifier
R3075 | page 29 | line 2157 | QUALIFIER | Indiamart Employee Benefit Trust (administered Trust to manage employees share based payment plans of the Company) | [I3] cons note 30 RPT list note/text
R3076 | page 29 | line 2107 | QUALIFIER | Indiamart Finance Limited (incorporated on 04 August 2026) | [I3] cons note 30 RPT list heading/qualifier
R3077 | page 29 | line 2106 | QUALIFIER | IIL Digital Private Limited (incorporated on 27 August 2024) | [I3] cons note 30 RPT list heading/qualifier
R3078 | page 29 | line 2159 | QUALIFIER | *With whom the Group had transactions during the period | [I3] cons note 30 RPT list heading/qualifier
R3079 | page 29 | line 2161 | QUALIFIER | ^ Transactions from 01 November 2025 | [I3] cons note 30 RPT list heading/qualifier
R3080 | page 29 | line 2114 | QUALIFIER | IB Monotaro Private Limited (upto 29 May 2026) | [I3] cons note 30 RPT list heading/qualifier
R3081 | page 30 | line 2177 | QUALIFIER | 30 Related party transactions (Cont'd) | [I3] cons note 30 RPT transactions heading/qualifier
R3082 | page 30 | line 2179 | QUALIFIER | The following table provides the total amount of transactions that have been entered into with the related parties for the period: | [I3] cons note 30 RPT transactions note/text
R3083 | page 30 | line 2186 | QUALIFIER | Rent & related miscellaneous expenses | [I3] cons note 30 RPT transactions heading/qualifier
R3084 | page 30 | line 2189 | QUALIFIER | Tax consultancy and litigation support service | [I3] cons note 30 RPT transactions heading/qualifier
R3085 | page 30 | line 2193 | QUALIFIER | Recruitment and training expenses | [I3] cons note 30 RPT transactions heading/qualifier
R3086 | page 30 | line 2196 | QUALIFIER | Dividend paid | [I3] cons note 30 RPT transactions heading/qualifier
R3087 | page 30 | line 2201 | QUALIFIER | Remuneration | [I3] cons note 30 RPT transactions heading/qualifier
R3088 | page 30 | line 2208 | QUALIFIER | Associates | [I3] cons note 30 RPT transactions heading/qualifier
R3089 | page 30 | line 2209 | QUALIFIER | Investment in associates | [I3] cons note 30 RPT transactions heading/qualifier
R3090 | page 30 | line 2212 | QUALIFIER | Advance given for share transfer | [I3] cons note 30 RPT transactions heading/qualifier
R3091 | page 30 | line 2215 | QUALIFIER | Web, advertisement & marketing services provided to | [I3] cons note 30 RPT transactions heading/qualifier
R3092 | page 30 | line 2224 | QUALIFIER | Terms and conditions of transactions with related parties | [I3] cons note 30 RPT transactions heading/qualifier
R3093 | page 30 | line 2225 | QUALIFIER | The transactions with related parties are entered on terms equivalent to those that prevail in arm's length transactions. Outstanding balances as at the period end are unsecured and interest free | [I3] cons note 30 RPT transactions note/text
R3094 | page 30 | line 2226 | QUALIFIER | and settlement occurs in cash. There have been no guarantees provided or received for any related party receivables or payables. This assessment is undertaken each financial year through | [I3] cons note 30 RPT transactions note/text
R3095 | page 30 | line 2227 | QUALIFIER | examining the financial position of the related party and the market in which the related party operates. | [I3] cons note 30 RPT transactions note/text
R3096 | page 30 | line 2185 | QUALIFIER | Entities where KMP exercise Significant | [I3] cons note 30 RPT transactions heading/qualifier
R3097 | page 30 | line 2192 | QUALIFIER | KMP and relatives of KMP's: | [I3] cons note 30 RPT transactions heading/qualifier
R3098 | page 31 | line 2233 | QUALIFIER | 30 Related party transactions (Cont'd) | [I3] cons note 30 RPT balances heading/qualifier
R3099 | page 31 | line 2234 | QUALIFIER | The following table discloses the related parties balances at the period / year end: | [I3] cons note 30 RPT balances note/text
R3100 | page 31 | line 2236 | QUALIFIER | Balance Outstanding at the period / year end | [I3] cons note 30 RPT balances heading/qualifier
R3101 | page 31 | line 2239 | QUALIFIER | Associates | [I3] cons note 30 RPT balances heading/qualifier
R3102 | page 31 | line 2240 | QUALIFIER | Investment in equity/preference instruments of associates (at cost)* | [I3] cons note 30 RPT balances heading/qualifier
R3103 | page 31 | line 2245 | QUALIFIER | (refer note 7 (iv)) | [I3] cross-reference in: IB Monotaro Private Limited (refer note 
R3104 | page 31 | line 2250 | QUALIFIER | Advance pending share transfer | [I3] cons note 30 RPT balances heading/qualifier
R3105 | page 31 | line 2253 | QUALIFIER | Investment in debt instruments of associates (at FVTPL) | [I3] cons note 30 RPT balances heading/qualifier
R3106 | page 31 | line 2256 | QUALIFIER | Trade receivables | [I3] cons note 30 RPT balances heading/qualifier
R3107 | page 31 | line 2259 | QUALIFIER | Trade Payable (including accrued expenses) | [I3] cons note 30 RPT balances heading/qualifier
R3108 | page 31 | line 2263 | QUALIFIER | Contract Liabilities | [I3] cons note 30 RPT balances heading/qualifier
R3109 | page 31 | line 2267 | QUALIFIER | *Does not include share of profit/loss of associate as accounted under equity method | [I3] cons note 30 RPT balances note/text
R3110 | page 58 | line 4031 | QUALIFIER | As per Ind AS 108 "Operating Segments", the Company has disclosed the segment information only as part of consolidated financial statements. | [I3] stand note 30 RPT list note/text
R3111 | page 58 | line 4041 | QUALIFIER | IndiaMart Finance Limited (incorporated on 04 August 2026) | [I3] stand note 30 RPT list heading/qualifier
R3112 | page 58 | line 4044 | QUALIFIER | IB Monotaro Private Limited (till 29 May 2026) | [I3] stand note 30 RPT list heading/qualifier
R3113 | page 58 | line 4051 | QUALIFIER | Dhruv Prakash Non-Executive Director (Upto 29 June 2026) | [I3] stand note 30 RPT list heading/qualifier
R3114 | page 58 | line 4052 | QUALIFIER | Rajesh Sawhney Independent Director (Upto 23 September 2025) | [I3] stand note 30 RPT list heading/qualifier
R3115 | page 58 | line 4086 | QUALIFIER | Indiamart Employee Benefit Trust (administered Trust to manage employees share based payment plans of the Company) | [I3] stand note 30 RPT list note/text
R3116 | page 58 | line 4088 | QUALIFIER | *With whom the Company had transactions during the reporting year. | [I3] stand note 30 RPT list heading/qualifier
R3117 | page 58 | line 4089 | QUALIFIER | ^ Transactions from 01 November 2025 | [I3] stand note 30 RPT list heading/qualifier
R3118 | page 59 | line 4103 | QUALIFIER | 30 Related party transactions (Cont'd) | [I3] stand note 30 RPT transactions heading/qualifier
R3119 | page 59 | line 4104 | QUALIFIER | The following table provides the total amount of transactions that have | [I3] stand note 30 RPT transactions note/text
R3120 | page 59 | line 4109 | QUALIFIER | Entities where KMP exercise Significant influence | [I3] stand note 30 RPT transactions heading/qualifier
R3121 | page 59 | line 4110 | QUALIFIER | Rent & related miscellaneous expenses | [I3] stand note 30 RPT transactions heading/qualifier
R3122 | page 59 | line 4113 | QUALIFIER | Tax consultancy and litigation support service | [I3] stand note 30 RPT transactions heading/qualifier
R3123 | page 59 | line 4116 | QUALIFIER | KMP and relatives of KMP's | [I3] stand note 30 RPT transactions heading/qualifier
R3124 | page 59 | line 4118 | QUALIFIER | Recruitment and training expenses | [I3] stand note 30 RPT transactions heading/qualifier
R3125 | page 59 | line 4121 | QUALIFIER | Dividend paid (refer balance outstanding) | [I3] stand note 30 RPT transactions heading/qualifier
R3126 | page 59 | line 4126 | QUALIFIER | Investments in subsidiaries | [I3] stand note 30 RPT transactions heading/qualifier
R3127 | page 59 | line 4133 | QUALIFIER | Investments in associates | [I3] stand note 30 RPT transactions heading/qualifier
R3128 | page 59 | line 4136 | QUALIFIER | Remuneration | [I3] stand note 30 RPT transactions heading/qualifier
R3129 | page 59 | line 4143 | QUALIFIER | Web, advertisement & marketing services provided to | [I3] stand note 30 RPT transactions heading/qualifier
R3130 | page 59 | line 4149 | QUALIFIER | Miscellaneous services provided to | [I3] stand note 30 RPT transactions heading/qualifier
R3131 | page 59 | line 4159 | QUALIFIER | Facilitation services availed from | [I3] stand note 30 RPT transactions heading/qualifier
R3132 | page 59 | line 4164 | QUALIFIER | Sale of Property, Plant & Equipment and Other Intangible | [I3] stand note 30 RPT transactions heading/qualifier
R3133 | page 59 | line 4167 | QUALIFIER | Share Based cost pertains to subsidiary | [I3] stand note 30 RPT transactions heading/qualifier
R3134 | page 59 | line 4171 | QUALIFIER | Pre-incorporation expenses incurred on behalf of | [I3] stand note 30 RPT transactions heading/qualifier
R3135 | page 60 | line 4181 | QUALIFIER | 30 Related party transactions (Cont'd) | [I3] stand note 30 RPT balances heading/qualifier
R3136 | page 60 | line 4184 | QUALIFIER | Balance Outstanding at the period / year end As at | [I3] stand note 30 RPT balances heading/qualifier
R3137 | page 60 | line 4187 | QUALIFIER | Subsidiary companies | [I3] stand note 30 RPT balances heading/qualifier
R3138 | page 60 | line 4188 | QUALIFIER | Investment in debt instruments of subsidiaries | [I3] stand note 30 RPT balances heading/qualifier
R3139 | page 60 | line 4189 | QUALIFIER | (Measured at FVTPL) | [I3] stand note 30 RPT balances heading/qualifier
R3140 | page 60 | line 4193 | QUALIFIER | Investment in equity/preference instruments and debentures of subsidiaries | [I3] stand note 30 RPT balances note/text
R3141 | page 60 | line 4194 | QUALIFIER | (At cost) | [I3] stand note 30 RPT balances heading/qualifier
R3142 | page 60 | line 4196 | QUALIFIER | ^ | [I3] marker on: Busy Infotech Private Limited (Formerly  | FOOTNOTE_MARKER
R3143 | page 60 | line 4199 | QUALIFIER | * | [I3] marker on: Livekeeping Technologies Private Limited | FOOTNOTE_MARKER
R3144 | page 60 | line 4203 | QUALIFIER | Investment in equity/preference instruments in associates (at cost) | [I3] stand note 30 RPT balances heading/qualifier
R3145 | page 60 | line 4205 | QUALIFIER | (refer note 7 (vii)) | [I3] cross-reference in: IB Monotaro Private Limited(refer note 7
R3146 | page 60 | line 4205 | QUALIFIER | * | [I3] marker on: IB Monotaro Private Limited(refer note 7 | FOOTNOTE_MARKER
R3147 | page 60 | line 4209 | QUALIFIER | Trade receivables | [I3] stand note 30 RPT balances heading/qualifier
R3148 | page 60 | line 4213 | QUALIFIER | Other Receivable | [I3] stand note 30 RPT balances heading/qualifier
R3149 | page 60 | line 4219 | QUALIFIER | Trade Payable (including accrued expenses) | [I3] stand note 30 RPT balances heading/qualifier
R3150 | page 60 | line 4225 | QUALIFIER | Contract Liabilities | [I3] stand note 30 RPT balances heading/qualifier
R3151 | page 60 | line 4231 | QUALIFIER | *Does not include provision for diminution of investment. | [I3] stand note 30 RPT balances heading/qualifier
R3152 | page 60 | line 4232 | QUALIFIER | ^ Includes deemed investment on account of cost of stock options allocated to employees of subsidiary companies. | [I3] stand note 30 RPT balances note/text
R3153 | page 60 | line 4234 | QUALIFIER | Terms and conditions of transactions with related parties | [I3] stand note 30 RPT balances heading/qualifier
R3154 | page 60 | line 4235 | QUALIFIER | The transactions with related parties are entered on terms equivalent to those that prevail in arm's length transactions. Outstanding | [I3] stand note 30 RPT balances note/text
R3155 | page 60 | line 4236 | QUALIFIER | balances at the period/year end are unsecured and interest free and settlement occurs in cash. There have been no guarantees provided or | [I3] stand note 30 RPT balances note/text
R3156 | page 60 | line 4237 | QUALIFIER | received for any related party receivables or payables. This assessment is undertaken each financial period through examining the | [I3] stand note 30 RPT balances note/text
R3157 | page 60 | line 4238 | QUALIFIER | financial position of the related party and the market in which the related party operates. | [I3] stand note 30 RPT balances note/text
R3158 | page 60 | line 4182 | QUALIFIER | The following table discloses the balances with related parties at the relevant period end: | [I3] stand note 30 RPT balances note/text
R3159 | page 20 | line 1494 | QUALIFIER | 9 Other assets | [I4] cons note 9 other assets heading/qualifier
R3160 | page 20 | line 1496 | QUALIFIER | Non-current (unsecured, considered good unless stated otherwise) | [I4] cons note 9 other assets heading/qualifier
R3161 | page 20 | line 1502 | QUALIFIER | Current (Unsecured, considered good unless stated otherwise) | [I4] cons note 9 other assets heading/qualifier
R3162 | page 49 | line 3539 | QUALIFIER | 11 Other assets | [I4] stand note 11 other assets heading/qualifier
R3163 | page 49 | line 3541 | QUALIFIER | Non-current (unsecured, considered good unless stated otherwise) | [I4] stand note 11 other assets heading/qualifier
R3164 | page 49 | line 3543 | QUALIFIER | (Refer Note 32 (a) | [I4] cross-reference in: Indirect taxes recoverable (Refer Note 3
R3165 | page 49 | line 3546 | QUALIFIER | Current (unsecured, considered good unless stated otherwise) | [I4] stand note 11 other assets heading/qualifier
