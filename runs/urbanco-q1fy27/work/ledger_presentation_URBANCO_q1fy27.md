# ENUMERATION LEDGER — URBANCO Q1 FY27 — Investor Presentation (Reg 30 Media Release, 5 pages)

Source: extract_presentation_URBANCO_q1fy27.txt (A1 extract). Doctype classified `presentation` per task instruction; content is the 5-page Reg 30 media release (no separate slide deck supplied).
Prior-quarter ledger: none available (first quarterly run for this ticker) — DROPPED_SLIDE check N/A, so noted.

=== A2 COUNT TEST ===
category: slides            grep_count: 5    sweep_count: 5    match: yes
category: numbers_on_slides grep_count: 158  sweep_count: 158  match: yes
category: spelled_out_numbers grep_count: 10  sweep_count: 10  match: yes
category: footnotes_qualifiers grep_count: 14 sweep_count: 14  match: yes
category: dropped_slides    grep_count: n/a  sweep_count: n/a  match: n/a (no prior-quarter ledger supplied)
category: zero_standing_items grep_count: 0  sweep_count: 0   match: yes (n/a — no financial tables in this doctype; narrative bullets only, all non-zero)
gate_a2: pass
=== END COUNT TEST ===

## METHOD NOTE
Grep pass 1 (slides): `grep -c '^\[page [0-9]+\]$'` on the extract file -> 5.
Grep pass 2 (numbers): `grep -noE '[0-9]+([,.][0-9]+)*%?'` applied within each page's line range (page1: L24-84, page2: L86-121, page3: L123-160, page4: L162-201, page5: L203-219), excluding the `[page N]` marker lines themselves and the A1 header/method-note block (L1-22) -> 158 numeric tokens.
Grep pass 3 (spelled-out number words): `grep -noiE '\b(one|two|three|four|five|six|seven|eight|nine|ten|first|second|third|fourth|fifth)\b'` within L24-219 -> 10 hits (one of which, L114, falls inside an A1 extraction annotation bracket, not source content — flagged, not dropped).
Manual sweep: independent line-by-line read of all 5 pages, re-deriving the same 158 numeric tokens, 10 spelled-out-number hits, and 14 footnote/qualifier instances by inspection; cross-checked token-for-token against the grep lists above. All three counts reconciled -> GATE A2 pass.

## TABLE 1 — SLIDES / PAGES (5 total)

| Slide/Page # | Line range | Title / heading | Content type | Flags |
|---|---|---|---|---|
| 1 | L24-84 | Regulation 30 covering letter to NSE / BSE + registered/corporate office block + digital signature | text (letter) + signature block | PRIOR_LEDGER_UNAVAILABLE |
| 2 | L86-121 | Media release headline + sub-bullets + opening paragraph + Q1 FY27 SNAPSHOT tile row | text (headline/bullets/paragraph) + tile block (TILE) |  |
| 3 | L123-160 | Key performance highlights: Consolidated, India Consumer Services (Ex InstaHelp), International, Native, InstaHelp | text (bulleted segment highlights) |  |
| 4 | L162-201 | About Urban Company Limited + Safe Harbour Statement | text (company profile paragraph) + text (legal disclaimer) |  |
| 5 | L203-219 | Disclaimer continuation (summary-form notice, no-advice / no-offer notice) | text (legal disclaimer, continued) |  |

## TABLE 2 — EVERY NUMBER ON EVERY SLIDE (158 rows; grep-count == manual-sweep-count == 158)

| # | Page | Line | Value | Context (verbatim line, trimmed) | Flags |
|---|---|---|---|---|---|
| 1 | 1 | 24 | 31 | July 31, 2026 | ADMIN_REGULATORY |
| 2 | 1 | 24 | 2026 | July 31, 2026 | ADMIN_REGULATORY |
| 3 | 1 | 30 | 400 | Mumbai - 400 051                                           Mumbai - 400 001 | ADMIN_REGULATORY |
| 4 | 1 | 30 | 051 | Mumbai - 400 051                                           Mumbai - 400 001 | ADMIN_REGULATORY |
| 5 | 1 | 30 | 400 | Mumbai - 400 051                                           Mumbai - 400 001 | ADMIN_REGULATORY |
| 6 | 1 | 30 | 001 | Mumbai - 400 051                                           Mumbai - 400 001 | ADMIN_REGULATORY |
| 7 | 1 | 32 | 544515 | Symbol: URBANCO                                            Scrip Code: 544515 | ADMIN_REGULATORY |
| 8 | 1 | 34 | 30 | Sub.: Disclosure under Regulation 30 of the SEBI (Listing Obligations and Disclosure | ADMIN_REGULATORY |
| 9 | 1 | 35 | 2015 | Requirements) Regulations, 2015 – Media Release | ADMIN_REGULATORY |
| 10 | 1 | 39 | 30 | In compliance with Regulation 30 and other applicable provisions of the SEBI (Listing Obligations... | ADMIN_REGULATORY |
| 11 | 1 | 40 | 2015 | Disclosure Requirements) Regulations, 2015, as amended, please find enclosed the media release | ADMIN_REGULATORY |
| 12 | 1 | 41 | 30 | on the financial results (standalone and consolidated) of the Company for the quarter ended June 30, | ADMIN_REGULATORY |
| 13 | 1 | 42 | 2026 | 2026. | ADMIN_REGULATORY |
| 14 | 1 | 58 | 2026.07.31 | SINGH Date:  2026.07.31 | SIGNATURE_TIMESTAMP |
| 15 | 1 | 59 | 16 | 16:05:19 +05'30' | SIGNATURE_TIMESTAMP |
| 16 | 1 | 59 | 05 | 16:05:19 +05'30' | SIGNATURE_TIMESTAMP |
| 17 | 1 | 59 | 19 | 16:05:19 +05'30' | SIGNATURE_TIMESTAMP |
| 18 | 1 | 59 | 05 | 16:05:19 +05'30' | SIGNATURE_TIMESTAMP |
| 19 | 1 | 59 | 30 | 16:05:19 +05'30' | SIGNATURE_TIMESTAMP |
| 20 | 1 | 62 | 26585 | Membership No.: A26585 | IDENTIFIER |
| 21 | 1 | 75 | 8 | Unit No. 8, Ground Floor, | ADDRESS |
| 22 | 1 | 76 | 7 | 7th & 8th Floor, Go Works, | ADDRESS |
| 23 | 1 | 76 | 8 | 7th & 8th Floor, Go Works, | ADDRESS |
| 24 | 1 | 77 | 1 | Rectangle 1, D4, Saket District Centre, | ADDRESS |
| 25 | 1 | 77 | 4 | Rectangle 1, D4, Saket District Centre, | ADDRESS |
| 26 | 1 | 78 | 183 | Plot 183, Rajiv Nagar, Udyog Vihar | ADDRESS |
| 27 | 1 | 79 | 110017 | New Delhi, 110017, Delhi, India | ADDRESS |
| 28 | 1 | 80 | 1 | Phase 1, Sector 20, | ADDRESS |
| 29 | 1 | 80 | 20 | Phase 1, Sector 20, | ADDRESS |
| 30 | 1 | 81 | 122016 | Gurgaon - 122016, Haryana, India | ADDRESS |
| 31 | 1 | 84 | 74140 | CIN: L74140DL2014PLC274413 / Email: Peoplesuccess@urbancompany.com/ www.urbancompany.com / Teleph... | IDENTIFIER |
| 32 | 1 | 84 | 2014 | CIN: L74140DL2014PLC274413 / Email: Peoplesuccess@urbancompany.com/ www.urbancompany.com / Teleph... | IDENTIFIER |
| 33 | 1 | 84 | 274413 | CIN: L74140DL2014PLC274413 / Email: Peoplesuccess@urbancompany.com/ www.urbancompany.com / Teleph... | IDENTIFIER |
| 34 | 1 | 84 | 91 | CIN: L74140DL2014PLC274413 / Email: Peoplesuccess@urbancompany.com/ www.urbancompany.com / Teleph... | IDENTIFIER |
| 35 | 1 | 84 | 11 | CIN: L74140DL2014PLC274413 / Email: Peoplesuccess@urbancompany.com/ www.urbancompany.com / Teleph... | IDENTIFIER |
| 36 | 1 | 84 | 444 | CIN: L74140DL2014PLC274413 / Email: Peoplesuccess@urbancompany.com/ www.urbancompany.com / Teleph... | IDENTIFIER |
| 37 | 1 | 84 | 570 | CIN: L74140DL2014PLC274413 / Email: Peoplesuccess@urbancompany.com/ www.urbancompany.com / Teleph... | IDENTIFIER |
| 38 | 1 | 84 | 56 | CIN: L74140DL2014PLC274413 / Email: Peoplesuccess@urbancompany.com/ www.urbancompany.com / Teleph... | IDENTIFIER |
| 39 | 2 | 86 | 44% | Urban Company posts 44% revenue growth (highest in 16 quarters); | HEADLINE_METRIC |
| 40 | 2 | 86 | 16 | Urban Company posts 44% revenue growth (highest in 16 quarters); | HEADLINE_METRIC |
| 41 | 2 | 87 | 33% | Adjusted EBITDA loss shrinks QoQ by 33%; Adjusted EBITDA (Ex InstaHelp) | HEADLINE_METRIC; EX_INSTAHELP_QUALIFIER |
| 42 | 2 | 88 | 67 | more than doubles YoY to ₹67 Cr | HEADLINE_METRIC; EX_INSTAHELP_QUALIFIER |
| 43 | 2 | 90 | 29% | ●​ India Consumer Services (Ex InstaHelp) records 29% YoY NTV growth with | HEADLINE_METRIC |
| 44 | 2 | 91 | 6.9% | 6.9% Adjusted EBITDA margins (170 bps improvement YoY) | HEADLINE_METRIC |
| 45 | 2 | 91 | 170 | 6.9% Adjusted EBITDA margins (170 bps improvement YoY) | HEADLINE_METRIC |
| 46 | 2 | 92 | 76% | ●​ International business NTV grew 76% YoY, emerging as a second profit | HEADLINE_METRIC |
| 47 | 2 | 94 | 60% | ●​ Native Net Revenue grew by 60% to ₹95 Cr., while Adjusted EBITDA margins | HEADLINE_METRIC |
| 48 | 2 | 94 | 95 | ●​ Native Net Revenue grew by 60% to ₹95 Cr., while Adjusted EBITDA margins | HEADLINE_METRIC |
| 49 | 2 | 95 | 410 | improved by 410 bps YoY | HEADLINE_METRIC |
| 50 | 2 | 96 | 98 | ●​ Consolidated Adjusted EBITDA loss shrinks QoQ from ₹(98) Cr. in Q4 FY26 to | HEADLINE_METRIC |
| 51 | 2 | 96 | 4 | ●​ Consolidated Adjusted EBITDA loss shrinks QoQ from ₹(98) Cr. in Q4 FY26 to | HEADLINE_METRIC |
| 52 | 2 | 96 | 26 | ●​ Consolidated Adjusted EBITDA loss shrinks QoQ from ₹(98) Cr. in Q4 FY26 to | HEADLINE_METRIC |
| 53 | 2 | 97 | 65 | ₹(65) Cr. in Q1 FY27 | HEADLINE_METRIC |
| 54 | 2 | 97 | 1 | ₹(65) Cr. in Q1 FY27 | HEADLINE_METRIC |
| 55 | 2 | 97 | 27 | ₹(65) Cr. in Q1 FY27 | HEADLINE_METRIC |
| 56 | 2 | 98 | 116% | ●​ Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26 | HEADLINE_METRIC; EX_INSTAHELP_QUALIFIER; INTERNAL_INCONSISTENCY_SEE_O1 |
| 57 | 2 | 98 | 67 | ●​ Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26 | HEADLINE_METRIC; EX_INSTAHELP_QUALIFIER; INTERNAL_INCONSISTENCY_SEE_O1 |
| 58 | 2 | 98 | 1 | ●​ Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26 | HEADLINE_METRIC; EX_INSTAHELP_QUALIFIER; INTERNAL_INCONSISTENCY_SEE_O1 |
| 59 | 2 | 98 | 26 | ●​ Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26 | HEADLINE_METRIC; EX_INSTAHELP_QUALIFIER; INTERNAL_INCONSISTENCY_SEE_O1 |
| 60 | 2 | 101 | 31 | Gurugram, July 31, 2026: Urban Company Limited (NSE: URBANCO), India's leading home | BODY_METRIC |
| 61 | 2 | 101 | 2026 | Gurugram, July 31, 2026: Urban Company Limited (NSE: URBANCO), India's leading home | BODY_METRIC |
| 62 | 2 | 102 | 30 | services platform, today announced its financial results for the quarter ended June 30, 2026 (Q1 | BODY_METRIC |
| 63 | 2 | 102 | 2026 | services platform, today announced its financial results for the quarter ended June 30, 2026 (Q1 | BODY_METRIC |
| 64 | 2 | 102 | 1 | services platform, today announced its financial results for the quarter ended June 30, 2026 (Q1 | BODY_METRIC |
| 65 | 2 | 103 | 27 | FY27). Urban Company delivered one of its strongest quarters, with broad-based growth across | BODY_METRIC |
| 66 | 2 | 105 | 42% | (NTV) grew 42% YoY to ₹1,465 crore, while revenue from operations increased 44% YoY to ₹528 | BODY_METRIC |
| 67 | 2 | 105 | 1,465 | (NTV) grew 42% YoY to ₹1,465 crore, while revenue from operations increased 44% YoY to ₹528 | BODY_METRIC |
| 68 | 2 | 105 | 44% | (NTV) grew 42% YoY to ₹1,465 crore, while revenue from operations increased 44% YoY to ₹528 | BODY_METRIC |
| 69 | 2 | 105 | 528 | (NTV) grew 42% YoY to ₹1,465 crore, while revenue from operations increased 44% YoY to ₹528 | BODY_METRIC |
| 70 | 2 | 106 | 13.2 | crore. The Company delivered 13.2 million orders during the quarter, an increase of 79% YoY. | BODY_METRIC |
| 71 | 2 | 106 | 79% | crore. The Company delivered 13.2 million orders during the quarter, an increase of 79% YoY. | BODY_METRIC |
| 72 | 2 | 107 | 1.2 | Further, the Company added approximately 1.2 million new users, making it the first-ever | BODY_METRIC |
| 73 | 2 | 109 | 98 | QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. Excluding the investments in InstaHelp, | BODY_METRIC; EX_INSTAHELP_QUALIFIER |
| 74 | 2 | 109 | 4 | QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. Excluding the investments in InstaHelp, | BODY_METRIC; EX_INSTAHELP_QUALIFIER |
| 75 | 2 | 109 | 26 | QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. Excluding the investments in InstaHelp, | BODY_METRIC; EX_INSTAHELP_QUALIFIER |
| 76 | 2 | 109 | 65 | QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. Excluding the investments in InstaHelp, | BODY_METRIC; EX_INSTAHELP_QUALIFIER |
| 77 | 2 | 109 | 1 | QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. Excluding the investments in InstaHelp, | BODY_METRIC; EX_INSTAHELP_QUALIFIER |
| 78 | 2 | 109 | 27 | QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. Excluding the investments in InstaHelp, | BODY_METRIC; EX_INSTAHELP_QUALIFIER |
| 79 | 2 | 110 | 116% | Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26 | BODY_METRIC; EX_INSTAHELP_QUALIFIER; INTERNAL_INCONSISTENCY_SEE_O2 |
| 80 | 2 | 110 | 67 | Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26 | BODY_METRIC; EX_INSTAHELP_QUALIFIER; INTERNAL_INCONSISTENCY_SEE_O2 |
| 81 | 2 | 110 | 1 | Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26 | BODY_METRIC; EX_INSTAHELP_QUALIFIER; INTERNAL_INCONSISTENCY_SEE_O2 |
| 82 | 2 | 110 | 26 | Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26 | BODY_METRIC; EX_INSTAHELP_QUALIFIER; INTERNAL_INCONSISTENCY_SEE_O2 |
| 83 | 2 | 114 | 2 | [TILE, page 2, native pdftotext -layout text (no OCR needed; pdfimages confirmed no raster chart/... | EXTRACTION_ANNOTATION_NOT_SOURCE_CONTENT |
| 84 | 2 | 115 | 1 | Q1 FY27 SNAPSHOT | SNAPSHOT_TILE |
| 85 | 2 | 115 | 27 | Q1 FY27 SNAPSHOT | SNAPSHOT_TILE |
| 86 | 2 | 117 | 1,465 | ₹1,465 Cr                 ₹528 Cr                 1.2M+                   ₹67 Cr | SNAPSHOT_TILE |
| 87 | 2 | 117 | 528 | ₹1,465 Cr                 ₹528 Cr                 1.2M+                   ₹67 Cr | SNAPSHOT_TILE |
| 88 | 2 | 117 | 1.2 | ₹1,465 Cr                 ₹528 Cr                 1.2M+                   ₹67 Cr | SNAPSHOT_TILE |
| 89 | 2 | 117 | 67 | ₹1,465 Cr                 ₹528 Cr                 1.2M+                   ₹67 Cr | SNAPSHOT_TILE |
| 90 | 2 | 118 | 42% | +42% YoY                +44% YoY            First-ever quarter         4.8% of NTV | SNAPSHOT_TILE |
| 91 | 2 | 118 | 44% | +42% YoY                +44% YoY            First-ever quarter         4.8% of NTV | SNAPSHOT_TILE |
| 92 | 2 | 118 | 4.8% | +42% YoY                +44% YoY            First-ever quarter         4.8% of NTV | SNAPSHOT_TILE |
| 93 | 2 | 119 | 1 | NTV                 Net Revenue           with > 1 mn new           Adj. EBITDA | SNAPSHOT_TILE |
| 94 | 2 | 121 | 16 | 16 quarters) | SNAPSHOT_TILE |
| 95 | 3 | 125 | 42% | ●​ NTV: grew 42% YoY to ₹1,465 Cr., with broad-based acceleration across India Consumer | SEGMENT_METRIC |
| 96 | 3 | 125 | 1,465 | ●​ NTV: grew 42% YoY to ₹1,465 Cr., with broad-based acceleration across India Consumer | SEGMENT_METRIC |
| 97 | 3 | 127 | 44% | ●​ Revenue from operations: Up 44% YoY to ₹528 Cr. | SEGMENT_METRIC |
| 98 | 3 | 127 | 528 | ●​ Revenue from operations: Up 44% YoY to ₹528 Cr. | SEGMENT_METRIC |
| 99 | 3 | 128 | 98 | ●​ Adjusted EBITDA: Loss reduced QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. | SEGMENT_METRIC |
| 100 | 3 | 128 | 4 | ●​ Adjusted EBITDA: Loss reduced QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. | SEGMENT_METRIC |
| 101 | 3 | 128 | 26 | ●​ Adjusted EBITDA: Loss reduced QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. | SEGMENT_METRIC |
| 102 | 3 | 128 | 65 | ●​ Adjusted EBITDA: Loss reduced QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. | SEGMENT_METRIC |
| 103 | 3 | 128 | 1 | ●​ Adjusted EBITDA: Loss reduced QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. | SEGMENT_METRIC |
| 104 | 3 | 128 | 27 | ●​ Adjusted EBITDA: Loss reduced QoQ from ₹(98) Cr. in Q4 FY26 to ₹(65) Cr. in Q1 FY27. | SEGMENT_METRIC |
| 105 | 3 | 129 | 132 | This loss was largely driven by a ₹(132) Cr. Adjusted EBITDA loss in InstaHelp. Excluding | SEGMENT_METRIC; LOSS_DRIVER_QUALIFIER; EX_INSTAHELP_QUALIFIER |
| 106 | 3 | 130 | 67 | InstaHelp, the business generated an Adjusted EBITDA profit of ₹67 Cr., or 4.8% of NTV, | SEGMENT_METRIC; EX_INSTAHELP_QUALIFIER |
| 107 | 3 | 130 | 4.8% | InstaHelp, the business generated an Adjusted EBITDA profit of ₹67 Cr., or 4.8% of NTV, | SEGMENT_METRIC; EX_INSTAHELP_QUALIFIER |
| 108 | 3 | 131 | 31 | more than double the ₹31 Cr. delivered in Q1 FY26. | SEGMENT_METRIC |
| 109 | 3 | 131 | 1 | more than double the ₹31 Cr. delivered in Q1 FY26. | SEGMENT_METRIC |
| 110 | 3 | 131 | 26 | more than double the ₹31 Cr. delivered in Q1 FY26. | SEGMENT_METRIC |
| 111 | 3 | 134 | 29% | ●​ NTV: grew 29% YoY to ₹1,056 Cr. — the fourth consecutive quarter of accelerating | SEGMENT_METRIC |
| 112 | 3 | 134 | 1,056 | ●​ NTV: grew 29% YoY to ₹1,056 Cr. — the fourth consecutive quarter of accelerating | SEGMENT_METRIC |
| 113 | 3 | 135 | 10% | growth (10% → 19% → 21% → 26% → 29%). | SEGMENT_METRIC; GROWTH_LADDER |
| 114 | 3 | 135 | 19% | growth (10% → 19% → 21% → 26% → 29%). | SEGMENT_METRIC; GROWTH_LADDER |
| 115 | 3 | 135 | 21% | growth (10% → 19% → 21% → 26% → 29%). | SEGMENT_METRIC; GROWTH_LADDER |
| 116 | 3 | 135 | 26% | growth (10% → 19% → 21% → 26% → 29%). | SEGMENT_METRIC; GROWTH_LADDER |
| 117 | 3 | 135 | 29% | growth (10% → 19% → 21% → 26% → 29%). | SEGMENT_METRIC; GROWTH_LADDER |
| 118 | 3 | 136 | 73 | ●​ Adjusted EBITDA: ₹73 Cr., or 6.9% of NTV, compared to 5.2% of NTV in Q1 FY26. | SEGMENT_METRIC |
| 119 | 3 | 136 | 6.9% | ●​ Adjusted EBITDA: ₹73 Cr., or 6.9% of NTV, compared to 5.2% of NTV in Q1 FY26. | SEGMENT_METRIC |
| 120 | 3 | 136 | 5.2% | ●​ Adjusted EBITDA: ₹73 Cr., or 6.9% of NTV, compared to 5.2% of NTV in Q1 FY26. | SEGMENT_METRIC |
| 121 | 3 | 136 | 1 | ●​ Adjusted EBITDA: ₹73 Cr., or 6.9% of NTV, compared to 5.2% of NTV in Q1 FY26. | SEGMENT_METRIC |
| 122 | 3 | 136 | 26 | ●​ Adjusted EBITDA: ₹73 Cr., or 6.9% of NTV, compared to 5.2% of NTV in Q1 FY26. | SEGMENT_METRIC |
| 123 | 3 | 137 | 21% | ●​ Annual transacting users grew ~21% YoY to ~8.2 million and spend per annual | SEGMENT_METRIC |
| 124 | 3 | 137 | 8.2 | ●​ Annual transacting users grew ~21% YoY to ~8.2 million and spend per annual | SEGMENT_METRIC |
| 125 | 3 | 138 | 7% | transacting user rose ~7% YoY, compounding into 29% YoY NTV growth. | SEGMENT_METRIC |
| 126 | 3 | 138 | 29% | transacting user rose ~7% YoY, compounding into 29% YoY NTV growth. | SEGMENT_METRIC |
| 127 | 3 | 139 | 2 | ●​ Tier 2 cities (beyond the top 10 metros) grew NTV 36.2% YoY, outpacing 28.7% growth in | SEGMENT_METRIC |
| 128 | 3 | 139 | 10 | ●​ Tier 2 cities (beyond the top 10 metros) grew NTV 36.2% YoY, outpacing 28.7% growth in | SEGMENT_METRIC |
| 129 | 3 | 139 | 36.2% | ●​ Tier 2 cities (beyond the top 10 metros) grew NTV 36.2% YoY, outpacing 28.7% growth in | SEGMENT_METRIC |
| 130 | 3 | 139 | 28.7% | ●​ Tier 2 cities (beyond the top 10 metros) grew NTV 36.2% YoY, outpacing 28.7% growth in | SEGMENT_METRIC |
| 131 | 3 | 140 | 10 | the top 10 cities, and continue to contribute a rising share of new customers. | SEGMENT_METRIC |
| 132 | 3 | 143 | 76% | ●​ NTV: Grew 76% YoY to ₹237 Cr. (58% YoY in constant currency), despite temporary | SEGMENT_METRIC; CONSTANT_CURRENCY_QUALIFIER |
| 133 | 3 | 143 | 237 | ●​ NTV: Grew 76% YoY to ₹237 Cr. (58% YoY in constant currency), despite temporary | SEGMENT_METRIC; CONSTANT_CURRENCY_QUALIFIER |
| 134 | 3 | 143 | 58% | ●​ NTV: Grew 76% YoY to ₹237 Cr. (58% YoY in constant currency), despite temporary | SEGMENT_METRIC; CONSTANT_CURRENCY_QUALIFIER |
| 135 | 3 | 146 | 135% | ●​ KSA joint venture (Waed, with SMASCO): NTV grew 135% YoY to ₹77 Cr. | SEGMENT_METRIC |
| 136 | 3 | 146 | 77 | ●​ KSA joint venture (Waed, with SMASCO): NTV grew 135% YoY to ₹77 Cr. | SEGMENT_METRIC |
| 137 | 3 | 149 | 60% | ●​ Net Revenue: Grew 60% YoY to ₹95 Cr. | SEGMENT_METRIC |
| 138 | 3 | 149 | 95 | ●​ Net Revenue: Grew 60% YoY to ₹95 Cr. | SEGMENT_METRIC |
| 139 | 3 | 150 | 9 | ●​ Adjusted EBITDA: ₹(9) Cr., with loss margins narrowing to (7.3)% of NTV from (11.4)% a | SEGMENT_METRIC |
| 140 | 3 | 150 | 7.3 | ●​ Adjusted EBITDA: ₹(9) Cr., with loss margins narrowing to (7.3)% of NTV from (11.4)% a | SEGMENT_METRIC |
| 141 | 3 | 150 | 11.4 | ●​ Adjusted EBITDA: ₹(9) Cr., with loss margins narrowing to (7.3)% of NTV from (11.4)% a | SEGMENT_METRIC |
| 142 | 3 | 152 | 3 | ●​ Launched two new products during the quarter: Native M3 Pro, a water purifier | SEGMENT_METRIC; PRODUCT_SPEC |
| 143 | 3 | 157 | 43% | ●​ Scale: Orders grew 43% QoQ to 3.82 million, with NTV reaching ₹53 Cr., up 32% QoQ. | SEGMENT_METRIC |
| 144 | 3 | 157 | 3.82 | ●​ Scale: Orders grew 43% QoQ to 3.82 million, with NTV reaching ₹53 Cr., up 32% QoQ. | SEGMENT_METRIC |
| 145 | 3 | 157 | 53 | ●​ Scale: Orders grew 43% QoQ to 3.82 million, with NTV reaching ₹53 Cr., up 32% QoQ. | SEGMENT_METRIC |
| 146 | 3 | 157 | 32% | ●​ Scale: Orders grew 43% QoQ to 3.82 million, with NTV reaching ₹53 Cr., up 32% QoQ. | SEGMENT_METRIC |
| 147 | 3 | 158 | 346 | ●​ Unit economics: Adjusted EBITDA loss per order improved to ₹(346), from ₹(447) in Q4 | SEGMENT_METRIC |
| 148 | 3 | 158 | 447 | ●​ Unit economics: Adjusted EBITDA loss per order improved to ₹(346), from ₹(447) in Q4 | SEGMENT_METRIC |
| 149 | 3 | 158 | 4 | ●​ Unit economics: Adjusted EBITDA loss per order improved to ₹(346), from ₹(447) in Q4 | SEGMENT_METRIC |
| 150 | 3 | 159 | 26 | FY26, driven by network densification. | SEGMENT_METRIC |
| 151 | 3 | 160 | 132 | ●​ P&L: Adjusted EBITDA loss of ₹(132) Cr. for the quarter. | SEGMENT_METRIC |
| 152 | 4 | 167 | 9 | repairs to salon and spa services. As per Urban Company’s 9M FY26 Earnings Index, | COMPANY_PROFILE_METRIC; EARNINGS_INDEX_BASIS_QUALIFIER |
| 153 | 4 | 167 | 26 | repairs to salon and spa services. As per Urban Company’s 9M FY26 Earnings Index, | COMPANY_PROFILE_METRIC; EARNINGS_INDEX_BASIS_QUALIFIER |
| 154 | 4 | 168 | 28,322 | average monthly net earnings in-hand reached INR 28,322 for all active service | COMPANY_PROFILE_METRIC |
| 155 | 4 | 169 | 5% | professionals (ex. InstaHelp), while the top 5% of service professionals earned INR 51,673. | COMPANY_PROFILE_METRIC |
| 156 | 4 | 169 | 51,673 | professionals (ex. InstaHelp), while the top 5% of service professionals earned INR 51,673. | COMPANY_PROFILE_METRIC |
| 157 | 4 | 171 | 10 | insurance, which includes life insurance cover of up to INR 10 lacs, disability cover of up to | COMPANY_PROFILE_METRIC |
| 158 | 4 | 172 | 6 | INR 6 lacs, as well as accidental hospitalisation and OPD treatment coverage, among other | COMPANY_PROFILE_METRIC |

## TABLE 3 — SPELLED-OUT NUMBER WORDS (10 rows; grep-count == manual-sweep-count == 10)

| # | Line | Word | Context | Flags |
|---|---|---|---|---|
| 1 | 92 | second | "emerging as a second profit engine for UC" — ordinal descriptor, International segment |  |
| 2 | 103 | one | "delivered one of its strongest quarters" — idiomatic usage, not a discrete metric |  |
| 3 | 107 | first | "the first-ever quarter" — ordinal, milestone claim (new-user acquisition) |  |
| 4 | 108 | one | "to cross one million new users acquired" — milestone threshold, distinct from the '1.2 million' figure |  |
| 5 | 114 | four | "four-tile snapshot row" — A1 EXTRACTION ANNOTATION bracket, NOT source document content | EXTRACTION_ANNOTATION_NOT_SOURCE_CONTENT |
| 6 | 118 | First | "First-ever quarter" — SNAPSHOT tile caption, repeats L107 claim |  |
| 7 | 134 | fourth | "the fourth consecutive quarter of accelerating growth" — ordinal, India Consumer Services NTV streak |  |
| 8 | 152 | two | "Launched two new products during the quarter" — Native segment |  |
| 9 | 153 | three | "a three-year maintenance-free life" — Native M3 Pro product spec |  |
| 10 | 154 | two | "two-way video calling" — Lock Ultra product spec |  |

## TABLE 4 — FOOTNOTES / FINE-PRINT DISCLAIMERS QUALIFYING A HEADLINE NUMBER (14 rows)

| ID | Line(s) | Footnote / qualifier text | What it qualifies |
|---|---|---|---|
| F1 | 87-88 | "(Ex InstaHelp)" in headline "Adjusted EBITDA (Ex InstaHelp) more than doubles YoY to ₹67 Cr" | qualifies the ₹67 Cr headline figure |
| F2 | 90-91 | "India Consumer Services (Ex InstaHelp) records 29% YoY NTV growth with 6.9% Adjusted EBITDA margins" | qualifies the 29%/6.9% bullet figures |
| F3 | 98 | "Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26" | qualifies ₹67 Cr / 116% — also see O1 (period-label inconsistency) |
| F4 | 109-110 | "Excluding the investments in InstaHelp, Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26" | qualifies ₹67 Cr / 116% — also see O2 (period-label inconsistency) |
| F5 | 120 | "(Ex-InstaHelp)" tile sub-caption under the 4th SNAPSHOT tile | qualifies tile figures ₹67 Cr / 4.8% of NTV |
| F6 | 129 | "This loss was largely driven by a ₹(132) Cr. Adjusted EBITDA loss in InstaHelp" | explanatory qualifier of the consolidated ₹(65) Cr loss (L128) |
| F7 | 129-130 | "Excluding [wraps to L130] InstaHelp, the business generated an Adjusted EBITDA profit of ₹67 Cr., or 4.8% of NTV" | qualifies the ₹67 Cr / 4.8% figure; phrase wraps across the L129/L130 line break |
| F8 | 133 | "India Consumer Services (Ex InstaHelp)" section header | qualifies the entire segment block L134-140 |
| F9 | 143-144 | "(58% YoY in constant currency)" qualifying "NTV: Grew 76% YoY to ₹237 Cr." | qualifies the 76% YoY International NTV headline growth figure |
| F10 | 167 | "As per Urban Company's 9M FY26 Earnings Index" — methodology-basis footnote | qualifies INR 28,322 (L168) and INR 51,673 (L169) earnings figures |
| F11 | 175-192 | Safe Harbour Statement (heading L175 + full paragraph) | blanket qualifier on all forward-looking statements/estimates in the release |
| F12 | 194-201 | Second disclaimer paragraph ("Any investment in securities...will also involve certain risks...") | blanket investment-risk / no-update-obligation qualifier |
| F13 | 203-208 | Page-5 disclaimer paragraph 1 ("information in this document is in summary form. No representation, warranty...") | blanket accuracy/adequacy disclaimer |
| F14 | 210-219 | Page-5 disclaimer paragraph 2 ("This document should not be construed as legal, tax, investment or other advice...") | blanket no-advice / no-offer / no-solicitation qualifier |

## TABLE 5 — INTERNAL INCONSISTENCY OBSERVATIONS (plain enumerated observations, not interpretation)

| ID | Line | Observation |
|---|---|---|
| O1 | 98 | Bullet reads "Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26." The period label reads "Q1 FY26." Elsewhere the same ₹67 Cr figure is labelled as the current-quarter (Q1 FY27) result: the SNAPSHOT tile at L115-120 is headed "Q1 FY27 SNAPSHOT" and shows ₹67 Cr under "Adj. EBITDA (Ex-InstaHelp)"; and L130-131 states the business "generated an Adjusted EBITDA profit of ₹67 Cr...more than double the ₹31 Cr. delivered in Q1 FY26," which assigns ₹31 Cr (not ₹67 Cr) to Q1 FY26. Flag: INTERNAL_INCONSISTENCY (period label on L98). |
| O2 | 110 | Identical wording to O1 repeats in the opening body paragraph: "Adjusted EBITDA (Ex InstaHelp) grew 116% YoY to reach ₹67 Cr. in Q1 FY26." Same period-label question as O1. Flag: INTERNAL_INCONSISTENCY (period label on L110). |

## TABLE 6 — DROPPED_SLIDE CHECK

Prior-quarter ledger path: none available (first quarterly run for this ticker). DROPPED_SLIDE comparison is N/A this cycle — noted per instruction rather than silently omitted.

## TABLE 7 — ZERO_STANDING CHECK

This doctype (Reg 30 media release / presentation) contains no financial statement tables (no balance sheet, P&L, or note-schedule grid) — all figures appear as narrative headline/bullet metrics. Rule 2 ("every line item in every financial table, including zero/nil/dash items") therefore has no applicable table to sweep. 0 zero-standing line items found; category marked N/A rather than silently dropped.
