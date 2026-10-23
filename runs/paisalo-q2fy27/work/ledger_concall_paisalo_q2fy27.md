# LEDGER concall PAISALO Q2 FY27 (A2)
Source: A1 structured extraction (ASR machine transcript, not company-filed). Rows reference A1 IDs; verbatim values stay in the structured file.

=== A2 COUNT TEST ===
category: participants         grep_count:    9   sweep_count:    9   match: yes
category: turns                grep_count:   40   sweep_count:   40   match: yes
category: questions            grep_count:   12   sweep_count:   12   match: yes
category: mgmt_numbers         grep_count:  118   sweep_count:  118   match: yes
category: forward              grep_count:   37   sweep_count:   37   match: yes
category: qualifiers_hedges    grep_count:   20   sweep_count:   20   match: yes
category: dates                grep_count:   23   sweep_count:   23   match: yes
category: entities             grep_count:   33   sweep_count:   33   match: yes
category: zero_standing        grep_count:    2   sweep_count:    2   match: yes
category: all_row_ids          grep_count:   288   sweep_count:  288   match: yes
gate_a2: pass
=== END COUNT TEST ===
ids_in_structured: 288 | ids_referenced_in_ledger: 288 | orphan_ids: [] | match: yes

## 1. Participants
| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R180 | participant-mgmt/host | ASR_MISHEARD |  |
| R181 | participant-mgmt/host |  |  |
| R182 | participant-mgmt/host |  |  |
| R183 | participant-mgmt/host | ASR_MISHEARD |  |
| R200 | participant-analyst |  |  |
| R203 | participant-analyst | ASR_MISHEARD |  |
| R204 | participant-analyst | ASR_MISHEARD |  |
| R205 | participant-analyst | ASR_MISHEARD |  |
| R206 | participant-analyst | ASR_MISHEARD |  |
| (none) | MGMT_ABSENCE | MGMT_ABSENCE | No promoter / CMD / MD among R181-R183 named speakers (Deputy MD, ED and CFO, CBO). ASR attribution only; flag, not confirmed absence. |

## 2. Speaker turns (sequential)
| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R001 | turn 1 MODERATOR |  | line line 1-23 |
| R002 | turn 2 HOST | ASR_MISHEARD | line line 24-32 |
| R003 | turn 3 MGMT-NAMED |  | line line 33-167 |
| R004 | turn 4 MGMT-NAMED |  | line line 168-250 |
| R005 | turn 5 MGMT-NAMED |  | line line 251-327 |
| R006 | turn 6 MODERATOR |  | line line 328-341 |
| R007 | turn 7 ANALYST |  | line line 342-355 |
| R008 | turn 8 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 356-374 |
| R009 | turn 9 ANALYST |  | line line 375-376 |
| R010 | turn 10 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 377-383 |
| R011 | turn 11 ANALYST |  | line line 384-385 |
| R012 | turn 12 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 386-396 |
| R013 | turn 13 ANALYST |  | line line 397-399 |
| R014 | turn 14 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 400-408 |
| R015 | turn 15 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 409-410 |
| R016 | turn 16 MODERATOR |  | line line 411-412 |
| R017 | turn 17 ANALYST | ASR_MISHEARD | line line 413-417 |
| R018 | turn 18 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 418-441 |
| R019 | turn 19 ANALYST |  | line line 442-444 |
| R020 | turn 20 MODERATOR |  | line line 445 |
| R021 | turn 21 ANALYST |  | line line 446-448 |
| R022 | turn 22 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 449-495 |
| R023 | turn 23 ANALYST |  | line line 496-497 |
| R024 | turn 24 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 498-505 |
| R025 | turn 25 ANALYST |  | line line 506-509 |
| R026 | turn 26 MODERATOR |  | line line 510-516 |
| R027 | turn 27 ANALYST |  | line line 517-531 |
| R028 | turn 28 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 532-558 |
| R029 | turn 29 MIXED |  | line line 559-560 |
| R030 | turn 30 MODERATOR |  | line line 561-566 |
| R031 | turn 31 ANALYST |  | line line 567-575 |
| R032 | turn 32 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 576-599 |
| R033 | turn 33 ANALYST |  | line line 600-602 |
| R034 | turn 34 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 603-634 |
| R035 | turn 35 ANALYST |  | line line 635-641 |
| R036 | turn 36 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 642-655 |
| R037 | turn 37 ANALYST |  | line line 656-660 |
| R038 | turn 38 MODERATOR |  | line line 661-662 |
| R039 | turn 39 MGMT-UNRESOLVED | SPEAKER_UNRESOLVED | line line 663-676 |
| R040 | turn 40 MODERATOR |  | line line 677-681 |

## 3. Questions
| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R041 | question | REPEAT_QUESTION | yields/NIM with R042,R045 |
| R042 | question | REPEAT_QUESTION | yields/NIM with R041,R045 |
| R043 | question | REPEAT_QUESTION | efficiency with R046,R047 |
| R044 | question |  |  |
| R045 | question | REPEAT_QUESTION ASR_MISHEARD | yields/NIM with R041,R042 |
| R046 | question | REPEAT_QUESTION | efficiency with R043,R047 |
| R047 | question | REPEAT_QUESTION | efficiency with R043,R046 |
| R048 | question | ASR_MISHEARD |  |
| R049 | question | REPEAT_QUESTION | cost of funds with R052 |
| R050 | question |  |  |
| R051 | question |  |  |
| R052 | question | REPEAT_QUESTION | cost of funds with R049 |

## 4. Numbers (mgmt numbers feed Role 5 check)
| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R053 | number-non-mgmt |  | engine or analyst-spoken, not management |
| R054 | number-non-mgmt |  | engine or analyst-spoken, not management |
| R055 | number-non-mgmt |  | engine or analyst-spoken, not management |
| R056 | mgmt-number |  |  |
| R057 | mgmt-number | ASR_MISHEARD |  |
| R058 | mgmt-number |  |  |
| R059 | mgmt-number | RESTATED | also R069 |
| R060 | mgmt-number | ASR_MISHEARD |  |
| R061 | mgmt-number | RESTATED | also R113 |
| R062 | mgmt-number | RESTATED | also R110 |
| R063 | mgmt-number | RESTATED | also R112 |
| R064 | mgmt-number |  |  |
| R065 | mgmt-number |  |  |
| R066 | mgmt-number | ASR_MISHEARD |  |
| R067 | mgmt-number |  |  |
| R068 | mgmt-number |  |  |
| R069 | mgmt-number |  |  |
| R070 | mgmt-number |  |  |
| R071 | mgmt-number |  |  |
| R072 | mgmt-number |  |  |
| R073 | mgmt-number |  |  |
| R074 | mgmt-number | ASR_MISHEARD RESTATED | also R072 |
| R075 | mgmt-number |  |  |
| R076 | mgmt-number | RESTATED | also R142,R146 |
| R077 | mgmt-number | RESTATED | also R145 |
| R078 | mgmt-number | RESTATED | also R144 |
| R079 | mgmt-number | RESTATED | also R085,R139 |
| R080 | mgmt-number | RESTATED | also R133,R138,R159 |
| R081 | mgmt-number | ASR_MISHEARD |  |
| R082 | mgmt-number | ASR_MISHEARD |  |
| R083 | mgmt-number |  |  |
| R084 | mgmt-number |  |  |
| R085 | mgmt-number |  |  |
| R086 | mgmt-number |  |  |
| R087 | mgmt-number |  |  |
| R088 | mgmt-number |  |  |
| R089 | mgmt-number |  |  |
| R090 | mgmt-number |  |  |
| R091 | mgmt-number |  |  |
| R092 | mgmt-number |  |  |
| R093 | mgmt-number |  |  |
| R094 | mgmt-number |  |  |
| R095 | mgmt-number |  |  |
| R096 | mgmt-number |  |  |
| R097 | mgmt-number |  |  |
| R098 | mgmt-number |  |  |
| R099 | mgmt-number | ASR_MISHEARD |  |
| R100 | mgmt-number |  |  |
| R101 | mgmt-number | ASR_MISHEARD |  |
| R102 | mgmt-number |  |  |
| R103 | mgmt-number |  |  |
| R104 | mgmt-number |  |  |
| R105 | mgmt-number |  |  |
| R106 | mgmt-number |  |  |
| R107 | mgmt-number |  |  |
| R108 | mgmt-number |  |  |
| R109 | mgmt-number |  |  |
| R110 | mgmt-number |  |  |
| R111 | mgmt-number |  |  |
| R112 | mgmt-number |  |  |
| R113 | mgmt-number |  |  |
| R114 | mgmt-number |  |  |
| R115 | mgmt-number |  |  |
| R116 | mgmt-number |  |  |
| R117 | mgmt-number | ASR_MISHEARD |  |
| R118 | mgmt-number | ASR_MISHEARD |  |
| R119 | mgmt-number |  |  |
| R120 | mgmt-number |  |  |
| R121 | mgmt-number |  |  |
| R122 | mgmt-number |  |  |
| R123 | mgmt-number | ASR_MISHEARD |  |
| R124 | mgmt-number | RESTATED | also R281 |
| R125 | mgmt-number | ASR_MISHEARD |  |
| R126 | mgmt-number |  |  |
| R127 | mgmt-number | RESTATED | also R128,R173,R174 |
| R128 | mgmt-number |  |  |
| R129 | mgmt-number | RESTATED | also R132,R225 |
| R130 | mgmt-number |  |  |
| R131 | mgmt-number |  |  |
| R132 | mgmt-number |  |  |
| R133 | mgmt-number |  |  |
| R134 | mgmt-number | RESTATED | also R136,R158 |
| R135 | mgmt-number | RESTATED | also R137 |
| R136 | mgmt-number |  |  |
| R137 | mgmt-number |  |  |
| R138 | mgmt-number |  |  |
| R139 | mgmt-number |  |  |
| R140 | mgmt-number |  |  |
| R141 | mgmt-number |  |  |
| R142 | mgmt-number | ASR_MISHEARD |  |
| R143 | mgmt-number | ASR_MISHEARD |  |
| R144 | mgmt-number |  |  |
| R145 | mgmt-number |  |  |
| R146 | mgmt-number |  |  |
| R147 | mgmt-number | ASR_MISHEARD |  |
| R148 | mgmt-number | ZERO_STANDING |  |
| R149 | mgmt-number |  |  |
| R150 | mgmt-number | ZERO_STANDING |  |
| R151 | mgmt-number |  |  |
| R152 | mgmt-number |  |  |
| R153 | mgmt-number |  |  |
| R154 | mgmt-number |  |  |
| R155 | mgmt-number |  |  |
| R156 | mgmt-number |  |  |
| R157 | mgmt-number |  |  |
| R158 | mgmt-number |  |  |
| R159 | mgmt-number |  |  |
| R160 | mgmt-number |  |  |
| R161 | mgmt-number | RESTATED | also R235 |
| R162 | mgmt-number | ASR_MISHEARD |  |
| R163 | mgmt-number | RESTATED | also R236 |
| R164 | mgmt-number | ASR_MISHEARD |  |
| R165 | mgmt-number | ASR_MISHEARD |  |
| R166 | number-non-mgmt |  | engine or analyst-spoken, not management |
| R167 | number-non-mgmt |  | engine or analyst-spoken, not management |
| R168 | mgmt-number |  |  |
| R169 | mgmt-number |  |  |
| R170 | mgmt-number | RESTATED | also R243 |
| R171 | mgmt-number |  |  |
| R172 | mgmt-number |  |  |
| R173 | mgmt-number | RESTATED | also R127,R244 |
| R174 | mgmt-number |  |  |
| R175 | mgmt-number |  |  |

## 5a. Forward commitments
| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R209 | forward-commitment |  |  |
| R210 | forward-commitment |  |  |
| R211 | forward-commitment |  |  |
| R212 | forward-commitment |  |  |
| R213 | forward-commitment |  |  |
| R214 | forward-commitment |  |  |
| R215 | forward-commitment |  |  |
| R216 | forward-commitment |  |  |
| R217 | forward-commitment |  |  |
| R218 | forward-commitment |  |  |
| R219 | forward-commitment |  |  |
| R220 | forward-commitment |  |  |
| R221 | forward-commitment |  |  |
| R222 | forward-commitment |  |  |
| R223 | forward-commitment |  |  |
| R224 | forward-commitment | RESTATED | also R244 |
| R225 | forward-commitment | RESTATED | also R129,R132 |
| R226 | forward-commitment |  |  |
| R227 | forward-commitment | RESTATED | also R238,R264,R266; end Q3 vs Christmas/New Year timing differs |
| R228 | forward-commitment |  |  |
| R229 | forward-commitment |  |  |
| R230 | forward-commitment |  |  |
| R231 | forward-commitment |  |  |
| R232 | forward-commitment |  |  |
| R233 | forward-commitment |  |  |
| R234 | forward-commitment |  |  |
| R235 | forward-commitment | RESTATED | also R161 |
| R236 | forward-commitment | RESTATED | also R163 |
| R237 | forward-commitment |  |  |
| R238 | forward-commitment | RESTATED | also R227,R266 |
| R239 | forward-commitment |  |  |
| R240 | forward-commitment |  |  |
| R241 | forward-commitment |  |  |
| R242 | forward-commitment |  |  |
| R243 | forward-commitment | RESTATED | also R170 |
| R244 | forward-commitment | RESTATED | also R224,R173,R127 |
| R245 | forward-commitment |  |  |

## 5b. Qualifiers / hedges
| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R269 | qualifier/hedge |  |  |
| R270 | qualifier/hedge |  |  |
| R271 | qualifier/hedge |  |  |
| R272 | qualifier/hedge |  |  |
| R273 | qualifier/hedge |  |  |
| R274 | qualifier/hedge |  |  |
| R275 | qualifier/hedge |  |  |
| R276 | qualifier/hedge |  |  |
| R277 | qualifier/hedge |  |  |
| R278 | qualifier/hedge |  |  |
| R279 | qualifier/hedge |  |  |
| R280 | qualifier/hedge |  |  |
| R281 | qualifier/hedge |  |  |
| R282 | qualifier/hedge |  |  |
| R283 | qualifier/hedge | RESTATED | also R277 |
| R284 | qualifier/hedge |  |  |
| R285 | qualifier/hedge |  |  |
| R286 | qualifier/hedge | FOOTNOTE_UNRESOLVED | ROE/ROA history pairing unresolved |
| R287 | qualifier/hedge |  |  |
| R288 | qualifier/hedge |  |  |

## 6. Dates
| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R246 | date |  |  |
| R247 | date |  |  |
| R248 | date |  |  |
| R249 | date |  |  |
| R250 | date |  |  |
| R251 | date | ASR_MISHEARD |  |
| R252 | date |  |  |
| R253 | date |  |  |
| R254 | date |  |  |
| R255 | date | ASR_MISHEARD |  |
| R256 | date |  |  |
| R257 | date |  |  |
| R258 | date |  |  |
| R259 | date |  |  |
| R260 | date | ASR_MISHEARD |  |
| R261 | date |  |  |
| R262 | date |  |  |
| R263 | date |  |  |
| R264 | date |  |  |
| R265 | date | RESTATED | also R267 |
| R266 | date |  |  |
| R267 | date | RESTATED | also R265 |
| R268 | date |  |  |

## 7. Entities
| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R176 | entity | ASR_MISHEARD |  |
| R177 | entity | ASR_MISHEARD |  |
| R178 | entity |  |  |
| R179 | entity |  |  |
| R180 | entity | ASR_MISHEARD |  |
| R181 | entity |  |  |
| R182 | entity |  |  |
| R183 | entity | ASR_MISHEARD |  |
| R184 | entity |  |  |
| R185 | entity |  |  |
| R186 | entity |  |  |
| R187 | entity |  |  |
| R188 | entity |  |  |
| R189 | entity |  |  |
| R190 | entity | ASR_MISHEARD |  |
| R191 | entity |  |  |
| R192 | entity |  |  |
| R193 | entity |  |  |
| R194 | entity |  |  |
| R195 | entity |  |  |
| R196 | entity |  |  |
| R197 | entity |  |  |
| R198 | entity |  |  |
| R199 | entity |  |  |
| R200 | entity |  |  |
| R201 | entity |  |  |
| R202 | entity |  |  |
| R203 | entity | ASR_MISHEARD |  |
| R204 | entity | ASR_MISHEARD |  |
| R205 | entity | ASR_MISHEARD |  |
| R206 | entity | ASR_MISHEARD |  |
| R207 | entity |  |  |
| R208 | entity |  |  |

## 8. MISSING_FROM_STRUCTURED
none found.
