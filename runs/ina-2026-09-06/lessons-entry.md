# LESSONS ENTRY — INA (Insolation Energy Ltd), run 2026-09-06

BRANCH NOTE FOR THE OPERATOR. CLAUDE.md requires that framework and prompt
amendments travel on a SEPARATE branch and PR from run outputs, and that an
amendment never rides a run PR. LESSONS.md and LESSONS_ARCHIVE.md are framework
memory, not run outputs. This file therefore holds the entries rather than
editing those two files from the run branch. Append them on a framework branch.

---

## FOR LESSONS_ARCHIVE.md (dated run entry, append verbatim)

### 2026-09-06 — INA (Insolation Energy Ltd), phase 1

Verdict REWORK on the confidence rule, overall 42. Scope stages 5 and 6 only;
the evidence base held (verifier A 83%, zero CRITICAL).

- Verifier B found 59 concall red flags where stages 5 and 6 caught 20.
  redflag_coverage 42%. The gap was COVERAGE, not accuracy: six of six
  promise-delivery spot-checks confirmed, no pipeline flag unsupported, and
  verifier B concurred credibility D was correct. Stages 5 and 6 verified peer
  PRICES and DATES well and peer OPERATING NORMS badly. Three of verifier B's
  seven CRITICALs were peer-testable operating norms nobody tested: usable
  capacity as a share of nameplate (INA's own CFO said 50-55% against peers at
  70-92%), cell ramp duration, and capex per GW. Candidate fix: a named
  operating-norms sub-checklist in prompts/06.
- A B05 hand-off to stage 6 was written and never executed. B05 flagged the
  Emvee and Premier DCR cell tie-up as worth checking against Premier's own
  concall; stage 6 did not check it, and Premier states it will have few cells
  to sell. Candidate fix: peer_questions[] becomes a checklist stage 6 must tick
  item by item, with an explicit not-checked status where it cannot.
- Citation-basis defect, systemic, caught independently by verifiers B and D:
  stages 5 and 6 cited each transcript's printed "Page X of Y" footer instead of
  the extraction "===== PAGE N =====" marker. An unnumbered SEBI cover letter
  offsets the two by exactly one page on EVERY transcript, so anchors drift by
  one, and two load-bearing Premier citations drifted 3 to 4 pages. Candidate
  fix: name the extraction marker as the sole anchor authority in every stage
  task message and bar the printed footer explicitly.
- B05 promise-tracker completeness: three missed promises absent from the
  tracker (FY26 volume 2,000-2,100MW, FY26 EPC revenue Rs 400cr, Units 1-2
  TOPCon conversion). Adding them moves the tally from 5 missed to 8. Accuracy
  was fine; the sweep was incomplete.
- COST, the largest avoidable item this run: stage 3 consumed 23.8% of all
  tokens because it ran three times. Run 1 was the analysis. Runs 2 and 3 were
  pure schema repair, appending the YAML block to the report file and then
  adding a missing monitorables[] field. Those two repair runs cost 658,377
  tokens, 17.5% of the run, and produced no analysis. Each resume re-read the
  stage's whole context. Candidate fix: state in every stage task message that
  the report file itself must end with the fenced YAML block and that returning
  it only in the reply does not count, and list the block's required fields by
  name so the stage self-checks before returning.
- DOWNSHIFT FAILURE: stage 0. DISPATCH lists stage 0 as a Haiku mechanical
  stage, but run-pipeline.md step 1 says "do this yourself", which puts it in
  the orchestrator session at the session model (Opus 5 this run). A designed
  conflict, not a routing accident. Candidate fix: route stage 0 to a haiku
  subagent, or drop stage 0 from the DISPATCH haiku list.
- Corpus finding worth remembering as a pattern: the FY2026 annual report OMITS
  the text of Notes 1-3, the Material Accounting Policies, while both balance
  sheets and the audit report cross-reference them. Verified with two
  independent extractors and a per-page scan for image-only pages. A stage
  flagged it, and stage 0 confirmed it before letting it stand rather than
  treating it as an extraction artifact. Worth doing every time a stage claims a
  section is missing.
- PDF tooling followed the known LESSONS.md pattern exactly: pypdf absent, then
  the _cffi_backend break, then poppler-utils failing on the first apt attempt
  and succeeding after apt-get update. Pre-extracting all 17 PDFs to page-marked
  text up front worked and no stage hit a render wall.
- Collector defects recurred as catalogued: sector_cap_row set to "EV charging /
  energy transition equipment" for a solar module maker, and header-only
  Profit_Loss, Balance_Sheet, Cash_Flow and Quarters CSVs for the subject and
  all three peers with only Data_Sheet populated.

---

## FOR LESSONS.md OPEN ACTIONS (one line, per the close-out rule)

- DOWNSHIFT FAILURE, stage 0 (INA 2026-09-06): DISPATCH routes stage 0 to haiku
  while run-pipeline.md step 1 runs it inline in the orchestrator session at the
  session model. Reconcile the two.
