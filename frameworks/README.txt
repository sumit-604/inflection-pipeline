COPY THESE EIGHT FILES HERE FROM YOUR CLAUDE.AI PROJECT BEFORE THE
FIRST RUN (stage 11 halts without them):
  Master_Project_Prompt_v3_6.md
  Section_1B_v3.3_Amendments.md
  Section_1B_v3_5_1_Reconciliation.md
  Section_1B_v3_6_Amendments.md
  Section_1B_v3_7_Amendments.md
  Section_1B_v3_8_Amendments.md
  Section_1B_v3_9_Amendments.md
  FTTCP_v2_1_Consolidated.md
Section_1B_v3_5_1_Reconciliation.md is the Pillar 1 normalization
authority for capital-cycle names. Its consolidated Amendment 9
SUPERSEDES the standalone Amendment 4.5 that still appears in
Section_1B_v3.3_Amendments.md (kept for history, banner-marked as
retired). Stage 11 injects all six Section 1B layers; where they
overlap, v3.9 governs the items it names (relative valuation
cross-check, step 1C), then v3.8, then v3.7, then v3.6,
then v3.5.1, then v3.3.
When you amend a framework, update the copy here. Stage 11 reads these
at run time, so amendments propagate with no pipeline edits.

ALSO MAINTAINED HERE (keep synced with the claude.ai project):
  Annual_Report_Analysis_Protocol_v1_3.md     (Role 6 AR review; Step 10.5
    tracker cross-check runs at Role 5.5, fed by the pipeline's
    ar_new_downstream_entities field)
  Downstream_Source_Discovery_Protocol_v1_0.md (source registry for
    downstream signal candidates; stage 9 names LIKELY sources against it,
    Role 5.5 verifies against it in claude.ai)

QUARTERLY PIPELINE (/run-quarterly) ALSO NEEDS THESE TWO PROTOCOL FILES
HERE (the A4 analyst halts without the one its docs require):
  Quarterly_Results_Review_Protocol_v1_4.md   (Role 4, for results filings)
  Quarterly_Concall_Analysis_Protocol_v1_1.md (Role 5, for concalls)
These are the analytical authority for the quarterly review; the
/run-quarterly extraction agents (A1-A3) govern extraction and reconcile
100% before A4 reads the protocol. Copy them from the claude.ai project
before the first quarterly run. Do not reconstruct a protocol from memory:
if the file its docs require is absent, /run-quarterly STOPS and reports.
