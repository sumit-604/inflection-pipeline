# A3 FORENSIC NOTES: FEDFINA q2fy27 (doctype: presentation, file tag "pressrelease")

Company: Fedbank Financial Services Ltd (FEDFINA). Lender (NBFC) readings applied.
Inputs read: A1 structured (R001-R247), A1 fulltext (160 lines, 3 pages), A2 ledger. Prior-quarter extract: none (ND). Source PDF and inputs/ not opened.
Units: Rs Cr as stated (fulltext line 79). Derived figures are marked [INFERENCE] and show their arithmetic. Derived figures are cross-checks only and never fill a missing disclosure.

## 0. Ledger reconciliation

- 247 of 247 structured IDs read at their cited fulltext lines. Every ledger range (R001-R200 table rows, R201-R214 narrative and ID numbers, R215-R228 entities, R229-R231 forward, R232-R242 dates, R243-R247 qualifiers) was checked against the fulltext. Reconciled: 100%.
- Arithmetic tie-out of the p2 P&L (lines 80-92), all five period columns: Core NII = interest income minus interest expense. NII = Core NII + DA. NTI = NII + other income. Op profit = NTI minus opex. PBT = op profit minus credit cost. PAT = PBT minus tax. All tie within 0.1 Cr rounding (line 105). Q1 + Q2 FY27 flows tie to the H1 FY27 column within 0.1 Cr. Cost-to-income recomputes (226.4/431.5 = 52.5%).
- Pipeline notes. These are not document findings.
  - A1 line drift. R205-R208 cite line 129, but the text sits at line 130. R204 cites line 130, but the text sits at line 131. The values are correct. This report cites the true lines.
  - A2 cross-ref labels R134-R136 (Disbursements, H1 columns) as point-in-time duplicates. Disbursements are a flow, so these cells are a drafting error, not a duplicate (FND-10).
  - A2 missed that R110/R111 (Shareholder's Fund, H1 columns) do NOT equal the Q2 point values (FND-03).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F8 | R081-R096 | 90-91 | "Tax Expenses 27.3 39.1 47.3 20.8% 73.0%" | AMBIGUOUS | ETR Q2FY27 = 47.3/178.0 = 26.6%. Q1FY27 = 25.5%. Q2FY26 = 25.4%. H1FY27 = 26.1%. Statutory rate is 25.17%. Q2 tax runs about 2.5 Cr above statutory (1.9% of PAT). Tax grew 20.8% QoQ against PBT growth of 16.0%. There is no current/deferred split and no prior-year adjustment line. Possible causes: disallowance, prior-period tax, DTA reversal. Ask management. |
| FND-02 | F10 | R105-R107, R113-R115 | 93-94 | "Shareholder's Fund 2709.8 3002.8 3165.0" / "Book Value Per Share (₹) 72.5 80.1 84.4" | NEUTRAL-FACT | [INFERENCE] Implied shares = SF/BVPS. Q2FY26: 37.35-37.40 Cr. Q2FY27: 37.48-37.52 Cr (ranges reflect BVPS rounding). YoY increase is 0.2-0.5%, which fits ESOP allotment. QoQ change is inside rounding. No EPS is shown, so the basic vs diluted spread is NOT FOUND. A4 should cross-check against known ESOPs. |
| FND-03 | F11 | R107, R111, R115, R119 | 93-94 | "Shareholder's Fund ... 3165.0 ... 2547.4 2926.1 14.9%" | AMBIGUOUS | The same date (30-Sep-2026) shows two net worth values in one table: 3165.0 (Q2 column) and 2926.1 (H1 FY27 column). The gap is 238.9 Cr, or 7.5%, above the 5% threshold. On the BVPS row the H1 column repeats the Q2 point value (84.4), so the two rows use different bases. Candidate reconciling items: an opening-balance (31-Mar) column, an average-equity column, or a population error. [INFERENCE] H1 ROE of 16.2% (line 125) back-solves to an opening balance near the H1 figure, which points to an opening or averaging basis. Ask for the basis. Do not use the H1 SF YoY (14.9%). |
| FND-04 | F11 | R098-R099, R106-R107 | 92-93 | "Profit After Tax 80.2 114.4 130.8" / "Shareholder's Fund 2709.8 3002.8 3165.0" | AMBIGUOUS | Net worth rose 162.2 Cr QoQ against Q2 PAT of 130.8 Cr. About 31.4 Cr of accretion (24% of PAT) is not PAT. ESOP issuance cannot explain this, because the implied share count is flat QoQ (FND-02). Candidates: an OCI reserve (FVOCI on loans held for assignment, cash-flow hedge reserve), share premium, other reserve movements. This needs the results-filing equity statement. It interacts with FND-06: a P&L DA loss alongside an equity gain outside P&L. |
| FND-05 | F12 (lender: loan book quality vs provisioning) | R073-R076, R161-R172, R205-R208, R204 | 89, 126-127, 130-131 | "QoQ Gross Stage III and Net Stage III are up by 27bps and 22 bps to 1.8% and 1.2% respectively." / "Credit Cost 31.5 34.1 27.1 -20.5%" | FORWARD-SIGNAL | Stage 3 rose while credit cost fell 20.5% QoQ. [INFERENCE] Net Stage 3 rose 22 of the 27 bps of new Gross Stage 3, so incremental provision cover is about 19% ((27-22)/27). Implied PCR (1 - NS3/GS3) fell from about 37.5% (Q1) to about 33% (Q2). The rounding range is 28.6-37.8%, so the 32% red line may already be breached. The Notion override clause says Pillar 2L 1.00x "self-withdraws to 0.80x if ... PCR thins further". The implied QoQ thinning meets that condition on the evidence available. Flag for the operator. The decision stays human. Lean bear: credit cost likely catches up next quarter, or write-offs drove the Q1 base. PCR is not disclosed, so management must state reported PCR and the Q2 write-offs. |
| FND-06 | F12 (lender: off-book assigned pool) | R025-R032 | 83 | "Net Gain on Direct Assignment 6.6 -12.9 -1.2 -90.9% -117.7% 1.2 -14.0" | AMBIGUOUS | DA income is negative for two quarters in a row (Q1 -12.9, Q2 -1.2; H1 -14.0 vs +1.2 a year ago). A negative net gain usually means reversal of the excess-interest-spread receivable on assigned pools (prepayment or foreclosure) or a fair-value loss. Assignment has stopped working as an income lever. Ask: (a) whether new assignment is paused, (b) the size of the assigned pool outstanding, (c) whether the Q1-Q2 loss is a one-off true-up or a run-rate. Link to FND-04 (OCI). |
| FND-07 | F12 (lender: capital vs book growth) | R121-R125, R105-R109, R177-R181 | 93, 102, 128 | "Asset Under Management 16,136 21,136 22,035 4.2% 36.6%" / "CRAR 21.6% 20.7% 21.0% 25 bps -68 bps" | AMBIGUOUS | AUM grew 36.6% YoY and net worth 16.8%, yet CRAR fell only 68 bps. AUM/SF moved from 5.95x to 6.96x. [INFERENCE] If Tier 1 is close to SF, implied risk-weighted asset growth is about 20% (1.168/0.972), far below AUM growth. Candidate reconciling items: Tier 2 issuance, a larger off-book share of AUM (assignment, co-lending), a lower-risk-weight mix, or a lower risk weight on gold. Ask for on-book vs off-book AUM, Tier 1 vs Tier 2, and the next equity-raise horizon. |
| FND-08 | F12 (lender: distribution build vs output) | R129-R132, R121-R124, R185-R196 | 102-103, 135-136 | "Branches 699 757 831 9.8%" / "Employees* 4,894 5,376 5,920 10.1%" / "Disbursements 5,205 6,760 6,676 -1.2%" | FORWARD-SIGNAL | 74 branches and 544 employees were added in one quarter. In the same quarter disbursements fell 1.2% QoQ and AUM grew 4.2%. [INFERENCE] AUM per branch fell from 27.9 Cr to 26.5 Cr. Opex rose 7.8% QoQ, and cost-to-income improved only 36 bps (line 123). The build runs ahead of output. Expect opex drag until the new branches mature. Ask for the product split of the 74 new branches (gold vs LAP) and their vintage productivity. This is checklist item 3: the gold branch count is not disclosed. |
| FND-09 | F12 (lender: fee income) | R041-R048 | 85 | "Other Income 28.3 25.7 27.8 8.2% -1.9% 59.4 53.5 -10.1%" | AMBIGUOUS | Other income fell 1.9% YoY (Q2) and 10.1% (H1) while AUM grew 36.6%. Fee and cross-sell income is shrinking relative to the book. Ask for the composition (insurance cross-sell, processing fees, treasury) and the reason for the decline. |
| FND-10 | F14 | R129-R136 | 103 | "Disbursements 5,205 6,760 6,676 -1.2% 28.3% 5,205 6,676 28.3%" | NEUTRAL-FACT | Disbursements are a flow. The H1 FY27 cell (6,676) repeats the Q2 figure; Q1 + Q2 = 13,436. The H1 FY26 cell (5,205) also repeats Q2FY26. The H1 disbursement column is a drafting error. Downstream stages must not use it. The true H1 FY27 figure is NOT FOUND in this document. |
| FND-11 | F14 | R025-R027, R161-R163, R207 | 83, 126, 130 | "Net Gain on Direct Assignment ... -12.9 -1.2" / "Gross NPA 1.9% 1.6% 1.8%" vs "Gross Stage III ... 1.8%" | NEUTRAL-FACT | The "Net Gain" label is kept on negative (loss) values. The table says "Gross NPA" and the bullet says "Gross Stage III" for the same figure. Together with FND-03 and FND-10, this makes four drafting inconsistencies in a 2-page release. Individually immaterial, cumulatively a governance data point. |
| FND-12 | F16 | R204, R145-R147 | 131 | "Our credit cost for Q2 stands at 0.6%." | AMBIGUOUS | No denominator is stated. [INFERENCE] 27.1 x 4 = 108.4 Cr annualised. On average AUM ((21,136+22,035)/2) that is about 0.50%. On average assets implied by ROA 2.8% (523.2/0.028 = about 18,686 Cr) it is about 0.58%, which matches the stated 0.6%. On the same basis Q1 would be about 0.78%. The checklist tripwire is 1.1% of average assets. On this reading the tripwire does not fire, but the basis needs confirmation. Ask management to state the basis and the Q1 comparable. |
| FND-13 | F16 | R221-R223, R137-R184 | 74, 120-131, 144 | "specializing in Loan Against Property and Gold Loans" | AMBIGUOUS | The release names two product lines but gives no product AUM split, no PCR, no gold tonnage, no gold branch count, no ST LAP data and no FY27 guidance (lines 152-155 carry only safe-harbour text). With no prior deck (ND), "dropped" cannot be tested. The non-disclosure covers 5 of 8 checklist items (2, 3, 7, 8, and the guidance half of item 1). Route to the results filing and the concall. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | PASS | 25 line items read. No zero, nil or dash value (ledger zero_standing 0). R027 is negative, not zero. |
| F2 | N.A. | The release gives one unlabelled set of figures. No standalone vs consolidated pair. |
| F3 | N.A. | No S-vs-C cost lines to compare. |
| F4 | N.A. | No auditor letter or Other Matters paragraph in a press release. The lender component-auditor check belongs to the results-filing A3. |
| F5 | N.A. | No EoM or going-concern text. Prior-quarter extract is ND. |
| F6 | PASS | Lexicon swept. Only hits: "is also being uploaded" (line 36, procedural) and "will not be in any way responsible" (line 154, disclaimer). No management commitment. No guidance. |
| F7 | PASS | "subject to certain risks and uncertainties" (line 152) appears only inside standard safe-harbour text. No product- or concentration-specific hedge. Newness cannot be tested (prior ND). |
| F8 | FINDING | FND-01. ETR 26.6% vs statutory 25.17%, up about 110 bps QoQ. No deferred split. |
| F9 | N.A. | No OCI lines in the release. FND-04 points to possible OCI movement for the results-filing A3. |
| F10 | FINDING | FND-02. Implied share count +0.2-0.5% YoY. EPS not shown, so the diluted spread is NOT FOUND. |
| F11 | FINDING | FND-03 (two Sep-2026 net worth values, 7.5% gap). FND-04 (31.4 Cr non-PAT accretion QoQ). |
| F12 | FINDING | Lender reading (loan book as segment): FND-05 PCR thinning, FND-06 DA loss, FND-07 CRAR vs AUM gap, FND-08 branch build vs output, FND-09 fee income. No reported segment table. |
| F13 | N.A. | Cover letter is a Reg 30 press-release intimation (lines 29-34). No board outcome items. |
| F14 | FINDING | FND-10 (H1 disbursements column). FND-11 (labels). FND-03 also counts. |
| F15 | N.A. | No consolidation entity list. Prior ND. |
| F16 | FINDING | FND-12 (credit cost basis unstated). FND-13 (non-disclosure of PCR, mix, tonnage, guidance). Drop-diff not assessable (prior ND). |
| F17 | N.A. | Not a concall. An informational checklist coverage table is given in section 4 for A4. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Intimation and press release uploaded on company website (procedural, not thesis-relevant) | 2026-10-15 | line 36 / R229 | underway ("is also being uploaded") |

No dated operational or financial commitment appears in the document. No FY27 guidance.

## 4. MONITORING CHECKLIST COVERAGE (informational; F17 is N.A. on this doctype)

| # | checklist item | this document | line | status |
|---|---|---|---|---|
| 1 | Credit cost <= 1.1% avg assets; FY27 guidance issued | 0.6%, basis unstated (about 0.58% on avg assets [INFERENCE], FND-12). No guidance. | 131 | Met on implied basis. Guidance absent. |
| 2 | PCR >= 38%, rising (red < 32%) | Not disclosed. Implied about 33% (range 28.6-37.8%), thinning QoQ (FND-05). | 126-127, 130 | NOT DISCLOSED. Implied adverse. |
| 3 | Gold branches 140-150, AUM/branch > Rs 13.3 Cr | Total branches only: 831. | 135, 146 | NOT DISCLOSED |
| 4 | C/I materially below ~57%, falling | 52.5% (Q1 52.8%, Q2FY26 56.9%) | 123 | Met. Pace slowed (-36 bps QoQ). |
| 5 | ROE toward 14-15%, ROA >= 2.5% | ROE 17.0%, ROA 2.8% | 124-125 | Met |
| 6 | GNPA at or below ~1.9-2.1% | 1.8%, +27 bps QoQ | 126, 130 | Met, rising |
| 7 | ST LAP in-housing complete, disbursals > Rs 208 Cr | Not mentioned | - | NOT DISCLOSED |
| 8 | Gold tonnage disclosed and rising | Not mentioned | - | NOT DISCLOSED |
| T1 | Tripwire: credit cost > 1.1% avg assets | about 0.6% | 131 | Not fired (basis caveat) |
| T2 | Tripwire: ROE fails 14% by FY28 | 17.0% Q2, 16.2% H1 | 125 | Not fired |
| T3 | Tripwire: PCR < 32%; override self-withdraws if PCR thins further | Implied PCR thinned QoQ, may be below 32% within rounding | 126-127, 130 | FLAG: the self-withdrawal condition appears met on implied figures. Reported PCR needed. Decision stays human. |

## 5. A4 QUESTION FEED (from FORWARD-SIGNAL and AMBIGUOUS findings)

FND-05, FND-08 (forward signals). FND-01, FND-03, FND-04, FND-06, FND-07, FND-09, FND-12, FND-13 (ambiguous).

```yaml
stage: A3-forensics
company: "FEDFINA"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\q2fy27\\runs\\fedfina-q2fy27\\work\\forensics_pressrelease_fedfina_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FND-01", check: "F8", line: "90-91", classification: "AMBIGUOUS", implication: "ETR 26.6% Q2 vs 25.17% statutory and 25.5% Q1; ~2.5 Cr excess tax; no deferred split; ask cause"}
  - {id: "FND-02", check: "F10", line: "93-94", classification: "NEUTRAL-FACT", implication: "Implied shares (SF/BVPS) +0.2-0.5% YoY, ESOP-consistent; EPS absent so diluted spread NOT FOUND"}
  - {id: "FND-03", check: "F11", line: "93-94", classification: "AMBIGUOUS", implication: "Sep-2026 net worth 3165.0 (Q2 col) vs 2926.1 (H1 col), 7.5% gap; basis differs from BVPS row; ask basis"}
  - {id: "FND-04", check: "F11", line: "92-93", classification: "AMBIGUOUS", implication: "SF +162.2 Cr QoQ vs PAT 130.8 Cr; 31.4 Cr non-PAT accretion (OCI/FVOCI on DA pools?); needs equity statement"}
  - {id: "FND-05", check: "F12", line: "89, 126-127, 130", classification: "FORWARD-SIGNAL", implication: "GS3 +27bps, NS3 +22bps, credit cost -20.5% QoQ; implied PCR ~37.5% to ~33% (range 28.6-37.8%); incremental cover ~19%; Pillar 2L self-withdrawal condition ('PCR thins further') appears met on implied figures; credit cost catch-up risk"}
  - {id: "FND-06", check: "F12", line: "83", classification: "AMBIGUOUS", implication: "Net DA gain negative two quarters (-12.9, -1.2; H1 -14.0); EIS reversal or fair-value loss; ask if assignment paused, pool size, run-rate"}
  - {id: "FND-07", check: "F12", line: "93, 102, 128", classification: "AMBIGUOUS", implication: "AUM +36.6% YoY, SF +16.8%, CRAR only -68bps; implied RWA growth ~20%; ask on/off-book AUM, Tier 2, raise horizon"}
  - {id: "FND-08", check: "F12", line: "102-103, 135-136", classification: "FORWARD-SIGNAL", implication: "+74 branches, +544 staff in one quarter while disbursements -1.2% QoQ; AUM/branch 27.9 to 26.5 Cr; opex drag ahead; gold-branch split undisclosed"}
  - {id: "FND-09", check: "F12", line: "85", classification: "AMBIGUOUS", implication: "Other income -1.9% YoY, -10.1% H1 against AUM +36.6%; fee/cross-sell shrinking; ask composition"}
  - {id: "FND-10", check: "F14", line: "103", classification: "NEUTRAL-FACT", implication: "H1 disbursement cells repeat Q2 flow (6,676 vs Q1+Q2 13,436); column unusable; true H1 NOT FOUND"}
  - {id: "FND-11", check: "F14", line: "83, 126, 130", classification: "NEUTRAL-FACT", implication: "'Net Gain' label on losses; 'Gross NPA' vs 'Gross Stage III' for same figure; four drafting inconsistencies cumulatively"}
  - {id: "FND-12", check: "F16", line: "131", classification: "AMBIGUOUS", implication: "Credit cost 0.6% with no denominator; ~0.58% on ROA-implied avg assets, ~0.50% on avg AUM; tripwire not fired on implied basis; confirm basis and Q1 comparable"}
  - {id: "FND-13", check: "F16", line: "74, 120-131, 144", classification: "AMBIGUOUS", implication: "No PCR, product mix, gold tonnage, gold branches, ST LAP, FY27 guidance; 5 of 8 checklist items undisclosed; drop-diff not assessable (prior ND)"}
forward_signals: ["FND-05", "FND-08"]
ambiguous: ["FND-01", "FND-03", "FND-04", "FND-06", "FND-07", "FND-09", "FND-12", "FND-13"]
commitments:
  - {commitment: "Press release and intimation uploaded on company website (procedural)", implied_date: "2026-10-15", ref: "line 36 / R229", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Headline is strong: ROE 17.0%, ROA 2.8%, C/I 52.5%, and every disclosed checklist ratio is met. The forensic weight sits in what the 2-page release omits. Stage 3 rose (+27/+22 bps) while credit cost fell 20.5% QoQ. Implied PCR thinned from about 37.5% to about 33%, inside a rounding band that crosses the 32% red line. The Notion override text self-withdraws Pillar 2L to 0.80x if PCR thins further, so FND-05 is the load-bearing item. It is an inference from rounded ratios; reported PCR and Q2 write-offs decide it. Second cluster: DA losses two quarters running, 31.4 Cr net worth accretion beyond PAT, and CRAR barely moving against 36.6% AUM growth. Together these hint at off-book or FVOCI mechanics that the results filing must explain. The branch build (+74) ran ahead of disbursements (-1.2% QoQ). H1 disbursement and H1 net worth columns are unusable. Pipeline notes: A1 line drift on R204-R208 (+1 line); A2 mislabelled R134-R136 as stock duplicates."
```
