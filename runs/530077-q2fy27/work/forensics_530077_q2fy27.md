# FORENSIC NOTES (A3): results | Puretrop Fruits Limited (formerly Freshtrop Fruits Limited) | 530077 | Q2 FY27

Doctype: results (filed outcome letter, limited review report, balance sheet, P&L, cash flow). No deck, no release, no call.
Basis: STANDALONE ONLY (no consolidated statements filed). Units: Rs Lakhs as printed (x0.01 = Rs Cr). Numbers not converted.
Inputs read: A1 structured (R001-R446), A1 fulltext (356 lines), A2 ledger. Source PDF and inputs/ NOT opened.
Prior-quarter fulltext: none (first quarterly run). Notion checklist: none (PRE-THESIS READ). F17 runs against the operator watch list.
Caveat: fulltext pages 3-6 are A1 visual transcriptions (no text layer). Every statement number below rests on that transcription. A1 internal tie-outs pass within 0.01-0.02 Lakhs, and A3 roll-forwards below (PPE, investments, receivables, payables, DTL, cash) also tie, so transcription risk is low but not zero. Line 157 is the one number A3 asks A1 to re-check (see A3-05).

## 1. LEDGER RECONCILIATION

| item | result |
|---|---|
| structured rows | 446 (R001-R446) |
| ledger rows | 446, orphan_ids none |
| rows read verbatim at cited fulltext line | 446 / 446 = 100% |
| ledger line refs vs fulltext | all match the fulltext line content |
| ZERO_STANDING rows | 54 (BS 20, PL 24, CF 6, CE 4), recount matches A2 |
| ledger label notes | RESTATED on R040/R041/R347/R348/R358/R359 means the same cash figure repeats across BS (L163), CF (L336) and CE (L349). It is NOT a prior-period restatement. A3 found no restatement. R391 (FORWARD) is filed by A2 under agenda_items; harmless. R373 partner name F. S. SHAH is image-only (A1 note); L134 text carries only "Mem. No. 133589". |
| NOT FOUND in filing (not estimated) | segment table, consolidation list, EoM / Other Matter / Going Concern paragraphs, buy-back note, discontinued-operation note, rename note, RPT disclosure, dividend, AGM / record date, director items, Note 3 |

## 2. KEY DERIVED NUMBERS (Rs Lakhs; derived from cited lines, arithmetic shown in the finding)

| metric | Q2 FY27 | Q1 FY27 | Q2 FY26 | H1 FY27 | H1 FY26 | FY26 |
|---|---|---|---|---|---|---|
| Revenue from ops (L221) | 2,640.84 | 2,802.51 | 2,689.43 | 5,443.36 | 5,483.89 | 12,188.22 |
| Material cost = L225 + L227 | 1,207.06 | 1,408.82 | 1,377.16 | 2,615.88 | 3,162.92 | 7,656.82 |
| Gross margin % | 54.3% | 49.7% | 48.8% | 51.9% | 42.3% | 37.2% |
| Other expenses % rev (L231) | 30.7% | 19.5% | 16.3% | 24.9% | 18.7% | 15.3% |
| EBITDA = PBT + fin + D&A - OI | 324.53 | 491.11 | 537.75 | 815.65 | 588.40 | 1,172.28 |
| EBITDA margin % | 12.3% | 17.5% | 20.0% | 15.0% | 10.7% | 9.6% |
| Other income % PBT (L222/L233) | 37.9% | 35.8% | 0.4% | 36.5% | 37.9% | 39.9% |
| PBT ex other income | 159.21 | 341.23 | 371.86 | 500.45 | 268.17 | 578.48 |
| ETR = (L237 + L238) / L235 | 7.1% | 14.1% | 29.0% | 11.8% | 24.6% | 24.5% |

Balance sheet (L148-L189), 31.03.2026 -> 30.09.2026: inventory 2,023.34 -> 5,291.18 (+161.5%); trade receivables 630.28 -> 234.92 (-62.7%); current investments 6,103.48 -> 3,905.31 (-36.0%); other bank balances 574.34 -> 22.22; short-term borrowings 22.70 -> 1,199.55; long-term borrowings 86.74 -> nil; net worth 13,785.48 -> 12,272.26.
Net cash (investments + cash + other bank - all borrowings): 6,576.65 -> 2,770.32, a fall of 3,806.33.
Working-capital days (derived): receivable days 18.9 (Mar, FY revenue / 365) -> 7.9 (Sep, H1 revenue / 183). Inventory days on revenue 60.6 -> 177.9. Inventory days on material cost 96.5 -> 370. The Sep figures are seasonal (H1 build). No 30.09.2025 balance sheet is in the filing, so no like-for-like YoY days comparison exists. The P&L inventory-change line (L227) gives the YoY build comparison instead.
Roll-forwards that TIE: PPE + CWIP 5,119.09 + 102.89 - 263.88 - 3.24 = 4,954.86 (exact); investments 6,103.48 - 3,254.95 + 903.70 + 126.09 + 26.98 = 3,905.30 (0.01); receivables change 395.36 = 373.63 + 21.73 FX; DTL 357.84 - 7.86 = 349.98 vs 350.00; payables-side change 102.42 + 2.87 FX = 105.29.
Roll-forwards that DO NOT tie: equity (A3-10, gap 40.10); current tax account (A3-05, gap about 50.00).

## 3. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R184-R201, R273, R274, R295, R296 | L240, L295, L307 | "10 Profit (Loss) from Discontinued Operations \| - \| - \| 139.12 \| - \| 2,034.14 \| 2,337.51" | AMBIGUOUS | FY26 PAT 2,529.02 (L243) is 71% discontinued (1,802.69, L242). Continuing FY26 PAT is 726.33 (EPS 9.11, L254), not 2,529.02 (EPS 31.73, L258). No note names the discontinued business. The FY26 cash flow carries the full 2,337.51 discontinued PBT inside operating profit (L295, L307 = 3,798.15) with no gain-on-disposal adjustment and no disposal proceeds in investing (L319-L323). Either the discontinued result was operating trading profit or a disposal gain sits in operating cash. The rows 10-12 stay in the template, so a residual item (deferred consideration, indemnity, true-up) can still land there. Any base built on FY26 total profit or FY26 CFO 2,407.65 (L317) is overstated. |
| A3-02 | F1 | R074, R075, R208-R213 | L187, L245 | "(c) Provisions \| - \| -" ; "(a) Items that will not be reclassified to profit or loss \| 6.57 \| 6.57" | AMBIGUOUS | Provisions are nil at both dates, yet OCI carries non-reclassifiable remeasurement items each period, which normally means a defined-benefit (gratuity) plan. The filing does not show where that obligation sits. Verify at the Annual Report: plan status, funded or unfunded, and classification. |
| A3-03 | F1 / F14 | R285, R345, R346, R356, R357 | L302, L335, L348 | "Unrealised Gain/(Loss) on foreign currency Cash and Cash Equivalents \| (22.51) \| (22.65)" ; "in Exchange Foreign Currency Account \| - \| -" | AMBIGUOUS | The cash flow books an FX loss on foreign-currency cash equivalents in both periods, but the cash-equivalent table shows nil foreign-currency balances at both dates. The FX-on-cash line looks like a plug, or the FX cash sits outside the table. Small (22.51) but it bears on how the exporter holds FX. |
| A3-04 | F8 | R166-R177 | L237, L238 | "Current Tax \| 18.00 \| 83.00 \| 115.12 \| 101.00 \| 133.40 \| 274.12" | FORWARD-SIGNAL | ETR 7.1% Q2 FY27 ((18.00 + 0.19) / 256.30) and 11.8% H1 FY27 (93.14 / 787.79), against 29.0% Q2 FY26, 24.5% FY26 and statutory 25.17%. Shield vs statutory: Q2 46.32 (1,807 bps, 19.5% of Q2 PAT 238.11); H1 105.15 (1,335 bps, 15.1% of H1 PAT 694.64). No note explains the rate. Candidates: concessional capital-gains rate on treasury income, a tax true-up, an exemption. Lean bear: if H2 runs at statutory, H2 PAT absorbs the step-up. Deferred tax: credits in 5 of 6 columns (L238), small (H1 7.86 = 100 bps of PBT), consistent with the DTL roll; no "earlier years" tax line exists. |
| A3-05 | F8 / F14 | R032, R033, R076, R077, R169, R311 | L157, L188, L316 | "(g) Income Tax Assets (Net) \| (6.62) \| -" | AMBIGUOUS | Tax account does not roll. Opening current tax liability 8.64 (L188) + H1 current tax 101.00 (L237) - tax paid 53.02 (L316) gives about 56.62 owed. The balance sheet shows a negative asset of (6.62) and nil liability, a gap of about 50.00. The (6.62) also equals the FY26 OCI tax figure at L246 ("(3.31) \| 0.52 \| (6.62)"). Possible carry-over error in the filing or in transcription. A1 should re-check L157 against the page image; A4 asks management for the tax-account roll. Cash tax paid is 52% of the H1 provision. |
| A3-06 | F9 | R208-R231 | L245, L247 | "(c) Items that will be reclassified to profit or loss \| (12.00) \| 12.06 \| (4.82) \| 0.06 \| (0.16) \| 4.11" | AMBIGUOUS | Reclassifiable OCI swings (12.00) in Q2 and +12.06 in Q1. Each quarter is 2.9x the full FY26 amount (4.11). The nature (cash-flow hedge reserve or FVOCI debt) is not disclosed. Non-reclassifiable OCI is 6.57 in both Q1 and Q2, which is FY26 26.29 / 4 to the paisa. Remeasurement looks booked as a pro-rata estimate, not a valuation. Verify hedge policy and actuarial assumptions at the Annual Report. |
| A3-07 | F10 | R052, R053, R244-R249, R333-R338, R388 | L171, L251, L329, L330, L331 | "Buy-Back of Shares \| (110.00) \| -" ; "16 Paid up Equity Share Capital ... \| 686.99 \| 686.99 \| 796.99" | NEUTRAL-FACT | Paid-up capital fell 796.99 -> 686.99 = 11.00 lakh shares extinguished at Rs 10 FV, 13.80% of the 79.699 lakh pre-buy-back count. Completed in Q1 FY27 (Q1 column already 686.99). Mechanical EPS uplift 16.0% (79.699 / 68.699). No note on the buy-back in this filing. Basic = diluted in all six columns; spread 0, no dilutive instruments shown. |
| A3-08 | F10 | R251-R268 | L254 | "Basic and Diluted Rs per share \| 3.47 \| 6.65 \| 3.33 \| 10.11 \| 4.09 \| 9.11" | AMBIGUOUS | Q1 EPS 6.65 = 456.53 / 68.699 and H1 EPS 10.11 = 694.64 / 68.699: both use the closing share count. The 31.03.2026 count was 79.699 lakh (L171). If the shares were extinguished after 1 April, the Ind AS 33 weighted average is higher and printed Q1 and H1 EPS are overstated. Ask the extinguishment date. |
| A3-09 | F10 (funding of the capital action) | R036, R037, R042, R043, R056, R057, R064, R065, R124-R129, R327, R329 | L161, L164, L182, L229, L327 | "(i) Short term borrowings \| 1,199.55 \| 22.70" | FORWARD-SIGNAL | The buy-back and the inventory build were funded by selling treasury (investments -2,198.17), running down deposits (-552.12) and borrowing (+1,176.85 short-term). Net cash fell 3,806.33 in six months (6,576.65 -> 2,770.32). Finance cost rose to 32.91 in Q2 from 18.41 in Q1 (+79%). The company now borrows while it still holds 3,905.31 of investments. Two readings: cheap seasonal export credit (benign), or reluctance to sell further treasury (cost drag). The H2 borrowing level separates them. Smaller treasury also shrinks the other-income base (A3-11). |
| A3-10 | F11 | R052-R055, R238-R243, R333-R338 | L171, L172, L331 | "Increase / (Decrease) in total Equity \| (2,130.10) \| 2.80" | AMBIGUOUS | Equity roll gap 40.10. Net worth 13,785.48 -> 12,272.26 with H1 total comprehensive income +704.53 means non-TCI reductions of 2,217.75. Cash flow equity outflows are 110.00 + 17.75 + 2,130.10 = 2,257.85. 40.10 of the (2,130.10) is not an equity movement. [INFERENCE] 2,217.75 = 110.00 FV + 17.75 expenses + 2,090.00 premium, consistent with 11.00 lakh shares at Rs 200; the price is NOT in the filing. Gap is 0.33% of net worth, below the 5% bar, but unexplained. No third-party net-worth number is in context. The FY26 line (2.80) is also unexplained. Candidate reconciling items: dividend, OCI reserve transfer, a misplaced operating item. |
| A3-11 | F17 (watch: revenue trend) | R082-R099, R136-R141, R148-R153 | L221, L222, L231, L233 | "(g) Other expenses \| 810.19 \| 545.28 \| 438.48" | FORWARD-SIGNAL | Revenue -1.8% YoY and -5.8% QoQ in Q2; H1 -0.7%. Other expenses +84.8% YoY and +48.6% QoQ, rising to 30.7% of revenue from 16.3%. Q2 EBITDA 324.53 vs 537.75 (-39.7%), margin 12.3% vs 20.0%. PBT excluding other income 159.21 vs 371.86 (-57.2%). Other income is 37.9% of Q2 PBT; the cash flow ties 169.66 of H1 other income (287.34) to treasury (L298 126.09, L303 26.98, L306 16.59). With investments down 36%, that support shrinks. Low tax (A3-04) hides part of the fall: continuing PAT is only -10.2% YoY. No note explains the other-expense spike. H1 EBITDA is up 38.6% because Q1 FY26 was weak (derived Q1 FY26 EBITDA 50.65), so the half and the quarter tell opposite stories. |
| A3-12 | F17 (watch: gross margin, inventory days) | R034, R035, R100-R117, R299, R313 | L159, L225, L227, L310, L317 | "(a) Inventories \| 5,291.18 \| 2,023.34" ; "(3,234.62) \| (2,821.55)" | FORWARD-SIGNAL | H1 gross margin 51.9% vs 42.3% (+960 bps); Q2 54.3% vs 48.8% (+550 bps). In the same half the inventory build was 3,234.62 vs 2,821.55 last year (+14.6%) on flat revenue, and closing inventory is 43% of FY26 revenue. Part of the margin gain can sit in closing inventory valuation (cost absorbed into stock). H2 sell-through and realisation on 5,291.18 of stock decides whether the margin holds. H1 operating cash flow -991.50 against PAT 694.64. FY26 H2 gross margin was about 33% (derived), so half-on-half comparison is the only valid one. |
| A3-13 | F17 (watch: receivable days) | R038, R039, R283, R297 | L162, L309 | "(ii) Trade receivables \| 234.92 \| 630.28" | NEUTRAL-FACT | Receivables fell 62.7%; days 18.9 -> 7.9 (seasonal basis). Collections 373.63 plus FX 21.73 tie the change. Bad debts nil (L304). No stress signal on receivables. |
| A3-14 | F17 (watch: RPT, business change) | R439-R441, R366 | L260-L263, L60 | "4 Previous Year's figures have been regrouped, reclassified wherever considered necessary." | AMBIGUOUS | The notes block carries three boilerplate notes. It is silent on the rename, the FY26 discontinued operation, the buy-back, related-party transactions and the other-expense spike. Silence count 1 quarter (first observed). Not yet a sustained-silence negative; becomes CONFIRMATORY-NEGATIVE if repeated next quarter while A3-11 deteriorates. |
| A3-15 | F12 | R439-R441, R440 | L260-L263 | "2 Revenue From Operations includes Export Incentives." | AMBIGUOUS | No segment table and no "single reportable segment" statement, in a company that discontinued an operation in FY26. The remaining business mix (processing, export, domestic) cannot be checked. No segment assets or liabilities to trend. |
| A3-16 | F14 | R301, R042, R043 | L164, L311 | "(Increase) / Decrease in financial assets \| 546.49 \| (444.20)" | AMBIGUOUS | The 552.12 fall in other bank balances (deposits) sits inside operating cash flow (546.49 = 552.12 - 5.19 loans - 0.44 other). Without it H1 operating cash flow is -1,543.62, not -991.50. In FY26 the deposit placement (444.20) depressed CFO. Deposits over 3 months are normally investing. Cash conversion must be read ex this line. |
| A3-17 | F14 | R440, R383 | L262 | "Revenue From Operations includes Export Incentives." | AMBIGUOUS | Export incentives sit inside revenue with no amount. Revenue and margin quality depend on scheme rates the filing does not quantify. |
| A3-18 | F14 | R441, R442, R437, R430, R232-R243, R378, R370, R421, R431 | L263, L289, L249, L250, L238, L178, L157, L204, L81, L83, L215 | "STATEMENT OF CASH FLOW FOR YEAR ENDED ON 30th SEPTEMBER 2026" | NEUTRAL-FACT | Drafting cluster: Note 3 missing (notes run 1, 2, 4); half-year cash flow titled "YEAR ENDED"; L249 labels the OCI subtotal (4.06) as "Total Comprehensive Income for the period" while L250 holds the real total (234.05); "Deffered" (L238), "liabilitites" (L178); a negative figure on the asset side (L157); old domain www.freshtrop.com and info@freshtrop.com still on letterhead (L204-L205, L278-L279); P&L title omits "standalone" (L215) though the review covers standalone (L83); auditor contact on gmail (L81). Each is immaterial. Together they are a governance data point on filing care. Page-2 OCR errors are A1 artefacts, not filing errors, and are excluded. |
| A3-19 | F15 | R366, R387, R371, R375, R380 | L60, L89, L139, L287 | "(FORMERLY KNOWN AS FRESHTROP FRUITS LIMITED)" | AMBIGUOUS | Entity rename Freshtrop Fruits -> Puretrop Fruits; CIN unchanged (L15400GJ1992PLC018365). No consolidation list exists, so the rename is the only entity change. [INFERENCE] rename, FY26 discontinued operation and a 13.8% buy-back in one twelve-month window read as a business reshape. The filing states none of the reasons. |

## 4. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | FINDING | 54 ZERO_STANDING rows read. Template anticipates: discontinued ops (live in FY26, A3-01), exceptional items (nil all 6 columns, L234), stock-in-trade purchases (nil, no trading, L226), bad debts (nil, L304), leases (nil both dates), provisions (nil despite DB OCI, A3-02), EEFC cash (nil despite FX-on-cash line, A3-03). NC investments print 0.00, not "-" (L153): a residual holding carried at nil; NEUTRAL. |
| F2 | N.A. | No consolidated statements filed (structured header; review covers standalone only, L83, L91). No S-vs-C gap to compute. |
| F3 | N.A. | No consolidated cost lines exist to compare; no subsidiaries disclosed. |
| F4 | PASS | Review report L83-L125 read: one auditor, no Other Matter paragraph, no component auditors. Unreviewed contribution 0%. |
| F5 | PASS | No EoM, Going Concern or modification; conclusion unmodified (L118-L125). No prior-quarter text to diff; this quarter is the baseline. |
| F6 | PASS | Lexicon hits are procedural or template only: "commenced" (L50, meeting time), "shall be made available" (L52, website), "will be reclassified" (L247, OCI template). No dated management commitment in the notes. |
| F7 | PASS | Hedge lexicon: only "assurance" in SRE 2410 boilerplate (L110, L115). No hedge in the notes. |
| F8 | FINDING | ETR 7.1% Q2, 11.8% H1 vs 25.17% (A3-04); current-tax account does not roll (A3-05). |
| F9 | FINDING | Reclassifiable OCI single-quarter swing 2.9x full FY26; identical 6.57 remeasurement in Q1 and Q2 (A3-06). |
| F10 | FINDING | Share count down 13.80% via buy-back (A3-07); EPS uses closing count (A3-08); funding shift to borrowings (A3-09). Basic-diluted spread 0. |
| F11 | FINDING | Net worth 12,272.26 = 686.99 + 11,585.27 ties. Equity roll vs cash flow gap 40.10 (A3-10). No third-party number in context. |
| F12 | FINDING | No segment disclosure or single-segment statement (A3-15). |
| F13 | PASS | Board approved results only (L44-L48); meeting 11:30-13:00 (L50); no AR, AGM, dividend, director or enabling-resolution item. |
| F14 | FINDING | Deposit flows in operating cash (A3-16); unquantified export incentives (A3-17); drafting cluster (A3-18); FX-on-cash vs nil EEFC (A3-03); tax asset sign (A3-05). |
| F15 | FINDING | Company rename Freshtrop -> Puretrop (A3-19). No consolidation list to diff. |
| F16 | N.A. | Results doctype; no presentation filed. |
| F17 | FINDING | Run per task instruction against the operator watch list (pre-thesis read, no Notion checklist, no call). Silence is measured against the filing notes. See section 6. |

## 5. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Results to be placed on www.puretrop.com | on filing, 27-Oct-2026 | R391, L52 | procedural (not a business commitment) |
| Buy-back of 11.00 lakh shares | completed by 30-Jun-2026 (Q1 paid-up 686.99, L251) | R333, L329; no note | completed (inferred from numbers; no note text) |
| Name change to Puretrop Fruits | completed on or before 27-Oct-2026 | R366, L60; no note | completed (inferred from letterhead; no note text) |

## 6. WHAT WAS NOT DISCUSSED (F17, against operator watch list)

| watch item | addressed in filing? | consecutive quarters of silence | note |
|---|---|---|---|
| Revenue trend | numbers only (L221), no commentary | 1 | Q2 -1.8% YoY, -5.8% QoQ (A3-11) |
| Gross margin | computable only (L225, L227), no commentary | 1 | H1 +960 bps with larger inventory build (A3-12) |
| Receivable days and inventory days | balance sheet only (L159, L162), no commentary | 1 | inventory +161.5%, receivables -62.7% |
| Related-party transactions | NOT FOUND in this filing | 1 | half-yearly RPT disclosure under Reg 23(9) is a separate filing; A4 should source it |
| Auditor remarks | ADDRESSED: unmodified limited review (L118-L125) | 0 | no EoM, no qualification |
| Business change / rename | letterhead only (L60, L89), no note | 1 | rename, FY26 discontinued op and buy-back unexplained (A3-01, A3-19) |
| F6 commitments | none beyond procedural | n/a | |

Silence counts start at 1 because this is the first observed quarter. No item is yet a sustained-silence confirmatory negative.

## 7. FLAGS FOR A4 (management questions)

FORWARD-SIGNAL: A3-04, A3-09, A3-11, A3-12.
AMBIGUOUS: A3-01, A3-02, A3-03, A3-05, A3-06, A3-08, A3-10, A3-14, A3-15, A3-16, A3-17, A3-19.

```yaml
stage: A3-forensics
company: "530077"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/530077-q2fy27/work/forensics_530077_q2fy27.md"
ledger_reconciled_pct: 100        # 446 / 446
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: FINDING
findings:
  - {id: "A3-01", check: "F1", line: "L240, L295, L307", classification: "AMBIGUOUS", implication: "FY26 PAT 2,529.02 is 71% discontinued (1,802.69); continuing base 726.33 / EPS 9.11. No note names the business; FY26 CFO 2,407.65 carries discontinued PBT 2,337.51 with no disposal adjustment."}
  - {id: "A3-02", check: "F1", line: "L187, L245", classification: "AMBIGUOUS", implication: "Provisions nil both dates while DB remeasurement OCI exists; gratuity obligation location unknown. Verify at AR."}
  - {id: "A3-03", check: "F1", line: "L302, L335, L348", classification: "AMBIGUOUS", implication: "FX loss (22.51) on FCY cash equivalents while EEFC balance nil both dates; FX-on-cash line looks like a plug."}
  - {id: "A3-04", check: "F8", line: "L237, L238", classification: "FORWARD-SIGNAL", implication: "ETR 7.1% Q2 / 11.8% H1 vs 25.17%; shield 105.15 Lakhs H1 = 15.1% of H1 PAT. H2 step-up risk; no note explains the rate."}
  - {id: "A3-05", check: "F8", line: "L157, L188, L316", classification: "AMBIGUOUS", implication: "Tax account gap about 50.00: 8.64 + 101.00 - 53.02 = 56.62 owed vs (6.62) printed on asset side; (6.62) equals FY26 OCI tax at L246. A1 to re-check L157."}
  - {id: "A3-06", check: "F9", line: "L245, L247", classification: "AMBIGUOUS", implication: "Reclassifiable OCI (12.00) Q2 / +12.06 Q1, each 2.9x full FY26 (4.11), nature undisclosed; remeasurement 6.57 identical Q1 and Q2 = FY26/4 (estimate, not valuation)."}
  - {id: "A3-07", check: "F10", line: "L171, L251, L329", classification: "NEUTRAL-FACT", implication: "Buy-back extinguished 11.00 lakh shares (13.80%) in Q1 FY27; mechanical EPS uplift 16.0%; no note. Basic = diluted, spread 0."}
  - {id: "A3-08", check: "F10", line: "L254", classification: "AMBIGUOUS", implication: "Q1 and H1 EPS divide by closing 68.699 lakh shares; if extinguished after 1-Apr, Ind AS 33 weighted EPS is lower than printed."}
  - {id: "A3-09", check: "F10", line: "L161, L164, L182, L229, L327", classification: "FORWARD-SIGNAL", implication: "Net cash 6,576.65 -> 2,770.32; ST borrowings 22.70 -> 1,199.55 while 3,905.31 investments held; finance cost Q2 +79% QoQ. Treasury and other-income base shrink."}
  - {id: "A3-10", check: "F11", line: "L171, L172, L331", classification: "AMBIGUOUS", implication: "Equity roll gap 40.10: non-TCI reduction 2,217.75 vs CF equity outflows 2,257.85. [INFERENCE] consistent with buy-back at Rs 200; price not in filing."}
  - {id: "A3-11", check: "F17", line: "L221, L222, L231, L233", classification: "FORWARD-SIGNAL", implication: "Q2 revenue -1.8% YoY; other expenses +84.8% YoY to 30.7% of revenue; EBITDA margin 12.3% vs 20.0%; PBT ex other income -57.2%; other income 37.9% of PBT; low ETR masks the fall."}
  - {id: "A3-12", check: "F17", line: "L159, L225, L227, L317", classification: "FORWARD-SIGNAL", implication: "H1 gross margin +960 bps alongside 14.6% larger inventory build on flat revenue; inventory 5,291.18 = 43% of FY26 revenue; H1 CFO -991.50. H2 sell-through decides whether the margin is real."}
  - {id: "A3-13", check: "F17", line: "L162, L309", classification: "NEUTRAL-FACT", implication: "Receivables 630.28 -> 234.92, days 18.9 -> 7.9; no collection stress; bad debts nil."}
  - {id: "A3-14", check: "F17", line: "L260-L263, L60", classification: "AMBIGUOUS", implication: "Notes silent on rename, FY26 discontinued op, buy-back, RPT and other-expense spike; silence count 1."}
  - {id: "A3-15", check: "F12", line: "L260-L263", classification: "AMBIGUOUS", implication: "No segment table or single-segment statement after an FY26 discontinued operation; business mix unverifiable."}
  - {id: "A3-16", check: "F14", line: "L164, L311", classification: "AMBIGUOUS", implication: "Deposit run-down 552.12 sits in operating cash; H1 CFO ex this line -1,543.62, not -991.50."}
  - {id: "A3-17", check: "F14", line: "L262", classification: "AMBIGUOUS", implication: "Export incentives inside revenue, amount not disclosed; revenue quality depends on scheme rates."}
  - {id: "A3-18", check: "F14", line: "L263, L289, L249, L238, L178, L204, L81, L215", classification: "NEUTRAL-FACT", implication: "Drafting cluster: Note 3 missing, half-year CF titled year, OCI subtotal mislabelled as TCI, typos, old freshtrop domain, gmail auditor contact. Cumulative governance data point."}
  - {id: "A3-19", check: "F15", line: "L60, L89, L139", classification: "AMBIGUOUS", implication: "Rename Freshtrop -> Puretrop, CIN unchanged, no note. [INFERENCE] rename + discontinued op + 13.8% buy-back read as a business reshape."}
forward_signals: ["A3-04", "A3-09", "A3-11", "A3-12"]
ambiguous: ["A3-01", "A3-02", "A3-03", "A3-05", "A3-06", "A3-08", "A3-10", "A3-14", "A3-15", "A3-16", "A3-17", "A3-19"]
commitments:
  - {commitment: "Results placed on www.puretrop.com", implied_date: "2026-10-27", ref: "R391 L52", status_word: "procedural"}
  - {commitment: "Buy-back of 11.00 lakh shares", implied_date: "by 2026-06-30", ref: "R333 L329 (no note)", status_word: "completed"}
  - {commitment: "Name change to Puretrop Fruits Limited", implied_date: "on or before 2026-10-27", ref: "R366 L60 (no note)", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Read the quarter as weaker than the headline. Q2 continuing PAT is down only 10.2% YoY because the effective tax rate fell to 7.1%. Pre-tax profit excluding other income is down 57.2%, driven by an 84.8% jump in other expenses that no note explains. The H1 gross margin gain of 960 bps coincides with a larger inventory build on flat revenue. Treat it as unproven until H2 sell-through. The balance sheet has changed shape: a 13.8% buy-back plus the stock build moved the company from 6,576.65 to 2,770.32 Lakhs net cash and onto short-term debt. That shrinks the treasury income, which supplied about 37% of pre-tax profit. FY26 total EPS 31.73 is 71% discontinued and must not be used as a base. Two roll gaps (equity 40.10, tax about 50.00) need answers. A1 should re-check L157, which is visually transcribed. F17 was run against the operator watch list by task instruction, not the results-doctype default N.A."
```
