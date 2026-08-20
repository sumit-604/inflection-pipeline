# DOWNSTREAM SOURCE DISCOVERY PROTOCOL v1.0

*Version 1.0 | August 2026 | Dhruva Research. Companion to Master Project Prompt v3.6 Role 5.5 (Downstream Signal Identification). This protocol governs HOW signal sources are discovered and verified. Role 5.5 governs WHEN signals are identified and WHERE they are written (the tracker gate). The TAM/SAM/SOM Downstream Signal Candidates section feeds Step 1 here.*

---

## PURPOSE

The reference case: a thesis on an oil and gas services company depended on a gas evacuation pipeline. The verification did not come from the company. It came from the pipeline owner's X handle, the anchor customer's concall, and the regulator's common-carrier authorization order. Three sources, none of them the target company, together establishing a dated, falsifiable catalyst.

That move was ad-hoc. This protocol makes it procedural. The claim underneath it: **every downstream signal is a demand chain, every chain has entities, and every entity TYPE has a standard, knowable set of places where its information lives.** Decompose the chain correctly and source discovery becomes mechanical.

---

## PART 1 — THE DEMAND CHAIN MAP

For every material revenue stream of the target company, complete this decomposition. One map per revenue stream, not one per company. A company with three revenue streams gets three maps.

| # | Field | Question it answers | Example (AESL/Oilmax, Amguri asset) |
|---|---|---|---|
| 1 | **Product / Service** | What exactly is sold? Be specific to the unit level. | Natural gas, boepd, from Amguri field, Assam |
| 2 | **Produced / delivered by** | Which entity in the group produces it? | Oilmax (being merged into listed AESL) |
| 3 | **Service scope** | What does the company do vs what do others do? Where does its responsibility end? | Oilmax owns and operates the field; evacuation depends on third-party pipeline |
| 4 | **Direct customer** | Who pays the invoice? | Gas buyers via Numaligarh refinery offtake / IGGL grid |
| 5 | **Demand driver** | WHY will the customer buy more? What changed? | DSF auction regime + pipeline connectivity unlocking stranded reserves |
| 6 | **Chain dependencies** | What third-party entities sit between the product and the cash? List EVERY one. | DNPL pipeline (200m link in refinery campus), IGGL grid, PNGRB authorization |
| 7 | **Verification points** | For each dependency and the demand driver: what observable event or number confirms progress, and what observation falsifies it? | DNPL-IGGL link completion by Dec 2026; PNGRB common-carrier order; Amguri ramp 1800→3000 boepd |

**Rules for the map:**

- Field 6 is where most analysts stop short. List every entity between the product and the cash: pipelines, approvals, certifications, logistics, the customer's own customer where relevant. A dependency not listed is a dependency not tracked.
- Field 7 must contain BOTH directions: the confirming observation AND the falsifying observation, each dated where possible. "Pipeline completes" is not a verification point. "DNPL-IGGL 200m link inside Numaligarh campus completed by Dec 2026, confirmed by IGGL disclosure or Oil India concall" is.
- If a single dependency appears in multiple maps (one pipeline serving three fields), flag it as a SHARED DEPENDENCY. Shared dependencies mean correlated catalysts, and correlated catalysts are counted ONCE in FTTCP composite probability, never as independent triggers.

---

## PART 2 — THE SOURCE REGISTRY (entity type → where information lives)

Every entity surfaced in Field 4 and Field 6 has a TYPE. Each type has a standard source map. This registry is the lookup table.

### Type 1 — Indian listed company (customer or counterparty)

| Source | What it gives | Access |
|---|---|---|
| BSE/NSE corporate announcements page for that company | Contracts, capex, approvals, resignations, in real time | Free; filterable by company |
| Its concall transcripts | Management commentary on the segment that touches your target | Free via exchange filings; Screener.in and Trendlyne aggregate |
| Its annual report (segment note, capex note, related party note) | Named suppliers, capacity plans, geography mix | Free |
| Its investor presentation | Guidance and project timelines | Free, IR page |
| Credit rating rationale (CRISIL / ICRA / CARE / India Ratings) | Third-party view of its capex, order book, counterparty risk | Free on rating agency websites, updated ~annually |

### Type 2 — Indian unlisted company (customer, JV partner, merger target)

| Source | What it gives | Access |
|---|---|---|
| Credit rating rationale documents | THE most underused source for unlisted entities: revenue, margins, debt, order book, project status, all third-party verified | Free on CRISIL/ICRA/CARE/India Ratings sites; search the entity name |
| MCA filings (AOC-4, MGT-7, charge registrations) | Audited financials with a lag, new borrowings signalling capex | MCA portal, nominal fee per document |
| Newspaper/trade press interviews of its promoters | Timelines and intent (treat as management claim, zero evidentiary weight, but useful for calendar-building) | Free |

### Type 3 — Foreign listed counterparty (US/EU/JP customer or partner)

| Source | What it gives | Access |
|---|---|---|
| SEC EDGAR (10-K, 10-Q, 8-K, S-1) | Segment revenue, supplier commentary, capacity plans, risk factors naming suppliers | Free; edgar.sec.gov; full-text search covers supplier names |
| Its earnings call transcripts | Quarterly cadence commentary on the product line your target feeds | Company IR page (free); aggregators for convenience |
| Its investor day decks | Multi-year sourcing and capacity roadmaps | IR page, free |
| For EU: annual reports + half-yearly reports | Same, semi-annual cadence | Company IR |
| For Japan: TSE filings, IR library | Same | Company IR, English versions usually available |

**EDGAR full-text search tip:** search the TARGET's name inside EDGAR (efts.sec.gov/LATEST/search-index?q="[target name]"). If a US customer names your Indian target in its filings, that single hit upgrades the whole thesis evidence quality to 📄.

### Type 4 — Government infrastructure entity (pipeline, port, transmission, SPV)

| Source | What it gives | Access |
|---|---|---|
| The SPV's own website "projects" or "media" page | Commissioning progress, tender awards | Free |
| **The SPV's X (Twitter) handle** | Often the FASTEST disclosure channel: photos of physical progress, commissioning announcements days before any filing | Free; this is the IGGL move |
| PIB (Press Information Bureau) releases for the ministry | Inaugurations, milestones, policy | pib.gov.in, free, RSS available |
| The parent PSU's concall (if listed) | Third-party confirmation of the infra timeline (the Oil India move) | Free via exchange |
| Parliament questions (Lok/Rajya Sabha Q&A database) | Dated, official status updates on public projects that nobody reads | sansad.in, free, searchable |

### Type 5 — Regulator / approval body

| Source | What it gives | Access |
|---|---|---|
| PNGRB (gas), CERC/SERC (power), TRAI (telecom), DGCA (aviation), CDSCO (pharma India), DGH (upstream oil/gas), RBI (lenders), SEBI, IRDAI | Orders, authorizations, tariff decisions, approval registers. Regulatory orders are the highest-grade evidence that exists: dated, official, binding | Each regulator's "orders" or "what's new" page, free |
| USFDA (drugs/devices for US-facing pharma) | Approval letters, warning letters, inspection outcomes, PDUFA calendar | fda.gov, free; also accessdata.fda.gov databases |
| clinicaltrials.gov | Phase status and readout timing for named molecules | Free, per-molecule watchable |
| EMA (Europe), PMDA (Japan) | Same for EU/JP-facing pharma | Free |

### Type 6 — Trade / export data

| Source | What it gives | Access |
|---|---|---|
| DGCI&S / tradestat.commerce.gov.in | HS-code level monthly exports, aggregate | Free, lagged, coarse |
| Commercial trade data (Volza, Export Genius, Cybex, Infodrive) | Shipment-level: product description, consignee name, volumes, monthly | Paid, ₹30k-1.5L/yr; the phreak molecule-tracking layer; buy only when the book justifies it |

### Type 7 — Commodity / macro

| Source | What it gives | Access |
|---|---|---|
| LBMA (precious), LME (base), MCX (domestic) | Price series | Free |
| PPAC (petroleum), CEA (power data), ICRA/CRISIL industry notes | Sector volume and utilization data | Free |
| Industry associations (SIAM auto, CMIE where subscribed, IBEF sector notes) | Volume prints, capacity data | Mostly free |

---

## PART 3 — THE SOURCE QUALITY HIERARCHY

When multiple sources speak to the same verification point, rank them. Higher rank wins conflicts. Only ranks 1-3 count toward the three-source evidence bars anywhere in the framework (Category-Break Override, 📄 evidence grading).

| Rank | Source class | Example |
|---|---|---|
| 1 | Regulatory order / official authorization | PNGRB common-carrier order; USFDA approval letter |
| 2 | The dependency owner's own disclosure | IGGL announcing link completion; pipeline SPV tender award |
| 3 | A third-party listed entity's filing or concall referencing the fact | Oil India concall confirming pipeline timeline; US customer's 10-Q naming the supplier |
| 4 | Credit rating rationale | ICRA rationale describing project status |
| 5 | Credible trade press with named officials | Interview with dated commitments |
| 6 | Target company's own claims | Concall guidance, investor deck. NEVER counts as downstream verification. Calendar value only |

**The AESL post used ranks 1, 2, and 3 simultaneously (PNGRB order + IGGL disclosures + Oil India concall). That is the template: triangulate a verification point across at least two ranks, never rely on rank 6.**

---

## PART 4 — SOCIAL AND ALERT LAYER (the semi-automation)

Source discovery is one-time per signal. Source MONITORING is recurring, and most of it can be made push-based instead of pull-based:

| Mechanism | Setup | Covers |
|---|---|---|
| X Lists (one private list per thesis cluster) | Add handles of: infra SPVs, PSU counterparties, ministries, regulators, sector journalists | Type 4 entities especially; the fastest channel |
| Google Alerts | One alert per dependency entity name + one per project name (e.g., "DNPL pipeline", "IGGL Numaligarh") | Types 2, 4, 5; press coverage |
| SEC EDGAR email alerts | Per foreign counterparty CIK | Type 3 filings, push on the day of filing |
| BSE/NSE watchlist announcements | Exchange app watchlist on Indian counterparties | Type 1, push |
| Regulator "what's new" pages | Bookmark folder, opened once monthly during the M1-M5 refresh | Type 5 |
| clinicaltrials.gov saved searches | Per molecule | Pharma theses |

What stays manual by design: reading the monthly refresh output and deciding what it means (Steps M3-M4). The alert layer feeds the refresh; it does not replace judgment.

Claude executes the monthly M1-M5 pull with web access against the Primary Source URLs in the tracker; the alert layer catches event-driven signals BETWEEN monthly refreshes so nothing waits up to 30 days.

---

## PART 5 — INTEGRATION WITH THE EXISTING PIPELINE

**Where this protocol runs:** inside Role 5.5, at Steps 1-3.

- The TAM/SAM/SOM Downstream Signal Candidates section (Claude Code pipeline) produces candidate entities → Part 1 Demand Chain Map is completed for each material revenue stream during Role 5.5 Step 1-2 → Part 2 Source Registry lookup assigns concrete sources per entity → Part 3 hierarchy grades them → only rank 1-3 sourced signals proceed to Role 5.5 Step 4 (the tracker write gate) as verified rows → Part 4 alert layer is set up for each newly written signal.
- The Demand Chain Map itself (Part 1 table, all revenue streams) is saved to the company's Notion page as part of the Role 5.5 output, so the chain reasoning is auditable later, not just the resulting signals.
- Shared dependencies flagged in Part 1 carry into FTTCP composite probability (correlated catalysts counted once) and into Role 3 pre-mortem (single-point-of-failure scenarios).

**Tracker fields this protocol populates:** Signal Name, Signal Type, Primary Source URL (deep link, per registry), Update Cadence, Falsifying Observation (from Field 7), Per-Company Thesis Element (from Fields 5-6).

---

## PART 6 — WORKED EXAMPLE (the reference case, run through the protocol)

Target: AESL (Oilmax merger). Revenue stream: Amguri gas production.

**Demand Chain Map:** Product = natural gas boepd from Amguri | Produced by = Oilmax | Scope = field ops only; evacuation is third-party | Customer = offtake via Numaligarh/IGGL | Demand driver = DSF regime + connectivity unlocking stranded reserves | Dependencies = DNPL 200m link (inside refinery campus), IGGL grid, PNGRB authorization | Verification = link completion by Dec 2026 (confirms); slippage past Q3 FY27 (falsifies); ramp 1800→3000 boepd (confirms).

**Registry lookup:** DNPL/IGGL = Type 4 → SPV website + X handle + PIB + parent PSU concall. PNGRB = Type 5 → orders page. Oil India = Type 1 → concall transcripts.

**Hierarchy check:** PNGRB order (rank 1) + IGGL disclosure (rank 2) + Oil India concall (rank 3). Three sources, three different ranks, none of them the target company. Passes every evidence bar in the framework.

**Tracker rows written:** (1) DNPL-IGGL link completion — Event-driven, Dec 2026 window, falsifier: slippage past Q3 FY27; SHARED across Amguri/Tiphuk/Duarmara maps → flagged correlated. (2) Amguri production ramp — Quarterly, from DGH/company production disclosures cross-checked. (3) PNGRB authorization status — Event-driven, already fired, health: Confirms.

**Alert layer:** X list with IGGL + Oil India + PNGRB + MoPNG handles; Google Alerts on "DNPL pipeline" and "IGGL Numaligarh".

Time cost honestly stated: 45-90 minutes per company at workup, near zero thereafter (alerts push; monthly refresh reads).

---

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 1.0 | August 2026 | Initial protocol. Demand Chain Map (7 fields, per revenue stream, shared-dependency flagging). Source Registry across 7 entity types with named sources and access notes. Source quality hierarchy (6 ranks; only 1-3 count toward evidence bars; target's own claims rank 6, never downstream verification). Social/alert semi-automation layer. Pipeline integration at Role 5.5 Steps 1-3 with Demand Chain Map saved to Notion. AESL/IGGL reference case worked end to end. |
