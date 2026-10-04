# Prompt audit, October 2026

Date: 2026-10-03. Target models: Opus 5.5 (`claude-opus-5-5`) and Sonnet 5.5 (`claude-sonnet-5-5`). Report only: nothing here is applied. The proposed edits are in `audits/prompt-audit-2026-10.patch`.

## Scope and method

- Files read: CLAUDE.md, every file under `.claude/` (6 commands, 24 agents, 2 hooks, the section-1b skill and its 17 chunks), every stage prompt in `prompts/` (21 files), every file in `frameworks/` (18 files), `team_workflow_project_instructions.md`, `verifiers/README.md`, and LESSONS.md (for contradictions only).
- `/checkup prompt-audit` is not a command in this session. The audit followed the `claude-api prompt-audit` checklist (pressure language, fossils, contradictions, keep list) plus the six October checks in the session brief.
- Five readers worked in parallel, one per file group. Each finding quotes the current text verbatim. A script then matched every quote against the file on disk: 169 edits matched exactly once and 4 banner or line inserts were made by hand: 173 edits form the patch. Questions (class Q) carry no edit, and 19 edits need a hand edit at apply time (class M).
- Hard limit kept: no proposed edit changes a threshold, multiple, band, cap, weight, gate, decision rule or amendment meaning. Where a fix might, the finding is a QUESTION (class Q).
- Framework files are operator-maintained and mirrored in the claude.ai project. Any approved edit under `frameworks/` must also be copied to the claude.ai project copy.

## Classes

| Class | Meaning | high | medium | low | total |
|---|---|---|---|---|---|
| A | wording (in patch) | 0 | 41 | 65 | 106 |
| B | alignment (in patch, needs ruling) | 25 | 28 | 14 | 67 |
| Q | question (no edit) | 22 | 43 | 15 | 80 |
| M | manual edit (not in patch) | 0 | 9 | 10 | 19 |
| all | | 47 | 121 | 104 | 272 |

Class B means the edit is wording, but it touches a rule statement: it aligns older text with a later amendment or ruling, or restates a number already ruled elsewhere. Each B edit waits for an explicit ruling.

## October checks: results

| Check | Result |
|---|---|
| Old-model phrasing ("think carefully", "step by step", "take your time", "be thorough") | One hit: Quarterly_Concall_Analysis_Protocol_v1_1.md line 184 "be thorough" (FW-R5-01). Emphasis stacks (CRITICAL, MUST, read carefully) are flagged per file, mostly in the Master and FTTCP. |
| Requests to write out reasoning or chain of thought | None found. The bounded `analyst_note` fields (200 words max) and one-line rationale fields ask for an output, not a thought dump, so they stay. |
| Retired-model fallback | prompts/00-orchestrator.md line 707 retries a refused stage "once on Opus 4.8" (ORC-01, high). Opus 4.8 cannot read Opus 5.5 thinking blocks, so a retry there runs without them. The edit retries on the stage's own frontmatter model. |
| Mid-session model switch | `.claude/commands/fttcp.md` sets `model: claude-opus-5-5` in its frontmatter with no effort (LEAD-01, high, question). Invoked from a session on any other model, it switches the session model and empties the prompt cache. |
| Piecemeal tasking | The Master, the AR protocol and the two Quarterly protocols are written as claude.ai dialogues: "Type GO", "show the table and wait". The pipeline agents are told never to stop, so these lines never wait. They are classified in the stop-point table below. |
| Stale paths and versions | 82 stale-ref findings. Main pattern: FTTCP cited as v2.0 or v2.1 and the Master cited as v3.6 as the live authority, in at least 9 files. README.txt and CLAUDE.md still say stage 11 reads frameworks/ at run time; stage 11 now reads only the section-1b skill (G5-README-01, high). |
| Contradictions and unmarked superseded text | 99 contradiction findings, 25 duplication findings and 18 old-phrasing findings. The highest-impact ones are listed below. |

## Highest-impact findings

| ID | File | Class | Issue |
|---|---|---|---|
| G5-AR-06 | `frameworks/Annual_Report_Analysis_Protocol_v1_3.md`:1064 | B | names v3.3 alone as the full set, which drops Amendments 9-26 (e.g. the 30x Pillar 1 cap, Step 1C, A21 base). |
| G5-AR-08 | `frameworks/Annual_Report_Analysis_Protocol_v1_3.md`:1248 | B | CLAUDE.md bars an entry zone without the A19 FV CAGR and return-source classification; OR-8 confirmed the tier divisor and A18.1 the exit-consistent basis. This restates ruled text only. |
| G4-MST-01 | `frameworks/Master_Project_Prompt_v3_6.md`:108 | B | Names the set only to v3.6, so a Role 2/3 reader treats A17-A26 as outside the authority; also drops "CRITICAL" and "read carefully". |
| G4-MST-02 | `frameworks/Master_Project_Prompt_v3_6.md`:266 | B | The header labels "v3.3" as the whole set and nothing in the section body tells a reader that Pillar 3, the Hurdle, the entry price and the projection horizon below are superseded. |
| G4-MST-05 | `frameworks/Master_Project_Prompt_v3_6.md`:568 | B | CLAUDE.md says "There is no STOP verdict" and runs never halt on company quality; the skill already uses "STOP band"; the threshold also misses Tier B 1.728 (v3.3 A4.3). If the operator reads "threshold" as a rule change |
| G4-MST-06 | `frameworks/Master_Project_Prompt_v3_6.md`:562 | B | Base text states one threshold; Amendment 4.3 (and OR-8) set two, so a Master-only reader mis-tests every Tier B name. This restates existing law, it does not change it. |
| G4-MST-07 | `frameworks/Master_Project_Prompt_v3_6.md`:658 | B | v3.8 Amendment 18.0 makes Year 4 a committed row and "NOT PROJECTED" for Year 4 REWORK; the template (also 2A at line 590) omits it. Apply the same column add to the 2A table after line 589 ("/ Revenue Year 4 / ₹___ Cr / |
| G4-MST-08 | `frameworks/Master_Project_Prompt_v3_6.md`:859 | B | CLAUDE.md bars any entry zone without the A19 FV CAGR and label; 4E has neither and ignores Tier B. |
| FW-R4-01 | `frameworks/Quarterly_Results_Review_Protocol_v1_4.md`:439 | B | Section_1B_v3_6_Amendments.md line 24 says Amendment 5's "capped at 24x" is SUPERSEDED and "must not be applied"; this cell still prints it. The edit removes the stale number. It does not change the governing value. |
| G5-README-01 | `frameworks/README.txt`:28 | B | stage 11 now reads the preloaded skill with "no file injection" (prompts/11-valuation-pipeline.md line 325), so line 29 "amendments propagate with no pipeline edits" is false; an amendment edited only here never reaches  |
| G5-1B33-02 | `frameworks/Section_1B_v3.3_Amendments.md`:77 | B | v3.6 line 5 promises superseded text is "banner-marked", but Amendment 5 carries no mark; verifier C reads this file directly and can apply 24x. |
| G5-1B33-03 | `frameworks/Section_1B_v3.3_Amendments.md`:35 | B | the unmarked table says CONDITIONAL caps the verdict and STOP blocks, which OR-2 overruled. |
| G5-1B36-01 | `frameworks/Section_1B_v3_6_Amendments.md`:3 | B | contradicts README ("Stage 11 injects all seven Section 1B layers") and the current wiring; a verifier reading the banner may treat Amendments 11-16 as not live. |
| G5-1B38-01 | `frameworks/Section_1B_v3_8_Amendments.md`:65 | B | Amendment 20 exists in v3.8 and v3.9 with different text (v3.9 adds 20.8 recompute and 20.9 "Operator-approved base still binds"; v3.8 20.0 says it "can supersede the pillar destination"); the v3.8 copy carries no mark. |
| ORC-01 | `prompts/00-orchestrator.md`:707 | B | names a retired model as the fallback; CLAUDE.md forbids changing a stage's model without editing its agent file. |
| ORC-02 | `prompts/00-orchestrator.md`:684-685 | B | cites FTTCP v1.2 as the live protocol and a manual session that phase 2 replaced; line 44 already calls this file "the archive dossier". |
| ORC-03 | `prompts/00-orchestrator.md`:692-696 | B | CLAUDE.md says "The pipeline produces payloads. claude.ai executes writes"; Notion_Save_Instructions.docx does not exist in the repo; runs live in runs/, not Drive. |
| ORC-04 | `prompts/00-orchestrator.md`:443-445 | B | contradicts PHASES (lines 19-27), which runs the verifiers in phase 1 when stage 11 does not yet exist; an orchestrator reading the table could wait for B11 in phase 1. |
| VER-01 | `prompts/12-verifiers-pipeline.md`:2 | B | contradicts the orchestrator PHASES and this file's own phase-1 scope for Verifier C (lines 210-216). |
| VER-02 | `prompts/12-verifiers-pipeline.md`:206-209 | B | rule 3 (line 227) and rule 8 audit 23 rows and categories 21-22; the scope text says 20 and 21, so the verifier holds two rubric sizes. |
| VER-04 | `prompts/12-verifiers-pipeline.md`:298-300 | B | prompt 09b now has six sections and a third verdict; this check would force a hard REWORK on a correct dossier with a freshness gap. |
| SYN-01 | `prompts/13-synthesis-pipeline.md`:101-103 | B | the CLAUDE.md matrix has seven postures; the list omits PRICED NARRATIVE (TRAP), the cell CLAUDE.md calls "the most seductive", so stage 13 cannot name it. |
| ORCH-Q-02 | `prompts/quarterly-00-orchestrator.md`:271 | B | Rule 4 is the pre-gate per-page OCR rule; the SEQUENCE step 1 (lines 135-138) and A1 superseded it, and the old text was never removed. |
| PR-A4-01 | `prompts/quarterly-a4-analyst.md`:52 | B | Lines 11-14, the agent file, and the orchestrator all forbid loading Master; this line tells A4 to consume it. |
| PR-A4-02 | `prompts/quarterly-a4-analyst.md`:65 | B | Role 4 Step 8A-W is the WATCHLIST / non-held branch, not a warrant branch; the wrong label can misroute the position decision. |
| CMD-FTTCP-01 | `.claude/commands/fttcp.md`:48-52 | Q | the one command CLAUDE.md names besides /run-pipeline for the spear gate never checks it. |
| LEAD-01 | `.claude/commands/fttcp.md`:4 | Q | a command-level model line is a mid-session model switch whenever the session model differs; CLAUDE.md fixes model and effort at session start. |
| CMD-RP-01 | `.claude/commands/run-pipeline.md`:393-395 | Q | as written, every phase-1 run either reports a false DOWNSHIFT FAILURE for stage 0 (it runs on the Opus orchestrator by design) or tempts the orchestrator to dispatch stage 0 to a haiku agent that does not exist; stage 1 |
| CMD-RQ-01 | `.claude/commands/run-quarterly.md`:136 | Q | An orchestrator reading line 136 can run a second loop that line 104 forbids without operator consent. |
| CMD-RQ-02 | `.claude/commands/run-quarterly.md`:53 | Q | The command and CLAUDE.md assign the Notion write to different actors. |
| CMD-STEP1-01 | `.claude/commands/step1.md`:12-20, 38, 126-140 | Q | the binding file and the command describe opposite spear workflows; a model following CLAUDE.md will refuse Step B or treat the auto-override as a gate breach. |
| G4-SK15-01 | `.claude/skills/section-1b/references/15-cost-of-capital-relative-valuation.md`:59 | Q | A stage that reads the macro-sheet row instead of the chunk uses a terminal growth 75 bps above the Master cap. |
| LES-01 | `LESSONS.md`:148-150 (versus CLAUDE.md line 16-17) | Q | an approved operator ruling and the binding CLAUDE.md rule disagree on the bear margin input. |
| G5-FTTCP-08 | `frameworks/FTTCP_v2_1_Consolidated.md`:562 | Q | as written FTTCP sets Decision Status itself, which conflicts with three binding statements; wording fix changes who decides, so MEANING-RISK. |
| G5-MIA-02 | `frameworks/Market_Implied_Assumptions_v1_0.md`:30 | Q | an exit PE chosen outside Section 1B enters a block that Role 1 consumes. |
| G4-MST-03 | `frameworks/Master_Project_Prompt_v3_6.md`:373 | Q | A Role 2/3 reader of the Master alone applies a pre-v3.4 Pillar 3; the marker is wording, but the heading change touches a pillar, so it is put as a question. |
| G4-MST-04 | `frameworks/Master_Project_Prompt_v3_6.md`:567 | Q | The Master and the skill give stage 14 and stage 11 opposite rules for the same band. |
| FW-R4-06 | `frameworks/Quarterly_Results_Review_Protocol_v1_4.md`:60 | Q | With the orchestrator's "protocol wins on analysis" clause, A4 receives two opposite instructions for the same case. |
| G5-1B39-01 | `frameworks/Section_1B_v3_9_Amendments.md`:126 | Q | the fast-growth trigger points at a state no stage can emit, so the second branch never fires or fires on guesswork. |
| CC-02 | `prompts/05-concall-pipeline.md`:88-91 | Q | the stage that is the SOLE source for the weights does not carry the A26.4 basis that CLAUDE.md NEVER-list binds. |
| PR-01 | `prompts/08-promoter-pipeline.md`:2, 11-14 | Q | a stage told to search a web it cannot reach either returns partial or fills from memory, which the NEVER-list forbids. |
| VA-01 | `prompts/10-input-assembly-pipeline.md`:19-22 | Q | the assembler pre-shades a Role 1 input before the stage that is told never to shade sees it. |
| VER-03 | `prompts/12-verifiers-pipeline.md`:262-263 | Q | as written the verifier can pass a shaded input or fail a compliant one. |
| ORCH-Q-01 | `prompts/quarterly-00-orchestrator.md`:313 | Q | The closing halt list contradicts the loop cap stated above it. |
| ORCH-Q-03 | `prompts/quarterly-00-orchestrator.md`:7 | Q | As written, the precedence clause hands A4 a protocol instruction to halt that its agent file forbids. |
| TWF-01 | `team_workflow_project_instructions.md`:85 | Q | duplicate of the run-pipeline defect; the claude.ai copy will audit Claude Code against a wrong list. |
| TWF-03 | `team_workflow_project_instructions.md`:14 | Q | contradicts step1.md, the current intake path. |

## Stop points

201 stop points across the instruction files: KEEP 60, MERGE 55, DROP 24, MECHANICAL (a halt on a missing file or failed parse, not an operator stop) 60. No stop point is changed by the patch. KEEP = an operator ruling is genuinely needed. MERGE = can be grouped with the stop named so you review once. DROP = only re-confirms arithmetic a verifier already checks.

| file:line | trigger | waits for | class | merge-with or reason |
|---|---|---|---|---|
| CLAUDE.md:215 | "If neither line exists, STOP." | Spear HIT or OVERRIDE line in companies/<TICKER>.md | KEEP | spear gate |
| CLAUDE.md:37-38 | "If one is missing, STOP and return to Role 2" | bull case built to depth (Rule H); loops to Role 2, no operator wait | MECHANICAL | output-depth loop, not an operator ruling (see CMD-FIN-03) |
| CLAUDE.md:75-76 | "Never run /fttcp or any valuation on an unsigned Mental Model" | signed Mental Model + Halt 1 PROCEED | KEEP | Mental Model signature / Halt 1 |
| CLAUDE.md:223 | "-> HALT 1: operator reads the dossier" | KILL / SHALLOW / PROCEED | KEEP | Halt 1 |
| run-pipeline.md:14-16 | "If more than one matches, list the matches and ask." | operator picks the run folder | DROP | not a ruling; fttcp.md line 40-42 resolves the same ambiguity without asking (MEANING-RISK: operator to confirm) |
| run-pipeline.md:14-15 | "If nothing matches, list the available runs and stop." | valid run folder | MECHANICAL | missing input |
| run-pipeline.md:97-98 | "halts the run with the stage named" | stage runs in foreground | MECHANICAL | execution failure |
| run-pipeline.md:131 (via 00-orchestrator.md:153-172) | SPEAR GATE "STOP the run at once" | Spear line | KEEP | spear gate; not named in this file (CMD-RP-07) |
| run-pipeline.md:159 | "HALT ONLY IF: manifest.yaml is missing" | manifest / non-empty inputs | MECHANICAL | missing input |
| run-pipeline.md:169-170 | "NOT FOUND ... blocks stage 11 in phase 3" | operator rules the sector cap row | KEEP | sector cap row ruling; MERGE candidate with the fttcp P/E BASE CARD gate where the row is confirmed |
| run-pipeline.md:192-196 | "HALT and tell the operator to re-collect" (cmp 0) | re-collected corpus | MECHANICAL | file says mechanical failure |
| run-pipeline.md:204-208 | freshness FAIL "Carry the failed pair into the empty-folder confirmation" | missing mate document | MERGE | already merged into the empty-folder question; keep merged |
| run-pipeline.md:210-233 | "PAUSE before executing any stage and ask the operator exactly once" | proceed with gaps or push documents; non-blocking | MERGE | with the freshness FAIL (done) and the cmp 0 re-collect message, so the operator gets one stage-0 corpus message |
| run-pipeline.md:269-271 | "second failure halts the run with the stage named" | valid YAML block | MECHANICAL | parse failure |
| run-pipeline.md:378-381 | "STOP and report which check failed" | well-formed 09b dossier | MECHANICAL | format failure |
| run-pipeline.md:429-437 | "HALT 1 — UNDERSTANDING GATE" | corpus gaps, Mental Model sign-off, KILL / SHALLOW WATCH / PROCEED | KEEP | Halt 1 |
| fttcp.md:39-46 | "list the available runs under runs/ and stop" / "say so plainly and stop" | run folder, manifest, blocks | MECHANICAL | missing input |
| fttcp.md:54-59 | "ROLE 5.5 TRACKER GATE ... STOP and print what is missing" | tracker rows with row-URL proof | KEEP | Role 5.5 tracker gate (see CMD-FTTCP-06) |
| fttcp.md:61-64 | "UNDERSTANDING GATE ... If any is missing, STOP" | signed Mental Model, Halt 1 PROCEED, 09b dossier | KEEP | Mental Model signature / Halt 1 |
| fttcp.md:77-81 | "STOP and report \"inputs/research/ missing\"" | scaffold re-run | MECHANICAL | missing folder |
| fttcp.md:82-84 | "STOP and report \"dossier missing\" ... and ask the operator" | handover dossier | KEEP | handover input gate (team workflow line 94); drop the "ask" wording (CMD-FTTCP-08) |
| fttcp.md:(absent) | spear gate per CLAUDE.md:205-215 | Spear line | KEEP | missing from the file (CMD-FTTCP-01) |
| fttcp.md:378-380 | "Ask me anything or give me your overrides." | operator review, overrides | MERGE | with VALUATION PILLAR APPROVAL (line 401) so review and P/E approval are one operator session; already sequential in one review |
| fttcp.md:398-399 | "Keep answering and recording until the operator signs off." | operator sign-off | MERGE | with VALUATION PILLAR APPROVAL; sign-off and approval are one decision moment |
| fttcp.md:401-419 | "VALUATION PILLAR APPROVAL (mandatory operator gate" | approved destination PE base + earnings basis | KEEP | P/E gate |
| finalize.md:14-16 | "If more than one matches, list the matches and ask." | operator picks the run folder | DROP | same as run-pipeline.md:14-16 |
| finalize.md:55-67 | "REFUSE to start" (deliberation or approved pillars missing) | fttcp-deliberation.md with OPERATOR-APPROVED VALUATION PILLARS | KEEP | P/E gate enforcement |
| finalize.md:123-124 | "STOP and tell the user which to add" | section-1b SKILL.md / Master file | MECHANICAL | missing file |
| finalize.md:141-146 | stage 15 runs, no Rule H STOP | (none; Rule H check absent) | MECHANICAL | see CMD-FIN-03 |
| step1.md:43 | "if `.env` is missing, STOP and tell the operator" | screener .env on disk | MECHANICAL | missing file |
| step1.md:168 | "print the Halt 1 message ... and STOP" | Halt 1 decision | KEEP | Halt 1 |
| step1.md:175-177 | "STOP and report the specific failure" | identity / corpus / stage blocker | MECHANICAL | mechanical blockers |
| compost.md:14-16 | "say so plainly and stop: there is nothing to compost" | archive entries | MECHANICAL | nothing to process |
| compost.md:43 | "Stop and ask the operator which proposals to apply." | operator approval of each prompt/framework edit | KEEP | framework amendment ruling |
| compost.md:60 | "Do not commit or push unless the operator asks." | operator commit instruction | MERGE | with compost.md:43 approval (ask once: which to apply and whether to commit/PR) |
| team_workflow:21 | "`/run-pipeline` and `/fttcp` STOP" | Spear line | KEEP | spear gate (duplicate of CLAUDE.md:215) |
| team_workflow:92 | "Halt 1 gate" | dossier + annex + signed model + PROCEED | KEEP | Halt 1 |
| team_workflow:93 | "Role 5.5 tracker gate" | three external signals per entity | KEEP | tracker gate (pass condition differs from fttcp.md:54; CMD-FTTCP-06) |
| team_workflow:94 | "Handover input gate ... absence = STOP" | handover dossier with Section 6 | KEEP | same as fttcp.md:82-84 |
| team_workflow:96 | "P/E gate and Amendments 16-19" | per-entity operator rulings | KEEP | P/E gate, Amendment 16-19 gates |
| team_workflow:31 | "Hand-off 4 — Operator ruling and verdict sentence" | gate-card rulings + verdict sentence | MERGE | with fttcp.md VALUATION PILLAR APPROVAL; same operator session |
| prompts/00-orchestrator.md:169 | "If neither line exists, STOP the run at once" | Spear HIT or OVERRIDE line in companies/<TICKER>.md | KEEP | spear gate, operator ruling 28-Aug-2026 |
| prompts/00-orchestrator.md:28-29 | "Phase 1 complete. Next: /fttcp" | operator reads dossier, signs model, KILL/SHALLOW/PROCEED (Halt 1) | KEEP | Halt 1 |
| prompts/09b-halt1-dossier.md:4-5 | "the operator reads to decide KILL / SHALLOW WATCH / PROCEED" | Halt 1 decision | KEEP | Halt 1 (same stop as 00:28) |
| prompts/09b-halt1-dossier.md:15 | "The kill/proceed decision is the operator's" | Halt 1 decision | MERGE | restates 09b:4-5 in the same file; one statement |
| prompts/09b-halt1-dossier.md:57-59 | "Signing happens only in claude.ai" | Mental Model signature | KEEP | Mental Model signature; operator does it in the same Halt 1 review |
| prompts/00-orchestrator.md:37-38 | "Refuses to start until `outputs/final/fttcp-deliberation.md` exists" | phase 2 FTTCP deliberation by operator | KEEP | FTTCP deliberation / pillar-approval gate |
| prompts/11-valuation-pipeline.md:180-187 | "approved by the operator at the FTTCP pillar-approval gate" | operator-approved exit PE base and basis (consumed here, stop lives in /fttcp) | KEEP | P/E gate |
| prompts/00-orchestrator.md:271-274 | "It DOES block stage 11 ... an ad hoc cap is an operator ruling" | operator ruling on a sector cap row when none fits | MERGE | merge with the /fttcp pillar-approval gate (11:180-187); the operator rules cap row and exit PE base in one sitting |
| prompts/00-orchestrator.md:414-417 | "leaves the answer to Keerti" | operator view on whether prior overrides still hold (refresh runs) | MERGE | merge with the phase 2 deliberation (00:37); asked at /fttcp, not after synthesis |
| prompts/00-orchestrator.md:694-695 | "never overwrite Decision Status from a pipeline run" | Decision Status stays operator-owned | KEEP | Decision Status |
| prompts/13-synthesis-pipeline.md:301-302 | "NEVER overwrite Decision Status from a pipeline run" | same | MERGE | same rule as 00:694-695; state once |
| .claude/agents/stage-15-devil.md:83 | "If any is missing, STOP. Do not write the devil's advocate." | Role 2 rerun to depth (steelman gate, Rule H) | KEEP | binding Master v3.7 Rule H and CLAUDE.md; returns to Role 2, not to the operator |
| prompts/11-valuation-pipeline.md:24-29 | "Where the framework says STOP ... continue immediately" | nothing (interim state line, then continue) | DROP | already converted to write-and-continue; interim lines are arithmetic checkpoints Verifier C re-derives |
| .claude/agents/stage-14-thesis.md:28-29 | "Where the framework says STOP and report interim state" | nothing (continue) | DROP | same as 11:24-29 |
| .claude/agents/stage-15-devil.md:28-29 | "Where the framework says STOP and report interim state" | nothing (continue) | DROP | same as 11:24-29; see AG-15-01 for the clash with line 83 |
| prompts/00-orchestrator.md:147-148 | "It halts ONLY if `manifest.yaml` is missing or unparseable" | manifest / inputs present | MECHANICAL | |
| prompts/00-orchestrator.md:245-252 | "`cmp` or `market_cap_cr` of 0 is a MECHANICAL FAILURE" | re-collection from standalone page | MECHANICAL | |
| prompts/00-orchestrator.md:702-705 | "Second failure: run halts, stage named." | valid YAML block | MECHANICAL | |
| prompts/00-orchestrator.md:706 | "3 retries, exponential backoff" | API recovery | MECHANICAL | |
| prompts/00-orchestrator.md:707 | "retry once on Opus 4.8, then halt with reason" | refusal resolution | MECHANICAL | see ORC-01 (stale model) |
| prompts/00-orchestrator.md:711-712 | "halt before the next stage and report per-stage spend" | cost circuit breaker | MECHANICAL | operator sees spend, but trigger is mechanical |
| prompts/09b-halt1-dossier.md:301-303 | "the orchestrator will re-run this stage" | complete Section 6 annex | MECHANICAL | |
| prompts/12-verifiers-pipeline.md:272-331 | "REWORK for stage 9 / 11 / 7 / 13 / 09b" (rules 6-14) | stage rerun | MECHANICAL | quality reruns, not operator stops |
| .claude/commands/run-quarterly.md:20-22 | "list candidate PDFs and ask which to run" | operator names the docs | MECHANICAL | missing input; only permitted setup question |
| .claude/commands/run-quarterly.md:25 | "If a needed one is absent, STOP and report" | missing protocol file | MECHANICAL | missing file |
| .claude/commands/run-quarterly.md:38-39 | "STOP and report the missing tool" | toolchain install | MECHANICAL | missing tool |
| .claude/commands/run-quarterly.md:69 | "Any gap = STOP for that document" | A1 page coverage | MECHANICAL | extraction gap |
| .claude/commands/run-quarterly.md:72-73 | "second mismatch escalates to the human" | A2 count test | MECHANICAL | count mismatch |
| .claude/commands/run-quarterly.md:103-104 | "STOP and ask the operator before a second iteration" | operator approves second loop | MECHANICAL | INCOMPLETE audit; listed as mechanical at line 136 (loop count conflict, CMD-RQ-01) |
| .claude/commands/run-quarterly.md:118-119 | "Decision Status changes only when a pre-committed trigger fires — flag, do not decide" | operator Decision Status ruling, post-run | KEEP | Decision Status; pipeline flags, does not wait |
| prompts/quarterly-00-orchestrator.md:33-35 | "absence is a hard STOP" | missing protocol file | MECHANICAL | missing file |
| prompts/quarterly-00-orchestrator.md:121-122 | "STOP and report the missing tool" | toolchain | MECHANICAL | missing tool |
| prompts/quarterly-00-orchestrator.md:140-141 | "Any page unaccounted for = STOP" | A1 coverage | MECHANICAL | extraction gap |
| prompts/quarterly-00-orchestrator.md:153-154 | "STOP and re-invoke A2 once ... second failure escalates to the human" | A2 count / orphan IDs | MECHANICAL | count mismatch |
| prompts/quarterly-00-orchestrator.md:155-156 | "STOP and diagnose before A3" | A2 token cost above A1 | MECHANICAL | source re-ingestion; missing from halt list at 312-313 |
| prompts/quarterly-00-orchestrator.md:162-163 | "Any blank check = STOP and re-invoke A3" | A3 blanks | MECHANICAL | blank check |
| prompts/quarterly-00-orchestrator.md:209-210 | "STOP and ask the operator before a second iteration" | operator approves second loop | MECHANICAL | INCOMPLETE audit; conflicts with line 313 "two loops" (ORCH-Q-01) |
| prompts/quarterly-00-orchestrator.md:258 | "Decision Status changes ONLY when a pre-committed trigger formally fires" | operator Decision Status ruling | KEEP | Decision Status; flag only, no in-run wait |
| prompts/quarterly-00-orchestrator.md:297-298 | "halt and diagnose" | downstream agent above A1 cost | MECHANICAL | discipline breach |
| prompts/quarterly-00-orchestrator.md:302-304 | "An orphaned ID ... fails the run" | completeness gate | MECHANICAL | orphan row ID |
| prompts/quarterly-00-orchestrator.md:314-315 | "If any required protocol file is absent, STOP" | missing file | MECHANICAL | duplicate of 33-35 |
| .claude/agents/quarterly-a1-extractor.md:25-26 | "Any page unaccounted for = halt and report the gap" | coverage | MECHANICAL | extraction gap |
| prompts/quarterly-a1-extractor.md:18-19 | "Page coverage 100% or you STOP and report" | coverage | MECHANICAL | GATE A1 |
| prompts/quarterly-a1-extractor.md:67 | "If pages are missing = GATE A1 gap, STOP." | coverage | MECHANICAL | GATE A1 (third copy in this file) |
| prompts/quarterly-a1-extractor.md:218-219 | "Emit the gap and stop." | coverage | MECHANICAL | GATE A1 |
| prompts/quarterly-a2-enumerator.md:22-23 | "If you find yourself needing the source document, STOP" | pipeline error | MECHANICAL | input discipline |
| prompts/quarterly-a3-forensics.md:21-22 | "If you find yourself needing the source document, STOP" | pipeline error | MECHANICAL | input discipline |
| prompts/quarterly-a4-analyst.md:25-26 | "you may NOT proceed — return the unreviewed rows and stop" | ledger rows unreviewed | MECHANICAL | coverage failure |
| prompts/quarterly-a4-analyst.md:37-38 | "If you find yourself needing the source document, STOP" | pipeline error | MECHANICAL | input discipline |
| prompts/quarterly-a4-analyst.md:101-102 | "Decision Status changes only when a pre-committed trigger formally fires; you flag, the human decides" | operator Decision Status ruling | KEEP | Decision Status |
| prompts/quarterly-a5-adversary.md:19-20 | "If you find yourself needing the source document, STOP" | pipeline error | MECHANICAL | input discipline |
| frameworks/Document_Review_Protocol_v1_1.md:60-61 | "stop and return the unreviewed rows" | ledger rows unreviewed | MECHANICAL | coverage failure |
| frameworks/Document_Review_Protocol_v1_1.md:143-145 | "A document review flags; the human decides" | operator Decision Status ruling | KEEP | Decision Status; flag only |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:26 | "If you find yourself wanting to write a verdict before completing Step 6, stop" | self-check, no operator | DROP | self-correction, not a wait; step order plus A5 audit cover it. Pipeline: not a wait |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:30 | "If you catch yourself doing any of these, STOP and restart" | self-check | DROP | self-correction, not a wait. Pipeline: not a wait |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:60 | "If Notion has no page for the company, stop and ask" | operator supplies thesis | MERGE | merge with orchestrator NOTION vs SPEAR route (orch 187-189: pre-thesis read). Pipeline: NOT obeyed; A4 never asks; conflicts (FW-R4-06) |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:115 | "STOP. Confirm Notion fetched ... Then proceed." | pre-flight confirmation | DROP | units in A1 header, notes in A2 ledger, coverage in A5 audit 1. Pipeline: NOT obeyed |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:189 | "STOP. Show the complete extraction table" | every cell filled or ND | DROP | A4 contract 2 (filled or ND) plus A5 arithmetic audit. Pipeline: NOT obeyed |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:218 | "Get explicit GO before proceeding to QoQ" | explicit operator GO | DROP | YoY math recomputed by A5 audit 2; diagnostics read at R4 Step 8 review. Pipeline: NOT obeyed; the only explicit GO in Role 4 |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:234 | "STOP. Show QoQ table and diagnostics." | review of QoQ | DROP | QoQ percentages recomputed by A5 audit 2. Pipeline: NOT obeyed |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:262 | "STOP. Present the bridge table and answers." | review of PAT bridge | DROP | A5 audit 2 recomputes the PAT bridge. Pipeline: NOT obeyed |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:317 | "STOP. Present cash quality (or asset quality) table" | review of cash table | DROP | derived ratios recomputed by A5 audit 2; INDETERMINATE cap is a rule, not a wait. Pipeline: NOT obeyed |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:361 | "STOP. Present the 5.5A tracker pull ... before proceeding to Step 6" | review of signal reconciliation and new tracker writes | MERGE | merge with R4 line 643 save confirmation (tracker write is a Notion action; no pipeline executor, FW-R4-07). Pipeline: NOT obeyed |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:398 | "If any condition has FIRED, stop and recommend immediate exit" | operator exit ruling | KEEP | thesis-broken trigger / Decision Status. Pipeline: A4 flags, no wait; orchestrator surfaces it in report |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:409 | "STOP. Present 6A through 6D in full." | review of thesis reconciliation | MERGE | merge with R4 line 522 (Step 8 position decision). Pipeline: NOT obeyed |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:431 | "STOP. Present 6.5A and 6.5B before Step 7." | review of A21 base and ledger ageing (decay trims) | MERGE | merge with R4 line 522 (decay trims are position actions). Pipeline: NOT obeyed; A4 cannot load Section 1B (ORCH-Q-07) |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:445 | "PASS / CONDITIONAL / STOP per v3.3 Amendment 2" | Hurdle verdict label | KEEP | P/E gate (Hurdle). A verdict label, not a wait. Pipeline: cannot compute without Section 1B |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:451 | "STOP. Show the pillar re-validation and any revised fair values." | review of destination PE / fair values | KEEP | P/E gate. Pipeline: NOT obeyed and not computable by A4; route to /fttcp and Role 1 |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:522 | "STOP. Present position decision, trigger refinements, and the single cleanest metric" | operator position ruling | KEEP | Decision Status. Pipeline: NOT a wait; A4 flags; operator rules after the run. This is the single end review the MERGE rows point to |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:592 | "STOP. Present the questions table, top 3 ranking, and channel recommendation." | review of management questions | MERGE | merge with R4 line 522 (one end review). A5 audit checks every FORWARD-SIGNAL/AMBIGUOUS finding has a question. Pipeline: NOT obeyed |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:641 | "inform me which sections saved successfully and which need retry" | Notion timeout | MECHANICAL | write failure |
| frameworks/Quarterly_Results_Review_Protocol_v1_4.md:643 | "STOP. Confirm save before ending the session." | save confirmation | MERGE | merge with orchestrator step 7 final report (save result goes in the report). Pipeline: orchestrator saves inline; no wait |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:99 | "STOP. Confirm Notion fetched, participants listed ... Then proceed." | pre-flight confirmation | DROP | participants and turns in A2 ledger; coverage in A5 audit 1. Pipeline: NOT obeyed |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:130 | "STOP. Show the claims inventory and the four diagnostics." | review of claims inventory | MERGE | merge with R5 line 547 (Step 8 position decision, one end review). Pipeline: NOT obeyed |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:184 | "STOP. Show the guidance table ... be thorough." | review of guidance table | MERGE | merge with R5 line 547. Pipeline: NOT obeyed; "be thorough" is old phrasing (FW-R5-01) |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:256 | "STOP. Show 3A through 3E." | review of credibility ratio and grade | MERGE | merge with R5 line 547 (the ratio feeds the position decision; A5 audit 2 can recompute the ratio). Pipeline: NOT obeyed |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:307 | "STOP. Show 4A, 4B, and 4C." | review of Q&A decomposition | MERGE | merge with R5 line 547. Pipeline: NOT obeyed |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:353 | "STOP. Show 5A and 5B." | review of new info / silence | MERGE | merge with R5 line 547. Pipeline: NOT obeyed |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:421 | "STOP. Show 6A through 6E." | review of tone, specificity ratio, archetype | DROP | specificity ratio is derived arithmetic A5 audit 2 recomputes; archetype reads at R5 line 547. Pipeline: NOT obeyed |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:468 | "STOP. Show 7A, 7B, 7C." | review of cross-reference | MERGE | merge with R5 line 547. Pipeline: NOT obeyed; 7B/7C peer inputs not passed (FW-R5-05) |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:524 | "Trim 25% immediately pending fuller assessment" | position action | KEEP | Decision Status / position ruling inside Step 8E. Pipeline: flagged only |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:547 | "STOP. Show 8A through 8F." | operator thesis / position ruling | KEEP | Decision Status, thesis-broken check, pillar inputs. Pipeline: NOT a wait; A4 flags, operator rules after the run |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:595 | "inform which sections saved successfully" | Notion timeout | MECHANICAL | write failure |
| frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md:597 | "STOP. Confirm save." | save confirmation | MERGE | merge with R4 line 643 and orchestrator step 7 final report. Pipeline: no wait |
| Master:51 | "verify the sector has three verified-qualifying entries before proceeding" | Operator's Sector Literacy log before Medium/Large sizing | KEEP | Operator-held data gating a sizing decision |
| Master:100 | "I will tell you which one I need" | Operator to name the role | DROP | Pipeline task message already names the role; chat-only |
| Master:132 | "STOP after each and wait for my \"GO\"" | GO after every Role 1 section | MERGE | Umbrella for 574/694/803; see G4-MST-18 |
| Master:138 | "If no FTTCP output exists for this company, STOP and run FTTCP first" | Missing upstream FTTCP output | MECHANICAL | Missing input |
| Master:574 | "Section 1 complete ... Hurdle Ratio ... Type GO." | GO after destination PE and Hurdle | MERGE | With the /fttcp pillar-approval gate (operator approves destination PE base and earnings basis there, A20.9); HR caps nothing per OR-2 |
| Master:694 | "Section 2 complete. Projections built ... Type GO." | GO after projections | DROP | Verifier C audits projections; no operator ruling |
| Master:803 | "Section 3 complete ... Type GO." | GO after method application | DROP | Arithmetic re-confirmation; Verifier C checks |
| Master:942 | "🛑 Say: \"Valuation complete...\"" | Nothing (end summary) | DROP | Not a wait; keep the summary line, drop the stop glyph |
| Master:1195 | "If any is missing, STOP and return to Role 2." | Bull case built to depth (Rule H) | KEEP | CLAUDE.md Rule H binds. Note: stage-15 wrapper says "Where the framework says STOP ... continue immediately", which conflicts with this stop; outside G4 files, flag to the wrapper audit |
| Master:1426 | "No FTTCP, no Role 1, no Role 2 may begin until this gate passes." | Tracker rows written with URLs | KEEP | Role 5.5 hard gate, post-Halt-1 claude.ai step per CLAUDE.md; executor unnamed (G4-MST-20) |
| Master:1444 | "the workup PAUSES at this gate" | Notion write to succeed | MERGE | Same gate as Master:1426 |
| Master:1517 | "Verify position status (Notion Decision Status) before any HOLD/ADD/TRIM/EXIT framing" | Decision Status lookup | KEEP | Decision Status is an operator field |
| Master:1519 | "no FTTCP, Role 1, or Role 2 may begin ... If the write fails, the workup pauses" | Same tracker gate | MERGE | Duplicate of Master:1426 (G4-MST-25) |
| chunk 09:28 | "A catalyst table with no downside row is REJECTED ... halts like a missing input" | Downside row present | MECHANICAL | Incomplete input |
| chunk 09:8 | "probability ... assigned by the operator" | Operator catalyst probabilities | MERGE | With the /fttcp pillar-approval gate (one operator review of probabilities, basis and base) |
| chunk 10:21 | "Where the operator approved an earnings basis at the FTTCP pillar-approval gate" | Operator-approved earnings basis | MERGE | With the /fttcp pillar-approval gate |
| chunk 10:44 | "The conditional probability is an operator input at the gate" | Conditional option probability | MERGE | With the /fttcp pillar-approval gate |
| chunk 15:96 | "value on the approved base unless the operator re-rules" | Operator re-rule if Step 1C diverges | KEEP | P/E gate (/fttcp pillar-approval gate); this is the anchor the other gate items merge into |
| chunk 05:106 | "the operator re-rules the cap" | Annual cap re-rule | KEEP | Operator cap ruling, maintenance not per-run; never blocks a run |
| chunk 16:10 | "Role 5.5's Step 4 HARD GATE must have passed" | Tracker rows written | MERGE | Same gate as Master:1426 |
| chunk 16:18 | "Three or more missing → declare FTTCP inconclusive" | Missing source documents | MECHANICAL | Missing input; proceeds at low confidence |
| chunk 17:18 | "Role 3 does not run unless this line declares a forward basis" | Rule H precondition | MERGE | Same stop as Master:1195 |
| chunk 11:41 | "ceiling verdict WATCHLIST ... named resolving condition" | Input leaves top quintile | KEEP | A17.4 entry gate (A17 gate, verdict ceiling not a halt) |
| FTTCP:36 | "its Step 4 HARD GATE must have passed" | Role 5.5 tracker rows written in claude.ai, row URLs as proof | MERGE | merge with the /fttcp pre-flight check (signed Mental Model + Halt 1 PROCEED) so the operator confirms hand-offs once; same gate as DSD:147 |
| FTTCP:112 | "declare FTTCP inconclusive and request additional inputs" | operator supplies missing sources (3+ missing) | MERGE | merge with Halt 1 corpus-gap resolution; the "proceed with low-confidence verdict" branch already exists |
| FTTCP:262 | "the number is the operator's call" | operator sets each catalyst probability | MERGE | merge with the FTTCP pillar-approval gate (v3.9 20.9) |
| FTTCP:265 | "A catalyst table with no downside row is REJECTED" | a downside row | MECHANICAL | text itself says it "halts like a missing input" |
| FTTCP:365 | "override-worthy specific catalyst ... documented in Notion" | operator override of the mechanical verdict | KEEP | operator ruling |
| FTTCP:515 | "Role 3 must have stress-tested the override before it is committed" | Role 3 test, then operator commits Category-Break Override | KEEP | sector-cap override is an operator ruling |
| FTTCP:562 | "update the row property ... immediately" | none (auto-writes Decision Status) | KEEP | should be an operator Decision Status ruling; see G5-FTTCP-08 |
| AR:19 | "STOP and fetch it before reading the AR" | Notion thesis fetched | MECHANICAL | missing input |
| AR:93 | "If Notion has no page for the company, STOP and ask." | operator supplies thesis baseline | MECHANICAL | missing input; duplicated at AR:1347 |
| AR:129 | "STOP. Confirm Notion fetched ... Then proceed." | self-check | MERGE | merge with AR:172 (one pre-flight + inventory review) |
| AR:168 | "Going Concern flag → STOP analysis" | analysis halts on quality | DROP | quality halt; propagate as flag to Step 13 overlay (MEANING-RISK, G5-AR-10) |
| AR:172 | "Get explicit GO before proceeding." | operator GO after inventory | MERGE | merge with AR:1044 (single operator review at the FTTCP refresh gate) |
| AR:234 | "STOP. Show 2A through 2D. Wait for GO." | operator GO | MERGE | merge with AR:1044 |
| AR:306 | "STOP. Show the P&L table" | presentation | MERGE | merge with AR:1117 |
| AR:334 | "STOP. Show 3L in full." | presentation | MERGE | merge with AR:1117 |
| AR:382 | "STOP. Present cash flow table and answers." | presentation | MERGE | merge with AR:1117 |
| AR:400 | "STOP. Present 4L." | presentation | MERGE | merge with AR:1117 |
| AR:482 | "STOP. Present 5A through 5D." | presentation | MERGE | merge with AR:1117 |
| AR:519 | "STOP. Present 5L-A through 5L-D." | presentation | MERGE | merge with AR:1117 |
| AR:653 | "STOP. Present Pass 1 list" | presentation | MERGE | merge with AR:1117 |
| AR:690 | "STOP. Present the chains." | presentation | MERGE | merge with AR:1117 |
| AR:782 | "STOP. Present 7A through 7D." | presentation | MERGE | merge with AR:1117 |
| AR:861 | "STOP. Present 8A through 8E." | presentation | MERGE | merge with AR:1117 |
| AR:902 | "STOP. Present 9A through 9F." | presentation | MERGE | merge with AR:1117 |
| AR:960 | "STOP. Present 10A through 10D." | presentation | MERGE | merge with AR:1117 |
| AR:1023 | "STOP. Present 10.5A cross-check" | presentation | MERGE | merge with AR:1117 |
| AR:1044 | "STOP. Present the gate table and the FTTCP disposition" | operator rules re-run vs carry-forward of FTTCP | KEEP | gates any Pillar 1 change (FTTCP sole authority) |
| AR:1062 | "PASS / CONDITIONAL / STOP" | none | DROP | band label only; caps no verdict per OR-2 |
| AR:1093 | "stop the protocol and recommend immediate exit" | operator exit decision | KEEP | thesis-broken exit is a Decision Status ruling; wording question G5-AR-10 |
| AR:1117 | "STOP. Present 11A through 11G." | presentation | MERGE | merge with AR:1263 |
| AR:1169 | "STOP. Present 12A through 12C." | presentation | MERGE | merge with AR:1263 |
| AR:1263 | "STOP. Present 13-H or 13-W" | operator position decision | KEEP | Decision Status |
| AR:1341 | "STOP. Confirm save before ending the session." | Notion write confirmation | MECHANICAL | write confirmation, not a ruling |
| 1B33:36 | "STOP — overvalued" | none | DROP | band label only per OR-2 |
| 1B33:179 | "unless the operator documents an override in the thesis" | operator sizing override (Tier B) | KEEP | operator ruling |
| 1B33:119 | "adjust caps if you disagree" | operator cap review | DROP | adopted 02-Jul-2026; stale invitation (G5-1B33-07) |
| 1B36:3 | "wiring is a pending operator decision" | operator wiring decision | DROP | resolved: skill now carries v3.6 (G5-1B36-01) |
| 1B36:91 | "No Pillar 3 growth premium ... before projected ROCE crosses" | B2 crossover flag | KEEP | Amendment 16 gate |
| 1B37:11 | "Classification gate. Every Section 1B derivation states upfront" | CONVERTER call | KEEP | Amendment 17 gate |
| 1B37:19 | "ceiling verdict WATCHLIST regardless of margin of safety" | input exits top quintile | KEEP | Amendment 17 entry gate |
| 1B38:32 | "an operator input at the gate" | operator conditional probability | KEEP | Amendment 18 gate; held at the FTTCP pillar-approval gate |
| 1B38:81 (20.6) | "flagged to the operator for a re-rule" | operator cap re-rule | MERGE | duplicate of 1B39:48; drop with the v3.8 Amendment 20 supersession |
| 1B39:48 | "the cap is re-ruled by the operator against the live median" | annual operator cap ruling | KEEP | sector cap ruling (maintenance, not per run) |
| 1B39:58 | "value on the approved base unless the operator re-rules" | operator re-rule at FTTCP pillar-approval gate | KEEP | P/E gate |
| 1B39:79 | "probability (0.00-1.00) assigned by the operator" | operator probabilities | MERGE | merge with 1B39:58 pillar-approval gate |
| 1B39:208 | "is **operator-only** and is not set here" | operator Decision Status | KEEP | Decision Status |
| 1B39:212 | "RULINGS REQUIRED FROM OPERATOR BEFORE STAGE 11" | E2E R1-R4 | KEEP | genuine sector-cap and Decision Status rulings; belongs in companies/E2E.md (G5-1B39-03) |
| DCA:83 | "The verdict never halts a run." | none | n/a | explicit no-stop; listed for completeness |
| MIA:77 | "The flag never halts a run" | none | n/a | explicit no-stop; listed for completeness |
| DSD:147 | "Role 5.5 Step 4 (the tracker write gate)" | verified rows written to tracker | KEEP | hand-off gate in claude.ai; FTTCP:36 merges here |
| README:2 | "stage 11 halts without them" | framework files present | MECHANICAL | missing file |
| README:46 | "the A4 analyst halts without the one its docs require" | protocol file present | MECHANICAL | missing file |
| README:53 | "/run-quarterly STOPS and reports" | protocol file present | MECHANICAL | missing file |

## All findings by file

### `"# Model:" header lines in every prompt`

- **X-04**: severity low, class M, duplication, line 01:2, 02:2, 03:2, 04:2, 05:2, 06:2, 07:2, 08:2, 09:2, 09b:2, 10:2, 11:2, 12:36, 12:124, 12:200, 12:378, 13:2; YAML `model:` literals 01:172, 02:179, 03:183, 04:90, 05:102, 06:133, 07:220, 08:128, 09:129, 09b:314, 10:97, 12:106, 12:407
  - Current:
    > # Model: Sonnet 5.5 | Emits: B01-gate0
  - Proposed:
    > # Model: per .claude/agents frontmatter (currently Sonnet 5.5) | Emits: B01-gate0
  - Why: all match today, but the prompt states which model it runs on in two places per file; CLAUDE.md says the agent file is the only place to change a model, so the prompt copy should point there.

### `.claude/agents/quarterly-a1-extractor.md`

- **AG-A1-01**: severity low, class Q, duplication, line 15
  - Current:
    > Non-negotiables:
  - Proposed:
    > QUESTION: Lines 16-60 restate prompts/quarterly-a1-extractor.md almost rule for rule, so both load every A1 run. Cut the agent body to the pointer (lines 7-13) plus the block-file rule (lines 56-60), which the prompt lacks?
  - Why: Same rules twice per invocation; any later edit to one copy creates drift.

### `.claude/agents/quarterly-a2-enumerator.md`

- **AG-A2-01**: severity low, class Q, duplication, line 15
  - Current:
    > Non-negotiables:
  - Proposed:
    > QUESTION: Same as AG-A1-01. Keep the pointer and the block-file rule (lines 30-34); cut lines 16-29 that restate the prompt?
  - Why: Duplicate load on the agent meant to be the cheapest in the chain.

### `.claude/agents/quarterly-a3-forensics.md`

- **AG-A3-01**: severity low, class A, other, line 18
  - Current:
    > - Read ONLY A1's structured extraction and fulltext plus the A2 ledger; never
  - Proposed:
    > - Read ONLY A1's structured extraction and fulltext, the A2 ledger, and the prior-quarter fulltext and Notion checklist your task message passes; never
  - Why: The prompt's INJECTED INPUTS (lines 206-207) pass a prior-quarter extract and the Notion checklist, which "ONLY" here excludes.
- **AG-A3-02**: severity low, class Q, duplication, line 16
  - Current:
    > Non-negotiables:
  - Proposed:
    > QUESTION: Same as AG-A1-01. Keep pointer and block-file rule (lines 32-36); cut the restated rules?
  - Why: Duplicate load on an Opus effort-high agent.

### `.claude/agents/quarterly-a4-analyst.md`

- **AG-A4-01**: severity low, class Q, duplication, line 20
  - Current:
    > Non-negotiables:
  - Proposed:
    > QUESTION: Same as AG-A1-01. Keep pointer, protocol-scoping sentence (lines 14-18) and block-file rule (lines 37-41); cut the restated rules?
  - Why: Duplicate load on an Opus effort-high agent.

### `.claude/agents/quarterly-a5-adversary.md`

- **AG-A5-01**: severity medium, class B, contradiction, line 17
  - Current:
    > - Complete all three audits (coverage, arithmetic, adversarial) in one run.
  - Proposed:
    > - Complete all four audits (0 deliverable-completeness, 1 coverage, 2 arithmetic, 3 adversarial) in one run.
  - Why: The prompt has four audits with audit 0 as a hard gate; "three" invites skipping the brief check.

### `.claude/agents/stage-01 ... verifier-d (shared template) + every prompts/0x-13 "No stops" line`

- **X-01**: severity low, class M, duplication, line agent files line 16 (stage-01..10, 13 at 16/17, verifier-a/b/c/d at 16/17); prompt lines 01:11, 02:16, 02:98, 03:20, 04:15, 05:15, 06:20, 07:28, 08:18, 09:21, 09b:26, 10:15, 12:44, 12:132, 12:221, 12:386
  - Current:
    > - Complete the entire stage in one run. Never stop to ask for confirmation.
  - Proposed:
    > 1. Execute the ENTIRE scorecard in one response. Do not stop for
    >    confirmation at any point. There is no human in this loop.
  - Why: the same no-stop rule is stated twice per stage (agent and prompt), sometimes three times (02, 12); one statement does the job.

### `.claude/agents/stage-02-notes-pass.md`

- **AG-02**: severity medium, class B, stale-ref, line 10-11
  - Current:
    > Read that file FIRST with the Read tool. Everything above its
    > "INJECTED INPUTS" section is your operating rules; follow them exactly.
  - Proposed:
    > Read that file FIRST with the Read tool. Your task message names the pass
    > (CALL 1, 2 or 3). Follow that CALL's rules; the text at its {{...}} markers
    > arrives in your task message.
  - Why: prompts/02 has no "INJECTED INPUTS" section; its inputs sit mid-file between the three CALL blocks, so "everything above" is undefined.

### `.claude/agents/stage-09b-dossier.md`

- **AG-09B-01**: severity medium, class B, duplication, line 15-26
  - Current:
    > - Assembly only: build from the committed blocks and stage reports given to
    >   you. No web search, no new numbers, no re-analysis.
  - Proposed:
    > - Assembly only, with the two scoped exceptions (Section 4e chains, Section 6
    >   annex) exactly as prompts/09b-halt1-dossier.md rule 2 states them.
  - Why: the agent restates rules 2, 4 and 5 of prompt 09b nearly word for word (and omits the Section 6 annex exception, so the agent copy reads stricter than the prompt); one authoritative copy avoids the drift already visible.

### `.claude/agents/stage-11-valuation.md`

- **AG-11-01**: severity low, class M, duplication, line 17-22
  - Current:
    > The section-1b skill is preloaded in your context. It carries the resolved
  - Proposed:
    > delete lines 17-22 (prompts/11 lines 3-14 state the same skill-first, source-wins rule).
  - Why: identical rule in two files; prompt 11 is the single source of truth per CLAUDE.md STRUCTURE.

### `.claude/agents/stage-14-thesis.md`

- **AG-14-01**: severity low, class A, other, line 15-16
  - Current:
    > in this wrapper ever conflict, THE INJECTED FRAMEWORK WINS. The framework
  - Proposed:
    > in this wrapper ever conflict, the framework file wins. The framework
  - Why: the framework is read from frameworks/, not injected; ALL-CAPS adds nothing.

### `.claude/agents/stage-15-devil.md`

- **AG-15-01**: severity medium, class B, contradiction, line 27-29
  - Current:
    > - Complete the entire role in one run. Never stop to ask for confirmation.
    >   Where the framework says STOP and report interim state, WRITE that
    >   interim line then continue immediately.
  - Proposed:
    > - Complete the entire role in one run. Never stop to ask for confirmation.
    >   Where the framework says STOP and report interim state, WRITE that
    >   interim line then continue immediately. The one exception is the
    >   STEELMAN GATE below: if it fails, return the gate table and write nothing else.
  - Why: line 83 ("If any is missing, STOP") contradicts "continue immediately" two screens earlier; the model must know which wins.
- **AG-15-02**: severity low, class A, other, line 16
  - Current:
    > and anything in this wrapper ever conflict, THE INJECTED FRAMEWORK WINS.
  - Proposed:
    > and anything in this wrapper ever conflict, the framework file wins.
  - Why: same as AG-14-01.

### `.claude/agents/verifier-a-numerical.md`

- **AG-VA-01**: severity medium, class A, duplication, line 78-83
  - Current:
    > - You are the pipeline's SOLE, FINAL, cross-family authority on source fidelity:
  - Proposed:
    > - Source-fidelity findings are a hard, non-overridable gate: apply rule 7 of
    >   your VERIFIER A section and mark each with `source_fidelity: true`.
  - Why: the same gate text appears in this agent, prompt 12 header (21-32), prompt 12 rule 7 (86-93), orchestrator (591-605) and prompt 13 (116-124); five copies for one rule invites drift.

### `.claude/agents/verifier-a/b/c/d (shared)`

- **AG-V-01**: severity medium, class M, stale-ref, line verifier-a 11, verifier-b 12, verifier-c 12, verifier-d 11
  - Current:
    > "INJECTED INPUTS" section is your operating rules; follow them exactly.
  - Proposed:
    > "INPUTS:" line in your section is your operating rules; follow them exactly.
  - Why: prompts/12 has no INJECTED INPUTS heading; each verifier section ends with an "INPUTS:" line instead.

### `.claude/commands/compost.md`

- **CMD-COMPOST-01**: severity low, class A, stale-ref, line 51
  - Current:
    > BUDGET REVIEW (Point 7, mandatory on every promotion). The active LESSONS.md
  - Proposed:
    > BUDGET REVIEW (mandatory on every promotion). The active LESSONS.md
  - Why: "Point 7" points at no numbered list in this file or CLAUDE.md.
- **CMD-COMPOST-02**: severity low, class A, other, line 60
  - Current:
    > Do not commit or push unless the operator asks.
  - Proposed:
    > Do not commit or push unless the operator asks. If you commit an applied fix, keep it on a framework branch apart from run outputs and open a PR to main the same day (CLAUDE.md SESSION DISCIPLINE).
  - Why: compost edits prompt files; CLAUDE.md requires a same-day PR for any committed amendment, which this file does not mention.

### `.claude/commands/finalize.md`

- **CMD-FIN-01**: severity medium, class Q, contradiction, line 37-43 (whole file)
  - Current:
    > table allows. After each stage returns, validate its YAML block and commit
    > before proceeding.
  - Proposed:
    > QUESTION: CLAUDE.md FERRY AND COMMIT HYGIENE says "Every run ends with session-cost.md (see run-pipeline close-out)". /finalize has no per-stage ledger and no close-out summary, so the stage 10 haiku DOWNSHIFT check never runs anywhere. Should /finalize append to the run's session-cost.md per stage and run the same close-out summary before step 9?
  - Why: the only haiku stage of phase 3 (stage 10) is never cost-checked, and the CLAUDE.md "every run" rule is unmet.
- **CMD-FIN-02**: severity medium, class Q, contradiction, line 319-322 and 340-342
  - Current:
    > FINALIZE GATE (team workflow v2 — hash by default). End the report with
    > the commit hash and the output of `git log -1 --stat`
  - Proposed:
    > QUESTION: the report must "End ... with the commit hash and `git log -1 --stat`", but the same step later says "End with exactly: Files committed. Ask me anything ...". Should the order be: report, hash and `--stat`, printed finals, then the fixed closing line? If yes, change "End the report with" to "Close the report section with".
  - Why: two "end with" rules in one step.
- **CMD-FIN-03**: severity medium, class Q, contradiction, line 141-146 and 69-72
  - Current:
    > proceed AUTONOMOUSLY through every step
    > below in one run, no stops.
  - Proposed:
    > QUESTION: CLAUDE.md line 35-38 (Master v3.7 Rule H) says never run Role 3 against a bull case not built to depth, and "If one is missing, STOP and return to Role 2". Step 4 runs stage 15 straight after stage 14 with no Rule H check, and line 72 says "no stops". Should step 4 open with the Rule H check (forward basis, margin bridge, five chains, Entrepreneur Ledger in B14) and loop back to stage 14 on a miss?
  - Why: the file's "no stops" contradicts a binding CLAUDE.md STOP.
- **CMD-FIN-04**: severity low, class A, other, line 37-43
  - Current:
    > EXECUTION DISCIPLINE: invoke every stage as a foreground subagent call
  - Proposed:
    > EXECUTION DISCIPLINE: as in .claude/commands/run-pipeline.md, including the PROVE COMPLETION checks (report file exists and is not empty, block file exists and parses, block came from this invocation) before any later stage reads the output.
  - Why: run-pipeline.md line 79-99 added the completion proof after background-dispatch failures; finalize runs the same pattern without it.
- **CMD-FIN-05**: severity low, class A, stale-ref, line 222
  - Current:
    > full save content structured per Notion_Save_Instructions conventions:
  - Proposed:
    > full save content structured per the claude.ai notion-save conventions (Notion_Save_Instructions, held in the claude.ai project, not in this repo):
  - Why: no Notion_Save_Instructions file exists in the repo; the reader cannot open it.
- **CMD-FIN-06**: severity low, class B, stale-ref, line 148-150
  - Current:
    > verifier-c-framework with the framework docs and B10, B11 for its
  - Proposed:
    > verifier-c-framework with B10, B11, frameworks/Master_Project_Prompt_v3_6.md (Master v3.7) and the section-1b skill chunks cited in B11, for its
  - Why: "the framework docs" is unnamed; stage 11 now runs off the section-1b skill and Verifier C check 15 compares cited chunks with sources.
- **CMD-FIN-07**: severity low, class M, duplication, line 344-358
  - Current:
    > - Hash by default: end any report that involves a commit with the hash and
  - Proposed:
    > Cut the last three rules (hash, dependency alignment, self-contained ferry); CLAUDE.md FERRY AND COMMIT HYGIENE already binds and step 9 restates the hash rule.
  - Why: third copy of the same rules in one session context.

### `.claude/commands/fttcp.md`

- **CMD-FTTCP-01**: severity high, class Q, contradiction, line 48-52
  - Current:
    > Two gates guard the entry to deliberation. Check both after name
  - Proposed:
    > QUESTION: CLAUDE.md SPEAR GATE (line 205-215) and 00-orchestrator.md line 156 say /fttcp on a new name requires a Spear HIT or OVERRIDE line in companies/<TICKER>.md, else STOP. fttcp.md lists only two preconditions and does not read 00-orchestrator.md. Should a third precondition "SPEAR GATE" be added here with the CLAUDE.md wording?
  - Why: the one command CLAUDE.md names besides /run-pipeline for the spear gate never checks it.
- **LEAD-01**: severity high, class Q, other, line 4
  - Current:
    > model: claude-opus-5-5
  - Proposed:
    > QUESTION: /fttcp pins `model:` in its command frontmatter with no effort. Invoked from a session on any other model, it switches the session model mid-session, which empties the prompt cache (CLAUDE.md SESSION DISCIPLINE). Delete the line and require the session to start on Opus 5.5 at the ruled effort (a), or keep it as a guard (b)?
  - Why: a command-level model line is a mid-session model switch whenever the session model differs; CLAUDE.md fixes model and effort at session start.
- **CMD-FTTCP-02**: severity medium, class Q, contradiction, line 3
  - Current:
    > model: claude-opus-5-5
  - Proposed:
    > QUESTION: CLAUDE.md DISPATCH says /fttcp runs on Opus 5.5 effort high, but this frontmatter sets no effort. CLAUDE.md SESSION DISCIPLINE also says the session model never changes mid-session, while a command `model:` line switches the session model when /fttcp starts in a session opened on another model. Keep the line and add `effort: high`, or remove it and require /fttcp to start in a fresh Opus 5.5 high session?
  - Why: frontmatter and DISPATCH disagree on effort, and the model line can bust the prompt cache that SESSION DISCIPLINE protects.
- **CMD-FTTCP-03**: severity medium, class Q, contradiction, line 378-380 and 476-478
  - Current:
    > written, and end with this line and nothing after it:
  - Proposed:
    > QUESTION: line 378-380 says the draft message ends with "Ask me anything or give me your overrides." and nothing after it; line 476-478 says the final message ends with "REMINDER — MERGE THIS BRANCH BEFORE STARTING ANY FTTCP SESSION." Is the REMINDER for the sign-off message only (after fttcp-deliberation.md is committed)? If so, write "End your sign-off message (after the deliberation commit) with, on its own line:".
  - Why: two "end with" rules collide on the draft message.
- **CMD-FTTCP-04**: severity medium, class M, contradiction, line 373-377 and 447
  - Current:
    > `fttcp: autonomous plain-language draft` and push with
  - Proposed:
    > Add after the push: "End the commit report with the commit hash and `git log -1 --stat`." Same at line 447 for the deliberation commit.
  - Why: CLAUDE.md "Hash by default" applies to every commit report; neither /fttcp commit asks for the hash.
- **CMD-FTTCP-05**: severity medium, class Q, contradiction, line 228-230 and 396-397
  - Current:
    > close every still-open call by the standing conservative rule (round DOWN
  - Proposed:
    > QUESTION: CLAUDE.md NEVER (v3.9 Amendment 25) bars shading an input to be safe in Role 1 projections. Line 396-397 defines the default-track sensitivity as "the more conservative of the two drafts", and that number travels into the Phase 3 valuation record. Is "more conservative" the intended default track, or should it read "the Claude Code draft" (or "the most evidenced draft")? The FTTCP round-DOWN rule at line 228 is FTTCP's own and is not questioned.
  - Why: possible collision between a "conservative" default and Amendment 25 where the P/E base card feeds Role 1.
- **CMD-FTTCP-06**: severity medium, class Q, contradiction, line 54-57
  - Current:
    > run's notion-payload must record downstream tracker rows written with
    > row-URL proof for this ticker.
  - Proposed:
    > QUESTION: team_workflow_project_instructions.md line 93 defines the Role 5.5 tracker gate as "minimum three EXTERNAL signals per entity (company-narrated rows do not count toward the floor)". This precondition checks only for rows with row-URL proof. Should the precondition carry the three-external-per-entity floor?
  - Why: the two texts state different pass conditions for the same gate.
- **CMD-FTTCP-07**: severity medium, class Q, other, line 127-139
  - Current:
    > frameworks/Section_1B_v3_10_Amendments.md — read ALL SEVEN layers in this
  - Proposed:
    > QUESTION: the section-1b skill (SKILL.md chunk table names /fttcp as a consumer of chunk 05 and others) carries the resolved v3.3-v3.10 set. Should /fttcp load the relevant skill chunks instead of all seven raw layer files, as stage 11 does?
  - Why: seven full amendment files are loaded every /fttcp session; the resolved skill already exists for this purpose and cites chunks Verifier C can check.
- **CMD-FTTCP-08**: severity low, class B, contradiction, line 82-84
  - Current:
    > and report "dossier missing" for a run that PASSED the Understanding Gate,
    > and ask the operator.
  - Proposed:
    > and report "dossier missing" for a run that PASSED the Understanding Gate. Name the expected path inputs/research/web-handover-dossier.md.
  - Why: "ask the operator" conflicts with line 14 "You ask the operator NOTHING before the draft"; the STOP plus report already hands the decision over.
- **CMD-FTTCP-09**: severity low, class A, duplication, line 140
  - Current:
    > 3. CLAUDE.md — the operating rules (NEVER list, dispatch, words, STYLE).
  - Proposed:
    > 3. CLAUDE.md is already in context; do not re-read it.
  - Why: CLAUDE.md loads at session start; a re-read spends tokens for no new content.
- **CMD-FTTCP-10**: severity low, class A, stale-ref, line 20
  - Current:
    > section stops and by jargon-dense drafts (LESSONS 2026-07-09); the fix is a
  - Proposed:
    > section stops and by jargon-dense drafts (LESSONS_ARCHIVE.md 2026-07-09); the fix is a
  - Why: the 2026-07-09 entry lives in LESSONS_ARCHIVE.md line 122, not the active LESSONS.md.
- **CMD-FTTCP-11**: severity low, class A, stale-ref, line 152
  - Current:
    > (B00-B13, confidence). B04-bizmodel.yaml is the business-type and
  - Proposed:
    > (B00-B09, B09b, B12a-B12d, B13-lite, confidence). B04-bizmodel.yaml is the business-type and
  - Why: at /fttcp time B10 and B11 do not exist (they are Phase 3), so "B00-B13" implies blocks that cannot be present.
- **CMD-FTTCP-12**: severity low, class M, old-phrasing / duplication, line 12-14, 27-28, 42, 233-234, 453-454
  - Current:
    > ## THIS COMMAND IS AUTONOMOUS — ZERO QUESTIONS
  - Proposed:
    > Keep the rule once in the heading section and once in NEVER; cut the restatements at line 27-28 ("you never turn a call into a question") and 233-234 ("never a reason to ask the operator").
  - Why: the same no-questions rule appears five times in caps-heavy form; current models follow it from one plain statement.
- **CMD-FTTCP-13**: severity low, class A, old-phrasing, line 116
  - Current:
    > ## LOAD ORDER (read all of this before writing a word)
  - Proposed:
    > ## LOAD ORDER (read before drafting)
  - Why: "before writing a word" repeats at line 48 and 142; one statement suffices.

### `.claude/commands/run-pipeline.md`

- **CMD-RP-01**: severity high, class Q, contradiction, line 393-395
  - Current:
    > DISPATCH routes to haiku (stage 0 validation, stage 10 assembly,
    > verifier A)
  - Proposed:
    > QUESTION: CLAUDE.md DISPATCH routes only stage 10 and verifier A to haiku, and line 134 says "VALIDATE (stage 0, do this yourself)", so stage 0 runs inline on the session model. Stage 10 also never runs in phase 1. Which do you want: (a) list only verifier A as the phase-1 mechanical stage and exclude inline stage 0 from the downshift check, or (b) give stage 0 a haiku agent file plus a DISPATCH line? LESSONS.md OPEN ACTIONS (ORCHPHARMA, item 6) already records this conflict.
  - Why: as written, every phase-1 run either reports a false DOWNSHIFT FAILURE for stage 0 (it runs on the Opus orchestrator by design) or tempts the orchestrator to dispatch stage 0 to a haiku agent that does not exist; stage 10 cannot appear in a phase-1 ledger at all.
- **CMD-RP-02**: severity medium, class A, stale-ref, line 286
  - Current:
    > NOT pass the valuation framework docs (Master Prompt v3.6, Section
  - Proposed:
    > NOT pass the valuation framework docs (Master Prompt v3.7 at frameworks/Master_Project_Prompt_v3_6.md, Section
  - Why: names the live authority by the old version label; the file banner reads Version 3.7.
- **CMD-RP-03**: severity medium, class B, contradiction, line 418-422
  - Current:
    > and report to the user: the corpus verdict and fragility verdict from
  - Proposed:
    > Add after the report list: "End the report with the commit hash and the output of `git log -1 --stat`; if the run made per-stage commits, list each hash, newest last."
  - Why: CLAUDE.md FERRY AND COMMIT HYGIENE requires every commit report to end with the hash and `git log -1 --stat`; finalize.md and step1.md carry this, run-pipeline step 7 does not.
- **CMD-RP-04**: severity medium, class B, contradiction, line 120-124
  - Current:
    > D and the Gate 0 + EM half of verifier C, then a synthesis-lite. Ends by
    > handing off to /fttcp for deliberation.
  - Proposed:
    > D and the Gate 0 + EM half of verifier C, then a synthesis-lite and the 09b dossier. Ends at HALT 1; /fttcp runs only after the operator signs the Mental Model, records PROCEED, and the Role 5.5 tracker gate is met.
  - Why: the summary skips Halt 1 and the claude.ai verification step, contradicting CLAUDE.md PIPELINE SEQUENCE and this file's own step 7 Halt 1 message.
- **CMD-RP-05**: severity low, class A, stale-ref, line 123-124
  - Current:
    > - PHASE 2: /fttcp runs/<folder> — operator deliberation, writes
  - Proposed:
    > - PHASE 2: /fttcp runs/<folder> — autonomous FTTCP draft, then operator review and the P/E base approval gate; writes
  - Why: /fttcp is now an autonomous draft followed by review (fttcp.md line 12), not section-by-section deliberation.
- **CMD-RP-06**: severity low, class B, contradiction, line 232-233
  - Current:
    > declared, not accidental. This is the single permitted question in
    > the pipeline.
  - Proposed:
    > declared, not accidental. This is the single permitted question before Halt 1, apart from name-resolution ambiguity.
  - Why: line 16 also asks ("list the matches and ask"), and step1.md line 24-25 speaks of "two interactive pauses", so "single ... in the pipeline" is false as written.
- **CMD-RP-07**: severity low, class A, other, line 131-134
  - Current:
    > Read prompts/00-orchestrator.md now; it is the authority on sequence,
  - Proposed:
    > Read prompts/00-orchestrator.md now; it is the authority on sequence, and its SPEAR GATE check runs before the stage 0 inventory below.
  - Why: the SPEAR GATE STOP (CLAUDE.md line 215) is invisible in this command file; it lives only in 00-orchestrator.md line 153, and step1.md line 139-140 refers to "the Phase 1 SPEAR GATE check" as if it were here.
- **CMD-RP-08**: severity low, class A, other, line 31-33
  - Current:
    > session-start hook runs a PDF tooling preflight and reports its result in
    > session context. Read that line first.
  - Proposed:
    > session-start hook runs a PDF tooling preflight on web sessions and reports its result in session context. Read that line first if present; on a local session there is none.
  - Why: session-start.sh line 80-86 exits before pdf_preflight when CLAUDE_CODE_REMOTE is not true, so /step1 on desktop never gets that line.
- **CMD-RP-09**: severity low, class A, old-phrasing, line 79-82
  - Current:
    > PROVE COMPLETION, DO NOT ASSUME IT. Stages have repeatedly been dispatched
  - Proposed:
    > PROVE COMPLETION. A returned call is not a finished stage. Before any later stage reads a stage's output:
  - Why: the 4-line backstory repeats the foreground rule at line 73-77; the checklist that follows does the work.

### `.claude/commands/run-quarterly.md`

- **CMD-RQ-01**: severity high, class Q, contradiction, line 136
  - Current:
    > audit after two loops. Company quality never halts.
  - Proposed:
    > QUESTION: Line 103-104 caps the A5 correction loop at ONE iteration, then STOP and ask the operator. Line 136 lists "INCOMPLETE audit after two loops" as the halt. Which count is the rule? (The orchestrator prompt carries the same split at lines 207-210 vs 313.)
  - Why: An orchestrator reading line 136 can run a second loop that line 104 forbids without operator consent.
- **CMD-RQ-02**: severity high, class Q, contradiction, line 53
  - Current:
    > the company's Notion page live and extract Decision Status, entry zone,
  - Proposed:
    > QUESTION: CLAUDE.md TEAM WORKFLOW says "The pipeline produces payloads. claude.ai executes writes." and that Claude Code has no live web access. This command fetches Notion live at step f and writes Notion inline at step 4. Is /run-quarterly an approved exception (Notion MCP in-session), or should step f read a ferried Notion extract and step 4 emit a Notion payload for claude.ai to write?
  - Why: The command and CLAUDE.md assign the Notion write to different actors.
- **CMD-RQ-03**: severity medium, class B, contradiction, line 37
  - Current:
    > c. TOOLCHAIN PRECHECK: verify pdftotext, pdfinfo, pdftoppm, tesseract. If
  - Proposed:
    > c. TOOLCHAIN PRECHECK: verify pdftotext, pdfinfo, pdffonts, pdftoppm, tesseract. If
  - Why: A1's text-layer gate runs pdffonts first; the orchestrator prompt (line 118) checks it, this command does not.
- **CMD-RQ-04**: severity medium, class B, contradiction, line 48
  - Current:
    > e. RUN FOLDER: create `runs/<ticker>-<quarter>/` with `inputs/` and `work/`
  - Proposed:
    > e. RUN FOLDER: create `runs/<ticker>-<quarter>/` with `inputs/`, `extracted/`, and `work/`
  - Why: A1 writes its fulltext and structured files to `extracted/` (orchestrator lines 81, 90-91); the command never creates it.
- **CMD-RQ-05**: severity medium, class B, contradiction, line 123
  - Current:
    > Commit the run folder with "quarterly review: <ticker> <quarter>". Then report
  - Proposed:
    > Write `session-cost.md` per orchestrator step 6b, then commit the run folder with `git commit -q -m "quarterly review: <ticker> <quarter>"`. End the report with the commit hash and `git log -1 --stat`. Then report
  - Why: CLAUDE.md FERRY AND COMMIT HYGIENE requires the hash and `git log -1 --stat` on every commit report and session-cost.md on every run; the command omits both.
- **CMD-RQ-06**: severity medium, class Q, duplication, line 57
  - Current:
    > ## 1. PER-DOCUMENT: A1 -> A2 -> A3 (foreground subagents, gated)
  - Proposed:
    > QUESTION: Sections 1-5 and RULES restate prompts/quarterly-00-orchestrator.md, which line 13 names as the authority. The copies have drifted (CMD-RQ-01, -03, -04, -05; no protocol scoping for a DOCUMENT REVIEW in section 2; no SIGNAL CONTEXT; no Spear fallback). Cut sections 1-5 to one line each that points to the orchestrator section, keeping only the setup steps in section 0?
  - Why: Two copies of the sequence already disagree in four places.
- **CMD-RQ-07**: severity low, class A, old-phrasing, line 13
  - Current:
    > Read `prompts/quarterly-00-orchestrator.md` NOW. It is the authority on
  - Proposed:
    > Read `prompts/quarterly-00-orchestrator.md` first. It is the authority on
  - Why: All-caps urgency adds nothing on current models.

### `.claude/commands/step1.md`

- **CMD-STEP1-01**: severity high, class Q, contradiction, line 12-20, 38, 126-140
  - Current:
    > Claude Code desktop has live web (WebSearch/WebFetch) in this setup. Steps B and
  - Proposed:
    > QUESTION: operator ruling 2026-09-05 (step1.md) replaces the web spear with a Step-1 intake run by Claude Code with live web. CLAUDE.md SPEAR GATE (line 191-215) still says "Claude Code never runs a spear pass: this container has no live web access" and points the operator to Claude web; team_workflow_project_instructions.md line 14 says the same. Should CLAUDE.md SPEAR GATE and team workflow Phase 0 record the 2026-09-05 ruling and the Step-1 OVERRIDE form, per CLAUDE.md "Dependency alignment"?
  - Why: the binding file and the command describe opposite spear workflows; a model following CLAUDE.md will refuse Step B or treat the auto-override as a gate breach.
- **CMD-STEP1-02**: severity medium, class Q, contradiction, line 107-111
  - Current:
    > PYTHONUTF8=1 py collect_to_repo.py --dry-run
  - Proposed:
    > QUESTION: CLAUDE.md SESSION DISCIPLINE line 101-103 says "The collect_to_repo.py collector runs on the operator's machine, out of session; in-session it appears only as collect_to_repo.py --push-again." /step1 runs it in session with --dry-run. Should CLAUDE.md add "except /step1 on the operator's desktop"?
  - Why: two binding texts disagree on whether the collector runs in session.
- **CMD-STEP1-03**: severity medium, class B, stale-ref, line 87-88
  - Current:
    > Read the Section 1B Sector Cap Table in
    > `frameworks/Master_Project_Prompt_v3_6.md` and choose the row that matches the
  - Proposed:
    > Read the sector cap table in the section-1b skill chunk 05 (`.claude/skills/section-1b/references/05-sector-cap.md`) and choose the row that matches the
  - Why: run-pipeline.md line 166-167 resolves the row from chunk 05 (the resolved v3.3-v3.10 table, which lists /step1 as a consumer); the Master file holds the base table only, so the two commands can pick from different tables.
- **CMD-STEP1-04**: severity low, class B, stale-ref, line 24-27
  - Current:
    > - Ask the operator no questions. The two interactive pauses in the normal
    >   pipeline are SUPPRESSED here and replaced by standing defaults:
    >   - PEER SELECTION never pauses. Claude picks the peers and records why.
  - Proposed:
    > - Ask the operator no questions. The one interactive pause in the normal pipeline (the stage-0 EMPTY-FOLDER CONFIRMATION) is SUPPRESSED here and replaced by a standing default. Peer selection is Claude's call, recorded with reasons.
  - Why: neither run-pipeline.md nor 00-orchestrator.md has a peer-selection pause; run-pipeline.md line 232 calls the empty-folder question "the single permitted question".
- **CMD-STEP1-05**: severity low, class A, stale-ref, line 164
  - Current:
    > `gh` is not installed;
  - Proposed:
    > If `gh` is not installed or not signed in,
  - Why: session-start.sh line 74 calls gh and the web container ships it; the hard claim is true only for one desktop setup.
- **CMD-STEP1-06**: severity low, class Q, other, line 132
  - Current:
    > Spear: OVERRIDE <YYYY-MM-DD> (operator standing ruling 2026-09-05: Step-1 intake replaces the web spear)
  - Proposed:
    > QUESTION: CLAUDE.md and 00-orchestrator.md line 166 define the exact form "Spear: OVERRIDE YYYY-MM-DD (operator)". Should the gate text accept this longer parenthetical, or should step1 write "(operator)" and put the ruling reference on the next line?
  - Why: a literal gate check may not match the longer form.

### `.claude/skills/section-1b/SKILL.md`

- **G4-SK-01**: severity low, class B, stale-ref, line 10
  - Current:
    > v3.8 (Amendments 18, 19)
  - Proposed:
    > v3.8 (Amendments 18, 19; its Amendment 20 text is superseded by the v3.9 Amendment 20, which renumbers the governance rule to 20.5)
  - Why: Section_1B_v3_8_Amendments.md also carries an earlier Amendment 20 (governance at 20.4, cap review at 20.6 with a "one step below, two reviews" test); a reader citing the v3.8 file gets different numbering and a different cap-review trigger than chunks 05 and 15.
- **G4-SK-02**: severity low, class Q, contradiction, line 30
  - Current:
    > This skill uses the operator's mapping: Rule B = Amendment 26.1 base-case revenue basis, Rule C = Amendment 26.2 margin bridge, Rule E = Amendment 26.4 relevant-period track record.
  - Proposed:
    > QUESTION: see G4-MST-23. Master line 1197 says Rules B and C are not defined in the repo, and v3.10 26.4 calls the guidance discount "the Rule B discount". Is the operator's mapping recorded anywhere in the repo, so this line can cite it?
  - Why: Two framework texts disagree on the Rule B label; the skill's chunks 07 and 17 build on its mapping.

### `.claude/skills/section-1b/references/15-cost-of-capital-relative-valuation.md`

- **G4-SK15-01**: severity high, class Q, contradiction, line 59
  - Current:
    > The macro sheet's standing practice also holds terminal growth at or below the risk-free rate, so the effective ceiling is the lowest of the three.
  - Proposed:
    > QUESTION (number difference): the chunk resolves the terminal growth ceiling as min(6%, nominal GDP, risk-free), so 6% binds this month. `macro-sheet.md` line 30 states "6.75% hard (min of nominal GDP 10% and risk-free 6.76%)" and line 4 says "effective terminal ceiling 6.75%", omitting the Master's 6% cap (Master line 778). No Section 1B layer names the risk-free rate as a ceiling. Which ceiling governs a DCF this month: 6% (Master plus chunk) or 6.75% (macro sheet)? And is the risk-free leg Section 1B law or macro-sheet practice?
  - Why: A stage that reads the macro-sheet row instead of the chunk uses a terminal growth 75 bps above the Master cap.

### `LESSONS.md`

- **LES-01**: severity high, class Q, contradiction, line 148-150 (versus CLAUDE.md line 16-17)
  - Current:
    > 5. OR-11 APPROVED 2026-09-28 (operator): for margin-reset names, set the Rule C
    >      bear margin from the evidence bridge, not the trailing 3-yr average.
  - Proposed:
    > QUESTION: CLAUDE.md NEVER says "the trailing 3-year average is the BEAR input" with no margin-reset exception. OR-11 is approved but not yet written into the framework or CLAUDE.md. Until it is, which binds a margin-reset name: CLAUDE.md or OR-11? Should CLAUDE.md line 17 add "(margin-reset names: OR-11, evidence bridge)" now, per Dependency alignment?
  - Why: an approved operator ruling and the binding CLAUDE.md rule disagree on the bear margin input.
- **LES-02**: severity medium, class Q, contradiction, line 3 (whole file)
  - Current:
    > Working operational memory. Hard budget: under 1,500 tokens.
  - Proposed:
    > QUESTION: the file holds 1,386 words (about 1,800+ tokens), over the CLAUDE.md MEMORY budget. Run /compost budget review: candidates to archive are the closed-in-spirit OPEN ACTIONS (ORCHPHARMA block, SYNGENE block) once each is promoted, and the PROMOTED TO LAW lines already in LESSONS_ARCHIVE.md.
  - Why: CLAUDE.md MEMORY calls the budget hard; every /run-pipeline, /fttcp and /finalize session pays for the excess.
- **LES-03**: severity low, class M, duplication, line 134-135
  - Current:
    > - Resolve the stage 0 routing conflict between /run-pipeline (orchestrator does it
  - Proposed:
    > No text change; close this line in the same commit that resolves CMD-RP-01 and TWF-01.
  - Why: confirms the known lead is already an open action; the fix should retire it.

### `frameworks/Annual_Report_Analysis_Protocol_v1_3.md`

- **G5-AR-06**: severity high, class B, stale-ref, line 1064
  - Current:
    > recompute Destination PE end-to-end per Section 1B v3.3 (both tracks
  - Proposed:
    > recompute Destination PE end-to-end per Section 1B (v3.3 base through v3.10, later layers govern) (both tracks
  - Why: names v3.3 alone as the full set, which drops Amendments 9-26 (e.g. the 30x Pillar 1 cap, Step 1C, A21 base).
- **G5-AR-08**: severity high, class B, contradiction, line 1248
  - Current:
    > - Entry price for 25% CAGR (= Fair Value ÷ 1.25³)
  - Proposed:
    > - Entry price = exit-consistent fair value ÷ (1 + tier hurdle)³ (Tier A 1.25, Tier B 1.20), shown with the Amendment 19 FV CAGR and return-source label
  - Why: CLAUDE.md bars an entry zone without the A19 FV CAGR and return-source classification; OR-8 confirmed the tier divisor and A18.1 the exit-consistent basis. This restates ruled text only.
- **G5-AR-01**: severity medium, class A, stale-ref, line 37
  - Current:
    > the FTTCP ROCE forward verdict is the sole authority (per FTTCP v2.1).
  - Proposed:
    > the FTTCP ROCE forward verdict is the sole authority (per FTTCP v2.3).
  - Why: cites v2.1 as the live protocol.
- **G5-AR-02**: severity medium, class A, stale-ref, line 1040
  - Current:
    > Pillar 1 per the FTTCP v2.1 sole-authority table.
  - Proposed:
    > Pillar 1 per the FTTCP v2.3 sole-authority table.
  - Why: same stale FTTCP label.
- **G5-AR-03**: severity medium, class A, stale-ref, line 1056
  - Current:
    > Apply the FTTCP v2.1 mapping table
  - Proposed:
    > Apply the FTTCP v2.3 mapping table
  - Why: same stale FTTCP label inside the 11A pillar table.
- **G5-AR-04**: severity medium, class A, stale-ref, line 964
  - Current:
    > established at initial workup via Master Project Prompt v3.6 Role 5.5
  - Proposed:
    > established at initial workup via Master Project Prompt v3.7 Role 5.5
  - Why: cites Master v3.6 as the live Role 5.5 authority.
- **G5-AR-05**: severity medium, class A, stale-ref, line 1050
  - Current:
    > ### 11A. Four-Pillar Destination PE re-validation (synced to Section 1B v3.9)
  - Proposed:
    > ### 11A. Four-Pillar Destination PE re-validation (synced to Section 1B v3.10)
  - Why: v3.10 (Amendment 26) is the top layer and governs projections that feed this table.
- **G5-AR-07**: severity medium, class B, contradiction, line 1062
  - Current:
    > | Recompute with audited EPS base and current PE | PASS / CONDITIONAL / STOP |
  - Proposed:
    > | Recompute with audited EPS base and current PE | PASS / CONDITIONAL / STOP (band shown; caps no verdict, Amendment 24 and operator ruling OR-2) |
  - Why: operator ruling OR-2 (2026-09-15) made the Hurdle band display-only; this row still reads as a gate, and CLAUDE.md says there is no STOP verdict.
- **G5-AR-09**: severity medium, class Q, contradiction, line 1249
  - Current:
    > - Margin of Safety price (20% below entry)
  - Proposed:
    > QUESTION: Master v3.5+ uses an evidence-scaled margin of safety (20%/30%/40%) and Section 1B v3.9 Amendment 25 expresses MoS as position size for fast-growth names. Should 13B read "Margin of Safety per the evidence scale, or as position size for fast-growth names (Amendment 25)"?
  - Why: fixed 20% conflicts with two later rules; changing it alters the MoS number, so MEANING-RISK.
- **G5-AR-10**: severity medium, class Q, contradiction, line 168
  - Current:
    > - Going Concern flag → STOP analysis, this is a structural break in the thesis
  - Proposed:
    > QUESTION: CLAUDE.md says "Never halt a run on company quality. Flags propagate; only mechanical failures halt." Should a Going Concern flag propagate to the Step 13 overlay (which already sets IMMEDIATE EXIT) instead of halting the review at Step 1? Same question for line 1093 "If any thesis-broken condition has FIRED, stop the protocol and recommend immediate exit".
  - Why: two quality halts in a protocol whose output feeds the pipeline; the change alters flow, so MEANING-RISK.
- **G5-AR-11**: severity medium, class A, piecemeal, line 306
  - Current:
    > 🛑 **STOP. Show the P&L table, reconciliation, decomposition, and diagnostic answers.**
  - Proposed:
    > Record the P&L table, reconciliation, decomposition, and diagnostic answers, then continue to Step 3L or Step 4.
  - Why: the protocol pauses 17 times (lines 129, 172, 234, 306, 334, 382, 400, 482, 519, 653, 690, 782, 861, 902, 960, 1023, 1044, 1117, 1169, 1263, 1341), mostly to "present" a table; one finish line per review with operator checkpoints only at Step 11-PRE and Step 13 does the same job (see STOP POINTS). Apply the same "Record ..., then continue" form to each line classed MERGE below.
- **G5-AR-12**: severity low, class A, old-phrasing, line 19
  - Current:
    > When triggered, you MUST execute the protocol below in full sequence. Do not skip steps. Do not jump to conclusions before completing the Notes triple-pass.
  - Proposed:
    > Run the steps in order. Draw conclusions only after the Notes triple-pass.
  - Why: three restatements of one instruction.
- **G5-AR-13**: severity low, class A, stale-ref, line 17
  - Current:
    > (with triple-pass on notes already done by the Gemini pipeline)
  - Proposed:
    > (with triple-pass on notes already done by the pipeline, stage 02)
  - Why: Gemini pipeline is retired; same at line 525 "If the Sheet 2 (Gemini pipeline) AR Deep Dive output".
- **G5-AR-14**: severity low, class A, stale-ref, line 1267
  - Current:
    > Save in this exact sequence per Notion_Save_Instructions:
  - Proposed:
    > Save in this exact sequence per the notion-save skill:
  - Why: no Notion_Save_Instructions file exists in the repo; the claude.ai notion-save skill now holds the save rules.

### `frameworks/Debt_Capacity_Assessment_v1_0.md`

- **G5-DCA-01**: severity medium, class A, stale-ref, line 3
  - Current:
    > Runs immediately BEFORE FTTCP v2.0 and after Role 5.5
  - Proposed:
    > Runs immediately BEFORE FTTCP (v2.3) and after Role 5.5
  - Why: names v2.0 as the live protocol.
- **G5-DCA-02**: severity low, class A, stale-ref, line 16
  - Current:
    > FTTCP v2.0 → Market-Implied Assumptions → Role 1 → Role 2 → Role 3
  - Proposed:
    > FTTCP v2.3 → Market-Implied Assumptions → Role 1 → Role 2 → Role 3
  - Why: same stale label in the placement diagram.
- **G5-DCA-03**: severity low, class A, stale-ref, line 25
  - Current:
    > consistent with the FTTCP v2.0 cyclical margin rule
  - Proposed:
    > consistent with the FTTCP cyclical margin rule (Part B, since v2.0)
  - Why: reads as a pointer to v2.0.

### `frameworks/Document_Review_Protocol_v1_1.md`

- **FW-DR-01**: severity low, class A, stale-ref, line 138
  - Current:
    > (the process verdict; canonical per CLAUDE.md and Master v3.6)
  - Proposed:
    > (the process verdict; canonical per CLAUDE.md and Master v3.7)
  - Why: The Master content is v3.7; the file path keeps v3_6.
- **FW-DR-02**: severity low, class Q, stale-ref, line 112
  - Current:
    > and the Dhruva-Research output style.
  - Proposed:
    > QUESTION: No repo file defines a "Dhruva-Research output style". Name the file (anti-ai-writing-style.md?) or drop the phrase?
  - Why: A4 cannot follow a style it cannot load.
- **FW-DR-03**: severity low, class A, other, line 153
  - Current:
    > - v1.1 — Step 10 provenance switched from a two-way prior-vs-document label to
  - Proposed:
    > - v1.1 — Step 11 provenance switched from a two-way prior-vs-document label to
  - Why: Provenance now lives in step 11 (the brief); step 10 is the Silence Audit.

### `frameworks/Downstream_Source_Discovery_Protocol_v1_0.md`

- **G5-DSD-01**: severity medium, class A, stale-ref, line 3
  - Current:
    > Companion to Master Project Prompt v3.6 Role 5.5 (Downstream Signal Identification).
  - Proposed:
    > Companion to Master Project Prompt v3.7 Role 5.5 (Downstream Signal Identification).
  - Why: cites Master v3.6 as live.
- **G5-DSD-02**: severity medium, class A, other, line 139
  - Current:
    > Claude executes the monthly M1-M5 pull with web access against the Primary Source URLs in the tracker;
  - Proposed:
    > Claude web (claude.ai) executes the monthly M1-M5 pull with live web access against the Primary Source URLs in the tracker; Claude Code has no live web and does not run it;
  - Why: "Claude" is ambiguous; Claude Code, which reads this file at stage 9, has no live web per CLAUDE.md.

### `frameworks/FTTCP_v2_1_Consolidated.md`

- **G5-FTTCP-08**: severity high, class Q, contradiction, line 562
  - Current:
    > If the verdict implies a Decision Status change, update the row property in the Notion COMPANIES MASTER database immediately
  - Proposed:
    > QUESTION: CLAUDE.md WORDS defines "flag" as "decision stays human", TEAM WORKFLOW says "The pipeline produces payloads. claude.ai executes writes", and Section 1B v3.9 Appendix B5 says a Decision Status change "is operator-only". Should 6B read "If the verdict implies a Decision Status change, flag it and put the proposed change in the Notion payload for the operator to rule on"?
  - Why: as written FTTCP sets Decision Status itself, which conflicts with three binding statements; wording fix changes who decides, so MEANING-RISK.
- **G5-FTTCP-01**: severity medium, class A, stale-ref, line 5
  - Current:
    > *Version 2.1 | 19 August 2026 | Dhruva Research. This single document replaces
  - Proposed:
    > *Version 2.3 (filename keeps the v2_1 stem) | first consolidated as v2.1 19 August 2026 | Dhruva Research. This single document replaces
  - Why: the first banner line names v2.1 while lines 9-11 say the content is v2.3; a reader stopping at line 5 cites the wrong version.
- **G5-FTTCP-02**: severity medium, class A, stale-ref, line 5
  - Current:
    > and Master Project Prompt cross-references move to v3.6.
  - Proposed:
    > and Master Project Prompt cross-references moved to v3.6 at that date (the live Master is v3.7; see line 11).
  - Why: reads as a present-tense pointer to Master v3.6 as the live authority.
- **G5-FTTCP-03**: severity medium, class A, stale-ref, line 32
  - Current:
    > Role 5.5 (Downstream Signal Identification, defined in Master Project Prompt v3.6) → Debt Capacity Assessment v1.0 → FTTCP v2.1 (this protocol,
  - Proposed:
    > Role 5.5 (Downstream Signal Identification, defined in Master Project Prompt v3.7) → Debt Capacity Assessment v1.0 → FTTCP v2.3 (this protocol,
  - Why: the enforced-sequence line cites an older Master and an older FTTCP as live (known lead).
- **G5-FTTCP-04**: severity medium, class A, stale-ref, line 36
  - Current:
    > Role 5.5 (Downstream Signal Identification, per Master Project Prompt v3.6) must precede FTTCP
  - Proposed:
    > Role 5.5 (Downstream Signal Identification, per Master Project Prompt v3.7) must precede FTTCP
  - Why: same stale Master label inside the Signal Gate rule.
- **G5-FTTCP-09**: severity medium, class Q, contradiction, line 484
  - Current:
    > Second-tier sources (rating agency, industry association, sector-focused independent research) may substitute for the competitor-absence source when direct verification is impossible
  - Proposed:
    > QUESTION: Downstream_Source_Discovery_Protocol_v1_0.md line 109 says "Only ranks 1-3 count toward the three-source evidence bars anywhere in the framework (Category-Break Override ...)" and ranks a credit rating rationale at 4 and trade press at 5. Which rule governs the Category-Break competitor-absence source?
  - Why: the two files give different source bars for the same override condition.
- **G5-FTTCP-10**: severity medium, class Q, contradiction, line 681
  - Current:
    > use the standing default of **13.5% for micro and small caps** (operator-confirmed default, Gate E, 13-Aug-2026)
  - Proposed:
    > QUESTION: Section 1B v3.6 Amendment 12 (line 32) restates the Master RRM base r as "small/micro 14%". Is the B2 minimum-ROCE default meant to differ from the RRM base r (13.5% vs 14%), or should B2 cite the RRM base?
  - Why: two default required returns for the same size bucket; a stage can pick either.
- **G5-FTTCP-11**: severity medium, class Q, contradiction, line 552
  - Current:
    > For planning purposes, use the LOWER BOUND of the 1.5-2.5x re-rating estimate.
  - Proposed:
    > QUESTION: Section 1B v3.10 Amendment 26.3 says Role 1 inputs state "the most evidenced path" and "Do not shade individual inputs". Does this lower-bound instruction survive 26.3 for Role 1 re-rating inputs, or is it now a stated BEAR reading?
  - Why: a per-input conservative choice in a valuation-facing table, which 26.3 retired for Role 1 projections.
- **G5-FTTCP-05**: severity low, class A, stale-ref, line 459
  - Current:
    > The sector cap in Section 1B of the Master Project Prompt (v3.6 onward,
  - Proposed:
    > The sector cap in Section 1B of the Master Project Prompt (v3.6 onward, now v3.7 with the Section 1B layer set to v3.10,
  - Why: "v3.6 onward" is technically true but is the only version anchor a reader sees.
- **G5-FTTCP-06**: severity low, class A, stale-ref, line 498
  - Current:
    > (Section 1B row G in v3.5, materialised as rows G2/G3)
  - Proposed:
    > (Section 1B row G, materialised as rows G2/G3 since Master v3.5)
  - Why: names v3.5 as if it were the current Section 1B.
- **G5-FTTCP-07**: severity low, class A, stale-ref, line 610
  - Current:
    > Role 7 (FTTCP v2.1)  ←— this protocol
  - Proposed:
    > Role 7 (FTTCP v2.3)  ←— this protocol
  - Why: sequence diagram labels the live protocol v2.1.
- **G5-FTTCP-12**: severity low, class A, old-phrasing, line 48
  - Current:
    > When triggered, you MUST execute the protocol below in full sequence. Do not produce a final FTTCP verdict before completing every step — especially Step 2C, which forces probability assessment with evidence.
  - Proposed:
    > Run the steps in order. The FTTCP verdict comes after every step is complete, including the Step 2C probability table.
  - Why: capitalised MUST plus a restated "do not" adds no rule.
- **G5-FTTCP-13**: severity low, class A, duplication, line 568
  - Current:
    > ## METHODOLOGICAL DISCIPLINE — RULES THAT MUST NEVER BE VIOLATED
  - Proposed:
    > ## METHODOLOGICAL DISCIPLINE (checklist; each rule is defined in the step it cites and this list adds none)
  - Why: rules 1-16 restate Steps 1-2E, 4 and Pillar 1 text verbatim in substance (e.g. Kernex cap stated at lines 305, 361, 378); labelling the list as a checklist stops it being read as a second source.
- **G5-FTTCP-14**: severity low, class A, stale-ref, line 104
  - Current:
    > Latest concall transcript (actual transcript, not Gemini-synthesised)
  - Proposed:
    > Latest concall transcript (actual transcript, not a pipeline synthesis)
  - Why: the pipeline is no longer Gemini; line 50 already says "never a pipeline synthesis".

### `frameworks/Market_Implied_Assumptions_v1_0.md`

- **G5-MIA-02**: severity high, class Q, contradiction, line 30
  - Current:
    > Use a reasonable exit PE for the sector and quality (state which, and why it is reasonable; do not use a round-number default).
  - Proposed:
    > QUESTION: CLAUDE.md says "Never use any exit PE from outside Section 1B ... It is the sole exit multiple authority." This step runs before Role 1 and picks its own "reasonable exit PE". Is Reading 2 exempt as a price-reading diagnostic, or must it use the sector cap or the live Step 1C peer base as its exit PE and say so?
  - Why: an exit PE chosen outside Section 1B enters a block that Role 1 consumes.
- **G5-MIA-01**: severity medium, class A, stale-ref, line 3
  - Current:
    > Runs immediately AFTER FTTCP v2.0 and immediately BEFORE Role 1.
  - Proposed:
    > Runs immediately AFTER FTTCP (v2.3) and immediately BEFORE Role 1.
  - Why: names v2.0 as the live protocol; same at line 14 "FTTCP v2.0 → MARKET-IMPLIED ASSUMPTIONS".
- **G5-MIA-03**: severity low, class B, contradiction, line 81
  - Current:
    > At a reasonable exit PE of 20x (a mild de-rating a maturing name should expect)
  - Proposed:
    > At an illustrative exit PE of 20x (shape only; a run takes its exit PE per Step 1)
  - Why: the worked example uses a round-number exit PE the same file forbids at line 30; mark it as shape-only.

### `frameworks/Master_Project_Prompt_v3_6.md`

- **G4-MST-01**: severity high, class B, stale-ref, line 108
  - Current:
    > CRITICAL: This prompt incorporates a proprietary FOUR-PILLAR exit multiple framework (Section 1B, v3.3 as amended through v3.5.1 and v3.6). Exit multiples are NOT assumed — they are EARNED through ROCE quality, cash conversion quality, growth visibility, and strategic scarcity, disciplined by the Hurdle Ratio and the sector cap. Read Section 1B carefully before assigning any exit multiple.
  - Proposed:
    > This prompt uses the Four-Pillar exit multiple framework (Section 1B: the v3.3 base plus the v3.5.1, v3.6, v3.7, v3.8, v3.9 and v3.10 amendment layers in frameworks/; later layers govern overlaps). Exit multiples are earned through ROCE quality, cash conversion quality, growth visibility and strategic scarcity, disciplined by the Hurdle Ratio and the sector cap. Pipeline stage 11 works from the section-1b skill, which carries the resolved rules.
  - Why: Names the set only to v3.6, so a Role 2/3 reader treats A17-A26 as outside the authority; also drops "CRITICAL" and "read carefully".
- **G4-MST-02**: severity high, class B, stale-ref, line 266
  - Current:
    > ## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE FRAMEWORK v3.3 (CRITICAL)
  - Proposed:
    > ## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE FRAMEWORK (base text; v3.3 to v3.10 layers govern)
    > 
    > The text below is the base. These later layers replace parts of it and are not restated here: v3.3 Amendments 4.1-4.2 (Pillar 3 splits into 3a/3b/3c, +6x combined cap), 4.3 (two-tier hurdle, Tier A 1.953 / Tier B 1.728); v3.7 Amendment 17 (CONVERTER gate before any pillar math); v3.8 Amendments 18-19 (Year 4 projection, exit-basis symmetry, FV path and FV CAGR); v3.9 Amendments 20-25 (Step 1C, run-rate base, probabilistic credit, Expectation Ledger, price decomposition, size-based MoS); v3.10 Amendment 26. Where base text and a layer differ, the layer governs.
  - Why: The header labels "v3.3" as the whole set and nothing in the section body tells a reader that Pillar 3, the Hurdle, the entry price and the projection horizon below are superseded.
- **G4-MST-03**: severity high, class Q, contradiction, line 373
  - Current:
    > | EM ≥40 with catalyst 0-12 months and mostly 📄 documented evidence | +6x |
  - Proposed:
    > QUESTION: Pillar 3 here is a single EM table (lines 365-385). v3.3 Amendment 4.1/4.2 made this table "3b" and added 3a and 3c under a combined +6x cap, and v3.9 A22 changed how evidence symbols feed it. The base text carries no marker. May the section heading read "Pillar 3 (base text: this table is 3b only; 3a, 3c and the +6x combined cap per v3.3 Amendments 4.1-4.2, see section-1b chunk 03)"?
  - Why: A Role 2/3 reader of the Master alone applies a pre-v3.4 Pillar 3; the marker is wording, but the heading change touches a pillar, so it is put as a question.
- **G4-MST-04**: severity high, class Q, contradiction, line 567
  - Current:
    > | HR(Base) < 1.953 but HR(Bull) ≥ 1.953 | CONDITIONAL — proceed, but flag "growth-dependent with de-rating headwind"; verdict capped at WATCHLIST / BUY-ON-DIPS; no BUY NOW |
  - Proposed:
    > QUESTION (MEANING-RISK): v3.9 Amendment 24 says the Hurdle Ratio "remains a feasibility check, not a gate", and the operator ruled on 2026-09-15 (OR-2, section-1b SKILL.md) that the band "caps no verdict". This row and lines 1115, 1116, 1119 and 1144 still use the band as a verdict cap (no BUY NOW, BUY-ON-DIPS ceiling, AVOID on STOP, Conviction Outlier needs a pass). Stage 14 reads these lines. Should each carry a marker "[Superseded by v3.9 A24 and ruling OR-2, 2026-09-15: band is shown, caps no verdict]", or does OR-2 not reach the Role 2 decision rules?
  - Why: The Master and the skill give stage 14 and stage 11 opposite rules for the same band.
- **G4-MST-05**: severity high, class B, contradiction, line 568
  - Current:
    > | HR(Bull EPS CAGR) < 1.953 | STOP — overvalued; 25% CAGR is infeasible even on bull-case earnings |
  - Proposed:
    > | HR(Bull EPS CAGR) < threshold | STOP band: the tier hurdle is infeasible even on bull-case earnings (a feasibility band, not a halt) |
  - Why: CLAUDE.md says "There is no STOP verdict" and runs never halt on company quality; the skill already uses "STOP band"; the threshold also misses Tier B 1.728 (v3.3 A4.3). If the operator reads "threshold" as a rule change, treat as part of G4-MST-04.
- **G4-MST-06**: severity high, class B, contradiction, line 562
  - Current:
    > Pass threshold: HR ≥ 1.953 (= 1.25³).
  - Proposed:
    > Pass threshold: HR ≥ 1.953 (= 1.25³) for Tier A; HR ≥ 1.728 (= 1.20³) for Tier B (v3.3 Amendment 4.3). The verdict card's first line states "Tier: [A/B] | Hurdle: [25%/20%]".
  - Why: Base text states one threshold; Amendment 4.3 (and OR-8) set two, so a Master-only reader mis-tests every Tier B name. This restates existing law, it does not change it.
- **G4-MST-07**: severity high, class B, contradiction, line 658
  - Current:
    > | Line Item | Year 0 | Year 1 | Year 2 | Year 3 | Year 5 |
  - Proposed:
    > | Line Item | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
  - Why: v3.8 Amendment 18.0 makes Year 4 a committed row and "NOT PROJECTED" for Year 4 REWORK; the template (also 2A at line 590) omits it. Apply the same column add to the 2A table after line 589 ("| Revenue Year 4 | ₹___ Cr | ₹___ Cr | ₹___ Cr |").
- **G4-MST-08**: severity high, class B, contradiction, line 859
  - Current:
    > | Price for 25% CAGR = Fair Value ÷ (1.25)³ | ₹___ |
  - Proposed:
    > | Price for the tier hurdle = exit-consistent Fair Value ÷ (1 + hurdle)³ (1.25 Tier A, 1.20 Tier B; v3.3 A4.3, v3.8 A18.5, ruling OR-8) | ₹___ |
    > | FV CAGR and return-source label (v3.8 A19; mandatory beside any entry zone) | ___% [COMPOUNDER / HYBRID / DISCOUNT-CLOSER] |
  - Why: CLAUDE.md bars any entry zone without the A19 FV CAGR and label; 4E has neither and ignores Tier B.
- **G4-MST-09**: severity medium, class B, stale-ref, line 932
  - Current:
    > - MY ENTRY PRICE range and MARGIN OF SAFETY PRICE
  - Proposed:
    > - MY ENTRY PRICE range and MARGIN OF SAFETY PRICE
    > - LATER-LAYER LINES: Tier line (A4.3, first line of card); FV CAGR and return-source label (A19); Step 1C line: pillar destination, adjusted peer base or PENDING LIVE PEER TABLE, % gap, governing multiple (A20); price decomposition T1/T2/T3/residual % (A24); CONVERTER classification (A17)
  - Why: The 4H field list predates A4.3 and A17-A24; stage 13/14 readers copy this list.
- **G4-MST-10**: severity medium, class A, stale-ref, line 185
  - Current:
    > | FTTCP ROCE forward verdict | FIRING / RECOVERING-to-FIRING / RECOVERING / STAGNANT / DECLINING (with probability) |
  - Proposed:
    > | FTTCP ROCE forward verdict | FIRING / RECOVERING / STAGNANT / DECLINING (with probability) |
  - Why: FTTCP has banned hybrid labels since v1.2; the skill and FTTCP use "RECOVERING, probability >60% with Strong catalysts". Same fix at line 294: "| RECOVERING (probability >60% with Strong catalysts) | Midpoint of current and FY[Y+2] expected ROCE |".
- **G4-MST-11**: severity medium, class A, stale-ref, line 138
  - Current:
    > - FTTCP v2.1 must have been run BEFORE this role
  - Proposed:
    > - FTTCP (file FTTCP_v2_1_Consolidated.md, content v2.3) must have been run BEFORE this role
  - Why: Cites v2.1 as the live protocol; banner line 3 already says v2.3.
- **G4-MST-12**: severity medium, class A, stale-ref, line 268
  - Current:
    > FTTCP v2.1 must already have been run
  - Proposed:
    > FTTCP v2.3 must already have been run
  - Why: Same stale version label as G4-MST-11.
- **G4-MST-14**: severity medium, class A, stale-ref, line 609
  - Current:
    > Single credit (v3.6 Amendment 4)
  - Proposed:
    > Single credit (Section 1B Amendment 4, v3.3 file)
  - Why: Amendment 4 lives in Section_1B_v3.3_Amendments.md; the v3.6 file holds Amendments 11-16, so a reader looking it up finds nothing. Same fix at line 1011 ("And single credit (v3.6 Amendment 4) still binds").
- **G4-MST-15**: severity medium, class A, stale-ref, line 134
  - Current:
    > (v3.6, Section 1B v3.10 Amendment 26.3)
  - Proposed:
    > (v3.7, Section 1B v3.10 Amendment 26.3)
  - Why: The A26 companion text landed in Master v3.7 (banner line 3, 08-Sep-2026); "v3.6" here collides with the Section 1B v3.6 layer name. Same "(v3.6, Section 1B v3.10" → "(v3.7, Section 1B v3.10" at lines 594, 597, 635, 636, 639, 672, 692, 850.
- **G4-MST-16**: severity medium, class A, other, line 13
  - Current:
    > By the time I paste analysis into this project, 10 specialised AI agents have already processed the company's annual report, concall transcripts, investor presentations, financial data, and peer comparisons through three automated pipelines.
  - Proposed:
    > *Scope note for pipeline agents: WHO I AM, MY INVESTMENT CRITERIA, SECTOR LITERACY TRACK, WHAT I WILL PASTE, the INPUT DATA fill tables, HOW THIS PROJECT GROWS, and COMPANIES.TXT GENERATOR address the operator's claude.ai project. A pipeline stage takes its inputs from its task message and run folder, not from pasted sheets.* By the time I paste analysis into this project, the pipeline has already processed the company's annual report, concall transcripts, investor presentations, financial data, and peer comparisons.
  - Why: "10 agents / three pipelines / Sheets 1-3" (lines 13, 79-96) no longer describe the pipeline, and a stage reading the Master looks for pasted sheets that never arrive.
- **G4-MST-17**: severity medium, class Q, other, line 1539
  - Current:
    > When Sumit pastes a list of screener.in URLs and asks for "companies.txt text" or "batch file text", respond with ONLY the ready-to-paste text block — no explanation needed.
  - Proposed:
    > QUESTION: This section (lines 1537-1560) addresses Sumit, not the operator (Keerti), and points to `py collect_batch.py`, which lives at tools/collector/collect_batch.py and runs off-session. Stages 14 and 15 load the whole Master. May it move out of the Master (for example to tools/collector/README) or carry the G4-MST-16 scope note?
  - Why: A human-addressed utility inside a framework file that agents "execute exactly" can be misread as an output rule.
- **G4-MST-18**: severity medium, class A, piecemeal, line 132
  - Current:
    > - Execute ONE SECTION at a time. STOP after each and wait for my "GO".
  - Proposed:
    > - Execute the sections in order. In the operator's claude.ai chat, stop after each section only when the operator asks for that. Pipeline stages run all sections in one pass and write the interim summary lines without waiting.
  - Why: Four "Type GO" stops (574, 694, 803, 942) split one role into four turns; the stage wrappers already override them, so the framework and wrappers disagree.
- **G4-MST-19**: severity medium, class Q, other, line 1281
  - Current:
    > Write out the specific dollar exposure at 3x sizing on the actual capital base.
  - Proposed:
    > QUESTION (MEANING-RISK): The Conviction Test (lines 1269-1318) asks for felt states ("must feel like states you could sit with") that only the operator holds, and for "the actual capital base", which no pipeline input carries. When stage 15 runs Role 3, should it state the 3x rupee figure from the recommended size and hand the three-outcome question to the operator as an open item, instead of answering it? Separately, "dollar exposure" should read "rupee exposure" (line 1520: all prices in INR).
  - Why: An agent answering this fabricates the operator's psychology and a capital figure (CLAUDE.md: NOT FOUND is the only fill).
- **G4-MST-20**: severity medium, class Q, contradiction, line 1426
  - Current:
    > No FTTCP, no Role 1, no Role 2 may begin until this gate passes.
  - Proposed:
    > QUESTION (MEANING-RISK): Step 4 is a live Notion write. CLAUDE.md says claude.ai executes writes and Claude Code has no live web. Should Step 4 name its executor ("Claude web writes the rows; a Claude Code stage checks the run folder for the Tracker Row URLs and, if they are absent, names the gap") so a Code stage does not try the write or halt?
  - Why: The gate text does not say who executes it; a Code agent reading it can attempt an impossible write.
- **G4-MST-21**: severity medium, class Q, contradiction, line 1452
  - Current:
    > Quarterly-cadence signals feed the 6-12 month window (relevant for the ROCE transition).
  - Proposed:
    > QUESTION: FTTCP (line 36) says Quarterly-cadence signals feed "the 12-month window (ROCE transition)"; the Master says "6-12 month". Which window governs?
  - Why: Numeric difference between the Master and FTTCP on the same rule.
- **G4-MST-22**: severity medium, class Q, contradiction, line 448
  - Current:
    > The Category-Break Override is the ONLY mechanism by which it can be raised.
  - Proposed:
    > QUESTION: Line 444 applies a routine "minimum 25% quality uplift on the sector cap", and line 510 treats both lifts as live. This sentence says the override is the only lift. This is open ruling OR-4 in section-1b SKILL.md. Until ruled, may the sentence read "The Category-Break Override is the only EXCEPTIONAL mechanism by which it can be raised; the routine quality uplift (line 444) is separate (open ruling OR-4)"?
  - Why: Two lines in the same section contradict each other.
- **G4-MST-13**: severity low, class A, stale-ref, line 73
  - Current:
    > FTTCP v2.1 (Quadruple Transition
  - Proposed:
    > FTTCP v2.3 (Quadruple Transition
  - Why: Live sequence cites the old version. Same one-token fix at line 75 ("the Signal Gate rule in FTTCP v2.1" → "v2.3"), line 186 ("from FTTCP v2.1 scored system" → "v2.3"), line 448 ("See FTTCP v2.1 Pillar 1 Integration" → "v2.3"), line 654 ("FTTCP v2.1 cyclical margin rule" → "v2.3"), line 955 ("[from v2.1 scored system]" → "[from FTTCP v2.3 scored system]"), line 1452 ("This is the FTTCP v2.1 Signal Gate rule" → "v2.3"). Lines 9 and 1568-1570 are dated history and stay.
- **G4-MST-23**: severity low, class Q, contradiction, line 1197
  - Current:
    > Section 1B v3.10 Amendment 26.4 refers to one of them as "the Rule B discount", the guidance discount by track record.
  - Proposed:
    > QUESTION: section-1b SKILL.md line 30 maps Rule B = Amendment 26.1 (base-case revenue basis), Rule C = 26.2, Rule E = 26.4, citing "the operator's mapping". This note says Rules B and C are not defined in the repo and must not be reconstructed. Which text is current? If the operator's mapping is real, may this note quote it?
  - Why: The Master and the skill disagree on whether a Rule B definition exists and what it covers.
- **G4-MST-24**: severity low, class B, contradiction, line 1515
  - Current:
    > - When I ask for the devil's advocate, be genuinely brutal. I need this to protect my capital. A weak devil's advocate is worse than none.
  - Proposed:
    > - When I ask for the devil's advocate, be genuinely brutal against the bull case as built (Rule H), with the same evidence bar as a bull claim (Rule J). A weak devil's advocate is worse than none.
  - Why: Read alone it pulls toward the "coroner" posture Rule J (line 1506) forbids.
- **G4-MST-25**: severity low, class A, duplication, line 1519
  - Current:
    > - **Role 5.5 Step 4 is a HARD GATE: no FTTCP, Role 1, or Role 2 may begin for a company until its downstream signals are physically written
  - Proposed:
    > - Role 5.5 Step 4 is a hard gate; see Role 5.5 Step 4 for its pass conditions.
  - Why: Restates lines 1426-1444 in full; one statement plus a pointer avoids drift.
- **G4-MST-26**: severity low, class A, duplication, line 1512
  - Current:
    > - **Exit PE is governed solely by Section 1B. The sector cap table (with documented quality uplift where applicable) is the only ceiling. No other exit PE rule exists.**
  - Proposed:
    > - Exit PE is governed solely by Section 1B (see MY INVESTMENT CRITERIA).
  - Why: The same rule appears at lines 19, 126-127, 137, 713 and 1512 with bold and caps each time.
- **G4-MST-27**: severity low, class A, duplication, line 1514
  - Current:
    > Never recommend Large unless Gate 0 is EXCELLENT and Promoter is TRUSTWORTHY or better.
  - Proposed:
    > Size per the Role 2 Section 7 position size rules.
  - Why: Restates line 1145 with a looser test (line 1145 also needs EM EXPANSION, CMP below MoS and the literacy gate), so the two can be read as different rules.
- **G4-MST-28**: severity low, class A, old-phrasing, line 1052
  - Current:
    > This is critical. Go through ALL the agent outputs and find every instance where one agent's findings contradict another's.
  - Proposed:
    > Find every place where one agent's findings contradict another's, across all agent outputs.
  - Why: Emphasis words add nothing for current models.
- **G4-MST-29**: severity low, class A, stale-ref, line 289
  - Current:
    > the FTTCP ROCE forward verdict is the SOLE authority (v1.2)
  - Proposed:
    > the FTTCP ROCE forward verdict is the SOLE authority (since FTTCP v1.2)
  - Why: Reads as if v1.2 is current; same at line 852 ("from Role 4 v1.2" → "from Role 4, since v1.2"; Quarterly protocol is v1.4).

### `frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md`

- **FW-R5-02**: severity medium, class A, stale-ref, line 499
  - Current:
    > (per FTTCP v1.2)
  - Proposed:
    > (per FTTCP v2.3, file FTTCP_v2_1_Consolidated.md)
  - Why: Names FTTCP v1.2 as the live authority for Pillar 1 ROCE selection; FTTCP v2.3 replaced it.
- **FW-R5-03**: severity medium, class Q, other, line 188
  - Current:
    > This step requires Notion access to prior concall logs.
  - Proposed:
    > QUESTION: Under /run-quarterly A4 has no Notion access and the orchestrator passes no prior concall log (see ORCH-Q-04). Add "(Under /run-quarterly the orchestrator passes the prior log inline; if not passed, mark 3A-3E ND with 'prior log not passed', never 'first concall'.)"?
  - Why: Without that, A4 may treat a missing input as "first concall" and skip the historical audit and the credibility ratio.
- **FW-R5-04**: severity medium, class Q, other, line 23
  - Current:
    > When triggered, you MUST execute the protocol below in full sequence.
  - Proposed:
    > QUESTION: Same as ORCH-Q-03. Add one line here (and in Role 4 INVOCATION): "Under /run-quarterly the 🛑 STOP lines are section checkpoints, not waits. A4 runs every step through. Steps 6C-fired and 8 surface as flags for the operator."?
  - Why: Ten STOP lines in this file tell the agent to wait; the agent is told never to wait.
- **FW-R5-01**: severity low, class A, old-phrasing, line 184
  - Current:
    > This is the most critical artifact of the concall — be thorough.**
  - Proposed:
    > This is the most critical artifact of the concall.**
  - Why: "be thorough" adds nothing; the table spec already sets depth. (Known lead.)
- **FW-R5-05**: severity low, class Q, other, line 444
  - Current:
    > For analysed companies in adjacent sectors, pull recent peer concalls (within ±4 weeks).
  - Proposed:
    > QUESTION: Under /run-quarterly A4 receives only this company's A1-A3 artifacts. Should 7B and 7C read "peer concalls / external sources not passed: UNVERIFIABLE this run" so line 609 ("If no peer reported in window, state explicitly") is not misused to claim no peer reported?
  - Why: A4 cannot pull peers, and the mandatory rule could be filled with a false "no peer reported".

### `frameworks/Quarterly_Results_Review_Protocol_v1_4.md`

- **FW-R4-01**: severity high, class B, stale-ref, line 439
  - Current:
    > ROCE Base (continuous formula: 0.5 × ROCE + 7.5, floor 9x, cap 24x)
  - Proposed:
    > ROCE Base (continuous formula per Section 1B Amendment 5 as amended by v3.6 Amendment 11; read the floor and cap from the section-1b skill)
  - Why: Section_1B_v3_6_Amendments.md line 24 says Amendment 5's "capped at 24x" is SUPERSEDED and "must not be applied"; this cell still prints it. The edit removes the stale number. It does not change the governing value.
- **FW-R4-06**: severity high, class Q, contradiction, line 60
  - Current:
    > If Notion has no page for the company, **stop and ask**
  - Proposed:
    > QUESTION: The orchestrator (lines 187-189) and Document Review Protocol route a missing Notion page to a PRE-THESIS READ, and A4 never stops. Add "(Under /run-quarterly: no wait; frame the review as a PRE-THESIS READ per the orchestrator.)" after this sentence?
  - Why: With the orchestrator's "protocol wins on analysis" clause, A4 receives two opposite instructions for the same case.
- **FW-R4-02**: severity medium, class A, stale-ref, line 439
  - Current:
    > apply the FTTCP v2.1 mapping table.
  - Proposed:
    > apply the FTTCP v2.3 mapping table (file FTTCP_v2_1_Consolidated.md).
  - Why: The live FTTCP content is v2.3; "v2.1" names an older version as current.
- **FW-R4-03**: severity medium, class A, stale-ref, line 435
  - Current:
    > The destination PE in Notion was set under Section 1B v3.3.
  - Proposed:
    > The destination PE in Notion was set under the Section 1B layer set (v3.3 base through v3.10).
  - Why: Names v3.3 alone as the full Section 1B authority.
- **FW-R4-04**: severity medium, class A, stale-ref, line 312
  - Current:
    > per Section 1B v3.3 lender carve-out
  - Proposed:
    > per the Section 1B lender carve-out (v3.3 base, as amended through v3.10)
  - Why: Same v3.3-alone citation.
- **FW-R4-05**: severity medium, class A, stale-ref, line 321
  - Current:
    > defined in Master Project Prompt v3.6
  - Proposed:
    > defined in the Master Project Prompt (v3.7; file Master_Project_Prompt_v3_6.md)
  - Why: Cites v3.6 as the live Master; the content is v3.7.
- **FW-R4-07**: severity medium, class Q, other, line 353
  - Current:
    > that dependency must be added to the tracker via Role 5.5 STEP 4 procedure
  - Proposed:
    > QUESTION: Under /run-quarterly A4 has no Notion tools and the orchestrator's save (step 4) covers only the review, Key Notes, forensics and audit. Who executes the Step 5.5C tracker write, the Step 5.5A tracker query, and the Step 6.5B "Save the refreshed ledger to Notion" (line 426)? Should A4 emit them as a payload for the orchestrator or claude.ai?
  - Why: Three required Notion actions have no executor in the agent pipeline.
- **FW-R4-08**: severity medium, class Q, contradiction, line 668
  - Current:
    > - Conservative bias. When uncertain, lean toward the bear interpretation. Better to be cautious and updated than confidently wrong.
  - Proposed:
    > QUESTION: CLAUDE.md (v3.9 Amendment 25) keeps conservative interpretation for document reading but bars shading Role 1 projection inputs. Steps 6.5 and 7 of this protocol refresh the A21 base and recompute fair values. Should this rule be scoped to "interpretation of filed evidence (Steps 0-6); Steps 6.5-7 follow Amendment 25: most evidenced path, conservatism in position size"?
  - Why: The blanket rule reaches projection steps that Amendment 25 governs.
- **FW-R4-09**: severity low, class Q, contradiction, line 445
  - Current:
    > PASS / CONDITIONAL / STOP per v3.3 Amendment 2
  - Proposed:
    > QUESTION: "STOP" here is the Hurdle Ratio verdict label from Master v3.7 (line 568), not a halt. CLAUDE.md says "There is no STOP verdict" for the process verdict. Gloss it once, e.g. "STOP (Hurdle verdict: overvalued; not a run halt)"?
  - Why: The word collides with the process-verdict rule and with the 🛑 STOP checkpoints.
- **FW-R4-10**: severity low, class A, old-phrasing, line 193
  - Current:
    > This is the step I am most likely to skip. **Do not skip it.**
  - Proposed:
    > Build this table explicitly
  - Why: Anti-skip pleading; the step order and A5 audit already enforce it.
- **FW-R4-11**: severity low, class A, old-phrasing, line 26
  - Current:
    > **Do not skip steps. Do not jump to conclusions before completing the analytical walks.**
  - Proposed:
    > Run every step in order.
  - Why: Line 660 restates the same rule; one plain statement is enough.
- **FW-R4-12**: severity low, class M, other, line 660
  - Current:
    > complete all 9 steps
  - Proposed:
    > complete every step (0 through 9, including 5.5, 6.5 and 8.5)
  - Why: The protocol now has twelve numbered steps; "9" undercounts after the 5.5 / 6.5 / 8.5 insertions.
- **FW-R4-13**: severity low, class Q, duplication, line 653
  - Current:
    > - **Notes must be read.** Do not skip Note 4 or Note 6 because they look administrative.
  - Proposed:
    > QUESTION: The notes-read rule appears at lines 35, 40, 70-87 and 653; Decision Status verification at 57, 455, 661. Keep one statement each (Step 0D and Step 0A) and cut the restatements?
  - Why: The same rule restated four times costs tokens on every A4 full-quarter run.

### `frameworks/README.txt`

- **G5-README-01**: severity high, class B, stale-ref, line 28
  - Current:
    > When you amend a framework, update the copy here. Stage 11 reads these
  - Proposed:
    > When you amend a framework, update the copy here AND regenerate the affected .claude/skills/section-1b/references chunks. Stage 11 reads the section-1b skill, not these
  - Why: stage 11 now reads the preloaded skill with "no file injection" (prompts/11-valuation-pipeline.md line 325), so line 29 "amendments propagate with no pipeline edits" is false; an amendment edited only here never reaches stage 11. CLAUDE.md STRUCTURE carries the same stale sentence (outside this file set).
- **G5-README-02**: severity medium, class B, stale-ref, line 16
  - Current:
    > retired). Stage 11 injects all seven Section 1B layers; where they
  - Proposed:
    > retired). Stage 11 reads all seven Section 1B layers through the section-1b skill; verifier C reads the files directly; where they
  - Why: describes file injection that no longer happens; the same "Stage 11 reads this alongside the earlier Section 1B files" line sits in every layer banner (v3.7 line 3, v3.8 line 3, v3.9 line 3, v3.10 line 3).
- **G5-README-04**: severity medium, class A, stale-ref, line 21
  - Current:
    > FILENAME NOTE. Two files carry a version number in the path that is
  - Proposed:
    > FILENAME NOTE. Three files carry a version number in the path that is
  - Why: FTTCP_v2_1_Consolidated.md (content v2.3) is the third; add "FTTCP_v2_1_Consolidated.md is at v2.3." after the Section 1B sentence.
- **G5-README-03**: severity low, class A, stale-ref, line 2
  - Current:
    > FIRST RUN (stage 11 halts without them):
  - Proposed:
    > FIRST RUN (stage 11 and verifier C depend on them):
  - Why: the halt now belongs to verifier C's file read and the skill build, not stage 11 injection; the files are already present.
- **G5-README-05**: severity low, class M, stale-ref, line 31
  - Current:
    > ALSO MAINTAINED HERE (keep synced with the claude.ai project):
  - Proposed:
    > Keep the line, and add three entries below it: Debt_Capacity_Assessment_v1_0.md (runs before FTTCP; feeds Module B7 and Role 1), Market_Implied_Assumptions_v1_0.md (runs after FTTCP, before Role 1), Document_Review_Protocol_v1_1.md (purpose per its banner).
  - Why: three files in frameworks/ are not listed anywhere in README (known lead); Debt Capacity and Market-Implied are section-1b skill sources.

### `frameworks/Section_1B_v3.3_Amendments.md`

- **G5-1B33-02**: severity high, class B, contradiction, line 77
  - Current:
    > **ROCE Base PE = 0.5 × ROCE(%) + 7.5, floored at 9x, capped at 24x.**
  - Proposed:
    > Insert above the Amendment 5 heading: "> **PARTLY SUPERSEDED.** The 24x cap is superseded by Section 1B v3.6 Amendment 11 (cap 30x with the elite extension above 33% ROCE). The formula, floor and rounding rules stand." (no change to line 77 itself)
  - Why: v3.6 line 5 promises superseded text is "banner-marked", but Amendment 5 carries no mark; verifier C reads this file directly and can apply 24x.
- **G5-1B33-03**: severity high, class B, contradiction, line 35
  - Current:
    > CONDITIONAL — proceed, but flag "growth-dependent with de-rating headwind"; verdict capped at WATCHLIST / BUY-ON-DIPS; no BUY NOW
  - Proposed:
    > Insert above the Amendment 2 table: "> **PARTLY SUPERSEDED.** Section 1B v3.9 Amendment 24 and operator ruling OR-2 (2026-09-15): the Hurdle Ratio is a feasibility check. Its PASS / CONDITIONAL / STOP band is computed and shown; it caps no verdict." (table text unchanged, kept for history)
  - Why: the unmarked table says CONDITIONAL caps the verdict and STOP blocks, which OR-2 overruled.
- **G5-1B33-01**: severity medium, class A, stale-ref, line 3
  - Current:
    > Read it together with the other Section_1B_* files (v3.5.1 Reconciliation, v3.6 Amendments, v3.7 Amendments, v3.8 Amendments); where they overlap, the later layer governs.
  - Proposed:
    > Read it together with the other Section_1B_* files (v3.5.1 Reconciliation, v3.6, v3.7, v3.8, v3.9 and v3.10 Amendments); where they overlap, the later layer governs.
  - Why: the banner of the base layer omits v3.9 and v3.10, the two layers that govern most overlaps.
- **G5-1B33-04**: severity medium, class Q, contradiction, line 38
  - Current:
    > If track record is Mixed or Poor, the Bull row of this check uses Base EPS CAGR + 5% maximum.
  - Proposed:
    > QUESTION: v3.10 Amendment 26.4 keys track record to the trailing four quarters of Role 5 delivery, not whole-company history, and 26.3 retires per-input conservatism in Role 1. Does this "Conservative-bias note" now read "track record over the trailing four quarters", and does the +5% cap survive 26.3?
  - Why: an unmarked conservative-bias rule that two v3.10 sub-amendments touch.
- **G5-1B33-05**: severity medium, class Q, contradiction, line 112
  - Current:
    > (same formula: 0.5 × ROE + 7.5, floor 9x, cap 24x)
  - Proposed:
    > QUESTION: does v3.6 Amendment 11 (30x cap with the elite extension) also apply to the lender ROE formula, or does the lender Pillar 1 keep the 24x cap?
  - Why: Amendment 11 names only ROCE; the lender line still says 24x with no mark.
- **G5-1B33-06**: severity low, class B, stale-ref, line 64
  - Current:
    > (e.g., hard evidence exists but the +4 trajectory-adjustment threshold was not met)
  - Proposed:
    > (e.g., the FTTCP ROCE verdict is STAGNANT or FIRING, so no forward uplift entered Pillar 1; FTTCP Pillar 1 Integration governs)
  - Why: the "+4 trajectory-adjustment" rule was deleted by FTTCP v1.2 (FTTCP line 433); the replacement text is FTTCP line 447's own condition.
- **G5-1B33-07**: severity low, class A, other, line 119
  - Current:
    > New rows covering the active universe (proposals — adjust caps if you disagree):
  - Proposed:
    > New rows covering the active universe (adopted 02-Jul-2026):
  - Why: adopted caps still read as an open invitation to change them; confirm adoption status (the Master cap table carries these rows).
- **G5-1B33-08**: severity low, class Q, other, line 190
  - Current:
    > mapping exactly to the stated ×0.70–×1.60 bounds
  - Proposed:
    > QUESTION: at r = 9% the formula gives 1.54, not the 1.60 upper bound. Should this read "consistent with the stated ×0.70–×1.60 bounds"?
  - Why: "exactly" is arithmetically false; the fix is wording but touches a bound, so asked.

### `frameworks/Section_1B_v3_5_1_Reconciliation.md`

- **G5-1B351-01**: severity medium, class A, stale-ref, line 3
  - Current:
    > Read it together with the other Section_1B_* files (v3.3 Amendments, v3.6 Amendments, v3.7 Amendments, v3.8 Amendments); where they overlap, the later layer governs.
  - Proposed:
    > Read it together with the other Section_1B_* files (v3.3, v3.6, v3.7, v3.8, v3.9 and v3.10 Amendments); where they overlap, the later layer governs.
  - Why: omits v3.9 and v3.10.
- **G5-1B351-02**: severity medium, class Q, stale-ref, line 49
  - Current:
    > - Amendment 10 (intrinsic cross-check) triggers and mechanics are unaffected;
  - Proposed:
    > QUESTION: Amendment 10's text is not in any frameworks/ file (the section-1b skill also lists it NOT FOUND). Where does Amendment 10 live, or should this line say "Amendment 10 (text not in repo)"?
  - Why: cites an amendment a stage cannot read.

### `frameworks/Section_1B_v3_6_Amendments.md`

- **G5-1B36-01**: severity high, class B, stale-ref, line 3
  - Current:
    > NOTE: stage 11 does not yet inject this file (see the pipeline-sync audit); wiring is a pending operator decision.
  - Proposed:
    > NOTE: stage 11 reads this layer through the section-1b skill; verifier C reads this file directly.
  - Why: contradicts README ("Stage 11 injects all seven Section 1B layers") and the current wiring; a verifier reading the banner may treat Amendments 11-16 as not live.
- **G5-1B36-02**: severity medium, class A, stale-ref, line 3
  - Current:
    > and below the v3.7 Amendments and the v3.8 Amendments;
  - Proposed:
    > and below the v3.7, v3.8, v3.9 and v3.10 Amendments;
  - Why: omits the two top layers.
- **G5-1B36-03**: severity medium, class A, stale-ref, line 101
  - Current:
    > - **FTTCP v2.0 is the sole source of the forward verdicts and the Part B outputs**
  - Proposed:
    > - **FTTCP (v2.3) is the sole source of the forward verdicts and the Part B outputs**
  - Why: names v2.0 as the live protocol.
- **G5-1B36-04**: severity low, class A, stale-ref, line 71
  - Current:
    > This interacts with the projection-horizon rule in Master v3.5 Role 1:
  - Proposed:
    > This interacts with the projection-horizon rule in Master Role 1 (since v3.5; now v3.7, and Section 1B v3.8 Amendment 18.0):
  - Why: cites Master v3.5 as the live Role 1.

### `frameworks/Section_1B_v3_7_Amendments.md`

- **G5-1B37-01**: severity low, class A, stale-ref, line 3
  - Current:
    > Stage 11 reads this alongside the earlier Section 1B files and the later v3.8 Amendments (which govern the items they name where the layers overlap).
  - Proposed:
    > Stage 11 reads this alongside the earlier Section 1B files and the later v3.8, v3.9 and v3.10 Amendments (which govern the items they name where the layers overlap).
  - Why: omits v3.9 and v3.10.

### `frameworks/Section_1B_v3_8_Amendments.md`

- **G5-1B38-01**: severity high, class B, duplication, line 65
  - Current:
    > ## AMENDMENT 20 — RELATIVE VALUATION CROSS-CHECK (STEP 1C)
  - Proposed:
    > Insert below the heading: "> **SUPERSEDED by Section 1B v3.9 Amendment 20 (reissued 07-Sep-2026), which governs Step 1C in full. Kept for history; do not apply this text.**"
  - Why: Amendment 20 exists in v3.8 and v3.9 with different text (v3.9 adds 20.8 recompute and 20.9 "Operator-approved base still binds"; v3.8 20.0 says it "can supersede the pillar destination"); the v3.8 copy carries no mark.
- **G5-1B38-02**: severity medium, class B, contradiction, line 34
  - Current:
    > or the entry-zone formula (entry = exit-consistent fair value ÷ 1.25^N, MoS per evidence scale)
  - Proposed:
    > or the entry-zone formula (entry = exit-consistent fair value ÷ (1 + tier hurdle)^N, Tier A 1.25, Tier B 1.20, MoS per evidence scale)
  - Why: 1.25 alone drops Tier B (v3.3 Amendment 4.3); operator ruling OR-8 confirmed the tier divisor.
- **G5-1B38-03**: severity low, class A, stale-ref, line 11
  - Current:
    > consistent with Master v3.6's existing runway language
  - Proposed:
    > consistent with the Master's existing runway language (since v3.5)
  - Why: names Master v3.6 as current.
- **G5-1B38-04**: severity low, class A, other, line 83
  - Current:
    > still passes through the FTTCP Hurdle, the upside/downside gate,
  - Proposed:
    > still passes through the Section 1B Hurdle Ratio (a feasibility check, OR-2), the upside/downside gate,
  - Why: the Hurdle Ratio is Section 1B Amendment 2, not an FTTCP element; same label at line 90 "FTTCP Hurdle Ratio formula's inputs".

### `frameworks/Section_1B_v3_9_Amendments.md`

- **G5-1B39-01**: severity high, class Q, contradiction, line 126
  - Current:
    > or FTTCP Revenue Transition = ACCELERATING
  - Proposed:
    > QUESTION: FTTCP defines no ACCELERATING state (backward: FIRING / STAGNANT / DECLINING / VOLATILE; forward: FIRING / STARTING / STAGNANT / DECLINING). Which FTTCP Revenue verdict triggers fast-growth: forward FIRING, or another test? (Same text in Master line 1152 and section-1b chunk 08.)
  - Why: the fast-growth trigger points at a state no stage can emit, so the second branch never fires or fires on guesswork.
- **G5-1B39-02**: severity medium, class B, contradiction, line 54
  - Current:
    > - the entry zone (entry = exit-consistent fair value / 1.25^N, MoS per evidence scale).
  - Proposed:
    > - the entry zone (entry = exit-consistent fair value / (1 + tier hurdle)^N, Tier A 1.25, Tier B 1.20, MoS per evidence scale).
  - Why: same Tier B omission as G5-1B38-02; OR-8 confirmed the tier divisor.
- **G5-1B39-03**: severity medium, class Q, stale-ref, line 212
  - Current:
    > ## APPENDIX C — RULINGS REQUIRED FROM OPERATOR BEFORE STAGE 11
  - Proposed:
    > QUESTION: R1-R4 (E2E sector cap, ledger probabilities, Decision Status, repo ruling line) have no record: companies/E2E.md does not exist and the section-1b skill lists R1 as still pending (OR-4). Are R1-R4 resolved, and should this company-specific appendix move to companies/E2E.md?
  - Why: a per-company pending gate sits in the shared framework layer with no visible resolution.
- **G5-1B39-04**: severity low, class Q, contradiction, line 131
  - Current:
    > - Non-fast-growth names retain the existing price-based margin of safety.
  - Proposed:
    > QUESTION: v3.10 line 22 says "Conservatism lives in position size (Amendment 25), not in the projection" and CLAUDE.md cites "v3.9 Amendment 25" for the no-shading rule. A25 itself covers fast-growth names only. Is the no-shading rule v3.10 26.3 (all Role 1 projections) with A25 as the sizing tool for fast growers only? If so, CLAUDE.md should cite 26.3.
  - Why: the scope of "MoS as size" reads differently in A25, A26 and CLAUDE.md.

### `model: ""` self-report fields (Opus stages)`

- **X-03**: severity medium, class M, other, line 11:266, 12:175, 12:357, 13:332, stage-14-thesis.md:57, stage-15-devil.md:65
  - Current:
    > model: ""  # your exact model ID, as pinned in the agent frontmatter
  - Proposed:
    > model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
  - Why: a subagent does not see its own frontmatter, so it guesses its ID and can write an older model name into the block; the Sonnet and Haiku stages already hard-code theirs, and the run-pipeline DOWNSHIFT check reads this field.

### `prompts/00-orchestrator.md`

- **ORC-01**: severity high, class B, stale-ref, line 707
  - Current:
    > - stop_reason refusal: log, retry once on Opus 4.8, then halt with reason.
  - Proposed:
    > - stop_reason refusal: log, retry once on the stage's own frontmatter model, then halt with reason.
  - Why: names a retired model as the fallback; CLAUDE.md forbids changing a stage's model without editing its agent file.
- **ORC-02**: severity high, class B, stale-ref, line 684-685
  - Current:
    > 4. `fttcp-handoff.md`: the self-sufficient input package for manual FTTCP
    >    v1.2 deliberation in a separate Opus session with no source PDFs. The
  - Proposed:
    > 4. `fttcp-handoff.md`: the archive dossier of the run, self-sufficient for
    >    a reader with no source PDFs (the FTTCP v2.3 deliberation already ran in
    >    phase 2 via /fttcp). The
  - Why: cites FTTCP v1.2 as the live protocol and a manual session that phase 2 replaced; line 44 already calls this file "the archive dossier".
- **ORC-03**: severity high, class B, contradiction, line 692-696
  - Current:
    > Plus one Notion save to COMPANIES MASTER (data_source_id
    > 345bb2b9-d3ab-8032-9b46-000ba16ab827) per Notion_Save_Instructions.docx:
  - Proposed:
    > Plus one Notion save PAYLOAD for COMPANIES MASTER (data_source_id
    > 345bb2b9-d3ab-8032-9b46-000ba16ab827), written to
    > outputs/final/notion-payload.md; claude.ai executes the write:
  - Why: CLAUDE.md says "The pipeline produces payloads. claude.ai executes writes"; Notion_Save_Instructions.docx does not exist in the repo; runs live in runs/, not Drive.
- **ORC-04**: severity high, class B, contradiction, line 443-445
  - Current:
    > Stages 12a-12d run in parallel after stage 11.
  - Proposed:
    > Verifiers A, B, D and the Gate 0 + Emerging Moat half of C run in phase 1
    > after stage 9; C's valuation half runs in phase 3 after stage 11.
  - Why: contradicts PHASES (lines 19-27), which runs the verifiers in phase 1 when stage 11 does not yet exist; an orchestrator reading the table could wait for B11 in phase 1.
- **ORC-05**: severity medium, class B, other, line 423-441
  - Current:
    > | 13 | Synthesis | 13-synthesis-pipeline.md | Opus 5.5 | everything | final outputs |
  - Proposed:
    > | 9b | Halt 1 dossier | 09b-halt1-dossier.md | Sonnet 5.5 | B00-B09 + verifier blocks | `B09b-dossier` |
    > | 14 | Role 2 thesis | (agent file stage-14-thesis.md) | Opus 5.5 | B10, B11, deliberation record | `B14-thesis` |
    > | 15 | Role 3 devil's advocate | (agent file stage-15-devil.md) | Opus 5.5 | B14 + all blocks | `B15-devil` |
  - Why: the authoritative stage table omits three dispatched stages, so the dependency list and parallelism rules never mention them.
- **ORC-06**: severity medium, class A, stale-ref, line 437-440
  - Current:
    > | 12a | Verifier A: numerical | verifier-a-numerical.md | Haiku 4.5 |
  - Proposed:
    > | 12a | Verifier A: numerical | 12-verifiers-pipeline.md (VERIFIER A) | Haiku 4.5 |
  - Why: the "Prompt file" column names agent files, which do not exist under prompts/.
- **ORC-07**: severity medium, class Q, contradiction, line 425
  - Current:
    > | 0 | Input validation | (inline) | Haiku 4.5 | folder + manifest | `B00-inputs` |
  - Proposed:
    > QUESTION: no stage-00 agent exists and run-pipeline step 1 says "VALIDATE (stage 0, do this yourself)", which runs stage 0 on the session model; run-pipeline close-out also lists stage 0 as haiku-routed. Should stage 0 get a haiku agent file, or should this row read "orchestrator session model (inline)"?
  - Why: the model claim for stage 0 matches no agent frontmatter.
- **ORC-08**: severity medium, class M, stale-ref, line 61, 64
  - Current:
    > Run folder structure (Google Drive, mirrored to local before run):
    > /inflection-alpha-runs/<ticker>-<YYYY-MM-DD>/
  - Proposed:
    > Run folder structure (repo, collected by collect_to_repo.py):
    > runs/<ticker>-<YYYY-MM-DD>/
  - Why: CLAUDE.md STRUCTURE puts runs in runs/<ticker>-<date>/; the Drive path is a dead location.
- **ORC-09**: severity medium, class B, contradiction, line 738-740
  - Current:
    > - Never conflates the Emerging Moat scan (stage 7) with FTTCP: FTTCP runs
    >   inside stage 11's framework inputs as final synthesis, per project
    >   taxonomy.
  - Proposed:
    > - Never conflates the Emerging Moat scan (stage 7) with FTTCP: FTTCP is the
    >   phase 2 deliberation (/fttcp), a separate analysis with a separate name.
  - Why: lines 31-35 put FTTCP in phase 2 before valuation; "inside stage 11 as final synthesis" is the pre-phase-split design.
- **ORC-10**: severity medium, class Q, contradiction, line 673-676
  - Current:
    > 1. `business-narrative.md`: 10 to 12 lines, plain English, Keerti's written
  - Proposed:
    > QUESTION: prompt 13 now opens this file with the 12-18 sentence BUSINESS UNDERSTANDING NARRATIVE and follows it with a headline and 6 to 8 paragraphs. Should line 673 point to prompt 13 ("structure per prompts/13-synthesis-pipeline.md DELIVERABLE 1") instead of "10 to 12 lines"?
  - Why: two length specs for one file; the length is a rule, so it is marked MEANING-RISK.
- **ORC-11**: severity medium, class Q, contradiction, line 585-589
  - Current:
    > CRITICAL numerical finding (fabricated or materially misread figure), or any
    > verifier's acceptance_rate falls below 60%, the synthesis verdict is REWORK
  - Proposed:
    > QUESTION: prompts/12 header (lines 10-13) limits this to a CONFIRMED CRITICAL and to rates computed on a denominator of 4 or more, and section 5 here (646-650) drops sub-4 components. Should line 585-587 carry the same two qualifiers so the three statements agree?
  - Why: the REWORK trigger is stated three ways (here, prompt 12, prompt 13 rule 1) with different qualifiers.
- **ORC-12**: severity medium, class Q, other, line 174-176
  - Current:
    > first verification priority: stage 0 records them in `B00` and every later
    > stage checks them before its own work.
  - Proposed:
    > QUESTION: no stage prompt (01-13) or agent file mentions the Spear load-bearing facts. Should the orchestrator task message carry them, or should each stage prompt get one line ("Check the Spear load-bearing facts in B00 first")?
  - Why: CLAUDE.md SPEAR GATE makes this binding, but the stages are never told.
- **ORC-13**: severity low, class B, other, line 2, 4
  - Current:
    > ## Sonnet 5.5 Primary Pipeline with Claude Verification Layer
    > Replaces the Gemini (Jaimini) upstream pipeline. One model family end to end.
  - Proposed:
    > ## Claude pipeline: Sonnet 5.5 evidence stages, Opus 5.5 valuation and synthesis, Haiku 4.5 assembly and Verifier A
  - Why: history line costs tokens each read; the header undersells the three-model dispatch.
- **ORC-14**: severity low, class A, old-phrasing, line 649-650
  - Current:
    > points, and `overall: min of the four` let exactly that decide a verdict.
  - Proposed:
    > points.
  - Why: incident history, not an instruction.
- **ORC-15**: severity low, class A, duplication, line 5-7, 736-737
  - Current:
    > Never lets any exit PE enter from outside the Section 1B layer set (v3.3
  - Proposed:
    > Never lets any exit PE enter from outside the Section 1B layer set named at the top of this file.
  - Why: the seven-layer list is repeated verbatim; one copy per file is enough.

### `prompts/01, 02, 03, 04 vs agent template "NOT FOUND"`

- **X-02**: severity medium, class M, contradiction, line 01:20-21, 02:24, 03:27, 04:27 (agent template line 17)
  - Current:
    > mark it "N/A (not in provided data)" and score it 0
  - Proposed:
    > mark it "NOT FOUND" and score it 0
  - Why: CLAUDE.md says "NOT FOUND is the only valid fill" and the agent file says "NOT FOUND"; four spellings make Verifier A and stage 10 grep-matching unreliable.

### `prompts/01-gate-0-pipeline.md`

- **G0-01**: severity medium, class M, stale-ref, line 3, 201
  - Current:
    > # Cache boundary: everything above INPUT DATA is stable.
    > ## INPUT DATA (injected by orchestrator, variable, below cache boundary)
  - Proposed:
    > # Cache boundary: everything above INJECTED INPUTS is stable.
    > ## INJECTED INPUTS (variable, below cache boundary)
  - Why: the agent file tells the stage that everything above "INJECTED INPUTS" is its rules; this file has no such heading.
- **G0-02**: severity low, class A, other, line 163
  - Current:
    > Produce the full scorecard in the original dashboard format (all blocks,
  - Proposed:
    > Produce the full scorecard as a dashboard (all blocks,
  - Why: the model never sees "the original" format.

### `prompts/02-notes-triple-pass-pipeline.md`

- **N-01**: severity medium, class B, contradiction, line 19
  - Current:
    > - Extract exact numbers in ₹ Crores. Do not round.
  - Proposed:
    > - Extract exact numbers in the unit printed on the face of the document, and
    >   name that unit in the anchor. Do not round and do not convert; stage 10
    >   converts once.
  - Why: orchestrator UNITS DECLARATION (320-321) says conversion happens once at stage 10 and no stage converts silently.
- **N-02**: severity low, class A, old-phrasing, line 17-18
  - Current:
    > - Go through EVERY SINGLE NOTE NUMBER from Note 1 to the last note. Do
    >   not skip any note, even if it looks routine.
  - Proposed:
    > - Read every note from Note 1 to the last, routine ones included.
  - Why: caps and the restated "do not skip" add no instruction.
- **N-03**: severity low, class Q, piecemeal, line 2
  - Current:
    > # Model: Sonnet 5.5 | Three sequential API calls | Emits: B02-notes (after Pass 3)
  - Proposed:
    > QUESTION: the three passes run as three subagent calls with pass outputs re-injected. Is the separate-call design deliberate (fresh read per pass)? If not, one call with the finish line "B02 YAML emitted after Pass 3 consolidation" would save two re-reads of the AR and two prompt prefills.
  - Why: piecemeal tasking; marked as a question because the triple-pass independence may be the point.

### `prompts/03-ar-deep-dive-pipeline.md`

- **AR-01**: severity medium, class B, contradiction, line 22-23
  - Current:
    > 2. Do NOT summarize loosely. Exact numbers in ₹ Crores, exact policy
  - Proposed:
    > 2. Do NOT summarize loosely. Exact numbers in the unit printed in the source (named in the anchor), exact policy
  - Why: same units conflict as N-01.
- **AR-02**: severity low, class M, old-phrasing, line 7-8, 152-156
  - Current:
    > #   1.3 — ar_new_downstream_entities YAML feed for Step 10.5B added.
    > # RATIONALE (protocol note): silence audits (Phase 4) catch what is not there; 6E
  - Proposed:
    > move the changelog (7-8) and the RATIONALE comment (152-156) to git history or a CHANGELOG line; keep the rule text.
  - Why: version history and rationale are read and paid for on every run without changing behaviour.

### `prompts/04-business-model-pipeline.md`

- **BM-01**: severity low, class B, other, line 80
  - Current:
    > The full card in the original box format, every field filled.
  - Proposed:
    > A one-page summary card in a box layout, every field filled (fields: the Section 1 summary table plus primary valuation method and top 5 must-track metrics).
  - Why: the stage cannot see "the original" format. (Field list is wording only; if the operator wants a specific card, name it.)

### `prompts/05-concall-pipeline.md`

- **CC-02**: severity high, class Q, contradiction, line 88-91
  - Current:
    > This grade feeds the Role 1 probability weights directly (A=Excellent
    > 20/50/30, B=Good 25/50/25, C=Mixed 35/45/20, D=Poor 45/40/15), so
  - Proposed:
    > QUESTION: Section 1B v3.10 Amendment 26.4 keys the 4D weights to "the trailing four quarters of delivery (the Role 5 credibility ratio), not whole-company history", and "Mixed history plus four quarters of delivery = Good weighting". This stage reads three transcripts and grades on the whole promise-delivery record. Should 4C state that the grade is set on the trailing four quarters of delivery (period stated when fewer exist), and should the weights table here be replaced by a pointer to Master 4D so it cannot drift from prompt 11 line 243-244?
  - Why: the stage that is the SOLE source for the weights does not carry the A26.4 basis that CLAUDE.md NEVER-list binds.
- **CC-01**: severity medium, class A, stale-ref, line 5
  - Current:
    > # the Role 1 valuation (per Master Prompt v3.3). Grade it carefully.
  - Proposed:
    > # the Role 1 valuation (per Master Prompt v3.7 Section 4D, as amended by Section 1B v3.10 Amendment 26.4).
  - Why: cites v3.3 as the live authority; "Grade it carefully" is old-model phrasing.

### `prompts/06-peer-concall-pipeline.md`

- **PC-01**: severity low, class A, other, line 100-118 (YAML 129-159)
  - Current:
    > ## PART 5: CROSS-PEER HYPOTHESIS (mandatory closing step)
  - Proposed:
    > cross_peer_hypothesis: ""     # Part 5 hypothesis, or the exact no-hypothesis line
  - Why: a mandatory output with no block field never reaches downstream stages, which read blocks.
- **PC-02**: severity low, class M, duplication, line 115
  - Current:
    > - Do not force a hypothesis where none exists. Absence of pattern is itself a finding.
  - Proposed:
    > delete (line 112-114 already says it).
  - Why: same rule twice in one list.
- **PC-03**: severity low, class A, old-phrasing, line 1, 4
  - Current:
    > # STAGE 6: PEER CONCALL VERIFICATION (PIPELINE MODE, NEW PROMPT)
  - Proposed:
    > # STAGE 6: PEER CONCALL VERIFICATION (PIPELINE MODE)
  - Why: "NEW PROMPT" and "(was unversioned = 1.0)" are history.

### `prompts/07-emerging-moat-pipeline.md`

- **EM-01**: severity medium, class B, contradiction, line 5-6
  - Current:
    > # FTTCP. FTTCP is a separate, later synthesis that runs inside the
    > # valuation stage's framework inputs. Never conflate the two.
  - Proposed:
    > # FTTCP. FTTCP is the separate phase 2 deliberation (/fttcp), run before
    > # valuation. Never conflate the two.
  - Why: describes the pre-phase-split design; FTTCP v2.3 states it "runs BEFORE valuation".
- **EM-02**: severity medium, class A, duplication, line 11-18 (also 10 and 224-225)
  - Current:
    > # THRESHOLDS RULING (operator, 20-Aug-2026): thresholds are ABSOLUTE on
  - Proposed:
    > # THRESHOLDS RULING (operator, 20-Aug-2026): see Section 5.
  - Why: the same ruling (bands absolute, ceiling 92, I1/I2 crossing legitimate, review checkpoint) is stated in the header, in Section 5 (177-181) and in the YAML comment; keep the Section 5 copy only.

### `prompts/08-promoter-pipeline.md`

- **PR-01**: severity high, class Q, contradiction, line 2, 11-14
  - Current:
    > # Model: Sonnet 5.5 + web search enabled | Emits: B08-promoter
  - Proposed:
    > QUESTION: CLAUDE.md SPEAR GATE says "this container has no live web access" and TEAM WORKFLOW says Claude Code "has NO live web access", yet stage-08 and stage-09 agent files grant WebSearch and WebFetch and these prompts depend on them. Which binds? If no web, should stages 8 and 9 write searches as PENDING LIVE VERIFICATION items for claude.ai (the 09b Section 4d pattern) instead of searching?
  - Why: a stage told to search a web it cannot reach either returns partial or fills from memory, which the NEVER-list forbids.
- **PR-02**: severity medium, class Q, other, line 98-100, 118
  - Current:
    > 6A scorecard: the 10 dimensions, each rated ✅/⚠️/🔴 strictly on
    > 6E final output card in the standard format.
  - Proposed:
    > QUESTION: "the 10 dimensions", "the standard matrix" and "the standard format" are not defined in this file or any file the stage reads. Name them here, or point to the file that holds them?
  - Why: the model invents the dimensions each run, so scorecards are not comparable across runs.
- **PR-03**: severity low, class A, old-phrasing, line 46
  - Current:
    > ## SECTION 2: LEGAL & REGULATORY RECORD (most critical, search hardest)
  - Proposed:
    > ## SECTION 2: LEGAL & REGULATORY RECORD
  - Why: effort exhortation; the section's length already signals weight.

### `prompts/09-tam-pipeline.md`

- **TAM-01**: severity medium, class Q, contradiction, line 33
  - Current:
    > 6. CONSERVATIVE BIAS: when choosing between estimates, take the lower.
  - Proposed:
    > QUESTION: the SOM-implied CAGR is a "FORMAL handoff" that stage 11 uses to "justify or cut" its base revenue (prompt 11 line 245-246). v3.9 Amendment 25 / v3.10 26.3 bar shading a Role 1 input to be safe. Should stage 9 report the most evidenced estimate with both readings (conservative and realistic, which line 60 already produces) and leave the choice to stage 11, rather than take the lower?
  - Why: a lower-by-rule SOM feeds a shaded cap into the base case through the cross-check.
- **TAM-02**: severity low, class A, old-phrasing, line 42
  - Current:
    > wrong definition makes every later number useless; spend effort here.
  - Proposed:
    > wrong definition makes every later number useless.
  - Why: effort exhortation.
- **TAM-03**: severity low, class Q, other, line 93
  - Current:
    > growth. 5C runway classification per the standard matrix (MASSIVE /
  - Proposed:
    > QUESTION: which matrix? State the class boundaries here or name the file.
  - Why: undefined reference, same as PR-02.

### `prompts/09b-halt1-dossier.md`

- **DOS-01**: severity medium, class M, contradiction, line 132, 329
  - Current:
    >     is the observation Stage 11 FTTCP tests. Until it fires, the
    >     proof_gate: ""             # B3: exact metric + threshold Stage 11 FTTCP tests
  - Proposed:
    >     is the observation FTTCP (phase 2, /fttcp) tests. Until it fires, the
    >     proof_gate: ""             # B3: exact metric + threshold FTTCP (/fttcp) tests
  - Why: FTTCP is the phase 2 deliberation, not part of stage 11.
- **DOS-02**: severity medium, class A, duplication, line 9-14 (repeats 47-56)
  - Current:
    > # ONE SCOPED EXCEPTION: Section 2 Part B4 (the recognition gap) poses, as an
  - Proposed:
    > # NO VALUATION: rule 4 below (one scoped exception, Section 2 Part B4).
  - Why: the no-valuation rule and its B4 exception appear twice in this file and a third time in the agent file.
- **DOS-03**: severity medium, class B, contradiction, line 361-366
  - Current:
    > ALL COMMITTED BLOCKS (B00 through B09 + verifier blocks B12a/B12b/B12c-
    > partial/B12d), inline:
  - Proposed:
    > ALL COMMITTED BLOCKS (B00 through B09 + verifier blocks B12a/B12b/B12c-
    > partial/B12d), as file paths under outputs/blocks/:
  - Why: orchestrator section 9 "JIT context is law: task messages carry file PATHS and small YAML blocks only".
- **DOS-04**: severity low, class A, other, line 5
  - Current:
    > # to decide KILL / SHALLOW WATCH / PROCEED.
  - Proposed:
    > # to decide KILL / SHALLOW / PROCEED.
  - Why: CLAUDE.md PIPELINE SEQUENCE names the choice KILL / SHALLOW / PROCEED.

### `prompts/10-input-assembly-pipeline.md`

- **VA-01**: severity high, class Q, contradiction, line 19-22
  - Current:
    >    upstream stages disagree on a value, record BOTH with anchors under
    >    conflicts[] and put the more conservative one in the table, marked.
  - Proposed:
    > QUESTION: CLAUDE.md ("Never shade an input to be safe"), v3.9 A25 and prompt 11 (override 3, and the Pillar 2 INDETERMINATE both-readings rule, section-1b OR-5) all say carry both readings and the separating observation. Should a JUDGMENT conflict go to the table as "CONFLICT: both readings" (both values, both anchors) for stage 11 to resolve, instead of the conservative pick?
  - Why: the assembler pre-shades a Role 1 input before the stage that is told never to shade sees it.
- **VA-02**: severity medium, class Q, other, line 48-86, 123-128
  - Current:
    > Blocks B01 through B09: {{ALL_BLOCKS_YAML}}
  - Proposed:
    > QUESTION: stage 11 reads B10.entity_count, B10.seasonal, the operator-approved exit PE base and pe_basis, the expectation ledger / FTTCP C.2 credit, and a live peer table when present; /finalize step supplies the deliberation record in the task message. None of these appear in THE TABLE TO FILL or in INJECTED INPUTS here. Add "FTTCP deliberation record: {{FTTCP_DELIBERATION_PATH}}" to INJECTED INPUTS and those fields to the table and YAML?
  - Why: the prompt that claims to be "the ONLY assembler of Role 1 inputs" does not list several inputs stage 11 depends on; today they arrive only through the task message.
- **VA-03**: severity low, class A, other, line 127
  - Current:
    > Results PDFs (3 quarters): {{RESULTS_EXTRACTS}}
  - Proposed:
    > Results PDFs (paths, up to 3 most recent): {{RESULTS_PDF_PATHS}}
  - Why: JIT law (paths, not contents) and the 0-3 results contract.

### `prompts/11-valuation-pipeline.md`

- **VAL-01**: severity medium, class Q, duplication, line 193-198, 226-235, 243-244
  - Current:
    > - 4D probability weights come ONLY from B10.credibility_grade
    >   (A 20/50/30, B 25/50/25, C 35/45/20, D 45/40/15).
  - Proposed:
    > QUESTION: line 14 says "If the skill and anything in this wrapper ever conflict, THE SKILL WINS", yet the wrapper restates the Pillar 1 formula, the Hurdle thresholds (1.953 / 1.728) and the 4D weights numerically. Replace each restated number with its chunk cite (chunk 01, chunk 06, chunk 17) so there is one numeric source? (Also 4D weights should name the A26.4 trailing-four-quarter basis, as line 175-177 already does.)
  - Why: three numeric copies (Master, skill, wrapper, plus prompt 05) mean a future amendment must be edited in four places.
- **VAL-02**: severity low, class A, other, line 215-216
  - Current:
    >   OR-5), and cap the run at PROCEED WITH CAVEATS with the missing evidence
  - Proposed:
    >   OR-5), and record in flags[] (FLAG-CASH, INDETERMINATE) that the gate
    >   verdict caps at PROCEED WITH CAVEATS, with the missing evidence
  - Why: B11 emits BUY/WATCHLIST/AVOID, not the five-verdict set; the cap belongs to stage 13 and needs a block field to travel.
- **VAL-03**: severity low, class A, stale-ref, line 324
  - Current:
    > {{MASTER_PROJECT_PROMPT_V36_ROLE1_SECTIONS}}
  - Proposed:
    > {{MASTER_PROJECT_PROMPT_ROLE1_SECTIONS}}  (file Master_Project_Prompt_v3_6.md, content v3.7)
  - Why: marker name reads as v3.6 being live.
- **VAL-04**: severity low, class A, old-phrasing, line 99-100
  - Current:
    >    entity (entity name in the block). INDIAGLYCO discarded a run for valuing one
    >    consolidated entity against a three-entity dossier; this gate prevents it.
  - Proposed:
    >    entity (entity name in the block).
  - Why: incident history, not instruction.

### `prompts/12-verifiers-pipeline.md`

- **VER-01**: severity high, class B, contradiction, line 2
  - Current:
    > # Four independent calls, fresh context each, run in parallel after B11.
  - Proposed:
    > # Four independent calls, fresh context each. Phase 1: A, B, D and C's
    > # Gate 0 + Emerging Moat half, after stage 9. Phase 3: C's valuation half, after B11.
  - Why: contradicts the orchestrator PHASES and this file's own phase-1 scope for Verifier C (lines 210-216).
- **VER-02**: severity high, class B, contradiction, line 206-209
  - Current:
    >   and the 20-category scan rules (prompts/07-emerging-moat-pipeline.md),
    >   for the B01 and B07 audits. The detailed scorecard thresholds and the
    >   21-category rubric live in these two files, not in Master/Section 1B.
  - Proposed:
    >   and the 22-category scan rules (prompts/07-emerging-moat-pipeline.md),
    >   for the B01 and B07 audits. The detailed scorecard thresholds and the
    >   22-category rubric (23 scored rows with R1) live in these two files, not in Master/Section 1B.
  - Why: rule 3 (line 227) and rule 8 audit 23 rows and categories 21-22; the scope text says 20 and 21, so the verifier holds two rubric sizes.
- **VER-03**: severity high, class Q, contradiction, line 262-263
  - Current:
    >    SOM cross-check performed; every unresolved input handled by the
    >    stated conservative rule, no silent fills; one-improvement-one-
  - Proposed:
    > QUESTION: prompt 11 override 3 now handles an unresolved input with "Both readings ... Separating observation ... confirm-by", and this rule's own Growth Symmetry block (line 240-241) FAILS an input lowered "to be conservative". Should "the stated conservative rule" read "the override-3 both-readings rule"?
  - Why: as written the verifier can pass a shaded input or fail a compliant one.
- **VER-04**: severity high, class B, contradiction, line 298-300
  - Current:
    >    outputs/reports/09b-understanding-dossier.md exists and contains all
    >    five sections in order; Section 1 ends with exactly one verdict line
    >    (CORPUS CURRENT or CORPUS GAPPED); Section 2 is marked DRAFT - PENDING
  - Proposed:
    >    outputs/reports/09b-understanding-dossier.md exists and contains all
    >    six sections in order (Section 6 annex ends with the corpus commit hash
    >    line); Section 1 ends with exactly one verdict line (CORPUS CURRENT,
    >    CORPUS GAPPED, or CORPUS GAPPED-FRESHNESS); Section 2 is marked DRAFT - PENDING
  - Why: prompt 09b now has six sections and a third verdict; this check would force a hard REWORK on a correct dossier with a freshness gap.
- **VER-05**: severity medium, class M, stale-ref, line 1-32 (no INJECTED INPUTS heading)
  - Current:
    > INPUTS: {{ALL_STAGE_REPORTS}} + {{ALL_SOURCE_PDFS}}
  - Proposed:
    > see AG-V-01 (fix in the agent files), or rename each "INPUTS:" line to "INJECTED INPUTS:".
  - Why: the agent pointer names a heading this file lacks.
- **VER-06**: severity medium, class M, duplication, line 10-32
  - Current:
    > # HARD SOURCE-FIDELITY GATE: Verifier A (Haiku) is the SOLE and FINAL
  - Proposed:
    > keep this header copy (the verifier file is the natural home); in prompt 00 (591-605) and prompt 13 (116-124) replace the restatement with "Source-fidelity gate: prompts/12-verifiers-pipeline.md header."
  - Why: see AG-VA-01; five copies.
- **VER-07**: severity low, class A, other, line 329
  - Current:
    >    credited in the price with no ledger row HALTS stage 11 (an expectation
  - Proposed:
    >    credited in the price with no ledger row forces REWORK for stage 11 (an expectation
  - Why: the verifier runs after stage 11, so it cannot halt it; the same sentence already says "REWORK for stage 11".
- **VER-08**: severity low, class A, other, line 363
  - Current:
    > business_understanding_narrative: {present: false, five_questions_answered: false, prose_only: false, section6_candidates_named: 0, valuation_vocab_leak: false, fails: []}  # rule 7; any fail = REWORK stage 13
  - Proposed:
    > (same line, comment "# rule 9; any fail = REWORK stage 13")
  - Why: the narrative check is rule 9; rule 7 is method plurality.
- **VER-09**: severity low, class A, other, line 127-128, 381
  - Current:
    > You are an independent concall auditor. You receive 15 raw transcripts
    > (3 main company, 12 peers)
  - Proposed:
    > You are an independent concall auditor. You receive the raw transcripts
    > (up to 3 main company, up to 12 peers)
  - Why: the input contract is 0-3 and 0-12; a fixed count invites a "missing transcript" finding.

### `prompts/13-synthesis-pipeline.md`

- **SYN-01**: severity high, class B, contradiction, line 101-103
  - Current:
    > in one line (RE-RATING LIVE / EARNINGS-ONLY / RESEARCH-WATCH / VALUE-TRAP RISK
    > / CONTRADICTION / AVOID). It informs the value-trap read and the WATCH
  - Proposed:
    > in one line (RE-RATING LIVE / EARNINGS-ONLY / RESEARCH-WATCH / PRICED
    > NARRATIVE (TRAP) / VALUE-TRAP RISK / CONTRADICTION / AVOID). It informs the value-trap read and the WATCH
  - Why: the CLAUDE.md matrix has seven postures; the list omits PRICED NARRATIVE (TRAP), the cell CLAUDE.md calls "the most seductive", so stage 13 cannot name it.
- **SYN-02**: severity medium, class Q, contradiction, line 113-114
  - Current:
    > 1. REWORK if the confidence delta forces it (any B12a CRITICAL, or any
    >    verifier acceptance_rate <60%, or overall delta <60). REWORK judges
  - Proposed:
    > QUESTION: same as ORC-11. Should this read "any CONFIRMED B12a CRITICAL, or any verifier acceptance_rate <60% on a denominator of 4 or more, or overall delta <60 where overall is computed"?
  - Why: prompt 12 header and orchestrator section 5 carry these qualifiers; this rule does not.
- **SYN-03**: severity medium, class A, stale-ref, line 205-206
  - Current:
    > Purpose: a self-sufficient input package for manual FTTCP v2.3
    > deliberation in a separate Opus session that will NOT have the source
  - Proposed:
    > Purpose: the run's archive dossier, self-sufficient for a reader that will
    > NOT have the source
  - Why: the FTTCP deliberation already ran in phase 2 before stage 13; orchestrator line 44 calls this file "the archive dossier".
- **SYN-04**: severity medium, class A, other, line 370-374
  - Current:
    > All blocks B01 through B12d: {{ALL_BLOCKS_YAML}}
  - Proposed:
    > All blocks B01 through B15 (including B09b, B14-thesis, B15-devil), as paths: {{ALL_BLOCK_PATHS}}
    > FTTCP deliberation record: {{FTTCP_DELIBERATION_PATH}}
    > Signed Mental Model (companies/<TICKER>.md): {{COMPANY_MEMORY_PATH}}
  - Why: the posture step (96-106) reads "the signed model", UGLINESS from 09b and the FTTCP proof gate, none of which are in the listed inputs.
- **SYN-05**: severity medium, class A, stale-ref, line 295-300, 348
  - Current:
    > After the three files, emit a notion_save block the orchestrator uses
    > per Notion_Save_Instructions: page title, THEN the BUSINESS UNDERSTANDING
  - Proposed:
    > After the four files, emit a notion_save block for claude.ai to execute
    > (the pipeline never writes): page title, THEN the BUSINESS UNDERSTANDING
  - Why: four files, not three; Notion_Save_Instructions is not in the repo; Drive is retired; CLAUDE.md says claude.ai executes writes.
- **SYN-06**: severity low, class B, contradiction, line 159-161
  - Current:
    > lowest tested price since listing, print: "MARKET-UNLIKELY ZONE —
  - Proposed:
    > lowest tested price since listing, print: "MARKET-UNLIKELY ZONE:
  - Why: CLAUDE.md STYLE bans em-dashes in synthesis outputs, and this line is printed into fttcp-recommendation.md verbatim.

### `prompts/quarterly-00-orchestrator.md`

- **ORCH-Q-01**: severity high, class Q, contradiction, line 313
  - Current:
    > INCOMPLETE audit after two loops, missing protocol files) halt the run.
  - Proposed:
    > QUESTION: Same split as CMD-RQ-01. Lines 207-210 cap the loop at one iteration then ask the operator; line 313 says the halt comes after two loops. Which is the rule? Also, should the halt list name the A2 COST CHECK (line 155-156) and the orphan-ID gate (line 302-304), which also halt?
  - Why: The closing halt list contradicts the loop cap stated above it.
- **ORCH-Q-02**: severity high, class B, contradiction, line 271
  - Current:
    > 4. The text layer is not trusted for image-heavy pages. OCR fallback is
  - Proposed:
    > 4. Text layer first (A1 TEXT-LAYER GATE). A document with a text layer is extracted text-only. OCR runs only on a no-text-layer scan, or on a logged zero-character page that holds a data-bearing figure.
  - Why: Rule 4 is the pre-gate per-page OCR rule; the SEQUENCE step 1 (lines 135-138) and A1 superseded it, and the old text was never removed.
- **ORCH-Q-03**: severity high, class Q, contradiction, line 7
  - Current:
    > a protocol file conflict on analysis, the protocol file wins. Where they
  - Proposed:
    > QUESTION: Role 4 and Role 5 carry interactive STOP and "stop and ask" lines (e.g. Role 4 line 60 "If Notion has no page for the company, stop and ask"; line 218 "Get explicit GO"). This orchestrator says A4 never stops and, at lines 187-189, routes a missing Notion page to a PRE-THESIS READ. Under the precedence clause the protocol wins on analysis. Add an explicit line: "Under /run-quarterly, protocol STOP lines are section checkpoints, not waits. A4 runs every step through and flags; the operator reviews the merged review once, at the end"?
  - Why: As written, the precedence clause hands A4 a protocol instruction to halt that its agent file forbids.
- **ORCH-Q-04**: severity medium, class Q, other, line 171
  - Current:
    > first per Step 0A and passes its Decision Status and monitoring checklist
  - Proposed:
    > QUESTION: Role 4 Step 0A and Role 5 Step 0A need more than Decision Status and the monitoring checklist: Bear/Base/Bull projections (Step 6A), thesis-broken conditions (6C), growth triggers (6D, R5 8A), four-pillar values (Step 7), the prior quarter's Questions-for-Management table (R4 line 662, R5 3E), and the previous concall promise log (R5 Step 3). Should the orchestrator pass those fields inline, or should A4 mark those steps ND with "not passed"?
  - Why: A4 cannot call Notion, so every Step 0A field not passed inline becomes an unexplained ND.
- **ORCH-Q-05**: severity medium, class Q, stale-ref, line 188
  - Current:
    > pass the Spear Pass template instead
  - Proposed:
    > QUESTION: No file in the repo defines a "Spear Pass template". Which file is it (a companies/<TICKER>.md Spear line, a claude.ai spear output, or a file still to add to frameworks/)? Name its path here.
  - Why: The orchestrator cannot pass a file that does not exist; Document Review Protocol line 53-54 depends on it.
- **ORCH-Q-06**: severity medium, class B, contradiction, line 229
  - Current:
    > 7. COMMIT the run folder (`work/` files) with message
  - Proposed:
    > 7. COMMIT the run folder (`extracted/`, `work/`, and `session-cost.md`) with `git commit -q -m "quarterly review: <ticker> <quarter>"`. End the report with the commit hash and `git log -1 --stat`. Report
  - Why: "`work/` files" leaves the A1 evidence spine and session-cost.md uncommitted, and CLAUDE.md requires the hash on every commit report.
- **ORCH-Q-07**: severity medium, class Q, other, line 177
  - Current:
    > PROTOCOL SCOPING (the analyst-stage token discipline). Pass ONLY the protocol
  - Proposed:
    > QUESTION: For a FULL QUARTER, Role 4 Step 6.5 and Step 7 (A21 base refresh, destination PE recompute, Hurdle Ratio, fair values) and Role 5 Step 8D need the Section 1B layer set, which this block forbids A4 to load. Line 28 also says the pipeline "does NOT run valuation". Should A4 mark Steps 6.5/7 and R5 8D "deferred to /fttcp and Role 1" and flag pillar-relevant facts only?
  - Why: A4 is told to run a step whose authority file it may not open.
- **ORCH-Q-08**: severity low, class B, contradiction, line 305
  - Current:
    > - analyst_note handoff (bounded prose). Every agent's YAML block carries an
  - Proposed:
    > - analyst_note handoff (bounded prose). The A2-A5 YAML blocks carry an
  - Why: A1's YAML (prompt lines 223-252) has no analyst_note field, and A1 is mechanical.

### `prompts/quarterly-a1-extractor.md`

- **PR-A1-01**: severity low, class A, old-phrasing, line 9
  - Current:
    > NOT interpret. You do NOT summarise. You do NOT form a view. A downstream agent
  - Proposed:
    > not interpret, summarise, or form a view. A downstream agent
  - Why: Three all-caps NOTs restate operating rule 2 (lines 15-17); one plain sentence does the job.

### `prompts/quarterly-a2-enumerator.md`

- **PR-A2-01**: severity medium, class B, contradiction, line 60
  - Current:
    > below tables). Record: note number, line number, first 15 words.
  - Proposed:
    > below tables). Record: note number and its structured row ID (the ID carries the line; do not re-copy note text).
  - Why: The DE-DUPLICATION CONTRACT (lines 25-40) bans re-copying claim text; "first 15 words" orders it.
- **PR-A2-02**: severity medium, class B, contradiction, line 85
  - Current:
    > 2. Every speaker turn, numbered sequentially, with speaker and first 10 words.
  - Proposed:
    > 2. Every speaker turn, numbered sequentially, with speaker and its structured row ID (no re-copied text).
  - Why: Same de-dup conflict as PR-A2-01.

### `prompts/quarterly-a3-forensics.md`

- **PR-A3-01**: severity low, class B, contradiction, line 98
  - Current:
    > Notion thesis (provided by A4; here just flag the spread).
  - Proposed:
    > Notion thesis (A4 runs that cross-check; here just flag the spread).
  - Why: A4 runs after A3 and cannot provide A3 anything.

### `prompts/quarterly-a4-analyst.md`

- **PR-A4-01**: severity high, class B, contradiction, line 52
  - Current:
    > - The protocol files (Role 4, Role 5) and Master v3.7 for framework context.
  - Proposed:
    > - The protocol file(s) your task message passes (Document Review, or Role 4 and/or Role 5). Master v3.7 is framework context by reference only; you never load it.
  - Why: Lines 11-14, the agent file, and the orchestrator all forbid loading Master; this line tells A4 to consume it.
- **PR-A4-02**: severity high, class B, contradiction, line 65
  - Current:
    > - The position-decision branch (protocol 8A, or 8A-W for warrant cases).
  - Proposed:
    > - The position-decision branch (protocol 8A for held names, or 8A-W for watchlist / non-held names).
  - Why: Role 4 Step 8A-W is the WATCHLIST / non-held branch, not a warrant branch; the wrong label can misroute the position decision.
- **PR-A4-03**: severity medium, class Q, other, line 64
  - Current:
    > - Pillar re-validation.
  - Proposed:
    > QUESTION: See ORCH-Q-07. A4 may not load Section 1B, so it cannot recompute destination PE, the Hurdle Ratio, or fair values (Role 4 Step 7). Change to "Pillar evidence: flag each fact that moves a pillar input; the recompute is deferred to /fttcp and Role 1"?
  - Why: The line orders work whose authority file A4 is barred from.
- **PR-A4-04**: severity medium, class B, contradiction, line 126
  - Current:
    > cash_conversion: ""            # structural | growth-induced | INDETERMINATE
  - Proposed:
    > cash_conversion: ""            # structural | growth-induced | INDETERMINATE | INDETERMINATE-WITH-DIRECTION
  - Why: Document Review Protocol v1.1 step 5b adds INDETERMINATE-WITH-DIRECTION; the YAML enum cannot carry it.
- **PR-A4-05**: severity medium, class Q, contradiction, line 85
  - Current:
    > findings. PROVENANCE-LABEL every figure: mark whether it comes from prior
  - Proposed:
    > QUESTION: For a FULL QUARTER the brief uses a two-way label (prior Notion/peer work vs this quarter's filings). CLAUDE.md says "Every claim carries its evidence tier", and the Document Review Protocol uses the five-tier FILED / AGENCY / MGMT / SECONDARY / INFERENCE set. Should the full-quarter brief use the five tiers too?
  - Why: Two provenance schemes run in one pipeline depending on doctype.

### `prompts/quarterly-a5-adversary.md`

- **PR-A5-01**: severity medium, class B, contradiction, line 86
  - Current:
    > 1. Complete all three audits in one run. Never stop to ask.
  - Proposed:
    > 1. Complete all four audits (0-3) in one run. Never stop to ask.
  - Why: The section header at line 25 is "THE FOUR AUDITS"; "three" drops the audit 0 hard gate.
- **PR-A5-02**: severity medium, class B, contradiction, line 29
  - Current:
    > non-empty: (1) a summary narrative (10-20 lines), (2) SECTOR intelligence,
  - Proposed:
    > non-empty: (1) a summary narrative (10-20 lines, or 200-400 words when the Document Review Protocol governs), (2) SECTOR intelligence,
  - Why: A4 line 89-93 lets the Document Review Protocol's 200-400 word length win; A5 can fail a compliant brief on line count.

### `team_workflow_project_instructions.md`

- **TWF-01**: severity high, class Q, contradiction, line 85
  - Current:
    > (the ones DISPATCH routes to haiku: stage 0 validation, stage 10 assembly, verifier A)
  - Proposed:
    > QUESTION: same as CMD-RP-01. Align this copy to whatever the operator rules there.
  - Why: duplicate of the run-pipeline defect; the claude.ai copy will audit Claude Code against a wrong list.
- **TWF-03**: severity high, class Q, contradiction, line 14
  - Current:
    > Claude Code has no live-web access and never runs this phase.
  - Proposed:
    > QUESTION: same as CMD-STEP1-01; operator ruling 2026-09-05 has /step1 replace the web spear with Claude Code live-web intake. Record it here?
  - Why: contradicts step1.md, the current intake path.
- **TWF-02**: severity medium, class B, contradiction, line 88
  - Current:
    > A DOWNSHIFT FAILURE or a COST SPIKE also earns a one-line entry in LESSONS.md naming the stage.
  - Proposed:
    > A DOWNSHIFT FAILURE or a COST SPIKE also earns a one-line entry in LESSONS_ARCHIVE.md naming the stage, plus a LESSONS.md OPEN ACTIONS line only while it stays open.
  - Why: run-pipeline.md line 408-414 and CLAUDE.md MEMORY send run history to the archive; the active file is budget-capped.
- **TWF-04**: severity low, class A, stale-ref, line 1-3 (versus CLAUDE.md line 244)
  - Current:
    > CLAUDE WEB × CLAUDE CODE — TEAM WORKFLOW v2.2 FOR COMPANY ANALYSIS
  - Proposed:
    > In CLAUDE.md line 244, change "(v2, five hand-offs:" to "(v2.2, five hand-offs:".
  - Why: CLAUDE.md cites v2 for a file whose banner is v2.2.
- **TWF-05**: severity low, class B, other, line 31
  - Current:
    > Claude Code runs stages 14 and 15 and `/finalize`.
  - Proposed:
    > Claude Code runs `/finalize`, which runs stages 10, 11, 14, 15, Verifier C's valuation half and the final synthesis.
  - Why: reads as if 14 and 15 run before or apart from /finalize; finalize.md steps 3-4 run them inside it.
- **TWF-06**: severity low, class A, stale-ref, line 107
  - Current:
    > End of v2.2. Replace the project-knowledge copy of team_workflow_project_instructions.md with this file and ferry the implementation prompt to Claude Code.
  - Proposed:
    > End of v2.2.
  - Why: one-time rollout instruction; the "implementation prompt" no longer exists and CLAUDE.md says the operator syncs the copies.
- **TWF-07**: severity low, class A, other, line 29
  - Current:
    > one verdict and one P/E gate card PER ENTITY
  - Proposed:
    > one verdict and one P/E BASE CARD PER ENTITY
  - Why: fttcp.md names the artifact "P/E BASE CARD"; two names for one card.

### `verifiers/README.md`

- **VR-01**: severity medium, class A, stale-ref, line 11
  - Current:
    > Grades the written FTTCP draft against the FTTCP v2.1 rubric using a model from a
  - Proposed:
    > Grades the written FTTCP draft against the FTTCP v2.3 rubric (file FTTCP_v2_1_Consolidated.md) using a model from a
  - Why: cites v2.1 as the live protocol; note fttcp_crossgrade.py line 14 carries the same "FTTCP v2.1 rubric" text (outside this audit's files) and its fixed rubric criteria should be checked against v2.3.

