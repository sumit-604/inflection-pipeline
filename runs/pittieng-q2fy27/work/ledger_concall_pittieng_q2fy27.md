# LEDGER: concall PITTIENG Q2 FY27 (A2 ENUMERATOR)

Source: A1 structured extraction runs/pittieng-q2fy27/extracted/pittieng-concall-q2fy27-structured.md. Row IDs are CONCALL rows (restart per document; R001-R589 here are not filing rows).
Source is machine ASR of a partial recording (opening remarks missing). Speaker labels INFERRED. 'block' (5-minute call block, b0-b10) replaces page. A1 flags ASR_UNCERTAIN, MIXED, INFERRED carried through. Row IDs are referenced, not re-copied; read values in the structured file.

=== A2 COUNT TEST ===
ids_in_structured: 589 | ids_referenced_in_ledger: 589 | orphan_ids: [] | match: yes
category: turns         grep_count: 158  sweep_count: 158  match: yes  (A1 header 158)
category: questions     grep_count: 47  sweep_count: 47  match: yes  (A1 header 47)
category: mgmt_numbers  grep_count: 176 NUMBER rows  sweep_count: 176  match: yes  (A1 header 176); by enclosing turn: management 107, analyst-cited 68, other 1
category: forward       grep_count: 60  sweep_count: 60  match: yes  (A1 header 60)
category: entities      grep_count: 50  sweep_count: 50  match: yes  (A1 header 50)
category: dates         grep_count: 37  sweep_count: 37  match: yes  (A1 header 37)
category: qualifiers    grep_count: 61  sweep_count: 61  match: yes  (A1 header 61)
category: zero_standing: 0 (concall has no financial tables)
gate_a2: pass
=== END COUNT TEST ===

## 1. PARTICIPANTS
Management: unnamed in the recording (A1: management speakers unnamed). Moderator: unnamed. Analyst names below come from moderator lines (ASR spelling). Firm: NOT FOUND in recording.
MGMT_ABSENCE: promoter/CMD presence cannot be tested; opening remarks missing so no management roster exists in this extraction. Flag MGMT_ABSENCE (UNTESTABLE, coverage gap), refs R001, R382.

| ROW_ID | category | A2 flags | note |
|---|---|---|---|
| R013 | participant analyst | INFERRED | fulltext L77-L96; opens: "Hi sir, good afternoon. Thank you."; INFERRED; Mohit Jain (moderator-named); turn 13 |
| R029 | participant analyst | INFERRED | fulltext L180-L185; opens: "Yeah, hi Akshay."; INFERRED; Mayank Chaturbe (moderator-named); turn 29 |
| R047 | participant analyst | INFERRED | fulltext L279-L284; opens: "Yeah."; INFERRED; Pratik Jain (moderator-named); turn 47 |
| R061 | participant analyst | INFERRED | fulltext L338-L341; opens: "Thank you."; INFERRED; Vive Ganguly (moderator-named); turn 61 |
| R070 | participant analyst | INFERRED | fulltext L367-L370; opens: "Good afternoon sir. Thank you so much for the"; INFERRED; Baala Subramanian (moderator-named); turn 70 |
| R078 | participant analyst | INFERRED | fulltext L401-L403; opens: "Yeah, hi. Congratulations on a strong quarter."; INFERRED; Rahul Kumar (moderator-named); turn 78 |
| R090 | participant analyst | INFERRED | fulltext L451-L454; opens: "Hi."; INFERRED; Kanant Ravedi (moderator-named); turn 90 |
| R098 | participant analyst | INFERRED | fulltext L479-L479; opens: "Hello, am I audible?"; INFERRED; Saksham Tyagi (moderator-named); turn 98 |
| R108 | participant analyst | INFERRED | fulltext L532-L532; opens: "Yeah, am I audible?"; INFERRED; Abhijit Mathura (moderator-named); turn 108 |
| R118 | participant analyst | INFERRED | fulltext L613-L644; opens: "Good afternoon, sir."; INFERRED; Rabindranath Nayak (moderator-named); turn 118 |
| R128 | participant analyst | INFERRED | fulltext L689-L690; opens: "Hello. Thank you for giving me the opportunity. My"; INFERRED; Lavya Baldota (moderator-named); turn 128 |
| R133 | participant analyst | INFERRED | fulltext L700-L704; opens: "Hello, sir. Am I out of them? Yes. My"; INFERRED; Preneru Chatterjee (moderator-named); turn 133 |

## 2. SPEAKER TURNS (sequential turn number)
| turn# | ROW_ID | speaker | block | ts | A2 flags | note |
|---|---|---|---|---|---|---|
| 1 | R001 | ANALYST | block 0 | [00:00] | INFERRED | line 33 |
| 2 | R002 | MANAGEMENT | block 0 | [00:25] | INFERRED MIXED | line 37 |
| 3 | R003 | ANALYST | block 0 | [01:11] | INFERRED MIXED | line 42 |
| 4 | R004 | MANAGEMENT | block 0 | [01:45] | INFERRED | line 47 |
| 5 | R005 | ANALYST | block 0 | [02:20] | INFERRED MIXED | line 53 |
| 6 | R006 | MANAGEMENT | block 0 | [02:48] | INFERRED | line 57 |
| 7 | R007 | ANALYST | block 0 | [03:15] | INFERRED MIXED | line 61 |
| 8 | R008 | MANAGEMENT | block 0 | [03:50] | INFERRED | line 66 |
| 9 | R009 | ANALYST | block 0 | [04:15] | INFERRED MIXED | line 70 |
| 10 | R010 | MANAGEMENT | block 0 | [04:23] | INFERRED MIXED | line 71 |
| 11 | R011 | ANALYST | block 0 | [04:41] | INFERRED | line 74 |
| 12 | R012 | MODERATOR | block 0 | [04:47] | INFERRED | line 75 |
| 13 | R013 | ANALYST | block 0 | [04:57] | INFERRED | line 77; moderator-named: fulltext L77-L96; opens: "Hi sir, good afternoon. Thank you."; INFERRED; Mohit Jain |
| 14 | R014 | MANAGEMENT | block 1 | [05:47] | INFERRED | line 97 |
| 15 | R015 | ANALYST | block 1 | [06:00] | INFERRED | line 101 |
| 16 | R016 | MANAGEMENT | block 1 | [06:02] | INFERRED | line 102 |
| 17 | R017 | ANALYST | block 1 | [06:24] | INFERRED | line 111 |
| 18 | R018 | MANAGEMENT | block 1 | [06:37] | INFERRED | line 116 |
| 19 | R019 | ANALYST | block 1 | [06:59] | INFERRED | line 124 |
| 20 | R020 | MANAGEMENT | block 1 | [07:17] | INFERRED | line 132 |
| 21 | R021 | ANALYST | block 1 | [07:33] | INFERRED | line 137 |
| 22 | R022 | MANAGEMENT | block 1 | [08:02] | INFERRED | line 147 |
| 23 | R023 | ANALYST | block 1 | [08:49] | INFERRED | line 164 |
| 24 | R024 | MANAGEMENT | block 1 | [08:51] | INFERRED | line 167 |
| 25 | R025 | ANALYST | block 1 | [08:55] | INFERRED | line 169 |
| 26 | R026 | MANAGEMENT | block 1 | [08:57] | INFERRED | line 170 |
| 27 | R027 | ANALYST | block 1 | [08:59] | INFERRED | line 173 |
| 28 | R028 | MODERATOR | block 1 | [09:04] | INFERRED | line 176 |
| 29 | R029 | ANALYST | block 1 | [09:13] | INFERRED | line 180; moderator-named: fulltext L180-L185; opens: "Yeah, hi Akshay."; INFERRED; Mayank Chaturbe |
| 30 | R030 | MANAGEMENT | block 1 | [09:30] | INFERRED MIXED | line 186 |
| 31 | R031 | ANALYST | block 2 | [10:54] | INFERRED | line 211 |
| 32 | R032 | MANAGEMENT | block 2 | [11:07] | INFERRED MIXED | line 214 |
| 33 | R033 | ANALYST | block 2 | [11:30] | INFERRED | line 221 |
| 34 | R034 | MANAGEMENT | block 2 | [11:41] | INFERRED | line 225 |
| 35 | R035 | ANALYST | block 2 | [11:55] | INFERRED | line 227 |
| 36 | R036 | MANAGEMENT | block 2 | [11:57] | INFERRED | line 229 |
| 37 | R037 | ANALYST | block 2 | [12:03] | INFERRED | line 231 |
| 38 | R038 | MANAGEMENT | block 2 | [12:13] | INFERRED | line 235 |
| 39 | R039 | ANALYST | block 2 | [13:15] | INFERRED | line 252 |
| 40 | R040 | MANAGEMENT | block 2 | [13:28] | INFERRED | line 256 |
| 41 | R041 | ANALYST | block 2 | [13:29] | INFERRED | line 257 |
| 42 | R042 | MANAGEMENT | block 2 | [13:40] | INFERRED | line 262 |
| 43 | R043 | ANALYST | block 2 | [13:44] | INFERRED | line 264 |
| 44 | R044 | MANAGEMENT | block 2 | [13:46] | INFERRED | line 266 |
| 45 | R045 | ANALYST | block 2 | [13:54] | INFERRED | line 269 |
| 46 | R046 | MODERATOR | block 2 | [14:03] | INFERRED | line 276 |
| 47 | R047 | ANALYST | block 2 | [14:10] | INFERRED | line 279; moderator-named: fulltext L279-L284; opens: "Yeah."; INFERRED; Pratik Jain |
| 48 | R048 | MANAGEMENT | block 2 | [14:30] | INFERRED | line 285 |
| 49 | R049 | ANALYST | block 3 | [15:06] | INFERRED | line 292 |
| 50 | R050 | MANAGEMENT | block 3 | [15:14] | INFERRED | line 293 |
| 51 | R051 | ANALYST | block 3 | [15:48] | INFERRED | line 299 |
| 52 | R052 | MANAGEMENT | block 3 | [16:12] | INFERRED | line 302 |
| 53 | R053 | ANALYST | block 3 | [16:52] | INFERRED | line 309 |
| 54 | R054 | MANAGEMENT | block 3 | [17:16] | INFERRED | line 313 |
| 55 | R055 | ANALYST | block 3 | [17:38] | INFERRED | line 317 |
| 56 | R056 | MANAGEMENT | block 3 | [17:46] | INFERRED | line 319 |
| 57 | R057 | ANALYST | block 3 | [17:55] | INFERRED | line 320 |
| 58 | R058 | MANAGEMENT | block 3 | [18:00] | INFERRED | line 321 |
| 59 | R059 | ANALYST | block 3 | [18:56] | INFERRED | line 332 |
| 60 | R060 | MODERATOR | block 3 | [19:02] | INFERRED | line 335 |
| 61 | R061 | ANALYST | block 3 | [19:11] | INFERRED | line 338; moderator-named: fulltext L338-L341; opens: "Thank you."; INFERRED; Vive Ganguly |
| 62 | R062 | MANAGEMENT | block 3 | [19:24] | INFERRED MIXED | line 342 |
| 63 | R063 | ANALYST | block 4 | [20:03] | INFERRED | line 353 |
| 64 | R064 | MANAGEMENT | block 4 | [20:13] | INFERRED | line 355 |
| 65 | R065 | ANALYST | block 4 | [20:36] | INFERRED | line 359 |
| 66 | R066 | MANAGEMENT | block 4 | [20:52] | INFERRED | line 361 |
| 67 | R067 | ANALYST | block 4 | [21:03] | INFERRED | line 363 |
| 68 | R068 | MANAGEMENT | block 4 | [21:13] | INFERRED | line 364 |
| 69 | R069 | MODERATOR | block 4 | [21:15] | INFERRED | line 365 |
| 70 | R070 | ANALYST | block 4 | [21:25] | INFERRED | line 367; moderator-named: fulltext L367-L370; opens: "Good afternoon sir. Thank you so much for the"; INFERRED; Baala Subramanian |
| 71 | R071 | MANAGEMENT | block 4 | [21:47] | INFERRED MIXED | line 371 |
| 72 | R072 | ANALYST | block 4 | [22:24] | INFERRED | line 378 |
| 73 | R073 | MANAGEMENT | block 4 | [22:47] | INFERRED | line 382 |
| 74 | R074 | ANALYST | block 4 | [23:24] | INFERRED | line 389 |
| 75 | R075 | MANAGEMENT | block 4 | [23:42] | INFERRED | line 392 |
| 76 | R076 | ANALYST | block 4 | [24:18] | INFERRED | line 399 |
| 77 | R077 | MODERATOR | block 4 | [24:25] | INFERRED | line 400 |
| 78 | R078 | ANALYST | block 4 | [24:34] | INFERRED | line 401; moderator-named: fulltext L401-L403; opens: "Yeah, hi. Congratulations on a strong quarter."; INFERRED; Rahul Kumar |
| 79 | R079 | MANAGEMENT | block 4 | [24:54] | INFERRED | line 404 |
| 80 | R080 | ANALYST | block 5 | [25:31] | INFERRED | line 409 |
| 81 | R081 | MANAGEMENT | block 5 | [25:46] | INFERRED | line 412 |
| 82 | R082 | ANALYST | block 5 | [25:57] | INFERRED | line 414 |
| 83 | R083 | MANAGEMENT | block 5 | [26:31] | INFERRED | line 420 |
| 84 | R084 | ANALYST | block 5 | [27:11] | INFERRED | line 428 |
| 85 | R085 | MANAGEMENT | block 5 | [27:29] | INFERRED | line 431 |
| 86 | R086 | ANALYST | block 5 | [28:00] | INFERRED | line 435 |
| 87 | R087 | MANAGEMENT | block 5 | [28:12] | INFERRED | line 438 |
| 88 | R088 | ANALYST | block 5 | [28:31] | INFERRED | line 441 |
| 89 | R089 | MODERATOR | block 5 | [28:42] | INFERRED | line 450 |
| 90 | R090 | ANALYST | block 5 | [28:51] | INFERRED | line 451; moderator-named: fulltext L451-L454; opens: "Hi."; INFERRED; Kanant Ravedi |
| 91 | R091 | MANAGEMENT | block 5 | [29:05] | INFERRED | line 455 |
| 92 | R092 | ANALYST | block 5 | [29:13] | INFERRED | line 456 |
| 93 | R093 | MANAGEMENT | block 5 | [29:37] | INFERRED | line 460 |
| 94 | R094 | ANALYST | block 5 | [29:55] | INFERRED | line 462 |
| 95 | R095 | MANAGEMENT | block 6 | [30:02] | INFERRED | line 466 |
| 96 | R096 | ANALYST | block 6 | [30:50] | INFERRED | line 475 |
| 97 | R097 | MODERATOR | block 6 | [30:57] | INFERRED | line 477 |
| 98 | R098 | ANALYST | block 6 | [31:06] | INFERRED | line 479; moderator-named: fulltext L479-L479; opens: "Hello, am I audible?"; INFERRED; Saksham Tyagi |
| 99 | R099 | MODERATOR | block 6 | [31:09] | INFERRED | line 480 |
| 100 | R100 | ANALYST | block 6 | [31:11] | INFERRED | line 481 |
| 101 | R101 | MANAGEMENT | block 6 | [31:44] | INFERRED | line 489 |
| 102 | R102 | ANALYST | block 6 | [32:37] | INFERRED | line 504 |
| 103 | R103 | MANAGEMENT | block 6 | [33:11] | INFERRED | line 515 |
| 104 | R104 | ANALYST | block 6 | [33:33] | INFERRED | line 521 |
| 105 | R105 | MANAGEMENT | block 6 | [33:37] | INFERRED | line 523 |
| 106 | R106 | ANALYST | block 6 | [33:38] | INFERRED | line 524 |
| 107 | R107 | MODERATOR | block 6 | [33:46] | INFERRED | line 527 |
| 108 | R108 | ANALYST | block 6 | [33:58] | INFERRED | line 532; moderator-named: fulltext L532-L532; opens: "Yeah, am I audible?"; INFERRED; Abhijit Mathura |
| 109 | R109 | MODERATOR | block 6 | [34:00] | INFERRED | line 533 |
| 110 | R110 | ANALYST | block 6 | [34:03] | INFERRED | line 534 |
| 111 | R111 | MANAGEMENT | block 6 | [34:27] | INFERRED | line 541 |
| 112 | R112 | ANALYST | block 6 | [34:53] | INFERRED | line 549 |
| 113 | R113 | MANAGEMENT | block 6 | [34:55] | INFERRED | line 550 |
| 114 | R114 | ANALYST | block 7 | [36:00] | INFERRED | line 573 |
| 115 | R115 | MANAGEMENT | block 7 | [36:16] | INFERRED | line 579 |
| 116 | R116 | ANALYST | block 7 | [37:22] | INFERRED | line 603 |
| 117 | R117 | MODERATOR | block 7 | [37:26] | INFERRED | line 604 |
| 118 | R118 | ANALYST | block 7 | [37:47] | INFERRED | line 613; moderator-named: fulltext L613-L644; opens: "Good afternoon, sir."; INFERRED; Rabindranath Nayak |
| 119 | R119 | MANAGEMENT | block 7 | [39:00] | INFERRED | line 645 |
| 120 | R120 | ANALYST | block 8 | [40:38] | INFERRED MIXED | line 678 |
| 121 | R121 | MANAGEMENT | block 8 | [41:00] | INFERRED | line 681 |
| 122 | R122 | ANALYST | block 8 | [41:02] | INFERRED | line 682 |
| 123 | R123 | MANAGEMENT | block 8 | [41:07] | INFERRED MIXED | line 683 |
| 124 | R124 | ANALYST | block 8 | [41:12] | INFERRED | line 684 |
| 125 | R125 | MANAGEMENT | block 8 | [41:19] | INFERRED | line 685 |
| 126 | R126 | ANALYST | block 8 | [41:29] | INFERRED | line 687 |
| 127 | R127 | MODERATOR | block 8 | [41:34] | INFERRED | line 688 |
| 128 | R128 | ANALYST | block 8 | [41:44] | INFERRED | line 689; moderator-named: fulltext L689-L690; opens: "Hello. Thank you for giving me the opportunity. My"; INFERRED; Lavya Baldota |
| 129 | R129 | MANAGEMENT | block 8 | [42:00] | INFERRED | line 691 |
| 130 | R130 | ANALYST | block 8 | [42:17] | INFERRED | line 694 |
| 131 | R131 | MANAGEMENT | block 8 | [42:25] | INFERRED MIXED | line 695 |
| 132 | R132 | MODERATOR | block 8 | [42:44] | INFERRED | line 698 |
| 133 | R133 | ANALYST | block 8 | [42:55] | INFERRED | line 700; moderator-named: fulltext L700-L704; opens: "Hello, sir. Am I out of them? Yes. My"; INFERRED; Preneru Chatterjee |
| 134 | R134 | MANAGEMENT | block 8 | [43:38] | INFERRED | line 705 |
| 135 | R135 | ANALYST | block 8 | [43:48] | INFERRED | line 706 |
| 136 | R136 | MANAGEMENT | block 8 | [43:48] | INFERRED | line 706 |
| 137 | R137 | ANALYST | block 8 | [44:15] | INFERRED | line 712 |
| 138 | R138 | MANAGEMENT | block 8 | [44:28] | INFERRED MIXED | line 714 |
| 139 | R139 | ANALYST | block 9 | [45:30] | INFERRED | line 723 |
| 140 | R140 | MANAGEMENT | block 9 | [45:48] | INFERRED | line 725 |
| 141 | R141 | ANALYST | block 9 | [46:30] | INFERRED | line 729 |
| 142 | R142 | MANAGEMENT | block 9 | [46:46] | INFERRED | line 732 |
| 143 | R143 | ANALYST | block 9 | [46:52] | INFERRED | line 733 |
| 144 | R144 | MANAGEMENT | block 9 | [46:57] | INFERRED | line 734 |
| 145 | R145 | ANALYST | block 9 | [47:03] | INFERRED | line 735 |
| 146 | R146 | MANAGEMENT | block 9 | [47:10] | INFERRED | line 737 |
| 147 | R147 | ANALYST | block 9 | [47:18] | INFERRED | line 739 |
| 148 | R148 | MANAGEMENT | block 9 | [47:23] | INFERRED | line 740 |
| 149 | R149 | ANALYST | block 9 | [47:25] | INFERRED | line 741 |
| 150 | R150 | MANAGEMENT | block 9 | [47:34] | INFERRED | line 742 |
| 151 | R151 | ANALYST | block 9 | [48:11] | INFERRED | line 749 |
| 152 | R152 | MANAGEMENT | block 9 | [48:26] | INFERRED | line 751 |
| 153 | R153 | ANALYST | block 9 | [49:15] | INFERRED | line 758 |
| 154 | R154 | MODERATOR | block 9 | [49:19] | INFERRED | line 759 |
| 155 | R155 | MODERATOR | block 9 | [49:22] | INFERRED | line 761 |
| 156 | R156 | MANAGEMENT | block 9 | [49:31] | INFERRED | line 762 |
| 157 | R157 | MODERATOR | block 10 | [50:00] | INFERRED | line 767 |
| 158 | R158 | UNATTRIBUTED | block 10 | [50:30] | INFERRED | line 769 |

Turn totals: UNATTRIBUTED 1, ANALYST 76, MANAGEMENT 64, MODERATOR 17, total 158. Q&A share: the whole recording is Q&A (no prepared remarks present).

## 3. QUESTIONS
| q# | ROW_ID | analyst (firm NOT FOUND) | turn# | block | A2 flags | note |
|---|---|---|---|---|---|---|
| 1 | R159 | unnamed (before first moderator line) | 1 | block 0 | INFERRED | line 34 |
| 2 | R160 | unnamed (before first moderator line) | 3 | block 0 | INFERRED | line 43 |
| 3 | R161 | unnamed (before first moderator line) | 5 | block 0 | INFERRED | line 53 |
| 4 | R162 | unnamed (before first moderator line) | 7 | block 0 | INFERRED | line 62 |
| 5 | R163 | fulltext L77-L96; opens: "Hi sir, good afternoon. Thank you."; INFERRED; Mohit Jain | 13 | block 0 | INFERRED | line 77 |
| 6 | R164 | fulltext L77-L96; opens: "Hi sir, good afternoon. Thank you."; INFERRED; Mohit Jain | 17 | block 1 | INFERRED | line 111 |
| 7 | R165 | fulltext L77-L96; opens: "Hi sir, good afternoon. Thank you."; INFERRED; Mohit Jain | 19 | block 1 | INFERRED | line 126 |
| 8 | R166 | fulltext L77-L96; opens: "Hi sir, good afternoon. Thank you."; INFERRED; Mohit Jain | 21 | block 1 | INFERRED | line 138 |
| 9 | R167 | fulltext L180-L185; opens: "Yeah, hi Akshay."; INFERRED; Mayank Chaturbe | 29 | block 1 | INFERRED | line 182 |
| 10 | R168 | fulltext L180-L185; opens: "Yeah, hi Akshay."; INFERRED; Mayank Chaturbe | 33 | block 2 | INFERRED | line 224 |
| 11 | R169 | fulltext L180-L185; opens: "Yeah, hi Akshay."; INFERRED; Mayank Chaturbe | 37 | block 2 | INFERRED | line 231 |
| 12 | R170 | fulltext L180-L185; opens: "Yeah, hi Akshay."; INFERRED; Mayank Chaturbe | 41 | block 2 | INFERRED | line 257 |
| 13 | R171 | fulltext L279-L284; opens: "Yeah."; INFERRED; Pratik Jain | 47 | block 2 | INFERRED | line 282 |
| 14 | R172 | fulltext L279-L284; opens: "Yeah."; INFERRED; Pratik Jain | 49 | block 3 | INFERRED | line 292 |
| 15 | R173 | fulltext L279-L284; opens: "Yeah."; INFERRED; Pratik Jain | 51 | block 3 | INFERRED | line 299 |
| 16 | R174 | fulltext L279-L284; opens: "Yeah."; INFERRED; Pratik Jain | 53 | block 3 | INFERRED | line 309 |
| 17 | R175 | fulltext L279-L284; opens: "Yeah."; INFERRED; Pratik Jain | 55 | block 3 | INFERRED | line 317 |
| 18 | R176 | fulltext L338-L341; opens: "Thank you."; INFERRED; Vive Ganguly | 61 | block 3 | INFERRED | line 338 |
| 19 | R177 | fulltext L338-L341; opens: "Thank you."; INFERRED; Vive Ganguly | 63 | block 4 | INFERRED | line 353 |
| 20 | R178 | fulltext L338-L341; opens: "Thank you."; INFERRED; Vive Ganguly | 65 | block 4 | INFERRED | line 359 |
| 21 | R179 | fulltext L367-L370; opens: "Good afternoon sir. Thank you so much for the"; INFERRED; Baala Subramanian | 70 | block 4 | INFERRED | line 368 |
| 22 | R180 | fulltext L367-L370; opens: "Good afternoon sir. Thank you so much for the"; INFERRED; Baala Subramanian | 72 | block 4 | INFERRED | line 378 |
| 23 | R181 | fulltext L367-L370; opens: "Good afternoon sir. Thank you so much for the"; INFERRED; Baala Subramanian | 74 | block 4 | INFERRED | line 389 |
| 24 | R182 | fulltext L401-L403; opens: "Yeah, hi. Congratulations on a strong quarter."; INFERRED; Rahul Kumar | 78 | block 4 | INFERRED | line 401 |
| 25 | R183 | fulltext L401-L403; opens: "Yeah, hi. Congratulations on a strong quarter."; INFERRED; Rahul Kumar | 80 | block 5 | INFERRED | line 409 |
| 26 | R184 | fulltext L401-L403; opens: "Yeah, hi. Congratulations on a strong quarter."; INFERRED; Rahul Kumar | 82 | block 5 | INFERRED | line 414 |
| 27 | R185 | fulltext L401-L403; opens: "Yeah, hi. Congratulations on a strong quarter."; INFERRED; Rahul Kumar | 86 | block 5 | INFERRED | line 435 |
| 28 | R186 | fulltext L451-L454; opens: "Hi."; INFERRED; Kanant Ravedi | 90 | block 5 | INFERRED | line 451 |
| 29 | R187 | fulltext L451-L454; opens: "Hi."; INFERRED; Kanant Ravedi | 92 | block 5 | INFERRED | line 456 |
| 30 | R188 | fulltext L451-L454; opens: "Hi."; INFERRED; Kanant Ravedi | 94 | block 5 | INFERRED | line 462 |
| 31 | R189 | fulltext L479-L479; opens: "Hello, am I audible?"; INFERRED; Saksham Tyagi | 100 | block 6 | INFERRED | line 481 |
| 32 | R190 | fulltext L479-L479; opens: "Hello, am I audible?"; INFERRED; Saksham Tyagi | 102 | block 6 | INFERRED | line 504 |
| 33 | R191 | fulltext L532-L532; opens: "Yeah, am I audible?"; INFERRED; Abhijit Mathura | 110 | block 6 | INFERRED | line 534 |
| 34 | R192 | fulltext L532-L532; opens: "Yeah, am I audible?"; INFERRED; Abhijit Mathura | 114 | block 7 | INFERRED | line 573 |
| 35 | R193 | fulltext L613-L644; opens: "Good afternoon, sir."; INFERRED; Rabindranath Nayak | 118 | block 7 | INFERRED | line 613 |
| 36 | R194 | fulltext L613-L644; opens: "Good afternoon, sir."; INFERRED; Rabindranath Nayak | 118 | block 7 | INFERRED | line 623 |
| 37 | R195 | fulltext L613-L644; opens: "Good afternoon, sir."; INFERRED; Rabindranath Nayak | 118 | block 7 | INFERRED | line 634 |
| 38 | R196 | fulltext L613-L644; opens: "Good afternoon, sir."; INFERRED; Rabindranath Nayak | 120 | block 8 | INFERRED | line 678 |
| 39 | R197 | fulltext L613-L644; opens: "Good afternoon, sir."; INFERRED; Rabindranath Nayak | 124 | block 8 | INFERRED | line 684 |
| 40 | R198 | fulltext L689-L690; opens: "Hello. Thank you for giving me the opportunity. My"; INFERRED; Lavya Baldota | 128 | block 8 | INFERRED | line 689 |
| 41 | R199 | fulltext L689-L690; opens: "Hello. Thank you for giving me the opportunity. My"; INFERRED; Lavya Baldota | 130 | block 8 | INFERRED | line 694 |
| 42 | R200 | fulltext L700-L704; opens: "Hello, sir. Am I out of them? Yes. My"; INFERRED; Preneru Chatterjee | 133 | block 8 | INFERRED | line 700 |
| 43 | R201 | fulltext L700-L704; opens: "Hello, sir. Am I out of them? Yes. My"; INFERRED; Preneru Chatterjee | 137 | block 8 | INFERRED | line 712 |
| 44 | R202 | fulltext L700-L704; opens: "Hello, sir. Am I out of them? Yes. My"; INFERRED; Preneru Chatterjee | 139 | block 9 | INFERRED | line 723 |
| 45 | R203 | fulltext L700-L704; opens: "Hello, sir. Am I out of them? Yes. My"; INFERRED; Preneru Chatterjee | 141 | block 9 | INFERRED | line 729 |
| 46 | R204 | fulltext L700-L704; opens: "Hello, sir. Am I out of them? Yes. My"; INFERRED; Preneru Chatterjee | 149 | block 9 | INFERRED | line 741 |
| 47 | R205 | fulltext L700-L704; opens: "Hello, sir. Am I out of them? Yes. My"; INFERRED; Preneru Chatterjee | 151 | block 9 | INFERRED | line 749 |

REPEAT_QUESTION: topic overlap on margin/inflation recovery (R159, R160, R163, R164) and on capex funding; listed as overlap for A3 judgment, not asserted identical. No A1 row carries REPEAT.

## 4. NUMBERS (speaker from enclosing turn)
| ROW_ID | speaker of enclosing turn | turn# | block | A2 flags | note |
|---|---|---|---|---|---|
| R206 | ANALYST | 1 | block 0 |  | line 34 |
| R207 | MANAGEMENT | 2 | block 0 | ASR_UNCERTAIN MIXED_TURN | line 39 |
| R208 | ANALYST | 3 | block 0 | MIXED_TURN | line 46 |
| R209 | ANALYST | 3 | block 0 | MIXED_TURN | line 46 |
| R210 | ANALYST | 5 | block 0 | ASR_UNCERTAIN MIXED_TURN | line 54 |
| R211 | ANALYST | 5 | block 0 | MIXED_TURN | line 55 |
| R212 | MANAGEMENT | 6 | block 0 |  | line 57 |
| R213 | MANAGEMENT | 6 | block 0 | ASR_UNCERTAIN | line 60 |
| R214 | ANALYST | 7 | block 0 | ASR_UNCERTAIN MIXED_TURN | line 61 |
| R215 | ANALYST | 7 | block 0 | MIXED_TURN | line 62 |
| R216 | ANALYST | 7 | block 0 | MIXED_TURN | line 63 |
| R217 | ANALYST | 7 | block 0 | MIXED_TURN | line 63 |
| R218 | MANAGEMENT | 8 | block 0 |  | line 66 |
| R219 | MANAGEMENT | 8 | block 0 |  | line 66 |
| R220 | MANAGEMENT | 8 | block 0 |  | line 66 |
| R221 | MANAGEMENT | 8 | block 0 |  | line 67 |
| R222 | MANAGEMENT | 8 | block 0 |  | line 67 |
| R223 | MANAGEMENT | 8 | block 0 |  | line 68 |
| R224 | MANAGEMENT | 10 | block 0 | MIXED_TURN | line 73 |
| R225 | ANALYST | 13 | block 1 |  | line 83 |
| R226 | ANALYST | 13 | block 1 |  | line 85 |
| R227 | ANALYST | 13 | block 1 |  | line 86 |
| R228 | ANALYST | 13 | block 1 |  | line 87 |
| R229 | ANALYST | 13 | block 1 |  | line 92 |
| R230 | ANALYST | 13 | block 1 |  | line 94 |
| R231 | MANAGEMENT | 16 | block 1 |  | line 105 |
| R232 | MANAGEMENT | 16 | block 1 |  | line 106 |
| R233 | ANALYST | 17 | block 1 |  | line 112 |
| R234 | ANALYST | 17 | block 1 |  | line 114 |
| R235 | MANAGEMENT | 18 | block 1 |  | line 117 |
| R236 | ANALYST | 19 | block 1 | ASR_UNCERTAIN | line 127 |
| R237 | ANALYST | 19 | block 1 | ASR_UNCERTAIN | line 127 |
| R238 | MANAGEMENT | 20 | block 1 |  | line 136 |
| R239 | ANALYST | 21 | block 1 | ASR_UNCERTAIN | line 139 |
| R240 | ANALYST | 21 | block 1 | ASR_UNCERTAIN | line 140 |
| R241 | ANALYST | 21 | block 1 | ASR_UNCERTAIN | line 141 |
| R242 | MANAGEMENT | 22 | block 1 |  | line 148 |
| R243 | MANAGEMENT | 22 | block 1 |  | line 153 |
| R244 | MANAGEMENT | 22 | block 1 |  | line 154 |
| R245 | MANAGEMENT | 30 | block 1 | MIXED_TURN | line 193 |
| R246 | MANAGEMENT | 30 | block 1 | MIXED_TURN | line 195 |
| R247 | MANAGEMENT | 30 | block 2 | MIXED_TURN | line 198 |
| R248 | MANAGEMENT | 30 | block 2 | MIXED_TURN | line 206 |
| R249 | MANAGEMENT | 30 | block 2 | MIXED_TURN | line 208 |
| R250 | MANAGEMENT | 32 | block 2 | ASR_UNCERTAIN MIXED_TURN | line 215 |
| R251 | MANAGEMENT | 32 | block 2 | ASR_UNCERTAIN MIXED_TURN | line 215 |
| R252 | MANAGEMENT | 32 | block 2 | MIXED_TURN | line 216 |
| R253 | MANAGEMENT | 32 | block 2 | MIXED_TURN | line 219 |
| R254 | MANAGEMENT | 32 | block 2 | MIXED_TURN | line 219 |
| R255 | MANAGEMENT | 38 | block 2 |  | line 235 |
| R256 | MANAGEMENT | 38 | block 2 |  | line 236 |
| R257 | MANAGEMENT | 38 | block 2 |  | line 238 |
| R258 | MANAGEMENT | 38 | block 2 |  | line 239 |
| R259 | MANAGEMENT | 38 | block 2 |  | line 241 |
| R260 | MANAGEMENT | 38 | block 2 |  | line 244 |
| R261 | MANAGEMENT | 38 | block 2 |  | line 245 |
| R262 | MANAGEMENT | 38 | block 2 |  | line 248 |
| R263 | ANALYST | 39 | block 2 |  | line 254 |
| R264 | ANALYST | 39 | block 2 |  | line 255 |
| R265 | ANALYST | 47 | block 2 |  | line 282 |
| R266 | MANAGEMENT | 48 | block 2 | ASR_UNCERTAIN | line 285 |
| R267 | MANAGEMENT | 48 | block 2 |  | line 287 |
| R268 | MANAGEMENT | 48 | block 2 | ASR_UNCERTAIN | line 288 |
| R269 | MANAGEMENT | 50 | block 3 | ASR_UNCERTAIN | line 293 |
| R270 | MANAGEMENT | 50 | block 3 |  | line 297 |
| R271 | ANALYST | 51 | block 3 |  | line 300 |
| R272 | MANAGEMENT | 52 | block 3 |  | line 307 |
| R273 | MANAGEMENT | 52 | block 3 |  | line 307 |
| R274 | ANALYST | 53 | block 3 | ASR_UNCERTAIN | line 311 |
| R275 | MANAGEMENT | 54 | block 3 |  | line 315 |
| R276 | ANALYST | 55 | block 3 |  | line 317 |
| R277 | ANALYST | 55 | block 3 |  | line 318 |
| R278 | ANALYST | 57 | block 3 |  | line 320 |
| R279 | MANAGEMENT | 58 | block 3 |  | line 323 |
| R280 | MANAGEMENT | 58 | block 3 | ASR_UNCERTAIN | line 326 |
| R281 | MANAGEMENT | 58 | block 3 |  | line 330 |
| R282 | MANAGEMENT | 58 | block 3 |  | line 331 |
| R283 | MANAGEMENT | 62 | block 3 | MIXED_TURN | line 343 |
| R284 | MANAGEMENT | 62 | block 3 | ASR_UNCERTAIN MIXED_TURN | line 344 |
| R285 | MANAGEMENT | 62 | block 3 | MIXED_TURN | line 345 |
| R286 | MANAGEMENT | 62 | block 3 | ASR_UNCERTAIN MIXED_TURN | line 347 |
| R287 | MANAGEMENT | 62 | block 3 | MIXED_TURN | line 348 |
| R288 | MANAGEMENT | 62 | block 3 | MIXED_TURN | line 348 |
| R289 | ANALYST | 63 | block 4 |  | line 354 |
| R290 | MANAGEMENT | 64 | block 4 |  | line 355 |
| R291 | MANAGEMENT | 64 | block 4 |  | line 356 |
| R292 | MANAGEMENT | 64 | block 4 |  | line 357 |
| R293 | MANAGEMENT | 64 | block 4 |  | line 357 |
| R294 | MANAGEMENT | 64 | block 4 |  | line 357 |
| R295 | ANALYST | 65 | block 4 |  | line 359 |
| R296 | MANAGEMENT | 66 | block 4 |  | line 362 |
| R297 | MANAGEMENT | 66 | block 4 |  | line 362 |
| R298 | ANALYST | 70 | block 4 |  | line 368 |
| R299 | ANALYST | 72 | block 4 |  | line 380 |
| R300 | ANALYST | 72 | block 4 |  | line 380 |
| R301 | MANAGEMENT | 73 | block 4 |  | line 382 |
| R302 | ANALYST | 74 | block 4 |  | line 391 |
| R303 | ANALYST | 74 | block 4 |  | line 389 |
| R304 | MANAGEMENT | 75 | block 4 | ASR_UNCERTAIN | line 396 |
| R305 | ANALYST | 78 | block 4 |  | line 403 |
| R306 | MANAGEMENT | 81 | block 5 | ASR_UNCERTAIN | line 413 |
| R307 | MANAGEMENT | 81 | block 5 | ASR_UNCERTAIN | line 413 |
| R308 | ANALYST | 82 | block 5 | ASR_UNCERTAIN | line 416 |
| R309 | MANAGEMENT | 83 | block 5 |  | line 423 |
| R310 | ANALYST | 90 | block 5 |  | line 454 |
| R311 | ANALYST | 92 | block 5 |  | line 456 |
| R312 | ANALYST | 92 | block 5 |  | line 459 |
| R313 | ANALYST | 100 | block 6 | ASR_UNCERTAIN | line 482 |
| R314 | ANALYST | 100 | block 6 |  | line 483 |
| R315 | ANALYST | 100 | block 6 |  | line 485 |
| R316 | ANALYST | 100 | block 6 |  | line 486 |
| R317 | ANALYST | 100 | block 6 |  | line 488 |
| R318 | MANAGEMENT | 101 | block 6 |  | line 490 |
| R319 | MANAGEMENT | 101 | block 6 |  | line 490 |
| R320 | MANAGEMENT | 101 | block 6 |  | line 495 |
| R321 | MANAGEMENT | 101 | block 6 |  | line 495 |
| R322 | MANAGEMENT | 101 | block 6 |  | line 495 |
| R323 | MANAGEMENT | 101 | block 6 |  | line 496 |
| R324 | ANALYST | 102 | block 6 |  | line 505 |
| R325 | ANALYST | 102 | block 6 |  | line 505 |
| R326 | ANALYST | 102 | block 6 |  | line 507 |
| R327 | ANALYST | 102 | block 6 |  | line 509 |
| R328 | MANAGEMENT | 103 | block 6 |  | line 515 |
| R329 | MANAGEMENT | 103 | block 6 |  | line 516 |
| R330 | ANALYST | 110 | block 6 |  | line 536 |
| R331 | ANALYST | 110 | block 6 |  | line 539 |
| R332 | ANALYST | 110 | block 6 |  | line 540 |
| R333 | MANAGEMENT | 111 | block 6 | ASR_UNCERTAIN | line 543 |
| R334 | MANAGEMENT | 111 | block 6 |  | line 543 |
| R335 | MANAGEMENT | 113 | block 7 |  | line 553 |
| R336 | MANAGEMENT | 113 | block 7 | ASR_UNCERTAIN | line 555 |
| R337 | MANAGEMENT | 113 | block 7 |  | line 566 |
| R338 | MANAGEMENT | 113 | block 7 |  | line 569 |
| R339 | MANAGEMENT | 115 | block 7 |  | line 580 |
| R340 | MANAGEMENT | 115 | block 7 | ASR_UNCERTAIN | line 591 |
| R341 | MANAGEMENT | 115 | block 7 |  | line 592 |
| R342 | MANAGEMENT | 115 | block 7 |  | line 594 |
| R343 | MANAGEMENT | 115 | block 7 |  | line 594 |
| R344 | MANAGEMENT | 115 | block 7 |  | line 596 |
| R345 | MANAGEMENT | 115 | block 7 | ASR_UNCERTAIN | line 601 |
| R346 | MODERATOR | 117 | block 7 |  | line 609 |
| R347 | ANALYST | 118 | block 7 |  | line 626 |
| R348 | ANALYST | 118 | block 7 |  | line 630 |
| R349 | MANAGEMENT | 119 | block 7 |  | line 655 |
| R350 | MANAGEMENT | 119 | block 7 |  | line 656 |
| R351 | MANAGEMENT | 119 | block 7 |  | line 657 |
| R352 | MANAGEMENT | 119 | block 7 |  | line 659 |
| R353 | ANALYST | 120 | block 8 | MIXED_TURN | line 679 |
| R354 | MANAGEMENT | 129 | block 8 |  | line 692 |
| R355 | ANALYST | 128 | block 8 |  | line 690 |
| R356 | ANALYST | 133 | block 8 |  | line 701 |
| R357 | ANALYST | 133 | block 8 |  | line 701 |
| R358 | ANALYST | 133 | block 8 |  | line 703 |
| R359 | ANALYST | 133 | block 8 |  | line 703 |
| R360 | ANALYST | 133 | block 8 |  | line 703 |
| R361 | ANALYST | 133 | block 8 | ASR_UNCERTAIN | line 704 |
| R362 | MANAGEMENT | 134 | block 8 |  | line 705 |
| R363 | ANALYST | 137 | block 8 | ASR_UNCERTAIN | line 712 |
| R364 | MANAGEMENT | 138 | block 8 | MIXED_TURN | line 714 |
| R365 | MANAGEMENT | 138 | block 8 | MIXED_TURN | line 715 |
| R366 | MANAGEMENT | 138 | block 9 | MIXED_TURN | line 720 |
| R367 | MANAGEMENT | 138 | block 9 | MIXED_TURN | line 721 |
| R368 | MANAGEMENT | 140 | block 9 |  | line 727 |
| R369 | MANAGEMENT | 140 | block 9 |  | line 727 |
| R370 | MANAGEMENT | 140 | block 9 |  | line 727 |
| R371 | MANAGEMENT | 140 | block 9 |  | line 727 |
| R372 | ANALYST | 143 | block 9 |  | line 733 |
| R373 | MANAGEMENT | 144 | block 9 |  | line 734 |
| R374 | MANAGEMENT | 146 | block 9 | ASR_UNCERTAIN | line 738 |
| R375 | MANAGEMENT | 146 | block 9 |  | line 738 |
| R376 | ANALYST | 149 | block 9 | ASR_UNCERTAIN | line 741 |
| R377 | MANAGEMENT | 150 | block 9 | ASR_UNCERTAIN | line 742 |
| R378 | MANAGEMENT | 150 | block 9 |  | line 744 |
| R379 | MANAGEMENT | 150 | block 9 |  | line 746 |
| R380 | MANAGEMENT | 150 | block 9 |  | line 748 |
| R381 | ANALYST | 151 | block 9 |  | line 750 |

Number totals: management-turn 107, analyst-cited 68, other 1, total 176. Analyst-cited numbers are not management disclosures; MIXED turns may misattribute.

## 5. FORWARD STATEMENTS
| ROW_ID | turn# | block | A2 flags | note |
|---|---|---|---|---|
| R432 | 4 | block 0 |  | line 47 |
| R433 | 4 | block 0 |  | line 50 |
| R434 | 5 | block 0 |  | line 53 |
| R435 | 7 | block 0 |  | line 62 |
| R436 | 8 | block 0 |  | line 68 |
| R437 | 10 | block 0 |  | line 72 |
| R438 | 10 | block 0 |  | line 73 |
| R439 | 18 | block 1 |  | line 123 |
| R440 | 20 | block 1 |  | line 132 |
| R441 | 20 | block 1 |  | line 136 |
| R442 | 22 | block 1 |  | line 147 |
| R443 | 22 | block 1 |  | line 154 |
| R444 | 22 | block 1 |  | line 159 |
| R445 | 22 | block 1 |  | line 162 |
| R446 | 24 | block 1 |  | line 167 |
| R447 | 30 | block 1 |  | line 189 |
| R448 | 30 | block 2 |  | line 200 |
| R449 | 30 | block 2 |  | line 205 |
| R450 | 34 | block 2 |  | line 225 |
| R451 | 36 | block 2 |  | line 229 |
| R452 | 38 | block 2 |  | line 248 |
| R453 | 38 | block 2 |  | line 235 |
| R454 | 42 | block 2 |  | line 263 |
| R455 | 48 | block 2 |  | line 285 |
| R456 | 48 | block 2 |  | line 287 |
| R457 | 50 | block 3 |  | line 293 |
| R458 | 50 | block 3 |  | line 297 |
| R459 | 52 | block 3 |  | line 302 |
| R460 | 52 | block 3 |  | line 307 |
| R461 | 54 | block 3 |  | line 313 |
| R462 | 58 | block 3 |  | line 323 |
| R463 | 58 | block 3 |  | line 330 |
| R464 | 62 | block 3 |  | line 348 |
| R465 | 64 | block 4 |  | line 355 |
| R466 | 66 | block 4 |  | line 361 |
| R467 | 71 | block 4 |  | line 371 |
| R468 | 73 | block 4 |  | line 382 |
| R469 | 75 | block 4 | ASR_UNCERTAIN | line 392 |
| R470 | 75 | block 4 |  | line 397 |
| R471 | 79 | block 4 |  | line 404 |
| R472 | 79 | block 5 |  | line 406 |
| R473 | 79 | block 5 |  | line 407 |
| R474 | 79 | block 5 |  | line 408 |
| R475 | 87 | block 5 |  | line 440 |
| R476 | 91 | block 5 |  | line 455 |
| R477 | 93 | block 5 |  | line 460 |
| R478 | 101 | block 6 |  | line 498 |
| R479 | 101 | block 6 |  | line 499 |
| R480 | 103 | block 6 |  | line 515 |
| R481 | 103 | block 6 |  | line 517 |
| R482 | 119 | block 7 |  | line 662 |
| R483 | 119 | block 8 |  | line 677 |
| R484 | 123 | block 8 |  | line 683 |
| R485 | 125 | block 8 |  | line 685 |
| R486 | 129 | block 8 |  | line 692 |
| R487 | 131 | block 8 |  | line 696 |
| R488 | 144 | block 9 |  | line 734 |
| R489 | 152 | block 9 |  | line 752 |
| R490 | 152 | block 9 |  | line 755 |
| R491 | 156 | block 9 |  | line 763 |

## 6. ENTITIES
| ROW_ID | block | A2 flags | note |
|---|---|---|---|
| R382 | block H | | line 26 |
| R383 | block H | | line 28 |
| R384 | block H | | line 28 |
| R385 | block H | | line 29 |
| R386 | block H | | line 26 |
| R387 | block H | | line 26 |
| R388 | block 0 | | line 42 |
| R389 | block 0 | | line 50 |
| R390 | block 0 | | line 76 |
| R391 | block 1 | | line 158 |
| R392 | block 1 | | line 171 |
| R393 | block 1 | | line 177 |
| R394 | block 1 | | line 184 |
| R395 | block 1 | | line 193 |
| R396 | block 2 | | line 217 |
| R397 | block 2 | | line 202 |
| R398 | block 3 | | line 349 |
| R399 | block 0 | | line 64 |
| R400 | block 2 | | line 276 |
| R401 | block 3 | | line 336 |
| R402 | block 4 | | line 365 |
| R403 | block 4 | | line 379 |
| R404 | block 4 | | line 379 |
| R405 | block 4 | | line 384 |
| R406 | block 4 | | line 387 |
| R407 | block 4 | | line 388 |
| R408 | block 4 | | line 400 |
| R409 | block 5 | | line 450 |
| R410 | block 6 | | line 477 |
| R411 | block 6 | | line 528 |
| R412 | block 7 | | line 610 |
| R413 | block 8 | | line 688 |
| R414 | block 8 | | line 698 |
| R415 | block 3 | | line 333 |
| R416 | block 4 | | line 375 |
| R417 | block 7 | | line 650 |
| R418 | block 7 | | line 651 |
| R419 | block 7 | | line 651 |
| R420 | block 7 | | line 652 |
| R421 | block 7 | | line 657 |
| R422 | block 8 | | line 693 |
| R423 | block 2 | | line 248 |
| R424 | block 9 | | line 756 |
| R425 | block 1 | | line 165 |
| R426 | block 9 | | line 762 |
| R427 | block 9 | | line 765 |
| R428 | block 5 | | line 416 |
| R429 | block 5 | | line 416 |
| R430 | block 2 | | line 224 |
| R431 | block 6 | | line 486 |

No prior-quarter list supplied; ENTITY_CHANGE not testable.

## 7. DATES
| ROW_ID | block | A2 flags | note |
|---|---|---|---|
| R492 | block H | | line 27 |
| R493 | block H | | line 27 |
| R494 | block H | | line 27 |
| R495 | block H | | line 29 |
| R496 | block H | | line 28 |
| R497 | block H | | line 28 |
| R498 | block H | | line 27 |
| R499 | block 0 | | line 40 |
| R500 | block 0 | | line 47 |
| R501 | block 0 | | line 51 |
| R502 | block 0 | | line 68 |
| R503 | block 1 | | line 154 |
| R504 | block 1 | | line 155 |
| R505 | block 1 | | line 169 |
| R506 | block 2 | | line 248 |
| R507 | block 2 | | line 254 |
| R508 | block 2 | | line 255 |
| R509 | block 2 | | line 285 |
| R510 | block 3 | | line 300 |
| R511 | block 4 | | line 361 |
| R512 | block 4 | | line 361 |
| R513 | block 4 | | line 375 |
| R514 | block 4 | | line 403 |
| R515 | block 5 | | line 406 |
| R516 | block 5 | | line 406 |
| R517 | block 5 | | line 456 |
| R518 | block 6 | | line 483 |
| R519 | block 6 | | line 486 |
| R520 | block 6 | | line 490 |
| R521 | block 6 | | line 505 |
| R522 | block 6 | | line 509 |
| R523 | block 6 | | line 517 |
| R524 | block 6 | | line 518 |
| R525 | block 9 | | line 738 |
| R526 | block 9 | | line 734 |
| R527 | block 9 | | line 763 |
| R528 | block 10 | | line 768 |

## 8. QUALIFIERS / HEDGES
| ROW_ID | turn# | block | A2 flags | note |
|---|---|---|---|---|
| R529 | - | block H | MACHINE-TRANSCRIBED  | line 25 |
| R530 | - | block H |  | line 28 |
| R531 | - | block H | ASR: faster-whisper model 'small', int8, CPU, language en, beam 1, 5-minute chunks | line 29 |
| R532 | - | block H |  | line 29 |
| R533 | - | block H |  | line 30 |
| R534 | - | block H |  | line 30 |
| R535 | 2 | block 0 |  | line 37 |
| R536 | 2 | block 0 | ASR term ASR_UNCERTAIN | line 39 |
| R537 | 3 | block 0 |  | line 42 |
| R538 | 3 | block 0 |  | line 42 |
| R539 | 4 | block 0 |  | line 48 |
| R540 | 4 | block 0 |  | line 50 |
| R541 | 4 | block 0 |  | line 51 |
| R542 | 5 | block 0 |  | line 53 |
| R543 | 6 | block 0 |  | line 57 |
| R544 | 8 | block 0 |  | line 68 |
| R545 | 14 | block 1 |  | line 99 |
| R546 | 15 | block 1 |  | line 101 |
| R547 | 16 | block 1 |  | line 105 |
| R548 | 18 | block 1 |  | line 117 |
| R549 | 19 | block 1 | ASR term ASR_UNCERTAIN | line 127 |
| R550 | 19 | block 1 |  | line 127 |
| R551 | 21 | block 1 | ASR term ASR_UNCERTAIN | line 139 |
| R552 | 22 | block 1 |  | line 147 |
| R553 | 22 | block 1 |  | line 162 |
| R554 | 32 | block 2 |  | line 215 |
| R555 | 42 | block 2 |  | line 263 |
| R556 | 48 | block 2 |  | line 286 |
| R557 | 48 | block 2 |  | line 287 |
| R558 | 50 | block 3 |  | line 294 |
| R559 | 54 | block 3 |  | line 313 |
| R560 | 56 | block 3 |  | line 319 |
| R561 | 58 | block 3 |  | line 321 |
| R562 | 58 | block 3 |  | line 326 |
| R563 | 62 | block 3 |  | line 348 |
| R564 | 64 | block 4 |  | line 357 |
| R565 | 73 | block 4 |  | line 384 |
| R566 | 75 | block 4 | ASR value ASR_UNCERTAIN | line 396 |
| R567 | 75 | block 4 |  | line 393 |
| R568 | 83 | block 5 |  | line 421 |
| R569 | 85 | block 5 |  | line 432 |
| R570 | 95 | block 6 |  | line 471 |
| R571 | 93 | block 5 |  | line 460 |
| R572 | 103 | block 6 |  | line 517 |
| R573 | 113 | block 7 |  | line 561 |
| R574 | 113 | block 7 |  | line 566 |
| R575 | 115 | block 7 | ASR_UNCERTAIN | line 601 |
| R576 | 111 | block 6 | ASR_UNCERTAIN | line 543 |
| R577 | 81 | block 5 | ASR_UNCERTAIN | line 413 |
| R578 | 6 | block 0 | ASR_UNCERTAIN | line 60 |
| R579 | 62 | block 3 | ASR_UNCERTAIN | line 344 |
| R580 | 119 | block 7 |  | line 655 |
| R581 | 119 | block 8 |  | line 675 |
| R582 | 119 | block 8 |  | line 677 |
| R583 | 123 | block 8 |  | line 683 |
| R584 | 125 | block 8 |  | line 685 |
| R585 | 136 | block 8 |  | line 706 |
| R586 | 140 | block 9 |  | line 725 |
| R587 | 144 | block 9 |  | line 734 |
| R588 | 150 | block 9 |  | line 742 |
| R589 | 152 | block 9 |  | line 751 |
