# A5 ADVERSARY / COMPLETENESS AUDIT: SUPREMEPWR (Supreme Power Equipment Limited), H1 FY27 results

Auditor: A5 (claude-opus-5-5). Audit date: 2026-10-17.
Inputs read: A4 review (runs/supremepwr-h1fy27/work/review_supremepwr_h1fy27.md, 659 lines), A1 fulltext (1,193 lines), A1 structured (R001-R554), A2 ledger.
Not opened: source PDF, inputs/, A3 notes, orchestrator material.
Anchors: "FT L###" = A1 fulltext line. "A4 L###" = review line. "LG L###" = ledger line. "R###" = structured row. All money in Rs Lakhs unless marked Cr (1 Cr = 100 lakh).

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT (A4 L559-564, five paragraphs, about 215 words, inside the 200-400 word band) | sector PRESENT (A4 L566-570) | business model PRESENT (A4 L572-576) | competition PRESENT (A4 L578-582) | forward map PRESENT (A4 L584-590, six catalysts, each with a bull and a bear fork; four dated, two ND by filing). Gate: PASS. No placeholder text in any part.

---

## 1. COVERAGE AUDIT

Method. I ran my own pass over the A1 fulltext, statement by statement: SA P&L FT L874-912 (with primary text FT L150-203), SA BS FT L917-957 (FT L205-272), SA CF FT L966-1020 (FT L341-404), CON P&L FT L1028-1089 (FT L502-577), CON BS FT L1094-1137 (FT L579-637), CON CF FT L1144-1186 (FT L709-777), notes FT L293-330 and FT L656-696, auditor reports FT L69-148 and FT L414-500, outcome letter FT L18-67, certificate FT L788-872. I diffed the result against LG L3-288. Then I grepped A4 for every R-ID, every fulltext line anchor and every quoted value, and tested each ledger row for a citation or a "reviewed, no finding" mark.

| Category | A2 count | My fresh count | Orphan ledger rows (absent from A4) | Status |
|---|---|---|---|---|
| Notes (SA 8, CON 9, CF 4) | 21 | 21 | 0 | PASS |
| Line items | 153 + 11 MISSING rows = 164 | 168 | 57 (list 1b) | FAIL: 4 rows missing from ledger (1a); 57 orphans |
| Zero-standing | 13 + 8 = 21 | 22 (adds FT L982 H1FY27 dash) | 6 (R142; R175; R353-R354; R355; R379; R391) | FAIL |
| Agenda items | 2 | 2 | 0 items; 2 sub-rows (R002 meeting time; R475/R508/R444 signature timing) | FAIL (sub-rows) |
| Auditor paragraphs | 9 ledger rows (7 + M10, M11) | 12 paragraphs (SA 5, CON 7) | 4 rows (R446/R447/R439/R438/R449; R529; R430-R437/R418-R421; R448/R476/R478/R488/R490) | FAIL: 2 paragraphs missing from ledger (1a); 4 orphans |
| Entities | 20 | 21 (adds Audit Committee) | 6 (R444, R446, R447, R448, R459, R460) | FAIL |
| Forward | 10 | 10 | 0 (ledger row LG L268 cited via R464, R466, R467, R403-R406) | PASS |
| Dates | 35 | 35 unique date units | 0 (ledger row LG L269 cited via R472-R474, R480) | PASS |
| Qualifiers | 48 | 49 (adds AS 25 framework qualifier) | 0 (ledger row LG L270 cited) | FAIL (1 missing from ledger) |
| Structured ID accounting | 554 / 554 | 554 / 554 | n.a. | PASS |

### 1a. Rows my fresh pass found that the ledger lacks (FAIL, loop to A2; type MISSING)

None of these appears in the structured file (grep for "line 899", "line 1060", "line 982", "line 379", "AS 25" returns no row) or in LG L276-288 (M01-M11).

| # | Fresh-pass unit | Fulltext | Values | Note |
|---|---|---|---|---|
| 1 | SA P&L item VII "Profit Before Extraordinary Items and Tax (V-VI)" | FT L899 (primary FT L183, L187) | 1,787.67 / 1,464.63 / 1,227.24 / 2,691.87 | A4 cites FT L899 as a PBT tie anchor (A4 L124), so the review uses a row the ledger never enumerated. |
| 2 | CON P&L item VII "Profit Before Extraordinary Items and Tax (V-VI)" | FT L1060 (primary FT L547) | 1,866.01 / 1,564.59 / 1,287.07 / 2,851.66 | CON twin of row 1. |
| 3 | SA CF "Profit On Sale of Fixed Asset" | FT L982 (primary FT L358) | H1FY27 dash; FY26 garbled "qas7)" | FY26 reads as (1.57) by tie: 2,691.87 + 165.26 + 128.24 - 20.43 - 1.57 = 2,963.37 = R150. The CON twin exists (R355-R356). The same tie proves the FY26 partnership-share cell is nil, so R148's (109.73) belongs to H1FY27, which confirms A4 L24. |
| 4 | SA CF "NET CASH FLOWS FROM (USED IN) OPERATING ACTIVITIES (A)" | FT L379 (values garbled at FT L378) | not legible | M08 (LG L285) lists rows B, D and closing cash, not row A. |
| 5 | SA auditor paragraph 2, management responsibility, AS 25 "Interim Financial Reporting" | FT L97-102 | n.a. | No structured row, no ledger row. Carries the reporting-framework qualifier. |
| 6 | CON auditor paragraph, management responsibility, AS 25 | FT L440-447 | n.a. | Same as row 5. |
| 7 | Entity "Audit Committee" | FT L39-40, L295, L660 | n.a. | A1 lists the Board of Directors as an entity (R461); by the same rule the Audit Committee is one. A4 names it (A4 L64). Low materiality. |

### 1b. Orphan ledger rows (FAIL, loop to A3; type MISSING)

Test: a ledger row is covered if A4 cites its R-ID, its fulltext line, or its value in context. A4's line "Structured IDs 554, referenced 554, orphans 0 ... No unreviewed ledger row" (A4 L16) repeats A2's ID count (LG L17). It is not a per-row review mark. These 70 ledger rows have no citation and no "reviewed, no finding" mark:

- SA P&L (1): R087-R090.
- SA BS (8): R095-R096, R101-R102, R109-R110, R111-R112, R117-R118, R123-R124, R125-R126, R135-R136.
- SA CF (15): R139-R140, R141-R142, R143-R144, R145-R146, R149-R150, R165-R166, R173-R174, R175-R176, R181-R182, R183-R184, R185-R186, R189-R190, R191-R192, R193-R194, R195-R196.
- CON P&L (3): R285-R288, R289-R292, R293-R296.
- CON BS (12): R297-R298, R299-R300, R301-R302, R309-R310, R317-R318, R319-R320, R321-R322, R325-R326, R329-R330, R331-R332, R339-R340, R341-R342.
- CON CF (18): R343-R344, R345-R346, R347-R348, R349-R350, R351-R352, R353-R354, R355-R356, R379-R380, R381-R382, R383-R384, R385-R386, R387-R388, R389-R390, R391-R392, R395-R396, R397-R398, R399-R400, R401-R402.
- Agenda sub-rows (2): R002; R475/R508/R444.
- Auditor rows (4): R446/R447/R439/R438/R449; R529; R430-R437/R418-R421; R448/R476/R478/R488/R490.
- Entities (6): R444, R446, R447, R448, R459, R460.
- Identifiers (1): R438-R441.

Most are immaterial; one "reviewed, no finding" register clears them. Six carry content that needs real review, not a tag:

| Row | What the extract shows | Why it matters |
|---|---|---|
| R123-R124 | SA investment in Danya 1,267.73 to 1,652.05 = +384.32. Cash contribution R179 (274.59). Residual 109.73 = retained profit share. | Confirms A3's H1FY27 column reading for R147/R148. Shows the parent's Danya profit share is non-cash (retained in the firm). Feeds A3-14 and A3-16. |
| R317-R320 | CON other current liabilities 1,844.40 to 1,441.77 (-402.63, = R369). CON short-term provisions 674.38 to 1,085.07 (+410.69, about equal to current tax R253 411.44). | The OCL fall reverses part of the FY26 inflow (+1,456.16, R370) that A4 says carried FY26 CFO (A4 L376). |
| R383-R384 | R383 (849.08) vs primary FT L756 (849.05). Components R377 + R379 + R381 = (849.05). | A1 OCR conflict; the CON CF otherwise ties: (573.76) + (849.05) + 473.07 = (949.74) = R397. |
| R185-R186, R189-R190 | SA STB in CF R185 419.51 vs BS change R103 - R104 = 418.52. CF financing components (246.60) + 510.87 + 419.51 = 683.78 vs R189 682.72. | 1.06 lakh residual; A1 re-read item. |
| R195-R196 | SA CF closing cash 21.98 (R195) vs BS 21.91 (R131, R193). | A1 OCR item. |
| R289 | FT L1087 OCR reads 2,80,67,330; primary FT L575 reads 2,50,67,330 (R289). | A1 carried the primary value correctly; confirm. |

---

## 2. ARITHMETIC AUDIT

Every derived cell in A4 Steps 1-8 recomputed from the structured raw values (lakh), then converted. Status PASS = match within rounding (0.01 Cr, 0.01 pp, 0.1 day).

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| SA Op EBITDA H1FY26 / H2FY26 / H1FY27 / FY26 (Cr) | 12.53 / 16.12 / 21.37 / 28.65 | 1,252.84 / 1,612.36 / 2,136.89 / 2,865.20 lakh = same | R055-R058, R035-R038, R031-R034, R007-R010 (FT L884-L901) | PASS |
| SA Op EBITDA margin | 15.53 / 14.74 / 16.81 / 15.07% | 15.53 / 14.74 / 16.81 / 15.07% | + R003-R006 (FT L883) | PASS |
| SA reported EBITDA (Cr) | 13.49 / 17.49 / 22.67 / 30.99 | 1,349.40 / 1,749.31 / 2,267.08 / 3,098.71 | same | PASS |
| SA core PBT (Cr) | 11.31 / 13.28 / 16.57 / 24.58 | 1,130.68 / 1,327.68 / 1,657.48 / 2,458.36 | same | PASS |
| SA OI / PBT | 7.87 / 9.35 / 7.28 / 8.67% | 7.87 / 9.35 / 7.28 / 8.67% | same | PASS |
| SA tax total (Cr) | 2.86 / 3.61 / 4.23 / 6.48 | 286.36 / 361.45 / 422.57 / 647.81 (H1FY26 deferred read as 0.30 credit) | R059-R066 (FT L903-904) | PASS |
| SA ETR | 23.33 / 24.68 / 23.64 / 24.07% | 23.33 / 24.68 / 23.64 / 24.07% | same | PASS |
| SA PAT tie (PBT - tax) | 940.87 / 1,103.18 / 1,365.09 / 2,044.06 | 940.88 / 1,103.18 / 1,365.10 / 2,044.06 | R067-R070 (FT L194) | PASS (credit reading of R065 confirmed) |
| SA PAT margin | 11.66 / 10.08 / 10.74 / 10.75% | 11.66 / 10.08 / 10.74 / 10.75% | same | PASS |
| SA gross margin | 22.36 / 20.99 / 24.67 / 21.57% | 22.36 / 20.99 / 24.67 / 21.57% | R015-R022 (FT L887-888) | PASS |
| SA ETR ex Danya share | 25.18% | 422.57 / (1,787.67 - 109.73) = 25.18% | FT L983 | PASS |
| SA total expenses H1FY27 | ND (R043 fails) | Line sum 11,056.61; TI - PBT = 12,843.98 - 1,787.67 = 11,056.31; R043 11,086.31 is 30.00 off | FT L889-894 | PASS (ND is correct) |
| SA H1 + H2 = FY26 (rev, PBT, current tax, PAT) | ties | 19,007.73; 2,691.87; 530.75; 2,044.06 | R003-R070 | PASS |
| Reserves rise = PAT | 1,365.09 | 10,159.80 - 8,794.70 = 1,365.10 | R093-R094 | PASS |
| CON Op EBITDA (Cr) | 14.11 / 18.71 / 23.35 / 32.82 | 1,411.31 / 1,871.11 / 2,335.45 / 3,282.42 | R249-R252, R229-R232, R225-R228, R201-R204 (FT L1043-L1064) | PASS |
| CON Op EBITDA margin | 18.77 / 17.58 / 17.26 / 18.07% | same | + R197-R200 | PASS |
| CON reported EBITDA (Cr) | 14.27 / 19.01 / 23.62 / 33.29 | 1,427.47 / 1,901.07 / 2,361.90 / 3,328.54 | same | PASS |
| CON core PBT (Cr) | 12.71 / 15.35 / 18.40 / 28.06 | 1,270.91 / 1,534.63 / 1,839.56 / 2,805.54 | same | PASS |
| CON OI / PBT | 1.26 / 1.91 / 1.42 / 1.62% | same | same | PASS |
| CON ETR | 26.17 / 28.59 / 26.19 / 27.50% | 336.81 / 447.29 / 488.72 / 784.10 over PBT | R253-R264 (FT L1067-1071) | PASS |
| CON prior-year tax reading | 0.37 charge H2FY26, FY26; nil H1 | 1,564.59 - 329.27 - 117.65 - 0.37 = 1,117.30 vs R266 1,117.29; 1,866.01 - 411.44 - 77.28 = 1,377.29 = R265 | FT L1071-1072 | PASS |
| CON PAT margin (group) | 12.64 / 10.50 / 10.18 / 11.38% | same | R265-R268 | PASS |
| CON gross margin | 26.51 / 24.72 / 25.22 / 25.46% | same | R209-R216 | PASS |
| CON total expenses H1FY27 foots | 116.91 | 11,691.35 | FT L1053 | PASS |
| CON DTL 30-Sep-26 | 227.39 | E&L sum 30,574.83 vs R321 30,574.82; DTL change 77.28 = R257 | FT L1105-1121 | PASS |
| SVC revenue gap (Cr) | (5.47) / (2.97) / (8.44) / +8.17 | (546.66) / (297.03) / (843.69) / 817.12 | R003-R006 vs R197-R200 | PASS |
| SVC Op EBITDA gap (Cr) and % SA PAT | 1.58 / 2.59 / 4.17 / 1.99; 16.8 / 23.5 / 20.4 / 14.5% | 158.47 / 258.75 / 417.22 / 198.56; 16.84 / 23.46 / 20.41 / 14.55% | derived | PASS |
| SVC margin gap (pp) | 3.24 / 2.84 / 3.00 / 0.45 | same | derived | PASS |
| MI / SA PAT | 1.00 / 1.28 / 1.15 / 0.89% | same | R269-R272 | PASS |
| Derived Danya PAT and % CON PAT | 0.94 / 1.41 / 2.35 / 1.22 Cr; 9.9 / 12.6 / 11.4 / 8.85% | same; cross-check 90% x 121.90 = 109.71 vs FT L983 109.73 | R269-R272 | PASS |
| Implied Danya employee cost (Cr) | 0.66 / (0.44) / 0.22 / 0.11 | 66.04 / (43.59) / 22.45 / 10.92 | R221-R224 vs R027-R030 | PASS |
| CON YoY: revenue, Op EBITDA, margin, D&A, FC | +79.95%, +65.48%, -151 bps, +415.4%, +189.5% | same | R197-R232 | PASS |
| CON YoY: EBIT, OI, core PBT, PBT, PAT, owners, EPS | 13.72 to 21.31 (+55.38%), +63.68%, +44.74%, +44.98%, +44.94%, +45.09%, +45.21% | same | same | PASS |
| SA YoY: revenue, Op EBITDA, margin, D&A, FC | +57.62%, +70.56%, +128 bps, +468.1%, +221.7% | same | R003-R038 | PASS |
| SA YoY: EBIT, OI, core PBT, PBT, PAT | 12.18 to 19.38 (+59.11%), +34.83%, +46.59%, +45.67%, +45.09% | same | same | PASS |
| GM change CON / SA | -129 bps / +231 bps | -128.6 / +231.1 bps | derived | PASS |
| D&A + FC as % CON revenue | 1.87% to 3.67% | 140.40 / 7,519.44; 495.89 / 13,530.91 | R225-R232 | PASS |
| HoH CON revenue / SA revenue | +41.56%, +27.12% / +35.65%, +16.20% | same | R197-R199, R003-R005 | PASS |
| HoH core PBT CON / SA | +19.87% / +24.84% | same | derived | PASS |
| CON PAT bridge components (Cr) | +15.94, -1.74, -4.96, -1.65, -1.91, +0.10, -1.52, -0.00 (0.41 lakh); total +4.27 | 1,593.55; -173.88; -495.53; -164.50; -190.99; +10.29; -151.50; -0.41; +427.03 | derived | PASS |
| SA PAT bridge components (Cr) | +10.39, +2.94, -4.49, -1.64, -1.93, +0.34, -1.31, -0.05; total +4.24 | 1,039.21; 293.81; -448.97 (line sum -449.28); -164.22; -193.03; +33.63; -130.77; -5.44; +424.22 | derived | PASS |
| OI share of PBT change CON / SA | 1.8% / 6.0% | 10.29 / 578.94; 33.63 / 560.43 | derived | PASS |
| Deferred tax as % SA PBT | 432 bps | 77.17 / 1,787.67 = 4.32% | R063, R055 | PASS |
| CON CFO/PAT FY26 / H1FY27 | 1.25x / -0.42x | 2,590.47 / 2,067.56; -573.76 / 1,377.29 | R375-R376 | PASS |
| CON FCF FY26 / H1FY27 (Cr) | (31.58) / (14.42) | 2,590.47 - 5,748.04; -573.76 - 867.85 | R375-R378 | PASS |
| CON WC change FY26 / H1FY27 (Cr) | +2.82 / (26.75) | +282.35 (= 3,437.89 - 3,155.53); (2,675.10) | FT L1164-1169 | PASS |
| CON receivable / inventory / payable days, Mar-26 | 80.1 / 141.0 / 116.8 | 80.10 / 141.03 / 116.77 | R336, R334, R314+R316 | PASS |
| CON receivable / inventory / payable days, Sep-26 | 84.8 / 158.2 / 122.3 | 84.77 / 158.18 / 122.34 | R335, R333, R313+R315 | PASS |
| CON CCC Mar-26 / Sep-26 | 104.4 / 120.6 (+16.2) | 104.36 / 120.61 (+16.25) | derived | PASS |
| CON payable days change | +5.5 | +5.57 unrounded | derived | PASS (rounding; STYLE S-5) |
| CON gross debt, cash, net debt (Cr) | 49.97 / 57.45; 9.75 / 0.25; 40.23 / 57.20 (+42.2%) | 4,997.30 / 5,744.56; 974.55 / 24.81; 4,022.75 / 5,719.75 (+42.18%) | R305-R306, R311-R312, R337-R338 | PASS |
| CON BS ties to CF (receivables, inventory, payables) | +1,583.64 / +2,535.78 / +2,239.25 | same | R335-R336 vs R359; R333-R334 vs R361; R313-R316 vs R367 | PASS |
| SA CFO/PAT FY26 / H1FY27 | 1.36x / -0.38x | 2,773.36 / 2,044.06; -522.90 / 1,365.09 | R169-R170 | PASS |
| SA FCF FY26 / H1FY27 (Cr) | (29.73) / (13.79) | 2,773.36 - 5,746.46; -522.90 - 855.85 | R171, R178 | PASS |
| SA WC change FY26 / H1FY27 (Cr) | +4.71 / (24.19) line sum, (24.16) implied | +471.18; (2,418.67); (305.20) - 2,110.46 = (2,415.66) | FT L987-994, R149, R165 | PASS |
| SA inventory days Mar-26 / Sep-26 | 95.9 / 134.6 | 95.92 / 134.60 | R127-R128 | PASS |
| SA payable days Mar-26 / Sep-26 | 107.9 / 114.7 | 107.85 / 114.68 (Mar-26 MSE at 2,879.29, FT L937) | R105-R108 | PASS |
| SA receivable days Sep-26; CCC Sep-26 | 75.4; 95.3 | 75.38; 95.30 | R129 | PASS |
| SA gross debt, net debt, net worth, ND/NW | 45.73 / 55.02; 35.99 / 54.80 (+52.3%); 112.94 / 126.59; 0.32x / 0.43x | 4,572.70 / 5,502.09; 3,598.91 / 5,480.18 (+52.27%); 11,293.81 / 12,658.91; 0.319 / 0.433 | R091-R104, R131-R132 | PASS |
| SA OCA BS vs CF gap | 217.76 = taxes paid | 739.73 - 521.97 = 217.76 = R167 | R133-R134, R157 | PASS |
| SA receivables BS vs CF gap; Mar-26 footing gap | 303.00; 300.01 | 718.82 - 415.82; assets 25,173.69 vs E&L 24,873.68 | R129-R130, R153 | PASS (see C-1 on what the gap means) |
| Indicative ROCE SA / CON | 23.6% / 23.6% | 4,135.56 / 17,540.62 = 23.58%; 4,315.60 / 18,277.01 = 23.61% | R055, R031, R249, R225, BS rows | PASS (CON includes MI; STYLE S-2) |
| Trailing PAT and EPS | 24.68 Cr; Rs 9.87 | 2,468.28; 4.41 + 5.46 | R274, R273, R278, R277 | PASS |
| Warrant economics | 5.27 received; 15.81 balance; +4.99%; 2,62,38,135 | 12,47,000 x 42.25 = 5,26,85,750; x 126.75 = 15,80,57,250; 1,247,000 / 24,991,135 = 4.99% | R411-R415 | PASS |
| Proceeds utilised + unutilised | 5.20 Cr + 6.55 lakh | 520.31 + 6.55 = 526.86 = R404 | R405-R406 | PASS |

Arithmetic mismatches above rounding: none.

---

## 3. ADVERSARIAL READ

### Claim 1. "Growth is real at the PBT line ... about 98% of the PBT change is recurring operations" (A4 L250, L317, L656)
Strongest bear counter from the extract. In H1FY27 the CON revenue exceeded SA revenue by 817.12 lakh (Rs 8.17 Cr; R197 13,530.91 - R003 12,713.79). In the same half, CON receivables rose 864.82 lakh (Rs 8.65 Cr) more than SA receivables (R359 1,583.64 - R153 718.82). The non-parent revenue excess and the non-parent receivable build are the same size (106%). Reading 1: intercompany balances were stable, so the group revenue booked outside the parent was uncollected at 30-Sep-26. Reading 2: intercompany receivables fell, so less of it is uncollected. Separating observation: Danya receivables and intercompany balances at 30-Sep-26 (not in the filing). The accrual part of the counter (PAT Rs 13.77 Cr vs CFO Rs (5.74) Cr) is already in A4 (A4 L333-L341). The revenue-to-receivable match is not.
Survives: YES. Type MISSING. Graft into A4 Step 2 diagnostic 3 (A4 L250) and the 1-SVC reading (A4 L206). Route A4.

### Claim 2. Indicative ROCE 23.6% (SA and CON) and "a group operating margin near 17%" as strength (A4 L417, L454, L580)
Strongest bear counter from the extract. The ROCE capital base excludes CON trade payables of 8,459.28 lakh (Rs 84.59 Cr; R313 + R315), which is 147% of gross borrowings (5,744.56, R305 + R311). Of that supplier credit, 4,083.10 lakh (Rs 40.83 Cr, 48.3%) is owed to micro and small enterprises (R313), up 490.07 lakh in the half (R314 3,593.03). A4 never mentions the MSE share. Floor test: MSE purchases cannot exceed total spend. CON half-year spend = purchases 12,653.73 (R209) + other direct 323.88 (R217) + other expenses 333.44 (R233) + capex 867.85 (R377) = 14,178.90 lakh. So the MSE dues equal at least 52.7 days of spend (4,083.10 / (14,178.90 / 183)). Payables carry GST and P&L spend does not; at an 18% rate the floor is about 44.7 days [INFERENCE: GST rate]. With capex excluded (if capital creditors sit in other liabilities) the floor is 56.1 days (47.6 GST-inclusive). The floor assumes every rupee came from MSEs. The statutory MSE payment term is 45 days, with interest at three times the bank rate past term and an income-tax disallowance (s.43B(h)) for dues unpaid past term [INFERENCE: MSMED Act 2006 s.15-16; Income Tax Act s.43B(h); PENDING LIVE VERIFICATION]. SA floor: 3,103.72 / (13,511.53 / 183) = 42.0 days (35.6 GST-inclusive), so any excess sits in the CON-minus-SA piece. Reading 1: purchases were back-loaded into September (fits the 2,535.78 inventory build, R213), so dues are fresh. Reading 2: part of the Rs 40.83 Cr is past term, with interest unprovided and an FY27 tax risk. Separating observation: the MSMED overdue-and-interest disclosure in the FY26 and FY27 annual reports (not in this filing). The return on capital holds only while this credit holds.
Survives: YES, as a named risk. Type MISSING. Graft one line into A4 Step 5 (payable days row A4 L340 and the funding answer A4 L379), and add one Step 8.5 question (overdue MSE amount and interest provided at 30-Sep-26). Route A4.

### Claim 3. "Stepping up on revenue and core PBT for three consecutive halves ... the run-rate did lift" (A4 L271, L273)
Strongest bear counter from the extract. The lift came with CON receivable days +4.7 and inventory days +17.2 (A4 L338-L339), and the CON Op EBITDA margin fell in each half (R197-R252: 18.77%, 17.58%, 17.26%). The filing does not show whether new assets or traded volume produced the lift.
Survives: YES, but A4 already states it ("Growth is bought with margin and working capital", A4 L271; source of lift not shown, A4 L273). No graft needed.

### Mandatory acquisition-economics probe
The filing describes no acquisition and no stake buy. "Purchases of stock in trade" (FT L887) and "purchase of tangible assets" (FT L1003) are trading and capex lines. The nearest analogue is the parent's cash contribution of 274.59 lakh to Danya Electric Company (R179, FT L1007). The profit share stays at 90% (FT L674). I tested it as a related-party capital decision.
- Price vs earnings. Parent capital in Danya at 30-Sep-26 = 1,652.05 lakh (R123). CON BS has no investments line (FT L1122-L1134), so the whole balance is the eliminated Danya capital. Annualised parent share = 109.73 x 2 = 219.46 lakh. Rs 16.52 Cr / Rs 2.19 Cr = about 7.5x earnings, a 13.3% post-tax yield on closing capital (15.0% on average capital).
- Capital movement. Parent capital rose 384.32 lakh (+30.3%; R123 - R124) = 274.59 cash (R179) + 109.73 retained share. Minority capital fell 7.81 (R303 398.95 vs R304 406.76) = share of profit 12.19 (R269) - withdrawal 20.00 (R393). Both tie to the lakh.
- Is the earnings period representative? Derived Danya PAT (MI x 10, R269-R271): 93.9 (H1FY26), 141.1 (H2FY26), 121.9 (H1FY27). Danya profit fell 13.6% half-on-half while the parent's capital in it rose 30.3%.
- Quality markers. Danya PBT H1FY27 = R249 1,866.01 - R055 1,787.67 + 109.73 = 188.07 lakh. Danya tax = (R253 411.44 - R059 345.40) + (R257 77.28 - R063 77.17) = 66.15, an effective rate of 35.2% (PAT check 188.07 - 66.15 = 121.92 vs MI x 10 = 121.90). Annualised pre-tax return on closing partners' capital (1,652.05 + 398.95 = 2,051.00) = 18.3% (20.2% on average capital), against group pre-tax ROCE 23.6%. The firm-level rate is about 10 pp above the parent's 25.18%: about 18.8 lakh extra tax per half, 1.4% of group PAT [rate explanation INFERENCE: partnership-firm tax at 30% plus surcharge and cess]. Debt, cash and customer tenure of Danya: ND.
- In the parent's favour: minority partners hold 19.5% of partners' capital (398.95 / 2,051.00) for a 10% profit share. That holds only if Danya pays no interest on capital or remuneration to partners (ND; A4 Q12 asks).
- Bear reading. In H1FY27 the listed parent put 30% more capital into a firm that the MD co-owns. Danya earns below the group return, pays a higher tax rate and earned less than in the prior half. The minority partners took out more than their share of profit. A4 has the 2.75 vs 0.20 flow (A4 L504) but not the return, the tax cost, the half-on-half profit fall or the BS tie.
Survives: YES, in part. Type MISSING. Graft into the A3-16 governance material (A4 0D CON 3 row, Q12, the flags list). It also explains why CON ETR (26.19%) exceeds SA ETR ex the Danya share (25.18%); A4 does not explain that gap. Route A4.

---

## OTHER FINDINGS ON A4 TEXT

C-1 (CONTRADICTION, route A4). Q13 (A4 L505) asks management to explain a "Rs 3.03 Cr" reclassification between the SA balance-sheet and cash-flow receivable changes. That figure is built on R130. A4's own preamble (A4 L23) excludes R130 from any change metric and routes it to A1. The flags (A4 L651) say the same. The extract points to extraction, not to the company:
- SA Mar-26 E&L sums to 24,873.68 (R092, R094, R096, R098, R100, R102, R104, MSE 2,879.29 per FT L937, R108, R110, R112). Assets sum to 25,173.69 with R130 at 4,821.09. The gap is 300.01. With the hundreds digit of R130 read as 5 (4,521.09), assets sum to 24,873.69 and the statement foots to 0.01.
- SA CF working-capital lines sum to (2,418.67) against an implied (2,415.66) (R165 - R149), a 3.01 residual. With the units digit of R153 read as 5 ((715.82)), the line sum is (2,415.67) and the residual is 0.01. The BS receivable change under the same reading is 715.82, equal to the CF.
- A3 found the same 5-read-as-8 pattern at R043: 11,086.31 vs TI - PBT 11,056.31.
I do not replace any value; NOT FOUND stands until A1 re-reads R130, R153 and R043 at source. Fix: hold Q13 out of the IR letter (A4 L516 says send all 17 verbatim) until the A1 re-read. Re-frame A3-13 as "probable extraction digit error, unconfirmed", not as a filed gap.

F-1 (FACTUAL, route A4). Q11 (A4 L503) says "Rs 8.65 Cr of the Rs 15.84 Cr CON receivables build sits in Danya". The extract supports only "CON receivables rose Rs 8.65 Cr more than SA receivables, cash-flow basis" (R359 - R153). CON change minus SA change = Danya change minus the change in intercompany balances, and A4 itself argues intercompany flows shifted (A4 L206). Reword.

F-2 (FACTUAL, route A4). The brief says the Rs 15.81 Cr balance "is due by about February 2027" (A4 L562). Note SA 3 says "payable within 18 months" (A4 L66). The extract says the balance is "payable upon the exercise of the warrants" (FT L312, L849-850) and holders "may exercise their right" within 18 months (FT L853-857). It is the holders' option, not an obligation of the holders and not a receivable. Reword both cells.

F-3 (FACTUAL, route A4). Step 9 cites a "BSE/NSE results filing" (A4 L524). The outcome letter goes to NSE only (FT L21-26). No BSE reference exists in the extract. Change to NSE.

---

## VERDICT

VERDICT: INCOMPLETE.
- A2 (MISSING): add the 4 valued line items (FT L899, L1060, L982, L379), the 2 AS 25 management-responsibility auditor paragraphs (FT L97-102, L440-447) and the Audit Committee entity (FT L39-40) to the ledger as MISSING_FROM_STRUCTURED, routed back to A1.
- A3 (MISSING): review or mark "reviewed, no finding" the 70 orphan ledger rows in 1b. Real review is required for R123-R124, R317-R320, R383-R384, R185-R186/R189-R190, R195-R196 and R289.
- A4 (MISSING): graft the three surviving bear counters (Claim 1 revenue-to-receivable match; Claim 2 MSE share and floor test; acquisition probe on Danya capital).
- A4 (CONTRADICTION): C-1, hold Q13 pending the A1 re-read.
- A4 (FACTUAL): F-1 Q11 attribution; F-2 warrant balance as option, not "due"; F-3 NSE, not BSE/NSE.
loop_back_to: A2. The chain re-runs A2, then A3, then A4. Arithmetic is clean (zero mismatches) and the plain-language brief gate passes, so the numbers can stand through the loop.

---

## STYLE NOTES (logged, no re-run)

- S-1. Step 3 table row label "H1FY28 and earlier history" (A4 L266) should read "H1FY25 and earlier history".
- S-2. CON indicative ROCE capital employed includes minority interest (172.25 = 168.18 + 4.07; 193.29 = 189.30 + 3.99), but the stated formula (A4 L454) says "net worth incl. warrants + debt". The 23.6% is right as computed. State the MI inclusion (ex MI it is 24.1%).
- S-3. Preamble says "auditor paragraphs 9 (+M10, M11)" (A4 L16). The ledger's 9 already include M10 and M11 (LG L232-242).
- S-4. Brief L560 tags "because the company spent Rs 57.48 Cr ..." as [FILED]. The capex figure is FILED; the causal link is INFERENCE. Tag them separately.
- S-5. CON payable-days change shows +5.5 from rounded endpoints; unrounded it is +5.57 (5.6). Rounding only.
- S-6. Two forward-map catalysts are undated (balance-confirmation adjustments; CWIP capitalisation, A4 L588-589). Name the first observation point (FY27 results, about 30-May-2027).

---

```yaml
stage: A5-adversary
company: "SUPREMEPWR"
quarter: "h1fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: ["R087-R090", "R095-R096", "R101-R102", "R109-R110", "R111-R112", "R117-R118", "R123-R124", "R125-R126", "R135-R136", "R139-R140", "R141-R142", "R143-R144", "R145-R146", "R149-R150", "R165-R166", "R173-R174", "R175-R176", "R181-R182", "R183-R184", "R185-R186", "R189-R190", "R191-R192", "R193-R194", "R195-R196", "R285-R288", "R289-R292", "R293-R296", "R297-R298", "R299-R300", "R301-R302", "R309-R310", "R317-R318", "R319-R320", "R321-R322", "R325-R326", "R329-R330", "R331-R332", "R339-R340", "R341-R342", "R343-R344", "R345-R346", "R347-R348", "R349-R350", "R351-R352", "R353-R354", "R355-R356", "R379-R380", "R381-R382", "R383-R384", "R385-R386", "R387-R388", "R389-R390", "R391-R392", "R395-R396", "R397-R398", "R399-R400", "R401-R402", "R002", "R475/R508/R444", "R446/R447/R439/R438/R449", "R529", "R430-R437/R418-R421", "R448/R476/R478/R488/R490", "R444", "R446", "R447", "R448", "R459", "R460", "R438-R441"]
  missing_from_ledger: ["FT L899 SA P&L item VII Profit Before Extraordinary Items and Tax (1,787.67/1,464.63/1,227.24/2,691.87)", "FT L1060 CON P&L item VII (1,866.01/1,564.59/1,287.07/2,851.66)", "FT L982 SA CF Profit On Sale of Fixed Asset (H1FY27 dash; FY26 garbled, ties as (1.57))", "FT L379 SA CF NET CASH FLOWS FROM OPERATING ACTIVITIES (A) (values garbled)", "FT L97-102 SA auditor management-responsibility paragraph, AS 25 qualifier", "FT L440-447 CON auditor management-responsibility paragraph, AS 25 qualifier", "FT L39-40/L295/L660 entity Audit Committee"]
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Growth is real at PBT; ~98% of PBT change recurring (A4 L250, L317, L656)", counter: "CON-over-SA revenue Rs 8.17 Cr equals CON-over-SA receivable build Rs 8.65 Cr; under stable intercompany balances the non-parent revenue was uncollected at 30-Sep-26", source_line: "R197, R003, R359, R153 (FT L1042, L883, L1164, L988)", type: MISSING}
  - {claim: "Indicative ROCE 23.6%; margin near 17% as strength (A4 L417, L454, L580)", counter: "Capital base excludes Rs 84.59 Cr supplier credit (147% of debt); Rs 40.83 Cr (48.3%) is MSE dues; floor 52.7 days of total spend (~44.7 GST-inclusive) vs 45-day statutory term [INFERENCE]; no overdue-MSE disclosure", source_line: "R313-R316, R209, R217, R233, R377 (FT L1116-1118, L1046-1052, L752)", type: MISSING}
  - {claim: "Danya capital contribution (acquisition-economics probe, nearest analogue; A4 L504)", counter: "Parent capital in Danya +30.3% to Rs 16.52 Cr (7.5x annualised share, 13.3% yield) while Danya PAT fell 13.6% HoH; Danya pre-tax return 18.3% vs group 23.6%; Danya tax 35.2% vs parent 25.18%; minority withdrew 20.00 vs 12.19 share", source_line: "R123-R124, R179, R249, R055, R253, R059, R257, R063, R269-R271, R303-R304, R393", type: MISSING}
findings_by_type:
  factual:
    - "F-1 A4 Q11 (A4 L503): 'Rs 8.65 Cr sits in Danya' unsupported; extract supports only CON-minus-SA receivable change (R359 - R153), which nets intercompany balances. Route A4."
    - "F-2 A4 L562 and L66: warrant balance called 'due' / 'payable within 18 months'; extract says payable upon optional exercise (FT L312, L849-857). Route A4."
    - "F-3 A4 L524: 'BSE/NSE results filing'; filing addressed to NSE only (FT L21-26). Route A4."
  missing:
    - "M-1 Ledger lacks 4 valued line items: FT L899, L1060, L982, L379. Route A2."
    - "M-2 Ledger lacks 2 auditor management-responsibility paragraphs with AS 25 qualifier: FT L97-102, L440-447. Route A2."
    - "M-3 Ledger lacks entity Audit Committee (FT L39-40, L295, L660). Route A2."
    - "M-4 70 orphan ledger rows with no A4 citation or 'reviewed, no finding' mark (list in coverage.orphan_rows); real review needed for R123-R124, R317-R320, R383-R384, R185-R186/R189-R190, R195-R196, R289. Route A3."
    - "M-5 Surviving bear counter not in A4: CON-over-SA revenue vs receivable match (Claim 1). Route A4."
    - "M-6 Surviving bear counter not in A4: MSE share of supplier credit and floor test (Claim 2). Route A4."
    - "M-7 Surviving bear counter not in A4: Danya capital return, tax cost, HoH profit fall, BS tie (acquisition probe). Route A4."
  contradiction:
    - "C-1 A4 Q13 (A4 L505) asks IR about a Rs 3.03 Cr receivable gap built on R130, which A4 L23 excludes; 5-for-8 digit readings at R130 and R153 would foot the Mar-26 SA BS (24,873.69 vs 24,873.68) and close the CF residual (0.01), same pattern as R043. Hold Q13 pending A1 re-read. Route A4."
  style:
    - "S-1 A4 L266 label 'H1FY28 and earlier' should be 'H1FY25 and earlier'."
    - "S-2 A4 L454 CON ROCE capital employed includes MI but formula omits it (ex MI 24.1%)."
    - "S-3 A4 L16 'auditor paragraphs 9 (+M10, M11)': ledger 9 already includes M10, M11."
    - "S-4 A4 L560 causal 'because' tagged FILED; causal link is INFERENCE."
    - "S-5 CON payable days change +5.5 rounded vs +5.57 unrounded."
    - "S-6 Two forward-map catalysts undated (A4 L588-589); name first observation point."
loop_back_to: "A2"
gap: "A2: add MISSING_FROM_STRUCTURED rows for FT L899, L1060, L982, L379 line items, FT L97-102 and L440-447 AS 25 auditor paragraphs, Audit Committee entity (route to A1). A3: review or mark 'reviewed, no finding' 70 orphan ledger rows; real review for R123-R124, R317-R320, R383-R384, R185-R186/R189-R190, R195-R196, R289. A4: graft 3 surviving bear counters (revenue-receivable match; MSE share and floor; Danya capital return and tax cost); C-1 hold Q13 pending A1 re-read of R130/R153/R043; F-1 Q11 attribution; F-2 warrant balance is an option, not due; F-3 NSE not BSE/NSE."
style_notes: ["S-1 A4 L266 H1FY28 label should be H1FY25", "S-2 CON ROCE CE includes MI, formula omits it", "S-3 auditor paragraph count wording", "S-4 causal clause tagged FILED", "S-5 payable days +5.5 vs +5.57 rounding", "S-6 two undated forward-map catalysts"]
analyst_note: "Arithmetic is clean: every derived A4 cell recomputes within rounding, and both consolidated statements foot and tie. INCOMPLETE comes from completeness, not numbers. First, A1 and A2 dropped four valued line items, two of them item VII rows that A4 itself cites as tie anchors. Second, 70 ledger rows carry no A4 citation; A4's 'no unreviewed ledger row' repeats A2's ID count. A 'reviewed, no finding' register clears most of them. R123-R124 needs real review: the parent's Danya capital rose Rs 3.84 Cr, of which Rs 1.10 Cr is the retained profit share. That confirms A3's H1FY27 column reading for the partnership share. Third, Q13 would send IR a question built on R130, a row A4 itself excludes. One 5-for-8 digit misread at R130 and at R153 foots the Mar-26 SA balance sheet and closes the cash-flow residual, the same pattern as R043. A1 should re-read before any IR letter. Fourth, three bear counters survive and are not in A4. The loop starts at A2; A3 and A4 follow."
```
