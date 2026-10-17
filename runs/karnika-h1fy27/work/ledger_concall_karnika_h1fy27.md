# A2 LEDGER: Karnika concall H1 FY27 (KARNIKA)
Source: A1 structured extraction R001-R246. IDs reference A1 rows; verbatim text lives there. Turn 0 = cover letter / cover page before the transcript (no speaker turn). Turn lines are A1 fulltext lines.

## Loop 2 delta
1. M006 added (L378, T24, "two growth drivers", spoken in words): mgmt_numbers 105 -> 106.
2. Audit list L156-160, L196-199, L228-230, L521-524, L684-685, L704-707, L1094-1095 plus secondary L531, L869-870, L1051-1053: all 10 read at fulltext and all are management forward statements, appended as M007-M016 (sec 5b). Weak intent statements with no number or date: M009 (focus "remains"), M013 (closing "Hopefully"), M015 (aspiration); kept as forward rows, none rejected. M014 mixes a forward clause ("will be only for brands of brand") with a present-tense fact (SIS garmenting); the forward clause is tagged.
3. Independent forward-phrase sweep (lexicon: will, would, target, expect*, plan*, going to, by FY/end, hope*, aim*, intend*, looking to, want to, soon, next quarter/year/phase) over management turns: 123 phrase hits on 95 lines. Line reconciliation: 57 lines sit in the span (same turn, within 6 lines) of an existing A1 FORWARD/QUALIFIER row; 17 lines fall in the new M-row spans (M007-M020); 21 lines are non-forward (thanks/hand-over L202-203, L233; descriptive billing flow L258-259, L764-767, L906; estimates "would be" L467, L480, L513, L570; descriptive "will see" L639, L700, L1016-1018, L829; growth "by 52%" L215). Unmapped lines: 0. 57 + 17 + 21 = 95.
4. The sweep found 4 further uncovered forward statements beyond the audit list, added as M017-M020 (L551-554, L670, L851, L859). The lexicon misses intent verbs (objective, priority, focus), so the audit list stays as a second route; M007, M008 and M009 were found only by the audit.
5. Forward count: structured FORWARD 47 + 14 new (M007-M020) = 61 management forward-statement rows. The Loop 1 test compared A1 tags with A1 tags (47 = 47) and was not independent. The new test is independent: 0 unmapped sweep lines after the 14 additions. A row-for-row count match is not possible, because one A1 row can span several hit lines and one line can hold several phrases; the match is made at line-cluster level.
6. ids_in_structured (246), turns (167), questions (67), participants and other categories unchanged. missing_from_structured: M001-M020.

## Loop 1 delta
1. T87 (fulltext L723-725, "This is across both your outlets like your...", answered "Yes" at T88) reclassified from acknowledgement to question: same kind as T60/T79/T124/T130/T136. Inserted as q36; later questions renumbered q37-q67. Questions 66 -> 67.
2. Five words-written management numbers added as MISSING_FROM_STRUCTURED: M001 (L306), M002 (L704-705), M003 (L867), M004 (L901), M005 (L1027). mgmt_numbers 100 -> 105. missing_from_structured: [M001..M005].
3. ids_in_structured, turns (167), participants and the other categories are unchanged.

ids_in_structured: 246 | ids_referenced_in_ledger: 246 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: struct_ids       grep_count: 246   sweep_count: 246   match: yes
category: participants     grep_count: 8   sweep_count: 8   match: yes
category: turns            grep_count: 167   sweep_count: 167   match: yes
category: questions        grep_count: 67   sweep_count: 67   match: yes
category: mgmt_numbers     grep_count: 106   sweep_count: 106   match: yes
category: forward_phrases  grep_count: 61   sweep_count: 61   match: yes
category: hedge_qualifiers grep_count: 20   sweep_count: 20   match: yes
category: dates            grep_count: 22   sweep_count: 22   match: yes
category: entities         grep_count: 53   sweep_count: 53   match: yes
category: zero_standing    grep_count: 0   sweep_count: 0   match: yes
notes: A1 header counts NUMBER 104 | ENTITY 53 | FORWARD 47 | DATE 22 | QUALIFIER 20 re-grepped by TYPE: matched. Turns: speaker-label regex on fulltext (167) vs line-range sweep (167). Questions: analyst turns less 8 acknowledgement turns (T37,64,89,113,117,134,140,163) and 2 audibility checks (T13,T67) = 67 (Loop 1: T87 moved from acknowledgement to question); the grep for "?" hit 81 lines, reconciled by manual sweep (several turns hold 2+ question marks, some questions have none).
mgmt_numbers: 104 NUMBER rows minus R001 (cover DIN), R050/R072/R103 (analyst-spoken) = 100, plus 5 MISSING_FROM_STRUCTURED rows M001-M005 (Loop 1) plus M006 (Loop 2) = 106.
Independent digit sweep of management turns against NUMBER row lines found only date/tier/B2B label hits plus L859 (INR199-499 restated, covered by R066) and L657 (100% domestic, covered by R204). Loop 1 audit then found 5 words-written management numbers the digit sweep missed: M001-M005 (sec 4).
gate_a2: pass
=== END COUNT TEST ===

## 1. PARTICIPANTS (8 distinct)
| # | name | designation / firm | side | IDs | flags |
|---|---|---|---|---|---|
| 1 | Niranjan Mundhra | Managing Director, Karnika | mgmt | R001 R110 R111 | NAME_VARIANT; MD_SILENT_IN_QA (speaks T3 only; every Q&A answer from T7 is the CFO) |
| 2 | Krishan Karnani | CFO, Karnika | mgmt | R112 | answers all Q&A |
| 3 | Mehal Gogia | Go India Advisors (host/moderator) | host | R113 R157 | - |
| 4 | Gunit Singh | Counter Cyclical | analyst | R114 | - |
| 5 | Disha | Sapphire Capital | analyst | R115 | - |
| 6 | Ashish Soni | MM Capital | analyst | R116 | two separate slots (T40-T64, T143-T161) |
| 7 | Saransh Gupta | SVAN Investments | analyst | R117 | - |
| 8 | Kamal Jeswani | You-First Capital | analyst | R118 | moderator says "Mr. Jeswani" |
MGMT_ABSENCE check: MD present (R111) but gives no Q&A answers; CFO alone answers.

## 2. SPEAKER TURNS (167)
| turn | speaker | A1 fulltext lines | words | A1 IDs in turn |
|---|---|---|---|---|
| 1 | Moderator | 88-99 | 101 | - |
| 2 | Mehal Gogia | 100-111 | 116 | R229 |
| 3 | Niranjan Mundhra | 112-213 | 725 | R002 R003 R004 R005 R006 R007 R008 R009 R010 R011 R012 R013 R014 R015 R016 R119 R121 R122 R123 R124 R156 R158 R159 R160 R161 R162 R163 R164 R165 R211 R212 R213 R214 R215 R230 R246 |
| 4 | Krishan Karnani | 214-236 | 177 | R017 R018 R019 R020 R021 R022 R023 R024 R025 R026 R027 R028 R029 R030 R031 R032 R033 R034 R035 R036 R037 R216 R217 R231 R242 R243 |
| 5 | Moderator | 237-241 | 33 | R114 |
| 6 | Gunit Singh | 242-245 | 29 | - |
| 7 | Krishan Karnani | 246-248 | 18 | R038 R039 |
| 8 | Gunit Singh | 249-254 | 60 | - |
| 9 | Krishan Karnani | 255-280 | 214 | R040 R041 R042 R120 R125 |
| 10 | Gunit Singh | 281-285 | 50 | - |
| 11 | Krishan Karnani | 286-321 | 386 | R043 R044 R045 R046 R047 R048 R126 R127 R128 R129 R131 R133 R134 R135 R136 R137 R234 |
| 12 | Moderator | 322-325 | 18 | R115 |
| 13 | Disha | 326-328 | 5 | - |
| 14 | Krishan Karnani | 329-331 | 6 | - |
| 15 | Disha | 332-344 | 78 | - |
| 16 | Krishan Karnani | 345-349 | 44 | R166 R167 R226 |
| 17 | Disha | 350-352 | 10 | - |
| 18 | Krishan Karnani | 353-356 | 32 | R168 R218 |
| 19 | Disha | 357-359 | 21 | - |
| 20 | Krishan Karnani | 360-366 | 70 | R169 R219 |
| 21 | Disha | 367-369 | 19 | R050 |
| 22 | Krishan Karnani | 370-372 | 12 | R049 R170 |
| 23 | Disha | 373-377 | 38 | - |
| 24 | Krishan Karnani | 378-391 | 170 | - |
| 25 | Disha | 392-394 | 15 | - |
| 26 | Krishan Karnani | 395-398 | 20 | R051 R052 R053 R233 |
| 27 | Disha | 399-402 | 19 | - |
| 28 | Krishan Karnani | 403-414 | 55 | R054 R055 R171 R172 R232 |
| 29 | Disha | 415-417 | 18 | - |
| 30 | Krishan Karnani | 418-420 | 11 | R056 R173 |
| 31 | Disha | 421-424 | 28 | - |
| 32 | Krishan Karnani | 425-430 | 64 | R057 R174 R175 |
| 33 | Disha | 431-434 | 28 | - |
| 34 | Krishan Karnani | 435-441 | 87 | R152 R176 R177 R220 |
| 35 | Disha | 442-444 | 5 | - |
| 36 | Krishan Karnani | 445-450 | 74 | R058 R059 R178 R225 |
| 37 | Disha | 451-453 | 16 | - |
| 38 | Krishan Karnani | 454-456 | 6 | - |
| 39 | Moderator | 457-460 | 19 | R116 |
| 40 | Ashish Soni | 461-465 | 40 | - |
| 41 | Krishan Karnani | 466-483 | 116 | R060 R061 R062 R063 R064 R151 R179 R224 |
| 42 | Ashish Soni | 484-487 | 27 | - |
| 43 | Krishan Karnani | 488-494 | 82 | R065 R140 R141 |
| 44 | Ashish Soni | 495-498 | 37 | - |
| 45 | Krishan Karnani | 499-504 | 70 | R180 |
| 46 | Ashish Soni | 505-510 | 54 | - |
| 47 | Krishan Karnani | 511-517 | 80 | R066 R067 R181 |
| 48 | Ashish Soni | 518-520 | 12 | - |
| 49 | Krishan Karnani | 521-526 | 55 | - |
| 50 | Ashish Soni | 527-530 | 28 | - |
| 51 | Krishan Karnani | 531-534 | 35 | R068 |
| 52 | Ashish Soni | 535-538 | 27 | - |
| 53 | Krishan Karnani | 539-556 | 143 | R146 R148 R182 R237 |
| 54 | Ashish Soni | 557-561 | 48 | - |
| 55 | Krishan Karnani | 562-574 | 153 | R069 R070 R236 R241 |
| 56 | Ashish Soni | 575-577 | 19 | - |
| 57 | Krishan Karnani | 578-583 | 58 | R071 R143 R144 R145 R183 |
| 58 | Ashish Soni | 584-586 | 21 | R072 |
| 59 | Krishan Karnani | 587-589 | 18 | R184 R221 R245 |
| 60 | Ashish Soni | 590-592 | 14 | - |
| 61 | Krishan Karnani | 593-595 | 3 | - |
| 62 | Ashish Soni | 596-599 | 29 | - |
| 63 | Krishan Karnani | 600-605 | 61 | R073 R074 R075 R185 R186 R222 |
| 64 | Ashish Soni | 606-612 | 25 | - |
| 65 | Krishan Karnani | 613-615 | 9 | - |
| 66 | Moderator | 616-619 | 19 | R117 |
| 67 | Saransh Gupta | 620-622 | 6 | - |
| 68 | Krishan Karnani | 623-625 | 7 | - |
| 69 | Saransh Gupta | 626-630 | 42 | - |
| 70 | Krishan Karnani | 631-633 | 3 | - |
| 71 | Saransh Gupta | 634-638 | 38 | - |
| 72 | Krishan Karnani | 639-652 | 150 | - |
| 73 | Saransh Gupta | 653-656 | 24 | - |
| 74 | Krishan Karnani | 657-659 | 12 | R204 |
| 75 | Saransh Gupta | 660-663 | 21 | - |
| 76 | Krishan Karnani | 664-666 | 18 | R076 R203 |
| 77 | Saransh Gupta | 667-669 | 21 | - |
| 78 | Krishan Karnani | 670-673 | 32 | R077 R078 |
| 79 | Saransh Gupta | 674-683 | 25 | - |
| 80 | Krishan Karnani | 684-687 | 27 | - |
| 81 | Saransh Gupta | 688-690 | 18 | - |
| 82 | Krishan Karnani | 691-693 | 5 | - |
| 83 | Saransh Gupta | 694-696 | 21 | - |
| 84 | Krishan Karnani | 697-715 | 197 | R079 R187 R223 |
| 85 | Saransh Gupta | 716-718 | 19 | - |
| 86 | Krishan Karnani | 719-722 | 28 | R080 R081 R188 R235 |
| 87 | Saransh Gupta | 723-725 | 10 | - (QUESTION, Loop 1) |
| 88 | Krishan Karnani | 726-728 | 16 | - |
| 89 | Saransh Gupta | 729-731 | 12 | - |
| 90 | Moderator | 732-735 | 19 | - |
| 91 | Gunit Singh | 736-739 | 23 | - |
| 92 | Krishan Karnani | 740-742 | 17 | R082 R083 |
| 93 | Gunit Singh | 743-753 | 43 | - |
| 94 | Krishan Karnani | 754-770 | 173 | R084 R085 R138 R139 R239 R240 |
| 95 | Gunit Singh | 771-773 | 14 | - |
| 96 | Krishan Karnani | 774-777 | 30 | - |
| 97 | Gunit Singh | 778-781 | 23 | - |
| 98 | Krishan Karnani | 782-785 | 26 | - |
| 99 | Gunit Singh | 786-789 | 36 | - |
| 100 | Krishan Karnani | 790-801 | 140 | R086 R087 R088 R089 R090 R130 R189 R190 |
| 101 | Gunit Singh | 802-804 | 14 | - |
| 102 | Krishan Karnani | 805-810 | 55 | R091 R092 |
| 103 | Gunit Singh | 811-820 | 32 | - |
| 104 | Krishan Karnani | 821-824 | 29 | R093 R191 |
| 105 | Gunit Singh | 825-827 | 12 | - |
| 106 | Krishan Karnani | 828-834 | 78 | - |
| 107 | Gunit Singh | 835-837 | 15 | - |
| 108 | Krishan Karnani | 838-840 | 12 | - |
| 109 | Gunit Singh | 841-843 | 15 | - |
| 110 | Krishan Karnani | 844-846 | 11 | R094 R153 |
| 111 | Gunit Singh | 847-850 | 24 | - |
| 112 | Krishan Karnani | 851-854 | 20 | - |
| 113 | Gunit Singh | 855-857 | 3 | - |
| 114 | Krishan Karnani | 858-861 | 38 | - |
| 115 | Gunit Singh | 862-865 | 30 | R142 |
| 116 | Krishan Karnani | 866-872 | 88 | - |
| 117 | Gunit Singh | 873-875 | 14 | - |
| 118 | Krishan Karnani | 876-878 | 7 | - |
| 119 | Moderator | 879-882 | 19 | R118 |
| 120 | Kamal Jeswani | 883-892 | 39 | - |
| 121 | Krishan Karnani | 893-897 | 36 | R095 |
| 122 | Kamal Jeswani | 898-900 | 16 | - |
| 123 | Krishan Karnani | 901-908 | 102 | R096 R097 R238 |
| 124 | Kamal Jeswani | 909-911 | 7 | - |
| 125 | Krishan Karnani | 912-914 | 3 | - |
| 126 | Kamal Jeswani | 915-917 | 9 | - |
| 127 | Krishan Karnani | 918-921 | 19 | R098 R099 |
| 128 | Kamal Jeswani | 922-925 | 25 | - |
| 129 | Krishan Karnani | 926-928 | 19 | - |
| 130 | Kamal Jeswani | 929-931 | 10 | - |
| 131 | Krishan Karnani | 932-935 | 32 | - |
| 132 | Kamal Jeswani | 936-938 | 9 | - |
| 133 | Krishan Karnani | 939-941 | 12 | R154 |
| 134 | Kamal Jeswani | 942-944 | 3 | - |
| 135 | Krishan Karnani | 945-947 | 4 | - |
| 136 | Kamal Jeswani | 948-950 | 6 | - |
| 137 | Krishan Karnani | 951-954 | 21 | R155 R192 |
| 138 | Kamal Jeswani | 955-957 | 10 | - |
| 139 | Krishan Karnani | 958-966 | 30 | R193 |
| 140 | Kamal Jeswani | 967-969 | 14 | - |
| 141 | Krishan Karnani | 970-972 | 4 | - |
| 142 | Moderator | 973-976 | 19 | - |
| 143 | Ashish Soni | 977-980 | 28 | - |
| 144 | Krishan Karnani | 981-985 | 51 | R194 R195 |
| 145 | Ashish Soni | 986-988 | 12 | - |
| 146 | Krishan Karnani | 989-995 | 81 | R196 |
| 147 | Ashish Soni | 996-999 | 22 | - |
| 148 | Krishan Karnani | 1000-1004 | 50 | R197 |
| 149 | Ashish Soni | 1005-1008 | 20 | - |
| 150 | Krishan Karnani | 1009-1011 | 17 | R198 |
| 151 | Ashish Soni | 1012-1015 | 30 | - |
| 152 | Krishan Karnani | 1016-1022 | 74 | R132 |
| 153 | Ashish Soni | 1023-1025 | 14 | - |
| 154 | Krishan Karnani | 1026-1035 | 49 | R100 R149 R150 |
| 155 | Ashish Soni | 1036-1040 | 50 | - |
| 156 | Krishan Karnani | 1041-1060 | 201 | R101 R147 R199 |
| 157 | Ashish Soni | 1061-1064 | 23 | - |
| 158 | Krishan Karnani | 1065-1067 | 11 | R102 R200 |
| 159 | Ashish Soni | 1068-1070 | 10 | R103 |
| 160 | Krishan Karnani | 1071-1074 | 20 | R104 R201 R244 |
| 161 | Ashish Soni | 1075-1078 | 21 | - |
| 162 | Krishan Karnani | 1079-1083 | 39 | R202 |
| 163 | Ashish Soni | 1084-1086 | 11 | - |
| 164 | Krishan Karnani | 1087-1089 | 7 | - |
| 165 | Moderator | 1090-1093 | 35 | - |
| 166 | Krishan Karnani | 1094-1102 | 46 | - |
| 167 | Moderator | 1103-1110 | 33 | R157 |
Turn 0 IDs (cover letter/cover page): R001 R105 R106 R107 R108 R109 R110 R111 R112 R113 R205 R206 R207 R208 R209 R210 R227 R228
Turn split: Krishan Karnani 78, Niranjan Mundhra 1, analysts 77, Moderator/host 11. Prepared remarks T3-T4 (lines 112-236); Q&A T5-T167.

## 3. QUESTIONS LEDGER (67)
| q# | turn | analyst | firm | topic | A2 flags |
|---|---|---|---|---|---|
| 1 | 6 | Gunit Singh | Counter Cyclical | own brand vs white label split | - |
| 2 | 8 | Gunit Singh | Counter Cyclical | sales channel mix (distributors) | - |
| 3 | 10 | Gunit Singh | Counter Cyclical | revenue by model, B2B meaning | - |
| 4 | 15 | Disha | Sapphire Capital | margin moderation, raw material | - |
| 5 | 17 | Disha | Sapphire Capital | raw material price outlook | - |
| 6 | 19 | Disha | Sapphire Capital | pass-through to consumer | - |
| 7 | 21 | Disha | Sapphire Capital | FY margin range | - |
| 8 | 23 | Disha | Sapphire Capital | Q2 growth drivers and growth forecast | - |
| 9 | 25 | Disha | Sapphire Capital | H1 Kidcity contribution | - |
| 10 | 27 | Disha | Sapphire Capital | Kidcity revenue this year/next | - |
| 11 | 29 | Disha | Sapphire Capital | Kidcity margin | - |
| 12 | 31 | Disha | Sapphire Capital | Karnika business outlook | - |
| 13 | 33 | Disha | Sapphire Capital | store additions and capex | - |
| 14 | 35 | Disha | Sapphire Capital | capex numbers (follow-up) | REPEAT_QUESTION (follow-up on T33 capex) |
| 15 | 40 | Ashish Soni | MM Capital | EBO/SIS capex and inventory | - |
| 16 | 42 | Ashish Soni | MM Capital | competitors and ASP | - |
| 17 | 44 | Ashish Soni | MM Capital | airport stores vs Brands of Brand | - |
| 18 | 46 | Ashish Soni | MM Capital | metro/tier positioning | - |
| 19 | 48 | Ashish Soni | MM Capital | accessories type | - |
| 20 | 50 | Ashish Soni | MM Capital | accessories scope SIS/EBO | - |
| 21 | 52 | Ashish Soni | MM Capital | Brands of Brand marketing spend | - |
| 22 | 54 | Ashish Soni | MM Capital | airport break-even | - |
| 23 | 56 | Ashish Soni | MM Capital | airports in plan | - |
| 24 | 58 | Ashish Soni | MM Capital | timing of 50 stores | - |
| 25 | 60 | Ashish Soni | MM Capital | confirm 50 stores total | REPEAT_QUESTION (confirm of T58 count) |
| 26 | 62 | Ashish Soni | MM Capital | growth plan beyond FY28 | - |
| 27 | 69 | Saransh Gupta | SVAN Investments | unorganised to organised shift | - |
| 28 | 71 | Saransh Gupta | SVAN Investments | differentiation vs regional players | - |
| 29 | 73 | Saransh Gupta | SVAN Investments | domestic vs exports | - |
| 30 | 75 | Saransh Gupta | SVAN Investments | store inventory and break-even | - |
| 31 | 77 | Saransh Gupta | SVAN Investments | store count by FY28 | - |
| 32 | 79 | Saransh Gupta | SVAN Investments | airport share of stores | - |
| 33 | 81 | Saransh Gupta | SVAN Investments | mall vs airport economics | REPEAT_QUESTION (restated at T83) |
| 34 | 83 | Saransh Gupta | SVAN Investments | mall vs airport economics (restated) | REPEAT_QUESTION (same analyst, repeat of T81) |
| 35 | 85 | Saransh Gupta | SVAN Investments | revenue from EBO segment | - |
| 36 | 87 | Saransh Gupta | SVAN Investments | clarify scope of INR50 lakh per EBO target (airport and malls?) | CLARIFYING_FOLLOWUP (Loop 1 reclass, 6-word turn, ends with ellipsis, no ?) |
| 37 | 91 | Gunit Singh | Counter Cyclical | B2B share of Karnika sales | REPEAT_QUESTION (repeat of T6; same analyst, follow-up) |
| 38 | 93 | Gunit Singh | Counter Cyclical | meaning of B2B | - |
| 39 | 95 | Gunit Singh | Counter Cyclical | local shops as end customers | - |
| 40 | 97 | Gunit Singh | Counter Cyclical | brand name used in Kidcity | - |
| 41 | 99 | Gunit Singh | Counter Cyclical | B2B payment terms and growth | - |
| 42 | 101 | Gunit Singh | Counter Cyclical | inventory returns | - |
| 43 | 103 | Gunit Singh | Counter Cyclical | 30-35% growth driven by Kidcity | REPEAT_QUESTION (growth-driver theme, cf T23) |
| 44 | 105 | Gunit Singh | Counter Cyclical | Kidcity working capital cycle | - |
| 45 | 107 | Gunit Singh | Counter Cyclical | future WC intensity | - |
| 46 | 109 | Gunit Singh | Counter Cyclical | Kidcity EBO count | - |
| 47 | 111 | Gunit Singh | Counter Cyclical | EBO location plan | - |
| 48 | 115 | Gunit Singh | Counter Cyclical | comparison with Purple United / FirstCry | - |
| 49 | 120 | Kamal Jeswani | You-First Capital | states of presence | - |
| 50 | 122 | Kamal Jeswani | You-First Capital | regional bifurcation | - |
| 51 | 124 | Kamal Jeswani | You-First Capital | North and Central share | - |
| 52 | 126 | Kamal Jeswani | You-First Capital | South India presence | - |
| 53 | 128 | Kamal Jeswani | You-First Capital | own brand vs wholesaler | REPEAT_QUESTION (B2B channel, cf T91/T93) |
| 54 | 130 | Kamal Jeswani | You-First Capital | Kidcity own brand channel | REPEAT_QUESTION (channel, cf T97) |
| 55 | 132 | Kamal Jeswani | You-First Capital | region of max sales | - |
| 56 | 136 | Kamal Jeswani | You-First Capital | East India concentration | - |
| 57 | 138 | Kamal Jeswani | You-First Capital | expansion plan | - |
| 58 | 143 | Ashish Soni | MM Capital | debt plan with expansion | - |
| 59 | 145 | Ashish Soni | MM Capital | funding timing | - |
| 60 | 147 | Ashish Soni | MM Capital | manufacturing capacity | - |
| 61 | 149 | Ashish Soni | MM Capital | accessories make vs outsource | - |
| 62 | 151 | Ashish Soni | MM Capital | FirstCry white label brands | - |
| 63 | 153 | Ashish Soni | MM Capital | FirstCry brand names | REPEAT_QUESTION (repeat of T151) |
| 64 | 155 | Ashish Soni | MM Capital | marketing plan | - |
| 65 | 157 | Ashish Soni | MM Capital | number of licensed brands | - |
| 66 | 159 | Ashish Soni | MM Capital | licence cost (INR10 cr) | - |
| 67 | 161 | Ashish Soni | MM Capital | own character plan | - |
REPEAT_QUESTION rows: 9.

## 4. MANAGEMENT NUMBERS (106 spoken incl. 6 MISSING_FROM_STRUCTURED, 4 non-mgmt flagged)
| ID | page | A1 line | turn | A2 flags | cross-ref |
|---|---|---|---|---|---|
| R001 | page 1 | 64 | 0 | NON_SPOKEN (cover letter) | - |
| R002 | page 3 | 129 | 3 | - | - |
| R003 | page 3 | 131 | 3 | RESTATED | R043 |
| R004 | page 3 | 132 | 3 | RESTATED | R095 |
| R005 | page 3 | 132 | 3 | - | - |
| R006 | page 3 | 132 | 3 | - | - |
| R007 | page 3 | 132 | 3 | - | - |
| R008 | page 4 | 164 | 3 | RESTATED | R041 |
| R009 | page 4 | 164 | 3 | - | - |
| R010 | page 4 | 165 | 3 | RESTATED, DIVERGENCE_CHECK (55-plus kiosks R010/R160 vs ~50 stores R184/R072/R245) | R160 |
| R011 | page 4 | 180 | 3 | RESTATED | R012 R246 |
| R012 | page 4 | 180 | 3 | RESTATED | R011 R246 |
| R013 | page 4 | 181 | 3 | - | - |
| R014 | page 4 | 189 | 3 | RESTATED | R164 |
| R015 | page 4 | 189 | 3 | RESTATED | R164 |
| R016 | page 4 | 190 | 3 | RESTATED | R049 R165 R170 |
| R017 | page 5 | 215 | 4 | - | - |
| R018 | page 5 | 216 | 4 | RESTATED | R028 R053 |
| R019 | page 5 | 216 | 4 | - | - |
| R020 | page 5 | 216 | 4 | - | - |
| R021 | page 5 | 217 | 4 | - | - |
| R022 | page 5 | 217 | 4 | - | - |
| R023 | page 5 | 221 | 4 | - | - |
| R024 | page 5 | 221 | 4 | - | - |
| R025 | page 5 | 222 | 4 | - | - |
| R026 | page 5 | 222 | 4 | - | - |
| R027 | page 5 | 223 | 4 | - | - |
| R028 | page 5 | 223 | 4 | RESTATED | R018 R053 |
| R029 | page 5 | 223 | 4 | - | - |
| R030 | page 5 | 223 | 4 | - | - |
| R031 | page 5 | 224 | 4 | - | - |
| R032 | page 5 | 224 | 4 | - | - |
| R033 | page 5 | 227 | 4 | - | - |
| R034 | page 5 | 227 | 4 | APPROX_FIGURE | - |
| R035 | page 5 | 228 | 4 | - | - |
| R036 | page 5 | 228 | 4 | - | - |
| R037 | page 5 | 228 | 4 | - | - |
| R038 | page 5 | 246 | 7 | RESTATED | R046 R082 |
| R039 | page 5 | 246 | 7 | RESTATED | R047 R083 |
| R040 | page 5 | 264 | 9 | - | - |
| R041 | page 5 | 265 | 9 | RESTATED | R008 |
| R042 | page 5 | 270 | 9 | - | - |
| R043 | page 6 | 286 | 11 | RESTATED | R003 |
| R044 | page 6 | 287 | 11 | - | - |
| R045 | page 6 | 294 | 11 | RESTATED | R051 |
| R046 | page 6 | 298 | 11 | RESTATED | R038 R082 |
| R047 | page 6 | 298 | 11 | RESTATED | R039 R083 |
| R048 | page 6 | 308 | 11 | - | - |
| R049 | page 7 | 370 | 22 | RESTATED, RANGE_WIDENED_FROM_ANALYST_18-19 (cf R050) | R016 R165 R170 |
| R050 | page 7 | 367 | 21 | ANALYST_STATED_NOT_MGMT | - |
| R051 | page 7 | 395 | 26 | RESTATED | R045 |
| R052 | page 7 | 395 | 26 | - | - |
| R053 | page 7 | 396 | 26 | RESTATED | R018 R028 |
| R054 | page 7 | 403 | 28 | RESTATED | R171 |
| R055 | page 8 | 412 | 28 | RESTATED | R172 |
| R056 | page 8 | 418 | 30 | RESTATED | R173 |
| R057 | page 8 | 425 | 32 | RESTATED | R174 |
| R058 | page 8 | 445 | 36 | RESTATED | R060 |
| R059 | page 8 | 448 | 36 | RESTATED | R178 |
| R060 | page 8 | 466 | 41 | RESTATED | R058 |
| R061 | page 8 | 467 | 41 | - | - |
| R062 | page 8 | 467 | 41 | - | - |
| R063 | page 9 | 480 | 41 | RESTATED | R064 |
| R064 | page 9 | 480 | 41 | RESTATED | R063 |
| R065 | page 9 | 488 | 43 | RESTATED | R066 R067 R068 |
| R066 | page 9 | 513 | 47 | RESTATED, RESTATED_ALSO_L859 (INR199-499 restated in EBO context, no new ID needed) | R065 R067 R068 |
| R067 | page 9 | 514 | 47 | RESTATED | R065 R066 R068 |
| R068 | page 9 | 532 | 51 | RESTATED | R065 R066 R067 |
| R069 | page 10 | 570 | 55 | - | - |
| R070 | page 10 | 572 | 55 | - | - |
| R071 | page 10 | 578 | 57 | - | - |
| R072 | page 10 | 584 | 58 | RESTATED, ANALYST_STATED_NOT_MGMT | R184 R245 |
| R073 | page 10 | 600 | 63 | RESTATED | R185 |
| R074 | page 10 | 601 | 63 | RESTATED | R077 R186 |
| R075 | page 10 | 602 | 63 | RESTATED | R078 R186 |
| R076 | page 11 | 664 | 76 | RESTATED | R203 |
| R077 | page 11 | 670 | 78 | RESTATED | R074 R186 |
| R078 | page 11 | 671 | 78 | RESTATED | R075 R186 |
| R079 | page 12 | 697 | 84 | - | - |
| R080 | page 12 | 719 | 86 | RESTATED | R081 R188 |
| R081 | page 12 | 720 | 86 | RESTATED | R080 R188 |
| R082 | page 12 | 740 | 92 | RESTATED | R038 R046 |
| R083 | page 12 | 740 | 92 | RESTATED | R039 R047 |
| R084 | page 13 | 756 | 94 | - | - |
| R085 | page 13 | 766 | 94 | - | - |
| R086 | page 13 | 791 | 100 | RESTATED | R088 |
| R087 | page 13 | 792 | 100 | RESTATED | R090 R189 R190 |
| R088 | page 13 | 792 | 100 | RESTATED | R086 |
| R089 | page 13 | 797 | 100 | - | - |
| R090 | page 13 | 799 | 100 | RESTATED | R087 R189 R190 |
| R091 | page 13 | 805 | 102 | - | - |
| R092 | page 13 | 806 | 102 | - | - |
| R093 | page 14 | 821 | 104 | RESTATED, DIVERGENCE_CHECK (Karnika 20-25% vs group 30-35% R014/R164; Kidcity is gap driver) | R191 |
| R094 | page 14 | 844 | 110 | RESTATED | R153 |
| R095 | page 15 | 893 | 121 | RESTATED | R004 |
| R096 | page 15 | 906 | 123 | RESTATED | R097 R098 R099 |
| R097 | page 15 | 906 | 123 | RESTATED | R096 R098 R099 |
| R098 | page 15 | 918 | 127 | RESTATED | R096 R097 R099 |
| R099 | page 15 | 919 | 127 | RESTATED | R096 R097 R098 |
| R100 | page 16 | 1027 | 154 | RESTATED | R149 R150 |
| R101 | page 17 | 1043 | 156 | - | - |
| R102 | page 17 | 1065 | 158 | RESTATED | R200 |
| R103 | page 17 | 1068 | 159 | ANALYST_STATED_NOT_MGMT | - |
| R104 | page 17 | 1071 | 160 | RESTATED | R201 R244 |
| M001 | n/a (not in structured) | fulltext L306 | 11 | MISSING_FROM_STRUCTURED; COUNT_RANGE "four, five, or six" retail outlets per family-shop partner (Nagarmal, Chunnilal) where Kidcity runs kids' counter; spoken in words | R126-R137 context |
| M002 | n/a (not in structured) | fulltext L704-705 | 84 | MISSING_FROM_STRUCTURED; DURATION "one and a half hours, an hour" airport dwell time (management rationale for airport visibility); spoken in words | R079 R187 R223 same turn |
| M003 | n/a (not in structured) | fulltext L867 | 116 | MISSING_FROM_STRUCTURED; COUNT_RANGE "four or five" FirstCry brands made on white label; spoken in words | R-IDs of FirstCry white label (T116/T152) |
| M004 | n/a (not in structured) | fulltext L901 | 123 | MISSING_FROM_STRUCTURED; LABEL_COUNT "two methods of billing" (bill-to/ship-to vs own-name warehouses); CFO says region data not held, West Bengal shows as billing state; spoken in words | - |
| M005 | n/a (not in structured) | fulltext L1027 | 154 | MISSING_FROM_STRUCTURED; COUNT_RANGE "10 to 12 products" per FirstCry brand and "three" brands (Mark & Mia, Ed-a-Mamma, Disney); numerals plus words | R149 R150 R100 context |
| M006 | n/a (not in structured) | fulltext L378 | 24 | MISSING_FROM_STRUCTURED; COUNT_LABEL "two growth drivers" (CFO): (1) white labeling opening Karnika to big corporates who then also buy under the Karnika brand, (2) Kidcity B2C; spoken in words. Same class as R040, R042, M004 | R040 R042 M004 |

## 5. FORWARD COMMITMENTS (47 A1 + 14 MISSING_FROM_STRUCTURED = 61) AND HEDGE / QUALIFIER PHRASES (20)
| ID | type | page | A1 line | turn | A2 flags | cross-ref |
|---|---|---|---|---|---|---|
| R158 | FORWARD | page 3 | 117 | 3 | RESTATED, FORWARD_COMMITMENT | R211 R230 |
| R159 | FORWARD | page 3 | 141 | 3 | FORWARD_COMMITMENT | - |
| R160 | FORWARD | page 4 | 165 | 3 | RESTATED, DIVERGENCE_CHECK (55-plus kiosks R010/R160 vs ~50 stores R184/R072/R245), FORWARD_COMMITMENT | R010 |
| R161 | FORWARD | page 4 | 168 | 3 | FORWARD_COMMITMENT | - |
| R162 | FORWARD | page 4 | 175 | 3 | FORWARD_COMMITMENT | - |
| R163 | FORWARD | page 4 | 184 | 3 | FORWARD_COMMITMENT | - |
| R164 | FORWARD | page 4 | 189 | 3 | RESTATED, FORWARD_COMMITMENT | R014 R015 |
| R165 | FORWARD | page 4 | 190 | 3 | RESTATED, FORWARD_COMMITMENT | R016 R049 R170 |
| R166 | FORWARD | page 7 | 345 | 16 | FORWARD_COMMITMENT | - |
| R167 | FORWARD | page 7 | 346 | 16 | FORWARD_COMMITMENT | - |
| R168 | FORWARD | page 7 | 353 | 18 | FORWARD_COMMITMENT | - |
| R169 | FORWARD | page 7 | 362 | 20 | FORWARD_COMMITMENT | - |
| R170 | FORWARD | page 7 | 370 | 22 | RESTATED, FORWARD_COMMITMENT | R016 R049 R165 |
| R171 | FORWARD | page 7 | 403 | 28 | RESTATED, FORWARD_COMMITMENT | R054 |
| R172 | FORWARD | page 8 | 411 | 28 | RESTATED, FORWARD_COMMITMENT | R055 |
| R173 | FORWARD | page 8 | 418 | 30 | RESTATED, FORWARD_COMMITMENT | R056 |
| R174 | FORWARD | page 8 | 425 | 32 | RESTATED, FORWARD_COMMITMENT | R057 |
| R175 | FORWARD | page 8 | 427 | 32 | FORWARD_COMMITMENT | - |
| R176 | FORWARD | page 8 | 437 | 34 | FORWARD_COMMITMENT | - |
| R177 | FORWARD | page 8 | 438 | 34 | FORWARD_COMMITMENT | - |
| R178 | FORWARD | page 8 | 447 | 36 | RESTATED, FORWARD_COMMITMENT | R059 |
| R179 | FORWARD | page 8 | 471 | 41 | FORWARD_COMMITMENT | - |
| R180 | FORWARD | page 9 | 499 | 45 | FORWARD_COMMITMENT | - |
| R181 | FORWARD | page 9 | 511 | 47 | FORWARD_COMMITMENT | - |
| R182 | FORWARD | page 10 | 546 | 53 | FORWARD_COMMITMENT | - |
| R183 | FORWARD | page 10 | 578 | 57 | FORWARD_COMMITMENT | - |
| R184 | FORWARD | page 10 | 587 | 59 | RESTATED, DIVERGENCE_CHECK (55-plus kiosks R010/R160 vs ~50 stores R184/R072/R245), FORWARD_COMMITMENT | R072 R245 |
| R185 | FORWARD | page 10 | 600 | 63 | RESTATED, FORWARD_COMMITMENT | R073 |
| R186 | FORWARD | page 10 | 601 | 63 | RESTATED, FORWARD_COMMITMENT | R074 R075 R077 R078 |
| R187 | FORWARD | page 12 | 710 | 84 | FORWARD_COMMITMENT | - |
| R188 | FORWARD | page 12 | 719 | 86 | RESTATED, FORWARD_COMMITMENT | R080 R081 |
| R189 | FORWARD | page 13 | 791 | 100 | RESTATED, FORWARD_COMMITMENT | R087 R090 R190 |
| R190 | FORWARD | page 13 | 798 | 100 | RESTATED, FORWARD_COMMITMENT | R087 R090 R189 |
| R191 | FORWARD | page 14 | 821 | 104 | RESTATED, FORWARD_COMMITMENT | R093 |
| R192 | FORWARD | page 15 | 951 | 137 | FORWARD_COMMITMENT | - |
| R193 | FORWARD | page 15 | 958 | 139 | FORWARD_COMMITMENT | - |
| R194 | FORWARD | page 16 | 981 | 144 | FORWARD_COMMITMENT | - |
| R195 | FORWARD | page 16 | 982 | 144 | FORWARD_COMMITMENT | - |
| R196 | FORWARD | page 16 | 989 | 146 | FORWARD_COMMITMENT | - |
| R197 | FORWARD | page 16 | 1000 | 148 | FORWARD_COMMITMENT | - |
| R198 | FORWARD | page 16 | 1009 | 150 | FORWARD_COMMITMENT | - |
| R199 | FORWARD | page 17 | 1057 | 156 | FORWARD_COMMITMENT | - |
| R200 | FORWARD | page 17 | 1065 | 158 | RESTATED, FORWARD_COMMITMENT | R102 |
| R201 | FORWARD | page 17 | 1071 | 160 | RESTATED, FORWARD_COMMITMENT | R104 R244 |
| R202 | FORWARD | page 17 | 1079 | 162 | FORWARD_COMMITMENT | - |
| R203 | FORWARD | page 11 | 664 | 76 | RESTATED, FORWARD_AS_PRESENT_FACT, FORWARD_COMMITMENT | R076 |
| R204 | FORWARD | page 11 | 657 | 74 | FORWARD_COMMITMENT | - |
| R227 | QUALIFIER | page 1 | 47 | 0 | HEDGE_OR_QUALIFIER | - |
| R228 | QUALIFIER | page 1 | 39 | 0 | HEDGE_OR_QUALIFIER | - |
| R229 | QUALIFIER | page 3 | 103 | 2 | HEDGE_OR_QUALIFIER | - |
| R230 | QUALIFIER | page 3 | 118 | 3 | RESTATED, HEDGE_OR_QUALIFIER | R158 R211 |
| R231 | QUALIFIER | page 5 | 227 | 4 | HEDGE_OR_QUALIFIER | - |
| R232 | QUALIFIER | page 7 | 403 | 28 | HEDGE_OR_QUALIFIER | - |
| R233 | QUALIFIER | page 7 | 395 | 26 | HEDGE_OR_QUALIFIER | - |
| R234 | QUALIFIER | page 6 | 294 | 11 | HEDGE_OR_QUALIFIER | - |
| R235 | QUALIFIER | page 12 | 719 | 86 | HEDGE_OR_QUALIFIER | - |
| R236 | QUALIFIER | page 10 | 562 | 55 | HEDGE_CONTRADICTION_CHECK (cf R237), HEDGE_OR_QUALIFIER | - |
| R237 | QUALIFIER | page 10 | 546 | 53 | HEDGE_CONTRADICTION_CHECK (cf R236), HEDGE_OR_QUALIFIER | - |
| R238 | QUALIFIER | page 15 | 904 | 123 | HEDGE_OR_QUALIFIER | - |
| R239 | QUALIFIER | page 13 | 756 | 94 | HEDGE_OR_QUALIFIER | - |
| R240 | QUALIFIER | page 13 | 766 | 94 | TRANSCRIPTION_ANOMALY, HEDGE_OR_QUALIFIER | - |
| R241 | QUALIFIER | page 10 | 572 | 55 | HEDGE_OR_QUALIFIER | - |
| R242 | QUALIFIER | page 5 | 216 | 4 | HEDGE_OR_QUALIFIER | - |
| R243 | QUALIFIER | page 5 | 221 | 4 | HEDGE_OR_QUALIFIER | - |
| R244 | QUALIFIER | page 17 | 1071 | 160 | RESTATED, ANALYST_CORRECTED, HEDGE_OR_QUALIFIER | R104 R201 |
| R245 | QUALIFIER | page 10 | 587 | 59 | RESTATED, HEDGE_OR_QUALIFIER | R072 R184 |
| R246 | QUALIFIER | page 4 | 180 | 3 | RESTATED, HEDGE_OR_QUALIFIER | R011 R012 |

### 5b. MISSING_FROM_STRUCTURED forward statements (Loop 2: M007-M020, 14 rows)
| ID | source | fulltext line | turn | A2 flags / claim note | cross-ref |
|---|---|---|---|---|---|
| M007 | n/a (not in structured) | fulltext L156-160 | 3 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT (MD prepared remarks, objective to combine Kidcity omnichannel with Karnika sourcing/manufacturing/distribution to expand market access across the kidswear value chain); intent, no number or date | R158 R211 |
| M008 | n/a (not in structured) | fulltext L196-199 | 3 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT (MD closing prepared remarks, "Our priority will be to execute consistently, convert growth into earnings, and deploy capital responsibly"); intent, no number or date | R159 R162 |
| M009 | n/a (not in structured) | fulltext L228-230 | 4 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT weak (CFO prepared remarks, "Our focus remains on managing costs, improving operational efficiencies... to support sustainable and profitable growth"); continuing-focus intent, no number; lexicon sweep hit on this line is a false positive ("by 94 bps") | R217 |
| M010 | n/a (not in structured) | fulltext L521-524 | 49 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT conditional (CFO: with branded accessories (bottle, purse, hair bands) added to kids garments "our margins will grow much higher"); no number; margin claim for A3 evidence check | R181 |
| M011 | n/a (not in structured) | fulltext L684-685 | 80 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT (CFO: "some will be on the airports, majority will be in the high-street shops or high-street malls"); store location mix of the 1,000 + 300-400 kiosk plan | R204 R186 |
| M012 | n/a (not in structured) | fulltext L704-707 | 84 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT (CFO: "we will also have this live online and we will be available in all the high-end malls, so revenue will be generated from there"); channel plan, no number | R187 M002 |
| M013 | n/a (not in structured) | fulltext L1094-1095 | 166 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT hedged (CFO closing: "Hopefully, we will achieve next milestones"); content-free closing, low materiality, listed for completeness | R202 |
| M014 | n/a (not in structured) | fulltext L531-532 | 51 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT scope (secondary, CFO: branded-accessories margin concept "will be only for brands of brand only"; SIS stays "purely on garmenting"). First clause is forward scope; second clause is present-tense fact (SIS model) | M010 R066 |
| M015 | n/a (not in structured) | fulltext L869-870 | 116 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT intent (secondary, CFO: "we want to be profitable and increase our business rather than doing only mass expenditure... on marketing"); aspiration statement, no number | M003 |
| M016 | n/a (not in structured) | fulltext L1051-1053 | 156 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT product plan (secondary, CFO: "what we are thinking in our concept, it will not just be Disney... Marvels will also be there, Disney, Panda"); hedged by "thinking"; licensed-character range plan | R199 R149 |
| M017 | n/a (not in structured) | fulltext L551-554 | 53 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT (sweep-found Loop 2; CFO: "My profit will come from the high-street shopping malls or online... Our visibility will be from the airport"); profit-source claim paired with R182/R237 airport break-even hedge | R182 R237 R236 |
| M018 | n/a (not in structured) | fulltext L670-671 | 78 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT RESTATED (sweep-found Loop 2; CFO: "By end of 29-30... planning for shop-in-shop around 1,000 kiosk and approx 300 to 400 kiosk"); restates R185/R186 in T78 (numbers captured as R-number rows, forward framing not tagged) | R185 R186 R074 R075 |
| M019 | n/a (not in structured) | fulltext L851-852 | 112 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT RESTATED (sweep-found Loop 2; CFO: "We are already planning for this for airports and high-end malls"); restates M012/R187 plan | M012 R187 |
| M020 | n/a (not in structured) | fulltext L859-860 | 114 | MISSING_FROM_STRUCTURED; FORWARD_COMMITMENT (sweep-found Loop 2; CFO: EBO brands-of-brand concept and INR199-499 SIS value line "we are aiming for Tier 2, Tier 3"); tier targeting, no number or date | R066 R204 |

## 6. DATES (22)
| ID | page | A1 line | turn |
|---|---|---|---|
| R205 | page 1 | 24 | 0 |
| R206 | page 1 | 36 | 0 |
| R207 | page 1 | 44 | 0 |
| R208 | page 1 | 47 | 0 |
| R209 | page 1 | 59 | 0 |
| R210 | page 2 | 68 | 0 |
| R211 | page 3 | 118 | 3 |
| R212 | page 3 | 123 | 3 |
| R213 | page 3 | 124 | 3 |
| R214 | page 4 | 180 | 3 |
| R215 | page 4 | 189 | 3 |
| R216 | page 5 | 222 | 4 |
| R217 | page 5 | 224 | 4 |
| R218 | page 7 | 354 | 18 |
| R219 | page 7 | 360 | 20 |
| R220 | page 8 | 436 | 34 |
| R221 | page 10 | 587 | 59 |
| R222 | page 10 | 600 | 63 |
| R223 | page 12 | 712 | 84 |
| R224 | page 8 | 471 | 41 |
| R225 | page 8 | 447 | 36 |
| R226 | page 7 | 346 | 16 |
Note: letter R205 16.10.2026 and signature R209 2026.10.16 13:21 follow the call R206/R210 (13-Oct-2026); intimation R207 07-Oct-2026. No timestamp conflict.

## 7. ENTITIES (53)
| ID | page | A1 line | turn | role group | A2 flags |
|---|---|---|---|---|---|
| R105 | page 1 | 33 | 0 | cover/regulatory | - |
| R106 | page 1 | 34 | 0 | cover/regulatory | - |
| R107 | page 1 | 28 | 0 | cover/regulatory | - |
| R108 | page 1 | 39 | 0 | cover/regulatory | - |
| R109 | page 1 | 55 | 0 | participant | - |
| R110 | page 1 | 62 | 0 | participant | NAME_VARIANT (Mundha/Mundhra) |
| R111 | page 2 | 73 | 0 | participant | - |
| R112 | page 2 | 75 | 0 | participant | - |
| R113 | page 2 | 78 | 0 | participant | - |
| R114 | page 5 | 238 | 5 | participant | - |
| R115 | page 6 | 322 | 12 | participant | - |
| R116 | page 8 | 457 | 39 | participant | - |
| R117 | page 11 | 616 | 66 | participant | - |
| R118 | page 14 | 879 | 119 | participant | - |
| R119 | page 4 | 156 | 3 | company/own brand/unit | - |
| R120 | page 5 | 270 | 9 | company/own brand/unit | - |
| R121 | page 4 | 174 | 3 | customer/white-label/SIS partner/trade | - |
| R122 | page 4 | 174 | 3 | customer/white-label/SIS partner/trade | - |
| R123 | page 4 | 174 | 3 | customer/white-label/SIS partner/trade | - |
| R124 | page 4 | 174 | 3 | customer/white-label/SIS partner/trade | - |
| R125 | page 5 | 268 | 9 | customer/white-label/SIS partner/trade | - |
| R126 | page 6 | 315 | 11 | customer/white-label/SIS partner/trade | - |
| R127 | page 6 | 315 | 11 | customer/white-label/SIS partner/trade | - |
| R128 | page 6 | 299 | 11 | customer/white-label/SIS partner/trade | - |
| R129 | page 6 | 299 | 11 | customer/white-label/SIS partner/trade | - |
| R130 | page 13 | 796 | 100 | customer/white-label/SIS partner/trade | - |
| R131 | page 6 | 288 | 11 | company/own brand/unit | - |
| R132 | page 16 | 1018 | 152 | company/own brand/unit | - |
| R133 | page 6 | 301 | 11 | customer/white-label/SIS partner/trade | - |
| R134 | page 6 | 301 | 11 | customer/white-label/SIS partner/trade | - |
| R135 | page 6 | 301 | 11 | customer/white-label/SIS partner/trade | - |
| R136 | page 6 | 305 | 11 | customer/white-label/SIS partner/trade | - |
| R137 | page 6 | 305 | 11 | customer/white-label/SIS partner/trade | - |
| R138 | page 13 | 760 | 94 | customer/white-label/SIS partner/trade | - |
| R139 | page 13 | 765 | 94 | customer/white-label/SIS partner/trade | - |
| R140 | page 9 | 490 | 43 | competitor/peer | - |
| R141 | page 9 | 491 | 43 | competitor/peer | - |
| R142 | page 14 | 862 | 115 | competitor/peer | ANALYST_NAMED_PEER |
| R143 | page 10 | 579 | 57 | location/listing | - |
| R144 | page 10 | 579 | 57 | location/listing | - |
| R145 | page 10 | 580 | 57 | location/listing | - |
| R146 | page 9 | 540 | 53 | licensed character | - |
| R147 | page 17 | 1052 | 156 | licensed character | - |
| R148 | page 9 | 540 | 53 | licensed character | - |
| R149 | page 16 | 1026 | 154 | customer/white-label/SIS partner/trade | RESTATED |
| R150 | page 16 | 1026 | 154 | customer/white-label/SIS partner/trade | RESTATED |
| R151 | page 8 | 472 | 41 | company/own brand/unit | - |
| R152 | page 8 | 436 | 34 | company/own brand/unit | - |
| R153 | page 14 | 844 | 110 | location/listing | RESTATED |
| R154 | page 15 | 939 | 133 | location/listing | - |
| R155 | page 15 | 951 | 137 | location/listing | - |
| R156 | page 3 | 117 | 3 | location/listing | - |
| R157 | page 18 | 1103 | 167 | host firm | - |
ENTITY_CHANGE: not assessable (no prior ledger). Kidcity (R119) is an acquired company, noted not diffed.

## 8. ZERO_STANDING
None. A transcript carries no standing line-item tables. Count 0.

## 9. DROPPED / MISSING
DROPPED_SLIDE: n/a (no prior deck). MISSING_FROM_STRUCTURED: 20 (M001-M006 numbers, sec 4; M007-M020 forward statements, sec 5b; added Loop 1 and Loop 2). FOOTNOTE_UNRESOLVED: none (A1 found no asterisk markers). Notes, agenda, auditor, line items: n/a for concall.

## 10. ID ACCOUNTABILITY
NUMBER R001-R104 (sec 4); ENTITY R105-R157 (sec 7; R110-R118 also sec 1); DATE R205-R226 (sec 6); FORWARD R158-R204 and QUALIFIER R227-R246 (sec 5). All 246 referenced.
```yaml
stage: A2-enumerator
company: "KARNIKA"
quarter: "h1fy27"
doctype: "concall"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/karnika-h1fy27/work/ledger_concall_karnika_h1fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 53
  turns: 167
  questions: 67
  mgmt_numbers: 106
  slides: 0
  slide_numbers: 0
flags_raised: [REPEAT_QUESTION, RESTATED, FORWARD_COMMITMENT, HEDGE_OR_QUALIFIER, MD_SILENT_IN_QA, NAME_VARIANT, DIVERGENCE_CHECK, ANALYST_STATED_NOT_MGMT, ANALYST_CORRECTED, FORWARD_AS_PRESENT_FACT, TRANSCRIPTION_ANOMALY, HEDGE_CONTRADICTION_CHECK]
ids_in_structured: 246
ids_referenced: 246
orphan_ids: []
missing_from_structured: [M001, M002, M003, M004, M005, M006, M007, M008, M009, M010, M011, M012, M013, M014, M015, M016, M017, M018, M019, M020]
gate_a2: pass
mismatch_note: ""
analyst_note: "Loop 2: M006 (words number) and 14 forward statements M007-M020 added; independent lexicon sweep 123 hits on 95 mgmt lines reconciles 57 covered + 17 new + 21 non-forward, 0 unmapped; forward rows 47 -> 61, mgmt_numbers 106. Loop 1: T87 reclassified as a question (66->67); five words-written numbers added M001-M005 (100->105). A1 carries no turn or question IDs, so turns (167) and questions (67) were built from the A1 fulltext speaker labels; each turn lists the R-IDs falling in its line range. The MD speaks only in prepared remarks (T3); the CFO answers all 77 Q&A answer turns (78 CFO turns incl. T4 prepared remarks). Store-target divergence for A3: 55-plus kiosks (R010/R160, deck-style opening) vs roughly 50 stores FY27-28 (R184/R245), with 1,300-1,400 outlets by FY29-30 (R186). Airport hedge pair R236/R237 (not profitable, break-even at best, then 'maybe we might be wrong'). R203 states SIS break-even as present fact. R240 is a transcription anomaly (100 square feet vs km radius). Mgmt widened the analyst's 18-19 percent margin frame to 17-20 percent (R049/R050). Kidcity H1 INR40cr vs INR80-100cr FY target (R052/R054) implies a steep H2 ramp."
```
