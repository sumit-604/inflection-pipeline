# DOWNSTREAM SOURCE DISCOVERY PROTOCOL v1.0

*Version 1.0 | 19 August 2026 | Produced in the claude.ai project on
19-Aug-2026.*

**STUB — content held in claude.ai project outputs, to be committed by the
operator.** The finished document was not present in the repository or in
the session context when this placeholder was created (20-Aug-2026). The
operator pastes the full protocol text over this stub, keeping this
filename, so the pipeline references below resolve without further edits.

What the full document carries (for reference until it lands):
- The Source Registry: the entity type -> primary source map (End-customer /
  Counterparty / Regulatory / Macro) that stage 9 SECTION 6 cites when it
  names a LIKELY primary source for each downstream signal candidate.
- The Role 5.5 verification procedure run in claude.ai: URL verification,
  cadence confirmation, and the tracker write to the DOWNSTREAM SIGNAL
  TRACKER database (data_source_id 926b65ce-ddd2-4d8b-8eae-05e66b6f6c9f).
  The pipeline never writes to the tracker; it produces candidate payloads
  only.
- The falsifying-observation discipline for each verified signal.

Referenced by: prompts/09-tam-pipeline.md (SECTION 6), prompts/
11-valuation-pipeline.md (FTTCP v2.1 Signal Gate), prompts/
13-synthesis-pipeline.md and .claude/commands/finalize.md (DOWNSTREAM
SIGNAL TRACKER PAYLOAD), prompts/12-verifiers-pipeline.md (Verifier C
check), CLAUDE.md STRUCTURE.
