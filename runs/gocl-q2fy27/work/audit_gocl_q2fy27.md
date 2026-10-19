# A5 ADVERSARY AUDIT: GOCL Corporation Limited (GOCL), Q2 FY27

Agent: A5 adversary, model claude-opus-5-5. Run date 2026-10-20.
Under audit: runs/gocl-q2fy27/work/review_gocl_q2fy27.md (862 lines. Part 1 is RL1-RL429. Part 2 is appended in the same file at RL430-RL861.)
Inputs read:
- A1 fulltext runs/gocl-q2fy27/extracted/gocl-results-q2fy27-fulltext.md (1,078 lines). The image transcription at L832-L1078 governs pages 4-7 and 12-14.
- A1 structured runs/gocl-q2fy27/extracted/gocl-results-q2fy27-structured.md (R001-R2233).
- A2 ledger runs/gocl-q2fy27/work/ledger_results_gocl_q2fy27.md.
I opened no source PDF and nothing under inputs/.
Anchor key: "L###" = fulltext line. "RL###" = review line. "R####" = structured row. Sums are in Rs lakhs unless marked Cr.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT

DELIVERABLE-COMPLETENESS: narrative PRESENT (RL722-RL736; 13 lines, inside the 10-20 band) | sector PRESENT (RL738-RL744) | business-model PRESENT (RL746-RL753) | competition PRESENT (RL755-RL760) | forward map PRESENT (RL762-RL775; 10 catalysts, three hard-dated: 24-Nov-2026, by 14-Feb-2027, by 30-May-2027; every catalyst has a bull fork and a bear fork). Gate: PASS.

---

## 1. COVERAGE AUDIT

Method: a fresh pass over the A1 fulltext, with no use of A2's counts. Notes, auditor paragraphs, agenda items, entities and forward statements come from the text-layer pages (L17-L831). Line items and cells come from the image transcription (L832-L1070). I then diffed by category against the A2 ledger. Last, I mapped every ledger section to the review.

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Numbered notes (C1-C8, S1-S8) | 16 | 16. Consolidated at L428, L434, L442, L471, L479, L486, L487, L493. Standalone at L764, L770, L772, L774, L782, L789, L797, L824. The OCR loses the numbers for consolidated Notes 4-8. Three things confirm the numbering: the EoM "Note 4" (L143), the statement refs (L911, L922) and the standalone BS refs "6 & 7" (L1016). | 0 | PASS |
| Unnumbered footnotes / qualifiers | 32 | 32. Unit, column-status, refer-note, EPS-annualisation and "#" markers on the statement pages, plus two notes headings (L427, L763) and two website lines (L495, L827). | 0 | PASS |
| Financial line items (image transcription) | 231 | 232. Consolidated P&L 32 (L833-L864), segment 26 (L866-L891), consolidated BS 37 (L893-L929), consolidated CF 38 (L931-L968), standalone P&L 28 (L970-L997), standalone BS 35 (L999-L1033), standalone CF 36 (L1035-L1070). | 0 | DIFF 1. L956 "Repayment of loans from Companies" has no structured row. No value prints in either period (A1 header L930). The OCR tokens R605-R606 at L404 are superseded and belong to adjacent lines. Logged STYLE S1, no loop. |
| Image NUMBER cells | 796 | 796. Printed cells only: 187 + 156 + 74 + 74 + 163 + 70 + 72. The ten unprinted reserves cells and L956 carry no row. | 0 | PASS |
| ZERO_STANDING line items / cells | 21 / 31 | 21 / 31 printed-dash lines and cells (L856, L870, L894, L919, L920, L935, L936, L951-L953, L961, L962, L964, L1000, L1024, L1040, L1055, L1056, L1059, L1060, L1066). L956 would be a 22nd, a blank label. | 0 | PASS (S1) |
| Superseded OCR rows | 949 | 949. grep SUPERSEDED_BY gives 950, which includes header line 5. The range arithmetic is 253+171+53+81+226+82+83. | 0 | PASS |
| Board agenda items | 4 | 4 (L40, L44, L49, L54) | 0 | PASS |
| Auditor paragraphs | 12 | 12. Consolidated paras 1-7 at L88, L95, L102, L113, L121, L143, L159. Standalone paras 1-5 at L515, L521, L529, L538, L556. | 0 | PASS. Mapping note S4. |
| Entities | 26 | 26 named parties. SEBI (L37, L110) and ICAI (L104, L531) appear only in boilerplate, as issuers of regulations and standards. | 0 | PASS. S3. |
| Forward / pending statements | 20 | 25: the 20 plus five units. These are the ACHT firm commitment (L434-L435), the detonator approval "initiated" (L449-L450), the standalone EoM pending text (L563-L567), the standalone Ecopolis consideration (L793) and the standalone Kukatpally advance (L801-L802). | 0 | PASS. All five sit in structured under other tags (R1399, R1239/R1308, R1415, R1432, R1433). A4 reviews each: RL57 and RL649; RL504, RL601 and RL648; RL72; RL69; RL70. Tag note S2. |
| Turns / questions / slides | 0 | 0. Results filing only, with no concall and no deck (RL6). | 0 | N/A |
| Structured row IDs | 2,233 | R001-R2233, contiguous | 0 | PASS |

Orphan check (ledger rows against the A4 review):
- A4 anchors by fulltext line, not by row ID. The exceptions are R1407, R1430, R1912, R1924 and R2090 (RL17). So I mapped each ledger section to its fulltext lines.
- Notes: 16 of 16 cited in the Step 0D table (RL56-RL73).
- Auditor paragraphs: EoM, Other Matter and both conclusions cited (RL72-RL73, RL81). The scope, SRE and entity-list paragraphs are covered at RL81 and RL191.
- Agenda: 4 of 4 cited (RL3, RL418, RL641).
- Entities: every counterparty with an economic role is cited.
- The footnotes, the remaining line items, the dates and the text-layer tokens fall under A4's contractual blanket mark "all reviewed" (RL15-RL21).
- I spot-checked the uncited lines for material content. Three items came up and are logged S9, S10 and S12. None changes a number in the review.
Orphan rows: none.

A4 preamble counts against the ledger: 16 notes, 231 line items, 32 qualifiers, 12 auditor paragraphs, 4 agenda items, 26 entities, 20 forward statements, 949 superseded rows, 3 FOOTING_GAP rows and 2 PRINTED_DIFF rows. All match.

---

## 2. ARITHMETIC AUDIT

I recomputed every derived cell from the image-transcribed lines. The six-value cells run Q2 FY26 / Q1 FY27 / Q2 FY27 / FY26 / H1 FY26 / H1 FY27, as in A4's columns.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Step 1-I consolidated, 23 lines x 6 periods, lakhs to Cr | RL98-RL122 | Every cell = lakhs / 100 to 2 dp | L833-L864 | PASS |
| Step 1-II standalone, 20 lines x 6 periods | RL128-RL147 | Every cell matches | L970-L997 | PASS |
| Shares; EPS Q2 FY27 | 4,95,72,500; Rs 8.17 | 991.45 / 2 = 495.725 lakh shares; 4,050.11 / 495.725 = 8.170 | L860, L853, L864 | PASS |
| Operating EBITDA, consolidated (Cr) | (7.26) (5.25) (14.46) (31.39) (13.26) (19.71) | (725.72) (524.95) (1,446.06) (3,138.86) (1,326.22) (1,971.01) | L843 + L840 + L839 - L834 | PASS |
| Op EBITDA margin, consolidated | -326.9 -122.5 -352.2 -321.5 -236.3 -234.9 % | -326.87 -122.51 -352.16 -321.50 -236.32 -234.89 % | / L833 | PASS |
| Reported EBITDA, consolidated | 45.22 57.11 50.65 397.43 134.52 107.76 | 4,521.93 5,711.06 5,065.24 39,742.60 13,451.97 10,776.30 | L845 + L840 + L839 | PASS |
| Core PBT ex-OI ex-exceptional, consolidated | (19.99) (6.12) (15.35) (82.30) (52.31) (21.46) | (1,998.60) (611.70) (1,534.54) (8,230.33) (5,231.04) (2,146.24) | L843 - L834 | PASS |
| OI / PBT, consolidated | 164.6 104.6 125.9 120.0 143.1 114.6 % | 164.59 104.62 125.89 120.00 143.06 114.61 % | L834 / L845 | PASS |
| ETR, consolidated | 31.40 22.03 28.95 19.31 20.38 25.28 % | same | L848 / L845 | PASS |
| PAT margin, consolidated | 632.0 942.8 986.3 15,588.8 22,034.5 964.1 % | 631.96 942.78 986.31 15,588.76 22,034.50 964.08 % | L853 / L833 | PASS |
| Operating EBITDA, standalone | (5.23) (5.17) (13.97) (27.33) (10.56) (19.15) | (523.28) (517.37) (1,397.32) (2,733.13) (1,055.88) (1,914.69) | L980 + L977 + L976 - L971 | PASS |
| Op EBITDA margin, standalone | -235.7 -120.7 -340.3 -279.9 -188.1 -228.2 % | -235.69 -120.74 -340.29 -279.94 -188.15 -228.17 % | / L970 | PASS |
| Reported EBITDA, standalone | 37.86 47.37 42.24 246.66 79.99 89.62 | 3,785.90 4,737.22 4,224.29 24,665.60 7,999.06 8,961.51 | L980 + L977 + L976 | PASS |
| Core PBT, standalone | (5.83) (6.04) (14.85) (30.03) (11.96) (20.89) | (582.93) (604.12) (1,484.92) (3,002.54) (1,195.92) (2,089.04) | L980 - L971 | PASS |
| OI / PBT, standalone | 115.6 113.0 135.9 112.3 115.2 123.8 % | 115.64 112.99 135.90 112.31 115.22 123.77 % | L971 / L980 | PASS |
| ETR, standalone | 26.18 23.53 31.27 26.34 22.91 27.18 % | same | L983 / L980 | PASS |
| PAT margin, standalone | 1,158.6 749.3 817.6 14,809.3 21,965.8 782.7 % | 1,158.65 749.29 817.62 14,809.34 21,965.80 782.72 % | L988 / L970 | PASS |
| S-C PAT gap (lakhs) and % of standalone | (1,169.37) -45.5; 829.10 25.8; 692.75 20.6; 7,610.16 5.3; 385.53 0.3; 1,521.85 23.2 | same; -45.46 25.82 20.63 5.26 0.31 23.17 % | L853 - L988 | PASS |
| HGHL Q2 gap decomposition | +643.51 -48.74 -0.88 +246.18 -147.32 | sums to 692.75 = gap; HGHL PAT 692.74 | L834/L971, L841/L978, L839/L976, L844, L846/L981, L161 | PASS |
| Unreviewed shares: Q2 PAT, H1 PAT, Q2 TCI, H1 TCI, assets | 17.1 18.8 11.6 14.3 26.2 % | 17.10 18.81 11.56 14.27 26.19 % | L160-L162, L853, L859, L912 | PASS |
| BS gaps: equity, assets, HGHL loans, HGHL cash | 980.05 Cr (46.9%); 981.95; 72,109.16; 235.61 | 98,005.25 (46.88%); 98,194.95; 72,109.16; 235.61 | L915/L1020, L912/L1017, L907/L1012, L905/L1010 | PASS |
| YoY consolidated, Q2 | rev +84.9; Op EBITDA loss +99.3; margin -25.3 pp; D&A +49.7; fin -99.9; EBIT (7.84) to (15.33), +95.6; OI +17.2; core PBT narrowed 23.2 (Rs 4.64 Cr); PBT +53.2; PAT cont +58.6; PAT +188.7; EPS +188.7 | +84.95; +99.26; -25.29; +49.69; -99.88; (783.86) to (1,533.09), +95.58; +17.16; 23.22 (464.06); +53.18; +58.63; +188.66; +188.69 | L833-L864 | PASS (revenue last digit, S7) |
| YoY standalone, Q2 | Op EBITDA +167.0; margin -104.6 pp; fin -62.3; EBIT +155.3; OI +30.5; core PBT +154.7; PBT +11.0; PAT cont +3.4; PAT +30.5; EPS +30.6 | +167.03; -104.60; -62.25; +155.30; +30.46; +154.73; +11.01; +3.35; +30.51; +30.64 | L970-L997 | PASS |
| Q2 YoY drivers (Cr) | OI +9.18; fin +12.13; exc +3.46; tax -4.21; disc +13.40; operating lines -7.49 | 917.50; 1,213.29; 346.15; -420.78; 1,340.11; -749.23 | L833-L852 | PASS |
| Opex growth | employee +109.6; other exp +73.8 YoY, +146.4 QoQ; unallocable exp 146.00 to 1,079.34 | 109.55; 73.76; 146.37; 5,886.19 - 5,740.19 = 146.00; 6,267.02 - 5,187.68 = 1,079.34 | L838, L841, L868, L878 | PASS |
| H1 OI | -11.0; ex-gain 11,802.89 / 11,702.89; like-for-like +2.9 / +3.8; interest share 90.7 | -11.05; same; +2.94 / +3.82; 90.71 | L834, L445, L800, L940 | PASS |
| Step 3 derived quarters | Q1 FY26: rev 3.39, margin -177.0, core (32.32), fin 25.79, exc +12.20. H2 FY26: rev 4.15, margin -436.7, core (29.99), fin 10.60, exc +1.80, land gain 17.90/18.90 | 339.18; -177.05; (3,232.44); 2,578.84; 1,220.09; 415.11; -436.66; (2,999.29); 1,060.19; 180.31; 1,790.30 / 1,890.30 | L833-L844, L444-L445, L799-L800 | PASS |
| Q2 against H1 | revenue -4.2 QoQ; H1 average revenue 4.20; H1 average core (10.73); EMS assets +34.5; EMS income -6.9 | -4.17; 419.57; (1,073.12); +34.53; -6.91 | L833, L843, L834, L882, L866 | PASS (the +34.5% read as capex: F1) |
| Segment table and EMS margins | RL270-RL278 | Every cell matches; margins -61.61 -42.29 -87.50 -14.11 -64.08 -85.98 % | L866-L888 | PASS |
| PAT bridge, Q2 YoY | GP 205.80 (92.7%) to 230.39 (56.1%); +1.75 (1.50) (1.77) (5.68) (0.29) +12.13 +9.18 +3.46 = +17.28; tax (4.21) = volume (5.42) + ETR +1.22; continuing +13.07; discontinued +13.40; net +26.47 | 174.83 -150.24 -176.95 -567.98 -28.89 +1,213.29 +917.50 +346.15 = 1,727.71; 542.45 - 121.68 = 420.77; 1,306.93; 1,340.11; 2,647.04; shares match to 0.1 pp | L833-L853 | PASS |
| OI-revert test | PBT 40.59; PAT 28.84 | 4,059.26; 2,884.04 | L845, L834, L848 | PASS |
| Cash, consolidated H1 | CFO (22.02) to 28.87 (+50.89); pre-WC 9.95 to (4.27); WC (8.84) to 42.22; CFO/PAT -0.02x / 0.36x; CFO/cont PAT -0.29x / 0.36x; FCF (26.22) to 26.14 | (2,202.25) to 2,886.88 (5,089.13); 995.19 to (426.70); (884.08) to 4,222.41; -0.018 / 0.357; -0.290 / 0.364; (2,622.49) to 2,614.25 | L943-L950, L853, L849 | PASS |
| WC days | rec 37.3 / 54.4; inv 260.3 / 66.2 (change -194.0); pay 8,281.8 / 1,337.2; CCC -7,984.2 / -1,216.6 | 37.31 / 54.38; 260.25 / 66.17 (-194.08); 8,281.93 / 1,337.17; -7,984.37 / -1,216.62 | L901, L904, L921, L833, L836-L837 | PASS (last digit, S7) |
| Net cash, loans, tax liabilities | 57.69 to 217.45 (+159.76); loans 2,982.83 to 3,070.99 (+88.16, +3.0%); tax 265.90 to 282.75 (+16.85) | 5,768.98 to 21,745.13 (15,976.15); 8,815.80 (+2.96%); 1,685.34 | L905-L907, L919, L925 | PASS |
| Cash, standalone H1 | CFO (24.31) to 24.22; pre-WC (6.77) to (11.25); WC 2.85 to 42.73; CFO/PAT -0.02x / 0.37x; cont -0.40x / 0.38x; FCF (25.17) to 21.50; interest 97.48 / received 97.66 (100.2%); loans +68.00; OFA -46.07; tax +15.77; net cash 52.32 to 215.10 | every value matches | L1010-L1013, L1029, L1043-L1063 | PASS |
| Treasury | yield 8.42 / 7.28 %; churn 66.5%; received 90.9 / 99.96 %; loans / assets 81.8%; HGHL loans 700.93 to 721.09 | 8.418; 7.282; 66.54; 90.85 / 99.96; 81.85; 70,093.36 / 72,109.16 | L907, L912, L940, L959, L1012, L1043, L1061 | PASS |
| Liquidity after dividend | 217.45 - 148.72 = 68.73; tax bridge 26.37 - 9.09 - 0.43 = 16.85; advance share of cash 51.4% | 21,745.13 - 14,871.75 = 6,873.38; 2,637.06 - 908.83 - 42.90 = 1,685.33 vs 1,685.34; 51.36% | L905-L906, L494, L846, L948, L851, L925, L953 | PASS |
| ROCE H1; operating EBIT H1 | 6.8%; (21.44) | (10,601.07 + 1.81) x 2 / 3,10,717.35 = 6.83%; (1,971.01) - 173.42 = (2,144.43) | L845, L839, L915, L919 | PASS |
| BVPS, P/B, position | 619.46; -2.3% against 634; 0.57x; +7.3% on cost | 619.46; 634.01 at Mar-26 (L915), -2.29%; 0.571; 7.27% | L915, L860 | PASS |
| Question figures | Q16 negative expense 1.96 Cr, write-back 4.53 Cr, 12.7%; Q17 100.79, +4.24; Q18 12.73; Q10 211.90; Q6 206 days | 267.44 - 463.33 = (195.89); 453.22; 12.70%; 10,079.32, +423.83; 1,273.28; 21,189.70; 206 | L872, L850, L938, L852-L853, L916, L834/L971, L902-L903 | PASS |
| Footing gaps carried | R1912 +2.00; R1924 10.00; R2090 +0.20 | 98,090.33 vs 98,092.33; (599.73) vs (609.73); 248.67 vs 248.87 | L960, L966, L997 | PASS |

Arithmetic mismatches above rounding: none. Four last-digit truncations are logged as S7.

---

## 3. ADVERSARIAL READ

A4's review is bearish and well anchored. I took the three most positive claims it makes.

### Claim 1: "Interest is cash-backed"
Where A4 says it: RL327 ("Interest income 110.21 (L940) is 99.96% received in cash"), RL350 ("Received 100.2% of accrued | Interest is cash-backed") and brief RL748 ("Interest is paid in cash, close to 100%").

Strongest bear counter, from the extract. The gross receipt is real. But in the same half the group lent the borrowers more than most of that interest back.
- Consolidated: loans given 1,56,115.79 (L957) less realised 1,47,300.00 (L958) = 8,815.79 net new lending. This ties to the loan-balance rise from 2,98,283.36 to 3,07,099.16 (L907). It is 80.0% of the 11,017.17 interest received (L959). Net cash recovered from the loan book in H1 = 2,201.38 lakhs (Rs 22.01 Cr).
- Standalone: given 1,54,100.00 (L1061) less realised 1,47,300.00 (L1062) = 6,800.00. This is 69.6% of the 9,766.00 interest received (L1063). Net cash recovered = Rs 29.66 Cr.
- The standalone counterparty label is singular: "Loan to Other Company" (L1061-L1062).
- Realisations are identical in the two statements (L958 = L1062). So HGHL lent 2,015.79 net new and realised nil [derived].
- H1 FY26 pattern: standalone net new lending of 1,08,305.00 was 18.5x the 5,866.68 interest received (L1061-L1063). That was the half in which the land-sale cash arrived.

Bull reading: Rs 1,473.00 Cr of principal came back in H1 (L1062), so the borrower(s) can repay at scale.
Bear reading: the borrower pays interest with money it re-borrows from GOCL in the same half. "Cash-backed" then holds on gross flows only.
Separating observation: H1 grants and realisations by borrower. This shows whether the same counterparty rolls the book.

Survives: YES. A4 states net new lending of 68.00 (RL353) but never sets it against interest received. GRAFT REQUIRED (finding M1).

### Claim 2: the Rs 111.68 Cr Kukatpally advance "shows continued appetite"
Where A4 says it: RL735 ("On the positive side, the company received a Rs 111.68 Cr advance"), RL741, and 6D "ON TRACK (advance only)" at RL499.

Strongest bear counter:
- The advance is "net" (L447, L802, L953). It sits as a liability associated with held-for-sale assets (L927). Segment discontinued liabilities went from 100.00 to 11,268.42 (L890).
- No acreage, no deed and no date are given. No acres were sold in H1 FY27, against 133.71 acres in FY26 (L444-L446).
- The detonator cessation approval on the same site has been "initiated" since 28-Nov-2024 (L449-L450).
- The guarantees are charged on company immovable property (L472, L775).

Survives: YES. A4 already carries every element: killing evidence at RL499, Q5 at RL585, Q21 at RL601, the forward-map bear fork at RL770 and "half of it is a buyer's advance" at RL751. No graft needed.

### Claim 3: "Debt-free"
Where A4 says it: RL393 ("the group is debt-free (borrowings nil, L919)"), RL462 (6B #4 GREEN, "not debt"), brief RL752 ("keeps a debt-free balance sheet") and RL757 ("a debt-free parent can fund early losses").

Strongest bear counter:
- Borrowings are nil (L919). But GOCL guarantees Rs 1,316.10 Cr of HNPCL and HEIL bank borrowings, "secured by charge on the Company's immovable properties" (L144, L472, L775).
- That is 62.9% of standalone equity of 2,09,074.08 (L1020) and 42.9% of consolidated equity of 3,07,079.33 (L915) [derived].
- After the dividend, liquid cash is Rs 68.73 Cr against Rs 282.75 Cr of tax liabilities (L905-L906, L494, L925).

Survives: YES, and A4 already carries it: RL72, RL543, RL545 and RL732. No graft needed. Lines RL752 and RL757 state "debt-free" with no qualifier in the same sentence (STYLE S8).

### MANDATORY ACQUISITION-ECONOMICS PROBE: HNPCL Scheme of Merger by Absorption (L44-L47, L479-L484, L782-L787)

Probe result: consideration Rs ND / HNPCL PAT ND = multiple NOT DETERMINABLE from the extract.
- The filing prints no swap ratio and no share count to be issued.
- HNPCL PAT is ND: "no effect of the scheme has been given" (L484), and no HNPCL financials appear. Price/book is also ND, because HNPCL net worth is not given.

Quality markers on file:
- ROCE, cash and customer tenure: ND.
- Debt, as a lower bound only: GOCL guarantees HNPCL bank and FI borrowings of Rs 1,096.10 Cr (L775; Rs 1,096.40 Cr at L472). So HNPCL borrowings are at least about Rs 1,096 Cr [INFERENCE: a guarantee does not exceed the borrowing it backs]. That is 52.4% of GOCL standalone equity (L1020).
- Process: an NCLT bench declined approval on 30-Jul-2026 with "certain observations" (L481). NCLAT set that aside on 25-Sep-2026 (L482).

A4 carries two accretion claims on this acquisition:
- 6D grades "HNPCL merger (Notion: about Rs 3,000 Cr topline, BVPS step-up; also imports debt)" as ON TRACK (RL501).
- The forward-map bull fork reads "the market prices the narrative of a larger book value" (RL768).

What A4 already says: HNPCL "debt, net worth and profit are not in this filing (ND)" (RL542). It also cites a Notion 28% dilution.

What A4 lacks:
- It never states that the purchase multiple cannot be computed.
- Q2 (RL582) asks only for debt and net worth. It does not ask for the swap ratio, the shares to be issued or HNPCL PAT.
- It does not name the document that holds the terms: the Notice and Explanatory Statement the Board reviewed (L49-L52). This run did not receive it.

Result: the bear reading survives. Leverage is the only quality marker on file, and the book-value accretion claim is untested. GRAFT REQUIRED (finding M2).

---

## FINDINGS (tagged)

F1. FACTUAL (loop to A4): the EMS capex evidence and its evidence tier.
- What A4 claims: RL263 lists "EMS segment assets +34.5% QoQ, L882" as evidence that "The EMS capex ... has commissioned without lifting run-rate". RL727 states "This happened after new capacity came into use [FILED Q2]".
- What the extract shows: the filing never mentions capacity. Capitalised CWIP was 76.01 lakhs (L894). H1 group capex was 272.63 (L950). PPE rose 160.11 over H1 (L893).
- The Q2 EMS asset rise was 546.80 (1,583.72 to 2,130.52, L882). That is twice the H1 group capex, and it follows a Q1 fall of 233.94 (1,817.66 to 1,583.72). Over H1, EMS assets rose 312.86 (+17.2%). Most of the Q2 jump is not fixed assets [derived].
- Fix: re-tag RL727 as [INFERENCE]. At RL263, state that the capitalised amount was Rs 0.76 Cr. Either drop the +34.5% as capex evidence or label it as total segment assets including working capital. The RED grade can stand on the CWIP-to-nil test. RL392 already gives the correct scale.

M1. MISSING (loop to A4): the surviving bear counter to "Interest is cash-backed" is not in the review. Graft these five changes:
- Add a row to Step 5-III: "Net new lending / interest received, H1 FY27: consolidated 80.0% (8,815.79 / 11,017.17; L957-L959); standalone 69.6% (6,800.00 / 9,766.00; L1061-L1063). Net cash recovered from the loan book: Rs 22.01 Cr consolidated, Rs 29.66 Cr standalone. Standalone counterparty label singular, 'Other Company' (L1061)."
- At RL327 and RL350, replace "Interest is cash-backed" with "Interest is received gross. Net of fresh lending to the same book, 70-80% went back out."
- Add the same qualifier to brief RL748.
- Add "borrower-level H1 grants and realisations" to missing-evidence item (2) at RL397.
- Extend Q1 (RL581) with "and H1 amounts lent and realised, by borrower".

M2. MISSING (loop to A4): the acquisition-economics frame for the HNPCL scheme is absent. Graft these changes:
- In Step 6D (RL501) and the position read (RL542), add: "Purchase multiple: NOT DETERMINABLE from this filing. Swap ratio, shares to be issued, HNPCL PAT and net worth are not disclosed (L479-L484). Source: the Notice and Explanatory Statement the Board reviewed (L49-L52), not in this run's inputs."
- Mark the Notion "BVPS step-up" as untested from the filing.
- Extend Q2 (RL582 and the YAML) to ask for the swap ratio, the shares to be issued, and HNPCL FY26 PAT and net worth.

CONTRADICTION: none.

---

## VERDICT

VERDICT: INCOMPLETE. Loop back to A4.
- F1 (FACTUAL): RL263 and RL727 overstate the EMS capex evidence and tag an inference as FILED.
- M1 (MISSING): the net-new-lending against interest-received counter is not grafted (L957-L959, L1061-L1063).
- M2 (MISSING): the HNPCL purchase multiple is not stated as ND, the missing inputs and source document are not named, and Q2 lacks the swap ratio and HNPCL PAT.
All three are text grafts to A4. No A2 or A3 re-run is needed. Arithmetic: clean. Coverage: no orphans. The one ledger diff is STYLE.

---

## STYLE NOTES (logged, no loop)

- S1 (A2). The ledger lacks consolidated CF line L956, "Repayment of loans from Companies". No value prints in either period (A1 header L930). Append it as line 232, ZERO_STANDING, label only, citing L956 (no row ID). This changes no figure, fact or conclusion in the review. I logged it as STYLE because the line carries no value. The operator may overrule.
- S2 (A1). Five pending units carry ENTITY, QUALIFIER or DATE tags, not FORWARD: L434-L435, L449-L450, L563-L567, L793 and L801-L802. Row R1239 says "ceased". L449-L450 says the Board "decided to cease ... and initiated the requisite approval".
- S3 (A1). SEBI (L37, L110) and ICAI (L104, L531) appear only in boilerplate. They are not ENTITY rows, which is acceptable.
- S4 (A2). Three mapping issues in the ledger:
  - Auditor para C1 maps to Board-letter rows R1370-R1371 (L40, L42), not to the auditor scope paragraph at L88.
  - Paras C2 and S1-S3 carry no row ID ("page group").
  - The RESTATED flag marks duplicate consolidated and standalone notes, but no figure was restated.
- S5 (A1). R1606 and R2073 place the reserves figure in the H Sep30,2025 column. The values equal the Mar-26 balance-sheet other equity (L914 3,13,302.40; L1019 2,16,389.43), so they likely belong in the FY Mar-26 column. A4 does not use them.
- S6 (A4). RL7, RL429 and the YAML review_path (RL860) point to a separate review_gocl_q2fy27.part2.md. That file does not exist; Part 2 is appended in this file at RL430. Fix the layout line and review_path before save.
- S7 (A4). Last-digit rounding, with no conclusion affected:
  - Revenue YoY +84.9% (exact +84.95%) at RL205, RL222 and RL237.
  - Inventory-days change -194.0 (exact -194.1) at RL331.
  - Mar-26 payable days 8,281.8 (8,281.9) and CCC -7,984.2 (-7,984.4) at RL332-RL333.
  - "about Rs 4.2 Cr" for Q1 FY27 revenue (4.29) at RL261.
- S8 (A4). Brief RL752 ("keeps a debt-free balance sheet") and RL757 ("a debt-free parent can fund early losses") need an in-sentence qualifier. The qualifier: Rs 1,316.10 Cr of guarantees secured on company property (L472, L775), and post-dividend liquid cash of Rs 68.73 Cr against Rs 282.75 Cr of tax. The review carries both points elsewhere.
- S9 (A4, optional). The consolidated CF adds back an unrealised FX loss of 746.24 (H1 FY27) and 2,584.45 (H1 FY26) at L941. The standalone CF shows a gain of 8.82 and a loss of 51.68 (L1044).
  - So about Rs 7.55 Cr (H1 FY27) and Rs 25.33 Cr (H1 FY26) sit outside the standalone.
  - Its P&L line cannot be placed. HGHL other income equals HGHL interest income exactly: 12,149.48 - 10,876.20 = 11,021.19 - 9,747.91 = 1,273.28.
  - Consider adding it to Q18, beside the exceptional FX gain the review strips out.
- S10 (A4, optional). The "quarter split ND" for the H1 FY26 land gain (RL254) can be resolved.
  - Realty segment income was 2,123.55 in Q1 FY26 (2,240.64 - 117.09, L867) against 117.09 in Q2 FY26.
  - So the gain sat in Q1 FY26, and the Q2 YoY OI comparison is like-for-like [derived].
- S11 (A4, optional). Two evidence-tier fixes:
  - RL741 "Hyderabad land demand let GOCL sell" is a causal inference under a [FILED Q2] tag.
  - RL728 "Corporate cost jumped Rs 7.95 Cr" uses the consolidated other-expense change (L841). The "corporate" label comes from A3's derived unallocable-cost read.
- S12 (informational; no change needed).
  - Borrowings of 61.52 at Mar-26 (L919) reached nil with no repayment line. Finance cost paid of 63.93 (L963) = 61.52 + 2.41 (L942) [derived], so the repayment likely sits inside "finance cost paid".
  - IDL sale proceeds of 10,700.00 print in the H1 FY26 column (L952, L1056), but the sale date is 15-Nov-2025 (L454).
  - Both are immaterial to Q2 FY27.

---

```yaml
stage: A5-adversary
company: "GOCL"
quarter: "Q2 FY27"
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
  orphan_rows: []
  missing_from_ledger:
    - "L956 consolidated CF 'Repayment of loans from Companies': label only, no value printed either period, no structured row (A1 header L930). Tagged STYLE S1, no loop; A2 appends as line 232."
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Interest is cash-backed (RL327, RL350, brief RL748)", counter: "H1 net new lending equals 80.0% of interest received consolidated (8,815.79 / 11,017.17) and 69.6% standalone (6,800.00 / 9,766.00); net cash recovered from the loan book Rs 22.01 Cr / Rs 29.66 Cr; standalone counterparty singular 'Other Company'", source_line: "L957-L959, L907, L1061-L1063, L1012", type: MISSING}
  - {claim: "HNPCL merger ON TRACK with Notion BVPS step-up (RL501); bull fork 'larger book value' (RL768)", counter: "Purchase multiple NOT DETERMINABLE: no swap ratio, shares issued, HNPCL PAT or net worth in filing; only quality marker on file is leverage, guaranteed HNPCL borrowings at least Rs 1,096.10 Cr = 52.4% of standalone equity; NCLT declined 30-Jul-2026 before NCLAT reversal", source_line: "L479-L484, L775, L472, L1020, L481-L482, L49-L52", type: MISSING}
  - {claim: "Debt-free balance sheet / debt-free parent can fund losses (brief RL752, RL757)", counter: "Rs 1,316.10 Cr guarantees secured on company immovable property = 62.9% of standalone equity; post-dividend liquid cash Rs 68.73 Cr vs tax Rs 282.75 Cr; already carried elsewhere in review, qualifier missing in-sentence", source_line: "L144, L472, L775, L1020, L905-L906, L494, L925", type: STYLE}
findings_by_type:
  factual:
    - "F1 (A4): RL263 cites EMS segment assets +34.5% QoQ as commissioned-capex evidence and RL727 tags 'new capacity came into use' as [FILED Q2]; filing never states capacity; capitalised CWIP Rs 0.76 Cr (L894), H1 capex Rs 2.73 Cr (L950), Q2 EMS asset rise Rs 5.47 Cr after Q1 fall Rs 2.34 Cr (L882). Re-tag as INFERENCE; state capitalised amount; drop or relabel the +34.5%."
  missing:
    - "M1 (A4): graft net-new-lending vs interest-received counter into Step 5 (RL327, RL350, 5-III), brief RL748, missing-evidence RL397 and Q1 RL581 (L957-L959, L1061-L1063)."
    - "M2 (A4): state HNPCL purchase multiple NOT DETERMINABLE (swap ratio, shares issued, HNPCL PAT, net worth absent, L479-L484); name the Notice and Explanatory Statement (L49-L52) as missing source; mark 6D BVPS step-up untested; add swap ratio and HNPCL PAT to Q2 (RL582)."
  contradiction: []
  style:
    - "S1 (A2): ledger lacks blank-label line L956; append as line 232."
    - "S2 (A1): five pending units not tagged FORWARD; R1239 'ceased' overstates L449-L450."
    - "S3 (A1): SEBI and ICAI named in boilerplate only, not ENTITY rows."
    - "S4 (A2): auditor para C1 mapped to Board-letter rows; C2, S1-S3 no row ID; RESTATED used for duplicate notes."
    - "S5 (A1): R1606/R2073 reserves in H Sep30,2025 column equal Mar-26 other equity (L914, L1019)."
    - "S6 (A4): RL7, RL429, YAML review_path name a non-existent part2 file."
    - "S7 (A4): last-digit truncations (revenue YoY 84.9 vs 84.95; inventory days -194.0 vs -194.1; payable days, CCC; Q1 revenue 'about 4.2')."
    - "S8 (A4): brief RL752 and RL757 'debt-free' need in-sentence guarantee and liquidity qualifier."
    - "S9 (A4, optional): unrealised FX loss add-back L941 vs L1044 (about Rs 7.55 Cr outside standalone H1 FY27) unplaced in P&L; add to Q18."
    - "S10 (A4, optional): H1 FY26 land gain sat in Q1 FY26 per realty segment income L867; RL254 'quarter split ND' resolvable."
    - "S11 (A4, optional): RL741 causal clause and RL728 'corporate cost' label carry FILED tags on inference."
    - "S12 (info): borrowings 61.52 repaid inside finance cost paid 63.93 (L919, L942, L963); IDL proceeds in H1 FY26 column before 15-Nov-2025 sale date (L952, L454)."
loop_back_to: "A4"
gap: "A4 text grafts only: (F1) RL263/RL727 EMS capex evidence and FILED tag unsupported, CWIP Rs 0.76 Cr vs Q2 EMS asset rise Rs 5.47 Cr (L882, L894, L950); (M1) add net new lending vs interest received, consolidated 80.0% re-lent and Rs 22.01 Cr net recovered (L957-L959), standalone 69.6% and Rs 29.66 Cr (L1061-L1063), to Step 5, brief RL748, RL397 and Q1; (M2) state HNPCL purchase multiple NOT DETERMINABLE with swap ratio, shares issued, HNPCL PAT and net worth named as missing (L479-L484), source Explanatory Statement (L49-L52) not in inputs, add them to Q2, mark 6D BVPS step-up untested."
style_notes:
  - "S1 L956 blank label missing from ledger (A2)"
  - "S2 FORWARD tagging gaps; R1239 descriptor (A1)"
  - "S3 SEBI/ICAI boilerplate entities (A1)"
  - "S4 auditor-para mapping and RESTATED usage (A2)"
  - "S5 reserves column placement R1606/R2073 (A1)"
  - "S6 part2 file reference (A4)"
  - "S7 last-digit truncations (A4)"
  - "S8 debt-free qualifier in brief (A4)"
  - "S9 FX loss add-back question (A4, optional)"
  - "S10 land-gain quarter resolvable (A4, optional)"
  - "S11 provenance tags RL741, RL728 (A4, optional)"
  - "S12 finance-cost-paid and IDL proceeds timing (info)"
analyst_note: "A4's arithmetic is clean: every derived cell recomputes from the image-transcribed lines to rounding, and the review is bearish and well anchored. The gaps sit in its positive claims. 'Interest is cash-backed' holds on gross receipts only. In H1 the group lent a net Rs 88.16 Cr back out, 80% of the Rs 110.17 Cr interest it received, and the standalone counterparty prints as a single 'Other Company'. That is the strongest bear counter on file, and A4 does not state it. The HNPCL scheme is an acquisition by absorption. The filing carries no swap ratio and no HNPCL earnings, so the purchase multiple cannot be computed. Yet A4 grades the merger ON TRACK on a Notion 'BVPS step-up' and asks only for debt and net worth. The terms sit in the Explanatory Statement the Board reviewed (L49-L52), which this run did not receive. The one ledger diff (L956) is a blank cash-flow label with no value in either period. I logged it as STYLE, not a loop; the operator may overrule. All three loop items are text grafts to A4."
```
