# A2 COMPLETENESS LEDGER: POONAWALLA q2fy27 results filing (standalone and consolidated, Reg 52 annexures)
Source: runs/poonawalla-q2fy27/extracted/poonawalla-results-q2fy27-structured.md (A1 rows R001-R1327). Fulltext used for count tests only. Prior ledger: ND.
De-dup contract: rows reference A1 ROW IDs; verbatim values stay in the structured file. Only T8 rows carry claim text.

ids_in_structured: 1327 | ids_referenced_in_ledger: 1327 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes          grep_count: 27   sweep_count: 27   match: yes   (strict "N." grep = 0 because filing uses "N]" markers; loose marker grep = 22 hits = 9 cons + 13 stand; minus 1 duplicate "11) (c)" sub-line = 21; plus 2 OCR-garbled markers ("I OJ" cons note 10, "I OJ" stand note 10) found on re-sweep = 23; plus 4 Annexure II notes = 27. Cons 10, stand 13, Annex II 4)
category: footnotes      grep_count: 10   sweep_count: 10   match: yes   (unnumbered notes/footnotes: lines 226, 469, 828, 912, 963, 964, 1033, 1038, 1144, 1568)
category: line_items     grep_count: 245  sweep_count: 245  match: yes   (statements: structured distinct NUMBER lines 219 vs fulltext wide-gap sweep 219 after removing 3 date-header lines and adding line 402 the regex missed; Reg 52(4) p18: 26 structured lines vs 25 sweep + line 994 blank value cell = 26)
category: zero_standing  grep_count: 33   sweep_count: 33   match: yes   (33 A1-flagged rows on 17 source lines; sweep of dash/NIL/Nil cells finds the same 17 lines. Plus 5 sweep-only candidates not counted, see T3)
category: agenda_items   grep_count: 11   sweep_count: 11   match: yes   (8 numbered items by grep: enclosures 1-6 and board approvals 1-2; plus 3 unnumbered units: results approval lead-in, Investor Presentation Reg 30, meeting times; Annexure A items counted separately: 5)
category: auditor_paras  grep_count: 25   sweep_count: 25   match: yes   (consolidated LRR 7, standalone LRR 6, security cover certificate 12; headers and signature blocks listed but not counted)
category: entities       grep_count: 2    sweep_count: 2    match: yes   (consolidation list: JASPL JV, PFL Employee Welfare Trust; A1 ENTITY rows 118 all referenced)
category: signatures     grep_count: 6    sweep_count: 6    match: yes   (cover letter, cons results, stand results, 3 auditor documents; cons LRR, stand LRR, certificate)
category: annex_lines    grep_count: 129  sweep_count: 129  match: yes   (pp19-30 source lines carrying rows: 10 footnote-page + 119 annexure)
category: missing_from_structured  sweep_count: 6 (T8)
gate_a2: pass
=== END COUNT TEST ===

Other A2 flags raised: AUDITOR_CHANGE (Kirtane and Pandit LLP described as "previous joint auditor"; MSKA and B K Khare now joint auditors), FORWARD rows pointer, MEETING_DURATION (107 min), ZERO_STANDING_CANDIDATE (5 lines), BLANK_STANDING (R797, RPS value cell blank beside NIL quantity), FOOTNOTE_UNRESOLVED (JASPL sale pending since 2021), RESTATED (QIP: note 7 cons/stand, Reg 32(1) pp20-22; JASPL: note 9 cons/stand, LRR para 4), ENTITY_CHANGE: ND.
Signature timestamp check: cover letter digitally signed 16:23:14 on 2026.10.09, after meeting close 3:32 PM. No premature-signature flag.

## T1 NOTES (numbered). Format: LEDGER_ID | structured ROW IDs (line range) | A2 flags | note
| LEDGER_ID | ROW IDs | fulltext lines | A2 flags / materiality note |
|---|---|---|---|
| NC0 (header, not counted) | R1242 | 472 | consolidated notes header |
| NC1 | R1142,R1243 | 473-479 | -; Consolidated note 1: basis of preparation |
| NC2 | R1005,R1143,R1244 | 480-482 | -; Consolidated note 2: Audit Committee review and Board approval |
| NC3 | R1245 | 483-486 | -; Consolidated note 3: limited review, unmodified conclusion |
| NC4 | R1099,R1246 | 487-489 | -; Consolidated note 4: filing with exchanges |
| NC5 | R1247 | 490-492 | -; Consolidated note 5: single segment |
| NC6 | R378-R379,R1248 | 493-496 | A1:OCR_SPACE; Consolidated note 6: ESOP allotment |
| NC7 | R380-R383,R1006,R1144,R1249 | 497-502 | RESTATED(QIP also on Reg 32(1) pp20-22); Consolidated note 7: QIP completed 13 April 2026 |
| NC8 | R384,R1145,R1250 | 503-508 | -; Consolidated note 8: CP and NCD issuance, listing |
| NC9 | R1007,R1100-R1102,R1146-R1148,R1251 | 509-515 | FOOTNOTE_UNRESOLVED(JASPL sale pending since 2021); Consolidated note 9: JASPL sale, assets held for sale (Ind AS 105) |
| NC10 | R1252 | 516-519 | -; Consolidated note 10 (marker OCR "I OJ"): regrouping of prior figures |
| NS1 | R1268-R1269 | 830-838 | -; Standalone note 1 (marker OCR "I]"): basis of preparation |
| NS2 | R1166,R1270 | 839-841 | -; Standalone note 2: Audit Committee review and Board approval |
| NS3 | R1271 | 842-843 | -; Standalone note 3: limited review |
| NS4 | R1103,R1272 | 844-845 | -; Standalone note 4: filing with exchanges |
| NS5 | R1273 | 846-846 | -; Standalone note 5: single segment |
| NS6 | R737,R1167,R1274 | 847-849 | A1:OCR_SPACE; Standalone note 6: ESOP allotment |
| NS7 | R738-R740,R1168,R1275 | 850-853 | RESTATED(QIP also on Reg 32(1) pp20-22) A1:OCR_SPACE; Standalone note 7: QIP |
| NS8 | R741,R1169,R1276 | 854-857 | -; Standalone note 8: CP and NCD issuance |
| NS9 | R1104-R1105,R1170-R1172,R1277 | 858-861 | FOOTNOTE_UNRESOLVED(JASPL sale pending since 2021); Standalone note 9: JASPL sale, held for sale |
| NS10 | R742,R1106,R1173,R1278 | 862-867 | -; Standalone note 10 (marker OCR "I OJ"): Reg 54 security cover maintained |
| NS11 | R743,R1012,R1174,R1279 | 868-869 | subnotes 11a-11d below; Standalone note 11 (marker OCR "I !]"): RBI transfer-of-loans disclosures, lead-in |
| NS11a (sub of NS11, not counted) | R744-R750,R1280 | 870-881 | A1:ZERO_STANDING; Standalone note 11(a): loans not in default transferred through assignment |
| NS11b (sub of NS11, not counted) | R751-R752,R1281 | 882-897 | A1:ZERO_STANDING ZERO_STANDING; Standalone note 11(b): loans not in default acquired through assignment (NIL) |
| NS11c (sub of NS11, not counted) | R753-R766,R1013,R1282-R1284 | 898-916 | A1:OCR_SPACE; Standalone note 11(c): stressed loans transferred to ARCs |
| NS11d (sub of NS11, not counted) | R1014-R1034,R1285 | 917-940 | A1:OCR_SUSPECT; Standalone note 11(d): ratings of security receipts |
| NS12 | R767-R790,R1175-R1178,R1286-R1291 | 941-965 | A1:COLUMN_UNRESOLVED OCR_SUSPECT ZERO_STANDING; Standalone note 12: COVID resolution framework table |
| NS13 | R1292 | 966-966 | -; Standalone note 13: regrouping of prior figures |
| ANXII_N1 | R1324 | 1751 | Annexure II note 1 (p30); column mapping on p30 unresolved |
| ANXII_N2 | R1325 | 1752 | Annexure II note 2 (p30); column mapping on p30 unresolved |
| ANXII_N3 | R1326 | 1753 | Annexure II note 3 (p30); column mapping on p30 unresolved |
| ANXII_N4 | R1327 | 1754 | Annexure II note 4 (p30); column mapping on p30 unresolved |

## T1b UNNUMBERED NOTES AND FOOTNOTES
| LEDGER_ID | ROW IDs | fulltext line | flags / note |
|---|---|---|---|
| FN01 | R1226 | 226 | JV (*) footnote: held for sale, equity method discontinued 13 Dec 2021 (auditor para 4) |
| FN02 | none | 469 | "Note:" under consolidated cash flow (p9) |
| FN03 | R1267 | 828 | "Note:" indirect method statement under standalone cash flow (p15) |
| FN04 | R763-R764,R1284 | 912 | Bullet under note 11(c): further 10,558 accounts transferred |
| FN05 | R790,R1290 | 963 | Footnote * IBC definition under note 12 table |
| FN06 | R1291 | 964 | Footnote # interest accrued under note 12 table |
| FN07 | R831,R1298 | 1033 | Footnote ** DRR not required for privately placed debentures (p19) |
| FN08 | R1299 | 1038 | Unmarked paragraph: CP and NCD issued/listed in H1 (p19) |
| FN09 | R843-R844,R1187,R1304 | 1144 | Footnote * on QIP table: net proceeds and issue expenses (p21) |
| FN10 | R1318 | 1568 | Footnote * on Annexure I outstanding column (p29) |

## T2 LINE ITEMS (financial statements pp7-9, 13-15 and Reg 52(4) p18). One row per source line; ROW IDs span the period columns.
| LEDGER_ID | statement | page | line | ROW IDs | A2 flags / note |
|---|---|---|---|---|---|
| LI7_292 | CONS P&L | 7 | 292 | R021-R026 | A1:OCR_SUSPECT |
| LI7_293 | CONS P&L | 7 | 293 | R027-R032 | - |
| LI7_294 | CONS P&L | 7 | 294 | R033-R038 | - |
| LI7_295 | CONS P&L | 7 | 295 | R039-R044 | - |
| LI7_296 | CONS P&L | 7 | 296 | R045-R050 | ZERO_STANDING |
| LI7_297 | CONS P&L | 7 | 297 | R051-R056 | - |
| LI7_298 | CONS P&L | 7 | 298 | R057-R062 | - |
| LI7_299 | CONS P&L | 7 | 299 | R063-R068 | - |
| LI7_301 | CONS P&L | 7 | 301 | R069-R074 | - |
| LI7_302 | CONS P&L | 7 | 302 | R075-R080 | - |
| LI7_303 | CONS P&L | 7 | 303 | R081-R086 | - |
| LI7_304 | CONS P&L | 7 | 304 | R087-R092 | - |
| LI7_305 | CONS P&L | 7 | 305 | R093-R098 | A1:OCR_SUSPECT |
| LI7_306 | CONS P&L | 7 | 306 | R099-R104 | - |
| LI7_307 | CONS P&L | 7 | 307 | R105-R110 | - |
| LI7_308 | CONS P&L | 7 | 308 | R111-R116 | - |
| LI7_310 | CONS P&L | 7 | 310 | R117-R122 | A1:OCR_SUSPECT |
| LI7_311 | CONS P&L | 7 | 311 | R123-R127 | ZERO_STANDING A1:OCR_SUSPECT |
| LI7_312 | CONS P&L | 7 | 312 | R128-R133 | A1:OCR_SUSPECT |
| LI7_313 | CONS P&L | 7 | 313 | R134-R139 | - |
| LI7_314 | CONS P&L | 7 | 314 | R140-R145 | - |
| LI7_317 | CONS P&L | 7 | 317 | R146-R151 | A1:OCR_SUSPECT |
| LI7_319 | CONS P&L | 7 | 319 | R152-R157 | A1:OCR_SUSPECT |
| LI7_323 | CONS P&L | 7 | 323 | R158-R163 | A1:OCR_SUSPECT |
| LI7_326 | CONS P&L | 7 | 326 | R164-R169 | - |
| LI7_329 | CONS P&L | 7 | 329 | R170-R175 | - |
| LI7_331 | CONS P&L | 7 | 331 | R176-R181 | A1:OCR_SUSPECT |
| LI7_332 | CONS P&L | 7 | 332 | R182-R187 | - |
| LI7_334 | CONS P&L | 7 | 334 | R188-R193 | A1:OCR_SUSPECT |
| LI7_336 | CONS P&L | 7 | 336 | R194-R199 | - |
| LI7_338 | CONS P&L | 7 | 338 | R200-R205 | A1:OCR_SUSPECT |
| LI7_339 | CONS P&L | 7 | 339 | R206-R211 | A1:OCR_SUSPECT |
| LI7_343 | CONS P&L | 7 | 343 | R212-R217 | - |
| LI7_344 | CONS P&L | 7 | 344 | R218-R223 | - |
| LI8_360 | CONS BS | 8 | 360 | R224-R225 | A1:OCR_SUSPECT |
| LI8_361 | CONS BS | 8 | 361 | R226-R227 | - |
| LI8_362 | CONS BS | 8 | 362 | R228-R229 | A1:OCR_SUSPECT |
| LI8_364 | CONS BS | 8 | 364 | R230-R231 | - |
| LI8_365 | CONS BS | 8 | 365 | R232-R233 | A1:OCR_SUSPECT |
| LI8_366 | CONS BS | 8 | 366 | R234-R235 | - |
| LI8_367 | CONS BS | 8 | 367 | R236-R237 | - |
| LI8_368 | CONS BS | 8 | 368 | R238-R239 | - |
| LI8_370 | CONS BS | 8 | 370 | R240-R241 | - |
| LI8_371 | CONS BS | 8 | 371 | R242-R243 | A1:OCR_SUSPECT |
| LI8_372 | CONS BS | 8 | 372 | R244-R245 | - |
| LI8_373 | CONS BS | 8 | 373 | R246-R247 | - |
| LI8_374 | CONS BS | 8 | 374 | R248-R249 | A1:OCR_SUSPECT |
| LI8_375 | CONS BS | 8 | 375 | R250-R251 | - |
| LI8_376 | CONS BS | 8 | 376 | R252-R253 | - |
| LI8_377 | CONS BS | 8 | 377 | R254-R255 | - |
| LI8_378 | CONS BS | 8 | 378 | R256-R257 | - |
| LI8_379 | CONS BS | 8 | 379 | R258-R259 | - |
| LI8_380 | CONS BS | 8 | 380 | R260-R261 | A1:OCR_SUSPECT |
| LI8_387 | CONS BS | 8 | 387 | R262-R263 | - |
| LI8_388 | CONS BS | 8 | 388 | R264-R265 | - |
| LI8_389 | CONS BS | 8 | 389 | R266-R267 | A1:OCR_SUSPECT |
| LI8_390 | CONS BS | 8 | 390 | R268-R269 | A1:OCR_SUSPECT |
| LI8_391 | CONS BS | 8 | 391 | R270-R271 | - |
| LI8_392 | CONS BS | 8 | 392 | R272-R273 | A1:OCR_SUSPECT |
| LI8_393 | CONS BS | 8 | 393 | R274-R275 | A1:OCR_SUSPECT |
| LI8_394 | CONS BS | 8 | 394 | R276-R277 | - |
| LI8_396 | CONS BS | 8 | 396 | R278-R279 | A1:OCR_SUSPECT |
| LI8_397 | CONS BS | 8 | 397 | R280-R281 | - |
| LI8_398 | CONS BS | 8 | 398 | R282-R283 | - |
| LI8_399 | CONS BS | 8 | 399 | R284-R285 | - |
| LI8_401 | CONS BS | 8 | 401 | R286-R287 | A1:OCR_SUSPECT |
| LI8_402 | CONS BS | 8 | 402 | R288-R289 | A1:OCR_SUSPECT |
| LI8_403 | CONS BS | 8 | 403 | R290-R291 | - |
| LI8_405 | CONS BS | 8 | 405 | R292-R293 | - |
| LI9_420 | CONS CF | 9 | 420 | R294-R295 | - |
| LI9_422 | CONS CF | 9 | 422 | R296-R297 | - |
| LI9_423 | CONS CF | 9 | 423 | R298-R299 | - |
| LI9_424 | CONS CF | 9 | 424 | R300-R301 | ZERO_STANDING |
| LI9_425 | CONS CF | 9 | 425 | R302-R303 | - |
| LI9_426 | CONS CF | 9 | 426 | R304-R305 | - |
| LI9_427 | CONS CF | 9 | 427 | R306-R307 | - |
| LI9_428 | CONS CF | 9 | 428 | R308-R309 | A1:OCR_SUSPECT |
| LI9_429 | CONS CF | 9 | 429 | R310-R311 | - |
| LI9_430 | CONS CF | 9 | 430 | R312-R313 | - |
| LI9_431 | CONS CF | 9 | 431 | R314-R315 | - |
| LI9_434 | CONS CF | 9 | 434 | R316-R317 | A1:OCR_SUSPECT |
| LI9_435 | CONS CF | 9 | 435 | R318-R319 | A1:OCR_SUSPECT |
| LI9_436 | CONS CF | 9 | 436 | R320-R321 | A1:OCR_SUSPECT |
| LI9_437 | CONS CF | 9 | 437 | R322-R323 | - |
| LI9_438 | CONS CF | 9 | 438 | R324-R325 | - |
| LI9_440 | CONS CF | 9 | 440 | R326-R327 | - |
| LI9_441 | CONS CF | 9 | 441 | R328-R329 | - |
| LI9_442 | CONS CF | 9 | 442 | R330-R331 | - |
| LI9_443 | CONS CF | 9 | 443 | R332-R333 | - |
| LI9_444 | CONS CF | 9 | 444 | R334-R335 | - |
| LI9_445 | CONS CF | 9 | 445 | R336-R337 | - |
| LI9_446 | CONS CF | 9 | 446 | R338-R339 | A1:OCR_SUSPECT |
| LI9_448 | CONS CF | 9 | 448 | R340-R341 | - |
| LI9_449 | CONS CF | 9 | 449 | R342-R343 | A1:OCR_SUSPECT |
| LI9_450 | CONS CF | 9 | 450 | R344-R345 | A1:OCR_SUSPECT |
| LI9_451 | CONS CF | 9 | 451 | R346-R347 | - |
| LI9_452 | CONS CF | 9 | 452 | R348-R349 | - |
| LI9_453 | CONS CF | 9 | 453 | R350-R351 | A1:OCR_SUSPECT |
| LI9_454 | CONS CF | 9 | 454 | R352-R353 | - |
| LI9_456 | CONS CF | 9 | 456 | R354-R355 | A1:OCR_SUSPECT |
| LI9_457 | CONS CF | 9 | 457 | R356-R357 | - |
| LI9_458 | CONS CF | 9 | 458 | R358-R359 | A1:OCR_SUSPECT |
| LI9_459 | CONS CF | 9 | 459 | R360-R361 | A1:OCR_SUSPECT |
| LI9_460 | CONS CF | 9 | 460 | R362-R363 | - |
| LI9_461 | CONS CF | 9 | 461 | R364-R365 | A1:OCR_SUSPECT |
| LI9_462 | CONS CF | 9 | 462 | R366-R367 | A1:OCR_SUSPECT |
| LI9_463 | CONS CF | 9 | 463 | R368-R369 | - |
| LI9_464 | CONS CF | 9 | 464 | R370-R371 | - |
| LI9_465 | CONS CF | 9 | 465 | R372-R373 | - |
| LI9_466 | CONS CF | 9 | 466 | R374-R375 | A1:OCR_SUSPECT |
| LI9_467 | CONS CF | 9 | 467 | R376-R377 | A1:OCR_SUSPECT |
| LI13_644 | STAND P&L | 13 | 644 | R399-R404 | A1:OCR_SUSPECT |
| LI13_645 | STAND P&L | 13 | 645 | R405-R410 | - |
| LI13_646 | STAND P&L | 13 | 646 | R411-R416 | - |
| LI13_647 | STAND P&L | 13 | 647 | R417-R422 | - |
| LI13_648 | STAND P&L | 13 | 648 | R423-R428 | ZERO_STANDING |
| LI13_649 | STAND P&L | 13 | 649 | R429-R434 | - |
| LI13_650 | STAND P&L | 13 | 650 | R435-R440 | - |
| LI13_651 | STAND P&L | 13 | 651 | R441-R446 | - |
| LI13_653 | STAND P&L | 13 | 653 | R447-R452 | A1:OCR_SUSPECT |
| LI13_654 | STAND P&L | 13 | 654 | R453-R458 | A1:OCR_SUSPECT |
| LI13_655 | STAND P&L | 13 | 655 | R459-R464 | A1:OCR_SUSPECT |
| LI13_656 | STAND P&L | 13 | 656 | R465-R470 | A1:OCR_SUSPECT |
| LI13_657 | STAND P&L | 13 | 657 | R471-R476 | - |
| LI13_658 | STAND P&L | 13 | 658 | R477-R482 | - |
| LI13_659 | STAND P&L | 13 | 659 | R483-R488 | - |
| LI13_660 | STAND P&L | 13 | 660 | R489-R494 | - |
| LI13_662 | STAND P&L | 13 | 662 | R495-R500 | A1:OCR_SUSPECT |
| LI13_663 | STAND P&L | 13 | 663 | R501-R504 | ZERO_STANDING A1:OCR_SUSPECT |
| LI13_664 | STAND P&L | 13 | 664 | R505-R510 | A1:OCR_SUSPECT |
| LI13_665 | STAND P&L | 13 | 665 | R511-R516 | - |
| LI13_666 | STAND P&L | 13 | 666 | R517-R522 | - |
| LI13_669 | STAND P&L | 13 | 669 | R523-R528 | A1:OCR_SUSPECT |
| LI13_671 | STAND P&L | 13 | 671 | R529-R534 | A1:OCR_SUSPECT |
| LI13_674 | STAND P&L | 13 | 674 | R535-R540 | A1:OCR_SUSPECT |
| LI13_676 | STAND P&L | 13 | 676 | R541-R546 | A1:OCR_SUSPECT |
| LI13_679 | STAND P&L | 13 | 679 | R547-R552 | A1:OCR_SUSPECT |
| LI13_681 | STAND P&L | 13 | 681 | R553-R558 | - |
| LI13_682 | STAND P&L | 13 | 682 | R559-R564 | - |
| LI13_683 | STAND P&L | 13 | 683 | R565-R570 | A1:OCR_SUSPECT |
| LI13_685 | STAND P&L | 13 | 685 | R571-R576 | A1:OCR_SUSPECT |
| LI13_686 | STAND P&L | 13 | 686 | R577-R582 | - |
| LI14_713 | STAND BS | 14 | 713 | R583-R584 | A1:OCR_SUSPECT |
| LI14_714 | STAND BS | 14 | 714 | R585-R586 | - |
| LI14_715 | STAND BS | 14 | 715 | R587-R588 | - |
| LI14_717 | STAND BS | 14 | 717 | R589-R590 | - |
| LI14_718 | STAND BS | 14 | 718 | R591-R592 | - |
| LI14_719 | STAND BS | 14 | 719 | R593-R594 | A1:OCR_SUSPECT |
| LI14_720 | STAND BS | 14 | 720 | R595-R596 | - |
| LI14_721 | STAND BS | 14 | 721 | R597-R598 | - |
| LI14_724 | STAND BS | 14 | 724 | R599-R600 | - |
| LI14_725 | STAND BS | 14 | 725 | R601-R602 | A1:OCR_SUSPECT |
| LI14_726 | STAND BS | 14 | 726 | R603-R604 | - |
| LI14_727 | STAND BS | 14 | 727 | R605-R606 | - |
| LI14_728 | STAND BS | 14 | 728 | R607-R608 | - |
| LI14_729 | STAND BS | 14 | 729 | R609-R610 | - |
| LI14_730 | STAND BS | 14 | 730 | R611-R612 | - |
| LI14_731 | STAND BS | 14 | 731 | R613-R614 | - |
| LI14_732 | STAND BS | 14 | 732 | R615-R616 | - |
| LI14_734 | STAND BS | 14 | 734 | R617-R618 | - |
| LI14_736 | STAND BS | 14 | 736 | R619-R620 | A1:OCR_SUSPECT |
| LI14_743 | STAND BS | 14 | 743 | R621-R622 | - |
| LI14_744 | STAND BS | 14 | 744 | R623-R624 | - |
| LI14_745 | STAND BS | 14 | 745 | R625-R626 | A1:OCR_SUSPECT |
| LI14_746 | STAND BS | 14 | 746 | R627-R628 | A1:OCR_SUSPECT |
| LI14_747 | STAND BS | 14 | 747 | R629-R630 | - |
| LI14_748 | STAND BS | 14 | 748 | R631-R632 | A1:OCR_SUSPECT |
| LI14_749 | STAND BS | 14 | 749 | R633-R634 | - |
| LI14_750 | STAND BS | 14 | 750 | R635-R636 | - |
| LI14_753 | STAND BS | 14 | 753 | R637-R638 | A1:OCR_SUSPECT |
| LI14_754 | STAND BS | 14 | 754 | R639-R640 | A1:OCR_SUSPECT |
| LI14_755 | STAND BS | 14 | 755 | R641-R642 | - |
| LI14_756 | STAND BS | 14 | 756 | R643-R644 | - |
| LI14_759 | STAND BS | 14 | 759 | R645-R646 | A1:OCR_SUSPECT |
| LI14_760 | STAND BS | 14 | 760 | R647-R648 | A1:OCR_SUSPECT |
| LI14_761 | STAND BS | 14 | 761 | R649-R650 | - |
| LI14_763 | STAND BS | 14 | 763 | R651-R652 | - |
| LI15_778 | STAND CF | 15 | 778 | R653-R654 | - |
| LI15_780 | STAND CF | 15 | 780 | R655-R656 | A1:OCR_SUSPECT |
| LI15_781 | STAND CF | 15 | 781 | R657-R658 | - |
| LI15_782 | STAND CF | 15 | 782 | R659-R660 | ZERO_STANDING |
| LI15_783 | STAND CF | 15 | 783 | R661-R662 | - |
| LI15_784 | STAND CF | 15 | 784 | R663-R664 | A1:OCR_SUSPECT |
| LI15_785 | STAND CF | 15 | 785 | R665-R666 | - |
| LI15_786 | STAND CF | 15 | 786 | R667-R668 | - |
| LI15_787 | STAND CF | 15 | 787 | R669-R670 | - |
| LI15_788 | STAND CF | 15 | 788 | R671-R672 | A1:OCR_SUSPECT |
| LI15_789 | STAND CF | 15 | 789 | R673-R674 | - |
| LI15_792 | STAND CF | 15 | 792 | R675-R676 | - |
| LI15_793 | STAND CF | 15 | 793 | R677-R678 | A1:OCR_SUSPECT |
| LI15_794 | STAND CF | 15 | 794 | R679-R680 | A1:OCR_SUSPECT |
| LI15_795 | STAND CF | 15 | 795 | R681-R682 | A1:OCR_SUSPECT |
| LI15_796 | STAND CF | 15 | 796 | R683-R684 | - |
| LI15_798 | STAND CF | 15 | 798 | R685-R686 | A1:OCR_SUSPECT |
| LI15_799 | STAND CF | 15 | 799 | R687-R688 | A1:OCR_SUSPECT |
| LI15_800 | STAND CF | 15 | 800 | R689-R690 | A1:OCR_SUSPECT |
| LI15_801 | STAND CF | 15 | 801 | R691-R692 | - |
| LI15_802 | STAND CF | 15 | 802 | R693-R694 | - |
| LI15_803 | STAND CF | 15 | 803 | R695-R696 | A1:OCR_SUSPECT |
| LI15_804 | STAND CF | 15 | 804 | R697-R698 | A1:OCR_SUSPECT |
| LI15_806 | STAND CF | 15 | 806 | R699-R700 | A1:OCR_SUSPECT |
| LI15_807 | STAND CF | 15 | 807 | R701-R702 | - |
| LI15_808 | STAND CF | 15 | 808 | R703-R704 | A1:OCR_SUSPECT |
| LI15_809 | STAND CF | 15 | 809 | R705-R706 | - |
| LI15_810 | STAND CF | 15 | 810 | R707-R708 | A1:OCR_SUSPECT |
| LI15_811 | STAND CF | 15 | 811 | R709-R710 | A1:OCR_SUSPECT |
| LI15_812 | STAND CF | 15 | 812 | R711-R712 | - |
| LI15_814 | STAND CF | 15 | 814 | R713-R714 | A1:OCR_SUSPECT |
| LI15_815 | STAND CF | 15 | 815 | R715-R716 | - |
| LI15_816 | STAND CF | 15 | 816 | R717-R718 | A1:OCR_SUSPECT |
| LI15_817 | STAND CF | 15 | 817 | R719-R720 | A1:OCR_SUSPECT |
| LI15_818 | STAND CF | 15 | 818 | R721-R722 | - |
| LI15_819 | STAND CF | 15 | 819 | R723-R724 | A1:OCR_SUSPECT |
| LI15_820 | STAND CF | 15 | 820 | R725-R726 | A1:OCR_SUSPECT |
| LI15_821 | STAND CF | 15 | 821 | R727-R728 | A1:OCR_SUSPECT |
| LI15_822 | STAND CF | 15 | 822 | R729-R730 | A1:OCR_SUSPECT |
| LI15_824 | STAND CF | 15 | 824 | R731-R732 | - |
| LI15_825 | STAND CF | 15 | 825 | R733-R734 | - |
| LI15_826 | STAND CF | 15 | 826 | R735-R736 | A1:OCR_SUSPECT |
| R52_989 | REG52(4) | 18 | 989 | R791-R792 | - |
| R52_990 | REG52(4) | 18 | 990 | R793 | A1:NOT_APPLICABLE |
| R52_991 | REG52(4) | 18 | 991 | R794 | A1:NOT_APPLICABLE |
| R52_993 | REG52(4) | 18 | 993 | R795-R796 | ZERO_STANDING |
| R52_994 | REG52(4) | 18 | 994 | R797 | - |
| R52_995 | REG52(4) | 18 | 995 | R798-R799 | - |
| R52_996 | REG52(4) | 18 | 996 | R800-R801 | ZERO_STANDING |
| R52_997 | REG52(4) | 18 | 997 | R802-R803 | - |
| R52_999 | REG52(4) | 18 | 999 | R804-R805 | - |
| R52_1000 | REG52(4) | 18 | 1000 | R806-R807 | - |
| R52_1002 | REG52(4) | 18 | 1002 | R808-R809 | - |
| R52_1003 | REG52(4) | 18 | 1003 | R810-R811 | - |
| R52_1004 | REG52(4) | 18 | 1004 | R812-R813 | - |
| R52_1005 | REG52(4) | 18 | 1005 | R814-R815 | - |
| R52_1006 | REG52(4) | 18 | 1006 | R816 | A1:NOT_APPLICABLE |
| R52_1007 | REG52(4) | 18 | 1007 | R817 | A1:NOT_APPLICABLE |
| R52_1008 | REG52(4) | 18 | 1008 | R818 | A1:NOT_APPLICABLE |
| R52_1009 | REG52(4) | 18 | 1009 | R819 | A1:NOT_APPLICABLE |
| R52_1010 | REG52(4) | 18 | 1010 | R820-R821 | - |
| R52_1011 | REG52(4) | 18 | 1011 | R822 | A1:NOT_APPLICABLE |
| R52_1012 | REG52(4) | 18 | 1012 | R823 | A1:NOT_APPLICABLE |
| R52_1013 | REG52(4) | 18 | 1013 | R824 | A1:NOT_APPLICABLE |
| R52_1015 | REG52(4) | 18 | 1015 | R825-R826 | - |
| R52_1016 | REG52(4) | 18 | 1016 | R827-R828 | - |
| R52_1018 | REG52(4) | 18 | 1018 | R829 | - |
| R52_1019 | REG52(4) | 18 | 1019 | R830 | - |

## T2b STATEMENT-PAGE NON-NUMERIC ROWS (entity/date/qualifier cross-references on table pages)
| LEDGER_ID | ROW IDs | note |
|---|---|---|
| TQ7 | R1004,R1132-R1137,R1232-R1236 | Non-numeric rows on statement page 7 (entity/date/qualifier cross-references) |
| R52Q | R1036,R1180-R1182,R1293-R1297 | Reg 52(4) page non-numeric rows (entity/date/qualifier) |
| TQ8 | R1138-R1139,R1237-R1238 | Non-numeric rows on statement page 8 (entity/date/qualifier cross-references) |
| TQ9 | R1140-R1141,R1239-R1241 | Non-numeric rows on statement page 9 (entity/date/qualifier cross-references) |
| TQ13 | R1156-R1161,R1259-R1262 | Non-numeric rows on statement page 13 (entity/date/qualifier cross-references) |
| TQ14 | R1162-R1163,R1263-R1264 | Non-numeric rows on statement page 14 (entity/date/qualifier cross-references) |
| TQ15 | R1164-R1165,R1265-R1267 | Non-numeric rows on statement page 15 (entity/date/qualifier cross-references) |

## T3 ZERO_STANDING ROWS (A1 flagged, A2 confirmed by independent dash/nil sweep of fulltext)
| ROW ID | page | line | A2 flag |
|---|---|---|---|
| R012 | 6 | 239 | ZERO_STANDING |
| R013 | 6 | 239 | ZERO_STANDING |
| R014 | 6 | 240 | ZERO_STANDING |
| R015 | 6 | 240 | ZERO_STANDING |
| R045 | 7 | 296 | ZERO_STANDING |
| R124 | 7 | 311 | ZERO_STANDING |
| R126 | 7 | 311 | ZERO_STANDING |
| R300 | 9 | 424 | ZERO_STANDING |
| R389 | 11 | 582 | ZERO_STANDING |
| R390 | 11 | 582 | ZERO_STANDING |
| R391 | 11 | 583 | ZERO_STANDING |
| R392 | 11 | 583 | ZERO_STANDING |
| R423 | 13 | 648 | ZERO_STANDING |
| R503 | 13 | 663 | ZERO_STANDING |
| R659 | 15 | 782 | ZERO_STANDING |
| R746 | 16 | 876 | ZERO_STANDING |
| R751 | 16 | 890 | ZERO_STANDING |
| R752 | 16 | 890 | ZERO_STANDING |
| R769 | 17 | 958 | ZERO_STANDING COLUMN_UNRESOLVED |
| R770 | 17 | 958 | ZERO_STANDING COLUMN_UNRESOLVED |
| R771 | 17 | 958 | ZERO_STANDING COLUMN_UNRESOLVED |
| R772 | 17 | 959 | ZERO_STANDING COLUMN_UNRESOLVED |
| R773 | 17 | 959 | ZERO_STANDING COLUMN_UNRESOLVED |
| R774 | 17 | 959 | ZERO_STANDING COLUMN_UNRESOLVED |
| R775 | 17 | 959 | ZERO_STANDING COLUMN_UNRESOLVED |
| R776 | 17 | 960 | ZERO_STANDING COLUMN_UNRESOLVED |
| R777 | 17 | 960 | ZERO_STANDING COLUMN_UNRESOLVED |
| R778 | 17 | 960 | ZERO_STANDING COLUMN_UNRESOLVED |
| R779 | 17 | 960 | ZERO_STANDING COLUMN_UNRESOLVED |
| R795 | 18 | 993 | ZERO_STANDING |
| R796 | 18 | 993 | ZERO_STANDING |
| R800 | 18 | 996 | ZERO_STANDING |
| R801 | 18 | 996 | ZERO_STANDING |

Sweep-only candidates, NOT counted (dash glyphs in OCR-garbled form/column areas, A1 did not emit a value row): fulltext lines 1111 (p20 form), 1656, 1662, 1664, 1686 (p30 Annexure II). Flag ZERO_STANDING_CANDIDATE, column mapping unresolved; A3 to confirm against the page image via A1 if material.

## T4 AGENDA ITEMS / BOARD OUTCOME LETTER
| LEDGER_ID | ROW IDs | fulltext lines | A2 flags / note |
|---|---|---|---|
| AG1 | R1109 | 36-42 | -; Board approval item 1: unaudited standalone and consolidated results Q2/H1 FY27 |
| ENC1 | R1094,R1215 | 43-46 | -; Enclosure 1: results (newspaper publication follows) |
| ENC2 | R981-R982,R1216 | 47-50 | AUDITOR_CHANGE context: Kirtane and Pandit LLP now "previous joint auditor" (see T5 AUDC7/AUDS6); Enclosure 2: Limited Review Reports (joint auditors MSKA, B K Khare) |
| ENC3 | none | 51-52 | -; Enclosure 3: Reg 52(4) line-item statement |
| ENC4 | R983 | 53-55 | -; Enclosure 4: QIP deviation statement Reg 32(1) |
| ENC5 | R1110 | 56-59 | -; Enclosure 5: Reg 52(7)/52(7A) statement |
| ENC6 | R1111-R1112,R1217 | 60-70 | -; Enclosure 6: Reg 54 security cover disclosure |
| AG4 | R984-R985,R1095 | 71-77 | -; Investor Presentation sent separately (Reg 30); NRC recommendation lead-in |
| AG2 | R002-R003,R986,R1096,R1113-R1115,R1218 | 78-89 | FORWARD (R1096,R1097,R1098); director re-appointment, term 30 Jan 2027 to 29 Jan 2030; Board approval: re-appointment of independent director Kemisha Soni, 2nd term, special resolution |
| AG3 | R1097 | 90-93 | FORWARD (postal ballot pending); Board approval: Postal Ballot Notice for the re-appointment |
| AGT | R004-R005,R1116 | 94-95 | MEETING_DURATION 107 min (1:45 PM to 3:32 PM); signature 16:23:14 is after close, no flag; Board meeting start 1:45 PM and end 3:32 PM (107 minutes) |

Agenda coverage note: the letter carries NO items for dividend, AR approval, AGM notice, record date, auditor appointment, ESOP grants or capital-raising enabling resolutions. Absence recorded, not inferred.

### T4b ANNEXURE A (director disclosure) items
| LEDGER_ID | ROW IDs | fulltext lines | note |
|---|---|---|---|
| ANXA1 | R007,R1118 | 117-126 | Annexure A item 1: reason for change |
| ANXA2 | R008,R1098,R1119,R1220 | 127-130 | Annexure A item 2: date and term of re-appointment |
| ANXA3 | R009-R011,R989-R997 | 131-158 | Annexure A item 3: brief profile |
| ANXA4 | R1221 | 159-167 | Annexure A item 4: relationship between directors |
| ANXA5 | R998,R1120,R1222 | 168-182 | Annexure A item 5: debarment confirmation, BSE/NSE circular references |

### T4c LETTER HEADER AND SIGNATURES
| LEDGER_ID | ROW IDs | fulltext lines | note |
|---|---|---|---|
| AG0 | R001,R976-R980,R1107-R1108 | 1-35 | Cover letter header, addressees, subject, regulation reference |
| SIG1 | R006,R987-R988,R1117,R1219 | 96-116 | Cover letter signatory (Company Secretary), digital signature 2026.10.09 16:23:14 |
| SIG2 | R385-R387,R1008-R1009,R1149 | 520-534 | Consolidated results signature block, DIN, CIN, addresses |
| SIG3 | R1035,R1179 | 967-983 | Standalone results signature block, place, date, addresses |
| AUDC8 | R016-R020,R1003,R1131 | 259-277 | Consolidated LRR signature block: firm regs, UDINs, place, date |
| AUDS7 | R394-R398,R1011,R1155 | 609-631 | Standalone LRR signature block: firm regs, UDINs, place, date |
| AUDK13 | R892-R894,R1066,R1210 | 1518-1531 | Certificate signature block: firm reg, UDIN, place, date |

## T5 AUDITOR REPORT PARAGRAPHS
Opinion type in all three documents: unmodified conclusion on limited review (consolidated and standalone) and limited assurance conclusion (certificate). No Emphasis of Matter. No Going Concern language. Other-matter style paragraphs: AUDC6, AUDS5. Prior-auditor paragraphs: AUDC7, AUDS6.
| LEDGER_ID | ROW IDs | fulltext lines | A2 flags / note |
|---|---|---|---|
| AUDC0 | R999-R1000 | 183-196 | -; Consolidated LRR header, addressee and title (header, not counted as a paragraph) |
| AUDC1 | R1121-R1122 | 197-202 | -; Consolidated LRR para 1: scope of review |
| AUDC2 | none | 203-208 | NO_STRUCTURED_ROW(boilerplate; unit located by line range); Consolidated LRR para 2: management responsibility, Ind AS 34 |
| AUDC3 | R1223-R1224 | 209-218 | -; Consolidated LRR para 3: SRE 2410 basis, no audit opinion |
| AUDC4 | R1001,R1123,R1225-R1226 | 219-227 | ENTITY list; ENTITY_CHANGE ND (no prior); Consolidated LRR para 4: entity list (JASPL JV, held for sale) |
| AUDC5 | none | 228-238 | NO_STRUCTURED_ROW(boilerplate; unit located by line range); Consolidated LRR para 5: conclusion (nothing came to attention) |
| AUDC6 | R012-R015,R1124,R1227-R1229 | 239-248 | OTHER_MATTER; unreviewed management-furnished data; Consolidated LRR para 6: JV figures unreviewed, management furnished (other matter) |
| AUDC7 | R1002,R1125-R1130,R1230-R1231 | 249-258 | AUDITOR_CHANGE(previous joint auditor Kirtane and Pandit LLP); Consolidated LRR para 7: prior period reviewed/audited by Kirtane and Pandit LLP |
| AUDS0 | none | 535-548 | NO_STRUCTURED_ROW(boilerplate; unit located by line range); Standalone LRR header, addressee and title (header, not counted as a paragraph) |
| AUDS1 | none | 549-555 | NO_STRUCTURED_ROW(boilerplate; unit located by line range); Standalone LRR para 1: scope |
| AUDS2 | none | 556-562 | NO_STRUCTURED_ROW(boilerplate; unit located by line range); Standalone LRR para 2: management responsibility |
| AUDS3 | R1253 | 563-571 | -; Standalone LRR para 3: SRE 2410 basis |
| AUDS4 | R1254 | 572-579 | -; Standalone LRR para 4: conclusion (nothing came to attention) |
| AUDS5 | R388-R393,R1010,R1150-R1151,R1255-R1257 | 580-597 | OTHER_MATTER; unreviewed management-furnished data; Standalone LRR para 5: PFL Employee Welfare Trust unreviewed, management furnished (other matter) |
| AUDS6 | R1152-R1154,R1258 | 598-608 | AUDITOR_CHANGE(previous joint auditor Kirtane and Pandit LLP); Standalone LRR para 6: prior period reviewed/audited by Kirtane and Pandit LLP |
| AUDK0 | R890,R1063-R1064,R1206 | 1357-1375 | -; Security cover certificate header, addressee, title (header, not counted as a paragraph) |
| AUDK1 | R891,R1207 | 1376-1378 | -; Certificate para 1: engagement letter |
| AUDK2 | R1208,R1310 | 1379-1391 | -; Certificate para 2: statement and basis |
| AUDK3 | none | 1392-1399 | NO_STRUCTURED_ROW(boilerplate; unit located by line range); Certificate para 3: management responsibility |
| AUDK4 | none | 1400-1404 | NO_STRUCTURED_ROW(boilerplate; unit located by line range); Certificate para 4: compliance responsibility |
| AUDK5 | R1311 | 1405-1424 | -; Certificate para 5: auditor responsibility, limited assurance |
| AUDK6 | R1065,R1209,R1312 | 1425-1437 | -; Certificate para 6: standalone results reviewed, unmodified conclusion 09 Oct 2026 |
| AUDK7 | none | 1438-1442 | NO_STRUCTURED_ROW(boilerplate; unit located by line range); Certificate para 7: Guidance Note basis |
| AUDK8 | none | 1443-1446 | NO_STRUCTURED_ROW(boilerplate; unit located by line range); Certificate para 8: SQC 1 compliance |
| AUDK9 | R1313-R1314 | 1447-1485 | -; Certificate para 9: limited assurance procedures (a) to (f) |
| AUDK10 | none | 1486-1498 | NO_STRUCTURED_ROW(boilerplate; unit located by line range); Certificate para 10: conclusion |
| AUDK11 | R1315 | 1499-1508 | -; Certificate para 11: restriction on distribution |
| AUDK12 | none | 1509-1517 | NO_STRUCTURED_ROW(boilerplate; unit located by line range); Certificate para 12: addressee and use restriction |

## T6 CONSOLIDATION ENTITIES (auditor entity lists)
| LEDGER_ID | ROW IDs | relationship | A2 flags |
|---|---|---|---|
| ENT01 | R1001,R1225 (line 224) | Jaguar Advisory Services Private Limited (JASPL): Joint venture; held for sale per Ind AS 105; equity method discontinued 13 Dec 2021; share of profit ~Nil | ENTITY_CHANGE: ND (no prior ledger) |
| ENT02 | R1010,R1255 (line 580) | PFL Employee Welfare Trust: Included in standalone statement; interim info unreviewed by other auditor; total assets Rs 0.41 cr, revenue and NPAT Nil | ENTITY_CHANGE: ND (no prior ledger) |
A1 ENTITY table rows (118) are all accounted in groups on this ledger (cover letter, annexure, auditors, notes, annexures). Entity_count_in_consolidation_list: 2.

## T7 ANNEXURES AND TABLES, pp19-30 (one row per source line that carries structured rows)
| LEDGER_ID | page | line | ROW IDs | table | A2 flags |
|---|---|---|---|---|---|
| FN19_1033 | 19 | 1033 | R831,R1298 | Reg 52(4) footnote page | - |
| FN19_1034 | 19 | 1034 | R832 | Reg 52(4) footnote page | - |
| FN19_1040 | 19 | 1040 | R833 | Reg 52(4) footnote page | - |
| FN19_1053 | 19 | 1053 | R834 | Reg 52(4) footnote page | - |
| FN19_1060 | 19 | 1060 | R835 | Reg 52(4) footnote page | - |
| ANX20_1079 | 20 | 1079 | R836 | QIP deviation statement (Rs million) table A | - |
| ANX20_1113 | 20 | 1113 | R837-R838 | QIP deviation statement (Rs million) table A | A1:COLUMN_UNRESOLVED |
| ANX20_1120 | 20 | 1120 | R839-R840 | QIP deviation statement (Rs million) table A | A1:COLUMN_UNRESOLVED |
| ANX21_1137 | 21 | 1137 | R841-R842,R1302 | QIP deviation statement (Rs million) table A/B | - |
| ANX21_1144 | 21 | 1144 | R843-R844,R1187,R1304 | QIP deviation statement (Rs million) table A/B | - |
| ANX21_1147 | 21 | 1147 | R845 | QIP deviation statement (Rs million) table A/B | - |
| ANX21_1150 | 21 | 1150 | R846,R1305 | QIP deviation statement (Rs million) table A/B | - |
| ANX21_1151 | 21 | 1151 | R847 | QIP deviation statement (Rs million) table A/B | - |
| ANX21_1152 | 21 | 1152 | R848 | QIP deviation statement (Rs million) table A/B | - |
| ANX22_1186 | 22 | 1186 | R849 | NCD proceeds deviation statement (Rs crore) | - |
| ANX22_1191 | 22 | 1191 | R850 | NCD proceeds deviation statement (Rs crore) | - |
| ANX22_1203 | 22 | 1203 | R851 | NCD proceeds deviation statement (Rs crore) | - |
| ANX23_1234 | 23 | 1234 | R852,R1046,R1192 | Reg 32 NCD issue list, ISIN/series/value date/amount | - |
| ANX23_1236 | 23 | 1236 | R853,R1047,R1193 | Reg 32 NCD issue list, ISIN/series/value date/amount | - |
| ANX23_1238 | 23 | 1238 | R854,R1048,R1194 | Reg 32 NCD issue list, ISIN/series/value date/amount | - |
| ANX23_1239 | 23 | 1239 | R855,R1049,R1195 | Reg 32 NCD issue list, ISIN/series/value date/amount | - |
| ANX23_1241 | 23 | 1241 | R856,R1050,R1196 | Reg 32 NCD issue list, ISIN/series/value date/amount | - |
| ANX23_1244 | 23 | 1244 | R857,R1051,R1197 | Reg 32 NCD issue list, ISIN/series/value date/amount | - |
| ANX23_1246 | 23 | 1246 | R858,R1052,R1198 | Reg 32 NCD issue list, ISIN/series/value date/amount | - |
| ANX23_1247 | 23 | 1247 | R859 | Reg 32 NCD issue list, ISIN/series/value date/amount | - |
| ANX24_1273 | 24 | 1273 | R860-R863,R1054,R1199 | Annexure A: utilisation of issue proceeds (absolute rupees) | A1:COLUMN_UNRESOLVED |
| ANX24_1281 | 24 | 1281 | R864-R867,R1055,R1200 | Annexure A: utilisation of issue proceeds (absolute rupees) | A1:COLUMN_UNRESOLVED |
| ANX24_1289 | 24 | 1289 | R868-R871,R1056,R1201 | Annexure A: utilisation of issue proceeds (absolute rupees) | A1:COLUMN_UNRESOLVED |
| ANX24_1296 | 24 | 1296 | R872-R875,R1057,R1202 | Annexure A: utilisation of issue proceeds (absolute rupees) | A1:COLUMN_UNRESOLVED |
| ANX24_1304 | 24 | 1304 | R876-R879,R1058,R1203 | Annexure A: utilisation of issue proceeds (absolute rupees) | A1:COLUMN_UNRESOLVED |
| ANX25_1332 | 25 | 1332 | R880-R883,R1060,R1204 | Annexure A: utilisation of issue proceeds (absolute rupees) | A1:COLUMN_UNRESOLVED |
| ANX25_1338 | 25 | 1338 | R884-R887,R1061,R1205 | Annexure A: utilisation of issue proceeds (absolute rupees) | A1:COLUMN_UNRESOLVED |
| ANX25_1341 | 25 | 1341 | R888-R889 | Annexure A: utilisation of issue proceeds (absolute rupees) | A1:COLUMN_UNRESOLVED |
| ANX29_1539 | 29 | 1539 | R895,R1068 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1540 | 29 | 1540 | R896,R1069 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1541 | 29 | 1541 | R897 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1542 | 29 | 1542 | R898,R1070 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1543 | 29 | 1543 | R899,R1071 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1544 | 29 | 1544 | R900,R1072 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1545 | 29 | 1545 | R901,R1073 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1546 | 29 | 1546 | R902,R1074 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1547 | 29 | 1547 | R903,R1075 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1548 | 29 | 1548 | R904,R1076 | Annexure I: ISIN-wise secured NCDs outstanding | A1:OCR_SPACE |
| ANX29_1549 | 29 | 1549 | R905,R1077 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1550 | 29 | 1550 | R906,R1078 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1551 | 29 | 1551 | R907,R1079 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1552 | 29 | 1552 | R908,R1080 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1553 | 29 | 1553 | R909,R1081 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1554 | 29 | 1554 | R910,R1082 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1555 | 29 | 1555 | R911,R1083 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1556 | 29 | 1556 | R912,R1084 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1557 | 29 | 1557 | R913,R1085 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1558 | 29 | 1558 | R914,R1086 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1559 | 29 | 1559 | R915,R1087 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1560 | 29 | 1560 | R916,R1088 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1561 | 29 | 1561 | R917,R1089 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1562 | 29 | 1562 | R918,R1090 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1563 | 29 | 1563 | R919,R1091 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1567 | 29 | 1567 | R920 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX30_1688 | 30 | 1688 | R921 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1700 | 30 | 1700 | R922-R923 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1703 | 30 | 1703 | R924-R925 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1705 | 30 | 1705 | R926-R927 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1706 | 30 | 1706 | R928-R929 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1707 | 30 | 1707 | R930-R931 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1708 | 30 | 1708 | R932-R935 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1709 | 30 | 1709 | R936,R1321 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1712 | 30 | 1712 | R937-R938 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1713 | 30 | 1713 | R939-R940 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1714 | 30 | 1714 | R941-R942 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1716 | 30 | 1716 | R943-R944 | Annexure II: book value of assets (columns A to O unresolved) | A1:OCR_SUSPECT A1:COLUMN_UNRESOLVED |
| ANX30_1717 | 30 | 1717 | R945-R949 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1722 | 30 | 1722 | R950-R951,R1322 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1723 | 30 | 1723 | R952 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1729 | 30 | 1729 | R953-R954 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1730 | 30 | 1730 | R955-R956 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1732 | 30 | 1732 | R957-R958 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1736 | 30 | 1736 | R959-R960 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1737 | 30 | 1737 | R961-R962 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1738 | 30 | 1738 | R963-R964 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1739 | 30 | 1739 | R965-R966 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1740 | 30 | 1740 | R967-R968 | Annexure II: book value of assets (columns A to O unresolved) | A1:COLUMN_UNRESOLVED |
| ANX30_1741 | 30 | 1741 | R969-R973 | Annexure II: book value of assets (columns A to O unresolved) | A1:OCR_SUSPECT A1:COLUMN_UNRESOLVED |
| ANX30_1742 | 30 | 1742 | R974-R975 | Annexure II: book value of assets (columns A to O unresolved) | A1:OCR_SUSPECT A1:COLUMN_UNRESOLVED |
| FN19_1051 | 19 | 1051 | R1037 | Reg 52(4) footnote page | - |
| FN19_1058 | 19 | 1058 | R1038 | Reg 52(4) footnote page | - |
| ANX20_1073 | 20 | 1073 | R1039 | QIP deviation statement (Rs million) table A | - |
| ANX20_1085 | 20 | 1085 | R1040 | QIP deviation statement (Rs million) table A | - |
| ANX20_1127 | 20 | 1127 | R1041 | QIP deviation statement (Rs million) table A | - |
| ANX21_1158 | 21 | 1158 | R1042 | QIP deviation statement (Rs million) table A/B | - |
| ANX21_1165 | 21 | 1165 | R1043 | QIP deviation statement (Rs million) table A/B | - |
| ANX22_1213 | 22 | 1213 | R1044 | NCD proceeds deviation statement (Rs crore) | - |
| ANX22_1221 | 22 | 1221 | R1045 | NCD proceeds deviation statement (Rs crore) | - |
| ANX23_1252 | 23 | 1252 | R1053 | Reg 32 NCD issue list, ISIN/series/value date/amount | - |
| ANX24_1317 | 24 | 1317 | R1059 | Annexure A: utilisation of issue proceeds (absolute rupees) | - |
| ANX25_1351 | 25 | 1351 | R1062 | Annexure A: utilisation of issue proceeds (absolute rupees) | - |
| ANX29_1537 | 29 | 1537 | R1067 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1577 | 29 | 1577 | R1092 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX30_1765 | 30 | 1765 | R1093 | Annexure II: book value of assets (columns A to O unresolved) | A1:OCR_SUSPECT |
| FN19_1041 | 19 | 1041 | R1183 | Reg 52(4) footnote page | - |
| FN19_1052 | 19 | 1052 | R1184 | Reg 52(4) footnote page | - |
| ANX20_1078 | 20 | 1078 | R1185 | QIP deviation statement (Rs million) table A | - |
| ANX20_1082 | 20 | 1082 | R1186 | QIP deviation statement (Rs million) table A | - |
| ANX21_1148 | 21 | 1148 | R1188 | QIP deviation statement (Rs million) table A/B | - |
| ANX21_1160 | 21 | 1160 | R1189 | QIP deviation statement (Rs million) table A/B | - |
| ANX22_1185 | 22 | 1185 | R1190 | NCD proceeds deviation statement (Rs crore) | - |
| ANX22_1216 | 22 | 1216 | R1191 | NCD proceeds deviation statement (Rs crore) | - |
| ANX29_1533 | 29 | 1533 | R1211 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1584 | 29 | 1584 | R1212 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX30_1587 | 30 | 1587 | R1213 | Annexure II: book value of assets (columns A to O unresolved) | - |
| ANX30_1762 | 30 | 1762 | R1214 | Annexure II: book value of assets (columns A to O unresolved) | - |
| FN19_1038 | 19 | 1038 | R1299 | Reg 52(4) footnote page | - |
| ANX20_1089 | 20 | 1089 | R1300 | QIP deviation statement (Rs million) table A | A1:OCR_SUSPECT |
| ANX20_1103 | 20 | 1103 | R1301 | QIP deviation statement (Rs million) table A | - |
| ANX21_1138 | 21 | 1138 | R1303 | QIP deviation statement (Rs million) table A/B | - |
| ANX22_1176 | 22 | 1176 | R1306 | NCD proceeds deviation statement (Rs crore) | - |
| ANX22_1204 | 22 | 1204 | R1307 | NCD proceeds deviation statement (Rs crore) | - |
| ANX23_1233 | 23 | 1233 | R1308 | Reg 32 NCD issue list, ISIN/series/value date/amount | - |
| ANX24_1264 | 24 | 1264 | R1309 | Annexure A: utilisation of issue proceeds (absolute rupees) | - |
| ANX29_1536 | 29 | 1536 | R1316 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1538 | 29 | 1538 | R1317 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX29_1568 | 29 | 1568 | R1318 | Annexure I: ISIN-wise secured NCDs outstanding | - |
| ANX30_1586 | 30 | 1586 | R1319 | Annexure II: book value of assets (columns A to O unresolved) | - |
| ANX30_1590 | 30 | 1590 | R1320 | Annexure II: book value of assets (columns A to O unresolved) | A1:OCR_QUALITY |
| ANX30_1733 | 30 | 1733 | R1323 | Annexure II: book value of assets (columns A to O unresolved) | - |
| ANX30_1751 | 30 | 1751 | R1324 | Annexure II: book value of assets (columns A to O unresolved) | - |
| ANX30_1752 | 30 | 1752 | R1325 | Annexure II: book value of assets (columns A to O unresolved) | - |
| ANX30_1753 | 30 | 1753 | R1326 | Annexure II: book value of assets (columns A to O unresolved) | - |
| ANX30_1754 | 30 | 1754 | R1327 | Annexure II: book value of assets (columns A to O unresolved) | - |

## T8 MISSING_FROM_STRUCTURED (A1 lacks a row; loop back to A1)
| ID | line | flag | claim text |
|---|---|---|---|
| M001 | 81 | MISSING_FROM_STRUCTURED | Independence confirmation: director meets Companies Act and SEBI LODR independence criteria; not debarred by SEBI or other authority; not related to any director (cover letter p2 lines 80-86) |
| M002 | 159 | MISSING_FROM_STRUCTURED | Annexure A item 4: Ms. Soni is not related inter-se to any Director of the Company (p3) |
| M003 | 168 | MISSING_FROM_STRUCTURED | Annexure A item 5: Ms. Soni is not debarred from holding office of Director by any SEBI order or other authority (p4) |
| M004 | 228 | MISSING_FROM_STRUCTURED | Consolidated LRR para 5 conclusion: nothing has come to attention that the Statement is not in accordance with Ind AS 34 (unmodified conclusion) |
| M005 | 572 | MISSING_FROM_STRUCTURED | Standalone LRR para 4 conclusion: nothing has come to attention (unmodified conclusion) |
| M006 | 1488 | MISSING_FROM_STRUCTURED | Certificate para 10 conclusion: nothing has come to attention that Statement details are not in agreement with unaudited standalone results, books and records (unmodified) |

```yaml
stage: A2-enumerator
company: "POONAWALLA"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/poonawalla-q2fy27/work/ledger_results_poonawalla_q2fy27.md"
counts:
  notes: 27                  # cons 10, stand 13, Annexure II 4
  footnotes_unnumbered: 10
  line_items: 245            # 219 statement lines + 26 Reg 52(4) lines
  zero_standing: 33          # rows, on 17 source lines
  agenda_items: 11
  annexure_a_items: 5
  auditor_paras: 25          # cons LRR 7, stand LRR 6, certificate 12
  entities: 2                # JASPL JV, PFL Employee Welfare Trust
  signature_blocks: 6
  annexure_table_lines: 129
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ZERO_STANDING_CANDIDATE, BLANK_STANDING, AUDITOR_CHANGE, FOOTNOTE_UNRESOLVED, RESTATED, MEETING_DURATION, MISSING_FROM_STRUCTURED, OCR_SUSPECT, COLUMN_UNRESOLVED]
ids_in_structured: 1327
ids_referenced: 1327
orphan_ids: []
missing_from_structured: [M001, M002, M003, M004, M005, M006]
gate_a2: pass
mismatch_note: ""
analyst_note: "M001-M006 are text units A1 did not anchor: director independence and no-debarment confirmations (cover letter, Annexure A items 4 and 5) and the three unmodified conclusions (cons LRR para 5, stand LRR para 4, certificate para 10). A3 should read opinion type from the ledger, not from A1 rows. Zero-standing: 33 A1 rows reconcile to the dash/NIL sweep on the same 17 lines. Five sweep-only dash lines (1111 on p20; 1656, 1662, 1664, 1686 on p30 Annexure II) sit in garbled column areas and are NOT counted; R797 (RPS value, blank beside NIL quantity) is a blank standing item. Notes use N] markers, so the strict N. grep returns 0; two OCR-garbled markers (cons and stand note 10) were found on re-sweep. Both auditors cite Kirtane and Pandit LLP as previous joint auditor; ENTITY_CHANGE cannot be tested, no prior ledger. JASPL sale is held for sale since 2021 and is restated in note 9 and LRR para 4."
```
