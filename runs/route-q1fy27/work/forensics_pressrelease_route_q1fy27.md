# A3 FORENSIC NOTES — Route Mobile Limited (ROUTE), Q1 FY27 — doctype: PRESS RELEASE (processed under PRESENTATION discipline)

Source A1 extract: `extract_pressrelease_route_q1fy27.txt` (3-page Regulation 30 press release, 113 lines, unit = Crores).
Source A2 ledger: `ledger_pressrelease_route_q1fy27.md` (8 tables; 33 numbered data points, 9 qualitative claims, 1 disclaimer, 2 signatory blocks).
Prior-quarter extract: NONE AVAILABLE — verbatim dropped-slide / EoM / entity diffs cannot be performed; flag `PRIOR_LEDGER_UNAVAILABLE` carried through F15/F16.

Ledger reconciliation: 100%. Every ledger row read verbatim at its cited line in the A1 extract before judging (Table 1 slides; Table 2 rows 1-33; Table 3 rows 1-9; Table 4 row 1; Table 5 rows 1-2; Tables 6-8 nil-content confirmations).

Doctype applicability (per task note): F16 applies; F6/F10 apply to numbers/phrases the release carries; F11 applies only if a reserves/net-worth figure is stated (it is not). Balance-sheet checks F2/F3/F4/F5/F8/F9/F11/F12/F13/F14/F15 are N.A. (no financial statements, no auditor report, no notes, no segments, no board resolutions in this document). F17 silence audit run against the supplied Notion monitoring checklist because the document is a management narrative and the checklist was supplied for that purpose.

---

## DERIVED FORENSIC MATH (from ledger rows, not stated in the release)

| Metric | Q1 FY27 | Q1 FY26 | Q4 FY26 | YoY | QoQ | Ledger rows |
|---|---|---|---|---|---|---|
| Revenue | 1,151.51 | 1,050.83 | 1,130.90 | +9.58% | +1.82% | 13,14,22 |
| PBT | 91.47 | 76.57 | 139.27 | +19.46% | **-34.32%** | 15,16,24 |
| PAT | 68.55 | 58.78 | 114.43 | +16.62% | **-40.09%** | 17,18,27 |
| PBT margin | 7.94% | 7.29% | 12.32% | +65 bps | **-438 bps** | 25 (only 7.94% stated) |
| Implied ETR | 25.06% | 23.23% | 17.84% | — | +722 bps | derived from 15-18,24,27 |

Notes: (i) PBT margin 7.94% is the ONLY margin stated (row 25); no gross margin, no EBITDA margin, and no prior-period margin comparator appear anywhere (`NO_PRIOR_MARGIN_COMPARATOR`). (ii) The QoQ PAT collapse (-40.1%) is amplified by a Q4 FY26 base that carried both a high PBT (139.27) and an abnormally low implied ETR (17.84% vs 25.17% statutory); Q1 FY27 ETR (25.06%) is normal. The release states none of this.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F6-01 | F6 | T3 r5, r7 | slide 2, ln 89-93 | "already being actively addressed through targeted actions to support margin recovery … With these initiatives already underway" | FORWARD-SIGNAL | Undated, unquantified management commitment to margin recovery. "underway" is a status word (lexicon hit). Feeds Role 5 promise-vs-delivery tracker: next quarter must show margin inflection or this becomes a broken promise. No milestone date, no named action, no quantum. |
| A3-F16-01 | F16 | T2 r9-10 vs r24,r27; r25 | slide 2, ln 58, 74-80, 88 | "Revenue … Rs. 1,151.51 crore, PAT … Rs. 68.55 crore" (banner) / "revenue growing year-on-year and quarter-on-quarter" | FORWARD-SIGNAL | Headline banner and CEO quote foreground the +1.82% QoQ revenue and favourable YoY, while the -34.3% QoQ PBT and -40.1% QoQ PAT are placed below the fold and never characterised. Framing choice = the profit deterioration is the story management is steering around. |
| A3-F16-02 | F16 | T2 r25 | slide 2, ln 78 | "The company's PBT margin stood at 7.94%." | AMBIGUOUS | Only PBT margin disclosed; the pre-committed Q1 FY27 gate metric — CONSOLIDATED GROSS MARGIN >=23% — is NOT disclosed, nor is EBITDA margin (thesis-broken trigger <10% 2Q). A single margin quoted with zero prior comparator prevents gate evaluation. A4 must ask for consolidated GM and adjusted EBITDA margin. |
| A3-F16-03 | F16 | T3 r5 | slide 2, ln 89-90 | "Profitability was affected by a combination of market-related factors" | AMBIGUOUS | The cause of a 438 bps QoQ PBT-margin compression is left unspecified (`UNSPECIFIED_MARKET_FACTORS`). Reframing an operational miss as external/"market-related" with no named factor is a softening. Direction uncertain -> A4 question. |
| A3-F17-01 | F17 | T3 r4-7 (silence) | slide 2, ln 82-94 | (no mention) — "expanding new customer relationships … accelerating the adoption of higher-value solutions" | CONFIRMATORY-NEGATIVE | Silence on every deteriorating monitored metric: consolidated GM (gate), adjusted EBITDA margin, CFO/PAT, DSO, New Products revenue YoY, Top-10 concentration, cash position. Management explicitly concedes margin pressure yet discloses no margin quality data. Sustained silence on a deteriorating metric = confirmatory negative per Role 5. |
| A3-F17-02 | F17 | T3 r6 (silence) | slide 2, ln 90-92 | (no mention of Truecaller BM or Heltar anywhere) | FORWARD-SIGNAL | Both this-quarter corporate actions — Truecaller BM partnership (2026-07-01) and Heltar acquisition (2026-07-13) — are absent. All three this-call watchpoints (Truecaller INR revenue; Truecaller wrapped into "New Products" vs separate; Truecaller pricing pass-through vs margin) are unanswered. Checklist items 13 (Truecaller KPI Rs 15+ Cr/qtr by Q2 FY27) and 14 (Heltar Rs 5+ Cr/qtr by Q2 FY27 + founders retained) start their silence clock. A4 to convert to management questions. |

Classifications used: FORWARD-SIGNAL = A3-F6-01, A3-F17-02. AMBIGUOUS = A3-F16-02, A3-F16-03. CONFIRMATORY-NEGATIVE = A3-F16-01 (framing of confirmed profit deterioration), A3-F17-01. All FORWARD-SIGNAL and AMBIGUOUS findings flagged for A4.

---

## CHECKLIST SCORECARD (all 17 — no blanks)

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | No financial table structure; Table 7 confirms no standing line items to test (narrative bullets only). |
| F2 Standalone vs consolidated | N.A. | Only consolidated headline figures shown; no standalone column. Balance-sheet decomposition not possible. |
| F3 Shell-entity detection | N.A. | No cost lines (materials/employee/depreciation) disclosed; cannot compare S vs C. |
| F4 Unaudited contribution ratio | N.A. | Press release, not audited financials; no auditor Other Matters paragraph. |
| F5 Going concern / EoM | N.A. | No auditor report / EoM paragraph in document; no prior ledger to diff. |
| F6 Forward-commitment phrase mining | FINDING | Lexicon hits "underway" (ln 92) and "already being actively addressed" (ln 89); margin-recovery commitment, undated/unquantified -> A3-F6-01. |
| F7 Hedge phrase mining | PASS | No F7-lexicon hedge added ("no assurance", "subject to", "evaluating", "in discussions", "endeavour" all absent). NOTE: absence of any safe-harbor disclaimer under forward-looking language (`NO_SAFE_HARBOR_DISCLAIMER`) is a drafting point, captured under F16 framing, not a hedge-addition. |
| F8 Tax forensics | N.A. | No tax line stated (doctype: N.A. unless figure stated). ETR derivable only (Q4 FY26 17.84% vs Q1 25.06%) — noted in Derived Math, not a standalone finding as no tax figure is disclosed. |
| F9 OCI forensics | N.A. | No OCI / actuarial disclosure in a press release. |
| F10 Share count & dilution | PASS | EPS basic Rs 9.94 = diluted Rs 9.94 (rows 19-20): zero spread, no dilutive instruments signalled. No paid-up capital figure to trace a corporate action; single period only. |
| F11 Reserves & net-worth tie-out | N.A. | No Other Equity / paid-up capital / net-worth figure stated in the release. |
| F12 Segment forensics | N.A. | No segment revenue/results/assets/liabilities disclosed. |
| F13 Board outcome beyond results | N.A. | No board resolution, AGM notice, record date, or director-term disclosure in this press release. |
| F14 Note drafting inconsistencies | N.A. | No notes and no auditor letter to cross-check. (Observation only: "Proximus Global Company" ln 60 / "part of Proximus Group" ln 103 / "Proximus Global" ln 107 used interchangeably — minor naming, not statement-level; no figure to reconcile.) |
| F15 Entity list diffs | N.A. | No consolidation entity list in document and no prior ledger; `PRIOR_LEDGER_UNAVAILABLE`. |
| F16 Dropped / reframed disclosures | FINDING | Headline foregrounds revenue/PAT and buries -34.3% QoQ PBT / -40.1% QoQ PAT; only PBT margin disclosed (gate metric consolidated GM absent); margin decline reframed as "market-related factors" -> A3-F16-01/02/03. Direct dropped-metric diff limited by absent prior ledger. |
| F17 Silence audit | FINDING | Against Notion checklist: silent on consolidated GM (gate), adj EBITDA margin, CFO/PAT, DSO, New Products revenue YoY, Top-10 concentration, cash, arbitration, Proximus holding, Truecaller BM KPI, Heltar integration, FY27 M&A pace -> A3-F17-01/02. Only item 12 (CEO continuity) is indirectly addressed (both CEOs quoted). |

Scorecard: PASS = 2 (F7, F10). FINDING = 3 (F6, F16, F17). N.A. = 12 (F1, F2, F3, F4, F5, F8, F9, F11, F12, F13, F14, F15). Total 17, no blanks. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Ref (line / claim) | Status word |
|---|---|---|---|---|
| 1 | Margin recovery via "targeted actions" | None stated | T3 r5, ln 89-90 | initiated ("being actively addressed") |
| 2 | Margin-recovery initiatives execution | None stated | T3 r7, ln 92 | underway ("already underway") |
| 3 | Improving operational efficiency | None stated | T3 r6, ln 90-91 | initiated (stated priority) |
| 4 | Rebuilding traffic with existing customers | None stated | T3 r6, ln 91 | initiated (stated priority) |
| 5 | Expanding new customer relationships | None stated | T3 r6, ln 91-92 | initiated (stated priority) |
| 6 | Accelerating adoption of higher-value solutions | None stated | T3 r6, ln 92 | initiated (stated priority) |
| 7 | "strengthen margins and deliver sustainable long-term growth" | None stated | T3 r7, ln 92-94 | confidence/guidance-like (no date) |

Every commitment is UNDATED and UNQUANTIFIED. None carries a milestone or KPI. Register is fully open for Role 5 promise-vs-delivery tracking at Q2 FY27; margin recovery (commitments 1-2, 7) is the load-bearing promise given the acknowledged margin pressure and the pre-committed GM gate.

---

## WHAT WAS NOT DISCUSSED (F17 detail vs Notion Section 8 checklist)

| Checklist item | Addressed? | Consecutive-Q silence (this cycle) | Note |
|---|---|---|---|
| 1 Gross Margin consol (GATE metric) | No | 1 (prior ledger unavailable) | Critical: pre-committed gate = consol GM >=23%; not disclosed. Gate UNVERIFIABLE. |
| 2 EBITDA Margin Adj (thesis-broken <10% 2Q) | No | 1 | Not disclosed despite conceded margin pressure. |
| 3 CFO/PAT trailing 4Q | No | 1 | No cash-flow data in release. |
| 4 DSO (Trade Recv/Rev x365) | No | 1 | No receivables data. |
| 5 New Products Revenue YoY (Trigger 3) | No | 1 | Watchpoint (b): whether Truecaller BM is inside "New Products" — unanswered. |
| 6 Top 10 Client Concentration | No | 1 | Narrative claims "customer engagement" but no concentration number. |
| 7 Loss of large enterprise clients | No | 1 | Claims "expanding new customer relationships"; no client-loss disclosure. |
| 8 Proximus Cross-Sell Revenue | No | 1 | No cross-sell figure. |
| 9 Rs 113 Cr Arbitration status | No | 1 | Not mentioned. |
| 10 Cash Position (net cash) | No | 1 | Not disclosed. |
| 11 Promoter/Proximus Holding | No | 1 | Not mentioned (Proximus affiliation described qualitatively only). |
| 12 CEO tenure / strategy continuity | Partial | 0 | Seckin Arikan (Chairman RML / CEO Proximus Global) and Tushar Agnihotri (CEO Route Mobile) both quoted — continuity intact. |
| 13 Truecaller BM revenue KPI (Rs 15+ Cr/qtr by Q2 FY27) | No | 1 (partnership 2026-07-01) | Watchpoint (a) INR revenue via Truecaller BM — silent. |
| 14 Heltar integration (Rs 5+ Cr/qtr by Q2 FY27 + founders) | No | 1 (BTA 2026-07-13) | Acquisition not mentioned at all. |
| 15 Aggregate FY27 M&A pace (<Rs 300 Cr) | No | 1 | Heltar consideration undisclosed; no M&A spend figure. |

Silence-clock caveat: consecutive-quarter counts default to 1 because no prior-quarter ledger was supplied; A4/A5 should confirm against the prior cycle before treating any single item as "sustained" silence. The aggregate pattern — margin pressure conceded but no margin-quality metric disclosed, and both fresh corporate actions omitted — is itself the confirmatory-negative signal.

---
```yaml
stage: A3-forensics
company: "ROUTE"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/route-q1fy27/work/forensics_pressrelease_route_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: PASS
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-F6-01", check: "F6", line: "slide 2, ln 89-93", classification: "FORWARD-SIGNAL", implication: "Undated unquantified margin-recovery commitment ('already underway'); feeds Role 5 promise-vs-delivery tracker."}
  - {id: "A3-F16-01", check: "F16", line: "slide 2, ln 58, 74-80, 88", classification: "CONFIRMATORY-NEGATIVE", implication: "Headline foregrounds +1.8% QoQ revenue; buries -34.3% QoQ PBT and -40.1% QoQ PAT, never characterised."}
  - {id: "A3-F16-02", check: "F16", line: "slide 2, ln 78", classification: "AMBIGUOUS", implication: "Only PBT margin 7.94% disclosed; pre-committed gate metric consolidated GM (>=23%) and EBITDA margin absent; gate unverifiable."}
  - {id: "A3-F16-03", check: "F16", line: "slide 2, ln 89-90", classification: "AMBIGUOUS", implication: "438 bps QoQ margin compression reframed as unspecified 'market-related factors'; softening -> A4 question."}
  - {id: "A3-F17-01", check: "F17", line: "slide 2, ln 82-94", classification: "CONFIRMATORY-NEGATIVE", implication: "Margin pressure conceded yet zero margin-quality metric disclosed (GM, EBITDA, CFO/PAT, DSO, concentration); sustained silence on deteriorating metric."}
  - {id: "A3-F17-02", check: "F17", line: "slide 2, ln 90-92", classification: "FORWARD-SIGNAL", implication: "Truecaller BM (2026-07-01) and Heltar (2026-07-13) both unmentioned; all three this-call Truecaller watchpoints unanswered; checklist items 13/14 silence clock starts."}
forward_signals: ["A3-F6-01", "A3-F17-02"]
ambiguous: ["A3-F16-02", "A3-F16-03"]
commitments:
  - {commitment: "Margin recovery via targeted actions", implied_date: "none stated", ref: "T3 r5, ln 89-90", status_word: "initiated"}
  - {commitment: "Margin-recovery initiatives execution", implied_date: "none stated", ref: "T3 r7, ln 92", status_word: "underway"}
  - {commitment: "Improving operational efficiency", implied_date: "none stated", ref: "T3 r6, ln 90-91", status_word: "initiated"}
  - {commitment: "Rebuilding traffic with existing customers", implied_date: "none stated", ref: "T3 r6, ln 91", status_word: "initiated"}
  - {commitment: "Expanding new customer relationships", implied_date: "none stated", ref: "T3 r6, ln 91-92", status_word: "initiated"}
  - {commitment: "Accelerating adoption of higher-value solutions", implied_date: "none stated", ref: "T3 r6, ln 92", status_word: "initiated"}
  - {commitment: "Strengthen margins and deliver sustainable long-term growth", implied_date: "none stated", ref: "T3 r7, ln 92-94", status_word: "confidence"}
gate_a3: pass
blank_checks: []
```
