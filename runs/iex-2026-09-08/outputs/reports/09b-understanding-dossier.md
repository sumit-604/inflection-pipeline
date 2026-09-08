# HALT 1 UNDERSTANDING DOSSIER

IEX | Indian Energy Exchange Ltd | Run date 2026-09-08 | Phase 1 evidence only

This is an understanding document. It carries no price, no exit multiple, no
fair value, and no verdict. The decision to KILL, run SHALLOW, or PROCEED is
the operator's, made after reading this dossier and signing the Mental Model
Declaration in claude.ai.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

### 1. Concalls
Three transcripts held, oldest first (B00.concall_quarter_map):
- Concall_Feb_2026_Transcript.pdf, filed 2026-02-05, Q3FY26.
- Concall_Apr_2026_Transcript.pdf, filed 2026-04-30, Q4FY26 and FY26 results, call held 24-Apr-2026.
- Concall_Jul_2026_Transcript.pdf, filed 2026-07-31, Q1FY27, the IEX Analyst Meet held 24-Jul-2026, which the company scheduled as its Q1FY27 earnings call (no separate Q1FY27 call exists).
A fourth transcript, Concall_Nov_2025_Q2FY26_Transcript.pdf, sits in inputs/other/ rather than inputs/concalls/, per the collector's 0-3 contract for the concalls/ folder, but was read and cited throughout the pipeline (B00.inventory, B05).
Most recent quarter covered: Q1FY27 (call 24-Jul-2026). Run date is 2026-09-08. Q2FY27 results are not yet due (typically late October), so no more-recent-quarter transcript is plausibly missing.

### 2. Annual reports
Two years held: Annual_Report_2026.pdf (FY26, primary) and Annual_Report_2025.pdf (FY25, comparative), each with the prior year's comparative balance sheet inside, extending the numeric window to FY24 (B01.run_note). The latest completed FY (FY26) is present. Only two AR PDFs are held, short of the "at least 3 years held" bar as a document count, though the FY24 comparative figures inside Annual_Report_2025.pdf partially substitute for a third full AR (B01).

### 3. Results filings
Three held: Q1FY27_Results_Unaudited_2026-07-23.pdf and its press release (board-approved 23-Jul-2026), and FY26_Q4_Audited_Results_2026-04-23.pdf. The latest results filing (Q1FY27) is newer than the latest AR's cover date is not the relevant test; the relevant test is that the AR (filed 14-Aug-2026) is not older than the latest audited annual results (FY26, audited results 23-Apr-2026) — it is not (B00.freshness_pairs, pair 4, PASS). No quarter-gap: Q1FY27 is the newest results filing and Q1FY27 is also the newest concall.

### 4. Investor presentations
Two held: Investor_Presentation_Analyst_Meet_2026-07-24 and Investor_Presentation_Q4FY26_2026-04-23. The most recent is the 24-Jul-2026 Analyst Meet deck, same date as the newest concall.

### 5. Research / rating
None held. inputs/rating/ and inputs/research/ are both empty. This is NOT a collection gap for rating: IEX carries only Rs11.16cr of Ind AS 116 lease liabilities, told BSE on 13-Apr-2026 it does not qualify as a Large Corporate, and has no listed debt, so no CRISIL/ICRA/CARE rating exists to collect (B00.input_gaps, B01.input_gaps). Broker research notes are absent and would in any case be non-anchored leads only (B00, B01).

### 6. Corporate actions
Thirteen announcement filings held, spanning the IGX DRHP filing intimation (15-Jul-2026), the Indian Coal Exchange incorporation (01-Jun-2026), four monthly Power Market Update filings (Mar-2026, Jun-2026, Jul-2026, Aug-2026), the rumour verification reply (20-Apr-2026), the BRSR, the secretarial compliance report, the FY26 Q4 press release, two scanned SAST Regulation 29(2) disclosures with no extractable text (21-Apr-2026, 10-Jun-2026), and the Large Corporate non-qualification letter (13-Apr-2026) (B00.inventory). Date range: roughly Mar-2026 to Aug-2026.

### 7. Freshness pair check
B00.freshness_verdict is CORPUS GAPPED-FRESHNESS. Of the four pairs (B00.freshness_pairs):
- Results to concall: PASS. Q1FY27 results (23-Jul-2026) mate to the Q1FY27 Analyst Meet transcript (24-Jul-2026, filed 31-Jul-2026).
- Rating bulletin to rationale: NOT_APPLICABLE. No rated debt, no bulletin exists to trigger the pair.
- Referenced regulatory order to order text: FAIL. The trigger document is the company's own rumour verification reply of 20-Apr-2026, which cites the CERC market coupling order and a CERC draft notification. The mate expected is the CERC market coupling order text, the APTEL judgment of 13-Feb-2026, and the two Supreme Court orders of 11-May-2026 and 27-Jul-2026. None of these four texts is present in the corpus, though all four are referenced repeatedly across the AR (Note 47 p.224), the concalls, and the rumour verification reply itself. This is the single highest-priority gap named across every stage report (B01, B03, B04, B05, B06, B07, B08, B09 all carry it at severity HIGH). The operator was asked at stage 0 and answered "proceed with the gaps."
- AR to latest audited annual results: PASS. Annual_Report_2026.pdf (filed 14-Aug-2026) does not trail FY26_Q4_Audited_Results_2026-04-23.pdf.

### 8. Verdict line

**CORPUS GAPPED-FRESHNESS.** Missing mate: the CERC market coupling order text, the APTEL judgment of 13-Feb-2026, and the two Supreme Court orders of 11-May-2026 and 27-Jul-2026 — findable-but-missing, expected source: CERC official notifications, the APTEL judgment record, and the Supreme Court of India cause list and order record. Other gaps carried under this verdict, all findable-but-missing unless stated otherwise:
- A CERC staff paper of December 2025, "Review of Transaction Fee charged by the Power Exchanges," proposing a fixed 1.5 paise/unit fee against the current ~2 paise ceiling. Found only by Stage 9's own web search; entirely absent from the corpus and unmentioned in any corpus document. Expected source: CERC official notifications.
- The Coal Rules text (Ministry of Coal notification barring e-auction platforms from operating six months after the coal exchange launches), referenced only by management's verbal characterisation (B05). Expected source: Ministry of Coal / Coal Controller Organization notification.
- Any CCO licence grant naming IEX for the Coal Exchange (B07.input_gaps). Expected source: Ministry of Coal / CCO notification.
- IGX OFS cash proceeds and price band: NOT FOUND anywhere in the corpus even after a full AR read (B01, B04). Expected source: the full IGX DRHP (held by the book-running lead managers, not collected) or a future exchange filing.
- PXIL and HPX individual FY26 volume/revenue disclosures (B09) — plausibly-nonexistent as public filings for unlisted competitor exchanges; IEX's own aggregate 80-85% share figure is the only disclosed cross-check.
- Named >1% shareholder register from the shareholding-pattern XML files: present in the corpus but not extractable with the tools available this run (B08.input_gaps); a tooling gap, not a collection gap.
- Two SAST Regulation 29(2) disclosures (21-Apr-2026, 10-Jun-2026): held but scanned images with no extractable text; OCR would resolve this without a new document.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** This declaration is not signed. Signing
happens only in claude.ai after live-web stress-testing. Nothing below marks
it approved.

### PART A — THE FROM STATE

**A1. Archetype.** Platform/network, with a licence/scarcity overlay, per line:
- Electricity exchange (DAM/RTM/TAM/Green), 91.7% of standalone revenue: platform/network archetype, licence/scarcity overlay (CERC-regulated exchange licence, one of a small named set).
- Certificates (REC/ESCerts), 4.2% of standalone revenue: platform/network archetype, but the licence/scarcity overlay is weakening (REC volume down 56.3% to 92.3% YoY across every disclosed FY27 month).
- Membership/subscription fees, 3.9%: recurring-subscription tail on the same platform, not a distinct archetype.
- Treasury income, 20.4% of standalone total revenue: not an archetype at all — a bond-fund return on the investment book, explicitly labelled "Treasury Income" in the company's own MD&A KPI table (AR p.64; B04.flags).

**A2. The simple analogy.** IEX is a marketplace where power plants and electricity buyers post prices on a screen, and a computer matches the best offers once a window closes. IEX never owns or delivers a single unit of electricity. It only runs the matching engine and takes a small fee, about 4 paise for every unit of power that clears through it, whichever side of the trade wins. Roughly 8 out of every 100 units of electricity used in India today are bought this way rather than through a long-term contract, and IEX clears 80 to 85 percent of that traded slice. The company holds no inventory, carries almost no debt, and its biggest single asset by far is a large, low-risk investment portfolio built from two decades of accumulated profit.

### PART B — THE TRANSITION

**B1. From to to, per line.**
- Electricity exchange (DAM+RTM+TAM+Green): FROM R4 FRANCHISE / SHARE-OF-WALLET LEADER (a near-monopoly liquidity pool with switching-cost lock-in and near-30% standalone margins on the transaction-fee line) — the tier the DAM franchise has occupied historically. TO an unresolved position between R3 VALUE-ADDED / SPEC'D SUPPLIER and R2 COST-ADVANTAGED CONVERTER on the DAM slice specifically, as CERC-ordered market coupling removes IEX's price-discovery role and turns DAM from a franchise the exchange owns into a bid-collection function it shares with a coupling operator. RTM and TAM, not yet coupled, sit closer to holding R4.
- Certificates (REC/ESCerts): FROM a thin R2/R3 slice already (4.2% of revenue, historically volatile) — no meaningful franchise ever built here. No clean TO state is evidenced; volume collapse (-56% to -92% YoY every FY27 month) reads as contraction, not transition, and this line fits no rung cleanly at present.
- Treasury income: not on the ladder. It is not an operating line and carries no rung.

**B2. The engine.** Two things physically change the DAM slice from franchise to shared-utility: (1) Grid India replaces IEX as the point of price discovery under CERC's coupling order, so the same bid IEX used to clear alone now clears through a shared national order book; (2) the mix shift already under way — DAM down from 95% of volume in FY16 to 39% in FY26, RTM up to 34% and growing 41% YoY in FY26 — moves the revenue base toward segments (RTM, TAM) that are not yet coupled and where management's own four-year TAM precedent shows a stable ~3.6-3.7 paise net fee even under three-way liquidity sharing (B04.analyst_note).

**B3. The proof gate.** The hard binary metric: two consecutive quarters in which electricity transaction-fee revenue growth equals or exceeds electricity traded-volume growth, computed from the standalone revenue note and the monthly Power Market Update volume series. As of the most recent evidence, this has not fired even once — revenue growth has trailed volume growth in every period on record (B02.top_findings rank 5; B04.must_track_metrics), and blended fee realisation fell from 4.33 to 4.16 paise/unit between Q1FY26 and Q1FY27 (a figure derived from filed revenue and volume, not itself printed anywhere — see Section 6, Q1). Until this gate fires, the "mix shift protects the franchise" claim is management narrative, not demonstrated fact.

**B4. The recognition gap (open question, resolved at Stage 11).** Whether the market has already priced in the coupling threat to DAM, the possibility that RTM/TAM growth fully offsets it, or some blend of the two is not established by this evidence base. Stage 11 resolves this via the PE gap between the current multiple and the Section 1B destination multiple implied by whichever rung the business actually occupies once the proof gate is tested. No number or conclusion is stated here.

**B5. The ugliness test.** Today's ugly optics — day-ahead volume declining outright in June (-6.6%) and July (-7.7%) 2026, fee realisation compressing, REC volume collapsing 56-92% YoY, and the rising non-operating share of profit (23.4% to 29.8% of PBT) — split into two different classifications and must not be merged:
- The DAM volume/fee pressure directly tied to coupling is best read as STRUCTURAL-FEATURE, not ARTIFACT-OF-CLIMB, on current evidence: it is the mechanical, ordered consequence of a regulator removing IEX's price-discovery role, not a temporary cost of an ascent to a higher tier. The evidence does not show a "climb" in progress on this slice; it shows a franchise function being reassigned.
- The REC collapse is a separate, unrelated ugliness with no franchise-migration story attached at all; it reads as plain deterioration, also STRUCTURAL on the evidence to date (the "buyer confusion" explanation management gives is contradicted by the company's own filed seller-side data, B05.red_flags).
- The rising non-operating PBT share is a reporting-composition fact, not itself ugly or a climb signal; it is flagged separately as FLAG-NON-OPERATING-EARNINGS.
No dominant variable in this evidence base currently supports classifying the ugliness as a temporary artifact of an ascent.

**B6. The transition falsifier.** Two consecutive quarters of DAM volume decline running concurrently with fee realisation below 4.10 paise/unit, with no offsetting acceleration in RTM/TAM revenue growth above their own recent trend, would falsify any thesis that the mix shift protects revenue as coupling proceeds. This is distinct from what would kill the business itself (Part C3).

### PART C — WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from B2 the engine and B3 the proof gate):
- Day-ahead volume, YoY, from the monthly Power Market Update. Current state: down 6.6% (June 2026) and 7.7% (July 2026), the exact segment coupling threatens (B05.triggers priority 2).
- Blended electricity fee realisation (revenue ÷ volume, derived, never printed). Current state: 4.16 paise/unit Q1FY27 against 4.33 a year earlier, drifting toward the 3.6-3.7 paise TAM blended rate (B05.triggers priority 3).
- RTM (and TAM) volume growth as the offsetting mix-shift engine. Current state: RTM guided at 25-30% forward growth but printed 10.2% (July) and 10.6% (August) 2026 (B05.promise_delivery, falsified).
- Supreme Court / final CERC coupling regulation outcome. Current state: appeal admitted 11-May-2026, interim stay refused 27-Jul-2026; no final regulation or ruling yet (B05.triggers priority 1).

**C2. What the model rejects.** Total addressable market size for Indian electricity generation is noise here: the binding constraint on the core electricity line is not market size (short-term power trading already has a large, growing, externally-verifiable pool, B09.tam_growth_pct 8.9%) but execution against a regulator actively redesigning the market structure and, separately, the fee cap. Coal Exchange tonnage claims (80mn to 120mn, revised ~50% without a bridge) are similarly not the binding question until a per-tonne fee and an IEX-specific licence exist (B09, B07). Sizing questions about the coal, gas, and carbon option pools are aspirational until conversion evidence (licence award, disclosed fee schedule) appears; the model treats them as optionality, not as load-bearing revenue.

**C3. The business falsifier** (distinct from B6, the transition falsifier). Evidence that would force re-declaring the FROM business itself, not just the transition: a final CERC coupling regulation or Supreme Court ruling that extends coupling to RTM and TAM as well as DAM, removing IEX's price-discovery role across the entire electricity franchise rather than one slice of it. RTM coupling is currently deferred "to a later stage" per CERC (B07.top_moat_risks); if that deferral does not hold, the FROM-state franchise itself, not just its DAM slice, is gone.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

(Drafted per the five-question spec in prompts/13-synthesis-pipeline.md; Stage 13's copy is the version of record and may be updated by later stages.)

IEX runs India's power exchange and never owns an electron. The product is a
matched trade. A generator or a distribution utility puts a bid on the screen,
the matching engine clears one price for that time block, the load despatch
centre confirms the schedule, and IEX invoices a fee of about 4 paise per unit
traded. Electricity transaction fees are 91.7 percent of standalone revenue,
certificate fees on renewable energy certificates are 4.2 percent, and annual
membership and subscription fees are 3.9 percent, so the electricity line is
the only stream above 10 percent and is the business. Treasury income is a
further 20.4 percent of standalone total revenue, and the company labels it
treasury income in its own metrics table; it is a return on the investment
book, not a second product line (B04, AR p.64).

The customers are state and private distribution utilities, generators,
traders and commercial and industrial open access buyers, about 9,000
registered participants in all. They stay because settlement, margining and
back office systems are wired into the venue, with over 70 percent of cleared
day-ahead volume arriving through bidding APIs, though one unnamed customer
was 16.2 percent of FY26 revenue against 15.65 percent the year before
(B02.top_findings rank 9, AR Note 28 p.211).

Demand today comes from India's short-term power market, the slice of
electricity bought outside long-term power purchase agreements, and two
external series report it every month: the CERC Short-Term Power Market
report and the CEA generation and demand-met data (B09.downstream_candidates).
Exchange-traded volume is about 8 to 9 percent of national consumption, and
IEX cleared 141 BU of electricity in FY26, up 16.9 percent (B04, B09).

Demand should grow for two reasons an outsider can check without the
company. India added non-fossil generation capacity through FY26, and
intermittent output needs a short-term market to balance it, which is what
the real-time segment does (B04.moats_present D2; B07 D2). Procurement is
also shifting off long-term power purchase agreements toward exchange
buying, and the same two monthly reports track that shift (B09.tam_growth_pct
8.9%, revenue_headroom_x 1.65).

The competitive advantage is not the same on every line. The real-time line
holds the strongest position, with customer ecosystem, digital platform
lock-in through APIs, regulatory first-mover status and the war chest all
scoring Strong in the emerging-moat scan (B07.active_categories C1, D2, E1,
G1). The day-ahead line is the one under attack, because coupling moves
price discovery to a shared operator and the liquidity network effect that
built day-ahead is the exact thing coupling neutralises (B04.flags; B07).
The certificate line has no moat worth naming: REC volume fell 81.4 percent
year on year in Q1FY27 and 86.6 percent in August 2026 (B05).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1 — Day-ahead volume and fee realisation under coupling.**
The corpus establishes: day-ahead is 39% of FY26 volume, down from 95% in
FY16 (B04, AR p.17/25/62); day-ahead volume fell 6.6% (June 2026) and 7.7%
(July 2026) YoY (B04, monthly Power Market Updates); blended electricity fee
realisation fell from 4.33 to 4.16 paise/unit (Q1FY26 to Q1FY27, derived, B02);
management's only quantification of coupling's DAM impact is a verbal 20-40%
range given once and effectively withdrawn in the same call (B05.red_flags).
It cannot establish: the actual CERC order text, the final coupling regulation
terms, or any rupee quantification of the exposure, because none of those
texts is in the corpus. Questions that decide it: (1) Does the final CERC
coupling regulation extend beyond DAM to RTM/TAM? (2) What does the Supreme
Court rule, and on what timeline? (3) Does day-ahead fee realisation stabilise
above 4.10 paise/unit once two more monthly prints are in?

**Vertical 2 — RTM/TAM as the offsetting engine.**
The corpus establishes: RTM is 34% of FY26 volume and grew 41% YoY in FY26
(B04); RTM growth guided at 25-30% forward but printed 10.2% (July) and 10.6%
(August) 2026 (B05.promise_delivery, missed); TAM's four-year precedent shows
a stable ~3.6-3.7 paise net fee under three-way liquidity sharing (B04.
analyst_note, Concall Apr-2026 p.15). It cannot establish: whether the RTM
deceleration is a temporary base-effect (FY26's 41% was itself unusually
high) or the start of a structural slowdown, because no independent volume
driver (weather, renewable intermittency, BESS arbitrage economics) is broken
out separately in the corpus. Questions that decide it: (1) Does RTM growth
return to 20%+ in a subsequent monthly print? (2) Does CERC rule on the three
pending petitions (Green RTM, Peak DAM/RTM, 11-month TAM), each "order
reserved" for 2+ years? (3) Is BESS merchant-flow arbitrage (cited by
management as a driver) sustainable at its current 4-5 rupee/cycle spread?

**Vertical 3 — Non-operating share of profit.**
The corpus establishes: other income Rs131.30cr plus IGX equity pickup
Rs19.80cr equals Rs151.10cr, 23.4% of FY26 consolidated PBT, rising to 29.8%
in Q1FY27 (B02.top_findings rank 5); this rise was never raised by management
or any analyst across four calls, and the peer check found the same blind
spot at MCX, BSE and CDSL (B06.verified). It cannot establish: whether the
treasury book's composition (recently reallocated away from target-maturity
plans into equity-index funds with no stated rationale, B02.top_findings rank
12) implies a deliberate change in risk appetite that could make this income
line more volatile going forward. Questions that decide it: (1) Does the
non-operating share sustain above 25-30% for two more quarters? (2) What
drove the FY26 treasury reallocation? (3) Does the investment book's risk
profile show up in a future MTM swing?

**Vertical 4 — Coupling litigation and regulatory outcome.**
The corpus establishes: APTEL dismissed IEX's appeal for want of standing on
13-Feb-2026; the Supreme Court admitted the appeal 11-May-2026 and refused an
interim stay 27-Jul-2026 (B04, B05, B07.catalysts_12m). It cannot establish:
the substance of any of these rulings, because none of the four order/
judgment texts (CERC order, APTEL judgment, two Supreme Court orders) is in
the corpus — this is the corpus's single highest-severity gap. Questions
that decide it: (1) What does the Supreme Court rule, and on what timeline?
(2) Does the final CERC regulation extend coupling to RTM/TAM? (3) What does
the December 2025 CERC fee-review staff paper (found only by web search,
absent from corpus) resolve to on the per-unit fee cap?

### 4b. Candidate signal table

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| CERC Short-Term Power Market report | STM volume growth falls below 10% for 2+ consecutive months | Monthly | CERC Market Monitoring Division official reports |
| CEA generation and demand-met data | Total generation growth decelerates sharply against the STM growth assumption underlying SOM | Monthly | Central Electricity Authority reports |
| CERC market-coupling final regulation / Supreme Court case status | Coupling extended to RTM/TAM, or ruling adverse to IEX with no cushioning terms | Event-driven | CERC official notifications; Supreme Court of India cause list |
| CERC transaction-fee review final order | Fixed fee set at or near the proposed 1.5 paise/unit (vs current ~2 paise ceiling) | Event-driven | CERC official notifications |
| Coal India Ltd monthly e-auction/SWMA allocation data | Coal India's own e-auction run-rate falls materially below the 100-120 MT range management cites for IEX's Coal Exchange | Monthly | Coal India Ltd investor disclosures |
| Ministry of Coal / Coal Controller Organization licence award | Licence delayed, shared, or denied to IEX specifically | Event-driven | Ministry of Coal / CCO official notification |
| Day-ahead volume YoY (monthly Power Market Update) | Two more consecutive months of outright decline | Monthly | BSE/NSE Regulation 30 filings, company IR page |
| Blended electricity fee realisation (derived) | Drift below 4.10 paise/unit for two consecutive quarters | Quarterly | Company results filings, standalone revenue note |
| Non-operating share of consolidated PBT | Sustained above 25-30% for two consecutive quarters | Quarterly | Company results filings, other income + associate pickup lines |
| REC sell-bid volume and clearing price | Sell bids remain collapsed (near -80%+ YoY) for two more monthly sessions with prices still rising | Monthly | Power Market Update filings |
| Whistleblower investigation resolution | Any FY27 disclosure of findings or closure resolving the Board's Report vs Notes/CARO status conflict | Event-driven / next AR cycle | Company quarterly notes, FY27 annual report |
| IGX OFS completion and proceeds | IPO delayed past the 31-Dec-2026 PNGRB deadline, or priced at a steep discount to carrying value | Event-driven | BSE/NSE filings, SEBI DRHP tracker |

### 4c. Fragility read

- variable_count: 4 (the Section 2 C1 dominant variables: day-ahead volume, fee realisation, RTM/TAM offsetting growth, coupling/Supreme Court outcome).
- verifiability_ratio: 3 of 4 externally observable (day-ahead volume and RTM/TAM growth via monthly Power Market Update filings; the coupling/court outcome via CERC notifications and the Supreme Court cause list); fee realisation is derived from company-filed revenue and volume, not itself company-narrated, but requires the company's own filed numbers rather than an independent series, so it sits between the two — counted here as externally computable but company-sourced.
- single_point_failure: the Supreme Court / final CERC coupling regulation outcome. An adverse ruling that extends coupling beyond DAM to RTM/TAM would remove the offsetting engine (B2/B3) entirely and would also trip the business falsifier (C3), not merely the transition falsifier (B6). No other single variable in this set does both.
- fragility_verdict: **FRAGILE**. One variable (the coupling/court outcome) can break both the transition thesis and, in its most adverse form, the FROM business itself; a second (fee realisation) is already trending the wrong way with no management reconciliation across three quarters of direct questioning; and the corpus holds none of the four texts (CERC order, APTEL judgment, two Supreme Court orders) that would let a reader assess the outcome directly rather than through management's own account, which carries a D credibility grade.

### 4d. Research brief

Numbered live-web work for claude.ai, the claude.ai work order:
1. Retrieve and read the CERC market-coupling Suo Motu order of 23-Jul-2025 in full.
2. Retrieve and read the APTEL judgment of 13-Feb-2026 dismissing IEX's appeal for want of standing.
3. Retrieve and read the two Supreme Court orders (admission, 11-May-2026; stay refusal, 27-Jul-2026), and check the current cause-list status of the appeal.
4. Retrieve the CERC staff paper "Review of Transaction Fee charged by the Power Exchanges" (Dec-2025) and assess its current regulatory status (draft, comment period, finalised).
5. Retrieve the Ministry of Coal notification on the incumbent e-auction-platform exclusion mechanism management calls the "Coal Rules," and verify management's characterisation of it.
6. Check whether the Coal Exchange licence has since been awarded, and to whom.
7. Search for the identity of the acquirer(s) in the two unreadable SAST Regulation 29(2) disclosures (21-Apr-2026, 10-Jun-2026); OCR the two source PDFs if a direct read is unavailable.
8. Search for IGX DRHP proceeds/price-band disclosures once the full (non-abridged) DRHP becomes available from the book-running lead managers.
9. Search for PXIL and HPX individual FY26 volume/revenue disclosures, if any exist publicly, to cross-check IEX's aggregate 80-85% market-share claim.
10. Search for any rating-agency or proxy-advisory (IiAS/SES/InGovern) commentary on IEX specific to the whistleblower status conflict or the market-coupling exposure, since none was found in this run's searches (B08.searches_skipped).
11. Confirm the resolution of the whistleblower investigation status conflict once the FY27 quarterly notes or AR are available.
12. Verify, from CERC/Grid India public materials, whether the pilot coupling run Grid India described in the Jul-2026 call ("four months period... run this pilot") predates or postdates management's Nov-2025 statement of "not aware about any developments" — the contradiction B12b flagged as unresolved.
13. PENDING LIVE VERIFICATION items named in Section 4e below, chains 1 and 2.

### 4e. Second-order stub

Rule F sets a floor of five chains for Role 2, Role 6, and FTTCP. This is a stub of two, drafted from corpus, to be extended to five with live web in claude.ai.

```
CHAIN 1: CERC ordered day-ahead market coupling with Grid India as coupling
operator (B04.flags; AR Note 47 p.224); day-ahead volume fell 6.6% (June
2026) and 7.7% (July 2026) YoY (B04, monthly Power Market Updates).
Link 1 [documented]: IEX's own fee-realisation drift (4.33 to 4.16
paise/unit, Q1FY26 to Q1FY27, derived from filed revenue and volume; no
printed realisation figure exists anywhere in the corpus, Section 6 Q1) sits
in the same two quarters as the day-ahead volume decline.
Link 2 [documented]: The AR itself gives zero rupee quantification of the
coupling exposure in the audited Notes (Note 47/53), while a much smaller
Rs5.04cr GST dispute (Note 39) receives a full quantified assessment
(B02.top_findings rank 2) — a materiality-judgement gap the annual report
itself does not explain.
Link 3 [INFERENCE]: If day-ahead fee revenue is falling faster than day-ahead
volume (a realisation-times-volume decomposition this corpus's aggregate
figures do not separate cleanly), the company may be facing early
price-competition pressure on DAM even before the coupling regulation is
finalised, which would mean the "franchise erosion" is already under way
ahead of the regulatory event everyone is watching for.
Binding constraint: whether Grid India, as coupling operator, sets terms that
let IEX retain its current fee on coupled DAM volume, or forces fee
competition. This is a regulatory design choice not yet made public in any
text this corpus holds.
Unsaid: management has never, across four quarters of direct questioning,
named the mechanical driver of the fee-realisation decline (B02.top_findings
rank 5's rupee bridge notwithstanding, the per-unit driver itself is
unstated); the closest connection anyone draws is B04's own analyst note
that TAM's stable 3.6-3.7 paise blended rate under three-way liquidity
sharing is a management-favourable precedent, never invoked by management
itself in this context.
Observation that confirms or breaks this chain, and confirm-by date: blended
electricity fee realisation from the Q2FY27 results filing (due late
October 2026, per the gate recommendation's falsification line). Below 4.10
paise/unit with day-ahead volume again down YoY confirms the chain; a
recovery above 4.20 paise/unit with day-ahead volume flat or up breaks it.
[PENDING LIVE VERIFICATION: whether Grid India has published any coupling
pilot terms sheet or draft operator agreement bearing on fee-sharing; open
this specifically at CERC's official notification page and any Grid India
market-coupling pilot documentation.]

CHAIN 2: Management's own promise record on forward guidance carries a
credibility grade of D (B05.credibility_grade, B12b concurring at "D or a
low C"), with RTM growth guided at 25-30% (Q1FY27 p.29) and printed at 10.2%
(July) and 10.6% (August) 2026 (B05.promise_delivery, missed).
Link 1 [documented]: The REC volume-decline explanation management gives
(buyer-side "confusion," Q3FY26 p.8 and Q1FY27 p.41) is directly contradicted
by the company's own filed Power Market Update three weeks earlier, which
reports sell bids down 86.1% YoY with clearing prices rising — a seller-side
failure, the opposite diagnosis (B05.red_flags, HIGH).
Link 2 [documented]: All three of IEX's 2023 product launches (HP-DAM,
HP-TAM, Ancillary Market) are management-admitted failures for want of
liquidity (Concall Jul-2026 p.12, per B12b MAJOR finding #3), and the growth
case for three further pending launches (Green RTM, Peak DAM/RTM, 11-month
TAM) rests on the same company that has not yet delivered a successful new
product launch since listing.
Link 3 [INFERENCE]: If the base rate for IEX's own product launches is
"illiquid and does not scale" (three-for-three so far), the pending-product
optionality register (B07) should be discounted materially below its
face-value framing in management's own commentary, independent of whether
coupling resolves favourably or not.
Binding constraint: whether liquidity, not regulatory approval, is the
actual constraint on new-product success — CERC approval alone (Green RTM,
Peak DAM/RTM, 11-month TAM all "order reserved" 2+ years) does not itself
solve the liquidity problem the three 2023 launches ran into.
Unsaid: no B05 or B07 row connects the three-for-three launch-failure base
rate to the discount rate the pending-launch optionality should carry;
B12b flagged this as a MAJOR under-weighting.
Observation that confirms or breaks this chain, and confirm-by date: whether
any one of Green RTM, Peak DAM/RTM, or the 11-month TAM contract, once
approved, shows traded-volume liquidity above a de minimis threshold within
two quarters of launch (no fixed date; watch for the next CERC order on any
of the three pending petitions, then track two quarters forward from
launch). [PENDING LIVE VERIFICATION: whether CERC has issued any order on
the three pending petitions since this corpus's cutoff; open CERC's official
notification page directly.]
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in
claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. IEX runs the screen where Indian power buyers and sellers post prices and get matched. It never owns or delivers electricity itself.
2. It earns a small fee, about 4 paise for every unit of power that clears on its platform, no matter which side wins the trade.
3. It clears roughly 80 to 85 percent of all electricity traded on an Indian exchange today.
4. Buyers and sellers are utilities, generators, traders, and large industrial power users, about 9,000 registered members.
5. They stay largely because their back-office and settlement systems are wired into IEX's platform, and switching means rebuilding that link.
6. One unnamed customer supplied 16.2 percent of FY26 revenue, up from 15.65 percent the year before; its identity and staying power are not known.
7. Demand for exchange-traded power grows as more renewable power comes online, because renewable output is unpredictable and needs a short-term market to balance it.
8. Demand also grows as utilities buy more power on the open market instead of locking it into long contracts, a shift that can be checked from government data every month.
9. Real-time trading is IEX's strongest position today, growing fast and outside the regulator's coupling order for now.
10. Day-ahead trading, historically IEX's core business, is the part under direct regulatory attack: a coupling order moves price-setting to a shared national operator, and day-ahead volume has already started falling.
11. Certificate trading, a much smaller line, has almost no advantage left; volumes have collapsed by more than half in every month reported this year.
12. The one big open question is whether growth in real-time and other segments can make up for what coupling takes away from day-ahead; the evidence so far says the fee earned per unit is already sliding, and nobody, including management, has fully explained why.
13. Taken together, the evidence base for this thesis is fragile: one regulatory and court outcome can break both the growth story and, in its worst form, the historic core business, and the company's own account of events carries a weak credibility grade.
14. The corpus could not establish what the actual coupling order, court judgments, or a newer proposed fee cut say in their own words; none of those texts was collected, only references to them.
15. The two biggest open questions this dossier leaves unanswered: what the Supreme Court and the final coupling rules actually decide, and whether income from IEX's cash and investment holdings, now nearly a third of one recent quarter's profit, is being counted the same way an operating fee is.

---

## SECTION 6: STANDING EXTRACTION ANNEX

### 1. Units

Two per-unit figures are printed, from a management answer, not from an
audited exhibit:

> "Against INR 0.04 (four paise), I think the margin is around (3.6 or 3.7
> paisa) INR 0.036, INR 0.037. That's the kind of number."
(Concall_Apr_2026_Transcript.txt, p.15, answer to a post-coupling hypothetical
about Term Ahead Market fee resilience.)

Comment: this covers the Term Ahead Market product specifically, not the
whole electricity basket, and it is a verbal management estimate, not an
audited figure.

No blended electricity-wide realisation figure (paise/kWh) is printed
anywhere in the corpus, in any filing, presentation, or transcript. It must
be derived. The volume and revenue lines it derives from:

> "Electricity (comprising RTM, DAM, TAM, Green Segments) 55,851.37" (lakh
Rupees, FY26) / "47,833.81" (FY25)
(Annual_Report_2026.pdf, standalone Note 28, p.211, "28. Revenue from
operations")

> "the Company cleared 141 BU of electricity in FY26" (paraphrase of the
volume series relied on by B04/B09; the underlying billion-unit figures sit
in the monthly Power Market Update filings and the AR's own volume tables,
AR p.4, p.17, p.25)

Comment: dividing Rs558.5137cr (Note 28, Electricity segment, FY26) by 141
BU gives approximately 3.96 paise/kWh for FY26, the DERIVED figure B04 and
B09 both carry. No comparable per-unit figure for Q1FY26/Q1FY27 (4.33 vs
4.16 paise) is printed in any filing; it is likewise derived from filed
standalone revenue and volume by the pipeline, not by the company.

### 2. Segment capital and debt

> "The Company is a power exchange. The entire operations are governed by
> similar set of risk and returns... Thus, the Company has only one
> operating segment, and no reportable segments in accordance with Ind AS
> 108 - Operating Segments."
(Annual_Report_2026.pdf, standalone Note 44 "Operating segments", p.216)

> "The Company does not have any debt outstanding as on 31 March 2026 and 31
> March 2025."
(Annual_Report_2026.pdf, standalone Note 43 "Capital Management", p.215-216)

Comment: no segment-level assets, liabilities, capital employed, or
borrowings allocation exists because IEX discloses a single reportable
segment under Ind AS 108. Total borrowings are Rs11.16cr, entirely an Ind AS
116 lease liability (B01, B04), unallocated by definition since there is
nothing to allocate against.

### 3. Guidance versus aspiration

(a) Guidance with a period:
> "electricity volume growth of 15-20% every year"
(Concall_Feb_2026_Transcript.txt p.6, repeated Concall Q3FY26 p.11, Concall
Q4FY26 p.13; per 05-concall.md guidance table.)

> "gas exchange (IGX) volume growth of 25-30%... next 4-5 years"
(Concall_Feb_2026_Transcript.txt p.13, i.e. Q3FY26 call; per 05-concall.md.)

(b) Aspiration without a firm period:
> "TAM long-duration product market size, additional 15-20 billion units"
(Q3FY26 call, p.13; per 05-concall.md.)

> Coal exchange opportunity: "about 80 million tonnes" (Q4FY26 call, p.5-6),
restated to "almost about 120 million tonnes" (Q1FY27 call, p.5 and p.31),
against a colleague's own figure in the same Q1FY27 session of "70-80
million tonnes" for incumbents (Q1FY27 call, p.7).

(c) Capacity or capability only:
> "over 70% of I-DAM cleared volume routed via API; more than 50% via
back-office API"
(Concall_Jul_2026_Transcript.txt, per B05.guidance, basis restated from a
prior quarter's ">70% of cleared volume" framing — a capability statement
about current infrastructure, not a forward commitment.)

Comment: the coal-exchange figure moved roughly 50 percent between two
calls nine weeks apart with no bridge given, and was internally
inconsistent within the same session (B05.red_flags MEDIUM; B12b MAJOR
finding #6 on citation precision, substance not disputed).

### 4. Concentration

> "Revenue amounting to ₹9,862.24 (31 March 2025: ₹8,379.07) which is more
than 10% of total revenue is attributable to single customer."
(Annual_Report_2026.pdf, standalone Note 28, p.211; figures in Rupees lakh,
i.e. Rs98.62cr FY26 against Rs83.79cr FY25.)

Comment: this computes to 16.2% of FY26 revenue from operations (Rs608.39cr
standalone) against 15.65% FY25 (B02.top_findings rank 9). The customer's
identity is NOT DISCLOSED anywhere in the corpus; the AR gives only the
rupee figure and the ">10%" threshold language, no name, sector, or contract
term. Geography concentration: NOT DISCLOSED in a segment sense — IEX
operates a single national market and does not disclose a geographic
revenue split. Product concentration is disclosed only as the two-way
Electricity-vs-Certificates revenue split in the same Note 28 (Rs558.51cr
vs Rs25.45cr FY26); no DAM/RTM/TAM/Green revenue-basis split exists anywhere
in the corpus, only volume shares (B04.input_gaps, B07.input_gaps).

### 5. Promise ledger

| Promised in | Promise | Delivery status | Evidence anchor |
|---|---|---|---|
| Concall_Feb_2026 (Q3FY26) p.7 | APTEL verdict within a month | DELIVERED (timing only) | APTEL order issued 13-Feb-2026, roughly two weeks after the call |
| Concall_Feb_2026 (Q3FY26) p.7 | "Things will definitely go in our favour" (substantive half) | MISSED | APTEL dismissed IEX's appeal for want of standing 13-Feb-2026; CERC then issued draft coupling regulations 17-Apr-2026 |
| Concall_Apr_2026 (Q4FY26) p.13 | 15-20% volume growth for FY27 | DELIVERED | Q1FY27 volume landed +15.9%, inside the band |
| Concall_Feb_2026 p.4-5 / Concall_Apr_2026 p.6 | Dividend policy, interim then final, ~50-65% payout | DELIVERED | Rs1.5 interim, Rs2 final declared as stated |
| Concall_Apr_2026 (Q4FY26) p.10 | CFO treasury-income recovery ("numbers going back to the earlier numbers") | DELIVERED | Standalone other income Rs22.11cr (Q4FY26) to Rs44.92cr (Q1FY27) |
| Concall_Feb_2026 p.12 | IGX IPO within the year | PARTIAL | DRHP filed 14-Jul-2026; not yet listed; CMD "not really fully aware" of exact status on the intervening call |
| Concall_Feb_2026 p.7-8 | REC volume to end FY26 better than FY25 | PARTIAL | FY26 REC volume +5% YoY, barely ahead |
| Concall_Jul_2026 (Q1FY27) p.29 | RTM growth of 25-30% going forward | MISSED | Jul-2026 RTM +10.2% YoY, Aug-2026 +10.6% YoY |
| Concall_Feb_2026 p.8, reasserted Concall_Jul_2026 p.41 | REC weakness is transitory ("confusion will clear") | MISSED | Q1FY27 -81.4% YoY, Aug-2026 -86.6% YoY; company's own seller-side filed data contradicts the buyer-side excuse |
| Concall_Apr_2026 p.11 | Buyback under active consideration | MISSED | Q1FY27 restates "will consider it in future," no decision across two quarters |
| Concall_Apr_2026 p.10 (favourable, not in B05's original tally) | IGX Q1FY27 "not get any growth" | BEATEN | +11.9% volume, +15.5% PAT (Q1FY27 press release p.2) |

Tally as scored by the pipeline: 4 delivered, 2 partial, 4 missed
(B05.promise_delivery); an independent verifier audit found this tally
directionally sound on all five spot-checked rows and flagged one additional
favourable row (IGX Q1FY27, above) as omitted (B12b).

### 6. Restated bases

No restatement of prior-period comparatives for any reorganisation, transfer,
or reclassification was found anywhere in the corpus. B02.restatements_found
is an explicit empty list. A targeted search of the annual report text for
standard restatement/regrouping boilerplate ("regrouped," "reclassified...
wherever necessary," "conform to") returned no matches beyond routine OCI
reclassification-to-P&L language (Annual_Report_2026.txt lines 12556, 13144,
16864-16867, 17602), which is a standard other-comprehensive-income
accounting note, not a comparative restatement. NOT DISCLOSED / not present:
no restatement note exists to quote.

### 7. Corporate-action clauses

No scheme, demerger, merger, preferential issue, or buyback is present in
this corpus for IEX itself. A buyback was discussed but not executed:

> Q4FY26: "definitely considering it" restated Q1FY27: "will consider it in
future"
(per B05.timeline_slippages; no scheme document filed.)

The one live corporate action with valuation-adjacent language is the IGX
offer-for-sale, sized in the abridged prospectus only:

> "IGX offer for sale of 1.671cr shares cuts IEX's 47.28% stake to the PNGRB
25% ceiling"
(prospectus__IGX_Draft_Abridged_Prospectus_2026-07.txt; per B04.flags;
announcements__IGX_DRHP_Filing_Intimation.)

Comment: the abridged prospectus (12pp) is held; the full IGX DRHP, which
would carry price band, ratios, and effective dates, sits with the
book-running lead managers and was NOT collected. NOT DISCLOSED: OFS price
band, proceeds, and effective date. Name the filing to fetch: the full IGX
Draft Red Herring Prospectus, once available from SEBI's public filing
system or the book-running lead managers.

### 8. Related-party perimeter

> "50. Related Party Disclosures
> a) List of Related parties:
> i) Key Managerial Personnel (KMP): Satyanarayan Goel (Chairman & Managing
> Director), Sudha Pillai, Pradeep Kumar Pujari, Kayyalathu Thomas Chacko,
> Tejpreet Singh Chopra, Rajeev Gupta, Gautam Dalmia, Amit Garg, Rohit Bajaj
> (Joint Managing Director), Vineet Harlalka (CFO & Company Secretary)
> ii) Subsidiary: ICX Private Limited (formerly International Carbon
> Exchange Private Limited)
> iii) Associate: Indian Gas Exchange Limited (IGX)"
(Annual_Report_2026.pdf, standalone Note 50, p.226)

> "i. Compensation to Key managerial personnel: Salary & wages 916.16,
> Perquisites 1.19" (Rs lakh, FY26)
> "iii. Transaction with ICX Private Limited: Business support services
> 34.19; Loan received back 150.00"
> "iv. Transaction with Indian Gas Exchange Limited: Business support
> services 55.25; Reimbursement of expenses to IGX 4.71"
(Annual_Report_2026.pdf, standalone Note 50, p.227, "b) Transactions with the
related parties")

Comment: no promoter-group entity is named because none exists (0.00%
promoter/promoter-group holding). The full related-party perimeter is KMP
compensation, the wholly-owned subsidiary ICX, and the 47.28% associate IGX.
Amounts are small relative to the balance sheet (largest single item Rs150cr
loan repayment from ICX). Outstanding balances: payable to KMP Rs332.31 lakh;
recoverable from ICX Rs11.22 lakh; recoverable from IGX Rs14.19 lakh (same
Note 50, p.227).

### 9. Pledge and shareholding

> Promoter and promoter-group holding: 0.00% at 30-Jun-2026, and at each of
the four earlier quarters held (30-Sep-2025, 31-Dec-2025, 31-Mar-2026, and
30-Jun-2025) per B08's structural note: "Four earlier quarters back to
Jun-2025 in the same folder show the same zero."
(Shareholding_Pattern_30_JUN_2026.xml and the four earlier-quarter XML files
in runs/iex-2026-09-08/inputs/shareholding/; B08.pledge_pct_latest = 0,
B08.pledge_trend "NOT APPLICABLE - no promoter/promoter-group shareholding
exists to pledge.")

Public holding 99.73%, employee benefit trusts 0.27% (30-Jun-2026,
B00.analyst_note, B08). Institutional holding, latest quarter: FII 12.63%,
DII approximately 31.47% (mutual funds 24.21% + insurance 4.7% + other DII
2.56%) (B08, 08-promoter.md line 399-400).

Comment: only five quarters of shareholding pattern are held in the corpus
(30-Jun-2025 through 30-Jun-2026), short of the twelve-quarter window this
question asks for. NOT DISCLOSED beyond that five-quarter window; the
named >1% shareholder register inside the XML files could not be extracted
with the tools available this run, a tooling limitation, not a collection
gap (B08.input_gaps). Pledge is 0% at every held quarter because no promoter
holding exists to pledge; this is a structural fact of a promoter-less
company, not a governance-conduct finding.

### 10. Verification

Every document quoted in this annex, filename and date:
- Annual_Report_2026.pdf, filed 14-Aug-2026 (standalone Notes 28, 43, 44, 50).
- Concall_Feb_2026_Transcript.pdf, filed 2026-02-05 (Q3FY26 call).
- Concall_Apr_2026_Transcript.pdf, filed 2026-04-30 (Q4FY26/FY26 call, held 24-Apr-2026).
- Concall_Jul_2026_Transcript.pdf, filed 2026-07-31 (Q1FY27 Analyst Meet, held 24-Jul-2026).
- IGX_Draft_Abridged_Prospectus_2026-07.pdf (Jul-2026).
- Shareholding_Pattern_30_JUN_2026.xml and the four earlier-quarter shareholding-pattern XML files (30-Sep-2025, 31-Dec-2025, 31-Mar-2026, and 30-Jun-2025).

CORPUS COMMIT HASH: e6a917153d8657ebf0395371149e8a091c79f429
