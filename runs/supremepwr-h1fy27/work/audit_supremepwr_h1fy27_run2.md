# A5 ADVERSARY / COMPLETENESS AUDIT: SUPREMEPWR (Supreme Power Equipment Limited), H1 FY27 results

Auditor: A5 (claude-opus-5-5). Audit date: 2026-10-17. Fresh context.
Inputs read: A4 review (correction loop 1), A1 fulltext, A1 structured (R001-R554), A2 ledger (incl. M01-M18). Source PDF, inputs/ and A3 not opened.
Anchor convention: "L###" = A1 fulltext line; "R###" = A1 structured row; "rev ###" = A4 review line; "led ###" = A2 ledger line. Figures in Rs lakh unless marked Cr (1 Cr = 100 lakh).

---

## AUDIT 0. DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: (1) summary narrative PRESENT (rev 626-634, about 300 words, figures tagged FILED/INFERENCE); (2) sector intelligence PRESENT (rev 636-641); (3) business-model intelligence PRESENT (rev 643-648); (4) competition intelligence PRESENT (rev 650-654); (5) forward map PRESENT (rev 656-662: six dated catalysts, each with a bull and a bear fork). Gate: PASS.

---

## AUDIT 1. COVERAGE

Fresh pass: grep and line sweep over the fulltext (L1-L1193, primary text layer and the L873-L1192 re-OCR), mapped to structured IDs and to ledger rows.

| Category | A2 count | My fresh count | Orphan / unmatched | Status |
|---|---|---|---|---|
| Notes | 21 (led 4) | 21: SA 8 (L294, L301, L305, L321, L323, L325, L329, L330), CON 9 (L658-696), CF 4 (L1019-1020, L1184-1185). Certificate notes R553/R554, CON header R535, BS footers R515/R534 listed separately | none | PASS |
| Line items | 153 structured + M01, M02, M08 (3 rows), M09, M12-M15 (led 5) | 153 structured: SA P&L 22 (+M01 L900, M02 L905, M12 L899); SA BS 23; SA CF 30 (+M03-M07 L995-1001, M08 L387/L395/L1015, M14 L982, M15 L379); CON P&L 25 (+M09 L1063, M13 L1060); CON BS 23; CON CF 30 | none (label-only "Paid up Equity Share Capital" rows carry no value: STYLE S-3) | PASS |
| Zero-standing | 13 line items (led 6; 21 dash cells) + 8 M rows | 13 line items, 21 dash cells (R051-054, R142, R163, R172, R175, R177, R187, R245-248, R261, R263, R353-355, R379, R391) + M01-M07, M09 | none | PASS |
| Agenda items | 2 (led 7) | 2 (L38, L45) | none | PASS |
| Auditor paragraphs | 9 structured groups + M10, M11, M16, M17 (led 8, 232-243) | 14 paragraphs (SA: L90, L97 [M16], L104, L119, L124 [M10], signature L136; CON: L432, L440 [M17], L449, L462, L467, L472, L476 [M11], signature L489) + certificate signature L858; all map to a structured row or M row | none | PASS |
| Entities | 20 + M18 (led 9) | 21 (R442-R461 + Audit Committee L40/L295/L660) | none | PASS |
| Forward | 10 (led 10) | 10 (L312, L313, L314, L318, L321, L686, L849, L853, L856, L818-825) | none | PASS |
| Dates | 35 (led 11) | 35 matched + 3 unmatched: signing dates L339 (SA notes page), L708 (CON notes page), L1192 (CON CF page). A1 rows the same stamp on SA BS (R485), SA CF (R487) and CON BS (R493) | 3 missing from structured and ledger | FAIL (M-1, A2) |
| Qualifiers | 48 (led 12) | 48 matched + 4 unmatched: column audit-status headers L214 (SA BS: 30-Sep-26 Unaudited / 31-Mar-26 Audited), L349 and L974 (SA CF: H1FY27 Unaudited / FY26 Audited), L588 (CON BS), L725 (CON CF). A1 rows this header for the two P&Ls only (R512 L161, R532 L1041) | 4 missing from structured and ledger | FAIL (M-1, A2) |
| ID reconciliation | 554 referenced, 0 orphan IDs (led 17) | R001-R554 contiguous (NUMBER 441, ENTITY 20, FORWARD 10, DATE 35, QUALIFIER 48); every ID referenced in led 21-297 | none | PASS |
| Ledger rows vs A4 | 572 IDs (554 R + 18 M) | A4 disposes all 572 by register reference (rev 16-22: 154 cited + 136 routed + 282 reviewed-no-finding = 572); A4 itself names a disposition for all 21 notes (rev 25) and all M12-M18 (rev 26), and cites every P&L, BS and CF range it uses | none found | PASS |

Notes on the coverage audit:
- A2's count test reports grep = sweep for dates (35/35) and qualifiers (48/48) (led 11-12). Those figures equal A1's row counts; the fulltext units above were not caught, so the count test did not run independently for these two categories.
- Orphan spot-check: the ID ranges A4 does not cite by number (face value R087-R090, identifiers R418-R441, signature and date rows, duplicate CF totals R384/R396/R398, certificate numbers R407-R410) carry no forensic content A4 leaves unaddressed. The rows behind the adversarial findings below (R015-R018 vs R209-R212; R105-R108 vs R313-R316; R127-R128 vs R333-R334; R019-R022 vs R213-R216) are cited in A4. The gap there is analysis, not citation.

---

## AUDIT 2. ARITHMETIC

Every derived metric in A4's tables was recomputed from the raw A1 rows. Tolerance: rounding at the stated precision.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| SA Op EBITDA H1FY27 / H1FY26 / H2FY26 / FY26 (Cr) | 21.37 / 12.53 / 16.12 / 28.65 (rev 165) | 2,136.89 / 1,252.84 / 1,612.36 / 2,865.20 | L901, L892, L891, L884 | PASS |
| SA Op EBITDA margin | 16.81 / 15.53 / 14.74 / 15.07% | 16.808 / 15.532 / 14.736 / 15.074% | L883 | PASS |
| SA reported EBITDA, core PBT | 22.67 / 13.49 / 17.49 / 30.99; 16.57 / 11.31 / 13.28 / 24.58 | 2,267.08 / 1,349.40 / 1,749.31 / 3,098.71; 1,657.48 / 1,130.68 / 1,327.68 / 2,458.36 | L884-901 | PASS |
| SA OI / PBT | 7.28 / 7.87 / 9.35 / 8.67% | 7.283 / 7.868 / 9.350 / 8.675% | L884, L901 | PASS |
| SA ETR | 23.64 / 23.33 / 24.68 / 24.07% | 422.57/1,787.67; 286.36/1,227.24 (DT 0.30 credit); 361.45/1,464.63; 647.81/2,691.87 | L903-904 | PASS |
| SA H1FY26 deferred tax sign | 0.30 credit (rev 45) | 1,227.24 - 286.66 + 0.30 = 940.88 vs PAT 940.87; FY26 117.36 - 0.30 = 117.06 | L901-904, L194 | PASS |
| SA PAT margin | 10.74 / 11.66 / 10.08 / 10.75% | 10.737 / 11.665 / 10.082 / 10.754% | L194, L883 | PASS |
| SA gross margin | 24.67 / 22.36 / 20.99 / 21.57% | GP 3,136.58 / 1,803.56 / 2,296.23 / 4,099.80 on revenue | L883, L887-888 | PASS |
| SA total expenses H1FY27 | ND (rev 150) | line sum 11,056.61 vs TI - PBT 11,056.31 (0.30 residual); R043 11,086.31 off by 30.00 | L885-894, L901 | PASS (ND correct) |
| CON Op EBITDA H1FY27 / H1FY26 / H2FY26 / FY26 (Cr) | 23.35 / 14.11 / 18.71 / 32.82 (rev 206) | 2,335.45 / 1,411.31 / 1,871.11 / 3,282.42 | L1043-1064 | PASS |
| CON Op EBITDA margin | 17.26 / 18.77 / 17.58 / 18.07% | 17.260 / 18.769 / 17.578 / 18.071% | L1042 | PASS |
| CON ETR | 26.19 / 26.17 / 28.59 / 27.50% | 488.72/1,866.01; 336.81/1,287.07; 447.29/1,564.59; 784.10/2,851.66 | L1067-1071 | PASS |
| CON prior-year tax placement | 0.37 lakh charge H2FY26 and FY26 (rev 49) | H2: 1,564.59 - 329.27 - 117.65 - 0.37 = 1,117.30 vs 1,117.29 | L1071-1072 | PASS |
| CON PAT margin; gross margin | 10.18 / 12.64 / 10.50 / 11.38%; 25.22 / 26.51 / 24.72 / 25.46% | 10.179 / 12.637 / 10.496 / 11.383%; GP 3,412.96 / 1,993.29 / 2,631.20 / 4,624.48 | L1042-1072 | PASS |
| CON total expenses H1FY27 | 116.91 (foots) | line sum 11,691.35 | L1046-1053 | PASS |
| S-vs-C revenue gap | (5.47) / (2.97) / (8.44) / +8.17 | -546.66 / -297.03 / -843.69 / +817.12 | L883 vs L1042 | PASS |
| S-vs-C Op EBITDA gap; % of SA PAT | 1.58 / 2.59 / 4.17 / 1.99; 16.8 / 23.5 / 20.4 / 14.5% | 158.47 / 258.75 / 417.22 / 198.56; 16.84 / 23.45 / 20.41 / 14.55% | derived | PASS |
| Group PAT incl. MI gap, % SA PAT | 1.00 / 1.28 / 1.15 / 0.89% | 9.39/940.87; 14.11/1,103.18; 23.50/2,044.06; 12.20/1,365.09 | L1072-1073, L194 | PASS |
| Danya PAT (MI x 10); % CON PAT | 0.94 / 1.41 / 2.35 / 1.22; 9.9 / 12.6 / 11.4 / 8.85% | 93.9 / 141.1 / 235.0 / 121.9; 9.88 / 12.63 / 11.37 / 8.85% | L1073 | PASS |
| Implied Danya employee cost | 0.66 / (0.44) / 0.22 / 0.11 | 66.04 / -43.59 / 22.45 / 10.92 | L890 vs L1049 | PASS |
| Receivables build, CON minus SA | at least 8.65 (8.65 / 8.68 / 11.68) | 1,583.64 - 718.82 = 864.82; - 715.82 = 867.82; - 415.82 = 1,167.82 | L1164, L988, L954 | PASS |
| CON YoY: revenue, Op EBITDA, core PBT, PBT, group PAT, owners PAT, EPS | +79.95 / +65.48 / +44.74 / +44.98 / +44.94 / +45.09 / +45.21% | 6,011.47/7,519.44; 924.14/1,411.31; 568.65/1,270.91; 578.94/1,287.07; 427.03/950.26; 424.23/940.87; 1.70/3.76 | L1042-1080 | PASS |
| CON YoY D&A, FC, EBIT | +415.4 / +189.5 / +55.38% | 204.10/39.60; 291.79/100.80; 2,131.35/1,371.71 | L1050-1051 | PASS |
| SA YoY: revenue, Op EBITDA, core PBT, PBT, PAT | +57.62 / +70.56 / +46.59 / +45.67 / +45.09% | 4,647.69/8,066.10; 884.05/1,252.84; 526.80/1,130.68; 560.43/1,227.24; 424.22/940.87 | L883-L194 | PASS |
| Margin moves (bps) | CON -151, SA +128; GM CON -129, SA +231 | -150.9 / +127.6; -128.6 / +231.1 | derived | PASS |
| D&A + FC as % CON revenue | 1.87% to 3.67% | 140.40/7,519.44 = 1.867%; 495.89/13,530.91 = 3.665% | L1050-1051 | PASS |
| HoH | CON +41.56 / +27.12%; SA +35.65 / +16.20%; core PBT +19.87 / +24.84% | 10,644.60/7,519.44; 13,530.91/10,644.60; 10,941.63/8,066.10; 12,713.79/10,941.63; 1,839.56/1,534.63; 1,657.48/1,327.68 | L883, L1042 | PASS |
| CON PAT bridge (rev 314-325) | +15.94, -1.74, -4.96, -1.65, -1.91, +0.10, -1.52, -0.00 = +4.27 | 1,593.55 - 173.88 - 495.53 - 164.50 - 190.99 + 10.29 - 151.50 - 0.41 = 427.03 = 1,377.29 - 950.26 | L1042-1072 | PASS |
| SA PAT bridge (rev 332-341) | +10.39, +2.94, -4.49, -1.64, -1.93, +0.34, -1.31, -0.05 = +4.24 | 1,039.21 + 293.81 - 448.97 - 164.22 - 193.03 + 33.63 - 130.77 - 5.44 = 424.22 = 1,365.09 - 940.87 | L883-904, L194 | PASS |
| CON CF: WC change, cash generated, CFO | (26.75); (363.76); (573.76) | -1,583.64 - 2,535.78 - 495.81 + 103.51 + 2,239.25 - 402.63 = -2,675.10; 2,311.34 - 2,675.10; - 210.00 | L1162-1170, L747-750 | PASS |
| CON CF FY26 WC | +2.82 | 282.35 | L1164-1169 | PASS |
| CON CFO/PAT; FCF | 1.25x / -0.42x; (31.58) / (14.42) | 2,590.47/2,067.56; -573.76/1,377.29; -1,441.61 | L750, L752, L1072 | PASS |
| CON receivable / inventory / payable days | 80.10 to 84.77; 141.04 to 158.18; 116.77 to 122.34 | 80.095 / 84.774; 141.035 / 158.177; 116.766 / 122.339 | L1132, L1131, L1116-1118, L1042-1047 | PASS |
| CON CCC | 104.36 to 120.61 | 104.364 / 120.612 | derived | PASS |
| CON gross debt, net debt | 49.97 to 57.45; 40.23 to 57.20 (+42.2%) | 4,997.30 / 5,744.56; 4,022.75 / 5,719.75 (+42.18%) | L1110, L1114, L1133 | PASS |
| CON trade payables / gross debt | 147.3% | 8,459.28 / 5,744.56 | L1116-1118 | PASS |
| SA CF WC change | (24.16) A3-13 reading; (24.19) as extracted; FY26 +4.71 | -2,415.67; -2,418.67; +471.18 | L987-993 | PASS |
| SA CFO recompute | (522.96) | -305.20 - 217.76 | L994, L998 | PASS |
| SA CFO/PAT; FCF | 1.36x / -0.38x; (29.73) / (13.79) | 2,773.36/2,044.06; -522.90/1,365.09; 2,773.36 - 5,746.46; -522.90 - 855.85 | L999, L1003, L1006 | PASS |
| SA inventory / payable / receivable days; CCC | 95.92 to 134.60; 107.86 to 114.68; 75.38; 95.30 | 95.917 / 134.596; 107.855 / 114.680; 75.379; 95.30 | L953, L937-939, L954, L887-888 | PASS |
| SA gross debt, net debt, ND/NW | 45.73 to 55.02; 35.99 to 54.80 (+52.3%); 0.32x to 0.43x | 4,572.70 / 5,502.09; 3,598.91 / 5,480.18 (+52.27%); 0.319 / 0.433 | L930, L934, L955, L926-927 | PASS |
| SA BS footing 30-Sep-26 | 28,802.45 | E&L 28,802.45 = assets 28,802.45 | L926-956 | PASS |
| SA Mar-26 BS on the A3-13 reading | 24,873.69 vs 24,873.68 | assets with receivables 4,521.09 = 24,873.69; E&L = 24,873.68 (with 4,821.09 assets = 25,173.69) | L926-956 | PASS |
| OCA BS change minus CF = taxes paid | 217.76 | 739.73 - 521.97 = 217.76 (CON: 705.81 - 495.81 = 210.00) | L956, L990, L998; L1134, L1166, L1170 | PASS |
| Danya capital roll | 12.68 to 16.52 = 2.75 cash + 1.10 share | 1,267.73 + 274.59 + 109.73 = 1,652.05 | L950, L1007, L983 | PASS |
| Danya multiple / yield | 7.5x / 13.3% | 1,652.05 / 219.46 = 7.53x; 219.46 / 1,652.05 = 13.28% | derived | PASS (text slip: STYLE S-1) |
| Danya PBT, tax, tax rate | 188.07, 66.15, 35.2% | 1,866.01 - 1,787.67 + 109.73; 488.72 - 422.57; 35.17% | L1064, L901, L983, L1067-1069, L903-904 | PASS |
| Danya pre-tax return | 18.3% / 18.2% | 376.14 / 2,051.00; 399.50 / 2,196.28 | L950, L1108, L1110-1114 vs L930-934 | PASS |
| Danya term debt | 317.80 to 21.35 | 3,311.60 - 2,993.80; 3,526.02 - 3,504.67 | L1110, L930 | PASS (context: STYLE S-2) |
| SA funding cost | 11.1% pre-tax / 8.3% post-tax | 560.22 / 5,037.40 = 11.12%; x 0.7483 = 8.32% | L891, L930, L934 | PASS |
| ROCE SA / CON / CON ex MI | 23.6 / 23.6 / 24.1% | 4,135.56 / 17,540.62; 4,315.60 / 18,277.01; 4,315.60 / 17,874.15 | L891, L901, L1050, L1064, BS | PASS |
| ROCE with trade payables as capital | 17.0 / 16.8% | 4,135.56 / 24,298.01; 4,315.60 / 25,616.66 | derived | PASS |
| MSE dues as days of spend; GST-grossed | 42.0 / 52.7; 35.6 / 44.7 | 3,103.72/13,511.53 x 183; 4,083.10/14,178.90 x 183; / 1.18 | L937, L1116, L887-893, L1003, L1046-1052, L752 | PASS |
| MSE share of payables | 41.1 / 48.3% | 3,103.72/7,560.72; 4,083.10/8,459.28 | same | PASS |
| Warrant balance; full-conversion count | 15.81 Cr; 2,62,38,135 (+4.99%) | 12,47,000 x 126.75 = 15,80,57,250; 12,47,000 / 2,49,91,135 = 4.990% | L842-846, L910 | PASS |
| Implied treasury-stock price | about Rs 135 | incremental 76,195 shares: 126.75 / (1 - 76,195/12,47,000) = 135.0 | L910-911 | PASS |
| EPS basic / diluted, all periods | 5.46 / 5.45; 4.41 / 4.40; 3.76 / 3.76; 8.18 / 8.15 | PAT / weighted counts | L907-911, L1080-1087 | PASS |
| DT vs DTL; deferral bps; ETR ex Danya share | 77.17 = 212.10 - 134.93; 432 bps; 25.18% | 77.17; 77.17/1,787.67 = 4.317%; 422.57/1,677.94 = 25.18% | L904, L931 | PASS |
| Trailing PAT / EPS | 24.68 Cr / Rs 9.87 | 1,103.18 + 1,365.10; 4.41 + 5.46 | L1074, L1080 | PASS |

Arithmetic mismatches above rounding: none.

---

## AUDIT 3. ADVERSARIAL READ

### Claim 1 (most positive): "Growth is real at PBT; about 98% of the PBT change is recurring; not driven by other income" (rev 278, rev 346, rev 730)
- Strongest bear counter from the extract: the growth did not convert to cash. CON CFO (573.76) against PAT 1,377.29 (L750, L1072); receivables +1,583.64 and inventory +2,535.78 in one half (L1164-1165); the revenue booked outside the parent (+817.12) came with a receivables build at least 864.82 above the parent's (L1164 vs L988); D&A and finance cost outran revenue (L1050-1051).
- Additional test: does the nil unrealised-profit elimination (Claim 2) inflate H1FY27 growth? No. Danya's implied stock rose only 48.03 in H1FY27 (L1047 vs L888) against 472.94 in H1FY26, so any unremoved margin would sit more in the base half than in the current half.
- Survives: YES. Already incorporated in A4 (rev 279, rev 281, rev 300). No new graft.

### Claim 2: "PAT ties to the rupee because standalone books the Danya share"; "the consolidated statement is the economic view of the group"; "the headline numbers tie internally" (rev 234, rev 217, rev 617)
- Strongest bear counter from the extract (two legs, both absent from A4):
  - Two-way goods trade with an MD-co-owned firm. CON purchases sit BELOW SA purchases in every FY26 period: H1FY26 6,900.07 vs 7,163.52 (-263.45); H2FY26 9,695.02 vs 10,047.21 (-352.19); FY26 16,595.10 vs 17,210.72 (-615.62) (L1046 vs L887). Under line-by-line elimination (CON note 3, L677-679), CON purchases minus SA purchases = Danya's third-party purchases minus the parent's purchases from Danya. A negative figure means the parent bought at least Rs 6.16 Cr from Danya in FY26 beyond Danya's own third-party buying. In the same year CON revenue sits Rs 8.44 Cr below SA (L1042 vs L883), so the parent sold at least Rs 8.44 Cr into Danya beyond Danya's external sales. CON "other creditors" sit below SA by 447.78 at 31-Mar-26 (2,627.00 L1118 vs 3,074.78 L939) and by 80.82 at 30-Sep-26 (4,376.18 vs 4,457.00), while CON MSE dues exceed SA (L1116 vs L937). Under consistent classification that is possible only if the parent owed Danya at least Rs 4.48 Cr at 31-Mar-26, or if consolidation regrouped balances. A4 rev 234 says "two cost lines consolidate below standalone in some periods"; purchases, the largest cost line, also consolidates below standalone in all three FY26 periods, and A4 does not draw the inference.
  - No unrealised profit eliminated in any period. CON owners PAT equals SA PAT in all four periods: 940.87 = 940.87; 1,103.18 = 1,103.18; 2,044.06 = 2,044.06; 1,365.10 vs 1,365.09 (L1074 vs L194). SA other income carries 90% of Danya's PAT (109.73 = 0.9 x 121.92) and MI carries 10% (12.19, L1073), so CON owners PAT minus SA PAT equals minus any consolidation adjustment. A zero gap in every period means the "unrealised profit in closing stock, if any" (L679) was eliminated at nil each time. Yet Danya's implied stock (CON minus SA inventories) was Rs 16.53 Cr at 31-Mar-26 and Rs 17.02 Cr at 30-Sep-26 (L1131 vs L953), 19.5% of group inventory, after a Rs 7.53 Cr build in FY26 (CON change in inventories 3,055.54 vs SA 2,302.79, L1047 vs L888; H1FY26 4.73 Cr, H2FY26 2.80 Cr) in the year the parent sold at least Rs 8.44 Cr into Danya.
  - Two readings. (1) Danya's stock holds no parent-sourced goods at any period end and the two-way trade is arm's-length operational flow; then nil is correct. (2) Goods cycle through the firm at undisclosed transfer prices and the elimination was not applied; then CON profit carries the parent's margin on goods still in Danya's stock. Bound [INFERENCE: upper bound, parent-sourced share not disclosed]: the FY26 build at the SA FY26 gross margin of 21.57% gives up to Rs 1.62 Cr pre-tax (5.7% of CON FY26 PBT 28.52 Cr); H1FY26 up to Rs 1.06 Cr (4.73 x 22.36%); H1FY27 up to about Rs 0.12 Cr (0.48 x 24.67%). Separating observation: intercompany sales, purchases and balances by direction at both dates, and the parent-sourced share of Danya's closing stock (FY27 audited consolidated accounts, AS 18 related-party note).
- Survives: YES. Not incorporated. Must be grafted (M-2, M-3).

### Claim 3: Danya capital bull: "the parent earns 13.3% post-tax on its Danya capital, above its after-tax cost of debt; the minority's 19.5% capital share against a 10% profit share subsidises the parent" (rev 431, rev 422, rev 426, rev 647)
- Strongest bear counter from the extract: the 13.3% yield rests on Danya profit that is earned partly on trade with the parent in both directions at prices the filing does not show (Claim 2 counter), and part of it may sit in Danya's Rs 17.02 Cr stock. The firm runs that stock with near-nil cash: CON minus SA cash is 2.90 lakh at 30-Sep-26 and 0.76 lakh at 31-Mar-26 (L1133 vs L955). The parent's exposure to Danya is the capital account (Rs 16.52 Cr, L950) plus trade balances in both directions, not the capital account alone.
- Survives: YES. Partly incorporated (unaudited status rev 429, intercompany-pricing reading in Q7 rev 565, 18.3% vs 23.6% rev 424). The stock, cash and trade-balance legs are not. Graft with M-2 and M-3.

### Mandatory acquisition-economics probe
- The filing describes no acquisition or stake buy (single subsidiary, L672-674; parent profit share fixed at 90%, L674). The nearest purchase is the parent's capital injection into Danya (274.59, L1007). A4 ran the probe on it (rev 417-431).
- Multiple, restated: closing capital Rs 16.52 Cr / annualised H1FY27 profit share Rs 2.19 Cr (109.73 x 2) = about 7.5x; 31-Mar-26 capital Rs 12.68 Cr / FY26 share Rs 2.12 Cr (0.9 x MI-derived Danya PAT 235.0, L1073) = about 6.0x. The Rs 2.75 Cr injected bought no extra profit share (90% before and after, L674), while the minority withdrew Rs 0.20 Cr (L1180).
- Quality markers: pre-tax return 18.3% vs group 23.6%; Danya debt Rs 2.42 Cr at 30-Sep-26 (down from Rs 4.25 Cr; L1110-1114 vs L930-934); cash near nil; stock Rs 17.02 Cr; receivables build at least Rs 8.65 Cr if intercompany balances held; customer tenure ND; profit -13.6% HoH (L1073); figures unaudited, review bracket unresolved (L684).
- Peak-year test: the H1FY27 share (Rs 1.10 Cr) sits below the H2FY26 share (0.9 x 1.41 = Rs 1.27 Cr), so the multiple is not flattered by a peak half. This is not a cheap high-quality asset: it is a working-capital-heavy, related-party firm on a mid-single-digit multiple of management-certified profit. The bear reading survives; A4 carries it (rev 431), and the M-2 and M-3 grafts complete it.

---

## FINDINGS

| ID | Type | Agent | Finding |
|---|---|---|---|
| M-1 | MISSING | A2 | Seven fulltext units have no structured row and no ledger row: column audit-status headers L214 (SA BS), L349/L974 (SA CF), L588 (CON BS), L725 (CON CF); signing dates L339 (SA notes page), L708 (CON notes page), L1192 (CON CF page). A1 rows the same kinds elsewhere (R512, R532; R485, R487, R493). A2's count test reports grep = sweep for dates and qualifiers (led 11-12) but recounts A1 rows. Materiality low; the BS/CF audit status supports A3-13 (an audited 31-Mar-26 balance sheet should foot). Fix: add as M19-M25; A3 disposes them. |
| M-2 | MISSING | A4 | Surviving bear counter not grafted: two-way goods trade with Danya. CON purchases below SA in H1FY26 (-2.63 Cr), H2FY26 (-3.52 Cr), FY26 (-6.16 Cr) (L1046 vs L887): the parent bought at least Rs 6.16 Cr from Danya in FY26. CON revenue below SA by Rs 8.44 Cr (L1042 vs L883): the parent sold at least Rs 8.44 Cr into Danya. CON other creditors below SA by Rs 4.48 Cr at 31-Mar-26 and Rs 0.81 Cr at 30-Sep-26 (L1118 vs L939): the parent owed Danya at least that, or balances were regrouped. Graft at rev 234 (correct "two cost lines" to name purchases), rev 431 (Danya readings), the flags (rev 616 and YAML flags), brief part 3 (rev 646 item c), and widen Q7 (rev 565) to purchases from Danya and balances by direction. |
| M-3 | MISSING | A4 | Surviving bear counter not grafted: nil unrealised-profit elimination. CON owners PAT = SA PAT in all four periods (L1074 vs L194), so no unrealised profit was eliminated (L679 "if any"), while Danya's implied stock stood at Rs 16.53 Cr / Rs 17.02 Cr (L1131 vs L953; 19.5% of group inventory) after a Rs 7.53 Cr FY26 build (L1047 vs L888), with near-nil cash (2.90 lakh, L1133 vs L955). Two readings and separating observation as in Claim 2. Bound up to Rs 1.62 Cr pre-tax in FY26 [INFERENCE]; H1FY27 growth not inflated. Graft at rev 234, rev 617 (qualify "headline numbers tie"), rev 431, the flags, and add a management question on the parent-sourced share of Danya's closing stock and the unrealised-profit computation. |

No FACTUAL or CONTRADICTION findings. No arithmetic mismatches.

---

## VERDICT

**INCOMPLETE.** Failing agents: A2 (M-1, MISSING: seven unenumerated fulltext units) and A4 (M-2 and M-3, MISSING: two surviving bear counters not grafted). Loop: A2 adds the seven rows; A3 disposes them; A4 grafts M-2 and M-3 and applies the style fixes. The brief gate passes, the arithmetic passes, and no orphan ledger row was found.

---

## STYLE NOTES (logged, no loop)

- S-1. rev 422: "16.52 / (1.10 x 2 = 2.19)". 1.10 x 2 is 2.20. Write "(109.73 lakh x 2 = 219.46 lakh)". The 7.5x and 13.3% stand.
- S-2. rev 571 and rev 701 (Q13): "Danya repaid Rs 2.96 Cr of its own". Write "repaid Rs 2.96 Cr of term debt; its short-term borrowings rose Rs 1.14 Cr, so its total debt fell Rs 1.82 Cr" (CON minus SA: LTB 317.80 to 21.35, L1110 vs L930; STB 106.80 to 221.12, L1114 vs L934). The term-debt figure stands.
- S-3. "Paid up Equity Share Capital" label rows in the SA P&L (L199, L909) and CON P&L (L572, L1083) carry no value in the re-OCR. A2 may log them as label-only rows. No figure is affected (BS R091, R297 carry 2,499.11).
- S-4. A1 anchors R117/R118 cite L945 (the PPE-and-intangibles header); the values sit on L947. No A4 figure uses them. Logged for A1.

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
  orphan_rows: []
  missing_from_ledger:
    - "L214 SA BS column audit status (30-Sep-26 Unaudited / 31-Mar-26 Audited), QUALIFIER"
    - "L349 and L974 SA CF column audit status (H1FY27 Unaudited / FY26 Audited), QUALIFIER"
    - "L588 CON BS column audit status, QUALIFIER"
    - "L725 CON CF column audit status, QUALIFIER"
    - "L339 SA notes page signing date 16-10-2026, DATE"
    - "L708 CON notes page signing date 16-10-2026, DATE"
    - "L1192 CON CF page signing date 16-10-2026, DATE"
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "PAT ties to the rupee because standalone books the Danya share; consolidated is the economic view; headline numbers tie (rev 234, 217, 617)", counter: "Elimination arithmetic proves two-way goods trade with the MD-co-owned firm in FY26: CON purchases below SA by Rs 6.16 Cr (parent bought at least that from Danya), CON revenue below SA by Rs 8.44 Cr (parent sold at least that into Danya), CON other creditors below SA by Rs 4.48 Cr at 31-Mar-26 (parent owed Danya, or a regrouping). Owners PAT equals SA PAT in all four periods, so no unrealised profit was ever eliminated, though Danya implied stock rose Rs 7.53 Cr in FY26 to Rs 17.02 Cr at 30-Sep-26 (19.5% of group inventory). Upper bound of unremoved margin about Rs 1.62 Cr pre-tax in FY26 [INFERENCE]; H1FY27 growth not inflated.", source_line: "L887 vs L1046; L883 vs L1042; L939 vs L1118; L194 vs L1074; L679; L953 vs L1131; L888 vs L1047", type: MISSING}
  - {claim: "Parent earns 13.3% post-tax on Danya capital, above after-tax cost of debt; minority subsidises the parent (rev 431, 647)", counter: "The yield rests on Danya profit earned partly on two-way trade with the parent at undisclosed prices and possibly sitting in Rs 17.02 Cr of stock run on near-nil cash (CON minus SA cash 2.90 lakh); the parent's exposure is the Rs 16.52 Cr capital account plus trade balances in both directions.", source_line: "L955 vs L1133; L953 vs L1131; L950; L939 vs L1118", type: MISSING}
findings_by_type:
  factual: []
  missing:
    - "M-1 (A2): seven fulltext units absent from structured and ledger: column audit-status headers L214, L349/L974, L588, L725; signing dates L339, L708, L1192. A2 count test for dates and qualifiers recounted A1 rows instead of grepping the fulltext."
    - "M-2 (A4): two-way intercompany goods trade not identified: CON purchases below SA by Rs 2.63 / 3.52 / 6.16 Cr in H1FY26 / H2FY26 / FY26 (L887 vs L1046); CON revenue below SA by Rs 8.44 Cr FY26; CON other creditors below SA by Rs 4.48 Cr at 31-Mar-26 (L939 vs L1118). rev 234 names two cost lines below standalone and omits purchases. Graft at rev 234, 431, flags, brief part 3; widen Q7."
    - "M-3 (A4): nil unrealised-profit elimination not tested: owners PAT equals SA PAT in all four periods (L194 vs L1074) while Danya implied stock is Rs 17.02 Cr (L953 vs L1131) after a Rs 7.53 Cr FY26 build (L888 vs L1047), cash near nil. Graft at rev 234, 617, 431, flags; add a management question."
  contradiction: []
  style:
    - "S-1: rev 422 '1.10 x 2 = 2.19' should read '109.73 lakh x 2 = 219.46 lakh'."
    - "S-2: rev 571 and 701 'Danya repaid Rs 2.96 Cr' should say term debt; Danya short-term borrowings rose Rs 1.14 Cr, net Rs 1.82 Cr (L1110-1114 vs L930-934)."
    - "S-3: Paid up Equity Share Capital label rows (L199/L909, L572/L1083) carry no value; A2 may log as label-only rows."
    - "S-4: A1 anchors R117/R118 cite L945; values sit on L947; logged for A1."
loop_back_to: "A2"
gap: "A2: add the seven fulltext units in coverage.missing_from_ledger as M rows (MISSING, low materiality). A3: dispose the new rows. A4: graft M-2 (two-way trade with Danya proven by CON purchases and revenue below SA in FY26 and CON other creditors below SA at 31-Mar-26) and M-3 (nil unrealised-profit elimination against Rs 17.02 Cr Danya stock and near-nil Danya cash) at rev 234, 431, 617, the flags and brief part 3, widen Q7, add one question; apply S-1 and S-2."
style_notes:
  - "S-1: rev 422 arithmetic text slip (1.10 x 2 = 2.19); figures stand."
  - "S-2: Q13 should say term debt and net Danya debt change Rs 1.82 Cr."
  - "S-3: blank Paid up Equity Share Capital label rows; no figure affected."
  - "S-4: A1 line anchor R117/R118 off by two lines; unused by A4."
analyst_note: "Arithmetic is clean: every derived cell in A4 recomputes within rounding, and the CON statements foot and tie. The gap is analytical. Elimination arithmetic proves two-way goods trade with Danya in FY26: CON purchases sit Rs 6.16 Cr below SA, so the parent bought at least that from the firm beyond the firm's own third-party buying; CON revenue sits Rs 8.44 Cr below SA, so the parent sold at least that into the firm; CON other creditors sit Rs 4.48 Cr below SA at 31-Mar-26. Owners PAT equals SA PAT to the rupee in all four periods, so no unrealised profit was ever eliminated, although Danya's implied stock rose Rs 7.53 Cr in FY26 to Rs 17.02 Cr (19.5% of group inventory) with near-nil cash. H1FY27 growth is not inflated by this (Danya stock +0.48 Cr); FY26 CON profit could carry up to about Rs 1.62 Cr pre-tax of unremoved margin. The coverage gap is mechanical and low materiality. A4's orphan disposition rests on the A3 register by reference; my spot-check of uncited ranges found nothing material left unaddressed."
```
