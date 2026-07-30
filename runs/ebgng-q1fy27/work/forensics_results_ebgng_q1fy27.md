# A3 FORENSIC NOTES — GNG Electronics Limited (EBGNG) — Q1 FY27 — DOCTYPE: results

Source extract: /home/user/inflection-pipeline/runs/ebgng-q1fy27/work/extract_results_ebgng_q1fy27.txt
Reconciliation contract: /home/user/inflection-pipeline/runs/ebgng-q1fy27/work/ledger_results_ebgng_q1fy27.md
Units: Rs Million as filed (x0.1 = Rs Cr). Column order every row: [Q1FY27 Jun-30-26 | Q4FY26 Mar-31-26 | Q1FY26 Jun-30-25 | FY26 audited].
Ledger reconciliation: 43/43 line-item rows read verbatim at cited lines + 10 notes + 12 auditor paras + 6 entities + 5 signature blocks = 100%.

DOCTYPE APPLICABILITY: results filing -> F1-F15 apply; F16, F17 = N.A.
STRUCTURAL CEILING: filing carries the P&L (statement of financial results) + two limited review reports ONLY. NO balance sheet, NO cash flow statement, NO segment asset/liability schedule. This caps F11, F12, and every working-capital / leverage / OCF read (mark what is NOT disclosed).

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F2 | Consol PAT row 15 / Standalone PAT row 15 | 636-640 (C) vs 274-278 (S) | consol PAT "289.30 / 421.48" vs standalone PAT "159.38 / 121.31" | AMBIGUOUS | Subsidiary PAT contribution swung from 247% of standalone PAT (Q4FY26) to 81.5% (Q1FY27); consol PAT fell -31% QoQ while standalone rose +31%. YoY the gap is stable (81.9%->81.5%), so the swing is Q4-balancing-figure seasonality, not clearly deterioration. A4 must ask whether overseas refurb profit is genuinely Q4-weighted or Q4 absorbs full-year true-ups. |
| FND-02 | F2 | Changes in inventory row 5 (S) & row 5 (C) | 220 (S) vs 582 (C) | standalone "(754.05)" vs consolidated "381.61" | FORWARD-SIGNAL | Sign divergence: parent (India) BUILT inventory ~754 M while the group DREW DOWN ~382 M (implied overseas + elimination drawdown ~1,136 M). Parent is stocking (component/memory supercycle build or pre-positioning stock for export to subs) while overseas subs sold through. Signals parent working-capital absorption and channel-stocking into next quarter. A4 question. |
| FND-03 | F2 (margin) | Revenue row 1 (C), Direct cost row 4 (C), Changes-inv row 5 (C) | 559-563, 576-580, 581-585 | revenue "4,124.61"; direct cost "2,726.46"; changes-inv "381.61" | NEUTRAL-FACT | Consolidated gross margin (Rev - [Direct cost + Changes in inv]) = 24.6% Q1FY27, vs 21.4% Q1FY26 and 20.1% FY26. The single most load-bearing thesis test — consolidated GM printing BELOW 17% — is DECISIVELY NOT triggered; margin EXPANDED. Confirmatory positive. Record explicitly for A4. |
| FND-04 | F4 | Auditor para 6 / subsidiary list | 474-480; 452-461 | "no law requiring audit of accounts for the entity, hence the figures are adopted by NBN Auditing of Accounts as provided by the management" | AMBIGUOUS | ~45% of consolidated PAT (Q1FY27 subsidiary contribution 129.92 M / 289.30 M; rising to ~71% in Q4FY26, ~70% FY26) rests on numbers NOT reviewed by the parent statutory auditor (Shankarlal Jain). Electronics Bazaar FZC is only limited-reviewed by component auditor NBN; the five US step-downs are UNAUDITED and management-furnished. Above 10% threshold -> FINDING. YoY level stable (45.0%->44.9%), so no separate YoY-jump finding. A4: request the FZC-vs-US-stepdown PAT split. |
| FND-05 | F8 | Total tax row 14 (C) vs (S); PBT row 11 | 630-634, 612-617 (C); 268-272, 250-255 (S) | consol total tax "68.11"; consol PBT "357.41"; consol current tax "63.71" | FORWARD-SIGNAL | Consolidated ETR = 19.1% Q1FY27 vs 25.17% statutory, and only 10.6% FY26 / 9.1% Q4FY26. Subsidiaries paid ~7.7 M tax (consol current tax 63.71 less standalone 56.00) on ~130 M subsidiary PAT = ~6% effective. The group's low tax rests on low-taxed foreign (UAE/US) earnings; consolidated ETR is RISING (10.6% -> 19.1%). UAE 9% corporate-tax regime (effective 2023) is a forward ETR step-up / margin headwind. A4 question. |
| FND-06 | F10 | EPS Diluted row 21 (S) & row 22 (C) vs Basic | 306-315 (S); 673-682 (C) | standalone "a) Basic ...1.06 ... b) Diluted ...1.12"; consol "Basic ...3.70 ... Diluted ...3.89" (FY26: 3.50/3.68 and 11.58/12.17) | AMBIGUOUS | Diluted EPS EXCEEDS Basic EPS in the Q4FY26 and FY26 columns on BOTH statements. Under Ind AS 33 diluted EPS can never exceed basic (anti-dilutive instruments are excluded). Implied diluted share count is SMALLER than basic — arithmetically impermissible. Q1FY27 and Q1FY26 columns are equal (no spread). Likely an IPO weighted-average / presentation error, but must be reconciled. A4 question; verify EPS computation at AR. |
| FND-07 | F10 | Paid-up equity capital row 19 (S) / row 20 (C) | 300-303 (S); 666-669 (C) | "228.02 / 228.02 / 194.27 / 228.02" | NEUTRAL-FACT | Paid-up rose 194.27 -> 228.02 (Rs 2 FV) between Q1FY26 and Q4FY26 = +16.875 M shares, tracing to the FY26 IPO fresh issue. No change Q4FY26->Q1FY27. Total ~114.01 M shares. Traces cleanly to a known corporate action; no unexplained capital movement. |
| FND-08 | F14 | Subsidiary list vs auditor para 6 | 458 vs 476-479 | list: "Electronic Bazaar B.V. - Stepdown subsidiary"; para 6: step-downs "incorporated in USA" | AMBIGUOUS | A "B.V." suffix denotes a Netherlands entity form, yet auditor para 6 describes all step-downs as USA-incorporated. Genuine source-level (not OCR) inconsistency -> jurisdiction of this entity is unclear, with tax/regulatory implications. Cumulative governance data point. A4: confirm the entity's true jurisdiction. |

Non-finding but recorded observations (NEUTRAL-FACT, no threshold breach): consolidated FX-translation OCI swung 299.06 (Q4FY26) -> 6.02 (Q1FY27) (lines 649-653) — expected multi-currency exposure, inflated Q4 comprehensive income; consolidated finance costs +30% YoY (106.56 -> 138.57, lines 591-595) roughly tracks revenue +32%, a leverage-rebuild proxy but unquantifiable without a balance sheet.

---

## CHECKLIST SCORECARD (all 17; PASS / FINDING / N.A.)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | PASS | Ledger zero_standing count = 0; no 0.00/dash/Nil row in either P&L. Absent template rows (NCI, exceptional items, share of associates — lines 99, 636) are structural non-presence, not zero-valued; consistent with wholly-owned subs, no associates/exceptionals this period. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | Subsidiary PAT contribution swung 247% -> 81.5% of standalone PAT QoQ (>5pp trigger) [FND-01]; inventory-sign divergence parent build vs group drawdown [FND-02]; consol GM 24.6% > 17% falsification line NOT breached [FND-03]. |
| F3 SHELL-ENTITY DETECTION | PASS | Subs are NOT shells: consol carries real incremental cost/revenue — employee benefits 318.60 vs standalone 146.37 (lines 586, 224), depreciation 32.80 vs 21.19 (596, 234), revenue 4,124.61 vs 2,297.56 (559, 197). Overseas refurb operations are the value-add. No going-concern EoM to reconcile. |
| F4 UNAUDITED CONTRIBUTION RATIO | FINDING | ~45% of consol PAT (rising to ~71% in Q4/FY) rests on component-auditor / management-furnished foreign numbers not reviewed by parent auditor; US step-downs unaudited [FND-04]. Above 10% threshold. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No going-concern paragraph and no Emphasis-of-Matter in either review report (unmodified conclusions, lines 135-142, 463-473). The only "Other Matters" (143-152, 490-498) is the standard Q4-balancing-figure qualifier. Per injected inputs, no prior-quarter extract exists to verbatim-diff; absence noted, not diffed from memory. |
| F6 FORWARD-COMMITMENT MINING | PASS | Notes 1-5 (standalone 316-333, consol 683-711) are boilerplate (Ind AS basis, single-segment, balancing-figure, reclassification). No lexicon hit that is a dateable business commitment. Non-substantive hits excluded: "commenced" = board-meeting start time (line 57); "arranging to publish...newspapers" = administrative (line 52). Commitment register empty. |
| F7 HEDGE PHRASE MINING | PASS | No lexicon hedge in notes. Only near-hit "subjected to limited review" (line 331) describes the Q4 balancing figure, not a business hedge on lumpiness/concentration. No pre-emptive legal cover added. |
| F8 TAX FORENSICS | FINDING | Consolidated ETR 19.1% Q1FY27 / 10.6% FY26 vs statutory 25.17%; subsidiary earnings taxed ~6%; ETR rising with UAE 9% regime as forward step-up risk [FND-05]. Deferred tax identical S vs C every period (4.40/(2.21)/0.42/(3.22), lines 263-267 = 625-629) -> foreign subs recognise zero deferred tax (noted). No "earlier years" tax-adjustment line present. |
| F9 OCI FORENSICS | PASS | Q1FY27 consol defined-benefit re-measurement (11.49) (lines 643-647) does NOT exceed full FY26 (43.23) -> no single-quarter swing exceeding prior year, no assumption-change trigger. FX-translation OCI volatility (299.06 -> 6.02, lines 649-653) is expected multi-currency exposure, recorded as neutral. |
| F10 SHARE COUNT & DILUTION | FINDING | Diluted EPS > Basic EPS in Q4FY26 and FY26 columns on both statements — impermissible under Ind AS 33 [FND-06]. Paid-up +16.875 M shares traces to FY26 IPO [FND-07]. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | Filing carries P&L only; no balance sheet, no Other Equity / reserves line. Only paid-up capital disclosed (228.02). Net-worth tie-out cannot be sourced from this document. |
| F12 SEGMENT FORENSICS | N.A. | Note 3 (lines 325-328, 695-698): single business segment (ICT Device), "no reportable business segments"; domestic + export "considered geographical segments" but NO geographical split figures and NO segment asset/liability schedule disclosed (no balance sheet). Nothing to trend. Open item for A4: request domestic-vs-export revenue split (bears on monitorable #5 Ingram/Supertron and export mix). |
| F13 BOARD OUTCOME BEYOND RESULTS | PASS | Single-item, 9-minute board meeting (15:15-15:24 IST, line 57) approving ONLY the results + limited review reports (lines 42-50). No AR/AGM approval, no record date, no dividend, no director appointment/resignation, no auditor change, no capital-raising enabling resolution. Nothing schedules a Role 6 AR event this cycle. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | "Electronic Bazaar B.V." (Dutch form) listed among USA-incorporated step-downs [FND-08]. Note-vs-letter audit/review wording is consistent (both say limited review). OCR artifacts (Note "S" marker line 332; "F7C" line 475; "I-lectronic Bazar" line 460; consol para-5 numbering gap) are extraction-level, not source inconsistencies — excluded. |
| F15 ENTITY LIST DIFFS | N.A. | 6-entity consolidation list present (lines 452-461). Per injected inputs NO prior-quarter extract was supplied; additions/deletions/renames/relationship changes cannot be verbatim-diffed. Absence noted, not inferred from memory. Open item carried to A4. |
| F16 PRESENTATION-SPECIFIC | N.A. | Not a presentation. |
| F17 CONCALL SILENCE AUDIT | N.A. | Not a concall/transcript. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|---|---|---|---|
| (none) | — | Notes 1-5, both statements (316-333, 683-711) are boilerplate; no dateable management commitment | — |

Non-substantive lexicon hits logged and excluded: "commenced" (board meeting start, line 57); "arranging to publish these results in the newspapers" (line 52, administrative Reg 47 compliance). Neither is a business milestone.

---

## MONITORING CHECKLIST — WHAT THIS FILING DOES / DOES NOT LET US TEST

| # | Monitorable | Testable here? | Read this quarter |
|---|---|---|---|
| 1 | OCF positive after 2 negative years | NO | No cash flow statement in filing. |
| 2 | Working capital / debtor days | NO | No balance sheet. (Parent inventory build [FND-02] is a directional WC-absorption hint only.) |
| 3 | Gross margin <17% kill line | YES | Consolidated GM 24.6% Q1FY27 (from 21.4% YoY / 20.1% FY26). Falsification NOT triggered; margin expanded [FND-03]. |
| 4 | WCL operating-vs-financing classification | NO | No cash flow statement. |
| 5 | Ingram Micro / Supertron distributor revenue | NO | No customer or geography revenue disclosed (single segment, Note 3). |
| 6 | FY27 guide delivery (~25% rev, ~50 bps margin) | PARTIAL | Consol revenue +32.1% YoY (3,122.79->4,124.61) beats ~25% guide; consol EBITDA margin ~12.0% vs ~10.3% YoY (+~170 bps) beats +50 bps guide. QoQ decline off Q4 is the seasonal balancing quarter. |
| 7 | KKOC governance / Rs 305 M tax demand | NO | No related-party or litigation/contingency note in this P&L-only filing. |
| 8 | Net debt / leverage >1.5x | NO | No balance sheet. Consol finance costs +30% YoY (106.56->138.57) is a re-leveraging proxy only, unquantifiable. |

---

## GATE A3

All 17 checks marked (PASS 6 / FINDING 5 / N.A. 6). No blanks. GATE A3 = pass.

```yaml
stage: A3-forensics
company: "EBGNG"
quarter: "Q1 FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/ebgng-q1fy27/work/forensics_results_ebgng_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: N.A.
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FND-01", check: "F2", line: "636-640 / 274-278", classification: "AMBIGUOUS", implication: "Subsidiary PAT contribution swung 247%->81.5% of standalone PAT QoQ; consol PAT -31% while standalone +31%. Q4-balancing seasonality vs deterioration - ask A4."}
  - {id: "FND-02", check: "F2", line: "220 / 582", classification: "FORWARD-SIGNAL", implication: "Parent built inventory ~754M while group drew down ~382M; parent channel-stocking / WC absorption into next quarter."}
  - {id: "FND-03", check: "F2", line: "559-585", classification: "NEUTRAL-FACT", implication: "Consolidated GM 24.6% > 17% falsification line - decisively NOT breached; margin expanded. Confirmatory positive."}
  - {id: "FND-04", check: "F4", line: "474-480 / 452-461", classification: "AMBIGUOUS", implication: "~45% of consol PAT (up to ~71% in Q4/FY) rests on non-statutory-auditor numbers; US step-downs unaudited/management-furnished. Request FZC-vs-US split."}
  - {id: "FND-05", check: "F8", line: "630-634 / 612-617", classification: "FORWARD-SIGNAL", implication: "Consol ETR 19.1% (10.6% FY26) vs 25.17% statutory; subsidiary earnings taxed ~6%; rising ETR + UAE 9% regime = forward margin headwind."}
  - {id: "FND-06", check: "F10", line: "306-315 / 673-682", classification: "AMBIGUOUS", implication: "Diluted EPS exceeds Basic EPS in Q4FY26 & FY26 both statements - impermissible under Ind AS 33; reconcile EPS computation."}
  - {id: "FND-07", check: "F10", line: "300-303 / 666-669", classification: "NEUTRAL-FACT", implication: "Paid-up +16.875M shares traces cleanly to FY26 IPO fresh issue; no unexplained capital movement."}
  - {id: "FND-08", check: "F14", line: "458 / 476-479", classification: "AMBIGUOUS", implication: "Electronic Bazaar B.V. (Dutch form) listed among USA-incorporated step-downs; jurisdiction unclear, tax/regulatory implication."}
forward_signals: ["FND-02", "FND-05"]
ambiguous: ["FND-01", "FND-04", "FND-06", "FND-08"]
commitments: []
gate_a3: pass
blank_checks: []
```
