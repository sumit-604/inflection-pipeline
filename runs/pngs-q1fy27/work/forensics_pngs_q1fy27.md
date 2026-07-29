# A3 FORENSIC NOTES — PNGS Reva Diamond Jewellery Limited (PNGSREVA) — Q1 FY27 — doctype: results

Source A1 extract: `runs/pngs-q1fy27/work/extract_results_pngs_q1fy27.txt` (6 pages, standalone-only Reg 33 filing)
A2 ledger: `runs/pngs-q1fy27/work/ledger_results_pngs_q1fy27.md`
Ledger reconciliation: 24/24 value rows read at cited lines + 4 auditor paras + 7 notes + 4 IPO rows + 4 mgmt-comment items + 4 signature blocks + 1 agenda item + 1 entity = 100%.
Unit: INR Million (x0.1 = Rs Crore). No prior-quarter ledger (first `/run-quarterly` cycle) — verbatim diffs where no prior exists are marked N.A.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| FN1 | F6 | §5 IPO util Total / Stores | 273, 278 | "Funding expenditure towards setting-up of 15 New Stores ... 2,865.64 ... 404.88 ... 2,460.76" | FORWARD-SIGNAL | 81.5% of net IPO proceeds (Rs2,845.63M of Rs3,491.23M) undeployed; only 14.1% of the 15-store object and 1.3% of its marketing object spent. Multi-quarter store-rollout capex runway ahead; the FD-interest tailwind on parked proceeds erodes as cash deploys. Dated by prospectus schedule (undated in this note). |
| FN2 | F6 | §3b Other income (l.179) + §5 footnote | 179, 279 | "temporarily retained in fixed deposits" / Other income "55.76" | AMBIGUOUS | Other income Rs55.76M is 3.7x QoQ (15.22) and 19.4x YoY (2.87), 15.3% of PBT, largely FD interest on unutilised IPO cash — non-operating and transient. QoQ tripling on a broadly similar FD balance is unexplained. A4: confirm composition and run-rate; strip from underlying earnings quality. |
| FN3 | F7 | §4 Note 3 | 254 | "there is no single customer or customer group who accounts for more than 10% of the total revenue" | AMBIGUOUS | Concentration now stated <10% vs 10.77% single customer carried on file (monitoring #8). Revenue runs through a related-party channel (34 SIS stores with P.N. Gadgil & Sons). A4: which customer moved below 10%, and is related-party SIS revenue aggregated as one "customer group" for this test? |
| FN4 | F8 | §3b Earlier year taxes | 200 | "Earlier year taxes ... 0.28" | NEUTRAL-FACT | Non-zero prior-year tax adjustment (Rs0.28M) populated only in the Mar-31-2026 (Q4/FY26) columns; nil in Q1FY27 and Q1FY26. Immaterial. ETR ~25.24% in line with statutory 25.17%; deferred tax persistently small credits (~25bps shield). Per F8 rule, any non-zero earlier-year tax = logged finding. |
| FN5 | F14 | §8 signatories #3/#4 | 291, 352 | "Director" (l.291) vs "Chairman & Director" (l.352) | NEUTRAL-FACT | Same DIN 00616617 (Govind Gadgil) signs the Notes and Management Comments sections of one filing with two different designations. Also para-1 drops "Limited" from the entity name (l.83, "PNGS Reva Diamond Jewellery"); UDIN OCR-garbled (l.151). Individually immaterial drafting/governance data points; verify clean UDIN from source PDF/BSE annex if precision needed. |
| FN6 | MON-#7 / #2 / #3 (inventory) | §3b Changes in inventories | 184 | "Changes in inventories of finished goods (304.78)" | FORWARD-SIGNAL | Rs30.48 Cr finished-goods build in the quarter directly confirms the pre-results warning that a strong Q1 pulls forward diamond inventory = near-term CFO pressure. Feeds tripwires #2 (inventory turn <1.20x), #3 (cumulative CFO/PAT). No balance-sheet inventory or cash-flow statement in this quarterly filing — turn/CFO not computable here (silence). Grows the sole FY26 audit KAM (Existence of Inventories, Rs335.55 Cr), raising FY27 audit focus. |
| FN7 | MON-#6 (EBITDA margin) | §3b rows l.178,183-188 | 178, 184 | Revenue "1,179.73"; COGS build via "(304.78)" | AMBIGUOUS | Operating EBITDA Rs339.27M = ~28.8% margin (gross margin 35.5%), materially above the modeled green band of 19-22% (red <18%). A4: reconcile margin definition and mix sustainability; is the diamond-studded mix (l.318, Rs1,159.87M of Rs1,179.73M) structurally lifting margin or is this a favorable-mix quarter? |
| FN8 | MON-#10 (store cadence) | §6 mgmt comment item 3 | 338-340 | "34 SIS stores with P. N. Gadgil & Sons Limited and 3 exclusive brand stores (34 SIS ... and 2 exclusive brand stores as on March 31, 2026)" | FORWARD-SIGNAL | Net +1 exclusive brand store this quarter against an IPO-funded 15-store plan (only 14.1% of store capex utilised). Rollout cadence slow relative to plan; store-opening pace is the near-term catalyst to track. |

---

## CHECKLIST SCORECARD (all 17)

| # | Check | Status | Basis (one line) |
|---|-------|--------|------------------|
| F1 | Zero-value standing line items | PASS | Both ZERO_STANDING rows benign: "Earlier year taxes" (l.200) anticipates prior-year tax true-ups (populated Rs0.28M in FY26 cols only, see FN4); "Other equity" (l.219) is the standard FY-end-only balance-sheet disclosure under Reg 33. No exceptional-item / profit-on-sale-of-subsidiary / impairment / discontinued-ops template lines lurking. |
| F2 | Standalone vs consolidated decomposition | N.A. | Standalone-only filing; no consolidated statement, no subsidiaries/JV/associates. No S-vs-C gap to decompose. |
| F3 | Shell-entity detection | N.A. | No consolidated cost lines and no subsidiaries to compare; nothing to test for shells. |
| F4 | Unaudited contribution ratio | N.A. | Auditor report carries no Other Matters paragraph and no component-auditor / JV / associate reliance (ledger §2, l.73); no unaudited contribution exists. |
| F5 | Going concern / EoM scope tracking | PASS | Auditor conclusion (para 4, l.125-130) is unmodified: "nothing has come to our attention ... that it contains any material misstatement." No Emphasis of Matter, no Other Matters, no Going Concern paragraph (ledger §2, l.73). Consistent with the FY26 UNMODIFIED audit baseline; same firm MSKA & Associates LLP, FRN 105047W/W101187, same partner (Yewale, M.No.158877). No prior-quarter EoM to diff. |
| F6 | Forward-commitment phrase mining | FINDING | IPO objects still to be deployed = dateable rollout/capex commitments (FN1); "temporarily retained in fixed deposits" (l.279) FD-interest tailwind (FN2). "completed the Initial Public Offering" (l.261) = past milestone; "will be available on the Stock Exchanges" (l.334) = boilerplate. See Commitment Register. |
| F7 | Hedge phrase mining | FINDING | No lexicon hedge ("no assurance"/"subject to"/"evaluating") newly added on revenue lumpiness. But Note 3 (l.254) affirmatively states no single customer >10%, a reframe vs the 10.77% single customer on file (FN3) — surfaced under F7's customer-concentration scope. |
| F8 | Tax forensics | FINDING | ETR Q1FY27 25.24%, Q4FY26 25.51%, Q1FY26 24.37%, FY26 25.23% — all ~ statutory 25.17%, no shield anomaly. Deferred tax persistent small credits (0.92/0.99/1.01, l.199), ~25bps shield, immaterial. "Earlier year taxes" Rs0.28M non-zero (l.200) = logged per F8 rule (FN4). Advance tax Rs30.00M paid TY2026-27 (l.343). |
| F9 | OCI forensics | PASS | Re-measurement loss on defined benefit plans small and stable: Q1FY27 (0.16), Q4FY26 (0.39), Q1FY26 (0.41), FY26 (0.59) (l.208). Single-quarter swing (0.16) is below the full prior year (0.59); no assumption-change signal. |
| F10 | Share count and dilution | PASS | Paid-up rose 218.66 -> 316.98 (l.218) YoY, tracing cleanly to the FY26 IPO (Note 6, l.261); ~9.83M shares at Rs10 FV. Stable QoQ (316.98). Basic = Diluted EPS every period (8.58/8.58, l.222-223) = no dilutive instruments. No new dilution this quarter (tripwire #7 not tripped). |
| F11 | Reserves and net worth tie-out | PASS | Other equity 4,835.02 (l.219) + Paid-up 316.98 (l.218) = statutory net worth Rs5,152.00M = Rs515.2 Cr (FY26). Internally consistent; no third-party figure (rating rationale / slide) present in this filing to diff against, none required this cycle. |
| F12 | Segment forensics | N.A. | Note 3 (l.251-254): single reportable segment per Ind AS 108; no segment assets/liabilities table disclosed. Nothing to trend. |
| F13 | Board outcome beyond the results | PASS | Sole agenda item is approval of Q1 FY27 unaudited standalone results (l.25, 28-32). Assessed for others: no AR/Board's-Report/MD&A approval, no AGM notice, no record date, no dividend, no director appointment/re-appointment, no auditor change, no capital-raising enabling resolution (ledger §1, keyword sweep l.15-46). No Role 6 AR event or funding round foreshadowed by this filing. |
| F14 | Note drafting inconsistencies | FINDING | Govind Gadgil signs as "Director" (l.291) and "Chairman & Director" (l.352) in one filing; entity name loses "Limited" in auditor para 1 (l.83); UDIN OCR-garbled (l.151). Cumulative governance/data-quality data point (FN5). Note 1 "limited review ... unmodified conclusion" (l.243-244) is consistent with the auditor letter — no note-vs-letter contradiction. |
| F15 | Entity list diffs | N.A. | Single reporting entity, standalone; no consolidation list and no prior-quarter list to diff (first `/run-quarterly` cycle). |
| F16 | Presentation-specific (dropped/reframed) | N.A. | Doctype is results filing, not a presentation deck. |
| F17 | Concall-specific silence audit | N.A. | Doctype is results filing, not a transcript. Monitoring cross-reference performed in the section below (not a concall). |

Blank checks: none. GATE A3: pass (17/17 carry an explicit status).

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Set up 15 New Stores (IPO object; Rs2,865.64M) | per prospectus schedule (undated in note); 14.1% deployed (Rs404.88M) at 30-Jun-2026 | Note 6, l.273/278 | underway |
| Marketing/promotion for launch of 15 New Stores (brand "Reva"; Rs354.00M) | per prospectus schedule (undated); 1.3% deployed (Rs4.61M) | Note 6, l.274-275 | initiated |
| General corporate purposes (Rs271.59M) | ongoing; 86.9% deployed (Rs236.11M) | Note 6, l.277 | near-complete |
| Initial Public Offering | FY ended 31-Mar-2026 | Note 6, l.261 | completed |
| Q1 results to be posted on BSE/NSE/company website | on/after 29-Jul-2026 | Mgmt comment 2, l.334 | boilerplate |

---

## MONITORING CHECKLIST CROSS-REFERENCE (thesis state, for A4)

- #2 inventory turn (red <1.20x) / #3 cumulative CFO/PAT (red <-0.5x): NOT COMPUTABLE from this filing — no balance-sheet inventory, no cash-flow statement (quarterly P&L only). But the Rs30.48 Cr finished-goods build (l.184, FN6) confirms the pre-results warning of near-term cash pressure; direction is adverse. Confirmatory silence on the actual turn/CFO numbers.
- #4 ROCE (red <16%): not disclosed in filing; not computable (no capital-employed balance sheet).
- #5 / #10 promoter pledge: no pledge disclosure in this filing (no shareholding-pattern table present); silence, not confirmation. Promoter holding 63.09% not restated here.
- #6 EBITDA margin (green 19-22%, red <18%): ~28.8% operating (FN7) — above green band; AMBIGUOUS, flagged for A4.
- #7 equity dilution tripwire: not tripped this quarter; paid-up flat QoQ, Basic=Diluted (F10).
- #8 single customer >20% or undisclosed (10.77% on file): Note 3 (l.254) now states none >10% (FN3) — reframe vs prior; AMBIGUOUS, flagged.
- Store cadence: +1 EBO to 3, SIS flat at 34 (l.338-340, FN8); slow vs IPO-funded 15-store plan.
- Open question (identity of 10.77% customer): still unresolved; the affirmative "<10%" statement (FN3) sharpens the question rather than answering it.
- Open question (ITGC / audit-trail remediation): not addressed in this filing; silence (limited-review report carries no such matter, l.73).
- Revenue confirm: Rs1,179.73M = Rs117.97 Cr (l.178/320) matches the pre-results update (+119.49% YoY vs Rs53.75 Cr); CONFIRMATORY-NEGATIVE only insofar as the growth is inventory-financed (FN6).

---

## CLASSIFICATION ROLL-UP

- FORWARD-SIGNAL: FN1, FN6, FN8
- AMBIGUOUS (-> A4 management questions): FN2, FN3, FN7
- NEUTRAL-FACT: FN4, FN5
- CONFIRMATORY-NEGATIVE: revenue growth is inventory-financed (embedded in FN6)

```yaml
stage: A3-forensics
company: "PNGSREVA"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/pngs-q1fy27/work/forensics_pngs_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FN1", check: "F6", line: "273,278", classification: "FORWARD-SIGNAL", implication: "81.5% of net IPO proceeds (Rs2,845.63M) undeployed; 15-store rollout at 14.1% and its marketing at 1.3% - multi-quarter capex runway; FD-interest tailwind erodes as cash deploys"}
  - {id: "FN2", check: "F6", line: "179,279", classification: "AMBIGUOUS", implication: "Other income Rs55.76M (3.7x QoQ, 19x YoY, 15.3% of PBT) largely FD interest on parked IPO cash - transient, non-operating; QoQ tripling unexplained"}
  - {id: "FN3", check: "F7", line: "254", classification: "AMBIGUOUS", implication: "Note 3 states no customer >10% vs 10.77% single customer on file; related-party SIS channel (P.N. Gadgil & Sons); confirm which customer moved and whether related-party revenue is aggregated"}
  - {id: "FN4", check: "F8", line: "200", classification: "NEUTRAL-FACT", implication: "Earlier year taxes Rs0.28M non-zero in FY26/Q4 columns only; immaterial; ETR ~25.2% in line with statutory 25.17%"}
  - {id: "FN5", check: "F14", line: "291,352", classification: "NEUTRAL-FACT", implication: "Same DIN signs one filing as Director vs Chairman & Director; entity name drops Limited (l.83); UDIN OCR-garbled (l.151) - drafting/data-quality data points"}
  - {id: "FN6", check: "MON-inventory", line: "184", classification: "FORWARD-SIGNAL", implication: "Rs30.48 Cr finished-goods build confirms pre-results warning of near-term CFO pressure; feeds tripwires #2 turn and #3 CFO/PAT; grows the sole FY26 audit KAM (Existence of Inventories)"}
  - {id: "FN7", check: "MON-margin", line: "178,184", classification: "AMBIGUOUS", implication: "Operating EBITDA margin ~28.8% (GM 35.5%) materially above modeled green band 19-22%; reconcile definition/mix sustainability"}
  - {id: "FN8", check: "MON-store-cadence", line: "338-340", classification: "FORWARD-SIGNAL", implication: "Only +1 EBO added vs IPO-funded 15-store plan (14.1% store capex used); rollout cadence slow relative to plan"}
forward_signals: ["FN1", "FN6", "FN8"]
ambiguous: ["FN2", "FN3", "FN7"]
commitments:
  - {commitment: "Set up 15 New Stores (IPO object Rs2,865.64M)", implied_date: "per prospectus schedule (undated); 14.1% deployed at 30-Jun-2026", ref: "Note 6, l.273/278", status_word: "underway"}
  - {commitment: "Marketing/promotion for 15 New Stores (Rs354.00M)", implied_date: "per prospectus schedule (undated); 1.3% deployed", ref: "Note 6, l.274-275", status_word: "initiated"}
  - {commitment: "General corporate purposes (Rs271.59M)", implied_date: "ongoing; 86.9% deployed", ref: "Note 6, l.277", status_word: "near-complete"}
  - {commitment: "Initial Public Offering", implied_date: "FY ended 31-Mar-2026", ref: "Note 6, l.261", status_word: "completed"}
  - {commitment: "Q1 results posted on BSE/NSE/company website", implied_date: "on/after 29-Jul-2026", ref: "Mgmt comment 2, l.334", status_word: "boilerplate"}
gate_a3: pass
blank_checks: []
```
