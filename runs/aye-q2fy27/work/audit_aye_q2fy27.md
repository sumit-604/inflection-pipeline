# A5 ADVERSARY / COMPLETENESS AUDIT: AYE FINANCE (AYE) Q2 FY27

Model: claude-opus-5-5. Run date 2026-10-23. Fresh context.
Inputs read: A4 review (work/review_aye_q2fy27.md), A1 fulltexts and structured files (extracted/), A2 ledgers (work/ledger_*).
Not read: the source PDFs, anything under inputs/, A3 notes, Notion, protocols.

Anchor key: `R:L###` / `P:L###` / `C:L###` = results / presentation / concall FULLTEXT line. `R:R###` / `P:R###` / `C:R###` = structured row. `REV L###` = line of the A4 review. `LED-R/P/C L###` = line of the A2 results / presentation / concall ledger.

---

## AUDIT 0: DELIVERABLE COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT | sector PRESENT | business model PRESENT | competition PRESENT | forward map PRESENT. Gate PASS.

| Part | Location | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | REV L1070-1083 | 13 numbered lines (band 10-20), each tagged FILED / MGMT / INFERENCE / prior Notion | PRESENT |
| 2. Sector intelligence | REV L1085-1093 | 8 bullets: segment, credit cycle, weather, rates, regulation, risk transfer, market size, not-disclosed list | PRESENT |
| 3. Business-model intelligence | REV L1095-1106 | Yield, cost, product mix, operating model, 5 drift items | PRESENT |
| 4. Competition intelligence | REV L1108-1113 | 3 competitor classes (P:R268), where Aye wins / loses, named peers labelled INFERENCE, risk to watch | PRESENT |
| 5. Forward map | REV L1115-1130 | Make-or-break line plus 11 dated catalysts, each with a bull and a bear fork | PRESENT |

---

## AUDIT 1: COVERAGE

Method. I re-ran the enumeration from the fulltext, the spine.
- Presentation: I took every digit-bearing line of P fulltext (1,020 lines). I diffed it against the set of `line N` anchors in the 913 structured rows, then opened each unmatched line.
- Results: I ran the same diff over the statement pages (R:L200-470) and the notes (R:L478-626). I counted notes, agenda items and signature timestamps by grep (`\d{1,2}:\d{2}` over the fulltext).
- Concall: I counted `[MODERATOR TURN]` tags. I spot-swept about 40 number-bearing management lines against the structured rows.
- Then I counted ID totals in each structured file and each ledger.

| Category | A2 count | Fresh count | Orphan rows (ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results: numbered notes | 12 | 12 (R:L479-626, notes 1-12) | 0 | PASS |
| Results: unnumbered notes | 4 | 4 (R:L342, 449, 525, 681) + the `#` footnote at R:L526, carried as R716 under Note 4 | 0 | PASS |
| Results: statement line items (pp4-7) | 328 | 328. Every digit-bearing statement line R:L214-253, 288-340 and 365-446 is anchored by a row | 0 | PASS |
| Results: agenda items | 2 | 2 (R:L43-46: results approved, "other agenda items") | 0 | PASS |
| Results: entities | 43 | 43 ENTITY rows | 0 | PASS |
| Results: zero-standing | 30 | 30 (31 grep hits less 1 in the A1 header) | 0 | PASS |
| **Results: signature timestamps (MISSING_FROM_STRUCTURED)** | **5 (M01-M05)** | **7 (R:L69, 184, 267, 465, 746, 980, 1438)** | n/a | **FAIL: R:L980 and R:L1438 are absent from both the structured file and the ledger** |
| Results: structured IDs vs ledger IDs | 755 / 755 | 755 / 755 | 0 | PASS |
| Presentation: slides | 44 | 44 ([page 1] to [page 44]) | 0 | PASS |
| **Presentation: number units** | **744** | **748: +83, +308, +6,865 at P:L667; +0 at P:L807** | n/a | **FAIL: ledger section 8 says "MISSING_FROM_STRUCTURED: none" (LED-P L999-1000)** |
| Presentation: structured IDs vs ledger IDs | 913 / 913 | 913 / 913 | 0 | PASS |
| Concall: questions | 10 | 10 (11 tags; C:L525 is a mid-question artefact) | 0 | PASS |
| Concall: speaker turns | 26 | 26 (10 Q + 10 A + T1-T4 + T25-T26) | 0 | PASS |
| Concall: management numbers | 191 | 191. The 40-line spot-sweep found no new gap (C:L278, 324, 332, 360-362, 378, 411, 413, 429-438, 446, 455-466, 527-546, 581, 591, 642-653, 719-734, 743, 748, 766-800, 827-836 all anchored) | 0 | PASS |
| Concall: MISSING_FROM_STRUCTURED | 7 | 7 confirmed at C:L72, 396, 500, 656, 721, 745, 762 | n/a | PASS (A1 gap correctly logged by A2) |
| Concall: structured IDs vs ledger IDs | 346 / 346 | 346 (ledger holds 362 row lines = 346 + 16 participant repeats) | 0 | PASS |

Unmatched presentation digit lines that I cleared (not data, or captured under a neighbouring line anchor): page footers, addresses and signature metadata (P:L26-67, 1014, 1017); index page ranges (P:L96-103); period axis labels; section numerals (P:L847-863); P:L154 "427" (captured as P:R080, anchored at L153); P:L666 "0.66%" (P:R525, anchored at L665); P:L716 "100%" (P:R565, anchored at L717); P:L745 "180 branches" (P:R575, L743); P:L295 "RBI 2014" (P:R182, L293); P:L442 director-bio year (immaterial).

### Coverage findings

**COV-1 [MISSING, loop A2].** P:L667 reads "Provision % 83 308 6,865". These are the 30-Jun-2026 gross loans: Stage 2 83, Stage 3 308, total 6,865. No structured row carries them. The grep for 6,865 / 308 / 83 in the presentation structured file returns only unrelated rows (R647, R800, R807). The P:L660-679 block is otherwise fully rowed (P:R510-R561). The ledger lists "none" missing (LED-P L999-1000). The values are load-bearing:
- they set Q1 GNPA 4.49% (308/6,865), REV L150 and L291;
- they set Stage 2 at 1.21% (REV L295);
- they set the Stage 3 move 308 to 299 behind the slippage proxy (REV L276).
A4 found the gap and read the fulltext directly (REV L21), so A4's numbers are right. The ledger is not.

**COV-2 [MISSING, loop A2].** P:L807 reads "0". It is the potential incremental capacity of the 33 branches of 10+ year vintage. It is the fourth addend of the existing-branch headroom: 2,301 + 1,547 + 560 + 0 = 4,408 (REV L415, L503). No structured row carries it, and the ledger does not list it. Low materiality, but a dropped number.

**COV-3 [MISSING, loop A2].** Two signature timestamps are absent from both the structured file and A2's M01-M05 list (LED-R L22-27):
- R:L980: auditor digital signature on the security-cover / covenant report, "Date: 2026.10.21 11:09:12+05'30'". This is the governance-relevant one.
- R:L1438: CS cover-letter signature, "Date:21-10-2026 11:39:14 +05:30".

**COV-4 [CONTRADICTION, loop A2].** LED-R L28 states: "No signature timestamp precedes the results approval (11:21)." R:L980 shows the auditor signed at 11:09:12. That is before the results approval (11:21, R:L45) and before the board meeting began (11:15, R:L43). The ledger contradicts the fulltext. A4 already flags and respects this (REV L20, A3-18, Q26, FLAG-PROCESS). The correction is to the ledger only.

**Orphan check (ledger rows absent from A4): 0.**
- A4's preamble (REV L25-35) marks all 755 + 5, all 913 and all 346 + 7 units reviewed, with zero orphans. That is the contract's explicit "reviewed" marker.
- Row-level spot-check: every numbered and unnumbered note is cited in 0D (REV L72-89). Every Q&A exchange E1-E10 is cited in 4A (REV L758-769). The opening turn is cited in Step 1. The closing turn is cited at C:L857-858 (REV L598).
- Eleven presentation slides carry no row-level cite and rest on the blanket marker alone: slides 1, 2, 4, 9, 10, 16, 29, 39, 41 (cited only through A3P-12), 42 and 43. I checked their content. It is cover, title, index, H1 restatements of cited Q2 rows, customer profile, collection tiers, the scrambled balance-sheet summary (A4 uses the filed balance sheet), shareholding, CSR and glossary. No finding is hidden there. Logged as STYLE (ST-4).

---

## AUDIT 2: ARITHMETIC

Every derived figure I found in A4's tables and text was recomputed from the extracted rows, about 150 values. **Mismatches above rounding: 0.** Representative lines below; "=" means exact to the printed decimals.

| Metric | A4 value | Recomputed | Source line(s) | Status |
|---|---|---|---|---|
| NII Q2 FY27 / Q1 FY27 / Q2 FY26 | 334.58 / 322.06 / 238.86 | 479.26-144.68 = 334.58; 452.67-130.61 = 322.06; 371.39-132.53 = 238.86 | R:R072-R074, R:R114-R116 | PASS |
| NII FY26 / H1 FY26 / H1 FY27 | 1,015.06 / 471.81 / 656.64 | 1,549.13-534.07; 730.67-258.86; 931.93-275.29 = same | R:R075-R077, R:R117-R119 | PASS |
| Other/fee income net (6 columns) | 55.18 / 36.99 / 47.86 / 229.04 / 98.44 / 84.85 | fees + DA + FV gain + other - FV loss = same, all six | R:R078-R107, R:R120-R125 | PASS |
| Q1 FY27 DA gain nil | 0.00 (cross-foot) | 452.67 + 19.56 + 5.14 = 477.37 = total revenue | R:R097; R:R089 blank | PASS |
| Opex (6 columns) | 166.13 / 180.49 / 184.74 / 661.07 / 314.74 / 365.23 | employee + D&A + other = same, all six | R:R132-R149 | PASS |
| PPOP (6 columns) | 127.91 / 178.56 / 197.70 / 583.03 / 255.51 / 376.26 | NII + other net - opex = same | derived | PASS |
| PBT tie-out (6 columns) | PPOP - impairment = PBT | 197.70-81.90 = 115.80; 178.56-81.41 = 97.15; 127.91-86.22 = 41.69; 583.03-335.73 = 247.30; 376.26-163.31 = 212.95; 255.51-172.93 = 82.58 | R:R126-R131, R:R156-R161 | PASS |
| Total expenses cross-check Q2 | n/a | 144.68 + 81.90 + 135.74 + 6.43 + 42.57 = 411.32 | R:R150 | PASS |
| Cost-to-income Q2 / Q1 / Q2 FY26 | 48.31% / 50.27% / 56.50% | 184.74/382.44 = 48.31%; 180.49/359.05 = 50.27%; 166.13/294.04 = 56.50% | P:R103-R105 (48.3 / 50.3 / 56.5) | PASS |
| Credit cost on avg AUM Q1 / Q2 | 4.53% / 4.39% | 325.64/7,184 = 4.533%; 327.60/7,460.5 = 4.391% | P:R209 (7,044), P:R073, P:R074 | PASS |
| GNPA table basis Sep-25 / Jun-26 | 4.84% / 4.49% | 272/5,615 = 4.844%; 308/6,865 = 4.487% | P:L672, **P:L667 (no structured row, COV-1)** | PASS |
| Stage 2 share Jun / Sep; change | 1.21% / 1.26%; +8.4% | 83/6,865 = 1.209%; 90/7,119 = 1.264%; 7/83 = 8.43% | P:L667, P:R514, P:R516 | PASS |
| Liquidity share of total assets | 15.3% | (851.21 + 490.45)/8,773.51 = 15.29% | R:R014, R:R016, R:R044 | PASS |
| Trust PAT share Q2 / H1 | 0.14% / 0.29% | 0.12/86.72 = 0.138%; 0.47/161.22 = 0.292% | R:R009, R:R010 | PASS |
| EPS-implied share count Q2 / H1; paid-up | 24.71 / 24.69 / 24.51 cr | 86.72/3.51 = 24.707; 161.22/6.53 = 24.689; 49.02/2 = 24.51 | R:R222, R:R225, R:R064 | PASS |
| YoY: NII, PPOP, finance cost, interest income | +40.1%, +54.6%, +9.2%, +29.0% | 1.4007, 1.5456, 1.0917, 1.2904 | derived | PASS |
| YoY: impairment, gross book, other net, D&A | -5.0%, +26.8%, -13.3%, +3.0% | 0.9499, 7,119/5,615 = 1.2679, 0.8673, 1.0304 | P:L672, P:R516 | PASS |
| Core PBT Q2 FY26 / Q2 FY27 / Q1 FY27; YoY | 14.95 / 101.18 / 92.01; +576.8% | 41.69-16.28-29.12+18.66; 115.80-10.12-4.50; 97.15-5.14; 101.18/14.95 = 6.768 | derived | PASS |
| Reported PBT YoY / PAT YoY / dil. EPS YoY | +177.8% / +151.1% / +96.6% | 2.7776 / 2.5114 / 1.9661 | R:R180-R182, R:R228-R230 | PASS |
| PPOP / net income YoY; QoQ | +820 bps; +200 bps | 43.50% to 51.69% = +819 bps; 49.73% to 51.69% = +196 bps | derived | PASS (rounding) |
| Tax rates; rate effect | 17.17% / 25.11%; 9.19 | 7.16/41.69 = 17.17%; 29.08/115.80 = 25.11%; 115.80 x 7.94% = 9.19 | R:R174, R:R176 | PASS |
| Ex-DA/FV other income YoY | 33.24 vs 28.44, +16.9% | 20.51+12.73; 18.10+10.34; 1.1688 | R:R078, R:R080, R:R102, R:R104 | PASS |
| Q1 FY26 derived: NII, PPOP%, core PBT | 232.95; 46.2%; 21.39 | 471.81-238.86; 127.60/276.21; 40.89-13.04-18.55+12.09 | H1 FY26 less Q2 FY26 rows | PASS |
| H2 FY26 derived: NII, PPOP%, core PBT, PAT | 543.25; 48.6%; 103.97; 128.51 | 1,015.06-471.81; 327.52/673.85; 164.72-38.65-58.12+36.02; 193.63-65.12 | FY26 less H1 FY26 rows | PASS |
| NII QoQ run-rates | +2.5%, +13.7%, +18.6%, +3.9% | 238.86/232.95; 271.63/238.86; 322.06/271.63; 334.58/322.06 | derived | PASS |
| 4A YoY bridge: components and shares | +95.72, +2.41, +2.39, -6.16, -24.62, +18.66, -18.61, +4.32 = +74.11 | sum = 74.11; shares 129.2 / 3.3 / 3.2 / -8.3 / -33.2 / 25.2 / -25.1 / 5.8 | derived | PASS |
| 4A recurring / non-recurring | +86.23 / -12.12; 116% | 95.72+2.41+2.39-18.61+4.32; -6.16-24.62+18.66; 86.23/74.11 = 116.4% | derived | PASS (see Claim 1 counter on classification) |
| 4B QoQ bridge | +12.52, +10.12, +0.95, -0.64, +0.44, -4.25, -0.49 = +18.65 | sum = 18.65; DA share 54.3% | derived | PASS |
| DA after tax; share of PAT rise | 7.57; 62.0% | 10.12 x 0.7483 = 7.573; 7.57/12.22 = 61.9% | derived | PASS |
| **H1 write-off identity** | 155.56 + 8.30 - 0.55 = 163.31 | Exact. The cash-flow block is interleaved (R:L365-396). I re-footed it: R:R248 "0-64)" must read (9.64), which equals the P&L FV gain R:R093. With that, adjustments foot to 637.51 = R:R274. H1 FY26 foots to 468.85 = R:R275, with 146.20 + 2.75 + 23.98 = 172.93 = R:R130 | R:R250, R:R256, R:R258, R:R129 | PASS (identity independently confirmed) |
| Q1 / Q2 ECL change; write-offs + settlements | +12.45 / -13.00; 68.96 / 94.90 | 287-274.55; 274-287; 81.41-12.45; 81.90+13.00; sum 163.86 = filed | P:L668, P:R520 | PASS (INFERENCE as labelled) |
| Cover restore need; post-tax; share of PAT | 296.9; 22.9; 17.1; 19.7% | 7,119 x 4.17%; -274; x 0.7483; /86.72 | P:R539, P:R516 | PASS |
| DA + ECL fall vs PBT rise; after tax | 23.12 > 18.65; 17.30 | 10.12+13.00; x 0.7483 = 17.30 | derived | PASS |
| H1 FY26 write-offs + settlements; YoY | 148.95; +10.0% | 146.20+2.75; 163.86/148.95 = 1.1001 | R:R257, R:R259 | PASS |
| Slippage proxy; annualised; % avg AUM; % avg gross | 86; 343.6; 4.6%; 4.9% | 94.90-9 = 85.9; x4; /7,460.5 = 4.61%; /6,992 = 4.91% | P:L667, P:R515 | PASS (INFERENCE) |
| DA-sold book ECL effect | ~0.26 | 39.95 x 0.66% = 0.264 | R:R355, P:R525 | PASS |
| PAT ex-DA; implied ATA; RoA ex-DA | 79.15; 8,586; 3.69% | 86.72-7.57; 346.88/4.04% = 8,586; 316.6/8,586 = 3.687% | P:R846 | PASS |
| Liquidity, borrowings, net loans H1 growth | +32.7%, +16.8%, +9.3% | 1,341.66/1,011.07; 5,858.32/5,017.63; 6,849.85/6,266.44 | R:R014-R017, R:R020-R021, R:R046-R049 | PASS |
| State Bucket 1 CE, Q1 vs Q2 averages | UP 51.57/49.53; RJ 59.93/55.57; Rest 56.90/55.77; BR 37.87/38.33 | (52.1+50.9+51.7)/3 etc. Same to 2 dp | P:L640 (P:R461-R484) | PASS |
| Disbursement YoY Q1 / Q2 (relabelled) | +21.8% / +10.0% | 1,219/1,001 (1,001 = 2,276-1,275) = 1.2178; 1,403/1,275 = 1.1004 | P:R077/R076 (swapped labels), P:R078, P:R132 | PASS. Relabel confirmed: 1,219 + 1,403 = 2,622 (P:L121), and 1,403/1,219 = +15% QoQ (P:L120) |
| Finance cost on ATA Q1 to Q2 | 6.46% to 6.74%, +28 bps | P:L917 right block | P:R787, P:R788, P:R797 | PASS |
| Credit cost on ATA if ECL held flat | 4.43% | 94.90 x 4 / (327.6/3.82% = 8,576) = 4.426% | derived | PASS |
| PAT run-rates | 322.44; 307.3; 346.88; 277.7; TTM 289.73 | 161.22 x 2; (161.22-7.57) x 2; 86.72 x 4; (86.72-7.57-9.73) x 4; 128.51+161.22 | derived | PASS |
| H1 diluted EPS YoY | +94.3% | 6.49/3.34 = 1.9431 | R:R231, R:R232 | PASS |
| DA % of total income Q2 / H1 | 1.92% / 1.00% | 10.12/527.12; 10.12/1,016.78 = 0.995% | R:R108, R:R111 | PASS |
| AUM per active loan | ~1.10 lakh | 7,597/6,92,676 = 1.097; 7,324/6,69,261 = 1.094 (6,92,676 = 43,530 + 10,179 + 6,38,967, P:L414-420) | P:R289-R291 | PASS |
| Co-lending NPL share | 19.9% | 10.61/53.31 = 19.90% (42.70 + 10.61 = 53.31) | R:L576-584 | PASS |
| Concall claim quantification | 31/43 = 72.1%; forward 6/13 = 46% | recounted from REV L620-662 | derived | PASS |
| Specificity; hedge count | 30/56 = 0.54; 19 | 30 listed rows counted; hedges re-found at C:L86, 295, 296, 313, 381, 498, 527, 532, 661, 150, 175, 209, 418, 230, 530, 227, 265, 255-256, 528 | C:R240-R295 | PASS |
| Credibility ratio and sensitivities | 70.0%; 87.5%; 60.0% | 3.5/(15-10); 3.5/4; 3.0/5 | REV L704-734 | PASS |
| 2L H2 implied credit cost / opex / NIM | 3.05 / 8.17 / 13.13 | 3.5x2-3.95; 8.5x2-8.83; 14.5x2-15.87 | P:R645, P:R647, P:R649 | PASS |
| 2L H2 pre-tax / post-tax RoA | 4.11 / 3.07 | 13.13+2.2-8.17-3.05 = 4.11; x 0.7483 = 3.0755 | P:R823 | PASS (rounding; see ST-5) |
| Q13 H2 NIM band | 12.6-13.6% | 14.25x2-15.87 = 12.63; 14.75x2-15.87 = 13.63 | P:R653 | PASS |
| Q17 AUM needed; headroom | 8,300-10,300; 4,408 | 7,597 x (1.28^3-1) = 8,335; x (1.33^3-1) = 10,276; 2,301+1,547+560+0 | P:L799-807 | PASS |
| AUM per branch | 13.30 | 7,597/571 | P:R074, P:R172 | PASS |
| MH+KA+MP map shares | 23.18% | 7.98+7.79+7.41 | P:R238, P:R240, P:R233 | PASS |
| Pre-IPO >5% holders | ~50% | 12.6+10.0+7.7+7.4+7.2+5.5 = 50.4 | P:L945-952 | PASS |
| M4 breached ISIN amount; M7 NCD balance | 55.22; 70 | 25.10+30.12; 220-150 | R:R528, R:R532, R:R563, R:R564 | PASS |
| Exchange 1 June ex-overlay ECL; loan growth | 275; 254 | 4.01% x 6,865 = 275.3; 7,119-6,865 | P:L667, P:R516 | PASS |
| RoA build (brief section 3) | 4.04% | (15.59 + 2.23 - 8.61 - 3.82) x (1-0.2511) = 4.04 | P:R810, P:R823, P:R646, P:R389 | PASS |
| NIM QoQ (Step 7A) | -35 bps | 15.59-15.94 = -35 on rounded; deck prints -34 bps on unrounded | P:R792, P:R793 | PASS (rounding; see ST-1) |

Evidence boundary (record only, not a finding). A4 carries a few inputs from outside A5's evidence set: prior-deck AUM growth 28.0% and CRAR 42.4% (via A3P-13 / A3P F11), the filed Q1 PCR 63.80% (A3-11), and Notion values ([N ...]). A5 cannot re-derive these inputs. The arithmetic A4 runs on them checks (for example 41.01 - 42.4 = -139 bps; 62.42 - 63.80 = -138 bps). A4 labels the provenance of each.

---

## AUDIT 3: ADVERSARIAL READ

A4's review already leans bear on earnings quality. The three most positive claims it still makes are below. For each I built the strongest counter from the extracted text alone.

### Claim 1. "YoY core growth is real and larger than reported" (REV L180) and "The YoY PAT increase is 116% recurring" (REV L237)

Strongest bear counter:
1. **Trough base.** Q2 FY26 core PBT of 14.95 is the lowest print in A4's own Step 3 series. Q1 FY26 was 21.39 and the H2 FY26 per-quarter average was 51.99 (REV L203-205). Q2 FY26 ran at 5.00% credit cost (P:R387), in the period the filing calls "industry wide stress" (R:R749). So +576.8% is a recovery-from-trough multiple, not a run-rate.
2. **Funding mix.** Finance cost on ATA fell 95 bps YoY, 7.69% to 6.74% (P:R798, P:R797). Blended CoB fell only 41 bps, 11.04% to 10.63% (P:L509). The residual, about 67 bps of ATA, is a lower debt share of assets after the Feb-26 IPO (leverage 4.03x to 3.24x, P:R853, P:R852). That is about Rs14 cr a quarter, roughly 19% of the 74.11 YoY PBT rise [INFERENCE: 10.63% x (7.69/11.04 - 6.74/10.63) x 8,576 / 4 = 14.2]. Management plans to re-lever to 4-4.5x (C:L272-274). That unwinds this part of NIM, and the FY27 NIM guide of 14.25-14.75% (P:R653) already assumes it.
3. **ECL draw counted as recurring.** The 4A "recurring" provision line (+4.32) includes the Q2 ECL stock draw of about 13 that A4 itself isolates in 4C. Moving it out leaves about 73.2 recurring, about 99% of the PBT change. The label holds, but the 116% overstates it.

Survives: **YES**. Each leg rests on extracted lines.

Already in A4, only in pieces: the QoQ reversal (REV L188), the IPO step in NII (REV L210), leverage 4.03x to 3.24x (REV L175), and H2 NIM about 13.13% (REV L694). Missing at the claim itself: the trough-base qualifier, the funding-mix share of the YoY gain, and the 4A/4C link on the ECL draw.

**Graft required (MISSING, A4).** Add under the Step 2 "Core PBT" row and as a 4A footnote:
"Bear counter (A5): the YoY core multiple runs off the FY26 stress trough (Q2 FY26 core 14.95, credit cost 5.00%, P:R387). About Rs14 cr a quarter of the YoY gain is the post-IPO funding mix: finance cost on ATA -95 bps (P:R798, P:R797) against CoB -41 bps (P:L509). Management plans to re-lever to 4-4.5x (C:L272-274), which unwinds it. The 4A recurring pool includes the ~13 Q2 ECL draw (4C); without it, recurring is ~73.2. The YoY recovery is real; its size is base- and capital-driven. The repeatable signal is QoQ core PBT +10.0%."

### Claim 2. Asset quality GREEN: "GNPA 4.20% ... GREEN on the trigger" (REV L291); "Sound 1.00x on the headline" (REV L317); "The classic MFI pre-crisis pattern is absent" (REV L320); over-lending tripwire GREEN (REV L389)

Strongest bear counter:
1. **The QoQ GNPA fall is write-off driven.** Add each quarter's write-offs and settlements back to its closing Stage 3 [INFERENCE on A4's own 4C split]:
   - Q1: (308 + 68.96) / 6,865 = 5.49% (P:L667).
   - Q2: (299 + 94.90) / 7,119 = 5.53% (P:R515, P:R516).
   On this basis Q2 is flat to slightly worse than Q1. The whole -29 bps headline improvement comes from the roughly 26 cr step-up in Q2 write-offs.
2. **Mix shift to unseasoned borrowers.** New-customer disbursement rose 23% YoY while repeat fell 16% (C:L98-102). Management itself says repeat loans "perform very well on the credit cost" (C:L259-260). 95% of the book was written after June 2024 (P:R433), and 32% of households carry MFI loans (C:L459). A4 reads the falling repeat share (52.0% to 51.4%, P:R592, P:R593) as GREEN for over-lending. The same fact means the incremental book is less seasoned and riskier.

Bull offset I checked: on an H1 basis the write-off-adjusted ratio did improve YoY, (272 + 148.95)/5,615 = 7.50% to (299 + 163.86)/7,119 = 6.50%. The YoY improvement is real; the QoQ improvement is write-off driven.

Survives: **YES**.
- Leg 1 is already in A4 in substance: 4C write-offs about 38% higher QoQ (REV L270), Stage 3 308 to 299 with about 95 written off (REV L276), brief line 5 (REV L1075), covenant reason "higher delinquencies" (REV L99). No graft needed.
- Leg 2 is absent. A4 treats new-borrower growth only as growth mix (REV L816, L1101) and a falling repeat share only as GREEN (REV L389).

**Graft required (MISSING, A4).** Add to Step 5L lender question 4 and watchlist item 8:
"Second reading (A5): the falling repeat share that clears tripwire 8 also means incremental lending tilts to first-time borrowers. New-customer disbursement +23% YoY, repeat -16% (C:L98-102). Management says repeat loans perform better on credit cost (C:L259-260). 95% of the book is post-June 2024 (P:R433); 32% household MFI overlap (C:L459). Separating observation: Bucket 1 CE and PAR X for the new-to-Aye cohort against the repeat cohort (fold into Q33)."

### Claim 3. Management credibility: "Credibility Ratio = 70.0% → Grade B → Role 1 track-record input 'Good'" (REV L730); archetype "COMMITTED & CREDIBLE" (REV L887); opex "DELIVERED (early)" (REV L711)

Strongest bear counter. Opex delivery is helped by the denominator. This is the same mechanism A4 calls out for credit cost in A4-02 (REV L159), but A4 does not apply it to opex.
- Rupee opex rose 2.4% QoQ, 180.49 to 184.74 (R:R132-R146).
- Implied ATA rose about 6.2%, 8,085 to 8,583 [from opex on ATA 8.93% to 8.61%, P:L920, P:R646].
- On average AUM the opex ratio moved 10.05% to 9.91% [180.49 x 4 / 7,184; 184.74 x 4 / 7,460.5]. That is -14 bps, against -32 bps on ATA.
- So more than half the reported improvement is idle liquidity in the denominator.

The commitment was set on the ATA basis (P:R654), so DELIVERED is correct on the guided metric. But the 70% / Grade B input to Role 1 rests partly on that item. Scoring opex PARTIALLY DELIVERED gives 3.0 / 5 = 60%, A4's own strict-reading boundary (REV L734).

Survives: **YES**. It is not in A4. A4's credibility sensitivity (REV L732-735) varies only the slippage and narrowing scores.

**Graft required (MISSING, A4).** Add to the 3A opex row and to the 3B sensitivity list:
"Qualifier (A5): opex delivery is denominator-assisted, as A4-02 shows for credit cost. Rupee opex +2.4% QoQ (R:R132-R146); opex on average AUM 10.05% to 9.91% (-14 bps) against -32 bps on ATA (P:L920, P:R646). DELIVERED stands on the guided ATA basis. Scored PARTIAL, the ratio is 60% (3.0/5)."

### Additional probe (not counted): Rs270 cr PAT trigger GREEN (REV L385)

Bear reading: on A4's own quality-adjusted Q2 run-rate of 277.7 (REV L426), the headroom over Rs270 cr looks like about 3%.

The counter fails on the extract. H1 FY27 PAT of 161.22 is already booked (R:R183). FY27 breaches only if H2 PAT falls below 108.78, about 54.4 a quarter. The quality-adjusted Q2 is 69.42 a quarter [86.72 - 7.57 - 9.73]. A breach needs a further fall of about 22% per quarter. GREEN stands.

### MANDATORY ACQUISITION-ECONOMICS PROBE: NOT TRIGGERED

The extracts describe no acquisition, purchase or stake buy.
- Note 5(b)(i): "The Company has not acquired any loans through assignment during the half year" (R:L546).
- Note 5(c)(iii): "has not acquired any stressed loan" (R:L569).
- The deck's "asset purchases" (P:L266) is the purpose of customer loans.
- Cash-flow "Purchase of investments" (4,987.92, R:R300) is treasury churn, matched by sales of 4,932.74 (R:R302).
- The rise in Arcil security receipts (A4 Q29) comes from earlier loan sales to an ARC, not a purchase.
- The gold-loan pilot is an organic branch build (C:L597-599).
There is no consideration and no target, so no multiple can be stated.

---

## VERDICT

**VERDICT: INCOMPLETE.** Loop back to **A2**. The A4 grafts ride the same loop.
- A2, MISSING: add MISSING_FROM_STRUCTURED entries for P:L667 (83 | 308 | 6,865, 30-Jun gross loans Stage 2, Stage 3, total) and P:L807 (0) to the presentation ledger. Add R:L980 (auditor signature 11:09:12) and R:L1438 (CS signature 11:39:14) to the results ledger M-list. A1 rows are optional, since A4 already reads the fulltext.
- A2, CONTRADICTION: correct LED-R L28. One timestamp, R:L980 at 11:09:12, precedes both the 11:15 board start and the 11:21 approval.
- A4, MISSING: graft the three surviving bear counters above (Claim 1 into Step 2 / 4A; Claim 2 into 5L Q4 / watchlist 8; Claim 3 into 3A / 3B).

No FACTUAL finding. No arithmetic mismatch. A4's numbers, protocol verdict (PROCEED WITH FLAGS) and position (HOLD 4%) do not depend on any of these items. The grafts are qualifiers, not reversals.

## STYLE NOTES (logged, no loop)

- **ST-1.** Step 7A (REV L904) "-35 bps QoQ (P:R792)". The deck prints -34 bps on unrounded figures (P:R793). Cite the printed value.
- **ST-2.** Step 1L heading (REV L118) says A4's net other income "matches" the deck for four columns. It omits Q2 FY26, where the deck prints 56 (P:L876) against 55.18 on the filed basis; the deck figure is reclassified (P:L887). State the 1-crore gap.
- **ST-3.** Brief line 11 (REV L1081) "fails on two of its four legs". Step 8A (REV L458) shows 1 pass, 1 fail, 1 not met, 1 unverifiable. Say "only one of four legs passes".
- **ST-4.** The preamble's blanket "all reviewed" marker carries 11 slides with no row-level cite: 1, 2, 4, 9, 10, 16, 29, 39, 41, 42 and 43. The contract is met. A one-line "reviewed, no finding" list would make it traceable.
- **ST-5.** Step 2L H2 post-tax RoA "3.07%" (REV L694) computes to 3.08% (4.11 x 0.7483 = 3.0755). Within rounding.

```yaml
stage: A5-adversary
company: "AYE"
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
    - {doc: "presentation", fulltext_line: 667, values: "83 | 308 | 6,865 (30-Jun-2026 gross loans Stage 2, Stage 3, total)", structured_row: "none", ledger_says: "MISSING_FROM_STRUCTURED: none"}
    - {doc: "presentation", fulltext_line: 807, values: "0 (potential capacity, 10+ yr vintage; 4th addend of 4,408 headroom)", structured_row: "none", ledger_says: "MISSING_FROM_STRUCTURED: none"}
    - {doc: "results", fulltext_line: 980, values: "auditor security-cover report signature 21-10-2026 11:09:12 (before 11:15 board start, R:L43)", structured_row: "none", ledger_says: "absent from M01-M05"}
    - {doc: "results", fulltext_line: 1438, values: "CS cover-letter signature 21-10-2026 11:39:14", structured_row: "none", ledger_says: "absent from M01-M05"}
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "YoY core PBT +576.8% is real and larger than reported; YoY PAT rise 116% recurring (REV L180, L237)", counter: "Base is the FY26 stress trough (Q2 FY26 core 14.95, credit cost 5.00%); ~Rs14 cr/qtr of the YoY gain is post-IPO funding mix (fin cost on ATA -95 bps vs CoB -41 bps), unwound by planned re-levering to 4-4.5x; the 4A recurring pool includes the ~13 Q2 ECL draw", source_line: "P:R387; P:R797; P:R798; P:L509; P:R852; P:R853; C:L272-274; P:R653; R:R126-R128", type: "MISSING"}
  - {claim: "Asset quality GREEN; over-lending tripwire GREEN; MFI pre-crisis pattern absent (REV L291, L317, L320, L389)", counter: "Falling repeat share also means incremental book tilts to first-time borrowers: new-customer disbursement +23% YoY, repeat -16%; mgmt says repeat loans perform better on credit cost; 95% of book post-Jun-2024; 32% household MFI overlap", source_line: "C:L98-102; C:L259-260; P:R433; C:L459; P:R592; P:R593", type: "MISSING"}
  - {claim: "Credibility 70% Grade B, Role 1 input Good; opex DELIVERED early (REV L711, L730, L887)", counter: "Opex delivery is denominator-assisted like A4-02: rupee opex +2.4% QoQ; opex on avg AUM 10.05% to 9.91% (-14 bps) vs -32 bps on ATA; scored PARTIAL the ratio is 60%", source_line: "R:R132-R146; P:L920; P:R646; P:R073; P:R074", type: "MISSING"}
findings_by_type:
  factual: []
  missing:
    - "COV-1 (A2): P:L667 values 83, 308, 6,865 (30-Jun gross loans S2, S3, total) absent from presentation structured file and ledger (LED-P L999-1000 says none)"
    - "COV-2 (A2): P:L807 value 0 (10+ yr vintage capacity) absent from structured file and ledger"
    - "COV-3 (A2): R:L980 auditor signature 11:09:12 and R:L1438 CS signature 11:39:14 absent from structured file and from ledger M01-M05"
    - "ADV-1 (A4): graft Claim 1 bear counter (trough base, IPO funding mix ~Rs14 cr/qtr, ECL draw inside recurring) at Step 2 Core PBT row and 4A"
    - "ADV-2 (A4): graft Claim 2 second reading (new-vs-repeat credit mix) at 5L lender Q4 and watchlist 8; fold cohort ask into Q33"
    - "ADV-3 (A4): graft Claim 3 qualifier (opex delivery denominator-assisted; ratio 60% if scored PARTIAL) at 3A opex row and 3B sensitivity"
  contradiction:
    - "COV-4 (A2): LED-R L28 says no signature timestamp precedes the 11:21 approval; R:L980 shows auditor signature 11:09:12, before 11:15 board start (R:L43). A4 already respects this (REV L20)"
  style:
    - "ST-1: Step 7A NIM -35 bps QoQ; deck prints -34 bps (P:R793)"
    - "ST-2: Step 1L deck fee-income match omits Q2 FY26 (deck 56 vs 55.18, reclassified P:L887)"
    - "ST-3: Brief line 11 'fails on two of four legs'; say only one of four passes (REV L458)"
    - "ST-4: 11 slides (1,2,4,9,10,16,29,39,41,42,43) rest on the blanket reviewed marker; add a reviewed-no-finding list"
    - "ST-5: Step 2L H2 post-tax RoA 3.07% computes to 3.08%"
loop_back_to: "A2"
gap: "A2 MISSING: add MISSING_FROM_STRUCTURED rows for presentation fulltext L667 (83 | 308 | 6,865) and L807 (0), and results fulltext L980 (auditor signature 11:09:12) and L1438 (CS signature 11:39:14). A2 CONTRADICTION: correct results ledger line 28 (R:L980 precedes the 11:15 board start). A4 MISSING on the same loop: graft the three surviving bear counters in audit section 3 (Step 2/4A; 5L Q4/watchlist 8; 3A/3B)."
style_notes:
  - "ST-1: cite printed -34 bps NIM QoQ (P:R793), not -35"
  - "ST-2: state deck Q2 FY26 fee & other income 56 vs filed-basis 55.18 (reclassified)"
  - "ST-3: brief line 11 should read 'only one of four add-gate legs passes'"
  - "ST-4: add per-slide reviewed-no-finding list for slides 1,2,4,9,10,16,29,39,41,42,43"
  - "ST-5: H2 post-tax RoA 3.08% not 3.07% (rounding)"
analyst_note: "A4's arithmetic holds: about 150 derived values recomputed, none off beyond rounding. The H1 write-off identity is sound. R:R248 '0-64)' is (9.64); with it the operating cash flow foots to 637.51, and H1 FY26 to 468.85, which validates the (0.55) ECL line. The failure sits at the spine. A1 dropped presentation L667, the 30-Jun Stage 2, Stage 3 and total gross loans behind Q1 GNPA 4.49% and the slippage proxy, plus L807. A1 also dropped results L980 and L1438. The A2 ledgers record none of these, and the results ledger states the reverse of L980. A4 caught all of it and read the fulltext, so the A2 fix is ledger-only and no A4 figure moves. Three bear counters survive and are absent from A4: the YoY core multiple is base- and IPO-funded, the repeat-to-new mix is a credit risk, and opex delivery is denominator-assisted. Each is a qualifier, not a reversal. PROCEED WITH FLAGS and HOLD should stand. The A2 to A4 re-run can be incremental."
```

---

## RE-AUDIT AFTER LOOP 1

Re-audit date 2026-10-23. Correction loop 1 of 1.
Re-read: the corrected A2 ledgers (ledger_results_aye_q2fy27.md, ledger_presentation_aye_q2fy27.md), their blocks (blocks/a2-results.yaml, blocks/a2-presentation.yaml), and the rewritten A4 review.
The A1 fulltexts did not change, so my loop-0 fulltext findings stay the reference.
Line references below (`REV L###`, `LED-R L###`, `LED-P L###`) point to the CORRECTED files. The loop-0 section above keeps its original line references.

### R1. Closure of loop-0 findings

| ID | Type | Loop-0 gap | Evidence after loop 1 | Status |
|---|---|---|---|---|
| COV-1 | MISSING | P:L667 (83 / 308 / 6,865) not in ledger | LED-P L1003 adds M01, line 667, labelled 30-Jun Stage 2, Stage 3, total. LED-P L3 logs it. blocks/a2-presentation.yaml L20 matches | CLOSED |
| COV-2 | MISSING | P:L807 ("0") not in ledger | LED-P L1004 adds M02, line 807, value 0, 10+ year vintage capacity | CLOSED (wording: R1-S3) |
| COV-3 | MISSING | R:L980 and R:L1438 not in ledger | LED-R L30 adds M06 (line 980, 11:09:12, flagged SIGNATURE_BEFORE_MEETING). LED-R L31 adds M07 (line 1438, 11:39:14). blocks/a2-results.yaml L23 lists M01-M07 | CLOSED |
| COV-4 | CONTRADICTION | LED-R L28 said no signature precedes the approval | LED-R L32 now reads: M06 at 11:09:12 is 6 min before the 11:15 start and 12 min before the 11:21 approval; the others fall at or after 11:21. That matches R:L43, R:L45 and R:L980 | CLOSED |
| ADV-1 | MISSING | Claim 1 bear counter | REV L184 (row verdict), L192, L197-201 (counter block), L249 (4A footnote), L291 (4D), L441 (6.5), L449 (Pillar 1), L982 (8D), L1016 (Section C), L1041 and L1254 (FLAG-BASE-EFFECT), L1117 (brief) | CLOSED. Anchors and figures match the loop-0 graft text |
| ADV-2 | MISSING | Claim 2 second reading | REV L333 (5L Q4), L402 (watchlist 8 now GREEN / AMBER), L406 (tally restated), L450 (Pillar 2L), L533 and L1207 (Q33 cohort ask), L542 (mapping), L832 (5A), L965 (8B), L1018 (Section C), L1042 and L1255 (FLAG-BORROWER-MIX), L1099 and L1122 (brief) | CLOSED |
| ADV-3 | MISSING | Claim 3 qualifier | REV L725 (3A row), L744-751 (3B sensitivity), L756 (3C), L904 (6E), L916 (7A), L991 (8E), L1004-1005 (concall verdict), L1040 and L1253 (flag), L1049 (A4-02), L1118 (brief) | CLOSED |
| ST-1 | STYLE | NIM QoQ -35 bps | REV L921 cites -34 bps as printed (P:R793) | APPLIED |
| ST-2 | STYLE | Deck Q2 FY26 fee income 56 not stated | REV L122 states 56 (P:L876) vs 55.18, reclassified (P:L887) | APPLIED |
| ST-3 | STYLE | Brief line 11 wording | REV L1102 "Only one of the four add-gate legs passes"; YAML flag REV L1242 | APPLIED |
| ST-4 | STYLE | No per-slide reviewed list | REV L39 lists the 11 slides plus the 6 dividers | APPLIED |
| ST-5 | STYLE | H2 post-tax RoA 3.07% | REV L708 now 3.08% [4.11 x 0.7483 = 3.0755] | APPLIED |

A2 structured-ID totals are unchanged (755 / 913). A2 logged the drops as MISSING_FROM_STRUCTURED and did not add A1 rows, which the loop-0 audit marked optional.

### R2. Fresh spot check of the A4 rewrite

DELIVERABLE-COMPLETENESS (re-check): narrative PRESENT (REV L1091-1104) | sector PRESENT (REV L1106-1114) | business model PRESENT (REV L1116-1127) | competition PRESENT (REV L1129-1134) | forward map PRESENT (REV L1136-1151, 11 dated rows, each with a bull and a bear fork). Gate PASS.

ARITHMETIC: I recomputed every figure the rewrite added or changed. **Mismatches above rounding: 0.**

| Metric | A4 value | Recomputed | Source line(s) | Status |
|---|---|---|---|---|
| Funding-mix carry; share of YoY PBT rise | ~14.2; ~19% | 10.63% x (7.69/11.04 - 6.74/10.63) x 8,576 / 4 = 14.2; 14.2 / 74.11 = 19.2% | P:R797, P:R798, P:L509 | PASS |
| Recurring pool ex ECL draw | ~73.2; ~99% | 86.23 - 13.0 = 73.23; 73.23 / 74.11 = 98.8% | REV L247, L249 | PASS |
| Opex on average AUM Q1 / Q2 | 10.05% / 9.91% | 721.96 / 7,184 = 10.05%; 738.96 / 7,460.5 = 9.905% | R:R132-R146; P:R073, P:R074 | PASS |
| Rupee opex QoQ | +2.4% | 184.74 / 180.49 = 1.0235 | R:R132-R146 | PASS |
| Credibility sensitivities | 87.5% A; 60% B (opex PARTIAL); 60% then C (narrowing DROPPED, 2 DROPPEDs); 50% then C, then D (both) | 3.5/4; 3.0/5; 3.0/5; 2.5/5. The grade mapping is monotonic and matches the loop-0 text (60% maps to B before any DROPPED downgrade) | REV L746-751 | PASS |
| 8E override test | 70% / 60% / 50% | Same as 3B. Only 50% falls below the 60% trigger | REV L991 | PASS (wording: R1-S4) |
| H2 post-tax RoA | 3.08% | 4.11 x 0.7483 = 3.0755 | REV L708 | PASS |
| NIM QoQ | -34 bps (printed) | P:R793 | REV L921 | PASS |
| 6B watchlist tally | 4 GREEN (1, 3, 4, 6); 3 split (2, 5, 8); 1 UNKNOWN (7) | 4 + 3 + 1 = 8 items | REV L395-406 | PASS |
| A4 analyst_note length | n/a | about 180 words, under the 200 cap | REV L1257 | PASS |

Dependency alignment: I searched the rewrite for stale loop-0 wording ("A to C", "5 GREEN", "fails on two", "-35 bps", "3.07%"). None remains. One stale block does remain, the reconciliation preamble (R1-1 below).

### R3. New findings after loop 1

**R1-1 [CONTRADICTION, loop A4].** The preamble table still counts the pre-loop ledgers.
- REV L33 reads "R001-R755 (755 rows) + M01-M05 signature lines | all 755 + 5 | 0".
- REV L34 reads "R001-R913 (913 rows) | all 913 | 0".
- The corrected ledgers now hold results M01-M07 (LED-R L25-31) and presentation M01-M02 (LED-P L1003-1004).
- A4's reconciliation count therefore disagrees with the ledgers it reconciles. The loop itself created this: A2 added rows, and A4 did not update its count.

**R1-2 [MISSING, loop A4].** Results ledger row M07 is now an orphan.
- M07 is R:L1438, the CS cover-letter signature at 21-10-2026 11:39:14.
- A grep of the rewritten review for "1438", "11:39" and "M07" returns no hits. M07 also sits outside the "755 + 5" reviewed set at REV L33.
- The other new rows are cited. M06 is cited at REV L22. Presentation M01 is cited at REV L23 and as P:L667 throughout. M02 is cited at REV L23.
- Substance: M07 falls after the 11:21 approval (R:L45). The CS-signing pattern is already carried in A3-16 (REV L610; Q23 at REV L1197). No new forensic is expected.

Fix for both findings is one A4 edit. Nothing in it changes an analysis figure.
- REV L33 becomes "R001-R755 (755 rows) + M01-M07 signature lines | all 755 + 7 | 0".
- REV L34 becomes "R001-R913 (913 rows) + M01-M02 (P:L667, P:L807) | all 913 + 2 | 0".
- Add one line: "M07 (R:L1438, CS cover-letter signature 11:39:14): reviewed, no finding; after the 11:21 approval; CS-signing pattern carried in A3-16."

Loop target: A4. The orphan rule maps an unreviewed row to A3. A3's forensic content for this row already exists (A3-16 for CS signing, A3-18 for M06), so only A4's reconciliation needs the edit.

STYLE (logged, no loop):
- **R1-S1.** The REV L7 change log says "No figure changed except the restated credibility sensitivity ... and the ST-5 rounding". The 6B tally also changed: REV L406 now reads 4 GREEN / 3 split, where loop 0 had 5 GREEN / 2 split. Watchlist item 8 status changed too (REV L402). The body figures are right; the log understates the change set.
- **R1-S2.** LED-P L1007 justifies the R076 relabel by saying 1,219 sits "beside +10% QoQ marker". The +10% on P:L150 is YoY disbursement growth (P:R079). The proof is 1,219 + 1,403 = 2,622 (P:L121) and 1,403 / 1,219 = +15% QoQ (P:L120). The relabel itself is correct.
- **R1-S3.** LED-P L1004 calls the P:L807 "0" an "axis/label base". It is the 10+ year cohort's potential-capacity value, the fourth addend of the 4,408 headroom (2,301 + 1,547 + 560 + 0).
- **R1-S4.** REV L991 says "one scoring choice reaches the 60% boundary and two reach the discount zone". Either single choice reaches 60%. Only both together reach 50%, the discount zone. Reword.

### R4. Verdict after loop 1

**VERDICT: INCOMPLETE.** Loop back to **A4**.
- Gap: R1-1 (CONTRADICTION, preamble counts) and R1-2 (MISSING, orphan row M07). One edit fixes both.
- All seven loop-0 findings are closed, and all five loop-0 style notes are applied.
- No FACTUAL finding. No arithmetic mismatch.
- The fix changes no analysis figure, no flag, no protocol verdict (PROCEED WITH FLAGS) and no position (HOLD 4%).

Why this is not STYLE: the fix changes a number in the reconciliation table (755 + 5 to 755 + 7) and a fact (orphans 0). The rules say such a finding is never STYLE. The orphan rule is a hard FAIL.

Remediation cap: the coordinator labelled this loop 1 of 1. If a second loop is refused, this goes to Halt 1 as an open item. The operator decides that, not A5. The open item is the two-row table edit plus one reviewed-no-finding line, as given in R3.

```yaml
stage: A5-adversary
company: "AYE"
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
  orphan_rows:
    - "results ledger M07: R:L1438 CS cover-letter signature 21-10-2026 11:39:14; not cited in the review and outside the REV L33 reviewed set (755 + 5)"
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "YoY core PBT +576.8% is real and larger than reported; YoY PAT rise 116% recurring", counter: "Trough base; ~Rs14 cr/qtr post-IPO funding mix unwound by re-levering to 4-4.5x; ~13 Q2 ECL draw inside recurring", source_line: "P:R387; P:R797; P:R798; P:L509; P:R852; P:R853; C:L272-274; P:R653", type: "MISSING", status: "grafted loop 1 (REV L184, L197-201, L249, L291)"}
  - {claim: "Asset quality GREEN; over-lending tripwire GREEN", counter: "Falling repeat share means incremental lending tilts to first-time borrowers (new +23% YoY, repeat -16%); repeat loans perform better on credit cost", source_line: "C:L98-102; C:L259-260; P:R433; C:L459; P:R592; P:R593", type: "MISSING", status: "grafted loop 1 (REV L333, L402, L533)"}
  - {claim: "Credibility 70% Grade B; opex DELIVERED early", counter: "Opex delivery denominator-assisted (-14 bps on avg AUM vs -32 bps on ATA); 60% if scored PARTIAL", source_line: "R:R132-R146; P:L920; P:R646; P:R073; P:R074", type: "MISSING", status: "grafted loop 1 (REV L725, L744-751)"}
findings_by_type:
  factual: []
  missing:
    - "R1-2 (A4): orphan ledger row results M07 (R:L1438, CS signature 11:39:14) neither cited nor marked reviewed in the review; substance already carried in A3-16 (REV L610)"
  contradiction:
    - "R1-1 (A4): preamble REV L33-34 counts 755 + M01-M05 and 913; corrected ledgers hold results M01-M07 (LED-R L25-31) and presentation M01-M02 (LED-P L1003-1004)"
  style:
    - "R1-S1: REV L7 change log omits the 6B tally change (now 4 GREEN / 3 split) and the watchlist 8 status change"
    - "R1-S2: LED-P L1007 relabel rationale calls +10% a QoQ marker; it is YoY (P:R079); proof is 1,219 + 1,403 = 2,622"
    - "R1-S3: LED-P L1004 calls the P:L807 '0' an axis base; it is the 10+ yr cohort capacity, 4th addend of 4,408"
    - "R1-S4: REV L991 wording; either single scoring choice gives 60%, only both together give 50%"
loop_back_to: "A4"
gap: "A4 edit, no figure changes: (1) REV L33 to 'R001-R755 (755 rows) + M01-M07 signature lines | all 755 + 7 | 0'; (2) REV L34 to 'R001-R913 (913 rows) + M01-M02 (P:L667, P:L807) | all 913 + 2 | 0'; (3) add 'M07 (R:L1438, CS cover-letter signature 11:39:14): reviewed, no finding; after the 11:21 approval; CS-signing pattern carried in A3-16'. A3 need not re-run (A3-16 and A3-18 already hold the forensic content)."
style_notes:
  - "R1-S1: list the 6B tally and watchlist 8 status change in the REV L7 change log"
  - "R1-S2: correct the R076 relabel rationale in LED-P L1007 (+10% is YoY)"
  - "R1-S3: describe P:L807 '0' as the 10+ yr cohort potential capacity in LED-P L1004"
  - "R1-S4: reword REV L991 so only both scoring choices together reach the 50% discount zone"
analyst_note: "Re-audit after loop 1 of 1. All seven loop-0 findings are closed. A2 added M01-M02 (presentation L667, L807) and M06-M07 (results L980, L1438) and corrected the signature-timing line; the blocks match. A4 grafted ADV-1 to ADV-3 with correct anchors and arithmetic. It aligned every dependent line (3B now A to D, 6B tally 4 GREEN / 3 split, two new flags) and applied all five style notes. I recomputed every new figure: zero mismatches. One defect remains, and the loop itself created it. A4's preamble (REV L33-34) still counts the pre-loop ledgers (755 + 5; 913), so results M07, the CS signature at 11:39:14, is an orphan row. In substance it is immaterial: it falls after the 11:21 approval, and A3-16 already carries the CS-signing pattern. The fix is two table rows plus one reviewed-no-finding line. It moves no figure, flag, verdict or position. The rules make an orphan row and a count contradiction non-STYLE, so the verdict is INCOMPLETE. If the one-loop cap binds, the operator decides whether to apply the edit or carry it to Halt 1 as an open item."
```

---

## RE-AUDIT AFTER LOOP 2

Re-audit date 2026-10-24. Correction loop 2, operator-approved 2026-10-24. Final iteration; no third loop.
Re-read: the rewritten A4 review and the current A2 ledgers. The A2 ledgers did not change in loop 2: R1-S2 and R1-S3 were logged only.
Line references below point to the loop-2 files.

### L2-1. Closure of loop-1 findings

| ID | Type | Loop-1 gap | Evidence after loop 2 | Status |
|---|---|---|---|---|
| R1-1 | CONTRADICTION | The preamble counted 755 + M01-M05 and 913 | REV L35: "R001-R755 (755 rows) + M01-M07 signature lines \| all 755 + 7 \| 0". REV L36: "R001-R913 (913 rows) + M01-M02 (P:L667, P:L807) \| all 913 + 2 \| 0". The ledgers agree: 7 M rows in results (LED-R L25-31) and 2 in presentation (LED-P L1003-1004). Concall REV L37 reads "+ M1-M7 \| all 346 + 7", and LED-C holds 7 M rows | CLOSED |
| R1-2 | MISSING | Orphan row M07 | REV L43: "M07 (R:L1438, CS cover-letter signature 21-10-2026 11:39:14): reviewed, no finding; after the 11:21 approval; CS-signing pattern carried in A3-16." REV L42 marks M06 reviewed via A3-18. REV L45 accounts for presentation M01 and M02 | CLOSED. Orphan rows: 0 |
| R1-S1 | STYLE | Change log incomplete | REV L7 now lists the watchlist 8 status change and the 6B tally change (5 GREEN / 2 split to 4 GREEN / 3 split) | APPLIED |
| R1-S4 | STYLE | 8E wording | REV L999: "Either single scoring choice (opex PARTIAL, or narrowing DROPPED) reaches the 60% boundary; only both together reach 50%, the discount zone" | APPLIED |
| R1-S2, R1-S3 | STYLE (A2) | Ledger wording | Logged only, as the coordinator ruled. Carried below | LOGGED |

### L2-2. Fresh spot check of the loop-2 rewrite

- **Scope.** Loop 2 changed only the header and preamble: REV L7, L9 and L35-45. REV L9 says "No figure changed".
- **Figures.** I checked 14 load-bearing figures and verdict lines by grep. All are unchanged, each 8 lines lower than in loop 1, which matches the header and preamble additions:
  - core PBT +576.8% (REV L192); funding-mix 14.2 (L207); recurring ~73.2 (L208, L257); 116% (L255, L299);
  - 163.86 identity (L287); 19.7% of Q2 PAT (L291); slippage proxy 4.6% (L296);
  - 6B tally 4 GREEN (L414); H2 post-tax RoA 3.08% (L716); opex 10.05% to 9.91% (L733);
  - 3B 60.0% / 60.0% / 50.0% (L756-758); position HOLD 4% (L1006); protocol verdict PROCEED WITH FLAGS (L1032).
- **Arithmetic.** Mismatches above rounding: 0.
- **Coverage.** Orphans 0. Missing from ledger 0. The preamble counts match all three ledgers.
- **Brief.** Unchanged and complete. All five parts are present.

### L2-3. Findings after loop 2

No FACTUAL, MISSING or CONTRADICTION finding.

STYLE (logged, no loop):
- **R2-S1 (A4).** The REV L24 source caution still says "results A2 ledger line 28 is wrong". A2 corrected that statement in loop 1 (now LED-R L32), and LED-R L28 is now M04. The caution is true as history and the facts it states are right (11:09:12 before 11:15). Add "(corrected by A2 in loop 1)". I missed this in the loop-1 re-audit.
- **R2-S2 (A4).** REV L45 says M01 and M02 "are used in Steps 1L, 4C and 5L". M01 (P:L667) is. M02 (P:L807) feeds the 4,408 headroom in 6D T3 and Q17, not those steps.
- **R1-S2 and R1-S3 (A2, carried).** The LED-P L1007 relabel rationale calls +10% a QoQ marker; it is YoY (P:R079). LED-P L1004 calls the P:L807 "0" an axis base; it is the 10+ year cohort capacity.

### L2-4. Verdict after loop 2

**VERDICT: COMPLETE (with style notes).** No loop. Notion save may proceed.
- All loop-0 and loop-1 findings are closed.
- Three bear counters are grafted and intact.
- Arithmetic mismatches: 0. Orphan rows: 0.
- Protocol verdict PROCEED WITH FLAGS and position HOLD 4% stand.
- Four style notes are recorded for the record: R2-S1, R2-S2, R1-S2 and R1-S3.

```yaml
stage: A5-adversary
company: "AYE"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
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
surviving_bear_counters:
  - {claim: "YoY core PBT +576.8% is real and larger than reported; YoY PAT rise 116% recurring", counter: "Trough base; ~Rs14 cr/qtr post-IPO funding mix unwound by re-levering to 4-4.5x; ~13 Q2 ECL draw inside recurring", source_line: "P:R387; P:R797; P:R798; P:L509; P:R852; P:R853; C:L272-274; P:R653", type: "MISSING", status: "grafted loop 1; intact loop 2 (REV L192, L205-209, L257, L299)"}
  - {claim: "Asset quality GREEN; over-lending tripwire GREEN", counter: "Falling repeat share means incremental lending tilts to first-time borrowers (new +23% YoY, repeat -16%); repeat loans perform better on credit cost", source_line: "C:L98-102; C:L259-260; P:R433; C:L459; P:R592; P:R593", type: "MISSING", status: "grafted loop 1; intact loop 2 (REV L341, L410)"}
  - {claim: "Credibility 70% Grade B; opex DELIVERED early", counter: "Opex delivery denominator-assisted (-14 bps on avg AUM vs -32 bps on ATA); 60% if scored PARTIAL", source_line: "R:R132-R146; P:L920; P:R646; P:R073; P:R074", type: "MISSING", status: "grafted loop 1; intact loop 2 (REV L733, L752-759)"}
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "R2-S1 (A4): REV L24 source caution still says 'results A2 ledger line 28 is wrong'; A2 corrected it in loop 1 (now LED-R L32; L28 is M04). Add '(corrected by A2 in loop 1)'"
    - "R2-S2 (A4): REV L45 says M01 and M02 are used in Steps 1L, 4C and 5L; M02 (P:L807) feeds the 4,408 headroom (6D T3, Q17), not those steps"
    - "R1-S2 (A2, carried): LED-P L1007 relabel rationale calls +10% a QoQ marker; it is YoY (P:R079)"
    - "R1-S3 (A2, carried): LED-P L1004 calls the P:L807 '0' an axis base; it is the 10+ yr cohort capacity, 4th addend of 4,408"
loop_back_to: ""
gap: ""
style_notes:
  - "R2-S1: mark the REV L24 ledger-line-28 caution as corrected by A2 in loop 1"
  - "R2-S2: REV L45 should tie M02 to the 4,408 headroom (6D T3, Q17), not Steps 1L/4C/5L"
  - "R1-S2: correct the R076 relabel rationale in LED-P L1007 (+10% is YoY)"
  - "R1-S3: describe P:L807 '0' as the 10+ yr cohort potential capacity in LED-P L1004"
analyst_note: "Re-audit after loop 2, the final iteration. R1-1 is closed. The preamble now reads 755 + M01-M07 and 913 + M01-M02 (REV L35-36), which matches the ledgers: 7 results M rows, 2 presentation M rows, and 7 concall M rows against REV L37. R1-2 is closed. M07 is marked reviewed, no finding (REV L43), and M06 is marked reviewed via A3-18 (REV L42). R1-S1 (REV L7) and R1-S4 (REV L999) are applied. I spot-checked 14 load-bearing figures and verdict lines. All are unchanged, each 8 lines lower than in loop 1, which matches the header and preamble additions. The brief, verdict PROCEED WITH FLAGS and HOLD 4% are intact. Two new STYLE notes remain, both cosmetic. The REV L24 caution still calls ledger line 28 wrong after A2 fixed it; I missed that in loop 1. REV L45 ties M02 to the wrong steps. Neither changes a number, fact or conclusion. Verdict COMPLETE with style notes; Notion save may proceed."
```
