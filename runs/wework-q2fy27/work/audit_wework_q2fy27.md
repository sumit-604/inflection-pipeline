# A5 ADVERSARY / COMPLETENESS RE-AUDIT (correction loop 1 of 1): WeWork India Management Ltd (WEWORK), Q2 FY27

Agent: A5 Adversary, model claude-opus-5-5. Date: 2026-10-28.
Review under audit (loop 1): runs/wework-q2fy27/work/review_wework_q2fy27.md (1,230 lines, read in full).
Loop-0 review (drift check only): runs/wework-q2fy27/work/review_wework_q2fy27_loop0.md (1,165 lines, read in full).
Loop-0 audit (items to verify closed): runs/wework-q2fy27/work/audit_wework_q2fy27_loop0.md.

Inputs read: the five A1 fulltexts (targeted line ranges and greps), the five A1 structured files (row-ID count grep), the five A2 ledgers (count-test headers).
Inputs not read: no source PDF, nothing under inputs/, no A3 forensics file, no orchestrator log. Disclosure: one grep ran on work/ with the glob `ledger_*_wework_q2fy27.md`, so it touched only the five ledgers.

Anchor convention: "rev L" = current (loop 1) review line. "rev0 L" = loop-0 review line. "results L", "deck L", "letter L", "press L", "concall L" = A1 fulltext lines.

---

## A. LOOP-0 ITEM CLOSURE (re-audit step 1)

| Item | Type | Loop-0 gap | Fixed at (rev L) | Fulltext re-check | Status |
|---|---|---|---|---|---|
| F1 | FACTUAL | FCFF classed as "does not rebuild"; formula called missing | L371 item 2, L478, L499, L585, L854, L864, L926, L964, L971, L1020-1022, L1166, L1213, L1227 | deck L660-667: 1,026.2 - 576.6 - 69.8 = 379.8; 379.8 - 363.8 = 16.0. deck L796: B (H1) 11.4. results L631: 783.68 Mn = 78.37; 78.37 - 69.8 = 8.57; 11.4 + 8.57 = 19.97. Full basis: 1,026.16 - 588.01 - 363.77 - 78.37 = (3.99) (results L627, L629, L631, L643-644) | CLOSED. A grep for "FCFF ... do(es) not rebuild" and "four unreconciled" finds no hit outside the change log |
| C1 | CONTRADICTION | capacity measurement-date "ambiguity" in flags and Q5 bear answer | L502 (Q5), L566 (mapping), L1169 (YAML Q5), L1219 (flag) | press L88-90 (145.3k, then 4.5k "in the first week of October"); deck L429-435 (Mar-26 126.9k, Sep-26 145.3k); concall L701-706 ("which ended in September 30th") | CLOSED. "ambiguit" and "7.2k" hit only the change log (rev L1125) |
| C2 | CONTRADICTION | 5-C "few new ROU in H1" vs Step 3 front-loading | L277 (Step 3), L335-336 (5-C) | results L542: 45,030.93 vs 45,939.04 Mn = (90.81) Cr; letter L735: ROU D&A H1 438.3; (90.81) + 438.3 = 347.49. results L575 + L583: +15.59 Cr; L643: principal 2,758.58 Mn = 275.86; 15.59 + 275.86 = 291.45 | CLOSED |
| M1 | MISSING | revenue-adjustment counter (claim 1) | L211, L252-255, L277, L303, L509, L955, L967, L983, L1018-1019, L1176, L1192, L1214, L1227 | letter L662: adjustment (1.3) Q2 FY27, 3.5 Q1 FY27, 3.7 Q2 FY26; letter L723: 2.2 H1 FY27, 6.3 H1 FY26; deck L704-706 same; deck L537 billed +32.5%; press L191-192 | CLOSED; every figure recomputes (Section E) |
| M2 | MISSING | ex-float FCF counter (claim 2) and direction label | L325, L327-328, L355, L367-371, L458, L956, L967, L1023-1024, L1216, L1227 | results L615, L626, L629, L631, L643-644 (CA); L267, L277, L280, L282, L293-294 (SA); concall L677-679 | CLOSED. Direction now "DETERIORATING ex-float" (rev L367); enum unchanged |
| M3 | MISSING | rent-free qualifier absent where the cash-rent claim is made (claim 3) | L969 (Section C net thesis), L1055-1060 (brief section 3), L1227 (analyst_note), L983 (monitorable M1) | concall L723-730; deck L795 (A: 245.6 to 298.2), L310 (area +27.1%), L404-408 (city mix) | CLOSED. The loop-0 sentence "That is real operating leverage on a cash basis" (rev0 L1038) is gone |

Style notes from loop 0, all closed:
- S1 rounding: rev L177 99.3%; L206 -230 bps; L222 -243 bps; L245, L250, L860, L969 +183 bps; L290 -2.30 pp.
- S2 associate strip named in the brief: rev L1017.
- S3 price line tagged SECONDARY: rev L1006, L1029.
- S4 L-F1-a added to the mapping table: rev L578; the letter count is now 17 of 17.
- S5 MFS-1 named: rev L33.
- S6 claim 4 restated on the deck basis: rev L632; deck L247-250 (7.5 MSF = 26%).
- S7 analyst's 2.9x recorded as defensible: rev L732; deck L472 (2.6 / 2.9 / 2.7), L488.
- S8 Q6 cites the call's contracted escalation: rev L503; concall L315.
- S9 "Undated" changed to NOT FOUND: rev L1099.
- S10 docs_merged lists five documents: rev L1152.

Result: 6 of 6 loop items closed; 10 of 10 style notes closed.

---

## B. DRIFT CHECK (re-audit step 2): PASS

Method: section-by-section read of both reviews, comparing every table row and paragraph.

| Change-log rows | Location checked | Matches log | New error introduced |
|---|---|---|---|
| #1-#2 (revision line; MFS-1) | rev L5, L33 | yes | none |
| #3-#4, #8 (S1 rounding) | rev L177, L206, L222, L245, L250, L290, L860 | yes | none; all recompute (Section E) |
| #5-#7, #9 (M1, C2 in Steps 2-4) | rev L211, L252-255, L277, L303 | yes | none |
| #10-#14 (M2, C2, F1 in Step 5 and Step 7) | rev L325-328, L335-336, L355, L366-371, L458 | yes | none |
| #15-#21 (8B, Q2, Q5, Q6, Q12, mapping, Step 9) | rev L478, L499, L502-503, L509, L566, L578, L585 | yes | none |
| #22-#24 (Section B claim 4, 4A row 12, 7A, 8E) | rev L632, L732, L854, L860, L864, L926 | yes | none |
| #25-#27 (Section C, verdict paragraph, monitorable M1) | rev L955-973, L983 | yes | none |
| #28-#31 (brief) | rev L1006, L1010-1029, L1048-1065, L1099 | yes | none |
| #32 (YAML) | rev L1152, L1166, L1169, L1176, L1192, L1213-1219, L1227 | yes | none |

Unlisted changes found: none. These sections match loop 0 word for word:
- the header (items 1-6), 0A-0E, all cells of 1-C and its derived table, 1-S except the FY26 (OI+FI)/PBT cell, and 1-SC;
- 2-C and 2-S except the margin rows and the core-PBT verdict; 2-IG; diagnostics 1 and 4-6;
- the Step 3 table and its one-off, run-rate and Q3-base bullets; the Step 4 table except the margin label; Step 4 answers 2-4; the SA bridge;
- the 5-C rows not logged; 5-S except the new row; the Step 5 mandatory questions; 5.5; 6A-6D; 6.5; Step 7 except the cash-multiplier row; 8A, 8B items 2-5 and 8C;
- Q1, Q3, Q4, Q7-Q11 and Q13-Q26; the top-3 and channel lines;
- Section B except the logged rows;
- monitorables M2-M18; brief sections 2 and 4; brief section 5 rows 1-8;
- YAML items not logged.

New-error test across locations:
- The 5-C row "Lease-adjusted CFO ... Improving" (rev L321) stays true. Pre-WC lease-adjusted CFO also rose, from 212.21 to 311.61 (+99.40). The ex-float fall comes from capex (+156.08), as rev L327 states. It does not contradict the "DETERIORATING ex-float" direction.
- Watch item 3, "GREEN ... Q3 rent-free expiry pending" (rev L422), is consistent with the M3 graft.

---

## C. DELIVERABLE-COMPLETENESS AUDIT (hard gate): PASS

| Brief part | Location | Status | Note |
|---|---|---|---|
| 1. Summary narrative | rev L1008-1029 | present | 20 lines (within 10-20); provenance-tagged; carries the M1, M2 and F1 grafts and the associate strip |
| 2. Sector intelligence | rev L1031-1043 | present | flex share, GCC share, lease-length shift, wage and tariff costs, Labour Codes, campus moves |
| 3. Business-model intelligence | rev L1045-1065 | present | lessee model, cash rent with the rent-free qualifier and per-sq-ft test, deposit float, managed-office mix, pricing |
| 4. Competition intelligence | rev L1067-1082 | present | share claims (modelled), brand, Grade A, structural weak points; peer page not passed, stated |
| 5. Forward map | rev L1084-1099 | present | make-or-break reading plus 9 catalysts, each with a bull and a bear fork; 7 dated, 1 per call, 1 NOT FOUND |

All five parts are present and non-empty.

---

## D. COVERAGE AUDIT: PASS (no orphan rows, nothing missing from the ledgers)

Fresh pass: I grepped each A1 fulltext again. Structured row IDs were counted with the pattern `^\|?\s*R\d{3,4}\b`. A1 and A2 were not re-run in loop 1, and every ledger count-test header still matches loop 0.

| Document | Category | A2 count | Fresh count (A5) | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | pages ([page N]) | 12 | 12 | - | PASS |
| Results | numbered notes, SA + CA | 21 | 21: SA 1) L194, 2) L250, 3-10 L316-355; CA 1) L535, 2) L598, 3 L666, 4 L671, unnumbered 5 L676, 6-11 L683-704 | 0 | PASS |
| Results | agenda items | 2 | 2 (L52, L60) | 0 | PASS |
| Results | auditor paragraphs | 10 | 10 (L101, L107, L115, L126; L387, L394, L402, L415, L433, L442) | 0 | PASS |
| Results | consolidation entities | 4 | 4 (L419-424) | 0 | PASS |
| Results | financial line items | 232 | 232: carried from the loop-0 line-by-line count. The fulltext is unchanged, and ledger line 6 still reads 232 | 0 | PASS |
| Results | structured row IDs | 1,112 | 1,112 | 0 | PASS |
| Concall | 10-minute time blocks | 7 | 7 (L21, L142, L244, L401, L590, L742, L894; L17 is the block map) | - | PASS |
| Concall | analyst hand-offs / analysts | 8 | 8 (L245, L403, L521, L682, L738, L845, L895, L919) | 0 | PASS |
| Concall | analyst questions | 19 | 19: the loop-0 line list holds. The fulltext is unchanged; the first block (L246-254) and the last block (L921-940) were re-read | 0 | PASS |
| Concall | speaker turns | 56 | 56: the ASR carries no speaker tags (concall L18), so turns are a hand count under A2's convention, unchanged since loop 0 | 0 | PASS |
| Concall | structured row IDs | 470 | 470 | 0 | PASS |
| Deck | slides | 40 | 40 | 0 | PASS |
| Deck | structured row IDs | 1,392 | 1,392 | 0 | PASS |
| Letter | pages | 31 | 31 | 0 | PASS (MFS-1 now named at rev L33) |
| Letter | structured row IDs | 1,570 | 1,570 | 0 | PASS |
| Press | pages | 5 | 5 | 0 | PASS |
| Press | structured row IDs | 197 | 197 | 0 | PASS |
| A4 vs ledgers | units reviewed | 21 notes / 56 turns / 76 slides | 0D covers all 21 notes (rev L67-81); 4A covers all 19 questions (rev L719-739); "Unreviewed ledger rows: none" (rev L31) | 0 | PASS |
| A4 vs A3 | finding IDs mapped | 83 FS/AMB + 2 CN | 83 + 2 mapped: results 16, deck 17, letter 17, press 10, concall 23 (rev L536-578, L580) | 0 | PASS |

orphan_rows: none. missing_from_ledger: none.

---

## E. ARITHMETIC AUDIT: PASS (no mismatch above rounding)

Scope: I recomputed every number that loop 1 added or changed from raw lines (results in Rs Mn x 0.1). Cells that loop 1 did not change are identical to loop 0 (Section B), and all of them passed in the loop-0 audit. Spot re-checks: CA Op EBITDA Q2 FY27 = 195.82 + 3,142.49 + 1,749.13 - 110.98 - 75.03 = 4,901.43 Mn = 490.14 (results L487-499). SA Op EBITDA = 489.86 (Q2 FY27) and 380.70 (Q2 FY26) (results L159-170).

| Metric | A4 value | Recomputed (A5) | Source line | Status |
|---|---|---|---|---|
| CA Op EBITDA margin change YoY | -230 bps | 63.834% - 66.135% = -230.2 bps | results L486-499 | PASS |
| SA Op EBITDA margin change YoY | -243 bps | 64.009% - 66.436% = -242.7 bps | results L158-170 | PASS |
| SA (OI+FI)/PBT FY26 | 99.3% | (135.37 + 361.67) / 500.44 = 99.32% | results L159, L160, L172 | PASS |
| Rent-adjusted margin change YoY | +183 bps | 186.14/767.84 = 24.243% vs 128.78/574.70 = 22.408%; +183.4 bps | deck L794, L797; results L486 | PASS |
| PAT-bridge margin label | -2.30 pp | -2.302 pp | derived | PASS |
| Ind AS-only revenue adjustment swing YoY / QoQ | +5.0 / +4.8 Cr | 1.3 - (-3.7) = 5.0; 1.3 - (-3.5) = 4.8 | letter L662; deck L704-706 | PASS |
| Billed revenue growth YoY | 32.5% | 766.5 / 578.4 - 1 = 32.52% | deck L526-537; letter L662 | PASS |
| Billed core PBT ex OI, FI: Q2 FY27 / Q2 FY26 / Q1 FY27 | (0.32) / (0.63) / (17.45) | 0.98 - 1.3; -4.33 + 3.7; -20.95 + 3.5 | results L486-499; letter L662 | PASS |
| Share of PBT rise outside billed operating profit | 12.76 of 14.21 (90%) | 7.76 + 5.0 = 12.76; 12.76 / 14.21 = 89.8% | results L487, L488, L503 | PASS |
| H1 billed core PBT | (22.18) to (17.76); +4.42 vs +8.52 | -28.48 + 6.3; -19.96 + 2.2; 4.42; 28.48 - 19.96 = 8.52 | letter L723; results L487-499 | PASS |
| Adjustment as share of Q2 revenue | 0.17% | 1.3 / 767.84 = 0.169% | letter L662 | PASS |
| Recurring core on billed revenue; swing share | ~+0.3 Cr; ~94% | 5.30 - 5.0 = 0.30; 5.0 / 5.30 = 94.3% | derived | PASS |
| Section C core swing | +5.31 Cr | 0.98 - (-4.33) = 5.31 | results L499 | PASS |
| Net ROU additions H1 | ~347.5 | (90.81) + 438.3 = 347.49 | results L542; letter L735 | PASS |
| Net new lease liabilities H1 | ~291.5 | 15.59 + 275.86 = 291.45 | results L575, L583, L643 | PASS |
| CA FCF after lease cash, capex, ROU, ex WC | (63.44) / (130.53); (67.09) | H1 FY26: 728.81 - 20.80 - 495.80 - 207.69 - 67.95 = (63.43). H1 FY27: 938.96 - 39.34 - 588.01 - 363.77 - 78.37 = (130.53) | results L615, L626, L629, L631, L643-644 | PASS (rounding) |
| Capex change / pre-WC lease-adjusted CFO change | +156.08 / +99.41 | 363.77 - 207.69 = 156.08; 311.61 - 212.21 = 99.40 | results L615, L626, L629, L643-644 | PASS (rounding) |
| Pre-WC lease-adjusted CFO / rent-adjusted Op EBITDA | 96.4% / 91.6%; -4.8 pp | 212.21 / 220.04 = 96.44%; 311.61 / 340.11 = 91.62% | results L615, L626, L643-644; rev L132 | PASS |
| WC change CA | (10.08) / +126.54 | 7,187.23 - 7,288.06; 10,655.03 - 9,389.64 | results L615, L625 | PASS |
| SA FCF ex WC | (63.25) / (131.46); (68.21) | 728.40 - 20.58 - 495.80 - 207.31 - 67.95 = (63.25); 937.90 - 39.00 - 588.01 - 363.98 - 78.37 = (131.46) | results L267, L277, L280, L282, L293-294 | PASS |
| Cash rent (A) YoY; area YoY; per sq ft | +21.4%; +27.1%; about -4.5% | 298.2 / 245.6 = +21.42%; deck +27.1%; 1.2142 / 1.271 - 1 = -4.47% | deck L795, L310 | PASS |
| City desk growth YoY | Hyd +94.1, Chennai +133.7, Bengaluru +7.9, Mumbai +5.3 | identical | deck L404-408 | PASS |
| Company FCFF and exclusion | 16.0; 20.0 (11.4 + 8.6); full basis (3.99) | see F1 row, Section A | deck L660-667, L796; results L627-644 | PASS |
| Brief core pretax ex OI, FI and associate | ~1.0 Cr | 20.45 - 18.60 - 0.87 = 0.98 | results L487, L488, L500, L503 | PASS |
| Brief WC swing; FCF (4.0) / (73.5); ex-WC (63.4) / (130.5) | 136.6 etc. | 136.62; (3.99) / (73.52); (63.44) / (130.53) | results L615-644 | PASS |
| ROU and lease-liability balances | 4,593.90 / 4,503.09; 5,217.53 / 5,233.12 | identical | results L542, L575, L583 | PASS |
| Occupancy fall from March | 320 bps | 86.9 - 83.7 | deck L314; letter (L-F16-b) | PASS |

Arithmetic verdict: no mismatch above rounding.

---

## F. ADVERSARIAL READ: three most positive claims in the loop-1 review

Acquisition-economics probe: NOT TRIGGERED. A grep of all five fulltexts for acqui/stake/consideration/share purchase/takeover/amalgamat returns only two kinds of line: the PPE cash-flow line "Acquisition of property, plant and equipment" (results L280, L629; letter L1080, L1511, L1723, L1852; deck L933) and the auditor phrase "consideration of the review reports" (results L434; letter L1244). No document describes a business purchase or a stake buy, so no purchase multiple exists to test.

The loop-0 claims (core profit turning positive, FCF improving, cash-rent leverage) now carry their grafted counters. The three most positive claims left in the review are these.

### Claim 1: volume is real on both bases
A4 text: "the volume story holds on both" (rev L967). Also "Volume is real on both bases (revenue +33.6% FILED; desks, members MGMT)" (rev L1227), and brief L1011-1012.

Strongest bear counter (same extract): the growth is bought capacity with weakening fill and flat price.
- Portfolio occupancy fell 114 bps QoQ and 320 bps from March (deck L314, L316).
- Growth-centre occupancy was flat at 64.9% to 64.8% (deck L509).
- Members grew 7.3% QoQ against desks at 8.8% (deck L309, L316).
- Core revenue per member fell 0.7% YoY (deck L500-503, L528).
- Renewal escalation runs below contracted escalation (concall L546-548).
- Billed revenue growth is 32.5%, not 33.6% (deck L537).

Survives: the counter is supported, but it does not defeat the claim. Filed revenue grew 33.6%, or 32.5% on billed revenue. Each counter point already sits in the review: rev L253, L420, L670, L708, L1219-1220, L503 (Q6), L1025, L1064-1065. No graft is needed.

### Claim 2: core Ind AS profit is recovering QoQ, and the recovery holds on billed revenue
A4 text: "core PBT moved from (17.45) to (0.32) QoQ [derived], so the QoQ recovery holds on that basis ... core Ind AS profit RECOVERING from a dip QoQ" (rev L277).

Strongest bear counter: part of the +17.13 Cr billed-basis QoQ gain is customisation revenue. It was about 18 Cr in Q2 against about 12 Cr in Q1 (30 Cr in H1; concall L414-415), and "one or two large ones" are inside it (concall L419). Sub-contracting cost reappeared at 2.76 Cr in Q2 against nil in Q1 (results L491). Net of that cost, about 3.2 Cr of the QoQ gain is customisation [derived]. H1 lease-termination gains (results L613) also mean some centres were exited, which lowers Ind AS D&A and interest (Q10).

Survives: in part, and the claim stands. Excluding customisation, the QoQ recovery is still about 11-14 Cr. The review already limits the claim: it is flat YoY on billed revenue (rev L277), and Q2 is still below the H2 FY26 average (rev L279). Customisation lumpiness sits at Step 6.5 (rev L448) and Q17 (rev L514). Management also says the stream is now "normalized" and partly amortised (concall L413-414, L424-427). The only gap is a missing cross-reference at Step 3. Logged as STYLE N2; no loop.

### Claim 3: the operating spread improves on a cash-rent basis
A4 text: "On a cash-rent basis the operating margin improved" (rev L245). Also "operating spread improves on a cash-rent basis (rent-adjusted margin 24.2%, +183 bps YoY)" (rev L969), and watch item 3 GREEN "improving on both bases" (rev L422).

Strongest bear counter: the landlord rent-free timing (concall L723-730), with cash rent per operational sq ft down about 4.5%. The loop-0 graft put this into the review at rev L969, L1055-1060 and L1227, and watch item 3 carries "Q3 rent-free expiry pending".

Second counter, new this round: the rent-adjusted margin is built on Ind AS revenue and Ind AS Op EBITDA. It therefore carries the same undefined revenue-adjustment swing that the review grafted for claim 1 (letter L662). On billed revenue the figures are as follows [derived]:
- Q2 FY27: (490.14 - 1.3 - 304.0) / 766.5 = 24.11%.
- Q2 FY26: (380.08 + 3.7 - 251.3) / 578.4 = 22.90%.
- The change is +121 bps, not +183 bps. About 62 bps of the gain is the 5.0 Cr swing.

Survives: in part, and the direction holds. The margin still improves on billed revenue. The 5.0 Cr swing is already disclosed four times in the review (rev L252-255, L303, L955, L1018), and the two readings and the Q3 separating observation do not change. The finding adds no new fact and changes no stated number, conclusion or verdict. Logged as STYLE N1; no loop.

---

## G. VERDICT

**COMPLETE.** loop_back_to: "" (none).
- All six loop-0 loop items (F1, C1, C2, M1, M2, M3) are closed against the fulltext.
- All ten loop-0 style notes are closed.
- The drift check finds no unlisted change and no new error from a listed change.
- The brief gate, coverage and arithmetic pass.
- The adversarial read finds no FACTUAL, MISSING or CONTRADICTION item. Two partial counters are logged as STYLE.
- A4's protocol verdict of PROCEED WITH FLAGS (rev L971) is unaffected.

The review may proceed to the run's operator-approval Notion write gate.

---

## H. STYLE NOTES (logged, no loop)

- N1. Rent-adjusted margin (rev L245, L969, L1227): add the billed-revenue reading beside +183 bps. On billed revenue it is 22.90% to 24.11%, or +121 bps [derived; letter L662; deck L794]. About 62 bps of the Ind AS gain is the same 5.0 Cr revenue-adjustment swing. The direction holds.
- N2. Step 3 QoQ recovery (rev L277): cross-reference the customisation step. Customisation revenue was about 18 Cr in Q2 against about 12 Cr in Q1 (concall L414-415), and sub-contracting cost was 2.76 Cr in Q2 against nil (results L491). Together that is about 3.2 Cr of the 17.13 Cr billed-basis QoQ gain. Step 6.5 (rev L448) and Q17 (rev L514) already carry the lumpiness.
- N3. Brief section 3 (rev L1048) tags the Q2 cash rent of Rs 298.2 Cr "[MGMT, from filed cash flow]". The filing has only an H1 cash flow (results L643-644). The Q2 rent (A) figure is the deck's split (deck L795), and it ties to the filed lines only at H1 (576.6 + 11.4 = 588.0). Tag it "[MGMT, deck p33; ties to filed H1 lease cash]".

---

```yaml
stage: A5-adversary
company: "WEWORK"
quarter: "q2fy27"
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
  - {claim: "Core Ind AS profit recovering QoQ; recovery holds on billed revenue, (17.45) to (0.32) (rev L277)", counter: "About 6 Cr of the QoQ gain is a customisation-revenue step (18 Cr Q2 vs ~12 Cr Q1, 'one or two large ones'), with 2.76 Cr sub-contracting cost reappearing; net ~3.2 Cr of the 17.13 Cr billed-basis gain. Claim stands (~11-14 Cr ex customisation); lumpiness already at Step 6.5 and Q17; logged, no graft", source_line: "concall L414-419, L424-427; results L491; rev L448, L514", type: STYLE}
  - {claim: "Operating spread improves on a cash-rent basis, rent-adjusted margin 24.2%, +183 bps YoY (rev L245, L969)", counter: "The rent-adjusted margin sits on Ind AS revenue and Op EBITDA, so it carries the 5.0 Cr revenue-adjustment swing; on billed revenue it moves 22.90% to 24.11%, +121 bps. Direction holds; the rent-free timing counter is already grafted; logged, no graft", source_line: "letter L662; deck L794, L797; results L486-499", type: STYLE}
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "N1: rent-adjusted margin +183 bps (rev L245, L969, L1227) includes the 5.0 Cr Ind AS-only revenue-adjustment swing; billed basis +121 bps (24.11% vs 22.90%); direction unchanged"
    - "N2: Step 3 QoQ recovery (rev L277) could cross-reference the ~6 Cr QoQ customisation step (concall L414-415) and the 2.76 Cr sub-contracting cost (results L491), already carried at rev L448 and Q17"
    - "N3: brief L1048 tags Q2 cash rent 298.2 Cr 'from filed cash flow'; the filing is H1 only (results L643-644); the Q2 figure is the deck p33 split (deck L795)"
loop_back_to: ""
gap: ""
style_notes:
  - "N1 add billed-basis rent-adjusted margin change (+121 bps) beside +183 bps"
  - "N2 cross-reference customisation step at Step 3 QoQ recovery"
  - "N3 retag Q2 cash rent 298.2 Cr as deck p33 split (ties to filed H1)"
  - "Loop-0 S1-S10 all closed in loop 1"
analyst_note: "Re-audit, loop 1 of 1. All six loop-0 items are closed against the fulltext. FCFF now rebuilds on the deck p28 formula with a 20.0 Cr exclusion. Capacity sits at 30-Sep. Net ROU additions are about 347.5 Cr. The three counters M1-M3 are grafted where the claims are made. All ten loop-0 style notes are closed. The drift check found no unlisted change: all 32 change-log rows sit at their stated locations, and every other table and paragraph matches loop 0. Every new number recomputes from raw lines within rounding. Coverage counts are unchanged and match all five ledgers. The three most positive claims left (volume, QoQ core recovery, cash-rent spread) are already hedged where they are made. Two refinements are logged as STYLE only. The +183 bps rent-adjusted margin carries the same 5.0 Cr revenue-adjustment swing and is +121 bps on billed revenue, so the direction holds. About 3.2 Cr net of the QoQ core recovery is customisation, which Step 6.5 and Q17 already flag. Neither changes a number, a conclusion or the PROCEED WITH FLAGS verdict. No acquisition is described, so the probe did not trigger."
```
