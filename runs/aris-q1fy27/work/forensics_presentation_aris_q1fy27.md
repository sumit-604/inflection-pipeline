# A3 FORENSIC NOTES — ARIS (Arisinfra Solutions Ltd) — Q1 FY27 — INVESTOR PRESENTATION

Agent: A3 FORENSIC NOTES | Model: claude-opus-4-8
Inputs reconciled: extract_presentation_aris_q1fy27.txt (1,251 lines / 42 pages) and
ledger_presentation_aris_q1fy27.txt (Tables 1-4).
Ledger reconciliation: 100% — every row of Table 1 (42 slides), Table 2 (211 number
rows), Table 3 (70 line items), Table 4 (10 footnotes) read verbatim at its cited line.
Prior-quarter deck: NONE (first quarterly run) — cross-deck DROPPED_SLIDE / softened-
guidance / entity-list diffs are N.A.; only within-deck reframing is judged.

Doctype scope (per task): F16 applies, plus the F6/F10/F11 numbers the deck carries, plus
F7 (disclaimer) and F13 (board content) judged. F1-F5, F8, F9, F12, F14, F15 are N.A.
(results/balance-sheet-filing checks with no counterpart in an IR deck). F17 is N.A. (no
concall transcript).

--------------------------------------------------------------------------------
## FINDINGS TABLE
--------------------------------------------------------------------------------

| id | check | ledger row ref | slide / line | verbatim quote | classification | forward implication |
|----|-------|----------------|--------------|----------------|----------------|---------------------|
| F16-1 | F16 | T2 L1025/1030 vs L767, L786, L847 | slide 36 vs 26/27/29; lines 1025, 1030, 767, 786, 847 | "1,302 ... 1,774 ... 361" (sl.36 Q1-FY27) vs "1,092" (sl.26 B2B Q1-FY27) / "1,540" (sl.27 CM Q1-FY27) | AMBIGUOUS | Segmental revenue for the SAME quarter disagrees across slides; slide-36 Q1-FY27 bars sum to 3,353 Mn while slides 26/27/29 sum to 2,909 Mn = reported consolidated 2,908 Mn (L1048). Slide 36's period attribution is unreliable — A4 must force a reconciliation of the true Q1-FY27 split. |
| F16-2 | F16 | T2 L1035 (SEGMENT_AXIS_LABEL_ERROR) | slide 36; line 1035 | "Q1-FY26  Q3-FY26  Q1-FY27" (Services x-axis) vs "Q1-FY26  Q4-FY26  Q1-FY27" (B2B, CM) | AMBIGUOUS | Services chart mid-period reads "Q3-FY26" where the two adjacent charts read "Q4-FY26"; the 361 Mn bar's period is unknown. If it is Q4-FY26, Services revenue fell 361 -> 277 (-23% QoQ) even as GDV pipeline grew — a recognition-timing signal the mislabel obscures. |
| F16-3 | F16 | T1 slide 39 (NO_QTR_BALANCE_SHEET); T3 L1152, L1157 | slide 39; line 1127 | "PARTICULARS (INR MN) ... FY24  FY25  FY26" (no Q1-FY27 column) | FORWARD-SIGNAL | The one table with no current-quarter column is the balance sheet, so debtor days (Notion MASTER metric, Red >160) cannot be computed for Q1-FY27. From disclosed years debtor days run 168 (FY24) -> 155 (FY25) -> 140 (FY26), still near the Red line; the quarter that would show the trajectory is omitted. |
| F16-4 | F16 | T4 F1/F2 (FOOTNOTE_ASTERISK_MISMATCH); T2 L250, L254 | slide 9; lines 250, 254 | "Net Debt to Equity*" ... "All Figures as of Q1-FY27" (no asterisk) | AMBIGUOUS | Marker/footnote mismatch leaves the temporal basis of the 15-metric panel undefined. ROE 10.6% / ROCE 17.2% reconcile to Q1-FY27 annualized (PAT 200 x4 / equity 7,510 = 10.6%) yet carry no "annualized" label — one strong quarter annualized presented as a headline return. |
| F16-5 | F16 | T2 L1000, L1002-1003, L856-857 | slides 35 & 29; lines 1000, 1002, 857 | "GDV under execution increasing to INR 18,391 Mn ... providing strong revenue visibility"; "secured a INR 6,500 Mn Daas contract" | FORWARD-SIGNAL | Gross Development Value (third-party project value) is used as an ARIS revenue-visibility proxy; ARIS earns only "10-14% Fees on GDV" (L857). GDV 18,391 Mn implies ~1,840-2,575 Mn of eventual ARIS fees, not 18,391 Mn. Gross-vs-net conflation flagged per Notion. |
| F16-6 | F16 | T3 L1048, L1070, L1078 | slides 34 & 37; lines 1048, 1078 | "Revenue from Operations 2,908 ... (15.3)%" (QoQ); "Diluted EPS 2.05 ... (20.5)%" (QoQ) | FORWARD-SIGNAL | Sequential deterioration is real — revenue -15.3% QoQ, PAT -7.8% QoQ, EPS -20.5% QoQ — but slide 34 headlines only YoY (+37.1% / +292.2%). Selective framing understates the current-quarter momentum reversal. |
| F16-7 | F16 | T2 L824 | slide 28; line 824 | "increasing plant utilisation from ~20% to 70%+" | AMBIGUOUS | CM capacity utilisation (Notion watch, Red <55%) is given only as an aspirational range, never a current point value. Cannot verify whether ARIS partner plants are above or below the 55% red line this quarter. |
| F6-1 | F6 | T2 L1000; L864 | slide 35; lines 1000, 864 | "ArisUnitern secured a INR 6,500 Mn Daas contract from Wadhwa Group in Mumbai, strengthening its order pipeline" | FORWARD-SIGNAL | Dateable commitment: a secured DaaS mandate to convert over the "18-24 Months Execution Time" (L864). Feeds the Role 5 promise-vs-delivery tracker — watch for revenue conversion and whether 6,500 Mn is GDV or ARIS fee (F16-5 overlap). |
| F10-1 | F10 | T3 L1070, L1078, L1111, L1119 | slides 37 & 38; lines 1078, 1119 | "Diluted EPS (INR) 2.05 / 0.54 / 2.58" (Q); "(5.30) / 0.36 / 6.84 / 2.05" (annual) | AMBIGUOUS | Only DILUTED EPS shown (no basic EPS, no share count). Back-solved weighted shares are internally inconsistent: FY25 ~167M vs FY26 ~88M vs Q4-FY26 ~84M vs Q1-FY27 ~98M — EPS not on a bonus/split-adjusted comparable base post-IPO. QoQ EPS -20.5% vs PAT -7.8% implies a ~16% share-count rise QoQ. |

--------------------------------------------------------------------------------
## CHECKLIST SCORECARD (all 17)
--------------------------------------------------------------------------------

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING | N.A. | Results/BS-filing check; deck reproduces P&L/BS with 15 ZERO_STANDING dashes (Table 3) but no template/note context to judge transaction class — no counterpart in an IR deck. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Deck is consolidated-only (slides 37-40); no standalone columns to decompose the S-vs-C gap. |
| F3 SHELL-ENTITY DETECTION | N.A. | No entity-level cost lines standalone vs consolidated in a deck; cannot test for shells. |
| F4 UNAUDITED CONTRIBUTION | N.A. | No auditor Other Matters paragraph in a presentation; results are "Unaudited" per cover letter (L35) but no component-auditor split given. |
| F5 GOING CONCERN / EoM | N.A. | No going-concern / Emphasis-of-Matter language in a deck; no prior deck for a verbatim diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Substantive dateable commitment on slide 35 (secured 6,500 Mn Wadhwa DaaS, L1000); see Commitment Register. Lexicon hits otherwise administrative ("will be presented", L33). |
| F7 HEDGE PHRASE MINING | PASS | Only standard forward-looking-statement + Valorem boilerplate on slide 41 (L1206-1229: "no representation or warranty", "may cause ... to differ materially", "not necessarily indicative", "may not be all inclusive"). No newly-added targeted hedge on lumpiness or concentration. |
| F8 TAX FORENSICS | N.A. | Results-filing check; per task scope N.A. (ETR is back-computable — Q1-FY27 tax 67 / PBT 267 = 25.1%, ~in line with 25.17% — but no tax-note detail in a deck). |
| F9 OCI FORENSICS | N.A. | No actuarial/assumption disclosure in a deck; OCI shown only as a single line ((2) Mn Q1-FY27, L1074) with no components. |
| F10 SHARE COUNT & DILUTION | FINDING | Only diluted EPS carried; no basic EPS, no share count; implied weighted share counts internally inconsistent across periods; QoQ EPS drop outpaces PAT drop (F10-1). |
| F11 RESERVES / NET-WORTH TIE-OUT | PASS | Equity Share Capital + Other Equity + NCI ties to Total Equity exactly for all 3 disclosed years (FY26: 164+7,227+119 = 7,510; FY25: 117+2,195+46 = 2,358; FY24: 18+1,398+5 = 1,421). No external net-worth figure to reconcile; Q1-FY27 not tieable — deferred to F16-3. |
| F12 SEGMENT FORENSICS | N.A. | No segment assets/liabilities disclosed (only segment revenue); per task scope N.A. |
| F13 BOARD OUTCOME | N.A. | IR deck carries no board resolution / AGM notice / AR-approval / director-term-date content; slide 12 bios have no appointment or expiry dates. Cover letter only notes concall on Aug 06, 2026 (L34). |
| F14 NOTE-DRAFTING INCONSISTENCY | N.A. | No auditor letter vs note text to cross-check in a deck (results are unaudited/limited-review per L35); numeric-label inconsistencies captured under F16-1/F16-2 instead. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list in a deck and no prior-quarter deck to diff against. |
| F16 DROPPED / REFRAMED DISCLOSURES | FINDING | Seven items: segment-revenue non-reconciliation (F16-1), Services axis mislabel (F16-2), omitted Q1-FY27 balance sheet / debtor-days blind spot (F16-3), asterisk/temporal-basis mismatch + unlabeled annualized returns (F16-4), GDV gross-vs-net revenue-proxy (F16-5), YoY-only framing of a QoQ decline (F16-6), utilisation range not a point value (F16-7). |
| F17 CONCALL SILENCE AUDIT | N.A. | No concall transcript supplied (concall scheduled Aug 06, 2026); silence audit runs when the A1 transcript exists. |

Statuses: PASS 2 (F7, F11) | FINDING 3 (F6, F10, F16) | N.A. 12. No blanks — GATE A3 pass.

--------------------------------------------------------------------------------
## COMMITMENT REGISTER (F6 forward-commitment phrases on slides)
--------------------------------------------------------------------------------

| commitment | implied date | slide / line ref | status word |
|------------|--------------|------------------|-------------|
| ArisUnitern "secured a INR 6,500 Mn Daas contract from Wadhwa Group in Mumbai" | execute over "18-24 Months" (slide 29, L864) from Q1-FY27 | slide 35, line 1000 | secured |
| "the company announced its entry into the large-scale asphalt market" | "late 2025"; now live (asphalt rev 529 Mn Q1-FY27, L994) | slide 11, line 311 (+ slide 35 L994) | announced / commenced (confirmed) |
| "It is building a diversified network of trusted SME/MSME suppliers and manufacturers" | undated / ongoing | slide 26, line 750 | underway |
| "New Category Expansion: Expanding into tiles, CP fittings, sanitaryware, electricals, and plumbing" | undated strategy tile | slide 32, line 936-938 | intends to |
| "Scale Contract Manufacturing: Increase secured capacity through additional third-party plant tie-ups" | undated strategy tile | slide 32, line 944-947 | proposes to |
| "The network can handle 10x higher volumes on the same infrastructure" | undated capability claim | slide 32, line 921 | intends to (capacity claim) |
| "that will be presented during Earnings Conference Call ... scheduled on August 06, 2026" | Aug 06, 2026 | slide 1, line 33-34 | administrative (non-material) |

--------------------------------------------------------------------------------
## SUPPORTING FORENSIC ARITHMETIC (sweep, not interpretation)
--------------------------------------------------------------------------------
- Debtor days = Trade receivables / Revenue x 365: FY24 3,204/6,968 = 168d; FY25 3,270/7,677 = 155d; FY26 4,100/10,675 = 140d. No Q1-FY27 receivables disclosed (F16-3).
- NWC days reported (slide 40, L1189-1193): 120 / 110 / 66 / 56. Improvement (120->56) far outpaces debtor-day improvement (168->140) because Trade Payables ballooned 449 -> 701 -> 1,733 Mn (L1151) — headline NWC gain is partly payable-stretch, not collection.
- Segment reconciliation (Q1-FY27): slides 26/27/29 = 1,092 + 1,540 + 277 = 2,909 Mn approx = reported 2,908 Mn (L1048). Slide 36 = 1,302 + 1,774 + 277 = 3,353 Mn — does NOT reconcile (F16-1). Segmental mix on slide 10 (B2B 37% / CM 53% / Services 10%) confirms the 1,092/1,540/277 split as the true Q1-FY27 basis.
- Annualized-return check (slide 9): PAT 200 x 4 / Total Equity 7,510 = 10.65% = disclosed ROE 10.6% -> returns are single-quarter annualized, unlabeled (F16-4).
- Implied diluted weighted shares (PAT/EPS): FY24 ~32.6M; FY25 ~166.7M; FY26 ~88.2M; Q1-FY26 ~94.4M; Q4-FY26 ~84.1M; Q1-FY27 ~97.6M — not on a comparable adjusted base (F10-1).

--------------------------------------------------------------------------------
## HANDOFF TO A4 (questions to raise with management)
--------------------------------------------------------------------------------
Forward-signals: F16-3 (publish/confirm Q1-FY27 balance sheet + debtor days), F16-5 (GDV-to-
fee conversion and timing; is 6,500 Mn Wadhwa figure GDV or ARIS fee?), F16-6 (drivers of the
-15.3% QoQ revenue decline), F6-1 (Wadhwa DaaS conversion schedule).
Ambiguous (need clarification): F16-1 (reconcile segmental revenue across slides 26/27/36),
F16-2 (Services chart Q3-FY26 vs Q4-FY26 period), F16-4 (temporal basis of slide-9 KPIs;
are ROE/ROCE annualized?), F16-7 (current CM utilisation point value vs 55% red line),
F10-1 (basic EPS + adjusted share count post-IPO; any ESOP/warrant overhang).

```yaml
stage: A3-forensics
company: "ARIS"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/aris-q1fy27/work/forensics_presentation_aris_q1fy27.md"
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
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F16-1", check: "F16", line: "slide 36 L1025/1030 vs slide 26 L767 / slide 27 L786", classification: "AMBIGUOUS", implication: "Q1-FY27 segment revenue disagrees across slides; slide-36 sums to 3,353 Mn vs 2,909 Mn = reported 2,908 Mn"}
  - {id: "F16-2", check: "F16", line: "slide 36 L1035", classification: "AMBIGUOUS", implication: "Services x-axis reads Q3-FY26 where peers read Q4-FY26; 361 Mn bar period unknown, may mask a -23% QoQ Services decline"}
  - {id: "F16-3", check: "F16", line: "slide 39 L1127", classification: "FORWARD-SIGNAL", implication: "No Q1-FY27 balance sheet column; debtor days (master monitorable, Red >160) uncomputable for the quarter; FY26 already ~140d"}
  - {id: "F16-4", check: "F16", line: "slide 9 L250/L254", classification: "AMBIGUOUS", implication: "Asterisk/footnote temporal-basis mismatch; ROE 10.6%/ROCE 17.2% are single-quarter annualized but unlabeled"}
  - {id: "F16-5", check: "F16", line: "slide 35 L1000/L1002; slide 29 L857", classification: "FORWARD-SIGNAL", implication: "GDV (gross project value) used as revenue-visibility proxy; ARIS earns only 10-14% fees on GDV — gross-vs-net conflation"}
  - {id: "F16-6", check: "F16", line: "slide 37 L1048/L1078", classification: "FORWARD-SIGNAL", implication: "Revenue -15.3% QoQ and EPS -20.5% QoQ de-emphasized; slide 34 headlines YoY only"}
  - {id: "F16-7", check: "F16", line: "slide 28 L824", classification: "AMBIGUOUS", implication: "CM utilisation given as ~20% to 70%+ range, no current point value vs Notion Red <55%"}
  - {id: "F6-1", check: "F6", line: "slide 35 L1000; slide 29 L864", classification: "FORWARD-SIGNAL", implication: "Secured INR 6,500 Mn Wadhwa DaaS mandate to convert over 18-24 months; promise-vs-delivery tracker item"}
  - {id: "F10-1", check: "F10", line: "slide 37 L1078; slide 38 L1119", classification: "AMBIGUOUS", implication: "Only diluted EPS shown; implied share counts inconsistent across periods; QoQ EPS -20.5% vs PAT -7.8% implies ~16% share rise"}
forward_signals: ["F16-3", "F16-5", "F16-6", "F6-1"]
ambiguous: ["F16-1", "F16-2", "F16-4", "F16-7", "F10-1"]
commitments:
  - {commitment: "Secured INR 6,500 Mn DaaS contract from Wadhwa Group", implied_date: "18-24 months from Q1-FY27", ref: "slide 35 L1000 / slide 29 L864", status_word: "secured"}
  - {commitment: "Announced entry into large-scale asphalt market", implied_date: "late 2025; live in Q1-FY27 (529 Mn)", ref: "slide 11 L311 / slide 35 L994", status_word: "commenced"}
  - {commitment: "Building diversified SME/MSME supplier network", implied_date: "ongoing", ref: "slide 26 L750", status_word: "underway"}
  - {commitment: "New Category Expansion into tiles/CP fittings/sanitaryware/electricals/plumbing", implied_date: "undated", ref: "slide 32 L936", status_word: "intends to"}
  - {commitment: "Scale Contract Manufacturing via additional third-party plant tie-ups", implied_date: "undated", ref: "slide 32 L944", status_word: "proposes to"}
gate_a3: pass
blank_checks: []
```
