# LEDGER: SYNGENE q2fy27 results (A2 enumerator)
source: runs/syngene-q2fy27/extracted/syngene-results-q2fy27-structured.md (A1 rows R001-R828); values live there, not here.
units: Rs million per A1 (x0.1 to Rs Crores). Prior-quarter ledger: none available.

=== A2 COUNT TEST ===
category: notes          grep_count: 9    sweep_count: 9    match: yes   (bare numerals l.455-463 = 9; nine note texts)
category: line_items     grep_count: 227  sweep_count: 227  match: yes   (distinct page|line on NUMBER rows pages 2-7 via shell = 227; label-boundary sweep = 227; 667 cells reconcile)
category: zero_standing  grep_count: 15   sweep_count: 15   match: yes   (dash cells in 15 line items)
category: agenda_items   grep_count: 1    sweep_count: 1    match: yes   (board letter; plus 2 non-agenda rows: times, website)
category: auditor_paras  grep_count: 12   sweep_count: 12   match: yes   (11 numbered l.525-618 + 1 unnumbered Master Circular para l.547)
category: entities       grep_count: 5    sweep_count: 5    match: yes   (note 2 list + parent + trust; auditor list of 5 agrees)
category: signatures     grep_count: 4    sweep_count: 4    match: yes
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 828 | ids_referenced_in_ledger: 828 | orphan_ids: [] | match: yes


### 1. Numbered notes (note number mapped by elimination, see R807)

| Note | Subject | Structured IDs | A2 flags | Cross-ref / materiality |
|---|---|---|---|---|
| Note 1 | basis of preparation / Audit Committee review | R703,R716-R717,R764-R765,R808-R809 |  | fulltext l.497-502; number mapped by elimination (R807) |
| Note 2 | consolidation scope / subsidiaries list | R706,R713-R714,R810,R812 |  | l.504-509; see entity table |
| Note 3 | single segment: CRMS | R715,R813 |  | l.495 |
| Note 4 | allotment of 729,727 shares to Syngene Employees Welfare Trust | R677-R678,R706-R707,R754,R795-R796 |  | l.471-473; markers on paid-up capital |
| Note 5 | USA biologics site: CWIP Rs 4,876m incl pre-operative Rs 1,246m | R679-R682,R708-R710,R728,R755-R756,R797-R798,R814-R815 | FORWARD,MGMT_VIEW | l.474-478; capitalisation is management view (FORWARD R728); pre-operative costs 585 to 1,246 in 6M per A1 values |
| Note 6 | New Labour Codes: gratuity exceptional FY26 | R683-R684,R711,R729,R757-R758,R793-R794,R816,R819 | FORWARD,EXCEPTIONAL | l.479-485; ongoing assessment (FORWARD R729) |
| Note 7 | termination benefits as exceptional items | R685-R687,R759,R793-R794,R817-R818 | EXCEPTIONAL | l.486-489; Rs 303m FY26, 135m Q1, 67m Q2: recurs across three periods |
| Note 8 | SMSL voluntary liquidation | R712,R730-R732,R760-R763,R769,R811 | FORWARD,ENTITY_CHANGE | l.490-494; entity name inconsistency |
| Note 9 | regrouping / reclassification of prior periods | R806 |  | l.463; standard regrouping note, nothing quantified |

### 1b. Unnumbered notes, footnotes, markers

| IDs | Item | A2 flags | Note |
|---|---|---|---|
| R801,R802 | See accompanying notes marker (cons/stand) |  |  |
| R793,R794 | [refer note 6 & 7] on Exceptional Items |  |  |
| R795,R796 | [refer note 4] on paid-up capital |  |  |
| R797,R798 | [refer note 5] on CWIP |  |  |
| R799,R800 | EPS annualised/not-annualised footnote |  | FY26 column annualised, five others not |
| R803,R804 | face value and Other Equity definition |  |  |
| R805 | Notes header |  |  |
| R807 | note numbers 1-8 detached bare numerals | FOOTNOTE_UNRESOLVED | mapping by elimination, A1 flagged |
| R787,R788,R789,R790,R791,R792 | audit-status column labels |  |  |
| R781,R782,R783,R784,R785,R786 | unit declarations |  |  |
| R826 | board letter qualifier: unaudited, LRR enclosed |  |  |

### 2. Line items, every financial table (IDs cover all period cells)

| Statement | Pg | Line | A1 label | IDs | Cells | A2 flags | Note |
|---|---|---|---|---|---|---|---|
| Cons P&L | 2 | 76 | a) Revenue from operations | R001-R006 | 6 |  |  |
| Cons P&L | 2 | 77 | b) Other Income | R007-R012 | 6 |  |  |
| Cons P&L | 2 | 78 | Total Income | R013-R018 | 6 |  |  |
| Cons P&L | 2 | 80 | a) Cost of chemicals, reagents and consumables consumed | R019-R024 | 6 |  |  |
| Cons P&L | 2 | 81 | b) Changes in inventories of finished goods and work-in-prog | R025-R030 | 6 |  |  |
| Cons P&L | 2 | 82 | c) Employee benefits expense | R031-R036 | 6 |  |  |
| Cons P&L | 2 | 83 | d) Finance costs | R037-R042 | 6 |  |  |
| Cons P&L | 2 | 84 | e) Depreciation and amortisation expense | R043-R048 | 6 |  |  |
| Cons P&L | 2 | 85 | f) Other expenses | R049-R054 | 6 |  |  |
| Cons P&L | 2 | 86 | g) Foreign exchange fluctuation loss, net | R055-R060 | 6 |  |  |
| Cons P&L | 2 | 87 | Total expenses | R061-R066 | 6 |  |  |
| Cons P&L | 2 | 88 | Profit before tax and exceptional items (1-2) | R067-R072 | 6 |  |  |
| Cons P&L | 2 | 89 | Exceptional Items, net gain/ (loss) [refer note 6 & 7] | R073-R078 | 6 | ZERO_STANDING | nil cells R075,R077; partial-period nil |
| Cons P&L | 2 | 90 | Profit before tax (3-4) | R079-R084 | 6 |  |  |
| Cons P&L | 2 | 92 | Current tax | R085-R090 | 6 |  |  |
| Cons P&L | 2 | 93 | Deferred tax | R091-R096 | 6 |  |  |
| Cons P&L | 2 | 94 | Total tax expense | R097-R102 | 6 |  |  |
| Cons P&L | 2 | 95 | Profit for the period / year (5-6) | R103-R108 | 6 |  |  |
| Cons P&L | 2 | 97 | (A) (i) Items that will not be reclassified to profit or (lo | R109-R114 | 6 |  |  |
| Cons P&L | 2 | 98 | (ii) Income tax relating to items that will not be reclassif | R115-R120 | 6 |  |  |
| Cons P&L | 2 | 99 | (B) (i) Items that will be reclassified to profit or (loss) | R121-R126 | 6 |  |  |
| Cons P&L | 2 | 100 | (ii) Income tax relating to items that will be reclassified  | R127-R132 | 6 |  |  |
| Cons P&L | 2 | 101 | Other comprehensive income for the period / year, net of tax | R133-R138 | 6 |  |  |
| Cons P&L | 2 | 102 | Total comprehensive income for the period / year (7+8) | R139-R144 | 6 |  |  |
| Cons P&L | 2 | 103 | Paid-up equity share capital (Face value of Rs.10 each) [ref | R145-R150 | 6 |  |  |
| Cons P&L | 2 | 104 | Reserves excluding revaluation reserves as per balance sheet | R151 | 1 |  | single value |
| Cons P&L | 2 | 106 | a) Basic | R152-R157 | 6 |  |  |
| Cons P&L | 2 | 107 | b) Diluted | R158-R163 | 6 |  |  |
| Cons BS | 3 | 137 | Property, plant and equipment | R164-R165 | 2 |  |  |
| Cons BS | 3 | 138 | Capital work-in-progress [refer note 5] | R166-R167 | 2 |  |  |
| Cons BS | 3 | 139 | Right-of-use assets | R168-R169 | 2 |  |  |
| Cons BS | 3 | 140 | Investment property | R170-R171 | 2 |  |  |
| Cons BS | 3 | 141 | Other intangible assets | R172-R173 | 2 |  |  |
| Cons BS | 3 | 142 | Intangible assets under development | R174-R175 | 2 |  |  |
| Cons BS | 3 | 144 | (i) Investments | R176-R177 | 2 |  |  |
| Cons BS | 3 | 145 | (ii) Derivative assets | R178-R179 | 2 |  |  |
| Cons BS | 3 | 146 | (iii) Other financial assets | R180-R181 | 2 |  |  |
| Cons BS | 3 | 147 | Deferred tax assets (net) | R182-R183 | 2 |  |  |
| Cons BS | 3 | 148 | Income tax assets (net) | R184-R185 | 2 |  |  |
| Cons BS | 3 | 149 | Other non-current assets | R186-R187 | 2 |  |  |
| Cons BS | 3 | 150 | Total non-current assets | R188-R189 | 2 |  |  |
| Cons BS | 3 | 152 | Inventories | R190-R191 | 2 |  |  |
| Cons BS | 3 | 154 | (i) Investments | R192-R193 | 2 |  |  |
| Cons BS | 3 | 155 | (ii) Trade receivables | R194-R195 | 2 |  |  |
| Cons BS | 3 | 156 | (iii) Cash and cash equivalents | R196-R197 | 2 |  |  |
| Cons BS | 3 | 157 | (iv) Bank balances other than (iii) above | R198-R199 | 2 |  |  |
| Cons BS | 3 | 158 | (v) Derivative assets | R200-R201 | 2 |  |  |
| Cons BS | 3 | 159 | (vi) Other financial assets | R202-R203 | 2 |  |  |
| Cons BS | 3 | 160 | Other current assets | R204-R205 | 2 |  |  |
| Cons BS | 3 | 161 | Total current assets | R206-R207 | 2 |  |  |
| Cons BS | 3 | 162 | Total assets | R208-R209 | 2 |  |  |
| Cons BS | 3 | 165 | Equity share capital | R210-R211 | 2 |  |  |
| Cons BS | 3 | 166 | Other equity | R212-R213 | 2 |  |  |
| Cons BS | 3 | 167 | Total equity | R214-R215 | 2 |  |  |
| Cons BS | 3 | 171 | (ii) Lease liabilities | R216-R217 | 2 |  |  |
| Cons BS | 3 | 172 | (iii) Derivative liabilities | R218-R219 | 2 |  |  |
| Cons BS | 3 | 173 | (iii) Other financial liabilities | R220-R221 | 2 |  |  |
| Cons BS | 3 | 174 | Provisions | R222-R223 | 2 | ZERO_STANDING | nil cells R222; partial-period nil |
| Cons BS | 3 | 175 | Other non-current liabilities | R224-R225 | 2 |  |  |
| Cons BS | 3 | 176 | Total non-current liabilities | R226-R227 | 2 |  |  |
| Cons BS | 3 | 179 | (i) Borrowings | R228-R229 | 2 |  |  |
| Cons BS | 3 | 180 | (ii) Lease liabilities | R230-R231 | 2 |  |  |
| Cons BS | 3 | 182 | total outstanding dues of micro and small enterprises | R232-R233 | 2 |  |  |
| Cons BS | 3 | 183 | total outstanding dues of creditors other than micro and sma | R234-R235 | 2 |  |  |
| Cons BS | 3 | 184 | (iv) Derivative liabilities | R236-R237 | 2 |  |  |
| Cons BS | 3 | 185 | (v) Other financial liabilities | R238-R239 | 2 |  |  |
| Cons BS | 3 | 186 | Provisions | R240-R241 | 2 |  |  |
| Cons BS | 3 | 187 | Current tax liabilities (net) | R242-R243 | 2 |  |  |
| Cons BS | 3 | 188 | Other current liabilities | R244-R245 | 2 |  |  |
| Cons BS | 3 | 189 | Total current liabilities | R246-R247 | 2 |  |  |
| Cons BS | 3 | 190 | Total equity and liabilities | R248-R249 | 2 |  |  |
| Cons CF | 4 | 204 | Profit for the year | R250-R251 | 2 |  |  |
| Cons CF | 4 | 206 | Depreciation and amortisation expense | R252-R253 | 2 |  |  |
| Cons CF | 4 | 207 | (Gain)/loss on disposal of property, plant and equipment (ne | R254-R255 | 2 |  |  |
| Cons CF | 4 | 208 | Impairment allowances of doubtfull trade receivables | R256-R257 | 2 |  |  |
| Cons CF | 4 | 209 | Bad debts written off | R258-R259 | 2 | ZERO_STANDING | nil cells R258; partial-period nil |
| Cons CF | 4 | 210 | Advances to suppliers written off | R260-R261 | 2 | ZERO_STANDING | nil cells R261; partial-period nil |
| Cons CF | 4 | 211 | Share-based payment expenses (net) | R262-R263 | 2 |  |  |
| Cons CF | 4 | 212 | Interest expense | R264-R265 | 2 |  |  |
| Cons CF | 4 | 213 | Unrealised foreign exchange gain | R266-R267 | 2 |  |  |
| Cons CF | 4 | 214 | Net gain on sale of current investments | R268-R269 | 2 |  |  |
| Cons CF | 4 | 215 | Interest income | R270-R271 | 2 |  |  |
| Cons CF | 4 | 216 | Interest on Income tax refund | R272-R273 | 2 | ZERO_STANDING | nil cells R273; partial-period nil |
| Cons CF | 4 | 217 | Tax expenses | R274-R275 | 2 |  |  |
| Cons CF | 4 | 218 | Operating profit before working capital changes | R276-R277 | 2 |  |  |
| Cons CF | 4 | 220 | Decrease/ (increase) in inventories | R278-R279 | 2 |  |  |
| Cons CF | 4 | 221 | Decrease/ (increase) in trade receivables | R280-R281 | 2 |  |  |
| Cons CF | 4 | 222 | Decrease/ (increase) in other financial and other assets | R282-R283 | 2 |  |  |
| Cons CF | 4 | 223 | Increase/ (decrease) in trade payables, provisions, financia | R284-R285 | 2 |  |  |
| Cons CF | 4 | 224 | Cash generated from/ (used in) operations | R286-R287 | 2 |  |  |
| Cons CF | 4 | 225 | Income taxes paid (net of refunds) | R288-R289 | 2 |  |  |
| Cons CF | 4 | 226 | Net cash flow generated from/ (used in) operating activities | R290-R291 | 2 |  |  |
| Cons CF | 4 | 228 | Purchase of property, plant and equipment inlcuding investme | R292-R293 | 2 |  |  |
| Cons CF | 4 | 229 | Proceeds from sale of property plant and equipments | R294-R295 | 2 |  |  |
| Cons CF | 4 | 230 | Purchase of intangible assets including intangible assets un | R296-R297 | 2 |  |  |
| Cons CF | 4 | 231 | Investment in equity shares | R298-R299 | 2 | ZERO_STANDING | nil cells R299; partial-period nil |
| Cons CF | 4 | 232 | Investment in bank deposits and inter corporate deposits | R300-R301 | 2 |  |  |
| Cons CF | 4 | 233 | Redemption/maturity of bank deposits and inter corporate dep | R302-R303 | 2 |  |  |
| Cons CF | 4 | 234 | Interest received | R304-R305 | 2 |  |  |
| Cons CF | 4 | 235 | Proceeds from sale of current investments | R306-R307 | 2 |  |  |
| Cons CF | 4 | 236 | Purchase of current investments | R308-R309 | 2 |  |  |
| Cons CF | 4 | 237 | Net cash flow generated from/ (used in) investing activities | R310-R311 | 2 |  |  |
| Cons CF | 4 | 239 | Proceeds from issue of equity shares | R312-R313 | 2 |  |  |
| Cons CF | 4 | 240 | Proceeds/ (repayments) from short term borrowings, net | R314-R315 | 2 |  |  |
| Cons CF | 4 | 241 | Lease liabilities paid (including interest) | R316-R317 | 2 |  |  |
| Cons CF | 4 | 242 | Dividend paid | R318-R319 | 2 |  |  |
| Cons CF | 4 | 243 | Interest paid | R320-R321 | 2 |  |  |
| Cons CF | 4 | 244 | Net cash flow generated from/ (used in) financing activities | R322-R323 | 2 |  |  |
| Cons CF | 4 | 245 | Net increase/(decrease) in cash and cash equivalents (1+2+3) | R324-R325 | 2 |  |  |
| Cons CF | 4 | 246 | Effect of exchange difference on cash and cash equivalents h | R326-R327 | 2 |  |  |
| Cons CF | 4 | 247 | Cash and cash equivalents at the beginning of the period/ ye | R328-R329 | 2 |  |  |
| Cons CF | 4 | 248 | Cash and cash equivalents at the end of the period/ year (4+ | R330-R331 | 2 |  |  |
| Cons CF | 4 | 250 | Balances with banks | R332-R333 | 2 |  |  |
| Cons CF | 4 | 251 | Total cash and cash equivalents | R334-R335 | 2 |  |  |
| Stand P&L | 5 | 267 | a) Revenue from operations | R336-R341 | 6 |  |  |
| Stand P&L | 5 | 268 | b) Other Income | R342-R347 | 6 |  |  |
| Stand P&L | 5 | 269 | Total Income | R348-R353 | 6 |  |  |
| Stand P&L | 5 | 271 | a) Cost of chemicals, reagents and consumables consumed | R354-R359 | 6 |  |  |
| Stand P&L | 5 | 272 | b) Changes in inventories of finished goods and work-in-prog | R360-R365 | 6 |  |  |
| Stand P&L | 5 | 273 | c) Employee benefits expense | R366-R371 | 6 |  |  |
| Stand P&L | 5 | 274 | d) Finance costs | R372-R377 | 6 |  |  |
| Stand P&L | 5 | 275 | e) Depreciation and amortisation expense | R378-R383 | 6 |  |  |
| Stand P&L | 5 | 276 | f) Other expenses | R384-R389 | 6 |  |  |
| Stand P&L | 5 | 277 | g) Foreign exchange fluctuation loss, net | R390-R395 | 6 |  |  |
| Stand P&L | 5 | 278 | Total expenses | R396-R401 | 6 |  |  |
| Stand P&L | 5 | 279 | Profit before tax and exceptional items (1-2) | R402-R407 | 6 |  |  |
| Stand P&L | 5 | 280 | Exceptional Items, net gain/ (loss) [refer note 6 & 7] | R408-R413 | 6 | ZERO_STANDING | nil cells R410,R412; partial-period nil |
| Stand P&L | 5 | 281 | Profit before tax (3-4) | R414-R419 | 6 |  |  |
| Stand P&L | 5 | 283 | Current tax | R420-R425 | 6 | ZERO_STANDING | nil cells R421; partial-period nil |
| Stand P&L | 5 | 284 | Deferred tax | R426-R431 | 6 |  |  |
| Stand P&L | 5 | 285 | Total tax expense | R432-R437 | 6 |  |  |
| Stand P&L | 5 | 286 | Profit for the period / year (5-6) | R438-R443 | 6 |  |  |
| Stand P&L | 5 | 288 | (A) (i) Items that will not be reclassified to profit or (lo | R444-R449 | 6 |  |  |
| Stand P&L | 5 | 289 | (ii) Income tax relating to items that will not be reclassif | R450-R455 | 6 |  |  |
| Stand P&L | 5 | 290 | unlabelled row between OCI A(ii) and B(i) | R456-R457 | 2 | ZERO_STANDING,COLUMN_UNRESOLVED | nil cells R456-R457; nil in ALL periods ; A1 flagged column unresolved (R827/R828) |
| Stand P&L | 5 | 291 | (B) (i) Items that will be reclassified to profit or (loss) | R458-R463 | 6 |  |  |
| Stand P&L | 5 | 292 | (ii) Income tax relating to items that will be reclassified  | R464-R469 | 6 |  |  |
| Stand P&L | 5 | 293 | Other comprehensive income for the period / year, net of tax | R470-R475 | 6 |  |  |
| Stand P&L | 5 | 294 | Total comprehensive income for the period / year (7+8) | R476-R481 | 6 |  |  |
| Stand P&L | 5 | 295 | Paid-up equity share capital (Face value of Rs.10 each) [ref | R482-R487 | 6 |  |  |
| Stand P&L | 5 | 296 | Reserves excluding revaluation reserves as per balance sheet | R488 | 1 |  | single value |
| Stand P&L | 5 | 298 | a) Basic | R489-R494 | 6 |  |  |
| Stand P&L | 5 | 299 | b) Diluted | R495-R500 | 6 |  |  |
| Stand BS | 6 | 330 | Property, plant and equipment | R501-R502 | 2 |  |  |
| Stand BS | 6 | 331 | Capital work-in-progress [refer note 5] | R503-R504 | 2 |  |  |
| Stand BS | 6 | 332 | Right-of-use assets | R505-R506 | 2 |  |  |
| Stand BS | 6 | 333 | Investment property | R507-R508 | 2 |  |  |
| Stand BS | 6 | 334 | Other intangible assets | R509-R510 | 2 |  |  |
| Stand BS | 6 | 335 | Intangible assets under development | R511-R512 | 2 |  |  |
| Stand BS | 6 | 337 | (i) Investments | R513-R514 | 2 |  |  |
| Stand BS | 6 | 338 | (ii) Derivative assets | R515-R516 | 2 |  |  |
| Stand BS | 6 | 339 | (iii) Other financial assets | R517-R518 | 2 |  |  |
| Stand BS | 6 | 340 | Deferred tax assets (net) | R519-R520 | 2 |  |  |
| Stand BS | 6 | 341 | Income tax assets (net) | R521-R522 | 2 |  |  |
| Stand BS | 6 | 342 | Other non-current assets | R523-R524 | 2 |  |  |
| Stand BS | 6 | 343 | Total non-current assets | R525-R526 | 2 |  |  |
| Stand BS | 6 | 345 | Inventories | R527-R528 | 2 |  |  |
| Stand BS | 6 | 347 | (i) Investments | R529-R530 | 2 |  |  |
| Stand BS | 6 | 348 | (ii) Trade receivables | R531-R532 | 2 |  |  |
| Stand BS | 6 | 349 | (iii) Cash and cash equivalents | R533-R534 | 2 |  |  |
| Stand BS | 6 | 350 | (iv) Bank balances other than (iii) above | R535-R536 | 2 |  |  |
| Stand BS | 6 | 351 | (v) Derivative assets | R537-R538 | 2 |  |  |
| Stand BS | 6 | 352 | (vi) Other financial assets | R539-R540 | 2 |  |  |
| Stand BS | 6 | 353 | Other current assets | R541-R542 | 2 |  |  |
| Stand BS | 6 | 354 | Total current assets | R543-R544 | 2 |  |  |
| Stand BS | 6 | 355 | Total assets | R545-R546 | 2 |  |  |
| Stand BS | 6 | 358 | Equity share capital | R547-R548 | 2 |  |  |
| Stand BS | 6 | 359 | Other equity | R549-R550 | 2 |  |  |
| Stand BS | 6 | 360 | Total equity | R551-R552 | 2 |  |  |
| Stand BS | 6 | 364 | (i) Lease liabilities | R553-R554 | 2 |  |  |
| Stand BS | 6 | 365 | (ii) Derivative liabilities | R555-R556 | 2 |  |  |
| Stand BS | 6 | 366 | (iii) Other financial liabilities | R557-R558 | 2 |  |  |
| Stand BS | 6 | 367 | Provisions | R559-R560 | 2 | ZERO_STANDING | nil cells R559; partial-period nil |
| Stand BS | 6 | 368 | Other non-current liabilities | R561-R562 | 2 |  |  |
| Stand BS | 6 | 369 | Total non-current liabilities | R563-R564 | 2 |  |  |
| Stand BS | 6 | 372 | (i) Lease liabilities | R565-R566 | 2 |  |  |
| Stand BS | 6 | 374 | total outstanding dues of micro and small enterprises | R567-R568 | 2 |  |  |
| Stand BS | 6 | 375 | total outstanding dues of creditors other than micro and sma | R569-R570 | 2 |  |  |
| Stand BS | 6 | 376 | (iII) Derivative liabilities | R571-R572 | 2 |  |  |
| Stand BS | 6 | 377 | (iv) Other financial liabilities | R573-R574 | 2 |  |  |
| Stand BS | 6 | 378 | Provisions | R575-R576 | 2 |  |  |
| Stand BS | 6 | 379 | Current tax liabilities (net) | R577-R578 | 2 |  |  |
| Stand BS | 6 | 380 | Other current liabilities | R579-R580 | 2 |  |  |
| Stand BS | 6 | 381 | Total current liabilities | R581-R582 | 2 |  |  |
| Stand BS | 6 | 382 | Total equity and liabilities | R583-R584 | 2 |  |  |
| Stand CF | 7 | 396 | Profit for the year | R585-R586 | 2 |  |  |
| Stand CF | 7 | 398 | Depreciation and amortisation expense | R587-R588 | 2 |  |  |
| Stand CF | 7 | 399 | (Gain)/loss on disposal of property, plant and equipment (ne | R589-R590 | 2 |  |  |
| Stand CF | 7 | 400 | Impairment allowances of doubtfull trade receivables | R591-R592 | 2 |  |  |
| Stand CF | 7 | 401 | Bad debts written off | R593-R594 | 2 | ZERO_STANDING | nil cells R593; partial-period nil |
| Stand CF | 7 | 402 | Provision for doubtful advances to supplier, column unresol~ | R595 | 1 | COLUMN_UNRESOLVED | A1 flagged column unresolved (R827/R828) ; single value |
| Stand CF | 7 | 403 | Share-based payment expenses (net) | R596-R597 | 2 |  |  |
| Stand CF | 7 | 404 | Interest expense | R598-R599 | 2 |  |  |
| Stand CF | 7 | 405 | Unrealised foreign exchange (gain)/loss | R600-R601 | 2 | ZERO_STANDING | nil cells R601; partial-period nil |
| Stand CF | 7 | 406 | Net gain on sale of current investments | R602-R603 | 2 |  |  |
| Stand CF | 7 | 407 | Interest on Income tax refund | R604-R605 | 2 | ZERO_STANDING | nil cells R605; partial-period nil |
| Stand CF | 7 | 408 | Interest income | R606-R607 | 2 |  |  |
| Stand CF | 7 | 409 | Tax expenses | R608-R609 | 2 |  |  |
| Stand CF | 7 | 410 | Operating profit before working capital changes | R610-R611 | 2 |  |  |
| Stand CF | 7 | 412 | Decrease/ (increase) in inventories | R612-R613 | 2 |  |  |
| Stand CF | 7 | 413 | Decrease/ (increase) in trade receivables | R614-R615 | 2 |  |  |
| Stand CF | 7 | 414 | Decrease/ (increase) in financial and other assets | R616-R617 | 2 |  |  |
| Stand CF | 7 | 415 | Increase/ (decrease) in trade payables, provisions, financia | R618-R619 | 2 |  |  |
| Stand CF | 7 | 416 | Cash generated from/ (used in) operations | R620-R621 | 2 |  |  |
| Stand CF | 7 | 417 | Income taxes paid (net of refunds) | R622-R623 | 2 |  |  |
| Stand CF | 7 | 418 | Net cash flow generated from/ (used in) operating activities | R624-R625 | 2 |  |  |
| Stand CF | 7 | 420 | Purchase of property, plant and equipment inlcuding investme | R626-R627 | 2 |  |  |
| Stand CF | 7 | 421 | Proceeds from sale of property plant and equipments | R628-R629 | 2 |  |  |
| Stand CF | 7 | 422 | Purchase of intangible assets including intangible assets un | R630-R631 | 2 |  |  |
| Stand CF | 7 | 423 | Investment in equity shares | R632-R633 | 2 | ZERO_STANDING | nil cells R633; partial-period nil |
| Stand CF | 7 | 424 | Investment in bank deposits and inter corporate deposits | R634-R635 | 2 |  |  |
| Stand CF | 7 | 425 | Redemption/maturity of bank deposits and inter corporate dep | R636-R637 | 2 |  |  |
| Stand CF | 7 | 426 | Interest received | R638-R639 | 2 |  |  |
| Stand CF | 7 | 427 | Proceeds from sale of current investments | R640-R641 | 2 |  |  |
| Stand CF | 7 | 428 | Purchase of current investments | R642-R643 | 2 |  |  |
| Stand CF | 7 | 429 | Net cash flow generated from/ (used in) investing activities | R644-R645 | 2 |  |  |
| Stand CF | 7 | 431 | Proceed from issue of equity shares | R646-R647 | 2 |  |  |
| Stand CF | 7 | 432 | Lease liabilities paid (including interest) | R648-R649 | 2 |  |  |
| Stand CF | 7 | 433 | Dividend paid | R650-R651 | 2 |  |  |
| Stand CF | 7 | 434 | Interest paid | R652-R653 | 2 | ZERO_STANDING | nil cells R652; partial-period nil |
| Stand CF | 7 | 435 | Net cash flow generated from / (used in) financing activitie | R654-R655 | 2 |  |  |
| Stand CF | 7 | 436 | Net increase/(decrease) in cash and cash equivalents (1+2+3) | R656-R657 | 2 |  |  |
| Stand CF | 7 | 437 | Effect of exchange difference on cash and cash equivalents h | R658-R659 | 2 |  |  |
| Stand CF | 7 | 438 | Cash and cash equivalents at the beginning of the period/ ye | R660-R661 | 2 |  |  |
| Stand CF | 7 | 439 | Cash and cash equivalents at the end of the period/ year (4+ | R662-R663 | 2 |  |  |
| Stand CF | 7 | 441 | Balances with banks | R664-R665 | 2 |  |  |
| Stand CF | 7 | 442 | Total cash and cash equivalents | R666-R667 | 2 |  |  |

### 2b. ZERO_STANDING line items

| Statement | Pg | Line | IDs | Nil cells |
|---|---|---|---|---|
| Cons P&L | 2 | 89 | R073-R078 | R075,R077 |
| Cons BS | 3 | 174 | R222-R223 | R222 |
| Cons CF | 4 | 209 | R258-R259 | R258 |
| Cons CF | 4 | 210 | R260-R261 | R261 |
| Cons CF | 4 | 216 | R272-R273 | R273 |
| Cons CF | 4 | 231 | R298-R299 | R299 |
| Stand P&L | 5 | 280 | R408-R413 | R410,R412 |
| Stand P&L | 5 | 283 | R420-R425 | R421 |
| Stand P&L | 5 | 290 | R456-R457 | R456-R457 |
| Stand BS | 6 | 367 | R559-R560 | R559 |
| Stand CF | 7 | 401 | R593-R594 | R593 |
| Stand CF | 7 | 405 | R600-R601 | R601 |
| Stand CF | 7 | 407 | R604-R605 | R605 |
| Stand CF | 7 | 423 | R632-R633 | R633 |
| Stand CF | 7 | 434 | R652-R653 | R652 |

RESTATED cross-refs: cons CF end cash R330-R331 = R334-R335 = BS cash R196; standalone R662-R663 = R664-R667 = R533; paid-up capital R145-R150 = BS R210-R211 (cons), R482-R487 = R547-R548 (stand); cons Other Equity 31-Mar-26 R213 = P&L reserves R151; stand R550 = R488; EPS basic/diluted R152-R157 vs R158-R163; cons vs stand same values: derivative assets R178/R515, derivative liabilities R218/R555, other NC liabilities R224/R561, intangibles under development R174/R511.

### 3. Agenda items / board outcome

| Item | Subject | IDs | Note |
|---|---|---|---|
| A1 | Approve unaudited standalone+consolidated results, quarter and half year ended 30-Sep-2026 | R734,R735,R826,R703 | "inter-alia" wording, but no other agenda item named in letter; no AR/AGM/dividend/record date/director/auditor/ESOP/fund-raising item disclosed. Absence recorded, not inferred |
| A-time | Board meeting 15:15-18:30 IST (3h15m) | R736,R674,R675 | CS letter signed 18:53:30 (R737), after meeting end; Chairperson note signature 18:24:32 (R767), before meeting end |
| A-web | Results to be posted on company website | R727,R733 | FORWARD |

### 3b. Signature blocks

| Signatory | Timestamp | IDs | Note |
|---|---|---|---|
| Company Secretary (Chethan Yogesh) | 2026.10.27 18:53:30 | R700,R737 | after board end 18:30 |
| Chairperson (Kiran Mazumdar Shaw) | 2026.10.27 18:24:32 | R704,R767,R766,R705 | before board end 18:30 |
| Auditor consolidated (Sandeep Karnani) | 2026.10.27 18:33:37 | R719,R774 | after board end |
| Auditor standalone (Sandeep Karnani) | 2026.10.27 18:32:46 | R719,R780 | after board end; 51s before consolidated report |

### 4. Auditor report paragraphs

| Para | Content | IDs | Note |
|---|---|---|---|
| C-1 | Consolidated: review scope, period, Reg 33 | R768,R688,R717 | l.525 |
| C-2 | Consolidated: management responsibility (Ind AS 34) | none (no discrete value in structured file) | l.531 |
| C-3 | Consolidated: SRE 2410, moderate assurance, no audit opinion | R820,R689,R721 | l.538 |
| C-3a | Consolidated (unnumbered): SEBI Master Circular procedures | R722 | l.547 |
| C-4 | Consolidated: entities included (5) | R723,R724,R725,R732,R718 | l.549-554; Scientific Solutions (ii) carried via R713 |
| C-5 | Consolidated: review conclusion unmodified; no EoM, no going concern language | R821 | l.555 |
| C-6 | Consolidated: predecessor auditor comparatives / FY26 audit (Other Matter) | R822,R770,R771,R772,R720 | l.563; AUDITOR_CHANGE (S.R. Batliboi is the new firm) |
| C-sig | Consolidated: signature, partner, UDIN, date | R718,R719,R691,R692,R693,R773,R774 | l.569-584; signed 18:33:37 |
| S-1 | Standalone: review scope, period, Reg 33 | R775,R726 | l.592 |
| S-2 | Standalone: management responsibility | none (no discrete value in structured file) | l.597 |
| S-3 | Standalone: SRE 2410, moderate assurance | R823,R690 | l.603 |
| S-4 | Standalone: review conclusion unmodified | R824 | l.612 |
| S-5 | Standalone: predecessor auditor comparatives (Other Matter) | R825,R776,R777,R778 | l.618; AUDITOR_CHANGE |
| S-sig | Standalone: signature, partner, UDIN, date | R694,R695,R696,R779,R780 | l.624-638; signed 18:32:46 |

### 5. Consolidation entities

| Entity | Relationship | IDs | A2 flags | Note |
|---|---|---|---|---|
| Syngene International Limited (parent, incl. Syngene Employees Welfare Trust per note 2) | Holding Company | R697,R723,R726 |  |  |
| Syngene Employees Welfare Trust | Consolidated trust (LTIP vehicle); auditor entity (v) | R706,R707,R725,R810 |  | allottee of 729,727 shares |
| Syngene USA Inc. | Wholly-owned subsidiary; owns Baltimore biologics site | R708,R724,R709,R710 |  | CWIP Rs 4,876m sits here |
| Syngene Scientific Solutions Limited | Subsidiary (consolidated) | R713 |  | note 2 (ii) and auditor entity (ii) |
| Syngene Manufacturing Solutions Limited (SMSL) | Wholly-owned subsidiary, in liquidation w.e.f. 15-Jun-2026 | R712,R714,R731,R732,R811 | ENTITY_CHANGE,NAME_INCONSISTENT | status change: liquidation; note 8 text names it "Syngene Manufacturing Limited (SMSL)" (R712) vs "Syngene Manufacturing Solutions Limited" (R714); no prior list so add/remove cannot be diffed |

Annexures: none in the filing. Director profiles: none.

### 6. Reference numbers (letter ref, phone, PINs, scrip, UDIN, firm/membership, note figures): residual IDs (7)

| ID | pg | line | A1 context | A2 flags |
|---|---|---|---|---|
| R668 | 1 | 19 | letter reference number |  |
| R669 | 1 | 24 | company telephone |  |
| R670 | 1 | 23 | company PIN, Bengaluru |  |
| R671 | 1 | 32 | BSE address PIN |  |
| R672 | 1 | 32 | NSE address PIN |  |
| R673 | 1 | 33 | BSE scrip code |  |
| R676 | 1 | 39 | SEBI LODR regulation cited |  |

### 6. Other ENTITY mentions: residual IDs (4)

| ID | pg | line | A1 context | A2 flags |
|---|---|---|---|---|
| R698 | 1 | 29 | stock exchange addressee |  |
| R699 | 1 | 30 | stock exchange addressee |  |
| R701 | 1 | 25 | company identification number |  |
| R702 | 1 | 20 | registered office |  |

### 6. FORWARD statements not under a note: residual IDs (0)

| ID | pg | line | A1 context | A2 flags |
|---|---|---|---|---|

### 6. Dates and periods: residual IDs (16)

| ID | pg | line | A1 context | A2 flags |
|---|---|---|---|---|
| R738 | 2 | 112 | consolidated statement period heading |  |
| R739 | 5 | 304 | standalone statement period heading |  |
| R740 | 2 | 120 | P&L column period |  |
| R741 | 2 | 123 | P&L column period |  |
| R742 | 2 | 118 | P&L column period |  |
| R743 | 2 | 127 | P&L column period |  |
| R744 | 2 | 131 | P&L column period |  |
| R745 | 2 | 114 | P&L column period |  |
| R746 | 3 | 195 | balance sheet date, consolidated |  |
| R747 | 3 | 197 | balance sheet comparative date, consolidated |  |
| R748 | 4 | 260 | cash flow period, consolidated |  |
| R749 | 4 | 262 | cash flow comparative period, consolidated |  |
| R750 | 6 | 391 | balance sheet date, standalone |  |
| R751 | 6 | 389 | balance sheet comparative date, standalone |  |
| R752 | 7 | 453 | cash flow period, standalone |  |
| R753 | 7 | 448 | cash flow comparative period, standalone |  |

### 6. Qualifiers not under notes/footnotes: residual IDs (2)

| ID | pg | line | A1 context | A2 flags |
|---|---|---|---|---|
| R827 | 5 | 290 | row has fewer values than columns; column not stated in text layer |  |
| R828 | 7 | 402 | row has fewer values than columns; column not stated in text layer |  |
```yaml
stage: A2-enumerator
company: "SYNGENE"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/syngene-q2fy27/work/ledger_results_syngene_q2fy27.md"
counts:
  notes: 9
  line_items: 227
  zero_standing: 15
  agenda_items: 1
  auditor_paras: 12
  entities: 5
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, NAME_INCONSISTENT, AUDITOR_CHANGE, COLUMN_UNRESOLVED, FOOTNOTE_UNRESOLVED, FORWARD, EXCEPTIONAL, MGMT_VIEW]
ids_in_structured: 828
ids_referenced: 828
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Counts reconcile: 227 line items (667 cells), 9 notes, 15 ZERO_STANDING (only standalone P&L unlabelled row l.290 is nil in all periods; the rest are partial-period dashes). Raised flags: SMSL is in liquidation from 15-Jun-2026 and note 8 names it differently from note 2 and the auditor list; no prior ledger so no entity diff. Auditor is new (S.R. Batliboi); comparatives and FY26 rest on a predecessor. Termination benefits are exceptional in three consecutive periods (note 7). USA site pre-operative costs capitalised on management view (note 5). Board letter says inter-alia but lists one item. Auditor reports signed 18:32-18:33, after 18:30 meeting end; Chairperson signed 18:24."
```
