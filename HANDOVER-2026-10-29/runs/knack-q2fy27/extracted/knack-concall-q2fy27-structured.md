=== A1 STRUCTURED EXTRACTION: KNACK Q2 FY27 CONCALL ===
source: knack-concall-q2fy27-fulltext.md (input Knack_Q2FY27_Concall_Transcript_ASR.txt; ASR faster-whisper small.en; management tier; numbers unverified, may be misheard)
ID range: R001-R934  (total 934 rows)
anchors: 'line L' = FULLTEXT FILE line (input line S = file line 38+S); 'page n/a' (no pages); turn T## per header turn table (15 turns T01-T15, T00 preamble); ts = [hh:mm:ss] on that line
row format: R### | page | line L | TYPE | verbatim value | context | turn | ts | flags
flags: ASR_DOUBT(reason) = possible mishearing (odd magnitude, unit missing, homophone, garbled label); NOT corrected. ZERO_STANDING = zero/nil value.

SWEEP REGEX (applied per line to text after the timestamp; case-insensitive except months; each non-overlapping match = one row):
  (?P<dig>\S*\d\S*)|(?P<num>\b(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|lakhs?|crores?|million|billion|per cent|percent|basis points?|tonnes?|tons?|MT|kg|rupees?|double)\b)|(?P<mon>(?-i:\b(?:January|February|March|April|May|June|July|August|September|Sept|October|November|December)\b))|(?P<per>\b(?:quarters?|half|FY|H[12]|financial year)\b)|(?P<fwd>\b(?:next year|going forward|going to|will|would|expect(?:s|ed|ing|ation)?|target(?:s|ed|ing)?|guidance|plan(?:s|ned|ning)?|by|capex|commission(?:ing|ed)?|ahead)\b)
  classification: dig tokens starting Q#/H#/F*#/FY/20xx -> DATE else NUMBER; num words/units/rupees -> NUMBER; months, quarter(s), half, FY, H1/H2, financial year -> DATE; will/would/expect*/target*/guidance/plan*/by/capex/commission*/ahead/going to/next year/going forward -> FORWARD
  SWEEP HITS: 828  = NUMBER 472 + DATE 216 + FORWARD 140
  RECONCILIATION: sweep rows emitted = 828 (equals hits 828: yes); manual rows = ENTITY 49 + FORWARD-STATEMENT 32 + QUALIFIER 25 = 106; total 828+106 = 934 = 934
  ASR_DOUBT rows: 326; ZERO_STANDING rows: 0
counts per table: NUMBER 472 | ENTITY 49 | FORWARD 172 (sweep 140 + statement 32) | DATE 216 | QUALIFIER 25

## NUMBER (sweep): R001-R472 (472 rows)
R001 | page n/a | line 39 | NUMBER | Knack_Q2FY27_Concall.mp3 | TRANSCRIPT (ASR). Source audio: Knack_Q2FY27_Concall.mp3 (3434s). Tool: faster-whisper small.en, | T00 | - | -
R002 | page n/a | line 39 | NUMBER | 3434s | (ASR). Source audio: Knack_Q2FY27_Concall.mp3 (3434s). Tool: faster-whisper small.en, int8, | T00 | - | -
R003 | page n/a | line 39 | NUMBER | int8 | (3434s). Tool: faster-whisper small.en, int8, beam 2, 600-second chunks, | T00 | - | -
R004 | page n/a | line 39 | NUMBER | 2 | faster-whisper small.en, int8, beam 2, 600-second chunks, VAD on. | T00 | - | -
R005 | page n/a | line 39 | NUMBER | 600-second | small.en, int8, beam 2, 600-second chunks, VAD on. Produced | T00 | - | -
R006 | page n/a | line 39 | NUMBER | 11:13 | VAD on. Produced 2026-10-28 11:13 IST by Claude Code. | T00 | - | -
R007 | page n/a | line 53 | NUMBER | 27 | Financial Aid 27 earnings call. On the | T02 | 00:01:15 | ASR_DOUBT(garbled quarter/FY label, stray percentage)
R008 | page n/a | line 57 | NUMBER | 50% | colubrulins, 50% within few weeks throughout | T02 | 00:02:09 | ASR_DOUBT('50% within few weeks' context garbled)
R009 | page n/a | line 58 | NUMBER | 75 | as an exporter to 75 countries. This factor | T02 | 00:02:22 | -
R010 | page n/a | line 60 | NUMBER | three | pressure. However, with our three decades | T02 | 00:02:39 | -
R011 | page n/a | line 63 | NUMBER | 2 | was impacted in quarter 2, F527. | T02 | 00:02:58 | -
R012 | page n/a | line 64 | NUMBER | 45% | About 45% to 50% of our | T02 | 00:03:03 | -
R013 | page n/a | line 64 | NUMBER | 50% | About 45% to 50% of our customers are | T02 | 00:03:03 | -
R014 | page n/a | line 67 | NUMBER | 3 | quarter 3 FI27 onwards subject to | T02 | 00:03:25 | -
R015 | page n/a | line 69 | NUMBER | three | on three key pillars which are | T02 | 00:03:39 | -
R016 | page n/a | line 71 | NUMBER | 25 | and other 25 plus industries, and many | T02 | 00:03:54 | -
R017 | page n/a | line 72 | NUMBER | 1-2% | accounts for only about 1-2% of our customers and | T02 | 00:04:01 | -
R018 | page n/a | line 76 | NUMBER | 30 | As on September 30, 2026, we sought more | T02 | 00:04:27 | ASR_DOUBT(customers/SKUs magnitude: 2040, 3974 vs 2000, 13500; repeated '2040')
R019 | page n/a | line 76 | NUMBER | 2040 | we sought more than 2040, 2040 customers with 3974 | T02 | 00:04:27 | ASR_DOUBT(customers/SKUs magnitude: 2040, 3974 vs 2000, 13500; repeated '2040')
R020 | page n/a | line 76 | NUMBER | 2040 | sought more than 2040, 2040 customers with 3974 SKUs | T02 | 00:04:27 | ASR_DOUBT(customers/SKUs magnitude: 2040, 3974 vs 2000, 13500; repeated '2040')
R021 | page n/a | line 76 | NUMBER | 3974 | 2040, 2040 customers with 3974 SKUs | T02 | 00:04:27 | ASR_DOUBT(customers/SKUs magnitude: 2040, 3974 vs 2000, 13500; repeated '2040')
R022 | page n/a | line 77 | NUMBER | 2000 | up from 2000 customers and 13500 SKUs | T02 | 00:04:39 | ASR_DOUBT(2000 customers, 13500 SKUs vs 2040, 3974 magnitude)
R023 | page n/a | line 77 | NUMBER | 13500 | from 2000 customers and 13500 SKUs at the end | T02 | 00:04:39 | ASR_DOUBT(2000 customers, 13500 SKUs vs 2040, 3974 magnitude)
R024 | page n/a | line 77 | NUMBER | one | the end of quarter one financial year 27. | T02 | 00:04:39 | ASR_DOUBT(2000 customers, 13500 SKUs vs 2040, 3974 magnitude)
R025 | page n/a | line 77 | NUMBER | 27 | quarter one financial year 27. | T02 | 00:04:39 | ASR_DOUBT(2000 customers, 13500 SKUs vs 2040, 3974 magnitude)
R026 | page n/a | line 79 | NUMBER | 75 | and we sold to 75 countries across six continents | T02 | 00:04:55 | ASR_DOUBT(74 vs 75 countries)
R027 | page n/a | line 79 | NUMBER | six | to 75 countries across six continents up from 74 | T02 | 00:04:55 | ASR_DOUBT(74 vs 75 countries)
R028 | page n/a | line 79 | NUMBER | 74 | six continents up from 74 countries | T02 | 00:04:55 | ASR_DOUBT(74 vs 75 countries)
R029 | page n/a | line 80 | NUMBER | 1 | the end of quarter 1, FY27 and 71 countries | T02 | 00:05:02 | ASR_DOUBT(71 countries, unit/period)
R030 | page n/a | line 80 | NUMBER | 71 | quarter 1, FY27 and 71 countries in FY26. | T02 | 00:05:02 | ASR_DOUBT(71 countries, unit/period)
R031 | page n/a | line 88 | NUMBER | 2nd | a recent update on 2nd October 2026, we announced | T02 | 00:05:43 | -
R032 | page n/a | line 88 | NUMBER | 3-year | a new order and 3-year contract | T02 | 00:05:43 | -
R033 | page n/a | line 89 | NUMBER | 150 | renewal worth about 150 crore per year from | T02 | 00:05:51 | -
R034 | page n/a | line 89 | NUMBER | crore | renewal worth about 150 crore per year from an | T02 | 00:05:51 | -
R035 | page n/a | line 89 | NUMBER | one | from an international customer, one of the largest | T02 | 00:05:51 | -
R036 | page n/a | line 99 | NUMBER | 2 | financial highlights for quarter 2 and H1 F5-27. Thank | T03 | 00:06:47 | -
R037 | page n/a | line 100 | NUMBER | 2 | financial performance for quarter 2, financial | T03 | 00:06:56 | -
R038 | page n/a | line 101 | NUMBER | 27 | and H-1 Peninsula 27, Thomas 27, our consolidated | T03 | 00:07:04 | -
R039 | page n/a | line 101 | NUMBER | 27 | H-1 Peninsula 27, Thomas 27, our consolidated revenue from | T03 | 00:07:04 | -
R040 | page n/a | line 101 | NUMBER | 294 | revenue from operation was 294 crores shared | T03 | 00:07:04 | -
R041 | page n/a | line 101 | NUMBER | crores | from operation was 294 crores shared | T03 | 00:07:04 | -
R042 | page n/a | line 102 | NUMBER | 193.26 | with the 193.26 crores in quarter 2 | T03 | 00:07:19 | ASR_DOUBT(294 crores unit/decimals; growth % vs revenue pair)
R043 | page n/a | line 102 | NUMBER | crores | with the 193.26 crores in quarter 2 Peninsula | T03 | 00:07:19 | ASR_DOUBT(294 crores unit/decimals; growth % vs revenue pair)
R044 | page n/a | line 102 | NUMBER | 2 | 193.26 crores in quarter 2 Peninsula 26, a year-on-year | T03 | 00:07:19 | ASR_DOUBT(294 crores unit/decimals; growth % vs revenue pair)
R045 | page n/a | line 102 | NUMBER | 26 | in quarter 2 Peninsula 26, a year-on-year growth increase | T03 | 00:07:19 | ASR_DOUBT(294 crores unit/decimals; growth % vs revenue pair)
R046 | page n/a | line 102 | NUMBER | 52.5% | year-on-year growth increase of 52.5%. | T03 | 00:07:19 | ASR_DOUBT(294 crores unit/decimals; growth % vs revenue pair)
R047 | page n/a | line 106 | NUMBER | 27 | financial year 27 was 49.77 gross compared | T03 | 00:07:46 | ASR_DOUBT('gross' likely crores; 49.77 vs 38.30)
R048 | page n/a | line 106 | NUMBER | 49.77 | financial year 27 was 49.77 gross compared with 38.30 | T03 | 00:07:46 | ASR_DOUBT('gross' likely crores; 49.77 vs 38.30)
R049 | page n/a | line 106 | NUMBER | 38.30 | 49.77 gross compared with 38.30 gross in quarter to | T03 | 00:07:46 | ASR_DOUBT('gross' likely crores; 49.77 vs 38.30)
R050 | page n/a | line 107 | NUMBER | 26 | financial year 26 of 29.9 percent. The | T03 | 00:07:54 | ASR_DOUBT('29.9 percent' stray; margin pair)
R051 | page n/a | line 107 | NUMBER | 29.9 | financial year 26 of 29.9 percent. The Ibita margin | T03 | 00:07:54 | ASR_DOUBT('29.9 percent' stray; margin pair)
R052 | page n/a | line 107 | NUMBER | percent | year 26 of 29.9 percent. The Ibita margin was | T03 | 00:07:54 | ASR_DOUBT('29.9 percent' stray; margin pair)
R053 | page n/a | line 107 | NUMBER | 16.35 | The Ibita margin was 16.35 percent against | T03 | 00:07:54 | ASR_DOUBT('29.9 percent' stray; margin pair)
R054 | page n/a | line 107 | NUMBER | percent | Ibita margin was 16.35 percent against | T03 | 00:07:54 | ASR_DOUBT('29.9 percent' stray; margin pair)
R055 | page n/a | line 108 | NUMBER | 19.25% | 19.25% a year ago, a | T03 | 00:08:03 | ASR_DOUBT('$285 billion point' likely basis points)
R056 | page n/a | line 108 | NUMBER | $285 | a decline of the $285 billion point. This reflected | T03 | 00:08:03 | ASR_DOUBT('$285 billion point' likely basis points)
R057 | page n/a | line 108 | NUMBER | billion | decline of the $285 billion point. This reflected industry-wise | T03 | 00:08:03 | ASR_DOUBT('$285 billion point' likely basis points)
R058 | page n/a | line 110 | NUMBER | 1 | with a log of 1 or 2 water and | T03 | 00:08:19 | -
R059 | page n/a | line 110 | NUMBER | 2 | log of 1 or 2 water and we | T03 | 00:08:19 | -
R060 | page n/a | line 111 | NUMBER | 3 | recover is from quarter 3, financial year 27. About | T03 | 00:08:26 | -
R061 | page n/a | line 111 | NUMBER | 27 | quarter 3, financial year 27. About the pack profit | T03 | 00:08:26 | -
R062 | page n/a | line 112 | NUMBER | 2 | tax for quarter 2, financial year 27 was | T03 | 00:08:34 | ASR_DOUBT(25.02 vs 20.64 crores)
R063 | page n/a | line 112 | NUMBER | 27 | quarter 2, financial year 27 was 25.02 crores versus | T03 | 00:08:34 | ASR_DOUBT(25.02 vs 20.64 crores)
R064 | page n/a | line 112 | NUMBER | 25.02 | financial year 27 was 25.02 crores versus 20.64 crores | T03 | 00:08:34 | ASR_DOUBT(25.02 vs 20.64 crores)
R065 | page n/a | line 112 | NUMBER | crores | year 27 was 25.02 crores versus 20.64 crores in | T03 | 00:08:34 | ASR_DOUBT(25.02 vs 20.64 crores)
R066 | page n/a | line 112 | NUMBER | 20.64 | was 25.02 crores versus 20.64 crores in quarter 2, | T03 | 00:08:34 | ASR_DOUBT(25.02 vs 20.64 crores)
R067 | page n/a | line 112 | NUMBER | crores | 25.02 crores versus 20.64 crores in quarter 2, financial | T03 | 00:08:34 | ASR_DOUBT(25.02 vs 20.64 crores)
R068 | page n/a | line 112 | NUMBER | 2 | 20.64 crores in quarter 2, financial | T03 | 00:08:34 | ASR_DOUBT(25.02 vs 20.64 crores)
R069 | page n/a | line 113 | NUMBER | 26 | year 26. Up 21.2%, the pack | T03 | 00:08:43 | ASR_DOUBT(21.2%, 8.22%, 10.34%)
R070 | page n/a | line 113 | NUMBER | 21.2% | year 26. Up 21.2%, the pack margin for | T03 | 00:08:43 | ASR_DOUBT(21.2%, 8.22%, 10.34%)
R071 | page n/a | line 113 | NUMBER | 8.22% | margin for quarter was 8.22% compared with 10.34%, a | T03 | 00:08:43 | ASR_DOUBT(21.2%, 8.22%, 10.34%)
R072 | page n/a | line 113 | NUMBER | 10.34% | was 8.22% compared with 10.34%, a decline of | T03 | 00:08:43 | ASR_DOUBT(21.2%, 8.22%, 10.34%)
R073 | page n/a | line 114 | NUMBER | 212 | 212 basis points, a product | T03 | 00:08:54 | ASR_DOUBT(212 basis points; 2.62 crores)
R074 | page n/a | line 114 | NUMBER | basis points | 212 basis points, a product from | T03 | 00:08:54 | ASR_DOUBT(212 basis points; 2.62 crores)
R075 | page n/a | line 114 | NUMBER | 2.62 | pad was affected by 2.62 crores | T03 | 00:08:54 | ASR_DOUBT(212 basis points; 2.62 crores)
R076 | page n/a | line 114 | NUMBER | crores | was affected by 2.62 crores | T03 | 00:08:54 | ASR_DOUBT(212 basis points; 2.62 crores)
R077 | page n/a | line 115 | NUMBER | 2 | of Mexico jadeine quarter 2 which I explained in | T03 | 00:09:02 | -
R078 | page n/a | line 116 | NUMBER | 2.07 | of the quarter was 2.07. So now H1 performance | T03 | 00:09:08 | ASR_DOUBT(EPS 2.07 unit missing)
R079 | page n/a | line 117 | NUMBER | 20 | Peninsula 20, 7 consolidated revenue from | T03 | 00:09:18 | ASR_DOUBT('rows' likely crores; '4%' garbled; 47.2%; 19.91%)
R080 | page n/a | line 117 | NUMBER | 7 | Peninsula 20, 7 consolidated revenue from operation | T03 | 00:09:18 | ASR_DOUBT('rows' likely crores; '4%' garbled; 47.2%; 19.91%)
R081 | page n/a | line 117 | NUMBER | 569.11 | revenue from operation was 569.11 rows up 47.2% from | T03 | 00:09:18 | ASR_DOUBT('rows' likely crores; '4%' garbled; 47.2%; 19.91%)
R082 | page n/a | line 117 | NUMBER | 47.2% | was 569.11 rows up 47.2% from 4% against 19.91% | T03 | 00:09:18 | ASR_DOUBT('rows' likely crores; '4%' garbled; 47.2%; 19.91%)
R083 | page n/a | line 117 | NUMBER | 4% | rows up 47.2% from 4% against 19.91% | T03 | 00:09:18 | ASR_DOUBT('rows' likely crores; '4%' garbled; 47.2%; 19.91%)
R084 | page n/a | line 117 | NUMBER | 19.91% | 47.2% from 4% against 19.91% | T03 | 00:09:18 | ASR_DOUBT('rows' likely crores; '4%' garbled; 47.2%; 19.91%)
R085 | page n/a | line 118 | NUMBER | 19.11% | ago. ROE stood at 19.11% | T03 | 00:09:56 | ASR_DOUBT(ROE 19.11% vs 'Both 2%')
R086 | page n/a | line 119 | NUMBER | 2% | Both 2% this ROC at 28.76%. | T03 | 00:10:00 | ASR_DOUBT(ROC 28.76%)
R087 | page n/a | line 119 | NUMBER | 28.76% | 2% this ROC at 28.76%. The moderation in ROE | T03 | 00:10:00 | ASR_DOUBT(ROC 28.76%)
R088 | page n/a | line 122 | NUMBER | 7 | for H-1 Peninsula F-1T, 7 was 55.55 crores compared | T03 | 00:10:23 | ASR_DOUBT(55.55 vs 41.30 crores)
R089 | page n/a | line 122 | NUMBER | 55.55 | Peninsula F-1T, 7 was 55.55 crores compared with 41.30 | T03 | 00:10:23 | ASR_DOUBT(55.55 vs 41.30 crores)
R090 | page n/a | line 122 | NUMBER | crores | F-1T, 7 was 55.55 crores compared with 41.30 | T03 | 00:10:23 | ASR_DOUBT(55.55 vs 41.30 crores)
R091 | page n/a | line 122 | NUMBER | 41.30 | 55.55 crores compared with 41.30 | T03 | 00:10:23 | ASR_DOUBT(55.55 vs 41.30 crores)
R092 | page n/a | line 123 | NUMBER | crores | crores in H-1 Peninsula F-1T, | T03 | 00:10:32 | ASR_DOUBT(34.5 percent)
R093 | page n/a | line 123 | NUMBER | 34.5 | H-1 Peninsula F-1T, up 34.5 percent. | T03 | 00:10:32 | ASR_DOUBT(34.5 percent)
R094 | page n/a | line 123 | NUMBER | percent | Peninsula F-1T, up 34.5 percent. | T03 | 00:10:32 | ASR_DOUBT(34.5 percent)
R095 | page n/a | line 124 | NUMBER | 9.76 | The PAD margin was 9.76 percent, against 10.68 percent | T03 | 00:10:37 | ASR_DOUBT(9.76 vs 10.68)
R096 | page n/a | line 124 | NUMBER | percent | PAD margin was 9.76 percent, against 10.68 percent in | T03 | 00:10:37 | ASR_DOUBT(9.76 vs 10.68)
R097 | page n/a | line 124 | NUMBER | 10.68 | was 9.76 percent, against 10.68 percent in H-1 Peninsula | T03 | 00:10:37 | ASR_DOUBT(9.76 vs 10.68)
R098 | page n/a | line 124 | NUMBER | percent | 9.76 percent, against 10.68 percent in H-1 Peninsula F-1T, | T03 | 00:10:37 | ASR_DOUBT(9.76 vs 10.68)
R099 | page n/a | line 125 | NUMBER | 6.06 | included a loss of 6.06 crores from the STYM-9 | T03 | 00:10:47 | ASR_DOUBT(6.06 crores)
R100 | page n/a | line 125 | NUMBER | crores | a loss of 6.06 crores from the STYM-9 JV | T03 | 00:10:47 | ASR_DOUBT(6.06 crores)
R101 | page n/a | line 125 | NUMBER | STYM-9 | 6.06 crores from the STYM-9 JV in Mexico. The | T03 | 00:10:47 | ASR_DOUBT(6.06 crores)
R102 | page n/a | line 127 | NUMBER | 3.1 | 3.1, this price will reverse | T03 | 00:11:02 | ASR_DOUBT('3.1' garbled)
R103 | page n/a | line 129 | NUMBER | 1 | Please press star and 1 on the touch-tone telephone. | T04 | 00:11:39 | -
R104 | page n/a | line 130 | NUMBER | 2 | may press star and 2. | T04 | 00:11:42 | -
R105 | page n/a | line 138 | NUMBER | 11,252 | this quarter we closed 11,252 which is 3% growth | T05 | 00:12:27 | ASR_DOUBT(11,252 vs '3% growth'; sentence garbled)
R106 | page n/a | line 138 | NUMBER | 3% | closed 11,252 which is 3% growth from the quarter. | T05 | 00:12:27 | ASR_DOUBT(11,252 vs '3% growth'; sentence garbled)
R107 | page n/a | line 139 | NUMBER | 90-91% | plant is almost utilized 90-91% capacity. Okay so current | T05 | 00:12:40 | ASR_DOUBT(90-91% capacity)
R108 | page n/a | line 140 | NUMBER | 90-90% | we are running at 90-90% utilization, so | T05 | 00:12:47 | -
R109 | page n/a | line 142 | NUMBER | 5,040 | Just we have added 5,040 metrics and quantity in | T05 | 00:12:59 | ASR_DOUBT('5,040 metrics' unit garbled)
R110 | page n/a | line 144 | NUMBER | three | are expecting quarter, quarter three financial year that would | T05 | 00:13:16 | -
R111 | page n/a | line 152 | NUMBER | 45 | with our customers, almost 45 to 50% customers we | T05 | 00:13:54 | -
R112 | page n/a | line 152 | NUMBER | 50% | customers, almost 45 to 50% customers we have | T05 | 00:13:54 | -
R113 | page n/a | line 156 | NUMBER | 26% | quarter there is almost 26% raw material has been | T05 | 00:14:18 | ASR_DOUBT(26% RM increase)
R114 | page n/a | line 157 | NUMBER | 7% | an impact of the 7%. | T05 | 00:14:23 | ASR_DOUBT(7% gross margin impact)
R115 | page n/a | line 159 | NUMBER | three | Reflect in the quarter three majorly and we are | T05 | 00:14:33 | -
R116 | page n/a | line 161 | NUMBER | one | and process almost take one one and a half | T05 | 00:14:56 | -
R117 | page n/a | line 161 | NUMBER | one | process almost take one one and a half month | T05 | 00:14:56 | -
R118 | page n/a | line 163 | NUMBER | 25-30% | gone up like a 25-30% immediately so impact on | T05 | 00:15:07 | ASR_DOUBT(25-30% price rise)
R119 | page n/a | line 164 | NUMBER | 15 | 15 Q1 F5 27 Q2 | T05 | 00:15:14 | ASR_DOUBT(11,252 label garbled)
R120 | page n/a | line 164 | NUMBER | 27 | 15 Q1 F5 27 Q2 F5 27 is | T05 | 00:15:14 | ASR_DOUBT(11,252 label garbled)
R121 | page n/a | line 164 | NUMBER | 27 | F5 27 Q2 F5 27 is 11,252 what would | T05 | 00:15:14 | ASR_DOUBT(11,252 label garbled)
R122 | page n/a | line 164 | NUMBER | 11,252 | Q2 F5 27 is 11,252 what would be the | T05 | 00:15:14 | ASR_DOUBT(11,252 label garbled)
R123 | page n/a | line 165 | NUMBER | 26 | quarter Q2 as per 26? | T05 | 00:15:51 | -
R124 | page n/a | line 166 | NUMBER | one | We have added one with 3 at 26 | T05 | 00:15:53 | ASR_DOUBT(9,927 and '1 with 3' garbled)
R125 | page n/a | line 166 | NUMBER | 3 | have added one with 3 at 26 was 9,927. | T05 | 00:15:53 | ASR_DOUBT(9,927 and '1 with 3' garbled)
R126 | page n/a | line 166 | NUMBER | 26 | one with 3 at 26 was 9,927. | T05 | 00:15:53 | ASR_DOUBT(9,927 and '1 with 3' garbled)
R127 | page n/a | line 166 | NUMBER | 9,927 | 3 at 26 was 9,927. | T05 | 00:15:53 | ASR_DOUBT(9,927 and '1 with 3' garbled)
R128 | page n/a | line 167 | NUMBER | 3 | And we dropped 3 at quarter Q2. | T05 | 00:16:05 | -
R129 | page n/a | line 171 | NUMBER | kg | our gross profit per kg is declined by roughly | T05 | 00:16:34 | ASR_DOUBT(10 rupees, 60 rupees per kg)
R130 | page n/a | line 171 | NUMBER | 10 | is declined by roughly 10 rupees, | T05 | 00:16:34 | ASR_DOUBT(10 rupees, 60 rupees per kg)
R131 | page n/a | line 171 | NUMBER | rupees | declined by roughly 10 rupees, | T05 | 00:16:34 | ASR_DOUBT(10 rupees, 60 rupees per kg)
R132 | page n/a | line 172 | NUMBER | 60 | is round by roughly 60 rupees per kg. Kg | T05 | 00:16:41 | -
R133 | page n/a | line 172 | NUMBER | rupees | round by roughly 60 rupees per kg. Kg is | T05 | 00:16:41 | -
R134 | page n/a | line 172 | NUMBER | kg | roughly 60 rupees per kg. Kg is | T05 | 00:16:41 | -
R135 | page n/a | line 172 | NUMBER | Kg | 60 rupees per kg. Kg is | T05 | 00:16:41 | -
R136 | page n/a | line 173 | NUMBER | 36 | currently 36 rupees versus last quarter | T05 | 00:16:46 | ASR_DOUBT(36 vs 51.52 rupees per kg)
R137 | page n/a | line 173 | NUMBER | rupees | currently 36 rupees versus last quarter we | T05 | 00:16:46 | ASR_DOUBT(36 vs 51.52 rupees per kg)
R138 | page n/a | line 173 | NUMBER | 51.52 | we were doing at 51.52 rupees. Is it correct | T05 | 00:16:46 | ASR_DOUBT(36 vs 51.52 rupees per kg)
R139 | page n/a | line 173 | NUMBER | rupees | were doing at 51.52 rupees. Is it correct sir? | T05 | 00:16:46 | ASR_DOUBT(36 vs 51.52 rupees per kg)
R140 | page n/a | line 175 | NUMBER | 25 | The price increment like 25 to 16 percent immediately | T05 | 00:17:00 | ASR_DOUBT('25 to 16 percent' garbled)
R141 | page n/a | line 175 | NUMBER | 16 | increment like 25 to 16 percent immediately immediate effect | T05 | 00:17:00 | ASR_DOUBT('25 to 16 percent' garbled)
R142 | page n/a | line 175 | NUMBER | percent | like 25 to 16 percent immediately immediate effect and | T05 | 00:17:00 | ASR_DOUBT('25 to 16 percent' garbled)
R143 | page n/a | line 177 | NUMBER | one | timeline is about one and a half month. | T06 | 00:17:12 | -
R144 | page n/a | line 178 | NUMBER | Seven | Hidansha from Seven Island BMS. Please go | T06 | 00:17:30 | -
R145 | page n/a | line 180 | NUMBER | two | just recently we added two machines on the | T06 | 00:17:49 | -
R146 | page n/a | line 181 | NUMBER | one | part of one and part of one | T06 | 00:17:53 | -
R147 | page n/a | line 181 | NUMBER | one | one and part of one start like every month | T06 | 00:17:53 | -
R148 | page n/a | line 182 | NUMBER | 100% | 100% it is a 21% | T06 | 00:18:01 | ASR_DOUBT(100%, 21% share)
R149 | page n/a | line 182 | NUMBER | 21% | 100% it is a 21% of the overall self | T06 | 00:18:01 | ASR_DOUBT(100%, 21% share)
R150 | page n/a | line 183 | NUMBER | 4 | will take like a 4 to 5 months because | T06 | 00:18:09 | -
R151 | page n/a | line 183 | NUMBER | 5 | like a 4 to 5 months because the design | T06 | 00:18:09 | -
R152 | page n/a | line 186 | NUMBER | 21% | today yes we have 21% revenue from the pinch | T06 | 00:18:24 | ASR_DOUBT(21% vs '17 or 18 years' (likely %))
R153 | page n/a | line 186 | NUMBER | 17 | last year it is 17 or 18 years | T06 | 00:18:24 | ASR_DOUBT(21% vs '17 or 18 years' (likely %))
R154 | page n/a | line 186 | NUMBER | 18 | it is 17 or 18 years | T06 | 00:18:24 | ASR_DOUBT(21% vs '17 or 18 years' (likely %))
R155 | page n/a | line 188 | NUMBER | ton | of the total metric ton per annum that we | T06 | 00:18:37 | -
R156 | page n/a | line 189 | NUMBER | 90-91% | all together is a 90-91% utilization but yes you | T06 | 00:18:43 | -
R157 | page n/a | line 190 | NUMBER | 100% | yes it is not 100% utilization of the pinch | T06 | 00:18:54 | -
R158 | page n/a | line 191 | NUMBER | 60-65-70% | say approximately 60-65-70% only after the new | T06 | 00:19:03 | ASR_DOUBT(60-65-70%)
R159 | page n/a | line 195 | NUMBER | two | and last area, last two quarters. | T06 | 00:19:28 | -
R160 | page n/a | line 197 | NUMBER | 23 | of pinch bottoms for 23 and 2, most in | T06 | 00:19:42 | ASR_DOUBT('23 and 2... March of 25' garbled)
R161 | page n/a | line 197 | NUMBER | 2 | bottoms for 23 and 2, most in March of | T06 | 00:19:42 | ASR_DOUBT('23 and 2... March of 25' garbled)
R162 | page n/a | line 197 | NUMBER | 25 | most in March of 25. | T06 | 00:19:42 | ASR_DOUBT('23 and 2... March of 25' garbled)
R163 | page n/a | line 199 | NUMBER | 60-70% | Base ratio set 60-70% is overall and now | T06 | 00:20:00 | ASR_DOUBT(60-70%)
R164 | page n/a | line 200 | NUMBER | three | the quarter through three would be more commercial, | T06 | 00:20:08 | -
R165 | page n/a | line 204 | NUMBER | ton | metric ton per mm capacity of | T06 | 00:20:35 | -
R166 | page n/a | line 205 | NUMBER | 20 | is covered like a 20, like 22 million back | T06 | 00:20:42 | ASR_DOUBT('20, like 22 million back per month' unit)
R167 | page n/a | line 205 | NUMBER | 22 | like a 20, like 22 million back per month, | T06 | 00:20:42 | ASR_DOUBT('20, like 22 million back per month' unit)
R168 | page n/a | line 205 | NUMBER | million | a 20, like 22 million back per month, so | T06 | 00:20:42 | ASR_DOUBT('20, like 22 million back per month' unit)
R169 | page n/a | line 206 | NUMBER | 11,252 | be is quantity at 11,252 metric ton. So basically | T06 | 00:20:50 | ASR_DOUBT(11,252 metric ton)
R170 | page n/a | line 206 | NUMBER | ton | quantity at 11,252 metric ton. So basically there is | T06 | 00:20:50 | ASR_DOUBT(11,252 metric ton)
R171 | page n/a | line 211 | NUMBER | 26 | the length of year 26. So that machine is | T06 | 00:21:26 | -
R172 | page n/a | line 212 | NUMBER | one | of one hour production capacity will | T06 | 00:21:33 | -
R173 | page n/a | line 212 | NUMBER | 91% | today we have already 91% capitalization. | T06 | 00:21:33 | -
R174 | page n/a | line 216 | NUMBER | one | will give you just one simple example. | T06 | 00:21:57 | -
R175 | page n/a | line 228 | NUMBER | one | industry. Okay first and one last question | T06 | 00:22:38 | -
R176 | page n/a | line 229 | NUMBER | 30,000 | facilities will add around 30,000 to 32,000 metric tons | T06 | 00:22:46 | ASR_DOUBT(30,000 to 32,000 MTPA)
R177 | page n/a | line 229 | NUMBER | 32,000 | add around 30,000 to 32,000 metric tons per annum. | T06 | 00:22:46 | ASR_DOUBT(30,000 to 32,000 MTPA)
R178 | page n/a | line 229 | NUMBER | tons | 30,000 to 32,000 metric tons per annum. | T06 | 00:22:46 | ASR_DOUBT(30,000 to 32,000 MTPA)
R179 | page n/a | line 232 | NUMBER | 42,000 | at installed capacity of 42,000 metric tons | T06 | 00:23:02 | ASR_DOUBT(42,000 MT)
R180 | page n/a | line 232 | NUMBER | tons | capacity of 42,000 metric tons | T06 | 00:23:02 | ASR_DOUBT(42,000 MT)
R181 | page n/a | line 233 | NUMBER | 30,000 | that we have almost 30,000 like 39,000 capacity. | T06 | 00:23:08 | ASR_DOUBT('30,000 like 39,000' garbled)
R182 | page n/a | line 233 | NUMBER | 39,000 | have almost 30,000 like 39,000 capacity. | T06 | 00:23:08 | ASR_DOUBT('30,000 like 39,000' garbled)
R183 | page n/a | line 234 | NUMBER | 70,000 | capacity reach into the 70,000, 69 to 72,000 in | T06 | 00:23:13 | ASR_DOUBT(70,000; 69 to 72,000)
R184 | page n/a | line 234 | NUMBER | 69 | reach into the 70,000, 69 to 72,000 in between. | T06 | 00:23:13 | ASR_DOUBT(70,000; 69 to 72,000)
R185 | page n/a | line 234 | NUMBER | 72,000 | the 70,000, 69 to 72,000 in between. | T06 | 00:23:13 | ASR_DOUBT(70,000; 69 to 72,000)
R186 | page n/a | line 236 | NUMBER | two | And two new pinch machines will | T06 | 00:23:23 | -
R187 | page n/a | line 236 | NUMBER | one | delivery is almost big, one, one and a half | T06 | 00:23:23 | -
R188 | page n/a | line 236 | NUMBER | one | is almost big, one, one and a half year. | T06 | 00:23:23 | -
R189 | page n/a | line 238 | NUMBER | two | in between our existing two machines, capacity, we can | T06 | 00:23:34 | -
R190 | page n/a | line 240 | NUMBER | 7 | after it is almost 7 matches. So, almost 70,000 | T06 | 00:23:42 | ASR_DOUBT('7 matches', 70,000, 25,000/30,000)
R191 | page n/a | line 240 | NUMBER | 70,000 | 7 matches. So, almost 70,000 the metrics are we | T06 | 00:23:42 | ASR_DOUBT('7 matches', 70,000, 25,000/30,000)
R192 | page n/a | line 240 | NUMBER | 25,000 | we can achieve almost 25,000 altogether or 30,000. | T06 | 00:23:42 | ASR_DOUBT('7 matches', 70,000, 25,000/30,000)
R193 | page n/a | line 240 | NUMBER | 30,000 | almost 25,000 altogether or 30,000. | T06 | 00:23:42 | ASR_DOUBT('7 matches', 70,000, 25,000/30,000)
R194 | page n/a | line 241 | NUMBER | 32,000 | Installed capacity is the 32,000 out of 72,000 is | T06 | 00:23:52 | ASR_DOUBT(32,000 out of 72,000; 25,000-30,000; 'later on 28')
R195 | page n/a | line 241 | NUMBER | 72,000 | the 32,000 out of 72,000 is the pinch water | T06 | 00:23:52 | ASR_DOUBT(32,000 out of 72,000; 25,000-30,000; 'later on 28')
R196 | page n/a | line 241 | NUMBER | 25,000 | can try first level 25,000 to 30,000 to achieve | T06 | 00:23:52 | ASR_DOUBT(32,000 out of 72,000; 25,000-30,000; 'later on 28')
R197 | page n/a | line 241 | NUMBER | 30,000 | first level 25,000 to 30,000 to achieve that pinch | T06 | 00:23:52 | ASR_DOUBT(32,000 out of 72,000; 25,000-30,000; 'later on 28')
R198 | page n/a | line 241 | NUMBER | 28 | water max later on 28. | T06 | 00:23:52 | ASR_DOUBT(32,000 out of 72,000; 25,000-30,000; 'later on 28')
R199 | page n/a | line 244 | NUMBER | 1 | please press star and 1. The next | T07 | 00:24:10 | -
R200 | page n/a | line 249 | NUMBER | 50% | bifurcation of 50% which is coming from | T07 | 00:24:50 | -
R201 | page n/a | line 249 | NUMBER | 50% | contract revenues and approximately 50% | T07 | 00:24:50 | -
R202 | page n/a | line 254 | NUMBER | 50% | our first of all 50% contract you like customers | T07 | 00:25:22 | -
R203 | page n/a | line 257 | NUMBER | 45 | it is the almost 45 to 50% contracture | T07 | 00:25:38 | -
R204 | page n/a | line 257 | NUMBER | 50% | the almost 45 to 50% contracture | T07 | 00:25:38 | -
R205 | page n/a | line 258 | NUMBER | 10 | work order will come 10 times every person. Secondly, | T07 | 00:25:47 | ASR_DOUBT(45 to 50%; 25-30% price rise)
R206 | page n/a | line 258 | NUMBER | 25-30% | is grown up like 25-30% | T07 | 00:25:47 | ASR_DOUBT(45 to 50%; 25-30% price rise)
R207 | page n/a | line 261 | NUMBER | one | play in the quarter one order and deliver into | T07 | 00:26:08 | -
R208 | page n/a | line 261 | NUMBER | two | deliver into the quarter two so why in one | T07 | 00:26:08 | -
R209 | page n/a | line 261 | NUMBER | one | two so why in one thing | T07 | 00:26:08 | -
R210 | page n/a | line 264 | NUMBER | one | second one reason is the oh | T07 | 00:27:00 | -
R211 | page n/a | line 264 | NUMBER | one | I repeat the first one because maybe | T07 | 00:27:00 | -
R212 | page n/a | line 266 | NUMBER | one | is the like a one one and a half | T07 | 00:27:12 | -
R213 | page n/a | line 266 | NUMBER | one | the like a one one and a half month | T07 | 00:27:12 | -
R214 | page n/a | line 266 | NUMBER | 50% | a half month our 50% customer is on contract | T07 | 00:27:12 | -
R215 | page n/a | line 271 | NUMBER | 25 | price is like a 25 to 30 percent increment | T07 | 00:27:42 | ASR_DOUBT(25 to 30 percent)
R216 | page n/a | line 271 | NUMBER | 30 | like a 25 to 30 percent increment global politically | T07 | 00:27:42 | ASR_DOUBT(25 to 30 percent)
R217 | page n/a | line 271 | NUMBER | percent | a 25 to 30 percent increment global politically issue | T07 | 00:27:42 | ASR_DOUBT(25 to 30 percent)
R218 | page n/a | line 273 | NUMBER | seven | the increment of the seven percent of our growth | T07 | 00:27:55 | ASR_DOUBT(seven percent gross margin)
R219 | page n/a | line 273 | NUMBER | percent | increment of the seven percent of our growth margin | T07 | 00:27:55 | ASR_DOUBT(seven percent gross margin)
R220 | page n/a | line 274 | NUMBER | 50 | so again basically the 50 percent of the contractor | T07 | 00:28:04 | -
R221 | page n/a | line 274 | NUMBER | percent | again basically the 50 percent of the contractor revenues | T07 | 00:28:04 | -
R222 | page n/a | line 278 | NUMBER | two | contractually there is a two system monthly price revision | T07 | 00:28:40 | -
R223 | page n/a | line 285 | NUMBER | one | will be delivered after one and one and a | T07 | 00:29:18 | -
R224 | page n/a | line 285 | NUMBER | one | delivered after one and one and a half months | T07 | 00:29:18 | -
R225 | page n/a | line 286 | NUMBER | three | it is like almost three two three and three | T07 | 00:29:24 | ASR_DOUBT(2/3/3.5 months)
R226 | page n/a | line 286 | NUMBER | two | is like almost three two three and three and | T07 | 00:29:24 | ASR_DOUBT(2/3/3.5 months)
R227 | page n/a | line 286 | NUMBER | three | like almost three two three and three and a | T07 | 00:29:24 | ASR_DOUBT(2/3/3.5 months)
R228 | page n/a | line 286 | NUMBER | three | three two three and three and a half months | T07 | 00:29:24 | ASR_DOUBT(2/3/3.5 months)
R229 | page n/a | line 286 | NUMBER | one | half months for the one month | T07 | 00:29:24 | ASR_DOUBT(2/3/3.5 months)
R230 | page n/a | line 287 | NUMBER | four | it is intact on four and four and a | T07 | 00:29:29 | ASR_DOUBT(4/4.5 months)
R231 | page n/a | line 287 | NUMBER | four | intact on four and four and a half month | T07 | 00:29:29 | ASR_DOUBT(4/4.5 months)
R232 | page n/a | line 292 | NUMBER | one | will be take the one and | T07 | 00:29:55 | -
R233 | page n/a | line 296 | NUMBER | two | Sir, demand, we have two types of vision. | T08 | 00:30:50 | -
R234 | page n/a | line 297 | NUMBER | 72 | are exporting more than 72 countries. | T08 | 00:30:54 | ASR_DOUBT(72 countries vs 75)
R235 | page n/a | line 299 | NUMBER | one | I will say the one example, dog food industry | T08 | 00:31:01 | -
R236 | page n/a | line 300 | NUMBER | double | in double digits. So, dog food | T08 | 00:31:06 | -
R237 | page n/a | line 304 | NUMBER | 27 | a we have a 27 different kind of industries, | T08 | 00:31:27 | ASR_DOUBT('27 different kinds of industries' vs '25 plus')
R238 | page n/a | line 313 | NUMBER | 80% | bottom bag varies the 80% those | T08 | 00:32:14 | ASR_DOUBT('80%' garbled)
R239 | page n/a | line 315 | NUMBER | 71-72% | total revenue contribution, like 71-72%. | T08 | 00:32:25 | ASR_DOUBT(71-72%)
R240 | page n/a | line 316 | NUMBER | PLW-50 | volume, it is on PLW-50, so we have a | T08 | 00:32:30 | ASR_DOUBT('PLW-50')
R241 | page n/a | line 323 | NUMBER | 2004 | the 2004 our company is the | T08 | 00:33:00 | -
R242 | page n/a | line 324 | NUMBER | one | at that time the one bag cost is a | T08 | 00:33:06 | ASR_DOUBT(10 rupees cost, 14 or 15 rupees)
R243 | page n/a | line 324 | NUMBER | 10 | bag cost is a 10 rupees and we | T08 | 00:33:06 | ASR_DOUBT(10 rupees cost, 14 or 15 rupees)
R244 | page n/a | line 324 | NUMBER | rupees | cost is a 10 rupees and we | T08 | 00:33:06 | ASR_DOUBT(10 rupees cost, 14 or 15 rupees)
R245 | page n/a | line 325 | NUMBER | 14 | selling at 14 or 15 rupees bag | T08 | 00:33:10 | ASR_DOUBT(40-50 percent)
R246 | page n/a | line 325 | NUMBER | 15 | selling at 14 or 15 rupees bag but now | T08 | 00:33:10 | ASR_DOUBT(40-50 percent)
R247 | page n/a | line 325 | NUMBER | rupees | at 14 or 15 rupees bag but now very | T08 | 00:33:10 | ASR_DOUBT(40-50 percent)
R248 | page n/a | line 325 | NUMBER | 40-50 | well accepted this scenario 40-50 percent | T08 | 00:33:10 | ASR_DOUBT(40-50 percent)
R249 | page n/a | line 325 | NUMBER | percent | accepted this scenario 40-50 percent | T08 | 00:33:10 | ASR_DOUBT(40-50 percent)
R250 | page n/a | line 327 | NUMBER | rupees | it like a 2022 rupees, | T08 | 00:33:21 | ASR_DOUBT(2022 rupees (likely 20-22))
R251 | page n/a | line 328 | NUMBER | 24 | 24 rupees bag, PLWPP and | T08 | 00:33:26 | ASR_DOUBT(28, 30, 32 rupees)
R252 | page n/a | line 328 | NUMBER | rupees | 24 rupees bag, PLWPP and their | T08 | 00:33:26 | ASR_DOUBT(28, 30, 32 rupees)
R253 | page n/a | line 328 | NUMBER | 28 | tag shifted into the 28, 30, 32 rupees. So | T08 | 00:33:26 | ASR_DOUBT(28, 30, 32 rupees)
R254 | page n/a | line 328 | NUMBER | 30 | shifted into the 28, 30, 32 rupees. So percentage | T08 | 00:33:26 | ASR_DOUBT(28, 30, 32 rupees)
R255 | page n/a | line 328 | NUMBER | 32 | into the 28, 30, 32 rupees. So percentage | T08 | 00:33:26 | ASR_DOUBT(28, 30, 32 rupees)
R256 | page n/a | line 328 | NUMBER | rupees | the 28, 30, 32 rupees. So percentage | T08 | 00:33:26 | ASR_DOUBT(28, 30, 32 rupees)
R257 | page n/a | line 330 | NUMBER | 1 | it is less than 1 or 2 percent. | T08 | 00:33:38 | ASR_DOUBT(1 or 2 percent)
R258 | page n/a | line 330 | NUMBER | 2 | less than 1 or 2 percent. | T08 | 00:33:38 | ASR_DOUBT(1 or 2 percent)
R259 | page n/a | line 330 | NUMBER | percent | than 1 or 2 percent. | T08 | 00:33:38 | ASR_DOUBT(1 or 2 percent)
R260 | page n/a | line 331 | NUMBER | one | of this product and one more, | T08 | 00:33:44 | -
R261 | page n/a | line 332 | NUMBER | seven | already many time mentioned seven reason customer will want | T08 | 00:33:49 | -
R262 | page n/a | line 334 | NUMBER | one | I want to add one more thing | T08 | 00:34:07 | -
R263 | page n/a | line 339 | NUMBER | 30 | bottom bag like a 30 year bag product paper | T08 | 00:34:31 | ASR_DOUBT(30 year)
R264 | page n/a | line 339 | NUMBER | 30 | pinch bottom bag is 30 year bag old product | T08 | 00:34:31 | ASR_DOUBT(30 year)
R265 | page n/a | line 341 | NUMBER | one | So, this is also one more factor for our | T08 | 00:34:43 | -
R266 | page n/a | line 355 | NUMBER | One | One first is that, sorry | T09 | 00:35:14 | -
R267 | page n/a | line 355 | NUMBER | 7 | the Q2 of volume 7, overall? | T09 | 00:35:14 | -
R268 | page n/a | line 356 | NUMBER | 10,940 | know the Q1 volume 10,940, it is the increase | T09 | 00:35:23 | ASR_DOUBT(Q1 10,940, 11,252%, 3% garbled)
R269 | page n/a | line 356 | NUMBER | 3% | is the increase by 3%, 11,252%. | T09 | 00:35:23 | ASR_DOUBT(Q1 10,940, 11,252%, 3% garbled)
R270 | page n/a | line 356 | NUMBER | 11,252% | the increase by 3%, 11,252%. | T09 | 00:35:23 | ASR_DOUBT(Q1 10,940, 11,252%, 3% garbled)
R271 | page n/a | line 360 | NUMBER | 52.52% | 52.52%. | T09 | 00:35:39 | ASR_DOUBT(52.52%)
R272 | page n/a | line 361 | NUMBER | 52.2% | In sales revenue growth 52.2% YY, EBITDA margin growth | T09 | 00:35:42 | ASR_DOUBT(52.2% vs 52.52%; 29.92%)
R273 | page n/a | line 361 | NUMBER | 29.92% | EBITDA margin growth is 29.92%. | T09 | 00:35:42 | ASR_DOUBT(52.2% vs 52.52%; 29.92%)
R274 | page n/a | line 363 | NUMBER | 13% | YY volume growth is 13%. | T09 | 00:35:59 | ASR_DOUBT(13%)
R275 | page n/a | line 364 | NUMBER | 1 | 1, 3%. | T09 | 00:36:01 | ASR_DOUBT(1, 3% fragment)
R276 | page n/a | line 364 | NUMBER | 3% | 1, 3%. | T09 | 00:36:01 | ASR_DOUBT(1, 3% fragment)
R277 | page n/a | line 376 | NUMBER | 89-91% | because we are almost 89-91% we are utilizing and | T09 | 00:36:51 | ASR_DOUBT(89-91% vs 90-91%)
R278 | page n/a | line 384 | NUMBER | one | expected like the quarter one like kind of thing | T09 | 00:37:38 | -
R279 | page n/a | line 384 | NUMBER | three | of thing into quarter three and quarter four. | T09 | 00:37:38 | -
R280 | page n/a | line 384 | NUMBER | four | quarter three and quarter four. | T09 | 00:37:38 | -
R281 | page n/a | line 386 | NUMBER | one | there is a single one percent is depends on | T09 | 00:37:55 | -
R282 | page n/a | line 386 | NUMBER | percent | is a single one percent is depends on the | T09 | 00:37:55 | -
R283 | page n/a | line 388 | NUMBER | 92 | the polymer example like 92 rupees before the war | T09 | 00:38:07 | ASR_DOUBT(92 rupees)
R284 | page n/a | line 388 | NUMBER | rupees | polymer example like 92 rupees before the war then | T09 | 00:38:07 | ASR_DOUBT(92 rupees)
R285 | page n/a | line 389 | NUMBER | 135 | up to the 135 140 rupees after war | T09 | 00:38:14 | ASR_DOUBT(135 140; 145 143)
R286 | page n/a | line 389 | NUMBER | 140 | up to the 135 140 rupees after war after | T09 | 00:38:14 | ASR_DOUBT(135 140; 145 143)
R287 | page n/a | line 389 | NUMBER | rupees | to the 135 140 rupees after war after that | T09 | 00:38:14 | ASR_DOUBT(135 140; 145 143)
R288 | page n/a | line 389 | NUMBER | 145 | reach up to the 145 143 | T09 | 00:38:14 | ASR_DOUBT(135 140; 145 143)
R289 | page n/a | line 389 | NUMBER | 143 | up to the 145 143 | T09 | 00:38:14 | ASR_DOUBT(135 140; 145 143)
R290 | page n/a | line 390 | NUMBER | 120 | it is reducing like 120 125 and it is | T09 | 00:38:22 | ASR_DOUBT(120 125; 160)
R291 | page n/a | line 390 | NUMBER | 125 | is reducing like 120 125 and it is like | T09 | 00:38:22 | ASR_DOUBT(120 125; 160)
R292 | page n/a | line 390 | NUMBER | 160 | and it is like 160 rupees so what happened | T09 | 00:38:22 | ASR_DOUBT(120 125; 160)
R293 | page n/a | line 390 | NUMBER | rupees | it is like 160 rupees so what happened it | T09 | 00:38:22 | ASR_DOUBT(120 125; 160)
R294 | page n/a | line 392 | NUMBER | 30 | In this, in our 30 years, we never seen | T09 | 00:38:35 | -
R295 | page n/a | line 392 | NUMBER | 30 | like this. In this 30 years, this is the | T09 | 00:38:35 | -
R296 | page n/a | line 394 | NUMBER | one | But there is a one percent, I will tell | T09 | 00:38:47 | -
R297 | page n/a | line 394 | NUMBER | percent | there is a one percent, I will tell you, | T09 | 00:38:47 | -
R298 | page n/a | line 395 | NUMBER | 99 | the market. But yes, 99 percent, we covered this | T09 | 00:38:52 | ASR_DOUBT(99 percent)
R299 | page n/a | line 395 | NUMBER | percent | market. But yes, 99 percent, we covered this everything. | T09 | 00:38:52 | ASR_DOUBT(99 percent)
R300 | page n/a | line 396 | NUMBER | one | October you have received one | T09 | 00:38:56 | -
R301 | page n/a | line 397 | NUMBER | 150 | good order of about 150 crore on some international | T09 | 00:39:06 | ASR_DOUBT(150 crore)
R302 | page n/a | line 397 | NUMBER | crore | order of about 150 crore on some international client | T09 | 00:39:06 | ASR_DOUBT(150 crore)
R303 | page n/a | line 398 | NUMBER | one | a kind of a one-off order this is our | T09 | 00:39:14 | -
R304 | page n/a | line 402 | NUMBER | one | contract up to the one year. | T09 | 00:39:32 | -
R305 | page n/a | line 405 | NUMBER | three | into three years, next three years. | T09 | 00:39:43 | -
R306 | page n/a | line 405 | NUMBER | three | into three years, next three years. | T09 | 00:39:43 | -
R307 | page n/a | line 406 | NUMBER | 150 | So this is a 150 crores every month order, | T09 | 00:39:45 | ASR_DOUBT('150 crores every month order')
R308 | page n/a | line 406 | NUMBER | crores | this is a 150 crores every month order, | T09 | 00:39:45 | ASR_DOUBT('150 crores every month order')
R309 | page n/a | line 407 | NUMBER | one | order, it is a one year minimum. | T09 | 00:39:48 | -
R310 | page n/a | line 408 | NUMBER | 150 | It is a minimum 150 crores. | T09 | 00:39:50 | ASR_DOUBT(150 crores minimum)
R311 | page n/a | line 408 | NUMBER | crores | is a minimum 150 crores. | T09 | 00:39:50 | ASR_DOUBT(150 crores minimum)
R312 | page n/a | line 410 | NUMBER | eight | We are serving only eight to nine countries and | T09 | 00:39:56 | ASR_DOUBT(eight to nine countries)
R313 | page n/a | line 410 | NUMBER | nine | serving only eight to nine countries and they are | T09 | 00:39:56 | ASR_DOUBT(eight to nine countries)
R314 | page n/a | line 411 | NUMBER | 150 | like this is the 150. This | T09 | 00:40:00 | -
R315 | page n/a | line 412 | NUMBER | 150 | is bottom of the 150 crores and this is | T09 | 00:40:09 | ASR_DOUBT(150 crores, three year)
R316 | page n/a | line 412 | NUMBER | crores | bottom of the 150 crores and this is not | T09 | 00:40:09 | ASR_DOUBT(150 crores, three year)
R317 | page n/a | line 412 | NUMBER | one | and this is not one year, this is a | T09 | 00:40:09 | ASR_DOUBT(150 crores, three year)
R318 | page n/a | line 412 | NUMBER | three | year, this is a three year contract. | T09 | 00:40:09 | ASR_DOUBT(150 crores, three year)
R319 | page n/a | line 422 | NUMBER | two | to two per participant. If you | T10 | 00:41:01 | -
R320 | page n/a | line 425 | NUMBER | 39 | decrease in H1 from 39 crores to | T10 | 00:41:17 | ASR_DOUBT(39 crores to 22 crores operating cash flow)
R321 | page n/a | line 425 | NUMBER | crores | in H1 from 39 crores to | T10 | 00:41:17 | ASR_DOUBT(39 crores to 22 crores operating cash flow)
R322 | page n/a | line 426 | NUMBER | 22 | 22 crores. I see three | T10 | 00:41:24 | -
R323 | page n/a | line 426 | NUMBER | crores | 22 crores. I see three items | T10 | 00:41:24 | -
R324 | page n/a | line 426 | NUMBER | three | 22 crores. I see three items a bit of | T10 | 00:41:24 | -
R325 | page n/a | line 427 | NUMBER | one | So is this seasonal one | T10 | 00:41:31 | -
R326 | page n/a | line 436 | NUMBER | 26.9 | the sale. So almost 26.9 crores we have increase | T10 | 00:42:27 | ASR_DOUBT(26.9 crores)
R327 | page n/a | line 436 | NUMBER | crores | sale. So almost 26.9 crores we have increase in | T10 | 00:42:27 | ASR_DOUBT(26.9 crores)
R328 | page n/a | line 439 | NUMBER | 55 | compared to domestic, so 55 crores investment is already | T10 | 00:42:48 | -
R329 | page n/a | line 439 | NUMBER | crores | to domestic, so 55 crores investment is already | T10 | 00:42:48 | -
R330 | page n/a | line 440 | NUMBER | two | So these are majorly two factors which is | T10 | 00:42:57 | ASR_DOUBT(55 crores)
R331 | page n/a | line 441 | NUMBER | two | previous year of quarter two operating cash flow | T10 | 00:43:02 | -
R332 | page n/a | line 444 | NUMBER | 22% | tax rate is still 22% which is new regime | T10 | 00:43:20 | ASR_DOUBT(22%)
R333 | page n/a | line 445 | NUMBER | 25% | effective tax rate is 25% so tax impact | T10 | 00:43:27 | ASR_DOUBT(25% effective tax)
R334 | page n/a | line 447 | NUMBER | 28 | already given the report 28 crores. So that has | T10 | 00:43:38 | ASR_DOUBT(28 crores IPO expense)
R335 | page n/a | line 447 | NUMBER | crores | given the report 28 crores. So that has been | T10 | 00:43:38 | ASR_DOUBT(28 crores IPO expense)
R336 | page n/a | line 453 | NUMBER | one | better than the quarter one | T10 | 00:44:21 | -
R337 | page n/a | line 454 | NUMBER | two | shine from the quarter two and quarter three we | T10 | 00:44:27 | -
R338 | page n/a | line 454 | NUMBER | three | quarter two and quarter three we are expecting | T10 | 00:44:27 | -
R339 | page n/a | line 456 | NUMBER | four | four is our targeted to | T10 | 00:44:38 | -
R340 | page n/a | line 457 | NUMBER | three | quarter three we are expecting to | T10 | 00:44:45 | -
R341 | page n/a | line 460 | NUMBER | three | also expecting to quarter three is better result from | T10 | 00:45:01 | -
R342 | page n/a | line 462 | NUMBER | 400 | capacity is like a 400 ton metric ton out | T10 | 00:45:08 | ASR_DOUBT(400 ton installed)
R343 | page n/a | line 462 | NUMBER | ton | is like a 400 ton metric ton out of | T10 | 00:45:08 | ASR_DOUBT(400 ton installed)
R344 | page n/a | line 462 | NUMBER | ton | a 400 ton metric ton out of that every | T10 | 00:45:08 | ASR_DOUBT(400 ton installed)
R345 | page n/a | line 463 | NUMBER | 80 | selling all course like 80 ton nearby and this | T10 | 00:45:13 | ASR_DOUBT(80 ton)
R346 | page n/a | line 463 | NUMBER | ton | all course like 80 ton nearby and this quarter | T10 | 00:45:13 | ASR_DOUBT(80 ton)
R347 | page n/a | line 464 | NUMBER | 120 | 120 metric tons and almost | T10 | 00:45:19 | ASR_DOUBT(120 MT)
R348 | page n/a | line 464 | NUMBER | tons | 120 metric tons and almost 120 metric | T10 | 00:45:19 | ASR_DOUBT(120 MT)
R349 | page n/a | line 464 | NUMBER | 120 | metric tons and almost 120 metric tons is the | T10 | 00:45:19 | ASR_DOUBT(120 MT)
R350 | page n/a | line 464 | NUMBER | tons | and almost 120 metric tons is the near by | T10 | 00:45:19 | ASR_DOUBT(120 MT)
R351 | page n/a | line 476 | NUMBER | one | Just one thing, now that I | T11 | 00:45:52 | -
R352 | page n/a | line 478 | NUMBER | one | the losses in the one quarter but | T11 | 00:46:05 | -
R353 | page n/a | line 481 | NUMBER | 3500 | are producing like a 3500 metric ton, 3000 ton | T11 | 00:46:16 | ASR_DOUBT(3500 MT / 3000 ton garbled)
R354 | page n/a | line 481 | NUMBER | ton | like a 3500 metric ton, 3000 ton | T11 | 00:46:16 | ASR_DOUBT(3500 MT / 3000 ton garbled)
R355 | page n/a | line 481 | NUMBER | 3000 | a 3500 metric ton, 3000 ton | T11 | 00:46:16 | ASR_DOUBT(3500 MT / 3000 ton garbled)
R356 | page n/a | line 481 | NUMBER | ton | 3500 metric ton, 3000 ton | T11 | 00:46:16 | ASR_DOUBT(3500 MT / 3000 ton garbled)
R357 | page n/a | line 482 | NUMBER | 400 | installed capacity is only 400, 400 metric ton per | T11 | 00:46:22 | ASR_DOUBT(400 MT per month)
R358 | page n/a | line 482 | NUMBER | 400 | capacity is only 400, 400 metric ton per month. | T11 | 00:46:22 | ASR_DOUBT(400 MT per month)
R359 | page n/a | line 482 | NUMBER | ton | only 400, 400 metric ton per month. So we | T11 | 00:46:22 | ASR_DOUBT(400 MT per month)
R360 | page n/a | line 488 | NUMBER | one | And one capacity you said 5040, | T11 | 00:46:57 | ASR_DOUBT('5040' garbled)
R361 | page n/a | line 488 | NUMBER | 5040 | one capacity you said 5040, sorry, you were saying | T11 | 00:46:57 | ASR_DOUBT('5040' garbled)
R362 | page n/a | line 489 | NUMBER | 500 | 500 metric, 400 metric ton | T11 | 00:47:01 | ASR_DOUBT(400 MT, 1890 MT garbled)
R363 | page n/a | line 489 | NUMBER | 400 | 500 metric, 400 metric ton installed capacity | T11 | 00:47:01 | ASR_DOUBT(400 MT, 1890 MT garbled)
R364 | page n/a | line 489 | NUMBER | ton | 500 metric, 400 metric ton installed capacity out of | T11 | 00:47:01 | ASR_DOUBT(400 MT, 1890 MT garbled)
R365 | page n/a | line 489 | NUMBER | 1890 | we are currently utilize 1890 | T11 | 00:47:01 | ASR_DOUBT(400 MT, 1890 MT garbled)
R366 | page n/a | line 490 | NUMBER | ton | metric ton, 70, 80, 90 metric | T11 | 00:47:08 | ASR_DOUBT(70, 80, 90 MT)
R367 | page n/a | line 490 | NUMBER | 70 | metric ton, 70, 80, 90 metric ton | T11 | 00:47:08 | ASR_DOUBT(70, 80, 90 MT)
R368 | page n/a | line 490 | NUMBER | 80 | metric ton, 70, 80, 90 metric ton and | T11 | 00:47:08 | ASR_DOUBT(70, 80, 90 MT)
R369 | page n/a | line 490 | NUMBER | 90 | metric ton, 70, 80, 90 metric ton and our | T11 | 00:47:08 | ASR_DOUBT(70, 80, 90 MT)
R370 | page n/a | line 490 | NUMBER | ton | 70, 80, 90 metric ton and our break even | T11 | 00:47:08 | ASR_DOUBT(70, 80, 90 MT)
R371 | page n/a | line 490 | NUMBER | 120 | our break even almost 120, 130 metric ton is | T11 | 00:47:08 | ASR_DOUBT(70, 80, 90 MT)
R372 | page n/a | line 490 | NUMBER | 130 | break even almost 120, 130 metric ton is our | T11 | 00:47:08 | ASR_DOUBT(70, 80, 90 MT)
R373 | page n/a | line 490 | NUMBER | ton | almost 120, 130 metric ton is our | T11 | 00:47:08 | ASR_DOUBT(70, 80, 90 MT)
R374 | page n/a | line 491 | NUMBER | one | one will break even and | T11 | 00:47:14 | ASR_DOUBT(120, 130 MT breakeven)
R375 | page n/a | line 491 | NUMBER | 120 | we are almost adding 120 metrics and sales from | T11 | 00:47:14 | ASR_DOUBT(120, 130 MT breakeven)
R376 | page n/a | line 494 | NUMBER | two | 2020. No sir sir two things two things sir | T11 | 00:47:37 | -
R377 | page n/a | line 494 | NUMBER | two | sir sir two things two things sir we just | T11 | 00:47:37 | -
R378 | page n/a | line 494 | NUMBER | one | we just added a one plant before like two | T11 | 00:47:37 | -
R379 | page n/a | line 494 | NUMBER | two | one plant before like two months back | T11 | 00:47:37 | -
R380 | page n/a | line 496 | NUMBER | one | new capacity in next one or two months. So | T11 | 00:47:52 | -
R381 | page n/a | line 496 | NUMBER | two | in next one or two months. So it will | T11 | 00:47:52 | -
R382 | page n/a | line 500 | NUMBER | 27 | 27. But yes in between | T11 | 00:48:14 | -
R383 | page n/a | line 501 | NUMBER | three | year you had only three pinch bottom machines | T11 | 00:48:19 | -
R384 | page n/a | line 502 | NUMBER | two | the the remaining two came only in let's | T11 | 00:48:29 | -
R385 | page n/a | line 503 | NUMBER | 27 | mean the in fiscal 27 should be higher than | T11 | 00:48:36 | -
R386 | page n/a | line 504 | NUMBER | 26 | 26 this quarter due to | T11 | 00:48:44 | -
R387 | page n/a | line 510 | NUMBER | three | three machines were there pinch | T11 | 00:49:18 | -
R388 | page n/a | line 510 | NUMBER | five | third quarter you have five pinch | T11 | 00:49:18 | -
R389 | page n/a | line 512 | NUMBER | one | compare it to quarter one quarter to previous year | T11 | 00:49:28 | -
R390 | page n/a | line 513 | NUMBER | one | To quarter one to quarter one it | T11 | 00:49:33 | ASR_DOUBT(45 to 50 percent)
R391 | page n/a | line 513 | NUMBER | one | quarter one to quarter one it is almost 45 | T11 | 00:49:33 | ASR_DOUBT(45 to 50 percent)
R392 | page n/a | line 513 | NUMBER | 45 | one it is almost 45 to 50 percent increment. | T11 | 00:49:33 | ASR_DOUBT(45 to 50 percent)
R393 | page n/a | line 513 | NUMBER | 50 | is almost 45 to 50 percent increment. This quarter | T11 | 00:49:33 | ASR_DOUBT(45 to 50 percent)
R394 | page n/a | line 513 | NUMBER | percent | almost 45 to 50 percent increment. This quarter | T11 | 00:49:33 | ASR_DOUBT(45 to 50 percent)
R395 | page n/a | line 514 | NUMBER | 27-28 | that is like a 27-28 percent. Already is there | T11 | 00:49:38 | ASR_DOUBT(27-28 percent)
R396 | page n/a | line 514 | NUMBER | percent | is like a 27-28 percent. Already is there and | T11 | 00:49:38 | ASR_DOUBT(27-28 percent)
R397 | page n/a | line 517 | NUMBER | one | reflected on our quarter one and quarter two compared | T11 | 00:49:53 | -
R398 | page n/a | line 517 | NUMBER | two | quarter one and quarter two compared to previous years | T11 | 00:49:53 | -
R399 | page n/a | line 521 | NUMBER | 10 | up by, you know, 10 rupees, | T12 | 00:50:21 | ASR_DOUBT(10 rupees, 100 to 110)
R400 | page n/a | line 521 | NUMBER | rupees | by, you know, 10 rupees, | T12 | 00:50:21 | ASR_DOUBT(10 rupees, 100 to 110)
R401 | page n/a | line 522 | NUMBER | 100 | 100 to 110, you can | T12 | 00:50:27 | -
R402 | page n/a | line 522 | NUMBER | 110 | 100 to 110, you can try to | T12 | 00:50:27 | -
R403 | page n/a | line 522 | NUMBER | 10 | try to pass that 10 rupees | T12 | 00:50:27 | -
R404 | page n/a | line 522 | NUMBER | rupees | to pass that 10 rupees | T12 | 00:50:27 | -
R405 | page n/a | line 524 | NUMBER | 10 | your product prices by 10 rupees. | T12 | 00:50:34 | -
R406 | page n/a | line 524 | NUMBER | rupees | product prices by 10 rupees. | T12 | 00:50:34 | -
R407 | page n/a | line 525 | NUMBER | 10 | you margins on that 10 rupees, right? | T12 | 00:50:42 | -
R408 | page n/a | line 525 | NUMBER | rupees | margins on that 10 rupees, right? | T12 | 00:50:42 | -
R409 | page n/a | line 528 | NUMBER | One | One should look at your | T12 | 00:50:53 | -
R410 | page n/a | line 533 | NUMBER | 30 | doubt about last 30 years but this year | T12 | 00:51:19 | -
R411 | page n/a | line 533 | NUMBER | one | year what upon quarter one and quarter two | T12 | 00:51:19 | -
R412 | page n/a | line 533 | NUMBER | two | quarter one and quarter two | T12 | 00:51:19 | -
R413 | page n/a | line 534 | NUMBER | 30 | a jump like a 30 percent. I already give | T12 | 00:51:23 | ASR_DOUBT(30 percent; 92, 125, 143, 120, 160)
R414 | page n/a | line 534 | NUMBER | percent | jump like a 30 percent. I already give you | T12 | 00:51:23 | ASR_DOUBT(30 percent; 92, 125, 143, 120, 160)
R415 | page n/a | line 534 | NUMBER | 92 | a bond price is 92 then 125, | T12 | 00:51:23 | ASR_DOUBT(30 percent; 92, 125, 143, 120, 160)
R416 | page n/a | line 534 | NUMBER | 125 | price is 92 then 125, | T12 | 00:51:23 | ASR_DOUBT(30 percent; 92, 125, 143, 120, 160)
R417 | page n/a | line 535 | NUMBER | 143 | 143 then again 120 and | T12 | 00:51:30 | ASR_DOUBT(92 then 125)
R418 | page n/a | line 535 | NUMBER | 120 | 143 then again 120 and then it shoot | T12 | 00:51:30 | ASR_DOUBT(92 then 125)
R419 | page n/a | line 535 | NUMBER | 160 | it shoot up to 160. So this second first | T12 | 00:51:30 | ASR_DOUBT(92 then 125)
R420 | page n/a | line 536 | NUMBER | 120 | 120 to 160 it is | T12 | 00:51:38 | ASR_DOUBT(120 to 160; 25 percent)
R421 | page n/a | line 536 | NUMBER | 160 | 120 to 160 it is a jump | T12 | 00:51:38 | ASR_DOUBT(120 to 160; 25 percent)
R422 | page n/a | line 536 | NUMBER | 25 | a jump like a 25 percent and definitely customer | T12 | 00:51:38 | ASR_DOUBT(120 to 160; 25 percent)
R423 | page n/a | line 536 | NUMBER | percent | jump like a 25 percent and definitely customer support | T12 | 00:51:38 | ASR_DOUBT(120 to 160; 25 percent)
R424 | page n/a | line 536 | NUMBER | 120 | definitely customer support like 120 to | T12 | 00:51:38 | ASR_DOUBT(120 to 160; 25 percent)
R425 | page n/a | line 537 | NUMBER | 130 | first rate is like 130 so we close the | T12 | 00:51:46 | ASR_DOUBT(120 to 130, 130 to 145)
R426 | page n/a | line 537 | NUMBER | 130 | close the order then 130 to 145 again that | T12 | 00:51:46 | ASR_DOUBT(120 to 130, 130 to 145)
R427 | page n/a | line 537 | NUMBER | 145 | order then 130 to 145 again that is 120 | T12 | 00:51:46 | ASR_DOUBT(120 to 130, 130 to 145)
R428 | page n/a | line 537 | NUMBER | 120 | 145 again that is 120 delivery is on at | T12 | 00:51:46 | ASR_DOUBT(120 to 130, 130 to 145)
R429 | page n/a | line 538 | NUMBER | 145 | time 145 the second order delivery | T12 | 00:51:54 | ASR_DOUBT(145; 120 130 price)
R430 | page n/a | line 538 | NUMBER | 120 | order delivery is the 120 130 price it should | T12 | 00:51:54 | ASR_DOUBT(145; 120 130 price)
R431 | page n/a | line 538 | NUMBER | 130 | delivery is the 120 130 price it should be | T12 | 00:51:54 | ASR_DOUBT(145; 120 130 price)
R432 | page n/a | line 538 | NUMBER | 160 | should be on the 160 price range of | T12 | 00:51:54 | ASR_DOUBT(145; 120 130 price)
R433 | page n/a | line 540 | NUMBER | one | the production time almost one and a half month | T12 | 00:52:07 | -
R434 | page n/a | line 548 | NUMBER | kg | try to the per kg | T12 | 00:53:00 | -
R435 | page n/a | line 551 | NUMBER | kg | incremental but definitely for kg we will get it | T12 | 00:53:18 | -
R436 | page n/a | line 552 | NUMBER | five | like a five percent but we can | T12 | 00:53:25 | ASR_DOUBT(5, 3, 4 percent)
R437 | page n/a | line 552 | NUMBER | percent | like a five percent but we can get | T12 | 00:53:25 | ASR_DOUBT(5, 3, 4 percent)
R438 | page n/a | line 552 | NUMBER | three | we can get the three percent or four percent | T12 | 00:53:25 | ASR_DOUBT(5, 3, 4 percent)
R439 | page n/a | line 552 | NUMBER | percent | can get the three percent or four percent maybe | T12 | 00:53:25 | ASR_DOUBT(5, 3, 4 percent)
R440 | page n/a | line 552 | NUMBER | four | the three percent or four percent maybe possibility like | T12 | 00:53:25 | ASR_DOUBT(5, 3, 4 percent)
R441 | page n/a | line 552 | NUMBER | percent | three percent or four percent maybe possibility like | T12 | 00:53:25 | ASR_DOUBT(5, 3, 4 percent)
R442 | page n/a | line 553 | NUMBER | 25 | can increment like a 25 rupees per kg but | T12 | 00:53:30 | ASR_DOUBT(25 rupees per kg; 22 20 rupees)
R443 | page n/a | line 553 | NUMBER | rupees | increment like a 25 rupees per kg but they | T12 | 00:53:30 | ASR_DOUBT(25 rupees per kg; 22 20 rupees)
R444 | page n/a | line 553 | NUMBER | kg | a 25 rupees per kg but they may be | T12 | 00:53:30 | ASR_DOUBT(25 rupees per kg; 22 20 rupees)
R445 | page n/a | line 553 | NUMBER | 22 | negotiate and like a 22 20 rupees | T12 | 00:53:30 | ASR_DOUBT(25 rupees per kg; 22 20 rupees)
R446 | page n/a | line 553 | NUMBER | 20 | and like a 22 20 rupees | T12 | 00:53:30 | ASR_DOUBT(25 rupees per kg; 22 20 rupees)
R447 | page n/a | line 553 | NUMBER | rupees | like a 22 20 rupees | T12 | 00:53:30 | ASR_DOUBT(25 rupees per kg; 22 20 rupees)
R448 | page n/a | line 559 | NUMBER | 100% | 100% we can get it | T12 | 00:53:58 | -
R449 | page n/a | line 561 | NUMBER | double | Q1 absolute a bit double tonne say over the | T12 | 00:54:12 | -
R450 | page n/a | line 561 | NUMBER | tonne | absolute a bit double tonne say over the next | T12 | 00:54:12 | -
R451 | page n/a | line 561 | NUMBER | two | say over the next two quarters is a bit | T12 | 00:54:12 | -
R452 | page n/a | line 562 | NUMBER | double | double kg whatever whatever it | T12 | 00:54:18 | ASR_DOUBT(55 rupees vs 54; 46, 47)
R453 | page n/a | line 562 | NUMBER | kg | double kg whatever whatever it is | T12 | 00:54:18 | ASR_DOUBT(55 rupees vs 54; 46, 47)
R454 | page n/a | line 562 | NUMBER | kg | it is the per kg is a 55 rupees | T12 | 00:54:18 | ASR_DOUBT(55 rupees vs 54; 46, 47)
R455 | page n/a | line 562 | NUMBER | 55 | per kg is a 55 rupees and this much | T12 | 00:54:18 | ASR_DOUBT(55 rupees vs 54; 46, 47)
R456 | page n/a | line 562 | NUMBER | rupees | kg is a 55 rupees and this much this | T12 | 00:54:18 | ASR_DOUBT(55 rupees vs 54; 46, 47)
R457 | page n/a | line 563 | NUMBER | 46 | of 46, 47 rupees, that proximate | T12 | 00:54:24 | ASR_DOUBT(46, 47 rupees)
R458 | page n/a | line 563 | NUMBER | 47 | of 46, 47 rupees, that proximate I | T12 | 00:54:24 | ASR_DOUBT(46, 47 rupees)
R459 | page n/a | line 563 | NUMBER | rupees | of 46, 47 rupees, that proximate I am | T12 | 00:54:24 | ASR_DOUBT(46, 47 rupees)
R460 | page n/a | line 564 | NUMBER | 54 | 54. | T12 | 00:54:28 | ASR_DOUBT(54)
R461 | page n/a | line 565 | NUMBER | 54 | 54 and this is 45. | T12 | 00:54:29 | ASR_DOUBT(54 and 45)
R462 | page n/a | line 565 | NUMBER | 45 | 54 and this is 45. | T12 | 00:54:29 | ASR_DOUBT(54 and 45)
R463 | page n/a | line 566 | NUMBER | 45 | 45. | T12 | 00:54:31 | ASR_DOUBT(45)
R464 | page n/a | line 568 | NUMBER | 54 | 54 and 45. | T12 | 00:54:33 | ASR_DOUBT(54 and 45)
R465 | page n/a | line 568 | NUMBER | 45 | 54 and 45. | T12 | 00:54:33 | ASR_DOUBT(54 and 45)
R466 | page n/a | line 569 | NUMBER | 10 | 10 rupees, 54. | T12 | 00:54:34 | ASR_DOUBT(10 rupees, 54)
R467 | page n/a | line 569 | NUMBER | rupees | 10 rupees, 54. | T12 | 00:54:34 | ASR_DOUBT(10 rupees, 54)
R468 | page n/a | line 569 | NUMBER | 54 | 10 rupees, 54. | T12 | 00:54:34 | ASR_DOUBT(10 rupees, 54)
R469 | page n/a | line 570 | NUMBER | 54 | 54 can be achieved in | T12 | 00:54:35 | ASR_DOUBT(54)
R470 | page n/a | line 570 | NUMBER | two | achieved in the next two quarters you will see | T12 | 00:54:35 | ASR_DOUBT(54)
R471 | page n/a | line 573 | NUMBER | one | one person depends on the | T12 | 00:54:52 | -
R472 | page n/a | line 581 | NUMBER | 27 | So, H-1 F-1 27 was a half of | T14 | 00:55:47 | ASR_DOUBT('H-1 F-1 27')

## ENTITY (manual list, named entities as heard): R473-R521 (49 rows)
R473 | page n/a | line 41 | ENTITY | Knack Packaging Limited | reporting company; Q2 and H1 FY27 call | T01 | 00:00:00 | -
R474 | page n/a | line 46 | ENTITY | Alpish Tulsipai Patel [ASR] | Chairman and Managing Director | T01 | 00:00:28 | -
R475 | page n/a | line 47 | ENTITY | Dr. Ajay Kumar Dubey [ASR] | Chief Financial Officer | T01 | 00:00:34 | -
R476 | page n/a | line 53 | ENTITY | Dr. Ajay Kumar Gube [ASR] | CFO, variant spelling | T02 | 00:01:15 | -
R477 | page n/a | line 54 | ENTITY | Air Factor PR [ASR] | investor relations partner | T02 | 00:01:22 | -
R478 | page n/a | line 98 | ENTITY | Dr Rajesh Dubey [ASR] | CFO, variant name at hand-off | T02 | 00:06:39 | -
R479 | page n/a | line 56 | ENTITY | West Asia | conflict named as input-cost cause | T02 | 00:02:02 | -
R480 | page n/a | line 57 | ENTITY | polymer | raw material, price rose; word garbled | T02 | 00:02:09 | -
R481 | page n/a | line 58 | ENTITY | Red Sea | disruption raised freight cost | T02 | 00:02:22 | -
R482 | page n/a | line 60 | ENTITY | NAC [ASR] | company self-reference, cost pressure | T02 | 00:02:39 | -
R483 | page n/a | line 70 | ENTITY | food, fat nutrition [ASR], fertilizer | customer industries named | T02 | 00:03:47 | -
R484 | page n/a | line 70 | ENTITY | 25 plus industries | customer industry count | T02 | 00:03:47 | -
R485 | page n/a | line 81 | ENTITY | US, Europe, Asia, Africa | export regions | T02 | 00:05:08 | -
R486 | page n/a | line 79 | ENTITY | six continents | export footprint | T02 | 00:04:55 | -
R487 | page n/a | line 83 | ENTITY | SMCG [ASR], pet food, agri customers | global customer groups | T02 | 00:05:21 | -
R488 | page n/a | line 88 | ENTITY | international customer, pet food and animal nutrition | order and 3-year renewal customer | T02 | 00:05:43 | -
R489 | page n/a | line 91 | ENTITY | United States | customer location | T02 | 00:06:03 | -
R490 | page n/a | line 97 | ENTITY | SionNag TV [ASR] Mexico | JV scale-up toward break-even | T02 | 00:06:34 | -
R491 | page n/a | line 115 | ENTITY | Mexico JV [ASR 'jadeine'] | JV share of loss | T03 | 00:09:02 | -
R492 | page n/a | line 125 | ENTITY | STYM-9 JV [ASR] Mexico | JV loss in consolidated PAT | T03 | 00:10:47 | -
R493 | page n/a | line 119 | ENTITY | IPO | cause of ROE/ROC moderation | T03 | 00:10:00 | -
R494 | page n/a | line 133 | ENTITY | Bhavna Israni [ASR] | analyst, T05 | T05 | 00:11:56 | -
R495 | page n/a | line 133 | ENTITY | Ambit Asset Management | analyst firm, T05 | T05 | 00:11:56 | -
R496 | page n/a | line 178 | ENTITY | Hidansha [ASR] | analyst, T06 | T06 | 00:17:30 | -
R497 | page n/a | line 178 | ENTITY | Seven Island BMS [ASR] | analyst firm, T06 | T06 | 00:17:30 | -
R498 | page n/a | line 245 | ENTITY | Aman Chawla | analyst, T07 | T07 | 00:24:20 | -
R499 | page n/a | line 245 | ENTITY | Ash for Holdings [ASR] | analyst firm, T07 | T07 | 00:24:20 | -
R500 | page n/a | line 293 | ENTITY | BRHP [ASR] | document cited by questioner (likely offer document) | T08 | 00:30:33 | -
R501 | page n/a | line 302 | ENTITY | Patigiri [ASR] | customer, supplied | T08 | 00:31:17 | -
R502 | page n/a | line 346 | ENTITY | Mr. Soura [ASR] | participant asked to rejoin queue | T09 | 00:34:54 | -
R503 | page n/a | line 349 | ENTITY | Hitesh | analyst, T09 | T09 | 00:35:01 | -
R504 | page n/a | line 349 | ENTITY | SBI | analyst firm, T09 | T09 | 00:35:01 | -
R505 | page n/a | line 423 | ENTITY | Prakash Kapadia | analyst, T10 | T10 | 00:41:07 | -
R506 | page n/a | line 423 | ENTITY | NCRST [ASR] | analyst firm, T10 | T10 | 00:41:07 | -
R507 | page n/a | line 473 | ENTITY | Sandeep Chhabra | analyst, T11 | T11 | 00:45:42 | -
R508 | page n/a | line 473 | ENTITY | Roushi Investments [ASR] | analyst firm, T11 | T11 | 00:45:42 | -
R509 | page n/a | line 519 | ENTITY | our rigid method [ASR] | analyst, T12 (addressed 'Abhijit [ASR]' line 493) | T12 | 00:50:09 | -
R510 | page n/a | line 519 | ENTITY | INE's Alpha Investment Management [ASR] | analyst firm, T12 | T12 | 00:50:09 | -
R511 | page n/a | line 531 | ENTITY | Abhijit [ASR] | analyst name as addressed, T12 | T12 | 00:51:06 | -
R512 | page n/a | line 179 | ENTITY | pinch bottom machinery / pinch bottom bags | product and machines | T06 | 00:17:39 | -
R513 | page n/a | line 210 | ENTITY | PLWCP [ASR] bag | finish product variant | T06 | 00:21:18 | -
R514 | page n/a | line 225 | ENTITY | PRWPP/PLWPP [ASR] bag | printed laminated woven PP bag | T06 | 00:22:19 | -
R515 | page n/a | line 310 | ENTITY | PP woven bag, jute bag | earlier product generations | T08 | 00:31:55 | -
R516 | page n/a | line 299 | ENTITY | dog food industry | end-industry named | T08 | 00:31:01 | -
R517 | page n/a | line 304 | ENTITY | rice, grain and pulses, fertilizer, cement, seeds, tyre tubes | end-industries named | T08 | 00:31:27 | -
R518 | page n/a | line 335 | ENTITY | paper bags / paper pinch bottom bags | substitute product migrating | T08 | 00:34:09 | -
R519 | page n/a | line 495 | ENTITY | rented plant | capacity added about two months earlier | T11 | 00:47:45 | -
R520 | page n/a | line 590 | ENTITY | new Gujarat plant | key expansion milestone | T14 | 00:56:41 | -
R521 | page n/a | line 448 | ENTITY | securities premium | IPO expense adjusted against | T10 | 00:43:48 | -

## FORWARD (sweep tokens: will, expect, target, plan, by, ahead, commission, capex, ...): R522-R661 (140 rows)
R522 | page n/a | line 39 | FORWARD | by | Produced 2026-10-28 11:13 IST by Claude Code. Speaker names | T00 | - | -
R523 | page n/a | line 42 | FORWARD | will | reminder, all participant lines will be in the lesson | T01 | 00:00:06 | -
R524 | page n/a | line 42 | FORWARD | will | only mode and there will be an | T01 | 00:00:06 | -
R525 | page n/a | line 44 | FORWARD | by | please signal an operator by pressing star then zero | T01 | 00:00:18 | -
R526 | page n/a | line 45 | FORWARD | by | senior management team led by our chairman | T01 | 00:00:22 | -
R527 | page n/a | line 47 | FORWARD | will | Ajay Kumar Dubey, who will share his perspective on | T01 | 00:00:34 | -
R528 | page n/a | line 49 | FORWARD | would | Before we begin, I would like to remind everyone | T01 | 00:00:42 | -
R529 | page n/a | line 53 | FORWARD | by | call, I am joined by Dr. Ajay Kumar Gube, | T02 | 00:01:15 | -
R530 | page n/a | line 60 | FORWARD | by | revision. NAC was impacted by this industry-wide cost pressure. | T02 | 00:02:39 | -
R531 | page n/a | line 66 | FORWARD | expect | cost pass-through and we expect this to reflect in | T02 | 00:03:18 | -
R532 | page n/a | line 68 | FORWARD | ahead | the industry, our growth ahead lies in our competitive | T02 | 00:03:33 | -
R533 | page n/a | line 82 | FORWARD | by | line growth was driven by significantly higher export volume, | T02 | 00:05:14 | -
R534 | page n/a | line 86 | FORWARD | ahead | orders from new customers ahead of our next phase | T02 | 00:05:36 | -
R535 | page n/a | line 93 | FORWARD | ahead | Looking ahead to the rest of | T02 | 00:06:10 | -
R536 | page n/a | line 93 | FORWARD | will | of FY27, our focus will be on profitable growth. | T02 | 00:06:10 | -
R537 | page n/a | line 95 | FORWARD | by | to improve it further by increasing the share of | T02 | 00:06:22 | -
R538 | page n/a | line 98 | FORWARD | will | more stronger. Now, I will hand over to Dr | T02 | 00:06:39 | -
R539 | page n/a | line 98 | FORWARD | will | Dubey, our CFO, who will provide | T02 | 00:06:39 | -
R540 | page n/a | line 100 | FORWARD | will | everyone. I will now walk through our | T03 | 00:06:56 | -
R541 | page n/a | line 103 | FORWARD | by | This growth was driven by the significantly higher export | T03 | 00:07:30 | -
R542 | page n/a | line 114 | FORWARD | by | beta pad was affected by 2.62 crores | T03 | 00:08:54 | -
R543 | page n/a | line 119 | FORWARD | expected | ROE and ROC was expected outcome of the IPO, | T03 | 00:10:00 | -
R544 | page n/a | line 120 | FORWARD | expected | which expected to capital based. The | T03 | 00:10:10 | -
R545 | page n/a | line 121 | FORWARD | expected | initiation. Both ratio were expected to improve in the | T03 | 00:10:17 | -
R546 | page n/a | line 127 | FORWARD | will | 3.1, this price will reverse the support of | T03 | 00:11:02 | -
R547 | page n/a | line 132 | FORWARD | will | Ladies and gentlemen, we will wait for a moment | T04 | 00:11:51 | -
R548 | page n/a | line 133 | FORWARD | ahead | Asset Management. Please go ahead. | T05 | 00:11:56 | -
R549 | page n/a | line 141 | FORWARD | going to | how the volume is going to be in coming | T05 | 00:12:54 | -
R550 | page n/a | line 143 | FORWARD | expecting | up and we are expecting for almost new capacity | T05 | 00:13:08 | -
R551 | page n/a | line 144 | FORWARD | expecting | So, we are expecting quarter, quarter three financial | T05 | 00:13:16 | -
R552 | page n/a | line 144 | FORWARD | would | three financial year that would be better in terms | T05 | 00:13:16 | -
R553 | page n/a | line 148 | FORWARD | planning | how much we are planning to take in Q3 | T05 | 00:13:36 | -
R554 | page n/a | line 150 | FORWARD | expecting | we are expecting in Q3? | T05 | 00:13:46 | -
R555 | page n/a | line 159 | FORWARD | would | are affecting in market would be stabilized and things | T05 | 00:14:33 | -
R556 | page n/a | line 159 | FORWARD | would | be stabilized and things would be in line. | T05 | 00:14:33 | -
R557 | page n/a | line 164 | FORWARD | would | 27 is 11,252 what would be the same number | T05 | 00:15:14 | -
R558 | page n/a | line 171 | FORWARD | by | per kg is declined by roughly 10 rupees, | T05 | 00:16:34 | -
R559 | page n/a | line 172 | FORWARD | by | ebita bulkage is round by roughly 60 rupees per | T05 | 00:16:41 | -
R560 | page n/a | line 176 | FORWARD | will | will give the price per | T05 | 00:17:05 | -
R561 | page n/a | line 178 | FORWARD | ahead | Island BMS. Please go ahead. Hello, I'm all right. | T06 | 00:17:30 | -
R562 | page n/a | line 183 | FORWARD | will | will take like a 4 | T06 | 00:18:09 | -
R563 | page n/a | line 185 | FORWARD | will | back and also we will continuously process on that | T06 | 00:18:18 | -
R564 | page n/a | line 196 | FORWARD | will | exactly quantity wise we will update you on those. | T06 | 00:19:34 | -
R565 | page n/a | line 199 | FORWARD | expecting | continuously. So we are expecting | T06 | 00:20:00 | -
R566 | page n/a | line 200 | FORWARD | would | the quarter through three would be more commercial, more | T06 | 00:20:08 | -
R567 | page n/a | line 202 | FORWARD | expecting | third quarter we are expecting much more utilization of | T06 | 00:20:21 | -
R568 | page n/a | line 203 | FORWARD | will | rice industry and we will get the good order | T06 | 00:20:27 | -
R569 | page n/a | line 212 | FORWARD | will | one hour production capacity will be increased because today | T06 | 00:21:33 | -
R570 | page n/a | line 214 | FORWARD | would | bottom would be more utilization. So | T06 | 00:21:46 | -
R571 | page n/a | line 216 | FORWARD | will | Sir, I will give you just one | T06 | 00:21:57 | -
R572 | page n/a | line 229 | FORWARD | will | then new facilities will add around 30,000 to | T06 | 00:22:46 | -
R573 | page n/a | line 230 | FORWARD | will | of how much output will be from pinch bottom | T06 | 00:22:52 | -
R574 | page n/a | line 231 | FORWARD | will | will be from the normal | T06 | 00:22:58 | -
R575 | page n/a | line 236 | FORWARD | will | two new pinch machines will come up because that | T06 | 00:23:23 | -
R576 | page n/a | line 237 | FORWARD | next year | So, next year, October, our target | T06 | 00:23:29 | -
R577 | page n/a | line 237 | FORWARD | target | next year, October, our target credit will come up | T06 | 00:23:29 | -
R578 | page n/a | line 237 | FORWARD | will | October, our target credit will come up into the | T06 | 00:23:29 | -
R579 | page n/a | line 245 | FORWARD | ahead | for Holdings, please go ahead. | T07 | 00:24:20 | -
R580 | page n/a | line 248 | FORWARD | by | by gross margin impact. So | T07 | 00:24:42 | -
R581 | page n/a | line 256 | FORWARD | will | is taken, now season will start | T07 | 00:25:33 | -
R582 | page n/a | line 258 | FORWARD | will | what at work order will come 10 times every | T07 | 00:25:47 | -
R583 | page n/a | line 262 | FORWARD | ahead | so. Sir please go ahead we are unable to | T07 | 00:26:15 | -
R584 | page n/a | line 277 | FORWARD | will | No, non-contracture first I will cover with the | T07 | 00:28:30 | -
R585 | page n/a | line 285 | FORWARD | will | order price and it will be delivered after one | T07 | 00:29:18 | -
R586 | page n/a | line 292 | FORWARD | will | at that time, it will be the start the | T07 | 00:29:55 | -
R587 | page n/a | line 292 | FORWARD | will | the production and it will be take the one | T07 | 00:29:55 | -
R588 | page n/a | line 294 | FORWARD | going to | So how are we going to manage the same? | T08 | 00:30:42 | -
R589 | page n/a | line 295 | FORWARD | will | first of all, I will explain about the demand. | T08 | 00:30:46 | -
R590 | page n/a | line 299 | FORWARD | will | like I will say the one example, | T08 | 00:31:01 | -
R591 | page n/a | line 312 | FORWARD | target | bags we directly target that customer those who | T08 | 00:32:08 | -
R592 | page n/a | line 322 | FORWARD | will | we will get the but we | T08 | 00:32:54 | -
R593 | page n/a | line 322 | FORWARD | will | get the but we will challenge accept talent and | T08 | 00:32:54 | -
R594 | page n/a | line 326 | FORWARD | will | at that time customer will happy to give them | T08 | 00:33:16 | -
R595 | page n/a | line 332 | FORWARD | will | mentioned seven reason customer will want join us. They | T08 | 00:33:49 | -
R596 | page n/a | line 333 | FORWARD | planning | that's how we are planning to expand our capacity | T08 | 00:33:55 | -
R597 | page n/a | line 350 | FORWARD | ahead | Please go ahead. | T09 | 00:35:04 | -
R598 | page n/a | line 356 | FORWARD | will | Q2 volume, just I will let you know the | T09 | 00:35:23 | -
R599 | page n/a | line 356 | FORWARD | by | it is the increase by 3%, 11,252%. | T09 | 00:35:23 | -
R600 | page n/a | line 368 | FORWARD | going to | you said like you're going to | T09 | 00:36:10 | -
R601 | page n/a | line 369 | FORWARD | going to | tag and that is going to mitigate the you | T09 | 00:36:16 | -
R602 | page n/a | line 371 | FORWARD | will | previous quarters will to that level with | T09 | 00:36:29 | -
R603 | page n/a | line 371 | FORWARD | will | price high or it will | T09 | 00:36:29 | -
R604 | page n/a | line 373 | FORWARD | will | across margin will normalize in Q4. | T09 | 00:36:40 | -
R605 | page n/a | line 380 | FORWARD | expecting | that is we are expecting and that is the | T09 | 00:37:17 | -
R606 | page n/a | line 381 | FORWARD | will | season will start right now already | T09 | 00:37:22 | -
R607 | page n/a | line 384 | FORWARD | expected | we have very good expected like the quarter one | T09 | 00:37:38 | -
R608 | page n/a | line 385 | FORWARD | will | So the Q3 will see a significant recovery | T09 | 00:37:45 | -
R609 | page n/a | line 385 | FORWARD | will | in Q2 may we will recover in Q3 right? | T09 | 00:37:45 | -
R610 | page n/a | line 388 | FORWARD | will | price like I will give you the polymer | T09 | 00:38:07 | -
R611 | page n/a | line 388 | FORWARD | will | the war then it will be the reach | T09 | 00:38:07 | -
R612 | page n/a | line 394 | FORWARD | expectation | have a very good expectation. But there is a | T09 | 00:38:47 | -
R613 | page n/a | line 394 | FORWARD | will | a one percent, I will tell you, | T09 | 00:38:47 | -
R614 | page n/a | line 416 | FORWARD | expectation | have a very good expectation from them so | T09 | 00:40:31 | -
R615 | page n/a | line 421 | FORWARD | would | from all participants. We would request you to please | T10 | 00:40:56 | -
R616 | page n/a | line 423 | FORWARD | ahead | from NCRST. Please go ahead. | T10 | 00:41:07 | -
R617 | page n/a | line 432 | FORWARD | would | asset terms and margins would be similar in | T10 | 00:42:05 | -
R618 | page n/a | line 433 | FORWARD | next year | Mexico and next year what would be | T10 | 00:42:11 | -
R619 | page n/a | line 433 | FORWARD | would | and next year what would be our capacity by | T10 | 00:42:11 | -
R620 | page n/a | line 433 | FORWARD | by | would be our capacity by next October those are | T10 | 00:42:11 | -
R621 | page n/a | line 442 | FORWARD | going to | is going to down. There was | T10 | 00:43:09 | -
R622 | page n/a | line 454 | FORWARD | expecting | quarter three we are expecting | T10 | 00:44:27 | -
R623 | page n/a | line 456 | FORWARD | targeted | four is our targeted to achieve this win-win | T10 | 00:44:38 | -
R624 | page n/a | line 457 | FORWARD | expecting | quarter three we are expecting to the good level | T10 | 00:44:45 | -
R625 | page n/a | line 460 | FORWARD | expecting | and we are also expecting to quarter three is | T10 | 00:45:01 | -
R626 | page n/a | line 463 | FORWARD | expecting | this quarter we are expecting | T10 | 00:45:13 | -
R627 | page n/a | line 464 | FORWARD | by | tons is the near by the breakeven over this | T10 | 00:45:19 | -
R628 | page n/a | line 465 | FORWARD | expecting | So we are expecting this next quarter will | T10 | 00:45:27 | -
R629 | page n/a | line 465 | FORWARD | will | expecting this next quarter will be the windy situation. | T10 | 00:45:27 | -
R630 | page n/a | line 467 | FORWARD | will | I will come back if I | T10 | 00:45:34 | -
R631 | page n/a | line 474 | FORWARD | ahead | Please go ahead. | T11 | 00:45:45 | -
R632 | page n/a | line 476 | FORWARD | will | that has been lost will be | T11 | 00:45:52 | -
R633 | page n/a | line 477 | FORWARD | will | from third quarter there will be an improvement. | T11 | 00:46:02 | -
R634 | page n/a | line 479 | FORWARD | will | the third quarter will be the winning situation | T11 | 00:46:11 | -
R635 | page n/a | line 479 | FORWARD | expecting | than that we are expecting little | T11 | 00:46:11 | -
R636 | page n/a | line 483 | FORWARD | expecting | were expecting a good margin on | T11 | 00:46:30 | -
R637 | page n/a | line 487 | FORWARD | expected | much more as we expected. | T11 | 00:46:52 | -
R638 | page n/a | line 491 | FORWARD | will | one will break even and so | T11 | 00:47:14 | -
R639 | page n/a | line 493 | FORWARD | will | October 2027 any capacity will get added or everything | T11 | 00:47:31 | -
R640 | page n/a | line 493 | FORWARD | will | get added or everything will happen only in October | T11 | 00:47:31 | -
R641 | page n/a | line 496 | FORWARD | will | two months. So it will be give a little | T11 | 00:47:52 | -
R642 | page n/a | line 520 | FORWARD | ahead | Management. Please go ahead. Yeah, thanks for taking | T12 | 00:50:15 | -
R643 | page n/a | line 521 | FORWARD | by | material prices moves up by, you know, 10 rupees, | T12 | 00:50:21 | -
R644 | page n/a | line 524 | FORWARD | by | increase your product prices by 10 rupees. | T12 | 00:50:34 | -
R645 | page n/a | line 527 | FORWARD | will | will look lower as this | T12 | 00:50:48 | -
R646 | page n/a | line 540 | FORWARD | will | everything but yes it will be the production time | T12 | 00:52:07 | -
R647 | page n/a | line 541 | FORWARD | will | yes later on it will be the good things | T12 | 00:52:14 | -
R648 | page n/a | line 545 | FORWARD | expect | but to sort of expect percentage margins to come | T12 | 00:52:41 | -
R649 | page n/a | line 547 | FORWARD | will | no on that I will very honestly tell you | T12 | 00:52:53 | -
R650 | page n/a | line 551 | FORWARD | will | definitely for kg we will get it so yes | T12 | 00:53:18 | -
R651 | page n/a | line 555 | FORWARD | will | normal price like I will give you the petrol | T12 | 00:53:40 | -
R652 | page n/a | line 570 | FORWARD | will | next two quarters you will see as in you | T12 | 00:54:35 | -
R653 | page n/a | line 577 | FORWARD | target | down but here our target is we are on | T12 | 00:55:16 | -
R654 | page n/a | line 579 | FORWARD | will | time constraints that we will take that as the | T13 | 00:55:29 | -
R655 | page n/a | line 585 | FORWARD | ahead | a key advantage, looking ahead | T14 | 00:56:10 | -
R656 | page n/a | line 586 | FORWARD | expect | Q3 and Q4 we expect volume group to continue | T14 | 00:56:16 | -
R657 | page n/a | line 586 | FORWARD | by | group to continue supported by the ramp up of | T14 | 00:56:16 | -
R658 | page n/a | line 588 | FORWARD | expect | We also expect margin to recover from | T14 | 00:56:27 | -
R659 | page n/a | line 589 | FORWARD | will | We will remain cautious on the | T14 | 00:56:34 | -
R660 | page n/a | line 589 | FORWARD | plan | deployment. The new Gujarat plan remains a key | T14 | 00:56:34 | -
R661 | page n/a | line 590 | FORWARD | will | timely completion and utilization will be primarily focused through | T14 | 00:56:41 | -

## FORWARD-STATEMENT (statement-level rows, manual): R662-R693 (32 rows)
R662 | page n/a | line 66 | FORWARD | already revised prices, expect this to reflect in realization from quarter 3 FY27 onwards subject to market stabilization | forward statement (statement-level) | T02 | 00:03:18 | -
R663 | page n/a | line 93 | FORWARD | rest of FY27 focus on profitable growth; restore EBITDA margin as pricing adjustments flow through from Q3 FY27 | forward statement (statement-level) | T02 | 00:06:10 | -
R664 | page n/a | line 95 | FORWARD | improve margin further by raising share of value added products, controlling costs, leveraging integrated setup | forward statement (statement-level) | T02 | 00:06:22 | -
R665 | page n/a | line 97 | FORWARD | scaling up Mexico JV towards break-even; building order book stronger | forward statement (statement-level) | T02 | 00:06:34 | -
R666 | page n/a | line 110 | FORWARD | expect margin to recover from quarter 3, financial year 27 | forward statement (statement-level) | T03 | 00:08:19 | -
R667 | page n/a | line 120 | FORWARD | ROE and ROC expected to improve in coming quarters as IPO funds deployed | forward statement (statement-level) | T03 | 00:10:10 | -
R668 | page n/a | line 127 | FORWARD | JV reaching [ASR] breakeven will reverse support to consolidated margin | forward statement (statement-level) | T03 | 00:11:02 | -
R669 | page n/a | line 142 | FORWARD | new capacity added August (5,040 [ASR]); plant ramping up; quarter 3 expected better in quantity, production, sale | forward statement (statement-level) | T05 | 00:12:59 | -
R670 | page n/a | line 158 | FORWARD | price pass-through reflects in quarter three majorly if market stabilised | forward statement (statement-level) | T05 | 00:14:27 | -
R671 | page n/a | line 199 | FORWARD | quarter three expected more commercial sale of pinch bottom, increasing utilisation | forward statement (statement-level) | T06 | 00:20:00 | -
R672 | page n/a | line 202 | FORWARD | third quarter expected much more pinch bottom use in rice industry, good orders | forward statement (statement-level) | T06 | 00:20:21 | -
R673 | page n/a | line 234 | FORWARD | after expansion capacity reaches 69 to 72,000 MT [ASR] | forward statement (statement-level) | T06 | 00:23:13 | -
R674 | page n/a | line 237 | FORWARD | two new pinch machines: target to come into production next year October | forward statement (statement-level) | T06 | 00:23:29 | -
R675 | page n/a | line 241 | FORWARD | pinch bottom to reach 25,000 to 30,000 of 72,000 [ASR] capacity later on 28 [ASR] | forward statement (statement-level) | T06 | 00:23:52 | -
R676 | page n/a | line 374 | FORWARD | Q3 and Q4 better in quantity and margin as always | forward statement (statement-level) | T09 | 00:36:42 | -
R677 | page n/a | line 384 | FORWARD | good expectation for quarter three and quarter four | forward statement (statement-level) | T09 | 00:37:38 | -
R678 | page n/a | line 385 | FORWARD | Q3 expected to see significant recovery in gross margin (analyst question; reply line 348) | forward statement (statement-level) | T09 | 00:37:45 | -
R679 | page n/a | line 479 | FORWARD | third quarter winning situation; little bit of loss also covered | forward statement (statement-level) | T11 | 00:46:11 | -
R680 | page n/a | line 454 | FORWARD | Mexico: Q3 almost achieve break-even; Q4 targeted 'not very committed' | forward statement (statement-level) | T10 | 00:44:27 | -
R681 | page n/a | line 463 | FORWARD | Mexico: expecting 120 MT this quarter, near breakeven; next quarter winning situation | forward statement (statement-level) | T10 | 00:45:13 | -
R682 | page n/a | line 485 | FORWARD | Q3 comes with loss recovery of very small portion | forward statement (statement-level) | T11 | 00:46:44 | -
R683 | page n/a | line 496 | FORWARD | new capacity from rented plant in next one or two months | forward statement (statement-level) | T11 | 00:47:52 | -
R684 | page n/a | line 499 | FORWARD | expansion capacity deadline October 2027 [ASR 'October 27'] | forward statement (statement-level) | T11 | 00:48:09 | -
R685 | page n/a | line 570 | FORWARD | per kg 54 [ASR] can be achieved in next two quarters | forward statement (statement-level) | T12 | 00:54:35 | -
R686 | page n/a | line 575 | FORWARD | yearly target achievable, on track | forward statement (statement-level) | T12 | 00:55:02 | -
R687 | page n/a | line 586 | FORWARD | Q3 and Q4 volume growth to continue supported by ramp up of contracted orders incl. renewed international contract and higher wallet share | forward statement (statement-level) | T14 | 00:56:16 | -
R688 | page n/a | line 588 | FORWARD | expect margin to recover from Q3 FY27 onwards as pricing adjustments flow through | forward statement (statement-level) | T14 | 00:56:27 | -
R689 | page n/a | line 589 | FORWARD | new Gujarat plant key milestone, timely completion and utilisation primary focus through 2027 | forward statement (statement-level) | T14 | 00:56:34 | -
R690 | page n/a | line 592 | FORWARD | update again next quarter | forward statement (statement-level) | T14 | 00:56:53 | -
R691 | page n/a | line 413 | FORWARD | contract customer can add more countries and varieties into portfolio; paper bags shifting to portfolio | forward statement (statement-level) | T09 | 00:40:14 | -
R692 | page n/a | line 333 | FORWARD | planning to expand capacity | forward statement (statement-level) | T08 | 00:33:55 | -
R693 | page n/a | line 137 | FORWARD | current plant utilisation about 90-91% (statement of present state, captured for continuity) | forward statement (statement-level) | T05 | 00:12:20 | -

## DATE (sweep: months, years, Q/H/FY labels, quarter, half, financial year): R694-R909 (216 rows)
R694 | page n/a | line 39 | DATE | 2026-10-28 | chunks, VAD on. Produced 2026-10-28 11:13 IST by Claude | T00 | - | -
R695 | page n/a | line 41 | DATE | Q2 | and welcome to the Q2 and H1 FY27 conference | T01 | 00:00:00 | -
R696 | page n/a | line 41 | DATE | H1 | to the Q2 and H1 FY27 conference call of | T01 | 00:00:00 | -
R697 | page n/a | line 41 | DATE | FY27 | the Q2 and H1 FY27 conference call of Knack | T01 | 00:00:00 | -
R698 | page n/a | line 47 | DATE | quarter | company's performance for the quarter | T01 | 00:00:34 | -
R699 | page n/a | line 54 | DATE | quarter | investor relations partner in quarter to FY22 percentage all | T02 | 00:01:22 | -
R700 | page n/a | line 54 | DATE | FY22 | partner in quarter to FY22 percentage all on | T02 | 00:01:22 | -
R701 | page n/a | line 55 | DATE | half | the industry, the first half of the year was | T02 | 00:01:55 | -
R702 | page n/a | line 63 | DATE | quarter | margin was impacted in quarter 2, F527. | T02 | 00:02:58 | -
R703 | page n/a | line 63 | DATE | F527 | impacted in quarter 2, F527. | T02 | 00:02:58 | ASR_DOUBT(fiscal label garbled)
R704 | page n/a | line 67 | DATE | quarter | quarter 3 FI27 onwards subject | T02 | 00:03:25 | -
R705 | page n/a | line 67 | DATE | FI27 | quarter 3 FI27 onwards subject to market | T02 | 00:03:25 | ASR_DOUBT(fiscal label garbled)
R706 | page n/a | line 76 | DATE | September | As on September 30, 2026, we sought | T02 | 00:04:27 | -
R707 | page n/a | line 76 | DATE | 2026 | As on September 30, 2026, we sought more than | T02 | 00:04:27 | -
R708 | page n/a | line 77 | DATE | quarter | at the end of quarter one financial year 27. | T02 | 00:04:39 | -
R709 | page n/a | line 77 | DATE | financial year | end of quarter one financial year 27. | T02 | 00:04:39 | ASR_DOUBT(fiscal label garbled)
R710 | page n/a | line 78 | DATE | half | our revenue during the half as of | T02 | 00:04:47 | -
R711 | page n/a | line 79 | DATE | September | September 2026 and we sold | T02 | 00:04:55 | -
R712 | page n/a | line 79 | DATE | 2026 | September 2026 and we sold to | T02 | 00:04:55 | -
R713 | page n/a | line 80 | DATE | quarter | at the end of quarter 1, FY27 and 71 | T02 | 00:05:02 | -
R714 | page n/a | line 80 | DATE | FY27 | end of quarter 1, FY27 and 71 countries in | T02 | 00:05:02 | -
R715 | page n/a | line 80 | DATE | FY26 | and 71 countries in FY26. | T02 | 00:05:02 | -
R716 | page n/a | line 82 | DATE | H1-FI27 | According to H1-FI27, our top line growth | T02 | 00:05:14 | ASR_DOUBT(fiscal label garbled)
R717 | page n/a | line 88 | DATE | October | recent update on 2nd October 2026, we announced a | T02 | 00:05:43 | -
R718 | page n/a | line 88 | DATE | 2026 | update on 2nd October 2026, we announced a new | T02 | 00:05:43 | -
R719 | page n/a | line 93 | DATE | FY27 | to the rest of FY27, our focus will be | T02 | 00:06:10 | -
R720 | page n/a | line 94 | DATE | Q3 | adjustments flow through from Q3 | T02 | 00:06:16 | -
R721 | page n/a | line 95 | DATE | FY27 | FY27 and then to improve | T02 | 00:06:22 | -
R722 | page n/a | line 99 | DATE | quarter | detailed financial highlights for quarter 2 and H1 F5-27. | T03 | 00:06:47 | -
R723 | page n/a | line 99 | DATE | H1 | for quarter 2 and H1 F5-27. Thank you, sir. | T03 | 00:06:47 | -
R724 | page n/a | line 99 | DATE | F5-27 | quarter 2 and H1 F5-27. Thank you, sir. Good | T03 | 00:06:47 | ASR_DOUBT(fiscal label garbled)
R725 | page n/a | line 100 | DATE | quarter | consolidated financial performance for quarter 2, financial | T03 | 00:06:56 | -
R726 | page n/a | line 101 | DATE | H-1 | and H-1 Peninsula 27, Thomas 27, | T03 | 00:07:04 | ASR_DOUBT(fiscal label garbled)
R727 | page n/a | line 102 | DATE | quarter | the 193.26 crores in quarter 2 Peninsula 26, a | T03 | 00:07:19 | -
R728 | page n/a | line 105 | DATE | quarter | margin our Ibita for quarter to | T03 | 00:07:39 | -
R729 | page n/a | line 106 | DATE | financial year | financial year 27 was 49.77 | T03 | 00:07:46 | ASR_DOUBT(fiscal label garbled)
R730 | page n/a | line 106 | DATE | quarter | with 38.30 gross in quarter to | T03 | 00:07:46 | -
R731 | page n/a | line 107 | DATE | financial year | financial year 26 of 29.9 | T03 | 00:07:54 | ASR_DOUBT(fiscal label garbled)
R732 | page n/a | line 111 | DATE | quarter | to recover is from quarter 3, financial year 27. | T03 | 00:08:26 | -
R733 | page n/a | line 111 | DATE | financial year | is from quarter 3, financial year 27. About the | T03 | 00:08:26 | ASR_DOUBT(fiscal label garbled)
R734 | page n/a | line 112 | DATE | quarter | tax for quarter 2, financial year 27 | T03 | 00:08:34 | -
R735 | page n/a | line 112 | DATE | financial year | tax for quarter 2, financial year 27 was 25.02 | T03 | 00:08:34 | ASR_DOUBT(fiscal label garbled)
R736 | page n/a | line 112 | DATE | quarter | versus 20.64 crores in quarter 2, financial | T03 | 00:08:34 | -
R737 | page n/a | line 113 | DATE | quarter | the pack margin for quarter was 8.22% compared with | T03 | 00:08:43 | -
R738 | page n/a | line 115 | DATE | quarter | loss of Mexico jadeine quarter 2 which I explained | T03 | 00:09:02 | -
R739 | page n/a | line 115 | DATE | half | I explained in the half year numbers | T03 | 00:09:02 | -
R740 | page n/a | line 116 | DATE | quarter | basis EES of the quarter was 2.07. So now | T03 | 00:09:08 | -
R741 | page n/a | line 116 | DATE | H1 | was 2.07. So now H1 performance I'll just take | T03 | 00:09:08 | -
R742 | page n/a | line 116 | DATE | H1 | I'll just take off H1 | T03 | 00:09:08 | -
R743 | page n/a | line 121 | DATE | quarters | improve in the coming quarters. About the | T03 | 00:10:17 | -
R744 | page n/a | line 122 | DATE | H-1 | profit after tax for H-1 Peninsula F-1T, 7 was | T03 | 00:10:23 | ASR_DOUBT(fiscal label garbled)
R745 | page n/a | line 122 | DATE | F-1T | tax for H-1 Peninsula F-1T, 7 was 55.55 crores | T03 | 00:10:23 | ASR_DOUBT(fiscal label garbled)
R746 | page n/a | line 123 | DATE | H-1 | crores in H-1 Peninsula F-1T, up 34.5 | T03 | 00:10:32 | ASR_DOUBT(fiscal label garbled)
R747 | page n/a | line 123 | DATE | F-1T | crores in H-1 Peninsula F-1T, up 34.5 percent. | T03 | 00:10:32 | ASR_DOUBT(fiscal label garbled)
R748 | page n/a | line 124 | DATE | H-1 | against 10.68 percent in H-1 Peninsula F-1T, PAD par | T03 | 00:10:37 | ASR_DOUBT(fiscal label garbled)
R749 | page n/a | line 124 | DATE | F-1T | percent in H-1 Peninsula F-1T, PAD par half | T03 | 00:10:37 | ASR_DOUBT(fiscal label garbled)
R750 | page n/a | line 124 | DATE | half | Peninsula F-1T, PAD par half | T03 | 00:10:37 | -
R751 | page n/a | line 137 | DATE | quarter | quarter and what is our | T05 | 00:12:20 | -
R752 | page n/a | line 137 | DATE | quarter | So basically in last quarter we have closed | T05 | 00:12:20 | -
R753 | page n/a | line 138 | DATE | quarter | and this quarter we closed 11,252 which | T05 | 00:12:27 | -
R754 | page n/a | line 138 | DATE | quarter | 3% growth from the quarter. Basically our | T05 | 00:12:27 | -
R755 | page n/a | line 141 | DATE | quarters | to be in coming quarters? | T05 | 00:12:54 | -
R756 | page n/a | line 142 | DATE | August | quantity in month of August only and the plant | T05 | 00:12:59 | -
R757 | page n/a | line 144 | DATE | quarter | So, we are expecting quarter, quarter three financial year | T05 | 00:13:16 | -
R758 | page n/a | line 144 | DATE | quarter | we are expecting quarter, quarter three financial year that | T05 | 00:13:16 | -
R759 | page n/a | line 144 | DATE | financial year | expecting quarter, quarter three financial year that would be | T05 | 00:13:16 | ASR_DOUBT(fiscal label garbled)
R760 | page n/a | line 147 | DATE | Q2 | we have taken in Q2 | T05 | 00:13:30 | -
R761 | page n/a | line 148 | DATE | Q3 | planning to take in Q3 as we said, there | T05 | 00:13:36 | -
R762 | page n/a | line 149 | DATE | quarter | and there is a quarter led in price person, | T05 | 00:13:40 | -
R763 | page n/a | line 150 | DATE | Q3 | we are expecting in Q3? | T05 | 00:13:46 | -
R764 | page n/a | line 155 | DATE | quarter | can say only the quarter to in initial of | T05 | 00:14:12 | -
R765 | page n/a | line 155 | DATE | quarter | in initial of the quarter and | T05 | 00:14:12 | -
R766 | page n/a | line 156 | DATE | quarter | ending of the quarter there is almost 26% | T05 | 00:14:18 | -
R767 | page n/a | line 159 | DATE | quarter | Reflect in the quarter three majorly and we | T05 | 00:14:33 | -
R768 | page n/a | line 161 | DATE | half | one one and a half month for the delivery | T05 | 00:14:56 | -
R769 | page n/a | line 162 | DATE | quarter | have in the last quarter we deliver in this | T05 | 00:15:02 | -
R770 | page n/a | line 162 | DATE | quarter | we deliver in this quarter and this quarter price | T05 | 00:15:02 | -
R771 | page n/a | line 162 | DATE | quarter | this quarter and this quarter price | T05 | 00:15:02 | -
R772 | page n/a | line 164 | DATE | Q1 | 15 Q1 F5 27 Q2 F5 | T05 | 00:15:14 | -
R773 | page n/a | line 164 | DATE | F5 | 15 Q1 F5 27 Q2 F5 27 | T05 | 00:15:14 | ASR_DOUBT(fiscal label garbled)
R774 | page n/a | line 164 | DATE | Q2 | 15 Q1 F5 27 Q2 F5 27 is 11,252 | T05 | 00:15:14 | -
R775 | page n/a | line 164 | DATE | F5 | Q1 F5 27 Q2 F5 27 is 11,252 what | T05 | 00:15:14 | ASR_DOUBT(fiscal label garbled)
R776 | page n/a | line 164 | DATE | quarter | the same number last quarter last year | T05 | 00:15:14 | -
R777 | page n/a | line 165 | DATE | quarter | Do you see in quarter Q2 as per 26? | T05 | 00:15:51 | -
R778 | page n/a | line 165 | DATE | Q2 | you see in quarter Q2 as per 26? | T05 | 00:15:51 | -
R779 | page n/a | line 167 | DATE | quarter | we dropped 3 at quarter Q2. | T05 | 00:16:05 | -
R780 | page n/a | line 167 | DATE | Q2 | dropped 3 at quarter Q2. | T05 | 00:16:05 | -
R781 | page n/a | line 169 | DATE | quarter | From quarter to the rain but | T05 | 00:16:16 | -
R782 | page n/a | line 173 | DATE | quarter | 36 rupees versus last quarter we were doing at | T05 | 00:16:46 | -
R783 | page n/a | line 174 | DATE | quarter | I resist the second quarter compared to the previous | T05 | 00:16:52 | -
R784 | page n/a | line 175 | DATE | quarter | quarter. The price increment like | T05 | 00:17:00 | -
R785 | page n/a | line 176 | DATE | quarter | give the price per quarter order is delivered into | T05 | 00:17:05 | -
R786 | page n/a | line 176 | DATE | quarter | order is delivered into quarter second because there was | T05 | 00:17:05 | -
R787 | page n/a | line 177 | DATE | half | about one and a half month. Thank you. Next | T06 | 00:17:12 | -
R788 | page n/a | line 195 | DATE | quarters | last area, last two quarters. | T06 | 00:19:28 | -
R789 | page n/a | line 197 | DATE | March | and 2, most in March of 25. | T06 | 00:19:42 | -
R790 | page n/a | line 200 | DATE | quarter | the quarter through three would be | T06 | 00:20:08 | -
R791 | page n/a | line 202 | DATE | quarter | our history. So third quarter we are expecting much | T06 | 00:20:21 | -
R792 | page n/a | line 204 | DATE | quarter | per mm capacity of quarter to of pinch bottom? | T06 | 00:20:35 | -
R793 | page n/a | line 211 | DATE | quarter | in the last quarter of, fourth quarter of | T06 | 00:21:26 | -
R794 | page n/a | line 211 | DATE | quarter | last quarter of, fourth quarter of the length of | T06 | 00:21:26 | -
R795 | page n/a | line 236 | DATE | half | one, one and a half year. | T06 | 00:23:23 | -
R796 | page n/a | line 237 | DATE | October | So, next year, October, our target credit will | T06 | 00:23:29 | -
R797 | page n/a | line 253 | DATE | quarter | after that in this quarter. Yes sir, sir I | T07 | 00:25:15 | -
R798 | page n/a | line 261 | DATE | quarter | goal play in the quarter one order and deliver | T07 | 00:26:08 | -
R799 | page n/a | line 261 | DATE | quarter | and deliver into the quarter two so why in | T07 | 00:26:08 | -
R800 | page n/a | line 266 | DATE | half | one one and a half month our 50% customer | T07 | 00:27:12 | -
R801 | page n/a | line 268 | DATE | quarter | quarter order delivery to the | T07 | 00:27:24 | -
R802 | page n/a | line 268 | DATE | quarter | delivery to the second quarter. So maybe that our | T07 | 00:27:24 | -
R803 | page n/a | line 270 | DATE | quarter | quarter, we can get the | T07 | 00:27:37 | -
R804 | page n/a | line 270 | DATE | quarter | price from the second quarter. But at the time | T07 | 00:27:37 | -
R805 | page n/a | line 270 | DATE | quarter | time of the second quarter, | T07 | 00:27:37 | -
R806 | page n/a | line 279 | DATE | quarter | quarterly price like first quarter whatever | T07 | 00:28:45 | -
R807 | page n/a | line 280 | DATE | quarter | comes into the second quarter order and second price | T07 | 00:28:50 | -
R808 | page n/a | line 280 | DATE | quarter | and second price second quarter | T07 | 00:28:50 | -
R809 | page n/a | line 281 | DATE | quarter | come into the third quarter so they are increasing | T07 | 00:28:55 | -
R810 | page n/a | line 281 | DATE | quarter | they are increasing like quarter to quarter | T07 | 00:28:55 | -
R811 | page n/a | line 281 | DATE | quarter | increasing like quarter to quarter | T07 | 00:28:55 | -
R812 | page n/a | line 282 | DATE | quarter | our major customer into quarter to quarter and on | T07 | 00:29:01 | -
R813 | page n/a | line 282 | DATE | quarter | customer into quarter to quarter and on the smaller | T07 | 00:29:01 | -
R814 | page n/a | line 284 | DATE | quarter | next last month quarter price last month price | T07 | 00:29:13 | -
R815 | page n/a | line 284 | DATE | quarter | last month price not quarter last month price so | T07 | 00:29:13 | -
R816 | page n/a | line 285 | DATE | half | and one and a half months so altogether | T07 | 00:29:18 | -
R817 | page n/a | line 286 | DATE | half | and three and a half months for the one | T07 | 00:29:24 | -
R818 | page n/a | line 287 | DATE | half | and four and a half month | T07 | 00:29:29 | -
R819 | page n/a | line 327 | DATE | 2022 | using it like a 2022 rupees, | T08 | 00:33:21 | -
R820 | page n/a | line 355 | DATE | Q2 | remarks, what was the Q2 of volume 7, overall? | T09 | 00:35:14 | -
R821 | page n/a | line 356 | DATE | Q2 | Sir Q2 volume, just I will | T09 | 00:35:23 | -
R822 | page n/a | line 356 | DATE | Q1 | let you know the Q1 volume 10,940, it is | T09 | 00:35:23 | -
R823 | page n/a | line 365 | DATE | quarter | the revenue growth this quarter, right? | T09 | 00:36:03 | -
R824 | page n/a | line 371 | DATE | quarters | previous quarters will to that level | T09 | 00:36:29 | -
R825 | page n/a | line 372 | DATE | Q4 | flow to the Q4 also I mean you | T09 | 00:36:35 | -
R826 | page n/a | line 373 | DATE | Q4 | margin will normalize in Q4. | T09 | 00:36:40 | -
R827 | page n/a | line 374 | DATE | Q3 | Q3 is always Q3 and | T09 | 00:36:42 | -
R828 | page n/a | line 374 | DATE | Q3 | Q3 is always Q3 and Q4 is better | T09 | 00:36:42 | -
R829 | page n/a | line 374 | DATE | Q4 | is always Q3 and Q4 is better for always | T09 | 00:36:42 | -
R830 | page n/a | line 384 | DATE | quarter | good expected like the quarter one like kind of | T09 | 00:37:38 | -
R831 | page n/a | line 384 | DATE | quarter | kind of thing into quarter three and quarter four. | T09 | 00:37:38 | -
R832 | page n/a | line 384 | DATE | quarter | into quarter three and quarter four. | T09 | 00:37:38 | -
R833 | page n/a | line 385 | DATE | Q3 | So the Q3 will see a significant | T09 | 00:37:45 | -
R834 | page n/a | line 385 | DATE | Q2 | we have lost in Q2 may we will recover | T09 | 00:37:45 | -
R835 | page n/a | line 385 | DATE | Q3 | we will recover in Q3 right? | T09 | 00:37:45 | -
R836 | page n/a | line 394 | DATE | quarter | in the quarter, we have a very | T09 | 00:38:47 | -
R837 | page n/a | line 396 | DATE | October | in the queue in October you have received one | T09 | 00:38:56 | -
R838 | page n/a | line 425 | DATE | H1 | gap flow decrease in H1 from 39 crores to | T10 | 00:41:17 | -
R839 | page n/a | line 428 | DATE | H1 | this normalize or generally H1 you know it bunches | T10 | 00:41:40 | -
R840 | page n/a | line 428 | DATE | H2 | and buy you know H2 | T10 | 00:41:40 | -
R841 | page n/a | line 429 | DATE | H2 | you said you know H2 is generally better for | T10 | 00:41:48 | -
R842 | page n/a | line 433 | DATE | October | our capacity by next October those are my | T10 | 00:42:11 | -
R843 | page n/a | line 438 | DATE | quarters | significantly compared to previous quarters. So the receivable cycle | T10 | 00:42:42 | -
R844 | page n/a | line 441 | DATE | quarter | compared to the last quarter or compared to the | T10 | 00:43:02 | -
R845 | page n/a | line 441 | DATE | quarter | the previous year of quarter two operating cash flow | T10 | 00:43:02 | -
R846 | page n/a | line 452 | DATE | quarter | quarter so the yes definitely | T10 | 00:44:16 | -
R847 | page n/a | line 453 | DATE | quarter | as possible but last quarter it is significant better | T10 | 00:44:21 | -
R848 | page n/a | line 453 | DATE | quarter | significant better than the quarter one | T10 | 00:44:21 | -
R849 | page n/a | line 454 | DATE | quarter | good shine from the quarter two and quarter three | T10 | 00:44:27 | -
R850 | page n/a | line 454 | DATE | quarter | the quarter two and quarter three we are expecting | T10 | 00:44:27 | -
R851 | page n/a | line 455 | DATE | quarter | in our provisional week quarter | T10 | 00:44:33 | -
R852 | page n/a | line 457 | DATE | quarter | quarter three we are expecting | T10 | 00:44:45 | -
R853 | page n/a | line 460 | DATE | quarter | are also expecting to quarter three is better result | T10 | 00:45:01 | -
R854 | page n/a | line 463 | DATE | quarter | last quarter average selling all course | T10 | 00:45:13 | -
R855 | page n/a | line 463 | DATE | quarter | ton nearby and this quarter we are expecting | T10 | 00:45:13 | -
R856 | page n/a | line 465 | DATE | quarter | are expecting this next quarter will be the windy | T10 | 00:45:27 | -
R857 | page n/a | line 477 | DATE | quarter | or only from third quarter there will be an | T11 | 00:46:02 | -
R858 | page n/a | line 478 | DATE | quarter | losses in the one quarter but | T11 | 00:46:05 | -
R859 | page n/a | line 479 | DATE | quarter | the third quarter will be the winning | T11 | 00:46:11 | -
R860 | page n/a | line 483 | DATE | quarter | but first and second quarter from the green field | T11 | 00:46:30 | -
R861 | page n/a | line 486 | DATE | quarter | But yes, third quarter is definitely comes with | T11 | 00:46:47 | -
R862 | page n/a | line 492 | DATE | October | Yeah. Between now and October 2027 between now and | T11 | 00:47:19 | -
R863 | page n/a | line 492 | DATE | 2027 | Between now and October 2027 between now and | T11 | 00:47:19 | -
R864 | page n/a | line 493 | DATE | October | October 2027 any capacity will | T11 | 00:47:31 | -
R865 | page n/a | line 493 | DATE | 2027 | October 2027 any capacity will get | T11 | 00:47:31 | -
R866 | page n/a | line 493 | DATE | October | will happen only in October now in | T11 | 00:47:31 | -
R867 | page n/a | line 494 | DATE | 2020 | 2020. No sir sir two | T11 | 00:47:37 | -
R868 | page n/a | line 498 | DATE | October | and production capacity before October. | T11 | 00:48:04 | -
R869 | page n/a | line 499 | DATE | October | currently we are saying October is our deadline for | T11 | 00:48:09 | -
R870 | page n/a | line 499 | DATE | October | the expansion capacity in October | T11 | 00:48:09 | -
R871 | page n/a | line 502 | DATE | March | let's say end of March 2026. | T11 | 00:48:29 | -
R872 | page n/a | line 502 | DATE | 2026 | say end of March 2026. | T11 | 00:48:29 | -
R873 | page n/a | line 504 | DATE | quarter | 26 this quarter due to the sharp | T11 | 00:48:44 | -
R874 | page n/a | line 505 | DATE | quarter | because of the this quarter because of the sharp | T11 | 00:48:52 | -
R875 | page n/a | line 508 | DATE | quarter | I'm sorry in third quarter then third quarter margin | T11 | 00:49:09 | -
R876 | page n/a | line 508 | DATE | quarter | third quarter then third quarter margin should logically | T11 | 00:49:09 | -
R877 | page n/a | line 509 | DATE | quarter | the previous year third quarter margin because previous year | T11 | 00:49:14 | -
R878 | page n/a | line 510 | DATE | quarter | year in this third quarter you have five pinch | T11 | 00:49:18 | -
R879 | page n/a | line 512 | DATE | quarter | can compare it to quarter one quarter to previous | T11 | 00:49:28 | -
R880 | page n/a | line 512 | DATE | quarter | it to quarter one quarter to previous year to | T11 | 00:49:28 | -
R881 | page n/a | line 513 | DATE | quarter | To quarter one to quarter one | T11 | 00:49:33 | -
R882 | page n/a | line 513 | DATE | quarter | To quarter one to quarter one it is almost | T11 | 00:49:33 | -
R883 | page n/a | line 513 | DATE | quarter | 50 percent increment. This quarter | T11 | 00:49:33 | -
R884 | page n/a | line 514 | DATE | quarter | is there and third quarter | T11 | 00:49:38 | -
R885 | page n/a | line 515 | DATE | quarter | last year previous year quarter to this quarter | T11 | 00:49:44 | -
R886 | page n/a | line 515 | DATE | quarter | year quarter to this quarter | T11 | 00:49:44 | -
R887 | page n/a | line 517 | DATE | quarter | a reflected on our quarter one and quarter two | T11 | 00:49:53 | -
R888 | page n/a | line 517 | DATE | quarter | our quarter one and quarter two compared to previous | T11 | 00:49:53 | -
R889 | page n/a | line 533 | DATE | quarter | this year what upon quarter one and quarter two | T12 | 00:51:19 | -
R890 | page n/a | line 533 | DATE | quarter | upon quarter one and quarter two | T12 | 00:51:19 | -
R891 | page n/a | line 535 | DATE | quarter | So this second first quarter to second quarter | T12 | 00:51:30 | -
R892 | page n/a | line 535 | DATE | quarter | first quarter to second quarter | T12 | 00:51:30 | -
R893 | page n/a | line 540 | DATE | half | almost one and a half month so from that | T12 | 00:52:07 | -
R894 | page n/a | line 561 | DATE | Q1 | go back to your Q1 absolute a bit double | T12 | 00:54:12 | -
R895 | page n/a | line 561 | DATE | quarters | over the next two quarters is a bit | T12 | 00:54:12 | -
R896 | page n/a | line 562 | DATE | quarter | and this much this quarter is like a | T12 | 00:54:18 | -
R897 | page n/a | line 570 | DATE | quarters | in the next two quarters you will see as | T12 | 00:54:35 | -
R898 | page n/a | line 576 | DATE | quarter | the yearly achievement. This quarter is a | T12 | 00:55:09 | -
R899 | page n/a | line 581 | DATE | H-1 | So, H-1 F-1 27 was a | T14 | 00:55:47 | ASR_DOUBT(fiscal label garbled)
R900 | page n/a | line 581 | DATE | F-1 | So, H-1 F-1 27 was a half | T14 | 00:55:47 | -
R901 | page n/a | line 581 | DATE | half | F-1 27 was a half of strong growth of | T14 | 00:55:47 | -
R902 | page n/a | line 582 | DATE | Q2 | on our margin in Q2, during the half we | T14 | 00:55:57 | -
R903 | page n/a | line 582 | DATE | half | in Q2, during the half we stayed focused | T14 | 00:55:57 | -
R904 | page n/a | line 586 | DATE | Q3 | to Q3 and Q4 we expect | T14 | 00:56:16 | -
R905 | page n/a | line 586 | DATE | Q4 | to Q3 and Q4 we expect volume group | T14 | 00:56:16 | -
R906 | page n/a | line 588 | DATE | Q3's | margin to recover from Q3's FY27 onwards as pricing | T14 | 00:56:27 | -
R907 | page n/a | line 588 | DATE | FY27 | to recover from Q3's FY27 onwards as pricing adjustments | T14 | 00:56:27 | -
R908 | page n/a | line 590 | DATE | 2027 | be primarily focused through 2027. | T14 | 00:56:41 | -
R909 | page n/a | line 593 | DATE | quarter | quarter. Thank you. Thank you. | T15 | 00:56:59 | -

## QUALIFIER (manual: spoken defining or restricting phrases): R910-R934 (25 rows)
R910 | page n/a | line 39 | QUALIFIER | Treat every figure as management-tier and unverified; numbers may be misheard; speaker names not identified; prefer filed documents where they conflict | ASR header disclaimer | T00 |  | -
R911 | page n/a | line 49 | QUALIFIER | certain statements may be forward-looking; actual results may differ materially (lines 11-14) | safe-harbor reminder | T01 | 00:00:42 | -
R912 | page n/a | line 55 | QUALIFIER | growth figures stated on year-on-year basis | basis of comparison | T02 | 00:01:55 | -
R913 | page n/a | line 62 | QUALIFIER | EBITDA grew on absolute basis; EBITDA margin impacted in Q2 FY27 | EBITDA qualifier | T02 | 00:02:52 | -
R914 | page n/a | line 64 | QUALIFIER | about 45% to 50% of customers on conversion cost model, price moves with polymer price | contract share qualifier | T02 | 00:03:03 | -
R915 | page n/a | line 67 | QUALIFIER | price pass-through reflects from Q3 FY27 onwards 'subject to market condition stabilization' | condition on pass-through | T02 | 00:03:25 | -
R916 | page n/a | line 72 | QUALIFIER | packaging typically accounts for only 1-2% of customers' product price | metric defined as share | T02 | 00:04:01 | -
R917 | page n/a | line 100 | QUALIFIER | figures are consolidated (revenue, EBITDA, PAT) per CFO | basis: consolidated | T03 | 00:06:56 | -
R918 | page n/a | line 110 | QUALIFIER | pricing adjustments follow with a lag of 1 or 2 quarters [ASR 'water'] | lag qualifier | T03 | 00:08:19 | -
R919 | page n/a | line 114 | QUALIFIER | Q2 PAT affected by 2.62 crores share of loss of Mexico JV | PAT qualifier | T03 | 00:08:54 | -
R920 | page n/a | line 119 | QUALIFIER | moderation in ROE and ROC attributed to IPO capital base; funds progressively deployed | ROE/ROC qualifier | T03 | 00:10:00 | -
R921 | page n/a | line 124 | QUALIFIER | H1 PAT included 6.06 crores loss from Mexico JV with no matching revenue in consolidated figures | PAT qualifier | T03 | 00:10:37 | -
R922 | page n/a | line 157 | QUALIFIER | gross margin impact of 7% against 26% raw material rise; rest passed on | gross margin qualifier | T05 | 00:14:23 | -
R923 | page n/a | line 168 | QUALIFIER | 'rough calculation' per-kg figures | approximation marker | T05 | 00:16:13 | -
R924 | page n/a | line 187 | QUALIFIER | pinch bottom 21% of revenue vs 17 or 18 [ASR] last year, 'approximate' | approximation marker | T06 | 00:18:30 | -
R925 | page n/a | line 268 | QUALIFIER | selling price fixed as per order date, not delivery time | pricing basis | T07 | 00:27:24 | -
R926 | page n/a | line 278 | QUALIFIER | contract pricing monthly or quarterly revision; biggest customer quarterly | price revision basis | T07 | 00:28:40 | -
R927 | page n/a | line 386 | QUALIFIER | 'single one percent depends on the market'; 99 percent covered | condition marker | T09 | 00:37:55 | -
R928 | page n/a | line 407 | QUALIFIER | US customer contract 'minimum 150 crores' per year, one year minimum; three year contract (lines 373-374) | contract qualifier | T09 | 00:39:48 | -
R929 | page n/a | line 445 | QUALIFIER | tax rate 22% new regime; effective tax rate 25% including surcharge | tax qualifier | T10 | 00:43:27 | -
R930 | page n/a | line 447 | QUALIFIER | IPO expense 28 crores eliminated from securities premium; deferred and current tax impact | tax/IPO qualifier | T10 | 00:43:38 | -
R931 | page n/a | line 455 | QUALIFIER | Mexico breakeven Q4 targeted per provisional view, 'not very committed' | commitment qualifier | T10 | 00:44:33 | -
R932 | page n/a | line 495 | QUALIFIER | added plant is a rented plant, new capacity in next one or two months | capacity qualifier | T11 | 00:47:45 | -
R933 | page n/a | line 559 | QUALIFIER | 'it is not 100% we can get it' on price pass-through; average out | pass-through qualifier | T12 | 00:53:58 | -
R934 | page n/a | line 576 | QUALIFIER | 'yearly we can achieve'; this quarter 'significant little bit down' | annual vs quarter qualifier | T12 | 00:55:09 | -

