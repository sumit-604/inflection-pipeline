# A5 AUDIT: Kross Limited (KROSS), Q2 FY27

Agent: A5 adversary / completeness auditor | model claude-opus-5-5 | date 2026-10-20
Instruction file: prompts/quarterly-a5-adversary.md

Inputs read (and only these):
- A4 review: runs/kross-q2fy27/work/review_kross_q2fy27.md (L1-L735; part 1 and part 2 already concatenated in this one file)
- A1 fulltexts: extracted/kross-results-q2fy27-fulltext.md (RES, 600 lines), extracted/kross-pressrelease-q2fy27-fulltext.md (PR, 124 lines), extracted/kross-presentation-q2fy27-fulltext.md (PPT, 788 lines)
- A1 structured: the three matching *-structured.md files (RES R001-R372, PR R001-R135, PPT R001-R665)
- A2 ledgers: work/ledger_results_kross_q2fy27.md, work/ledger_pressrelease_kross_q2fy27.md, work/ledger_presentation_kross_q2fy27.md

Not read: the source PDFs, anything under inputs/, A3 forensic notes, orchestrator commentary. No source access was needed; no pipeline error to report.

Anchor key: RES / PR / PPT Lnnn = fulltext line. REV Lnnn = line in the A4 review under audit. R### = A1 structured row (per document). Units: RES and PR in Rs Mn; Rs Cr = Mn x 0.1. PPT in Rs Cr.

Scope note: the Role 5 (concall) sections read "pending Role 5 addendum" by design (REV L4, L392-L395, L524-L530). Not failed.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business_model PRESENT | competition PRESENT | forward_map PRESENT. Gate PASSES.

| Part | Heading in review | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | "### 1. Summary narrative" REV L585 | 16 lines (REV L586-L601), inside the 10-20 line band for a Role 4 read. Names both readings and the separating observation (REV L600-L601). | present |
| 2. Sector intelligence | "### 2. Sector intelligence" REV L603 | 7 lines: CV and tractor demand, input cost, policy, cyclicality, ND items (REV L604-L610). | present |
| 3. Business-model intelligence | "### 3. Business-model intelligence" REV L612 | 12 lines: two revenue engines with shares, integration, utilisation, unit economics, cash cycle, model drift (REV L613-L624). | present |
| 4. Competition intelligence | "### 4. Competition intelligence" REV L626 | 7 lines: position, edge, weakness, concentration, risk to watch (REV L627-L633). | present |
| 5. Forward map | "### 5. Forward map" REV L635 | 8 catalysts, each with a bull fork and a bear fork (REV L638-L647). Three rows are undated (REV L640, L642, L644) because the source gives no date; that is the NOT FOUND rule, not a gap (STYLE note S9). | present |

---

## 1. COVERAGE AUDIT

Method. (a) Fresh grep pass over each A1 fulltext: page markers, numbered notes, statement lines in the image transcriptions, table cells, ZERO_STANDING dashes, auditor paragraphs, agenda items. (b) Slide-by-slide sweep of the PPT and PR fulltext for any material unit (number, dated event, entity, forward claim, qualifier) that has no A1 structured row. (c) Check that every structured ID appears in its ledger. (d) Check every ledger row against A4: cited, or covered by A4's explicit "every ledger ID reviewed / Unreviewed rows: none" statement (REV L22, L26-L28, L36).

| Document | Category | A2 count | Fresh count (A5) | Orphan rows | Status |
|---|---|---|---|---|---|
| RES | pages | 7 | 7 ([page 1]-[page 7]) | none | PASS |
| RES | numbered notes | 7 (+2 footnotes R059, R060) | 7 (RES L224, L228, L233, L238, L243, L246, L248). A second series on p6/p7 ("Notes ... 1. Statement of Assets and Liabilities", RES L269-L270; "2. Statement of Unaudited Cash Flows", RES L337-L338) is the balance sheet and cash flow, enumerated as line items. | none | PASS |
| RES | line items | 304 | 304 = P&L 24 lines x 6 cols (RES L412-L435) + BS 35 x 2 (RES L438-L472) + CF 45 x 2 (RES L475-L519) | none | PASS |
| RES | ZERO_STANDING | 18 | 18 (RES L424 x3, L435 x5, L478 x2, L481, L482, L499, L503 x2, L507, L509 x2) | none | PASS |
| RES | agenda items | 2 | 2 (RES L41-L47) | none | PASS |
| RES | auditor paragraphs | 4 | 4 (RES L90-L98, L100-L105, L107-L115, L117-L124) | none | PASS |
| RES | consolidation entities | 0 | 0 (Note 5, RES L243-L244) | none | PASS |
| RES | superseded IDs | 21 (+R068 resolved) | 21 (R008-R027, R030) | none | PASS |
| RES | all structured IDs | 372 | 372; every ID R001-R372 appears in the ledger (checked row by row) | none | PASS |
| PR | pages | 2 | 2 | none | PASS |
| PR | table cells | 42 | 42 = 7 rows x 6 cols (PR L118-L124) | none | PASS |
| PR | active numbers | 57 | 57 (R001-R003, R046-R057, R094-R135) | none | PASS |
| PR | entities / forwards / dates / qualifiers | 12 / 10 / 8 / 6 | 12 / 10 / 8 / 6 (structured type counts sum to 135; sweep found no material unit without a row) | none | PASS |
| PR | superseded IDs | 42 | 42 (R004-R045) | none | PASS |
| PPT | slides | 38 | 38 ([page 1]-[page 38]) | none | PASS |
| PPT | all structured IDs | 665 | 665; per-slide id_count in the ledger sums to 665; row ledger L97-L761 lists R001-R665 | none | PASS |
| PPT | superseded IDs | 21 | 21 (R195, R203, R211, R219, R227, R238, R239, R241, R348-R353, R355-R361) | none | PASS |
| PPT | fresh-pass material units without a structured row | n/a (A2 counts structured rows only) | 1: PPT L341-L346 (p15 milestone "Established foundry Unit-V, a high-pressure mould line along with its machine shop") | n/a | FAIL (MISSING, loop A2) |
| All | ledger rows cited in A4 or marked reviewed | 1,172 | A4 marks every ID reviewed (REV L22, L26-L28, L36). Accepted for immaterial rows. Two material row groups are cited nowhere: RES R225/R226/R333 (other non-current assets) and PPT R416-R438 (FY22-FY26 revenue and gross margin, not layout-scrambled; A4's scrambled carve-out at REV L30 covers R439-R608 only) | none formally | MISSING x2 (loop A4) |

### Coverage findings

C1-F1 (MISSING, A2). PPT p15, L341-L346: "Established foundry Unit-V, a high-pressure mould line along with its machine shop". It sits in the milestone row before "Publicly listed on BSE and NSE on 16th September 2024" (PPT L341-L346). The A1 rows for p15 hold years (R313-R325) and counterparties (R326-R333) only; no row carries this event. So the ledger lacks it. It matters: PPT L511-L515 (p24) also says an HPML foundry was set up in 2023, while PPT L116, PPT L131-L135 and PR L66-L67 say the HPML is still being installed ("progressing as planned"). A4 cites only p24 and calls it a single "unexplained drafting conflict" (REV L382; PPT-FN-08 i), and grades the HPML RED at REV L347. With p15, two slides describe an HPML as already established. Fix: A2 adds the unit; A3 adds one forensic line; A4 adds it to 6D and Q13 (same line or a second line? REV L477).

C1-F2 (MISSING, A4). RES R225/R226 (other non-current assets 466.64 to 503.45 Mn, RES L444) and R333 (investing outflow -36.81 Mn, RES L500; H1 FY26 +24.90 Mn inflow) are cited nowhere in A4. The company classes this change inside investing activities, which points to capital advances; the nature is not disclosed. It changes two A4 facts. Capex incl. this line: H1 FY27 63.26 Cr (591.60 + 4.16 + 36.81 Mn) vs H1 FY26 59.12 Cr (609.88 + 6.20 - 24.90 Mn) = +7.0%, not -3.3% (REV L247). FCF on that basis: -58.53 Cr vs -54.03 Cr = worse by 4.50 Cr, not "flat" (REV L248). A4 must show both bases and add the line to Q11 (REV L475).

C1-F3 (MISSING, A4). PPT R416-R438 (p30, PPT L616-L620; not flagged LAYOUT_SCRAMBLED) give FY22-FY26 revenue 297.5 / 488.6 / 620.3 / 620.4 / 673.2 Cr and gross margin 46.1% / 40.7% / 42.6% / 43.0% / 45.7%. A4 cites none of them. They qualify two A4 readings. (i) The 8C thresholds (REV L444-L445): FY26's 45.7% is the five-year high after FY22, and Q2 FY27's 43.90% sits above the FY23-FY25 band (40.7-43.0%). A Q3 print of 42.6-43.0% would read "bear" under A4's line (below 43.9%) while equal to the FY24-FY25 level. A4 must state both readings. (ii) FY25 revenue was flat on FY24 (620.4 vs 620.3 Cr), which feeds bear counter A below.

---

## 2. ARITHMETIC AUDIT

Method: every derived metric in A4's tables recomputed in Rs Mn from RES L412-L519 (image transcriptions, which govern), then converted. Tolerance: last displayed digit. Result: one formula error (FACTUAL); four display-rounding notes (STYLE). Everything else ties.

| Metric (review line) | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Rs Cr conversion, 21 P&L lines x 6 cols (REV L105-L121) | as tabled | all within 0.01 Cr | RES L412-L433 | PASS |
| Operating EBITDA Q2FY26 / Q1 / Q2FY27 / FY26 / H1FY26 / H1FY27 (REV L128) | 14.75 / 22.55 / 30.60 / 87.95 / 30.92 / 53.32 Cr | 147.53 / 225.53 / 306.00 / 879.47 / 309.21 / 533.18 Mn (PBT + D&A + FC - OI) | RES L413, L418, L419, L422 | PASS |
| Operating EBITDA margin (REV L129) | 11.27 / 12.23 / 13.02 / 13.06 / 11.44 / 12.71% | 11.269 / 12.235 / 13.016 / 13.064 / 11.441 / 12.712% | RES L412 | PASS |
| Reported EBITDA and margin (REV L130-L131) | 15.80 / 22.95 / 32.77 / 92.20 / 34.06 / 55.88; 12.07 / 12.45 / 13.94 / 13.70 / 12.60 / 13.32% | 158.00 / 229.45 / 327.73 / 921.95 / 340.55 / 558.83 Mn; 12.068 / 12.447 / 13.940 / 13.695 / 12.600 / 13.324% | RES L418-L419, L422 | PASS |
| Core PBT ex-OI (REV L132) | 10.78 / 17.44 / 24.78 / 70.79 / 22.56 / 42.38 | 107.80 / 174.35 / 247.81 / 707.94 / 225.62 / 423.81 Mn | RES L413, L422 | PASS |
| OI / PBT (REV L133) | 8.85 / 2.20 / 8.06 / 5.66 / 12.20 / 5.71% | 8.853 / 2.199 / 8.062 / 5.661 / 12.197 / 5.707% | RES L413, L422 | PASS |
| ETR (REV L134) | 31.65 / 25.33 / 26.96 / 26.42 / 26.90 / 26.22% | 31.648 / 25.327 / 26.964 / 26.421 / 26.899 / 26.216% | RES L422, L426 | PASS |
| PAT margin (REV L135) | 6.17 / 7.22 / 8.37 / 8.20 / 6.95 / 7.91% | 6.175 / 7.222 / 8.374 / 8.202 / 6.950 / 7.907% | RES L412, L427 | PASS |
| Gross margin (REV L136) | 46.23 / 44.79 / 43.90 / 45.71 / 46.09 / 44.33% | 46.226 / 44.791 / 43.904 / 45.711 / 46.095 / 44.333% | RES L412, L415, L416 | PASS |
| Employee / rev; other expense / rev (REV L137-L138) | 6.76 / 5.58 / 4.56 / 5.85 / 6.61 / 5.01%; 28.20 / 26.97 / 26.33 / 26.79 / 28.05 / 26.61% | 6.755 / 5.583 / 4.561 / 5.854 / 6.605 / 5.010%; 28.202 / 26.974 / 26.327 / 26.793 / 28.049 / 26.611% | RES L417, L420 | PASS |
| Share-adjusted EPS = PAT / 64.51 Mn (REV L122) | 1.25 / 2.06 / 3.05 / 8.56 / 2.91 / 5.14 | 1.253 / 2.064 / 3.052 / 8.559 / 2.912 / 5.141 | RES L427, L434 | PASS |
| PR implied Q1 (H1 less Q2) (REV L143) | EBITDA margin 12.33%, PAT 13.47 Cr | 227.2 / 1,843.4 = 12.33%; 331.6 - 196.9 = 134.7 Mn | PR L118-L122 | PASS |
| YoY: revenue / op EBITDA / margin (REV L154-L156) | +79.6% / +107.4% / +175 bps | x1.7957 / x2.0742 / +174.7 bps | RES L412 | PASS |
| YoY: D&A / finance / finance QoQ (REV L157-L158) | +44.6% / +48.9% / +22.8% | x1.4458 / x1.4888 / x1.2279 | RES L418-L419 | PASS |
| Operating EBIT and YoY (REV L159) | 12.52 / 27.37 Cr, +118.6% | 125.21 / 273.73 Mn, x2.1862 | RES L418-L419, L422 | PASS |
| YoY: OI / core PBT / PBT / PAT (REV L160-L163) | +107.5% / +129.9% / +127.9% / +143.5% | x2.0754 / x2.2988 / x2.2790 / x2.4352 | RES L413, L422, L427 | PASS |
| EPS YoY (REV L164) | +143.5% computed; +146.4% reported | x2.4352; 3.08 / 1.25 = x2.464 | RES L432 | PASS |
| H1 revenue YoY; FY27 base growth needed; H1 share of FY26 (REV L167) | +55.2%; +23%; 62.3% | x1.5519; 830 / 673.20 = x1.2329; 0.6230 | RES L412 | PASS |
| Margin walk: GM / employee / other expense / net (REV L168) | -232 / +219 / +188 / +175 bps | -232.2 / +219.4 / +187.5 / +174.7 bps | RES L412-L420 | PASS |
| ETR benefit on Q2 PBT (REV L170) | 12.62 Mn | (0.316479 - 0.269644) x 269.54 = 12.62 | RES L422, L426 | PASS |
| OI ratios (REV L172) | 5.5x Q1; 51% of FY26 OI; 14.43 Mn unexplained; 19.5% of QoQ PBT rise; core PBT +42.1% QoQ | 5.54x; 51.2%; 25.65 - 6.63 - 4.59 = 14.43; 17.81 / 91.27 = 19.51%; x1.4213 | RES L413, L422, L480, L483 | PASS |
| Q1 FY26 derived; Q2 FY26 QoQ (REV L184-L185) | 139.36 Cr, 11.60%, 11.78 Cr; -6.1% | 1,393.55 Mn, 11.602%, 117.82 Mn; -6.05% | RES L412-L422 (H1 FY26 col) | PASS |
| H2 FY26 derived (REV L188) | 402.93 (201.46/qtr), 14.15%, 48.23 (24.12/qtr), +53.9% vs Q2 FY26 | 4,029.26 Mn, 14.153%, 482.32 Mn, x1.5388 | RES L412-L422 (FY26 col) | PASS |
| Q1 FY27 vs H2 avg; Q1 YoY; Q2 QoQ (REV L189-L190) | -8.5%; +32.3%; +27.5% | x0.9150; x1.3228; x1.2753 | RES L412 | PASS |
| Q2 margin vs FY26 margin (REV L193) | "4 bps" | 4.8 bps unrounded | RES L412-L422 | STYLE S2 (display rounding) |
| Q2 vs H1 average run-rate (REV L195) | +12.1% over 209.72 Cr | 2,350.92 / 2,097.16 = x1.1210 | RES L412 | PASS |
| PAT bridge rows (REV L208-L219) | +481.54 / -54.59 / -268.48 / +158.47 / -9.95 / -8.51 / +11.26 / +151.27 / -47.87 / +12.62 / +116.02 Mn | 481.55 / -54.59 / -268.48 / 158.47 / -9.95 / -8.51 / 11.26 / 151.27 / -47.87 / 12.62 / 116.02 (sum ties exactly) | RES L412-L427 | PASS |
| Bridge % of PAT change (REV L208-L217) | 415.1 / -47.1 / -231.4 / 136.6 / -8.6 / -7.3 / 9.7 / 130.4 / -41.3 / 10.9% | same to 0.1 pp | as above | PASS |
| Recurring share (REV L222) | 82.0% (95.17 Mn) | 116.02 - 8.22 - 12.62 = 95.17 | as above | PASS (basis note S6) |
| OI-revert PAT (REV L223) | 188.64 / 183.86 / 181.00 Mn; +124% to +133% | 188.64 / 183.85 / 180.99; +123.9% / +133.4% | RES L413, L422, L426 | PASS |
| DTL roll (REV L225) | +17.94 = 17.86 + 0.08 | 114.23 - 96.29 = 17.94 | RES L461, L425, L429 | PASS |
| ETR vs 25.17% statutory (REV L225) | 179 bps | 179.6 bps unrounded | RES L426 | STYLE S4 (rounding) |
| CFO; CFO/PAT (REV L238-L239) | 5.09 / 4.73 Cr, -7.1%; 27.1% / 14.3% | 50.92 / 47.28 Mn, -7.15%; 27.11% / 14.26% | RES L496, L427 | PASS |
| Pre-WC profit; WC absorption (REV L240-L241) | 32.22 / 54.76 Cr, +69.9%; -18.18 / -40.39 Cr, 2.2x, 73.8% | x1.6994; -181.84 / -403.94 Mn, 2.22x, 73.77% | RES L484, L494 | PASS |
| WC components (REV L242-L246) | +17.77/-9.12; -8.09/-4.10; -12.12/-23.89; -11.75/+5.93; -4.76/-9.12 Cr | match; components sum to -403.92 vs -403.94 filed | RES L485-L493 | PASS |
| Capex; FCF (REV L247-L248) | 61.61 / 59.58 Cr, -3.3%; -56.52 / -54.85 Cr | 616.08 / 595.76 Mn, -3.30%; -565.16 / -548.48 Mn | RES L496-L498 | PASS on A4's basis; see C1-F2 for the other-NCA basis |
| Receivable days (REV L249-L250) | 106.9 to 90.0 (FY basis); 89.1 to 90.0 (half basis) | 106.90; 90.01; 89.06 | RES L448, L412 | PASS |
| Inventory days (REV L251) | 105.4 / 87.4 to 86.0; -1.4 | 105.42 / 87.41 to 85.95; -1.46 | RES L446, L415-L416 | STYLE S3 (rounding) |
| Payable days; CCC (REV L252-L253) | 59.7 / 49.5 to 51.5; 152.6 / 127.0 to 124.4 | 59.72 / 49.52 to 51.52; 152.60 / 126.95 to 124.44 | RES L465-L466 | PASS |
| PPE, capitalised, CWIP (REV L254-L255) | +14.31; ~20.5; 16.00 to 54.92, 3.4x | 143.07 Mn; 20.54 (uses total D&A); 3.43x | RES L438-L439, L419 | PASS (note S7) |
| Gross borrowings and tie (REV L256) | 52.37 to 117.14 Cr; +64.77 = 48.80 + 15.98 | 523.65 to 1,171.36 Mn; 647.71 = 487.96 + 159.75 exact | RES L458, L463, L506, L508 | PASS |
| Liquidity; net debt; ND/E (REV L257-L258) | 25.37 to 28.22; 26.99 to 88.91, 3.3x; 0.06 to 0.17 | 253.74 to 282.24; 269.91 to 889.12, 3.29x; 0.055 to 0.170 | RES L447, L449-L450, L457 | PASS |
| ND / T4Q op EBITDA; EBITDA / finance (REV L259) | 0.31x to 0.81x (110.34 Cr); 11.8x | 0.307 to 0.806 (1,103.44 Mn); 11.81x | RES L412-L422, L418 | PASS |
| Other equity roll (REV L65) | 4,575.10 + 331.87 = 4,906.97 | exact | RES L456, L431 | PASS |
| Dilution as share count (REV L66) | 4.65%; equity leg 2.33% | 3.0 / 64.51 = 4.650%; 1.5 / 64.51 = 2.325% | RES L238, L434 | PASS |
| "Forward EPS dilution up to 4.65%" (REV L76) | 4.65% | EPS falls 1 - 64.51 / 67.51 = 4.44% (equity leg: 2.27%) | RES L238, L434 | FAIL (FACTUAL, loop A4) |
| 6A pro-rata, H2-needed, Q2 x 2 (REV L328-L331) | 395/415/440; 370.57/410.57/460.57; 470.18; 28.0/32.5/38.0; 22.84/31.84/42.84; 39.37; 4.25/4.95/5.75 | all exact | RES L412, L427 | PASS |
| Base margin needed over Q2-Q4 (REV L329) | ~13.2% | (0.13 x 830 - 22.55) / (830 - 184.34) = 13.22% | RES L412 | PASS |
| EPS on 66.01 Mn (REV L331) | 5.02 | 331.63 / 66.01 = 5.024 | RES L427 | PASS |
| ROCE (REV L333, L335) | 16.76% / 15.89%; FY26 15.29% | 992.98 / 5,925.61; 941.68 / 5,925.61; 831.12 / 5,434.87 | RES L455-L464, L418, L422 | PASS |
| 6.5A run-rate and T4Q (REV L407) | 940.37 / 78.74; 822.36 / 110.34 (13.42%) / 69.59 / Rs 10.79; +7% / +21% vs base | exact; 1,103.44 / 8,223.57 = 13.418%; 695.93 / 64.51 = 10.79 | RES L412-L427 | PASS |
| Capital employed growth; trailing PE (REV L409, L415) | +18%; 22.6x | +18.06%; 244 / 10.79 = 22.61 | RES L455-L464 | PASS |
| Trailer revenue (REV L379) | ~115.9 / ~74.9 Cr | 115.92 / 74.95 | PPT L397, RES L412 | PASS (rounding) |
| Exports on component base (REV L384) | ~6.3% | 3.21 / 50.69 = 6.33% | PPT L787, L395 | PASS |
| GM QoQ; QoQ revenue rise (REV L385, L462) | -89 bps; 50.75 Cr | -88.7 bps; 235.09 - 184.34 | RES L412-L416 | PASS |
| OCA, OCL, OFL (REV L464, L476) | 54.32; 4.55 to 0.67; 12.47 to 7.23 Cr | 543.19; 45.46 to 6.73; 124.73 to 72.31 Mn | RES L452, L467-L468 | PASS |

Discrepancy shown (FACTUAL). REV L76 (0D, Note 4 row) says "Forward EPS dilution up to 4.65%". 4.65% is the share-count increase (3.0 Mn / 64.51 Mn, REV L66). EPS on full conversion falls by 1 - 64.51 / 67.51 = 4.44% before any return on the proceeds; the equity leg alone cuts EPS 2.27% (1 - 64.51 / 66.01). Source: RES L238 (15,00,000 shares + 15,00,000 warrants), RES L434 (paid-up 322.55 Mn at FV Rs 5). Fix the label or the number at REV L76; REV L408 states the share-count basis and is correct.

---

## 3. ADVERSARIAL READ

The three most positive claims in A4, each attacked from the same extract. Rule J applies: each graft states both readings and the observation that separates them; it does not replace A4's view.

### Claim A. "The growth is real." Revenue +79.6% YoY to Rs 235.09 Cr; core PBT +129.9%; trajectory "STEPPING UP" (REV L586-L589, L167, L169, L193)

Strongest bear counter. The YoY base is a trough, and the sequential step is small.
- Q2 FY26 revenue of 130.92 Cr was the weakest quarter the filing lets us derive: -6.1% vs Q1 FY26 (139.36 Cr derived) and 35.0% below the H2 FY26 average quarter of 201.46 Cr (RES L412, H1 FY26 and FY26 columns).
- FY25 revenue was flat on FY24: 620.4 vs 620.3 Cr (PPT L617; R418-R419). FY26 grew 8.5%.
- FY26 was back-loaded far beyond management's own seasonality claim: H2 FY26 revenue was 1.49x H1 FY26 (4,029.26 vs 2,702.75 Mn), against "H2 is always 10-15% up than H1" (PPT L102).
- Against the latest half: H1 FY27 revenue is +4.1% over H2 FY26 (419.43 vs 402.93 Cr). H1 FY27 core PBT ex-OI is 12.1% BELOW H2 FY26 (42.38 vs 48.23 Cr). Q2 FY27 core PBT is +2.8% above the H2 FY26 average quarter (247.81 vs 241.16 Mn), and Q2 operating margin 13.02% is below H2 FY26's 14.15% (RES L412-L422).

Bull reading kept. H1 is the seasonally weak half, so H1 FY27 matching or beating H2 FY26 is itself growth; on a 10-15% seasonal uplift, H1 FY27 revenue sits about 15-20% above a seasonally adjusted H2 FY26.

Separating observation: H2 FY27 revenue against H1 FY27 x 1.10-1.15 = 461-482 Cr, and Q3 FY27 core PBT against Q2's 24.78 Cr.

Survives? YES. Every number except PPT L617 can be built from A4's own Step 1 and Step 3 tables (REV L105, L184-L190), but A4 never draws the inference; the brief tells the operator "The growth is real" with the 79.6% figure and no base context (REV L586-L589). Graft into Step 2 diagnostics 1 and 3, the Step 3 trajectory line, and the brief. Type MISSING. Loop A4.

### Claim B. "Share of PAT change from recurring core operations: about 82%"; PAT still +124% to +133% YoY if other income reverts (REV L222-L223)

Strongest bear counter. "Recurring" is a line-nature label; recurrence of the Q2 revenue level is not shown. The QoQ step that lifted Q2 is concentrated (MGMT shares x FILED revenue, the same method A4 uses at REV L379):
- Trailer half: 74.95 Cr in Q1 to 115.92 Cr in Q2 = +40.97 Cr, 80.7% of the 50.75 Cr QoQ rise. The component half rose 109.39 to 119.17 Cr, +8.9% (PPT L395-L397; RES L412).
- Top-5 customers: 109.63 to 150.95 Cr = +41.33 Cr, 81.4% of the QoQ rise. Revenue outside the top 5 rose 74.71 to 84.14 Cr, +12.6% (PPT L788 image transcription; legend-reading caveat applies; RES L412).
- A4's own Q3 asks whether a one-time fleet order sits in the jump (REV L462). Until it is answered, the 82% cannot be read as run-rate.

Bull reading kept. YoY growth was broad across both halves: trailer +103.2% (57.05 to 115.92 Cr) and components +61.3% (73.87 to 119.17 Cr), so the YoY bridge is not one-segment.

Separating observation: Q3 FY27 trailer share and top-5 share (deck) against Q2's 49.31% and 64.21%, read with the Q3 answer.

Survives? YES, in part. A4 states the concentration qualitatively (REV L577 flag 5, L593, L462) but does not quantify that about 81% of the QoQ step came from the trailer half and from the top 5, and does not qualify the Step 4 "recurring" label with it. Graft one qualifying sentence with the 81% arithmetic into Step 4 (REV L222) and flag 5. Type MISSING. Loop A4.

### Claim C. FY27 tracks "at or above Base" on revenue, PAT and EPS; branch "AT OR ABOVE BASE"; upside flag Q2 x 4 = 940.37 Cr (REV L328-L337, L427-L428, L577 flag 10)

Strongest bear counter. PAT and EPS clear Base pro-rata only with the other income A4 itself calls unexplained. A4 makes the ex-OI basis govern trigger 1 for exactly this reason (REV L355), but lands PAT and EPS on reported figures.
- Unexplained H1 OI: 25.65 - 6.63 - 4.59 = 14.43 Mn (RES L413, L480, L483). After tax at the H1 ETR of 26.22%: 10.65 Mn.
- H1 PAT ex that OI: 331.63 - 10.65 = 320.98 Mn = 32.10 Cr, below the Base pro-rata of 32.5 Cr and above Bear's 28.0 Cr (RES L427). On the Q1 + Q2 sum (329.98 Mn, RES L565) it is 31.93 Cr.
- EPS ex that OI: Rs 4.98 on 64.51 Mn (just above Base's 4.95); Rs 4.86 on 66.01 Mn (below Base).
- The 6A reading (REV L337) becomes: 2 at or above Base (revenue, EPS) and 2 between Bear and Base (margin, PAT) on the current share count; 1 and 3 on the post-allotment count. The 8A-W branch label "AT OR ABOVE BASE" (REV L428) then holds on revenue only.
- The Q2 x 4 annualisation (940.37 Cr) extrapolates the quarter whose QoQ step was about 81% concentrated (Claim B).

Bull reading kept. A 50% pro-rata test understates an H2-heavy year (H2 FY26 was 59.9% of FY26 revenue), so a 0.4 Cr shortfall at H1 is not meaningful; revenue lands above Base pro-rata on any basis.

Separating observation: the Q4 call or FY27 AR naming the 1.44 Cr of other income (Q4, REV L463), and FY27 PAT ex-OI against 65 Cr.

Survives? YES. Absent from A4. Graft into 6A (a second reading line), the 8A-W branch line, and flag 10. Type MISSING (the basis inconsistency with REV L355 is noted, not separately tagged). Loop A4.

### Mandatory acquisition-economics probe: DOES NOT FIRE

No acquisition, purchase of a business, or stake buy is described. Evidence: "Investment in shares" is nil in both halves (RES L503; R339-R340); Note 5 says the company has no subsidiary, associate or JV (RES L243-L244); a case-insensitive grep of all three fulltexts for acqui / stake / takeover / amalgamation / merger finds only "acquiring new customers" (PPT L479). The non-current investment of 4.96 Cr is unchanged (RES L442). The nearest analogue is the greenfield seamless tube plant: ~Rs 167 Cr (PPT L251) = 1.9x FY26 operating EBITDA (87.95 Cr) and 32% of Sep-26 equity (522.95 Cr, RES L457). The deck says it is "funded through a mix of debt & internal accruals" (PPT L257-L260), while H1 FCF is -54.85 Cr (RES L496-L498). A4 already carries this at 6B #8 (REV L350). No further graft.

---

## FINDINGS REGISTER (tagged)

| ID | Type | Finding | Line evidence | Loop |
|---|---|---|---|---|
| F1 | MISSING | PPT p15 milestone "Established foundry Unit-V, a high-pressure mould line along with its machine shop" has no structured row and no ledger unit. With p24 (PPT L511-L515), two slides say an HPML already exists; A4 cites p24 only (REV L382). | PPT L341-L346; PPT L116; PR L66-L67 | A2 (then A3, A4) |
| F2 | MISSING | Surviving bear counter A (YoY base effect; H1 FY27 core PBT 12.1% below H2 FY26) absent. | RES L412-L422; PPT L617; PPT L102 | A4 |
| F3 | MISSING | Surviving bear counter B (about 81% of the QoQ step from the trailer half and from the top 5) not quantified; Step 4 "recurring" label unqualified. | PPT L395-L397, L788; RES L412; REV L222 | A4 |
| F4 | MISSING | Surviving bear counter C (PAT/EPS "at Base" depends on unexplained OI; ex-OI H1 PAT 32.10 Cr vs 32.5 Cr Base pro-rata) absent. | RES L413, L427, L480, L483; REV L337, L355, L428 | A4 |
| F5 | MISSING | Other non-current assets +36.81 Mn investing outflow (RES R225/R226/R333) cited nowhere; on that basis capex is +7.0% not -3.3%, FCF -58.53 Cr not -54.85 Cr. | RES L444, L500; REV L247-L248 | A4 |
| F6 | MISSING | FY22-FY26 revenue and gross margin (PPT R416-R438, not scrambled) cited nowhere; GM 40.7-46.1% band qualifies the 8C thresholds; FY25 revenue flat. | PPT L616-L620; REV L444-L445 | A4 |
| F7 | FACTUAL | "Forward EPS dilution up to 4.65%" is the share-count increase; EPS falls 4.44% (equity leg 2.27%). | RES L238, L434; REV L76 | A4 |

CONTRADICTION findings: none. A4's RES, PR and PPT line cites in Steps 0-8.5 and the brief were checked against the fulltexts; every cite checked lands on the stated content.

---

## VERDICT

VERDICT: INCOMPLETE.
- Failing agents: A2 (F1, MISSING: one fresh-pass unit absent from the ledger), then A3 (one forensic line on F1), then A4 (F2-F6 MISSING, F7 FACTUAL).
- loop_back_to: A2. The A2 and A3 work is one unit each; the substantive work is A4's six grafts and one fix.
- Exact gap: see the YAML gap field.
- Not failing: the plain-language brief gate (all five parts present), the arithmetic (one label error, everything else ties within rounding), and the ledger counts (every count matches a fresh grep).

---

## STYLE NOTES (logged; no re-run)

- S1. REV L8 says the review is split into this file and review_kross_q2fy27.part2.md, and the YAML review_path (REV L733) still names the part-2 file. The audited file already holds both parts (L1-L735). Update the two lines.
- S2. REV L193: "4 bps" below the FY26 margin is 4.8 bps unrounded (13.064% vs 13.016%). Display rounding.
- S3. REV L251: Sep-26 inventory days recompute to 85.9 (1,096.56 / 2,334.84 x 183 = 85.95), and the like-for-like change to -1.5 days. Rounding level.
- S4. REV L225: Q2 ETR is 180 bps above 25.168% unrounded, not 179. Rounding level.
- S5. REV L217: the ETR-change label credits the base effect to the 1.16 Mn earlier-years tax. That item explains about 0.98 pp of the 4.68 pp ETR fall (2.64 of 12.62 Mn). The rest is the deferred-tax ratio, 9.77% of PBT in Q2 FY26 vs 4.88% in Q2 FY27 (RES L425), net of a higher current-tax ratio, 20.88% to 22.09% (RES L423). Step 2 diagnostic 4 (REV L170) names both; the label is shorthand.
- S6. REV L222 taxes the OI change at the current ETR; the bridge (REV L216) taxes the PBT change at the prior ETR. On the bridge's basis the recurring share is 82.5%, not 82.0%. Immaterial.
- S7. REV L254: "~20.5 Cr capitalised" uses total D&A, which includes RoU and intangible amortisation (about 0.30 Cr net of the 4.16 Mn additions, RES L440-L441, L498). PPE-only is about 20.2 Cr. The "~" covers it.
- S8. REV L352 compares A4's average-CE H1 ROCE (16.76%) with a SECONDARY FY26 16%. A like-for-like closing-CE figure is computable from filed lines: H1 FY27 annualised 15.48% (992.98 / 6,416.35 Mn) vs FY26 15.29% (REV L335). It supports "flat" on filed numbers; cite it.
- S9. Forward-map rows at REV L640, L642, L644 are undated (ND). Correct under the NOT FOUND rule; noted only.
- S10. Optional corroboration for Q9 (REV L473): the deck's EPS Q-o-Q of 47.9% (PPT L785) equals PAT Q-o-Q, while the printed EPS gives 3.08 / 2.06 = +49.5%. The deck's own growth figure implies Q2 EPS of about Rs 3.05, which supports RES-F14-01.

---

```yaml
stage: A5-adversary
company: "KROSS"
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
    - "PPT p15 fulltext L341-L346: 'Established foundry Unit-V, a high-pressure mould line along with its machine shop' (milestone before the 16-Sep-2024 listing). No A1 structured row (p15 rows R313-R333 hold years and counterparties only), so no ledger unit. Bears on the HPML trigger: with PPT L511-L515 two slides say an HPML exists, while PPT L116 and PR L66-L67 say installation is in progress."
arithmetic_mismatches:
  - {metric: "Forward EPS dilution on full conversion (review L76, 0D Note 4 row)", a4_value: "up to 4.65%", recomputed: "EPS -4.44% (1 - 64.51/67.51); 4.65% is the share-count increase (3.0/64.51); equity leg EPS -2.27% (1 - 64.51/66.01)", source_line: "RES L238 (15,00,000 shares + 15,00,000 warrants); RES L434 (paid-up 322.55 Mn at FV Rs 5)"}
surviving_bear_counters:
  - {claim: "The growth is real: revenue +79.6% YoY to Rs 235.09 Cr, core PBT +129.9%, trajectory stepping up (review L586-L589, L167, L169, L193)", counter: "YoY base is a trough. Q2 FY26 revenue 130.92 Cr was -6.1% vs Q1 FY26 and 35.0% below the H2 FY26 average quarter (201.46 Cr). FY25 revenue was flat on FY24 (620.4 vs 620.3 Cr). FY26 H2 revenue was 1.49x H1, far above MGMT's 10-15% seasonality. H1 FY27 revenue is +4.1% over H2 FY26 and H1 FY27 core PBT ex-OI is 12.1% below it (42.38 vs 48.23 Cr); Q2 core PBT is +2.8% over the H2 FY26 average quarter. Bull reading: H1 is the weak half. Separating observation: H2 FY27 revenue vs 461-482 Cr (H1 x 1.10-1.15) and Q3 core PBT vs 24.78 Cr.", source_line: "RES L412-L422 (H1 FY26 and FY26 columns); PPT L617; PPT L102", type: MISSING}
  - {claim: "82% of the PAT change is recurring core; PAT still +124% to +133% YoY if other income reverts (review L222-L223)", counter: "Recurrence of the Q2 revenue level is unproven. About 81% of the Rs 50.75 Cr QoQ rise came from the trailer half (74.95 to 115.92 Cr; component half +8.9%) and 81% from the top-5 customers (109.63 to 150.95 Cr; others +12.6%), MGMT shares x FILED revenue. A4's own Q3 asks whether a one-time fleet order is in it. Bull reading: YoY growth was broad (trailer +103%, components +61%). Separating observation: Q3 trailer and top-5 shares vs 49.31% and 64.21%.", source_line: "PPT L395-L397; PPT L788; RES L412; review L462", type: MISSING}
  - {claim: "FY27 tracks at or above Base on revenue, PAT and EPS; branch AT OR ABOVE BASE; upside flag Q2 x 4 = 940.37 Cr (review L337, L428, L577)", counter: "PAT and EPS clear Base pro-rata only with the 14.43 Mn of H1 other income A4 calls unexplained (and excludes for trigger 1 at review L355). Ex that OI after tax (10.65 Mn), H1 PAT = 32.10 Cr vs Base pro-rata 32.5 Cr (between Bear and Base); EPS Rs 4.86 on 66.01 Mn vs 4.95. Reading becomes 2 at/above and 2 between on the current count, 1 and 3 post-allotment. Bull reading: 50% pro-rata understates an H2-heavy year. Separating observation: identity of the 1.44 Cr OI (Q4) and FY27 PAT ex-OI vs 65 Cr.", source_line: "RES L413, L427, L480, L483, L565; review L328-L337, L355", type: MISSING}
findings_by_type:
  factual:
    - "F7: review L76 'Forward EPS dilution up to 4.65%' is the share-count increase; EPS falls 4.44% on full conversion (equity leg 2.27%). RES L238, L434. Loop A4."
  missing:
    - "F1: PPT L341-L346 Unit-V high-pressure mould line milestone has no structured row and no ledger unit; A4 cites only p24 (review L382) for the HPML conflict. Loop A2, then A3, then A4."
    - "F2: surviving bear counter A (YoY base effect; H1 FY27 core PBT 12.1% below H2 FY26; FY25 revenue flat, PPT L617) absent from Steps 2-3 and the brief. Loop A4."
    - "F3: surviving bear counter B (about 81% of the QoQ step from the trailer half and from the top 5; PPT L395-L397, L788) not quantified; Step 4 'recurring' label (review L222) unqualified. Loop A4."
    - "F4: surviving bear counter C (ex-unexplained-OI H1 PAT 32.10 Cr below Base pro-rata 32.5 Cr; EPS 4.86 on 66.01 Mn) absent from 6A and 8A-W (review L337, L428). Loop A4."
    - "F5: RES R225/R226/R333 other non-current assets +36.81 Mn investing outflow (RES L444, L500) cited nowhere; on that basis H1 capex is 63.26 Cr (+7.0%, not -3.3%) and FCF -58.53 Cr vs -54.03 Cr (worse, not flat). Loop A4."
    - "F6: PPT R416-R438 FY22-FY26 revenue and gross margin (PPT L616-L620; not scrambled) cited nowhere; GM 46.1/40.7/42.6/43.0/45.7% shows FY26 was the five-year high and Q2's 43.90% sits above FY23-FY25, which qualifies the 8C thresholds (review L444-L445). Loop A4."
  contradiction: []
  style:
    - "S1: review L8 and L733 still describe a separate part-2 file; the audited file holds both parts."
    - "S2: review L193 '4 bps' is 4.8 bps unrounded."
    - "S3: review L251 Sep-26 inventory days 85.9 not 86.0; like-for-like -1.5 not -1.4."
    - "S4: review L225 ETR 180 bps above 25.168% unrounded, not 179."
    - "S5: review L217 ETR label credits the 1.16 Mn earlier-years tax; it explains about 0.98 of 4.68 pp; the rest is the deferred-tax ratio (RES L425) net of a higher current-tax ratio (RES L423)."
    - "S6: review L222 taxes the OI change at current ETR vs the bridge's prior ETR; recurring 82.5% on one basis. Immaterial."
    - "S7: review L254 ~20.5 Cr capitalised uses total D&A; PPE-only about 20.2 Cr."
    - "S8: review L352 could cite the like-for-like closing-CE ROCE 15.48% vs FY26 15.29%; supports flat."
    - "S9: forward-map rows at review L640, L642, L644 undated (ND); correct under NOT FOUND."
    - "S10: PPT L785 EPS Q-o-Q 47.9% equals PAT Q-o-Q; implies Q2 EPS about Rs 3.05; optional support for Q9."
loop_back_to: "A2"
gap: "A2: add a ledger unit for PPT p15 L341-L346 (Unit-V high-pressure mould line milestone, no A1 structured row). A3: one forensic line reading it with PPT L511-L515 against PPT L116 and PR L66-L67. A4: (1) graft bear counter A (YoY base effect; H1 FY27 revenue +4.1% and core PBT -12.1% vs H2 FY26; FY25 revenue flat, PPT L617) into Step 2 diagnostics 1 and 3, the Step 3 trajectory line and the brief, with the bull reading and the H2 FY27 461-482 Cr test; (2) graft counter B (about 81% of the Rs 50.75 Cr QoQ step from the trailer half and from the top 5) into Step 4 L222 and flag 5; (3) graft counter C (ex-unexplained-OI H1 PAT 32.10 Cr vs Base pro-rata 32.5 Cr; EPS 4.86 on 66.01 Mn) into 6A L337, 8A-W L428 and flag 10; (4) fix L76 to share count +4.65% and EPS -4.44%; (5) cite other non-current assets +36.81 Mn (RES L444, L500) with capex and FCF on both bases and add it to Q11; (6) cite FY22-FY26 gross margin 40.7-46.1% (PPT L620) against the 8C thresholds with both readings; (7) add the p15/p24 HPML point to 6D and Q13."
style_notes:
  - "S1: update review L8 and L733; the part-2 content is already in the audited file."
  - "S2-S4: three display-rounding differences (review L193, L225, L251); none changes a number at its displayed purpose."
  - "S5-S7: labelling and basis notes on the tax bridge and capitalisation (review L217, L222, L254)."
  - "S8: cite closing-CE ROCE 15.48% vs 15.29% at review L352."
  - "S9: undated forward-map rows are correct ND."
  - "S10: PPT L785 EPS Q-o-Q supports RES-F14-01; optional cite in Q9."
analyst_note: "A4's arithmetic is clean: every Step 1 to 6.5 metric recomputes within rounding from RES L412-L519, and every checked anchor lands. The one formula error is the 4.65% EPS-dilution label. The audit fails on completeness. Three bear counters survive from the same extract: the YoY base effect (on a sequential basis H1 FY27 core PBT is 12.1% below H2 FY26), the concentration of the QoQ step (about 81% from the trailer half and from the top 5), and the dependence of the PAT 'at Base' reading on unexplained other income. Each has a bull reading (H2 seasonality; broad YoY growth across both halves; pro-rata understates an H2-heavy year), so the grafts should state both readings and the separating observation, not replace A4's view. The A2 fix is one ledger row (PPT L341-L346) and the A3 fix is one line; the substantive work is A4's. No acquisition is described, so the purchase-economics probe does not fire; the seamless capex funding is already at 6B #8."
```
