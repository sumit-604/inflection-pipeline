# A2 LEDGER: WEWORK q2fy27 concall (source ASR machine transcript; all numbers management tier, unverified)

ids_in_structured: 470 | ids_referenced_in_ledger: 470 | orphan_ids: [] | match: yes

```
=== A2 COUNT TEST ===
category: participants    grep_count: 13   sweep_count: 13   match: yes
category: turns           grep_count: 56   sweep_count: 56   match: yes
category: questions       grep_count: 19   sweep_count: 19   match: yes
category: mgmt_numbers    grep_count: 233  sweep_count: 233  match: yes
category: forward         grep_count: 60   sweep_count: 60   match: yes
category: hedges          grep_count: 46   sweep_count: 46   match: yes
category: dates           grep_count: 36   sweep_count: 36   match: yes
category: entities_other  grep_count: 26   sweep_count: 26   match: yes
category: zero_standing   grep_count: 0    sweep_count: 0    match: yes
structured per-table header: NUMBER 233, ENTITY 39 (13 participants + 26 other), FORWARD 60, DATE 36, QUALIFIER 46, QA 56 = 470
gate_a2: pass
=== END COUNT TEST ===
```

Row format: ROW_ID | category | A2 flags | page / line / turn | note. Claim text stays in A1 structured file at the ID.
Flags: ASR_UNCERTAIN = A1 marked possible mishearing; ASR_GAP = known transcript defect; ASR_NAME = name as heard.
ZERO_STANDING: none (a concall has no standing line items). MGMT_ABSENCE: none (MD and CEO speaks, R235/R416). ENTITY_CHANGE: none (no prior ledger). MISSING_FROM_STRUCTURED: none.


## 1. PARTICIPANTS (n=13)

R235 | participant | ASR_NAME | p1 L32 T01 | MD and CEO present; no MGMT_ABSENCE
R236 | participant | ASR_NAME | p1 L33 T02 | speaker/analyst/moderator identity
R237 | participant | ASR_NAME | p1 L33 T02 | speaker/analyst/moderator identity
R251 | participant | ASR_NAME | p2 L160 T03 | Cliff/Clifford (R262) same speaker as heard; designation not given
R255 | participant | ASR_NAME, ASR_GAP | p3 L245 T05 | first analyst unidentified; name and firm NOT FOUND
R256 | participant | ASR_NAME | p4 L403 T13 | speaker/analyst/moderator identity
R261 | participant | ASR_NAME | p4 L521 T17 | speaker/analyst/moderator identity
R262 | participant | ASR_NAME | p5 L661 T23 | speaker/analyst/moderator identity
R263 | participant | ASR_NAME | p5 L682 T27 | speaker/analyst/moderator identity
R264 | participant | ASR_NAME | p5 L738 T32 | speaker/analyst/moderator identity
R268 | participant | ASR_NAME | p6 L845 T37 | speaker/analyst/moderator identity
R271 | participant | ASR_NAME | p7 L895 T42 | firm not stated
R272 | participant | ASR_UNCERTAIN, ASR_NAME, ASR_GAP | p7 L919 T47 | last analyst unidentified; name and firm NOT FOUND

## 2. SPEAKER TURNS (T01-T56) (n=56)

R415 | speaker turn | - | p1 L32 T01
R416 | speaker turn | - | p1 L33 T02
R417 | speaker turn | - | p2 L160 T03
R418 | speaker turn | - | p2 L223 T04
R419 | speaker turn | - | p2 L239 T05
R420 | speaker turn | ASR_GAP | p3 L246 T06 | first analyst intro lost, hallucinated heading near 00:20:00 (src line 222)
R421 | speaker turn | - | p3 L255 T07
R422 | speaker turn | - | p3 L304 T08
R423 | speaker turn | - | p3 L311 T09
R424 | speaker turn | - | p3 L348 T10
R425 | speaker turn | - | p3 L355 T11
R426 | speaker turn | - | p4 L402 T12
R427 | speaker turn | - | p4 L403 T13
R428 | speaker turn | - | p4 L404 T14
R429 | speaker turn | - | p4 L413 T15
R430 | speaker turn | - | p4 L518 T16
R431 | speaker turn | - | p4 L521 T17
R432 | speaker turn | - | p4 L526 T18
R433 | speaker turn | - | p4 L534 T19
R434 | speaker turn | - | p4 L581 T20
R435 | speaker turn | - | p4 L589 T21
R436 | speaker turn | ASR_GAP | p5 L647 T22 | audio break 00:43:18-00:43:46, ROCE answer repeated; not a distinct turn
R437 | speaker turn | - | p5 L660 T23
R438 | speaker turn | - | p5 L665 T24
R439 | speaker turn | - | p5 L674 T25
R440 | speaker turn | - | p5 L677 T26
R441 | speaker turn | - | p5 L682 T27
R442 | speaker turn | - | p5 L684 T28
R443 | speaker turn | - | p5 L696 T29
R444 | speaker turn | - | p5 L734 T30
R445 | speaker turn | - | p5 L735 T31
R446 | speaker turn | - | p5 L738 T32
R447 | speaker turn | - | p5 L741 T33
R448 | speaker turn | - | p6 L744 T34
R449 | speaker turn | - | p6 L789 T35
R450 | speaker turn | - | p6 L803 T36
R451 | speaker turn | - | p6 L845 T37
R452 | speaker turn | - | p6 L848 T38
R453 | speaker turn | - | p6 L854 T39
R454 | speaker turn | - | p6 L875 T40
R455 | speaker turn | - | p6 L879 T41
R456 | speaker turn | - | p7 L895 T42
R457 | speaker turn | - | p7 L897 T43
R458 | speaker turn | - | p7 L900 T44
R459 | speaker turn | - | p7 L913 T45
R460 | speaker turn | - | p7 L915 T46
R461 | speaker turn | - | p7 L919 T47
R462 | speaker turn | - | p7 L921 T48
R463 | speaker turn | - | p7 L924 T49
R464 | speaker turn | - | p7 L926 T50
R465 | speaker turn | - | p7 L928 T51
R466 | speaker turn | - | p7 L936 T52
R467 | speaker turn | - | p7 L941 T53
R468 | speaker turn | - | p7 L950 T54
R469 | speaker turn | - | p7 L952 T55
R470 | speaker turn | - | p7 L956 T56

## 3. QUESTIONS (analyst Qs) (n=19)

R420 | analyst question | - | p3 L246 T06
R422 | analyst question | - | p3 L304 T08
R424 | analyst question | - | p3 L348 T10
R428 | analyst question | - | p4 L404 T14
R432 | analyst question | REPEAT_QUESTION | p4 L526 T18 | renewal question also at R422 and R452
R434 | analyst question | - | p4 L581 T20 | renewal capex follow-up to R432
R437 | analyst question | - | p5 L660 T23
R439 | analyst question | - | p5 L674 T25 | clarification of R437
R442 | analyst question | - | p5 L684 T28
R444 | analyst question | REPEAT_QUESTION | p5 L734 T30 | margin follow-up to R442; margin also R447
R447 | analyst question | - | p5 L741 T33
R449 | analyst question | - | p6 L789 T35
R452 | analyst question | REPEAT_QUESTION | p6 L848 T38 | renewal/expiry question also at R422 and R432
R454 | analyst question | - | p6 L875 T40 | follow-up to R452
R457 | analyst question | - | p7 L897 T43
R459 | analyst question | REPEAT_QUESTION | p7 L913 T45 | pledge follow-up to R457
R462 | analyst question | - | p7 L921 T48
R464 | analyst question | - | p7 L926 T50
R466 | analyst question | - | p7 L936 T52 | follow-up to R464

## 4. MANAGEMENT NUMBERS (T = turn containing the line) (n=233)

R001 | mgmt number | - | p1 L44 T02
R002 | mgmt number | - | p1 L45 T02
R003 | mgmt number | - | p1 L46 T02
R004 | mgmt number | - | p1 L46 T02
R005 | mgmt number | - | p1 L47 T02
R006 | mgmt number | - | p1 L47 T02
R007 | mgmt number | - | p1 L48 T02
R008 | mgmt number | ASR_UNCERTAIN | p1 L48 T02
R009 | mgmt number | - | p1 L50 T02
R010 | mgmt number | - | p1 L52 T02
R011 | mgmt number | - | p1 L53 T02
R012 | mgmt number | - | p1 L54 T02
R013 | mgmt number | - | p1 L57 T02
R014 | mgmt number | - | p1 L58 T02
R015 | mgmt number | - | p1 L59 T02
R016 | mgmt number | - | p1 L63 T02
R017 | mgmt number | - | p1 L64 T02
R018 | mgmt number | - | p1 L65 T02
R019 | mgmt number | - | p1 L67 T02
R020 | mgmt number | - | p1 L68 T02
R021 | mgmt number | - | p1 L70 T02
R022 | mgmt number | - | p1 L71 T02
R023 | mgmt number | - | p1 L79 T02
R024 | mgmt number | - | p1 L80 T02
R025 | mgmt number | - | p1 L80 T02
R026 | mgmt number | - | p1 L81 T02
R027 | mgmt number | - | p1 L85 T02
R028 | mgmt number | - | p1 L91 T02
R029 | mgmt number | - | p1 L92 T02
R030 | mgmt number | - | p1 L93 T02
R031 | mgmt number | - | p1 L94 T02
R032 | mgmt number | - | p1 L94 T02
R033 | mgmt number | - | p1 L97 T02
R034 | mgmt number | - | p1 L97 T02
R035 | mgmt number | - | p1 L98 T02
R036 | mgmt number | - | p1 L100 T02
R037 | mgmt number | - | p1 L100 T02
R038 | mgmt number | - | p1 L101 T02
R039 | mgmt number | - | p1 L105 T02
R040 | mgmt number | - | p1 L119 T02
R041 | mgmt number | ASR_UNCERTAIN | p1 L121 T02
R042 | mgmt number | - | p1 L121 T02
R043 | mgmt number | - | p1 L121 T02
R044 | mgmt number | - | p1 L121 T02
R045 | mgmt number | ASR_UNCERTAIN | p1 L123 T02
R046 | mgmt number | - | p1 L123 T02
R047 | mgmt number | ASR_UNCERTAIN | p1 L123 T02
R048 | mgmt number | - | p1 L123 T02
R049 | mgmt number | ASR_UNCERTAIN | p1 L123 T02
R050 | mgmt number | - | p1 L124 T02
R051 | mgmt number | - | p1 L124 T02
R052 | mgmt number | - | p1 L125 T02
R053 | mgmt number | - | p1 L125 T02
R054 | mgmt number | - | p1 L127 T02
R055 | mgmt number | - | p1 L127 T02
R056 | mgmt number | - | p1 L127 T02
R057 | mgmt number | - | p1 L128 T02
R058 | mgmt number | - | p1 L128 T02
R059 | mgmt number | - | p1 L128 T02
R060 | mgmt number | - | p1 L129 T02
R061 | mgmt number | ASR_UNCERTAIN | p1 L129 T02
R062 | mgmt number | - | p1 L130 T02
R063 | mgmt number | - | p1 L131 T02
R064 | mgmt number | - | p1 L132 T02
R065 | mgmt number | - | p1 L132 T02
R066 | mgmt number | - | p1 L133 T02
R067 | mgmt number | - | p1 L133 T02
R068 | mgmt number | - | p1 L134 T02
R069 | mgmt number | - | p1 L134 T02
R070 | mgmt number | - | p1 L135 T02
R071 | mgmt number | - | p1 L136 T02
R072 | mgmt number | - | p1 L136 T02
R073 | mgmt number | - | p1 L136 T02
R074 | mgmt number | ASR_UNCERTAIN | p1 L137 T02
R075 | mgmt number | - | p1 L137 T02
R076 | mgmt number | - | p1 L138 T02
R077 | mgmt number | - | p1 L139 T02
R078 | mgmt number | - | p1 L140 T02
R079 | mgmt number | - | p2 L143 T02
R080 | mgmt number | - | p2 L143 T02
R081 | mgmt number | - | p2 L144 T02
R082 | mgmt number | - | p2 L145 T02
R083 | mgmt number | - | p2 L145 T02
R084 | mgmt number | - | p2 L146 T02
R085 | mgmt number | - | p2 L147 T02
R086 | mgmt number | - | p2 L147 T02
R087 | mgmt number | - | p2 L148 T02
R088 | mgmt number | - | p2 L149 T02
R089 | mgmt number | - | p2 L149 T02
R090 | mgmt number | ASR_UNCERTAIN | p2 L152 T02
R091 | mgmt number | - | p2 L152 T02
R092 | mgmt number | - | p2 L153 T02
R093 | mgmt number | - | p2 L153 T02
R094 | mgmt number | - | p2 L154 T02
R095 | mgmt number | - | p2 L155 T02
R096 | mgmt number | ASR_UNCERTAIN | p2 L155 T02
R097 | mgmt number | - | p2 L156 T02
R098 | mgmt number | - | p2 L156 T02
R099 | mgmt number | - | p2 L157 T02
R100 | mgmt number | - | p2 L158 T02
R101 | mgmt number | - | p2 L162 T03
R102 | mgmt number | - | p2 L162 T03
R103 | mgmt number | - | p2 L164 T03
R104 | mgmt number | - | p2 L164 T03
R105 | mgmt number | - | p2 L165 T03
R106 | mgmt number | - | p2 L165 T03
R107 | mgmt number | - | p2 L165 T03
R108 | mgmt number | - | p2 L167 T03
R109 | mgmt number | - | p2 L167 T03
R110 | mgmt number | - | p2 L169 T03
R111 | mgmt number | - | p2 L169 T03
R112 | mgmt number | - | p2 L170 T03
R113 | mgmt number | - | p2 L170 T03
R114 | mgmt number | - | p2 L171 T03
R115 | mgmt number | - | p2 L171 T03
R116 | mgmt number | - | p2 L172 T03
R117 | mgmt number | - | p2 L173 T03
R118 | mgmt number | ASR_UNCERTAIN | p2 L174 T03
R119 | mgmt number | - | p2 L176 T03
R120 | mgmt number | - | p2 L181 T03
R121 | mgmt number | - | p2 L181 T03
R122 | mgmt number | - | p2 L183 T03
R123 | mgmt number | ASR_UNCERTAIN | p2 L183 T03
R124 | mgmt number | - | p2 L184 T03
R125 | mgmt number | - | p2 L184 T03
R126 | mgmt number | - | p2 L185 T03
R127 | mgmt number | - | p2 L185 T03
R128 | mgmt number | - | p2 L186 T03
R129 | mgmt number | - | p2 L187 T03
R130 | mgmt number | - | p2 L187 T03
R131 | mgmt number | ASR_UNCERTAIN | p2 L187 T03
R132 | mgmt number | - | p2 L188 T03
R133 | mgmt number | - | p2 L188 T03
R134 | mgmt number | - | p2 L190 T03
R135 | mgmt number | - | p2 L191 T03
R136 | mgmt number | - | p2 L191 T03
R137 | mgmt number | - | p2 L192 T03
R138 | mgmt number | - | p2 L192 T03
R139 | mgmt number | - | p2 L196 T03
R140 | mgmt number | ASR_UNCERTAIN | p2 L196 T03
R141 | mgmt number | - | p2 L196 T03
R142 | mgmt number | - | p2 L196 T03
R143 | mgmt number | - | p2 L197 T03
R144 | mgmt number | ASR_UNCERTAIN | p2 L197 T03
R145 | mgmt number | ASR_UNCERTAIN | p2 L197 T03
R146 | mgmt number | ASR_UNCERTAIN | p2 L197 T03
R147 | mgmt number | - | p2 L198 T03
R148 | mgmt number | - | p2 L199 T03
R149 | mgmt number | - | p2 L199 T03
R150 | mgmt number | - | p2 L200 T03
R151 | mgmt number | - | p2 L201 T03
R152 | mgmt number | - | p2 L202 T03
R153 | mgmt number | ASR_UNCERTAIN | p2 L206 T03
R154 | mgmt number | - | p2 L207 T03
R155 | mgmt number | - | p2 L207 T03
R156 | mgmt number | - | p2 L207 T03
R157 | mgmt number | - | p2 L207 T03
R158 | mgmt number | - | p2 L208 T03
R159 | mgmt number | - | p2 L208 T03
R160 | mgmt number | - | p2 L208 T03
R161 | mgmt number | - | p2 L209 T03
R162 | mgmt number | - | p2 L210 T03
R163 | mgmt number | - | p2 L211 T03
R164 | mgmt number | - | p2 L211 T03
R165 | mgmt number | - | p2 L213 T03
R166 | mgmt number | - | p2 L213 T03
R167 | mgmt number | ASR_UNCERTAIN | p2 L215 T03
R168 | mgmt number | - | p2 L216 T03
R169 | mgmt number | - | p2 L216 T03
R170 | mgmt number | ASR_UNCERTAIN | p2 L217 T03
R171 | mgmt number | ASR_UNCERTAIN | p2 L217 T03
R172 | mgmt number | - | p2 L221 T03
R173 | mgmt number | - | p3 L257 T07
R174 | mgmt number | - | p3 L312 T09
R175 | mgmt number | - | p3 L313 T09
R176 | mgmt number | ASR_UNCERTAIN | p3 L315 T09
R177 | mgmt number | - | p3 L323 T09
R178 | mgmt number | - | p3 L323 T09
R179 | mgmt number | - | p3 L327 T09
R180 | mgmt number | ASR_UNCERTAIN | p3 L333 T09
R181 | mgmt number | - | p3 L334 T09
R182 | mgmt number | - | p3 L336 T09
R183 | mgmt number | - | p3 L336 T09
R184 | mgmt number | - | p3 L337 T09
R185 | mgmt number | - | p3 L338 T09
R186 | mgmt number | - | p3 L338 T09
R187 | mgmt number | - | p3 L338 T09
R188 | mgmt number | - | p3 L339 T09
R189 | mgmt number | - | p3 L340 T09
R190 | mgmt number | - | p4 L407 T14
R191 | mgmt number | - | p4 L414 T15
R192 | mgmt number | - | p4 L415 T15
R193 | mgmt number | - | p4 L499 T15
R194 | mgmt number | - | p4 L528 T18
R195 | mgmt number | - | p4 L572 T19
R196 | mgmt number | ASR_UNCERTAIN | p4 L584 T20
R197 | mgmt number | - | p4 L585 T20
R198 | mgmt number | - | p5 L637 T21
R199 | mgmt number | - | p5 L661 T23
R200 | mgmt number | - | p5 L665 T24
R201 | mgmt number | - | p5 L687 T28
R202 | mgmt number | - | p5 L701 T29
R203 | mgmt number | - | p5 L703 T29
R204 | mgmt number | ASR_UNCERTAIN | p5 L704 T29
R205 | mgmt number | - | p5 L707 T29
R206 | mgmt number | - | p6 L743 T33
R207 | mgmt number | - | p6 L749 T34
R208 | mgmt number | - | p6 L756 T34
R209 | mgmt number | - | p6 L779 T34
R210 | mgmt number | - | p6 L783 T34
R211 | mgmt number | ASR_UNCERTAIN | p6 L790 T35
R212 | mgmt number | ASR_UNCERTAIN | p6 L791 T35
R213 | mgmt number | ASR_UNCERTAIN | p6 L794 T35
R214 | mgmt number | - | p6 L794 T35
R215 | mgmt number | ASR_UNCERTAIN | p6 L800 T35
R216 | mgmt number | - | p6 L812 T36
R217 | mgmt number | - | p6 L821 T36
R218 | mgmt number | - | p6 L829 T36
R219 | mgmt number | - | p6 L829 T36
R220 | mgmt number | - | p6 L830 T36
R221 | mgmt number | - | p6 L830 T36
R222 | mgmt number | - | p6 L851 T38
R223 | mgmt number | - | p6 L851 T38
R224 | mgmt number | - | p6 L855 T39
R225 | mgmt number | - | p6 L859 T39
R226 | mgmt number | - | p6 L865 T39
R227 | mgmt number | ASR_UNCERTAIN | p6 L867 T39
R228 | mgmt number | - | p6 L883 T41
R229 | mgmt number | - | p7 L898 T43
R230 | mgmt number | - | p7 L910 T44
R231 | mgmt number | ASR_UNCERTAIN | p7 L923 T48
R232 | mgmt number | - | p7 L928 T51
R233 | mgmt number | - | p7 L933 T51

## 5a. FORWARD COMMITMENTS (n=60)

R273 | forward commitment | - | p2 L146 T02
R274 | forward commitment | - | p2 L147 T02
R275 | forward commitment | - | p2 L149 T02
R276 | forward commitment | - | p2 L149 T02
R277 | forward commitment | - | p2 L150 T02
R278 | forward commitment | - | p3 L257 T07
R279 | forward commitment | - | p3 L266 T07
R280 | forward commitment | - | p3 L267 T07
R281 | forward commitment | - | p3 L279 T07
R282 | forward commitment | - | p3 L323 T09
R283 | forward commitment | - | p3 L342 T09
R284 | forward commitment | - | p3 L345 T09
R285 | forward commitment | - | p3 L356 T11
R286 | forward commitment | - | p3 L361 T11
R287 | forward commitment | - | p3 L370 T11
R288 | forward commitment | - | p3 L372 T11
R289 | forward commitment | - | p3 L374 T11
R290 | forward commitment | - | p3 L378 T11
R291 | forward commitment | - | p3 L383 T11
R292 | forward commitment | - | p3 L387 T11
R293 | forward commitment | - | p3 L399 T11
R294 | forward commitment | - | p4 L421 T15
R295 | forward commitment | - | p4 L476 T15
R296 | forward commitment | - | p5 L641 T21
R297 | forward commitment | - | p5 L646 T21
R298 | forward commitment | - | p5 L665 T24
R299 | forward commitment | - | p5 L708 T29
R300 | forward commitment | - | p5 L710 T29
R301 | forward commitment | - | p5 L714 T29
R302 | forward commitment | - | p5 L723 T29
R303 | forward commitment | - | p5 L725 T29
R304 | forward commitment | - | p5 L727 T29
R305 | forward commitment | - | p5 L730 T29
R306 | forward commitment | - | p5 L736 T31
R307 | forward commitment | - | p6 L762 T34
R308 | forward commitment | - | p6 L772 T34
R309 | forward commitment | - | p6 L778 T34
R310 | forward commitment | - | p6 L786 T34
R311 | forward commitment | ASR_UNCERTAIN | p6 L794 T35
R312 | forward commitment | - | p6 L810 T36
R313 | forward commitment | - | p6 L821 T36
R314 | forward commitment | - | p6 L825 T36
R315 | forward commitment | - | p6 L829 T36
R316 | forward commitment | - | p6 L837 T36
R317 | forward commitment | - | p6 L862 T39
R318 | forward commitment | - | p6 L869 T39
R319 | forward commitment | - | p6 L872 T39
R320 | forward commitment | - | p6 L879 T41
R321 | forward commitment | - | p6 L883 T41
R322 | forward commitment | - | p6 L890 T41
R323 | forward commitment | - | p7 L901 T44 | promoter pledge
R324 | forward commitment | - | p7 L904 T44 | promoter pledge
R325 | forward commitment | - | p7 L909 T44 | promoter pledge
R326 | forward commitment | - | p7 L915 T46 | promoter pledge
R327 | forward commitment | - | p7 L928 T51
R328 | forward commitment | - | p7 L929 T51
R329 | forward commitment | - | p7 L931 T51
R330 | forward commitment | - | p7 L934 T51
R331 | forward commitment | - | p7 L942 T53
R332 | forward commitment | - | p7 L952 T55

## 5b. HEDGES / QUALIFIERS (n=46)

R369 | hedge/qualifier | - | p1 L22 T01
R370 | hedge/qualifier | - | p1 L25 T01
R371 | hedge/qualifier | - | p1 L26 T01
R372 | hedge/qualifier | - | p1 L34 T02
R373 | hedge/qualifier | FOOTNOTE_UNRESOLVED | p1 L48 T02
R374 | hedge/qualifier | - | p1 L68 T02
R375 | hedge/qualifier | - | p1 L91 T02
R376 | hedge/qualifier | - | p1 L121 T02
R377 | hedge/qualifier | - | p1 L127 T02
R378 | hedge/qualifier | - | p1 L137 T02
R379 | hedge/qualifier | - | p2 L152 T02
R380 | hedge/qualifier | - | p2 L155 T02
R381 | hedge/qualifier | - | p2 L164 T03
R382 | hedge/qualifier | - | p2 L165 T03
R383 | hedge/qualifier | - | p2 L174 T03
R384 | hedge/qualifier | ASR_UNCERTAIN | p2 L181 T03
R385 | hedge/qualifier | ASR_UNCERTAIN | p2 L183 T03
R386 | hedge/qualifier | - | p2 L205 T03
R387 | hedge/qualifier | - | p2 L207 T03
R388 | hedge/qualifier | - | p2 L209 T03
R389 | hedge/qualifier | - | p2 L217 T03
R390 | hedge/qualifier | - | p2 L219 T03
R391 | hedge/qualifier | - | p2 L221 T03
R392 | hedge/qualifier | FOOTNOTE_UNRESOLVED | p3 L245 T05
R393 | hedge/qualifier | ASR_UNCERTAIN | p3 L315 T09
R394 | hedge/qualifier | - | p3 L323 T09
R395 | hedge/qualifier | - | p3 L325 T09
R396 | hedge/qualifier | - | p3 L339 T09
R397 | hedge/qualifier | - | p4 L413 T15
R398 | hedge/qualifier | - | p4 L415 T15
R399 | hedge/qualifier | - | p4 L424 T15
R400 | hedge/qualifier | - | p4 L537 T19
R401 | hedge/qualifier | - | p4 L546 T19
R402 | hedge/qualifier | - | p5 L643 T21
R403 | hedge/qualifier | - | p5 L647 T22
R404 | hedge/qualifier | - | p5 L654 T22
R405 | hedge/qualifier | - | p5 L666 T24
R406 | hedge/qualifier | - | p5 L677 T26
R407 | hedge/qualifier | - | p5 L697 T29
R408 | hedge/qualifier | - | p6 L744 T34
R409 | hedge/qualifier | - | p6 L754 T34
R410 | hedge/qualifier | - | p6 L778 T34
R411 | hedge/qualifier | - | p6 L803 T36
R412 | hedge/qualifier | - | p6 L804 T36
R413 | hedge/qualifier | - | p6 L814 T36
R414 | hedge/qualifier | - | p7 L912 T44

## 6. DATES AND TIMELINES (n=36)

R333 | date/timeline | - | p1 L24 T01
R334 | date/timeline | - | p1 L33 T02
R335 | date/timeline | - | p1 L44 T02
R336 | date/timeline | - | p1 L50 T02
R337 | date/timeline | - | p1 L119 T02
R338 | date/timeline | - | p1 L123 T02
R339 | date/timeline | - | p1 L123 T02
R340 | date/timeline | - | p1 L123 T02
R341 | date/timeline | - | p2 L149 T02
R342 | date/timeline | - | p2 L150 T02
R343 | date/timeline | - | p2 L190 T03
R344 | date/timeline | - | p2 L192 T03
R345 | date/timeline | - | p2 L192 T03
R346 | date/timeline | - | p2 L208 T03
R347 | date/timeline | - | p2 L213 T03
R348 | date/timeline | - | p2 L213 T03
R349 | date/timeline | - | p3 L257 T07
R350 | date/timeline | - | p3 L302 T07
R351 | date/timeline | - | p3 L371 T11
R352 | date/timeline | - | p4 L444 T15
R353 | date/timeline | - | p4 L569 T19
R354 | date/timeline | - | p5 L637 T21
R355 | date/timeline | - | p5 L702 T29
R356 | date/timeline | - | p5 L705 T29
R357 | date/timeline | - | p5 L711 T29
R358 | date/timeline | - | p5 L725 T29
R359 | date/timeline | - | p5 L729 T29
R360 | date/timeline | - | p5 L735 T31
R361 | date/timeline | - | p6 L779 T34
R362 | date/timeline | ASR_UNCERTAIN | p6 L793 T35
R363 | date/timeline | - | p6 L826 T36
R364 | date/timeline | - | p6 L843 T36
R365 | date/timeline | - | p6 L865 T39
R366 | date/timeline | - | p7 L927 T50
R367 | date/timeline | - | p7 L928 T51
R368 | date/timeline | - | p7 L931 T51

## 7. OTHER ENTITIES (n=26)

R234 | entity (non-participant) | - | p1 L24 T01
R238 | entity (non-participant) | - | p1 L34 T02
R239 | entity (non-participant) | - | p1 L46 T02
R240 | entity (non-participant) | - | p1 L48 T02
R241 | entity (non-participant) | - | p1 L69 T02
R242 | entity (non-participant) | - | p1 L93 T02
R243 | entity (non-participant) | - | p1 L95 T02
R244 | entity (non-participant) | - | p1 L96 T02
R245 | entity (non-participant) | - | p1 L134 T02
R246 | entity (non-participant) | - | p1 L140 T02
R247 | entity (non-participant) | - | p2 L143 T02
R248 | entity (non-participant) | - | p2 L143 T02
R249 | entity (non-participant) | - | p2 L144 T02
R250 | entity (non-participant) | - | p2 L144 T02
R252 | entity (non-participant) | - | p2 L170 T03
R253 | entity (non-participant) | - | p2 L176 T03
R254 | entity (non-participant) | - | p2 L217 T03
R257 | entity (non-participant) | - | p4 L445 T15
R258 | entity (non-participant) | - | p4 L446 T15
R259 | entity (non-participant) | - | p4 L449 T15
R260 | entity (non-participant) | - | p4 L449 T15
R265 | entity (non-participant) | - | p6 L749 T34
R266 | entity (non-participant) | - | p6 L749 T34
R267 | entity (non-participant) | - | p6 L750 T34
R269 | entity (non-participant) | CUSTOMER_EXIT_RISK | p6 L865 T39 | large customer may move out
R270 | entity (non-participant) | ASR_UNCERTAIN | p6 L866 T39

## 8. CROSS-REFERENCES AND MATERIALITY (A2 observations, no interpretation)
- RESTATED, desks and seat target: R275/R276 (FY27 guidance 150-155k, 190-200k) reappear in QA R442/R443 (150k as of Oct 5).
- RESTATED, renewal rate: R423, R433, R453 (80 to 85%) across three answers; questions R422, R432, R452 are REPEAT_QUESTION.
- RESTATED, promoter pledge: R229, R230, R323-R326, R414 and QA R457-R460.
- RESTATED, capex: QA R465 (~500 cr FY27, ~600 cr FY28) answers R464.
- ASR_GAP: R255/R420 (first analyst intro, 00:20:00-00:20:55) and R436 (audio break 00:43:18-00:43:46). Answers near those spans may be incomplete.
- ASR_UNCERTAIN: 38 rows flagged by A1; A3 should not rely on them without filed documents.
- Turns: 56 turns from A1's QA table, moderator hand-offs counted. Q&A opens at T04 (R419).
