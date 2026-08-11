# FORENSIC NOTES — concall — raymondrealty — Q1 FY27

Agent: A3 FORENSIC NOTES | Model: claude-opus-4-8 | Doctype: **concall**
A1 extract: `extract_concall_raymondrealty_q1fy27.txt` (217 orig lines; dialogue L13-L217)
A2 ledger: `ledger_concall_raymondrealty_q1fy27.md`
Line convention: **all `Lnn` cites are the ORIGINAL transcript line number** (the number preceding the tab in the A1 extract), matching the A2 ledger convention. `Tn` = turn number in Section B.

Ledger reconciliation: **100%** — every ledger row read at its cited line before judging (Participants P1-P15, Turns T1-T103, Questions Q1a-Q10b, Numbers N1-N71, Commitments/Hedges C1-C19, and all Section F data-quality flags).

Doctype applicability applied per the checklist: on a concall **F6 / F7 / F17 apply** and most balance-sheet checks (F1-F5, F8-F10, F12, F13, F16) are N.A. F11, F14, F15 were run because the call itself surfaced leverage, naming, and entity-incorporation content; each is marked with its basis below.

---

## FINDINGS TABLE

| id | check | ledger row ref | line / turn | verbatim quote (short) | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F6 | C7 / N57 / N58 | T19/L49; T25/L61 | "we are on track to launch two of the Mahin projects this year ... first one ... latter part of Q3 ... then Q4 ... second Mahim" | FORWARD-SIGNAL | Dated launch milestones: Mahim-1 Q3 (Nov-Dec FY27), Mahim-2 Q4 (Feb-Mar). Trackable next quarter; Mahim-2 sits at the FY27 tail = slippage risk (Notion monitor #4). |
| FND-02 | F6 | C6 / N55 | T15/L41 | "the Parel project ... close to about 18 months away as far as hitting the market" | FORWARD-SIGNAL | Parel (₹8,500cr GDV, flagship SoBo) contributes no revenue until ~H2 FY28+; near-term pipeline is the 4 launched + 2 Mahim. |
| FND-03 | F6 | C8 / N61 | T25/L61 | "six JDAs would have been launched by the end of this year which is FY27 out of the total eight" | FORWARD-SIGNAL | Promise-vs-delivery: 4 launched now → 6 by FY27-end (the 2 incremental = the 2 Mahim). Direct Role-5 tracker row. |
| FND-04 | F6 | N12 vs N15 / C1 | T3/L17 | "margins ... expanded from 11% to 13% ... firmly and completely on track to achieving our full-year ... guidance of 17 to 19%" | FORWARD-SIGNAL | Q1 EBITDA margin 13% vs full-year 17-19% guide implies H2 must run materially above 19%; steep back-ended ramp = margin-bridge risk. Notion monitor #1 (13% is below the 18% green line). |
| FND-05 | F6 (guidance) | N68 vs N50 / C10 | T28/L67 | "for the last 6 years ... our ROC has been upward of 25% ... going forward we are making a commitment of 20%" | AMBIGUOUS | Forward ROC guidance (≥20%) steps DOWN from the >25% six-year history. Return-profile derating during the growth push; unexplained. → A4 question. |
| FND-06 | F7 | C15 / C16 | T89/L189 | "we have not given any guidance on net profit ... we don't have a policy just now of giving that out ... Let me not give you a number" | CONFIRMATORY-NEGATIVE | EBITDA guided but PAT/OCF explicitly refused, while interest cost admittedly grows faster than EBITDA. Bottom-line/cash-conversion opacity; caps confidence per CLAUDE.md INDETERMINATE cash-conversion rule. |
| FND-07 | F7 | C11 / C13 / C14 / C19 | T55/L121; T99/L209 | "don't have it readily available ... don't hold me to it ... we will share a better number ... put a disclosure out" | AMBIGUOUS | Full-year interest cost hedged ~5x (~₹100-120cr); no CFO/IR present to give the live number; management promised a separate disclosure = trackable commitment + finance-data-availability gap. → A4 question. |
| FND-08 | F11 | N16 / N17 / N18 | T3/L17 | "debt to equity ratio of 7% ... This number 7X is comfortably below our internal target of 1x" | AMBIGUOUS | D/E stated as both "7%" and "7X" against a 1x ceiling. Net worth cannot be tied out: implied equity swings from ~₹118cr (7X) to ~₹11,770cr (0.07x) off net debt ₹824cr. Units inconsistent within one sentence. → A4 question. |
| FND-09 | F6 | N23 | T3/L17 | "at least ... 6 to 7 years of growth is already there ... work for at least 7 to 8 years going forward" | AMBIGUOUS | Growth-visibility horizon stated two ways in the same turn (6-7 vs 7-8 yrs). Minor, but flag to pin the actual pipeline runway. → A4 question. |
| FND-10 | F15 | Q3a / T23 answer | T22/L55 → T23/L57 | "we have many SPVS and ... in anticipation of new projects we have to keep SPVS ready ... 10X Mahalakmi Limited" | FORWARD-SIGNAL | New SPV incorporated ahead of an undisclosed deal ("whenever there is a deal signed we will come back and you'll be the first ones to know"). Pipeline signal; watch for a new JDA/RPT next quarter. |
| FND-11 | F17 | Notion monitor #6 | L13-L217 (absent) | related-party loans to subsidiaries — not raised by anyone | CONFIRMATORY-NEGATIVE | ₹1,000-1,200cr related-party sub-loan monitor untouched on a debt-heavy quarter; sustained silence on a live governance monitor. |
| FND-12 | F17 | Notion monitor #7 | L13-L217 (absent) | Raymond Ltd promoter governance (JK House / Vijaypat / Singhania) — not raised | AMBIGUOUS | Promoter-governance monitor untouched; consistent silence. Note: the only ownership-governance thread raised was the FII/DII decline (T93/L197), not the promoter dispute. |
| FND-13 | F17 | Notion monitor #9 | L13-L217 (absent) | Thane commercial optionality — not raised (only Thane residential discussed) | CONFIRMATORY-NEGATIVE | 12-month silence window advancing toward expiry of the Thane commercial-optionality leg of the thesis. |
| FND-14 | F17 | Notion monitor #10 / C15 / C17 | T89/L189; T92/L195 | "I don't have that number just now so I can't answer it but I can get back to you" | CONFIRMATORY-NEGATIVE | No operating-cash-flow / CFO trajectory given despite two direct asks. FTTCP cash-conversion DECLINING verdict left unrebutted at the pre-committed binary-gate quarter. |
| FND-15 | F17 | P2 / P3 (MGMT_ABSENCE) | T8/L27 → T9/L29 | "Ankor is traveling uh so he may not be able to get proper connectivity" | AMBIGUOUS | Group CFO (P2, zero turns entire call) and CFO (P3, traveling) both silent; every debt/finance/interest question fielded by the MD. Finance-function accessibility gap on the quarter it mattered most. → A4 question. |
| FND-16 | F17 / F6 | Notion monitor #3 / N16 / N70 | T39/L89; T34/L79; T43/L97 | "this debt may not moderate for another 1 two years ... No, absolutely" | CONFIRMATORY-NEGATIVE | Net debt rose to ₹824cr (gross ₹1,095cr); management confirms elevated debt and interest persist ~1-2 more years. Directly confirms the FTTCP ~2-more-years-negative-CFO thesis and pressures Notion monitor #3 (>₹1,000cr by Q2). |
| FND-17 | F17 / F7 | Q10a / C19 | T97/L205; T98/L207 | "interest expense on dues to government ... the 9.6% math ... works out to a cost of about 20 crores and the balance ..." | AMBIGUOUS | Headline 9.6% cost of debt understates true finance burden: a separate ~₹45cr FY26 "dues to government" interest leg (at 8-9%) sits outside the bank-rate narrative. Effective finance cost higher than the 9.6% framing. → A4 question. |

---

## CHECKLIST SCORECARD (all 17)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | **N.A.** | Concall carries no financial-statement template; no `ZERO_STANDING` ledger rows exist. |
| F2 STANDALONE vs CONSOLIDATED | **N.A.** | No standalone/consolidated statements in a transcript; nothing to decompose. |
| F3 SHELL-ENTITY DETECTION | **N.A.** | No cost lines to compare S-vs-C. SPVs mentioned qualitatively (10X Mahalakshmi) but no operational data → routed to F15. |
| F4 UNAUDITED CONTRIBUTION RATIO | **N.A.** | No auditor's Other Matters in a concall. |
| F5 GOING CONCERN / EoM SCOPE | **N.A.** | No EoM/going-concern paragraph in a transcript. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | Dense dated commitments (FND-01/02/03/04/05/09); full register below. |
| F7 HEDGE PHRASE MINING | **FINDING** | PAT/OCF guidance refused (FND-06); interest cost hedged ~5x (FND-07). |
| F8 TAX FORENSICS | **N.A.** | No ETR / deferred-tax / prior-year-tax data disclosed on the call. |
| F9 OCI FORENSICS | **N.A.** | No OCI / actuarial data in a concall. |
| F10 SHARE COUNT & DILUTION | **N.A.** | No paid-up capital / EPS / warrant / ESOP data. FII+DII holding decline (20-22%→~8%, T93/L197) is an ownership fact, not a dilution mechanic; management explicitly avoids equity dilution (T89/L189). |
| F11 RESERVES / NET-WORTH TIE-OUT | **FINDING** | D/E ratio internally inconsistent ("7%" vs "7X" vs 1x ceiling); net worth cannot be tied out (FND-08). |
| F12 SEGMENT FORENSICS | **N.A.** | No segment assets/liabilities tables in a concall. |
| F13 BOARD OUTCOME BEYOND RESULTS | **N.A.** | No AR/AGM/record-date/director-term content. SPV incorporation captured in F15. |
| F14 NOTE DRAFTING INCONSISTENCIES | **PASS** | Name variances L5 "Sani"/"Swani" and L8 "Saburval"/"Sani Desa" are ASR artifacts (Amit Saburval confirmed genuine at L199; single-person spelling variance for the MD). No note-vs-auditor or genuine entity-name inconsistency exists in a transcript. Substantive numeric inconsistencies routed to F11 (D/E) and F6 (growth horizon). |
| F15 ENTITY LIST DIFFS | **FINDING** | New SPV "10X Mahalakshmi Limited" incorporated, kept ready ahead of an undisclosed deal (FND-10). |
| F16 PRESENTATION-SPECIFIC | **N.A.** | Doctype is concall, not a presentation deck. |
| F17 CONCALL SILENCE AUDIT | **FINDING** | Notion monitors #6, #7, #9, #10 not addressed; both CFOs silent; net-debt/interest deterioration confirmed (FND-11 through FND-17). Table below. |

Scorecard tally: **FINDING = 5** (F6, F7, F11, F15, F17) · **PASS = 1** (F14) · **N.A. = 11** (F1-F5, F8-F10, F12, F13, F16). 17/17 marked; no blanks.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Full-year EBITDA margin 17-19% | FY27 | T3/L17; T28/L67; T74/L159; T89/L189 | on track (Q1 actual 13%) |
| Pre-sales growth ≥20% YoY ("minimum") | FY27 | T3/L17 | committed |
| Revenue growth ≥20% YoY ("minimum") | FY27 | T3/L17 | committed |
| ROCE ≥20% | FY27 | T3/L17; T28/L67 | committed (down from >25% 6-yr history) |
| Debt-to-equity ≤1x discipline | ongoing | T3/L17; T9/L29; T72/L155 | maintained |
| Parel project to market (~18 months) | ~H2 FY28 | T15/L41 | underway (signed, planning/approvals) |
| Mahim-1 launch | Q3 FY27 (Nov-Dec) | T19/L49; T25/L61 | on track |
| Mahim-2 launch | Q4 FY27 (Feb-Mar) | T19/L49; T25/L61 | on track |
| 6 of 8 JDAs launched | by FY27-end | T25/L61 | in progress (4 launched) |
| JDA margins scale to ~20% as projects mature | FY28 | T74/L159 | future |
| Disclose exact FY27 interest-cost number | "give us some time" | T55/L121; T99/L209 | promised / pending |
| Bring in project-level PE / institutional investor | no date given | T95/L201 | initiated (vague, no mechanism) |

---

## F17 — WHAT WAS NOT DISCUSSED (silence audit vs Notion monitor + F6 commitments)

| topic | source monitor | discussed? | consecutive-Q silence | note |
|---|---|---|---|---|
| Q1 EBITDA margin | Notion #1 | YES (13%, T3/L17) | 0 | Below 18% green line; single-Q so far. |
| Booking value | Notion #2 | YES (₹700cr, T3/L17) | 0 | Above ₹500cr green. |
| Net debt trajectory | Notion #3 | YES (₹824cr net / ₹1,095cr gross, T39/L89) | 0 | Rising; mgmt confirms no moderation ~1-2 yrs (FND-16). |
| Mahim 1 & 2 launch | Notion #4 | YES (Q3/Q4, T19/L49) | 0 | Mahim-2 at FY27 tail. |
| New JDA signings vs ₹8,000cr target | Notion #5 | PARTIAL (Parel ₹8,500cr + Kandivali, T25/L61) | — | No progress stated against the aggregate FY27 signing target. |
| Related-party loans to subs | Notion #6 | **NO** (FND-11) | silence continues | Governance monitor untouched. |
| Promoter governance (JK House/Singhania) | Notion #7 | **NO** (FND-12) | silence continues | Only FII/DII decline raised, not promoter dispute. |
| Cost of debt | Notion #8 | YES (9.6%, T3/L17) | 0 | Within 9.5-9.75% band; but "dues to government" leg understates true cost (FND-17). |
| Thane commercial optionality | Notion #9 | **NO** (FND-13) | silence continues | Only Thane residential discussed; optionality window ticking toward expiry. |
| Quarterly CFO / operating cash flow | Notion #10 | **NO — refused** (FND-14) | silence continues | PAT and OCF guidance explicitly declined (FND-06). |
| Finance-function presence (CFO/Group CFO) | F17 add | ABSENT | — | Both CFOs silent; MD fields all finance Qs (FND-15). |

Per Role 5, sustained silence on deteriorating cash/leverage and governance monitors (#6, #7, #9, #10) at the **pre-committed binary-gate quarter** is a confirmatory negative.

---

## HANDOFF TO A4

- **FORWARD-SIGNAL (convert to management questions):** FND-01, FND-02, FND-03, FND-04, FND-10.
- **AMBIGUOUS (convert to management questions):** FND-05, FND-07, FND-08, FND-09, FND-12, FND-15, FND-17.
- **CONFIRMATORY-NEGATIVE (weigh in verdict):** FND-06, FND-11, FND-13, FND-14, FND-16.

```yaml
stage: A3-forensics
company: "raymondrealty"
quarter: "q1fy27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/raymondrealty-q1fy27/work/forensics_raymondrealty_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: PASS
  F15: FINDING
  F16: N.A.
  F17: FINDING
findings:
  - {id: "FND-01", check: "F6", line: "T19/L49; T25/L61", classification: "FORWARD-SIGNAL", implication: "Mahim-1 Q3 / Mahim-2 Q4 FY27 dated launch milestones; Mahim-2 at FY27 tail = slippage risk"}
  - {id: "FND-02", check: "F6", line: "T15/L41", classification: "FORWARD-SIGNAL", implication: "Parel ~18 months to market; no revenue before ~H2 FY28"}
  - {id: "FND-03", check: "F6", line: "T25/L61", classification: "FORWARD-SIGNAL", implication: "6 of 8 JDAs launched by FY27-end (4 done); promise-vs-delivery tracker row"}
  - {id: "FND-04", check: "F6", line: "T3/L17", classification: "FORWARD-SIGNAL", implication: "Q1 margin 13% vs 17-19% FY guide => steep back-ended H2 margin ramp; bridge risk"}
  - {id: "FND-05", check: "F6", line: "T28/L67", classification: "AMBIGUOUS", implication: "Forward ROC guidance 20% steps down from >25% six-year history; unexplained derating"}
  - {id: "FND-06", check: "F7", line: "T89/L189", classification: "CONFIRMATORY-NEGATIVE", implication: "PAT/OCF guidance explicitly refused while interest grows faster than EBITDA; cash-conversion opacity"}
  - {id: "FND-07", check: "F7", line: "T55/L121; T99/L209", classification: "AMBIGUOUS", implication: "Full-year interest cost hedged ~5x; no live figure; disclosure promised = trackable + data gap"}
  - {id: "FND-08", check: "F11", line: "T3/L17", classification: "AMBIGUOUS", implication: "D/E stated as 7% vs 7X vs 1x ceiling; net worth un-tie-outable; implied equity swings 100x"}
  - {id: "FND-09", check: "F6", line: "T3/L17", classification: "AMBIGUOUS", implication: "Growth-visibility horizon 6-7 vs 7-8 years in same turn; pin the runway"}
  - {id: "FND-10", check: "F15", line: "T22/L55; T23/L57", classification: "FORWARD-SIGNAL", implication: "New SPV 10X Mahalakshmi Ltd incorporated ahead of undisclosed deal; watch next-Q JDA/RPT"}
  - {id: "FND-11", check: "F17", line: "L13-L217 (absent)", classification: "CONFIRMATORY-NEGATIVE", implication: "Related-party sub-loans (Notion #6) not addressed; governance-monitor silence"}
  - {id: "FND-12", check: "F17", line: "L13-L217 (absent)", classification: "AMBIGUOUS", implication: "Promoter governance (Notion #7) untouched; only FII/DII decline raised"}
  - {id: "FND-13", check: "F17", line: "L13-L217 (absent)", classification: "CONFIRMATORY-NEGATIVE", implication: "Thane commercial optionality (Notion #9) silent; window nearing expiry"}
  - {id: "FND-14", check: "F17", line: "T89/L189; T92/L195", classification: "CONFIRMATORY-NEGATIVE", implication: "No OCF/CFO trajectory given; FTTCP cash-conversion DECLINING unrebutted at binary-gate quarter"}
  - {id: "FND-15", check: "F17", line: "T8/L27; T9/L29", classification: "AMBIGUOUS", implication: "Group CFO + CFO both silent (one traveling); MD fields all finance Qs; accessibility gap"}
  - {id: "FND-16", check: "F17", line: "T39/L89; T34/L79; T43/L97", classification: "CONFIRMATORY-NEGATIVE", implication: "Net debt 824 / gross 1,095; elevated debt+interest confirmed ~1-2 more yrs; confirms neg-CFO thesis"}
  - {id: "FND-17", check: "F17", line: "T97/L205; T98/L207", classification: "AMBIGUOUS", implication: "9.6% cost-of-debt understates true finance burden; ~45cr dues-to-government leg outside the narrative"}
forward_signals: ["FND-01", "FND-02", "FND-03", "FND-04", "FND-10"]
ambiguous: ["FND-05", "FND-07", "FND-08", "FND-09", "FND-12", "FND-15", "FND-17"]
commitments:
  - {commitment: "EBITDA margin 17-19%", implied_date: "FY27", ref: "T3/L17;T28/L67;T74/L159;T89/L189", status_word: "on-track"}
  - {commitment: "Pre-sales growth >=20% YoY", implied_date: "FY27", ref: "T3/L17", status_word: "committed"}
  - {commitment: "Revenue growth >=20% YoY", implied_date: "FY27", ref: "T3/L17", status_word: "committed"}
  - {commitment: "ROCE >=20%", implied_date: "FY27", ref: "T3/L17;T28/L67", status_word: "committed"}
  - {commitment: "Debt-to-equity <=1x discipline", implied_date: "ongoing", ref: "T3/L17;T9/L29;T72/L155", status_word: "maintained"}
  - {commitment: "Parel to market ~18 months", implied_date: "~H2 FY28", ref: "T15/L41", status_word: "underway"}
  - {commitment: "Mahim-1 launch", implied_date: "Q3 FY27 (Nov-Dec)", ref: "T19/L49;T25/L61", status_word: "on-track"}
  - {commitment: "Mahim-2 launch", implied_date: "Q4 FY27 (Feb-Mar)", ref: "T19/L49;T25/L61", status_word: "on-track"}
  - {commitment: "6 of 8 JDAs launched", implied_date: "FY27-end", ref: "T25/L61", status_word: "in-progress"}
  - {commitment: "JDA margins scale to ~20%", implied_date: "FY28", ref: "T74/L159", status_word: "future"}
  - {commitment: "Disclose exact FY27 interest-cost number", implied_date: "unspecified", ref: "T55/L121;T99/L209", status_word: "promised"}
  - {commitment: "Bring in project-level PE/institutional investor", implied_date: "unspecified", ref: "T95/L201", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
