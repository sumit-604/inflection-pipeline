# A3 FORENSIC NOTES — CONCALL — ECOSMOBILITY (ECOS India Mobility & Hospitality Ltd) — Q1 FY27

**Doctype:** concall (Q1 FY27 earnings call, quarter ended 30 June 2026; transcript, 105 source lines)
**Model:** claude-opus-4-8 | **Agent:** A3 FORENSIC NOTES
**Inputs reconciled:** A1 extract (105 lines), A2 concall ledger (all flag rows read at cited lines), prior merged review (Step 6C SETTLED trigger + Role 5 grade C, carried consistent), new-docs verified supplement, Notion thesis digest.
**Ledger reconciliation:** 100% — every A2 flag row read verbatim at its source line before judging: NUMBER_DISCREPANCY (L21); ZERO_STANDING ×5 (L37, L65, L69, L83, L91); DROPPED_QUESTION (L92); MULTI_QUESTION_TURN (L95); REPEAT_QUESTION ×3 clusters (margin L32/L56/L74; employee cost L40/L86; active-client count L76/L96).

**Consistency note (bound to the merged review, not re-opened):** the Step 6C thesis-break trigger stays SETTLED / NOT-FIRED on its literal measure (consolidated reported EBITDA margin sub-12% ×3 consecutive; Q4 FY26 13.43% resets any run). This forensic file does NOT re-open that verdict; it hunts the concall for what it tells us about the FUTURE and feeds A4/Role 5. Role 5 this quarter is UPGRADED from the deck-only C (Mixed) read because a live, adversarial Q&A now exists — the pushed answers are the new evidence.

---

## SECTION 1 — FINDINGS TABLE

Classification taxonomy (A3 operating rules): FORWARD-SIGNAL / AMBIGUOUS / CONFIRMATORY-NEGATIVE / NEUTRAL-FACT. Severity annotation in brackets uses the task's RED-FLAG / AMBIGUOUS / FORWARD-SIGNAL / BENIGN scale. FORWARD-SIGNAL and AMBIGUOUS findings are flagged `→A4` for conversion into management questions.

| id | check | ledger row | line/turn | verbatim quote | classification [severity] | forward implication |
|----|-------|-----------|-----------|----------------|---------------------------|---------------------|
| **F6-01** | F6 | Sec.5 row 4 (guidance) | **L23** (CFO) | "we now expect EBITDA margin for FY27 to be around 10%" | **FORWARD-SIGNAL [RED-FLAG]** `→A4` | Formal DOWNWARD guidance revision one quarter after the guide. ~10% EBITDA on 15-18% revenue = FY27 absolute EBITDA ~₹93 Cr ≈ FY26 ₹93.9 Cr → **THIRD consecutive flat/profitless bottom-line year.** |
| **F7-01** | F7 | (guidance reframing) | **L23** (CFO) / L32 (analyst) | "below the 11% to 13% which we had initially indicated for FY27" | **AMBIGUOUS [RED-FLAG]** `→A4` | Notion record tracked FY27 recovery band as **13-15%**; management now anchors "initial" guide at **11-13%**, then cuts to ~10%. A downward walk of the reference point itself. Analyst Jani independently cites "11-13%" (L32), which partly corroborates an FY27-specific 11-13% guide vs the 13-15% multi-year target — ambiguous, not resolved; A4 must pin which band was ever formal. |
| **F17-01** | F17 | (credibility, external) | **L44** (Pulkit Singh, Dness Capital) | "Changing guidance in one quarter does not help ... we expect more transparency around guidance so sudden changes are not based on one month of data" | **CONFIRMATORY-NEGATIVE [RED-FLAG]** `→A4` | External, on-record corroboration of a guidance-credibility problem. Management acknowledged ("I understand your frustration ... we should have guided better", L45). Directly feeds Role 5 promise-vs-delivery. |
| **F14-01** | F14 | NUMBER_DISCREPANCY | **L21** (CFO) | "Our EBITDA margin for the quarter was 9.3% [as transcribed; reconciles to reported 10.34%]" | **AMBIGUOUS [BENIGN-lean]** `→A4` | Stated 9.3% vs reported/audited 10.34%. Most probable = transcription artifact of spoken "10.3%" (single digit dropped; deck/results tie exactly at 10.34%). Flagged either way: if genuine, a CFO understating margin ~100bps on-record is a disclosure-hygiene issue. Lean transcription artifact; carry both. |
| **F1-01** | F1 | ZERO_STANDING ×5 | **L69** (canonical) + L37/L65/L83/L91 | "No, we do not declare that; costs are common to the organization ... hard to give an accurate division" | **CONFIRMATORY-NEGATIVE + AMBIGUOUS [RED-FLAG on L69]** `→A4` | Management REFUSED the ETS-vs-CCR segment-EBITDA-margin split — the single most-requested disaggregation in a mix-driven margin decline. Refusing to show which segment bleeds, while conceding decline is "more evident in ETS" (L61), is a non-disclosure that conceals the direction of the compression. See F17 silence table for the other four. |
| **F12-01** | F12 | (segment economics) | **L12 / L57 / L61** | "More evident in ETS because it is bulk / mass business" (L61); "we absorb part of that low rate out of the margins we get from our vendors" (L57) | **FORWARD-SIGNAL [FORWARD-SIGNAL/RED-FLAG]** `→A4` | ETS rose to 59% of revenue (L12, up QoQ). Price cuts to win business are absorbed off vendor margins, concentrated in ETS bulk work. Mix is shifting toward the lower-yield, thinner-margin segment; corroborates the revenue-per-trip −8% mechanical driver. Margin compression is structural/mix-led, not one-off. |
| **F6-02** | F6 | Sec.5 row 12 | **L75** (CMD) | "the operating leverage will start kicking in at some point — which we feel at something over ₹1,000 crores of revenue" | **FORWARD-SIGNAL [FORWARD-SIGNAL]** `→A4` | Recovery/inflection pushed to the FY28 revenue milestone (~₹1,000 Cr; ₹845 Cr annualised now). No FY27 margin recovery underwritten — consistent with the ~10% guide. The thesis's operating-leverage leg is explicitly deferred a full year. |
| **F6-03** | F6 | Sec.5 rows 1/10/2 | **L16 / L45** (CMD) | "expecting to launch our B2C app this quarter" (L16); CCR automation "once settled (within this quarter) it will start delivering productivity results" (L45) | **FORWARD-SIGNAL [FORWARD-SIGNAL]** `→A4` | Two dated Q2 FY27 milestones create a testable promise-vs-delivery checkpoint next quarter (B2C app live; CCR-automation productivity showing in employee cost). SIXT "progressing as planned" (L16) is undated — softer. |
| **F13-01** | F13 | Sec.5 rows 7/9 | **L27 / L39** (CFO/CMD) | "final dividend of INR 2.38 per equity share ... subject to shareholder approval at the upcoming AGM" (L27); "Only last month we onboarded a senior professional in strategic finance" (L39) | **FORWARD-SIGNAL + NEUTRAL-FACT [BENIGN]** `→A4` | AGM is the next governance/return event (per review ~21 Sep 2026). ₹150 Cr cash + fresh senior strategic-finance hire + "will be looking at certain opportunities" = M&A optionality being staffed up. Capital-deployment optionality AND risk: buyback/return pushback (L38) deflected; cash could fund margin-dilutive M&A into adjacencies with no demonstrated moat. |
| **F7-02** | F7 | Sec.6 rows 1/6/7 | **L33 / L75 / L83** (CMD) | "we are not sure of the longevity of this intensity of competition or how long it lasts" (L75); "I would not comment on moderation" (L83) | **FORWARD-SIGNAL [FORWARD-SIGNAL]** `→A4` | Cluster of pre-emptive hedges on the margin/pricing path. "Hopeful of maintaining these margins" (L33, not "improving") + refusal to call moderation = management is signalling Q2 pricing pressure remains live. A hedge, not a recovery. |
| **F17-02** | F17 | DROPPED_QUESTION | **L92** (Sapphire Capital) | "With the increase in oil prices, has the vendor been reluctant ... [Question not completed — participant line dropped.]" | **AMBIGUOUS [AMBIGUOUS]** `→A4` | Vendor cost pass-through under oil-price inflation went unanswered (line dropped, no management response recorded). In a vendor-sourced model this is a live margin input; the silence is mechanical, not a refusal, but the input is unaddressed. A4 should re-ask. |
| **F17-04** | F17 | (moat/returns challenge) | **L52 / L53** (Kesha Gag; CMD) | "return on capital will come around the cost of capital" (L52); CMD three-part "right to win": relationships / vendor supply base / processes (L53) | **AMBIGUOUS [AMBIGUOUS]** `→A4` | Analyst framed the industry as no-entry-barrier → ROCE→WACC. CMD's defence is qualitative/narrative (client relationships, supply base, processes) with NO quantified moat evidence, offered in the same call ROCE is disclosed to have fallen 42.9%→29.4%. Directionally the numbers side with the challenger, not the defence. Assess as narrative, not substantiated. |

**Findings not separately tabled but logged in-check:** F17 silence table (Section 3) carries the remaining ZERO_STANDING refusals (L37 event-mgmt "not very material"; L65 client losses "not majorly"; L83 moderation refused; L91 no B2C target) and the three REPEAT_QUESTION clusters. F6 commitment register (Section 4) carries all dated management commitments.

---

## SECTION 2 — CHECKLIST SCORECARD (all 17; no blanks — GATE A3)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 — Zero-value standing / non-disclosure register | **FINDING** | 5 ZERO_STANDING refusals; canonical = segment-margin split refused (L69). |
| F2 — Standalone vs consolidated decomposition | **N.A.** | Concall carries consolidated CFO remarks only; no S-vs-C tables to decompose. (Done in results A3.) |
| F3 — Shell-entity detection | **N.A.** | No standalone-vs-consolidated cost lines in a transcript. |
| F4 — Unaudited contribution ratio | **N.A.** | No auditor Other-Matters paragraph in a concall. |
| F5 — Going concern / EoM scope | **N.A.** | No auditor / EoM language on the call. |
| F6 — Forward-commitment phrase mining | **FINDING** | Guidance cut to ~10% (L23), rev 15-18% (L49), B2C app + CCR-automation this quarter (L16/L45), op-leverage deferred to >₹1,000 Cr (L75), M&A (L39), dividend (L27). |
| F7 — Hedge phrase mining | **FINDING** | 10 hedges; pre-emptive margin/pricing hedges (L33/L75/L83) + guidance reframing (L23). |
| F8 — Tax forensics | **N.A.** | No tax-rate / deferred-tax commentary on the call (implied ETR 24.08% ties to results, examined in results A3 F8-01). |
| F9 — OCI forensics | **N.A.** | No OCI / actuarial discussion in the transcript. |
| F10 — Share count & dilution | **N.A.** | No share-count / instrument discussion; no capital action on the call. |
| F11 — Reserves & net-worth tie-out | **N.A.** | Only cash ₹1,558 Mn stated (L27); no net-worth reconciliation in a transcript. |
| F12 — Segment forensics | **FINDING** | ETS to 59% mix (L12); gross-margin decline "more evident in ETS" (L61); price cuts absorbed off vendor margins (L57); segment margin split refused (L69). |
| F13 — Board outcome beyond results | **FINDING** | Final dividend ₹2.38 pending AGM (L27); senior strategic-finance hire + M&A exploration (L39); ₹150 Cr cash deployment optionality. |
| F14 — Drafting / stated-figure inconsistency | **FINDING** | Stated EBITDA margin "9.3%" (L21) vs reported/audited 10.34% — NUMBER_DISCREPANCY. |
| F15 — Entity list diffs | **N.A.** | No consolidation-list disclosure in a concall. |
| F16 — Presentation-specific (dropped/reframed disclosures) | **N.A.** | Doctype is concall, not presentation (handled in new-docs A3 F16-01..06). |
| F17 — Concall silence audit | **FINDING** | Dropped Q8 (L92); 5 refusals/nils; guidance-credibility pushback (L44); 3 REPEAT_QUESTION clusters; moat-challenge non-substantive (L53). |

**Tally:** FINDING ×7 (F1, F6, F7, F12, F13, F14, F17) · N.A. ×10 · PASS ×0 · blank ×0. **GATE A3: PASS.**

---

## SECTION 3 — F17 CONCALL-SILENCE AUDIT ("What Was NOT Discussed / Was Refused")

Cross-referenced against the F6 commitments, the Notion monitoring checklist (7 tripwires) and the A2 REPEAT_QUESTION clusters. Per Role 5, sustained silence on a deteriorating metric is a confirmatory negative.

| Topic asked / expected | Line | Management response | Silence type | Consecutive-Q silence | Read |
|------------------------|------|---------------------|--------------|------------------------|------|
| **ETS vs CCR segment EBITDA-margin split** | L68→L69 | "No, we do not declare that" | REFUSED | ≥2Q (deck was also silent) | **CONFIRMATORY-NEGATIVE** — the most-requested disaggregation in a mix-driven decline; refusal conceals which segment bleeds. |
| **Is ETS pricing pressure moderating vs FY26?** | L82→L83 | "I would not comment on moderation" | REFUSED | 1Q (first live Q&A) | **FORWARD-SIGNAL** — refusing to call moderation = pressure still live into Q2. |
| **Oil-price impact on vendor economics** | L92 | (line dropped, no answer) | DROPPED | 1Q | **AMBIGUOUS** `→A4` — live margin input unaddressed; re-ask. |
| **B2C app FY27 revenue/user target** | L90→L91 | "we don't have a high target this year ... from next year we will schedule a guidance" | DEFERRED / no target | new | FORWARD-SIGNAL — optionality with zero near-term contribution; guidance explicitly pushed to FY28. |
| **Event-management new line — size/economics** | L36→L37 | "This is not very material" | MINIMISED / no number | new (board-approved object-clause change per results F13-01) | NEUTRAL-FACT→watch — sized as immaterial; A4 to confirm capital/margin at AGM. |
| **Client losses to competition** | L64→L65 | "Not majorly. Maybe one or two ..." | SOFTENED / no count | 1Q | NEUTRAL-FACT — no hard number; benign but uncorroborated. |
| **Buyback / shareholder return on ₹150 Cr cash** | L38→L39 | deflected to "certain opportunities ... better picture in coming quarters" | DEFLECTED | 1Q | AMBIGUOUS — capital-return question dodged; cash may route to M&A instead. |
| **Cash-flow statement / CFO-PAT (Notion tripwire 6)** | — | not mentioned | UNADDRESSED | ≥2Q (INDETERMINATE per review) | CONFIRMATORY-NEGATIVE — half the quality thesis; resolves only at FY26 AR. |
| **13-15% EBITDA / FY28 ₹1,000-1,200 Cr targets (as previously guided)** | L23/L75 | reframed to 11-13% then cut to ~10%; inflection reaffirmed only at ">₹1,000 Cr" undated | REFRAMED / WITHDRAWN | ≥2Q | CONFIRMATORY-NEGATIVE — load-bearing thesis numbers walked down. |

**REPEAT_QUESTION clusters (A2) — disclosure-quality signal:** analysts pressed the SAME unresolved points across independent questioner blocks — margin trajectory (L32 Jani / L56 Jain / L74 Sam Sha), employee cost (L40 Jani / L86 Salon Sha), active-client count reconciliation (L76 Sam Sha / L96 Chen). Three independent clusters = the call did not resolve the margin/cost/client-count questions to analysts' satisfaction on first ask. **Carried as CONFIRMATORY-NEGATIVE on disclosure quality.**

**Resolved-on-call (NOT silence — consistency confirmed):** active-client 1,400 vs >1,700 total reconciled (L77); online booking 14% given (L95); ETS 15 + CCR 46 = 61 new clients (L100); fleet utilization 10-11k of ~19k (L81). MULTI_QUESTION_TURN (L95) — both bundled asks answered inline. These are transparency positives that keep Role 5 out of grade D.

---

## SECTION 4 — COMMITMENT REGISTER (F6)

| Commitment | Implied date | Turn/line | Status word |
|-----------|--------------|-----------|-------------|
| FY27 EBITDA margin ~10% (REVISED down from 11-13% "initial" / 13-15% Notion) | FY27 | L23 | revised / guidance |
| FY27 revenue growth 15-18% (reaffirmed) | FY27 | L49 | reaffirmed |
| FY27 employee cost +~20% | FY27 | L25 / L41 / L87 | guidance |
| B2C app launch (premium CCR) | Q2 FY27 ("this quarter") | L16 / L91 | underway (no FY27 target; FY28 guidance) |
| CCR automation platform — settle & deliver productivity | within Q2 FY27 | L45 | in transition / underway (built over ~2 yrs) |
| SIXT India-GSA distribution build-out | ongoing / undated | L16 | progressing as planned |
| M&A opportunities — "better picture" | coming quarters | L39 | initiated (senior strategic-finance hire onboarded last month) |
| Operating-leverage inflection | at >₹1,000 Cr revenue (~FY28) | L75 | deferred (structural) |
| Internal pricing threshold below which no business | ongoing | L33 / L35 / L83 | in place (undisclosed level) |
| Final dividend ₹2.38/share FY26 | pending AGM (~21 Sep 2026) | L27 | board-recommended / contingent |
| Leadership-bandwidth hiring | through FY27 | L16 / L87 | underway |
| B2C revenue guidance | from FY28 ("next year") | L91 | deferred |

---

## SECTION 5 — GUIDANCE-vs-DELIVERY (feeds A4 Role 5)

**The downward walk of the margin guide (three reference points, one direction):**

| Reference point | Source | EBITDA margin |
|-----------------|--------|---------------|
| Prior recovery guide (thesis-tracked, analyst-corroborated Q2/Q3 FY26) | Notion digest | **13-15%** |
| "Initially indicated for FY27" (as retro-framed on THIS call) | L23 (CFO); L32 analyst echoes "11-13%" | **11-13%** |
| **Revised on this call** | L23 (CFO) | **~10%** |
| **Actual delivered Q1 FY27** | L21 (reconciled 10.34%) | **10.34%** |

**Adjudication of the reframing:** AMBIGUOUS, lean bear. Either (a) the FY27-specific initial guide was genuinely 11-13% while 13-15% was the multi-year recovery target — partly supported by analyst Jani independently citing 11-13% (L32); or (b) management is retro-lowering the anchor after the miss. Conservative call: the reference point has been walked down 13-15 → 11-13 → 10 regardless of which framing is "official," and A4 must pin which band was ever formal (question 10 in the review already carries this).

**Delivery arithmetic — the third flat year (quantified):**
- FY26 revenue from ops ₹808.2 Cr; EBITDA (excl OI) ₹93.9 Cr (11.6%).
- FY27 at +15-18% revenue → **₹929-954 Cr**. At ~10% EBITDA margin → **₹93-95 Cr EBITDA**.
- vs FY26 ₹93.9 Cr → **essentially FLAT (−1% to +1.6%)**. Absolute EBITDA plateau extends: FY24 ₹90.0 → FY25 ₹92.4 → FY26 ₹93.9 → **FY27e ~₹93-95 Cr**.
- Under the original 13-15% guide, FY27 EBITDA would have been ₹121-143 Cr. The ~10% guide is a **₹28-50 Cr (23-35%) haircut** to the EBITDA the thesis underwrote.
- With PAT flatter still (FY25 −, FY26 −4.2%), the ~10% + 15-18% combination = **a THIRD consecutive year of flat/profitless bottom line.** This is the central forensic conclusion of the call.

**Role 5 credibility read (this-quarter, live Q&A now available):** management CUT margin guidance one quarter after issuing it, on ~one month of data (analyst L44), reframed the anchor downward, and REFUSED the segment split that would show where the miss sits — while defending the moat qualitatively as ROCE falls 42.9%→29.4%. Growth claims remain corroborated and operational reconciliations (client count, mix, fleet, online %) were answered transparently, which keeps this out of grade D. Net: consistent with the deck-derived **grade C (Mixed)**, now with live-Q&A evidence of a guidance-reliability problem (external corroboration L44). Discount forward margin commentary 30-50%; anchor to filing numbers.

---

## SECTION 6 — FORWARD-SIGNAL / AMBIGUOUS LIST (for A4 conversion into management questions)

**FORWARD-SIGNAL (`→A4`):**
- **F6-01** — FY27 EBITDA guidance cut to ~10% → third flat/profitless year. (RED-FLAG severity.)
- **F12-01** — ETS mix to 59%, price cuts off vendor margins concentrated in ETS → structural/mix-led compression.
- **F6-02** — operating leverage deferred to >₹1,000 Cr revenue (FY28) → no FY27 recovery underwritten.
- **F6-03** — B2C app + CCR-automation dated to Q2 FY27 → testable milestones next quarter.
- **F7-02** — pre-emptive margin/pricing hedges (L33/L75/L83) → Q2 pressure still live.
- **F13-01** — ₹150 Cr cash + strategic-finance hire + M&A → capital-deployment optionality AND margin-dilution risk.
- **F17-03** — B2C no-target / event-mgmt "not very material" / moderation refused → forward disclosure gaps.

**AMBIGUOUS (`→A4`):**
- **F7-01** — guidance reframing 13-15 → 11-13 → 10; which band was ever formal?
- **F14-01** — stated 9.3% vs reported 10.34%; transcription artifact or misstatement?
- **F17-02** — dropped oil-price/vendor question (L92); re-ask vendor cost pass-through.
- **F17-04** — "right to win" moat defence is narrative, not quantified, against falling ROCE.
- **F1-01 (segment leg)** — segment-margin split refused (L69); which segment carries the compression?

**CONFIRMATORY-NEGATIVE (recorded, feed Role 5 tracker):**
- **F17-01** — analyst on-record guidance-credibility pushback (L44), management acknowledged.
- **F1-01** — segment-margin refusal conceals compression direction.
- **F17-03 / REPEAT clusters** — three independent analyst clusters press unresolved margin/cost/client-count points.

---

## SECTION 7 — CROSS-CHECK CONSISTENCY (spoken figures vs deck/results)

All management-spoken figures tie to the deck/results verified supplement (no number games): revenue ₹2,113.72 Mn ✓; EBITDA ₹218.47 Mn ✓; PAT ₹145.50 Mn ✓; cash & investments ₹1,558 Mn ✓; trips ~1.48 Mn, +27% YoY ✓; 61 new clients = 15 ETS + 46 CCR ✓ (L100); fleet ~19-19.5k, daily utilization 10-11k ✓; online booking 14% ✓; ETS 59% / CCR 41% ✓. The only stated-figure exception is the EBITDA-margin "9.3%" (L21, F14-01), reconciling to 10.34% — treated as transcription artifact, flagged. Internal-consistency positive: keeps Role 5 out of grade D.

---

```yaml
stage: A3-forensics
company: "ECOSMOBILITY"
quarter: "Q1FY27"
doctype: "concall"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/ecosmobility-q1fy27/work/forensics_concall_ecosmobility_q1fy27.md"
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
  F10: N.A.
  F11: N.A.
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F6-01", check: "F6", line: "L23", classification: "FORWARD-SIGNAL", implication: "FY27 EBITDA guidance cut to ~10% (from 11-13%/13-15%); ~10% on 15-18% revenue = FY27 EBITDA ~Rs93-95 Cr flat vs FY26 Rs93.9 Cr = third flat/profitless year. Severity RED-FLAG."}
  - {id: "F7-01", check: "F7", line: "L23", classification: "AMBIGUOUS", implication: "Guidance anchor walked down 13-15 -> 11-13 -> 10; pin which band was ever formal (analyst echoes 11-13 at L32)."}
  - {id: "F17-01", check: "F17", line: "L44", classification: "CONFIRMATORY-NEGATIVE", implication: "Analyst (Dness Capital) on-record pushback on changing guidance on one month of data; management acknowledged. External corroboration of a credibility problem."}
  - {id: "F14-01", check: "F14", line: "L21", classification: "AMBIGUOUS", implication: "Stated EBITDA margin 9.3% vs reported 10.34%; likely transcription artifact of '10.3%', flagged either way."}
  - {id: "F1-01", check: "F1", line: "L69", classification: "CONFIRMATORY-NEGATIVE", implication: "ETS-vs-CCR segment margin split REFUSED; conceals which segment drives the mix-led compression. Plus 4 further ZERO_STANDING non-disclosures (L37/L65/L83/L91)."}
  - {id: "F12-01", check: "F12", line: "L61", classification: "FORWARD-SIGNAL", implication: "Gross-margin decline 'more evident in ETS'; price cuts absorbed off vendor margins (L57); ETS mix to 59% (L12) = structural mix-led compression, not one-off."}
  - {id: "F6-02", check: "F6", line: "L75", classification: "FORWARD-SIGNAL", implication: "Operating-leverage inflection deferred to >Rs1,000 Cr revenue (~FY28); no FY27 recovery underwritten."}
  - {id: "F6-03", check: "F6", line: "L16", classification: "FORWARD-SIGNAL", implication: "B2C app + CCR-automation both dated to Q2 FY27 (L16/L45); testable promise-vs-delivery checkpoint next quarter."}
  - {id: "F13-01", check: "F13", line: "L27", classification: "FORWARD-SIGNAL", implication: "Dividend Rs2.38 pending AGM (~21 Sep 2026); Rs150 Cr cash + senior strategic-finance hire + M&A exploration (L39) = capital-deployment optionality AND margin-dilution risk; buyback pushback deflected."}
  - {id: "F7-02", check: "F7", line: "L75", classification: "FORWARD-SIGNAL", implication: "Pre-emptive margin/pricing hedges (L33/L75/L83); 'not sure of longevity' + 'would not comment on moderation' signal Q2 pressure still live."}
  - {id: "F17-02", check: "F17", line: "L92", classification: "AMBIGUOUS", implication: "Oil-price/vendor cost pass-through question dropped (line lost); live margin input unaddressed; A4 to re-ask."}
  - {id: "F17-04", check: "F17", line: "L53", classification: "AMBIGUOUS", implication: "'Right to win' moat defence (relationships/supply/processes) is qualitative narrative, unquantified, against ROCE falling 42.9%->29.4%; numbers side with the no-barrier challenge (L52)."}
forward_signals: ["F6-01", "F12-01", "F6-02", "F6-03", "F7-02", "F13-01"]
ambiguous: ["F7-01", "F14-01", "F17-02", "F17-04"]
commitments:
  - {commitment: "FY27 EBITDA margin ~10% (revised down)", implied_date: "FY27", ref: "L23", status_word: "revised"}
  - {commitment: "FY27 revenue growth 15-18%", implied_date: "FY27", ref: "L49", status_word: "reaffirmed"}
  - {commitment: "FY27 employee cost +~20%", implied_date: "FY27", ref: "L25/L41/L87", status_word: "guidance"}
  - {commitment: "B2C app launch (premium CCR)", implied_date: "Q2 FY27", ref: "L16/L91", status_word: "underway"}
  - {commitment: "CCR automation platform settle & deliver productivity", implied_date: "within Q2 FY27", ref: "L45", status_word: "in-transition"}
  - {commitment: "SIXT India-GSA distribution build-out", implied_date: "ongoing/undated", ref: "L16", status_word: "progressing"}
  - {commitment: "M&A opportunities - better picture", implied_date: "coming quarters", ref: "L39", status_word: "initiated"}
  - {commitment: "Operating-leverage inflection", implied_date: "at >Rs1,000 Cr revenue (~FY28)", ref: "L75", status_word: "deferred"}
  - {commitment: "Final dividend Rs2.38/share FY26", implied_date: "pending AGM ~21 Sep 2026", ref: "L27", status_word: "board-recommended"}
  - {commitment: "Leadership-bandwidth hiring", implied_date: "through FY27", ref: "L16/L87", status_word: "underway"}
  - {commitment: "B2C revenue guidance", implied_date: "from FY28", ref: "L91", status_word: "deferred"}
gate_a3: pass
blank_checks: []
```
