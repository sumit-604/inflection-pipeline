# A2 COMPLETENESS LEDGER — EMVDL Q1 FY27 (Results Filing)
Source: /home/user/inflection-pipeline/runs/emvdl-q1fy27/work/extract_results_emvdl_q1fy27.txt
Line numbers below cite the A1 extract's own embedded line numbers (column 1 of the
extract file, tab-delimited). Real file line = embedded line + 14 (14-line header block).
Doctype: results. Two results statements (standalone + consolidated), each with own
notes section; one Reg 30 Board Outcome letter with 4 agenda items and 2 sub-annexures
(A, B); one consolidation entity list (Annexure 1, 183 named entities + 1 JV = 184).

```
=== A2 COUNT TEST ===
category: notes          grep_count: 25   sweep_count: 25   match: yes
category: line_items     grep_count: 57   sweep_count: 57   match: yes
category: zero_standing  grep_count: 7    sweep_count: 7    match: yes
category: agenda_items   grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras  grep_count: 14   sweep_count: 14   match: yes
category: entities       grep_count: 184  sweep_count: 184  match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method note on grep vs sweep: grep pass used `grep -n -E "^\s*[0-9]+\.\s"` plus a
section-scoped pattern `sed -n '<notes-range>p' | grep -nP '^\s*\d+\s+[A-Z]'` isolated to
the standalone (lines 469-528) and consolidated (lines 932-1039) notes blocks; both OCR
artifacts ("IO" for "10") required manual correction. Sweep pass was a full manual
line-by-line read of the entire 1050-line extract (both Read tool calls, offset 0 and
offset 781). Entity count cross-checked two ways: (a) manual enumeration of Annexure 1
S.No columns 1-183 plus the separate 1-row Joint Venture table = 184; (b) the
consolidated notes' own Note 1 states "184 subsidiaries/joint ventures" — self-consistent,
match: yes.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (Reg 30 letter, pages 1-3)

Board meeting: commenced 04:00 PM, concluded 05:30 PM, August 10, 2026 (1h30m meeting).

| # | Agenda item | Line(s) | Detail | Flags |
|---|---|---|---|---|
| A | Unaudited financial results (standalone and consolidated), Q1 FY27, with Limited Review Reports | 22-29 | Approved; results + review reports to be uploaded to company website and published in newspapers per Reg 47 | — |
| B | Fund-raise via issuance of convertible warrants, preferential issue, private placement, up to INR 362.62 cr to promoter group | 31-82 | 3,25,18,900 warrants, exercise price INR 111.51/warrant (incl. premium INR 109.51), allottee Embassy Property Developments Pvt Ltd (Promoter Group); conversion window 18 months per SEBI ICDR, promoter voluntarily committed to convert within 6 months; subject to shareholder approval at ensuing AGM; disclosure at Annexure A | CAPITAL_RAISE |
| C | Appointment of Mr. Neel Virwani as Senior Management Personnel | 84-98 | Promoter Group member (son of Chairman Jitendra Virwani, brother of MD Aditya Virwani); Mumbai-based; effective October 1, 2026; subject to shareholder approval at AGM; disclosure at Annexure B | RELATED_PARTY |
| D | Re-appointment of Director — Mr. Jitendra Virwani (Chairman & Non-Executive Director) | 100-108 | Retires by rotation, offers himself for re-appointment on existing terms; subject to AGM approval; disclosure at Annexure B | — |

Additional letter content (not standalone agenda items but disclosure-bearing):
| Item | Line(s) | Detail | Flags |
|---|---|---|---|
| AGM notice commitment | 124-126 | Notice convening AGM to be circulated and intimated to exchanges within prescribed timelines | — |
| Digital signature block (Board Outcome letter) | 131-137 | Vikas Khandelwal, Company Secretary; digitally signed 2026.08.10 20:10:50 +05'30' — i.e., ~2h40m after 05:30 PM meeting conclusion | — (post-conclusion signing, no timing flag) |

---

## 2. ANNEXURE A — Reg 30 Preferential Issue Disclosure (pages 4-5)

| Item | Line(s) | Particular | Value | Flags |
|---|---|---|---|---|
| A-1 | 159-160 | Type of securities | Unlisted warrants convertible into equity shares of FV INR 2 | — |
| A-2 | 162-163 | Type of issuance | Preferential allotment, Chapter V SEBI ICDR | — |
| A-3 | 165-167 | Total securities / amount | 3,25,18,900 warrants @ INR 111.51 = INR 3,62,61,82,539 | — |
| A-4(i) | 171 | Names of investors | Embassy Property Developments Pvt Ltd (Promoter Group) | RELATED_PARTY |
| A-4(ii) pre/post table | 173-178 | Pre-preferential: 19,37,92,592 shares (13.94%); Post-preferential: 22,63,11,492 shares (15.90%) — Embassy Property Developments Pvt Ltd | — |
| A-4(ii) aggregate impact | 197-198 | Promoter Group aggregate holding to rise 42.65% -> 43.96% (+1.31%) on full warrant conversion | — |
| A-4(ii) issue price / investor count | 200-204 | Issue price INR 111.51/warrant; Number of investors: 1 (One) | CONCENTRATED_ALLOTTEE |
| A-4(iii) | 206-209 | Conversion commitment: within 6 months (voluntary, vs 18-month SEBI ICDR max); each warrant convertible into 1 equity share | — |
| A-4(iv) | 211 | Cancellation/termination of proposal | Not applicable | ZERO_STANDING |

---

## 3. ANNEXURE B — Director / SMP Change Disclosure (pages 6-8)

| Field | Line(s) — Jitendra Virwani | Line(s) — Neel Virwani | Flags |
|---|---|---|---|
| DIN | 234 — 00027674 | 234 — Not applicable (SMP, not director) | — |
| Reason for change | 236-247 — Re-appointment (retires by rotation, continuation of existing role, no change to terms; originally approved at EGM 25-Mar-2025) | 236-247 — New appointment as Senior Management Personnel per Reg 16(1)(d), w.e.f. Oct 1, 2026 | — |
| Brief profile | 249 — "Please refer below" (full profile at lines 279-291) | 249 — "Please refer below" (full profile at lines 294-317) | — |
| Relationships between directors | 250-269 — Father of Aditya Virwani (MD); not related to any other director | 250-269 — Not a director (SMP); disclosed voluntarily: son of Jitendra Virwani (Chairman), brother of Aditya Virwani (MD) | RELATED_PARTY |
| Non-debarment confirmation | 270-275 — Confirmed not debarred by SEBI/any authority | 270-275 — Confirmed not debarred by SEBI/any authority | — |

| Profile block | Line(s) | Content summary |
|---|---|---|
| Jitendra Virwani full profile | 279-290 | Age ~60; Chairman of Embassy Group since 1993 founding; 100msf+ portfolio; introduced WeWork to India (2017); founded Embassy Office Parks REIT (2019); Non-Exec Chairman WeWork India (2024), oversaw its 2025 IPO; appointed Chairman EDL (2025); Fellow RICS; equestrian sport advocate, education philanthropy |
| Neel Virwani full profile | 294-317 | Age ~27; BBA, Hult International Business School; associated with Embassy Group since April 2024; mentored by Jitendra Virwani, Aditya Virwani, Karan Virwani; exposure to business development, strategy, project execution, MMR expansion (Embassy Citadel, Worli) |

---

## 4. STANDALONE FINANCIAL RESULTS — LINE ITEMS (page 11, lines 418-457)
Unit: Rs millions. Periods: Q1FY27 (Jun-30-26, Unaudited) | Q4FY26 (Mar-31-26, Unaudited, balancing figure per Note 3) | Q1FY26 (Jun-30-25, Unaudited) | FY26 (Mar-31-26, Audited).

| Line | Line item | Line# | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Revenue from operations | 419 | 129.45 | 958.11 | 1,188.45 | 4,121.87 | — |
| 2 | Other income | 420 | 141.71 | 411.61 | 67.89 | 1,141.79 | — |
| 3 | Total Income | 421 | 271.16 | 1,369.72 | 1,256.34 | 5,263.66 | — |
| 4 | Land, material and contract cost | 424 | 187.63 | 770.39 | 770.31 | 3,145.81 | — |
| 5 | Employee benefits expense | 425 | 439.87 | 490.86 | 360.04 | 1,500.54 | — |
| 6 | Finance costs | 426 | 224.27 | 404.02 | 781.70 | 1,892.17 | — |
| 7 | Depreciation and amortisation expenses | 427 | 78.49 | 70.64 | 56.03 | 311.43 | — |
| 8 | Other expenses | 428 | 236.61 | 499.13 | 191.95 | 1,386.67 | — |
| 9 | Total Expenses | 429 | 1,166.87 | 2,235.04 | 2,160.03 | 8,236.62 | — |
| 10 | Loss before exceptional items and tax (1-2) | 431 | (895.71) | (865.32) | (903.69) | (2,972.96) | — |
| 11 | Exceptional items, net gain | 432-434 | – | 35.31 | – | 13.44 | ZERO_STANDING (dash Q1FY27, Q1FY26) |
| 12 | Loss before tax (3-4) | 433-436 | (895.71) | (830.01) | (903.69) | (2,959.52) | — |
| 13 | Current tax (incl. earlier year taxes) | 438 | (9.82) | – | (9.89) | (32.83) | — (single-period dash, not a standing template item) |
| 14 | Deferred tax charge/(credit) | 439 | 16.99 | (31.81) | (5.76) | (96.03) | — |
| 15 | Total tax charge/(credit) | 440 | 7.17 | (31.81) | (15.65) | (128.86) | — |
| 16 | Loss for the period/year (5-6) | 442 | (902.88) | (798.20) | (888.04) | (2,830.66) | — |
| 17 | OCI — Remeasurements of defined benefit plans, net of taxes | 445 | – | 0.35 | – | 12.46 | ZERO_STANDING (dash Q1FY27, Q1FY26) |
| 18 | Other comprehensive income for the period/year, net of tax | 446 | – | 0.35 | – | 12.46 | — (subtotal of line 17; same underlying signal, not separately counted) |
| 19 | Total comprehensive income for the period/year (7+8) | 449 | (902.88) | (797.85) | (888.04) | (2,818.20) | — |
| 20 | Paid-up equity share capital (FV Rs 2 each) | 451 | 2,780.07 | 2,780.07 | 2,730.50 | 2,780.07 | — |
| 21 | EPS — Basic (Rs) | 454 | (0.65) | (0.57) | (0.69) | (2.08) | — |
| 22 | EPS — Diluted (Rs) | 455 | (0.65) | (0.57) | (0.69) | (2.08) | — |
| 23 | Other equity | 457 | (blank) | (blank) | (blank) | 1,10,223.45 | ZERO_STANDING (only reported at FY-end per format; blank in all quarter columns) |

## 5. STANDALONE NOTES (page 12, lines 469-528)

| Note # | Line(s) | First ~15 words | Flags |
|---|---|---|---|
| 1 | 470-473 | "The unaudited standalone financial results of Embassy Developments Limited... reviewed by the audit committee and approved by the Board" (note numeral dropped by OCR at header) | — |
| 2 | 475-477 | "The unaudited financial results has been prepared in accordance with the Indian Accounting Standards..." | — |
| 3 | 479-480 | "The figures for the quarter ended March 31, 2026 are the balancing figures between audited figures..." | — |
| 4 | 482-485 | "The Company's primary business segment is reflected based on principal business activities... one reportable business segment" | — |
| 5 | 487-492 | "Pursuant to Embassy Developments Limited Employee Stock Option Scheme - 2015 (ESOS 2025) scheme..." grants 5,36,798 options + 3,26,260 PSUs; 1,94,165 lapsed; net outstanding 1,46,99,601 options / 48,04,041 PSUs | — |
| 6 | 494-511 | "The Company had a wholly owned subsidiary M/s Sinnar Thermal Power Limited (STPL)..." demerger, corporate guarantee, CIRP initiated Dec-9-2025, stayed by NCLAT Dec-11-2025, NCLAT allowed appeal May-4-2026, Company no longer under CIRP | LEGAL_CONTINGENCY |
| 7 | 513-516 | "Subsequent to the quarter ended June 30, 2026, the Company has issued 1,02,000 senior secured redeemable unrated unlisted NCDs..." Rs 10,200.00m aggregate; Rs 9,200.00m used for debt repayment | SUBSEQUENT_EVENT |
| 8 | 518-520 | "During the quarter ended June 30, 2026, the Registrar of Companies approved the strike off of three non-operational subsidiaries..." plus one foreign subsidiary struck off | ENTITY_CHANGE |
| 9 | 522-523 | "The Company, along with one of its subsidiaries, entered into a Share Purchase Agreement to sell its shares in another subsidiary..." Rs 1,000.00m; completed Apr-16-2026 | — |
| 10 | 526 | "Previous period, year numbers have been regrouped/reclassified wherever considered necessary" | — |
| 11 | 527-528 | "The aforesaid financial results are also available on the Company's website... and Stock Exchanges websites" | — |

Standalone auditor sign-off block (page 12, unaudited results statement, not the review
report): "...on behalf of Board of Directors... Managing Director, Place Bengaluru, Date
August 10, 2026" — line 529-536. Signatory name garbled/omitted by OCR (designation
"Managing Director" legible). Flag: SIGNATORY_NAME_NOT_LEGIBLE.

---

## 6. STANDALONE AUDITOR REVIEW REPORT (pages 9-10, lines 341-402)
Auditor: Agarwal Prakash & Co., Chartered Accountants, Firm Reg No. 005975N.

| Para | Line(s) | Type | Content | Flags |
|---|---|---|---|---|
| 1 | 348-353 | Scope/Introduction | Reviewed standalone unaudited results for quarter ended 30 June 2026, per Reg 33 | — |
| 2 | 355-361 | Management responsibility | Statement prepared per Ind AS 34, management's responsibility; auditor expresses conclusion, not opinion | — |
| 3 | 363-372 | Review standard | Conducted per SRE 2410; review is substantially less in scope than an audit; no audit opinion expressed | — |
| 4 | 379-386 | Conclusion (unmodified) | "nothing has come to our attention that causes us to believe... has not disclosed the information required... or that it contains any material misstatement" | Unmodified/clean conclusion; no EOM, no Other Matters, no Going Concern paragraph present in this report |

Signature block: Vikas Agarwal, Partner, Membership No. 09784 [sic, elsewhere 097848],
UDIN: 26097848GGMEHZ6100, Place: New Delhi, Date: 10 August 2026 — line 394-401.

---

## 7. CONSOLIDATED FINANCIAL RESULTS — LINE ITEMS (page 18, lines 880-923)
Unit: Rs millions. Same 4-period structure as standalone.

| Line | Line item | Line# | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Revenue from operations | 881 | 2,167.54 | 3,424.63 | 6,809.19 | 17,318.32 | — |
| 2 | Other income | 882 | 245.27 | 647.45 | 131.32 | 1,732.89 | — |
| 3 | Total Income | 883 | 2,412.81 | 4,072.08 | 6,940.51 | 19,051.21 | — |
| 4 | Land, material and contract cost | 885 | 2,054.65 | 3,657.29 | 5,925.32 | 16,070.36 | — |
| 5 | Employee benefits expense | 886 | 772.65 | 764.38 | 620.21 | 2,633.55 | — |
| 6 | Finance costs | 887 | 1,185.68 | 1,399.38 | 1,604.21 | 5,493.14 | — |
| 7 | Depreciation and amortization expense | 888 | 129.82 | 126.14 | 67.07 | 478.68 | — |
| 8 | Other expenses | 889 | 646.81 | 1,614.01 | 371.28 | 3,350.21 | — |
| 9 | Total Expenses | 890 | 4,789.61 | 7,561.20 | 8,588.09 | 28,026.04 | — |
| 10 | Loss before exceptional item and tax (1-2) | 891 | (2,376.80) | (3,489.12) | (1,647.58) | (8,974.83) | — |
| 11 | Exceptional items, net gain | 892 | – | 40.38 | – | 1.61 | ZERO_STANDING (dash Q1FY27, Q1FY26) |
| 12 | Loss before tax (3-4) | 893 | (2,376.80) | (3,448.74) | (1,647.58) | (8,973.21) | — |
| 13 | Current tax (incl. earlier year taxes) | 895 | 11.93 | 27.98 | 56.52 | 111.58 | — |
| 14 | Deferred tax credit | 896 | (9.04) | (221.02) | (48.10) | (341.95) | — |
| 15 | Total tax expense/(credit) | 897 | 2.89 | (193.04) | 8.42 | (230.37) | — |
| 16 | Loss after tax and before share of JV net profit/(loss) (5-6) | 898-900 | (2,379.69) | (3,255.70) | (1,656.00) | (8,742.85) | — |
| 17 | Share of net profit/(loss) in joint ventures | 901 | 35.67 | 21.38 | (0.44) | 18.10 | — |
| 18 | Loss after share of net profit/(loss) of JV (7+8) | 902 | (2,344.02) | (3,234.32) | (1,656.44) | (8,724.75) | — |
| 19 | OCI — Remeasurements of defined benefit plans, net of taxes | 905 | – | 4.07 | – | (16.51) | ZERO_STANDING (dash Q1FY27, Q1FY26) |
| 20 | OCI — Exchange difference in translation of foreign operations | 907 | OCR-garbled | 12.01(?) | 0.01 | (2.96) | OCR_GARBLED — only 3 of 4 period values legible; source PDF verification needed |
| 21 | Total other comprehensive income, net of income tax | 909-910 | – | 2.06 | 0.01 | (19.47) | — (subtotal of lines 19+20; same underlying signal, not separately counted) |
| 22 | Total comprehensive income for the period/year (9+10) | 911 | (2,344.02) | (3,232.26) | (1,656.43) | (8,774.22) | — |
| 23 | (Loss) attributable to — Equity holders of the Company | 913 | (2,342.94) | (3,237.79) | (1,658.49) | (8,726.45) | — |
| 24 | (Loss) attributable to — Non-controlling interest | 914 | (1.07) | 3.47 | 2.05 | 1.70 | — |
| 25 | Total comprehensive loss attributable to — Equity holders | 917 | (2,342.94) | (3,235.73) | (1,658.48) | (8,775.92) | — |
| 26 | Total comprehensive loss attributable to — Non-controlling interest | 918 | (1.07) | 3.47 | 2.05 | 1.70 | — |
| 27 | Paid up Equity Share Capital (FV Rs 2 per share) | 919 | 2,780.07 | 2,780.07 | 2,730.50 | 2,780.07 | — |
| 28 | EPS — Basic (Rs) | 921 | (1.69) | (2.33) | (1.29) | (6.43) | — |
| 29 | EPS — Diluted (Rs) | 922 | (1.69) | (2.33) | (1.29) | (6.43) | — |
| 30 | Other equity (including NCI) | 923 | (blank) | (blank) | (blank) | 96,859.81 | ZERO_STANDING (only reported at FY-end; blank in all quarter columns) |

## 8. CONSOLIDATED NOTES (pages 19-20, lines 932-1039)

| Note # | Line(s) | First ~15 words | Flags |
|---|---|---|---|
| 1 | 933-938 | "The unaudited consolidated financial results of EDL... reviewed by audit committee and approved by Board... pertains to EDL, Holding Company, along with its 184 subsidiaries/joint ventures" | — |
| 2 | 940-942 | "The unaudited consolidated financial results has been prepared in accordance with the Indian Accounting Standards..." | — |
| 3 | 944-945 | "The figures for the quarter ended March 31, 2026 represents the balancing amounts between the audited..." | — |
| 4 | 947-950 | "The Group's primary business segment is reflected based on principal business activities... one reportable segment" | — |
| 5 | 953-958 | "Pursuant to Embassy Developments Limited ESOS 2025 scheme..." grants 5,36,798 options + 3,26,260 PSUs; 1,94,165 lapsed; net outstanding 1,46,99,601 / 48,04,041 | — |
| 6 | 960-963 | "Subsequent to the quarter ended June 30, 2026, the Company has issued 1,02,000 senior secured redeemable NCDs..." Rs 10,200.00m; Rs 9,200.00m for debt repayment | SUBSEQUENT_EVENT |
| 7 | 966-968 | "During the quarter ended June 30, 2026, the Registrar of Companies approved the strike off of three non-operational subsidiaries..." plus one foreign subsidiary | ENTITY_CHANGE |
| 8 | 970-988 | "The Company had a wholly owned subsidiary M/s Sinnar Thermal Power Limited (STPL)..." same CIRP narrative as standalone Note 6 | LEGAL_CONTINGENCY |
| 9 | 997-1009 | "Embassy East Business Parks Limited (subsidiary) (EEBPL) holds leasehold rights over land under a Lease-cum-Sale Agreement..." KIADB resumption order Mar-16-2026 challenged, High Court allowed writ petition May-12-2026, Division Bench set aside that order Jun-15-2026, EEBPL retains possession pending fresh consideration on merits | LEGAL_CONTINGENCY (consolidated-only note, no standalone equivalent) |
| 10 | 1011-1019 | "Additional information on standalone financial results of the Company" — sub-table: Total income, Loss before tax, Loss after tax, Total comprehensive loss (4 line items, Q1FY27/Q4FY26/Q1FY26/FY26), reconciles exactly to Section 4 above | — |
| 11 | 1021-1031 | "The Board of Directors of Equinox India Infraestate Limited (Transferee Company)... approved draft Scheme of Amalgamation" for merger of Spero Properties and Services Pvt Ltd (wholly owned subsidiary, Transferor) into Transferee, appointed date Apr-1-2025; NCLT Mumbai Bench final hearing Aug-14-2026; NCLT New Delhi Bench final hearing Aug-27-2026 | SUBSEQUENT_EVENT / PENDING_APPROVAL |
| 12 | 1033-1034 | "The Company, along with one of its subsidiaries, entered into a Share Purchase Agreement to sell its shares..." Rs 1,000.00m; completed Apr-16-2026 (mirrors standalone Note 9) | — |
| 13 | 1036 | "Previous period/year numbers have been regrouped/reclassified wherever considered necessary" | — |
| 14 | 1038-1039 | "The aforesaid unaudited consolidated financial results are also available on the Company's website... and Stock Exchanges websites" | — |

### 8a. Note 10 sub-table — Additional standalone information disclosed within consolidated notes (line 1011-1019)
| Line item | Line# | Q1FY27 | Q4FY26 | Q1FY26 | FY26 |
|---|---|---|---|---|---|
| Total income | 1016 | 271.16 | 1,369.72 | 1,256.34 | 5,263.66 |
| Loss before tax | 1017 | (895.71) | (830.01) | (903.69) | (2,959.52) |
| Loss after tax | 1018 | (902.88) | (798.20) | (888.04) | (2,830.66) |
| Total comprehensive loss | 1019 | (902.88) | (797.85) | (888.04) | (2,818.20) |

Cross-check: this sub-table reconciles exactly with Section 4 (Standalone Financial
Results) lines 3, 12, 16, 19. No discrepancy found.

Consolidated results sign-off block (page 20, end of results statement): "For n.d on
behalf of Board of Directors... Managing Director, Place Bengaluru, Date: August 10,
2026" — line 1041-1049. Signatory name garbled/omitted by OCR. Flag: SIGNATORY_NAME_NOT_LEGIBLE.

---

## 9. CONSOLIDATED AUDITOR REVIEW REPORT (pages 13-14, lines 547-635)
Auditor: Agarwal Prakash & Co., Chartered Accountants, Firm Reg No. 005975N.

| Para | Line(s) | Type | Content | Flags |
|---|---|---|---|---|
| 1 | 554-563 | Scope/Introduction | Reviewed consolidated unaudited results of Holding Company, its subsidiaries, partnership firm, LLPs (together "the Group"), and its joint venture, per Annexure 1 entity list, for quarter ended 30 June 2026 | — |
| 2 | 565-571 | Management responsibility | Statement prepared per Ind AS 34, Holding Company management/Board responsibility; auditor expresses conclusion, not opinion | — |
| 3 | 573-586 | Review standard | Conducted per SRE 2410 plus SEBI Circular CIR/CFD/CMD1/44/2019 procedures under Reg 33(8); review substantially less in scope than audit; no audit opinion expressed | — |
| 4 | 588-602 | Conclusion (unmodified) | "nothing has come to our attention... has not disclosed the information required... or that it contains any material misstatement," based on own review plus other auditors' reports | Unmodified/clean conclusion overall |
| 5-intro | 604 | Other Matters — introduction | "The accompanying Statement includes the unaudited interim financial results, in respect of:" | OTHER_MATTERS |
| 5a | 606-609 | Other Matters — subsidiaries reviewed by other auditors | 35 entities: total revenue Rs 1,645.39m, total net loss after tax Rs (627.36)m, total comprehensive income Rs (627.36)m for the quarter | OTHER_AUDITOR_RELIANCE |
| 5b | 611-613 | Other Matters — joint venture reviewed by other auditor | 1 JV: Group's share of profit/(loss) after tax Rs 35.70m | OTHER_AUDITOR_RELIANCE |
| 5c | 615-617 | Other Matters — LLP reviewed by other auditor | 1 LLP: Group's share of profit/(loss) after tax Rs (0.03)m | OTHER_AUDITOR_RELIANCE |
| 5-mgmt-furnished | 619-624 | Other Matters — reliance basis | Reports on these entities furnished by management; conclusion based solely on other auditors' review reports and own procedures; conclusion not modified re: this reliance | UNAUDITED_MGMT_FURNISHED |
| 5-foreign | 626-635 | Other Matters — foreign subsidiaries | Certain of the above subsidiaries located outside India, prepared under local GAAP, reviewed by other auditor under local review standards; Holding Company management converted to Indian GAAP; auditor reviewed the conversion adjustments only | FOREIGN_SUBSIDIARY_CONVERSION |

Signature block: [Vikas Agarwal], Partner, Membership No. 097848, UDIN:
26097848CSAKTS237, Place: New Delhi, Date: 10 August 2026 — line 643-649. Same partner
as standalone report signed same date; UDIN differs (two separate UDINs for the two
reports, correct SEBI practice) — no flag.

---

## 10. ANNEXURE 1 — CONSOLIDATION ENTITY LIST (pages 15-17, lines 656-862)
183 named entities (S.No. 1-183) + 1 joint venture = 184 total, matching Note 1's stated
"184 subsidiaries/joint ventures." No prior-quarter ledger was supplied to this run
(PRIOR_LEDGER_PATH not injected), so an entity-by-entity ADD/REMOVE/RENAME diff against
Q4FY26 could not be mechanically performed; this list is captured as the baseline for
that diff in a future quarter. One in-period change is directly evidenced by this
filing's own text (entity #152, struck off during the quarter, and the strike-off of
"three non-operational subsidiaries plus one foreign subsidiary" per Note 7/8 above) =
flagged ENTITY_CHANGE. All entities default relationship type "Subsidiary" unless noted.

| S.No. | Entity name | Line range | Relationship / flags |
|---|---|---|---|
| 1-9 | Athena Land Development Ltd; Athena Builders and Developers Ltd; Athena Buildwell Ltd; Athena Infrastructure Ltd; Ceres Constructions Ltd; Ceres Estate Ltd; Ceres Infrastructure Ltd; Ceres Land Development Ltd; Ceres Properties Ltd | 657-670 | Subsidiary |
| 10-19 | Diana Infrastructure Ltd; Diana Land Development Ltd; Fama Infrastructure Ltd; Fama Properties Ltd; Equinox India Buildcon Ltd (fka Indiabulls Buildcon Ltd); Makala Infrastructure Ltd; Devona Constructions Ltd (fka Indiabulls Constructions Ltd); Equinox India Landcon Ltd (fka Indiabulls Lands Ltd); Ivonne Infrastructure Ltd; Bridget Estate Ltd (fka Indiabulls Estate Ltd) | 672-694 | Subsidiary; several renamed from "Indiabulls" legacy names |
| 20-29 | Equinox India Commercial Estate Ltd (fka Indiabulls Commercial Estate Ltd); Serida Engineering Ltd (fka Indiabulls Engineering Ltd); Equinox India Land Holdings Ltd (fka Indiabulls Land Holdings Ltd); Lavone Infrastructure Projects Ltd (fka Indiabulls Infrastructure Projects Ltd); Equinox India Commercial Properties Ltd (fka Indiabulls Commercial Properties Ltd); Manjola Infrastructure Ltd; Equinox India Infraestate Ltd (fka Indiabulls Infraestate Ltd); Juventus Constructions Ltd; Juventus Land Development Ltd; Lucina Land Development Ltd | 695-717 | Subsidiary; multiple renamed from "Indiabulls" legacy names |
| 30-40 | Nilgiri Infraestate Ltd; Nilgiri Infrastructure Development Ltd; Nilgiri Infrastructure Projects Ltd; Noble Realtors Ltd; Nilgiri Land Holdings Ltd; Nilgiti Lands Ltd; Nilgiti Land Development Ltd; Nilgiri Infrastructure Ltd; Selene Constructions Ltd; Selene Infrastructure Ltd; Selene Land Development Ltd | 658-678 | Subsidiary |
| 41-51 | Shivalik Properties Ltd; Sylvanus Properties Ltd; Triton Properties Ltd; Vindhyachal Land Development Ltd; Vindhyachal Infrastructure Ltd; Zeus Buildwell Ltd; Zeus Estate Ltd; Devona Properties Ltd; Sentia Real Estate Ltd; Sophia Real Estate Ltd; Sophia Constructions Ltd | 680-694 | Subsidiary |
| 52-67 | Albina Real Estate Ltd; Airmid Properties Ltd; Albasta Properties Ltd; Varali Constructions Ltd; Citra Properties Ltd; Apesh Properties Ltd; Corns Real Estate Ltd; Fornax Constructions Ltd; Lavone Management Services Ltd (fka IB Holdings Ltd); Elena Properties Ltd; Elena Constructions Ltd; Fornax Real Estate Ltd; Sentia Developers Ltd; Citra Developers Ltd; Devona Developers Ltd; Indiabulls Realty Company Ltd | 695-717 | Subsidiary |
| 68-79 | Indiabulls Projects Ltd; Lenus Properties Ltd; Sentia Infrastructure Ltd; Sepset Developers Ltd; Varali Infrastructure Ltd; Mariana Real Estate Ltd; Albasta Infrastructure Ltd; Albasta Real Estate Ltd; Angles Constructions Ltd; Lenus Infrastructure Ltd; Mariana Properties Ltd; Serida Properties Ltd | 725-750 | Subsidiary |
| 80-91 | Mabon Constructions Ltd; Mabon Infrastructure Ltd; Indiabulls Industrial Infrastructure Ltd; Varali Properties Ltd; Apesh Constructions Ltd; Equinox India Assets Ltd (fka IB Assets Ltd); Fama Builders and Developers Ltd; Juventus Infrastructure Ltd; Kailash Buildwell Ltd; Kaltha Developers Ltd; Nilgiri Buildwell Ltd; Serida Infrastructure Ltd | 752-775 | Subsidiary |
| 92-104 | Ashkit Constructions Ltd; Vonnie Real Estate Ltd; Fama Land Development Ltd; Amadis Land Development Ltd; Karakoram Buildwell Ltd; Karakoram Properties Ltd; Aedos Real Estate Company Ltd; Lucina Estate Ltd; Triton Infrastructure Ltd; Vindhyachal Buildwell Ltd; Zeus Builders and Developers Ltd; Paidia Infrastructure Ltd; Fama Estate Ltd | 777-800 | Subsidiary |
| 105-117 | Lucina Builders and Developers Ltd; Lorita Developers Ltd; Fama Construction Ltd; Lavone Builders and Developers Ltd; Juventus Properties Ltd; Lucina Buildwell Ltd; Lucina Properties Ltd; Selene Buildwell Ltd; Selene Properties Ltd; Tefia Land Development Ltd; Vindhyachal Developers Ltd; Zeus Properties Ltd; Varali Developers Ltd | 725-748 | Subsidiary |
| 118-134 | Platane Infrastructure Ltd; Triton Buildwell Ltd; Galium Builders and Developers Ltd; Linnet Infrastructure Ltd; Linnet Constructions Ltd; Linnet Developers Ltd; Linnet Real Estate Ltd; Linnet Properties Ltd; Edesia Constructions Ltd; Edesia Developers Ltd; Edesia Infrastructure Ltd; Lorena Developers Ltd; Lorena Builders Ltd; Lorena Infrastructure Ltd; Lorena Constructions Ltd; Lorena Real Estate Ltd; Parmida Properties Ltd | 750-780 | Subsidiary |
| 135-147 | Majesta Developers Ltd; Majesta Infrastructure Ltd; Majesta Builders Ltd; Majesta Properties Ltd; Majesta Constructions Ltd; Nerissa Infrastructure Ltd; Nerissa Real Estate Ltd; Nerissa Developers Ltd; Nerissa Properties Ltd; Nerissa Constructions Ltd; Fama Real Estate Ltd (fka Cobitis Real Estate Ltd); Tapir Constructions Ltd; Airmid Real Estate Ltd | 782-805 | Subsidiary |
| 148-158 | Kenneth Builders & Developers Ltd; Catherine Builders & Developers Ltd; Bridget Builders and Developers Ltd; Hermes Properties Ltd; Dev Property Development Ltd; Brenformexa Ltd; M Holdco 1 Ltd; M Holdco 2 Ltd; M Holdco 3 Ltd; Navilith Holdings Ltd; EMBDL - Employees Welfare Trust (fka Indiabulls Real Estate Ltd - Employees Welfare Trust) | 814-832 | #152 flagged ENTITY_CHANGE — "struck off on 26 May 2026" (per entity list itself); #158 is a Trust, not a company |
| 159-169 | Sky Forest Projects Ltd#; Spero Properties and Services Pvt Ltd; RGE Constructions and Development Ltd#; Vigor Developments Ltd#; Equinox Developments Ltd#; Sion Eden Developers Ltd#; Embassy One Developers Ltd#; Embassy Realty Ventures Ltd#; Embassy One Commercial Property Developments Ltd#; Embassy Orange Developers Ltd#; Embassy East Business Parks Ltd# | 833-848 | "#" entities changed status Private -> Public during FY26 (per footnote, line 818-822) |
| 170-181 | Basal Projects Ltd#; Embassy Infra Developers Ltd#; Ardor Projects Ltd#; Summit Developments Ltd#; Lotus Projects Ltd# (OCR: "Lo1n1s"); Cohort Projects Ltd#; Embassy International Riding School; Virtuous Developments Ltd#; Reque Developers Ltd#; Cereus Ventures Ltd#; Grove Ventures; Embassy Investment Management Services LLP | 849-862 | #181 is an LLP, not a company; #176/#180 have no "#" suffix (no Pvt->Public status change noted) |
| 182-183 | Upscarf Salon De Elegance LLP; Squadron Developers Ltd# | 814-815 | #182 is an LLP |
| JV-1 | Embassy-Columbia Pacific ASL Private Limited | 826-827 | Joint Venture (Group's share of P&L reported separately at Note 8/consolidated auditor para 5b) |

Footnote captured: "#Companies status has been changed from Private Limited to Public
Limited during the previous year ended 31 March 2026" — line 818-822. This is
historical (pre-quarter) context, not an in-quarter change; not flagged ENTITY_CHANGE.

---

## 11. DIGITAL SIGNATURE / TIMESTAMP BLOCKS

| # | Signatory | Designation | Timestamp | Line(s) | Flags |
|---|---|---|---|---|---|
| 1 | Vikas Khandelwal | Company Secretary | Digitally signed 2026.08.10 20:10:50 +05'30' | 131-137 | Signed ~2h40m after 05:30 PM board meeting conclusion — post-conclusion, no timing flag |
| 2 | Vikas Agarwal | Partner, Agarwal Prakash & Co. (standalone review report) | 10 August 2026, Place: New Delhi; UDIN 26097848GGMEHZ6100 | 394-401 | — |
| 3 | [Vikas Agarwal] | Partner, Agarwal Prakash & Co. (consolidated review report) | 10 August 2026, Place: New Delhi; UDIN 26097848CSAKTS237 | 643-649 | — |
| 4 | [name not legible — OCR] | Managing Director (standalone results sign-off) | August 10, 2026, Place: Bengaluru | 529-536 | SIGNATORY_NAME_NOT_LEGIBLE |
| 5 | [name not legible — OCR] | Managing Director (consolidated results sign-off) | August 10, 2026, Place: Bengaluru | 1041-1049 | SIGNATORY_NAME_NOT_LEGIBLE |

---

## 12. SUMMARY OF FLAGS RAISED
ZERO_STANDING (x7: Annexure A-4(iv) cancellation/termination field, standalone
Exceptional items, standalone OCI-Remeasurements, standalone Other equity, consolidated
Exceptional items, consolidated OCI-Remeasurements, consolidated Other equity) | CAPITAL_RAISE | RELATED_PARTY (x2) | CONCENTRATED_ALLOTTEE |
LEGAL_CONTINGENCY (x3: standalone STPL/CIRP note, consolidated STPL/CIRP note,
consolidated EEBPL/KIADB note) | SUBSEQUENT_EVENT (x3: NCD issuance x2, Scheme of
Amalgamation) | ENTITY_CHANGE (x2: strike-offs note, entity #152 struck-off-in-list) |
PENDING_APPROVAL | OTHER_MATTERS | OTHER_AUDITOR_RELIANCE (x3) |
UNAUDITED_MGMT_FURNISHED | FOREIGN_SUBSIDIARY_CONVERSION | OCR_GARBLED |
SIGNATORY_NAME_NOT_LEGIBLE (x2)

No prior-quarter ledger was available for this run; entity ADD/REMOVE/RENAME diff versus
Q4FY26 is deferred to the next quarter's A2 pass using this ledger as baseline.
