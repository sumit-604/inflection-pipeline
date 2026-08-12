# A3 FORENSIC NOTES — DGML (Deccan Gold Mines Ltd), Q1 FY27 — DOCTYPE: CONCALL

Source extract: `/home/user/inflection-pipeline/runs/deccangold-q1fy27/work/extract_concall_dgml_q1fy27.txt`
Enumeration spine: `/home/user/inflection-pipeline/runs/deccangold-q1fy27/work/ledger_concall_dgml_q1fy27.md`
Model: claude-opus-4-8 | Ledger reconciled: 100% (all 6 tables, 95 number rows, 21 questions, 4 response blocks read at cited lines)

## COVERAGE / SCOPE NOTES
- **FRESH COVERAGE.** DGML has NO existing Notion monitoring page and NO `companies/DGML.md` memory file. There are **no pre-committed tripwires, no prior operator rulings, and no prior-quarter extract** to diff against. The F17 silence audit therefore runs against the F6 commitment set and the ledger's unanswered-question table only (Table 8), NOT against a checklist. All silence counts are FIRST-OBSERVATION (0 prior quarters of established silence trackable).
- **Doctype = concall.** Per the doctype applicability rule, F6 / F7 / F17 apply in full; the statement/auditor/balance-sheet checks (F2, F3, F4, F5, F8, F9, F11, F12, F15) are N.A. because a concall carries no Reg 33 filing numbers, no auditor Other Matters / EoM paragraph, no OCI/tax schedule, no segment tables, and no consolidation list. Each N.A. below still captures any verbal concall statement that BEARS on it, per instruction.
- **Single-spokesperson concentration.** MD (Dr Modali, ASR-corrupted) is the sole voice for the entire call; the newly appointed director Ms J Deonish is named as present but never speaks (ledger `SILENT_ATTENDEE`). No CFO voice at any point. Weighed under F13.
- **Maturity-ladder lens applied throughout.** Management itself concedes only Junagiri and Kyrgyzstan/Altyn Tor have completed feasibility; every other project number is, in management's own words, "very tentative" pre-drill (line 489-490, "before the completion of drilling programs it will still remain as a kind of very tentative numbers"). Forward guidance resting on un-drilled resource is flagged wherever it appears.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-a | F1 | D1 / N-note "Rs520mn" (Table 8, Table 6 truncation note) | 399-400, 480-481 | "inventory was around 522 millions ... this quarter there was no change in inventory as per the PNLN statement" / mgmt: "we will reply to this particular one ... in terms of the P&L statement" | AMBIGUOUS | Consolidated inventory static despite a quarter of production/sales; deferred, no number given on call. Possible stale/unrealisable stock or a consolidation-scope quirk. A4 question. |
| F1-b | F1 | F14 (Table 7); ZERO_STANDING (Flags) | 421-423 | "I honestly I doubt whether we'll get dividends in this financial year uh it might happen next year but I cannot guarantee" | AMBIGUOUS (INDETERMINATE) | Geomysore is an ASSOCIATE: Rs6.35cr profit share is booked (equity method) but cash arrives only as dividend, which mgmt doubts this FY. Cash-conversion INDETERMINATE — per CLAUDE.md caps any verdict at PROCEED WITH CAVEATS, must not resolve to clean PROCEED. |
| F6 | F6 | Table 7 (F1-F17), N9/N15/N33/etc `FWD` rows | see Commitment Register | "board has approved uh this particular raise" (60); "we are going to deliver by October 2026" (150); "September 15th is the target" (190) | FORWARD-SIGNAL | 17+ dated/dateable commitments feed the Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. Q2 FY27 is the first delivery checkpoint on almost all of them. |
| F7 | F7 | Table 6 truncation note; D2 | 462-463, 489-490, 274 | "exchange of ideas on this" (462); "very tentative numbers" (490); "based on our uh guesstimate rather" (274) | AMBIGUOUS | Pre-emptive hedges cluster on (a) offtake funding not yet contracted, (b) all non-Junagiri/Kyrgyzstan resource numbers, (c) processing-plant sizing. Tells you next quarter's "guidance" stays soft. A4 questions. |
| F10 | F10 | N1 (Rs137cr raise); QIP note; rights-issue Q8 | 60-63, 337-338, 377 | "137 crores ... through CCDs equity shares and equity warrants ... HNAs ... and also the management ... they are also contributing" (60-63); "rights issue as we did ... at rupees 80" (377) | FORWARD-SIGNAL | Stacked dilution overhang: Rs137cr CCD + equity + warrants (pending shareholder approval) ON TOP of a still-pending larger QIP (line 338) and a recent rights issue at ~Rs80. Management + HNI participation = RELATED-PARTY placement. Dilution quantum unquantified on call. |
| F13 | F13 | Table 1 P3-P6; F15 (AGM) | 66-73, 483-485 | "brought in Mr j Deonish ... she was actually the managing director for Geomiser services since from 2012 to 2022"; "DT as an independent director she retired"; "few more board changes are expected" | AMBIGUOUS | (1) Former Geomysore (the associate) MD joins DGML board = related-party governance link into the entity that supplies the profit share. (2) An independent director retired and was NOT renewed (per F13 rule, the bigger signal). (3) "Few more board changes expected" = unsettled board. (4) Physical AGM confirmed, Mumbai — schedule the AGM as a Role 6 event. |
| F14 | F14 | NUMBER_INCONSISTENCY / ASR_GARBLE flags | 514, 519, 399/481 | "40,000 trolls of national critical mental mission" (514) vs "44,000 crores of national critical mental mission money" (519) | NEUTRAL-FACT | Same speaker, same passage, two figures for the same NCMM corpus; plus Rs522mn (investor) vs Rs520mn (mgmt restatement) inventory. Mostly ASR-attributable but the NCMM pair is speaker-side. Low materiality; logged as a data-quality/governance data point only. |
| F16-a | F16 | Q9 (Table 4); F1/F4 (Table 7) | 380-384 | "as we used to share in the you know earlier slides ... so uh this those slides are not included this time" | FORWARD-SIGNAL | GUIDANCE-SLIDE WITHDRAWAL. Prior deck guided Junagiri 600kg / Rs900-1,000cr FY27 & 800kg FY28; Kyrgyzstan 160kg / Rs300cr FY27 & 350kg FY28. Those slides were DROPPED this quarter. Mgmt verbally softens Junagiri to "500 to 600" (441) and reaffirms 150-160 (445) but declines the topline (Rs) numbers entirely. Classic walk-back. |
| F16-b | F16 | Q3 (Table 4); EBITDA note (Table 6 trunc) | 361-364, 434 | investor: "substantially lower ... versus what we were expecting like say 60 65% ... total profit ... is around 30%"; mgmt: "to stabilize to about 65 or 70% of EITA ... it will take another quarter or two" | FORWARD-SIGNAL | Margin walk-back: realised Junagiri PAT margin ~30% vs a previously indicated 60-65%; management pushes the 65-70% EBITDA target out by "another quarter or two." Near-term margin miss + deferred recovery. |
| F16-c | F16 | Q4/Q10/D3; F1 (Table 7) | 427-428, 441-442, 489-490 | "whether this 600 kilos ... let us wait give us one more quarter"; other projects' numbers "will still remain as a kind of very tentative numbers" | AMBIGUOUS | Fuller forward guidance actively declined; the reaffirmed numbers rest on one quarter of data and, for all non-feasibility projects, on un-drilled resource. FY28 output from mines other than Junagiri/Kyrgyzstan (Hardik Jane Q10) never answered. |
| F17 | F17 | Table 8 (D1-D5); Q10 | see Silence Table | Q6 dor-bar ignored in RB1 until re-asked (369-370 -> 500-501); D3 FY28-other-mines "no resolving line found" | CONFIRMATORY-NEGATIVE | Deferred/unanswered items concentrate on the hardest quantitative asks (inventory realisation, FY28 non-flagship output, tentative-project economics). First-observation; establishes the baseline silence set for next quarter's tracker. |

Classification key (per operating rules): FORWARD-SIGNAL and AMBIGUOUS findings are handed to A4 to convert into management questions. RED-FLAG emphasis (per task): F1-b (cash INDETERMINATE), F10 (related-party dilution stack), and F16-a (guidance withdrawal) are the three findings A4/A5 should weight most heavily.

---

## CHECKLIST SCORECARD (all 17, exactly one status each — GATE A3)

| Check | Status | One-line basis |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | **FINDING** | Two ZERO_STANDING threads: Rs522/520mn inventory "no change per P&L" (deferred, F1-a) and associate dividend/cash-conversion INDETERMINATE (F1-b, line 421-423). |
| F2 STANDALONE vs CONSOLIDATED | **N.A.** | Concall carries no S-vs-C statement pair to decompose. Note: the entire consolidated PAT uplift is the Rs6.35cr equity-method associate share (Geomysore/Junagiri) — captured in F1-b/F4. |
| F3 SHELL-ENTITY DETECTION | **N.A.** | No standalone-vs-consolidated cost lines in a transcript. |
| F4 UNAUDITED CONTRIBUTION RATIO | **N.A.** | No auditor Other Matters paragraph in a concall. Bearing note for A4: Rs6.35cr / Rs25cr = ~25% of Junagiri PAT reaches DGML via an associate whose figures are equity-method, not line-consolidated — the associate-accounted portion is exactly the number that will show as "unaudited/associate" on the eventual filing. |
| F5 GOING CONCERN / EoM SCOPE | **N.A.** | No auditor EoM in a concall and no prior-quarter extract supplied to verbatim-diff. |
| F6 FORWARD-COMMITMENT PHRASE MINING | **FINDING** | 17+ dated commitments mined (register below); dense "board has approved / going to deliver by October / September 15th target / by mid next year" lexicon. |
| F7 HEDGE PHRASE MINING | **FINDING** | Hedge cluster: "exchange of ideas" (462), "guesstimate" (274), "very tentative numbers" (490), "I cannot guarantee" (423), "subject to shareholders approval" (61), "considering" offtake (463). |
| F8 TAX FORENSICS | **N.A.** | No ETR / deferred-tax / prior-year-tax detail in a concall (the only "profit of tax of 25 crores" at line 115 is a Geomysore-level figure, not a DGML tax schedule). |
| F9 OCI FORENSICS | **N.A.** | No OCI / actuarial disclosure in a transcript. |
| F10 SHARE COUNT AND DILUTION | **FINDING** | Stacked dilutive instruments openly discussed: Rs137cr CCD + equity shares + equity warrants (60-61), pending larger QIP (338), recent rights issue at ~Rs80 (377), with management/HNI participation (62-63) = related-party. |
| F11 RESERVES / NET WORTH TIE-OUT | **N.A.** | No balance-sheet equity figures in a concall. |
| F12 SEGMENT FORENSICS | **N.A.** | Two "verticals" described qualitatively (gold / critical minerals) but no segment assets/liabilities/revenue table to trend. |
| F13 BOARD OUTCOME BEYOND RESULTS | **FINDING** | Chair change (Kasam out, Ilango in), independent director "DT" retired and not renewed, related-party director (ex-Geomysore MD) appointed, "few more board changes expected," physical AGM Mumbai confirmed (66-73, 483-485). |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | Speaker-side number inconsistency: NCMM corpus stated Rs40,000cr (514) then Rs44,000cr (519) in the same passage; inventory Rs522mn vs Rs520mn (399 vs 481). Low materiality, mostly ASR-adjacent; logged as data-quality point. |
| F15 ENTITY LIST DIFFS | **N.A.** | No consolidation entity list in a concall and no prior-quarter extract to diff. |
| F16 DROPPED / REFRAMED DISCLOSURES | **FINDING** | Guidance slides dropped (F16-a), margin expectation walked back 60-65% -> ~30% actual with recovery deferred (F16-b), fuller guidance declined and rests on un-drilled resource (F16-c). |
| F17 CONCALL SILENCE AUDIT | **FINDING** | Deferred/unanswered on the hardest quant asks (inventory realisation, FY28 non-flagship output, tentative-project economics); dor-bar question ignored until re-asked. First-observation baseline (no Notion checklist exists). |

Blank checks: none. **GATE A3: PASS.** (8 FINDING, 9 N.A., 0 PASS-clean, 0 blank.)

---

## COMMITMENT REGISTER (from F6 — feeds Role 5 tracker & FTTCP timeline)

| Commitment | Implied date | Line/turn ref | Status word |
|---|---|---|---|
| Rs137cr raise (CCD + equity + warrants) closes | pending shareholder approval, near-term | 60-61 | board-approved / pending |
| Larger QIP for principal funding | undated ("when we actually go for a larger funding") | 338, 340 | proposed / pending |
| Altyn Tor (Kyrgyzstan) full-scale commissioning & production start | "next week" from call date | 140-142 | underway (commissioning) |
| Altyn Tor inauguration date announced | TBD, "not very very far" | 161 | intended |
| Altyn Tor revised mine design / life-of-mine plan | by October 2026 | 150-151 | in the process of |
| Altyn Tor underground resource / mining work begins | from September 2026 | 152 | commencing |
| Junagiri revised in-mine resource estimate | by October | 102 | expected |
| Junagiri 2,500 tpd processing approvals | in process | 123-124 | in the process of acquiring |
| Junagiri full-year production clarity (500-600kg test) | end of Q2 FY27 | 427-428, 441-442 | reaffirmed / to-be-demonstrated |
| Finland 51% stake acquisition | "this coming quarter" | 177-178 | intends to |
| Finland drilling start (~1,500m) | September 15 target | 190-191 | target set |
| Finland feasibility study | 2027 | 105-106 | plans to |
| Balukona mining-lease application | "next year" | 240 | plans to |
| Balukona process-flow-sheet / feasibility | mid next year | 246 | will do |
| Spain (HESA) full assay results | mid-September | 270 | expected |
| Spain preliminary resource model | early October | 271 | will be completed |
| Mozambique 200 tpd concentrate plant | end-2027, fallback Q1 FY28 | 291-294 | aims to / hope to |
| 3 new gold assets (due diligence) into production | end-2027 / 2028 | 111-113, 215-218 | doing due diligence |
| Physical AGM (Mumbai) | this FY | 483-485 | guaranteed / committed |
| Nikhil Gohil emailed queries answered point-by-point | post-call | 486-491 | will respond (email) |
| Rs522/520mn inventory realisation answer | post-call, via P&L reply | 480-481 | deferred to email |

Status-transition note: several items are at the confirmable "underway -> completed" boundary — Altyn Tor commissioning ("next week") and the October 2026 Kyrgyzstan LOM plan are the nearest hard milestones and become promise-vs-delivery checkpoints at the Q2 FY27 call.

---

## WHAT WAS NOT DISCUSSED (F17 silence audit — first observation, no prior baseline)

| Item | Origin | Status this call | Consecutive quarters silent |
|---|---|---|---|
| Rs522/520mn consolidated inventory realisation timeline & why no P&L movement | Shaswat Vijay Q14 (398-400) | DEFERRED to email; no number on call (480-481) | 1 (first observed) |
| FY28 production from mines OTHER than Junagiri/Kyrgyzstan | Hardik Jane Q10 (384) | NOT answered — no resolving line; RB1 guidance covers only the two flagship mines (441-445) | 1 (first observed) |
| Junagiri/Kyrgyzstan Rs topline guidance (prior Rs900-1,000cr / Rs300cr) | dropped slides (380-384) | Withheld — mgmt gives only kg volumes verbally, declines Rs figures | 1 (first observed) |
| Dor-bar / refinery mechanics at Altyn Tor | Ankit Gupta Q6 (369-370) | Ignored in RB1; answered only after re-ask as Q20 (501-512) | 1 (first observed) |
| QIP size/timing (the "larger funding") | mgmt's own reference (338) | Left open, no quantum or date | 1 (first observed) |
| Tentative-project economics (capex/resource/annual production per project) | Nikhil Gohil email (486-491) | Explicitly declined on call as "very tentative," deferred to email | 1 (first observed) |
| Uzbekistan critical-minerals offer to GoI | Sundar Padmanaban Q19 (496-497) | Near-non-answer: "no concrete ... project information" (527-530) | 1 (first observed) |

Per Role 5, none of these can yet be scored as "sustained silence on a deteriorating metric" (fresh coverage). They form the baseline set to re-check at Q2 FY27; the inventory-realisation and FY28-non-flagship-output silences are the two to watch — both are quantitative asks management chose not to answer.

---

## MATURITY-LADDER TAG (domain overlay for A4/A5)

| Bucket | Projects / numbers | Basis |
|---|---|---|
| FEASIBILITY-BACKED (rely-on) | Junagiri (500-600kg reaffirmed), Altyn Tor/Kyrgyzstan (150-160kg) | Mgmt: only these two have completed feasibility (489) |
| PRE-DRILL / TENTATIVE (do not underwrite) | Finland (>5-6t target), Balukona (3,000 tpd plant), Spain tungsten (3Mt resource), Mozambique (200-1,000 tpd), all "dream pipeline 2030" & 2-tons/annum Junagiri-2029/30 | Mgmt's own "very tentative numbers" caveat (489-490); "guesstimate" (274) |
| CASH vs BOOK divergence | Rs6.35cr associate profit booked, dividend doubted this FY (F1-b) | Equity-method associate; cash only via dividend (420-423) |
| LITIGATION-CONTINGENT | Ganajur (~1t if lease granted, 2-3yrs), Hatti (prospecting licence only) | In court; "let's wait what happens" (204, 476-480) |

---

```yaml
stage: A3-forensics
company: "DGML"
quarter: "Q1FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/deccangold-q1fy27/work/forensics_dgml_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "F1-a", check: "F1", line: "399-400,480-481", classification: "AMBIGUOUS", implication: "Rs522/520mn consolidated inventory shows no P&L movement despite a production quarter; realisation deferred, no number given."}
  - {id: "F1-b", check: "F1", line: "421-423", classification: "AMBIGUOUS", implication: "Associate (Geomysore) cash-conversion INDETERMINATE: Rs6.35cr profit booked, dividend doubted this FY; caps verdict at PROCEED WITH CAVEATS."}
  - {id: "F6", check: "F6", line: "60,150,190", classification: "FORWARD-SIGNAL", implication: "17+ dated commitments; Q2 FY27 is first delivery checkpoint (Altyn Tor commissioning, Oct-2026 LOM plan)."}
  - {id: "F7", check: "F7", line: "462-463,489-490", classification: "AMBIGUOUS", implication: "Hedges concentrate on uncontracted offtake funding and all pre-drill resource numbers; next-quarter guidance stays soft."}
  - {id: "F10", check: "F10", line: "60-63,337-338,377", classification: "FORWARD-SIGNAL", implication: "Stacked dilution: Rs137cr CCD+warrants + pending QIP + recent rights at ~Rs80, with mgmt/HNI (related-party) participation; quantum unquantified."}
  - {id: "F13", check: "F13", line: "66-73,483-485", classification: "AMBIGUOUS", implication: "Related-party director (ex-Geomysore MD) added, independent director not renewed, more board changes pending; physical AGM Mumbai = Role 6 event."}
  - {id: "F14", check: "F14", line: "514,519", classification: "NEUTRAL-FACT", implication: "Speaker-side NCMM corpus inconsistency (Rs40,000cr vs Rs44,000cr) and inventory Rs522 vs Rs520mn; low materiality data-quality note."}
  - {id: "F16-a", check: "F16", line: "380-384", classification: "FORWARD-SIGNAL", implication: "Prior guidance slides (Junagiri 600kg/Rs900-1,000cr, Kyrgyzstan 160kg/Rs300cr, FY28 figures) dropped this quarter; verbal reaffirmation softened, Rs topline withheld."}
  - {id: "F16-b", check: "F16", line: "361-364,434", classification: "FORWARD-SIGNAL", implication: "Margin walk-back: realised ~30% PAT vs prior 60-65% indication; 65-70% EBITDA target pushed out another quarter or two."}
  - {id: "F16-c", check: "F16", line: "427-428,489-490", classification: "AMBIGUOUS", implication: "Fuller guidance declined; reaffirmed numbers rest on one quarter of data and, for non-flagship projects, on un-drilled resource; FY28 other-mine output unanswered."}
  - {id: "F17", check: "F17", line: "480-481", classification: "CONFIRMATORY-NEGATIVE", implication: "Hardest quant asks (inventory realisation, FY28 non-flagship output, tentative-project economics) deferred/unanswered; first-observation baseline."}
forward_signals: ["F6", "F10", "F16-a", "F16-b"]
ambiguous: ["F1-a", "F1-b", "F7", "F13", "F16-c"]
commitments:
  - {commitment: "Rs137cr CCD/equity/warrant raise closes", implied_date: "pending shareholder approval", ref: "L60-61", status_word: "board-approved"}
  - {commitment: "Larger QIP principal funding", implied_date: "undated", ref: "L338", status_word: "proposed"}
  - {commitment: "Altyn Tor commissioning & production start", implied_date: "next week from call", ref: "L140-142", status_word: "underway"}
  - {commitment: "Altyn Tor revised LOM plan", implied_date: "Oct 2026", ref: "L150-151", status_word: "in-process"}
  - {commitment: "Junagiri revised resource estimate", implied_date: "October", ref: "L102", status_word: "expected"}
  - {commitment: "Junagiri 500-600kg FY27 test", implied_date: "end Q2 FY27", ref: "L427-428", status_word: "reaffirmed"}
  - {commitment: "Finland 51% stake acquisition", implied_date: "coming quarter", ref: "L177-178", status_word: "intends"}
  - {commitment: "Finland drilling start ~1,500m", implied_date: "Sep 15", ref: "L190-191", status_word: "target-set"}
  - {commitment: "Finland feasibility study", implied_date: "2027", ref: "L105-106", status_word: "plans"}
  - {commitment: "Balukona mining-lease application", implied_date: "next year", ref: "L240", status_word: "plans"}
  - {commitment: "Balukona feasibility/flow-sheet", implied_date: "mid next year", ref: "L246", status_word: "will-do"}
  - {commitment: "Spain HESA full assay results", implied_date: "mid-September", ref: "L270", status_word: "expected"}
  - {commitment: "Spain preliminary resource model", implied_date: "early October", ref: "L271", status_word: "will-complete"}
  - {commitment: "Mozambique 200 tpd concentrate plant", implied_date: "end-2027/Q1 FY28", ref: "L291-294", status_word: "aims"}
  - {commitment: "3 new gold assets into production", implied_date: "end-2027/2028", ref: "L111-113", status_word: "due-diligence"}
  - {commitment: "Physical AGM in Mumbai", implied_date: "this FY", ref: "L483-485", status_word: "committed"}
  - {commitment: "Nikhil Gohil emailed-query response", implied_date: "post-call", ref: "L486-491", status_word: "deferred-email"}
  - {commitment: "Rs520mn inventory realisation answer", implied_date: "post-call", ref: "L480-481", status_word: "deferred-email"}
gate_a3: pass
blank_checks: []
```
