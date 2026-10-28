# LEDGER: results | IndiaMART InterMESH Limited (INDIAMART) | q2fy27 | A2 enumerator (sonnet-5-5)
Source: extracted/indiamart-results-q2fy27-structured.md (R001-R849). Rows referenced by ID; no claim text re-copied. Units INR million.

```
=== A2 COUNT TEST ===
category: ids_total           grep_count: 849  sweep_count: 849  match: yes  (R-row grep vs header 'ID range R001-R849' vs ledger index)
category: notes_numbered     grep_count: 11   sweep_count: 11   match: yes  (fulltext numbered notes 5 consol + 6 standalone vs structured R813-817,R827-832)
category: notes_footnotes    grep_count: 5    sweep_count: 5    match: yes  (fulltext a/b/c segment notes + 2 cash flow footnotes vs structured)
category: line_items         grep_count: 220   sweep_count: 220   match: yes  (distinct page+line pairs R001-R690 vs distinct page+label groups)
category: zero_standing      grep_count: 26    sweep_count: 26    match: yes  (grep [ZERO_STANDING] in structured vs ledger section 3; fulltext dash tokens unreconcilable, pages scrambled, see analyst_note)
category: agenda_items       grep_count: 1    sweep_count: 1    match: yes  (letter carries one agenda item; times R705,R706)
category: auditor_paras      grep_count: 10   sweep_count: 10   match: yes  (fulltext headings 6 consol incl Other Matters a,b + 4 standalone; plus Annexure I list)
category: entities           grep_count: 14   sweep_count: 14   match: yes  (fulltext Annexure I Subsidiary/Associate lines vs R733-R746)
category: signature_blocks   grep_count: 3    sweep_count: 3    match: yes  (CS letter, consol MD, standalone MD)
category: turns/questions/mgmt_numbers/slides: not applicable to results doctype
gate_a2: pass
=== END COUNT TEST ===
```

ID ACCOUNTABILITY: ids_in_structured: 849 | ids_referenced_in_ledger: 849 | orphan_ids: [] | match: yes

## 1. NOTES (numbered notes and unnumbered footnotes)
ROW_ID | category | flags | cross-ref / materiality
R813 | note_numbered | RESTATED consol/standalone | consol note 1 (approval, unmodified opinion)
R814 | note_numbered | RESTATED consol/standalone | consol note 2 (Ind AS basis)
R815 | note_numbered | RESTATED consol/standalone | consol note 3 (cash flow Annexure I)
R816 | note_numbered | RESTATED consol/standalone | consol note 4 (publication)
R817 | note_numbered | RESTATED consol/standalone | consol note 5 (Labour Codes; pairs R760,R761,R764)
R827 | note_numbered | RESTATED consol/standalone | standalone note 1
R828 | note_numbered | RESTATED consol/standalone | standalone note 2
R829 | note_numbered | RESTATED consol/standalone | standalone note 3
R830 | note_numbered | RESTATED consol/standalone | standalone note 4 (segments only in consolidated)
R831 | note_numbered | RESTATED consol/standalone | standalone note 5
R832 | note_numbered | RESTATED consol/standalone | standalone note 6 (Labour Codes; pairs R762,R763,R765)
R809 | note_unnumbered | FOOTNOTE | segment note a (operating segment definition)
R810 | note_unnumbered | FOOTNOTE | segment note b (two reportable segments)
R811 | note_unnumbered | FOOTNOTE | segment note c (segment descriptions)
R820 | note_unnumbered | FOOTNOTE | consol cash flow footnote (other income components)
R835 | note_unnumbered | FOOTNOTE | standalone cash flow footnote (other income components)

## 2. LINE ITEMS (220 line-item groups; each group = all period columns of one statement line)
GROUP | page | label | ROW_IDs | flags
L001 | p7 | consolidated revenue from operations | R001-R006 (6 values) | 
L002 | p7 | consolidated other income | R007-R012 (6 values) | 
L003 | p7 | consolidated total income | R013-R018 (6 values) | 
L004 | p7 | consolidated employee benefits expense | R019-R024 (6 values) | 
L005 | p7 | consolidated finance costs | R025-R030 (6 values) | 
L006 | p7 | consolidated depreciation and amortisation | R031-R036 (6 values) | 
L007 | p7 | consolidated other expenses | R037-R042 (6 values) | 
L008 | p7 | consolidated total expenses | R043-R048 (6 values) | 
L009 | p7 | consolidated profit before share of loss in associates and tax | R049-R054 (6 values) | 
L010 | p7 | consolidated share in net loss of associates | R055-R060 (6 values) | 
L011 | p7 | consolidated profit before tax | R061-R066 (6 values) | 
L012 | p7 | consolidated current tax | R067-R072 (6 values) | 
L013 | p7 | consolidated deferred tax | R073-R078 (6 values) | 
L014 | p7 | consolidated total tax expense | R079-R084 (6 values) | 
L015 | p7 | consolidated net profit | R085-R090 (6 values) | 
L016 | p7 | consolidated OCI not reclassified (net of tax) | R091-R096 (6 values) | 
L017 | p7 | consolidated total comprehensive income | R097-R102 (6 values) | 
L018 | p7 | consolidated paid up equity share capital | R103-R108 (6 values) | 
L019 | p7 | consolidated other equity | R109 (1 values) | 
L020 | p7 | consolidated basic EPS INR | R110-R115 (6 values) | 
L021 | p7 | consolidated diluted EPS INR | R116-R121 (6 values) | 
L022 | p15 | standalone revenue from operations | R122-R127 (6 values) | 
L023 | p15 | standalone other income | R128-R133 (6 values) | 
L024 | p15 | standalone total income | R134-R139 (6 values) | 
L025 | p15 | standalone employee benefits expense | R140-R145 (6 values) | 
L026 | p15 | standalone finance costs | R146-R151 (6 values) | 
L027 | p15 | standalone depreciation and amortisation | R152-R157 (6 values) | 
L028 | p15 | standalone other expenses | R158-R163 (6 values) | 
L029 | p15 | standalone total expenses | R164-R169 (6 values) | 
L030 | p15 | standalone profit before tax | R170-R175 (6 values) | 
L031 | p15 | standalone current tax | R176-R181 (6 values) | 
L032 | p15 | standalone deferred tax | R182-R187 (6 values) | 
L033 | p15 | standalone total tax expense | R188-R193 (6 values) | 
L034 | p15 | standalone net profit | R194-R199 (6 values) | 
L035 | p15 | standalone OCI not reclassified (net of tax) | R200-R205 (6 values) | 
L036 | p15 | standalone total comprehensive income | R206-R211 (6 values) | 
L037 | p15 | standalone paid up equity share capital | R212-R217 (6 values) | 
L038 | p15 | standalone other equity | R218 (1 values) | 
L039 | p15 | standalone basic EPS INR | R219-R224 (6 values) | 
L040 | p15 | standalone diluted EPS INR | R225-R230 (6 values) | 
L041 | p9 | segment Web and related services segment revenue | R231-R236 (6 values) | 
L042 | p9 | segment Accounting Software segment revenue | R237-R242 (6 values) | 
L043 | p9 | segment total segment revenue | R243-R248 (6 values) | 
L044 | p9 | segment inter-segment revenue Web and related | R249-R254 (6 values) | ZERO_STANDING:R250-R251,R253
L045 | p9 | segment inter-segment revenue Accounting Software | R255-R260 (6 values) | ZERO_STANDING:R255-R260
L046 | p9 | segment total inter-segment revenue | R261-R266 (6 values) | ZERO_STANDING:R262-R263,R265
L047 | p9 | segment external revenue Web and related services | R267-R272 (6 values) | 
L048 | p9 | segment external revenue Accounting Software | R273-R278 (6 values) | 
L049 | p9 | segment total revenue from operations external | R279-R284 (6 values) | 
L050 | p9 | segment segment result Web and related services | R285-R290 (6 values) | 
L051 | p9 | segment segment result Accounting Software | R291-R296 (6 values) | 
L052 | p9 | segment total segment result | R297-R302 (6 values) | 
L053 | p9 | segment finance cost | R303-R308 (6 values) | 
L054 | p9 | segment depreciation and amortisation | R309-R314 (6 values) | 
L055 | p9 | segment other income | R315-R320 (6 values) | 
L056 | p9 | segment profit before share of loss in associates, exceptional items and tax | R321-R326 (6 values) | 
L057 | p9 | segment share in net loss of associates | R327-R332 (6 values) | 
L058 | p9 | segment profit before tax | R333-R338 (6 values) | 
L059 | p9 | segment segment assets Web and related services | R339-R344 (6 values) | 
L060 | p9 | segment segment assets Accounting Software | R345-R350 (6 values) | 
L061 | p9 | segment segment assets Unallocable | R351-R356 (6 values) | 
L062 | p9 | segment total segment assets | R357-R362 (6 values) | 
L063 | p9 | segment segment liabilities Web and related services | R363-R368 (6 values) | 
L064 | p9 | segment segment liabilities Accounting Software | R369-R374 (6 values) | 
L065 | p9 | segment total segment liabilities | R375-R380 (6 values) | 
L066 | p8 | consolidated balance sheet property, plant and equipment | R381-R382 (2 values) | 
L067 | p8 | consolidated balance sheet right-of-use assets | R383-R384 (2 values) | 
L068 | p8 | consolidated balance sheet goodwill | R385-R386 (2 values) | 
L069 | p8 | consolidated balance sheet other intangible assets | R387-R388 (2 values) | 
L070 | p8 | consolidated balance sheet investment in associates | R389-R390 (2 values) | 
L071 | p8 | consolidated balance sheet non-current investments | R391-R392 (2 values) | 
L072 | p8 | consolidated balance sheet non-current loans | R393-R394 (2 values) | 
L073 | p8 | consolidated balance sheet non-current other financial assets | R395-R396 (2 values) | 
L074 | p8 | consolidated balance sheet deferred tax assets (net) | R397-R398 (2 values) | ZERO_STANDING:R397
L075 | p8 | consolidated balance sheet non-current tax assets (net) | R399-R400 (2 values) | 
L076 | p8 | consolidated balance sheet other non-current assets | R401-R402 (2 values) | 
L077 | p8 | consolidated balance sheet total non-current assets | R403-R404 (2 values) | 
L078 | p8 | consolidated balance sheet current investments | R405-R406 (2 values) | 
L079 | p8 | consolidated balance sheet trade receivables | R407-R408 (2 values) | 
L080 | p8 | consolidated balance sheet cash and cash equivalents | R409-R410 (2 values) | 
L081 | p8 | consolidated balance sheet bank balances other than cash | R411-R412 (2 values) | 
L082 | p8 | consolidated balance sheet current loans | R413-R414 (2 values) | 
L083 | p8 | consolidated balance sheet current other financial assets | R415-R416 (2 values) | 
L084 | p8 | consolidated balance sheet other current assets | R417-R418 (2 values) | 
L085 | p8 | consolidated balance sheet total current assets | R419-R420 (2 values) | 
L086 | p8 | consolidated balance sheet total assets | R421-R422 (2 values) | 
L087 | p8 | consolidated balance sheet share capital | R423-R424 (2 values) | 
L088 | p8 | consolidated balance sheet other equity | R425-R426 (2 values) | 
L089 | p8 | consolidated balance sheet total equity | R427-R428 (2 values) | 
L090 | p8 | consolidated balance sheet non-current lease liabilities | R429-R430 (2 values) | 
L091 | p8 | consolidated balance sheet non-current contract liabilities | R431-R432 (2 values) | 
L092 | p8 | consolidated balance sheet non-current provisions | R433-R434 (2 values) | 
L093 | p8 | consolidated balance sheet deferred tax liabilities (net) | R435-R436 (2 values) | 
L094 | p8 | consolidated balance sheet total non-current liabilities | R437-R438 (2 values) | 
L095 | p8 | consolidated balance sheet current lease liabilities | R439-R440 (2 values) | 
L096 | p8 | consolidated balance sheet trade payables MSME dues | R441-R442 (2 values) | 
L097 | p8 | consolidated balance sheet trade payables other creditors | R443-R444 (2 values) | 
L098 | p8 | consolidated balance sheet other current financial liabilities | R445-R446 (2 values) | 
L099 | p8 | consolidated balance sheet current contract liabilities | R447-R448 (2 values) | 
L100 | p8 | consolidated balance sheet other current liabilities | R449-R450 (2 values) | 
L101 | p8 | consolidated balance sheet current provisions | R451-R452 (2 values) | 
L102 | p8 | consolidated balance sheet current tax liabilities (net) | R453-R454 (2 values) | 
L103 | p8 | consolidated balance sheet total current liabilities | R455-R456 (2 values) | 
L104 | p8 | consolidated balance sheet total liabilities | R457-R458 (2 values) | 
L105 | p8 | consolidated balance sheet total equity and liabilities | R459-R460 (2 values) | 
L106 | p16 | standalone balance sheet property, plant and equipment | R461-R462 (2 values) | 
L107 | p16 | standalone balance sheet right-of-use assets | R463-R464 (2 values) | 
L108 | p16 | standalone balance sheet intangible assets | R465-R466 (2 values) | 
L109 | p16 | standalone balance sheet investment in subsidiaries and associates | R467-R468 (2 values) | 
L110 | p16 | standalone balance sheet non-current investments | R469-R470 (2 values) | 
L111 | p16 | standalone balance sheet non-current loans | R471-R472 (2 values) | 
L112 | p16 | standalone balance sheet non-current other financial assets | R473-R474 (2 values) | 
L113 | p16 | standalone balance sheet non-current tax assets (net) | R475-R476 (2 values) | 
L114 | p16 | standalone balance sheet other non-current assets | R477-R478 (2 values) | 
L115 | p16 | standalone balance sheet total non-current assets | R479-R480 (2 values) | 
L116 | p16 | standalone balance sheet current investments | R481-R482 (2 values) | 
L117 | p16 | standalone balance sheet trade receivables | R483-R484 (2 values) | 
L118 | p16 | standalone balance sheet cash and cash equivalents | R485-R486 (2 values) | 
L119 | p16 | standalone balance sheet bank balances other than cash | R487-R488 (2 values) | 
L120 | p16 | standalone balance sheet current loans | R489-R490 (2 values) | 
L121 | p16 | standalone balance sheet current other financial assets | R491-R492 (2 values) | 
L122 | p16 | standalone balance sheet other current assets | R493-R494 (2 values) | 
L123 | p16 | standalone balance sheet total current assets | R495-R496 (2 values) | 
L124 | p16 | standalone balance sheet total assets | R497-R498 (2 values) | 
L125 | p16 | standalone balance sheet share capital | R499-R500 (2 values) | 
L126 | p16 | standalone balance sheet other equity | R501-R502 (2 values) | 
L127 | p16 | standalone balance sheet total equity | R503-R504 (2 values) | 
L128 | p16 | standalone balance sheet non-current lease liabilities | R505-R506 (2 values) | 
L129 | p16 | standalone balance sheet non-current contract liabilities | R507-R508 (2 values) | 
L130 | p16 | standalone balance sheet non-current provisions | R509-R510 (2 values) | 
L131 | p16 | standalone balance sheet deferred tax liabilities (net) | R511-R512 (2 values) | 
L132 | p16 | standalone balance sheet total non-current liabilities | R513-R514 (2 values) | 
L133 | p16 | standalone balance sheet current lease liabilities | R515-R516 (2 values) | 
L134 | p16 | standalone balance sheet trade payables MSME dues | R517-R518 (2 values) | 
L135 | p16 | standalone balance sheet trade payables other creditors | R519-R520 (2 values) | 
L136 | p16 | standalone balance sheet other current financial liabilities | R521-R522 (2 values) | 
L137 | p16 | standalone balance sheet current contract liabilities | R523-R524 (2 values) | 
L138 | p16 | standalone balance sheet other current liabilities | R525-R526 (2 values) | 
L139 | p16 | standalone balance sheet current provisions | R527-R528 (2 values) | 
L140 | p16 | standalone balance sheet current tax liabilities (net) | R529-R530 (2 values) | 
L141 | p16 | standalone balance sheet total current liabilities | R531-R532 (2 values) | 
L142 | p16 | standalone balance sheet total liabilities | R533-R534 (2 values) | 
L143 | p16 | standalone balance sheet total equity and liabilities | R535-R536 (2 values) | 
L144 | p11 | consolidated cash profit before tax | R537-R538 (2 values) | 
L145 | p11 | consolidated cash depreciation and amortisation | R539-R540 (2 values) | 
L146 | p11 | consolidated cash interest, dividend and other income | R541-R542 (2 values) | 
L147 | p11 | consolidated cash liabilities and provisions no longer required written back | R543-R544 (2 values) | 
L148 | p11 | consolidated cash fair value gain/(loss) net, interest and income from sale of mutual funds, ETFs, bonds, debentures, units of investment trust and AIFs | R545-R546 (2 values) | 
L149 | p11 | consolidated cash fair value loss on measurement of investment in other entities | R547-R548 (2 values) | ZERO_STANDING:R548
L150 | p11 | consolidated cash net gain on disposal of PPE | R549-R550 (2 values) | ZERO_STANDING:R550
L151 | p11 | consolidated cash finance costs | R551-R552 (2 values) | 
L152 | p11 | consolidated cash share-based payment expense | R553-R554 (2 values) | 
L153 | p11 | consolidated cash share of net loss of associates | R555-R556 (2 values) | 
L154 | p11 | consolidated cash operating profit before working capital changes | R557-R558 (2 values) | 
L155 | p11 | consolidated cash change in trade receivables | R559-R560 (2 values) | 
L156 | p11 | consolidated cash change in other financial assets | R561-R562 (2 values) | 
L157 | p11 | consolidated cash change in other assets | R563-R564 (2 values) | 
L158 | p11 | consolidated cash change in other financial liabilities | R565-R566 (2 values) | 
L159 | p11 | consolidated cash change in trade payables | R567-R568 (2 values) | 
L160 | p11 | consolidated cash change in contract liabilities | R569-R570 (2 values) | 
L161 | p11 | consolidated cash change in provisions and other liabilities | R571-R572 (2 values) | 
L162 | p11 | consolidated cash cash generated from operations | R573-R574 (2 values) | 
L163 | p11 | consolidated cash income tax paid (net) | R575-R576 (2 values) | 
L164 | p11 | consolidated cash net cash from operating activities | R577-R578 (2 values) | 
L165 | p11 | consolidated cash proceeds from sale of PPE | R579-R580 (2 values) | ZERO_STANDING:R580
L166 | p11 | consolidated cash purchase of PPE, intangibles, CWIP and capital advances | R581-R582 (2 values) | 
L167 | p11 | consolidated cash purchase of current investments | R583-R584 (2 values) | 
L168 | p11 | consolidated cash ICDs placed with financial institutions and bodies corporate | R585-R586 (2 values) | ZERO_STANDING:R585
L169 | p11 | consolidated cash redemption of ICDs | R587-R588 (2 values) | ZERO_STANDING:R587
L170 | p11 | consolidated cash proceeds from sale of current investments | R589-R590 (2 values) | 
L171 | p11 | consolidated cash interest, dividend and income from investment units | R591-R592 (2 values) | 
L172 | p11 | consolidated cash investment in bank deposits | R593-R594 (2 values) | 
L173 | p11 | consolidated cash redemption of bank deposits | R595-R596 (2 values) | 
L174 | p11 | consolidated cash investment in associates and other entities | R597-R598 (2 values) | 
L175 | p11 | consolidated cash net cash from investing activities | R599-R600 (2 values) | 
L176 | p11 | consolidated cash repayment of lease liabilities incl interest | R601-R602 (2 values) | 
L177 | p11 | consolidated cash payment of deferred consideration | R603-R604 (2 values) | ZERO_STANDING:R603
L178 | p11 | consolidated cash dividend paid | R605-R606 (2 values) | 
L179 | p11 | consolidated cash proceeds from issue of equity shares on ESOP exercise | R607-R608 (2 values) | ZERO_STANDING:R608
L180 | p11 | consolidated cash net cash used in financing activities | R609-R610 (2 values) | 
L181 | p11 | consolidated cash net increase in cash and cash equivalents | R611-R612 (2 values) | 
L182 | p11 | consolidated cash opening cash and cash equivalents | R613-R614 (2 values) | 
L183 | p11 | consolidated cash closing cash and cash equivalents | R615-R616 (2 values) | 
L184 | p18 | standalone cash profit before tax | R617-R618 (2 values) | 
L185 | p18 | standalone cash depreciation and amortisation | R619-R620 (2 values) | 
L186 | p18 | standalone cash interest and other income | R621-R622 (2 values) | 
L187 | p18 | standalone cash fair value gain and income from sale of mutual funds, bonds, debentures, AIFs and investment trust | R623-R624 (2 values) | 
L188 | p18 | standalone cash fair value loss on measurement of investment in other entities | R625-R626 (2 values) | ZERO_STANDING:R626
L189 | p18 | standalone cash gain on disposal of PPE | R627-R628 (2 values) | ZERO_STANDING:R628
L190 | p18 | standalone cash share-based payment expense | R629-R630 (2 values) | 
L191 | p18 | standalone cash impairment loss on investment | R631-R632 (2 values) | ZERO_STANDING:R631
L192 | p18 | standalone cash finance costs | R633-R634 (2 values) | 
L193 | p18 | standalone cash other | R635-R636 (2 values) | ZERO_STANDING:R636
L194 | p18 | standalone cash operating profit before working capital changes | R637-R638 (2 values) | 
L195 | p18 | standalone cash change in trade receivables | R639-R640 (2 values) | 
L196 | p18 | standalone cash change in other financial assets | R641-R642 (2 values) | 
L197 | p18 | standalone cash change in other assets | R643-R644 (2 values) | 
L198 | p18 | standalone cash change in other financial liabilities | R645-R646 (2 values) | 
L199 | p18 | standalone cash change in trade payables | R647-R648 (2 values) | 
L200 | p18 | standalone cash change in contract liabilities | R649-R650 (2 values) | 
L201 | p18 | standalone cash change in provisions and other liabilities | R651-R652 (2 values) | 
L202 | p18 | standalone cash cash generated from operations | R653-R654 (2 values) | 
L203 | p18 | standalone cash income tax paid (net) | R655-R656 (2 values) | 
L204 | p18 | standalone cash net cash from operating activities | R657-R658 (2 values) | 
L205 | p18 | standalone cash proceeds from sale of PPE | R659-R660 (2 values) | 
L206 | p18 | standalone cash purchase of PPE, intangibles and capital advances | R661-R662 (2 values) | 
L207 | p18 | standalone cash purchase of current investments | R663-R664 (2 values) | 
L208 | p18 | standalone cash ICDs placed with financial institutions | R665-R666 (2 values) | ZERO_STANDING:R665
L209 | p18 | standalone cash investment in subsidiaries, associates and other entities | R667-R668 (2 values) | 
L210 | p18 | standalone cash proceeds from sale of current investments | R669-R670 (2 values) | 
L211 | p18 | standalone cash interest and income from investment units | R671-R672 (2 values) | 
L212 | p18 | standalone cash investment in bank deposits | R673-R674 (2 values) | 
L213 | p18 | standalone cash net cash from/(used in) investing activities | R675-R676 (2 values) | 
L214 | p18 | standalone cash repayment of lease liabilities incl interest | R677-R678 (2 values) | 
L215 | p18 | standalone cash payment of dividends | R679-R680 (2 values) | 
L216 | p18 | standalone cash proceeds from issue of equity shares on ESOP exercise | R681-R682 (2 values) | ZERO_STANDING:R682
L217 | p18 | standalone cash net cash used in financing activities | R683-R684 (2 values) | 
L218 | p18 | standalone cash net decrease in cash and cash equivalents | R685-R686 (2 values) | 
L219 | p18 | standalone cash opening cash and cash equivalents | R687-R688 (2 values) | 
L220 | p18 | standalone cash closing cash and cash equivalents | R689-R690 (2 values) | 

## 3. ZERO_STANDING (26 values, nil/dash rows)
ROW_ID | page | line | flag | label (from A1 row)
R250 | p9 | l471 | ZERO_STANDING | segment inter-segment revenue Web and related, Q1 FY27
R251 | p9 | l471 | ZERO_STANDING | segment inter-segment revenue Web and related, Q2 FY26
R253 | p9 | l471 | ZERO_STANDING | segment inter-segment revenue Web and related, H1 FY26
R255 | p9 | l473 | ZERO_STANDING | segment inter-segment revenue Accounting Software, Q2 FY27
R256 | p9 | l473 | ZERO_STANDING | segment inter-segment revenue Accounting Software, Q1 FY27
R257 | p9 | l473 | ZERO_STANDING | segment inter-segment revenue Accounting Software, Q2 FY26
R258 | p9 | l473 | ZERO_STANDING | segment inter-segment revenue Accounting Software, H1 FY27
R259 | p9 | l473 | ZERO_STANDING | segment inter-segment revenue Accounting Software, H1 FY26
R260 | p9 | l473 | ZERO_STANDING | segment inter-segment revenue Accounting Software, FY26
R262 | p9 | l475 | ZERO_STANDING | segment total inter-segment revenue, Q1 FY27
R263 | p9 | l475 | ZERO_STANDING | segment total inter-segment revenue, Q2 FY26
R265 | p9 | l475 | ZERO_STANDING | segment total inter-segment revenue, H1 FY26
R397 | p8 | l400 | ZERO_STANDING | consolidated balance sheet deferred tax assets (net), 30-Sep-2026
R548 | p11 | l574 | ZERO_STANDING | consolidated cash fair value loss on measurement of investment in other entities, 6m to 30-Sep-2025
R550 | p11 | l575 | ZERO_STANDING | consolidated cash net gain on disposal of PPE, 6m to 30-Sep-2025
R580 | p11 | l594 | ZERO_STANDING | consolidated cash proceeds from sale of PPE, 6m to 30-Sep-2025
R585 | p11 | l599 | ZERO_STANDING | consolidated cash ICDs placed with financial institutions and bodies corporate, 6m to 30-Sep-2026
R587 | p11 | l600 | ZERO_STANDING | consolidated cash redemption of ICDs, 6m to 30-Sep-2026
R603 | p11 | l611 | ZERO_STANDING | consolidated cash payment of deferred consideration, 6m to 30-Sep-2026
R608 | p11 | l614 | ZERO_STANDING | consolidated cash proceeds from issue of equity shares on ESOP exercise, 6m to 30-Sep-2025
R626 | p18 | l953 | ZERO_STANDING | standalone cash fair value loss on measurement of investment in other entities, 6m to 30-Sep-2025
R628 | p18 | l954 | ZERO_STANDING | standalone cash gain on disposal of PPE, 6m to 30-Sep-2025
R631 | p18 | l956 | ZERO_STANDING | standalone cash impairment loss on investment, 6m to 30-Sep-2026
R636 | p18 | l958 | ZERO_STANDING | standalone cash other, 6m to 30-Sep-2025
R665 | p18 | l978 | ZERO_STANDING | standalone cash ICDs placed with financial institutions, 6m to 30-Sep-2026
R682 | p18 | l990 | ZERO_STANDING | standalone cash proceeds from issue of equity shares on ESOP exercise, 6m to 30-Sep-2025
Note: R397 (consol DTA 30-Sep-2026 dash) maps to a fulltext line printed beside 'Non-current tax assets' (line 400); A1 mapped from page render. Alignment uncertainty carried to A3.

## 4. BOARD OUTCOME LETTER / AGENDA ITEMS
ROW_ID | category | flags | note
R769 | agenda/board |  | Agenda item 1: approval of audited consolidated and standalone results (only agenda item present)
R848 | agenda/board |  | approval statement
R849 | agenda/board |  | auditor report enclosure
R753 | agenda/board |  | website dissemination
R705 | agenda/board |  | meeting start 11:00
R706 | agenda/board |  | meeting end 15:00 (4 hours)
R768 | agenda/board |  | letter date
R770 | agenda/board |  | period
R703 | agenda/board |  | BSE scrip code
R725 | agenda/board |  | addressee NSE
R726 | agenda/board |  | addressee BSE
R727 | agenda/board |  | regulation
R728 | agenda/board |  | company
Absent from letter (no row, nothing to reference): dividend, AR/AGM, director changes, auditor change, ESOP grants, enabling resolutions.

## 5. AUDITOR REPORT PARAGRAPHS (10 headed sections plus Annexure I)
Para | scope | ROW_IDs | flags
A1 | consol Opinion (unmodified, Note 1 R813) | R730,R731,R772,R773 | 
A2 | consol Basis for Opinion | R755 | 
A3 | consol Mgmt/Board responsibilities (going concern wording) | R766 | 
A4 | consol Auditor responsibilities (SEBI 33(8) circular) | R756 | 
A5 | consol Other Matters (a): five subsidiaries audited by other auditors | R691-R697,R757,R836,R837,R841,R777 | 
A6 | consol Other Matters (b): seven associates + one unaudited associate (management furnished) | R698-R702,R838,R839,R840,R776 | UNAUDITED_ASSOCIATE_INFO
A7 | consol signature block / UDIN | R732,R708,R709,R710,R774,R717,R718,R719,R720,R721 | 
S1 | standalone Opinion | R759,R791 | 
S2 | standalone Basis for Opinion | (no separate row) | 
S3 | standalone Mgmt responsibilities | (no separate row) | 
S4 | standalone Auditor responsibilities incl going concern | R767 | 
S5 | standalone signature / UDIN | R711,R792 | 
X1 | Annexure I entity list (consolidation list) | R733-R746 | 
Standalone report has no Other Matters paragraph. No Emphasis of Matter in either report. No going-concern material uncertainty; standard wording only (R766,R767). Opinion unmodified in both. S2,S3 are boilerplate with no dedicated structured row.

## 6. ENTITIES / CONSOLIDATION LIST (14 consolidated entities: 6 subsidiaries, 8 associates)
ROW_ID | relationship | flags
R733 | subsidiary | 
R734 | subsidiary | 
R735 | subsidiary | ENTITY_CHANGE(renamed, 'formerly')
R736 | subsidiary | ENTITY_CHANGE(renamed, 'formerly')
R737 | subsidiary | ENTITY_CHANGE(new sub 04-Aug-2026)
R738 | subsidiary | 
R739 | associate | 
R740 | associate | ENTITY_CHANGE(associate ceased 29-May-2026)
R741 | associate | 
R742 | associate | 
R743 | associate | 
R744 | associate | 
R745 | associate | 
R746 | associate | ENTITY_CHANGE(unverifiable, w.e.f. 11-Apr-2025; no prior ledger)
Segments: R747 Web and related services, R748 Accounting Software services. Status restatements: R778,R779,R780,R842,R843,R844 (RESTATED). Prior-quarter list unavailable: ENTITY_CHANGE flags reflect status words printed in this filing only.

## 7. SIGNATURE BLOCKS
ROW_ID | signatory | flags
R729 | Company Secretary Manoj Bhargava, Board outcome letter | 
R707 | CS signature time 15:06:41 (after 15:00 close) | 
R771 | CS signature date | 
R750 | MD & CEO Dinesh Chandra Agarwal | 
R723 | MD signature time consolidated 12:35:37 | SIGNATURE_BEFORE_MEETING_END(signed 12:3x, meeting concluded 15:00)
R724 | MD signature time standalone 12:34:50 | SIGNATURE_BEFORE_MEETING_END(signed 12:3x, meeting concluded 15:00)
R789 | signing date consol | 
R796 | signing date standalone | 
R758 | place Noida | 
R732 | auditor partner David Jones | 
R774 | auditor report date consol 27-Oct | 
R792 | auditor report date standalone 27-Oct | 
FLAG SIGNATURE_BEFORE_MEETING_END: MD signatures (12:35, 12:34) precede stated meeting end 15:00. Auditor report dated 27-Oct, same day as Board approval; Audit Committee 26-Oct (R785,R794).

## 8. FULL ID COVERAGE INDEX (every structured ID, category, flags)
ROW_ID | table | ledger category | flags
R001 | NUMBER | line_items | 
R002 | NUMBER | line_items | 
R003 | NUMBER | line_items | 
R004 | NUMBER | line_items | 
R005 | NUMBER | line_items | 
R006 | NUMBER | line_items | 
R007 | NUMBER | line_items | NEGATIVE_OTHER_INCOME_Q2
R008 | NUMBER | line_items | 
R009 | NUMBER | line_items | 
R010 | NUMBER | line_items | 
R011 | NUMBER | line_items | 
R012 | NUMBER | line_items | 
R013 | NUMBER | line_items | 
R014 | NUMBER | line_items | 
R015 | NUMBER | line_items | 
R016 | NUMBER | line_items | 
R017 | NUMBER | line_items | 
R018 | NUMBER | line_items | 
R019 | NUMBER | line_items | 
R020 | NUMBER | line_items | 
R021 | NUMBER | line_items | 
R022 | NUMBER | line_items | 
R023 | NUMBER | line_items | 
R024 | NUMBER | line_items | 
R025 | NUMBER | line_items | 
R026 | NUMBER | line_items | 
R027 | NUMBER | line_items | 
R028 | NUMBER | line_items | 
R029 | NUMBER | line_items | 
R030 | NUMBER | line_items | 
R031 | NUMBER | line_items | 
R032 | NUMBER | line_items | 
R033 | NUMBER | line_items | 
R034 | NUMBER | line_items | 
R035 | NUMBER | line_items | 
R036 | NUMBER | line_items | 
R037 | NUMBER | line_items | 
R038 | NUMBER | line_items | 
R039 | NUMBER | line_items | 
R040 | NUMBER | line_items | 
R041 | NUMBER | line_items | 
R042 | NUMBER | line_items | 
R043 | NUMBER | line_items | 
R044 | NUMBER | line_items | 
R045 | NUMBER | line_items | 
R046 | NUMBER | line_items | 
R047 | NUMBER | line_items | 
R048 | NUMBER | line_items | 
R049 | NUMBER | line_items | 
R050 | NUMBER | line_items | 
R051 | NUMBER | line_items | 
R052 | NUMBER | line_items | 
R053 | NUMBER | line_items | 
R054 | NUMBER | line_items | 
R055 | NUMBER | line_items | 
R056 | NUMBER | line_items | 
R057 | NUMBER | line_items | 
R058 | NUMBER | line_items | 
R059 | NUMBER | line_items | 
R060 | NUMBER | line_items | 
R061 | NUMBER | line_items | 
R062 | NUMBER | line_items | 
R063 | NUMBER | line_items | 
R064 | NUMBER | line_items | 
R065 | NUMBER | line_items | 
R066 | NUMBER | line_items | 
R067 | NUMBER | line_items | 
R068 | NUMBER | line_items | 
R069 | NUMBER | line_items | 
R070 | NUMBER | line_items | 
R071 | NUMBER | line_items | 
R072 | NUMBER | line_items | 
R073 | NUMBER | line_items | 
R074 | NUMBER | line_items | 
R075 | NUMBER | line_items | 
R076 | NUMBER | line_items | 
R077 | NUMBER | line_items | 
R078 | NUMBER | line_items | 
R079 | NUMBER | line_items | 
R080 | NUMBER | line_items | 
R081 | NUMBER | line_items | 
R082 | NUMBER | line_items | 
R083 | NUMBER | line_items | 
R084 | NUMBER | line_items | 
R085 | NUMBER | line_items | 
R086 | NUMBER | line_items | 
R087 | NUMBER | line_items | 
R088 | NUMBER | line_items | 
R089 | NUMBER | line_items | 
R090 | NUMBER | line_items | 
R091 | NUMBER | line_items | 
R092 | NUMBER | line_items | 
R093 | NUMBER | line_items | 
R094 | NUMBER | line_items | 
R095 | NUMBER | line_items | 
R096 | NUMBER | line_items | 
R097 | NUMBER | line_items | 
R098 | NUMBER | line_items | 
R099 | NUMBER | line_items | 
R100 | NUMBER | line_items | 
R101 | NUMBER | line_items | 
R102 | NUMBER | line_items | 
R103 | NUMBER | line_items | 
R104 | NUMBER | line_items | 
R105 | NUMBER | line_items | 
R106 | NUMBER | line_items | 
R107 | NUMBER | line_items | 
R108 | NUMBER | line_items | 
R109 | NUMBER | line_items | 
R110 | NUMBER | line_items | 
R111 | NUMBER | line_items | 
R112 | NUMBER | line_items | 
R113 | NUMBER | line_items | 
R114 | NUMBER | line_items | 
R115 | NUMBER | line_items | 
R116 | NUMBER | line_items | 
R117 | NUMBER | line_items | 
R118 | NUMBER | line_items | 
R119 | NUMBER | line_items | 
R120 | NUMBER | line_items | 
R121 | NUMBER | line_items | 
R122 | NUMBER | line_items | 
R123 | NUMBER | line_items | 
R124 | NUMBER | line_items | 
R125 | NUMBER | line_items | 
R126 | NUMBER | line_items | 
R127 | NUMBER | line_items | 
R128 | NUMBER | line_items | 
R129 | NUMBER | line_items | 
R130 | NUMBER | line_items | 
R131 | NUMBER | line_items | 
R132 | NUMBER | line_items | 
R133 | NUMBER | line_items | 
R134 | NUMBER | line_items | 
R135 | NUMBER | line_items | 
R136 | NUMBER | line_items | 
R137 | NUMBER | line_items | 
R138 | NUMBER | line_items | 
R139 | NUMBER | line_items | 
R140 | NUMBER | line_items | 
R141 | NUMBER | line_items | 
R142 | NUMBER | line_items | 
R143 | NUMBER | line_items | 
R144 | NUMBER | line_items | 
R145 | NUMBER | line_items | 
R146 | NUMBER | line_items | 
R147 | NUMBER | line_items | 
R148 | NUMBER | line_items | 
R149 | NUMBER | line_items | 
R150 | NUMBER | line_items | 
R151 | NUMBER | line_items | 
R152 | NUMBER | line_items | 
R153 | NUMBER | line_items | 
R154 | NUMBER | line_items | 
R155 | NUMBER | line_items | 
R156 | NUMBER | line_items | 
R157 | NUMBER | line_items | 
R158 | NUMBER | line_items | 
R159 | NUMBER | line_items | 
R160 | NUMBER | line_items | 
R161 | NUMBER | line_items | 
R162 | NUMBER | line_items | 
R163 | NUMBER | line_items | 
R164 | NUMBER | line_items | 
R165 | NUMBER | line_items | 
R166 | NUMBER | line_items | 
R167 | NUMBER | line_items | 
R168 | NUMBER | line_items | 
R169 | NUMBER | line_items | 
R170 | NUMBER | line_items | 
R171 | NUMBER | line_items | 
R172 | NUMBER | line_items | 
R173 | NUMBER | line_items | 
R174 | NUMBER | line_items | 
R175 | NUMBER | line_items | 
R176 | NUMBER | line_items | 
R177 | NUMBER | line_items | 
R178 | NUMBER | line_items | 
R179 | NUMBER | line_items | 
R180 | NUMBER | line_items | 
R181 | NUMBER | line_items | 
R182 | NUMBER | line_items | 
R183 | NUMBER | line_items | 
R184 | NUMBER | line_items | 
R185 | NUMBER | line_items | 
R186 | NUMBER | line_items | 
R187 | NUMBER | line_items | 
R188 | NUMBER | line_items | 
R189 | NUMBER | line_items | 
R190 | NUMBER | line_items | 
R191 | NUMBER | line_items | 
R192 | NUMBER | line_items | 
R193 | NUMBER | line_items | 
R194 | NUMBER | line_items | 
R195 | NUMBER | line_items | 
R196 | NUMBER | line_items | 
R197 | NUMBER | line_items | 
R198 | NUMBER | line_items | 
R199 | NUMBER | line_items | 
R200 | NUMBER | line_items | 
R201 | NUMBER | line_items | 
R202 | NUMBER | line_items | 
R203 | NUMBER | line_items | 
R204 | NUMBER | line_items | 
R205 | NUMBER | line_items | 
R206 | NUMBER | line_items | 
R207 | NUMBER | line_items | 
R208 | NUMBER | line_items | 
R209 | NUMBER | line_items | 
R210 | NUMBER | line_items | 
R211 | NUMBER | line_items | 
R212 | NUMBER | line_items | 
R213 | NUMBER | line_items | 
R214 | NUMBER | line_items | 
R215 | NUMBER | line_items | 
R216 | NUMBER | line_items | 
R217 | NUMBER | line_items | 
R218 | NUMBER | line_items | 
R219 | NUMBER | line_items | 
R220 | NUMBER | line_items | 
R221 | NUMBER | line_items | 
R222 | NUMBER | line_items | 
R223 | NUMBER | line_items | 
R224 | NUMBER | line_items | 
R225 | NUMBER | line_items | 
R226 | NUMBER | line_items | 
R227 | NUMBER | line_items | 
R228 | NUMBER | line_items | 
R229 | NUMBER | line_items | 
R230 | NUMBER | line_items | 
R231 | NUMBER | line_items | 
R232 | NUMBER | line_items | 
R233 | NUMBER | line_items | 
R234 | NUMBER | line_items | 
R235 | NUMBER | line_items | 
R236 | NUMBER | line_items | 
R237 | NUMBER | line_items | 
R238 | NUMBER | line_items | 
R239 | NUMBER | line_items | 
R240 | NUMBER | line_items | 
R241 | NUMBER | line_items | 
R242 | NUMBER | line_items | 
R243 | NUMBER | line_items | 
R244 | NUMBER | line_items | 
R245 | NUMBER | line_items | 
R246 | NUMBER | line_items | 
R247 | NUMBER | line_items | 
R248 | NUMBER | line_items | 
R249 | NUMBER | line_items | 
R250 | NUMBER | line_items | ZERO_STANDING
R251 | NUMBER | line_items | ZERO_STANDING
R252 | NUMBER | line_items | 
R253 | NUMBER | line_items | ZERO_STANDING
R254 | NUMBER | line_items | 
R255 | NUMBER | line_items | ZERO_STANDING
R256 | NUMBER | line_items | ZERO_STANDING
R257 | NUMBER | line_items | ZERO_STANDING
R258 | NUMBER | line_items | ZERO_STANDING
R259 | NUMBER | line_items | ZERO_STANDING
R260 | NUMBER | line_items | ZERO_STANDING
R261 | NUMBER | line_items | 
R262 | NUMBER | line_items | ZERO_STANDING
R263 | NUMBER | line_items | ZERO_STANDING
R264 | NUMBER | line_items | 
R265 | NUMBER | line_items | ZERO_STANDING
R266 | NUMBER | line_items | 
R267 | NUMBER | line_items | 
R268 | NUMBER | line_items | 
R269 | NUMBER | line_items | 
R270 | NUMBER | line_items | 
R271 | NUMBER | line_items | 
R272 | NUMBER | line_items | 
R273 | NUMBER | line_items | 
R274 | NUMBER | line_items | 
R275 | NUMBER | line_items | 
R276 | NUMBER | line_items | 
R277 | NUMBER | line_items | 
R278 | NUMBER | line_items | 
R279 | NUMBER | line_items | 
R280 | NUMBER | line_items | 
R281 | NUMBER | line_items | 
R282 | NUMBER | line_items | 
R283 | NUMBER | line_items | 
R284 | NUMBER | line_items | 
R285 | NUMBER | line_items | 
R286 | NUMBER | line_items | 
R287 | NUMBER | line_items | 
R288 | NUMBER | line_items | 
R289 | NUMBER | line_items | 
R290 | NUMBER | line_items | 
R291 | NUMBER | line_items | 
R292 | NUMBER | line_items | 
R293 | NUMBER | line_items | 
R294 | NUMBER | line_items | 
R295 | NUMBER | line_items | 
R296 | NUMBER | line_items | 
R297 | NUMBER | line_items | 
R298 | NUMBER | line_items | 
R299 | NUMBER | line_items | 
R300 | NUMBER | line_items | 
R301 | NUMBER | line_items | 
R302 | NUMBER | line_items | 
R303 | NUMBER | line_items | 
R304 | NUMBER | line_items | 
R305 | NUMBER | line_items | 
R306 | NUMBER | line_items | 
R307 | NUMBER | line_items | 
R308 | NUMBER | line_items | 
R309 | NUMBER | line_items | 
R310 | NUMBER | line_items | 
R311 | NUMBER | line_items | 
R312 | NUMBER | line_items | 
R313 | NUMBER | line_items | 
R314 | NUMBER | line_items | 
R315 | NUMBER | line_items | 
R316 | NUMBER | line_items | 
R317 | NUMBER | line_items | 
R318 | NUMBER | line_items | 
R319 | NUMBER | line_items | 
R320 | NUMBER | line_items | 
R321 | NUMBER | line_items | 
R322 | NUMBER | line_items | 
R323 | NUMBER | line_items | 
R324 | NUMBER | line_items | 
R325 | NUMBER | line_items | 
R326 | NUMBER | line_items | 
R327 | NUMBER | line_items | 
R328 | NUMBER | line_items | 
R329 | NUMBER | line_items | 
R330 | NUMBER | line_items | 
R331 | NUMBER | line_items | 
R332 | NUMBER | line_items | 
R333 | NUMBER | line_items | 
R334 | NUMBER | line_items | 
R335 | NUMBER | line_items | 
R336 | NUMBER | line_items | 
R337 | NUMBER | line_items | 
R338 | NUMBER | line_items | 
R339 | NUMBER | line_items | 
R340 | NUMBER | line_items | 
R341 | NUMBER | line_items | 
R342 | NUMBER | line_items | 
R343 | NUMBER | line_items | 
R344 | NUMBER | line_items | 
R345 | NUMBER | line_items | 
R346 | NUMBER | line_items | 
R347 | NUMBER | line_items | 
R348 | NUMBER | line_items | 
R349 | NUMBER | line_items | 
R350 | NUMBER | line_items | 
R351 | NUMBER | line_items | 
R352 | NUMBER | line_items | 
R353 | NUMBER | line_items | 
R354 | NUMBER | line_items | 
R355 | NUMBER | line_items | 
R356 | NUMBER | line_items | 
R357 | NUMBER | line_items | 
R358 | NUMBER | line_items | 
R359 | NUMBER | line_items | 
R360 | NUMBER | line_items | 
R361 | NUMBER | line_items | 
R362 | NUMBER | line_items | 
R363 | NUMBER | line_items | 
R364 | NUMBER | line_items | 
R365 | NUMBER | line_items | 
R366 | NUMBER | line_items | 
R367 | NUMBER | line_items | 
R368 | NUMBER | line_items | 
R369 | NUMBER | line_items | 
R370 | NUMBER | line_items | 
R371 | NUMBER | line_items | 
R372 | NUMBER | line_items | 
R373 | NUMBER | line_items | 
R374 | NUMBER | line_items | 
R375 | NUMBER | line_items | 
R376 | NUMBER | line_items | 
R377 | NUMBER | line_items | 
R378 | NUMBER | line_items | 
R379 | NUMBER | line_items | 
R380 | NUMBER | line_items | 
R381 | NUMBER | line_items | 
R382 | NUMBER | line_items | 
R383 | NUMBER | line_items | 
R384 | NUMBER | line_items | 
R385 | NUMBER | line_items | 
R386 | NUMBER | line_items | 
R387 | NUMBER | line_items | 
R388 | NUMBER | line_items | 
R389 | NUMBER | line_items | 
R390 | NUMBER | line_items | 
R391 | NUMBER | line_items | 
R392 | NUMBER | line_items | 
R393 | NUMBER | line_items | 
R394 | NUMBER | line_items | 
R395 | NUMBER | line_items | 
R396 | NUMBER | line_items | 
R397 | NUMBER | line_items | ZERO_STANDING
R398 | NUMBER | line_items | 
R399 | NUMBER | line_items | 
R400 | NUMBER | line_items | 
R401 | NUMBER | line_items | 
R402 | NUMBER | line_items | 
R403 | NUMBER | line_items | 
R404 | NUMBER | line_items | 
R405 | NUMBER | line_items | 
R406 | NUMBER | line_items | 
R407 | NUMBER | line_items | 
R408 | NUMBER | line_items | 
R409 | NUMBER | line_items | 
R410 | NUMBER | line_items | 
R411 | NUMBER | line_items | 
R412 | NUMBER | line_items | 
R413 | NUMBER | line_items | 
R414 | NUMBER | line_items | 
R415 | NUMBER | line_items | 
R416 | NUMBER | line_items | 
R417 | NUMBER | line_items | 
R418 | NUMBER | line_items | 
R419 | NUMBER | line_items | 
R420 | NUMBER | line_items | 
R421 | NUMBER | line_items | 
R422 | NUMBER | line_items | 
R423 | NUMBER | line_items | 
R424 | NUMBER | line_items | 
R425 | NUMBER | line_items | 
R426 | NUMBER | line_items | 
R427 | NUMBER | line_items | 
R428 | NUMBER | line_items | 
R429 | NUMBER | line_items | 
R430 | NUMBER | line_items | 
R431 | NUMBER | line_items | 
R432 | NUMBER | line_items | 
R433 | NUMBER | line_items | 
R434 | NUMBER | line_items | 
R435 | NUMBER | line_items | 
R436 | NUMBER | line_items | 
R437 | NUMBER | line_items | 
R438 | NUMBER | line_items | 
R439 | NUMBER | line_items | 
R440 | NUMBER | line_items | 
R441 | NUMBER | line_items | 
R442 | NUMBER | line_items | 
R443 | NUMBER | line_items | 
R444 | NUMBER | line_items | 
R445 | NUMBER | line_items | 
R446 | NUMBER | line_items | 
R447 | NUMBER | line_items | 
R448 | NUMBER | line_items | 
R449 | NUMBER | line_items | 
R450 | NUMBER | line_items | 
R451 | NUMBER | line_items | 
R452 | NUMBER | line_items | 
R453 | NUMBER | line_items | 
R454 | NUMBER | line_items | 
R455 | NUMBER | line_items | 
R456 | NUMBER | line_items | 
R457 | NUMBER | line_items | 
R458 | NUMBER | line_items | 
R459 | NUMBER | line_items | 
R460 | NUMBER | line_items | 
R461 | NUMBER | line_items | 
R462 | NUMBER | line_items | 
R463 | NUMBER | line_items | 
R464 | NUMBER | line_items | 
R465 | NUMBER | line_items | 
R466 | NUMBER | line_items | 
R467 | NUMBER | line_items | 
R468 | NUMBER | line_items | 
R469 | NUMBER | line_items | 
R470 | NUMBER | line_items | 
R471 | NUMBER | line_items | 
R472 | NUMBER | line_items | 
R473 | NUMBER | line_items | 
R474 | NUMBER | line_items | 
R475 | NUMBER | line_items | 
R476 | NUMBER | line_items | 
R477 | NUMBER | line_items | 
R478 | NUMBER | line_items | 
R479 | NUMBER | line_items | 
R480 | NUMBER | line_items | 
R481 | NUMBER | line_items | 
R482 | NUMBER | line_items | 
R483 | NUMBER | line_items | 
R484 | NUMBER | line_items | 
R485 | NUMBER | line_items | 
R486 | NUMBER | line_items | 
R487 | NUMBER | line_items | 
R488 | NUMBER | line_items | 
R489 | NUMBER | line_items | 
R490 | NUMBER | line_items | 
R491 | NUMBER | line_items | 
R492 | NUMBER | line_items | 
R493 | NUMBER | line_items | 
R494 | NUMBER | line_items | 
R495 | NUMBER | line_items | 
R496 | NUMBER | line_items | 
R497 | NUMBER | line_items | 
R498 | NUMBER | line_items | 
R499 | NUMBER | line_items | 
R500 | NUMBER | line_items | 
R501 | NUMBER | line_items | 
R502 | NUMBER | line_items | 
R503 | NUMBER | line_items | 
R504 | NUMBER | line_items | 
R505 | NUMBER | line_items | 
R506 | NUMBER | line_items | 
R507 | NUMBER | line_items | 
R508 | NUMBER | line_items | 
R509 | NUMBER | line_items | 
R510 | NUMBER | line_items | 
R511 | NUMBER | line_items | 
R512 | NUMBER | line_items | 
R513 | NUMBER | line_items | 
R514 | NUMBER | line_items | 
R515 | NUMBER | line_items | 
R516 | NUMBER | line_items | 
R517 | NUMBER | line_items | 
R518 | NUMBER | line_items | 
R519 | NUMBER | line_items | 
R520 | NUMBER | line_items | 
R521 | NUMBER | line_items | 
R522 | NUMBER | line_items | 
R523 | NUMBER | line_items | 
R524 | NUMBER | line_items | 
R525 | NUMBER | line_items | 
R526 | NUMBER | line_items | 
R527 | NUMBER | line_items | 
R528 | NUMBER | line_items | 
R529 | NUMBER | line_items | 
R530 | NUMBER | line_items | 
R531 | NUMBER | line_items | 
R532 | NUMBER | line_items | 
R533 | NUMBER | line_items | 
R534 | NUMBER | line_items | 
R535 | NUMBER | line_items | 
R536 | NUMBER | line_items | 
R537 | NUMBER | line_items | 
R538 | NUMBER | line_items | 
R539 | NUMBER | line_items | 
R540 | NUMBER | line_items | 
R541 | NUMBER | line_items | 
R542 | NUMBER | line_items | 
R543 | NUMBER | line_items | 
R544 | NUMBER | line_items | 
R545 | NUMBER | line_items | 
R546 | NUMBER | line_items | 
R547 | NUMBER | line_items | 
R548 | NUMBER | line_items | ZERO_STANDING
R549 | NUMBER | line_items | 
R550 | NUMBER | line_items | ZERO_STANDING
R551 | NUMBER | line_items | 
R552 | NUMBER | line_items | 
R553 | NUMBER | line_items | 
R554 | NUMBER | line_items | 
R555 | NUMBER | line_items | 
R556 | NUMBER | line_items | 
R557 | NUMBER | line_items | 
R558 | NUMBER | line_items | 
R559 | NUMBER | line_items | 
R560 | NUMBER | line_items | 
R561 | NUMBER | line_items | 
R562 | NUMBER | line_items | 
R563 | NUMBER | line_items | 
R564 | NUMBER | line_items | 
R565 | NUMBER | line_items | 
R566 | NUMBER | line_items | 
R567 | NUMBER | line_items | 
R568 | NUMBER | line_items | 
R569 | NUMBER | line_items | 
R570 | NUMBER | line_items | 
R571 | NUMBER | line_items | 
R572 | NUMBER | line_items | 
R573 | NUMBER | line_items | 
R574 | NUMBER | line_items | 
R575 | NUMBER | line_items | 
R576 | NUMBER | line_items | 
R577 | NUMBER | line_items | 
R578 | NUMBER | line_items | 
R579 | NUMBER | line_items | 
R580 | NUMBER | line_items | ZERO_STANDING
R581 | NUMBER | line_items | 
R582 | NUMBER | line_items | 
R583 | NUMBER | line_items | 
R584 | NUMBER | line_items | 
R585 | NUMBER | line_items | ZERO_STANDING
R586 | NUMBER | line_items | 
R587 | NUMBER | line_items | ZERO_STANDING
R588 | NUMBER | line_items | 
R589 | NUMBER | line_items | 
R590 | NUMBER | line_items | 
R591 | NUMBER | line_items | 
R592 | NUMBER | line_items | 
R593 | NUMBER | line_items | 
R594 | NUMBER | line_items | 
R595 | NUMBER | line_items | 
R596 | NUMBER | line_items | 
R597 | NUMBER | line_items | 
R598 | NUMBER | line_items | 
R599 | NUMBER | line_items | 
R600 | NUMBER | line_items | 
R601 | NUMBER | line_items | 
R602 | NUMBER | line_items | 
R603 | NUMBER | line_items | ZERO_STANDING
R604 | NUMBER | line_items | 
R605 | NUMBER | line_items | 
R606 | NUMBER | line_items | 
R607 | NUMBER | line_items | 
R608 | NUMBER | line_items | ZERO_STANDING
R609 | NUMBER | line_items | 
R610 | NUMBER | line_items | 
R611 | NUMBER | line_items | 
R612 | NUMBER | line_items | 
R613 | NUMBER | line_items | 
R614 | NUMBER | line_items | 
R615 | NUMBER | line_items | 
R616 | NUMBER | line_items | 
R617 | NUMBER | line_items | 
R618 | NUMBER | line_items | 
R619 | NUMBER | line_items | 
R620 | NUMBER | line_items | 
R621 | NUMBER | line_items | 
R622 | NUMBER | line_items | 
R623 | NUMBER | line_items | 
R624 | NUMBER | line_items | 
R625 | NUMBER | line_items | 
R626 | NUMBER | line_items | ZERO_STANDING
R627 | NUMBER | line_items | 
R628 | NUMBER | line_items | ZERO_STANDING
R629 | NUMBER | line_items | 
R630 | NUMBER | line_items | 
R631 | NUMBER | line_items | ZERO_STANDING
R632 | NUMBER | line_items | 
R633 | NUMBER | line_items | 
R634 | NUMBER | line_items | 
R635 | NUMBER | line_items | 
R636 | NUMBER | line_items | ZERO_STANDING
R637 | NUMBER | line_items | 
R638 | NUMBER | line_items | 
R639 | NUMBER | line_items | 
R640 | NUMBER | line_items | 
R641 | NUMBER | line_items | 
R642 | NUMBER | line_items | 
R643 | NUMBER | line_items | 
R644 | NUMBER | line_items | 
R645 | NUMBER | line_items | 
R646 | NUMBER | line_items | 
R647 | NUMBER | line_items | 
R648 | NUMBER | line_items | 
R649 | NUMBER | line_items | 
R650 | NUMBER | line_items | 
R651 | NUMBER | line_items | 
R652 | NUMBER | line_items | 
R653 | NUMBER | line_items | 
R654 | NUMBER | line_items | 
R655 | NUMBER | line_items | 
R656 | NUMBER | line_items | 
R657 | NUMBER | line_items | 
R658 | NUMBER | line_items | 
R659 | NUMBER | line_items | 
R660 | NUMBER | line_items | 
R661 | NUMBER | line_items | 
R662 | NUMBER | line_items | 
R663 | NUMBER | line_items | 
R664 | NUMBER | line_items | 
R665 | NUMBER | line_items | ZERO_STANDING
R666 | NUMBER | line_items | 
R667 | NUMBER | line_items | 
R668 | NUMBER | line_items | 
R669 | NUMBER | line_items | 
R670 | NUMBER | line_items | 
R671 | NUMBER | line_items | 
R672 | NUMBER | line_items | 
R673 | NUMBER | line_items | 
R674 | NUMBER | line_items | 
R675 | NUMBER | line_items | 
R676 | NUMBER | line_items | 
R677 | NUMBER | line_items | 
R678 | NUMBER | line_items | 
R679 | NUMBER | line_items | 
R680 | NUMBER | line_items | 
R681 | NUMBER | line_items | 
R682 | NUMBER | line_items | ZERO_STANDING
R683 | NUMBER | line_items | 
R684 | NUMBER | line_items | 
R685 | NUMBER | line_items | 
R686 | NUMBER | line_items | 
R687 | NUMBER | line_items | 
R688 | NUMBER | line_items | 
R689 | NUMBER | line_items | 
R690 | NUMBER | line_items | 
R691 | NUMBER | auditor_paras | 
R692 | NUMBER | auditor_paras | 
R693 | NUMBER | auditor_paras | 
R694 | NUMBER | auditor_paras | 
R695 | NUMBER | auditor_paras | 
R696 | NUMBER | auditor_paras | 
R697 | NUMBER | auditor_paras | 
R698 | NUMBER | auditor_paras | 
R699 | NUMBER | auditor_paras | 
R700 | NUMBER | auditor_paras | UNAUDITED_ASSOCIATE_INFO
R701 | NUMBER | auditor_paras | 
R702 | NUMBER | auditor_paras | UNAUDITED_ASSOCIATE_INFO
R703 | NUMBER | agenda_items | 
R704 | NUMBER | signature_blocks | 
R705 | NUMBER | agenda_items | 
R706 | NUMBER | agenda_items | 
R707 | NUMBER | signature_blocks | 
R708 | NUMBER | auditor_paras | 
R709 | NUMBER | auditor_paras | 
R710 | NUMBER | auditor_paras | 
R711 | NUMBER | auditor_paras | 
R712 | NUMBER | identifiers_other_numbers | CIN_PREFIX_MISMATCH(L vs U)
R713 | NUMBER | identifiers_other_numbers | CIN_PREFIX_MISMATCH(L vs U)
R714 | NUMBER | identifiers_other_numbers | 
R715 | NUMBER | identifiers_other_numbers | 
R716 | NUMBER | identifiers_other_numbers | 
R717 | NUMBER | auditor_paras | 
R718 | NUMBER | auditor_paras | 
R719 | NUMBER | auditor_paras | 
R720 | NUMBER | auditor_paras | 
R721 | NUMBER | auditor_paras | 
R722 | NUMBER | identifiers_other_numbers | 
R723 | NUMBER | signature_blocks | SIGNATURE_BEFORE_MEETING_END(signed 12:3x, meeting concluded 15:00)
R724 | NUMBER | signature_blocks | SIGNATURE_BEFORE_MEETING_END(signed 12:3x, meeting concluded 15:00)
R725 | ENTITY | agenda_items | 
R726 | ENTITY | agenda_items | 
R727 | ENTITY | agenda_items | 
R728 | ENTITY | agenda_items | 
R729 | ENTITY | signature_blocks | 
R730 | ENTITY | auditor_paras | 
R731 | ENTITY | auditor_paras | 
R732 | ENTITY | auditor_paras | 
R733 | ENTITY | entities | 
R734 | ENTITY | entities | 
R735 | ENTITY | entities | ENTITY_CHANGE(renamed, 'formerly')
R736 | ENTITY | entities | ENTITY_CHANGE(renamed, 'formerly')
R737 | ENTITY | entities | ENTITY_CHANGE(new sub 04-Aug-2026)
R738 | ENTITY | entities | 
R739 | ENTITY | entities | 
R740 | ENTITY | entities | ENTITY_CHANGE(associate ceased 29-May-2026)
R741 | ENTITY | entities | 
R742 | ENTITY | entities | 
R743 | ENTITY | entities | 
R744 | ENTITY | entities | 
R745 | ENTITY | entities | 
R746 | ENTITY | entities | ENTITY_CHANGE(unverifiable, w.e.f. 11-Apr-2025; no prior ledger)
R747 | ENTITY | entities | 
R748 | ENTITY | entities | 
R749 | ENTITY | other_entities_refs | 
R750 | ENTITY | signature_blocks | 
R751 | ENTITY | other_entities_refs | 
R752 | ENTITY | signature_blocks | 
R753 | ENTITY | agenda_items | 
R754 | ENTITY | other_entities_refs | 
R755 | ENTITY | auditor_paras | 
R756 | ENTITY | auditor_paras | 
R757 | ENTITY | auditor_paras | 
R758 | ENTITY | signature_blocks | 
R759 | ENTITY | auditor_paras | 
R760 | FORWARD | forward_looking | 
R761 | FORWARD | forward_looking | 
R762 | FORWARD | forward_looking | 
R763 | FORWARD | forward_looking | 
R764 | FORWARD | forward_looking | 
R765 | FORWARD | forward_looking | 
R766 | FORWARD | auditor_paras | 
R767 | FORWARD | auditor_paras | 
R768 | DATE | agenda_items | 
R769 | DATE | agenda_items | 
R770 | DATE | agenda_items | 
R771 | DATE | signature_blocks | 
R772 | DATE | auditor_paras | 
R773 | DATE | auditor_paras | 
R774 | DATE | auditor_paras | 
R775 | DATE | auditor_paras | 
R776 | DATE | auditor_paras | 
R777 | DATE | auditor_paras | 
R778 | DATE | entities | ENTITY_CHANGE(new sub 04-Aug-2026)
R779 | DATE | entities | ENTITY_CHANGE(associate ceased 29-May-2026)
R780 | DATE | entities | ENTITY_CHANGE(unverifiable, w.e.f. 11-Apr-2025; no prior ledger)
R781 | DATE | dates | 
R782 | DATE | dates | 
R783 | DATE | dates | 
R784 | DATE | dates | 
R785 | DATE | dates | 
R786 | DATE | dates | 
R787 | DATE | dates | 
R788 | DATE | dates | 
R789 | DATE | signature_blocks | 
R790 | DATE | dates | 
R791 | DATE | auditor_paras | 
R792 | DATE | auditor_paras | 
R793 | DATE | dates | 
R794 | DATE | dates | 
R795 | DATE | dates | 
R796 | DATE | signature_blocks | 
R797 | DATE | dates | 
R798 | DATE | dates | 
R799 | DATE | dates | 
R800 | QUALIFIER | qualifiers | 
R801 | QUALIFIER | qualifiers | 
R802 | QUALIFIER | qualifiers | 
R803 | QUALIFIER | qualifiers | 
R804 | QUALIFIER | qualifiers | 
R805 | QUALIFIER | qualifiers | 
R806 | QUALIFIER | qualifiers | 
R807 | QUALIFIER | qualifiers | 
R808 | QUALIFIER | qualifiers | 
R809 | QUALIFIER | notes_unnumbered_footnote | 
R810 | QUALIFIER | notes_unnumbered_footnote | 
R811 | QUALIFIER | notes_unnumbered_footnote | 
R812 | QUALIFIER | qualifiers | 
R813 | QUALIFIER | notes_numbered | 
R814 | QUALIFIER | notes_numbered | 
R815 | QUALIFIER | notes_numbered | 
R816 | QUALIFIER | notes_numbered | 
R817 | QUALIFIER | notes_numbered | 
R818 | QUALIFIER | qualifiers | 
R819 | QUALIFIER | qualifiers | 
R820 | QUALIFIER | notes_unnumbered_footnote | 
R821 | QUALIFIER | qualifiers | 
R822 | QUALIFIER | qualifiers | 
R823 | QUALIFIER | qualifiers | 
R824 | QUALIFIER | qualifiers | 
R825 | QUALIFIER | qualifiers | 
R826 | QUALIFIER | qualifiers | 
R827 | QUALIFIER | notes_numbered | 
R828 | QUALIFIER | notes_numbered | 
R829 | QUALIFIER | notes_numbered | 
R830 | QUALIFIER | notes_numbered | 
R831 | QUALIFIER | notes_numbered | 
R832 | QUALIFIER | notes_numbered | 
R833 | QUALIFIER | qualifiers | 
R834 | QUALIFIER | qualifiers | 
R835 | QUALIFIER | notes_unnumbered_footnote | 
R836 | QUALIFIER | auditor_paras | 
R837 | QUALIFIER | auditor_paras | 
R838 | QUALIFIER | auditor_paras | UNAUDITED_ASSOCIATE_INFO
R839 | QUALIFIER | auditor_paras | UNAUDITED_ASSOCIATE_INFO
R840 | QUALIFIER | auditor_paras | 
R841 | QUALIFIER | auditor_paras | 
R842 | QUALIFIER | entities | ENTITY_CHANGE(associate ceased 29-May-2026)
R843 | QUALIFIER | entities | ENTITY_CHANGE(new sub 04-Aug-2026)
R844 | QUALIFIER | entities | ENTITY_CHANGE(unverifiable, w.e.f. 11-Apr-2025; no prior ledger)
R845 | QUALIFIER | qualifiers | 
R846 | QUALIFIER | qualifiers | 
R847 | QUALIFIER | qualifiers | CIN_PREFIX_MISMATCH(L vs U)
R848 | QUALIFIER | agenda_items | 
R849 | QUALIFIER | agenda_items | 

MISSING_FROM_STRUCTURED: none found.
