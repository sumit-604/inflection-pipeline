# A3 FORENSIC NOTES: concall GRWRHITECH q2fy27

Document: Q2 and H1 FY27 earnings call, 23-Oct-2026, machine-transcribed (ASR, faster-whisper small, no diarization). Not a company-filed transcript (fulltext L0001).
Inputs read: A1 structured (R001-R419), A1 fulltext (L0001-L0842, all lines), A2 ledger (419 rows plus MFS01). Source PDF and inputs/ not opened.
Prior-quarter fulltext: none. Every silence count below is "1 (this call); prior quarters NOT FOUND".
Number tag: every figure is [ASR, verify against filed transcript]. "Derived" = arithmetic on stated ASR figures only, no estimate.
Cite convention: "L0nnn" = fulltext 4-digit line prefix (A1 row anchors drift 1-3 lines in places, e.g. R058 line 54 vs L0053; I cite the fulltext prefix).

## LEDGER RECONCILIATION
- Structured rows read at fulltext line: 419 of 419 (R001-R419). MFS01 read at L0520. Total 420 of 420 = 100%.
- Turn table T01-T97 checked against fulltext cues. Agrees.
- A1 row errors found: none on value. Two reading risks for A4:
  - R049 "26.30%" is verbatim at L0049 but conflicts with the stated H1 figures (FN01).
  - R283 / R303 "28 to 31" is a period (FY28-FY31), not a margin range. L0662: "for medium term 28 to 31 you have mentioned 27 percent plus" (FN16).
- MFS01 (L0520 "there is one product, we can simply say this is 85%"): the speaker warns against a single-product reading ("Don't take like", L0519). Adds nothing to R258 / R261 (85-120%). NEUTRAL, no finding.

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN01 | F14 | R041,R043,R049 | L0047-L0049 | "EBITDA margin expanding by 464 basis points to 26.30%" | NEUTRAL-FACT | Stated H1 EBITDA 381 / revenue 1329 = 28.7% (derived). The YoY check also gives 28.7%: H1 FY26 = 1063 rev, 256 EBITDA, 24.1%, +464 bps. 26.30% is an ASR mishear or a different basis. Use 28.7% [derived, ASR] until the filed transcript confirms. |
| FN02 | F6 | R105,R107,R108,R293,R294,R300 | L0085, L0645, L0655 | "upgraded our FY 27 Abitah margin guidance by 200 basis points to 27% plus minus 2% while reaffirming our revenue target of more than 2500 crores" | FORWARD-SIGNAL | H1 is 1329 (53% of the 2500 floor). Revenue guidance was not raised. Floor implies H2 >= 1171, below H1. At 27% midpoint on 2500, H2 EBITDA = 294, H2 margin ~25.1% (derived) vs H1 28.7%. Top of band (29% on 2600) allows ~29%. Q2 PAT 129 < derived Q1 PAT 133 despite +10% QoQ revenue. Management frames it as seasonal ("Q3 will be seasonally low but Q4 will be back", L0655). The call does not say if the 27% includes other income (Notion says it does). |
| FN03 | F7 | R209-R216, R262, R263 | L0386-L0392, L0539-L0545 | "we have received around 31 crore ... 11 crore has been in our book ... we expect in Q3 another refund of around 30 crore that is the last one ... 16 crore will come to our books" / "we are reducing it from COGS. But we are not counting in the sales. We are reversing in the sales and adding it into COGS." | AMBIGUOUS | US tariff refunds give 27 Cr of one-time gain (11 to date + 16 in Q3), booked through COGS at the US subsidiary. Timing of the 11 Cr by quarter is not stated. If it fell in Q2, it is ~1.6 pp of Q2 margin (11/696, derived). The 16 Cr in Q3 flatters the seasonally low quarter, and the source ends after Q3 ("the last one"). The accounting description contradicts itself (reduce COGS vs reverse sales and add to COGS). This is the only subsidiary mention on the call and a candidate cause of the Q2 subsidiary PAT jump (results-review open item). |
| FN04 | F7 | R165-R171, R174 | L0259-L0266, L0273-L0278 | "The customer concentration is definitely there and there are more customers of not that big size but of course half of that size there are a couple of customers or one third of that" | FORWARD-SIGNAL | Analyst cites 30%, management does not correct it (Notion holds 34%). Concentration goes beyond one name: "a couple" at half and one at one third of the top customer. The top customer is automotive ("does not do any of the architectural", L0278), tied to a US EV maker (L0266, ASR "best car or EV car seller in US"), still unnamed. "we are not worried about they will go down" (L0273-L0274) is assertion, not evidence. No volume data (FN14). Thesis-broken 2 cannot be monitored from this call. |
| FN05 | F7 | R180-R186, R060, R061 | L0299-L0322, L0054 | "inventory to our Europe USA customers ... Their inventory has increased because number of days have gone by 15 to 25 so roughly 20 days overall company export level inventories that increase" | AMBIGUOUS | Company inventory is 58-60 days (L0317), built on purpose for raw-material security. Separately, Europe/US customer or channel inventory rose ~20 days. If this is channel fill, part of Q2 export revenue was pulled forward, and Q3 can destock. Working capital is held at 29 days (L0054) only through "sold out with advances" (L0321-L0322). Receivable discounting was not discussed. Lean bear: treat as possible pull-forward until H2 export run-rate shows otherwise. |
| FN06 | F6 | R070-R072, R272, R406 | L0063, L0604-L0605, L0829 | "TPU film line remains on track for commissioning in Q3 FY27" vs "as of now, I'm not sure because line is yet to start commissioning. Everything is going on." | FORWARD-SIGNAL | The call is on 23-Oct-2026, already inside Q3 FY27, and the line has not started commissioning. About 10 weeks remain to the deadline. External TPU revenue (75-100 Cr) is "in the coming year, not this year" (L0829), so FY27 gets no TPU revenue. The FY28 margin step-up (FN08) depends on this date. Q3 call is the milestone check: "on track" -> "commissioned". |
| FN07 | F7 | R120, R392, R401, R408 | L0820-L0821, L0831 | "we have a understanding with them that we buy this much of resin from them" / "this is the first trial for us ... If it all works, we will think of further expansions" | AMBIGUOUS | The Lubrizol MoU (24-Sep-2026 per Notion) carries a resin purchase understanding of undisclosed volume. It could be a minimum-offtake obligation on a line not yet commissioned. Management calls the TPU vertical a "first trial", which is a hedge on a stated "fifth vertical" (L0816). Terms: NOT FOUND on call. |
| FN08 | F6 | R285, R287-R296, R305-R307, R393-R396 | L0813, L0644-L0646, L0663-L0668 | "75% of this TPU will go to our PPF business, where we expect a good margin expansion of 1.5 to 2% is 150 to 200 basis points for consolidated level" / "we are talking 28 28.5 for sure" | FORWARD-SIGNAL | FY28 margin is now a verbal "for sure" 28-28.5%, next to a hedge in the same answer ("we exactly we can't comment", L0644). PPF is 24% of revenue at a stated 20-25% margin (L0744). 150-200 bps consolidated from PPF alone needs ~6-8 pp on PPF margin (derived: 1.5-2.0 / 0.24). That is a large cost claim on a line yet to commission. The bridge is only as good as FN06. |
| FN09 | F6 | R146-R148, R162, R163, R199-R206, R313-R323 | L0221-L0225, L0252-L0254, L0369-L0376, L0684-L0695 | "this new line will is able to contribute roughly 450 to 500 crores ... and ppm can add around 250 from the current level so ... we can reach roughly 3500 crore" | AMBIGUOUS | 3500 = Q2 run-rate ~2784 (696 x 4) + new SCF line 450-500 + PPF 250 (derived). The PPF 250 matches 73% utilisation (668 annual -> ~915 at full). The sum leaves out existing SCF headroom: SCF at 75% (~1420 annual) implies ~470 Cr more at full (derived). Either 3500 understates the capacity, or the SCF utilisation figure does not convert to revenue. Direction unknown: ask. Timing of full SCF utilisation also conflicts: "Q2 next year" (L0376) vs "next year Q1 we will hit almost 100 percent" (L0685). The new line comes June 2027 (L0687), so Q1 FY28 may be capacity-capped. |
| FN10 | F6 | R137-R142, R164, R310, R311, R058 | L0190-L0198, L0255-L0256, L0675-L0676, L0053 | "we will definitely aim in next three years more investments, but as of now, I can't tell unless it is approved by the board" / "we have like a lot of KPEX we expect to come but definitely I'll put forward this within the management" | FORWARD-SIGNAL | Growth past the 3500 ceiling and the 25-30% CAGR talk (L0469) need capex that the board has not approved. Expect a board capex announcement within the 12-month window. The dividend request was deflected to capex while cash is 933 Cr (L0053). The ~170 Cr capex figure from the results review was not reconciled. The call names only the 191 Cr SCF project (L0065). |
| FN11 | F6 | R223-R227, R231-R233 | L0409-L0414 | "that was approved by Ministry of Commerce however Finance Ministry did not apply it so we are taking some necessary steps to make that happen" | CONFIRMATORY-NEGATIVE | The anti-dumping duty on Chinese PPF was recommended but not imposed. The Notion open item resolves to NOT NOTIFIED. The "necessary steps" are undated and not described (legal challenge, fresh application or representation). PPF share stays at 60% against cheap imports (L0420-L0422). Any PPF share gain must come without ADD support. |
| FN12 | F6 | R087-R095, R325-R339 | L0698, L0705, L0708-L0714, L0076 | "I didn't give 200 crore for one year so the target are like 50 crore first year I mean next year then 100 crore and then 200 crore" | AMBIGUOUS | An analyst recalls "200 cr revenue from the home solution ... by f528" from last quarter (L0698). Management restates it as 50 Cr in FY28, then 100, then 200. Without the prior transcript this is either a walk-back or an analyst misreading. Studio count conflicts: "40 studios in h1" (L0705) vs "we added 14 studios" (L0708) and 9 -> 14 (L0074-L0075). The 50-studio date is "December 2027" (L0076) vs "next ... 9 to 12 months" (L0709). Check against the Q1 FY27 transcript. |
| FN13 | F7 | R364-R366 | L0767-L0771 | "they asked us that this was run despite told not to run but we accepted this is okay" / "our normally plans are pretty old" | AMBIGUOUS | The MPCB matter came up only because an analyst asked. Prepared remarks were silent. Management admits running a boiler against a regulator direction and blames "miscommunication". It calls the matter a penalty. The Reg 30 filing (Notion) calls it a 25 lakh bank-guarantee forfeiture. The amount is small. The signals are aged plant and a compliance lapse admitted on record. Ask about other open MPCB directions and consent conditions. |
| FN14 | F17 | R018, R409 | L0026, L0835 | "Today on the call we are joined by Mr. Deepak Joshi, Director Sales & Marketing." / "the volume, so that's why we give revenue numbers" | AMBIGUOUS | The only company speaker is the sales director. No CMD, promoter or CFO spoke. Every finance and governance open item went unanswered (other income in EBITDA, finance cost, receivable discounting, subsidiary transfer pricing, CFO vacancy, joint auditor change). He also declined volume data, so price and mix cannot be split from volume. Silence count 1 (prior NOT FOUND). It becomes CONFIRMATORY-NEGATIVE if it repeats at Q3. |
| FN15 | F7 | R187-R197, R351-R375 | L0328-L0341, L0757, L0775 | "if it goes up definitely there is a challenge but we will try to pass on this to our customers normally we pass on in some cases easily in some cases with difficulty" / "maybe 650-660 only 40-50 crore will be affected" | AMBIGUOUS | Q2 absorbed a 37 Cr cost headwind (RM +4%, logistics +9 Cr, L0328-L0330), restated as "35 crore plus" (L0356). The RM part (28 Cr, derived) is hard to square with a 4% rise on an RM base of ~45-50% of costs (L0776). Ask for the split. 40-50 Cr of quarterly revenue is crude-linked price that unwinds if crude falls (L0775). Prices were raised "couple of months ago" (L0757). Lower crude cuts revenue and helps margin. Higher crude passes through only partly. |
| FN16 | F14 | R283, R284, R302-R304 | L0628-L0629, L0662-L0663 | "for medium term 28 to 31 you have mentioned 27 percent plus and down below that you have mentioned 150 to 200 bits plus for TPU backward integration" | NEUTRAL-FACT | The presentation's medium-term guidance (FY28-FY31) is 27%+ plus 150-200 bps TPU, about 28.5-29%. "28 to 31" is the years, not the margin. A4 must not read it as a 28-31% margin band. The medium-term floor is the same as the FY27 midpoint: past TPU, the deck guides no further expansion. |
| FN17 | F14 | R129-R131, R153, R154, R410-R413 | L0156-L0158, L0237, L0836 | "today we are roughly 30% of our sales is coming from architectural business. So from window films" vs "30% of SCF sales" | NEUTRAL-FACT | Architectural is 30% of SCF, not of company sales. 30% x 51% x 696 x 4 = ~426 Cr (derived), which matches "roughly 400 crore" (L0159). Geography split US 51 / EU 15 / India 20 / RoW 12 sums to 98% (L0836). These are drafting or ASR errors. The pattern is spoken figures shifting between bases. |
| FN18 | F7 | R346-R349, R381-R382, R384-R389 | L0742-L0744, L0792, L0798-L0801 | "they go up to 40-45% I'm talking about beta margin ... medium kind of product is 30 to 35%. PPS remains 20 to 25%." | AMBIGUOUS | Product margins are disclosed but the basis is undefined ("beta margin", likely EBITDA, ASR). IPD is 10-12% (L0792). A weighted check (51% x ~35 + 24% x ~22.5 + 25% x ~11 = ~26%, derived) is close to the 27% reported EBITDA, so EBITDA-level is plausible. D2C "+10-15% on existing margins" (L0798) is unclear: pp or relative. PPF is the lowest-margin consumer line, and the TPU bridge (FN08) targets it. |

## CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | N.A. | Concall. No line-item template. A2: ZERO_STANDING none. |
| F2 | N.A. | No standalone vs consolidated tables on a call. The only subsidiary reference (US tariff refund, L0539) is logged at FN03. |
| F3 | N.A. | No cost-line tables by entity. |
| F4 | N.A. | No auditor Other Matters on a call. |
| F5 | N.A. | No EoM / going-concern text. No prior transcript. |
| F6 | FINDING | 20 commitments registered. Status-relevant: TPU "on track" vs "yet to start commissioning" (FN06), FY27 guidance implies H2 step-down (FN02), FY28 "28 28.5 for sure" (FN08), 3500 ceiling arithmetic (FN09), capex pending board (FN10), ADD not imposed (FN11), D2C target restated (FN12). |
| F7 | FINDING | Hedges and qualifiers on concentration (FN04), channel inventory (FN05), Lubrizol "first trial" (FN07), MPCB (FN13), cost pass-through "with difficulty" (FN15), undefined margin basis (FN18), TPU estimate "initial estimate" (L0580), "exact number I can't quote" (L0623). |
| F8 | PASS | H1 PBT 350, PAT 262 -> ETR 25.1% (derived) vs statutory 25.17%. No deferred-tax or prior-year tax disclosure on the call. |
| F9 | N.A. | No OCI on a call. |
| F10 | N.A. | No paid-up capital or EPS on the call. |
| F11 | N.A. | No net worth figures. Cash 933 Cr only (L0053). |
| F12 | N.A. | Segment revenue shares and utilisation only. No segment assets or liabilities. Capacity arithmetic is logged under F6 (FN09). |
| F13 | N.A. | No board outcome on the call. The board-pending capex (L0192) is logged at FN10. |
| F14 | FINDING | Internal inconsistencies: H1 margin 26.30% vs derived 28.7% (FN01), "28 to 31" period vs margin (FN16), 30% of sales vs SCF and geography 98% (FN17), studio count 40 vs 14 (FN12), tariff accounting self-contradiction (FN03). Most are ASR-attributable. FN03 is management-attributable. |
| F15 | N.A. | No consolidation entity list on a call. |
| F16 | N.A. | Presentation-specific. The deck is referenced only through analyst readings (FN16). |
| F17 | FINDING | 10 checklist items not addressed and 3 partly addressed (table below). Management limited to the sales director (FN14). |

## COMMITMENT REGISTER (F6)

| # | commitment | implied date | ref | status word |
|---|---|---|---|---|
| C01 | TPU film line commissioning | Q3 FY27 (by 31-Dec-2026) | L0063; L0604-L0605 | underway ("on track"; "yet to start commissioning") |
| C02 | TPU external (25% merchant) sales 75-100 Cr at ~35% EBITDA | FY28 ("not this year") | L0578-L0608; L0829 | initiated (estimate, "initial estimate" L0580) |
| C03 | TPU captive (75%) to PPF: +150-200 bps consolidated margin | FY28 onward | L0813; L0663-L0668 | initiated |
| C04 | Lubrizol MoU, resin purchase understanding, joint OE marketing | undated | L0064; L0127-L0146; L0820-L0824 | initiated (MoU signed per Notion 24-Sep-2026) |
| C05 | SCF capacity expansion 191 Cr, ~1200 lakh sq ft fungible, commercial production | H1 FY28, "roughly by June 2027", "try a little early" | L0065-L0066; L0250; L0687 | underway ("progressing") |
| C06 | New SCF line adds 450-500 Cr; PPF adds ~250 Cr; peak 3500 Cr at full utilisation | FY28-FY29 (not dated) | L0221-L0254; L0693-L0695 | stated capacity, not a forecast (L0254) |
| C07 | FY27 revenue > 2500 Cr (reaffirmed) | FY27 | L0085; L0201 | reaffirmed |
| C08 | FY27 EBITDA margin 27% +/- 2% (upgraded from 25 +/- 2) | FY27 | L0085; L0645 | upgraded |
| C09 | FY28 revenue "targeting 3000 plus" | FY28 | L0624 | new (exact number "can't quote") |
| C10 | FY28 margin "28 plus", "28 28.5 for sure"; FY28 guidance "elevated" | FY28 | L0644-L0646 | new |
| C11 | Medium-term margin 27%+ plus 150-200 bps TPU (presentation) | FY28-FY31 | L0662-L0668 | restated |
| C12 | PPF utilisation to ~90% | ~6 months (by ~Apr 2027) | L0372-L0373 | underway (73% Q2) |
| C13 | SCF full utilisation | Q2 FY28 (L0376) or Q1 FY28 (L0685), conflicting | L0376; L0685 | underway (75% Q2) |
| C14 | Final US tariff refund ~30 Cr (16 Cr to books, 14 Cr to customers) | Q3 FY27 | L0389-L0392 | expected, "the last one" |
| C15 | Anti-dumping duty: "taking some necessary steps" | undated | L0412-L0414 | stalled (Commerce approved, Finance did not impose) |
| C16 | Home solution studios +12 in Q3 (14 -> 26); 50 studios | Q3 FY27; Dec 2027 (L0076) or 9-12 months (L0709) | L0075-L0076; L0709 | underway |
| C17 | D2C revenue 50 Cr, then 100 Cr, then 200 Cr | FY28 for 50 Cr; rest undated | L0712-L0714 | restated (vs analyst's recalled 200 Cr by FY28, L0698) |
| C18 | Architectural to 1000 Cr; 50% of window film; 35-40% growth; each segment >= 20% growth | undated | L0246; L0180; L0838 | target |
| C19 | 25-30% growth, exports and domestic; run rate 3000-3500 | undated ("next two, three years" in question) | L0466-L0470 | target |
| C20 | Further capex in next three years, subject to board; dividend request "put forward within the management" | within 3 years; undated | L0190-L0198; L0675-L0676 | not yet approved |
| C21 | Q1 margin ~30% "sustainable seasonal level"; Q3 seasonally low, Q4 back | ongoing | L0045; L0655 | stated pattern |

## WHAT WAS NOT DISCUSSED (F17 silence audit vs Notion checklist)

| item | addressed? | cite / note | consecutive quarters silent |
|---|---|---|---|
| TB1 ROCE < 15% for 2 quarters | NO | ROCE never mentioned | 1 (prior NOT FOUND) |
| TB2 34% customer cuts volume > 20% | PARTIAL | Concentration acknowledged (L0262). No volume data, volume split declined (L0835). Customer "growing their business" (L0274) is assertion. | 1 on volume |
| TB3 operating EBITDA margin < 18% for 2 quarters | YES (not breached) | Q2 27.2% (L0039). "Operating" basis vs other income not stated. | 0 |
| TB4 promoter verdict AVOID on re-run | NO | No promoter or CMD on the call (L0026) | 1 |
| Identity of 34% customer | PARTIAL | "best car or EV car seller in US" (L0266, ASR). Not named. Not architectural (L0278). | 1 on identity |
| FY27 revenue vs base; guidance 2500+ and 27% +/- 2% incl. other income | PARTIAL | Guidance restated (L0085). "Including other income" basis not stated. | 1 on basis |
| TPU commissioning Q3 FY27 | YES | L0063; L0604-L0605 ("yet to start commissioning") | 0 |
| Lubrizol TPU MoU | YES | L0127-L0146; L0810-L0832. Terms not disclosed. | 0 |
| ADD notification | YES | Not imposed by Finance Ministry (L0411-L0412) | 0 |
| MPCB 25 lakh BG forfeiture | YES (analyst-prompted) | L0767-L0771. Absent from prepared remarks. | 0 |
| H2 margin excluding other income | NO | Only "Q3 will be seasonally low but Q4 will be back" (L0655) | 1 |
| ~170 Cr capex (FY27 or medium term) | NO | Call cites 191 Cr SCF (L0065) and 900 Cr over six years (L0188). 170 not reconciled. | 1 |
| Subsidiary transfer pricing; Q2 subsidiary PAT jump | NO | Only the US subsidiary tariff refund through COGS (L0539-L0545), a candidate driver (FN03) | 1 |
| Finance cost nature (no borrowings) | NO | Not raised | 1 |
| Receivable discounting | NO | Only "sold out with advances" (L0321-L0322) | 1 |
| US and Middle East revenue share | YES | US 51%, RoW 12% "basically Middle East" (L0836) | 0 |
| CFO vacancy | NO | No CFO on the call | 1 |
| Joint auditor change | NO | Not raised | 1 |

## A4 HAND-OFF (FORWARD-SIGNAL and AMBIGUOUS findings to convert into questions)
FORWARD-SIGNAL: FN02, FN04, FN06, FN08, FN10.
AMBIGUOUS: FN03, FN05, FN07, FN09, FN12, FN13, FN14, FN15, FN18.

```yaml
stage: A3-forensics
company: "GRWRHITECH"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/grwrhitech-q2fy27/work/forensics_concall_grwrhitech_q2fy27.md"
ledger_reconciled_pct: 100        # 419 of 419 structured rows + MFS01 (L0520) read at fulltext line
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "FN01", check: "F14", line: "L0047-L0049", classification: "NEUTRAL-FACT", implication: "H1 margin stated 26.30% conflicts with 381/1329 = 28.7% derived (YoY +464 bps also gives 28.7%); use 28.7% [derived, ASR] pending filed transcript"}
  - {id: "FN02", check: "F6", line: "L0085; L0645; L0655", classification: "FORWARD-SIGNAL", implication: "Revenue floor 2500 not raised on H1 1329; 27% midpoint implies H2 margin ~25.1% vs H1 28.7% (derived); Q2 PAT 129 < derived Q1 133; other-income basis of guidance not stated"}
  - {id: "FN03", check: "F7", line: "L0386-L0392; L0539-L0545", classification: "AMBIGUOUS", implication: "27 Cr one-time US tariff refund to books via COGS at US subsidiary (11 to date, 16 in Q3, last one); flatters Q2/Q3 margin; accounting description self-contradictory; candidate driver of subsidiary PAT jump"}
  - {id: "FN04", check: "F7", line: "L0259-L0266; L0273-L0278", classification: "FORWARD-SIGNAL", implication: "Top customer ~30% (analyst figure, uncorrected; Notion 34%) plus a couple at half and one at one-third; automotive, US EV-linked, unnamed; concentration broader than one name"}
  - {id: "FN05", check: "F7", line: "L0299-L0322; L0054", classification: "AMBIGUOUS", implication: "Europe/US customer inventory up ~20 days; possible Q2 export pull-forward and Q3 destock; WC 29 days held via customer advances; receivable discounting unaddressed"}
  - {id: "FN06", check: "F6", line: "L0063; L0604-L0605; L0829", classification: "FORWARD-SIGNAL", implication: "TPU 'on track for Q3 FY27' but 'yet to start commissioning' on 23-Oct (inside Q3); no FY27 TPU revenue; FY28 margin bridge hinges on this date"}
  - {id: "FN07", check: "F7", line: "L0820-L0821; L0831", classification: "AMBIGUOUS", implication: "Lubrizol resin purchase 'understanding' of undisclosed quantity, possible offtake obligation; TPU vertical called 'first trial'"}
  - {id: "FN08", check: "F6", line: "L0813; L0644-L0646", classification: "FORWARD-SIGNAL", implication: "FY28 margin '28 28.5 for sure' beside 'can't comment'; 150-200 bps consolidated from PPF (24% of revenue, 20-25% margin) needs ~6-8 pp PPF margin gain (derived)"}
  - {id: "FN09", check: "F6", line: "L0221-L0254; L0369-L0376; L0684-L0695", classification: "AMBIGUOUS", implication: "3500 = run-rate 2784 + new line 450-500 + PPF 250; omits ~470 Cr existing SCF headroom at 75% (derived); SCF full timing Q1 vs Q2 FY28 conflicts; Q1 FY28 may be capacity-capped"}
  - {id: "FN10", check: "F6", line: "L0190-L0198; L0255-L0256; L0675-L0676", classification: "FORWARD-SIGNAL", implication: "Growth past 3500 needs board-unapproved capex; dividend deflected to capex with 933 Cr cash; ~170 Cr capex figure unreconciled (call cites 191 Cr SCF)"}
  - {id: "FN11", check: "F6", line: "L0409-L0414", classification: "CONFIRMATORY-NEGATIVE", implication: "ADD approved by Commerce, not imposed by Finance Ministry; 'necessary steps' undated; PPF share gains must come without ADD"}
  - {id: "FN12", check: "F6", line: "L0698; L0705-L0714; L0076", classification: "AMBIGUOUS", implication: "D2C 200 Cr by FY28 (analyst recall) restated as 50 Cr FY28 then 100/200; studios 40 vs 14; 50-studio date Dec 2027 vs 9-12 months; diff vs Q1 transcript"}
  - {id: "FN13", check: "F7", line: "L0767-L0771", classification: "AMBIGUOUS", implication: "MPCB lapse admitted ('run despite told not to run'), analyst-prompted, absent from prepared remarks; 'plants are pretty old'; penalty vs BG-forfeiture framing"}
  - {id: "FN14", check: "F17", line: "L0026; L0835", classification: "AMBIGUOUS", implication: "Only Director Sales & Marketing spoke; all finance/governance items unanswered (other income, finance cost, receivable discounting, subsidiary TP, CFO vacancy, joint auditor); volume split declined"}
  - {id: "FN15", check: "F7", line: "L0328-L0341; L0757; L0775", classification: "AMBIGUOUS", implication: "37 Cr cost headwind split (RM +4% vs 28 Cr derived) does not reconcile; 40-50 Cr/quarter revenue is crude-linked price; pass-through 'with difficulty'"}
  - {id: "FN16", check: "F14", line: "L0628-L0629; L0662-L0663", classification: "NEUTRAL-FACT", implication: "'28 to 31' is FY28-FY31 window, not a margin band; medium-term guide 27%+ plus 150-200 bps TPU; no expansion beyond TPU"}
  - {id: "FN17", check: "F14", line: "L0156-L0158; L0237; L0836", classification: "NEUTRAL-FACT", implication: "Architectural 30% is of SCF not company (~426 Cr derived matches 400); geography sums 98%; bases drift in spoken figures"}
  - {id: "FN18", check: "F7", line: "L0742-L0744; L0792; L0798-L0801", classification: "AMBIGUOUS", implication: "Product margins (SCF 40-45/30-35, PPF 20-25, IPD 10-12) on undefined 'beta margin' basis; D2C +10-15% pp vs relative unclear"}
forward_signals: ["FN02", "FN04", "FN06", "FN08", "FN10"]
ambiguous: ["FN03", "FN05", "FN07", "FN09", "FN12", "FN13", "FN14", "FN15", "FN18"]
commitments:
  - {commitment: "TPU line commissioning", implied_date: "Q3 FY27 (by 31-Dec-2026)", ref: "L0063; L0604-L0605", status_word: "underway"}
  - {commitment: "TPU external sales 75-100 Cr at ~35% margin", implied_date: "FY28", ref: "L0578-L0608; L0829", status_word: "initiated"}
  - {commitment: "TPU captive +150-200 bps consolidated margin", implied_date: "FY28", ref: "L0813", status_word: "initiated"}
  - {commitment: "Lubrizol MoU resin purchase understanding", implied_date: "undated", ref: "L0820-L0821", status_word: "initiated"}
  - {commitment: "SCF 191 Cr expansion, ~1200 lakh sq ft, commercial production", implied_date: "H1 FY28 (~June 2027)", ref: "L0065-L0066; L0250; L0687", status_word: "underway"}
  - {commitment: "Peak revenue 3500 Cr at full utilisation (new line 450-500, PPF +250)", implied_date: "undated", ref: "L0221-L0254; L0693-L0695", status_word: "initiated"}
  - {commitment: "FY27 revenue > 2500 Cr", implied_date: "FY27", ref: "L0085", status_word: "reaffirmed"}
  - {commitment: "FY27 EBITDA margin 27% +/- 2% (from 25 +/- 2)", implied_date: "FY27", ref: "L0085; L0645", status_word: "upgraded"}
  - {commitment: "FY28 revenue 3000 plus", implied_date: "FY28", ref: "L0624", status_word: "initiated"}
  - {commitment: "FY28 margin 28-28.5% 'for sure'", implied_date: "FY28", ref: "L0644-L0646", status_word: "initiated"}
  - {commitment: "Medium-term margin 27%+ plus 150-200 bps TPU", implied_date: "FY28-FY31", ref: "L0662-L0668", status_word: "restated"}
  - {commitment: "PPF utilisation to ~90%", implied_date: "~Apr 2027", ref: "L0372-L0373", status_word: "underway"}
  - {commitment: "SCF full utilisation", implied_date: "Q1 or Q2 FY28 (conflicting)", ref: "L0376; L0685", status_word: "underway"}
  - {commitment: "Final tariff refund ~30 Cr (16 to books)", implied_date: "Q3 FY27", ref: "L0389-L0392", status_word: "initiated"}
  - {commitment: "ADD 'necessary steps'", implied_date: "undated", ref: "L0412-L0414", status_word: "stalled"}
  - {commitment: "Studios +12 in Q3; 50 studios", implied_date: "Q3 FY27; Dec 2027 or 9-12 months", ref: "L0075-L0076; L0709", status_word: "underway"}
  - {commitment: "D2C revenue 50 Cr then 100 then 200", implied_date: "FY28 for 50 Cr", ref: "L0712-L0714", status_word: "restated"}
  - {commitment: "Architectural to 1000 Cr, 50% of window film, 35-40% growth; segments >= 20%", implied_date: "undated", ref: "L0246; L0180; L0838", status_word: "initiated"}
  - {commitment: "Further capex in 3 years subject to board; dividend request to management", implied_date: "within 3 years", ref: "L0190-L0198; L0675-L0676", status_word: "initiated"}
  - {commitment: "Q1 ~30% margin sustainable; Q3 seasonally low, Q4 back", implied_date: "ongoing", ref: "L0045; L0655", status_word: "restated"}
gate_a3: pass
blank_checks: []
analyst_note: "Three numbers frame H2. (1) H1 EBITDA margin is 28.7% on the stated 381/1329. The spoken 26.30% is an ASR or basis conflict, so A4 should not anchor on it. (2) A 27% FY27 midpoint and an unraised 2500 floor imply an H2 margin near 25%. Q3 also carries a 16 Cr one-time tariff refund through COGS. Underlying H2 may sit below 25%, and Q2's 27.2% may include up to 11 Cr of the same refund. (3) Whether guided EBITDA includes other income is unanswered on the call. With 933 Cr cash this decides how close operating margin runs to thesis-broken 3. The FY28 28-28.5% 'for sure' depends on a TPU line that had not started commissioning inside its own deadline quarter. It also needs a 6-8 pp PPF margin gain. Concentration runs wider than one customer. No volume data, so thesis-broken 2 cannot be monitored from calls. All finance and governance items went unanswered because only the sales director spoke. Silence count 1; repeat at Q3 = CONFIRMATORY-NEGATIVE. All figures are ASR. A4 should confirm FN01, FN03 and FN09 against the filed transcript when it posts."
```
