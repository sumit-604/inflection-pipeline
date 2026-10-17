# LEDGER results FEDFINA q2fy27 (A2)
ids_in_structured: 748 | ids_referenced_in_ledger: 748 | orphan_ids: [] | match: yes (plus 5 MFS rows and SIG-6/7 with no A1 ID)

=== A2 COUNT TEST ===
category: notes        grep_count: 36   sweep_count: 36   match: yes
category: line_items   grep_count: 339  sweep_count: 339  match: yes
category: zero_standing grep_count: 38  sweep_count: 38   match: yes
category: agenda_items grep_count: 6    sweep_count: 6    match: yes   (1 item + 5 enclosures a-e)
category: auditor_paras grep_count: 19  sweep_count: 19   match: yes   (5 review + 14 certificate)
category: entities     grep_count: 38   sweep_count: 38   match: yes   (R611-R648)
category: signatures   grep_count: 7    sweep_count: 7    match: yes
category: forward/dates/other qualifiers  8 / 35 / 21  match: yes
category: turns/questions/mgmt_numbers/slides: n/a (results filing)
gate_a2: pass
=== END COUNT TEST ===
Note: line_items = distinct (page, line, item-label) groups over 610 NUMBER rows; grep = awk/sort -u normalised, sweep = Python grouping. Prior ledger ND; ENTITY_CHANGE not testable.

## 1. NOTES AND FOOTNOTES (36)
ROW_ID | category | location | A2 flags | cross-ref / materiality note
R692 | note | p5 L256 | - | footnote # EPS (P&L); 
R697 | note | p8 L414 | - | Note 1; 
R698 | note | p8 L421 | - | Note 2; 
R699 | note | p8 L423 | - | Note 3; cross R367,R368 (NCD Rs 27,875 Lakhs; cover 1.10)
R700 | note | p8 L426 | - | Note 4; cross R371 ZERO_STANDING
R701 | note | p8 L429 | - | Note 5; cross R369 (shares allotted)
R702 | note | p8 L432 | - | Note 6; cross R372,R648 ZERO_STANDING
R703 | note | p8 L434 | - | Note 7; 
R704 | note | p8 L437 | - | Note 8; cross R706
R705 | note | p8 L466 | - | footnote * (IBC s3(7)) on Note 8 table; 
R706 | note | p8 L468 | - | Note 8 second disclosure (RBI 2020-21/17); cross R704
R707 | note | p9 L478 | - | Note 9; 
R708 | note | p9 L507 | - | footnote * EPS (Reg 52(4)); 
R709 | note | p9 L508 | - | Reg 52(4) footnote 1; 7 ratios not applicable
R710 | note | p9 L510 | - | Reg 52(4) footnote 2; 
R711 | note | p9 L511 | - | Reg 52(4) footnote 3; 
R712 | note | p9 L512 | - | Reg 52(4) footnote 4; 
R713 | note | p9 L513 | - | Reg 52(4) footnote 5; 
R714 | note | p9 L514 | - | Reg 52(4) footnote 6; 
R715 | note | p9 L515 | - | Reg 52(4) footnote 7; 
R716 | note | p9 L517 | - | Note 10; 
R717 | note | p9 L519 | - | Note 10(I); 
R718 | note | p9 L527 | FOOTNOTE_UNRESOLVED | Note 10(I) footnote *; FOOTNOTE_UNRESOLVED: marker present, footnote text not found
R719 | note | p9 L530 | - | Note 10(II); 
R720 | note | p9 L539 | - | Note 10(iii); 
R721 | note | p9 L540 | - | Note 10(iv); 
R722 | note | p9 L542 | - | Note 11; 
R735 | note | p13 L813 | - | Annexure I note 1; 
R736 | note | p13 L814 | - | Annexure I note 2; 
R737 | note | p13 L815 | - | Annexure I note 3; 
R738 | note | p13 L816 | - | Annexure I note 4; 
R739 | note | p13 L818 | - | Annexure I note 5; unit INR crore vs Lakhs elsewhere
R740 | note | p13 L819 | - | Annexure I note 6; cross R520,R741 (cover 1.24 vs contractual 1.10)
R743 | note | p14 L843 | - | footnote * INE007N07041; 
R744 | note | p14 L868 | - | footnote * INE007N07058; 
R745 | note | p14 L893 | - | unnumbered footnote under INE007N07066 ratios; 

## 2. LINE ITEMS (all financial tables incl. nil rows; R001-R610 NUMBER rows)
ROW_ID | category | location | A2 flags | cross-ref / materiality note
R001-R006 | line_item | p5 L218 | - | Interest Income (6 values)
R007-R012 | line_item | p5 L219 | - | Fee and Commission Income (6 values)
R013-R018 | line_item | p5 L220 | - | Net Gain on fair value changes (6 values)
R019-R024 | line_item | p5 L221 | - | Total Revenue from Operations (6 values)
R025-R030 | line_item | p5 L222 | - | Other Income (6 values)
R031-R036 | line_item | p5 L223 | - | Total Income (6 values)
R037-R042 | line_item | p5 L225 | - | Finance cost (6 values)
R043-R048 | line_item | p5 L226 | - | Impairment on financial instruments and other receivable (6 values)
R049-R054 | line_item | p5 L227 | - | Employee benefit expense (6 values)
R055-R060 | line_item | p5 L228 | - | Depreciation and amortisation expense (6 values)
R061-R066 | line_item | p5 L229 | - | Other expenses (6 values)
R067-R072 | line_item | p5 L230 | - | Total Expenses (6 values)
R073-R078 | line_item | p5 L231 | - | Profit before tax (6 values)
R079-R084 | line_item | p5 L232 | - | Tax expense (6 values)
R085-R090 | line_item | p5 L233 | - | Current tax (6 values)
R091-R096 | line_item | p5 L234 | ZERO_STANDING(R091,R092,R093,R094,R095) | Short/(Excess) provision for earlier years (6 values)
R097-R102 | line_item | p5 L235 | - | Deferred tax (6 values)
R103-R108 | line_item | p5 L236 | - | Net Profit for the period/year (6 values)
R109-R114 | line_item | p5 L237 | - | Other Comprehensive Income (6 values)
R115-R120 | line_item | p5 L239 | ZERO_STANDING(R117) | Re-measurement of net defined benefit plan (6 values)
R121-R126 | line_item | p5 L240 | ZERO_STANDING(R123) | Tax effect on re-measurement (6 values)
R127-R132 | line_item | p5 L241 | ZERO_STANDING(R129) | OCI not reclassified, Total (6 values)
R133-R138 | line_item | p5 L243 | - | Fair value gain/(loss) OCI - Loans (6 values)
R139-R144 | line_item | p5 L245 | ZERO_STANDING(R141,R143,R144) | Fair value gain/(loss) OCI - Investment in Government Securities (6 values)
R145-R150 | line_item | p5 L247 | - | Effective portion of gain on hedging instruments in cash flow hedge (6 values)
R151-R156 | line_item | p5 L248 | - | Tax effect on (i),(ii),(iii) (6 values)
R157-R162 | line_item | p5 L249 | - | OCI reclassified, Total (6 values)
R163-R168 | line_item | p5 L250 | - | Total Comprehensive Income (6 values)
R169-R174 | line_item | p5 L251 | - | Paid-up equity share capital (6 values)
R175-R180 | line_item | p5 L254 | - | EPS Basic (Rs, not annualised) (6 values)
R181-R186 | line_item | p5 L255 | - | EPS Diluted (Rs, not annualised) (6 values)
R187 | line_item | p5 L251 | - | Reserves excl revaluation reserve (1 values)
R188 | line_item | p5 L253 | - | EPS face value per share (1 values)
R189 | line_item | p6 L274 | - | BS Cash and cash equivalents, As at Sep 30 2026 (1 values)
R190 | line_item | p6 L274 | - | BS Cash and cash equivalents, As at Mar 31 2026 (1 values)
R191 | line_item | p6 L275 | - | BS Bank balances other than cash, As at Sep 30 2026 (1 values)
R192 | line_item | p6 L275 | - | BS Bank balances other than cash, As at Mar 31 2026 (1 values)
R193 | line_item | p6 L276 | - | BS Derivative financial instruments (asset), As at Sep 30 2026 (1 values)
R194 | line_item | p6 L276 | - | BS Derivative financial instruments (asset), As at Mar 31 2026 (1 values)
R195 | line_item | p6 L278 | - | BS Trade receivables, As at Sep 30 2026 (1 values)
R196 | line_item | p6 L278 | - | BS Trade receivables, As at Mar 31 2026 (1 values)
R197 | line_item | p6 L279 | - | BS Other receivables, As at Sep 30 2026 (1 values)
R198 | line_item | p6 L279 | - | BS Other receivables, As at Mar 31 2026 (1 values)
R199 | line_item | p6 L280 | - | BS Loans, As at Sep 30 2026 (1 values)
R200 | line_item | p6 L280 | - | BS Loans, As at Mar 31 2026 (1 values)
R201 | line_item | p6 L281 | - | BS Investments, As at Sep 30 2026 (1 values)
R202 | line_item | p6 L281 | - | BS Investments, As at Mar 31 2026 (1 values)
R203 | line_item | p6 L282 | - | BS Other financial assets, As at Sep 30 2026 (1 values)
R204 | line_item | p6 L282 | - | BS Other financial assets, As at Mar 31 2026 (1 values)
R205 | line_item | p6 L283 | - | BS Total Financial assets, As at Sep 30 2026 (1 values)
R206 | line_item | p6 L283 | - | BS Total Financial assets, As at Mar 31 2026 (1 values)
R207 | line_item | p6 L286 | ZERO_STANDING(R207) | BS Current tax assets (net), As at Sep 30 2026 (1 values)
R208 | line_item | p6 L286 | - | BS Current tax assets (net), As at Mar 31 2026 (1 values)
R209 | line_item | p6 L287 | - | BS Deferred tax assets (net), As at Sep 30 2026 (1 values)
R210 | line_item | p6 L287 | - | BS Deferred tax assets (net), As at Mar 31 2026 (1 values)
R211 | line_item | p6 L288 | - | BS Property, Plant and Equipment, As at Sep 30 2026 (1 values)
R212 | line_item | p6 L288 | - | BS Property, Plant and Equipment, As at Mar 31 2026 (1 values)
R213 | line_item | p6 L289 | - | BS Right of Use Assets, As at Sep 30 2026 (1 values)
R214 | line_item | p6 L289 | - | BS Right of Use Assets, As at Mar 31 2026 (1 values)
R215 | line_item | p6 L290 | - | BS Capital work in progress, As at Sep 30 2026 (1 values)
R216 | line_item | p6 L290 | - | BS Capital work in progress, As at Mar 31 2026 (1 values)
R217 | line_item | p6 L291 | - | BS Intangible assets under development, As at Sep 30 2026 (1 values)
R218 | line_item | p6 L291 | - | BS Intangible assets under development, As at Mar 31 2026 (1 values)
R219 | line_item | p6 L292 | - | BS Other Intangible assets, As at Sep 30 2026 (1 values)
R220 | line_item | p6 L292 | - | BS Other Intangible assets, As at Mar 31 2026 (1 values)
R221 | line_item | p6 L293 | - | BS Other non-financial assets, As at Sep 30 2026 (1 values)
R222 | line_item | p6 L293 | - | BS Other non-financial assets, As at Mar 31 2026 (1 values)
R223 | line_item | p6 L294 | - | BS Total Non-financial assets, As at Sep 30 2026 (1 values)
R224 | line_item | p6 L294 | - | BS Total Non-financial assets, As at Mar 31 2026 (1 values)
R225 | line_item | p6 L296 | - | BS TOTAL ASSETS, As at Sep 30 2026 (1 values)
R226 | line_item | p6 L296 | - | BS TOTAL ASSETS, As at Mar 31 2026 (1 values)
R227 | line_item | p6 L300 | - | BS Derivative financial instruments (liability), As at Sep 30 2026 (1 values)
R228 | line_item | p6 L300 | ZERO_STANDING(R228) | BS Derivative financial instruments (liability), As at Mar 31 2026 (1 values)
R229 | line_item | p6 L303 | - | BS Trade payables MSME, As at Sep 30 2026 (1 values)
R230 | line_item | p6 L303 | - | BS Trade payables MSME, As at Mar 31 2026 (1 values)
R231 | line_item | p6 L305 | - | BS Trade payables other than MSME, As at Sep 30 2026 (1 values)
R232 | line_item | p6 L305 | - | BS Trade payables other than MSME, As at Mar 31 2026 (1 values)
R233 | line_item | p6 L306 | - | BS Debt securities, As at Sep 30 2026 (1 values)
R234 | line_item | p6 L306 | - | BS Debt securities, As at Mar 31 2026 (1 values)
R235 | line_item | p6 L307 | - | BS Borrowings (other than debt securities), As at Sep 30 2026 (1 values)
R236 | line_item | p6 L307 | - | BS Borrowings (other than debt securities), As at Mar 31 2026 (1 values)
R237 | line_item | p6 L308 | - | BS Subordinated Liabilities, As at Sep 30 2026 (1 values)
R238 | line_item | p6 L308 | - | BS Subordinated Liabilities, As at Mar 31 2026 (1 values)
R239 | line_item | p6 L309 | - | BS Lease Liability, As at Sep 30 2026 (1 values)
R240 | line_item | p6 L309 | - | BS Lease Liability, As at Mar 31 2026 (1 values)
R241 | line_item | p6 L310 | - | BS Other financial liabilities, As at Sep 30 2026 (1 values)
R242 | line_item | p6 L310 | - | BS Other financial liabilities, As at Mar 31 2026 (1 values)
R243 | line_item | p6 L311 | - | BS Total Financial liabilities, As at Sep 30 2026 (1 values)
R244 | line_item | p6 L311 | - | BS Total Financial liabilities, As at Mar 31 2026 (1 values)
R245 | line_item | p6 L314 | - | BS Current tax liabilities (net), As at Sep 30 2026 (1 values)
R246 | line_item | p6 L314 | ZERO_STANDING(R246) | BS Current tax liabilities (net), As at Mar 31 2026 (1 values)
R247 | line_item | p6 L315 | - | BS Provision, As at Sep 30 2026 (1 values)
R248 | line_item | p6 L315 | - | BS Provision, As at Mar 31 2026 (1 values)
R249 | line_item | p6 L316 | - | BS Other non-financial liabilities, As at Sep 30 2026 (1 values)
R250 | line_item | p6 L316 | - | BS Other non-financial liabilities, As at Mar 31 2026 (1 values)
R251 | line_item | p6 L317 | - | BS Total Non-financial liabilities, As at Sep 30 2026 (1 values)
R252 | line_item | p6 L317 | - | BS Total Non-financial liabilities, As at Mar 31 2026 (1 values)
R253 | line_item | p6 L321 | - | BS Equity share capital, As at Sep 30 2026 (1 values)
R254 | line_item | p6 L321 | - | BS Equity share capital, As at Mar 31 2026 (1 values)
R255 | line_item | p6 L322 | - | BS Other equity, As at Sep 30 2026 (1 values)
R256 | line_item | p6 L322 | - | BS Other equity, As at Mar 31 2026 (1 values)
R257 | line_item | p6 L323 | - | BS Total equity, As at Sep 30 2026 (1 values)
R258 | line_item | p6 L323 | - | BS Total equity, As at Mar 31 2026 (1 values)
R259 | line_item | p6 L325 | - | BS TOTAL LIABILITIES AND EQUITY, As at Sep 30 2026 (1 values)
R260 | line_item | p6 L325 | - | BS TOTAL LIABILITIES AND EQUITY, As at Mar 31 2026 (1 values)
R261-R262 | line_item | p7 L339 | - | CF Net profit before tax (2 values)
R263-R264 | line_item | p7 L341 | - | CF Finance cost (2 values)
R265-R266 | line_item | p7 L342 | - | CF Share based payment to employee (2 values)
R267-R268 | line_item | p7 L343 | - | CF Depreciation (2 values)
R269-R270 | line_item | p7 L344 | - | CF Interest income from Investment (adj) (2 values)
R271-R272 | line_item | p7 L345 | - | CF Interest on Fixed Deposit (adj) (2 values)
R273-R274 | line_item | p7 L346 | - | CF Loss on sale of tangible assets (2 values)
R275 | line_item | p7 L347 | - | CF Loss on sale of NCD (1 values)
R276-R277 | line_item | p7 L348 | - | CF Profit on sale of mutual fund units (net) realised (2 values)
R278-R279 | line_item | p7 L349 | - | CF Gain/(Loss) fair valuation mutual fund unrealised (2 values)
R280-R281 | line_item | p7 L350 | - | CF Security deposit fair valuation (2 values)
R282-R283 | line_item | p7 L351 | - | CF EIR impact on Loans (2 values)
R284-R285 | line_item | p7 L352 | - | CF Excess interest spread on Direct Assignment (net) (2 values)
R286-R287 | line_item | p7 L353 | - | CF Impairment on financial instrument (2 values)
R288-R289 | line_item | p7 L354 | - | CF Operating profit before working capital changes (2 values)
R290-R291 | line_item | p7 L357 | - | CF (Increase)/decrease in loans (2 values)
R292-R293 | line_item | p7 L358 | - | CF (Increase)/decrease in financial and non financial asset (2 values)
R294-R295 | line_item | p7 L359 | - | CF (Increase)/decrease in trade and other receivables (2 values)
R296-R297 | line_item | p7 L360 | - | CF Increase/(decrease) in trade payables (2 values)
R298-R299 | line_item | p7 L361 | - | CF Increase/(decrease) in provisions (2 values)
R300-R301 | line_item | p7 L362 | - | CF Increase/(decrease) in financial and non financial liabilities (2 values)
R302-R303 | line_item | p7 L364 | - | CF Cash generated from/(used in) operating activities (2 values)
R304-R305 | line_item | p7 L365 | - | CF Direct taxes paid (net of refund) (2 values)
R306-R307 | line_item | p7 L366 | - | CF Net cash from/(used in) operating activities (2 values)
R308-R309 | line_item | p7 L369 | - | CF Purchase of tangible assets (2 values)
R310-R311 | line_item | p7 L370 | - | CF Purchase of Intangible assets (2 values)
R312 | line_item | p7 L371 | - | CF Investment in Government securities (1 values)
R313 | line_item | p7 L372 | - | CF Redemption of Government securities (1 values)
R314 | line_item | p7 L373 | - | CF Redemption/(Investment) of NCD (1 values)
R315-R316 | line_item | p7 L374 | - | CF Investment in Mutual Fund (2 values)
R317-R318 | line_item | p7 L375 | - | CF Redemption/(Investment) of SR's (2 values)
R319-R320 | line_item | p7 L376 | - | CF Sale of Mutual Fund (2 values)
R321-R322 | line_item | p7 L377 | - | CF Redemption of fixed deposit (2 values)
R323-R324 | line_item | p7 L378 | - | CF Investment in fixed deposit (2 values)
R325-R326 | line_item | p7 L379 | - | CF Interest on fixed deposits (investing) (2 values)
R327-R328 | line_item | p7 L380 | - | CF Interest income from Investment (investing) (2 values)
R329-R330 | line_item | p7 L381 | - | CF Net cash from/(used in) Investing activities (2 values)
R331-R332 | line_item | p7 L384 | - | CF Debt Securities availed (2 values)
R333-R334 | line_item | p7 L385 | - | CF Debt Securities repaid (2 values)
R335-R336 | line_item | p7 L386 | - | CF Borrowings availed (2 values)
R337-R338 | line_item | p7 L387 | - | CF Borrowings repaid (2 values)
R339-R340 | line_item | p7 L388 | - | CF Finance Cost paid (2 values)
R341-R342 | line_item | p7 L389 | - | CF Lease Payment (principal) (2 values)
R343-R344 | line_item | p7 L390 | - | CF Lease Payment (interest) (2 values)
R345-R346 | line_item | p7 L391 | - | CF Share application money pending allotment (2 values)
R347-R348 | line_item | p7 L392 | - | CF Equity Shares Issued (2 values)
R349-R350 | line_item | p7 L393 | - | CF Share Premium net of Share Issue Expenses (2 values)
R351-R352 | line_item | p7 L395 | - | CF Net cash from/(used in) financing activities (2 values)
R353-R354 | line_item | p7 L397 | - | CF Net increase/(decrease) in cash and cash equivalents (2 values)
R355-R356 | line_item | p7 L398 | - | CF Cash and cash equivalents at beginning (2 values)
R357-R358 | line_item | p7 L399 | - | CF Closing cash and cash equivalents (2 values)
R359-R360 | line_item | p7 L402 | - | CF Cash on hand (2 values)
R361-R362 | line_item | p7 L404 | - | CF Balances with banks in current accounts (2 values)
R363-R364 | line_item | p7 L405 | - | CF Fixed deposit maturity less than 3 months (2 values)
R365-R366 | line_item | p7 L406 | - | CF Cash and cash equivalents (components total) (2 values)
R367 | line_item | p8 L423 | - | NCDs secured outstanding Sep 30 2026 (1 values)
R368 | line_item | p8 L424 | - | minimum security cover required (1 values)
R369 | line_item | p8 L429 | - | equity shares allotted on ESOP exercise (1 values)
R370 | line_item | p8 L429 | - | face value per equity share allotted (1 values)
R371 | line_item | p8 L426 | ZERO_STANDING(R371) | ESOS 2024 and ESOS 2018 grants, Q2 FY27 ZERO_STANDING (1 values)
R372 | line_item | p8 L432 | ZERO_STANDING(R372) | subsidiary count as on Sep 30 2026 ZERO_STANDING (1 values)
R373 | line_item | p8 L461 | - | Personal Loans resolution exposure, end prior half-year (A) (1 values)
R374 | line_item | p8 L461 | - | Personal Loans debt slipped into NPA during half-year (1 values)
R375 | line_item | p8 L461 | ZERO_STANDING(R375) | Personal Loans written off during half-year ZERO_STANDING (1 values)
R376 | line_item | p8 L461 | - | Personal Loans amount paid by borrowers during half-year (1 values)
R377 | line_item | p8 L461 | - | Personal Loans resolution exposure, end this half-year (1 values)
R378 | line_item | p8 L462 | ZERO_STANDING(R378) | Corporate persons resolution exposure all columns ZERO_STANDING (1 values)
R379 | line_item | p8 L463 | ZERO_STANDING(R379) | Of which MSMEs resolution exposure ZERO_STANDING (1 values)
R380 | line_item | p8 L464 | ZERO_STANDING(R380) | Others resolution exposure ZERO_STANDING (1 values)
R381 | line_item | p8 L465 | - | Total resolution exposure end previous half-year (A) (1 values)
R382 | line_item | p8 L465 | - | Total debt slipped into NPA during half-year (1 values)
R383 | line_item | p8 L465 | ZERO_STANDING(R383) | Total written off during half-year ZERO_STANDING (1 values)
R384 | line_item | p8 L465 | - | Total amount paid by borrowers during half-year (1 values)
R385 | line_item | p8 L465 | - | Total resolution exposure end this half-year (1 values)
R386 | line_item | p8 L475 | - | number of accounts restructured as at Sep 30 2026 (1 values)
R387 | line_item | p8 L475 | - | amount outstanding restructured Sep 30 2026, INR Lakhs (1 values)
R388 | line_item | p9 L483 | - | Reg52(4) Debt-Equity Ratio, Sep 30 2026 (1 values)
R389 | line_item | p9 L483 | - | Reg52(4) Debt-Equity Ratio, Jun 30 2026 (1 values)
R390 | line_item | p9 L483 | - | Reg52(4) Debt-Equity Ratio, Mar 31 2026 (1 values)
R391 | line_item | p9 L483 | - | Reg52(4) Debt-Equity Ratio, Sep 30 2025 (1 values)
R392 | line_item | p9 L484 | - | Reg52(4) Debt Service Coverage Ratio, Sep 30 2026 (1 values)
R393 | line_item | p9 L484 | - | Reg52(4) Debt Service Coverage Ratio, Jun 30 2026 (1 values)
R394 | line_item | p9 L484 | - | Reg52(4) Debt Service Coverage Ratio, Mar 31 2026 (1 values)
R395 | line_item | p9 L484 | - | Reg52(4) Debt Service Coverage Ratio, Sep 30 2025 (1 values)
R396 | line_item | p9 L485 | - | Reg52(4) Interest Service Coverage Ratio, Sep 30 2026 (1 values)
R397 | line_item | p9 L485 | - | Reg52(4) Interest Service Coverage Ratio, Jun 30 2026 (1 values)
R398 | line_item | p9 L485 | - | Reg52(4) Interest Service Coverage Ratio, Mar 31 2026 (1 values)
R399 | line_item | p9 L485 | - | Reg52(4) Interest Service Coverage Ratio, Sep 30 2025 (1 values)
R400 | line_item | p9 L486 | - | Reg52(4) Outstanding redeemable preference shares, Sep 30 2026 (1 values)
R401 | line_item | p9 L486 | - | Reg52(4) Outstanding redeemable preference shares, Jun 30 2026 (1 values)
R402 | line_item | p9 L486 | - | Reg52(4) Outstanding redeemable preference shares, Mar 31 2026 (1 values)
R403 | line_item | p9 L486 | - | Reg52(4) Outstanding redeemable preference shares, Sep 30 2025 (1 values)
R404 | line_item | p9 L487 | - | Reg52(4) Capital redemption reserve (INR Lakhs), Sep 30 2026 (1 values)
R405 | line_item | p9 L487 | - | Reg52(4) Capital redemption reserve (INR Lakhs), Jun 30 2026 (1 values)
R406 | line_item | p9 L487 | - | Reg52(4) Capital redemption reserve (INR Lakhs), Mar 31 2026 (1 values)
R407 | line_item | p9 L487 | - | Reg52(4) Capital redemption reserve (INR Lakhs), Sep 30 2025 (1 values)
R408 | line_item | p9 L488 | - | Reg52(4) Debenture redemption reserve, Sep 30 2026 (1 values)
R409 | line_item | p9 L488 | - | Reg52(4) Debenture redemption reserve, Jun 30 2026 (1 values)
R410 | line_item | p9 L488 | - | Reg52(4) Debenture redemption reserve, Mar 31 2026 (1 values)
R411 | line_item | p9 L488 | - | Reg52(4) Debenture redemption reserve, Sep 30 2025 (1 values)
R412 | line_item | p9 L489 | - | Reg52(4) Current liability ratio, Sep 30 2026 (1 values)
R413 | line_item | p9 L489 | - | Reg52(4) Current liability ratio, Jun 30 2026 (1 values)
R414 | line_item | p9 L489 | - | Reg52(4) Current liability ratio, Mar 31 2026 (1 values)
R415 | line_item | p9 L489 | - | Reg52(4) Current liability ratio, Sep 30 2025 (1 values)
R416 | line_item | p9 L490 | - | Reg52(4) Total debts to total assets, Sep 30 2026 (1 values)
R417 | line_item | p9 L490 | - | Reg52(4) Total debts to total assets, Jun 30 2026 (1 values)
R418 | line_item | p9 L490 | - | Reg52(4) Total debts to total assets, Mar 31 2026 (1 values)
R419 | line_item | p9 L490 | - | Reg52(4) Total debts to total assets, Sep 30 2025 (1 values)
R420 | line_item | p9 L491 | - | Reg52(4) Net worth (INR Lakhs), Sep 30 2026 (1 values)
R421 | line_item | p9 L491 | - | Reg52(4) Net worth (INR Lakhs), Jun 30 2026 (1 values)
R422 | line_item | p9 L491 | - | Reg52(4) Net worth (INR Lakhs), Mar 31 2026 (1 values)
R423 | line_item | p9 L491 | - | Reg52(4) Net worth (INR Lakhs), Sep 30 2025 (1 values)
R424 | line_item | p9 L493 | - | Reg52(4) CRAR, Sep 30 2026 (1 values)
R425 | line_item | p9 L493 | - | Reg52(4) CRAR, Jun 30 2026 (1 values)
R426 | line_item | p9 L493 | - | Reg52(4) CRAR, Mar 31 2026 (1 values)
R427 | line_item | p9 L493 | - | Reg52(4) CRAR, Sep 30 2025 (1 values)
R428 | line_item | p9 L494 | - | Reg52(4) GNPA, Sep 30 2026 (1 values)
R429 | line_item | p9 L494 | - | Reg52(4) GNPA, Jun 30 2026 (1 values)
R430 | line_item | p9 L494 | - | Reg52(4) GNPA, Mar 31 2026 (1 values)
R431 | line_item | p9 L494 | - | Reg52(4) GNPA, Sep 30 2025 (1 values)
R432 | line_item | p9 L495 | - | Reg52(4) NNPA, Sep 30 2026 (1 values)
R433 | line_item | p9 L495 | - | Reg52(4) NNPA, Jun 30 2026 (1 values)
R434 | line_item | p9 L495 | - | Reg52(4) NNPA, Mar 31 2026 (1 values)
R435 | line_item | p9 L495 | - | Reg52(4) NNPA, Sep 30 2025 (1 values)
R436 | line_item | p9 L496 | - | Reg52(4) Liquidity Coverage ratio, Sep 30 2026 (1 values)
R437 | line_item | p9 L496 | - | Reg52(4) Liquidity Coverage ratio, Jun 30 2026 (1 values)
R438 | line_item | p9 L496 | - | Reg52(4) Liquidity Coverage ratio, Mar 31 2026 (1 values)
R439 | line_item | p9 L496 | - | Reg52(4) Liquidity Coverage ratio, Sep 30 2025 (1 values)
R440 | line_item | p9 L497 | - | Reg52(4) Provision Coverage Ratio (PCR), Sep 30 2026 (1 values)
R441 | line_item | p9 L497 | - | Reg52(4) Provision Coverage Ratio (PCR), Jun 30 2026 (1 values)
R442 | line_item | p9 L497 | - | Reg52(4) Provision Coverage Ratio (PCR), Mar 31 2026 (1 values)
R443 | line_item | p9 L497 | - | Reg52(4) Provision Coverage Ratio (PCR), Sep 30 2025 (1 values)
R444-R449 | line_item | p9 L502 | - | Reg52(4) Net profit margin (6 values)
R450-R455 | line_item | p9 L503 | - | Reg52(4) Net Profit after tax (INR Lakhs) (6 values)
R456-R461 | line_item | p9 L505 | - | Reg52(4) EPS Basic (6 values)
R462-R467 | line_item | p9 L506 | - | Reg52(4) EPS Diluted (6 values)
R468 | line_item | p9 L524 | - | NPA accounts transferred to ARCs (1 values)
R469 | line_item | p9 L527 | ZERO_STANDING(R469) | Net book value NPA loans transferred ZERO_STANDING (1 values)
R470 | line_item | p9 L528 | - | aggregate consideration NPA transfer to ARCs INR Lakhs (1 values)
R471 | line_item | p9 L529 | ZERO_STANDING(R471) | Additional consideration realised ZERO_STANDING (1 values)
R472 | line_item | p9 L533 | - | aggregate loan amount transferred by assignment INR Lakhs (1 values)
R473 | line_item | p9 L534 | - | weighted average residual maturity months, assignment (1 values)
R474 | line_item | p9 L535 | - | weighted average holding period months, assignment (1 values)
R475 | line_item | p9 L536 | - | retention of beneficial economic interest, assignment (1 values)
R476 | line_item | p9 L537 | - | coverage of tangible security, assignment (1 values)
R477 | line_item | p9 L538 | - | rating-wise distribution of rated loans (1 values)
R478 | line_item | p9 L539 | ZERO_STANDING(R478) | loans acquired via assignment Q2 FY27 ZERO_STANDING (1 values)
R479 | line_item | p9 L540 | ZERO_STANDING(R479) | stressed loans acquired Q2 FY27 ZERO_STANDING (1 values)
R480 | line_item | p9 L517 | - | RBI Master Direction reference (1 values)
R481 | line_item | p13 L755 | - | Annexure I security cover (INR crore) PPE book value (1 values)
R482 | line_item | p13 L758 | - | Annexure I security cover (INR crore) Capital WIP (1 values)
R483 | line_item | p13 L760 | - | Annexure I security cover (INR crore) Right of Use Assets (1 values)
R484 | line_item | p13 L762 | - | Annexure I security cover (INR crore) Intangible Assets (1 values)
R485 | line_item | p13 L764 | - | Annexure I security cover (INR crore) Intangible Assets under Development (1 values)
R486 | line_item | p13 L766 | - | Annexure I security cover (INR crore) Investments (1 values)
R487 | line_item | p13 L767 | - | Annexure I security cover (INR crore) Loans: Col F pari passu (1 values)
R488 | line_item | p13 L767 | - | Annexure I security cover (INR crore) Loans: not charged (1 values)
R489 | line_item | p13 L767 | - | Annexure I security cover (INR crore) Loans total (1 values)
R490 | line_item | p13 L767 | - | Annexure I security cover (INR crore) Loans: pari passu charge value (Col M/N) (1 values)
R491 | line_item | p13 L767 | - | Annexure I security cover (INR crore) Loans: total value (1 values)
R492 | line_item | p13 L769 | - | Annexure I security cover (INR crore) Trade Receivables (1 values)
R493 | line_item | p13 L771 | - | Annexure I security cover (INR crore) Cash and Cash Equivalents (1 values)
R494 | line_item | p13 L774 | - | Annexure I security cover (INR crore) Bank Balances Col C (1 values)
R495 | line_item | p13 L774 | - | Annexure I security cover (INR crore) Bank Balances other (1 values)
R496 | line_item | p13 L774 | - | Annexure I security cover (INR crore) Bank Balances total (1 values)
R497 | line_item | p13 L776 | - | Annexure I security cover (INR crore) Others exclusive (1 values)
R498 | line_item | p13 L776 | - | Annexure I security cover (INR crore) Others not charged (1 values)
R499 | line_item | p13 L776 | - | Annexure I security cover (INR crore) Others total (1 values)
R500 | line_item | p13 L777 | - | Annexure I security cover (INR crore) Assets Total exclusive (1 values)
R501 | line_item | p13 L777 | - | Annexure I security cover (INR crore) Assets Total pari passu (1 values)
R502 | line_item | p13 L777 | - | Annexure I security cover (INR crore) Assets Total not charged (1 values)
R503 | line_item | p13 L777 | - | Annexure I security cover (INR crore) Assets Total all (1 values)
R504 | line_item | p13 L777 | - | Annexure I security cover (INR crore) Assets Total Col M/N (1 values)
R505 | line_item | p13 L777 | - | Annexure I security cover (INR crore) Assets total value (1 values)
R506 | line_item | p13 L784 | - | Annexure I security cover (INR crore) Debt securities NCDs (1 values)
R507 | line_item | p13 L791 | - | Annexure I security cover (INR crore) Subordinated debt (1 values)
R508 | line_item | p13 L793 | - | Annexure I security cover (INR crore) Borrowings Bank (1 values)
R509 | line_item | p13 L795 | - | Annexure I security cover (INR crore) Debt Securities (annotated not to be filled) (1 values)
R510 | line_item | p13 L796 | - | Annexure I security cover (INR crore) Others borrowings (1 values)
R511 | line_item | p13 L797 | - | Annexure I security cover (INR crore) Trade payables (1 values)
R512 | line_item | p13 L798 | - | Annexure I security cover (INR crore) Lease liabilities (1 values)
R513 | line_item | p13 L799 | - | Annexure I security cover (INR crore) Provisions (1 values)
R514 | line_item | p13 L800 | - | Annexure I security cover (INR crore) Others liabilities (1 values)
R515 | line_item | p13 L801 | - | Annexure I security cover (INR crore) Liabilities Total pari passu (1 values)
R516 | line_item | p13 L801 | - | Annexure I security cover (INR crore) Liabilities Total not backed (1 values)
R517 | line_item | p13 L801 | - | Annexure I security cover (INR crore) Liabilities Total other (1 values)
R518 | line_item | p13 L801 | - | Annexure I security cover (INR crore) Liabilities Total all (1 values)
R519 | line_item | p13 L803 | - | Annexure I security cover (INR crore) Cover on Book Value (1 values)
R520 | line_item | p13 L819 | - | contractual security cover to maintain (Note 6) (1 values)
R521 | line_item | p14 L833 | - | CRAR actual, ISIN INE007N07041 (1 values)
R522 | line_item | p14 L833 | - | CRAR minimum covenant INE007N07041 (1 values)
R523 | line_item | p14 L836 | - | NNPA actual INE007N07041 (1 values)
R524 | line_item | p14 L836 | - | NNPA maximum covenant INE007N07041 (1 values)
R525 | line_item | p14 L839 | - | GNPA actual INE007N07041 (1 values)
R526 | line_item | p14 L839 | - | GNPA maximum covenant INE007N07041 (1 values)
R527 | line_item | p14 L841 | - | Total liability/Adjusted tangible net worth actual INE007N07041 (1 values)
R528 | line_item | p14 L842 | - | Total liability/ATNW maximum INE007N07041 (1 values)
R529 | line_item | p14 L858 | - | CRAR actual, INE007N07058 (1 values)
R530 | line_item | p14 L860 | - | CRAR minimum covenant INE007N07058 (1 values)
R531 | line_item | p14 L862 | - | NNPA actual INE007N07058 OCR_UNCERTAIN (1 values)
R532 | line_item | p14 L862 | - | NNPA max covenant INE007N07058 (1 values)
R533 | line_item | p14 L864 | - | GNPA actual INE007N07058 (1 values)
R534 | line_item | p14 L864 | - | GNPA max covenant INE007N07058 (1 values)
R535 | line_item | p14 L866 | - | Total liability/ATNW actual INE007N07058 (1 values)
R536 | line_item | p14 L866 | - | Total liability/ATNW maximum INE007N07058 (1 values)
R537 | line_item | p14 L884 | - | CRAR actual, INE007N07066 (1 values)
R538 | line_item | p14 L885 | - | CRAR minimum covenant INE007N07066 (1 values)
R539 | line_item | p14 L887 | - | NNPA actual INE007N07066 (1 values)
R540 | line_item | p14 L887 | - | NNPA max covenant INE007N07066 (1 values)
R541 | line_item | p14 L889 | - | GNPA actual INE007N07066 OCR_UNCERTAIN (1 values)
R542 | line_item | p14 L889 | - | GNPA max covenant INE007N07066 (1 values)
R543 | line_item | p14 L891 | - | Debt to Equity actual INE007N07066 (1 values)
R544 | line_item | p14 L891 | - | Debt to Equity maximum INE007N07066 (1 values)
R545-R548 | line_item | p15 L956 | - | RPT Interest received FD/Current A/c (INR lakhs) (4 values)
R549-R551 | line_item | p15 L959 | - | RPT Interest paid Term Loan (INR lakhs) (3 values)
R552-R555 | line_item | p15 L960 | - | RPT Interest on WCDL (INR lakhs) (4 values)
R556-R558 | line_item | p15 L961 | - | RPT Interest on NCDs (INR lakhs) (3 values)
R559-R561 | line_item | p15 L962 | - | RPT MTM Gain/(Loss) Derivative (INR lakhs) (3 values)
R562-R565 | line_item | p15 L963 | ZERO_STANDING(R563,R564) | RPT Derivative Margin Deposit (INR lakhs) (4 values)
R566-R569 | line_item | p15 L965 | - | RPT Servicing Fee Income on Securitisation (INR lakhs) (4 values)
R570-R573 | line_item | p15 L966 | ZERO_STANDING(R572) | RPT Brand usage charges (INR lakhs) (4 values)
R574-R576 | line_item | p15 L969 | ZERO_STANDING(R576) | RPT Bank Charges paid (INR lakhs) (3 values)
R577-R579 | line_item | p15 L972 | - | RPT Interest paid on margin money (INR lakhs) (3 values)
R580-R581 | line_item | p15 L973 | - | RPT KYC Documentation Charges (Perfios) (INR lakhs) (2 values)
R582-R583 | line_item | p15 L974 | - | RPT Remuneration to MD & CEO (INR lakhs) (2 values)
R584-R585 | line_item | p15 L975 | - | RPT Remuneration to CFO (INR lakhs) (2 values)
R586-R587 | line_item | p15 L976 | - | RPT Remuneration to Company Secretary (INR lakhs) (2 values)
R588-R589 | line_item | p15 L977 | - | RPT Exercise of ESOP (CFO) (INR lakhs) (2 values)
R590-R592 | line_item | p15 L978 | ZERO_STANDING(R592) | RPT Director Sitting Fees Ramesh Sundararajan (INR lakhs) (3 values)
R593-R595 | line_item | p15 L979 | ZERO_STANDING(R595) | RPT Director Sitting Fees Sunil Gulati (INR lakhs) (3 values)
R596-R599 | line_item | p15 L980 | ZERO_STANDING(R598,R599) | RPT Director Sitting Fees Shyam Srinivasan (INR lakhs) (4 values)
R600-R603 | line_item | p15 L991 | ZERO_STANDING(R602,R603) | RPT Director Sitting Fees Sonal Dave (INR lakhs) (4 values)
R604-R607 | line_item | p15 L992 | ZERO_STANDING(R606,R607) | RPT Director Sitting Fees Mona Bhide (INR lakhs) (4 values)
R608-R610 | line_item | p15 L997 | ZERO_STANDING(R610) | RPT Director Sitting Fees Muralidharan Rajamani (INR lakhs) (3 values)

## 2b. ZERO_STANDING INDEX (38)
ROW_ID | category | location | A2 flags | cross-ref / materiality note
R091 | line_item | p5 L234 | ZERO_STANDING | Short/(Excess) provision for earlier years, Q2 FY27 (qtr Sep 30 2026)
R092 | line_item | p5 L234 | ZERO_STANDING | Short/(Excess) provision for earlier years, Q1 FY27 (qtr Jun 30 2026)
R093 | line_item | p5 L234 | ZERO_STANDING | Short/(Excess) provision for earlier years, Q2 FY26 (qtr Sep 30 2025)
R094 | line_item | p5 L234 | ZERO_STANDING | Short/(Excess) provision for earlier years, H1 FY27
R095 | line_item | p5 L234 | ZERO_STANDING | Short/(Excess) provision for earlier years, H1 FY26
R117 | line_item | p5 L239 | ZERO_STANDING | Re-measurement of net defined benefit plan, Q2 FY26 (qtr Sep 30 2025)
R123 | line_item | p5 L240 | ZERO_STANDING | Tax effect on re-measurement, Q2 FY26 (qtr Sep 30 2025)
R129 | line_item | p5 L241 | ZERO_STANDING | OCI not reclassified, Total, Q2 FY26 (qtr Sep 30 2025)
R141 | line_item | p5 L245 | ZERO_STANDING | Fair value gain/(loss) OCI - Investment in Government Securities, Q2 FY26 (qtr Sep 30 2025
R143 | line_item | p5 L245 | ZERO_STANDING | Fair value gain/(loss) OCI - Investment in Government Securities, H1 FY26
R144 | line_item | p5 L245 | ZERO_STANDING | Fair value gain/(loss) OCI - Investment in Government Securities, FY26 (Mar 31 2026)
R207 | line_item | p6 L286 | ZERO_STANDING | BS Current tax assets (net), As at Sep 30 2026
R228 | line_item | p6 L300 | ZERO_STANDING | BS Derivative financial instruments (liability), As at Mar 31 2026
R246 | line_item | p6 L314 | ZERO_STANDING | BS Current tax liabilities (net), As at Mar 31 2026
R371 | line_item | p8 L426 | ZERO_STANDING | ESOS 2024 and ESOS 2018 grants, Q2 FY27 ZERO_STANDING
R372 | line_item | p8 L432 | ZERO_STANDING | subsidiary count as on Sep 30 2026 ZERO_STANDING
R375 | line_item | p8 L461 | ZERO_STANDING | Personal Loans written off during half-year ZERO_STANDING
R378 | line_item | p8 L462 | ZERO_STANDING | Corporate persons resolution exposure all columns ZERO_STANDING
R379 | line_item | p8 L463 | ZERO_STANDING | Of which MSMEs resolution exposure ZERO_STANDING
R380 | line_item | p8 L464 | ZERO_STANDING | Others resolution exposure ZERO_STANDING
R383 | line_item | p8 L465 | ZERO_STANDING | Total written off during half-year ZERO_STANDING
R469 | line_item | p9 L527 | ZERO_STANDING | Net book value NPA loans transferred ZERO_STANDING
R471 | line_item | p9 L529 | ZERO_STANDING | Additional consideration realised ZERO_STANDING
R478 | line_item | p9 L539 | ZERO_STANDING | loans acquired via assignment Q2 FY27 ZERO_STANDING
R479 | line_item | p9 L540 | ZERO_STANDING | stressed loans acquired Q2 FY27 ZERO_STANDING
R563 | line_item | p15 L963 | ZERO_STANDING | RPT Derivative Margin Deposit (INR lakhs), value during half year
R564 | line_item | p15 L963 | ZERO_STANDING | RPT Derivative Margin Deposit (INR lakhs), opening balance
R572 | line_item | p15 L966 | ZERO_STANDING | RPT Brand usage charges (INR lakhs), opening balance
R576 | line_item | p15 L969 | ZERO_STANDING | RPT Bank Charges paid (INR lakhs), opening balance
R592 | line_item | p15 L978 | ZERO_STANDING | RPT Director Sitting Fees Ramesh Sundararajan (INR lakhs), opening balance
R595 | line_item | p15 L979 | ZERO_STANDING | RPT Director Sitting Fees Sunil Gulati (INR lakhs), opening balance
R598 | line_item | p15 L980 | ZERO_STANDING | RPT Director Sitting Fees Shyam Srinivasan (INR lakhs), opening balance
R599 | line_item | p15 L980 | ZERO_STANDING | RPT Director Sitting Fees Shyam Srinivasan (INR lakhs), closing balance
R602 | line_item | p15 L991 | ZERO_STANDING | RPT Director Sitting Fees Sonal Dave (INR lakhs), opening balance
R603 | line_item | p15 L991 | ZERO_STANDING | RPT Director Sitting Fees Sonal Dave (INR lakhs), closing balance
R606 | line_item | p15 L992 | ZERO_STANDING | RPT Director Sitting Fees Mona Bhide (INR lakhs), opening balance
R607 | line_item | p15 L992 | ZERO_STANDING | RPT Director Sitting Fees Mona Bhide (INR lakhs), closing balance
R610 | line_item | p15 L997 | ZERO_STANDING | RPT Director Sitting Fees Muralidharan Rajamani (INR lakhs), opening balance

## 3. AGENDA ITEMS / BOARD OUTCOME (single-item meeting; no AR/AGM/dividend/director/auditor/ESOP/fund-raise items)
ROW_ID | category | location | A2 flags | cross-ref / materiality note
R728 | agenda_item | p1 L44 | - | Agenda item 1: unaudited Q2/H1 results approved; reviewed and recommended by Audit Committee; cross R726,R657
R726 | agenda_item | p1 L52 | - | Item 1(b): LRR by KKC and V Sankar Aiyar, unmodified; cross R616,R617
R698 | agenda_item | p8 L421 | - | Item 1(a): results approved and taken on record; cross R728
R707 | agenda_item | p9 L478 | - | Item 1(c): Reg 52(4) ratio disclosure enclosure; cross R697; enclosure text see MFS-1
R680 | agenda_item | p13 L734 | - | Item 1(d): Reg 54 security cover as Annexure 1; cross R681; MFS-1
R747 | agenda_item | p15 L943 | - | Item 1(e): Reg 23(9) RPT half year as Annexure 2; cross R673; MFS-1
R659 | agenda_item | p2 L78 | - | Board meeting 11.10 a.m. to 12:25 p.m. (75 minutes); timing recorded
R649 | agenda_item | p1 L61 | - | Newspaper publication commitment Regs 47/52; cross R618,R619

## 4. ANNEXURES AND TABLES (3 annexures; no director profiles or appointment annexures in filing)
ROW_ID | category | location | A2 flags | cross-ref / materiality note
R468-R480 | annexure | - | - | Note 10 disclosure tables (NPA transfer to ARCs, assignment) and RBI Master Direction reference
R481-R520 | annexure | - | - | Annexure I (agenda: Annexure 1) security cover table, INR crore; R735-R742 notes; R680 date
R521-R544 | annexure | - | - | Annexure II covenant compliance, ISIN blocks INE007N07041/07058/07066; R681-R691 dates; R746 status
R545-R610 | annexure | - | - | RPT annexure (agenda: Annexure 2), half year; R747,R748 column notes; R629-R638 related persons
R633-R638 | annexure | p15 | - | Director profiles: none (no appointment item). Directors appear only as RPT counterparties; effective dates R674-R678.

## 5. AUDITOR PARAGRAPHS (19: review report 5, security cover certificate 14)
ROW_ID | category | location | A2 flags | cross-ref / materiality note
R661,R660,R616,R617 | auditor_para RR-1 | fulltext L129 | - | scope: review of statement; opinion unmodified; no EoM/Going Concern in structured rows
R723 | auditor_para RR-2 | fulltext L135 | - | management/Board responsibility; opinion unmodified; no EoM/Going Concern in structured rows
R724 | auditor_para RR-3 | fulltext L144 | - | SRE 2410 limited review scope; opinion unmodified; no EoM/Going Concern in structured rows
R725,R726 | auditor_para RR-4 | fulltext L152 | - | conclusion unmodified; no Going Concern/EoM; opinion unmodified; no EoM/Going Concern in structured rows
R727,R662,R663,R664 | auditor_para RR-5 | fulltext L168 | - | Other Matter: comparatives reviewed by KKC only; opinion unmodified; no EoM/Going Concern in structured rows
R729 | auditor_para SC-1 | fulltext L579 | - | issued per engagement letter; opinion unmodified; no EoM/Going Concern in structured rows
R639,R699 | auditor_para SC-2 | fulltext L581 | - | NCD money raised; opinion unmodified; no EoM/Going Concern in structured rows
R671 | auditor_para SC-3 | fulltext L584 | - | Reg 56(1)(d); opinion unmodified; no EoM/Going Concern in structured rows
R639,R647 | auditor_para SC-4 | fulltext L591 | - | V Sankar Aiyar as statutory auditor requested; opinion unmodified; no EoM/Going Concern in structured rows
R730 | auditor_para SC-5 | fulltext L600 | - | management responsibility for Statement; opinion unmodified; no EoM/Going Concern in structured rows
R730,R652 | auditor_para SC-6 | fulltext L607 | - | management covenant compliance duty; opinion unmodified; no EoM/Going Concern in structured rows
R731 | auditor_para SC-7 | fulltext L613 | - | auditor limited assurance; opinion unmodified; no EoM/Going Concern in structured rows
R732 | auditor_para SC-8 | fulltext L630 | - | test basis, guidance note; opinion unmodified; no EoM/Going Concern in structured rows
R732 | auditor_para SC-9 | fulltext L635 | - | scope excludes other compliance; opinion unmodified; no EoM/Going Concern in structured rows
R732 | auditor_para SC-10 | fulltext L644 | - | quality control standards; opinion unmodified; no EoM/Going Concern in structured rows
R732 | auditor_para SC-11 | fulltext L648 | - | limited assurance procedures; opinion unmodified; no EoM/Going Concern in structured rows
R733 | auditor_para SC-12 | fulltext L691 | - | conclusion; opinion unmodified; no EoM/Going Concern in structured rows
R734 | auditor_para SC-13 | fulltext L702 | - | restriction on use; opinion unmodified; no EoM/Going Concern in structured rows
R734 | auditor_para SC-14 | fulltext L710 | - | request of Company, use limitation; opinion unmodified; no EoM/Going Concern in structured rows

## 6. ENTITIES (38; consolidation list = none)
ROW_ID | category | location | A2 flags | cross-ref / materiality note
R611 | entity | p1 L19 | - | listed entity / filer 
R612 | entity | p1 L26 | - | exchange 
R613 | entity | p1 L26 | - | exchange 
R614 | entity | p1 L30 | - | NSE symbol 
R615 | entity | p1 L30 | - | BSE scrip code 
R616 | entity | p1 L49 | - | joint statutory auditor 
R617 | entity | p1 L49 | - | joint statutory auditor 
R618 | entity | p1 L63 | - | newspaper for publication 
R619 | entity | p1 L63 | - | newspaper for publication 
R620 | entity | p2 L92 | - | Company Secretary & Compliance Officer, Mem A21472 
R621 | entity | p1 L70 | - | company identifier 
R622 | entity | p4 L187 | - | KKC partner, ICAI 033494, FRN 105146W/W100621 
R623 | entity | p4 L187 | - | V Sankar Aiyar partner, ICAI 107022, FRN 109208W 
R624 | entity | p3 L139 | - | regulator 
R625 | entity | p3 L146 | - | professional body 
R626 | entity | p8 L418 | - | regulators cited in notes 
R627 | entity | p9 L523 | - | NPA transferee 
R628 | entity | p15 L956 | - | Promoter, related party promoter / related party; cross RPT annexure
R629 | entity | p15 L973 | - | entity with common director 
R630 | entity | p15 L974 | - | MD & CEO (w.e.f. November 11 2024) 
R631 | entity | p15 L975 | - | Chief Financial Officer 
R632 | entity | p15 L976 | - | Company Secretary 
R633 | entity | p15 L978 | - | Independent Director 
R634 | entity | p15 L979 | - | Independent Director 
R635 | entity | p15 L980 | - | Non-Executive Director (w.e.f. Sep 25 2024) 
R636 | entity | p15 L987 | - | Independent Director (w.e.f. Sep 24 2024) 
R637 | entity | p15 L988 | - | Independent Director (w.e.f. Nov 29 2024) 
R638 | entity | p15 L997 | - | Independent Director (w.e.f. Jan 24 2025) 
R639 | entity | p10 L559 | - | statutory auditor issuing security cover certificate 
R640 | entity | p14 L829 | - | secured NCD 
R641 | entity | p14 L848 | - | secured NCD 
R642 | entity | p14 L874 | - | secured NCD 
R643 | entity | p14 L897 | - | unsecured NCD 
R644 | entity | p14 L901 | - | unsecured NCD 
R645 | entity | p14 L905 | - | unsecured NCD 
R646 | entity | p14 L909 | - | unsecured NCD 
R647 | entity | p10 L588 | - | recipient of security cover certificate 
R648 | entity | p8 L432 | ZERO_STANDING | consolidation list: none consolidation list empty; cross R372,R702; ENTITY_CHANGE not testable (no prior ledger)

## 7. SIGNATURE BLOCKS (7) and UDIN
ROW_ID | category | location | A2 flags | cross-ref / materiality note
R620 | signature | p2 L92 | - | Company Secretary P Iyengar, cover letter p2; no timestamp in structured
R622 | signature | p4 L187 | - | KKC partner H Dedhia, review report p4, 15 Oct 2026 (R665)
R623 | signature | p4 L187 | - | V Sankar Aiyar partner S Nagabushanam, review report p4, 15 Oct 2026
R670 | signature | p9 L554 | - | Results statement signing date 15/10/2026 p9; signatory name not in structured
R639 | signature | p10 L559 | - | Security cover certificate p12 signed by S Nagabushanam, R672
MFS-1 | MISSING_FROM_STRUCTURED | fulltext L46-56 | MISSING_FROM_STRUCTURED | Agenda item 1 enclosures a-e (results, LRR, Reg 52(4), Reg 54 Annexure 1, Reg 23(9) Annexure 2) exist only as prose in fulltext; 1(c)-(e) have no own row
MFS-2 | MISSING_FROM_STRUCTURED | fulltext L190 | MISSING_FROM_STRUCTURED | Review report UDINs (2) present but garbled in text layer; no UDIN row in structured
MFS-3 | MISSING_FROM_STRUCTURED | fulltext L730 | MISSING_FROM_STRUCTURED | Security cover certificate UDIN present but garbled; no row
MFS-4 | MISSING_FROM_STRUCTURED | fulltext L525 | MISSING_FROM_STRUCTURED NOT DISCLOSED | Note 10(I): 'Aggregate principal outstanding of loans transferred' label present, value cell blank; no A1 row ID
MFS-5 | MISSING_FROM_STRUCTURED | fulltext L526 | MISSING_FROM_STRUCTURED NOT DISCLOSED | Note 10(I): 'Weighted average residual tenor of the loans transferred' label present, value cell blank; no A1 row ID
SIG-6 | signature | fulltext L812 | MISSING_FROM_STRUCTURED | Annexure I company signature block ('For Fedbank Financial Services Limited'); no A1 row ID
SIG-7 | signature | fulltext L932 (mark L934) | MISSING_FROM_STRUCTURED | Annexure II company signature block; no A1 row ID
Observation (no interpretation): digital signature timestamps not in text layer; results signature vs meeting conclusion 12:25 pm not testable.

## 8. FORWARD ITEMS (8), DATES (35), OTHER QUALIFIERS
ROW_ID | category | location | A2 flags | cross-ref / materiality note
R649 | forward | p1 L61 | - | publication commitment
R650 | forward | p8 L418 | - | forward compliance statement
R651 | forward | p14 L912 | - | covenant statement
R652 | forward | p14 L926 | - | Part B other covenants
R653 | forward | p14 L842 | - | ongoing covenant INE007N07041/07058
R654 | forward | p14 L834 | - | ongoing covenant INE007N07041/07058
R655 | forward | p14 L885 | - | ongoing covenant INE007N07066
R656 | forward | p13 L819 | - | forward security cover obligation
R657 | date | p1 L24 | RESTATED | board meeting/letter date; cross R667,R665,R670,R672 (15 Oct 2026 restated)
R658 | date | p1 L36 | RESTATED | results period; cross R660,R673
R659 | date | p2 L78 | - | board meeting timing
R660 | date | p3 L119 | RESTATED | year to date period; cross R658
R661 | date | p4 L168 | - | comparative review period
R662 | date | p4 L170 | - | prior KKC review report date (Q1 FY27)
R663 | date | p4 L171 | - | prior KKC review report date (Q2 FY26)
R664 | date | p4 L173 | - | FY26 audit report date
R665 | date | p4 L193 | RESTATED | review report signing date; cross R657,R667,R670
R666 | date | p5 L213 | - | FY26 year end
R667 | date | p8 L421 | RESTATED | board approval date; cross R657,R665,R670,R672
R668 | date | p8 L418 | - | SEBI operational circular date
R669 | date | p9 L517 | - | RBI Master Direction date
R670 | date | p9 L554 | RESTATED | results signing date; cross R657,R667,R665
R671 | date | p10 L585 | - | SEBI master circular date (Reg 56)
R672 | date | p12 L728 | RESTATED | security cover certificate date; cross R657,R667
R673 | date | p15 L940 | - | RPT period
R674 | date | p15 L974 | - | MD & CEO effective date
R675 | date | p15 L980 | - | Shyam Srinivasan effective
R676 | date | p15 L987 | - | Sonal Dave effective
R677 | date | p15 L988 | - | Mona Bhide effective
R678 | date | p15 L997 | - | Muralidharan Rajamani effective
R679 | date | p8 L437 | - | resolution disclosure circulars
R680 | date | p13 L734 | RESTATED | Annexure I Security Cover as-at date; cross R681
R681 | date | p14 L824 | RESTATED | Annexure II compliance as-at date; cross R680
R682 | date | p14 L844 | RESTATED | audited-figures basis date for ATNW covenant, INE007N07041; cross R683
R683 | date | p14 L869 | RESTATED | audited-figures basis date, INE007N07058; cross R682
R684 | date | p14 L893 | - | basis date for INE007N07066 ratios
R685 | date | p14 L830 | - | Trust deed date INE007N07041
R686 | date | p14 L849 | - | Trust deed date INE007N07058
R687 | date | p14 L875 | - | Trust deed date INE007N07066
R688 | date | p14 L898 | - | Trust deed date INE007N08015
R689 | date | p14 L902 | - | Trust deed date INE007N08023
R690 | date | p14 L906 | RESTATED | Trust deed date INE007N08031; cross R691
R691 | date | p14 L910 | RESTATED | Trust deed date INE007N08049; cross R690
R693 | qualifier | p5 L208 | - | unit and audit status of results
R694 | qualifier | p5 L223 | - | line-item definition
R695 | qualifier | p6 L268 | - | balance sheet unit/status
R696 | qualifier | p7 L334 | - | cash flow unit/status
R723 | qualifier | p3 L134 | - | auditor qualifier
R724 | qualifier | p3 L147 | - | auditor scope
R725 | qualifier | p3 L152 | - | auditor conclusion
R726 | qualifier | p1 L52 | - | cover letter qualifier
R727 | qualifier | p4 L174 | - | auditor other matter
R728 | qualifier | p1 L44 | - | cover qualifier
R729 | qualifier | p10 L574 | - | certificate title
R730 | qualifier | p10 L594 | - | basis of security cover statement
R731 | qualifier | p10 L613 | - | auditor scope
R732 | qualifier | p11 L640 | - | auditor scope limitation
R733 | qualifier | p12 L691 | - | auditor conclusion
R734 | qualifier | p12 L710 | - | restriction on use
R741 | qualifier | p13 L803 | - | security cover
R742 | qualifier | p13 L794 | - | form annotation
R746 | qualifier | p14 L832 | - | compliance status
R747 | qualifier | p15 L943 | - | RPT unit/period
R748 | qualifier | p15 L946 | - | RPT column definition

```yaml
stage: A2-enumerator
company: "FEDFINA"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "C:\Users\SUMIT SHARMA\repos\inflection-pipeline\.claude\worktrees\q2fy27\runs\fedfina-q2fy27\work\ledger_results_fedfina_q2fy27.md"
counts:
  notes: 36
  line_items: 339
  zero_standing: 38
  agenda_items: 6
  auditor_paras: 19
  entities: 38
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
  signatures: 7
flags_raised: [ZERO_STANDING, RESTATED, FOOTNOTE_UNRESOLVED, MISSING_FROM_STRUCTURED]
ids_in_structured: 748
ids_referenced: 748
orphan_ids: []
missing_from_structured: [MFS-1 agenda enclosures 1(c)-(e) prose only, MFS-2 review report UDINs garbled, MFS-3 certificate UDIN garbled, MFS-4 Note 10(I) aggregate principal outstanding blank (L525) NOT DISCLOSED, MFS-5 Note 10(I) weighted average residual tenor blank (L526) NOT DISCLOSED]
gate_a2: pass
mismatch_note: ""
analyst_note: "Single-item board outcome (results only; no AR, AGM, dividend, director, auditor or fund-raise items). Consolidation list is empty (Note 6, R648); ENTITY_CHANGE untestable, no prior ledger. 38 ZERO_STANDING rows: Note 8 resolution table (Corporate persons, MSME, Others, write-offs), Note 10 NPA transfer to ARCs (net book value, additional consideration), no loans acquired, no ESOS grants, and RPT opening/closing balances at zero (Derivative Margin Deposit approved Rs 24,500 lakhs, opening nil, closing 1,615.50). R718 asterisk on NPA transfer table has no footnote text. Annexure labelling differs between cover letter (Annexure 1 security cover, 2 RPT) and filing pages. Line items counted as page/line/label groups, not rows. Correction loop 1: added MFS-4/5 (blank Note 10(I) cells) and Annexure I (L812) and II (L932) signature blocks; signatures now 7."
```
