=== A2 COUNT TEST ===
category: slides         grep_count: 42  sweep_count: 42  match: yes   (pdfinfo 42 pages; 42 [page N] markers in fulltext)
category: slide_numbers  grep_count: 1059 sweep_count: 1059 match: yes  (NUMBER-table rows 909 grep == 909 swept across 108 page-group rows; plus ENTITY 62, FORWARD 23, DATE 35, QUALIFIER 30; header counts agree)
category: line_items     grep_count: 909 sweep_count: 909 match: yes   (slide numeric rows; P&L p27, BS p29, 5-yr p30 included)
category: zero_standing  grep_count: 5   sweep_count: 5   match: yes   (R251, R301, R302, R639, R640)
category: entities       grep_count: 62  sweep_count: 62  match: yes
category: forward        grep_count: 23  sweep_count: 23  match: yes
category: dates          grep_count: 35  sweep_count: 35  match: yes
category: footnotes_qualifiers grep_count: 30 sweep_count: 30 match: yes
category: dropped_slides prior deck: none on record -> not testable
ids_in_structured: 1059 | ids_referenced_in_ledger: 1059 | orphan_ids: [] | match: yes
gate_a2: pass
=== END COUNT TEST ===

# LEDGER: Paisalo Q2 FY27 investor presentation (ROW_ID | category | A2 flags | note)
Rows are referenced by ID range; verbatim values live in the structured file at that ID. No MISSING_FROM_STRUCTURED rows found.

## 1. SLIDES (number | title | content type)
| S1 | Cover letter to BSE/NSE (22.10.2026) | text | rows via section 2 | signature 14:12:21 IST
| S2 | Cover / Investor Presentation Q2FY2027 | text | R003 |
| S3 | Safe Harbor | text | R1031-R1032 |
| S4 | Index | text | R-none (index numerals only) | no rows; R-less slide
| S5 | Result Snapshot (divider) | divider | no rows |
| S6 | Quarter At a Glance | table/KPI | |
| S7 | Highlights for the Quarter | text | |
| S8 | Robust Financial & Operational Performance (AUM/Income) | chart | SERIES_UNRESOLVED |
| S9 | Robust Financial & Operational Performance (Yield/Spread/CoB) | chart | axis lacks Q1FY27 as printed |
| S10 | At a Glance (divider) | divider | no rows |
| S11 | Business at a Glance | text | |
| S12 | Proven through Cycles, Scaling with Stability | chart | |
| S13 | Proven through Stress, Consistent in Quality | chart | SERIES_UNRESOLVED |
| S14 | Strategic Liability Diversification / Lender Base | chart | SERIES_UNRESOLVED |
| S15 | Deepening Promoter Ownership | chart | ZERO_STANDING rows |
| S16 | Strategic Levers (divider) | divider | no rows |
| S17 | Growth Strategy | text | |
| S18 | High-Touch: Pan India Network | chart | |
| S19 | Business Correspondent | chart | FOOTNOTE_UNRESOLVED |
| S20 | Broadening Product Suite | text | |
| S21 | Scaling Loan Book with Sustained Disbursals | chart | SERIES_UNRESOLVED |
| S22 | AI Deeply Engrained Across Lending Lifecycle | text | |
| S23 | Key Initiatives in Q2FY2027 | text | |
| S24 | Strong Balance Sheet and Prudent ALM | chart | |
| S25 | Co-lending Provides Optionality | table/text | |
| S26 | Financial Performance (divider) | divider | no rows |
| S27 | Profit & Loss Summary | table | |
| S28 | RoE Tree | table | |
| S29 | Balance Sheet Summary | table | header date as printed |
| S30 | Financial Performance Over the Years | table | |
| S31 | Annexure (divider) | divider | no rows |
| S32 | Underwriting and Risk Management | text | |
| S33 | Robust Collection Efficiency | chart | |
| S34 | Shareholding Structure | table/text | |
| S35 | Backed by Experienced Board | text/photo | |
| S36 | Experienced & Professional Management | text/photo | |
| S37 | ESG (divider) | divider | no rows |
| S38 | Taking Opportunities to the Last Mile | text | footnote 6,415* |
| S39 | Our Progress on Triple A Strategy (customers) | chart | |
| S40 | Our Progress on Triple A Strategy (Accessibility) | table | |
| S41 | Sustainability Snapshot | text | |
| S42 | Thank You / contact | text | entity rows only |
Dividers with zero structured rows: S5, S10, S16, S26, S31, S37 (S4 index too); dropped-slide diff not run (no prior ledger).

## 2. SLIDE NUMBERS / LINE ITEMS (NUMBER table, 909) | range | cat | page | count | flags
| R001..R002 | NUMBER | p1 | 2 | |
| R003..R003 | NUMBER | p2 | 1 | |
| R004..R028 | NUMBER | p6 | 25 | |
| R029..R047 | NUMBER | p7 | 19 | |
| R048..R087 | NUMBER | p8 | 40 | |
| R088..R147 | NUMBER | p9 | 60 | |
| R148..R155 | NUMBER | p11 | 8 | |
| R156..R179 | NUMBER | p12 | 24 | |
| R180..R213 | NUMBER | p13 | 34 | |
| R214..R259 | NUMBER | p14 | 46 | |
| R260..R313 | NUMBER | p15 | 54 | |
| R314..R318 | NUMBER | p17 | 5 | |
| R319..R354 | NUMBER | p18 | 36 | |
| R355..R401 | NUMBER | p19 | 47 | |
| R402..R433 | NUMBER | p21 | 32 | |
| R434..R438 | NUMBER | p22 | 5 | |
| R439..R462 | NUMBER | p23 | 24 | |
| R463..R484 | NUMBER | p24 | 22 | |
| R485..R490 | NUMBER | p25 | 6 | |
| R491..R578 | NUMBER | p27 | 88 | |
| R579..R623 | NUMBER | p28 | 45 | |
| R624..R671 | NUMBER | p29 | 48 | |
| R672..R751 | NUMBER | p30 | 80 | |
| R752..R767 | NUMBER | p33 | 16 | |
| R768..R777 | NUMBER | p34 | 10 | |
| R778..R784 | NUMBER | p35 | 7 | |
| R785..R802 | NUMBER | p36 | 18 | |
| R803..R809 | NUMBER | p38 | 7 | |
| R810..R824 | NUMBER | p39 | 15 | |
| R825..R902 | NUMBER | p40 | 78 | |
| R903..R909 | NUMBER | p41 | 7 | |

Flags inside NUMBER ranges: SERIES_UNRESOLVED on 57 rows (p8 R065-R066 Q3FY26 income pair, p13 1-decimal series R181-R182, p14 lender mix, p21 business mix); ZERO_STANDING on R251, R301, R302, R639, R640 (R639/R640 tax assets nil both periods, balance sheet standing line). Page-anchored-only: R030, R315, R447, R449, R784. Restated: AUM 72,659 on p6 R004 / p7 R030 / p21; PAT 656 on p6 R028 / p7. p29 header '31st September, 2025' printed (non-existent date, flag as printed).

## 3. ENTITIES (62, R910-R971) | cat entity | flags: none ENTITY_CHANGE (no prior list); R934 page-anchored only
| R910..R915 | ENTITY | p1 | 6 | |
| R916..R916 | ENTITY | p3 | 1 | |
| R917..R917 | ENTITY | p4 | 1 | |
| R918..R918 | ENTITY | p6 | 1 | |
| R919..R919 | ENTITY | p11 | 1 | |
| R920..R926 | ENTITY | p12 | 7 | |
| R927..R929 | ENTITY | p14 | 3 | |
| R930..R930 | ENTITY | p15 | 1 | |
| R931..R932 | ENTITY | p17 | 2 | |
| R933..R933 | ENTITY | p18 | 1 | |
| R934..R937 | ENTITY | p19 | 4 | |
| R938..R939 | ENTITY | p20 | 2 | |
| R940..R940 | ENTITY | p21 | 1 | |
| R941..R941 | ENTITY | p22 | 1 | |
| R942..R942 | ENTITY | p25 | 1 | |
| R943..R943 | ENTITY | p34 | 1 | |
| R944..R955 | ENTITY | p35 | 12 | |
| R956..R968 | ENTITY | p36 | 13 | |
| R969..R969 | ENTITY | p38 | 1 | |
| R970..R970 | ENTITY | p41 | 1 | |
| R971..R971 | ENTITY | p42 | 1 | |

## 4. FORWARD (23, R972-R994) | R972 page-anchored only
| R972..R972 | FORWARD | p6 | 1 | |
| R973..R977 | FORWARD | p7 | 5 | |
| R978..R979 | FORWARD | p11 | 2 | |
| R980..R980 | FORWARD | p13 | 1 | |
| R981..R986 | FORWARD | p17 | 6 | |
| R987..R987 | FORWARD | p20 | 1 | |
| R988..R988 | FORWARD | p22 | 1 | |
| R989..R989 | FORWARD | p23 | 1 | |
| R990..R990 | FORWARD | p24 | 1 | |
| R991..R992 | FORWARD | p25 | 2 | |
| R993..R993 | FORWARD | p32 | 1 | |
| R994..R994 | FORWARD | p41 | 1 | |

## 5. DATES (35, R995-R1029)
| R995..R996 | DATE | p1 | 2 | |
| R997..R997 | DATE | p2 | 1 | |
| R998..R998 | DATE | p6 | 1 | |
| R999..R1002 | DATE | p7 | 4 | |
| R1003..R1003 | DATE | p8 | 1 | |
| R1004..R1004 | DATE | p9 | 1 | |
| R1005..R1005 | DATE | p11 | 1 | |
| R1006..R1009 | DATE | p12 | 4 | |
| R1010..R1010 | DATE | p13 | 1 | |
| R1011..R1012 | DATE | p14 | 2 | |
| R1013..R1015 | DATE | p15 | 3 | |
| R1016..R1016 | DATE | p18 | 1 | |
| R1017..R1017 | DATE | p19 | 1 | |
| R1018..R1018 | DATE | p21 | 1 | |
| R1019..R1019 | DATE | p23 | 1 | |
| R1020..R1020 | DATE | p24 | 1 | |
| R1021..R1021 | DATE | p27 | 1 | |
| R1022..R1022 | DATE | p28 | 1 | |
| R1023..R1023 | DATE | p29 | 1 | |
| R1024..R1024 | DATE | p30 | 1 | |
| R1025..R1025 | DATE | p33 | 1 | |
| R1026..R1026 | DATE | p34 | 1 | |
| R1027..R1027 | DATE | p39 | 1 | |
| R1028..R1028 | DATE | p40 | 1 | |
| R1029..R1029 | DATE | p41 | 1 | |

## 6. FOOTNOTES / QUALIFIERS (30, R1030-R1059) | R1037 and R1048 FOOTNOTE_UNRESOLVED (p8 pair order; p19 '#' markers no text); R1056-R1057 footnote 6,415* resolved (426+1,690+4,299)
| R1030..R1030 | QUALIFIER | p1 | 1 | |
| R1031..R1032 | QUALIFIER | p3 | 2 | |
| R1033..R1035 | QUALIFIER | p6 | 3 | |
| R1036..R1036 | QUALIFIER | p7 | 1 | |
| R1037..R1037 | QUALIFIER | p8 | 1 | |
| R1038..R1038 | QUALIFIER | p9 | 1 | |
| R1039..R1041 | QUALIFIER | p12 | 3 | |
| R1042..R1043 | QUALIFIER | p14 | 2 | |
| R1044..R1046 | QUALIFIER | p15 | 3 | |
| R1047..R1047 | QUALIFIER | p17 | 1 | |
| R1048..R1048 | QUALIFIER | p19 | 1 | |
| R1049..R1049 | QUALIFIER | p24 | 1 | |
| R1050..R1052 | QUALIFIER | p25 | 3 | |
| R1053..R1053 | QUALIFIER | p27 | 1 | |
| R1054..R1054 | QUALIFIER | p28 | 1 | |
| R1055..R1055 | QUALIFIER | p29 | 1 | |
| R1056..R1057 | QUALIFIER | p38 | 2 | |
| R1058..R1058 | QUALIFIER | p40 | 1 | |
| R1059..R1059 | QUALIFIER | p41 | 1 | |
