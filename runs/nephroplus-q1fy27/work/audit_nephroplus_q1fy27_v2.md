# A5 ADVERSARY / COMPLETENESS AUDIT — NephroPlus (Nephrocare Health Services Ltd) — Q1 FY27 (v2, MERGED)

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Audit date: 12 August 2026
Review under audit: `/home/user/inflection-pipeline/runs/nephroplus-q1fy27/work/review_nephroplus_q1fy27_v2.md`
Independence: re-derived from the 5 A1 extracts + 5 A2 ledgers only. Did not defer to A4/A3 cites — every number below recomputed from the primary extract at its cited line.

## DOCUMENT-PROVENANCE RESOLUTION (checked FIRST, since the prior INCOMPLETE touched the AGM channel)

Two distinct source files exist; the merge handles the doctype mismatch correctly:
- `extract_concall_*.txt` → source `concall_transcript_nephroplus_q1fy27.txt`, a genuine 126-line IIFL-hosted Q1 FY27 earnings transcript. All "C l.X / turn Y" cites in Section B map cleanly to its inner source lines (spot-checked: l.58 = one-time RFID depreciation benefit; l.62 = "not giving any guidance on the loss assumptions"; l.117 = platform-only disclosure refusal; l.81 = "four clusters ... pack the bags and leave"). Role 5 is legitimately NOT N.A. — the transcript is real, not fabricated.
- `extract_agm_*.txt` → source `concall_nephroplus_q1fy27.pdf` (MISLABELED), whose A1 header carries a DOCTYPE_MISMATCH note; content is the Reg 30 "Proceedings of the 17th AGM" (ref SE/74, 12-Aug-2026). The review treats it as the AGM/Board-Outcome document and cites "AGM L…" to its inner source lines. No concall content is invented from this file. Provenance handled correctly.

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate) — PASS

| Brief part | Location | Present / Empty |
|---|---|---|
| (1) Summary narrative (10-20 lines) | §19.1 | PRESENT — ~25-line substantive narrative, numbers-first, anchored |
| (2) SECTOR intelligence | §19.2 | PRESENT — CKD driver, reimbursement dependence, organized-shift thesis, provenance-tagged |
| (3) BUSINESS-MODEL intelligence | §19.3 | PRESENT — asset-light BOO model, four cost levers, India-vs-intl margin structure, fixed-capacity note |
| (4) COMPETITION intelligence | §19.4 | PRESENT — #1 India/Asia, PH #2 of ~900, UZ sole private, Saudi binary-tender/Tibbiyah JV, Fresenius/DaVita |

All four present and non-placeholder. Gate cleared.

## 1. COVERAGE AUDIT (fresh independent enumeration vs A2 ledgers)

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results — notes | 21 | 21 (8 standalone + 11 consolidated numbered + 2 unnumbered EPS asterisk footnotes) | none | OK |
| Results — line items / entities / agenda / annexure / auditor paras / signatures | 67 / 26 / 10 / 10 / 11 / 5 | matched each | none | OK |
| Presentation — slides / disclosure units | 46 / 341 | 46 slides confirmed; DU sweep consistent (reported-EBITDA recon slide 9, ROCE 21.04% DU150, intl mix DU143, Tibbiyah JV DU182, BS/CF slides 42-44) | none (A1–A16 all incorporated) | OK |
| Press release — total rows | 44 | 7+8+3+19+3+1+2+1 = 44 | none | OK |
| Concall — participants / turns / questions / mgmt-number rows / forward-hedge | 17 / 103 / 36 / 81 / 18 | Re-traced turn table 1→103 against inner source lines 4–124; 17 participants; 36 topic rows; 18 forward/hedge. Matched. | none | OK |
| AGM — resolutions / directors present / in attendance / present-rows | 6 / 8 / 7 / 51 | 6 resolutions (L131-152); 8 directors (L61-72); 7 attendees (L76-87); quorum/timing/recusal/auditor/signatures/procedural reconcile | none | OK |

Coverage disposition: every ledger row is cited in A4 or dispositioned as reviewed-no-finding. Every concall/AGM FORWARD-SIGNAL and HEDGE row (18 concall forward rows; the AGM RESULT_PENDING / undisclosed-terms rows) maps to a Section-16 management question (Q14-Q25) or a Section-17 monitorable. No orphan row → no A3 loopback. My fresh pass found no row the ledgers lack → no A2 loopback.
Minor note (not a FAIL): the results ledger's TIGHT_SIGNATURE_TIMING flag on the two MD signatures was itself dispositioned by A2 as "not before conclusion, no breach" and never elevated to an A3 F-finding; A4's blanket "all reviewed" disposition is adequate.

## 2. ARITHMETIC AUDIT (recomputed from ₹ Millions ×0.1, consolidated unless noted)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Revenue YoY | +23.7% | (281.75−227.78)/227.78 = 23.69% | R L582 | OK |
| Operating EBITDA Q1FY27 (PBT_preJV+D+Fin−OI) | 63.88 | (445.96+245.40+22.06−74.59)/10 = 63.88 | R L595/589/588/583 | OK |
| Operating EBITDA Q1FY26 | 47.56 | 475.67/10 = 47.57 | R L595/589/588/583 | OK (0.01 rounding) |
| Op EBITDA YoY | +34.3% | 16.32/47.56 = 34.3% | — | OK |
| Op EBITDA margin | 22.7% / 20.9% (+180 bps) | 63.88/281.75=22.67%; 47.56/227.78=20.88% | — | OK |
| Reported EBITDA (inc OI) | 71.35 | 713.42/10 = 71.34 | R L595/589/588 | OK (0.01 rounding) |
| Effective tax rate Q1FY27 | 22.1% | 9.06/41.03 = 22.08% | R L604/599 | OK |
| ETR Q4FY26 / Q1FY26 / FY26 | 8.6% / 16.9% / 21.2% | 2.85/33.22=8.58%; 4.82/28.52=16.9%; 20.63/97.47=21.16% | R L604/599 | OK |
| PAT YoY | +34.9% | 8.27/23.70 = 34.9% | R L606 | OK |
| Reported PBT YoY | +43.9% | 12.51/28.52 = 43.86% | R L599 | OK |
| Core PBT ex-OI (after JV) YoY | +53.0% | (33.57−21.94)/21.94 = 53.0% | R L599/583 | OK |
| PAT bridge sum | +8.27 | +16.32 −5.02 +3.89 +0.88 −3.57 −4.24 = +8.26 | R L588-606 | OK (0.01 rounding) |
| EPS basic YoY | +13.1% | (3.19−2.82)/2.82 = 13.1% | R L626 | OK |
| Standalone rev / EBITDA / PAT YoY | +14.5% / +22.2% / +150.6% | 14.48%; 22.2%; 125.63/50.14−1 = 150.6% | R L262/283 | OK |
| International revenue mix | 44.9% | (906.29+321.34+36.12)/2817.54 = 44.85% | R L699-703 | OK |
| Subsidiary share of consol PAT (Q1FY27/Q4/Q1FY26) | 60.7 / 64.1 / 78.9% | 19.41/31.97; 19.48/30.37; 18.69/23.70 | R L283/606 | OK |
| Adj EBITDA / Adj PAT (spoken) | 65.1 (+31%) / 37 (+41.7%) | Press-release table L48/L51: 65.1 vs 49.8 = +30.7%; 36.8 vs 26.0 = +41.7% | PR L47-52 | OK (mgmt figures, correctly labelled non-GAAP) |
| Adj EBITDA-margin bps (F14.1) | +120 filed vs +125 spoken | 23.1−21.9 = 1.2pp = 120 bps; Prashant's "125" (C l.27) is the internal inconsistency | PR/P L310; C l.10/27 | OK — inconsistency correctly identified |
| Reported EBITDA recon (presentation) | 63.88 anchor | Slide 9: 65.1 −1.3 ESOP −0.0 Saudi = 63.9 | P DU055-059 | OK (cell-for-cell to filing) |
| **AGM board count (the corrected item)** | **8 directors, 4 independent = 50%** | **AGM L61-72: Vuppala (exec/promoter) + Sharma/Gupta/Thakur (3 nominee) + Sultania/Manchanda/Kumlien/Bakshi (4 independent) = 8; 4/8 = 50%** | **AGM L61-72** | **OK — correction verified** |
| Net cash Mar-26 (Notion correction) | ~₹403 Cr | (123.9+170.6+131.6) − (0.0+23.0) = 403.1; vs total assets 1,470.9 → "₹1,533 Cr" memory unreconcilable | P L1489-1497 | OK |
| Receivable days Mar-26 / CFO-PAT FY26 | ~116 / 3.03x | 316.9/998.8×365 = 115.8; 232.6/76.84 = 3.03x | P L1490/1517, R L606 | OK |
| Goodwill % net worth Mar-26 | 7.8% | 86.7/1,116.5 = 7.76% | P L1477/1472 | OK |

No mismatch above rounding. The scattered 0.01 differences are pure rounding of ₹-Millions-to-Crore conversions and are below materiality. AR days 121→101 and capex ₹44 Cr are spoken concall figures with no Q1 balance sheet to verify — the review correctly labels them UNVERIFIABLE / partial and does NOT relax the INDETERMINATE cash-conversion cap. No arithmetic FAIL → no A4 loopback.

**Verification of the corrected item:** The prior INCOMPLETE was on C3's AGM board composition. Re-derived independently from AGM L61-72: exactly 8 directors present — 1 executive/promoter (Vikram Vuppala), 3 nominee (Gaurav Sharma, Vishal Vijay Gupta, Sunil Kumar Thakur), 4 independent (Hemant Sultania, Om Prakash Manchanda, Annette Kumlien, Ajay Bakshi) = 50% independent. The correction in §C3 and §18 is CORRECT. (Note: the "7 in attendance" non-director list — Kamal Shah, Rohit Singh, Prashant Goenka, Kishore Kathri, Amit Bajaj, Vaibhav Dandawate, Rashida Adenwala — is a separate roster and is not conflated with the board count. Recusal on Items 5-6 with independent NRC chair Manchanda presiding is confirmed at AGM L123-127.)

## 3. ADVERSARIAL READ — three most positive claims, strongest bear counter, survival test

**Claim 1 — "Operating-led, clean quarter: revenue +23.7%, operating EBITDA +34.3%, margin +180 bps."**
Bear counter (same text): the newly-given medium-term guidance is 15-20% (C l.12), BELOW the 23.7% delivered; the RPT tailwind (~11% CAGR, +9.2% this Q) is lumpy and non-repeatable (PH +55-60% Oct-24; CGHS +35% after ~10-11 yrs), management itself said "one should not expect that same cagr number to continue forever" (C l.40); and part of the QoQ margin gain is a one-time RFID/near-zero-machine depreciation benefit that reverses (C l.58). Counter SURVIVES — but is already grafted (F6.8, F7.3, F1.1; Step 2 [v2 UPDATE], Q17/Q19). Not an unincorporated gap.

**Claim 2 — "Adjusted EBITDA 23.1% / adjusted PAT +41.7% — profitability strengthening."**
Bear counter (same text): every headline management spoke was ADJUSTED; reported EBITDA ₹63.88 Cr and reported PAT ₹31.97 Cr / +34.9% were never verbalised; the adjustment adds back the Saudi JV loss (₹3.6 Cr) and ESOP, and the "*" adjusted-EBITDA definition is inconsistent across documents (ESOP-only vs Saudi+ESOP). Counter SURVIVES — but already grafted (F16.1, PR-F14-1; Step 1c [v2 UPDATE], flags list, Q3/Q14). Not a gap.

**Claim 3 — "KSA growth trigger resolved favourably; no tripwire fired."**
Bear counter (same text): KSA is a binary government-tender market — "you win one of the four clusters ... If you don't win, you pack the bags and leave" (C l.81); first revenue is unquantified, the JV-loss run-rate was refused under ~5x questioning (C l.62/80), and the timeline is given three irreconcilable ways (couple of months / 3-4 quarters / one-to-two quarters or longer). Counter SURVIVES — but already grafted (F17.3, F6.5; Step 6D "ON TRACK but BINARY", §8C single cleanest metric, Q14/Q15). Not a gap.

Supplementary positives (AR days GREEN; 50%-independent-board "governance-positive") both carry their bear counters in-text: AR structurally high / cash still INDETERMINATE (Step 5); three undisclosed promoter-economics items + pending vote tallies (§C2, Q22-Q25). No surviving bear counter is absent from the review → nothing must be grafted → no A4 loopback on the adversarial axis.

## DISCIPLINE CHECKS
- INDETERMINATE cash conversion NOT silently relaxed: verdict explicitly capped at PROCEED WITH CAVEATS with the four missing-evidence items named (no Q1 CFS, no Q1 BS, capex not isolable, net cash/CCC not refreshed). OK.
- No exit PE / valuation / destination-multiple recomputed: Step 7 explicitly holds; only the price-gate observation (CMP ~₹644 vs entry ₹345-423). OK.
- Standalone AND consolidated both treated (Step 1a/1b, Step 2/2b). OK.
- Doctype-mismatch provenance handled without fabricating concall content (real transcript used for Role 5; mislabeled PDF used for AGM). OK.

## VERDICT

**COMPLETE.** The corrected §C3 AGM board composition is independently verified right (8 directors, 4 independent = 50%). A fresh full audit of the remaining review passes on all four axes: the plain-language brief carries all four parts; the coverage enumeration matches every A2 ledger with zero orphans; every derived metric recomputes within rounding from the primary extracts; and all three strongest bear counters are already incorporated. No loopback required.
