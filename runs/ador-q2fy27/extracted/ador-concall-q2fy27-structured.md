=== A1 STRUCTURED EXTRACTION (concall, ASR transcript) ===
company: Ador Welding Limited (ADOR) | quarter: Q2 FY27 | source: Ador_Q2FY27_Concall_Transcript_ASR.txt | fulltext: runs/ador-q2fy27/extracted/ador-concall-q2fy27-fulltext.md
ROW ID RANGE: R001-R293 (293 rows)
row format: R### | page N (= 5-min chunk; 0 = provenance header) | line L (fulltext file line) | TYPE | verbatim/ASR value | context [mm:ss] flags
types: NUMBER, ENTITY, FORWARD, DATE, QUALIFIER (mandatory five) plus CLAIM (management claim, non-numeric) and QUESTION (analyst question). Counts: NUMBER 61, ENTITY 34, FORWARD 35, DATE 13, QUALIFIER 7, CLAIM 96, QUESTION 47
evidence tier: EVERY number is ASR-tier (machine transcript, unverified). ASR_UNCLEAR rows: 66 (definition: data rows whose value or context text carries the ASR_UNCLEAR token). Normalised readings appear only in parentheses and never replace the ASR text.
units: Crores, x1 to Rs Crores. No conversion applied.
coverage: all 635 source lines present in fulltext; 9 of 9 five-minute chunks; timestamp gap [39:57]-[40:30] noted (ASR loss, row TIMESTAMP_GAP).
speaker turns (inferred, every attribution INFERRED): 148 turns total; 61 management (MD) turns; analyst questioners: 10 distinct (Q1-Q10); question rows: 47

--- TURN MAP (source line range | fulltext line range | timestamp | inferred speaker) ---
T | src 9-15 | ft 29-35 | 00:00-00:29 | [INFERRED SPEAKER] MODERATOR
T | src 16-17 | ft 36-37 | 00:36-00:38 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 18-18 | ft 38-38 | 00:41-00:41 | [INFERRED SPEAKER] MODERATOR
T | src 19-47 | ft 39-67 | 00:42-04:11 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 48-54 | ft 68-74 | 04:18-04:50 | [INFERRED SPEAKER] MODERATOR
T | src 55-55 | ft 76-76 | 05:00-05:00 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 56-56 | ft 77-77 | 05:01-05:01 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 57-61 | ft 78-82 | 05:02-05:19 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 62-69 | ft 83-90 | 05:26-06:18 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 70-73 | ft 91-94 | 06:35-06:47 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 74-79 | ft 95-100 | 06:52-07:08 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 80-83 | ft 101-104 | 07:11-07:17 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 84-86 | ft 105-107 | 07:19-07:32 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 87-89 | ft 108-110 | 07:34-07:40 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 90-103 | ft 111-124 | 07:44-08:28 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 104-105 | ft 125-126 | 08:31-08:32 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 106-107 | ft 127-128 | 08:38-08:46 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 108-108 | ft 129-129 | 08:47-08:47 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 109-120 | ft 130-141 | 08:51-09:21 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 121-123 | ft 142-144 | 09:25-09:27 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 124-124 | ft 145-145 | 09:33-09:33 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 125-125 | ft 146-146 | 09:36-09:36 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 126-131 | ft 147-152 | 09:40-09:50 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 132-132 | ft 153-153 | 09:52-09:52 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 133-135 | ft 154-157 | 09:56-10:00 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 136-136 | ft 158-158 | 10:07-10:07 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 137-143 | ft 159-165 | 10:14-10:38 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 144-145 | ft 166-167 | 10:44-10:46 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 146-146 | ft 168-168 | 10:53-10:53 | [INFERRED SPEAKER] MODERATOR
T | src 147-147 | ft 169-169 | 10:57-10:57 | [INFERRED SPEAKER] ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)
T | src 148-148 | ft 170-170 | 11:00-11:00 | [INFERRED SPEAKER] MODERATOR
T | src 149-150 | ft 171-172 | 11:07-11:10 | [INFERRED SPEAKER] ANALYST Q2 Suraj Malu (Katharaman Adventures)
T | src 151-153 | ft 173-175 | 11:15-11:26 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 154-159 | ft 176-181 | 11:28-11:46 | [INFERRED SPEAKER] ANALYST Q2 Suraj Malu (Katharaman Adventures)
T | src 160-167 | ft 182-189 | 11:49-12:16 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 168-169 | ft 190-191 | 12:19-12:24 | [INFERRED SPEAKER] ANALYST Q2 Suraj Malu (Katharaman Adventures)
T | src 170-179 | ft 192-201 | 12:25-12:56 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 180-181 | ft 202-203 | 13:00-13:07 | [INFERRED SPEAKER] ANALYST Q2 Suraj Malu (Katharaman Adventures)
T | src 182-185 | ft 204-207 | 13:09-13:21 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 186-186 | ft 208-208 | 13:24-13:24 | [INFERRED SPEAKER] ANALYST Q2 Suraj Malu (Katharaman Adventures)
T | src 187-188 | ft 209-210 | 13:27-13:31 | [INFERRED SPEAKER] MODERATOR
T | src 189-190 | ft 211-212 | 13:32-13:36 | [INFERRED SPEAKER] MODERATOR
T | src 191-191 | ft 213-213 | 13:39-13:39 | [INFERRED SPEAKER] ANALYST Q3 Harga Gandhi (Bajaj Alternate Investment Management)
T | src 192-192 | ft 214-214 | 13:43-13:43 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 193-196 | ft 215-218 | 13:45-13:58 | [INFERRED SPEAKER] ANALYST Q3 Harga Gandhi (Bajaj Alternate Investment Management)
T | src 197-207 | ft 219-229 | 14:02-14:48 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 208-208 | ft 230-230 | 14:51-14:51 | [INFERRED SPEAKER] ANALYST Q3 Harga Gandhi (Bajaj Alternate Investment Management)
T | src 209-209 | ft 231-231 | 14:54-14:54 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 210-211 | ft 233-234 | 15:00-15:07 | [INFERRED SPEAKER] ANALYST Q3 Harga Gandhi (Bajaj Alternate Investment Management)
T | src 212-217 | ft 235-240 | 15:11-15:30 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 218-222 | ft 241-245 | 15:35-15:46 | [INFERRED SPEAKER] ANALYST Q3 Harga Gandhi (Bajaj Alternate Investment Management)
T | src 223-233 | ft 246-256 | 15:51-16:36 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 234-235 | ft 257-258 | 16:40-16:42 | [INFERRED SPEAKER] ANALYST Q3 Harga Gandhi (Bajaj Alternate Investment Management)
T | src 236-236 | ft 259-259 | 16:46-16:46 | [INFERRED SPEAKER] MODERATOR
T | src 237-238 | ft 260-261 | 16:47-16:51 | [INFERRED SPEAKER] MODERATOR
T | src 239-242 | ft 262-265 | 16:53-17:03 | [INFERRED SPEAKER] ANALYST Q4 Dharmil Vani (Gidwick Capital)
T | src 243-254 | ft 266-277 | 17:05-17:36 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 255-258 | ft 278-281 | 17:41-17:50 | [INFERRED SPEAKER] ANALYST Q4 Dharmil Vani (Gidwick Capital)
T | src 259-269 | ft 282-292 | 17:52-18:19 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 270-271 | ft 293-294 | 18:22-18:23 | [INFERRED SPEAKER] ANALYST Q4 Dharmil Vani (Gidwick Capital)
T | src 272-272 | ft 295-295 | 18:28-18:28 | [INFERRED SPEAKER] MODERATOR
T | src 273-276 | ft 296-299 | 18:29-18:42 | [INFERRED SPEAKER] MODERATOR
T | src 277-278 | ft 300-301 | 18:44-18:45 | [INFERRED SPEAKER] ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]
T | src 279-279 | ft 302-302 | 18:46-18:46 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 280-284 | ft 303-307 | 18:48-19:02 | [INFERRED SPEAKER] ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]
T | src 285-302 | ft 308-326 | 19:06-20:00 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 303-303 | ft 327-327 | 20:04-20:04 | [INFERRED SPEAKER] ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]
T | src 304-305 | ft 328-329 | 20:10-20:15 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 306-308 | ft 330-332 | 20:21-20:32 | [INFERRED SPEAKER] ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]
T | src 309-312 | ft 333-336 | 20:40-20:54 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 313-313 | ft 337-337 | 21:01-21:01 | [INFERRED SPEAKER] ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]
T | src 314-315 | ft 338-339 | 21:06-21:10 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 316-318 | ft 340-342 | 21:17-21:26 | [INFERRED SPEAKER] ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]
T | src 319-325 | ft 343-349 | 21:31-22:10 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 326-332 | ft 350-356 | 22:18-22:54 | [INFERRED SPEAKER] ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]
T | src 333-338 | ft 357-362 | 22:59-23:27 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 339-339 | ft 363-363 | 23:34-23:34 | [INFERRED SPEAKER] ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]
T | src 340-340 | ft 364-364 | 23:40-23:40 | [INFERRED SPEAKER] MODERATOR
T | src 341-342 | ft 365-366 | 23:46-23:54 | [INFERRED SPEAKER] ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]
T | src 343-346 | ft 367-370 | 24:01-24:15 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 347-347 | ft 371-371 | 24:20-24:20 | [INFERRED SPEAKER] ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]
T | src 348-352 | ft 372-376 | 24:26-24:46 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 353-353 | ft 377-377 | 24:50-24:50 | [INFERRED SPEAKER] ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]
T | src 354-359 | ft 378-384 | 24:57-25:08 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 360-363 | ft 385-388 | 25:10-25:19 | [INFERRED SPEAKER] ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]
T | src 364-375 | ft 389-400 | 25:20-25:44 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 376-378 | ft 401-403 | 25:45-25:52 | [INFERRED SPEAKER] ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]
T | src 379-393 | ft 404-418 | 25:56-26:28 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 394-397 | ft 419-422 | 26:33-26:37 | [INFERRED SPEAKER] ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]
T | src 398-401 | ft 423-426 | 26:39-26:44 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 402-403 | ft 427-428 | 26:46-26:47 | [INFERRED SPEAKER] ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]
T | src 404-405 | ft 429-430 | 26:47-26:48 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 406-406 | ft 431-431 | 26:51-26:51 | [INFERRED SPEAKER] MODERATOR
T | src 407-411 | ft 432-436 | 26:52-27:01 | [INFERRED SPEAKER] MODERATOR
T | src 412-412 | ft 437-437 | 27:06-27:06 | [INFERRED SPEAKER] ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)
T | src 413-413 | ft 438-438 | 27:07-27:07 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 414-423 | ft 439-448 | 27:10-27:38 | [INFERRED SPEAKER] ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)
T | src 424-451 | ft 449-476 | 27:42-28:44 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 452-458 | ft 477-483 | 28:46-29:03 | [INFERRED SPEAKER] ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)
T | src 459-461 | ft 484-486 | 29:05-29:10 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 462-462 | ft 487-487 | 29:13-29:13 | [INFERRED SPEAKER] ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)
T | src 463-470 | ft 488-495 | 29:17-29:30 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 471-473 | ft 496-498 | 29:34-29:38 | [INFERRED SPEAKER] ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)
T | src 474-480 | ft 499-505 | 29:42-29:54 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 481-482 | ft 506-507 | 29:56-29:58 | [INFERRED SPEAKER] ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)
T | src 483-484 | ft 509-510 | 30:00-30:05 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 485-485 | ft 511-511 | 30:10-30:10 | [INFERRED SPEAKER] ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)
T | src 486-486 | ft 512-512 | 30:16-30:16 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 487-488 | ft 513-514 | 30:23-30:29 | [INFERRED SPEAKER] ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)
T | src 489-491 | ft 515-517 | 30:33-30:44 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 492-493 | ft 518-519 | 30:49-30:57 | [INFERRED SPEAKER] ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)
T | src 494-500 | ft 520-526 | 31:01-31:34 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 501-502 | ft 527-528 | 31:40-31:45 | [INFERRED SPEAKER] ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)
T | src 503-505 | ft 529-531 | 31:48-31:58 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 506-506 | ft 532-532 | 32:02-32:02 | [INFERRED SPEAKER] ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)
T | src 507-507 | ft 533-533 | 32:07-32:07 | [INFERRED SPEAKER] MODERATOR
T | src 508-512 | ft 534-538 | 32:13-32:37 | [INFERRED SPEAKER] ANALYST Q8 Rohit (I Thought PMS)
T | src 513-528 | ft 539-554 | 32:44-34:07 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 529-530 | ft 555-556 | 34:15-34:20 | [INFERRED SPEAKER] ANALYST Q8 Rohit (I Thought PMS)
T | src 531-531 | ft 557-557 | 34:25-34:25 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 532-532 | ft 558-558 | 34:33-34:33 | [INFERRED SPEAKER] ANALYST Q8 Rohit (I Thought PMS)
T | src 533-542 | ft 559-569 | 34:38-35:14 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 543-547 | ft 570-574 | 35:19-35:37 | [INFERRED SPEAKER] ANALYST Q8 Rohit (I Thought PMS)
T | src 548-557 | ft 575-584 | 35:46-36:35 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 558-560 | ft 585-587 | 36:42-36:57 | [INFERRED SPEAKER] ANALYST Q8 Rohit (I Thought PMS)
T | src 561-568 | ft 588-595 | 36:59-37:36 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 569-569 | ft 596-596 | 37:38-37:38 | [INFERRED SPEAKER] ANALYST Q8 Rohit (I Thought PMS)
T | src 570-571 | ft 597-598 | 37:40-37:43 | [INFERRED SPEAKER] MODERATOR
T | src 572-572 | ft 599-599 | 37:45-37:45 | [INFERRED SPEAKER] MODERATOR
T | src 573-573 | ft 600-600 | 37:50-37:50 | [INFERRED SPEAKER] ANALYST Q9 Yash Patil (Laland Brocha) [firm ASR_UNCLEAR]
T | src 574-574 | ft 601-601 | 37:54-37:54 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 575-578 | ft 602-605 | 37:58-38:11 | [INFERRED SPEAKER] ANALYST Q9 Yash Patil (Laland Brocha) [firm ASR_UNCLEAR]
T | src 579-584 | ft 606-611 | 38:15-38:38 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 585-587 | ft 612-614 | 38:46-38:56 | [INFERRED SPEAKER] ANALYST Q9 Yash Patil (Laland Brocha) [firm ASR_UNCLEAR]
T | src 588-592 | ft 615-619 | 38:59-39:20 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 593-593 | ft 620-620 | 39:25-39:25 | [INFERRED SPEAKER] ANALYST Q9 Yash Patil (Laland Brocha) [firm ASR_UNCLEAR]
T | src 594-597 | ft 621-624 | 39:38-39:57 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 598-599 | ft 626-627 | 40:30-40:34 | [INFERRED SPEAKER] MODERATOR
T | src 600-603 | ft 628-631 | 40:36-41:02 | [INFERRED SPEAKER] ANALYST Q10 Nasser Pirak (Native Invest) [name ASR_UNCLEAR]
T | src 604-611 | ft 632-639 | 41:12-41:33 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 612-612 | ft 640-640 | 41:42-41:42 | [INFERRED SPEAKER] ANALYST Q10 Nasser Pirak (Native Invest) [name ASR_UNCLEAR]
T | src 613-621 | ft 641-649 | 41:53-42:21 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 622-622 | ft 650-650 | 42:26-42:26 | [INFERRED SPEAKER] ANALYST Q10 Nasser Pirak (Native Invest) [name ASR_UNCLEAR]
T | src 623-624 | ft 651-652 | 42:28-42:31 | [INFERRED SPEAKER] MODERATOR
T | src 625-626 | ft 653-654 | 42:32-42:37 | [INFERRED SPEAKER] MODERATOR
T | src 627-632 | ft 655-660 | 42:41-42:54 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 633-633 | ft 661-661 | 42:56-42:56 | [INFERRED SPEAKER] MD (Aditya Malukani)
T | src 634-635 | ft 662-663 | 42:57-43:01 | [INFERRED SPEAKER] MODERATOR
(source lines 1-8 = provenance header; the MD line 16 'Thank you very much sir', and mixed analyst/MD single lines at [20:10], [24:50], [34:25], [35:46], [43:01] boundaries are attribution-ambiguous.)

--- ROWS ---
R001 | page 0 | line 20 | QUALIFIER | MACHINE-TRANSCRIBED (ASR). NOT A COMPANY-FILED TRANSCRIPT. | provenance qualifier [hdr] 
R002 | page 0 | line 21 | ENTITY | Ador Welding Limited (BSE 517041, NSE ADOR) | company identity [hdr] 
R003 | page 0 | line 21 | NUMBER | 517041 | BSE scrip code [hdr] 
R004 | page 0 | line 22 | DATE | Q2 FY27 Analysts / Institutional Investors Meet | event name [hdr] 
R005 | page 0 | line 22 | DATE | 23-Oct-2026 | event date [hdr] 
R006 | page 0 | line 23 | ENTITY | adorwelding.com .../Ador-Welding-Limited-Q2-FY27-Audio-File.mp3 | source audio file [hdr] 
R007 | page 0 | line 23 | NUMBER | 5,169,312 bytes | audio file size [hdr] 
R008 | page 0 | line 23 | NUMBER | 43:04 | audio duration [hdr] 
R009 | page 0 | line 23 | ENTITY | BSE filing AWL/SEC/SE/2026-27/52 | filing reference [hdr] 
R010 | page 0 | line 23 | DATE | 23-Oct-2026 | BSE filing date [hdr] 
R011 | page 0 | line 24 | QUALIFIER | faster-whisper 'small', compute_type int8, CPU, language en, beam 1, no VAD; 5-minute chunks | ASR method [hdr] 
R012 | page 0 | line 25 | QUALIFIER | no speaker labels; names and numbers may be misheard; treat every number as ASR-tier evidence | ASR caveat [hdr] 
R013 | page 0 | line 26 | QUALIFIER | No transcript was filed on BSE or the company site as of 23-Oct-2026 16:45 IST | filing status [hdr] 
R014 | page 0 | line 26 | DATE | 23-Oct-2026 16:45 IST | filing status check time [hdr] 
R015 | page 1 | line 29 | CLAIM | 'Adore Welding Limited due to FF27 earnings conference call' ASR_UNCLEAR; reading: Ador, Q2 FY27 | call identification [00:00] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MODERATOR]
R016 | page 1 | line 29 | DATE | FF27 (ASR_UNCLEAR; normalised Q2 FY27) | call period [00:00] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MODERATOR]
R017 | page 1 | line 30 | QUALIFIER | all participant lines in listen only mode | call format [00:06] [INFERRED SPEAKER: MODERATOR]
R018 | page 1 | line 34 | QUALIFIER | conference is being recorded | call format [00:26] [INFERRED SPEAKER: MODERATOR]
R019 | page 1 | line 35 | ENTITY | Mr. Aditya Malukani, managing director and CEO | speaker [00:29] [INFERRED SPEAKER: MODERATOR]
R020 | page 1 | line 39 | CLAIM | slight delay, technical issue on company side | call start [00:42] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R021 | page 1 | line 41 | ENTITY | Mr. Sudha Narayanasi, F.O. and head of strategy (ASR; F.O. likely CFO) | management attendee ASR_UNCLEAR [00:52] ASR_UNCLEAR [INFERRED SPEAKER: MD (Aditya Malukani)]
R022 | page 1 | line 41 | ENTITY | Mr. Bide, company secretary and chief compliance officer | management attendee [00:52] [INFERRED SPEAKER: MD (Aditya Malukani)]
R023 | page 1 | line 41 | ENTITY | SGA, investor relations advisors | IR advisor [00:52] [INFERRED SPEAKER: MD (Aditya Malukani)]
R024 | page 1 | line 42 | CLAIM | investor deck referenced | presentation reference [01:03] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R025 | page 1 | line 43 | NUMBER | 75 years | company age, completed 'yesterday' [01:06] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R026 | page 1 | line 43 | DATE | yesterday (22-Oct-2026 by call date) completed 75 years | anniversary [01:06] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R027 | page 1 | line 44 | DATE | 1951 | first India's first welding manufacturer [01:12] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R028 | page 1 | line 44 | CLAIM | first India's first welding manufacturer | company claim [01:12] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R029 | page 1 | line 44 | NUMBER | five manufacturing units | manufacturing units [01:12] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R030 | page 1 | line 45 | NUMBER | more than 850 people | headcount [01:19] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R031 | page 1 | line 45 | NUMBER | over 1500 companies (ASR; presence in) | customer presence ASR_UNCLEAR [01:19] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R032 | page 1 | line 45 | NUMBER | 15 countries | international presence [01:19] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R033 | page 1 | line 45 | ENTITY | government recognize R&D center | R&D centre [01:19] [INFERRED SPEAKER: MD (Aditya Malukani)]
R034 | page 1 | line 46 | NUMBER | Rs.7.5 per equity share | interim dividend declared [01:28] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R035 | page 1 | line 46 | CLAIM | board declared interim dividend | dividend [01:28] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R036 | page 1 | line 47 | NUMBER | about 23% year on year | Q2 FY27 revenue growth YoY [01:35] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R037 | page 1 | line 47 | NUMBER | Rs.345 crores | Q2 FY27 revenue [01:35] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R038 | page 1 | line 47 | NUMBER | 8-1 revenue also up 23% (ASR_UNCLEAR; likely H1) | H1 FY27 revenue growth YoY [01:35] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R039 | page 1 | line 47 | NUMBER | 654 crores | H1 FY27 revenue (ASR 8-1) [01:35] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R040 | page 1 | line 47 | CLAIM | revenue up 23% YoY in quarter and half | headline [01:35] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R041 | page 1 | line 48 | CLAIM | healthy demand across infrastructure, power, oil and gas, railways, shipbuilding, defence, heavy fabrication | demand drivers [01:46] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R042 | page 1 | line 49 | CLAIM | strong capital goods activity in India favourable operating environment | demand [01:55] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R043 | page 1 | line 50 | NUMBER | 34.2% (ASR 'Growth margins'; reading gross margin) | Q2 FY27 gross margin ASR_UNCLEAR [02:00] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R044 | page 1 | line 50 | CLAIM | input cost inflation particularly higher | margin pressure [02:00] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R045 | page 1 | line 51 | CLAIM | 'Steve' (ASR; likely steel) and other raw material prices a key pressure | cost pressure ASR_UNCLEAR [02:10] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R046 | page 1 | line 51 | CLAIM | calibrated price increases taken | pricing action [02:10] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R047 | page 1 | line 51 | FORWARD | will continue price increases in a measured manner | pricing [02:10] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R048 | page 1 | line 52 | NUMBER | EBITDA grew 9% in the quarter | Q2 FY27 EBITDA growth [02:18] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R049 | page 1 | line 52 | NUMBER | each one EBITTA margin was 11.2% (ASR_UNCLEAR; likely H1 EBITDA margin) | H1 EBITDA margin ASR_UNCLEAR [02:18] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R050 | page 1 | line 52 | CLAIM | margin slightly higher than last year | EBITDA margin vs prior year [02:18] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R051 | page 1 | line 53 | FORWARD | objective of steadily improving EBITDA margins unchanged | margin objective [02:26] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R052 | page 1 | line 53 | CLAIM | input cost cycles may affect pace in individual quarters | caveat [02:26] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R053 | page 1 | line 54 | CLAIM | three drivers: international reach, product mix, customer engagement | growth drivers [02:36] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R054 | page 1 | line 55 | CLAIM | Middle East principal international market via Dubai hub | exports [02:44] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R055 | page 1 | line 55 | ENTITY | Middle East; Dubai hub | export geography [02:44] [INFERRED SPEAKER: MD (Aditya Malukani)]
R056 | page 1 | line 56 | FORWARD | expanding network and evaluating opportunities in Europe | exports [02:51] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R057 | page 1 | line 56 | ENTITY | Europe | export geography [02:51] [INFERRED SPEAKER: MD (Aditya Malukani)]
R058 | page 1 | line 57 | CLAIM | partnerships offer higher end welding power solutions | product mix [02:59] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R059 | page 1 | line 58 | ENTITY | HyperThemes (ASR; likely Hypertherm) Master Distributor in India, plasma cutting | partner ASR_UNCLEAR [03:10] ASR_UNCLEAR [INFERRED SPEAKER: MD (Aditya Malukani)]
R060 | page 1 | line 58 | CLAIM | advanced plasma cutting systems offered | product [03:10] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R061 | page 1 | line 59 | CLAIM | introducing specialised high performance consumables for demanding applications | product mix [03:14] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R062 | page 1 | line 60 | CLAIM | strengthening direct relations with key customers while supporting distribution | customer engagement [03:20] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R063 | page 1 | line 62 | CLAIM | automation strategic priority; rising labour costs and skilled welder shortage | automation [03:35] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R064 | page 1 | line 63 | ENTITY | Liburi (ASR_UNCLEAR) orbital welding technology partnership; power, nuclear, oil and gas, shipbuilding | partner ASR_UNCLEAR [03:46] ASR_UNCLEAR [INFERRED SPEAKER: MD (Aditya Malukani)]
R065 | page 1 | line 65 | CLAIM | investing in new consumables line per CAPEX plan shared earlier | capex [03:59] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R066 | page 1 | line 65 | FORWARD | investments to modernise base, support future demand, scale efficiently | capex purpose [03:59] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R067 | page 1 | line 67 | CLAIM | opening remarks end, Q&A opened | structure [04:11] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R068 | page 1 | line 69 | QUALIFIER | Q&A queue via star and one | call format [04:23] [INFERRED SPEAKER: MODERATOR]
R069 | page 1 | line 74 | ENTITY | Radraksh Vahegya (ASR) from I Thought Financial Consulting | analyst Q1 [04:50] [INFERRED SPEAKER: MODERATOR]
R070 | page 2 | line 78 | QUESTION | Q1a: clarity on gross margin; price hike taken; expect more recovery in second half? | analyst Q1 [05:02] ASR-tier [INFERRED SPEAKER: ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)]
R071 | page 2 | line 83 | NUMBER | approximately 80% of gross margin dip from severe cost inflation | Q2 gross margin dip attribution [05:26] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R072 | page 2 | line 83 | CLAIM | severe inflation in costs across the board | margin [05:26] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R073 | page 2 | line 85 | NUMBER | about 15-20% of dip from aggressive growth strategy | Q2 gross margin dip attribution [05:50] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R074 | page 2 | line 86 | CLAIM | growth plan does not impact margins very heavily | margin [05:58] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R075 | page 2 | line 87 | FORWARD | going forward definitely see margin recovery | gross margin recovery [06:01] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R076 | page 2 | line 88 | FORWARD | fairly confident on long term goal for next three four years | long-term plan [06:06] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R077 | page 2 | line 88 | NUMBER | next three four years | horizon (ASR three four) [06:06] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R078 | page 2 | line 89 | CLAIM | don't see Q2 as hurting too badly; would have liked better | Q2 margin [06:14] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R079 | page 2 | line 90 | CLAIM | supply chain and inflationary cost pressure severe, now settled down | margin [06:18] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R080 | page 2 | line 90 | FORWARD | quite confident will recover as we go forward | margin recovery [06:18] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R081 | page 2 | line 92 | QUESTION | Q1b: sustainable number to pencil in going forward | analyst Q1 [06:37] ASR-tier [INFERRED SPEAKER: ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)]
R082 | page 2 | line 95 | NUMBER | between the 13 level (ASR_UNCLEAR; follows as 12-13) | margin level [06:52] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R083 | page 2 | line 97 | NUMBER | 12-13 level | margin target range (EBITDA per [07:15]) [06:54] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R084 | page 2 | line 97 | FORWARD | has to be between 12-13 level, then push upwards | EBITDA margin target [06:54] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R085 | page 2 | line 99 | CLAIM | be patient through quarterly global issues | margin [07:02] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R086 | page 2 | line 103 | QUESTION | Q1c: 12-13 would be EBITDA level? (confirming) | analyst Q1 [07:15] ASR-tier [INFERRED SPEAKER: ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)]
R087 | page 2 | line 105 | NUMBER | gross margin at least 36 to 37-38 | gross margin ideal range [07:19] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R088 | page 2 | line 105 | FORWARD | gross margin recovery to 36 to 37-38 ideally; shouldn't be a problem | gross margin recovery [07:19] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R089 | page 2 | line 109 | QUESTION | Q1d: visibility on 20% plus growth going forward? | analyst Q1 [07:36] ASR-tier [INFERRED SPEAKER: ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)]
R090 | page 2 | line 109 | NUMBER | 20% plus growth | growth rate referenced by analyst [07:36] ASR-tier [INFERRED SPEAKER: ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)]
R091 | page 2 | line 113 | CLAIM | part of growth inflationary | growth composition [07:48] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R092 | page 2 | line 114 | NUMBER | plus 10% double digit region growth | growth ex-inflation [07:50] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R093 | page 2 | line 114 | FORWARD | seeing growth in plus 10% double digit region | growth outlook [07:50] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R094 | page 2 | line 115 | CLAIM | seeing volumes growth as well | volume [07:57] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R095 | page 2 | line 117 | CLAIM | international market providing even more opportunity | exports [08:02] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R096 | page 2 | line 119 | FORWARD | growth sustainable | growth outlook [08:10] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R097 | page 2 | line 122 | CLAIM | demand a little better than expected | demand [08:20] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R098 | page 2 | line 126 | QUESTION | Q1e: export share in H1 FY27 and visibility? | analyst Q1 [08:32] ASR-tier [INFERRED SPEAKER: ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)]
R099 | page 2 | line 127 | NUMBER | 15 to 20% export share, H1 slightly higher part | H1 FY27 export share [08:38] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R100 | page 2 | line 129 | QUESTION | Q1f: major delta in exports going forward? | analyst Q1 [08:47] ASR-tier [INFERRED SPEAKER: ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)]
R101 | page 2 | line 130 | FORWARD | exports very important part of long-term strategy; continue aggressive | exports [08:51] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R102 | page 2 | line 134 | CLAIM | export mix at times different to ideal margin mix | export mix [09:03] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R103 | page 2 | line 139 | CLAIM | exports still margin accretive (ASR 'margin-accurative') | export margin ASR_UNCLEAR [09:15] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R104 | page 2 | line 141 | FORWARD | intend to grow exports | exports [09:21] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R105 | page 2 | line 144 | QUESTION | Q1g: any EBITDA losses on the flare (ASR; unclear) segment in H1? | analyst Q1 ASR_UNCLEAR [09:27] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)]
R106 | page 2 | line 148 | CLAIM | flare segment pretty much done; no losses | segment ASR_UNCLEAR [09:41] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R107 | page 2 | line 148 | ENTITY | flare segment (ASR_UNCLEAR) | segment [09:41] ASR_UNCLEAR [INFERRED SPEAKER: MD (Aditya Malukani)]
R108 | page 2 | line 151 | NUMBER | no losses (nil) in flare segment ZERO_STANDING | flare segment EBITDA H1 [09:48] ZERO_STANDING ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R109 | page 2 | line 153 | QUESTION | Q1h: revenue contribution of that segment in H1? | analyst Q1 [09:52] ASR-tier [INFERRED SPEAKER: ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)]
R110 | page 2 | line 154 | CLAIM | segment revenue insignificant, no bearing on anything | segment [09:56] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R111 | page 3 | line 158 | QUESTION | Q1i: any other one-offs in H1 numbers? | analyst Q1 [10:07] ASR-tier [INFERRED SPEAKER: ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)]
R112 | page 3 | line 160 | CLAIM | inflationary incoming logistics cost; product mix heavier in Q2 than thought | one-offs [10:19] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R113 | page 3 | line 167 | QUESTION | Q1j: (cut off) last calls mentioned we are still hoping... | analyst Q1 truncated [10:46] ASR-tier [INFERRED SPEAKER: ANALYST Q1 Radraksh Vahegya (I Thought Financial Consulting)]
R114 | page 3 | line 168 | CLAIM | moderator asks analyst to rejoin queue | structure [10:53] ASR-tier [INFERRED SPEAKER: MODERATOR]
R115 | page 3 | line 170 | ENTITY | Suraj Malu (ASR) from Katharaman Adventures | analyst Q2 ASR_UNCLEAR [11:00] ASR_UNCLEAR [INFERRED SPEAKER: MODERATOR]
R116 | page 3 | line 172 | QUESTION | Q2a: volume growth in this quarter? | analyst Q2 [11:10] ASR-tier [INFERRED SPEAKER: ANALYST Q2 Suraj Malu (Katharaman Adventures)]
R117 | page 3 | line 173 | NUMBER | volume growth 'approximate high ... team level' ASR_UNCLEAR | Q2 volume growth ASR_UNCLEAR [11:15] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R118 | page 3 | line 178 | QUESTION | Q2b: raw material breakup; 50-60% mild steel? which components rose? | analyst Q2 [11:34] ASR-tier [INFERRED SPEAKER: ANALYST Q2 Suraj Malu (Katharaman Adventures)]
R119 | page 3 | line 179 | NUMBER | 50-60 percent (analyst: mild steel share of raw material) | analyst assumption [11:38] ASR-tier [INFERRED SPEAKER: ANALYST Q2 Suraj Malu (Katharaman Adventures)]
R120 | page 3 | line 183 | CLAIM | steel very large segment of raw material; chemicals; electronics and PCBs on equipment | raw material mix [11:54] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R121 | page 3 | line 183 | ENTITY | steel; chemicals; electronics; PCBs; copper | raw materials [11:54] [INFERRED SPEAKER: MD (Aditya Malukani)]
R122 | page 3 | line 189 | CLAIM | 'Go metals' ASR_UNCLEAR | ASR_UNCLEAR [12:16] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R123 | page 3 | line 194 | CLAIM | copper fluctuating quite a bit; everything across the board going up | raw material [12:33] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R124 | page 3 | line 198 | DATE | July (rapid cost rise) | cost shock timing [12:46] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R125 | page 3 | line 201 | CLAIM | market readjusted already; not stressed | pricing [12:56] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R126 | page 3 | line 202 | QUESTION | Q2c: will volume growth continue going forward? | analyst Q2 [13:00] ASR-tier [INFERRED SPEAKER: ANALYST Q2 Suraj Malu (Katharaman Adventures)]
R127 | page 3 | line 204 | FORWARD | volume growth fairly decent going forward | volume outlook [13:09] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R128 | page 3 | line 206 | FORWARD | remain aggressive on targets into H2 (HY2) | H2 FY27 outlook [13:17] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R129 | page 3 | line 211 | ENTITY | Harga Gandhi (ASR) from Bajaj Alternate Investment Management Limited | analyst Q3 ASR_UNCLEAR [13:32] ASR_UNCLEAR [INFERRED SPEAKER: MODERATOR]
R130 | page 3 | line 215 | QUESTION | Q3a: Ador Weldors (ASR 'Eddor Weldors') digital welding management; vision; acquisition? | analyst Q3 [13:45] ASR-tier [INFERRED SPEAKER: ANALYST Q3 Harga Gandhi (Bajaj Alternate Investment Management)]
R131 | page 3 | line 219 | ENTITY | Weldors (Ador Weldors) digital welder data product | product [14:02] [INFERRED SPEAKER: MD (Aditya Malukani)]
R132 | page 3 | line 219 | CLAIM | gives welder data to customer to see welding efficiency; step by step accepted in field | product [14:02] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R133 | page 3 | line 221 | CLAIM | Weldors not going to be a game changer; technology upgrade and more data | product [14:19] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R134 | page 3 | line 226 | CLAIM | looking at more high-end machines (ASR 'synthetic') that give more information; tie-ups | automation ASR_UNCLEAR [14:38] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R135 | page 3 | line 231 | CLAIM | impact takes longer; part of moving up value chain | automation [14:54] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R136 | page 4 | line 233 | QUESTION | Q3b: acquisition on robotics side? | analyst Q3 [15:00] ASR-tier [INFERRED SPEAKER: ANALYST Q3 Harga Gandhi (Bajaj Alternate Investment Management)]
R137 | page 4 | line 235 | CLAIM | very early, nothing going to happen; tiny ecosystem; exploring options | M&A [15:11] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R138 | page 4 | line 235 | FORWARD | exploring options for automation value-add; no commitment | M&A [15:11] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R139 | page 4 | line 244 | QUESTION | Q3c: segment margin ranking (industrial MNR, welding automation, equipment, consumables) | analyst Q3 [15:41] ASR-tier [INFERRED SPEAKER: ANALYST Q3 Harga Gandhi (Bajaj Alternate Investment Management)]
R140 | page 4 | line 249 | CLAIM | MNR smaller in size, higher margins | segment margin [16:06] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R141 | page 4 | line 250 | CLAIM | consumables greater turns, depends on product mix | segment margin [16:12] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R142 | page 4 | line 253 | CLAIM | equipment margin slightly heavier cost due to India heavy manufacturing vs sourcing | segment margin [16:25] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R143 | page 4 | line 255 | FORWARD | automation will take time to reach equipment and consumables level | segment [16:33] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R144 | page 4 | line 260 | ENTITY | Dharmil Vani (ASR) from Gidwick Capital | analyst Q4 ASR_UNCLEAR [16:47] ASR_UNCLEAR [INFERRED SPEAKER: MODERATOR]
R145 | page 4 | line 264 | QUESTION | Q4a: inventory: any one-off or build-up on a backup (ASR) | analyst Q4 ASR_UNCLEAR [16:58] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: ANALYST Q4 Dharmil Vani (Gidwick Capital)]
R146 | page 4 | line 266 | CLAIM | inventory not one-off; higher inventory, payables down | inventory [17:05] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R147 | page 4 | line 271 | NUMBER | order backlog (ASR 'order back') ~75, 80% of reason for inventory | inventory driver ASR_UNCLEAR [17:19] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R148 | page 4 | line 273 | NUMBER | 15, 20% of reason: availability of steel in market | inventory driver [17:25] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R149 | page 4 | line 276 | DATE | 30th September (balance sheet date) | balance sheet date [17:33] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R150 | page 4 | line 277 | FORWARD | inventory level will even out (ASR 'through video') | inventory [17:36] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R151 | page 4 | line 279 | QUESTION | Q4b: payables drop due to macro instability or paying quickly for discounts? | analyst Q4 [17:42] ASR-tier [INFERRED SPEAKER: ANALYST Q4 Dharmil Vani (Gidwick Capital)]
R152 | page 4 | line 282 | CLAIM | payables a mix of availability, conditions, growth, product mix; stabilised | payables [17:52] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R153 | page 4 | line 292 | CLAIM | not a trend; not stressed over coming months | payables [18:19] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R154 | page 4 | line 298 | ENTITY | 'the same Paul from Paula' (ASR_UNCLEAR) | analyst Q5 ASR_UNCLEAR [18:37] ASR_UNCLEAR [INFERRED SPEAKER: MODERATOR]
R155 | page 4 | line 305 | QUESTION | Q5a: last year aspiration of 2000 crore revenue by FY29(?) ASR '529'; on track? existing capacity? | analyst Q5 [18:55] ASR-tier [INFERRED SPEAKER: ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]]
R156 | page 4 | line 305 | NUMBER | 2000 crore revenue aspiration | aspiration (analyst) [18:55] ASR-tier [INFERRED SPEAKER: ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]]
R157 | page 4 | line 305 | DATE | 'a 529' ASR_UNCLEAR (likely FY29) | aspiration target year [18:55] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]]
R158 | page 4 | line 308 | CLAIM | 'very far off track' then 'fairly on track' ASR_UNCLEAR | on-track statement [19:06] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R159 | page 4 | line 309 | CLAIM | fairly on track; last six, eight, nine months show opportunities | on-track [19:11] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R160 | page 4 | line 309 | NUMBER | last six, eight, nine months | period [19:11] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R161 | page 4 | line 316 | FORWARD | on a certain path to 2000 crore, encouraging | aspiration [19:32] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R162 | page 4 | line 318 | FORWARD | certain amount of CAPEX in next two, three years; not extraordinary | capex [19:39] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R163 | page 4 | line 321 | NUMBER | 35 to 40 crores a year normal average capex | capex run-rate [19:49] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R164 | page 4 | line 324 | NUMBER | 60, 70 crores (ASR 'times') for one to two years | capex peak [19:56] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R165 | page 4 | line 324 | FORWARD | capex up to 60-70 crores for one to two years; beyond nothing very significant | capex [19:56] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R166 | page 5 | line 327 | QUESTION | Q5b: major debt requirement or equity dilution for capex? | analyst Q5 [20:04] ASR-tier [INFERRED SPEAKER: ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]]
R167 | page 5 | line 328 | CLAIM | no debt/dilution expected; not part of plan at moment | funding [20:10] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R168 | page 5 | line 328 | FORWARD | no equity dilution or major debt planned for capex | funding [20:10] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R169 | page 5 | line 330 | QUESTION | Q5c: Q2 gross margin lowest or pain continues in Q3, Q4? | analyst Q5 [20:21] ASR-tier [INFERRED SPEAKER: ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]]
R170 | page 5 | line 333 | CLAIM | Q2 dip bigger than okay; will push back; not the norm | margin [20:40] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R171 | page 5 | line 333 | FORWARD | will recover from Q2 dip; will not be the norm | margin recovery [20:40] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R172 | page 5 | line 337 | QUESTION | Q5d: expect Q3 onwards gross margin recovered? | analyst Q5 [21:01] ASR-tier [INFERRED SPEAKER: ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]]
R173 | page 5 | line 338 | FORWARD | working hard to recover; only days in Q3 now | Q3 FY27 recovery [21:06] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R174 | page 5 | line 338 | DATE | Q3 (only days in) | timing [21:06] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R175 | page 5 | line 341 | QUESTION | Q5e: for 2000 crore, split of growth between volume, product mix, realisation? | analyst Q5 [21:23] ASR-tier [INFERRED SPEAKER: ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]]
R176 | page 5 | line 343 | NUMBER | 60 70 percent of growth from product mix | growth composition [21:31] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R177 | page 5 | line 343 | FORWARD | 60-70% of growth to come from product mix | growth composition [21:31] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R178 | page 5 | line 347 | CLAIM | 'a third of it' for innovations vs 20 25 percent stated (ASR inconsistency) | ASR_UNCLEAR [21:57] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R179 | page 5 | line 349 | NUMBER | 20 25 percent from innovations, equipment, partnerships, automation | growth composition [22:10] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R180 | page 5 | line 350 | ENTITY | diffusion engineer (ASR; peer, likely Diffusion Engineers) | peer ASR_UNCLEAR [22:18] ASR_UNCLEAR [INFERRED SPEAKER: ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]]
R181 | page 5 | line 350 | QUESTION | Q5f: peers moving to engineering services; is welding consumables market growing enough for 2000 crore? domestic or international? | analyst Q5 [22:18] ASR-tier [INFERRED SPEAKER: ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]]
R182 | page 5 | line 352 | CLAIM | analyst says Ador exited the same (engineering services) division | analyst claim [22:29] ASR-tier [INFERRED SPEAKER: ANALYST Q5 Paul (Paula) [name ASR_UNCLEAR]]
R183 | page 5 | line 357 | CLAIM | welding consumable market provides adequate growth; linked to steel consumption | industry [22:59] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R184 | page 5 | line 364 | ENTITY | Thurman the grower (ASR) from Heloise Capital | analyst Q6 ASR_UNCLEAR [23:40] ASR_UNCLEAR [INFERRED SPEAKER: MODERATOR]
R185 | page 5 | line 366 | QUESTION | Q6a: raw material price rise from freight or other reasons? | analyst Q6 [23:54] ASR-tier [INFERRED SPEAKER: ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]]
R186 | page 5 | line 369 | CLAIM | freight relevant, especially imports; steel tremendous increases largest part | raw material [24:10] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R187 | page 5 | line 371 | QUESTION | Q6b: temporary and will settle down? | analyst Q6 [24:20] ASR-tier [INFERRED SPEAKER: ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]]
R188 | page 5 | line 374 | CLAIM | steel not softening soon; not as rapid increase either | steel outlook [24:36] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R189 | page 5 | line 375 | CLAIM | company not big enough to influence steel prices | steel [24:41] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R190 | page 5 | line 377 | QUESTION | Q6c: purchases primarily on spot basis? | analyst Q6 [24:50] ASR-tier [INFERRED SPEAKER: ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]]
R191 | page 5 | line 378 | CLAIM | a little strategic buying (seen in 30-Sep balance); can't do excessive | procurement [24:57] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R192 | page 6 | line 380 | DATE | 30th September (strategic stock in balance sheet) | date [25:00] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R193 | page 6 | line 387 | QUESTION | Q6d: how much passed through on finished product? | analyst Q6 [25:14] ASR-tier [INFERRED SPEAKER: ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]]
R194 | page 6 | line 389 | CLAIM | all passed through, later than liked in Q2 | pass-through [25:20] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R195 | page 6 | line 395 | CLAIM | most passed through very quickly; Q2 slow on a few things; temporary | pass-through [25:35] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R196 | page 6 | line 416 | CLAIM | last three months unprecedentedly sporadic rise (ASR) | cost shock ASR_UNCLEAR [26:23] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R197 | page 6 | line 416 | NUMBER | last three (months) | period [26:23] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R198 | page 6 | line 420 | QUESTION | Q6e: medium term come back to same margin trail? | analyst Q6 [26:34] ASR-tier [INFERRED SPEAKER: ANALYST Q6 Thurman the grower (Heloise Capital) [name ASR_UNCLEAR]]
R199 | page 6 | line 423 | FORWARD | get to between 12 to 13 level; have to make that happen | EBITDA margin target [26:39] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R200 | page 6 | line 423 | NUMBER | 12 to 13 level | margin target [26:39] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R201 | page 6 | line 434 | ENTITY | Mahesh Attal (ASR) from Dharia Investment Advisers | analyst Q7 ASR_UNCLEAR [26:57] ASR_UNCLEAR [INFERRED SPEAKER: MODERATOR]
R202 | page 6 | line 439 | QUESTION | Q7a: electrode demand rising from small manufacturing; unorganised players taking share; how catered? | analyst Q7 [27:10] ASR-tier [INFERRED SPEAKER: ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)]
R203 | page 6 | line 449 | CLAIM | welding consumable is engineering product with approval structures | competition [27:42] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R204 | page 6 | line 455 | NUMBER | couple of thousand SKUs in consumables | SKU count [27:56] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R205 | page 6 | line 457 | CLAIM | tier one/two/three companies and customer approvals | competition [28:01] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R206 | page 6 | line 462 | CLAIM | unorganised product customer not Ador customer | unorganised [28:14] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R207 | page 6 | line 466 | ENTITY | oil and gas; ship building (specialised sectors) | end markets [28:22] [INFERRED SPEAKER: MD (Aditya Malukani)]
R208 | page 6 | line 471 | CLAIM | not stressed about unorganised sector; cares about organised market share | competition [28:35] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R209 | page 6 | line 478 | QUESTION | Q7b: gross margins down due to steel prices rising above anticipation; when tapering off? | analyst Q7 [28:48] ASR-tier [INFERRED SPEAKER: ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)]
R210 | page 6 | line 490 | CLAIM | steel prices do not seem to be softening (repeated) | steel [29:20] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R211 | page 6 | line 494 | CLAIM | pass-through happening better now | pass-through [29:27] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R212 | page 6 | line 497 | QUESTION | Q7c: price increase vs steel price increase? | analyst Q7 [29:35] ASR-tier [INFERRED SPEAKER: ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)]
R213 | page 6 | line 499 | CLAIM | price increase in line with steel; lag or contracts differ | pricing [29:42] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R214 | page 6 | line 507 | QUESTION | Q7d: will pass-through in next quarter suffice? | analyst Q7 [29:58] ASR-tier [INFERRED SPEAKER: ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)]
R215 | page 7 | line 510 | FORWARD | get back to target margin level; only way | margin [30:05] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R216 | page 7 | line 511 | QUESTION | Q7e: steel percentage increase QoQ? | analyst Q7 [30:10] ASR-tier [INFERRED SPEAKER: ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)]
R217 | page 7 | line 512 | NUMBER | 7-8% steel price increase Q2 vs Q1 | QoQ steel increase [30:16] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R218 | page 7 | line 513 | QUESTION | Q7f: steel share of raw material? | analyst Q7 [30:23] ASR-tier [INFERRED SPEAKER: ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)]
R219 | page 7 | line 515 | CLAIM | declined to give steel share of raw material (competitor profile) | NOT DISCLOSED [30:33] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R220 | page 7 | line 518 | QUESTION | Q7g: which high value segments? | analyst Q7 [30:49] ASR-tier [INFERRED SPEAKER: ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)]
R221 | page 7 | line 520 | CLAIM | high value: specialised steels consumables; stronger approvals; better equipment technology; automation | product mix [31:01] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R222 | page 7 | line 522 | ENTITY | shipbuilding sector; oil and gas sector approvals | approvals [31:11] [INFERRED SPEAKER: MD (Aditya Malukani)]
R223 | page 7 | line 527 | QUESTION | Q7h: inorganic growth, anything in pipeline? | analyst Q7 [31:40] ASR-tier [INFERRED SPEAKER: ANALYST Q7 Mahesh Attal (Dharia Investment Advisers)]
R224 | page 7 | line 529 | CLAIM | exploring slowly; ecosystem small; no detail until more clarity | M&A [31:48] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R225 | page 7 | line 529 | FORWARD | continue looking at inorganic options | M&A [31:48] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R226 | page 7 | line 533 | ENTITY | Rohit from I thought PMS (ASR) | analyst Q8 [32:07] [INFERRED SPEAKER: MODERATOR]
R227 | page 7 | line 535 | QUESTION | Q8a: talk more on product mix and going deeper with customers | analyst Q8 [32:21] ASR-tier [INFERRED SPEAKER: ANALYST Q8 Rohit (I Thought PMS)]
R228 | page 7 | line 540 | CLAIM | strong distribution network across country | distribution [32:48] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R229 | page 7 | line 541 | CLAIM | not strong enough in front of very large direct customers | customer engagement [32:55] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R230 | page 7 | line 545 | CLAIM | not supplying large enough share of wallet at some large customers | customer engagement [33:19] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R231 | page 7 | line 548 | NUMBER | top 50 top 100 consumers (customers) in country | target customer base [33:34] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R232 | page 7 | line 548 | FORWARD | be more aggressive in front of top 50/100 customers; takes time | customer engagement [33:34] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R233 | page 7 | line 553 | CLAIM | top customers' mix on continuous (wire) products; aggressive entry needed | product mix [34:00] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R234 | page 7 | line 555 | QUESTION | Q8b: recap 60-70% growth from product mix; what does it mean? | analyst Q8 [34:15] ASR-tier [INFERRED SPEAKER: ANALYST Q8 Rohit (I Thought PMS)]
R235 | page 7 | line 555 | NUMBER | 60 70 percent | growth from product mix (analyst recap) [34:15] ASR-tier [INFERRED SPEAKER: ANALYST Q8 Rohit (I Thought PMS)]
R236 | page 7 | line 557 | CLAIM | 60-70% refers to incremental growth | clarification [34:25] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R237 | page 7 | line 559 | CLAIM | gaps are product, sales, customer gaps | product mix [34:38] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R238 | page 7 | line 561 | NUMBER | 'a thousand five thousand sq us' ASR_UNCLEAR (SKUs) | SKU count ASR_UNCLEAR [34:50] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R239 | page 8 | line 564 | CLAIM | closed many product gaps in last three years | product gaps [35:00] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R240 | page 8 | line 564 | NUMBER | last three years | period [35:00] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R241 | page 8 | line 567 | CLAIM | no longer worried about product gap; focus on revenue and margins | product [35:10] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R242 | page 8 | line 568 | NUMBER | two, three years ago | period [35:12] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R243 | page 8 | line 572 | QUESTION | Q8c: after merger (Contact?) around 220-230 crore; trying to grow segment? | analyst Q8 ASR_UNCLEAR [35:21] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: ANALYST Q8 Rohit (I Thought PMS)]
R244 | page 8 | line 572 | NUMBER | 220 230 crores | segment revenue (merged entity ASR 'contact') ASR_UNCLEAR [35:21] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: ANALYST Q8 Rohit (I Thought PMS)]
R245 | page 8 | line 575 | ENTITY | phone tech (ASR_UNCLEAR; merged entity) fabrication industry products | merger ASR_UNCLEAR [35:46] ASR_UNCLEAR [INFERRED SPEAKER: MD (Aditya Malukani)]
R246 | page 8 | line 583 | NUMBER | 8, 10, 12% growth for MNR/contact segment | segment growth [36:28] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R247 | page 8 | line 583 | FORWARD | segment can grow 8-12%, step by step; not 20% | segment outlook [36:28] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R248 | page 8 | line 584 | CLAIM | segment very important part of margins | segment [36:35] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R249 | page 8 | line 586 | QUESTION | Q8d: employee incentivisation, ESOP plan? | analyst Q8 [36:49] ASR-tier [INFERRED SPEAKER: ANALYST Q8 Rohit (I Thought PMS)]
R250 | page 8 | line 588 | NUMBER | approximately 50 people part of ESOP plan | ESOP [36:59] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R251 | page 8 | line 588 | CLAIM | senior management larger chunk | ESOP [36:59] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R252 | page 8 | line 590 | NUMBER | a year and a little bit over a year ago | ESOP intro timing [37:10] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R253 | page 8 | line 592 | CLAIM | incentive plans linked to profitability | incentive [37:18] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R254 | page 8 | line 599 | ENTITY | Yash Patil (ASR) from Laland Brocha (ASR_UNCLEAR) | analyst Q9 ASR_UNCLEAR [37:45] ASR_UNCLEAR [INFERRED SPEAKER: MODERATOR]
R255 | page 8 | line 602 | QUESTION | Q9a: short term bank borrowing from 28 crore to 92.27(?) ASR; for WC? elevated? | analyst Q9 [37:58] ASR-tier [INFERRED SPEAKER: ANALYST Q9 Yash Patil (Laland Brocha) [firm ASR_UNCLEAR]]
R256 | page 8 | line 602 | NUMBER | 28 crores | short-term borrowing prior (ASR) [37:58] ASR-tier [INFERRED SPEAKER: ANALYST Q9 Yash Patil (Laland Brocha) [firm ASR_UNCLEAR]]
R257 | page 8 | line 602 | NUMBER | 90 to 2.27 crores (ASR_UNCLEAR) | short-term borrowing current ASR_UNCLEAR [37:58] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: ANALYST Q9 Yash Patil (Laland Brocha) [firm ASR_UNCLEAR]]
R258 | page 8 | line 603 | NUMBER | 20 crores (ASR 'I prefer 20 crores') | ASR_UNCLEAR [38:05] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: ANALYST Q9 Yash Patil (Laland Brocha) [firm ASR_UNCLEAR]]
R259 | page 8 | line 605 | NUMBER | 527 (ASR_UNCLEAR; likely FY27) | period ASR_UNCLEAR [38:11] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: ANALYST Q9 Yash Patil (Laland Brocha) [firm ASR_UNCLEAR]]
R260 | page 8 | line 606 | CLAIM | borrowing mostly LCs and VGs (BGs); working capital controllable | borrowings [38:15] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R261 | page 8 | line 606 | ENTITY | LCs; VGs (ASR; bank guarantees) | instruments [38:15] [INFERRED SPEAKER: MD (Aditya Malukani)]
R262 | page 8 | line 610 | CLAIM | strategic purchases/stock; don't read too much into H1 data | borrowings [38:31] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R263 | page 8 | line 610 | NUMBER | 'as you go to 20%' ASR_UNCLEAR | ASR_UNCLEAR [38:31] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R264 | page 8 | line 613 | QUESTION | Q9b: is 30-35 crore capex sufficient or more needed? | analyst Q9 [38:49] ASR-tier [INFERRED SPEAKER: ANALYST Q9 Yash Patil (Laland Brocha) [firm ASR_UNCLEAR]]
R265 | page 8 | line 615 | NUMBER | 30-35 crores capex this year (FY27) | FY27 capex [38:59] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R266 | page 8 | line 615 | FORWARD | capex this year approx 30-35 crores | FY27 capex [38:59] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R267 | page 8 | line 617 | NUMBER | 60, 65 to 70 (ASR) crore capex for next two financial years | FY27-28 capex ASR_UNCLEAR [39:10] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R268 | page 8 | line 618 | FORWARD | two years FY27, FY28 slight jump in capex then reduce; nothing exceptionally large | capex [39:15] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R269 | page 8 | line 618 | DATE | FY27, FY28 | capex years [39:15] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R270 | page 8 | line 620 | QUESTION | Q9c: shipbuilding opportunity and current order book? | analyst Q9 [39:25] ASR-tier [INFERRED SPEAKER: ANALYST Q9 Yash Patil (Laland Brocha) [firm ASR_UNCLEAR]]
R271 | page 8 | line 621 | CLAIM | declined to disclose order book (confidential) | NOT DISCLOSED [39:38] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R272 | page 8 | line 622 | CLAIM | shipbuilding a lot of opportunity in India; some benefit seen | shipbuilding [39:45] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R273 | page 8 | line 624 | FORWARD | believe shipbuilding can be incremental growth | shipbuilding [39:57] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R274 | page 9 | line 626 | CLAIM | [39:57]->[40:30] 33s gap with no transcribed text (ASR silence/loss) | TIMESTAMP_GAP [40:30] ASR-tier [INFERRED SPEAKER: MODERATOR]
R275 | page 9 | line 626 | ENTITY | Nasser Pirak (ASR) from Native Invest | analyst Q10 ASR_UNCLEAR [40:30] ASR_UNCLEAR [INFERRED SPEAKER: MODERATOR]
R276 | page 9 | line 629 | QUESTION | Q10a: tapping top 40-50 consumers; no visible movement annually; how? | analyst Q10 [40:39] ASR-tier [INFERRED SPEAKER: ANALYST Q10 Nasser Pirak (Native Invest) [name ASR_UNCLEAR]]
R277 | page 9 | line 629 | NUMBER | top 40, 50 consumers | analyst figure [40:39] ASR-tier [INFERRED SPEAKER: ANALYST Q10 Nasser Pirak (Native Invest) [name ASR_UNCLEAR]]
R278 | page 9 | line 633 | NUMBER | 21% growth (ASR 'for each by once' ASR_UNCLEAR period) | growth claim ASR_UNCLEAR [41:15] ASR_UNCLEAR ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R279 | page 9 | line 633 | CLAIM | outperforming industry average growth rate | growth vs industry [41:15] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R280 | page 9 | line 639 | CLAIM | seeing some benefit in last six, eight months | customer strategy [41:33] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R281 | page 9 | line 639 | NUMBER | last six, eight months | period [41:33] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R282 | page 9 | line 640 | QUESTION | Q10b: other export geographies besides Middle East? | analyst Q10 [41:42] ASR-tier [INFERRED SPEAKER: ANALYST Q10 Nasser Pirak (Native Invest) [name ASR_UNCLEAR]]
R283 | page 9 | line 641 | CLAIM | present in US(ASR), parts of Africa, two markets in Europe, entering third | export geography [41:53] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R284 | page 9 | line 641 | ENTITY | US; Africa; Europe | export geography [41:53] [INFERRED SPEAKER: MD (Aditya Malukani)]
R285 | page 9 | line 643 | FORWARD | entering a third European market | exports [42:03] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R286 | page 9 | line 645 | NUMBER | Middle East about 80-85% of exports | export mix [42:06] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R287 | page 9 | line 646 | FORWARD | other markets expected to grow; FTAs coming in; greater pull | exports [42:11] ASR-tier [INFERRED SPEAKER: MD (Aditya Malukani)]
R288 | page 9 | line 646 | ENTITY | FDAs (ASR; likely FTAs) | trade agreements ASR_UNCLEAR [42:11] ASR_UNCLEAR [INFERRED SPEAKER: MD (Aditya Malukani)]
R289 | page 9 | line 653 | CLAIM | moderator: last question | structure [42:32] ASR-tier [INFERRED SPEAKER: MODERATOR]
R290 | page 9 | line 659 | ENTITY | SGA, IR partner (ASR 'IMS Territory Relations partner') | IR partner ASR_UNCLEAR [42:49] ASR_UNCLEAR [INFERRED SPEAKER: MD (Aditya Malukani)]
R291 | page 9 | line 662 | ENTITY | Adore (Ador) Welding Limited | closing [42:57] [INFERRED SPEAKER: MODERATOR]

R292 | page 3 | line 230 | QUESTION | Do you see impact come in a quarter of movies? (ASR_UNCLEAR; likely 'in a quarter or two'; answer R135) | Q3d: Weldors/automation impact timing [14:51] ASR-tier ASR_UNCLEAR [INFERRED SPEAKER: ANALYST Q3 Harga Gandhi (Bajaj Alternate Investment Management)]
R293 | page 8 | line 585 | NUMBER | 12 to 18 months or probably 24 months | analyst: period of senior hiring [36:42] ASR-tier [INFERRED SPEAKER: ANALYST Q8 Rohit (I Thought PMS)]
=== END STRUCTURED ===
