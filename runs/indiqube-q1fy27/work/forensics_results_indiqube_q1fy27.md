# A3 FORENSIC NOTES — IndiQube Spaces Limited (INDIQUBE) — Q1FY27 — DOCTYPE: results

Source extract: `/home/user/inflection-pipeline/runs/indiqube-q1fy27/work/extract_results_indiqube_q1fy27.txt` (285 lines, 5 pages, OCR text layer).
Ledger reconciled: `/home/user/inflection-pipeline/runs/indiqube-q1fy27/work/ledger_results_indiqube_q1fy27.md` — all A2 rows (Tables A–I: 6 notes, 4 footnotes, 29 statement rows, 8 IPO-table rows, 1 agenda item, 4 auditor paras, 3 signature blocks, 1 entity) read verbatim at cited lines. **Ledger reconciled 100%.**

## SCOPE & DATA-QUALITY PREAMBLE (read before findings)
- **STANDALONE-only filing.** Single entity (IndiQube Spaces Limited), single reportable segment (Note 5, line 249), no subsidiaries / JVs / associates / "Group" / consolidation list anywhere in the 285-line extract. Consequence: **F2 (S-vs-C gap), F3 (shell entities), F4 (unaudited component contribution), F15 (entity-list diff) are structurally N.A.** and are marked so with basis, not scored PASS. **F16/F17 are N.A. by doctype** (results filing, no deck, no transcript).
- **OCR corruption on the financials page (page 4).** Garbled labels ("Total exnenses" L178, "Depreciaiion" L176, "Total exnense" L184, "comorchensive" L191, "comnrehcnsivc" L193) and mangled bracket/sign glyphs on the loss rows (L180 "(305.10]", L184 "1132.08", L185 "1226.52", L193 "1236.511"). **Digit values verified intact by column arithmetic cross-read** (Total income − Total expenses = Loss before tax; LBT − tax = LAT; LAT + OCI = Total comprehensive loss). All four key watch figures confirmed: Revenue from operations **4,226.85M** (L167), Loss before tax **(305.10)M** (L180), Loss after tax **(238.82)M** (L185), Basic/Diluted EPS **(1.13)** (L198-199). Sign integrity is inferred, not read clean; A4/A5 should re-verify against the filed PDF.
- **CENTRAL INTERPRETATION ISSUE — DO NOT RESOLVE (flagged for A4).** Statutory Ind AS results show a **LOSS** (PAT (238.82)M) while management framing / Notion thesis item #2 expects an IGAAP-equivalent **PROFIT**. The Ind AS 116 lease-accounting distortion (ROU depreciation 1,878.93M + lease-liability finance cost 1,272.19M = 3,151.12M of non-cash / financing charge against 4,226.85M revenue) is the driver. **No IGAAP bridge is present in this filing.** This report surfaces the hard forensic evidence of the distortion (F8: current tax positive despite book loss) but does NOT resolve profit-vs-loss — that is an A4 management question.
- **Prior-reference caveat.** PRIOR_EXTRACT_PATH = NONE (first pipeline run for INDIQUBE). The only comparator for F5 (auditor / EoM diff) is **Notion memory** (FY26 AR: Walker Chandiok & Co LLP, unmodified, 2 KAMs, CARO xiii RPT arm's-length, Note 42 audit-trail deficiencies). **This is memory, not a prior extract** — verbatim-diff was not possible and is flagged.

---

## FINDINGS TABLE

| id | check | ledger row ref | line | verbatim quote | classification | forward implication |
|----|-------|----------------|------|----------------|----------------|---------------------|
| A3-F6-01 | F6 | Table D (Note 4 IPO table) | 239 / 234-238 | "Total ... 6,044.59 ... 2,690.37 3,354.22" (L239); new objects "520.00", "550.00", "160.00", "640.00" all with Utilised "." (L234-238) | FORWARD-SIGNAL | Rs 3,354.22M (₹335.4 Cr) of ₹604.5 Cr net IPO proceeds unutilised at quarter-end (only 44.5% deployed); Rs 1,870M sits in FOUR newly-added objects at 0% utilisation. Deployment pace is the dateable commitment to track next quarter; item #234 "security deposit for new centers" (₹52 Cr) and #238 "strategic commercial real estate opportunities" (₹64 Cr) are the promoter-linked-recipient risk surface flagged in Notion pre-committed Q1 questions. |
| A3-F8-01 | F8 | Table C rows 182-185 | 180-185 | "-Current tax 81.62" (L182) against "Loss before tax ... (305.10]" (L180); "-Deferred tax (147.90)" (L183) | FORWARD-SIGNAL | **Current tax expense is POSITIVE (81.62M) while book result is a pre-tax LOSS (305.10M)** — hard evidence the Ind AS 116 distortion produces a book loss on a tax-profitable / cash-profitable base. Persistent deferred-tax CREDITS every period (Q1FY27 (147.90), Q4FY26 (99.94), Q1FY26 (170.80), FY26 (510.48)) = DTA build on lease-timing differences whose recoverability depends on future taxable profit. This is the objective anchor for the IGAAP-vs-IndAS bridge A4 must obtain. |
| A3-F10-01 | F10 | Table C rows 195, 198-199 | 195 / 198-199 | "Paid-up equity share capital ... 211.99 ... 182.58 ... 211.99" (L195); "b) Diluted (1.13) (1.07) (2.01) (5.28)" (L199) | AMBIGUOUS | Paid-up capital rose Rs 29.41M (182.58→211.99, Re.1 face = +29.41M shares) between Q1FY26 and post-IPO, but Note 4 discloses a fresh issue of only **27,432,636** shares — a ~1.98M-share (~Rs 1.98M) bridge gap unexplained in this filing (possible pre-IPO ESOP exercise / bonus / conversion). Separately, basic = diluted EPS in EVERY period is **mechanically forced in loss periods** (dilutive potential shares are anti-dilutive and excluded); the ledger inference "no dilutive instruments" (L199 flag) is therefore NOT evidenced — ESOPs/warrants could be masked. Both feed an A4 dilution question. |
| A3-F13-01 | F13 | Table B footnote ••; Table D | 241-243 / 230 | "the Board of Directors in their meeting held on 20 May 2026 approved seeking shareholders' approval by way of Postal ballot for change and variation in the objects of utilization of the IPO proceeds ... approved ... through postal ballot on 24 June 2026" | FORWARD-SIGNAL | Within ~11 months of the 30-Jul-2025 listing the company revised its IPO objects (special resolution passed 24-Jun-2026): "new centers" capex allocation cut nearly in half (4,626.49→2,756.49) and FOUR new objects (₹187 Cr) added, incl. "strategic commercial real estate opportunities" (₹64 Cr). A material redirection of primary-raise capital this early is a strategy-shift and capital-allocation-governance signal; A4 should probe rationale and any promoter/related-party destination. |

*No FINDING rows for F1, F5, F7, F9, F11, F14 (marked PASS with basis below). F2/F3/F4/F12/F15/F16/F17 marked N.A.*

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| # | Check | Status | One-line basis |
|---|-------|--------|----------------|
| F1 | Zero-value standing line items | **PASS** | No ZERO_STANDING P&L rows. Only nil-glyphs: PARTIAL_DASH on inventories Q1FY26 (L173) and BLANK_STANDING Other equity in quarter cols (L196) — both benign interim/template artifacts. Structural absence of Exceptional-items / Discontinued-ops / Profit-on-sale-of-investment lines reviewed (LINE_ITEM_TYPE_ABSENT): a clean P&L with no exceptional-item smoothing channel, not a concern. |
| F2 | Standalone vs consolidated decomposition | **N.A.** | Standalone-only filing; no consolidated statement exists to decompose (single entity, no subsidiaries/JVs). |
| F3 | Shell-entity detection | **N.A.** | No subsidiaries or consolidation cost lines to compare; standalone-only. |
| F4 | Unaudited contribution ratio | **N.A.** | No component/JV/associate auditors; auditor report has NO Other Matters para (Table F, L124 confirmed absent). Nothing rests on unreviewed numbers. |
| F5 | Going concern / EoM scope tracking | **PASS** | Auditor report carries NO Emphasis of Matter, NO Other Matters, NO going-concern language (Table F, all grep-confirmed absent). Opinion UNMODIFIED (Board letter L37; Para 4 L124-129). Auditor stable: Walker Chandiok & Co LLP, partner Lokesh Khemka, UDIN 26067878FTHRZP6916 (L134-143) — same firm as FY26 AR per Notion memory (satisfies checklist #4). No prior interim extract → verbatim-diff impossible; comparison basis is MEMORY, not a prior extract (flagged). FY26 AR's 2 KAMs + Note 42 audit-trail deficiency are AR/audit-level items not expected in an SRE 2410 limited review — carry to a Role 6 AR deep dive, not a Q1 finding. |
| F6 | Forward-commitment phrase mining (notes) | **FINDING** | A3-F6-01. Lexicon hits: "has completed the Initial Public Offering" (L218, completed), "were listed ... on 30 July 2025" (L222, completed), "Board of Directors ... approved seeking shareholders' approval" (L241, completed 24-Jun-2026), "was reallocated" (L247, completed), plus four new IPO objects at 0% utilisation = live undated deployment commitments. See Commitment Register. NB "commenced at 04:03 PM" (L34) is a "commenc" lexicon hit but is board-meeting timing boilerplate, not a commitment. |
| F7 | Hedge phrase mining | **PASS** | No hedge-lexicon hits ("no assurance" / "subject to" [as a hedge] / "evaluating" / "exploring" / "in discussions" / "endeavour") in the Notes. Note this is a short limited-review package with no MD&A / risk-factors section that would normally carry such language; absence is scope-driven, not necessarily reassuring. |
| F8 | Tax forensics | **FINDING** | A3-F8-01. ETR on loss: tax credit (66.28)/LBT (305.10) = 21.7%. Current tax POSITIVE (81.62) despite pre-tax book LOSS = Ind AS 116 distortion evidence. Deferred-tax persistent credits every period = DTA build / carryforward, future ETR step-up risk. No "tax adjustments relating to earlier years" line present (that sub-check clean). |
| F9 | OCI forensics | **PASS** | Re-measurement gain on DB plans Q1FY27 3.09 (L189) vs FY26 full-year 12.35 — ~25% of annual, normal quarterly run-rate. Net OCI Q1FY27 2.31 does NOT exceed full prior-year 9.24; no single-quarter swing signalling a discount-rate/plan-asset assumption change. |
| F10 | Share count and dilution | **FINDING** | A3-F10-01. Paid-up bridge 182.58→211.99 (+29.41M) exceeds disclosed fresh issue (27.43M shares) by ~1.98M — untraced in this doc. Basic=Diluted EPS is mechanically forced in loss periods, so "no dilutive instruments" cannot be inferred; possible masked ESOPs/warrants. |
| F11 | Reserves and net worth tie-out | **PASS** | Other equity 4,935.50 + Paid-up 211.99 = statutory net worth 5,147.49M at FY26 (₹514.75 Cr; ~₹24.3/share book value on 211.99M shares). Quarter-column Other equity blank = standard interim convention. NO third-party comparator (rating rationale / slide) in this extract to diff against; nothing to reconcile beyond the internal tie-out, which holds. |
| F12 | Segment forensics | **N.A.** | Single reportable segment per Ind AS 108 (Note 5, L249-250); no segment-wise asset/liability/revenue table exists or is required, so there is no segment trend to analyse. |
| F13 | Board outcome beyond the results | **FINDING** | A3-F13-01. Bare single-agenda-item, 13-minute meeting (04:03–04:16 PM, L34-35) with no AR approval / AGM notice / dividend / director term dates / capital-raising resolution. The forward-relevant board-adjacent action is the disclosed 20-May-2026 board approval + 24-Jun-2026 postal-ballot revision of IPO objects (footnote ••). |
| F14 | Note drafting inconsistencies | **PASS** | No substantive note-vs-letter mismatch: Note 1 "reviewed by the Statutory Auditors" (L209-210) is consistent with the SRE 2410 limited-review letter (no note claims "audit"). Entity name consistent across letter/statement/notes. Apparent anomalies (statement title L159 "STATEMENT OF FINANCIAL RESUHS" missing "Unaudited"; garbled labels) are OCR artifacts per A2 flags, not drafting defects; verify at source PDF. |
| F15 | Entity list diffs | **N.A.** | Standalone single entity; no consolidation list, and no prior-quarter entity list exists (first run) to diff. |
| F16 | Presentation-specific (dropped/reframed) | **N.A.** | Doctype = results filing; no investor presentation/deck in scope. |
| F17 | Concall-specific silence audit | **N.A.** | Doctype = results filing; no concall transcript in scope. (Absence-of-IGAAP-bridge and non-disclosure of the Innoprop RPT receivable are captured narratively below and routed to A4 rather than scored here.) |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|------------|--------------|----------|-------------|
| Complete IPO of 29,542,340 equity shares at ₹237 | Q2FY26 (quarter ended 30-Sep-2025) | Note 4, L218-221 | completed |
| List equity shares on NSE & BSE | 30 Jul 2025 | Note 4, L222 | completed |
| Obtain shareholder approval (postal ballot) to revise IPO objects | 24 Jun 2026 | Footnote ••, L241-243 | completed |
| Reallocate Rs 16.95M from "Repayment of borrowings" to "General corporate purposes" | done (as at 30 Jun 2026) | Footnote A, L245-248 | completed |
| Deploy remaining Rs 1,480.21M on new-centers capex (₹148 Cr of ₹275.6 Cr revised) | undated | Table D, L230 | underway (46% of revised object deployed) |
| Deploy Rs 520.00M — security deposit for new centers (NEW object) | undated (post 24-Jun-2026) | Table D, L234 | initiated (0% utilised) |
| Deploy Rs 550.00M — fit-out/interior in non-IndiQube properties (NEW object) | undated | Table D, L235-236 | initiated (0% utilised) |
| Deploy Rs 160.00M — renewable power infrastructure (NEW object) | undated | Table D, L237 | initiated (0% utilised) |
| Deploy Rs 640.00M — strategic commercial real estate opportunities (NEW object) | undated | Table D, L238 | initiated (0% utilised) |

---

## NOTES TO A4 (routing of forward-signal / ambiguous findings and open Notion questions)
- **A3-F6-01, A3-F8-01, A3-F13-01 → management questions (FORWARD-SIGNAL).** A3-F10-01 → dilution/share-count reconciliation question (AMBIGUOUS).
- **Central unresolved issue (route as the #1 A4 question):** obtain the IGAAP / Ind-AS-116-adjusted PAT bridge. Statutory Ind AS = LOSS (238.82)M; F8 shows current tax is positive (81.62)M, consistent with an underlying tax/cash profit. Notion checklist item #2 (IGAAP-adj PAT positive & growing) is the load-bearing gate and CANNOT be answered from this filing — it is absent.
- **Notion pre-committed Q1 questions status in this doc:** (a) Innoprop receivable ₹4→₹14Cr — NOT disclosed (no related-party note / balance sheet in this interim package); silence to carry. (b) Prior-auditor identity — not raised; Walker Chandiok & Co LLP is and (per memory) was the auditor. (c) IPO deployment plan & any promoter-linked recipient — partially addressed by Note 4 (₹335.4 Cr still unutilised; new "strategic CRE opportunities" object ₹64 Cr is the recipient-scrutiny surface).
- **Monitoring checklist reads from this filing:** #4 auditor unmodified & stable = SATISFIED (unmodified, same firm). #2 IGAAP PAT = UNRESOLVED (bridge absent). Items #1 (occupancy), #3 (RPT/new promoter entities), #5 (net debt ex-lease), #6 (VAS %) are NOT disclosed in this results-only package — deteriorating-metric silence to log per Role 5.

---

```yaml
stage: A3-forensics
company: "INDIQUBE"
quarter: "Q1FY27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/indiqube-q1fy27/work/forensics_results_indiqube_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: FINDING
  F14: PASS
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F6-01", check: "F6", line: "239/234-238", classification: "FORWARD-SIGNAL", implication: "Rs 3,354.22M (44.5% deployed) IPO proceeds unutilised; Rs 1,870M in four new objects at 0% - deployment pace + promoter-linked-recipient surface to track"}
  - {id: "A3-F8-01", check: "F8", line: "180-185", classification: "FORWARD-SIGNAL", implication: "Current tax POSITIVE 81.62M despite pre-tax book LOSS 305.10M = hard evidence of Ind AS 116 distortion; persistent deferred-tax credits = DTA build; anchors the IGAAP bridge A4 must obtain"}
  - {id: "A3-F10-01", check: "F10", line: "195/198-199", classification: "AMBIGUOUS", implication: "Paid-up bridge +29.41M vs disclosed 27.43M fresh-issue shares = ~1.98M untraced; basic=diluted EPS mechanically forced in loss periods so no-dilution inference unproven - possible masked ESOPs"}
  - {id: "A3-F13-01", check: "F13", line: "241-243", classification: "FORWARD-SIGNAL", implication: "IPO objects revised via 24-Jun-2026 postal ballot within ~11 months of listing; new-centers capex allocation halved, four new objects (Rs 1,870M) added incl strategic CRE - capital-allocation-governance signal"}
forward_signals: ["A3-F6-01", "A3-F8-01", "A3-F13-01"]
ambiguous: ["A3-F10-01"]
commitments:
  - {commitment: "Complete IPO of 29,542,340 shares at Rs 237", implied_date: "Q2FY26", ref: "Note 4 L218", status_word: "completed"}
  - {commitment: "List equity shares on NSE & BSE", implied_date: "2025-07-30", ref: "Note 4 L222", status_word: "completed"}
  - {commitment: "Postal-ballot approval to revise IPO objects", implied_date: "2026-06-24", ref: "Footnote L241-243", status_word: "completed"}
  - {commitment: "Reallocate Rs 16.95M to General corporate purposes", implied_date: "2026-06-30", ref: "Footnote A L245-248", status_word: "completed"}
  - {commitment: "Deploy Rs 1,480.21M remaining new-centers capex", implied_date: "undated", ref: "Table D L230", status_word: "underway"}
  - {commitment: "Deploy Rs 520.00M security deposit new centers (new object)", implied_date: "undated", ref: "Table D L234", status_word: "initiated"}
  - {commitment: "Deploy Rs 550.00M fit-out non-IndiQube properties (new object)", implied_date: "undated", ref: "Table D L235-236", status_word: "initiated"}
  - {commitment: "Deploy Rs 160.00M renewable power infra (new object)", implied_date: "undated", ref: "Table D L237", status_word: "initiated"}
  - {commitment: "Deploy Rs 640.00M strategic CRE opportunities (new object)", implied_date: "undated", ref: "Table D L238", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
