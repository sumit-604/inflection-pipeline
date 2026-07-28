# Notion Save Payload — COMPANIES MASTER

This is a payload file only. No live Notion write is performed by the pipeline. The orchestrator applies it per Notion_Save_Instructions.

## Save instructions (explicit)

- Fetch the live COMPANIES MASTER page for ENTERO first if it exists.
- NEVER overwrite Decision Status from a pipeline run. Decision Status is operator-owned.
- Append the run summary below as a new dated run entry. Do not replace existing content.
- Append the single disagreement-log row (verifier-disagreement-log.md) to the "Verifier Disagreement Log" page.

## Payload

```yaml
notion_save:
  page_title: "ENTERO — Entero Healthcare Solutions Ltd"
  ticker: "ENTERO"
  run: "entero-2026-07-27"
  run_date: "2026-07-27"
  mode: append-never-overwrite-status
  run_summary:
    headline: "Pharma distributor roll up turns cash positive"
    verdict: "PROCEED WITH CAVEATS (evidence gate; INDETERMINATE cash cap)"
    decision: "AVOID (on valuation) at CMP Rs1,273"
    business_read: "FTTCP +5 of 8, BUY candidate transition; price not there"
    tier: "A, 25% hurdle (Tier B barred by promoter CONCERN)"
    destination_pe: "15.0x both tracks (operator override), forward owners' EPS basis"
    fair_value_base: "Rs1,112 (bear Rs857 / bull Rs1,422)"
    hurdle_ratio: "base 0.74 / bull 0.90 = STOP"
    prob_weighted_3yr_cagr: "-4.3%"
    entry_range: "Rs506 to Rs569"
    mos_price: "Rs455"
    zone_reachability: "MARKET-UNLIKELY (entry top 55.3% below CMP); DEEP WATCH"
    position_size: "None; WATCHLIST only if price enters zone AND cash/margin durability prints"
    flags_active: ["FLAG-PROMOTER (CONCERN)", "FLAG-CASH (INDETERMINATE)", "FLAG-GATE0 (AVERAGE)", "SHARED CATALYST"]
    confidence_overall: 83
    devils_advocate: "AVOID SURVIVES (over-determined)"
    falsification_metric: "NWC days >65 in Q1/Q2 FY27 with OCF/EBITDA <50%"
    publish_candidate: false
  drive_link: "{{DRIVE_FOLDER_LINK}}"
  drive_link_note: "Drive folder link NOT PROVIDED to this run; local run folder runs/entero-2026-07-27/"
  files_written:
    - "outputs/final/business-narrative.md"
    - "outputs/final/fttcp-recommendation.md"
    - "outputs/final/verifier-summary.md"
    - "outputs/final/fttcp-handoff.md"
    - "outputs/final/verifier-disagreement-log.md"
    - "outputs/final/notion-payload.md"
```

## SAVE PERFORMED (2026-07-28)
- COMPANIES MASTER: NEW page created (no prior ENTERO page existed, so no operator-owned
  Decision Status to preserve). URL: https://app.notion.com/p/3abbb2b9d3ab81eebf38ef32aab39417
  Decision Status set to WATCHLIST / AVOID as the pipeline read, flagged in Key Notes for
  operator confirmation. All Gate 0 / EM / promoter / entry / MoS / CMP fields populated.
- Verifier Disagreement Log: the single ENTERO row prepended (newest first) to
  https://app.notion.com/p/3a1bb2b9d3ab816e85c0d8e75bd3be7e
- Drive folder link was not provided to this run; artifacts referenced via the GitHub branch.
