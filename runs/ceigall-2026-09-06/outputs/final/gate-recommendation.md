# CEIGALL — GATE RECOMMENDATION (PHASE 1, EVIDENCE ONLY)

**VERDICT: PROCEED WITH CAVEATS**

Conditional. The verdict above holds under the redflag_coverage reading of the
FLAG RULES gate. Under the strict acceptance_rate reading the verdict is
REWORK. The orchestrator did not rule on which reading governs and this stage
does not either. The operator rules at Halt 1. Section 1 sets out both.

Ceigall India Ltd | CEIGALL | CMP Rs 356.0 | Market cap Rs 6,198 cr
FY26 consolidated revenue Rs 4,022 cr | Order book Rs 18,554 cr at 4.8x book to bill
Listed August 2024 | Road and highway EPC with a HAM concession portfolio
Sector row: EPC / Civil construction | Run: ceigall-2026-09-06

Verdict selection rule applied: rule 3 (FLAG-PROMOTER and FLAG-CASH active),
with the INDETERMINATE cash determination capping the outcome at PROCEED WITH
CAVEATS per the FLAG RULES and CLAUDE.md. Both flag blocks travel inline
below, unchanged by the cap.

PHASE 1 SCOPE. Stages 10 and 11 have not run. This file carries no BUY,
WATCHLIST or AVOID call, no entry range, no margin of safety price, no
destination multiple, no fair value and no Hurdle verdict. None of those
exists yet for this name.

TRANSITION POSTURE. Not assignable in phase 1. The posture needs three state
variables and two are unavailable: the Mental Model Declaration is unsigned,
so the proof gate and the ugliness classification are not set, and the
recognition gap resolves only at stage 11.

---

## 1. THE UNRESOLVED GATE RULE QUESTION

Stated first, before the flags, because it decides whether the rest of this
file is a gate recommendation or a rerun order.

### The rule

FLAG RULES, prompts/00-orchestrator.md Section 4: "If Verifier A finds any
CRITICAL numerical finding, or any verifier's acceptance_rate falls below 60%,
the synthesis verdict is REWORK regardless of company quality."

### The facts, stated fairly

1. No CRITICAL numerical finding survives. Verifier A run 2 emitted one, on
   FY26 standalone operating cash flow. The orchestrator re-read the source
   page and cleared it: the line reads 4,569.46 unbracketed against (2,709.12)
   bracketed for the prior year, and the statement brackets negatives, so the
   figure is positive as stage 3 reported. Logged in
   outputs/final/verifier-disagreement-log.md, disposition FLAG CLEARED.
2. Verifier B's strict acceptance_rate is 47, below the 60 floor. That number
   is 20 caught out of 43 independent flags, following the rubric literally
   with no credit for a partial catch.
3. Verifier B's redflag_coverage is 70. That is 30 of 43, counting caught plus
   partially caught. redflag_coverage is the metric Section 5 of the
   orchestrator names for this verifier when computing the confidence delta.
4. Verifier B states the residual is dominated by a twelve item MINOR tail, of
   which the pipeline carries one. On CRITICAL and MAJOR flags alone, 19 of 31
   are caught and 28 of 31 are surfaced, which is 90 percent.
5. Both Verifier B passes report `pipeline_flags_not_supported` as empty.
   Nothing the pipeline claimed was unsupported. The failure was coverage, not
   fabrication.
6. The coverage failure was diagnosed and remediated. Stage 5 ran three times
   and stage 6 ran twice. Coverage moved from 48 percent against the
   pre remediation artifacts to 70 percent against the remediated ones.
   Verifier B was not run a third time because its own independent flag list
   grew from 33 to 43 between passes, so a third pass would measure a moving
   denominator rather than the pipeline's improvement.

### Reading A: the acceptance_rate floor binds literally

Verdict under this reading: **REWORK**.

REWORK judges the analysis, not the company. The failing stage is stage 5,
concall red flag extraction, measured at 47 percent strict catch rate on
verifier B's independent list. A rerun under this reading must: close the
twelve item MINOR tail verifier B named, re-audit against a frozen flag list
so the denominator stops moving, and re-measure both acceptance_rate and
redflag_coverage on the same artifacts.

My recommended verdict under Reading A: REWORK, and I would scope the rerun to
verifier B alone with a frozen denominator, not to stage 5 again. Stage 5 has
already run three times against a growing list.

### Reading B: redflag_coverage is the governing metric for verifier B

Verdict under this reading: **PROCEED WITH CAVEATS**, per rule 3 with the
INDETERMINATE cash cap.

Under this reading the rule's purpose decides its scope. The rule exists to
stop an analysis that cannot be trusted from reaching a verdict. Nothing this
pipeline asserted was unsupported, on either verifier B pass. 90 percent of
the thesis weight flags are surfaced. Section 5 of the orchestrator names
redflag_coverage, not acceptance_rate, as this verifier's contribution to the
confidence delta, and that figure is 70, above the floor.

My recommended verdict under Reading B: PROCEED WITH CAVEATS, with both flag
blocks inline and the cash determination unresolved.

### What is not in dispute either way

The remediation record, the empty unsupported flag list, and the twelve item
MINOR residual are facts under both readings. The disagreement is only about
which of verifier B's two published rates the FLAG RULES sentence points at.
The operator rules. This stage does not.

---

## 2. ACTIVE FLAG BLOCKS

### FLAG-PROMOTER

```
FLAG-PROMOTER
Verdict:            CONCERN
Scorecard:          clean 2 | caution 6 | red 2
Deal-breakers:      NONE

Top finding 1:
  Independent Director Gurpreet Kaur holds a filing verified directorship at
  C&C Constructions Ltd, the outside company that is beneficiary of Ceigall's
  static, unexplained Rs 500m related party loan, unchanged for two years and
  accruing interest. Multiple web aggregators additionally list her as a
  C&C Constructions promoter category holder.
  Evidence tier: VERIFIED (directorship) / UNVERIFIED (promoter classification)
  Evidence: Annual_Report_2026.pdf sheet 48 (Corporate Governance directorship
  table); Note 49 RPT (via B02); WebSearch aggregator results, 2026-09-06.
  Appointment date 14-Feb-2025.

Top finding 2:
  Nine distinct KMP or Board level changes in about 17 months at a company
  under two years post IPO, including three CEO level transitions: Narula out
  Mar-2025, Hoshing in Sep-2025 and out Jul-2026, Saravanan in as CEO Feb-2026
  and elevated to WTD Jul-2026. Plus one CFO, two VP and one GM departure
  between Jun and Aug 2025.
  Evidence tier: VERIFIED
  Evidence: Annual_Report_2026.pdf sheets 35, 46, 51 (B08). The nine event
  table required cross referencing three separate AR sections that do not
  individually list all nine.

Further adverse findings carried:
  - Two former Ceigall senior KMPs (VP Procurement Avneet Luthra, VP HR Simran
    Sehgal, both resigned effective 30-Jun-2025) subsequently appear on C&C
    Constructions' board or promoter list. Evidence tier: MEDIA REPORTED, two
    independent sources (B08).
  - CMD FY26 remuneration Rs 125.52m at a disclosed 6,276x ratio to median
    employee remuneration, plus a 1 percent of net profit commission
    entitlement. Anchor Annual_Report_2026.pdf sheet 84 (Annexure-3).
    RESOLUTION-LIMITED and UNCONFIRMED: see Section 6. Not to be quoted
    downstream as verified. The CONCERN verdict does not rest on this item.
  - DGGI GST search action 14-May-2025, wrongful ITC availment on IPO related
    expenses, reversed as inadvertent. Quantum NOT FOUND (B08, AR sheet 46).
  - Rs 89.65m procurement fraud, 3 vendors and 6 employees, FIR lodged by the
    Company 22-Jan-2026, qualified IFC opinion at both levels, amount stated
    fully recovered (B08, AR sheets 68 and 46; B12a Target 5 verified amount
    and FIR date exactly).
  - Promoter pledge percentage NOT FOUND. Shareholding filing absent from the
    corpus and no Ceigall specific pledge figure surfaced on web search. This
    is an unconfirmed gap, not a verified zero (B08).

TRANSITION EVIDENCE (found, and it is real):
  1. New outside hire CEO A. Saravanan, career infrastructure executive with
     cited MoRTH and NHAI project execution recognition, elevated to WTD and
     CEO for a defined two year term effective 01-Jul-2026 (AR sheet 24).
  2. Dr. Pawan Kumar appointed WTD 01-Jul-2026, domain credentialed in highway
     sector research and materials, a non family appointment (AR sheet 24).
  3. Secretarial auditor Lal Ghai & Associates affirmatively disclosed both the
     DGGI search action and the fraud and FIR in a dedicated exception annexure
     rather than filing a silent clean report (AR sheet 46). Genuine governance
     communication candour.
  4. Reputable outside internal auditor Grant Thornton Bharat LLP, not a
     captive in house function (AR sheet 25).
  5. Audit Committee and NRC Chairman Arun Goyal reappointed for a second
     consecutive five year term from 01-Mar-2026, giving institutional
     continuity through the executive churn.

Verdict basis: compromised independence of an ID sitting directly on top of an
unexplained static Rs 500m related party loan, combined with nine KMP or Board
changes in seventeen months at a company barely two years past IPO. No
personal SEBI or criminal exposure to the promoter was found, which keeps this
at CONCERN rather than AVOID.

Stage status: B08 status is PARTIAL. Five WebFetch attempts at primary or near
primary sources were EGRESS_BLOCKED by container network policy (RHP PDF,
Ceigall's own NHAI termination letter, two shareholding aggregators, one
governance news site). Web evidence rests on WebSearch snippets. The
Kaur as C&C promoter claim is the single highest priority live verification
item for claude.ai.

Group company map provenance: WEB-DERIVED, NOT FILING-ANCHORED. The IPO
prospectus is absent, so every group company relationship carries that
provenance.
```

### FLAG-CASH

```
FLAG-CASH
DETERMINATION:      INDETERMINATE
Consequence:        verdict capped at PROCEED WITH CAVEATS. Missing evidence
                    named below, per CLAUDE.md.
Rating agency verbatim quote: NOT AVAILABLE. inputs/rating/ is empty. No
                    rating rationale exists in this corpus. The investor
                    presentation cites a grade only (IND AA-/Stable, B04).
                    This is the document that normally settles the
                    determination and it is the one that is missing.

EVIDENCE FOR GROWTH-INDUCED:
  - Consolidated CFO burn improved 82 percent year on year: Rs -5,155.57m FY25
    to Rs -912.83m FY26 (B03; consolidated figure verified exactly by B12a
    Target 10).
  - Standalone parent CFO turned positive at Rs 4,569.40m in FY26 against
    Rs (2,709.12)m in FY25, while investing activities show Rs 3,136.75m of
    fresh loans flowing from parent into SPVs (B03; the standalone line
    re-verified by the orchestrator at Annual_Report_2026.pdf sheet 80,
    reading 4,569.46 unbracketed). The contractor generates cash and the
    concessions consume it. That is a mechanism, not a symptom.
  - RUSCA (Receivable Under Service Concession Arrangements) is a concession
    financial asset amortising over 15 to 20 years, not trade credit; its
    +40.5 percent growth to Rs 14,578.90m is a build phase artefact and should
    not be read on a debtor turnover basis (B04 irrelevant_ratios; figure
    verified exactly by B12a Target 2 at Rs 14,578.91m, growth 40.47 percent).
  - capex_embedded_growth_pct is 0 and equipment is rented, so the capital is
    going into concessions rather than plant (B07, B09).
  - Consolidated ROCE 31.98 to 19.22 percent and ROE 33.57 to 14.39 percent
    FY24 to FY26 are described as largely a mechanical artefact of capital
    locked in pre COD SPVs, not necessarily a quality collapse (B04).
  - Peers are in the same build: all three are simultaneously entering solar,
    BESS, transmission, metro, mining or water in the same period (B06
    industry_cross_read).

EVIDENCE FOR STRUCTURAL:
  - Cumulative CFO against cumulative PAT is -0.70x over FY21 to FY26, with
    CFO negative in five of six years while PAT rose from Rs 112.5cr FY21 to
    Rs 311.89cr FY26 (B01 Block B, 0 of 20, deal-breaker rules 2 and 4).
  - Contract Assets, which are EPC revenue booked ahead of billing and not a
    HAM concession asset, rose 61.8 percent from Rs 8,733.43m FY25 to
    Rs 14,132.39m FY26 with nil impairment, faster than the 17.1 percent
    consolidated revenue growth (B12a Target 1 verified source truth; B02
    rank 1). Contract Assets plus RUSCA equal about 71.4 percent of FY26
    revenue with nil impairment, the auditors' own top Key Audit Matter (B02).
  - Trade receivables ageing MIX deteriorated: over six months share of gross
    receivables rose from about 9.4 percent FY25 to about 28 percent FY26,
    even as the absolute balance fell 18.8 percent (B02 Note 12; B12a Target 9
    verified).
  - Payable days rose 79 to 138 and WIP days 37 to 98; net working capital
    days fell to 49 only because payables were stretched (B04; B05 peer
    question 6).
  - Rs 2,952.13m of trade payables are economically reverse factoring or SCF
    liabilities whose discounting cost the Company bears, not disclosed inside
    Borrowings (B02 rank 5, Note 27/28 and Note 58). RESOLUTION-LIMITED and
    UNCONFIRMED: see Section 6.
  - MSME payables more than doubled from Rs 409.93m to Rs 1,039.51m (verified
    exactly, B12a Target 8a); unpaid statutory interest to small suppliers rose
    212 percent from Rs 5.20m to Rs 16.22m (B02 Note 73/28). The interest
    sub figure is RESOLUTION-LIMITED and UNCONFIRMED: see Section 6.
  - Management deflected the working capital days target question in two calls
    (Nov-2025, Aug-2026), giving qualitative language and never a number (B05
    repeated_evasions).
  - IPO proceeds are 100 percent utilised and royalty income has ceased,
    disclosed as an aside in the Aug-2026 call, one quarter before an Rs 859cr
    FY27 equity commitment against which Rs 23cr was infused in Q1 FY27, a
    2.7 percent run rate (B05 FLAG-FUNDING-CAPACITY).
  - Management asserts "cash flow will not be a challenge" and "equity is not
    a problem" (May-2026 call), never reconciled against the negative
    consolidated CFO by management or by any analyst across four calls (B05
    FLAG-CASHFLOW-NARRATIVE). All three peers instead name the specific driver
    of every debt and working capital movement; no peer uses a blanket
    reassurance framing (B06 contradicted).

WHY INDETERMINATE AND NOT ONE OR THE OTHER:
  Both mechanisms are evidenced and neither dominates the record. The HAM SPV
  funding is real, documented at the primary statement level, and improving.
  The EPC side working capital stretch is also real, is growing faster than
  revenue, and is not explained by the HAM build. The corpus contains no split
  of consolidated operating cash flow between HAM SPV construction outflow and
  EPC working capital movement, and no segment level cash flow. Without that
  split, and without the rating rationale, the determination cannot be made on
  filed evidence. It is not made here.

MISSING EVIDENCE THAT WOULD SETTLE IT, named per CLAUDE.md:
  1. The rating rationale carrying the agency's own working capital
     commentary. Where to obtain: India Ratings (IND AA-/Stable is cited in
     the investor presentation) published rationale, or the agency website.
     HIGH priority.
  2. A split of consolidated operating cash flow between HAM SPV construction
     outflow and EPC working capital movement, or SPV level cash flows. Where
     to obtain: subsidiary financial statements filed with the AR, AOC-1
     detail, or a direct management question.
  3. The FY25 annual report, to anchor the Contract Assets FY24 baseline of
     Rs 4,039m. Where to obtain: BSE or NSE filings, or the company website.
  4. The receivables ageing schedule and the reverse factoring quantum inside
     trade payables at readable resolution. Where to obtain: a higher
     resolution render of Note 27/28, or live verification.
  5. A management stated working capital days target, deflected twice on
     calls. Where to obtain: the next quarterly call.

RESOLVING METRIC. The single quarterly print that moves this determination in
either direction: H1 FY27 consolidated operating cash flow read alongside
Contract Assets plus RUSCA as a share of trailing twelve month revenue. If
consolidated CFO turns positive or the burn narrows again while the ratio
holds at or below 71 percent, the determination resolves GROWTH-INDUCED. If
consolidated CFO prints more negative than the FY26 full year Rs -912.83m
while the ratio rises past 71 percent, it resolves STRUCTURAL. Source: the H1
FY27 results filing cash flow statement and the balance sheet notes.
```

### FLAG-GATE0

```
FLAG-GATE0
Classification:     AVOID
Grand total:        45 / 160
Core score:         37 / 100
Moat score:         8 / 60  (MODERATE, 2 of 12 moats confirmed)
Blocks:             A 14/20 | B 0/20 | C 15/20 | D 8/20 | E 0/20
Data:               6 years, FY2021 to FY2026, screener Data_Sheet

Deal-breakers fired (2):
  - Rule 2: Block B (0) < 8, caps classification at max GOOD.
  - Rule 4: Cumulative CFO/PAT (-0.70x) < 0.50, caps classification at max
    AVERAGE.

Depressor detail:
  - Block B 0/20 is the dominant evidenced depressor. CFO negative in five of
    six years FY22 to FY26 through a debt and equity funded HAM build, while
    PAT rose Rs 112.5cr to Rs 311.89cr. This is a real cash conversion gap,
    not a data artefact (B01).
  - Block E 0/20 is an EVIDENCE GAP, not a scored quality finding. No
    shareholding corpus was provided. It must not be read as a governance red
    flag on its own and should be re-scored when the filing lands (B01).
  - Block F moat score 8/60 is depressed partly by five of twelve tests (M2,
    M5, M7, M9 plus one) scoring 0 for PEER DATA NEEDED rather than confirmed
    absence of moat. M6 and M8 score 0 as not applicable to an EPC road
    contractor (B01).
  - FCF (B2, B3), Payable Days (B4, M12) and Current Ratio (D4) scored N/A at
    0: the screener sheet carries no PPE purchase line and lumps payables
    inside an undifferentiated Other Liabilities line. Not estimated, per the
    never estimate rule (B01).
  - FY21 ROCE of 47.10 percent sits on a pre scale, pre IPO capital base
    (982,100 shares, net worth Rs 305cr) before the FY22 split, FY24 bonus and
    Aug-2024 IPO. It drives A4 to 0 mechanically and is flagged as not
    comparable rather than softened (B01).
  - Blocks A (14/20) and C (15/20) independently show a growth and returns
    profile that the AVOID classification does not reflect, because the
    classification rests on Core below 40 driven almost entirely by B and E.

Verifier C re-derived all 51 Gate 0 rules from source data with zero fails.
One ADVISORY: the M3 rule does not name the ROCE basis; the stage used FY26
(16.76 percent) and scored 3, and median ROCE (22.72 percent) would score 5,
lifting Block F to 10/60 and the grand total to 47/160. Core score, moat
class, moats confirmed and the AVOID classification are unchanged either way
(B12c).
```

### Other active flags, carried

Not full blocks. Each is live, each is anchored, none is a verdict rule
trigger on its own.

| Flag | Stage | One line |
|---|---|---|
| FLAG-CONCALL-SILENCE | B05 | Four calls of silence on the fraud, the qualified IFC opinion at both levels, the NHAI SPV termination, the sister SPV auditor resignation, the leadership churn, and contingent liabilities at 83.7 percent of net worth. No analyst asked any of them. |
| FLAG-DISCLOSURE-DECAY | B05 | Consolidated debt disclosure went full breakdown to aggregate to ratio to none; consolidated EBITDA and PAT disclosure went given to dropped. Both reached zero in the Aug-2026 call. |
| FLAG-CASHFLOW-NARRATIVE | B05 | "Cash flow will not be a challenge" asserted against negative consolidated CFO in FY25 and FY26, never reconciled. Cash and FDR separately overstated about 71 percent via a written erratum (Rs 171cr against Rs 241cr). Liquidity disclosed on three non comparable bases in three quarters. |
| FLAG-RECONCILIATION | B05 | Order book roll forward does not close in any of three testable quarters on either a consolidated or a standalone revenue basis. Renewable inflow against closing renewable book leaves an Rs 443cr gap. Aug-2026 per project HAM equity list sums to Rs 567cr against a stated Rs 550cr, and the same call states both 10 and 11 HAM projects. |
| FLAG-REPEATED-EVASION | B05 | Mahesh Patil (ICICI Securities) asked in May-2026 and Aug-2026 whether the margin beat was a one off. Answered both times with an unrelated list of newly started projects, never yes or no. Bears on whether FY26 and Q1 FY27 margin is a sustainable base. |
| FLAG-FUNDING-CAPACITY | B05 | IPO proceeds 100 percent utilised and royalty income ceased, disclosed as an aside, one quarter before an Rs 859cr FY27 equity plan, in the same call consolidated disclosure went dark. |
| FLAG-MISSTATEMENT | B05 | Feb-2026 claim "we were always guiding 10% to 15%, our growth is much more than that" is false against the same call's 9M FY26 growth of 7.6 percent standalone and 8.7 percent consolidated. |
| FLAG-PEER-CONTRADICTION x5 | B06 | Five separate peer contradictions. Listed in Section 4. |
| FLAG-PEER-RESOLVES-GAP | B06 | All three peers name the West Asia conflict as the crude, bitumen and logistics cost driver in this exact window, which very likely resolves Ceigall's unnamed "war situation". |
| FLAG-EMOAT-SPARSE | B07 | Adjusted emerging moat score 4.3/92, below even the 12 to 24 MODEST band. Four of 22 categories carry any weight, all WEAK. R&D and technology absorption are explicit NIL across FY25 and FY26. Genuinely sparse, not under searched. |
| FLAG-EMOAT-NETTED | B07 | The documented specialised structure delivery record nets against the C credibility grade and named timeline slippages. Net WEAK. |
| FLAG-HYBRID-VALUATION | B04 | Two archetypes in one set of accounts with opposite cash and working capital profiles. The AR segment split (EPC 57.86, HAM 41.68, O&M 0.46 percent) does not disclose how much of HAM is construction phase versus post COD annuity. Material to method choice at stage 11. |
| FLAG-PRERISK-RENEWABLES | B04 | Renewable and T&D verticals show 0.0 percent completion on every order book line at 30-Jun-2026 despite Rs 39,365m and Rs 4,068m of cumulative LOA and PPA value. Not a revenue stream; must not be modelled as one. |
| FLAG-TAM-SCOPE-NARROW | B09 | Conservative TAM of Rs 1.22 lakh cr is scoped to the NHAI Roads and Bridges budget line only. State highway, metro rail and tunnel capex Ceigall also bids into is NOT FOUND as a consolidated figure and is excluded, so TAM is understated. |
| FLAG-SOM-CAGR-SHORTFALL | B09 | SOM implied revenue CAGR of about 10 percent at year 3 and year 5 sits below management's own minimum 15 percent FY27 guide. |
| FLAG-AWARD-SLOWDOWN | B09 | FY26 NHAI new awards fell about 22 percent to about 3,100 km in the same year Ceigall's inflow beat its Rs 5,000cr guide by more than 2x at Rs 11,332cr. The divergence is unexplained by Ceigall. |
| FLAG-CAPACITY-FINANCING | B09 | SOM is not physically capex constrained because equipment is rented. Financing capacity, working capital and bonding, is the binding constraint on scaling to the SOM path. |
| FLAG-CITATION-CORRECTION | B06 | Eighteen quote anchors corrected across two passes. Root cause: transcripts carry a printed "Page N of M" header running one page behind the PDF marker. Substance correct in every case. |

---

## 3. CONFIDENCE DELTA (PHASE 1)

| Component | Value | Source | Basis |
|---|---|---|---|
| numerical_acceptance | 75 | B12a run 2 | 12 deliberately hardest AR figures audited, not a representative sample; 9 verified clean or substantially clean after the orchestrator source re-check. B12a run 1 audited 48 numbers broadly at 97.9 percent with zero CRITICAL and zero MAJOR. The conservative targeted figure is used. |
| redflag_coverage | 70 | B12b run 2 | (20 caught + 10 partially caught) / 43 independent flags, measured against the remediated B05 run 2 and B06 run 2. First audit measured 48 percent against the superseded artifacts. On CRITICAL and MAJOR alone, 90 percent surfaced. |
| framework_adherence | 95 | B12c | 81 of 85 rules passed. Gate 0 51/51, Emerging Moat 30/34. Zero CRITICAL, zero MAJOR. Valuation adherence NOT included, pending phase 3. |
| peer_utilisation | 100 | B12d | 3 of 3 peers substantive on audit, 12 of 12 transcripts used, stage's own count agreed. |
| **overall** | **70** | minimum of the four | Band 60 to 74. |

**Band effect.** Overall 70 sits in the 60 to 74 band, so a PROCEED verdict
downgrades one level to PROCEED WITH CAVEATS. This run does not reach PROCEED
on its own rules, so the band effect is not the binding constraint here. The
INDETERMINATE cash cap and the active flags are.

**The weakest component.** redflag_coverage at 70 is the binding number, and
it measures how much of the concall red flag surface the pipeline reached, not
company quality. framework_adherence at 95 and peer_utilisation at 100 both
sit high. numerical_acceptance at 75 is a conservative reading of a
deliberately adversarial targeted pass; the broad pass read 97.9 percent.

---

## 4. CONTRADICTED CLAIMS (PEER STAGE)

Each is a priority monitoring item. Each was tested against three peers over
12 transcripts.

| Claim tested | Ruling | Contradicting peers | Anchor |
|---|---|---|---|
| Ceigall's "cash flow is not a problem" / "amazing" narrative despite negative CFO is sector wide tone | CONTRADICTED | HGINFRA, KNRCON. No peer uses blanket reassurance; all name the specific driver of each debt and working capital move | HGINFRA-Concall_May_2026_Transcript.txt, p.5 |
| Non disclosure of the Malout-Abohar-Sadhuwali HAM sale price is industry standard opacity | CONTRADICTED | HGINFRA, PNCINFRA both disclose hard enterprise value or consideration on completed monetisations | HGINFRA-Concall_Aug_2025_Transcript.txt, p.5-6; PNCINFRA-Concall_Nov_2025_Transcript.txt, p.10 |
| Folding bonus and royalty income into headline EBITDA margin without separate disclosure is standard sector practice | CONTRADICTED | PNCINFRA, KNRCON, HGINFRA all name, quantify and attribute one off items to specific projects and quarters | PNCINFRA-Concall_May_2026_Transcript.txt, p.15 |
| Peer managements only address fraud, IFC qualifications, auditor resignations or leadership churn when compelled by a filing, so Ceigall's silence is sector standard | CONTRADICTED (re-ruled from UNVERIFIABLE in run 1) | HGINFRA discloses a live CBI and Anti-Corruption Bureau search, an 87 percent order inflow guidance miss and a lender loan recall unprompted; KNRCON discloses an NHAI show cause with a one month bidding suspension against subsidiary and parent unprompted; PNCINFRA confirms a comparable matter candidly when asked | HGINFRA-Concall_Feb_2026_Transcript.txt, p.6; KNRCON-Concall_Aug_2025_Transcript.txt, p.4 |
| Escalation cost is fully compensated by the authority (Ceigall, May-2026) | CONTRADICTED | PNCINFRA calls it "some relief... to certain extent", time boxed to three months; KNRCON frames it as a faster pass through cycle, not a guarantee; HGINFRA's own Q4 FY26 margin fell to 9.37 percent on unrecovered escalation in the identical quarter | PNCINFRA-Concall_May_2026_Transcript.txt, p.6 and p.21; HGINFRA-Concall_May_2026_Transcript.txt, p.6 |

Partially verified, carried but not contradicted: Ceigall's NHAI award pace
deflection as sector reticence; the unreconciled shifting HAM, renewable and
T&D equity totals; the working capital stretch as sector wide; the four call
refusal to split segment margins. One clean VERIFIED finding runs the other
way and against Ceigall: all three peers routinely give unbilled revenue,
retention, mobilisation advance and named debtor splits in rupees when asked,
and Ceigall gave one such figure across four calls.

---

## 5. CROSS BLOCK INCONSISTENCIES RECONCILED

**Call count and leadership churn count.** B07 top_moat_risks says
"three calls" of management silence and "5 KMP/Board changes in ~14 months".
Both figures are superseded. B05 run 3 established FOUR calls of silence across
Nov-2025, Feb-2026, May-2026 and Aug-2026. B08 established NINE KMP or Board
level changes over about 17 months, Mar-2025 to Jul-2026, from cross
referencing three separate AR sections that do not individually list all nine.
B07 was written before both runs and was not re-run. **The later figures
govern: four calls, nine changes in about 17 months.** B06 carries the same
defect, describing the silence as "3-call" in five places against a four call
B05, flagged MINOR by verifier B. Every use in this file and in the narrative
uses four and nine.

**Which step down SPV carries the CARO flags. OPEN ITEM, not resolved.** B02
Pass 2 read row 5 of the CARO exception table at sheet 105 and identified
Ceigall Ludhiana Bathinda Greenfield Highway Pvt Ltd as carrying both the cash
losses marker and the statutory auditor resignation marker. B03's own full
clarity re render of the same sheet placed both markers on row 4, Ceigall
Ludhiana Rupnagar Greenfield Highway Pvt Ltd, which is also the entity whose
NHAI concession was terminated per Note 35, with row 5 showing no footnote
marker on that reading. Neither pass resolved it, and B03 logged it as an open
cross pass discrepancy on the grounds that a table this dense at scan
resolution cannot be called with confidence from either pass alone. **Neither
figure governs. It is carried open.** The answer decides whether this is ONE
troubled project company, where the termination, the auditor resignation and
the cash losses all sit on Rupnagar, or TWO separate troubled project
companies. Resolve at Halt 1 by a higher resolution render of sheet 105 or by
live verification of the CARO table.

---

## 6. FIGURES THAT MAY NOT BE QUOTED DOWNSTREAM AS VERIFIED

Three RESOLUTION-LIMITED figures from B12a run 2. Each was self described by
the verifier as unlocatable or unreadable at rendered resolution, which the
verifier's own brief defines as RESOLUTION-LIMITED rather than a mismatch.
Each is UNCONFIRMED, not contradicted. None is cleared. All three go to Halt 1
for live verification.

| Figure | Claimed | Anchor | Status |
|---|---|---|---|
| Reverse factoring quantum inside trade payables | Rs 2,952.13m | Note 27/28, sheets 119-120 | UNCONFIRMED. Table anchor present, specific figure unlocatable at resolution. |
| MSME unpaid statutory interest | Rs 5.20m to Rs 16.22m, +212 percent | Note 27, sheets 119-120 | UNCONFIRMED. Interest detail unlocatable at resolution. The MSME payables figures either side of it, Rs 409.93m to Rs 1,039.51m, WERE verified exactly, so the scale finding stands. |
| CMD FY26 remuneration ratio | Rs 125.52m at 6,276x median employee | Annexure-3, sheets 44-45 | UNCONFIRMED. Table present, values unreadable at rendered resolution. |

One live source fidelity flag stands, and it is the only one:

| Figure | Verifier A finding | Disposition |
|---|---|---|
| Contract Assets FY24 baseline Rs 4,039m, supporting the "tripled in two years" framing | MAJOR, source_fidelity true. FY26 reads Rs 14,132.39m and FY25 reads Rs 8,733.43m; FY24 is not shown in the note | GATE HELD, corrected at source. The FY26 figure and the nil impairment are verified. The FY24 comparator is not in the FY26 note and is unanchored in this corpus. **The verified statement downstream must use is: Contract Assets rose 61.8 percent from Rs 8,733.43m at FY25 to Rs 14,132.39m at FY26.** The tripling framing may not be repeated until the FY25 annual report is obtained. The finding survives; its framing narrows. |

---

## 7. CORPUS GAPS FOR THE OPERATOR

Corpus verdict: **CORPUS GAPPED**. Freshness verdict: **FRESHNESS PAIRS OK**,
all four pairs PASS, so the freshness cap does NOT apply to this run.

| Gap | Priority | Why it matters | Where to obtain |
|---|---|---|---|
| Prospectus / RHP | HIGH | Company listed August 2024, inside the recently listed window. Promoter and group company history, the group company map and restated pre IPO financials are unavailable. The B08 group company map is WEB-DERIVED, not filing anchored, because of this gap. | SEBI or exchange filing archive, or the lead manager's site. Note the ICICI Securities hosted RHP fetch was EGRESS_BLOCKED in container. |
| Rating rationale | HIGH | Bears directly on FLAG-CASH. It is the document that normally separates STRUCTURAL from GROWTH-INDUCED cash conversion and carries the agency's own working capital commentary. Its absence is the reason the determination is INDETERMINATE. | India Ratings published rationale (IND AA-/Stable is cited in the investor presentation only, with no rationale document in the corpus). |
| Shareholding pattern | MEDIUM in the input record, HIGH in effect | Drove Gate 0 Block E to 0 of 20 as a pure evidence gap. FII and DII holdings unresolved, so the institutional absence qualifier for the UA multiplier cannot be affirmed. Promoter pledge percentage is NOT FOUND, an unconfirmed gap and not a verified zero. | BSE or NSE quarterly shareholding pattern filing. |
| Results filings | MEDIUM | inputs/results/ is empty. Gate 0 ran from the screener Data_Sheet alone, with no quarterly or annual filing PDF anchoring latest period figures. Also blocks the H1 FY27 cash flow read that resolves FLAG-CASH. | BSE or NSE quarterly and annual results filings. |
| Substantive announcements | MEDIUM | Only filing held is a routine Reg 30 AGM dispatch letter. No order wins, acquisitions, capital raises or divestments. The documented ACTION record was unavailable to stages 5, 7 and 8. | BSE or NSE corporate announcements. |
| Third party research | LOW | Never anchored evidence. Lead generation and management intent cross check lost only. No named competitors could be sourced from the provided documents. | Broker research portals. |

Corpus defects that shaped the run, not gaps: the annual report is scanned
with no text layer on 150 of 151 pages, so every AR figure was read off a
rendered page and cited by PDF sheet, and OCR was attempted and rejected. Four
of five screener CSVs are header only, a known collector defect; Data_Sheet is
populated and Gate 0 used it. The manifest sector cap row was hand set to
"EPC / Civil construction" after the auto picker chose "Cables / Industrial
products", and needs confirming at phase 3.

Spear gate: satisfied by operator OVERRIDE dated 2026-09-06, not by a spear
pass. No load bearing facts were named, so this run had no
spear derived verification priority to check first. No prior run and no
company memory exist for this name.

---

## 8. MONITORABLES AND TRIGGERS

Eight items, deduplicated from the stage records.

1. Watch consolidated operating cash flow at H1 FY27 and again at FY27 full
   year. FY26 was minus Rs 91 crore against minus Rs 516 crore in FY25. Read
   it in the cash flow statement of the results filing. This is the single
   item that resolves FLAG-CASH between a build phase and a collection
   problem.
2. Watch Contract Assets plus RUSCA as a share of trailing twelve month
   revenue. It sits at about 71 percent. Read it from notes 11 and 7 of the
   next annual report or the equivalent results schedule. A further rise says
   revenue keeps outrunning billing.
3. Watch for any first impairment or expected credit loss provision against
   Contract Assets or RUSCA. Any non nil number is the signal. Read it in the
   provisioning notes. It would confirm the auditors' own top Key Audit Matter
   turning into a loss.
4. Watch standalone revenue growth against the reaffirmed minimum 15 percent
   FY27 guide. Q1 FY27 printed 10.2 percent, and only the 15.7 percent
   consolidated figure was volunteered. Read it in the quarterly results and
   the call. It tests guidance credibility directly.
5. Watch EBITDA margin against the guided 11 to 12.5 percent band, on a like
   for like basis excluding bonus and royalty income. Two consecutive quarters
   below 11 percent kills the margin trigger. It tests whether the FY26 beat
   was a one off, the question management declined twice.
6. Watch for a disclosed sale consideration and realised equity IRR on the
   next HAM divestment, Bathinda-Dabwali or Jalbehra-Shahbad. Both already
   slipped past the September 2026 target and went silent in the August 2026
   call. Read it in an exchange filing or the call. It tests whether capital
   recycling is repeatable or a single event.
7. Watch HAM and solar equity actually infused against the Rs 859 crore FY27
   commitment. Rs 23 crore went in during Q1 FY27, a 2.7 percent run rate.
   Read it in the quarterly call. It tests funding capacity now that IPO
   proceeds are fully used and royalty income has stopped.
8. Watch whether consolidated debt and consolidated EBITDA figures return to
   the call. Both went to zero disclosure in the August 2026 call. Two
   consecutive quarters of restored disclosure confirms; a third dark quarter
   kills the credibility grade toward D.

---

## 9. FALSIFICATION LINE

The single next quarter print that would do the most damage: **H1 FY27
consolidated operating cash flow prints more negative than the FY26 full year
figure of minus Rs 91 crore, while Contract Assets plus RUSCA rise above 71
percent of trailing twelve month revenue.** That combination removes the
growth induced reading of the cash gap, because the burn would be widening in
a year where HAM equity infusion is running at 2.7 percent of its own
commitment, and it would put the EPC working capital stretch, not the
concession build, at the centre of the negative cash flow.

---

## 10. PUBLISH CHECK

No publish candidate this analysis.
