# A3 FORENSIC NOTES — MANINDS | Q1 FY27 (2026-09) | doctype: presentation

Inputs read (no source access): A1 structured (R001-R335), A1 fulltext (lines 1-1051),
A2 ledger (R### + MF01-MF10). Every ledger row read at its cited line before judging.
Ledger reconciliation: 335/335 structured IDs + MF01-MF10 all accounted = 100%.
Prior-quarter deck: none supplied (F16 cross-deck diff not runnable; noted below).

---
## FINDINGS TABLE

| id | check | ledger ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A1 | F2 | R159 / R171 | L769, L806 (slides 28/29) | standalone "PAT ... 1,958" vs consolidated "PAT ... 1,705" | FORWARD-SIGNAL | Subsidiary net PAT swung from +162 (FY25: consol 1,532 > SA 1,370) to -253 (FY26: consol 1,705 < SA 1,958). A -415 swing = 21% of SA PAT, far above the 5pp gate. Consol PAT grew 11.3% while standalone grew 42.8%; consol revenue grew 1.7% vs standalone 10.8%. Subsidiaries (ex-NPC, which consolidates only from Q2 FY27) are shrinking and net loss-making. A4 question. |
| A2 | F6 | R273,R274,R277,R280,R286,R107 | L124-125,418,445,935,559 | "Production Targeted: Mar'2027"; "Project launch on track for Mid-September 2026"; NPC "expected to be reflected from Q2 FY27 onwards"; "Will be Upgraded to 120\"" | FORWARD-SIGNAL | Dated management commitments to load into the Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. Two Mar 2027 commissionings (Dammam, Jammu), NPC full contribution Q2 FY27, Merino launch mid-Sep 2026 (~2 weeks post-deck). See COMMITMENT REGISTER. |
| A3 | F10 | R173 / R174 | L823, L825 (slide 30) | "Equity Share Capital FY24 324 / FY25 324 / FY26 375" | NEUTRAL-FACT | Paid-up capital +15.7% in FY26 (324->375 INR Mn) = a completed equity issuance (~10M new shares at Rs5 face). Other Equity +4,741 (15,749->20,490) exceeds retained PAT (~1,705), confirming a premium raise. Likely NPC/capex funding. Deck discloses no basic-vs-diluted EPS; dilution flag for A4/Notion warrant cross-check. |
| A4 | F12 | R191 / R199 / R201 / R183 | L828, L840, L842, L843 (slide 30) | "Capital WIP FY24 305 / FY25 1,334 / FY26 3,258"; "Inventories ... 6,456 ... 15,350"; "Trade Receivables ... 3,551 ... 10,098" | AMBIGUOUS | CWIP 10x in two years = Jammu (Rs350Cr of Rs600Cr spent) + Dammam pre-commissioning build with zero revenue yet; more capex to come. Simultaneously inventories 2.4x, current receivables 2.8x, trade payables 2.9x (5,028->14,712) while consol revenue is flat (+1.7%). Working-capital intensity rising with no revenue growth. Also "Other financial liabilities" 301->5,797 (R185) at FY26 close (pre-NPC): candidate NPC-consideration payable. A4 concall question on WC direction and the 5,797 item. |
| A5 | F14 | R088 / R103 / R110 / R324 | L468, L531, L579, L639 | "Since more than two decades" vs "40+ Years" vs "held ... since 2005" | AMBIGUOUS | Saudi Aramco relationship stated in three irreconcilable framings: "2+ decades" and approved-vendor "since 2005" (~20 yrs) contradict "40+ Years." Immaterial to numbers, but a drafting/governance data point; A4 to clarify actual approved-vendor tenure (it underwrites the whole "buy vs greenfield" moat claim). |
| A6 | F16 | R153 / R165 (MF02/MF04) | L775, L812 (slides 28/29) | "* EBITDA is inclusive of Other Income, since it's operational in nature" | FORWARD-SIGNAL | Both headline EBITDA numbers include Other Income in numerator AND Total Income in denominator. Clean consol EBITDA = 4,679-286 = 4,393 on revenue 35,639 = 12.3%, below the Notion 13% floor tripwire and far from the 15% five-year target (R222). Standalone clean = 4,928-531 = 4,397 / 34,552 = 12.7% vs reported 14.0%. ROCE 18.4% (R018) likely rides the same inflated EBIT. A4 question on clean-margin trajectory. |
| A7 | F16 | R217 | L899-909 (slide 32) | "6,269; 3,820; 3,409; 1,833; 2,128; margins 53.8%; 40.6%; 35.9%; 23.7%; 26.1%" | AMBIGUOUS | Page-32 quarterly Gross Profit values imply a 53.8% single-quarter gross margin, irreconcilable with the page-31 annual FY26 GP margin of 38.0% (R211) and with the Total-Income ordering; A1 flagged per-quarter mapping unresolvable. Chart-data opacity on the deck's only quarterly-trend slide. Do not rely on per-quarter GP bars. |

---
## CHECKLIST SCORECARD (all 17)

| # | Status | Basis |
|---|---|---|
| F1 | PASS | Three nil-standing units read (R194 Intangibles FY24 "-", R206 Current Tax Assets "-" all years, MF10 Greenfield "Order book on day one Nil"). R194 = intangibles first recognised FY25 (small: 5,3). R206 = company always in tax-payable position (current tax LIABILITY positive). MF10 = rhetorical build-vs-buy framing, not a ledger line. No exceptional/disposal/impairment template lines lurking. |
| F2 | FINDING | Standalone-vs-consolidated PAT divergence, see A1. |
| F3 | N.A. | Presentation carries no entity-level cost decomposition (only aggregate SA and consol P&L). Shell-vs-operating test needs per-subsidiary Cost of Materials / Employee Benefits, absent here. Aggregate check shows subs DO operate (consol opex 31,246 > SA 30,155). |
| F4 | N.A. | No auditor's Other Matters / component-auditor disclosure in a corporate presentation. |
| F5 | N.A. | No auditor EoM / Going Concern paragraph in a presentation; no prior deck for verbatim diff. |
| F6 | FINDING | Forward-commitment phrases mined; dated milestones registered, see A2 + COMMITMENT REGISTER. |
| F7 | PASS | Only boilerplate safe-harbor disclaimer (R269, L1013-1037). No note-level hedge newly added on revenue lumpiness or customer concentration. The 40-day NPC "lower contribution" wording (R220) is an explanation, not a hedge. |
| F8 | PASS | ETR near statutory: SA FY26 672/2,630 = 25.6% (FY25 26.1%); consol FY26 665/2,370 = 28.1% (FY25 26.5%). DTL flat (R178: 258/276/258), no persistent-credit pattern. No "tax relating to earlier years" line. Note carried to analyst_note: NPC's 11.4% Zakat rate (R133) will lower group ETR once it consolidates from Q2 FY27. |
| F9 | N.A. | No OCI / actuarial statement in a presentation. |
| F10 | FINDING | Paid-up capital +15.7% FY26 = equity raise, see A3. |
| F11 | PASS | Net worth ties: 375 + 20,490 = 20,865 = Shareholders Fund (R175); page-4 headline Rs2,087 Cr (R020) = 20,865 Mn within rounding. ROE 9.2% reconciles on average net worth ((16,073+20,865)/2). No third-party gap >5%. |
| F12 | FINDING | No formal segment table, but consolidated BS shows CWIP pre-commissioning build + working-capital ballooning, see A4. |
| F13 | N.A. | Not a board-outcome filing; no AGM notice, no director term dates, no AR approval trigger (management bios on slide 8 carry no appointment dates). |
| F14 | FINDING | Aramco-tenure drafting inconsistency, see A5. (Minor typos "four decade", "non only", "liasioning" noted, immaterial.) |
| F15 | N.A. | No prior-quarter deck supplied; consolidation-list diff not runnable. NPC becomes a new consol entity from Q2 FY27 (via MISIC) but no prior list to diff against. |
| F16 | FINDING | Two reframing findings within this deck: EBITDA/Total-Income "inclusive of Other Income" flatters margins below the 13% clean floor (A6); quarterly GP chart data unmappable/inconsistent (A7). Cross-deck drop test NOT runnable (no prior deck) — standing gap flagged. |
| F17 | N.A. | Not a concall; no transcript to run the silence audit against. |

---
## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Dammam Coating Plant (KSA) production | Mar 2027 | R273/R300 (L124) | targeted / underway |
| Jammu SS seamless plant production (Rs350Cr of Rs600Cr spent) | Mar 2027 | R274/R277/R318 (L418) | underway |
| NPC full earnings contribution to consol | Q2 FY27 | R286/R334 (L941) | underway (100% acquired 21 May 2026) |
| Merino Shelters project launch | Mid-Sep 2026 | R280/R321 (L445) | on track (imminent) |
| Merino Shelters Rs35-50Cr cashflow | FY27 | R281 (L446) | expected |
| Merino Shelters annual cashflow | from FY28 | R278/R320 (L433) | planned |
| Merino Shelters Rs700-800Cr revenue | next 5-6 yrs | R279 (L440) | projected |
| NPC HSAW OD upgrade to 120" | no date | R107 (L559) | will be upgraded |
| NPC value-added coating-mill expansion (post-acq) | no date | slide 21 (L541) | planned |
| Group Revenue CAGR 20-25% | next 5 yrs | R221/R291 (L965) | target |
| Group EBITDA margin to 15% stable | next 5 yrs | R222/R292 (L969) | target |

---
## RECONCILIATION NOTE
All 335 structured rows read at their lines; the 10 MISSING_FROM_STRUCTURED units read from
fulltext. The two highest-value A2 misses (MF02/MF04, EBITDA "inclusive of Other Income" on
R153/R165) drive finding A6 and the sub-13% clean-margin call. MF10 (Greenfield Nil order book)
folded into F1. No row unread; no source PDF opened.

```yaml
stage: A3-forensics
company: "MANINDS"
quarter: "2026-09"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "runs/maninds-corppres-2026-09/work/final-gate/forensics_maninds_2026-09.md"
ledger_reconciled_pct: 100
checklist:
  F1: PASS
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: PASS
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A1", check: "F2", line: "L769/L806", classification: "FORWARD-SIGNAL", implication: "Subsidiary net PAT swung +162 (FY25) to -253 (FY26), 21% of SA PAT; consol PAT +11.3% vs SA +42.8%; loss-making subs ex-NPC"}
  - {id: "A2", check: "F6", line: "L124/L418/L445/L941", classification: "FORWARD-SIGNAL", implication: "Dated catalysts: Dammam+Jammu Mar2027, NPC full contribution Q2FY27, Merino launch mid-Sep2026"}
  - {id: "A3", check: "F10", line: "L823", classification: "NEUTRAL-FACT", implication: "Paid-up capital +15.7% FY26 = completed equity raise (~10M shares); dilution + no diluted-EPS disclosure"}
  - {id: "A4", check: "F12", line: "L828/L840/L842", classification: "AMBIGUOUS", implication: "CWIP 10x (Jammu/Dammam pre-commissioning, more capex due) + WC intensity rising (inv 2.4x, recv 2.8x) on flat +1.7% revenue; 5,797 other-fin-liab spike"}
  - {id: "A5", check: "F14", line: "L468/L579", classification: "AMBIGUOUS", implication: "Aramco tenure stated 2+ decades / since-2005 vs 40+ years; underwrites the moat claim, clarify"}
  - {id: "A6", check: "F16", line: "L775/L812", classification: "FORWARD-SIGNAL", implication: "EBITDA incl Other Income both sides: clean consol margin 12.3% below Notion 13% floor and 15% target; ROCE likely inflated"}
  - {id: "A7", check: "F16", line: "L899-909", classification: "AMBIGUOUS", implication: "Quarterly GP chart implies 53.8% margin vs 38.0% annual; per-quarter mapping unresolvable; chart-data opacity"}
forward_signals: ["A1", "A2", "A6"]
ambiguous: ["A4", "A5", "A7"]
commitments:
  - {commitment: "Dammam Coating Plant production", implied_date: "Mar 2027", ref: "R273/R300", status_word: "underway"}
  - {commitment: "Jammu SS plant production", implied_date: "Mar 2027", ref: "R274/R277", status_word: "underway"}
  - {commitment: "NPC full earnings contribution", implied_date: "Q2 FY27", ref: "R286/R334", status_word: "underway"}
  - {commitment: "Merino Shelters project launch", implied_date: "Mid-Sep 2026", ref: "R280/R321", status_word: "on-track"}
  - {commitment: "Merino Shelters FY27 cashflow Rs35-50Cr", implied_date: "FY27", ref: "R281", status_word: "expected"}
  - {commitment: "Merino Shelters annual cashflow", implied_date: "FY28", ref: "R278/R320", status_word: "planned"}
  - {commitment: "Merino Shelters revenue Rs700-800Cr", implied_date: "5-6 yrs", ref: "R279", status_word: "projected"}
  - {commitment: "NPC HSAW OD upgrade to 120\"", implied_date: "none", ref: "R107", status_word: "planned"}
  - {commitment: "NPC value-added coating expansion", implied_date: "none", ref: "slide21", status_word: "planned"}
  - {commitment: "Group Revenue CAGR 20-25%", implied_date: "5 yrs", ref: "R221/R291", status_word: "target"}
  - {commitment: "Group EBITDA margin to 15%", implied_date: "5 yrs", ref: "R222/R292", status_word: "target"}
gate_a3: pass
blank_checks: []
analyst_note: "Two threads bind the findings. First, the deck flatters the present: EBITDA and Total Income both carry Other Income (MF02/MF04), so the clean consolidated margin is 12.3%, under the 13% Notion floor and far from the 15% target; ROCE 18.4% likely rides the same inflated EBIT. Second, the FY26 consolidated balance sheet (pre-NPC, March close) already shows a 10x CWIP build and working capital ballooning (inventories 2.4x, receivables 2.8x) on flat +1.7% revenue, while subsidiaries flipped from +162 to -253 PAT. NPC (11.4% Zakat tax, 24.8% EBITDA margin) consolidates only from Q2 FY27 and is the entire re-rating case; every FY26 number here is the OLD business, and the old business is margin-thin and WC-heavy. A4 should press on: what are the loss-making subs, where is the 5,797 other-financial-liability, and is the clean margin really climbing to 15%."
```
