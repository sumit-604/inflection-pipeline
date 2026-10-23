# A5 ADVERSARY / COMPLETENESS AUDIT: PAISALO Q2 FY27

- Stage: A5 adversary | model: claude-opus-5-5 | run date: 2026-10-23 (resumed after machine restart; no prior partial output existed)
- Under audit: work/review_paisalo_q2fy27.md (A4, 1,186 lines)
- Inputs read: A1 fulltexts (results, presentation, concall), A2 ledgers (results, presentation, concall). Read-only. No source PDF opened. Nothing under inputs/ opened. A3 reasoning not read.
- Anchor conventions: `RF l.N` = results fulltext line; `DK L.N` = presentation fulltext line; `CC l.N` = concall SOURCE line (ASR); `rev l.N` = A4 review line; `(c)` = my arithmetic.

---

## AUDIT 0: DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business_model PRESENT | competition PRESENT | forward_map PRESENT. Gate PASS.

| Part | Heading (rev line) | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | "### 1. SUMMARY NARRATIVE" (rev l.1014) | 18 lines (rev l.1015-1032), inside the 10-20 band; each line tagged FILED / MGMT / INFERENCE / Notion | PRESENT |
| 2. Sector intelligence | "### 2. SECTOR INTELLIGENCE" (rev l.1034) | 5 bullets: rate cycle, monsoon, co-lending regulation, funding mix (73% vs 69%, ties DK L.1155-1157), peer gap stated UNVERIFIABLE | PRESENT |
| 3. Business-model intelligence | "### 3. BUSINESS-MODEL INTELLIGENCE" (rev l.1041) | 8 bullets: ticket, spread, fee share, opex/AUM, credit cost, ROE mix, model drift, non-disclosures | PRESENT |
| 4. Competition intelligence | "### 4. COMPETITION INTELLIGENCE" (rev l.1051) | 5 bullets: reach, funding-cost disadvantage, state concentration (ties DK L.407-408, L.1173-1179), UGRO, yield-pricing test | PRESENT |
| 5. Forward map | "### 5. FORWARD MAP" (rev l.1058) | make-or-break reading plus 11 dated catalysts, each with a bull fork and a bear fork | PRESENT |

---

## AUDIT 1: COVERAGE (fresh enumeration over A1 fulltexts, diffed against A2 ledgers)

| Category | A2 count | My fresh count | Method (fulltext lines) | Orphan rows | Status |
|---|---|---|---|---|---|
| Results: numbered notes | 9 | 9 | grep `^\d\.` RF l.564, 567, 568, 572, 573, 598, 601, 603, 607 | none | PASS |
| Results: footnotes | 8 | 8 | CP discount prices RF l.588, 592, 596; DRR exemption l.619-620; Net Worth definition l.627; stray asterisk l.1070; UDIN garbled l.717, l.784 | none | PASS |
| Results: statement line items | 251 | 251 | hand count of value rows: SA P&L 50 (l.799-857), SA BS 36 (l.880-924), SA CF 35 (l.947-985), CON P&L 56 (l.1004-1069), CON BS 39 (l.1093-1140), CON CF 35 (l.1162-1200) | none | PASS |
| Results: Reg 52 ratio rows | 22 (14 R-rows + 8 M-rows) | 22 | lettered rows a to s-iii, RF l.1214-1237; the 8 M-rows (b, c, d, f value, o, p, q, s) confirmed at l.1215, 1216, 1217, 1219, 1230, 1231, 1232, 1234 | none | PASS |
| Results: note 5 issuance lines | 10 | 10 | 7 NCD series RF l.579-585 + 3 CP series l.586, 590, 594 | none | PASS |
| Results: agenda items | 2 | 2 | RF l.49, l.52 ("inter alia") | none | PASS |
| Results: auditor paragraphs | 10 | 10 | SA l.678, 684, 691, 699; CON l.739, 746, 753, 760, 765, 767; no EoM, Other Matter or going-concern text found | none | PASS |
| Presentation: slides | 42 | 42 | `[page N]` markers DK L.18-915 (42), 6 dividers + index with no rows | none | PASS |
| Concall: speaker turns | 40 | 40 | re-derived from moderator cues and question marks (CC l.022, 032, 167-168, 246-251, 326-341, 374-376, 385, 398-412, 418, 442-446, 497-516, 530-532, 558-566, 575-576, 599-603, 634-642, 656-663, 677) | none | PASS |
| Concall: questions | 12 | 12 | Mehta 4 (l.347-355, 376, 384-385, 397-398); Manar 2 (l.414-417); Shah 2 (l.447-448, 497); Reizada 1 (l.517-530); Suthaki 3 (l.573-575, 601-602, 637-641) | none | PASS |
| Concall: analysts | 5 | 5 | l.339, 411, 445, 514, 565 | none | PASS |
| Concall: defensive phrases (A4 Step 6C) | 9 (A4) | 9 | "we believe" l.152, 667; "we expect" family l.078, 195, 214, 365, 379, 391; "early to draw definitive conclusions" l.201 | n/a | PASS |

Ledger-to-review check:
- A4 cites all 9 notes in its Step 0D table (rev l.79-88), all 8 footnotes (rev l.88) and all 8 M-rows (rev l.28).
- A4 cites all 12 questions in Step 4A (rev l.707-718). Substantive turns R001-R014, R016-R018, R020-R024, R027-R028, R030-R036 and R039 are cited by line.
- Some units carry no line citation: 8 zero-content turns (R015, R019, R025, R026, R029, R037, R038, R040: thanks and moderator reminders, CC l.409-410, 442-444, 506-516, 559-563, 656-662, 677-681) and some slides (S1-S3, S11 apart from L.240, S17, S32, S35, S36, S38, S41, S42, plus the dividers). The preamble's explicit statement covers them: "All 9 notes, 40 turns and 42 slides reviewed ... No ledger row is unreviewed" (rev l.24, l.32). I read S11, S32 and S41 (DK L.222-248, L.712-739, L.890-914). None holds a load-bearing item that A4 lacks (see STYLE S5).
- Orphan rows: NONE. Rows missing from the ledger: NONE.

Coverage verdict: PASS.

---

## AUDIT 2: ARITHMETIC (recomputed from raw extracted numbers; Rs Lakhs x0.01 = Rs Cr; deck Rs Mn)

| # | Metric (A4 location) | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|---|
| 1 | CON NII Q2 FY27 / Q1 FY27 / Q2 FY26 (1L-A) | 135.66 / 134.93 / 109.94 | 135.66 / 134.93 / 109.94 | RF l.1004, l.1017 | PASS |
| 2 | CON NII FY26 / H1 FY26 / H1 FY27 | 530.39 / 216.55 / 270.59 | 530.39 / 216.55 / 270.59 | RF l.1004, l.1017 | PASS |
| 3 | CON other/fee income, all 6 columns | 16.30 / 9.77 / 11.98 / 38.98 / 34.13 / 21.75 | same | RF l.1005, 1007, 1008 | PASS |
| 4 | CON opex, all 6 columns | 44.84 / 46.77 / 60.45 / 207.52 / 88.13 / 107.22 | same | RF l.1025-1027 | PASS |
| 5 | CON PPOP, all 6 columns; PPOP less provisions less exceptional = PBT | 80.92 / 97.94 / 87.19 / 361.35 / 162.07 / 185.13 | same; ties to PBT 69.00 / 82.21 / 87.43 / 318.41 / 132.60 / 169.64 | RF l.1019-1031 | PASS |
| 6 | SA NII / other / opex / PPOP, all 6 columns (1L-B) | e.g. Q2 132.36 / 11.95 / 58.03 / 86.28 | same in every column | RF l.799-826 | PASS |
| 7 | Tax lines CON and SA, all columns | CON 17.46 / 20.89 / 21.79 / 81.20 / 33.88 / 42.68 | same (SA also ties) | RF l.828-829, l.1033-1034 | PASS |
| 8 | C/I CON Q2 FY26 / Q1 / Q2 / H1 FY27 | 35.52 / 32.32 / 40.95 / 36.68% | 35.52 / 32.32 / 40.95 / 36.68% | RF l.1015, 1017, 1025-1027 | PASS |
| 9 | C/I SA Q2 FY26 / Q1 / Q2 | 36.66 / 30.90 / 40.22% | same | RF l.810, 812, 820-822 | PASS |
| 10 | C/I on NII CON | 40.79 / 34.66 / 44.56% | same | (c) | PASS |
| 11 | Credit cost annualised Q1 / Q2 / H1 | 0.98% / -0.01% / 0.46% | 62.92/6,404.15 = 0.98%; -0.96/6,986.65 = -0.01%; 15.49/6,683.4 x2 = 0.46% | RF l.1021; DK L.1023 | PASS |
| 12 | RoA filed Q1 / Q2 / H1 | 3.73 / 3.63 / 3.65% | 245.24/6,582.47; 262.56/7,235.13; 253.92/6,952.40 | RF l.1035, l.1113; DK L.970 | PASS |
| 13 | RoE filed Q1 / Q2 / H1 | 13.46 / 13.86 / 13.62% | 245.24/1,822.44; 262.56/1,893.93; 253.92/1,864.47 | RF l.1140; DK L.977 | PASS |
| 14 | YoY CON: NII, net total income, PPOP, interest income, finance cost, D&A, fees, other/fee, PBT, PAT, EPS (Step 2) | +23.4, +17.0, +7.7, +27.7, +32.6, +151.9, -39.6, -26.5, +26.7, +27.4, +26.3% | identical | RF l.1004-1035, l.1062 | PASS |
| 15 | YoY SA: NII, NTI, PPOP, FC, II, PBT, PAT, EPS | +27.0, +19.8, +13.8, +34.2, +30.5, +26.9, +28.0, +26.8% | identical | RF l.799-848 | PASS |
| 16 | Core PPOP ex-treasury CON / SA | 81.86 to 85.33 (+4.2%) / 76.75 to 84.42 (+10.0%) | CON same; SA Q2 FY26 76.74 (7,673.55 lakh); YoY +10.0% unchanged | RF l.803, 808, 814 | PASS (rounding, STYLE S4) |
| 17 | Core PPOP ex-treasury QoQ (Section C) | -12.1% | 97.10 to 85.33 = -12.1% | RF l.1005-1027 | PASS |
| 18 | Core PBT ex-treasury CON / SA | 69.94 to 85.57 (+22.3%) / 69.20 to 84.80 (+22.5%) | same | RF l.1031, l.826 | PASS |
| 19 | ETR Q2 FY26 / Q1 / Q2 | 25.30 / 25.41 / 24.92% | 1,745.72/6,900.09; 2,089.11/8,220.51; 2,178.91/8,743.04 | RF l.1031-1034 | PASS |
| 20 | 4A YoY PAT bridge (core +3.49 to +2.61, 18.5%; treasury +2.79 to +2.08, 14.8%; provisions +12.16 to +9.08, 64.4%; ETR +0.33, 2.3%) | sum +14.10 | 2.61+2.08+9.08+0.33 = 14.10 = 65.64-51.54 | RF l.1004-1035 | PASS |
| 21 | 4B QoQ bridge (NII +0.73, fees +1.19, FV +1.03, opex -13.69, provisions +15.98, ETR +0.43) | PAT +4.33 (+7.1%) | 4.34 vs 4.33 (rounding); 432.73/6,131.40 = +7.06% | RF l.1004-1035 | PASS |
| 22 | Provisions at Q2 FY26 level: PBT | 75.27, +9.1% | 87.19-11.92 = 75.27; /69.00 = +9.1% | (c) | PASS |
| 23 | Step 3 deck: H2 FY26 NII 3,187 / opex 1,202 / PPOP 1,985 / prov 127 / PAT 1,385; Q2 PPOP -12.1% vs H2 avg; AUM +19.1% | as stated | 5,694-2,507; 2,088-886; 422-295; 2,372-987; 872/992.5; 72,659/61,009 | DK L.930-936, L.991-995, L.1023 | PASS |
| 24 | Implied Q3 PPOP to hold PAT 656 with provisions 157 | about 1,031 (+18%) | 656/0.751+157 = 1,030.5; /872 = +18.2% | (c) | PASS |
| 25 | CFO ex-loan growth / PAT: SA H1 FY27, SA H1 FY26, CON H1 FY27, SA FY26 | 119.95 (0.95x) / 86.09 (0.88x) / 121.27 (0.96x) / 224.07 (0.95x) | same | RF l.959, 968, 1174, 1183 | PASS (arithmetic; reading qualified by M2) |
| 26 | SA-vs-CON PAT gap % of SA PAT | 0.90 / 0.74 / 1.45 / 0.82 / 1.28 / 1.07% | same | RF l.834, l.1035 | PASS |
| 27 | Note 5 total; weighted NCD coupon | Rs476.98 Cr; 10.26% | 294.92+124.47+57.59 = 476.98; 4,301.15/419.39 = 10.26% | RF l.579-596 | PASS |
| 28 | Paid-up capital change; FCCB equity | +0.51%; Rs21.17 Cr | 9,142.11/9,095.84 = +0.51%; 2,116.50 lakh | RF l.845, l.981 | PASS |
| 29 | Fee share of total income Q2 FY27 / Q2 FY26 | 3.65% / 7.48% | 1,012.47/27,730.77; 1,675.80/22,401.42 | RF l.1007, l.1015 | PASS |
| 30 | AUM YoY; disbursement YoY and QoQ | +33.3%; +42.2%, -9.5% | 72,659/54,494; 15,673/11,025; 15,673/17,309 | DK L.1023 | PASS |
| 31 | Headcount, touchpoints, AUM/employee, employee cost per head | -10.8%, +46.5%, 16.7 to 25.0 Mn, +18.1% | same | DK L.1008, L.1018; RF l.1025 | PASS |
| 32 | AUM / deck net worth; top-5 states | 3.83x; 87.7% | 72,659/18,981; 26.2+20.1+15.2+13.4+12.8 | DK L.1023, L.1057, L.1173-1179 | PASS |
| 33 | P/B on filed CON book; price vs entry max / MoS | 3.74x (book Rs21.18); 2.14x / 2.73x | 1,93,596.20/9,142.11 = Rs21.18; 79.3/21.18 | RF l.1140, l.845 | PASS |
| 34 | Nupur: revenue YoY, implied C/I, other-expense multiple, debt securities, cash, CF-vs-BS borrowings gap | -39.3%; 11.9% to 72.6%; 11.5x; Rs55.70 Cr; Rs42.95 Cr; Rs49.02 Cr | 496.80/818.42; 68.93/581.05 to 241.92/333.21; 195.34/17.05; 1,51,139.36-1,45,569.36; 9,959.80-5,664.56; 87,046.23-82,143.85 lakh (SA CF ties exactly at 84,585.13) | RF l.808-822 vs l.1013-1027; l.880, 911, 975 vs l.1093, 1124-1125, 1190 | PASS |
| 35 | Reg 52 "net profit margin" basis; PAT margin | PBT/TI 31.93 / 31.55%; 23.90% | 16,825.87/52,695.98; 16,963.55/53,759.69; 12,591.92/52,695.98 | RF l.1233, l.808, l.826 | PASS |
| 36 | SA H1 C/I if deferred-expense build is expensed | 35.6% to about 41.9% | 101.52/285.03; (101.52+17.91)/285.03 | RF l.899, l.820-822, l.810-812 | PASS |
| 37 | Q&A share; specificity; credibility; hedge count | 49%; 0.62; 90%; 9 | 18.17/37.15 min; 13/21; 4.5/5; 2+6+1 | CC l.003, l.329, l.660 | PASS |
| 38 | Fully diluted share uplift | +8.4%, about 76.8 Mn | 46.50/42.90 = 1.0839; x914.2 Mn | DK L.781, L.788 (inputs as cited); DK L.371 | PASS |
| 39 | Deck p28 credit-cost gap (QfM 5) | Rs6-8 Cr | 0.35-0.45% x 72,351.5 Mn avg assets / 4 = Rs6.3-8.1 Cr | DK L.952, L.970 | PASS |
| **40** | **Step 1 opening-claims quantified share (rev l.630)** | **30 of 44 = 68%** | **29 of 44 = 65.9%**: A4's own table marks YES on rows 2, 3, 5-10, 14-16, 18-21, 23, 24, 30, 33-43 (29) and NO on 15 | **rev l.584-627 (built from CC l.037-322)** | **FAIL (F1)** |
| **41** | **FY19-FY21 credit-cost range (Step 5L Q1, rev l.327)** | **"3.1-3.8%"** | **3.1% / 3.8% / 2.4%, so the range is 2.4-3.8%** (FY19@660 3.1%, FY20@781 3.8%, FY21@942 2.4%). A4's own QfM 6 (rev l.508) prints 3.1, 3.8 and 2.4 | **DK L.1104-1107, L.1131** | **FAIL (F2)** |

Arithmetic verdict: 39 of 41 PASS. 2 FACTUAL mismatches; neither changes a conclusion (see F1, F2).

---

## AUDIT 3: ADVERSARIAL READ (three most positive claims, bear counters from the same extract)

### P1. "Asset quality GREEN; Elite asset-quality multiplier (x1.15) holds" (rev l.296-297, l.327, l.384-385, l.460; brief l.1029 "Bad loans stay low at 0.66%")
- **Strongest bear counter:** the GNPA ratio sits on a growing, unseasoned denominator, and the stock of bad loans rose.
  - GNPA% x AUM, a proxy because the GNPA denominator is not disclosed (loan assets sit within 2.1% of AUM, DK L.964 vs L.1023): Rs441 Mn (Q2 FY26, 0.81% x 54,494) to Rs470 Mn (Q1 FY27, 0.70% x 67,074) to Rs480 Mn (Q2 FY27, 0.66% x 72,659). That is +8.6% YoY and +2.1% QoQ (c) (DK L.1023, L.1029-1032).
  - One-year-lagged GNPA ratio: 480 / 54,494 = 0.88%. That is above the 0.81% printed a year ago (c).
  - H1 FY27 disbursement was 17,309 + 15,673 = 32,982 Mn, or 45.4% of 30-Sep AUM. Q2 alone (15,673 Mn, 21.6% of AUM) cannot be 90+ days past due by 30-Sep (DK L.1023) (c).
  - Agri repayments are half-yearly. Management says it is "early to draw definitive conclusions" and dates the test to end-Oct or early-Nov (CC l.197-202, l.212-213).
- **What A4 already has:** write-off-driven history (FN25), two GNPA histories (FN14), the p28 credit-cost mismatch (FN11) and drought stress (C07). A4 has NOT computed the denominator or seasoning effect (no "absolute", "lagged" or "season" analysis anywhere in the review).
- **Survives:** YES. **Graft into A4:** Step 5L mandatory question 1, Step 7 pillar 2 row, and brief summary line l.1029. Type MISSING (M1).

### P2. "AUM +33.3% YoY, above the Bull scenario; growth GREEN" (rev l.302, l.367, l.383, l.416)
- **Strongest bear counter:** the growth does not turn into earnings, and it is bought with capital.
  - NII +23.4% and core PPOP ex-treasury +4.2% against AUM +33.3% (RF l.1004-1027).
  - Q2 disbursement fell 9.5% QoQ, although management calls it back-ended "record" disbursement (DK L.146, L.1023; CC l.420-421).
  - D/E rose from 2.41x (SA, 31-Mar) to 2.83x. CRAR fell from 35.8% to 30.7% in two quarters (RF l.911-923, l.1214; DK L.1060-1063).
  - ROA is at the Bear scenario while growth is above Bull.
- **Survives:** YES, but A4 already carries it: Step 2 diagnostics 1 and 3 (rev l.220-222), Step 5L CRAR and D/E rows (rev l.305-306), Step 6A ROA at Bear (rev l.368), FN24 equity-need monitorable (rev l.1003). **No graft required.**

### P3. "Cash conversion growth-induced; CFO excluding loan growth covers 0.95x of PAT" (rev l.321-324, l.963)
- **Strongest bear counter:** the H1 multiple is flattered by tax timing.
  - SA H1 FY27 current tax was Rs38.45 Cr (RF l.828). Income tax paid in cash was Rs3.07 Cr (RF l.964).
  - The opening current-tax asset of Rs24.66 Cr was absorbed (RF l.890) and a Rs10.79 Cr liability was built (RF l.917). That is a Rs35.38 Cr H1 tailwind.
  - Tax-normalised SA CFO ex-loan growth: 119.95 - 35.38 = 84.57, or 0.67x PAT (c). CON: 121.27 - 34.94 = 86.33, or 0.68x (RF l.1033, l.1179) (c).
  - H1 FY26 on the same basis: 86.09 - 20.28 = 65.81, or 0.68x (RF l.828, l.964). The H1 shortfall is seasonal.
  - FY26 full year is clean: tax paid Rs72.33 Cr vs current tax Rs72.26 Cr, ratio about 0.95x. So the "growth-induced" class survives on the full-year basis, not on the H1 0.95x.
- **What A4 already has:** the deferred-expense point (rev l.324). Tax paid is not discussed anywhere.
- **Survives:** YES, as a qualifier. **Graft into A4:** Step 5L cash-quality paragraph and the Section C cash-conversion row. Type MISSING (M2).

### Mandatory acquisition-economics probe
- **What the corpus describes:** no company acquisition, purchase of a business, or target with stated PAT. The only stake buy is the promoter group's Q1 FY27 purchase (DK L.153-157). Promoter shares went from 379.7 to 425.1 Mn, +45.4 Mn = 4.99% of the FY26 base of 909.5 Mn (DK L.365, L.1163) (c).
- **Price:** NOT FOUND in the extract, so price / earnings cannot be computed.
- **Nearest priced equity transaction:** the Q2 FCCB conversion at Rs45.74 (RF l.598). That is about 16.5x H1-annualised CON EPS (45.74 / 2.78) and 2.16x 30-Sep CON book per share (45.74 / 21.18) (c). It is an issue price, not a purchase by the company, and dilution is bounded at +0.51% (RF l.845).
- **Bear reading:** "underscoring confidence" (DK L.155-157) cannot be priced. The 4.99% sits at the SAST 5% creeping limit. A4 already carries this (FN06, QfM 15, flag rev l.1176). **No graft required.**

---

## FINDINGS BY TYPE

FACTUAL (loop A4):
- **F1.** Step 1 diagnostics (rev l.630) say "Quantified: 30 of 44 = 68%". A4's own table (rev l.584-627) supports 29 of 44 = 65.9%. Fix the count; the "backward-heavy" conclusion stands.
- **F2.** Step 5L question 1 (rev l.327) says "FY19-FY21 credit cost ran 3.1-3.8%". The deck p13 series gives FY21 = 2.4% (DK L.1107 at FY21 x930, L.1131), so the range is 2.4-3.8%. It also conflicts with A4's own QfM 6 (rev l.508). The write-off conclusion stands.

MISSING (loop A4):
- **M1.** P1 surviving bear counter: the GNPA denominator and seasoning effect (figures in Audit 3, P1) are absent from Step 5L Q1, the Step 7 pillar 2 row and brief l.1029.
- **M2.** P3 surviving bear counter: the H1 tax-timing qualifier on the 0.95x cash conversion (figures in Audit 3, P3) is absent from the Step 5L cash paragraph and the Section C row.

CONTRADICTION: none beyond F2's internal mismatch, which is tagged FACTUAL.

---

## VERDICT

**VERDICT: INCOMPLETE.** Loop back to **A4**. Findings: 2 FACTUAL (F1, F2) and 2 MISSING (M1, M2).
- No A2 or A3 re-run is needed. Coverage is clean: no orphan rows and no rows missing from the ledger.
- The A4 fix is bounded. Correct two numbers. Graft two qualifiers using the figures and lines in Audit 3.
- None of the four findings changes the protocol verdict (PROCEED WITH FLAGS), the proposed AVOID flag, or any thesis-broken trigger state.

## STYLE NOTES (logged, no re-run)
- **S1.** Step 4B (rev l.281): "369%" divides a pre-tax provision swing (15.98) by a post-tax PAT change (4.33). The method is disclosed. The like-for-like post-tax figure is 11.92 / 4.33 = 275%; show both.
- **S2.** "D/E 2.41x (31-Mar)" is on the SA basis (RF l.911-923). CON at 31-Mar is 2.43x (RF l.1124-1127, l.1140). Label the basis at rev l.462, 513, 956, 1026 and 1169.
- **S3.** The coverage mark for zero-content units rests on a blanket preamble. List them by ID as "reviewed, no finding": turns R015, R019, R025, R026, R029, R037, R038, R040; slides S1-S3, S17, S32, S35, S36, S38, S41, S42 and the dividers. The orphan test then runs mechanically.
- **S4.** SA core PPOP ex-treasury Q2 FY26 is printed 76.75; recomputed 76.74. Rounding only; YoY +10.0% unchanged.
- **S5.** Optional enrichment: deck p41 shows 378 new hires and 16.58% employee turnover (excluding field officers) against 2,905 employees (DK L.893-897). This bears on whether the 10.8% headcount fall is attrition or AI substitution. Immaterial to any number or conclusion.

```yaml
stage: A5-adversary
company: "PAISALO"
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
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "Step 1 opening-claims quantified share (rev l.630)", a4_value: "30 of 44 = 68%", recomputed: "29 of 44 = 65.9%", source_line: "A4 table rev l.584-627 (rows YES: 2,3,5-10,14-16,18-21,23,24,30,33-43)"}
  - {metric: "FY19-FY21 credit-cost range (Step 5L Q1, rev l.327)", a4_value: "3.1-3.8%", recomputed: "2.4-3.8% (FY19 3.1, FY20 3.8, FY21 2.4)", source_line: "DK L.1104-1107, L.1131"}
surviving_bear_counters:
  - {claim: "Asset quality GREEN; Elite x1.15 holds; bad loans low at 0.66% (rev l.296, l.327, l.460, l.1029)", counter: "GNPA ratio rests on an unseasoned, growing book: GNPA x AUM proxy 441 to 480 Mn (+8.6% YoY, +2.1% QoQ); lagged ratio 0.88% vs 0.81% a year ago; H1 disbursement 32,982 Mn = 45.4% of AUM; half-yearly agri dues test Oct-Nov", source_line: "DK L.1023, L.1029-1032, L.964; CC l.197-202, l.212-213", type: "MISSING"}
  - {claim: "Cash conversion growth-induced; CFO ex-loan growth 0.95x PAT (rev l.321-324, l.963)", counter: "H1 0.95x carries Rs35.38 Cr current tax not paid in cash (tax Rs38.45 Cr vs paid Rs3.07 Cr; opening tax asset Rs24.66 Cr absorbed; Rs10.79 Cr liability built); tax-normalised 0.67x SA / 0.68x CON, same as H1 FY26 0.68x; class holds on FY26 full-year 0.95x only", source_line: "RF l.828, l.890, l.917, l.964, l.1033, l.1179", type: "MISSING"}
findings_by_type:
  factual:
    - "F1: Step 1 quantified share 30/44 = 68% should be 29/44 = 65.9% (rev l.630 vs table rev l.584-627)"
    - "F2: Step 5L Q1 FY19-FY21 credit cost '3.1-3.8%' should be 2.4-3.8% (DK L.1104-1107); conflicts with A4 QfM 6 rev l.508"
  missing:
    - "M1: GNPA denominator/seasoning bear counter absent from Step 5L Q1, Step 7 pillar 2, brief l.1029"
    - "M2: H1 cash-conversion tax-timing qualifier absent from Step 5L cash paragraph and Section C row"
  contradiction: []
  style:
    - "S1: Step 4B 369% mixes pre-tax swing over post-tax PAT change; post-tax like-for-like 275%"
    - "S2: D/E 2.41x (31-Mar) is SA basis; CON 2.43x; label basis"
    - "S3: list zero-content turns/slides by ID as reviewed, no finding"
    - "S4: SA core PPOP ex-treasury Q2 FY26 76.75 vs 76.74 (rounding)"
    - "S5: optional: deck p41 attrition 16.58% and 378 new hires bear on AI headcount claim"
loop_back_to: "A4"
gap: "A4 to (1) correct Step 1 quantified share to 29/44 = 65.9% (F1); (2) correct Step 5L Q1 FY19-FY21 credit-cost range to 2.4-3.8% (F2); (3) graft the GNPA denominator/seasoning bear counter into Step 5L Q1, Step 7 pillar 2 and brief l.1029 (M1); (4) graft the H1 tax-timing qualifier (0.67x tax-normalised) into the Step 5L cash paragraph and Section C (M2). No A2 or A3 re-run."
style_notes:
  - "S1: Step 4B 369% is pre-tax over post-tax; show post-tax 275% alongside"
  - "S2: label D/E 2.41x as SA (CON 31-Mar 2.43x) at rev l.462, 513, 956, 1026, 1169"
  - "S3: enumerate zero-content units by ID as reviewed, no finding"
  - "S4: SA Q2 FY26 core PPOP ex-treasury 76.74 not 76.75"
  - "S5: optional p41 attrition/new-hire enrichment for the AI headcount claim"
analyst_note: "All five brief parts are present. Fresh counts match every ledger: 9 notes, 8 footnotes, 251 statement lines, 22 Reg 52 rows, 10 note-5 lines, 10 auditor paragraphs, 42 slides, 40 turns, 12 questions. No orphan rows; nothing missing from the ledger. Core SA and CON arithmetic reproduces to the lakh, both PAT bridges sum, and deck values tie to the resolved appendix. Two small misstatements (F1, F2) change no conclusion. Two bear counters survive and are absent from A4. First, GNPA 0.66% sits on a book that is 45% under six months old; the absolute GNPA proxy rose 8.6% YoY and the lagged ratio is 0.88%. The proxy uses AUM as base because the GNPA denominator is not disclosed. Second, H1 cash conversion of 0.95x carries Rs35 Cr of current tax not yet paid; tax-normalised it is 0.67x, the same seasonality as H1 FY26, so the growth-induced class rests on FY26 full-year data. Neither changes the AVOID flag or PROCEED WITH FLAGS; both qualify the Elite asset-quality band and the cash test. No company acquisition exists; the promoter stake-buy price is NOT FOUND. The loop is A4 only."
```

---

## RE-AUDIT (loop iteration 1)

- Trigger: A4 rewrote work/review_paisalo_q2fy27.md (revision line rev l.10; correction log rev l.1091-1101). The file now runs to about 1,213 lines. Line numbers below are in the REWRITTEN review.
- Inputs: the same as the first audit (A1 fulltexts, A2 ledgers, the rewritten A4 review). No source PDF, nothing under inputs/, no A3 reasoning.
- Scope as instructed: check the four loop items at their new locations, re-run the brief gate, run a coverage and drop spot check, and recompute every number the rewrite touched.

### R1. Loop items

| Item | New location (rev l.) | What I checked | Recomputed / matched against | Status |
|---|---|---|---|---|
| F1 | l.643 | Now reads "29 of 44 = 65.9%" and lists the YES rows (2, 3, 5-10, 14-16, 18-21, 23, 24, 30, 33-43). The Step 1 table still has 44 rows. "30 of 44" and "= 68%" now appear only in the log's "Old" column (l.1095). | 29/44 = 65.9% | CLOSED |
| F2 | l.332; l.473; YAML flag l.1196 | Now reads "2.4-3.8% (FY19 3.1%, FY20 3.8%, FY21 2.4%)" with anchors DK L.1104-1107, L.1131. QfM 6 is consistent. "3.1-3.8" appears only in the log (l.1096). | DK L.1104 (3.1%@649), L.1105 (3.8%@781), L.1107 (2.4%@942) | CLOSED |
| M1 | PROXY block l.334-340 (two readings and a separating observation); Step 7 pillar 2 l.473; brief l.1043 | Proxy maths, quotes and cross-references (details below). | see below | CLOSED |
| M2 | Cash table rows l.323-326; paragraph l.329; Section C l.976; YAML flag l.1197 | Tax figures, normalised ratios and the class conclusion (details below). | see below | CLOSED |

M1 detail:
- Proxy maths: 0.81% x 54,494 = 441.40; 0.66% x 72,659 = 479.55 (printed 479.5); change +8.64%. Lagged ratio 479.55/54,494 = 0.880%. Seasoning: 32,982/72,659 = 45.4%; 32,982/71,144 = 46.4% (DK L.964 loan assets 71,144). All match.
- Quotes: "it is still early to draw definitive conclusions" matches CC l.201. The half-yearly instalment structure for agri-equipment matches CC l.197-199. "by end of October or early November" matches CC l.212-213.
- Cross-references are in place at:
  - Step 2 GNPA verdict, l.213
  - Step 5L table, l.297
  - Early warning #3, l.423
  - 7A, l.853 (CONFIRMED on the ratio, PARTIALLY CONTRADICTED in rupees)
  - 8D, l.926
  - 8F, l.950
  - Section C, l.969 and l.977
  - Monitorable 7, l.1007
  - YAML monitorable, l.1176
- Brief l.1043 rounds +8.6% to "about 9%" and tags it INFERENCE, proxy. That is acceptable. The arithmetic part of the line ("the ratio fell because the book grew") holds under both readings.

M2 detail:
- Tax not paid in cash: SA H1 FY27 3,845.25 - 307.49 = 3,537.76 lakh = Rs35.38 Cr. CON 3,878.12 - 383.99 = 3,494.13 = Rs34.94 Cr. H1 FY26 3,178.44 - 1,149.68 = 2,028.76 = Rs20.29 Cr. FY26 7,225.79 - 7,232.56 = -6.77 lakh = -Rs0.07 Cr (RF l.828, 964, 1033, 1179).
- Normalised ratios: SA 119.95 - 35.38 = 84.57, /125.92 = 0.67x. CON 121.27 - 34.94 = 86.33, /126.96 = 0.68x. H1 FY26 86.09 - 20.29 = 65.80, /97.47 = 0.68x. FY26 224.14, /234.69 = 0.955, printed 0.96x.
- Balance-sheet anchors: opening tax asset Rs24.66 Cr (RF l.890); closing liability Rs10.79 Cr (RF l.917).
- A4's H1 FY26 Rs20.29 Cr is more exact than my first-audit Rs20.28 Cr. The difference is rounding.
- The class conclusion ("growth-induced holds on FY26 full year") matches mine. The A4 YAML keeps `cash_conversion: "growth-induced"`, which is consistent.

### R2. Style items
- Applied:
  - S2: SA/CON label at l.475, l.528, l.969, l.1039, l.1142 and l.1199. The deck-series references at l.464 and l.472 ("2.43x to 2.89x (deck)") are a different, correctly labelled series.
  - S4: 76.74 at l.205 and l.218.
- Not applied: S1 (369% at l.282 unchanged), S3 and S5. All three are STYLE, logged only, no loop.

### R3. Brief gate (re-run): PASS
- Narrative (l.1028-1046) is now 19 lines, inside the 10-20 band. The added line is l.1043 (M1). The S2 label is at l.1039.
- Sector (l.1049-1053, 5 bullets), business model (l.1056-1063, 8 bullets) and competition (l.1066-1070, 5 bullets) are unchanged in content.
- Forward map (l.1073-1087) is unchanged: a make-or-break reading plus 11 dated catalysts, each with a bull and a bear fork.

### R4. Coverage and drop spot check: PASS (nothing dropped)

| Unit | First audit | Rewrite | Status |
|---|---|---|---|
| Step 1 opening-claim rows | 44 | 44 | intact |
| Step 8.5 QfM rows | 39 | 39 | intact |
| Step 4A Q&A rows | 12 | 12 | intact |
| Step 7A cross-reference rows | 18 | 18 | intact |
| Monitorables table rows | 21 | 21 (l.1001-1021) | intact |
| Forward-map catalyst rows | 11 | 11 | intact |
| YAML questions_for_management | 39 | 39 (l.1130-1168) | intact |
| YAML monitorables | 20 | 20 (l.1170-1189) | intact |
| YAML flags | 19 | 21 (l.1191-1211) | all 19 originals present (one relabelled for S2); 2 added: M1 at l.1196, M2 at l.1197 |
| Preamble ledger line (9 notes / 40 turns / 42 slides, all reviewed) | present | present (l.25) | intact |

Untouched-arithmetic spot check: these still read exactly as audited in iteration 0.
- PPOP rows CON and SA (l.125, l.146)
- CON C/I 35.52 / 32.32 / 40.95% (l.161)
- Filed RoA 3.73 / 3.63% (l.171) and RoE 13.46 / 13.86% (l.173)
- 4A core subtotal +3.49 / +2.61 / 18.5% (l.261) and provision line +12.16 / +9.08 / 64.4% (l.263)
- 4B 369% (l.282)
- protocol_verdict "PROCEED WITH FLAGS" (l.1118)

### R5. New findings from the rewrite
- FACTUAL: none.
- MISSING: none.
- CONTRADICTION: none.
- The PROTOCOL verdict and the proposed AVOID flag are unchanged, which is consistent with the first audit's expectation.

### RE-AUDIT VERDICT

**VERDICT: COMPLETE (iteration 1).** F1, F2, M1 and M2 are closed and re-verified against the extract. The brief gate passes. No row, question, monitorable or flag was dropped. Every number the rewrite touched recomputes. Open items are STYLE only (S1, S3, S5), logged with no re-run. The review may proceed to the Notion save gate.

```yaml
stage: A5-adversary
company: "PAISALO"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
iteration: 1
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "S1: Step 4B 369% (rev l.282) mixes pre-tax swing over post-tax PAT change; post-tax like-for-like 275%; not applied"
    - "S3: list zero-content turns R015, R019, R025, R026, R029, R037, R038, R040 and slides S1-S3, S17, S32, S35, S36, S38, S41, S42 by ID as reviewed, no finding; not applied"
    - "S5: optional: deck p41 attrition 16.58% and 378 new hires (DK L.893-897) bear on the AI headcount claim; not applied"
loop_back_to: ""
gap: ""
style_notes:
  - "S1: show post-tax 275% beside the pre-tax/post-tax 369% at rev l.282"
  - "S3: enumerate zero-content units by ID as reviewed, no finding"
  - "S5: optional p41 attrition/new-hire enrichment for the AI headcount claim"
analyst_note: "Iteration 1 closes all four loop items. F1 now reads 29 of 44 = 65.9% (rev l.643). F2 now reads 2.4-3.8% with FY21 at 2.4% (rev l.332, l.473). M1 adds a labelled PROXY block (rev l.334-340): absolute GNPA Rs441.4 Mn to Rs479.5 Mn (+8.6%), lagged ratio 0.88%, H1 disbursement 45.4% of AUM, two readings and a separating observation. It is cross-referenced through Step 7, 7A, 8D, 8F, Section C, monitorable 7 and brief l.1043. M2 adds tax rows and a qualifier (rev l.323-329, l.976): Rs35.38 Cr current tax unpaid, tax-normalised 0.67x SA and 0.68x CON against 0.68x in H1 FY26; the class holds on FY26 full year. I recomputed every touched number from RF and DK lines and checked every quote against the CC lines. The drop check finds all 44 claims, 39 questions, 12 Q&A rows, 18 cross-reference rows, 21 monitorables, 11 catalysts and 19 original flags intact, plus 2 added flags. S2 and S4 were applied. S1, S3 and S5 remain STYLE only. The protocol verdict PROCEED WITH FLAGS and the AVOID flag are unchanged."
```
