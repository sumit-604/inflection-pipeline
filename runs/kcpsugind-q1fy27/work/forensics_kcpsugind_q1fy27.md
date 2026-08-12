# A3 FORENSIC NOTES — K.C.P. Sugar and Industries Corporation Ltd (KCPSUGIND) — Q1 FY27 — DOCTYPE: results

Source A1 extract: `runs/kcpsugind-q1fy27/work/extract_results_kcpsugind_q1fy27.txt`
Reconciled against A2 ledger: `runs/kcpsugind-q1fy27/work/ledger_results_kcpsugind_q1fy27.md`
OCR-suspect cells confirmed against source PDF pages 3-4 via Read page rendering.
Ledger reconciliation: 117/117 enumerated disclosure units read at their cited lines = 100%.
Unit: Rs Lakhs (x0.01 = Rs Crores). All line cites are A1-extract lines unless "PDF p." is stated.

---

## 0. OCR-SUSPECT CONFIRMATION (A2 ARITHMETIC_CHECK / OCR_SUSPECT — resolved against PDF pages 3-4)

Every A2-flagged cell was rendered from the source PDF and is an **OCR artifact**, not a filing
error. The clean printed values are:

| A2 flag (line) | OCR text in extract | PDF printed value | Verdict |
|---|---|---|---|
| Segment Assets, Sugar standalone Year-Ended (241) | 43896.65 | **13896.65** | OCR-ARTIFACT (spurious "4" prefix); matches its own 31.03.2026 quarter column 13896.65 |
| Segment Assets, Power & Fuel standalone Year-Ended (243) | 4436.47 | **1436.47** | OCR-ARTIFACT (1->4 prefix drift) |
| Segment Assets Total standalone (247) | 53314.14 | 53314.14 | CONFIRMED — total is correct; foots with corrected components (13896.65+3068.96+1436.47+2941.45+2538.96+29431.65 = 53314.14) |
| Segment Liabilities, Power & Fuel consolidated Year-Ended (252) | 46.30 | **16.30** | OCR-ARTIFACT (1->4) |
| Capital Employed Total consolidated 30.06.2025 (265) | 4694133 | **46941.33** | OCR-ARTIFACT (dropped decimal point) |
| P&L (iii) Equity Instruments Through OCI, consolidated current qtr (182-183) | 434,41 | **134.41** | OCR-ARTIFACT (1->4); net OCI ties: 134.41 - 18.70 tax = 115.71 total (line 184) |
| P&L IX Continuing Ops, consolidated current qtr (170) | "4624." / "261 77" | **4624.77** | CONFIRMED as 4624.77 |
| Segment Engineering revenue, consolidated current qtr (219) | 1174.13 | **1171.13** | OCR-ARTIFACT (minor); use 1171.13 |

None of the flagged cells is a genuine digit-insertion by the company. Arithmetic integrity of the
segment tables is intact once OCR is corrected. No ARITHMETIC_CHECK finding survives confirmation.

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / PDF | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F2-01 | F2 | P&L r24 (PAT); Seg 4.2 r229 (Eng result) | 176; 219/229 | "Profit / (Loss) For The Period ... 4556.47 ... 4624.77"; Eng result "4.32 ... 135.28" | FORWARD-SIGNAL | S-vs-C PAT gap collapsed to +68.30 L (1.5% of SA PAT) from +152.69 L (8.7%) a year ago while the revenue gap WIDENED (988.78 L vs 402.01 L). Subsidiary (Eimco) profit contribution is evaporating even as its revenue grows — margin compression at the re-rating engine. |
| A3-F5-01 | F5 | LRR SA para 4-5 / CONS para 4-5 | 332-343; 436-447 | "the remaining expenses that are relatable to the sugar ... will be absorbed at the end of the last quarter ... i. Other expenditure Rs.943.99 ii. Depreciation Rs.58.11" | FORWARD-SIGNAL | Emphasis-of-matter-style seasonal-deferral paragraph, verbatim-identical amounts in both reports (Rs 943.99 L + Rs 58.11 L = Rs 1,002.10 L / ~Rs 10.0 Cr of off-season cost deferred out of Q1 into Q4 FY27). Q1 profit is flattered by ~Rs 10 Cr; the charge lands in the seasonal quarter. Deferral is entirely at the holding/sugar-unit level (no incremental subsidiary deferral). |
| A3-F6-01 | F6 | LRR para 4; Agenda 3; Agenda 5 | 338/442; 61; 100 | "will be absorbed at the end of the last quarter"; "shall be paid / dispatched within 30 days from the date of ensuing AGM"; "The Board approved the Supply contract order of Rs. 1,53,40,01,569" | FORWARD-SIGNAL | Three dateable commitments: (a) deferred cost absorbed by Q4 FY27; (b) dividend dispatch by ~24 Oct 2026 (AGM 24 Sep + 30 days); (c) Rs 153.40 Cr intra-group supply contract approved — an executable order for Eimco. |
| A3-F8-01 | F8 | P&L r15/r17/r18 | 163; 165-166; Note 6 @283 | "Current Tax : -  -  -  -"; SA PBT "5314.34"; "Other Income includes Fair Value Gain on Equity Investments to the tune of Rs.5121.91 Lakhs" | FORWARD-SIGNAL | Standalone ETR 14.3% (757.87/5314.34) vs 25.17% statutory — a ~1,090 bps shield. Zero standalone current tax on Rs 53.1 Cr PBT; entire tax is deferred, sitting on UNREALISED FVTPL gains (Rs 51.22 Cr = 96% of SA PBT). When the equity book is monetised, current/LTCG cash tax crystallises. Earnings quality: strip the MTM and standalone pre-tax operating profit is only ~Rs 1.9 Cr. |
| A3-F9-01 | F9 | P&L r29 (Equity instr. thru OCI) | 182-183 + PDF p3 | "(iii) Equity Instruments Through Other Comprehensive Income ... 134.41 (116.37) (1.77) (148.84)" | FORWARD-SIGNAL | Consolidated FVOCI equity reserve swung to +134.41 L this quarter (sign-flip from -1.77 L year-ago quarter and negative in every prior period shown; magnitude ~= full prior-year -148.84 L). Market-driven, not actuarial. Both books (P&L FVTPL + OCI FVOCI) rode a strong equity quarter; a down market reverses both simultaneously. Standalone routes equity gains through P&L, consolidated splits some through OCI — the S-vs-C divergence A2 flagged. |
| A3-F12-01 | F12 | Seg 4.3 r244; 4.4 r253/r250 | 244; 253; 250 | Eng consol assets "15269.34 ... 11964.27"; Eng consol liab "4087.92 ... 2263.55"; Sugar liab "5515.33 ... 3172.82" | AMBIGUOUS | Engineering (Eimco) consolidated assets +27.6% YoY and liabilities +80.6% YoY while its segment result fell 58% YoY = working-capital-funded order ramp with margin compression (advances/creditors building ahead of recognised profit). Sugar segment liabilities +73.9% YoY (cane dues vs WC — unresolved). Both need concall questions. |
| A3-F13-01 | F13 | Agenda 2 (AGM) | 52-55 | "The 31st AGM of the Company is scheduled to be held on Thursday, 24th September 2026" | NEUTRAL-FACT | AGM 24 Sep 2026 => full FY26 Annual Report drops within ~6 weeks => schedule a Role 6 AR Deep Dive event (balance sheet, investment-book carrying value, RPT schedule, cash flow all become visible). |
| A3-F13-02 | F13 | Agenda 4 (Record date) | 87-94 | "Record Date Thursday, 17th September 2026 ... Book Closure Friday, 18th September 2026 to Thursday, 24th September 2026" | AMBIGUOUS | Record date (Thu 17 Sep) is printed BEFORE the book-closure open date (Fri 18 Sep) — internal date inconsistency as filed. Immaterial to value but a governance/drafting data point; likely a typo, worth a control-quality question. |
| A3-F13-03 | F13 | Agenda 5 (RPT supply contract) | 97-104 | "The Board approved the Supply contract order of Rs. 1,53,40,01,569 ... from The EIMCO-KCP Limited, Wholly owned Subsidiary" | FORWARD-SIGNAL | Rs 153.40 Cr related-party supply contract with the WOS Eimco-KCP. This is NOT the Rs 257 Cr Eimco/Hyundai order — value differs and the filing never names Hyundai or Rs 257 Cr. The thesis's Reg-30 confirmation of the Rs 257 Cr order has NOT arrived in this filing (tripwire — see Section 4). Disclosure gives counterparty/relationship/amount but no arm's-length statement and no Reg 23 shareholder-approval reference (intra-group WOS is largely RPT-exempt, but Rs 153.40 Cr is material vs ~Rs 260 Cr group revenue). |
| A3-F14-01 | F14 | Agenda 5; Annexure-1 #3 | 100-104; 98; 518 | "supply of engineering parts via KCP Sugar and Industries Corporation Limited, Thuvakkudi"; "The EIMCO-KCP Limited" vs "THE EIMCO-K.C.P Limited" | AMBIGUOUS | Supply-contract direction is ambiguously drafted ("order ... from EIMCO-KCP ... for supply ... via KCP Sugar") — unclear whether the parent is buyer, seller or pass-through conduit; the Rs value flows intra-group either way. Entity-name variant (EIMCO-KCP vs EIMCO-K.C.P) across tables. Individually immaterial, cumulatively a drafting/governance data point; the contract direction needs a management question. |
| A3-OI-01 | F8 (quality) | P&L r2 (Other Income); Note 6 | 148; 283 | "Other Income 5477.56 ... "; "Fair Value Gain on Equity Investments to the tune of Rs.5121.91 Lakhs" | FORWARD-SIGNAL | 93.5% of standalone Other Income and 96% of standalone PBT is non-operating unrealised MTM on the equity book. Year-ago the FV gain was Rs 2,280.52 L (87% of Other Income); Q4 FY26 Other Income was NEGATIVE (-952.74 L) i.e. an MTM loss quarter. Reported PAT is a leveraged bet on quarter-end equity prices, not on the operating businesses. |

---

## 2. CHECKLIST SCORECARD (F1-F17, every check one status)

| # | Status | Basis (one line) |
|---|---|---|
| F1 | PASS | 8 ZERO_STANDING rows all read; every one is a standing Ind-AS template line nil across ALL comparative periods (Exceptional Items 162; Discontinued Ops 171-175; SA Current Tax 165; SA Reversal-earlier-years 167-168; SA Equity-instr-OCI 182-183; Seg Unallocated result 231; EPS-discontinued 195-196). None went non-zero->zero, so none is a suppressed/newly-nil line. The Exceptional Items line is the standing vehicle for any future profit-on-sale-of-investment/subsidiary given the Rs 332 Cr book — noted, not an issue this quarter. |
| F2 | FINDING | A3-F2-01: S-vs-C PAT gap collapsed to 1.5% from 8.7% of SA PAT YoY while revenue gap widened; Eimco profit contribution evaporating. |
| F3 | PASS | Cost lines differ SA vs CONS (Materials 2108.86 vs 2671.56 @151; Employee 152.81 vs 429.01 @156; Depn 56.11 vs 89.88 @158) => Eimco is a real operating subsidiary, not a shell. Quality Engineering step-down is tiny (income Rs 28.93 L, loss Rs 5.49 L @472-475) but component-audited; no Going Concern EoM anywhere. |
| F4 | PASS | Consolidated Other-Matters para 7 (472-479): only 1 step-down subsidiary not reviewed by principal auditor (Quality Engineering); net loss Rs 5.49 L = 0.12% of consolidated PAT 4624.77 L — far below 10%, and it is component-auditor-reviewed, not management-furnished. |
| F5 | FINDING | A3-F5-01: seasonal-deferral emphasis paragraph, Rs 1,002.10 L off-season cost deferred out of Q1 into Q4 FY27; verbatim-identical across SA/CONS reports. (No prior-quarter extract supplied, so no QoQ scope diff possible — noted.) |
| F6 | FINDING | A3-F6-01: commitment register built — deferred cost absorbed by Q4 FY27; dividend dispatch ~24 Oct 2026; Rs 153.40 Cr supply contract board-approved. |
| F7 | PASS | Only procedural/boilerplate hedges present: Note 1 seasonal caveat "can neither be construed as an indicator of the overall annual operations" (268-269) and "subject to the approval of shareholders" (84). No NEWLY-ADDED hedge on revenue lumpiness or customer concentration (no prior-quarter to diff; none reads as pre-emptive cover beyond the standing seasonal note). |
| F8 | FINDING | A3-F8-01 + A3-OI-01: SA ETR 14.3%, zero current tax on Rs 53.1 Cr PBT, entire tax deferred on unrealised MTM => future cash-tax crystallisation; earnings 96% MTM-dependent. "Tax relating to earlier years" is NIL both books this quarter (9.61 L only in prior periods) — no earlier-years finding this quarter. |
| F9 | FINDING | A3-F9-01: consolidated FVOCI equity reserve +134.41 L single-quarter swing (sign-flip, ~= full prior year), market-driven; OCR-corrected from 434.41. |
| F10 | PASS | Paid-up capital 1133.85 L unchanged all periods/both books (190); Basic = Diluted EPS (no spread, no dilutive instruments); no corporate action. |
| F11 | PASS | Net worth ties out cleanly: SA Other Equity 35060.35 + 1133.85 = 36194.20 vs SA Capital Employed 36194.21 (191, 265); CONS 44817.27 + 1133.85 = 45951.12 vs CONS Capital Employed 45951.11. Gap <0.01%. No third-party number in filing to reconcile against. |
| F12 | FINDING | A3-F12-01: Engineering consol assets +27.6% / liabilities +80.6% YoY with result -58% (WC-funded order ramp + margin compression); Sugar liabilities +73.9% YoY (ambiguous). |
| F13 | FINDING | A3-F13-01/02/03: AGM 24 Sep => AR deep-dive schedule; record-date/book-closure date inconsistency; Rs 153.40 Cr RPT supply contract; note dividend Re 0.10 (Rs 1.13 Cr, ~10% of consol PAT) is paid despite a standalone FY26 loss (-261.86 L) i.e. from reserves. |
| F14 | FINDING | A3-F14-01: ambiguous supply-contract direction wording + EIMCO-KCP entity-name variant across tables. |
| F15 | N.A. | Consolidation list is 4 entities (516-519) and internally cross-consistent (Eimco = agenda-5 counterparty; Quality Engineering = para-7 unreviewed step-down), but NO prior-quarter entity list was supplied, so additions/deletions/reclassifications cannot be diffed this run (A2 marks ENTITY_CHANGE N/A). |
| F16 | N.A. | Doctype = results, not a presentation. |
| F17 | N.A. | Doctype = results, no concall transcript. Monitoring-checklist silence captured narratively in Section 4 (items 3/5/7/8 not disclosable from a quarterly results filing). |

Scorecard tally: FINDING x8 (F2,F5,F6,F8,F9,F12,F13,F14) | PASS x6 (F1,F3,F4,F7,F10,F11) | N.A. x3 (F15,F16,F17). No blanks. GATE A3: pass.

---

## 3. COMMITMENT REGISTER (from F6)

| commitment | implied date | note/ref | status word |
|---|---|---|---|
| Off-season expenses (Rs 943.99 L other + Rs 58.11 L depn) "will be absorbed at the end of the last quarter" | Q4 FY27 (Jan-Mar 2027) | LRR para 4, lines 338 / 442 | underway (deferred, pending absorption) |
| Final dividend Re 0.10/share "shall be paid / dispatched within 30 days from the date of ensuing AGM" | ~24 Oct 2026 (AGM 24 Sep +30d) | Agenda 3, line 61 | board-approved (subject to member approval) |
| 31st AGM "is scheduled to be held" via VC/OAVM | 24 Sep 2026 | Agenda 2, line 54 | scheduled |
| Record date fixed for dividend eligibility | 17 Sep 2026 (book closure 18-24 Sep) | Agenda 4, lines 89-91 | board-approved |
| "The Board approved the Supply contract order of Rs. 1,53,40,01,569" with WOS Eimco-KCP | executable now | Agenda 5, line 100 | board-approved |

---

## 4. RESOLUTION OF A2-FLAGGED ITEMS & MONITORING CHECKLIST

**A2 ZERO_STANDING (8 rows):** No suppressed/newly-nil line. All 8 are standing Ind-AS template rows nil
across every comparative period (see F1). The Exceptional Items line (162) and Profit-on-sale lines are
absent — no exceptional monetisation of the investment book or subsidiary this quarter.

**A2 RELATED_PARTY (Rs 153.40 Cr Eimco-KCP supply contract):** Disclosed as agenda item 5 (line 100).
It is a SEPARATE item from the Rs 257 Cr Eimco/Hyundai order, NOT the same — value differs and Hyundai /
Rs 257 Cr are never named in the filing. Disclosure states counterparty (WOS), relationship and amount
but omits any arm's-length assertion or Reg 23 approval path. See A3-F13-03 / A3-F14-01.

**A2 Other Income concentration (Note 6, 93.5% FV gain):** Confirmed and escalated — A3-OI-01: it is 96%
of standalone PBT and entirely unrealised MTM; Q4 FY26 was an MTM-loss quarter, so PAT swings with
quarter-end equity prices. Earnings-quality FORWARD-SIGNAL.

**A2 ARITHMETIC_CHECK / OCR_SUSPECT (5 cells):** All 5 confirmed OCR artifacts against PDF pages 3-4;
clean values in Section 0. Filing arithmetic is intact.

### Notion monitoring checklist (8 items)

1. **Rs 257 Cr order Reg-30 confirmation:** NOT confirmed in this filing. Only a Rs 153.40 Cr intra-group
   supply contract is disclosed (line 100). **TRIPWIRE FIRED.**
2. **Eimco/Engineering PBIT margin >= ~30%:** consolidated Engineering result 135.28 / revenue 1171.13 =
   **11.6%** (vs 39.4% year-ago quarter, 31.3% FY26). **TRIPWIRE FIRED** (<~20%). Lines 219, 229.
3. **Investment book >= Rs 332 Cr:** cannot confirm — no balance sheet in a quarterly results filing.
   Only proxy is Note 6 FV GAIN of Rs 51.22 Cr this quarter (line 283), which points to a marked-UP book,
   not a drawdown. Flag: not directly disclosed.
4. **Sugar segment loss narrowing (not past Rs 25 Cr/yr):** Q1 FY27 Sugar result is a **PROFIT of
   Rs 2.14 Cr** (214.42 L, line 226) vs a Rs 1.07 Cr loss year-ago; FY26 full-year was -Rs 17.3 Cr. No
   deterioration. Not fired.
5. **Consolidated CFO positive:** no cash flow statement in the filing (quarterly omission). **Flag:
   absent** — cannot verify; carry to AR deep-dive.
6. **Engineering revenue resuming YoY growth + recognising order:** consolidated Engineering revenue
   +42.0% YoY (1171.13 vs 824.55, line 219) — YES growing; but standalone engineering division -56.2%
   (186.48 vs 425.45) and the Rs 153.40 Cr order is only just board-approved, not yet in revenue.
7. **Standalone short-term borrowings stable:** no balance sheet; not disclosed. Proxy: standalone
   Finance Costs +36.7% YoY (278.59 vs 203.82, line 157) — consistent with higher borrowing. Flag: absent.
8. **RP deposit share <= ~27% / Schedule V ratifications:** not disclosed in this filing. Flag: absent.

### Standalone vs Consolidated PAT gap (first-class metric)

| Period | Standalone PAT (L) | Consolidated PAT (L) | Gap (L) | Gap % of SA PAT |
|---|---|---|---|---|
| Q1 FY27 (30.06.2026) | 4556.47 | 4624.77 | +68.30 | +1.5% |
| Q1 FY26 (30.06.2025) | 1762.53 | 1915.22 | +152.69 | +8.7% |
| Q4 FY26 (31.03.2026, bal. fig.) | (2130.60) | (1519.60) | +611.00 | n.m. |
| FY26 (year 31.03.2026) | (261.86) | 1113.07 | +1374.93 | n.m. |

Driver: the gap is the net subsidiary contribution, dominated by Eimco engineering. Eimco pre-tax
contribution = consol Eng result - standalone Eng result = 135.28 - 4.32 = **130.96 L** this quarter, vs
175.37 L year-ago and 2,052.32 L in FY26. After consolidated current tax (26.02 L) and the step-down
subsidiary loss (5.49 L), the net PAT uplift is just 68.30 L. **The subsidiary engine that added
Rs 13.75 Cr to FY26 PAT added only Rs 0.68 Cr this quarter** — Eimco is growing its top line but its
profit contribution has collapsed (margin from 31.3% FY26 to 11.6% now). This is the central forensic
read of the quarter and directly undercuts the "Eimco re-rated at 15x" thesis leg.

---

## 5. TRIPWIRES FIRED (for A4/A5)

- **Reg 30 fails to confirm the Rs 257 Cr Eimco/Hyundai order** — FIRED. Filing discloses only a separate
  Rs 153.40 Cr intra-group supply contract; the Rs 257 Cr order remains unconfirmed within the 2-quarter
  watch window. (A3-F13-03)
- **Eimco/Engineering PBIT margin <~20%** — FIRED at 11.6% (from 31.3% FY26 / 39.4% year-ago). (A3-F2-01,
  A3-F12-01)

Not fired: sugar annual PBIT-loss > Rs 25 Cr (Q1 sugar +Rs 2.14 Cr); FVTPL material drawdown (Rs 51.22 Cr
GAIN this quarter). Cannot assess from this doctype: investment-book drawdown >20%, consolidated CFO
second consecutive negative year (no balance sheet / cash flow in a quarterly results filing).

FORWARD-SIGNAL findings for A4 to convert into management questions: A3-F2-01, A3-F5-01, A3-F6-01,
A3-F8-01, A3-F9-01, A3-F13-03, A3-OI-01.
AMBIGUOUS findings for A4: A3-F12-01, A3-F13-02, A3-F14-01.

---

```yaml
stage: A3-forensics
company: "kcpsugind"
quarter: "q1fy27"
doctype: "results"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/kcpsugind-q1fy27/work/forensics_kcpsugind_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: PASS
  F4: PASS
  F5: FINDING
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-F2-01", check: "F2", line: "176;219;229", classification: "FORWARD-SIGNAL", implication: "S-vs-C PAT gap collapsed to 1.5% from 8.7% of SA PAT YoY while revenue gap widened; Eimco profit contribution evaporating"}
  - {id: "A3-F5-01", check: "F5", line: "332-343;436-447", classification: "FORWARD-SIGNAL", implication: "Seasonal-deferral emphasis para: Rs 1002.10 L off-season cost deferred out of Q1 into Q4 FY27, identical in both reports; Q1 profit flattered ~Rs 10 Cr"}
  - {id: "A3-F6-01", check: "F6", line: "338;61;100", classification: "FORWARD-SIGNAL", implication: "Dateable commitments: deferred cost absorbed by Q4 FY27; dividend dispatch ~24 Oct 2026; Rs 153.40 Cr supply contract approved"}
  - {id: "A3-F8-01", check: "F8", line: "163;165-166;283", classification: "FORWARD-SIGNAL", implication: "SA ETR 14.3%, zero current tax on Rs 53.1 Cr PBT, all tax deferred on unrealised MTM; future cash-tax crystallisation; earnings 96% MTM-dependent"}
  - {id: "A3-F9-01", check: "F9", line: "182-183", classification: "FORWARD-SIGNAL", implication: "Consolidated FVOCI equity reserve +134.41 L single-quarter sign-flip (~full prior year); market-driven, reverses on a down quarter; OCR-corrected from 434.41"}
  - {id: "A3-F12-01", check: "F12", line: "244;253;250", classification: "AMBIGUOUS", implication: "Engineering consol assets +27.6% / liabilities +80.6% YoY with result -58% (WC-funded order ramp + margin compression); Sugar liabilities +73.9% YoY"}
  - {id: "A3-F13-01", check: "F13", line: "52-55", classification: "NEUTRAL-FACT", implication: "AGM 24 Sep 2026 => FY26 Annual Report within ~6 weeks => schedule Role 6 AR Deep Dive"}
  - {id: "A3-F13-02", check: "F13", line: "87-94", classification: "AMBIGUOUS", implication: "Record date 17 Sep printed before book-closure open 18 Sep; internal date inconsistency / control-quality question"}
  - {id: "A3-F13-03", check: "F13", line: "97-104", classification: "FORWARD-SIGNAL", implication: "Rs 153.40 Cr RPT supply contract with WOS Eimco-KCP is NOT the Rs 257 Cr Hyundai order; Reg-30 confirmation of Rs 257 Cr order absent (tripwire); no arm's-length/Reg 23 disclosure"}
  - {id: "A3-F14-01", check: "F14", line: "100-104;98;518", classification: "AMBIGUOUS", implication: "Ambiguous supply-contract direction wording + EIMCO-KCP entity-name variant across tables; cumulative drafting/governance data point"}
  - {id: "A3-OI-01", check: "F8", line: "148;283", classification: "FORWARD-SIGNAL", implication: "93.5% of SA Other Income and 96% of SA PBT is non-operating unrealised MTM on equity book; Q4 FY26 was an MTM-loss quarter; PAT swings with quarter-end equity prices"}
forward_signals: ["A3-F2-01","A3-F5-01","A3-F6-01","A3-F8-01","A3-F9-01","A3-F13-03","A3-OI-01"]
ambiguous: ["A3-F12-01","A3-F13-02","A3-F14-01"]
commitments:
  - {commitment: "Off-season expenses Rs 1002.10 L will be absorbed at end of last quarter", implied_date: "Q4 FY27", ref: "LRR para 4 line 338/442", status_word: "underway"}
  - {commitment: "Final dividend Re 0.10/share dispatched within 30 days of AGM", implied_date: "2026-10-24", ref: "Agenda 3 line 61", status_word: "board-approved"}
  - {commitment: "31st AGM held via VC/OAVM", implied_date: "2026-09-24", ref: "Agenda 2 line 54", status_word: "scheduled"}
  - {commitment: "Record date fixed for dividend eligibility", implied_date: "2026-09-17", ref: "Agenda 4 line 89", status_word: "board-approved"}
  - {commitment: "Rs 153.40 Cr supply contract with WOS Eimco-KCP approved", implied_date: "executable now", ref: "Agenda 5 line 100", status_word: "board-approved"}
gate_a3: pass
blank_checks: []
```
