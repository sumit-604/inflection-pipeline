# MERGED QUARTERLY REVIEW — DGML (Deccan Gold Mines Ltd), Q1 FY27

**Agent:** A4 ANALYST | **Model:** claude-opus-4-8
**Doctype in scope:** CONCALL ONLY (Q1 FY27, June-2026 quarter IR call)
**Protocols run:** Role 5 (Quarterly Concall Analysis Protocol v1.1) in full. Role 4 (Quarterly Results Review Protocol v1.2) is **N.A.** for this run — see preamble.
**Coverage status:** FIRST COVERAGE / BASELINE. No Notion page, no `companies/DGML.md`, no prior Decision Status, no entry zone, no active tripwires, no prior-quarter extract, no prior concall log. Everything defined here becomes next quarter's checklist.

Sources:
- A1 extract: `/home/user/inflection-pipeline/runs/deccangold-q1fy27/work/extract_concall_dgml_q1fy27.txt`
- A2 ledger: `/home/user/inflection-pipeline/runs/deccangold-q1fy27/work/ledger_concall_dgml_q1fy27.md`
- A3 forensics: `/home/user/inflection-pipeline/runs/deccangold-q1fy27/work/forensics_dgml_q1fy27.md`

---

## 0. LEDGER-RECONCILIATION PREAMBLE (CONTRACTUAL, BEFORE STEP 1)

**Ledger contains 95 numbered claims (notes) / 15 questioner turns / 21 distinct questions / 4 management response blocks / 12 prepared-remarks topic blocks. There are 0 slides (concall, no deck supplied). ALL reviewed at their cited line numbers.**

- 95 quantitative claims (Ledger Table 6, N1–N95 plus the truncation-note residue): all reviewed.
- 15 questioner turns (Ledger Table 3, T1–T15): all reviewed; T2 and T8 (Jacob Matthew, same individual) produced no content (connectivity), flagged `NO_RESPONSE`.
- 21 distinct questions/requests (Ledger Table 4, Q1–Q21): all reviewed; Q17 is a `REQUEST_NOT_QUERY` (physical AGM).
- 4 management response blocks (Ledger Table 5, RB1–RB4): all reviewed.

**Findings incorporated (A3 IDs):** F1-a, F1-b, F6, F7, F10, F13, F14, F16-a, F16-b, F16-c, F17. (A3 checklist: 8 FINDING, 9 N.A., 0 blank; GATE A3 PASS.)

**No ledger row is unreviewed. Proceeding.**

**ROLE 4 (RESULTS-FILING REVIEW) — N.A. STATEMENT.** This is a concall-only run. No Reg 33 results filing and no investor presentation were supplied. Role 4's numerical-baseline artifacts — the extraction tables from an audited/limited-reviewed filing, the YoY/QoQ walks, the PAT bridge off filed numbers, the standalone-vs-consolidated statement decomposition (A3 F2), the auditor Other-Matters / EoM read (F5), tax and OCI forensics (F8/F9), segment tables (F12), and the reserves tie-out (F11) — cannot be produced and are **N.A.**, not fabricated. Where the concall states verbal financials, they are carried below as **MANAGEMENT-ASSERTED, UNAUDITED, CONCALL-SOURCED** numbers and labelled so at every use. The four Geomysore/Junagiri figures that anchor the quarter — Rs87cr revenue, Rs25cr PAT, Rs6.35cr DGML profit share, 59 kg gold sold (L56, L115) — plus the Rs522mn / Rs520mn inventory figures (L399, L481) and the Rs137cr raise (L60) are all in this asserted-unaudited class. None has been reconciled to a filing because no filing exists in this run.

---

## ROLE 5 — CONCALL ANALYSIS (Q1 FY27)

### STEP 0 — PRE-FLIGHT

**0A. Notion / prior log.** None. First concall under the protocol. Promise-vs-Delivery tracking STARTS this quarter (baseline). No prior triggers, thesis-broken conditions, Promoter Verdict, or Management Grade to load.

**0B. Participants (Ledger Table 1).**

| Role | Name (canonical; ASR variant) | Notes | Line |
|---|---|---|---|
| Managing Director (promoter-side, sole spokesperson) | Dr Hanumantha Rao Modali ("Madali"/"Modali"/"Mutali") | Speaks entire call; the ONLY management voice | 42, 418, 544 |
| Moderator/IR desk | Shivani | Procedural only; affiliation not stated | 345, 348 |
| New Chairman | Mr Ilango (surname corrupted) | Ex-CEO "K energy", founder "HEC"; referenced, not a live speaker | 66–68 |
| Outgoing Chairman | Mr Kasam | Retired after 5 years | 66–67 |
| Retired independent director | "DT" | Retired, **not renewed** | 66–67 |
| New director | Ms J Deonish ("Jade") | Non-exec non-independent; **former MD of Geomysore Services 2012–2022** (the associate); present on call but **never speaks** — `SILENT_ATTENDEE` | 69–72 |
| Questioners (live) | Nikon Devpura, Hitesh Gupta, Ankit Gupta (CRK), Tan Sony (KTPL), Hardik Jane (Whitestone PMS), Pranav Jain (Dealwell), Shaswat Vijay (SIC Wealth), Kunal Shah (Hartwood), Imran Gani, Sundar Padmanaban, 1 unidentified | 12 identifiable + 1 `UNIDENTIFIED_SPEAKER` | Table 1 |
| Emailed queries (not live) | Nikhil Gohil ("from Aabad") | Answered by email only | 486–491 |

**Yellow flags from the participant list (protocol 0B / non-negotiables):**
- **No CFO voice on the call.** A single promoter-MD answers every question — operational, financial, legal, governance — with no finance second. On a quarter whose entire reported profit is an equity-method associate share, the absence of a CFO to speak to the consolidation, the inventory line and the dividend mechanics is a governance yellow flag. Positive read: promoter candour (protocol prefers promoter presence). Negative read: single-spokesperson concentration; nobody to cross-check the numbers live.
- **`SILENT_ATTENDEE`.** The newly-appointed director who ran the associate (Geomysore) 2012–2022 is on the call and never speaks. Related-party governance link (see F13) with no live accountability.
- **Board in flux:** Chair changed, an independent director retired and was not renewed, "few more board changes expected" (L73).

**0C. Call structure / date.** Q1 FY27 (June-2026 quarter). Call date on/around 2026-08 (transcript "yesterday you might have seen no additional taxes… by the state governments", L518, ties to a recent policy item). No filing date to measure lag against (concall-only). Body split ~60% prepared monologue (L39–346) / ~40% Q&A + responses (L347–550), flagged `MONOLOGUE_HEAVY` — the inverse of the protocol's "spend 60% of effort on Q&A" expectation for the *call*; the analytical effort here is nonetheless concentrated on Q&A per protocol.

**0D. Safe-harbour caveats.** None read into the transcript (no formal forward-looking-statement disclaimer captured). Management instead self-caveats verbally and heavily: "very tentative numbers" (L490), "guesstimate" (L274), "I cannot guarantee" (L423). Absence of a formal safe-harbour paired with dense verbal hedging is logged.

**0E. Business type.** **Standard operating business** (junior mining explorer transitioning to producer). NOT a lender — Step 2 (not 2L) guidance set applies.

---

### STEP 1 — OPENING-REMARKS CLAIMS INVENTORY

Every material opening-remarks claim (prepared blocks B1–B12, L39–346). Type per protocol. Quantified = has a number/date/binary milestone.

| # | Claim | Type | Quantified? | Line |
|---|---|---|---|---|
| C1 | "June quarter has clearly established us as the producer" (explorer→producer transition) | Strategic | NO | 45–47 |
| C2 | Two defined verticals: gold (producing) + critical/battery minerals (drilling) | Strategic | NO | 48–51 |
| C3 | Geomysore/Junagiri contributed Rs6.35cr PAT share, booked to DGML (equity method) | Backward | YES (Rs6.35cr) | 55–56 |
| C4 | Geomysore sold 59 kg gold (bullion) in the quarter | Backward | YES (59 kg) | 56 |
| C5 | "Gold in stock is much more… all going to be sold in coming months"; next quarter "much bigger" | Forward Soft | NO | 57–58 |
| C6 | Altyn Tor bar production started; September-quarter revenue + profit expected | Forward Soft | NO | 58–60 |
| C7 | Board approved Rs137cr raise via CCDs + equity shares + equity warrants; pending shareholder approval | Operational / Capital | YES (Rs137cr) | 60–61 |
| C8 | HNIs + management (incl. MD and Ms J Deonish) participating in the raise | Strategic / RPT | NO | 62–63 |
| C9 | Raise funds exploration of projects OTHER than Kyrgyzstan | Operational | NO | 64–65 |
| C10 | Board changes: Kasam out, Ilango in as Chair; DT (independent) retired; Ms J Deonish appointed | Governance | NO | 66–73 |
| C11 | Junagiri to increase to 2,500 tons/day; up to 2 tons gold/annum by ~2029–30 | Forward Guidance | YES (2,500 tpd; 2 t; ~2029–30) | 89–91 |
| C12 | Junagiri Q1 output: 112 kg dor bar → ~90 kg bullion; ~1 kg/day strike rate | Backward | YES (112 kg / 90 kg) | 93–94 |
| C13 | Junagiri revised in-mine resource estimate by October | Forward Guidance | YES (October) | 102 |
| C14 | Finland feasibility study targeted 2027 | Forward Guidance | YES (2027) | 105–106 |
| C15 | 3 new gold assets under due diligence, production by end-2027/2028 | Forward Soft | YES-ish (dates, no names/size) | 111–113 |
| C16 | Junagiri Q1 (verbal): Rs87cr revenue, Rs25cr PAT, Rs6.35cr DGML share; 40 kg gold + 60 kg dor bar in stock (~80 kg gold-equiv) | Backward | YES | 115–117 |
| C17 | Gold price ~Rs1,50,000 / 10 g; holding stock to sell into strength | Backward/Strategic | YES (Rs1.5L/10g) | 119–120 |
| C18 | Junagiri long-run target 40 t gold resource, LOM >25 years; largest gold mine in India in 3–4 years | Forward Soft | YES (40 t / 25 yr) but pre-drill | 122–126 |
| C19 | Junagiri ~1,000 direct jobs created | Backward | YES (~1,000) | 126–128 |
| C20 | Altyn Tor cumulative investment >Rs300cr | Backward | YES (>Rs300cr) | 136 |
| C21 | Altyn Tor commissioning "next week"; inauguration date TBD | Forward Guidance | YES (next week — binary) | 140–142 |
| C22 | Altyn Tor tailings: mgmt asserts ~6 Mt @ ~1.3 g/t AND ~780 kg contained gold — these do NOT reconcile (6 Mt × 1.3 g/t = 7,800 kg, a 10× gap; NUMBER_INCONSISTENCY, L153–154, ledger N30/N36/N37); ~1 Mt low-grade stockpile; 4–5 yrs feed claim rests on this unreconciled resource | Backward/Operational | NO — internally inconsistent | 147–154 |
| C23 | Altyn Tor revised mine-design/LOM plan by October 2026; underground resource work from Sept | Forward Guidance | YES (Oct 2026 / Sept) | 150–152 |
| C24 | Altyn Tor employment ~200 now → ~350 eventual (30 India engineers + 70 local) | Operational | YES | 162–165 |
| C25 | Kyrgyz government offering a SECOND gold project (~10 t gold implied) | Forward Soft | YES-ish (~10 t) | 167, 213 |
| C26 | Finland Kalwala/Pakali: 27.36 sq km; Kuika grade >5 g/t vs Junagiri ~1.4–1.5 g/t; target 4 t; Pakali ~2 t hist @ ~3.5 g/t | Operational | YES | 171–184 |
| C27 | Finland $1–2M for 51% stake, this/coming quarter; drilling start Sept 15, ~1,500 m; results 3–6 months | Forward Guidance | YES | 177–178, 190–192 |
| C28 | Ganajur: in court, hearings resumed after 2-yr delay; precedent (rights accrued before 2015); if lease granted ~1 t gold in 2–3 yrs | Strategic / Litigation | YES-ish (dates conditional) | 194–204 |
| C29 | Balukona NiCuPGE: 30 sq km composite (2025); 15th hole / ~2,500 m; ~1.3 km zone, ~700 m proven; ML application next year; ~3,000 tpd plant; feasibility mid next year | Operational / Forward | YES | 228–246 |
| C30 | Spain tungsten Logos/Maria: ~307 sq km granted (+30 pending); 7 holes / ~3,000 m; best 88% & 1.21% WO3 (ASR-garble) at 535 m; HESA results mid-Sept, resource model early Oct; ~1,000 tpd plant; ~3 Mt target | Operational / Forward | YES (some `ASR_GARBLE`) | 251–276 |
| C31 | Mozambique Li-Cs-Ta: ~150 sq km / 3 licences; 85% held; 4–5 pegmatites; 200 tpd concentrate plant end-2027 / Q1 FY28; first CM revenue ~2028 | Operational / Forward | YES | 278–297 |
| C32 | Critical-mineral prices last 12m: tungsten +622%, "Mozam" commodity +196%, lithium +108%, graphite +5% | Macro/Tailwind | YES | 312–315 |
| C33 | MoU with SERI (CSIR-CECRI) to supply Li/Ni/graphite concentrates for battery R&D, tech-transfer intended; MoU with Extera (beach-sand/CM blocks) | Strategic / Partnership | NO | 317–325 |
| C34 | Fund-raise rationale: short/intermediate drilling money now; larger QIP later "when we go for a larger funding" | Forward Soft / Capital | NO (QIP undated) | 337–341 |
| C35 | "Investors should look forward for full-scale commercial production from Kyrgyzstan" next quarter | Forward Soft | NO | 342 |

**Four mandatory diagnostics after the inventory:**
1. **% quantified vs unquantified (opening):** of 35 opening claims, ~24 carry a number/date/binary (~0.69) and ~11 are directional/strategic. Numerically dense, but the density is concentrated in *un-drilled, pre-feasibility* project targets that management itself calls "tentative" (L490). Specificity ≠ substance (see Step 6E).
2. **New vs reaffirmation:** almost everything is NEW (first coverage). The two items that are *reaffirmations of prior guidance* — Junagiri 500–600 kg and Kyrgyzstan 150–160 kg — are exactly the two that were **softened** and had their **Rs topline dropped** (F16-a).
3. **Quietly dropped:** the **prior guidance SLIDES** (Junagiri FY27 ~600 kg / Rs900–1,000cr topline & FY28 ~800 kg; Kyrgyzstan FY27 ~160 kg / Rs300cr & FY28 ~350 kg) were not shown this quarter and only surfaced because analyst Hardik Jane raised them (L381–384). **DROPPED without acknowledgment** (F16-a).
4. **Internal contradictions in opening:** (a) "clearly established as the producer" (L46) vs financials "still in the initial stages" (L53); (b) raise is for "projects OTHER than Kyrgyzstan" (L64) while Kyrgyzstan is simultaneously "almost ready for full-scale production" needing commissioning capex "next week" (L140); (c) "40 tons of gold… largest gold mine in the country" (L122–126) rests on drilling "still" ongoing, not a booked resource.

---

### STEP 2 — FORWARD GUIDANCE EXTRACTION

Standard-business guidance set. "Last Quarter" / "Two Quarters Ago" columns are `ND` (no prior Role 5 log; first coverage) — EXCEPT where an analyst read the *prior deck* into the record (that becomes the de-facto "Last Quarter" reference and the walk-back evidence). Every number is MANAGEMENT-ASSERTED, UNAUDITED, CONCALL-SOURCED.

| Metric | This Quarter's Guidance (line) | Prior (from dropped slides, per analyst) (line) | Two Qtrs Ago | Trajectory | Confidence |
|---|---|---|---|---|---|
| Junagiri production FY27 | 500–600 kg (L441) | ~600 kg (L381) | ND | Lowered/softened | MEDIUM ("let us wait, give us one more quarter", L428) |
| Junagiri production FY28 | 750–800 kg (L442) | ~800 kg (L382) | ND | Maintained | LOW (pre-drill) |
| Junagiri Rs topline FY27 | **WITHHELD** (L489–490) | ~Rs900–1,000cr (L382) | ND | **Withdrawn** | — (declined) |
| Kyrgyzstan production 2027 | 150–160 kg (L445) | ~160 kg (L383) | ND | Maintained | MEDIUM |
| Kyrgyzstan production FY28 | 300–350 kg (L445) | ~350 kg (L383) | ND | Maintained | LOW |
| Kyrgyzstan Rs topline | **WITHHELD** | ~Rs300cr (L383) | ND | **Withdrawn** | — |
| EBITDA margin band | ~65–70% target, "another quarter or two" to stabilise (L434) | investor: prior indication 60–65% (L363) | ND | Lowered/deferred; realised ~30% PAT margin (L363) | LOW (deferred) |
| FY28 output, mines OTHER than the two flagships | **NOT ANSWERED** (Q10, L384; no resolving line) | ND | ND | Withdrawn/absent | — |
| Capex envelope (portfolio) | ">Rs1,000cr identified, may need ~Rs2,000cr" (L453, L469); Rs400–500cr per standard plant, Rs650–700cr Balukona (L449–451); underground: Altyn Tor Rs150–200cr, Junagiri Rs400cr+ (L536–541) | ND | ND | New | LOW ("guesstimate", "tentatively") |
| Funding mix | Gold: 50/50 or 40:60 equity:debt (L468); Critical minerals: offtake-funded (L455–463) | Rights issue at ~Rs80 recently (L377) | ND | New | LOW (offtake "considering") |
| Dividend / payout (cash from associate) | "I doubt whether we'll get dividends this FY… might happen next year… cannot guarantee" (L421–423) | ND | ND | New | **INDETERMINATE** |
| New product / milestones | Altyn Tor commission "next week" (L140); Finland 51% this qtr, drill Sept 15 (L177,190); Oct-2026 LOM plans (Junagiri + Kyrgyzstan) (L102,150); Spain resource model early-Oct (L271) | ND | ND | New | MEDIUM–HIGH (binary, dated) |

**Diagnostic answers:**
- **Widen or tighten?** Management **lowered/softened** the two reaffirmed volume numbers, **withdrew** all Rs topline guidance, and **deferred** the margin target. Net = **increasing uncertainty**, not confidence.
- **Prior guidance dropped without acknowledgment?** **YES** — the topline/margin slides (F16-a, F16-b). Major credibility flag, mitigated only by this being first coverage (no cumulative pattern yet).
- **Arithmetic consistency (asserted numbers):** Junagiri Q1 PAT margin = Rs25cr / Rs87cr = **28.7%** (matches investor's "around 30%", L363) — NOT the 60–65% previously indicated. DGML's booked share = Rs6.35cr / Rs25cr = **25.4%** of Junagiri PAT (consistent with an associate-stake economics; the exact equity % is not stated on the call — `ND`). 59 kg sold vs ~90 kg produced ⇒ ~31 kg (plus prior stock) unsold, reconciling to the stated 40 kg gold + 60 kg dor bar (~80 kg gold-equiv) closing stock (L116, L430–431). The internal arithmetic of the *reported* quarter reconciles; the *forward* numbers are the soft ones.
- **Vs Four-Pillar projections:** N.A. — no Notion Four-Pillar model exists (first coverage). Baseline only.
- **What analysts pressed for and management refused:** Rs topline guidance for both flagship mines (Hitesh Gupta Q4, Hardik Jane Q9), FY28 output for non-flagship mines (Hardik Jane Q10), per-project economics (Nikhil Gohil, deferred to email). Refusal on addressable flagship-mine topline is itself information.

---

### STEP 3 — PROMISE vs DELIVERY AUDIT (BASELINE — FIRST OBSERVATION)

No prior concall log exists. Per protocol Step 3, the historical audit is **skipped** and the log **starts this quarter**. The A3 Commitment Register (21 dated/dateable commitments) is adopted as the **baseline promise register**; every row becomes a Q2 FY27 delivery test.

**3A/3B. Credibility ratio:** **NOT YET COMPUTABLE** (0 trailing quarters). No points, no ratio, no grade-from-history. Role 1 "management delivery track record" input = **UNESTABLISHED** (must be treated as such downstream; no session substitution permitted once a history exists, but none exists yet).

**3C. Pattern:** none trackable (n=1). The single within-quarter tell — dropping the topline slides while an analyst had to reintroduce them — is logged as the FIRST data point toward a possible future "drops commitments quietly when they don't deliver" pattern.

**3D. Promoter Verdict / Management Grade:** **BASELINE, provisional Grade "unrated — watch."** The 6E archetype (Step 6) is the operative label this quarter.

**3E. Prior Questions-for-Management:** none (first coverage). The forward question set is built fresh in the Questions-for-Management table below.

**BASELINE PROMISE REGISTER (adopted from A3 F6 — the Q2 FY27 delivery checklist):**

| # | Commitment | Implied date | Line | Status word (this call) | Q2 FY27 test |
|---|---|---|---|---|---|
| P1 | Rs137cr CCD+equity+warrant raise closes | pending shareholder approval | 60–61 | board-approved / pending | Approved & drawn? terms/dilution disclosed? |
| P2 | Larger QIP for principal funding | undated | 338 | proposed | Sized/dated yet? |
| P3 | Altyn Tor commissioning & production start | "next week" | 140–142 | underway | Commissioned? first Kyrgyz revenue booked? |
| P4 | Altyn Tor inauguration announced | "not very far" | 161 | intended | Date set/held? |
| P5 | Altyn Tor revised mine-design/LOM plan | Oct 2026 | 150–151 | in-process | Delivered? >5 t underground confirmed? |
| P6 | Altyn Tor underground/mining work begins | Sept 2026 | 152 | commencing | Started? |
| P7 | Junagiri revised in-mine resource estimate | October | 102 | expected | Published? |
| P8 | Junagiri 2,500 tpd processing approvals | in process | 123–124 | acquiring | Granted? |
| P9 | Junagiri 500–600 kg FY27 validation | end Q2 FY27 | 427–428 | reaffirmed | On pace (H1 run-rate)? |
| P10 | Finland 51% stake acquisition | this/coming quarter | 177–178 | intends | Closed? $ paid? |
| P11 | Finland drilling start ~1,500 m | Sept 15 | 190–191 | target-set | Started on date? |
| P12 | Finland feasibility study | 2027 | 105–106 | plans | Milestones set? |
| P13 | Balukona mining-lease application | next year | 240 | plans | Filed? |
| P14 | Balukona feasibility / flow-sheet | mid next year | 246 | will-do | On track? |
| P15 | Spain HESA full assay results | mid-Sept | 270 | expected | Released? |
| P16 | Spain preliminary resource model | early Oct | 271 | will-complete | Published? |
| P17 | Mozambique 200 tpd concentrate plant | end-2027 / Q1 FY28 | 291–294 | aims | On track? |
| P18 | 3 new gold assets into production | end-2027 / 2028 | 111–113 | due-diligence | Any signed/named? |
| P19 | Physical AGM in Mumbai | this FY | 483–485 | committed | Held physically? |
| P20 | Nikhil Gohil emailed-query response | post-call | 486–491 | deferred-email | Sent? content? |
| P21 | Rs522/520mn inventory realisation answer | post-call via P&L | 480–481 | deferred-email | Answered? number given? |

---

### STEP 4 — Q&A DECOMPOSITION (the heart of the analysis)

**4A. Q&A inventory (Ledger Tables 3–5; response quality graded per protocol 4A).**

| # | Analyst & firm | Question (1-line) | Category | Response quality | Substance / line |
|---|---|---|---|---|---|
| Q1 | Nikon Devpura, indiv | How does cash flow reach DGML from the associate — dividend commitment? | Financial | **C→D** partial; INDETERMINATE | "I doubt… this FY… cannot guarantee", L421–423 |
| Q2 | Nikon Devpura | Bring in a large promoter group, or stay professionally managed? | Governance | B | "not decided… professional team… future maybe", L470–476 |
| Q3 | Hitesh Gupta, indiv | Revenue/PAT far below the 60–65% margin indicated (~30% actual) — clarify | Financial | **B/C** reframed to EBITDA | "stabilise to 65–70% EBITDA… another quarter or two", L434 |
| Q4 | Hitesh Gupta | Will you give forward Rs guidance for Kyrgyzstan & Junagiri? | Forward Guidance | **D** refusal on Rs | volumes only; Rs withheld, L489–490 |
| Q5 | Ankit Gupta, CRK | Altyn Tor output this year and next? | Forward Guidance | B | 150–160 kg 2027; 300–350 kg after, L444–445 |
| Q6 | Ankit Gupta, CRK | Do dor bars need a refinery; is it set up at Altyn Tor? | Operational | **E→A (delayed)** ignored in RB1, answered only after re-ask | L369–370 → L500–512 |
| Q7 | Ankit Gupta, CRK | Total capex ~Rs2,000–2,200cr across projects; 50/50 debt:equity? | Financial | B | ~Rs2,000cr, offtake for CM, 40:60 gold, L447–469 |
| Q8 | Tan Sony, KTPL | Balukona funding — another rights issue (like the ~Rs80 one)? | Financial | **C** general, not rights-specific | offtake/debt-equity generic, L455–463 |
| Q9 | Hardik Jane, Whitestone PMS | Does prior slide guidance (600 kg/Rs900–1,000cr; 160 kg/Rs300cr; FY28) still stand? | Forward Guidance | **C** volumes softened, Rs dropped | L441–445; slides "not included this time", L381 |
| Q10 | Hardik Jane | FY28 output from mines OTHER than Junagiri/Kyrgyzstan? | Forward Guidance | **E** not addressed | no resolving line |
| Q11 | Pranav Jain, Dealwell | Revenue expectation now vs the "2030 dream pipeline"? | Strategic | C | qualitative only, L473–476 |
| Q12 | Pranav Jain | Strategic partnership with a deep-pocketed player? | Governance | B | "not now… maybe later", L470–476 |
| Q13 | Pranav Jain | Ganajur to production — 2–3 yrs or sooner? | Strategic/Litigation | C | litigation update, no firm timeline, L476–480 |
| Q14 | Shaswat Vijay, SIC Wealth | Rs522mn consol inventory — when realised; why no P&L change? | Financial | **D** deferred to email | L480–481 |
| Q15 | Kunal Shah, Hartwood | How is capex financed? | Financial | B | (same cluster as Q7), L447–469 |
| Q16 | Pranav Jain (f/u) | Legal status Ganajur vs Hatti (prospecting licence)? | Strategic/Litigation | B | ML vs PL distinction, L476–480 |
| Q17 | Imran Gani, indiv | REQUEST: physical AGM this year | Governance | A | "I guarantee… Mumbai", L483–485 |
| Q18 | Sundar Padmanaban | How much GoI funding support for these projects? | Macro/Policy | B | none now; future via NCMM/NMET, L513–526 |
| Q19 | Sundar Padmanaban | Uzbekistan CM offer to GoI — any news? | Macro | **D/E** near-non-answer | "no concrete… information", L527–530 |
| Q20 | Ankit Gupta (f/u) | Re-ask dor bar/refinery mechanics | Operational | A | Bangalore refinery, LBMA settle in Kyrgyzstan, L501–512 |
| Q21 | Unidentified | How does capex change going underground? | Operational | B | Altyn Tor Rs150–200cr; Junagiri Rs400cr+, L534–541 |

**4B. Question pattern analysis.**
- **Most-repeated topic = capex funding** (Q7 Ankit, Q8 Tan Sony, Q15 Kunal Shah — three separate analysts). Repeated question = the market does not trust the first answer. Given a Rs137cr raise + pending QIP + recent rights issue, the funding overhang is the #1 buy-side concern (ties F10).
- **Second cluster = forward guidance / topline** (Q4, Q9, Q10, Q11) — four analysts pushing for Rs numbers management would not give. This is the topic management does not want quantified (ties F16-a/-c).
- **Management graded C/D/E on:** cash-from-associate (Q1), Rs topline (Q4), FY28 non-flagship output (Q10), inventory realisation (Q14), Uzbekistan (Q19), and the dor-bar question was ignored until re-asked (Q6). The evasions cluster on the two hardest quantitative asks: **near-term cash** and **forward Rs guidance**.
- **Buy-side vs sell-side split:** the room is predominantly individual investors, PMS and small AIF/wealth desks (Whitestone PMS, SIC Wealth, Dealwell, Hartwood, CRK Research). No large mutual-fund/institutional analyst. Consistent with a micro-cap, pre-institutional name — per Master v3.3 this is NOT a negative signal per se, but it means the pushback is retail-grade; the sharpest questions (Hardik Jane on dropped slides, Shaswat Vijay on inventory) came from the PMS/wealth seats.
- **Hosting-broker softball?** No house-broker lead detected; the call is IR-desk moderated. Not an orchestrated-softball pattern.
- **Pushback:** mild. Hitesh Gupta (Q3) pushed on the margin miss and Hardik Jane (Q9) on the dropped slides — these are the genuinely contested topics.

**4C. The three most thesis-relevant exchanges.**

**Exchange 1 — Cash from the associate (Q1, Nikon Devpura → RB, L421–423).**
- Q: as DGML is only an associate of the Junagiri project, how does cash (not just booked profit) reach DGML — is there a dividend commitment?
- A (verbatim core): "profits already booked in ours… in terms of cash flow it has to come as dividend only… I honestly I doubt whether we'll get dividends in this financial year… it might happen next year but I cannot guarantee."
- Said specifically: the Rs6.35cr is equity-method book profit; cash arrives only as a GMS-board-decided dividend; management doubts any dividend this FY.
- Did NOT say: any dividend policy, any minimum, any cash-upstreaming mechanism, DGML's exact equity % in Geomysore.
- Thesis implication: **cash conversion is INDETERMINATE.** The entire reported consolidated profit uplift is non-cash to DGML this year. Per CLAUDE.md this **caps the verdict at PROCEED WITH CAVEATS** and cannot resolve to a clean PROCEED (F1-b).
- Follow-up we would have asked: what is DGML's exact stake in Geomysore, and what dividend policy governs upstreaming once the plant expansion capex is funded?

**Exchange 2 — The dropped guidance slides and the margin miss (Q3 Hitesh + Q9 Hardik → RB, L381–384, 434, 441–445, 489–490).**
- Q: the Junagiri revenue/PAT is "substantially lower… versus… 60–65%… total profit is around 30%"; and the prior slides guided ~600 kg / Rs900–1,000cr FY27 and Kyrgyzstan ~160 kg / Rs300cr — "this guidance remains the same or… change?" and "those slides are not included this time."
- A: reframes to "stabilise to about 65 or 70% of EBITDA… another quarter or two"; reaffirms volumes ("500 to 600", "150–160") but **declines all Rs topline** ("very tentative numbers… may not be a very good idea to give").
- Said specifically: volume guidance stands (softened at the low end); margin target restated as EBITDA and pushed out.
- Did NOT say: why the topline slides were withdrawn; a revised Rs number; why realised PAT margin was ~30% vs the ~60–65% previously implied.
- Thesis implication: **guidance withdrawal + margin walk-back** (F16-a, F16-b). Classic soft-guidance quarter. First observation, so no credibility-ratio hit yet, but the FIRST data point of a possible over-promise pattern.
- Follow-up: reconcile the ~30% realised PAT margin to the prior 60–65% indication line by line, and confirm whether the Rs topline is withdrawn or merely deferred.

**Exchange 3 — Capex quantum and how it is funded (Q7/Q8/Q15 → RB, L447–469).**
- Q (three analysts): total capex ~Rs2,000–2,200cr across Spain/Balukona/Mozambique/Finland/Ganajur; is 50/50 debt:equity fair; is Balukona another rights issue?
- A: "we may require around 2,000 crores"; gold projects funded ~40% equity / 60% debt; critical-mineral projects to be **offtake-funded** ("many graphite projects in Africa are funded by Elon Musk… his money comes in as an offtake arrangement… supply concentrate for the next 10 years at a discounted price"); "exchange of ideas" with copper smelters, nothing contracted.
- Said specifically: ~Rs2,000cr envelope; a funding *philosophy* (offtake for CM, debt/equity for gold).
- Did NOT say: any signed offtake, any term sheet, any bank sanction, the dilution quantum of the Rs137cr raise or the pending QIP.
- Thesis implication: a **~Rs2,000cr funding requirement against a company doing Rs6.35cr of booked (non-cash) profit** and raising Rs137cr in stacked instruments with related-party participation (F10). The offtake model is aspirational, not contracted (F7). This is the dilution/solvency overhang to size.
- Follow-up: what is the pro-forma diluted share count post-Rs137cr and post-QIP, and is any offtake or bank facility signed rather than "in discussion"?

---

### STEP 5 — NEW INFORMATION AUDIT

**5A. New disclosures (all first-coverage; materiality relative to a not-yet-built thesis).**

| Disclosure | Type | Material? | Thesis impact |
|---|---|---|---|
| Rs137cr raise (CCD + equity + warrants), mgmt/HNI participation, pending shareholder vote (L60–63) | New capex/capital + RPT | YES | Dilution + related-party overhang (F10) |
| Pending larger QIP, undated (L338) | New capital | YES | Second dilution layer (F10) |
| Recent rights issue at ~Rs80 (surfaced by analyst, L377) | Capital history | YES | Third dilution layer; sets a recent price reference |
| Altyn Tor/Kyrgyzstan producing dor bar; commissioning "next week" (L140) | New capacity | YES | Nearest hard catalyst |
| Geomysore/Junagiri producing; Rs6.35cr equity-method share booked (L55) | New segment economics | YES | First production revenue; but non-cash to DGML |
| New Chair (Ilango), independent director retired & not renewed, ex-Geomysore MD to board (L66–73) | New senior management / governance | YES | Governance/RPT signal (F13) |
| Kyrgyz government offering a SECOND gold project (~10 t) (L167) | New geography/asset | YES-soft | Optionality, un-diligenced |
| 3 new gold assets under due diligence (L111) | New pipeline | YES-soft | Unnamed, unsized |
| SERI (CSIR-CECRI) battery-R&D MoU; Extera beach-sand MoU (L317–325) | New partnership | YES-soft | Downstream optionality, non-binding |
| Consolidated inventory ~Rs522/520mn, no P&L movement this quarter (L399, 481) | Negative surprise / unresolved | YES | Static-inventory question (F1-a), deferred |
| Graphite project in Africa under review (L306) | New asset | NO-soft | Early optionality |
| Critical-mineral price moves: W +622%, +196%, Li +108%, graphite +5% (L312) | Macro | YES | Sector-cycle backdrop |
| Indian CM policy: NCMM corpus (Rs40,000/44,000cr — inconsistent), NMET Rs16,000cr overseas-exploration funding, no state tax, public-hearing waiver (L513–521) | Regulatory | YES | Structural tailwind for CM vertical |

**5B. What was NOT discussed (silence audit — first observation; no prior baseline to diff, so run against the F6 register and Ledger Table 8).**

| Expected topic | Why it should have been discussed | Significance of silence |
|---|---|---|
| Rs522/520mn inventory realisation & why zero P&L movement in a production quarter | Direct analyst question (Shaswat Vijay Q14) | **AMBER** — deferred to email, no number on call (F1-a) |
| FY28 output from mines OTHER than Junagiri/Kyrgyzstan | Direct analyst question (Hardik Jane Q10) | **AMBER** — never answered; guidance covers only the two flagships (F16-c) |
| Rs topline guidance for both flagship mines (prior ~Rs900–1,000cr / Rs300cr) | Was on prior slides; two analysts asked | **AMBER→RED** — withheld; slides dropped (F16-a) |
| Dilution quantum of the Rs137cr raise and the pending QIP | Three analysts pressed on funding | **AMBER** — quantum never given (F10) |
| DGML's exact equity % in Geomysore | Determines the cash/dividend claim | **AMBER** — never stated; `ND` throughout |
| Dor-bar/refinery mechanics at Altyn Tor | Direct analyst question (Ankit Q6) | **AMBER** — ignored in RB1 until re-asked (F17) |
| QIP size/timing | Management's own reference (L338) | **AMBER** — left open |
| Per-project economics (capex/resource/annual output) | Nikhil Gohil emailed list | Declined on call as "very tentative", deferred to email (F7) |
| Uzbekistan CM offer to GoI | Direct analyst question (Sundar Q19) | Near-non-answer (D5) |

Per Role 5, none can yet be scored "sustained silence on a deteriorating metric" (n=1). These form the **baseline silence set to re-check at Q2 FY27**; the inventory-realisation and FY28-non-flagship-output silences are the two to watch.

---

### STEP 6 — TONE & SPECIFICITY

**6A. Tone comparison across concalls.** No prior concall in the log → all rows `ND` (baseline). The only within-call tone shift trackable is on the reaffirmed guidance: prior deck's firm slide numbers → this call's verbal "let us wait, give us one more quarter" (L428) and "very tentative numbers" (L490). **Direction on guidance specificity: DOWNGRADED** (numbers → hedged verbal ranges), which is the single most important tone signal available this quarter.

**Management-tone read (mandated).** The MD's register is **promoter-confident on narrative, hedged on numbers**. Confidence vocabulary dominates the prepared remarks — "clearly established us as the producer" (L46), "biggest takeaway" (L47), "very very confident" (L444), "I'm very proud" (L268). But every time an analyst asks for a testable figure — cash, topline, FY28 output, dilution — the register flips to hedge: "I cannot guarantee" (L423), "guesstimate" (L274), "very tentative" (L490), "exchange of ideas" (L462). The pattern is a **confident-narrative / hedged-number split**: strong on story, evasive on the arithmetic that would test it. Read adversarially (protocol), this is the bear case revealing itself — the story is producer-transition, but the near-term cash and margin are soft and the forward numbers were withdrawn.

**6B. Specificity score (whole call).**
- Quantified forward statements (number/date/binary): ~16 (Ledger Table 7 F1–F13, F15, F16 — dated drilling starts, resource-model dates, plant sizes, capex bands, commissioning "next week", AGM commitment).
- Unquantified/soft forward statements: ~5–6 (dividend "cannot guarantee", QIP undated, offtake "considering", strategic-partner "not decided", second Kyrgyz project un-diligenced, "2030 dream pipeline").
- **Specificity ratio ≈ 16 / 22 ≈ 0.73 → HIGHLY SPECIFIC concall.**

**6C. Defensive-language / hedge count (protocol threshold >5 = hedge-heavy).**
"I cannot guarantee" (L423), "I honestly I doubt" (L422), "guesstimate" (L274), "very tentative numbers" (L490), "exchange of ideas… very preliminary stage" (L462), "we hope to" (L291), "considering" offtake (L463), "let us wait / give us one more quarter" (L204, L428), "I don't say it's too early but… somewhere in the middle" (L214), "we will reply… next" [deferral] (L481). **≥10 hedge instances → HEDGE-HEAVY call**, concentrated on cash, dividend, forward guidance, and un-drilled resource economics.

**6D. Confidence indicators (genuine specificity).** Dated near-term milestones with binary tests: Altyn Tor commissioning "next week" (L140), Finland drilling "September 15th" (L190), Oct-2026 LOM plans (L150), Spain resource model "early October" (L271), physical AGM "I guarantee… Mumbai" (L483). Promoter answering operational, financial and legal questions directly (positive per protocol). Acknowledgment of the margin miss with an explicit — if deferred — recovery timeline (L434).

**6E. Management archetype (Specificity × Credibility 2×2).**
- Specificity = 0.73 (>0.5, high).
- Credibility = **UNESTABLISHED** (no trailing-4 history; first coverage).
- With credibility not yet measurable, the archetype cannot be finalised. **Provisional label: OVERPROMISER-WATCH.** The combination present this quarter — very high specificity on un-drilled/pre-feasibility targets, PLUS a same-quarter guidance-slide withdrawal and margin walk-back — is precisely the entry signature of the Overpromiser quadrant (protocol's "danger quadrant": hyper-specific guidance the delivery record does not yet back). Treatment until a track record exists: **anchor to what is producing and cash-testable (Junagiri output, Altyn Tor commissioning), treat all pre-drill project numbers and Rs targets as promotional, and require pre-committed delivery thresholds — not narrative — before any position action.** If Q2 FY27 delivers the near-term binaries (Altyn Tor commissioned, Junagiri H1 run-rate on pace, Oct LOM plans published), the archetype can migrate toward COMMITTED & CREDIBLE; if the dropped-slide/soft-number pattern repeats, it confirms OVERPROMISER.

---

### STEP 7 — CROSS-REFERENCE vs FILING AND PEERS

**7A. Concall narrative vs filing numbers.** **No filing supplied (concall-only run).** Every reconciliation is therefore **UNVERIFIABLE against a filing.** The concall's own asserted numbers are internally consistent for the reported quarter (Step 2 arithmetic check) but remain MANAGEMENT-ASSERTED, UNAUDITED.

| Concall claim | Filing evidence | Reconciliation |
|---|---|---|
| Rs6.35cr associate profit share booked (L55) | none supplied | UNVERIFIABLE (asserted) |
| Junagiri Rs87cr rev / Rs25cr PAT (L115) | none supplied | UNVERIFIABLE (Geomysore-level, not DGML P&L) |
| Consol inventory ~Rs522/520mn, no P&L change (L399,481) | none supplied | UNVERIFIABLE; flagged for the eventual filing (F1-a) |
| Rs137cr raise board-approved (L60) | none supplied | UNVERIFIABLE (board disclosure would confirm) |
| >Rs300cr invested in Kyrgyzstan (L136) | none supplied | UNVERIFIABLE (would appear as CWIP/investment) |

**Standalone vs consolidated (mandated, both always).** With no filing, the S-vs-C statement pair cannot be decomposed (A3 F2 = N.A.). What the call establishes qualitatively: **the entire consolidated profit uplift this quarter is the Rs6.35cr equity-method share of the Geomysore associate.** On a DGML *standalone* basis there is no mining revenue of substance disclosed on the call; DGML is a holding/associate-interest vehicle whose reported profit is non-cash associate income. The standalone-vs-consolidated PAT gap is therefore effectively **~100% of consolidated profit sitting in the associate line** (asserted; exact standalone PAT `ND`). This is the single most important structural fact for the eventual filing review and is carried forward as the primary Q2 reconciliation item.

**7B. Peer concall cross-check.** **No peer in the analysed universe** (first coverage; DGML is the only listed Indian junior gold-to-producer of its kind at this scale, and no adjacent-sector peer concall was supplied within ±4 weeks). Peer cross-check is therefore **N.A. this quarter, stated explicitly** per protocol. (Directional external context — the tungsten +622% / lithium +108% price moves management cited — is management-sourced, not an independent peer check.)

**7C. Concall vs external channel checks.** No independent third-party source supplied. The Indian CM-policy items (NCMM corpus, NMET overseas funding, no-state-tax, public-hearing waiver, L513–521) are management-asserted and should be verified against the actual policy notifications before being underwritten (the NCMM corpus figure is internally inconsistent, Rs40,000cr vs Rs44,000cr, F14).

---

### STEP 8 — THESIS & POSITION (BASELINE)

**8A. Growth-trigger status.** No Notion triggers exist (first coverage). **Baseline trigger set established** for future tracking:

| Trigger (baseline) | Concall evidence | Baseline status |
|---|---|---|
| Junagiri ramps to 500–600 kg FY27 / stabilises 65–70% EBITDA | L441, L434 | ON TRACK (unproven; 1 quarter) |
| Altyn Tor commissioned and cash-generating | L140 | NEAR-TERM (commission "next week") |
| Cash actually upstreams from Geomysore (dividend) | L421–423 | **AT RISK** — INDETERMINATE this FY |
| Critical-mineral vertical reaches first concentrate/revenue | L296 | 2028+ (pre-drill) |
| Ganajur lease restored (litigation) | L194–204 | CONTINGENT (in court) |
| Funding secured without excessive dilution | L60, L338, L453 | **AT RISK** — stacked raise + Rs2,000cr need |

**8B. Watchlist (baseline established, no prior rows).** Inventory realisation; dividend upstreaming; dilution quantum; Altyn Tor commissioning date; Oct-2026 LOM plans; Ganajur hearing. All carried into Monitorables below.

**8C. Thesis-broken check.** No thesis-broken conditions exist yet (first coverage). **Baseline conditions proposed** for Notion: (i) associate dividend not upstreamed for 2+ FYs while capex escalates; (ii) a second consecutive quarter of withdrawn/soft topline guidance; (iii) dilution beyond a to-be-set threshold from stacked raises; (iv) Junagiri H1 run-rate materially below the 500 kg low end. None fired (n=1).

**8D. Four-Pillar inputs.** N.A. — no Section 1B model exists for DGML (first coverage); no exit multiple is assigned here (exit PE authority is Section 1B v3.3, invoked only at Role 1, not in this quarterly review). Baseline note for the eventual Role 1: Pillar 2 (Cash Conversion) will open at **INDETERMINATE / provisionally weak** given the associate-dividend doubt (the drag is *growth-induced* — capex reinvestment at Geomysore, not a structurally leaky model — but it is unrealised, so no growth-offset can be credited until a dividend actually flows).

**8E. Position decision.** **NOT RATED — BASELINE ESTABLISHED.** There is no existing position and no Notion Decision Status to frame against; therefore no HOLD/ADD/TRIM/EXIT language applies. Decision Status verified = **None (first coverage).** Position branch = **n/a** (no held position; not an 8A-W warrant-holder decision — the warrants here are a company-level issuance, not a position we hold). The output of this review is a **baseline monitoring page**, not a buy/sell.

**8F. Updated questions for management** — see the dedicated Questions-for-Management table below (serves as both the Step 8F forward set and the contractual A3-finding conversion).

---

## MANDATED SPECIAL ANALYSES

### (i) Guidance walk-back analysis (F16-a / F16-b / F16-c)

| Element | Prior (dropped slide / prior indication) | This quarter | Nature |
|---|---|---|---|
| Junagiri FY27 volume | ~600 kg (L381) | 500–600 kg verbal (L441) | Softened at low end |
| Junagiri FY27 topline | ~Rs900–1,000cr (L382) | **withheld** (L489) | **Withdrawn** |
| Junagiri FY28 volume | ~800 kg (L382) | 750–800 kg (L442) | Maintained |
| Kyrgyzstan FY27 volume | ~160 kg (L383) | 150–160 kg (L445) | Maintained |
| Kyrgyzstan FY27 topline | ~Rs300cr (L383) | **withheld** | **Withdrawn** |
| Junagiri margin | ~60–65% implied (L363) | ~30% realised PAT; 65–70% EBITDA target pushed "another quarter or two" (L434) | **Walk-back + deferral** |
| FY28 non-flagship output | (on prior "dream pipeline") | **not answered** (L384) | **Withdrawn/absent** |

The walk-back is **material and same-quarter**: the guidance slides were removed from the deck and only re-entered the record because an analyst quoted them (F16-a); the margin expectation dropped from ~60–65% to a realised ~30% with recovery deferred (F16-b); and fuller guidance was actively declined as "very tentative", resting on un-drilled resource for every non-flagship project (F16-c). First observation, so no cumulative credibility penalty yet — but this is the founding data point of the promise-vs-delivery record and the reason for the OVERPROMISER-WATCH archetype.

### (ii) Capital-allocation & dilution read (F10)

**Stacked dilution, three layers, quantum undisclosed:**
1. **Rs137cr** via CCDs + equity shares + equity warrants, board-approved, **pending shareholder vote** (L60–61).
2. A **pending larger QIP** for principal funding, **undated and unsized** (L338, L340).
3. A **recent rights issue at ~Rs80** (surfaced by analyst Tan Sony, L377).

**Related-party participation:** the Rs137cr raise includes **management (the MD and Ms J Deonish) and HNIs** (L62–63). Insider participation can be a confidence signal, but on a warrant/CCD structure it is also a **related-party placement** whose pricing and dilution terms were not disclosed on the call. Against a stated portfolio funding need of **~Rs2,000cr** (L453, L469) versus Rs6.35cr of booked (non-cash) profit, the dilution runway is long and the terms opaque. The critical-mineral leg is meant to be **offtake-funded** (the "Elon Musk / graphite" analogy, L457) but nothing is contracted ("exchange of ideas… very preliminary", L462). **Dilution quantum is the single biggest unquantified risk this quarter** and the top Q2 question.

### (iii) Associate-accounting & cash-conversion analysis (F1-b) — INDETERMINATE

- **Structure:** Geomysore Services operates Junagiri; DGML holds an **associate** interest (equity-accounted). Exact DGML equity % = **`ND`** (never stated on the call). Implied by Rs6.35cr / Rs25cr ≈ **25.4% economic share** of Junagiri PAT (asserted, not confirmed as the equity stake).
- **Book vs cash:** Rs6.35cr is **equity-method book profit**, not cash. Cash reaches DGML **only via a Geomysore-board dividend** (L420).
- **Dividend outlook:** management **"doubts"** any dividend this FY, "might happen next year," **"cannot guarantee"** (L421–423) — because Geomysore's cash is being reinvested into plant expansion and land acquisition.
- **Verdict impact (CLAUDE.md, binding):** cash conversion is **INDETERMINATE**. It must **NOT** silently resolve to PROCEED. It **caps the verdict at PROCEED WITH CAVEATS**, with the **missing evidence named**: (a) DGML's exact Geomysore stake; (b) a stated dividend policy or upstreaming mechanism; (c) the timing of the first dividend. Character of the drag: **growth-induced** (reinvestment), not structural — but unrealised, so no Pillar-2 growth-offset can be credited until cash actually flows.
- **Inventory cross-link (F1-a):** the ~Rs522/520mn consolidated inventory showed **no P&L movement** this quarter despite a production/sales quarter (L399–400, L481). Deferred to email, no number given. Possible stale/slow-moving stock or a consolidation-scope quirk (the associate is equity-accounted, so Junagiri's own inventory would NOT flow through DGML's consolidated inventory line — which itself needs reconciling on the eventual filing). Carried as an open Q2 item.

### (iv) Project maturity classification — exploration → feasibility → production

| Bucket | Projects / numbers | Basis (line) |
|---|---|---|
| **FEASIBILITY-BACKED (rely-on)** | **Junagiri** (Geomysore associate; producing; 500–600 kg FY27 reaffirmed); **Altyn Tor / Kyrgyzstan** (commissioning "next week"; 150–160 kg 2027; tailings-fed) | Mgmt: only these two have completed feasibility (L489); Junagiri producing (L93), Altyn Tor commissioning (L140) |
| **PRE-DRILL / TENTATIVE (do NOT underwrite)** | **Finland** Kalwala/Pakali (>5–6 t target, feasibility not started); **Balukona** NiCuPGE (15 holes, ~700 m proven, 3,000 tpd plant *planned*, feasibility mid-next-year); **Spain tungsten** Logos/Maria (7 holes, resource model *early Oct*, 3 Mt *target*, assay `ASR_GARBLE`); **Mozambique** Li-Cs-Ta (mapping/soil only, plant end-2027); the 40 t / "largest mine" / 2-t-per-annum Junagiri-2029/30 vision; the "2030 dream pipeline" | Mgmt's own "very tentative numbers… before completion of drilling programs" (L489–490); "guesstimate" (L274) |
| **LITIGATION-CONTINGENT** | **Ganajur** (mining lease, in court; ~1 t IF lease granted, 2–3 yrs); **Hatti** (prospecting licence only — earlier stage than Ganajur) | In court, "let's wait what happens" (L204); ML vs PL distinction (L476–480) |
| **UNDER REVIEW / BACK OF QUEUE** | **Tanzania** gold (results "not fully satisfactory"); graphite project in Africa (reviewing); second Kyrgyz project + 3 DD gold assets (un-diligenced) | L106–107 (Tanzania), L306 (graphite), L167/L111 (pipeline) |

Only **two** of the portfolio's ~10 named projects are feasibility-backed and producing/commissioning. Every headline resource target beyond those two is pre-drill by management's own admission. Underwrite the two flagships; treat the rest as optionality.

---

## QUESTIONS FOR MANAGEMENT (contractual — every FORWARD-SIGNAL / AMBIGUOUS finding produces ≥1 row; deferred items D1/D3 converted)

| # | Question | From finding | Why it matters | Watch next concall |
|---|---|---|---|---|
| QM1 | What is DGML's exact equity % in Geomysore Services, and what dividend policy governs cash upstreaming once Junagiri's expansion capex is funded? | F1-b | Cash conversion is INDETERMINATE; the whole reported profit is non-cash | A stated stake + dividend policy, or a first declared dividend |
| QM2 | Will any dividend be paid by Geomysore in FY27; if not, when — and what is the cash bridge to DGML in the interim? | F1-b | Determines whether booked profit ever becomes cash | Dividend declared / timeline hardened |
| QM3 | Why did the FY26 consolidated inventory (~Rs522/520mn) show zero P&L movement in a production quarter, and when is it realised? | F1-a / D1 | Static inventory in a "producer" quarter is a data-quality/realisation flag | The promised P&L-statement answer / a number |
| QM4 | What is the pro-forma diluted share count after the Rs137cr CCD+warrant+equity raise AND the pending QIP, at what strike/conversion terms? | F10 | Dilution quantum is undisclosed against a ~Rs2,000cr need | Terms + share count disclosed |
| QM5 | On the Rs137cr raise, what price/terms are the management and HNI (related-party) participants receiving vs public shareholders? | F10 | Related-party placement pricing governance | RPT pricing disclosed / approved |
| QM6 | Is the QIP sized and dated yet, and how does it rank against the recent ~Rs80 rights issue and the CCDs? | F10 | Sequencing of three dilution layers | QIP quantum/date |
| QM7 | Which of the Q2 dated commitments actually landed — Altyn Tor commissioning ("next week"), Finland Sept-15 drill start, Oct-2026 Junagiri & Kyrgyzstan LOM plans, Spain early-Oct resource model? | F6 | These are the first promise-vs-delivery tests of the record | Each binary hit or slipped |
| QM8 | Are any critical-mineral OFFTAKE arrangements actually signed (vs "exchange of ideas"), and with whom? | F7 | The CM funding model is aspirational, not contracted | A signed offtake/term sheet |
| QM9 | Will you restate the withdrawn Rs topline guidance for Junagiri and Kyrgyzstan, or is it permanently replaced by volume-only guidance? | F16-a | Guidance slides were dropped without acknowledgment | Rs guidance restored or explicitly retired |
| QM10 | Reconcile the realised ~30% Junagiri PAT margin to the previously indicated ~60–65%, and confirm the path/timeline to 65–70% EBITDA. | F16-b | Margin walk-back with deferred recovery | Margin trending to target or not |
| QM11 | What FY28 production do you expect from mines OTHER than Junagiri and Kyrgyzstan (Finland/Balukona/Spain/Mozambique)? | F16-c / D3 | Never answered; the whole "growth beyond the two flagships" question | A number or an explicit "too early" |
| QM12 | Given the ex-Geomysore MD now sits on the DGML board, what related-party controls govern DGML–Geomysore transactions, and why was the retiring independent director not renewed? | F13 | Related-party governance link + independent-director attrition | Board composition / RPT policy |
| QM13 | What are the "few more board changes expected", and will independent-director strength be restored? | F13 | Unsettled board | New appointments disclosed |
| QM14 | Reconcile the Altyn Tor tailings figures: which of the three is correct — ~6 Mt tonnage, ~1.3 g/t grade, or ~780 kg contained gold? 6 Mt × 1.3 g/t implies 7,800 kg, not 780 kg (a 10× gap). | C22 / NUMBER_INCONSISTENCY (L153–154) | The 4–5 year "de-risked feed" resource base is internally inconsistent by 10× | A single reconciled tailings resource (tonnage × grade = contained gold) |

---

## MONITORABLES / CATALYST LIST (dates from the A3 commitment register)

| # | Item | Implied date | Source (line) |
|---|---|---|---|
| M1 | **Altyn Tor / Kyrgyzstan full-scale commissioning + first production** ("next week" / imminent) | ~Aug 2026 (imminent) | L140–142 |
| M2 | Altyn Tor inauguration date announced | "not very far" | L161 |
| M3 | Altyn Tor underground/mining work begins | Sept 2026 | L152 |
| M4 | **Junagiri revised in-mine resource estimate** | October 2026 | L102 |
| M5 | **Altyn Tor revised mine-design / LOM plan** | October 2026 | L150–151 |
| M6 | Finland 51% stake acquisition closes ($1–2M) | "this/coming quarter" | L177–178 |
| M7 | **Finland drilling start (~1,500 m)** | Sept 15, 2026 | L190 |
| M8 | Mozambique Li-Cs-Ta drilling start | mid/end-Sept 2026 | L290, L293 |
| M9 | Spain (HESA) full assay results | mid-September 2026 | L270 |
| M10 | Spain preliminary resource model | early October 2026 | L271 |
| M11 | **Shareholder approval of the Rs137cr raise** | near-term (post-call) | L61 |
| M12 | Larger QIP sizing/timing | undated | L338 |
| M13 | **Ganajur court hearing** (resumes after 2-yr delay) | expected "very soon" (post-July) | L195–197 |
| M14 | **Physical AGM, Mumbai** | this FY | L483–485 |
| M15 | Nikhil Gohil emailed per-project data response | post-call | L486–491 |
| M16 | Inventory-realisation answer via P&L reply | post-call | L480–481 |
| M17 | Balukona mining-lease application | "next year" | L240 |
| M18 | Balukona / Spain feasibility (flow-sheet) | mid next year | L246, L273 |
| **M0** | **Q2 FY27 concall = the decisive quarter** — first guidance-validation checkpoint on M1, M4, M5, M7, M9, M10, the dividend question, and the dilution terms | Nov 2026 (est.) | L427–428, L437, L442 |

---

## VERDICT

**PROCEED WITH CAVEATS.**

- **Cash conversion = INDETERMINATE** (F1-b). Per CLAUDE.md this is the binding cap: the verdict cannot be a clean PROCEED. **Missing evidence named:** DGML's exact Geomysore stake, a dividend/upstreaming policy, and dividend timing. The entire reported consolidated profit uplift (Rs6.35cr) is non-cash associate income; management doubts any dividend this FY.
- **Flags propagate (no STOP; no mechanical failure).** The following are surfaced prominently and carried into the baseline monitoring page:
  - **F10 — stacked, related-party dilution overhang:** Rs137cr CCD+warrant+equity (mgmt/HNI participation) + pending QIP + recent ~Rs80 rights issue; quantum undisclosed against a ~Rs2,000cr portfolio need.
  - **F16-a — guidance-slide withdrawal:** prior Rs topline slides dropped without acknowledgment; only volume guidance retained, softened.
  - **F16-b — margin walk-back:** realised ~30% PAT vs ~60–65% indicated; 65–70% EBITDA target deferred "a quarter or two."
  - **F1-a — static inventory:** ~Rs522/520mn, no P&L movement, realisation deferred.
  - **F7 / F16-c — soft forward numbers:** every non-flagship project number is "tentative"/pre-drill; FY28 non-flagship output unanswered.
  - **F13 — governance:** related-party director added (ex-Geomysore MD), independent director not renewed, more board changes pending; single-spokesperson call, no CFO.
  - **C22 / NUMBER_INCONSISTENCY — unreconciled tailings resource:** the Altyn Tor "4–5 years of de-risked tailings feed" claim rests on figures that do not internally reconcile — 6 Mt × 1.3 g/t = 7,800 kg, not the stated ~780 kg (10× gap, L153–154). Bear counter (grafted): the near-term production base management leans on is quantified with a number that is wrong by an order of magnitude somewhere, and the underground >5 t that would extend life is still pre-drill.
- **Not a REWORK or INSUFFICIENT EVIDENCE:** the ledger reconciled 100% (95/15/21/4), A3 GATE PASS, and the analysis is complete; the gaps are management-disclosure gaps (named as questions), not extraction failures.
- **Baseline, first coverage:** no position, no Decision Status, no buy/sell. Decision Status = **not rated / baseline established.** Management archetype = **OVERPROMISER-WATCH** (high specificity, credibility unestablished, same-quarter walk-back). Q2 FY27 is the decisive validation quarter.

Cash conversion tag: **INDETERMINATE.** Position branch: **n/a.** Decision Status verified: **None (first coverage).**

---

## PLAIN-LANGUAGE BRIEF

### 1. Summary narrative

Deccan Gold Mines held its June-2026 quarter investor call and its headline message was that it has crossed from being an explorer to being a producer. Gold is now coming out of two mines: the Junagiri project in Karnataka (run by an associate company, Geomysore) and the Altyn Tor project in Kyrgyzstan, which management says will be commissioned "next week." For the quarter, management stated Junagiri did about Rs87 crore of revenue and Rs25 crore of profit, of which Deccan Gold's share was Rs6.35 crore. These are numbers spoken on the call, not from an audited filing, and they should be read as management's own unaudited figures.

There are three things a plain reader should hold onto. First, the Rs6.35 crore is an accounting share of profit, not cash in Deccan Gold's bank. Cash only arrives if Geomysore pays a dividend, and management openly said it "doubts" any dividend this financial year and "cannot guarantee" one. So the profit is real on paper but has not turned into cash. Second, the company is raising money in layers: Rs137 crore now through convertible debentures, shares and warrants (with the promoters and some wealthy investors putting money in themselves), a larger QIP still to come, and a rights issue done recently at about Rs80. How much this dilutes existing shareholders was not spelled out, and the company says it may eventually need around Rs2,000 crore across all its projects. Third, the detailed revenue and profit guidance slides shown in earlier quarters were quietly dropped this time; management gave only rough production volumes and refused to give rupee-revenue targets, and the profit margin came in around 30% versus the 60-65% investors thought they had been told.

The positives are genuine: two mines are actually producing or about to, there is a lot of gold sitting in stock waiting to be sold into a strong gold price (about Rs1.5 lakh per 10 grams), and the company has a large portfolio of gold and battery-metal projects in India, Kyrgyzstan, Finland, Spain and Mozambique. The catch is that only the two flagship mines are backed by completed feasibility studies. Everything else is pre-drilling, and management itself called those numbers "very tentative." The verdict is Proceed With Caveats: this is first-time coverage, there is no position to hold, and the honest reading is "watch closely, prove the cash and the dilution before believing the story." The next quarter is the one that will tell us whether management delivers what it promised.

### 2. Sector intelligence
*(Provenance: all figures below are from THIS QUARTER'S CONCALL; no prior Notion or peer work exists — first coverage.)*

- Gold and critical minerals are in a strong up-cycle. Management cited 12-month price moves of tungsten +622%, a Mozambique-linked commodity +196%, lithium +108%, and graphite +5% (L312-315) — presented as validation of the two-vertical strategy. These are management-sourced and should be independently verified.
- Indian critical-mineral policy is a structural tailwind management is leaning on: a National Critical Mineral Mission corpus (stated inconsistently as Rs40,000cr and Rs44,000cr in the same passage — a data-quality flag, L514/L519), NMET funding of ~Rs16,000cr earmarked to support overseas exploration by private companies (L520-521, with a per-project cap of "a million dollars or something"), removal of the public-hearing requirement for critical-mineral projects (faster timelines), and a state commitment to levy no additional state taxes on these industries (L517-519). Tax incentives were also cited for lithium, nickel and cobalt.
- Gold economics: dor bars are the standard mine product; they are refined (in India, at the Bangalore refinery, settled at the Indian Bullion & Jewellers Association price; in Kyrgyzstan, by law at a government refinery at the LBMA price). Junagiri uniquely set up its own small refinery (cost ~Rs4-5cr) to sell bullion directly (L502-512).

### 3. Business-model intelligence
*(Provenance: all figures from THIS QUARTER'S CONCALL; first coverage.)*

- Deccan Gold is a junior explorer transitioning to producer. Critically, its flagship Junagiri cash flow comes through an ASSOCIATE (Geomysore), so profit is equity-accounted (Rs6.35cr booked, L55) but cash depends on a dividend that management doubts this year (L421-423). This is the core model risk: booked profit is not cash.
- Two funding models run in parallel: gold projects funded by equity + debt (roughly 40:60, L468); critical-mineral projects intended to be OFFTAKE-funded — management's analogy was that "graphite projects in Africa are funded by Elon Musk," who funds the mine in exchange for 10-year discounted concentrate supply (L457-459). No offtake is signed yet ("exchange of ideas… very preliminary", L462).
- Unit economics disclosed: Junagiri Q1 ~30% PAT margin on ~Rs87cr revenue (L363, L115); ~1 kg/day gold strike rate (L94); Altyn Tor first 4-5 years fed from ~6 Mt tailings at ~1.3 g/t — but management's own contained-gold figure (~780 kg, L154) does not reconcile: 6 Mt × 1.3 g/t = 7,800 kg, a 10× gap, so at least one of tonnage / grade / contained-gold is wrong (NUMBER_INCONSISTENCY, ledger N30/N36/N37). The de-risked-tailings-feed thesis rests on an unreconciled resource number. Portfolio capex philosophy: ~Rs400-500cr per standard 2,000 tpd plant, ~Rs650-700cr for the larger Balukona plant, up to ~Rs2,000cr total (L449-453). Model-drift signal this quarter: guidance shifted from specific rupee targets to volume-only ranges (the withdrawn slides).

### 4. Competition intelligence
*(Provenance: all figures from THIS QUARTER'S CONCALL; first coverage.)*

- At the Balukona nickel-copper-PGE project in Chhattisgarh, **Vedanta ("Vanta") is literally the next-door neighbour**, also exploring the same belt (L236). Vedanta appears twice: as a competitor on the ground AND as a potential customer — management expects to sell its future nickel-copper-palladium concentrate to Indian smelters "owned by big companies like Adani and Vedanta" (L235, L461). So the same peer is both rival and possible offtaker.
- Internationally, management flagged that **Chinese companies routinely counter-bid** for the licences Deccan Gold pursues ("once you make an offer, a counter offer is always given by another company, primarily… Chinese", L334) — the key competitive risk in acquiring and holding overseas ground. Tungsten scarcity is framed the same way: "majority of it is done by Chinese" (L312).
- Structural weakness vs these peers: Deccan Gold is a small company self-funding via dilution while competitors (Vedanta, Adani, Chinese majors) have balance-sheet depth. Management's stated edge is its technical exploration team and first-mover overseas licences; its stated funding answer to the size mismatch is the offtake model (the Elon Musk/graphite analogy) and, for nickel-copper, selling concentrate into the very smelters its larger neighbours own.

---

```yaml
stage: A4-analyst
company: "DGML"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
docs_merged: [concall]
ledger_reconciliation:
  notes: 95
  turns: 15
  slides: 0
  all_reviewed: true
  a3_findings_incorporated: [F1-a, F1-b, F6, F7, F10, F13, F14, F16-a, F16-b, F16-c, F17]
protocol_verdict: "PROCEED WITH CAVEATS"
cash_conversion: "INDETERMINATE"
decision_status_verified: "None (first coverage / baseline established)"
position_branch: "n/a"
sc_gap_pat_pct: ["~100% of consolidated profit uplift sits in the Geomysore associate line (Rs6.35cr equity-method); DGML standalone mining PAT ND — no filing supplied, concall-only"]
questions_for_management:
  - {q: "DGML exact equity % in Geomysore + dividend/upstreaming policy", from_finding_id: "F1-b"}
  - {q: "Will any Geomysore dividend be paid FY27; if not, when, and what is the interim cash bridge", from_finding_id: "F1-b"}
  - {q: "Why zero P&L movement on ~Rs522/520mn inventory in a production quarter; realisation timing", from_finding_id: "F1-a"}
  - {q: "Pro-forma diluted share count post Rs137cr raise + pending QIP, and terms", from_finding_id: "F10"}
  - {q: "RPT pricing/terms for management & HNI participants in the Rs137cr raise vs public shareholders", from_finding_id: "F10"}
  - {q: "Is the QIP sized/dated; ranking vs the ~Rs80 rights issue and the CCDs", from_finding_id: "F10"}
  - {q: "Q2 delivery on dated commitments: Altyn Tor commissioning, Finland Sep-15 drill, Oct-2026 LOM plans, Spain early-Oct resource model", from_finding_id: "F6"}
  - {q: "Any critical-mineral offtake actually signed (vs exchange of ideas) and with whom", from_finding_id: "F7"}
  - {q: "Will withdrawn Rs topline guidance for Junagiri/Kyrgyzstan be restored or permanently replaced by volume-only", from_finding_id: "F16-a"}
  - {q: "Reconcile realised ~30% Junagiri PAT margin to prior ~60-65%; path/timeline to 65-70% EBITDA", from_finding_id: "F16-b"}
  - {q: "FY28 production from mines OTHER than Junagiri/Kyrgyzstan", from_finding_id: "F16-c"}
  - {q: "RPT controls over DGML-Geomysore given ex-Geomysore MD on DGML board; why independent director not renewed", from_finding_id: "F13"}
  - {q: "What are the 'few more board changes expected'; will independent-director strength be restored", from_finding_id: "F13"}
monitorables:
  - {item: "Altyn Tor commissioning + first production", implied_date: "imminent (~Aug 2026)", source_ref: "L140-142"}
  - {item: "Junagiri revised in-mine resource estimate", implied_date: "Oct 2026", source_ref: "L102"}
  - {item: "Altyn Tor revised mine-design/LOM plan", implied_date: "Oct 2026", source_ref: "L150-151"}
  - {item: "Finland drilling start ~1,500m", implied_date: "Sep 15 2026", source_ref: "L190"}
  - {item: "Spain HESA full assays / preliminary resource model", implied_date: "mid-Sep / early-Oct 2026", source_ref: "L270-271"}
  - {item: "Finland 51% stake close ($1-2M)", implied_date: "this/coming quarter", source_ref: "L177-178"}
  - {item: "Shareholder approval of Rs137cr raise", implied_date: "near-term post-call", source_ref: "L61"}
  - {item: "Larger QIP sizing/timing", implied_date: "undated", source_ref: "L338"}
  - {item: "Ganajur court hearing", implied_date: "expected soon (post-July 2026)", source_ref: "L195-197"}
  - {item: "Physical AGM, Mumbai", implied_date: "this FY", source_ref: "L483-485"}
  - {item: "Inventory-realisation answer via P&L reply", implied_date: "post-call", source_ref: "L480-481"}
  - {item: "Q2 FY27 concall = decisive guidance-validation quarter", implied_date: "~Nov 2026", source_ref: "L427-428"}
flags: ["F10 stacked related-party dilution overhang (quantum undisclosed)", "F16-a guidance-slide withdrawal", "F16-b margin walk-back ~60-65% to ~30%, recovery deferred", "F1-b associate cash-conversion INDETERMINATE (dividend doubted this FY)", "F1-a static Rs522/520mn inventory, realisation deferred", "F7/F16-c non-flagship project numbers tentative/pre-drill; FY28 other-mine output unanswered", "F13 related-party director added + independent director not renewed + more board changes pending", "single-spokesperson call, no CFO voice", "OVERPROMISER-WATCH archetype (high specificity, credibility unestablished)"]
plain_language_brief_included: true
review_path: "/home/user/inflection-pipeline/runs/deccangold-q1fy27/work/review_dgml_q1fy27.md"
```
