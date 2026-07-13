# collect_to_repo — Additional Input Sources Spec (v4 proposal)

Status: proposal, 2026-07-12. Root cause: the AIMTRON 2026-07-12 run reached
its conclusions without the IPO prospectus and recent exchange announcements;
an external analyst blog then supplied promoter pedigree, the group-company
map, the FY23 55% related-party figure, and the AIC/ICS deal economics, all of
which live in the prospectus and Reg 30 filings we never collected. This spec
adds four source folders to the collector and the input contract so those
documents are pulled deterministically.

Companion change: `prompts/00-orchestrator.md` Section 1 (INPUT CONTRACT,
DEGRADATION MAP, manifest `listed_date`) and `.claude/commands/run-pipeline.md`
(stage-0 inventory + empty-folder pause) already carry the matching folders.

## Folders to add

| Folder | Contents | Anchored? | Consumed by |
|---|---|---|---|
| `inputs/prospectus/` | DRHP + RHP (0-2 PDF) | Yes (filing) | Stage 2/3 (restated FY history, notes), Stage 8 (promoter/group), FTTCP backward baseline |
| `inputs/announcements/` | Exchange / SEBI Reg 30 filings, last ~12 months | Yes (filing) | Stage 5, Stage 7, Stage 8, intent-and-action cross-check |
| `inputs/shareholding/` | Latest quarterly shareholding pattern | Yes (filing) | Stage 10 (FII+DII for UA), Stage 8 (pledge/holding trend) |
| `inputs/research/` | Sell-side / broker notes | NO — leads only | Synthesis + intent-and-action cross-check (never anchored) |

## Manifest addition

Add `listed_date: YYYY-MM-DD` (optional). If `run_date - listed_date <= ~3
years`, the prospectus is a MANDATORY fetch and an empty `inputs/prospectus/`
is a HIGH-priority gap, not a routine absence. If `listed_date` is absent, the
collector infers recency from the presence of an IPO/DRHP record on the
exchange and sets the same flag.

## Source endpoints (deterministic filings)

These are canonical public sources. Exact API paths and required
headers/cookies drift; the collector must reuse the same session/rate-limit
handling it already uses for screener.in, and verify each endpoint at build
time rather than trusting the literal path below.

### 1. Prospectus (DRHP / RHP)
- **SEBI**: sebi.gov.in → Filings → Public Issues → DRHPs / Final Offer
  Documents. Primary authority.
- **NSE**: nseindia.com IPO section / archives (mainboard and SME) — the SME
  platform (NSE Emerge) hosts SME DRHPs.
- **BSE**: bseindia.com → Corporates → Public Issues; BSE SME for SME IPOs.
- **Fallback**: the lead merchant banker's site and the company IR page.
- Filename: `PROSPECTUS_<TICKER>_<DRHP|RHP>_<YYYYMMDD>.pdf`. Target
  `inputs/prospectus/`. Fetch both DRHP and RHP when present.
- Trigger: always attempt when `listed_date` within ~3y, or when unknown.

### 2. Announcements / Reg 30 (last ~12 months)
- **NSE**: corporate announcements JSON, e.g.
  `nseindia.com/api/corporate-announcements?index=equities&symbol=<SYMBOL>`
  (requires the standard NSE cookie/referer handshake).
- **BSE**: announcements API, e.g.
  `api.bseindia.com/BseIndiaAPI/api/AnnGetData/w` with the scrip code, or the
  page `bseindia.com/corporates/ann.aspx`.
- Filter to material events: acquisitions/divestments, capital raises
  (preferential / QIP / warrants), order wins, board/management changes,
  scheme of arrangement / reverse-merger, credit-rating actions.
- Filename: `ANN_<TICKER>_<YYYYMMDD>_<slug>.pdf`. Target
  `inputs/announcements/`. Keep the last ~12 months; cap at ~30 most-material
  if volume is high.

### 3. Shareholding pattern (latest quarter)
- **NSE**: `nseindia.com/api/corporate-share-holdings-master?index=equities&symbol=<SYMBOL>`
  or the shareholding-pattern page.
- **BSE**: `bseindia.com/corporates/shpMasterNew.aspx` (scrip code).
- Capture the latest filed quarter (promoter %, pledge %, FII, DII, public).
- Filename: `SHP_<TICKER>_<YYYYMMDD>.<csv|pdf>`. Target `inputs/shareholding/`.

### 4. Research (non-anchored)
- No deterministic public API. Operator supplies broker PDFs manually, or the
  collector pulls from a licensed aggregator if configured.
- Filename: `RESEARCH_<BROKER>_<TICKER>_<YYYYMMDD>.pdf`. Target
  `inputs/research/`.
- The collector must tag these non-anchored (e.g., a sidecar `.meta` or a
  `research_manifest.yaml`) so no stage treats a research figure as evidence.

## Collector behavior notes
- Preserve the existing empty-folder / `--push-again` flow: a folder the
  collector could not fill is left empty and surfaces in the stage-0 pause.
- Large born-digital PDFs (prospectus routinely 300-500pp) must be committed
  as-is; the pipeline pre-extracts them to text at read time (the AIMTRON /
  EBGNG 32MB image-render lesson). The collector does not need to pre-extract.
- Dedup by document hash; keep the most recent when the same filing appears on
  both exchanges.
- Announcements and shareholding are quarterly-refreshable; on a `refresh`
  run, re-pull only the delta since the prior run's newest filing.

## Why this matters (one line)
The intent-and-action cross-check (proposed FTTCP Step 2E) can only grade
"documented management ACTION" if the action documents (Reg 30 filings) are in
the run folder; and for any company listed within ~3 years the prospectus is
the single foundational document, without it the backward baseline, the
promoter/group picture, and the related-party trajectory are all built on
thinner evidence than the market already has.
