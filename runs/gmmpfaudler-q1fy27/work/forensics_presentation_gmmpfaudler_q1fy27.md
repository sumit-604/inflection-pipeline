# A3 FORENSIC NOTES — GMM Pfaudler Limited (GMMPFAUDLR) — Q1 FY27 — DOCTYPE: PRESENTATION

Source deck: investor_presentation_q1fy27.pdf (29 slides). A1 extract:
extract_presentation_gmmpfaudler_q1fy27.txt (847 lines). A2 ledger:
ledger_presentation_gmmpfaudler_q1fy27.md. Prior-quarter deck: NONE supplied
(F16 DROPPED-disclosure diff has no baseline — WITHIN-deck reframing only).
Model: claude-opus-4-8. Reconciliation: 100% of A2 rows read at cited lines.

Conservative bias applied: where direction is uncertain the finding leans bear
and is flagged AMBIGUOUS for A4 to convert into a management question.

---

## LEDGER RECONCILIATION (A2 -> A1 verbatim, 100%)

- Table 1 (29 slides): all slide blocks read at their cited `[page N]` lines
  (28-806). Titles/content-types confirmed against extract.
- Table 2 (414 numbers across 29 slides): every number-bearing block read at
  its block-start line; the two financial-summary tables (p.25 line 672, p.26
  line 698) read cell-by-cell.
- Table 3 (6 footnotes): all read verbatim — ₹355 Cr large-order caveat x3
  (lines 256, 498, 566), FY26 PPA restatement (line 200), two "subject to
  casting" table footers (lines 695, 721).
- Table 4 (DROPPED_SLIDE): N.A. — no prior deck. Marked explicitly.
- A2 flags resolved below: ZERO_STANDING x3 (F1/F12), AXIS_BINDING_UNCERTAIN x3
  (resolved non-load-bearing, see note), REPEAT_FOOTNOTE x1 (F16), RESTATEMENT
  x1 (F16).

AXIS_BINDING_UNCERTAIN resolution (slides 6/17/18): the uncertain bars are the
Q2/Q3 FY26 interior columns of trend charts. Endpoints tie exactly to the p.25
consolidated table (Q1FY26 EBITDA 101, Q4FY26 75, Q1FY27 94 — line 681) and to
the division cards on p.16. No gate or arithmetic-consistency check in this
report is load-bearing on the interior Q2/Q3 ordering, so the flag is retained
but does NOT generate a finding.

---

## FINDINGS TABLE

| id | check | ledger row ref | slide/line | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F1 | T2 s25 ZERO_STANDING; T1 s20 | p.25 L687 / p.20 L595-598 | "Exceptional Items … - / 9 / -100% / - / NA"; "Group-wide refinancing to restructure and reduce debt … Within next 12-18 months" | FORWARD-SIGNAL | Exceptional-items line exists to carry European restructuring/impairment charges; ₹9 Cr booked Q4 FY26, zero this quarter (gate 7 GREEN). But refinancing + intercompany-loan unwind is "underway" over 12-24 months — fresh exceptionals are a live forward risk, not a closed chapter. |
| FN-02 | F1 | T2 s26 ZERO_STANDING | p.26 L717 | "Other Comprehensive Income … 0 / 2 / -100% / 0 / -" | NEUTRAL-FACT | Standalone OCI rounds to zero because DB-plan remeasurement is small and FX-translation of foreign subs sits at the consolidated level (consol OCI ₹5 Cr). Benign; explains the zero row. |
| FN-03 | F2 | T2 s25 L690 / s26 L715 | p.25 L690 / p.26 L715 | consol PAT "22 … 10 … 118%"; standalone PAT "11 … 17 … -33%" | FORWARD-SIGNAL | The +118% YoY consolidated PAT headline is entirely a subsidiary swing: subs contributed -₹7 Cr in Q1 FY26 (standalone PAT 17 > consol 10) and +₹11 Cr in Q1 FY27 (consol 22 > standalone 11) — an +18 Cr subsidiary swing. Meanwhile the STANDALONE (domestic) engine deteriorated: revenue +2% YoY, EBITDA -28% YoY (36->26), PAT -33% YoY. Headline masks domestic weakness. |
| FN-04 | F6 | T1 s9/s20/s29 | p.9 L312 / p.20 L595-606 / p.29 L830-843 | "Repayment of approx. EUR 7 million of debt by the end of Q2 FY27, funded through internal accruals"; "Within next 12-18 months"; "Within next 18-24 months" | FORWARD-SIGNAL | Dateable commitments feeding the Role 5 promise-vs-delivery tracker (see register). Gate 9 = AMBER: concrete near-term EUR 7M repayment + timelines, but NO advisor mandate named; Notion notes debt/tax restructuring has been "next year" for two prior calls — this is the third dating. |
| FN-05 | F7 | T1 s29 | p.29 L830-843 | "Gradual improvement expected over the medium term"; "Benefits expected to materialize progressively as restructuring is completed" | AMBIGUOUS | Pre-emptive hedging on the exact thesis lever (EBIT-to-PAT conversion). Open-ended, no hard date, layered over wide 12-24 month ranges — telling us conversion improvement is not imminent. |
| FN-06 | F8 | T2 s25 L686-690 | p.25 L686-690 | "Profit before tax after exceptional items 40 … Tax 18 … Profit after tax 22" | FORWARD-SIGNAL | Consolidated ETR = 18/40 = 45.0% -> gate 3 RED boundary (>=45%). vs standalone ETR 3/15 = 20% and statutory 25.17%. Q1 FY26 was 21/32 = 65.6%, so improving but still at the red line. The consol-vs-standalone ETR gap is the structural European tax drag flagged in the Notion thesis as the biggest P&L catalyst. |
| FN-07 | F9 | T2 s25 L692 | p.25 L692 | "Other Comprehensive Income 5 … 55 … -91%" | AMBIGUOUS | Consolidated OCI collapsed from ₹55 Cr (Q1 FY26) to ₹5 Cr. The ₹55 Cr prior-year OCI (FX-translation of foreign ops) EXCEEDED that quarter's PAT (₹10 Cr) and drove TCI to ₹65 Cr — flattering the YoY TCI base (now -59% to ₹27 Cr). Verify FX/actuarial assumptions at the Annual Report. |
| FN-08 | F12 | T2 s16/s17/s18; ZERO_STANDING HET | p.16 L474-499 / p.17 L501 / p.18 L536 | "Revenue – Q1 FY27 … Flat YoY" (HET); "Order Intake … ▼ -78% YoY*" (PST) | FORWARD-SIGNAL | Divisions disclose revenue + order intake ONLY — no division PBIT/margin, assets, or liabilities. Overseas/India region split is gone, so gate 1 (overseas PBIT margin, last seen 4.4% and falling) is no longer trackable. HET revenue disclosed as "Flat" (no %); PST order intake -78% is distorted by the ₹355 Cr one-off (net of it PST order intake rose). Division-level profitability opacity coincides with the reorganization. |
| FN-09 | F13 | T1 s9 | p.9 L313 | "Revision of its dividend payout frequency from semi-annual to annual, with no change in the Company's Dividend Distribution Policy" | AMBIGUOUS | Board-level change to capital-return cadence. Read conservatively it is cash-conservation ahead of the debt restructuring; "no change in policy" softens optics. A4 question: is annual-only frequency a liquidity signal? |
| FN-10 | F16 | T1 s15 | p.15 L453-457 | "From Segments and Regions … To Global Divisions" | FORWARD-SIGNAL | Reporting-basis change from segments (Technologies/Systems/Services) + regions (India/Intl) to FOUR global divisions (CRT/PPT/HET/PST). Removes the India-vs-Overseas split. Comparability break: the deteriorating overseas-margin metric (gate 1, thesis-break watch) is retired precisely as the reorganization lands. Info-suppression read; lean bear. |
| FN-11 | F16 | T1 s22; T2 s25 L681-682 | p.22 L634-635 / p.25 L681-682 | "margin recovery over previous quarter with significant improvement in earnings"; EBITDA "94 … 75 … 25%" (QoQ) vs "101 … -7%" (YoY) | AMBIGUOUS / CONFIRMATORY-NEGATIVE | Deck leads with QoQ (EBITDA +25%, PAT +44%) off a weak Q4 FY26 base that itself carried a ₹9 Cr exceptional, while YoY EBITDA is -7% and consolidated EBITDA margin fell 258 bps to 10.1%. Baseline-shifting to flatter. Gate 5 = RED (margin 10.1% < 11%, even clean of exceptionals). |
| FN-12 | F16 | T3 rows 1-3 REPEAT_FOOTNOTE | p.7 L256 / p.16 L498 / p.18 L566 | "*Q1 FY26 order intake includes a large order of NR 355 Cr" | AMBIGUOUS | One non-recurring ₹355 Cr order qualifies THREE headline comparisons (deck order-intake chart, PST revenue chart, PST order-intake chart). Backlog (₹2,289 Cr) carries no definition (gross/net of GST, executed/pending). Optics should be read net of the one-off. |
| FN-13 | F16 | T3 row 4 RESTATEMENT | p.6 L200 | "¹ FY 26 restated for Semco and GMM Inox Poland PPA." | FORWARD-SIGNAL | Q2/Q3 FY26 PAT & EPS trend bars are on a restated basis (SEMCO + GMM Inox Poland purchase-price allocation). PPA can still finalise/shift; goodwill+intangibles ~₹852 Cr (Notion) = 70.8% of parent equity — gate 8 impairment risk is real and NOT monitored anywhere in this deck. |
| FN-14 | F16 | T1 (no BS/CF slide) | p.25 L672 / p.26 L698 | deck carries only "Consolidated Financial Summary" and "Standalone Financial Summary" (P&L) | FORWARD-SIGNAL | The deck omits any balance sheet, net-worth/reserves line, and cash-flow statement. Standalone quarterly CFO (gate 2, which collapsed to ₹18.41 Cr FY26) is NOT disclosable from this deck. Opacity on the most deteriorated cash metric. |

---

## NOTION MONITORING-GATE READINGS (this deck reads gates 1,4,5,7,10; also 3,8,9)

| Gate | Metric | Reading from deck | Colour | Cite |
|---|---|---|---|---|
| 1 | Overseas/division PBIT margin | NOT DISCLOSED — region split retired; no division PBIT | RED-adjacent (info suppressed) | p.15 L453, p.16 L474 |
| 2 | Standalone CFO (quarter) | NOT DISCLOSED — no cash-flow statement in deck | not readable | p.26 L698 |
| 3 | Effective tax rate | 18/40 = 45.0% consolidated | RED (>=45% boundary) | p.25 L686-690 |
| 4 | Order backlog trajectory | ₹2,289 Cr, up from ₹2,205 Cr opening (+4% QoQ, +20% YoY) | GREEN | p.7 L214 / p.9 L304 |
| 5 | Consolidated EBITDA margin | 10.1% (clean of exceptionals) | RED (<11%) | p.25 L681-682 |
| 6 | AGM Gelhaus vote (04-Aug-26) | NOT MENTIONED (deck dated 05-Aug, silent on AGM) | not readable | p.1 L29 |
| 7 | Fresh Europe exceptionals | Zero this quarter (₹9 Cr was Q4 FY26) | GREEN (line still standing) | p.25 L687 |
| 8 | Goodwill/intangibles impairment | None disclosed; goodwill balance not shown | GREEN by absence (unmonitored) | p.25 L687 |
| 9 | Debt restructuring progress | Timelines (12-18m / 18-24m) + EUR 7M repayment Q2 FY27; no advisor mandate | AMBER | p.20 L595-606 |
| 10 | Diversification order-intake mix | Non-traditional ~43% (top band 31->33->42->43); slide 29 "~45%" | AMBER (40-50%, not >50%) | p.8 L268 / p.29 L817-819 |

---

## CHECKLIST SCORECARD (all 17; exactly one status each — GATE A3)

| # | Status | Basis |
|---|---|---|
| F1 | FINDING | Exceptional Items row (p.25 L687) exists for European restructuring/impairment charges — ₹9 Cr Q4 FY26, zero now; standalone OCI zero row (p.26 L717) explained (FX sits at consol). FN-01, FN-02. |
| F2 | FINDING | S-vs-C PAT contribution swung -₹7 Cr -> +₹11 Cr YoY (>5pp of standalone PAT); consol +118% masks standalone -33%. FN-03. |
| F3 | PASS | Consolidated Material Cost 366 vs standalone 119, Other Costs 465 vs 91 (p.25/26) — subsidiaries carry real cost bases, not shells; no going-concern language in a deck. |
| F4 | N.A. | No auditor Other-Matters / component-auditor disclosure in an investor deck. |
| F5 | N.A. | No auditor EoM / going-concern paragraph in a deck; no prior deck for verbatim diff. |
| F6 | FINDING | Dateable commitments: EUR 7M repayment Q2 FY27; refinancing 12-18m; group tax 18-24m; intercompany-loan unwind 12-18m; org streamlining by FY27. FN-04. Commitment register below. |
| F7 | FINDING | Hedges softening the EBIT-to-PAT conversion thesis ("gradual", "progressively", "medium term"). FN-05. |
| F8 | FINDING | Consolidated ETR 45.0% (gate 3 RED boundary) vs standalone 20%, statutory 25.17%; European tax drag. FN-06. |
| F9 | FINDING | Consolidated OCI ₹55 Cr -> ₹5 Cr YoY (-91%); prior-year FX-translation OCI exceeded that quarter's PAT and flattered TCI base. FN-07. |
| F10 | PASS | Only Basic EPS disclosed (no diluted EPS, no paid-up capital line); no corporate action; consol EPS 5.32 > implied on total PAT 22.1 is consistent with minorities absorbing subsidiary losses, not a dilution event. |
| F11 | N.A. | Deck carries no balance sheet, Other Equity, or net-worth line — nothing to tie out. Absence itself flagged under F16 (FN-14). |
| F12 | FINDING | Division disclosure = revenue + order intake only; no division PBIT/assets/liabilities; region split retired (gate 1 lost); HET "Flat" precision gap; PST -78% one-off distortion. FN-08. |
| F13 | FINDING | Dividend frequency semi-annual -> annual (board-level capital-return change). FN-09. |
| F14 | PASS | No note-vs-auditor conflict possible in a deck; division sums tie to totals (466+255+74+131=926≈925; 502+367+58+80=1007); "-2.30" EPS and "+719%" verified consistent with underlying (Q3 loss; HET off ₹7 Cr base). No genuine drafting inconsistency. |
| F15 | N.A. | Deck carries no period-over-period consolidation entity list; acquisition history table (p.28) is not a consolidation scope list; no prior deck. |
| F16 | FINDING | Reporting-basis change to 4 divisions (removes overseas split); QoQ-vs-weak-Q4 framing; repeat ₹355 Cr footnote x3; FY26 PPA restatement; no balance-sheet/CFO disclosure. FN-10 through FN-14. |
| F17 | N.A. | Not a concall — no transcript to run the silence audit against (per injected note). |

No blank checks. GATE A3 = PASS.

---

## COMMITMENT REGISTER (from F6)

| Commitment | Implied date | Ref (slide/line) | Status word |
|---|---|---|---|
| Repay approx. EUR 7 million of debt, funded through internal accruals | End of Q2 FY27 | p.9 L312 / p.20 L598 | planned (debt reduction "already started") |
| Group-wide refinancing to restructure and reduce debt; remove intercompany loans causing FX | Within next 12-18 months | p.20 L595-598 | underway ("already started") |
| Group Tax Strategy — review/simplify legal-entity structure | Within next 18-24 months | p.20 L600-602 | initiated (reviewing) |
| Intercompany loan termination (unwind cross-currency loan between subsidiaries) | Within next 12-18 months | p.20 L604-606 | in the process of |
| Reorganization into four distinct global divisions | Q1 FY27 (announced); streamlining largely completed by FY27 | p.9 L310 / p.29 L830-834 | underway ("to be largely completed by FY27") |
| EBIT-to-PAT conversion improvement | "medium term" / "progressively as restructuring is completed" (no hard date) | p.29 L840-843 | underway (initiatives) |
| Positive momentum expected to continue with healthy order pipeline | ongoing | p.22 L638 | expected to continue |

---

## FORWARD IMPLICATIONS SUMMARY (for A4)

FORWARD-SIGNAL (8): FN-01, FN-03, FN-04, FN-06, FN-08, FN-10, FN-13, FN-14.
AMBIGUOUS -> A4 management questions (5): FN-05, FN-07, FN-09, FN-11, FN-12.

Bear-leaning read: the +118% consolidated PAT headline and "margin recovery"
messaging rest on (a) a subsidiary loss-to-profit swing while the domestic
standalone engine shrank (PAT -33%, EBITDA -28% YoY), (b) a QoQ comparison off
a weak, exceptional-laden Q4 base, and (c) a reporting reorganization that
retires the overseas-margin disclosure (gate 1) exactly when it was
deteriorating and hides division profitability. Gates 3 (ETR 45%) and 5 (EBITDA
margin 10.1%) both read RED; gates 9 and 10 AMBER; gate 4 the one clean GREEN.
Debt/tax restructuring is dated for the third time with still no advisor
mandate. Goodwill (~₹852 Cr) impairment risk is unmonitored in the deck.
```yaml
stage: A3-forensics
company: "GMMPFAUDLR"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/gmmpfaudler-q1fy27/work/forensics_presentation_gmmpfaudler_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: N.A.
  F12: FINDING
  F13: FINDING
  F14: PASS
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN-01", check: "F1", line: "p.25 L687 / p.20 L595", classification: "FORWARD-SIGNAL", implication: "Exceptional-items line stands for European restructuring/impairment; zero now (gate7 GREEN) but restructuring underway 12-24m = fresh-exceptional risk live"}
  - {id: "FN-02", check: "F1", line: "p.26 L717", classification: "NEUTRAL-FACT", implication: "Standalone OCI zero because FX-translation sits at consol level; benign"}
  - {id: "FN-03", check: "F2", line: "p.25 L690 / p.26 L715", classification: "FORWARD-SIGNAL", implication: "Consol PAT +118% is a subsidiary loss->profit swing (+18 Cr); standalone PAT -33% and EBITDA -28% YoY hidden by the headline"}
  - {id: "FN-04", check: "F6", line: "p.9 L312 / p.20 L595-606", classification: "FORWARD-SIGNAL", implication: "Dated commitments; gate9 AMBER (timelines + EUR7M Q2FY27, no advisor mandate; third consecutive dating)"}
  - {id: "FN-05", check: "F7", line: "p.29 L830-843", classification: "AMBIGUOUS", implication: "Hedged EBIT-to-PAT conversion ('gradual','progressively','medium term') = improvement not imminent"}
  - {id: "FN-06", check: "F8", line: "p.25 L686-690", classification: "FORWARD-SIGNAL", implication: "Consolidated ETR 45.0% = gate3 RED boundary vs standalone 20%; structural European tax drag"}
  - {id: "FN-07", check: "F9", line: "p.25 L692", classification: "AMBIGUOUS", implication: "Consol OCI 55->5 (-91%); prior-year FX OCI exceeded PAT and flattered YoY TCI base; verify assumptions at AR"}
  - {id: "FN-08", check: "F12", line: "p.16 L474-499 / p.17 L501 / p.18 L536", classification: "FORWARD-SIGNAL", implication: "Divisions show revenue+order intake only, no PBIT/assets/liabilities; gate1 overseas margin lost; HET 'Flat', PST -78% one-off distortion"}
  - {id: "FN-09", check: "F13", line: "p.9 L313", classification: "AMBIGUOUS", implication: "Dividend frequency semi-annual->annual; possible cash-conservation signal ahead of restructuring"}
  - {id: "FN-10", check: "F16", line: "p.15 L453-457", classification: "FORWARD-SIGNAL", implication: "Reporting-basis change to 4 divisions retires India/Overseas split; comparability break; deteriorating overseas-margin metric suppressed"}
  - {id: "FN-11", check: "F16", line: "p.22 L634 / p.25 L681", classification: "AMBIGUOUS", implication: "QoQ framing off weak exceptional-laden Q4 base masks YoY EBITDA -7% and margin -258bps; gate5 RED (10.1%)"}
  - {id: "FN-12", check: "F16", line: "p.7 L256 / p.16 L498 / p.18 L566", classification: "AMBIGUOUS", implication: "One ₹355 Cr one-off qualifies three headline order comparisons; backlog undefined (gross/net, executed/pending)"}
  - {id: "FN-13", check: "F16", line: "p.6 L200", classification: "FORWARD-SIGNAL", implication: "FY26 Q2/Q3 restated for SEMCO+GMM Inox Poland PPA; PPA can shift; ~₹852 Cr goodwill impairment risk (gate8) unmonitored in deck"}
  - {id: "FN-14", check: "F16", line: "p.25 L672 / p.26 L698", classification: "FORWARD-SIGNAL", implication: "Deck omits balance sheet, net worth and cash-flow; standalone CFO (gate2) not disclosable = opacity on the most deteriorated cash metric"}
forward_signals: ["FN-01","FN-03","FN-04","FN-06","FN-08","FN-10","FN-13","FN-14"]
ambiguous: ["FN-05","FN-07","FN-09","FN-11","FN-12"]
commitments:
  - {commitment: "Repay approx. EUR 7 million of debt via internal accruals", implied_date: "End Q2 FY27", ref: "p.9 L312 / p.20 L598", status_word: "planned"}
  - {commitment: "Group-wide refinancing to restructure/reduce debt and remove intercompany FX loans", implied_date: "12-18 months", ref: "p.20 L595-598", status_word: "underway"}
  - {commitment: "Group Tax Strategy - simplify legal-entity structure", implied_date: "18-24 months", ref: "p.20 L600-602", status_word: "initiated"}
  - {commitment: "Intercompany loan termination (unwind cross-currency loan)", implied_date: "12-18 months", ref: "p.20 L604-606", status_word: "in-process"}
  - {commitment: "Reorganization into four global divisions", implied_date: "streamlining largely completed by FY27", ref: "p.9 L310 / p.29 L830", status_word: "underway"}
  - {commitment: "EBIT-to-PAT conversion improvement", implied_date: "medium term (no hard date)", ref: "p.29 L840-843", status_word: "underway"}
gate_a3: pass
blank_checks: []
```

