# A2 LEDGER: results | GRWRHITECH | q2fy27
Source: A1 structured extraction R001-R1782 (no source PDF read). Rows reference A1 IDs; values stay in the structured file.

=== A2 COUNT TEST ===
category: notes          grep_count: 7   sweep_count: 7   match: yes   (numbered notes in fulltext: standalone 3 at p8, consolidated 4 at p15; ids R1729-31, R1749-52)
category: footnotes      grep_count: 14   sweep_count: 14   match: yes   (unnumbered asterisk/footnote/definition rows R1766-R1779; fulltext asterisk lines on pp29-42 cluster into these)
category: line_items     grep_count: 205   sweep_count: 205   match: yes   (label regex found in fulltext within +/-2 lines, vs manual list: SA P&L 24, SA BS 30, SA CF 38, CONS P&L 32, CONS BS 31, CONS CF 41, media table 9)
category: zero_standing  grep_count: 11   sweep_count: 11   match: yes   (blank/dash-valued rows; text layer displaced; visual confirm)
category: agenda_items   grep_count: 3   sweep_count: 3   match: yes   (1 numbered item + 2 enclosures; meeting start 11:30 A.M.; end time illegible)
category: auditor_paras  grep_count: 13   sweep_count: 13   match: yes   (standalone 4 + consolidated 7 numbered + 2 unnumbered; plus 2 sign-off blocks)
category: entities       grep_count: 6   sweep_count: 6   match: yes   (3 subsidiaries x 2 locations: LRR para 4 and Note 3; 4 distinct entities incl. parent)
category: forward_stmts  grep_count: 37   sweep_count: 37   match: yes
category: slides         grep_count: 24   sweep_count: 24   match: yes   (pages 20-43; 4 sparse divider pages)
category: slide_numbers  grep_count: 580   sweep_count: 580   match: yes   (NUMBER 385 + DATE 195)
category: turns/questions/mgmt_numbers   not applicable (results filing)
gate_a2: pass
=== END COUNT TEST ===
ids_in_structured: 1782 | ids_referenced_in_ledger: 1782 | orphan_ids: [] | match: yes

## 1. NOTES, FOOTNOTES, DISCLAIMERS
ROW ID | category | A2 flags | cross-ref / materiality
---|---|---|---
R1729 | Note 1 standalone (p8) | - | approval 22 Oct 2026 by Audit Committee and Board
R1730 | Note 2 standalone (p8) | - | one segment, Polyester Films
R1731 | Note 3 standalone (p8) | - | regrouping of prior figures
R1749 | Note 1 consolidated (p15) | - | approval 22 Oct 2026
R1750 | Note 2 consolidated (p15) | - | one segment
R1751 | Note 3 consolidated (p15) | - | consolidation perimeter; see entities R1313-R1318
R1752 | Note 4 consolidated (p15) | - | regrouping of prior figures
R1766 | unnumbered footnote p29 | FOOTNOTE | -
R1767 | unnumbered footnote p29 | FOOTNOTE | -
R1768 | unnumbered footnote p29 | FOOTNOTE | RESTATED: ROCE adjusted for revaluation reserve Rs 764 Cr (p29, p42 R1778)
R1769 | unnumbered footnote p29 | FOOTNOTE | RESTATED: ROCE adjusted for revaluation reserve Rs 764 Cr (p29, p42 R1778)
R1770 | unnumbered footnote p31 | FOOTNOTE | -
R1771 | unnumbered footnote p31 | FOOTNOTE | -
R1772 | unnumbered footnote p32 | FOOTNOTE | -
R1773 | unnumbered footnote p35 | FOOTNOTE | -
R1774 | unnumbered footnote p35 | FOOTNOTE | -
R1775 | unnumbered footnote p35 | FOOTNOTE | -
R1776 | unnumbered footnote p35 | FOOTNOTE | -
R1777 | unnumbered footnote p42 | FOOTNOTE | -
R1778 | unnumbered footnote p42 | FOOTNOTE | RESTATED: ROCE adjusted for revaluation reserve Rs 764 Cr (p29, p42 R1778)
R1779 | unnumbered footnote p42 | FOOTNOTE | -
R1761 | disclaimer p22 | DISCLAIMER | safe harbour / regrouping caveat
R1762 | disclaimer p22 | DISCLAIMER | safe harbour / regrouping caveat
R1763 | disclaimer p22 | DISCLAIMER | safe harbour / regrouping caveat
R1764 | disclaimer p22 | DISCLAIMER | safe harbour / regrouping caveat
R1740 | UDIN lines illegible (p4, p11) | FOOTNOTE_UNRESOLVED | auditor UDINs unreadable in text layer

## 2. LINE ITEMS (financial tables; ZERO_STANDING flagged)
Value columns on pages 5-7 and 12-14 are column-displaced in A1 (see R1726, R1743); the row ID shown is the NUMBER row on or nearest the label line. Line = fulltext line of the label. Downstream reads values at the ID.

### Standalone P&L
ROW ID(s) | item | fulltext line | A2 flags | note
---|---|---|---|---
R062-R064 | Revenue from Operations | 170 | - | 
R069-R071 | Other Income | 171 | - | 
R075-R077 | Total Income | 173 | - | 
R082-R084 | Cost of Materials Consumed | 177 | - | 
R089-R091 | Changes in inventories of FG/WIP/stock-in-trade | 179 | - | 
R094-R096 | Power & Fuel | 181 | - | 
R100-R102 | Employee benefit expenses | 182 | - | 
R106-R108 | Finance Cost | 184 | - | 
R112-R114 | Depreciation and amortisation expense | 185 | - | 
R119-R121 | Other expenses | 190 | - | 
R125-R127 | Total Expenses | 191 | - | 
R131-R133 | Profit before tax | 193 | - | 
R141-R143 | Current Tax | 197 | - | 
R147-R149 | Deferred Tax | 198 | - | 
R153-R155 | Total Tax Expenses | 200 | - | 
R159-R161 | Net Profit after tax | 202 | - | 
R169-R171 | OCI items not reclassified to P&L | 206 | - | 
R175-R177 | OCI income tax on items not reclassified | 207 | - | 
R181-R183 | Total OCI net of tax | 208 | - | 
R184-R186 | Total comprehensive income net of tax | 209 | - | 
R200 | Paid-up Equity Share Capital (FV Rs 10) | 214 | - | 
R202-R203 | Reserves excl Revaluation Reserves | 217 | - | 
- | Basic EPS (Rs) | 223 | NO_NUMBER_ROW | 
- | Diluted EPS (Rs) | 224 | NO_NUMBER_ROW | 

### Standalone BS
ROW ID(s) | item | fulltext line | A2 flags | note
---|---|---|---|---
R218-R219 | PPE | 236 | - | 
R222-R223 | Capital work in progress | 238 | - | 
R226-R227 | Intangible assets | 240 | - | 
R228-R229 | Intangible assets under development | 242 | - | 
R234-R235 | Investments (non-current) | 246 | - | 
R236-R237 | Other financial assets (non-current) | 248 | - | 
R238-R239 | Other non-current assets | 250 | - | 
R243-R244 | Inventories | 253 | - | 
R245-R246 | Investments (current) | 255 | - | 
R247-R248 | Trade receivables | 256 | - | 
R249-R250 | Cash and cash equivalents | 257 | - | 
R251-R252 | Bank balances other than cash | 258 | - | 
R253-R254 | Loans (current) | 259 | - | 
R255-R256 | Other financial assets (current) | 260 | - | 
R255-R256 | Assets Classified as Held for Sale | 261 | ZERO_STANDING | blank or dash in all periods in text layer; template signal; confirm visually
R257-R258 | Other current assets | 262 | - | 
R257-R258 | TOTAL ASSETS | 264 | - | 
R261-R263 | Equity share capital | 268 | - | 
R264-R266 | Other equity | 269 | - | 
R269-R270 | Lease liabilities (non-current) | 273 | - | 
R269-R270 | Deferred tax liabilities (net) | 274 | - | 
R271-R272 | Provisions (non-current) | 275 | - | 
R276-R277 | Lease liabilities (current) | 279 | - | 
R280-R281 | Trade payables Micro and Small Enterprises | 281 | - | 
R280-R281 | Trade payables Other than MSE | 282 | - | 
R282-R283 | Other financial liabilities | 283 | - | 
R284-R285 | Other current liabilities | 284 | - | 
R286-R287 | Current tax liability (net) | 285 | - | 
R286-R287 | Provisions (current) | 286 | - | 
R290-R291 | TOTAL EQUITY AND LIABILITIES | 288 | - | 

### Standalone CF
ROW ID(s) | item | fulltext line | A2 flags | note
---|---|---|---|---
R292-R293 | Profit before tax | 298 | - | 
R296-R297 | Depreciation and amortisation | 302 | - | 
R298-R299 | Finance cost | 303 | - | 
R300-R301 | Interest income | 304 | - | 
R302 | Unrealised exchange (gain)/loss | 305 | - | 
R303 | Profit/loss on sale or write-off of PPE | 306 | - | 
R303 | Dividend income | 307 | - | 
R304-R305 | Sundry balances written back | 308 | - | 
R306 | Net gain on financial assets | 309 | - | 
R309 | Operating profit | 313 | - | 
R316 | Inventories | 319 | - | 
R317-R318 | Trade receivables | 320 | - | 
R319-R320 | Loans | 321 | - | 
R321-R322 | Other financial assets | 322 | - | 
R321-R322 | Other assets | 323 | - | 
R325 | Trade payables | 325 | - | 
R326-R327 | Other financial liabilities | 326 | - | 
R328-R329 | Other liabilities | 327 | - | 
R330-R331 | Provisions | 328 | - | 
R334 | Cash generated from operations | 330 | - | 
R335 | Direct taxes paid | 331 | - | 
R337-R338 | Net cash flow from operating activities (A) | 333 | - | 
R342-R343 | Purchase of PPE and intangibles | 336 | - | 
R342-R343 | Proceeds from sale of PPE | 337 | - | 
R344 | Interest income (investing) | 338 | - | 
R345-R346 | Investment in subsidiary | 339 | - | 
R347 | Dividend income (investing) | 340 | - | 
R348 | Net (investment)/redemption of mutual funds | 341 | - | 
R348 | Net cash used in investing (B) | 342 | - | 
R351-R352 | Finance cost (financing) | 345 | - | 
R353-R354 | Repayment of lease liability | 346 | - | 
R355-R356 | Dividend paid | 347 | - | 
R357-R358 | Movement in margin money deposit | 348 | - | 
R359-R360 | Movement in unclaimed dividend account | 349 | - | 
R363-R364 | Net cash from/(used in) financing (C) | 351 | - | 
R365-R366 | Net increase/(decrease) in cash (A+B+C) | 352 | - | 
R365-R366 | Cash and cash equivalents (opening 1 April) | 354 | - | 
- | Cash and cash equivalents (closing 30 Sept) | 355 | NO_NUMBER_ROW | 

### Consolidated P&L
ROW ID(s) | item | fulltext line | A2 flags | note
---|---|---|---|---
R437-R439 | Revenue from Operations | 509 | - | 
R443-R445 | Other Income | 510 | - | 
R450-R452 | Total Income | 513 | - | 
R457-R459 | Cost of Materials Consumed | 516 | - | 
R463-R465 | Changes in inventories | 518 | - | 
R469-R471 | Power & Fuel | 520 | - | 
R475-R477 | Employee benefit expenses | 521 | - | 
R481-R483 | Finance Cost | 523 | - | 
R487-R489 | Depreciation and amortisation expense | 525 | - | 
R493-R495 | Other expenses | 526 | - | 
R499-R501 | Total Expenses | 530 | - | 
R505-R507 | Profit before tax | 532 | - | 
R515-R517 | Current Tax | 536 | - | 
R521-R523 | Deferred Tax | 537 | - | 
R527-R529 | Total Tax Expenses | 539 | - | 
R533-R535 | Net Profit after tax | 541 | - | 
R542-R544 | OCI items not reclassified to P&L | 545 | - | 
R548-R550 | OCI income tax on items not reclassified | 546 | - | 
R554-R556 | OCI items that will be reclassified to P&L | 549 | ZERO_STANDING | blank or dash in all periods in text layer; template signal; confirm visually
- | OCI income tax on items reclassified | 551 | ZERO_STANDING, NO_NUMBER_ROW | blank or dash in all periods in text layer; template signal; confirm visually
R560-R562 | Total OCI net of tax | 554 | - | 
R566-R568 | Total comprehensive income net of tax | 557 | - | 
R573-R575 | Profit attributable Owners of the parent | 561 | - | 
R580-R582 | Profit attributable Non-controlling interest | 562 | ZERO_STANDING | blank or dash in all periods in text layer; template signal; confirm visually
R587-R589 | OCI attributable Owners of the parent | 566 | - | 
R587-R589 | OCI attributable Non-controlling interest | 567 | ZERO_STANDING | blank or dash in all periods in text layer; template signal; confirm visually
R595 | TCI attributable Owners of the parent | 571 | - | 
R596-R598 | TCI attributable Non-controlling interest | 572 | ZERO_STANDING | blank or dash in all periods in text layer; template signal; confirm visually
R602-R603 | Paid-up Equity Share Capital | 574 | - | 
R615 | Reserves excl Revaluation Reserves | 578 | - | 
- | Basic EPS (Rs) | 584 | NO_NUMBER_ROW | 
- | Diluted EPS (Rs) | 585 | NO_NUMBER_ROW | 

### Consolidated BS
ROW ID(s) | item | fulltext line | A2 flags | note
---|---|---|---|---
R618-R619 | PPE | 597 | - | 
R622-R624 | Capital work in progress | 599 | - | 
R628-R629 | Intangible assets | 601 | - | 
R630-R631 | Intangible assets under development | 603 | - | 
R636-R637 | Investments (non-current) | 607 | - | 
R638-R639 | Other financial assets (non-current) | 609 | - | 
R640 | Deferred tax assets (net) | 611 | - | 
R643-R644 | Other non-current assets | 613 | - | 
R649-R650 | Inventories | 616 | - | 
R653-R654 | Investments (current) | 618 | - | 
R655-R656 | Trade receivables | 619 | - | 
R657 | Cash and cash equivalents | 620 | - | 
R658 | Bank balances other than cash | 621 | - | 
R659-R660 | Loans (current) | 622 | - | 
R661 | Other financial assets (current) | 623 | - | 
R661 | Assets Classified as Held for Sale | 624 | ZERO_STANDING | blank or dash in all periods in text layer; template signal; confirm visually
R662-R663 | Other current assets | 625 | - | 
R662-R663 | TOTAL ASSETS | 627 | - | 
R666-R668 | Equity share capital | 631 | - | 
R669-R671 | Other equity | 632 | - | 
R674-R675 | Lease liabilities (non-current) | 636 | - | 
R674-R675 | Deferred tax liabilities (net) | 637 | - | 
R676-R677 | Provisions (non-current) | 638 | - | 
R681-R682 | Lease liabilities (current) | 642 | - | 
R685-R686 | Trade payables Micro and Small Enterprises | 644 | - | 
R685-R686 | Trade payables Other than MSE | 645 | - | 
R687-R688 | Other financial liabilities | 646 | - | 
R689-R690 | Other current liabilities | 647 | - | 
R691-R692 | Current tax liability (net) | 648 | - | 
R691-R692 | Provisions (current) | 649 | - | 
R695-R696 | TOTAL EQUITY AND LIABILITIES | 651 | - | 

### Consolidated CF
ROW ID(s) | item | fulltext line | A2 flags | note
---|---|---|---|---
R697-R698 | Profit before tax | 665 | - | 
R699-R700 | Depreciation and amortisation | 671 | - | 
R701-R702 | Finance cost | 673 | - | 
R703-R704 | Interest income | 675 | - | 
R705-R706 | Unrealised exchange (gain)/loss | 677 | - | 
R707 | Profit/loss on sale or write-off of PPE | 678 | - | 
R707 | Profit on sale of investment | 679 | ZERO_STANDING | blank or dash in all periods in text layer; template signal; confirm visually
R708-R709 | Dividend income | 681 | - | 
R710-R711 | Sundry balances written back | 683 | - | 
R710-R711 | Provision for doubtful advances | 684 | ZERO_STANDING | blank or dash in all periods in text layer; template signal; confirm visually
R712-R714 | Net gain on financial assets | 685 | ZERO_STANDING | blank or dash in all periods in text layer; template signal; confirm visually
R715-R716 | Operating profit | 689 | - | 
R717-R718 | Transfer of Foreign Currency Translation Reserve | 690 | - | 
R724-R725 | Inventories | 695 | - | 
R726 | Trade receivables | 696 | - | 
R727-R728 | Loans | 697 | - | 
R729-R730 | Other financial assets | 698 | - | 
R729-R730 | Other assets | 699 | - | 
R733-R734 | Trade payables | 701 | - | 
R735-R736 | Other financial liabilities | 702 | - | 
R735-R736 | Other liabilities | 703 | - | 
R737-R738 | Provisions | 704 | - | 
R737-R738 | Cash generated from operations | 706 | - | 
R739-R740 | Direct taxes paid | 707 | - | 
R741-R742 | Net cash flow from operating activities (A) | 709 | - | 
R745 | Purchase of PPE and intangibles | 712 | - | 
R746-R747 | Proceeds from sale of PPE | 713 | - | 
R748-R749 | Interest income (investing) | 714 | - | 
R750 | Dividend income (investing) | 715 | - | 
R751 | Net (investment)/redemption of mutual funds | 716 | - | 
R752-R753 | Net cash used in investing (B) | 718 | - | 
R756-R757 | Finance cost (financing) | 721 | - | 
R758-R759 | Repayment of lease liability | 722 | - | 
R760-R761 | Dividend paid | 723 | - | 
R762-R763 | Movement in margin money deposit | 724 | - | 
R764-R765 | Movement in unclaimed dividend account | 725 | - | 
R768-R769 | Net cash from/(used in) financing (C) | 727 | - | 
R770-R771 | Net increase/(decrease) in cash (A+B+C) | 728 | - | 
R772-R773 | Cash and cash equivalents (opening 1 April) | 730 | - | 
R772-R773 | Effects of exchange rate changes on cash | 731 | ZERO_STANDING | blank or dash in all periods in text layer; template signal; confirm visually
- | Cash and cash equivalents (closing 30 Sept) | 733 | NO_NUMBER_ROW | 

### Media release summary table (page 16)
ROW ID(s) | item | fulltext line | A2 flags | note
---|---|---|---|---
R795-R797 | Revenue from operations | 772 | RESTATED | restates consolidated P&L p12; page-16 values displaced (R1754)
R805-R807 | EBITDA | 774 | RESTATED | restates consolidated P&L p12; page-16 values displaced (R1754)
R816-R818 | EBITDA margin % | 776 | RESTATED | restates consolidated P&L p12; page-16 values displaced (R1754)
R826-R828 | PBT | 778 | RESTATED | restates consolidated P&L p12; page-16 values displaced (R1754)
R837-R839 | PBT margin % | 780 | RESTATED | restates consolidated P&L p12; page-16 values displaced (R1754)
R843-R845 | Cash Profit | 782 | RESTATED | restates consolidated P&L p12; page-16 values displaced (R1754)
R849-R851 | PAT | 784 | RESTATED | restates consolidated P&L p12; page-16 values displaced (R1754)
R854-R856 | PAT margin % | 786 | RESTATED | restates consolidated P&L p12; page-16 values displaced (R1754)
R859-R861 | EPS (INR) | 788 | RESTATED | restates consolidated P&L p12; page-16 values displaced (R1754)

## 3. AGENDA ITEMS AND MEETING TIMES (Board Outcome letter, pages 1-2)
ROW ID | item | A2 flags | note
---|---|---|---
R007 | Agenda item 1: Unaudited Financial Results (Standalone and Consolidated), Q2 and H1 ended 30-Sep-2026, with Limited Review Reports | - | only numbered agenda item; no AR approval, AGM, dividend, director, auditor, ESOP or capital-raising item
R1297 | Press Release enclosed | ENCLOSURE | pages 16-19
R1347 | Investor Presentation enclosed | ENCLOSURE | pages 20-43
R1435 | Board meeting start 11:30 A.M., 22 Oct 2026 | - | date token row
R1712 | Board meeting end time illegible ("concluded around ? a.m.") | FOOTNOTE_UNRESOLVED | duration not computable; verify visually
Annexures / director profiles: none in this filing.

## 5. AUDITOR REPORT PARAGRAPHS
ref | paragraph | A2 flags | IDs / note
---|---|---|---
A1 | Standalone LRR p3 para 1: review scope, Reg 33 submission | - | R1732
A2 | Standalone LRR p3 para 2: management responsibility, Ind AS 34 basis | - | page-group rows only (no dedicated structured row)
A3 | Standalone LRR p3 para 3: SRE 2410, moderate assurance, no audit opinion | - | R1733
A4 | Standalone LRR p3-4 para 4: conclusion, nothing has come to attention (unmodified) | UNMODIFIED | R1734
A5 | Consolidated LRR p9 para 1: review of Group statement | - | page-group rows only (no dedicated structured row)
A6 | Consolidated LRR p9 para 2: responsibility, Ind AS 34 | - | page-group rows only (no dedicated structured row)
A7 | Consolidated LRR p9 para 3: SRE 2410, no audit opinion | - | R1735
A8 | Consolidated LRR p10 unnumbered: SEBI circular CIR/CFD/CMD1/44/2019 procedures | - | R1320, R1736
A9 | Consolidated LRR p10 para 4: entities included (3 listed) | - | R1313-R1315
A10 | Consolidated LRR p10 para 5: conclusion, unmodified, relies on other auditors and management report | UNMODIFIED | page-group rows only (no dedicated structured row)
A11 | Consolidated LRR p10 para 6 Other Matters: two subsidiaries reviewed by other auditors | OTHER_AUDITOR_RELIANCE | R1319, R1737
A12 | Consolidated LRR p10-11 para 7: one subsidiary NOT reviewed by other auditors, management-furnished, not material | MGMT_FURNISHED_ENTITY | R1738
A13 | Consolidated LRR p11: "Our conclusion is not modified in respect of the above matters." | UNMODIFIED | R1739
S1 | Standalone sign-off p4: Naitik J Mehta (J. H. Mehta, M.No. 130010), Asha Patel (V Sankar Aiyar, M.No. 166048), Mumbai, 22 Oct 2026 | NO_TIMESTAMP | R1305-R1308
S2 | Consolidated sign-off p11, same partners; UDINs illegible | FOOTNOTE_UNRESOLVED | R1740
Opinion type: limited review conclusion, unmodified, both reports. Emphasis of Matter: none. Going Concern language: none found.

## 6. ENTITIES (consolidation list)
ROW ID | entity | relationship | A2 flags
---|---|---|---
R1298 | Garware Hi-Tech Films Limited | parent / holding company | -
R1313, R1316 | Garware Hi-Tech Films International Limited | 100% subsidiary (LRR 4a; Note 3) | -
R1314, R1318 | Global Hi-Tech Films Inc. | 100% step-down subsidiary (Note 3); listed alongside direct subsidiaries in LRR para 4b | STEP_DOWN_ONLY_IN_NOTE3
R1315, R1317 | Garware Hi-Tech Global Trading FZCO | 100% subsidiary (LRR 4c; Note 3 spelling lacks hyphens) | NAME_VARIANT
No prior list supplied: ENTITY_CHANGE not assessable (none raised). LRR paras 6-7 split the subsidiaries into 2 reviewed by other auditors and 1 management-furnished; which is which is not named: flag UNIDENTIFIED_ENTITY_ASSIGNMENT. Other entity rows (auditors, exchanges, people, events, products, awards, CSR) are accounted in section 11.

## 7. SIGNATURE BLOCKS
ROW ID | signatory | A2 flags | note
---|---|---|---
R1302 | Awaneesh Srivastava, Company Secretary, FCS 8513 (letter p2) | NO_TIMESTAMP | scanned, no digital timestamp in text layer
R1312 | Vice-Chairperson and Joint Managing Director, results signature pp8, 15 (name not in line; Ms. Monika Garware per R1346) | NO_TIMESTAMP | dated 22nd October 2026; p15 date cut off
R1307-R1308 | Auditor partners pp4, 11, dated 22 Oct 2026 | NO_TIMESTAMP | UDIN illegible R1740

## 8. FORWARD-LOOKING STATEMENTS (one row per FORWARD ID)
ROW ID | page | A2 flags | cross-ref / materiality
---|---|---|---
R1391 | p16 | FORWARD | GUIDANCE_CHANGE: raise of 200 bps to 27% +/-2%; prior range 23-27% per R1401; restated R1402, R1406, R1422
R1392 | p16 | FORWARD | RESTATED R1403, R1405 (Rs 2,500+ Cr)
R1393 | p17 | FORWARD | RESTATED R1399, R1424 (TPU Q3 FY27)
R1394 | p17 | FORWARD | RESTATED with variance: Rs 191 Cr here vs Rs 192 Cr at R1425 (p33); ~1,200 LSF restated R1395, R1425
R1395 | p17 | FORWARD | cross-ref R1394, R1425
R1396 | p17 | FORWARD | -
R1397 | p17 | FORWARD | cross-ref R1398, R1409
R1398 | p17 | FORWARD | -
R1399 | p18 | FORWARD | RESTATED R1393
R1400 | p18 | FORWARD | -
R1401 | p18 | FORWARD | cross-ref R1391 (prior guidance range)
R1402 | p29 | FORWARD | -
R1403 | p29 | FORWARD | -
R1404 | p29 | FORWARD | -
R1405 | p29 | FORWARD | -
R1406 | p29 | FORWARD | -
R1407 | p29 | FORWARD | -
R1408 | p29 | FORWARD | -
R1409 | p29 | FORWARD | -
R1410 | p29 | FORWARD | -
R1411 | p29 | FORWARD | AS_EXTRACTED: p29 table cell, column-displaced (R1782)
R1412 | p29 | FORWARD | AS_EXTRACTED: p29 table cell, column-displaced (R1782)
R1413 | p29 | FORWARD | -
R1414 | p29 | FORWARD | -
R1415 | p29 | FORWARD | -
R1416 | p29 | FORWARD | -
R1417 | p29 | FORWARD | -
R1418 | p27 | FORWARD | -
R1419 | p27 | FORWARD | RESTATED R1424 (Rs 118 Cr TPU capex)
R1420 | p27 | FORWARD | -
R1421 | p32 | FORWARD | -
R1422 | p32 | FORWARD | -
R1423 | p32 | FORWARD | -
R1424 | p33 | FORWARD | RESTATED R1419 (118 Cr), TPU 360 LSF p.a.
R1425 | p33 | FORWARD | RESTATED variance vs R1394
R1426 | p37 | FORWARD | target 300 vs 250+ current (R1366)
R1427 | p31 | FORWARD | -

## 9. SLIDES (pages 20-43; press release pages 16-19 are not slides)
slide(page) | title | content type | A2 flags | structured IDs on slide
---|---|---|---|---
20 | Title: Q2 & H1 FY27 Investor Presentation | text | - | R1523-R1524
21 | Contents | text | - | R908-R911
22 | Safe Harbour / disclaimers | text | - | R1761-R1764
23 | Divider "Business Highlights" (zero text, photos) | photo | SPARSE_SLIDE | none (no text)
24 | Message from the CMD (Dr. S B Garware) | text | - | R912-R914, R1353, R1525-R1528
25 | Q2 & H1 FY27 Consolidated Financial Performance | chart+table | - | R915-R942, R1529-R1548, R1760
26 | Quarterly Consolidated Performance Trend (revenue, EBITDA, PAT, EBITDA bridge) | chart | - | R943-R1011, R1549-R1622, R1765, R1781
27 | Strategic Technology Partnership: GHFL x Lubrizol TPU | text+chart | - | R1012-R1016, R1418-R1420, R1782
28 | New vertical: PDLC films for Smart Architecture | text+photo | - | R1017-R1019
29 | Raises FY27 EBITDA Margin Guidance to 27% +/-2% (FY25 to FY27E, medium-term) | table | - | R1020-R1066, R1402-R1417, R1623-R1629, R1766-R1769
30 | Divider, page marker "11" only | photo | SPARSE_SLIDE | R1067
31 | Over 3 Decades of Innovation, Excellence & Growth (metrics, capacity, divisions) | table+text | - | R1068-R1085, R1352, R1354-R1366, R1427, R1630-R1635, R1770-R1771
32 | 2017-2026 Value Transformation Journey | chart+text | - | R1086-R1095, R1372, R1421-R1423, R1636-R1640, R1713-R1714, R1772
33 | A Journey of Scalable Innovation (capacity timeline) | chart | - | R1096-R1123, R1424-R1425, R1641-R1663, R1715-R1719
34 | Synergising marketing strategies & Hi-tech products | text | - | R1124-R1126, R1367-R1371
35 | Business Strategy: Four Pillars | text | - | R1127-R1137, R1373, R1664-R1667, R1773-R1776
36 | Divider, page marker "17" only | photo | SPARSE_SLIDE | R1138
37 | Product Overview (SCF, PPF, shrink film) | text | - | R1139-R1141, R1379, R1426
38 | Product Strategy: Premium Market Positioning (awards) | text | - | R1142-R1161, R1374-R1378, R1380
39 | Divider, page marker "20" only | photo | SPARSE_SLIDE | R1162
40 | Environmental Stewardship / ESG | text | - | R1163-R1173, R1381-R1385, R1668-R1669
41 | Building Better Communities (CSR) | text+photo | - | R1386-R1390
42 | Consolidated Annual Performance (FY22-FY26) | chart | - | R1174-R1288, R1670-R1710, R1777-R1780
43 | Thank You / IR contact | text | - | R1289-R1292, R1350-R1351
No prior deck supplied: DROPPED_SLIDE not assessable.

## 10. SLIDE NUMBERS (NUMBER + DATE tokens per slide, incl. chart OCR labels)
slide | NUMBER ids | DATE ids | counts
---|---|---|---
20 | - | R1523-R1524 | N0 D2
21 | R908-R911 | - | N4 D0
22 | - | - | N0 D0
23 | - | - | N0 D0
24 | R912-R914 | R1525-R1528 | N3 D4
25 | R915-R942 | R1529-R1548 | N28 D20
26 | R943-R1011 | R1549-R1622 | N69 D74
27 | R1012-R1016 | - | N5 D0
28 | R1017-R1019 | - | N3 D0
29 | R1020-R1066 | R1623-R1629 | N47 D7
30 | R1067 | - | N1 D0
31 | R1068-R1085 | R1630-R1635 | N18 D6
32 | R1086-R1095 | R1636-R1640, R1713-R1714 | N10 D7
33 | R1096-R1123 | R1641-R1663, R1715-R1719 | N28 D28
34 | R1124-R1126 | - | N3 D0
35 | R1127-R1137 | R1664-R1667 | N11 D4
36 | R1138 | - | N1 D0
37 | R1139-R1141 | - | N3 D0
38 | R1142-R1161 | - | N20 D0
39 | R1162 | - | N1 D0
40 | R1163-R1173 | R1668-R1669 | N11 D2
41 | - | - | N0 D0
42 | R1174-R1288 | R1670-R1710 | N115 D41
43 | R1289-R1292 | - | N4 D0

## 11. ID ACCOUNTABILITY GROUPS (every structured ID, by page and type)
page | type | category | ID ranges | n
---|---|---|---|---
1 | DATE | board outcome letter | R1428-R1435, R1711-R1712 | 10
1 | ENTITY | board outcome letter | R1293-R1301 | 9
1 | NUMBER | board outcome letter | R001-R017 | 17
2 | ENTITY | board outcome letter | R1302 | 1
2 | NUMBER | board outcome letter | R018-R028 | 11
3 | DATE | standalone LRR | R1436-R1441 | 6
3 | ENTITY | standalone LRR | R1303-R1304, R1309 | 3
3 | NUMBER | standalone LRR | R029-R046 | 18
3 | QUALIFIER | standalone LRR | R1732-R1734 | 3
4 | DATE | standalone LRR | R1442-R1443 | 2
4 | ENTITY | standalone LRR | R1305-R1308 | 4
4 | NUMBER | standalone LRR | R047-R057 | 11
4 | QUALIFIER | standalone LRR | R1740 | 1
5 | DATE | standalone P&L | R1444-R1450 | 7
5 | ENTITY | standalone P&L | R1310-R1311 | 2
5 | NUMBER | standalone P&L | R058-R216 | 159
5 | QUALIFIER | standalone P&L | R1720-R1726 | 7
6 | DATE | standalone BS | R1451-R1452 | 2
6 | NUMBER | standalone BS | R217-R291 | 75
6 | QUALIFIER | standalone BS | R1727 | 1
7 | DATE | standalone CF | R1453-R1457 | 5
7 | NUMBER | standalone CF | R292-R366 | 75
7 | QUALIFIER | standalone CF | R1728 | 1
8 | DATE | standalone notes/signature | R1458-R1461 | 4
8 | ENTITY | standalone notes/signature | R1312, R1321 | 2
8 | NUMBER | standalone notes/signature | R367-R372 | 6
8 | QUALIFIER | standalone notes/signature | R1729-R1731 | 3
9 | DATE | consolidated LRR | R1462-R1466 | 5
9 | NUMBER | consolidated LRR | R373-R393 | 21
9 | QUALIFIER | consolidated LRR | R1735 | 1
10 | DATE | consolidated LRR | R1467-R1475 | 9
10 | ENTITY | consolidated LRR | R1313-R1315, R1319-R1320 | 5
10 | NUMBER | consolidated LRR | R394-R423 | 30
10 | QUALIFIER | consolidated LRR | R1736-R1738 | 3
11 | DATE | consolidated LRR | R1476-R1477 | 2
11 | NUMBER | consolidated LRR | R424-R432 | 9
11 | QUALIFIER | consolidated LRR | R1739 | 1
12 | DATE | consolidated P&L | R1478-R1484 | 7
12 | NUMBER | consolidated P&L | R433-R616 | 184
12 | QUALIFIER | consolidated P&L | R1741-R1746 | 6
13 | DATE | consolidated BS | R1485-R1486 | 2
13 | NUMBER | consolidated BS | R617-R696 | 80
13 | QUALIFIER | consolidated BS | R1747 | 1
14 | DATE | consolidated CF | R1487-R1491 | 5
14 | NUMBER | consolidated CF | R697-R773 | 77
14 | QUALIFIER | consolidated CF | R1748 | 1
15 | DATE | consolidated notes | R1492-R1495 | 4
15 | ENTITY | consolidated notes | R1316-R1318 | 3
15 | NUMBER | consolidated notes | R774-R784 | 11
15 | QUALIFIER | consolidated notes | R1749-R1752 | 4
16 | DATE | media release | R1496-R1508 | 13
16 | ENTITY | media release | R1322-R1324 | 3
16 | FORWARD | media release | R1391-R1392 | 2
16 | NUMBER | media release | R785-R876 | 92
16 | QUALIFIER | media release | R1753-R1758 | 6
17 | DATE | media release | R1509-R1518 | 10
17 | ENTITY | media release | R1325-R1335 | 11
17 | FORWARD | media release | R1393-R1398 | 6
17 | NUMBER | media release | R877-R890 | 14
17 | QUALIFIER | media release | R1759 | 1
18 | DATE | media release | R1519-R1522 | 4
18 | ENTITY | media release | R1336-R1346 | 11
18 | FORWARD | media release | R1399-R1401 | 3
18 | NUMBER | media release | R891-R900 | 10
19 | ENTITY | media release | R1347-R1349 | 3
19 | NUMBER | media release | R901-R907 | 7
20 | DATE | investor presentation | R1523-R1524 | 2
21 | NUMBER | investor presentation | R908-R911 | 4
22 | QUALIFIER | investor presentation | R1761-R1764 | 4
24 | DATE | investor presentation | R1525-R1528 | 4
24 | ENTITY | investor presentation | R1353 | 1
24 | NUMBER | investor presentation | R912-R914 | 3
25 | DATE | investor presentation | R1529-R1548 | 20
25 | NUMBER | investor presentation | R915-R942 | 28
25 | QUALIFIER | investor presentation | R1760 | 1
26 | DATE | investor presentation | R1549-R1622 | 74
26 | NUMBER | investor presentation | R943-R1011 | 69
26 | QUALIFIER | investor presentation | R1765, R1781 | 2
27 | FORWARD | investor presentation | R1418-R1420 | 3
27 | NUMBER | investor presentation | R1012-R1016 | 5
27 | QUALIFIER | investor presentation | R1782 | 1
28 | NUMBER | investor presentation | R1017-R1019 | 3
29 | DATE | investor presentation | R1623-R1629 | 7
29 | FORWARD | investor presentation | R1402-R1417 | 16
29 | NUMBER | investor presentation | R1020-R1066 | 47
29 | QUALIFIER | investor presentation | R1766-R1769 | 4
30 | NUMBER | investor presentation | R1067 | 1
31 | DATE | investor presentation | R1630-R1635 | 6
31 | ENTITY | investor presentation | R1352, R1354-R1366 | 14
31 | FORWARD | investor presentation | R1427 | 1
31 | NUMBER | investor presentation | R1068-R1085 | 18
31 | QUALIFIER | investor presentation | R1770-R1771 | 2
32 | DATE | investor presentation | R1636-R1640, R1713-R1714 | 7
32 | ENTITY | investor presentation | R1372 | 1
32 | FORWARD | investor presentation | R1421-R1423 | 3
32 | NUMBER | investor presentation | R1086-R1095 | 10
32 | QUALIFIER | investor presentation | R1772 | 1
33 | DATE | investor presentation | R1641-R1663, R1715-R1719 | 28
33 | FORWARD | investor presentation | R1424-R1425 | 2
33 | NUMBER | investor presentation | R1096-R1123 | 28
34 | ENTITY | investor presentation | R1367-R1371 | 5
34 | NUMBER | investor presentation | R1124-R1126 | 3
35 | DATE | investor presentation | R1664-R1667 | 4
35 | ENTITY | investor presentation | R1373 | 1
35 | NUMBER | investor presentation | R1127-R1137 | 11
35 | QUALIFIER | investor presentation | R1773-R1776 | 4
36 | NUMBER | investor presentation | R1138 | 1
37 | ENTITY | investor presentation | R1379 | 1
37 | FORWARD | investor presentation | R1426 | 1
37 | NUMBER | investor presentation | R1139-R1141 | 3
38 | ENTITY | investor presentation | R1374-R1378, R1380 | 6
38 | NUMBER | investor presentation | R1142-R1161 | 20
39 | NUMBER | investor presentation | R1162 | 1
40 | DATE | investor presentation | R1668-R1669 | 2
40 | ENTITY | investor presentation | R1381-R1385 | 5
40 | NUMBER | investor presentation | R1163-R1173 | 11
41 | ENTITY | investor presentation | R1386-R1390 | 5
42 | DATE | investor presentation | R1670-R1710 | 41
42 | NUMBER | investor presentation | R1174-R1288 | 115
42 | QUALIFIER | investor presentation | R1777-R1780 | 4
43 | ENTITY | investor presentation | R1350-R1351 | 2
43 | NUMBER | investor presentation | R1289-R1292 | 4

## 12. MISSING_FROM_STRUCTURED (fulltext sweep: lines with digits and zero structured rows)
line | page | claim text | flag
---|---|---|---
77 | 2 | CIN: LI0889MHl957PLC010889 (page-2 footer, garbled; page-1 CIN is R1299) | MISSING_FROM_STRUCTURED
495 | 12 | CIN : L10889MH1957PLC010889 (consolidated results header) | MISSING_FROM_STRUCTURED
1478 | 43 | CIN: L10889MH1957PLC010889 (presentation back page) | MISSING_FROM_STRUCTURED
751 | 15 | Place: Mumbai / VICE-CHAIRPERSON AND JOINT MANAGING DIRECT9R (garbled title; date cut "22nd October, 20") | MISSING_FROM_STRUCTURED (low materiality)
All other digit-bearing lines without rows are page markers or headings. No loop back needed unless A3 checks CIN.

```yaml
stage: A2-enumerator
company: "GRWRHITECH"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/grwrhitech-q2fy27/work/ledger_results_grwrhitech_q2fy27.md"
counts:
  notes: 7
  line_items: 205
  zero_standing: 11
  agenda_items: 3
  auditor_paras: 13
  entities: 4
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 24
  slide_numbers: 580
flags_raised: [ZERO_STANDING, RESTATED, GUIDANCE_CHANGE, FOOTNOTE_UNRESOLVED, MGMT_FURNISHED_ENTITY, OTHER_AUDITOR_RELIANCE, UNIDENTIFIED_ENTITY_ASSIGNMENT, SPARSE_SLIDE, NO_TIMESTAMP, MISSING_FROM_STRUCTURED]
ids_in_structured: 1782
ids_referenced: 1782
orphan_ids: []
missing_from_structured: [CIN line 77 p2, CIN line 495 p12, CIN line 1478 p43, signature date line 751 p15]
gate_a2: pass
mismatch_note: ""
analyst_note: "Zero-standing rows (11) are blank or dash in the displaced text layer, mainly consolidated NCI attributions, OCI reclassified lines, held-for-sale, and cash flow lines for sale of investments and doubtful advances. A1 could not pair columns on pp5-7, 12-14, so confirm values visually. Consolidation: LRR lists 3 subsidiaries, Note 3 calls Global Hi-Tech Films Inc a step-down; one subsidiary (nil revenue, assets Rs 0.18 Cr) is management-furnished and unnamed. FORWARD: FY27 EBITDA guidance raised 200 bps to 27% +/-2% (prior 23-27%, R1401); SCF line capex shows Rs 191 Cr (R1394) vs Rs 192 Cr (R1425). Board end time and UDINs illegible. Three CIN lines plus one signature-date line are MISSING_FROM_STRUCTURED, low materiality. No prior ledger: ENTITY_CHANGE and DROPPED_SLIDE not assessable."
```
