# A2 LEDGER - GALLANTT Q2 FY27 results

ids_in_structured: 449 | ids_referenced_in_ledger: 449 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes (rows incl restated)           grep_count: 15   sweep_count: 15   match: yes
category: line_items (distinct stmt lines)     grep_count: 96   sweep_count: 96   match: yes
category: line_item_cells                      grep_count: 296   sweep_count: 296   match: yes
category: zero_standing_cells (all)            grep_count: 27   sweep_count: 27   match: yes
category: agenda_items (board letter)          grep_count: 1   sweep_count: 1   match: yes
category: superseded_rows                      grep_count: 8   sweep_count: 8   match: yes
category: auditor_rows R399-R449               grep_count: 51   sweep_count: 51   match: yes
category: consolidated subsidiaries            grep_count: 1   sweep_count: 1   match: yes
category: structured ids vs header 449         grep_count: 449   sweep_count: 449   match: yes
gate_a2: pass
=== END COUNT TEST ===

line_item_cells = 296 (P&L 156 = 26 lines x 6 cols; BS 70 = 35 x 2; CF 70 = 35 x 2); distinct statement lines = 96. A1 NUMBER count 320 also holds non-table numbers.

FILING FLAGS: (1) STANDALONE_STATEMENT_ABSENT: standalone auditor review report p12 (R402,R403) but no standalone statements; only consolidated (p2-5, p7-10). (2) DATE_INCONSISTENCY: subject line 03-Nov-2025 (R009,R010) vs body 19-Oct-2026 (R012). (3) Pages 2-5 duplicate pages 7-10; 8 SUPERSEDED rows. (4) Pages 6 and 11 duplicate notes 1-5. (5) Source item numbering skips 13.

## Cover letter items (14)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R001 | p1:L20 |  |
R002 | p1:L22 |  |
R003 | p1:L24 |  |
R004 | p1:L24 |  |
R005 | p1:L26 |  |
R006 | p1:L29 |  |
R007 | p1:L30 |  |
R008 | p1:L30 |  |
R019 | p1:L56 |  |
R020 | p1:L66 |  |
R024 | p1:L84 |  |
R025 | p1:L85 |  |
R026 | p1:L89 |  |
R027 | p1:L90 |  |

## Agenda items and meeting facts (one item: results; times R011) (10)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R009 | p1:L34 | DATE_INCONSISTENCY (subject 03-Nov-2025 vs body 19-Oct-2026 R012) |
R010 | p1:L34 | DATE_INCONSISTENCY |
R011 | p1:L35 | MEETING_TIMES 04:30 PM to 11:00 PM (~6.5h) |
R012 | p1:L37 |  |
R013 | p1:L41 |  |
R014 | p1:L42 |  |
R015 | p1:L45 |  |
R016 | p1:L49 |  |
R017 | p1:L52 |  |
R018 | p1:L52 |  |

## Signature blocks (company side) (13)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R021 | p1:L68 | SIGNATURE_BLOCK |
R022 | p1:L72 | SIGNATURE_BLOCK SIG_23:11 after meeting end 23:00 (not before; no flag trigger) |
R023 | p1:L74 | SIGNATURE_BLOCK |
R033 | p2:L174 | SIGNATURE_BLOCK |
R038 | p3:L284 | SIGNATURE_BLOCK |
R062 | p6:L472 | SIGNATURE_BLOCK |
R063 | p6:L474 | SIGNATURE_BLOCK SIGNATORY_NAME_ILLEGIBLE |
R064 | p6:L474 | SIGNATURE_BLOCK |
R070 | p7:L562 | SIGNATURE_BLOCK |
R231 | p8:L669 | SIGNATURE_BLOCK |
R396 | p11:L855 | SIGNATURE_BLOCK |
R397 | p11:L857 | SIGNATURE_BLOCK SIGNATORY_NAME_ILLEGIBLE |
R398 | p11:L857 | SIGNATURE_BLOCK |

## SUPERSEDED garbled-text rows (accounted explicitly) (8)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R028 | p2:L93 | SUPERSEDED_ID | ->p7 L1056-1082
R035 | p3:L188 | SUPERSEDED_ID | ->p8 L1083-1118
R039 | p4:L296 | SUPERSEDED_ID | ->p9 L1119-1147
R042 | p5:L381 | SUPERSEDED_ID | ->p10 L1148-1156
R065 | p7:L487 | SUPERSEDED_ID | ->p7 L1056-1082
R228 | p8:L575 | SUPERSEDED_ID | ->p8 L1083-1118
R302 | p9:L679 | SUPERSEDED_ID | ->p9 L1119-1147
R361 | p10:L775 | SUPERSEDED_ID | ->p10 L1148-1156

## Statement titles, units, dates, footers (40)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R029 | p2:L95 |  |
R030 | p2:L100 |  |
R031 | p2:L100 |  |
R032 | p2:L108 |  |
R034 | p2:L184 |  |
R036 | p3:L188 |  |
R037 | p3:L191 |  |
R040 | p4:L299 |  |
R041 | p4:L302 |  |
R043 | p5:L381 |  |
R044 | p5:L384 |  |
R048 | p6:L429 |  |
R049 | p6:L429 |  |
R054 | p6:L448 |  |
R055 | p6:L453 |  |
R057 | p6:L458 |  |
R058 | p6:L458 |  |
R059 | p6:L458 |  |
R060 | p6:L459 |  |
R061 | p6:L459 |  |
R066 | p7:L487 |  |
R067 | p7:L489 |  |
R068 | p7:L489 |  |
R069 | p7:L497 |  |
R071 | p7:L571 |  |
R229 | p8:L575 |  |
R230 | p8:L578 |  |
R303 | p9:L682 |  |
R304 | p9:L686 |  |
R362 | p10:L775 |  |
R363 | p10:L779 |  |
R382 | p11:L820 |  |
R383 | p11:L820 |  |
R388 | p11:L840 |  |
R389 | p11:L844 |  |
R391 | p11:L849 |  |
R392 | p11:L849 |  |
R393 | p11:L849 |  |
R394 | p11:L850 |  |
R395 | p11:L850 |  |

## Notes (numbered, unnumbered, restated) (15)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R045 | p5:L398 | NOTE |
R046 | p5:L400 | NOTE |
R047 | p6:L428 | NOTE |
R051 | p6:L435 | NOTE |
R052 | p6:L440 | NOTE |
R053 | p6:L448 | NOTE |
R056 | p6:L458 | NOTE see R370 |
R364 | p10:L793 | NOTE RESTATED (=R045) |
R365 | p10:L794 | NOTE RESTATED (=R046) |
R380 | p10:L1156 | NOTE RESTATED (=R045/R046) |
R381 | p11:L819 | NOTE RESTATED (=R047) |
R385 | p11:L828 | NOTE RESTATED (=R051) |
R386 | p11:L833 | NOTE RESTATED (=R052) |
R387 | p11:L840 | NOTE RESTATED (=R053) |
R390 | p11:L849 | NOTE RESTATED (=R056) |

## Financial table line items (every cell) (296)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R072 | p7:L1057 |  |
R073 | p7:L1057 |  |
R074 | p7:L1057 |  |
R075 | p7:L1057 |  |
R076 | p7:L1057 |  |
R077 | p7:L1057 |  |
R078 | p7:L1058 |  |
R079 | p7:L1058 |  |
R080 | p7:L1058 |  |
R081 | p7:L1058 |  |
R082 | p7:L1058 |  |
R083 | p7:L1058 |  |
R084 | p7:L1059 |  |
R085 | p7:L1059 |  |
R086 | p7:L1059 |  |
R087 | p7:L1059 |  |
R088 | p7:L1059 |  |
R089 | p7:L1059 |  |
R090 | p7:L1060 |  |
R091 | p7:L1060 |  |
R092 | p7:L1060 |  |
R093 | p7:L1060 |  |
R094 | p7:L1060 |  |
R095 | p7:L1060 |  |
R096 | p7:L1061 |  |
R097 | p7:L1061 |  |
R098 | p7:L1061 |  |
R099 | p7:L1061 |  |
R100 | p7:L1061 |  |
R101 | p7:L1061 |  |
R102 | p7:L1062 |  |
R103 | p7:L1062 |  |
R104 | p7:L1062 |  |
R105 | p7:L1062 |  |
R106 | p7:L1062 |  |
R107 | p7:L1062 |  |
R108 | p7:L1063 |  |
R109 | p7:L1063 |  |
R110 | p7:L1063 |  |
R111 | p7:L1063 |  |
R112 | p7:L1063 |  |
R113 | p7:L1063 |  |
R114 | p7:L1064 |  |
R115 | p7:L1064 |  |
R116 | p7:L1064 |  |
R117 | p7:L1064 |  |
R118 | p7:L1064 |  |
R119 | p7:L1064 |  |
R120 | p7:L1065 |  |
R121 | p7:L1065 |  |
R122 | p7:L1065 |  |
R123 | p7:L1065 |  |
R124 | p7:L1065 |  |
R125 | p7:L1065 |  |
R126 | p7:L1066 |  |
R127 | p7:L1066 |  |
R128 | p7:L1066 |  |
R129 | p7:L1066 |  |
R130 | p7:L1066 |  |
R131 | p7:L1066 |  |
R132 | p7:L1067 |  |
R133 | p7:L1067 |  |
R134 | p7:L1067 |  |
R135 | p7:L1067 |  |
R136 | p7:L1067 |  |
R137 | p7:L1067 |  |
R138 | p7:L1068 | PBT_Q2_DOWN_YOY (vs R139) |
R139 | p7:L1068 |  |
R140 | p7:L1068 |  |
R141 | p7:L1068 |  |
R142 | p7:L1068 |  |
R143 | p7:L1068 |  |
R144 | p7:L1069 | ZERO_STANDING |
R145 | p7:L1069 | ZERO_STANDING |
R146 | p7:L1069 | ZERO_STANDING |
R147 | p7:L1069 | ZERO_STANDING |
R148 | p7:L1069 | ZERO_STANDING |
R149 | p7:L1069 | ZERO_STANDING |
R150 | p7:L1070 |  |
R151 | p7:L1070 |  |
R152 | p7:L1070 |  |
R153 | p7:L1070 |  |
R154 | p7:L1070 |  |
R155 | p7:L1070 |  |
R156 | p7:L1071 |  |
R157 | p7:L1071 |  |
R158 | p7:L1071 |  |
R159 | p7:L1071 |  |
R160 | p7:L1071 |  |
R161 | p7:L1071 |  |
R162 | p7:L1072 |  |
R163 | p7:L1072 |  |
R164 | p7:L1072 |  |
R165 | p7:L1072 |  |
R166 | p7:L1072 |  |
R167 | p7:L1072 |  |
R168 | p7:L1073 |  |
R169 | p7:L1073 |  |
R170 | p7:L1073 |  |
R171 | p7:L1073 |  |
R172 | p7:L1073 |  |
R173 | p7:L1073 |  |
R174 | p7:L1074 | PAT_Q2_DOWN_YOY (vs R175) |
R175 | p7:L1074 |  |
R176 | p7:L1074 |  |
R177 | p7:L1074 |  |
R178 | p7:L1074 |  |
R179 | p7:L1074 |  |
R180 | p7:L1075 | ZERO_STANDING ASSOCIATE_LINE_NO_ASSOCIATE_IN_PERIMETER |
R181 | p7:L1075 | ASSOCIATE_LINE_NO_ASSOCIATE_IN_PERIMETER |
R182 | p7:L1075 | ZERO_STANDING ASSOCIATE_LINE_NO_ASSOCIATE_IN_PERIMETER |
R183 | p7:L1075 | ZERO_STANDING ASSOCIATE_LINE_NO_ASSOCIATE_IN_PERIMETER |
R184 | p7:L1075 | ASSOCIATE_LINE_NO_ASSOCIATE_IN_PERIMETER; H1FY26 169.37 vs FY26 nil |
R185 | p7:L1075 | ZERO_STANDING ASSOCIATE_LINE_NO_ASSOCIATE_IN_PERIMETER; FY26 nil vs H1FY26 169.37 |
R186 | p7:L1076 |  |
R187 | p7:L1076 |  |
R188 | p7:L1076 |  |
R189 | p7:L1076 |  |
R190 | p7:L1076 |  |
R191 | p7:L1076 |  |
R192 | p7:L1077 |  |
R193 | p7:L1077 |  |
R194 | p7:L1077 |  |
R195 | p7:L1077 |  |
R196 | p7:L1077 |  |
R197 | p7:L1077 |  |
R198 | p7:L1078 | ZERO_STANDING |
R199 | p7:L1078 | ZERO_STANDING |
R200 | p7:L1078 | ZERO_STANDING |
R201 | p7:L1078 | ZERO_STANDING |
R202 | p7:L1078 | ZERO_STANDING |
R203 | p7:L1078 | ZERO_STANDING |
R204 | p7:L1079 |  |
R205 | p7:L1079 |  |
R206 | p7:L1079 |  |
R207 | p7:L1079 |  |
R208 | p7:L1079 |  |
R209 | p7:L1079 |  |
R210 | p7:L1080 |  |
R211 | p7:L1080 |  |
R212 | p7:L1080 |  |
R213 | p7:L1080 |  |
R214 | p7:L1080 |  |
R215 | p7:L1080 |  |
R216 | p7:L1081 |  |
R217 | p7:L1081 |  |
R218 | p7:L1081 |  |
R219 | p7:L1081 |  |
R220 | p7:L1081 |  |
R221 | p7:L1081 |  |
R222 | p7:L1082 |  |
R223 | p7:L1082 |  |
R224 | p7:L1082 |  |
R225 | p7:L1082 |  |
R226 | p7:L1082 |  |
R227 | p7:L1082 |  |
R232 | p8:L1084 |  |
R233 | p8:L1084 |  |
R234 | p8:L1085 | CWIP_UP vs R235 |
R235 | p8:L1085 |  |
R236 | p8:L1086 |  |
R237 | p8:L1086 |  |
R238 | p8:L1087 |  |
R239 | p8:L1087 |  |
R240 | p8:L1088 |  |
R241 | p8:L1088 |  |
R242 | p8:L1089 |  |
R243 | p8:L1089 |  |
R244 | p8:L1090 |  |
R245 | p8:L1090 |  |
R246 | p8:L1091 |  |
R247 | p8:L1091 |  |
R248 | p8:L1092 |  |
R249 | p8:L1092 |  |
R250 | p8:L1093 |  |
R251 | p8:L1093 |  |
R252 | p8:L1094 |  |
R253 | p8:L1094 |  |
R254 | p8:L1095 | CASH_DROP 10,165.48 to 111.58 (R255 prior) |
R255 | p8:L1095 |  |
R256 | p8:L1096 |  |
R257 | p8:L1096 |  |
R258 | p8:L1097 |  |
R259 | p8:L1097 |  |
R260 | p8:L1098 |  |
R261 | p8:L1098 |  |
R262 | p8:L1099 |  |
R263 | p8:L1099 |  |
R264 | p8:L1100 |  |
R265 | p8:L1100 |  |
R266 | p8:L1101 |  |
R267 | p8:L1101 |  |
R268 | p8:L1102 |  |
R269 | p8:L1102 |  |
R270 | p8:L1103 |  |
R271 | p8:L1103 |  |
R272 | p8:L1104 |  |
R273 | p8:L1104 |  |
R274 | p8:L1105 |  |
R275 | p8:L1105 |  |
R276 | p8:L1106 |  |
R277 | p8:L1106 |  |
R278 | p8:L1107 |  |
R279 | p8:L1107 |  |
R280 | p8:L1108 |  |
R281 | p8:L1108 |  |
R282 | p8:L1109 |  |
R283 | p8:L1109 |  |
R284 | p8:L1110 |  |
R285 | p8:L1110 |  |
R286 | p8:L1111 |  |
R287 | p8:L1111 |  |
R288 | p8:L1112 |  |
R289 | p8:L1112 | ZERO_STANDING ZERO_STANDING_PRIOR_ONLY |
R290 | p8:L1113 |  |
R291 | p8:L1113 |  |
R292 | p8:L1114 |  |
R293 | p8:L1114 |  |
R294 | p8:L1115 |  |
R295 | p8:L1115 |  |
R296 | p8:L1116 |  |
R297 | p8:L1116 | ZERO_STANDING ZERO_STANDING_PRIOR_ONLY |
R298 | p8:L1117 |  |
R299 | p8:L1117 |  |
R300 | p8:L1118 |  |
R301 | p8:L1118 |  |
R305 | p9:L1120 |  |
R306 | p9:L1120 |  |
R307 | p9:L1121 |  |
R308 | p9:L1121 |  |
R309 | p9:L1122 |  |
R310 | p9:L1122 |  |
R311 | p9:L1123 |  |
R312 | p9:L1123 | ZERO_STANDING |
R313 | p9:L1124 |  |
R314 | p9:L1124 |  |
R315 | p9:L1125 |  |
R316 | p9:L1125 | ZERO_STANDING |
R317 | p9:L1126 | ZERO_STANDING |
R318 | p9:L1126 |  |
R319 | p9:L1127 |  |
R320 | p9:L1127 |  |
R321 | p9:L1128 |  |
R322 | p9:L1128 |  |
R323 | p9:L1129 |  |
R324 | p9:L1129 |  |
R325 | p9:L1130 |  |
R326 | p9:L1130 |  |
R327 | p9:L1131 |  |
R328 | p9:L1131 |  |
R329 | p9:L1132 |  |
R330 | p9:L1132 |  |
R331 | p9:L1133 |  |
R332 | p9:L1133 |  |
R333 | p9:L1134 |  |
R334 | p9:L1134 |  |
R335 | p9:L1135 |  |
R336 | p9:L1135 |  |
R337 | p9:L1136 |  |
R338 | p9:L1136 |  |
R339 | p9:L1137 |  |
R340 | p9:L1137 |  |
R341 | p9:L1138 |  |
R342 | p9:L1138 |  |
R343 | p9:L1139 |  |
R344 | p9:L1139 |  |
R345 | p9:L1140 |  |
R346 | p9:L1140 |  |
R347 | p9:L1141 |  |
R348 | p9:L1141 |  |
R349 | p9:L1142 | ZERO_STANDING |
R350 | p9:L1142 |  |
R351 | p9:L1143 |  |
R352 | p9:L1143 |  |
R353 | p9:L1144 |  |
R354 | p9:L1144 |  |
R355 | p9:L1145 |  |
R356 | p9:L1145 |  |
R357 | p9:L1146 |  |
R358 | p9:L1146 |  |
R359 | p9:L1147 |  |
R360 | p9:L1147 |  |
R366 | p10:L1149 |  |
R367 | p10:L1149 |  |
R368 | p10:L1150 |  |
R369 | p10:L1150 |  |
R370 | p10:L1151 | ZERO_STANDING DIVIDEND_APPROVED_AGM_30SEP_NIL_PAID_H1 (see R056/R057) |
R371 | p10:L1151 |  |
R372 | p10:L1152 |  |
R373 | p10:L1152 |  |
R374 | p10:L1153 |  |
R375 | p10:L1153 |  |
R376 | p10:L1154 |  |
R377 | p10:L1154 |  |
R378 | p10:L1155 |  |
R379 | p10:L1155 |  |

## Auditor report paragraphs and facts (28)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R399 | p12:L872 | PINCODE_DIFFERS_R421 (201 304 vs 201 301) |
R400 | p12:L875 |  |
R401 | p12:L877 |  |
R402 | p12:L881 | STANDALONE_STATEMENT_ABSENT |
R403 | p12:L887 | STANDALONE_STATEMENT_ABSENT (review report only, no statements in filing) |
R404 | p12:L887 |  |
R405 | p12:L895 |  |
R406 | p12:L900 |  |
R407 | p12:L910 |  |
R408 | p12:L917 |  |
R409 | p13:L924 | AUDITOR_CHANGE (predecessor, name not stated) |
R410 | p13:L924 |  |
R411 | p13:L926 |  |
R412 | p13:L926 | AUDITOR_CHANGE |
R413 | p13:L929 |  |
R421 | p14:L951 | PINCODE_DIFFERS_R399 |
R422 | p14:L955 |  |
R423 | p14:L961 |  |
R424 | p14:L967 |  |
R425 | p14:L969 |  |
R426 | p14:L980 |  |
R427 | p14:L987 |  |
R428 | p14:L987 |  |
R443 | p15:L1028 | AUDITOR_CHANGE |
R444 | p15:L1028 |  |
R445 | p15:L1038 |  |
R446 | p15:L1040 |  |
R447 | p15:L1041 |  |

## Auditor signature block (9)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R414 | p13:L933 | SIGNATURE_BLOCK |
R415 | p13:L933 | SIGNATURE_BLOCK |
R416 | p13:L937 | SIGNATURE_BLOCK |
R417 | p13:L940 | SIGNATURE_BLOCK |
R418 | p13:L942 | SIGNATURE_BLOCK UDIN_DIFFERS_FROM_R449 (standalone vs consolidated, as extracted) |
R419 | p13:L944 | SIGNATURE_BLOCK |
R420 | p13:L946 | SIGNATURE_BLOCK |
R448 | p15:L1044 | SIGNATURE_BLOCK |
R449 | p15:L1054 | SIGNATURE_BLOCK UDIN_DIFFERS_FROM_R418 |

## Entities / consolidation perimeter and subsidiary figures (16)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R050 | p6:L429 |  |
R384 | p11:L820 |  |
R429 | p14:L993 | ENTITY_LIST_ONE_ONLY |
R430 | p14:L993 |  |
R431 | p15:L1002 |  |
R432 | p15:L1011 | OTHER_AUDITOR_RELIANCE |
R433 | p15:L1013 |  |
R434 | p15:L1015 | ZERO_STANDING NIL_REVENUE_SUBSIDIARY |
R435 | p15:L1015 | ZERO_STANDING |
R436 | p15:L1015 |  |
R437 | p15:L1015 |  |
R438 | p15:L1016 | ZERO_STANDING |
R439 | p15:L1016 | ZERO_STANDING |
R440 | p15:L1017 |  |
R441 | p15:L1017 |  |
R442 | p15:L1026 | MGMT_ASSERTION_UNVERIFIED |

## MISSING_FROM_STRUCTURED
none found.

## ENTITY_CHANGE
none flaggable (no prior ledger). Perimeter: Suryalaxmi Technologies Pvt Ltd, wholly-owned subsidiary (R429); associate profit line R180-R185 exists though no associate is listed.

```yaml
stage: A2-enumerator
company: "GALLANTT"
quarter: "Q2 FY27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/gallantt-q2fy27/work/ledger_results_gallantt_q2fy27.md"
counts:
  notes: 15
  line_items: 96
  zero_standing: 27
  agenda_items: 1
  auditor_paras: 51
  entities: 1
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, SUPERSEDED_ID, STANDALONE_STATEMENT_ABSENT, DATE_INCONSISTENCY, AUDITOR_CHANGE, OTHER_AUDITOR_RELIANCE, RESTATED, ASSOCIATE_LINE_NO_ASSOCIATE_IN_PERIMETER, UDIN_DIFFERS, PINCODE_DIFFERS, SIGNATORY_NAME_ILLEGIBLE]
ids_in_structured: 449
ids_referenced: 449
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "line_items=96 distinct statement lines (296 cells: P&L 156, BS 70, CF 70); notes=15 rows (5 distinct P&L notes + 2 cash-flow notes, restated on pp6/11 and pp5/10). zero_standing=27 cells incl 6 nil-subsidiary figures. 8 SUPERSEDED garbled rows (R028,R035,R039,R042,R065,R228,R302,R361) all accounted, pointing to transcription L1056-1156. Filing has standalone auditor review report (R402/R403) but no standalone statements. Subject date 03-Nov-2025 (R009/R010) vs body 19-Oct-2026. Associate profit line R180-R185 present though perimeter lists only one wholly-owned subsidiary; H1FY26 169.37 vs FY26 nil. Auditor changed (predecessor unnamed R409/R412). Standalone and consolidated UDINs differ in format (R418 vs R449) and auditor pincode differs (R399 vs R421), as extracted. Dividend Rs2 approved at AGM 30-Sep but H1 dividend paid nil (R370). Cash fell 10,165.48 to 111.58."
```
