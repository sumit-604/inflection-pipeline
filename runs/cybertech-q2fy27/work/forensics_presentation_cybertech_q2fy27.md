# A3 FORENSIC NOTES: CYBERTECH Q2FY27 (doctype: presentation)

Agent: A3-forensics | model: claude-opus-5-5 | run date: 2026-10-24
Inputs read: A1 structured (runs/cybertech-q2fy27/extracted/cybertech-presentation-q2fy27-structured.md, R001-R326), A1 fulltext (runs/cybertech-q2fy27/extracted/cybertech-presentation-q2fy27-fulltext.md, L1-L348; slide 15 image-verified block L308-L337 governs), A2 ledger (runs/cybertech-q2fy27/work/ledger_presentation_cybertech_q2fy27.md).
Cross-document reads (verification only): results-filing fulltext (Rs lakh, x0.01 to Rs Cr; deck INR mn = lakh / 10) and press-release fulltext (INR mn). Both line numbers cited on every mismatch, prefixed RES and PR. Deck lines carry no prefix.
Prior-quarter fulltext: NONE. Notion checklist: NONE. Source PDF and inputs/ not opened.

## LEDGER RECONCILIATION
- Ledger accounts for 326 of 326 structured IDs (orphans: none). A3 read all 326 rows in the structured file and each at its cited fulltext line. Reconciled: 326 / 326 = 100%.
- Slide 15 numeric rows R166-R308 (and R314) were read against the image-verified block L309-L337, not the row-shifted raw layer L268-L304 (R319, A1 note).
- Every slide 15 figure was also tied to the results filing (RES L100-L128). All ties within 0.1 mn rounding except one cell (A3P-04).
- Arithmetic re-performed on the deck. Expense sums, PBT, PAT, TCI and every printed growth % tie within rounding, except Q2FY26 TCI (A3P-04). Finance cost YoY 104.3% (L315) ties on unrounded lakh (46.48 / 22.75, RES L106).

## FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3P-01 | F1 | R269, R270, R272, R274, R275, R277 (vs R271, R273, R276, R278) | L327-L328, slide 15 | "a) Remeasurement of the net defined benefit liabilities \| - \| - \| \| (1.7) \| \| - \| (3.4)" | AMBIGUOUS | The template line takes a quarterly actuarial remeasurement. FY26 booked one each quarter: Q2FY26 (1.7) mn, H1FY26 (3.4) mn. Q1 and Q2FY27 print nil. The FY26 full-year figure is +33.30 lakh (RES L118), so H2FY26 swung about +66.9 lakh against H1. Two readings. (a) Interim actuarial valuation stopped, so the FY27 remeasurement lands in one Q4 lump. (b) Assumptions did not move. A4 question: is a Q4FY27 OCI catch-up coming? Verify discount-rate assumptions at the FY26 and FY27 Annual Reports. |
| A3P-02 | F8 | R257, R259 (R256 near-zero) | L323, slide 15 | "c) Tax adjustments for earlier years \| (0.0) \| 0.7 \| \| - \| \| 0.7 \| -" | NEUTRAL-FACT | Earlier-year tax is non-zero: Q1FY27 0.7 mn (RES L114: 7.41 lakh), Q2FY27 (0.18) lakh. That is 0.6% of Q1 PBT. Immaterial. Logged because the rule makes any non-zero value a FINDING. |
| A3P-03 | F8 | R246-R255 | L321-L322, slide 15 | "b) Deferred Tax \| 4.0 \| 4.8 \| \| (1.2) \| \| 8.8 \| 0.7" | AMBIGUOUS | Book ETR is steady: Q2FY27 24.9% (28.7/115.4), Q1FY27 24.8%, Q2FY26 24.1%, H1FY27 24.8%, H1FY26 24.3%. Statutory rate is 25.17%. Current-tax-only rate fell: H1FY27 20.9% (50.5/241.6) vs H1FY26 24.0% (53.3/222.3). Deferred charge is 14.7% of H1FY27 tax vs 1.3% in H1FY26. Net DTL rose from 235.72 to 326.47 lakh (RES L174). This is no DTA shield. Book tax runs about 390 bps above cash tax. When the temporary difference reverses, cash tax steps up; book ETR does not. A4 question: what temporary difference builds the DTL (fair-value gains, US subsidiary timing, Labour Code provisions)? |
| A3P-04 | F9 | R281, R291 (R283, R293 tie) | L330, L332, slide 15 | deck "a) Foreign currency translation reserve \| 21.8 \| (2.5) \| \| (2.9)"; RES L121 "Foreign currency translation reserve \| 217.88 \| (24.96) \| 290.47" | NEUTRAL-FACT | The deck prints Q2FY26 FCTR as (2.9) mn. The filing shows +290.47 lakh = +29.0 mn, so both magnitude and sign are wrong. Both deck layers (raw L296, image L330) print (2.9), so this is the deck's own error, not an extraction artefact. Deck Q2FY26 TCI 114.3 (L332) matches RES L123 (1,143.43 lakh) but does not foot to the deck's own lines (86.6 - 1.7 + 0.4 - 2.9 = 82.4). The filing governs. Anyone who builds Q2FY26 OCI from the deck understates it by 31.9 mn. Governance data point: the deck is not tied out to the filing. |
| A3P-05 | F10 | R294-R298, R299-R308 | L333, L336-L337, slide 15 | "Paid up equity share capital (Face value: Rs.10 per share) \| 303.8 \| 302.8 \| \| 311.3" | NEUTRAL-FACT | Paid-up capital moves with no explanation on the deck. Traced in the filing. (1) Buyback: "Buyback of equity shares (including transaction costs) \| (1,498.00)" (RES L235). Capital falls 3,113.06 to 3,028.06 lakh, i.e. 8.5 lakh shares extinguished, about Rs 176 per share including costs (computed). Q1FY27 implied weighted shares are 30.98 mn (94.8/3.06), so the buyback completed inside Q1FY27. (2) ESOP: "allotted 1,00,000 equity shares" (RES L432); proceeds 47.60 lakh (RES L234). Basic minus diluted EPS spread is 0.00-0.02 (L336-L337; FY26 9.77/9.75, RES L127-L128), not widening. Outstanding options: NOT FOUND. Q2 EPS rose 2.9% YoY (2.86 vs 2.78) while PAT rose 0.3% (L324). The gap is buyback accretion, not operations. The deck never mentions the buyback. |
| A3P-06 | F12 | R134-R145, R148-R151 | L247, slide 13 | "Q2FY27 Technology 68.0%, State/Local Government 15.0%, Utilities 8.0%, Others 10.0%" | FORWARD-SIGNAL | Industry shares x operating revenue (shares are of operating revenue per PR L118; computed; whole-% rounding gives about +/-3.7 mn). State/Local Government: 52.9 / 75.3 / 110.0 mn (Q2FY26 / Q1FY27 / Q2FY27), +46% QoQ and +108% YoY. Technology: 429.2 / 492.8 / 498.4 mn, +1.1% QoQ and +16.1% YoY. Government supplied about 34.7 of the 48.5 mn QoQ increment (about 72%). The quarter's growth engine moved from Technology to public-sector work. Public-sector work tends to be project-based and tied to US state budget cycles. A4 question: what drove the government step-up (named programmes, contract length, recurring vs one-time)? Ind AS 108 shows a single segment (RES L433), so no segment asset or liability test is possible. |
| A3P-07 | F14 | R318, R284-R288, R182 | L313, L329-L331, L311, slide 15 | "b) Income tax relating to items that will not be reclassified to profit and loss" (L331, under L329 "Items that will be reclassified") | NEUTRAL-FACT | Label drift. (1) The L331 caption contradicts its heading. The filing carries the same caption (RES L122), so the error is inherited. (2) Deck cost label "Cost of Hardware / Software package/ for service delivery Outsourced project cost" (L313) vs filing "Outsourced service costs" (RES L104). Values tie (176.6 mn = 1,765.85 lakh). The deck label is a legacy template from the hardware/software package era. (3) Deck "Total Revenue (1+2)" (L311) vs filing "Total Income (1+2)" (RES L102). Each is immaterial alone. Together they are a governance data point. |
| A3P-08 | F14 | R074 | L147, slide 9 | "Co-founded the company in 1990" | NEUTRAL-FACT | The same-day PR says "Founded in 1995" (PR L129). The CIN "L72100MH1995PLC084788" (RES L96) shows a 1995 incorporation. 1990 may refer to a predecessor or group entity; the deck does not say. Low priority. Cross-check against the AR company history. |
| A3P-09 | F14 | R021-R025, R326, R009 | L81-L82, L343, L41 | "Partnerships with Leading Technology Players - SAP, Esri, Cisco, Salesforce and Microsoft"; "© 2020" | NEUTRAL-FACT | The deck partner list leaves out AWS. The same-day PR names "partnerships with AWS and Microsoft Azure" (PR L83-L84) and "Esri Platinum Partner" (PR L75). The copyright reads 2020 (L343). The safe harbor cites "conditions in India" (L41), yet 99% of revenue is US (L246). Stale template. The deck lags the company's current partner set. |
| A3P-10 | F16 | R094, R100, R108-R115 | L181, L223, slides 11-12 | "Reported EBITDA at 128.2 million (16.4% of total revenue)"; "QoQ De-Growth 7.8%" | FORWARD-SIGNAL | The deck's EBITDA includes other income: 128.2 = PBT 115.4 + finance 4.6 + D&A 8.1 (L319, L315, L316), and the margin is on total revenue (R100). The headline EBITDA de-growth is an other-income effect. Other income fell 81.9 to 47.3 mn (L310), mainly because mutual-fund fair-value gains fell from 264.50 to 18.69 lakh at H1 (RES L212). Core operating EBITDA = op revenue - outsourced - employee - other expenses (computed from L309, L313, L314, L317): 46.2 mn (7.9% of op rev) Q2FY26, 57.2 mn (8.4%) Q1FY27, 80.9 mn (11.0%) Q2FY27. That is +41% QoQ and +75% YoY; H1 138.1 vs 95.5 mn (+45%). Other income share of PBT: 69.7%, 64.9%, 41.0%. Earnings are moving from treasury to operations. Bear lean: this is one quarter of a 260 bps core step-up. Other expenses fell 1.3% QoQ (L317) while revenue rose 7.1%. A4 question: does Q2 core margin carry one-offs, and does management track an EBITDA that excludes other income? |
| A3P-11 | F16 | R158, R159, R161, R164, R165 | L254, L255, L261, slide 14 | "Top Client revenue 55%"; "Top 3 Client revenue 68%"; "Number of Projects - 136" | AMBIGUOUS | Concentration and project counts carry no period basis (quarter, H1 or LTM). Only the client count is tagged "(LTM)" (L253). On a quarterly basis, the top client is about 403 mn of 733.0 mn (computed). The top-3 share (68%) equals the Technology share (68%, L247). Whether the top clients sit in Technology is NOT FOUND. No prior deck, so the trend cannot be assessed. A4 question: state the period basis, the 4-quarter trend, and the top client's contract term and renewal date. |
| A3P-12 | F16 | R134-R136 | L247 (deck) vs PR L116-L118 | PR: "revenue from the Technology sector continued to witness strong momentum and contributed 68%" | AMBIGUOUS | The same-day PR calls Technology "strong momentum". The deck shows Technology's share falling 73% to 72% to 68% (L247), and implied Technology revenue rose +1.1% QoQ (A3P-06). The two same-day documents frame the same data differently. Lean bear: Technology, the sector that likely holds the concentration exposure (A3P-11), flattened sequentially. A4 question: is Technology flat QoQ because of the top client? |

## CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | FINDING | 13 ZERO_STANDING rows plus near-zero R256, all explained. Tax-adjustment line (R258, R260): assessment true-ups, non-zero in Q1FY27 (see A3P-02). Tax on reclassifiable items (R284-R288): FCTR on foreign subsidiaries is untaxed, so this standing line is nil in every period. Remeasurement lines: nil after being booked in FY26 quarters, an anomaly (A3P-01). |
| F2 | N.A. | The deck prints consolidated only ("Consolidated Unaudited Financial Statements", L268). No standalone column. S-vs-C is results-filing scope. |
| F3 | N.A. | No standalone cost lines in the deck. Shell test is results-filing scope (RES L431 lists 3 subsidiaries). |
| F4 | N.A. | No auditor Other Matters paragraph in the deck. |
| F5 | N.A. | No Going Concern or EoM paragraph in the deck. No prior quarter to diff. |
| F6 | PASS | Lexicon scan of L1-L348: zero commitment hits. "shall" appears only in safe-harbor disclaimers (L33, L48). "will be reclassified" is a table caption (L329). The deck holds no guidance or plans beyond R009 (L38). Commitment register empty. |
| F7 | PASS | One lexicon hit: "subject to risks including loss of principal amount" (L46), standard safe-harbor boilerplate. No new hedge on lumpiness or concentration. |
| F8 | FINDING | ETR 24.1-24.9% vs 25.17% statutory. Earlier-year tax non-zero (A3P-02). Deferred charge builds a DTL; cash tax runs about 390 bps below book (A3P-03). |
| F9 | FINDING | Q2FY26 FCTR misprinted (A3P-04). Q2FY27 FCTR +21.8 mn does not exceed the FY26 full year (+86.7 mn, RES L121: 866.80 lakh), so no swing finding. The remeasurement practice change is logged at A3P-01. |
| F10 | FINDING | Paid-up change traced to a buyback and an ESOP allotment, both absent from the deck. Basic/diluted spread is flat (A3P-05). |
| F11 | PASS | Deck paid-up 303.8 mn ties to 3,038.06 lakh (RES L124, L166). Deck "Other equity" is blank (L334), as in the filing's quarterly columns (RES L125). The deck shows no net-worth figure to reconcile, so no gap above 5%. The equity roll-forward is results-filing scope. |
| F12 | FINDING | Industry mix shift toward State/Local Government (A3P-06). Single Ind AS 108 segment (RES L433), so no segment asset or liability trend exists. |
| F13 | N.A. | The deck carries no board outcome, AGM, director term or enabling resolution. |
| F14 | FINDING | Caption, label and entity-history inconsistencies (A3P-07, A3P-08, A3P-09). |
| F15 | N.A. | The deck carries no consolidation list. Entity diff is results-filing scope, and there is no prior to diff. |
| F16 | FINDING | No prior deck, so dropped-slide and dropped-metric diffs cannot be assessed (A2 DROPPED_SLIDE: none assessable). Within-deck reframing found: EBITDA includes other income (A3P-10). Concentration and project bases are undefined (A3P-11). PR vs deck framing differs on Technology (A3P-12). |
| F17 | N.A. | Doctype is presentation, not concall. No Notion monitoring checklist exists (no page, no company memory, no spear). Zero F6 commitments to audit. |

## COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| (none) | - | Deck holds no dated or dateable commitment. Only the generic safe harbor (R009, L38). | - |

## QUESTIONS FLAGGED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)
- A3P-10: Q2 core EBITDA excluding other income reached 11.0% of operating revenue, from 8.4% in Q1. What drove it, and does it include one-offs? Will management report EBITDA excluding other income?
- A3P-06: State/Local Government revenue rose to about 110 mn from about 75 mn QoQ. Which programmes drove it? What are the contract length and renewal profile?
- A3P-11: What period basis do the 55% top-client and 68% top-3 figures use? What are the 4-quarter trend and the top client's contract term?
- A3P-12: Technology revenue was about flat QoQ (+1.1%). Is that the top client?
- A3P-03: What temporary difference builds the deferred tax liability? When does it reverse into cash tax?
- A3P-01: Has interim actuarial remeasurement stopped? Is a Q4 OCI catch-up expected?

```yaml
stage: A3-forensics
company: "CYBERTECH"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/cybertech-q2fy27/work/forensics_presentation_cybertech_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3P-01", check: "F1", line: "L327-L328 (RES L118)", classification: "AMBIGUOUS", implication: "Remeasurement nil Q1/Q2FY27 after (1.7) mn Q2FY26; interim actuarial valuation may have stopped, Q4 OCI lump risk"}
  - {id: "A3P-02", check: "F8", line: "L323 (RES L114)", classification: "NEUTRAL-FACT", implication: "Earlier-year tax 0.7 mn Q1FY27, 0.6% of PBT, immaterial"}
  - {id: "A3P-03", check: "F8", line: "L321-L322 (RES L174)", classification: "AMBIGUOUS", implication: "Current-tax rate 20.9% H1FY27 vs 24.0% H1FY26; DTL build 235.72->326.47 lakh; cash tax step-up on reversal"}
  - {id: "A3P-04", check: "F9", line: "L330, L332 vs RES L121, L123", classification: "NEUTRAL-FACT", implication: "Deck Q2FY26 FCTR (2.9) vs filing +29.0 mn; deck TCI 114.3 does not foot to own lines; filing governs"}
  - {id: "A3P-05", check: "F10", line: "L333, L336-L337 (RES L234, L235, L432)", classification: "NEUTRAL-FACT", implication: "Paid-up 311.3->302.8->303.8 = buyback 1,498.00 lakh (8.5 lakh shares) + 1 lakh ESOP shares; EPS +2.9% YoY vs PAT +0.3% is buyback accretion; deck silent"}
  - {id: "A3P-06", check: "F12", line: "L247", classification: "FORWARD-SIGNAL", implication: "State/Local Govt implied rev 75.3->110.0 mn QoQ (~72% of increment); Technology +1.1% QoQ; growth engine moved to public sector"}
  - {id: "A3P-07", check: "F14", line: "L311, L313, L329-L331 (RES L102, L104, L122)", classification: "NEUTRAL-FACT", implication: "Caption contradicts heading; legacy cost and total-revenue labels differ from filing"}
  - {id: "A3P-08", check: "F14", line: "L147 (PR L129, RES L96)", classification: "NEUTRAL-FACT", implication: "Deck founding 1990 vs PR 1995 and CIN 1995"}
  - {id: "A3P-09", check: "F14", line: "L81-L82, L343, L41 (PR L75, L83-L84)", classification: "NEUTRAL-FACT", implication: "Partner list omits AWS named in PR; copyright 2020; India-centric safe harbor on 99% US revenue"}
  - {id: "A3P-10", check: "F16", line: "L181, L223, L309-L319 (RES L212)", classification: "FORWARD-SIGNAL", implication: "Reported EBITDA includes other income; core EBITDA ex-OI 46.2->57.2->80.9 mn (7.9%->8.4%->11.0%); OI share of PBT 69.7%->41.0%"}
  - {id: "A3P-11", check: "F16", line: "L254, L255, L261", classification: "AMBIGUOUS", implication: "Top client 55% / top-3 68% / 136 projects with no period basis; concentration trend unassessable"}
  - {id: "A3P-12", check: "F16", line: "L247 vs PR L116-L118", classification: "AMBIGUOUS", implication: "PR 'strong momentum' for Technology vs deck share 73->68% and +1.1% QoQ implied revenue"}
forward_signals: ["A3P-06", "A3P-10"]
ambiguous: ["A3P-01", "A3P-03", "A3P-11", "A3P-12"]
commitments: []
gate_a3: pass
blank_checks: []
analyst_note: "The deck's headline weakness (EBITDA -7.8% QoQ, PBT -8.5%) is an other-income effect. Mutual-fund fair-value gains collapsed (RES L212). Core operating EBITDA rose 41% QoQ to 11.0% of operating revenue. The quality question is whether that core step-up recurs. Read it with A3P-06: government work supplied about 72% of the QoQ increment, and such work tends to be lumpy. Technology, which likely holds the 55% client, was flat. EPS growth includes buyback accretion (A3P-05). No checklist item covers two pointers for A4 and the results-filing A3. (1) Finance costs doubled YoY (L315) while borrowings went to nil (RES L178). (2) Equity roll-forward: 21,230.00 + TCI 2,008.37 + ESOP 47.60 - buyback 1,498.00 = 21,787.97 lakh vs 20,572.73 reported (RES L168). The 1,215 lakh gap has no deck explanation. One candidate is a declared but unpaid dividend in current other financial liabilities (124.47 to 1,484.90 lakh, RES L183)."
```
