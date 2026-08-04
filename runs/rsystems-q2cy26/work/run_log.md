# Run Log — RSYSTEMS Q2 CY2026

- Ticker: RSYSTEMS (NSE: RSYSTEMS, BSE: 532735 / 977286)
- Company: R Systems International Limited
- Period: Quarter and six months ended June 30, 2026 (calendar-year reporter → Q2 CY2026)
- Invoked: /run-quarterly RSYSTEMS --docs <results> <press release>

## Setup / Prechecks
- Protocol files present: Quarterly_Results_Review_Protocol_v1_2.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Master_Project_Prompt_v3.3.md — OK
- Toolchain: pdftotext/pdfinfo/pdftoppm/tesseract initially MISSING → installed poppler-utils + tesseract-ocr via apt-get — OK
- Company memory companies/RSYSTEMS.md: ABSENT (new coverage)

## Document-class detection
- inputs/results_rsystems_q2cy26.pdf (21pp): Reg 30/33/52 Board Outcome + audited standalone & unaudited consolidated financial results → doctype = results
- inputs/presentation_rsystems_q2cy26.pdf (11pp): Earnings Press Release, management commentary + highlights + key deal wins (not Reg 33 statement, not a concall transcript) → doctype = presentation
- No concall transcript supplied this run.

## GATE A1 — PASS (both documents)
- results: 21/21 pages, formfeed 21, 1357 lines, unit=Millions (x0.1→Cr), no OCR. extract_results_rsystems_q2cy26.txt
- presentation: 11/11 pages, formfeed 11, 579 lines, unit=Millions (x0.1→Cr, parallel US$mn), no OCR. extract_presentation_rsystems_q2cy26.txt

## A2 — enumerators launched (results ledger + presentation ledger)

## GATE A2 — PASS (both documents)
- results: 8 agenda items, 31 notes, 281 line items (6 zero-standing), 27 auditor paras, 31 entities (5 ENTITY_CHANGE Novigo + Velotio/Scaleworx amalgamation). Count reconciled.
- presentation: 189 gated rows across 18 categories (1 ZERO_STANDING). Count reconciled.

## A3 — forensics launched (results F1-F17 + presentation F1-F17), Notion Step-5 checklist passed inline

## GATE A3 — PASS (both documents)
- results forensics: 17/17 statuses, 13 findings (7 forward-signal, 6 ambiguous), all line-cited. Key: S-vs-C PAT gap +51pp Q1->Q2; finance cost 4.4x (int cover 25.4x->9.35x); static NCI 1923.88m (Novigo CCPS); 21 subs unreviewed = 20.6% Q PAT; IT-services segment margin 16.16%->12.65% QoQ; OCRPS 5.16m allotted; hedge loss 89.63m to reclassify; governance refresh via postal ballot.
- presentation forensics: 17/17 statuses, 12 findings. Key: reported PAT -26.7% YoY masked by +35.4% adjusted (NOIDA gain stripped); INR 30.2% vs US$ 17.7% gap (FX+Novigo); Novigo rev unquantified; ETR 30.98%; silent on organic CC / ACV / fixed-price mix / ROCE.

## A4 — analyst launched (merged Role 4 + Role 5 review)

## A4 — COMPLETE. Verdict: PROCEED WITH FLAGS. Decision Status UNCHANGED (WATCHLIST/BUY, flag not decide).
- Consol Q2 YoY: Rev 462.02->601.70 (+30.2%); core operating PBT ex-OI +51.6%; reported PAT 75.85->55.57 (-26.7%) = base effect of vanished Q2CY25 NOIDA gain Rs 43.60 Cr; adj PAT +35.4%, adj EBITDA margin 20.1% (from 17.3%).
- S-vs-C PAT gap: 11.1% (Q2CY25) -> 4.0% (Q1CY26) -> 55.2% (Q2CY26); FY25 -6.6%. 51pp QoQ swing.
- CFO/PAT 1.35x H1 -> FIRING (not INDETERMINATE). Net cash ex-lease +63.12 Cr.
- 13 Questions-for-Management (every A3 ambiguous/forward-signal mapped). Notion OCRPS unit error caught: 5.16 million shares NOT 5.16 Cr.

## A5 — adversary launched

## A5 — loop 1: INCOMPLETE -> loop back to A4
- Coverage PASS (all A2 counts reproduced). OCRPS 5.16 million correction confirmed correct.
- FAIL-1: Reported EBITDA H1 CY25 stated 174.99 (19.35%) vs recomputed 189.99 (21.00%) [PBT 1559.11 + D&A 304.44 + FC 36.31 = 1899.86 mn]. 15 Cr / 165 bps error, H1 CY25 column only.
- FAIL-2: H1 CY26 working-capital change stated "+23.61 Cr released / no drag" vs recomputed -18.30 Cr net USE (2065.14 - 2248.17). Wrong sign; 51.19 Cr receivables release offset by 47.58 Cr other-assets build.
- Audit 3: cash-conversion "no WC drag" bear counter survives, must be grafted.

## A4 — loop-1 fixes landed (all 3)
- FIX1: Reported EBITDA H1 CY25 -> 189.99 (21.00%). FIX2: H1 CY26 WC -> net USE 18.30 Cr. FIX3: cash-quality bear counter grafted (1.35x despite WC use; WC-neutral ~1.50x); new Q14 on 47.58 Cr other-assets build.
- Verdict PROCEED WITH FLAGS unchanged; Decision Status WATCHLIST/BUY unchanged; INDETERMINATE-cash cap still not triggered.

## A5 — loop 2 launched (fresh context)

## A5 — loop 2: COMPLETE. Gate A5 passes. Proceed to Notion save.
- All 3 fixes verified correct, no new errors, coverage + standalone/consolidated completeness hold, all bear counters grafted. Novigo appears once in press release (DSO footnote), corroborating silence flag.
