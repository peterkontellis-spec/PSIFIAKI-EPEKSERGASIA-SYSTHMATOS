# DSP shared project status

**Course:** HMMY458 / ΤΗΛ301 — Ψηφιακή Επεξεργασία Σήματος, 2026–2027
**Last updated:** 23 October 2026 (Europe/Athens)
**Current focus:** Lab 1 — due **29 October 2026, 23:30**
**Main requirements reference:** [DSP Master Guide](docs/DSP_Master_Guide.md)

## How we maintain this report

Everyone should read this file before starting work. After each coherent set of repository changes, update the affected rows, next actions, decisions, validation results and change log, and include this file in the same commit as the work. Reconcile teammates' updates before pushing. Read-only reviews need an update only when they reveal new status, requirements or blockers.

Use **Not started**, **In progress**, **Ready for review**, **Done**, or **Blocked**. Name owners only when agreed. Mark work Done only when the files exist and the relevant checks pass; link those files or record the verification evidence. Repository completion and eClass submission are separate milestones. This is a shared manual/agent workflow, not an automatic watcher of every push.

## Current snapshot

- Initial inspection of `main` at `d2346ae` found only [README.txt](README.txt). No exercise code, figures, report or submission ZIP was committed at that point. Teammates' uncommitted/offline work is unknown.
- **22 October:** added simple Lab 1 scripts, 15 passing numerical checks, seven reproducible figures and a working report. See [verification](lab1/VERIFICATION.md) and [run instructions](lab1/README.md).
- **23 October:** fixed stale generated figures and completed the required 3A magnitude plot. All 18 tests pass; all eight default figures reproduce byte-for-byte. The radians convention is explicit, and phase-unit independence of this magnitude result is verified.
- **Re-review of `1c7c2df`:** independent checks confirm both fixes. Scores are 9 / 9 / 9 / 9 / 7.5 across the five fronts below. At that review, final 1B instructions, report theory completion and the verified ZIP remained outstanding; the theory completion is recorded below.
- **Report theory completed, 23 October:** added the assignment’s DFT/inverse and ideal reconstruction formulas, with the preparation notes’ FFT frequency mapping. All 18 existing tests passed again; direct checks of the written transform formulas and bin mapping passed at `1e-10`. A local report preview contains all eight figures.
- **Report presentation reviewed, 23 October:** reorganized the report with a results table, typeset equations, numbered figure captions and sources. Added [HTML](lab1/report.html) and [PDF](lab1/report.pdf) reading copies. Independent report-only estimate improved from **8.3/10 to 8.8/10**; this is not an official-grade prediction.
- **Greek report added, 23 October:** [PDF](lab1/report_el.pdf), [HTML](lab1/report_el.html) and [Markdown](lab1/report_el.md), with shorter explanations and eight figures labelled in Greek. All ten display equations match the English source exactly; all plotted arrays and axis ranges match the original scripts exactly. The English version and solution code are unchanged. This translation has not received a new expert score.
- Owners and group naming remain open by user instruction. Exercise 1B’s final Hz plot still awaits its physical sampling rate; the unspecified 3A phase unit does not block its completed magnitude plot.
- eClass showed **Group 69, 3/3 members**, for the signed-in account on 16 October. Earlier chat/repository references to Group 41 need team reconciliation before naming final deliverables; no group membership was changed.
- No submission was shown for the signed-in account during the 16 October eClass check. A teammate's separate submission has not been independently checked.

## Dates

All times are Europe/Athens. Verified course requirements take priority over planning estimates.

| Milestone | Date/time | Confidence / source |
|---|---|---|
| Group registration | 18 October 2026, 23:30 | Official; already shown complete for the checked account, Group 69 |
| Lab 1 tutorial and questions | 22 October 2026, 11:00–12:00 | Official announcement, linked in master guide |
| **Lab 1 submission** | **29 October 2026, 23:30** | Official assignment and announcement |
| Lab 2 release → submission | 30 October → 13 November 2026 | Existing README only; confirm with eClass; cutoff time unknown |
| Lab 3 release → submission | 13 November → 27 November 2026 | Existing README only; confirm with eClass; cutoff time unknown |
| Lab 4 release → submission | 3 December → 20 December 2026 | Existing README only; confirm with eClass; cutoff time unknown |
| Mandatory written lab exam | Course exam day; January initially, September also provided for | 30 minutes, multiple choice, ≥5 required for lab credit; exact date/time unknown |

## Lab 1 work board

The linked files now exist. Owners remain unassigned until the team agrees. Ready for review means the listed checks passed, not that the entire lab is ready to submit.

| Work item | Status | Owner | Required outcome / next step |
|---|---|---|---|
| Shared documentation | Done | — | This file, master guide and AGENTS.md added; existing README preserved |
| Team coordination and setup | In progress | Unassigned | [Run instructions](lab1/README.md) and pinned dependencies added; ownership and group naming remain open |
| Exercise 1: convolution and FFT | In progress | Unassigned | [Code](lab1/exercise1.py): 1A/1C verified; 1B calculation tested but final Hz plot awaits sampling-rate clarification |
| Exercise 2: sampling and reconstruction | Ready for review | Unassigned | [Code](lab1/exercise2.py), three figures and [report explanation](lab1/report.md); no extra numerical reconstruction method added |
| Exercise 3A: alias-free sampling | Ready for review | Unassigned | [Code](lab1/exercise3.py), [magnitude plot](lab1/figures/ex3a_spectrum.png) and report complete; 128 samples at 256 Hz; explicit radians convention and phase independence verified |
| Exercise 3B: aliases at 20 kHz sampling | Ready for review | Unassigned | [Code](lab1/exercise3.py), eight spectra in two figures, alias/sign explanation; explicit permitted choices N=400 and phase=0 |
| Report and figures | In progress | Unassigned | Greek [source](lab1/report_el.md), [PDF](lab1/report_el.pdf) and [HTML](lab1/report_el.html), plus the retained [English version](lab1/report.md); theory complete and eight captioned figures in each language. Final 1B figure and agreed group/author details remain open |
| Reproducibility and review | Ready for review | Unassigned | [18 numerical and rerun tests](lab1/verify.py) pass; clean-folder execution reproduces all eight default figures; [evidence and limits](lab1/VERIFICATION.md) |
| ZIP and eClass submission | Not started | Unassigned | One ZIP with separate commented code, report and execution instructions; verify upload and retain confirmation |

## Rough work order

1. Review the verified scripts and working report; owners and group naming stay open.
2. Clarify the physical sampling rate for 1B; generate and review its final plot.
3. Complete the report with the 1B result and agreed group/author details; the theory additions are complete. Put the agreed `--fs` value in the main run instructions.
4. Repeat only affected checks after any changes, then perform a final review against every subquestion.
5. Build the ZIP, run its code from a fresh extraction, and verify the group upload before 29 October at 23:30. Select a submission owner explicitly.

## Validation targets

- **Exercise 1:** lengths 9 and 8; full convolution length 16, indices −6 through 9; formula result agrees with library result; padded FFT product agrees with linear convolution within a stated tolerance. State the sample interval used for the Hz axis.
- **Exercise 2:** components at 5 and 2.5 Hz; Nyquist rate 10 samples/s; correct sample times at 20, 10 and 5 Hz; explain the boundary case and finite-record/reconstruction effects. A longer record does not fix aliasing.
- **Exercise 3A:** exactly 128 samples; choose a rate above 120 Hz to avoid the boundary case; record the explicit radians convention for `+30`; at the chosen exact FFT bins, verify that radians/degrees give the same magnitudes within `1e-12`.
- **Exercise 3B:** 18,000/18,500/19,000/19,500 Hz alias to magnitude-spectrum frequencies 2,000/1,500/1,000/500 Hz at 20 kHz sampling. Account for sine sign/phase. Declare phase and sample-count choices.
- **Delivery:** every required graph is labelled; source code is separate from the report; execution instructions work; ZIP contains all required files; eClass confirmation is recorded separately.

**Checks performed so far:** 18 automated tests passed, including both stale-output rerun regressions. All scripts ran in a clean copy; eight default figures reproduced byte-for-byte in the checked environment. The seven existing figures were visually reviewed on 22 October and are unchanged; the new 3A figure was visually reviewed on 23 October. The largest all-bin radians/degrees magnitude difference was `3.7623497442574107e-14` (absolute tolerance `1e-12`). See [VERIFICATION.md](lab1/VERIFICATION.md) for sources, tolerances and remaining limits.

## Open decisions and blockers

| Topic | Next action | Impact |
|---|---|---|
| Task owners / submission owner | Team assigns responsibilities | Prevent duplicate work and missed upload |
| Group 41 versus current eClass Group 69 | Confirm team naming and any old repository description | Use the correct group identification in deliverables |
| Exercise 1 sample interval and spectra interpretation | State assumption / seek clarification; show both inputs together | Correct Hz axes and report explanation |
| Exercise 2 reconstruction discussion | Uses the required original/samples plots and written theory, following preparation pp. 19–21 | No extra numerical reconstruction algorithm introduced |
| Exercise 3 phase and 3B record length | 3A uses an explicit radians convention; the printed unit remains unconfirmed, but the requested magnitude is invariant at the chosen bins. 3B uses documented phase 0 and 400 samples | 3A magnitude complete; no claim of staff clarification |
| Labs 2–4 schedule | Verify README dates against official assignments/announcements | Dates remain provisional |

## Report organization and presentation review — 23 October 2026

The same expert reviewed the English report at `37a598e` and the revised English reading copies. The scores below assess that report, not the whole Python project or the subsequent Greek translation, and do not predict the instructor’s grade.

| Report area | Before → after / 10 |
|---|---|
| Mathematical correctness | 9 → 9 |
| Specification coverage | 8 → 8 |
| Explanation and reasoning | 9 → 9 |
| Organization | 8 → 9 |
| Presentation | 7.5 → 9 |
| **Overall report estimate** | **8.3 → 8.8** |

The review confirmed preserved DFT/inverse scaling and signs, convolution proof, reconstruction relationships and 3A phase reasoning. The full given 3A expression is now shown. A results table, clear exercise/subpart headings, eight interpretive captions and a source list organize the same work. Ten equations are typeset in both reading copies. Coverage remains 8 because 1B is unfinished; no missing work is concealed by the layout.

**Checks:** compared content with the earlier report; verified eight original figure hashes, eight captions, ten equations, seven HTML contents links and all embedded assets. The HTML is self-contained; the PDF has 11 pages. PDF pages were rendered and visually checked; the expert independently checked representative pages. No clipped equations, overlapping text or unresolved rendering placeholders were found. The HTML design scan returned no findings; its browser layout was not visually rechecked because local-file browser automation is blocked. No solution scripts or numerical figure data changed, so numerical tests were not rerun for this presentation-only change; the last 18-test run remains the report-theory update above.

**Remaining:** 1B’s physical rate, figure and explanation; final run instructions using that rate; agreed author/group details; and a verified ZIP. eClass submissions were not accessed or changed. The PDF and HTML are reading copies, not a completed submission package.

## Python expert re-review — 23 October 2026

Reviewed commit `1c7c2df6e5c7e55492aa53e801f7f663824813f9` against the supplied assignment and preparation notes. **The stale-output defect is resolved and 3A is complete; the project is not yet ready to submit.** No numerical defect was found. This review changed no solution code.

| Review front | Previous → current / 10 | Assessment |
|---|---|---|
| Assignment and preparation compliance | 8 → 9 | 3A is complete with an explicit, justified convention; required 1B plot remains missing |
| DSP and mathematical correctness | 9 → 9 | Tested calculations and the record-specific phase-independence argument are correct |
| Python clarity and simplicity | 9 → 9 | Small, readable changes; no additional solution methods |
| Testing and reproducibility | 8 → 9 | Both output regressions pass and eight figures reproduce exactly |
| Report completeness and submission readiness | 6.5 → 7.5 | 1B, final instructions, report finishing and ZIP verification remain |

**Independent evidence:** all 18 tests passed in a clean copy; all three default scripts ran and all eight PNGs matched committed files byte-for-byte. An explicit `--fs 20` run followed by the default removed only the previous 1B figure and preserved an unrelated file. Degrees followed by default Exercise 3 restored the committed radians-labelled figure. The new 3A plot was visually checked. Its all-bin radians/degrees difference was `3.7623497442574107e-14`, below `1e-12`; peaks are 6 at ±20 Hz and 9 at ±60 Hz. No fresh dependency installation, other-OS run or live eClass recheck was performed.

### Findings and submission checklist at the reviewed commit

1. **Resolve 1B’s physical sampling rate** under the user’s constraints. [Report](lab1/report.md), line 19 of the reviewed commit, records the missing required Hz plot. Generate and visually inspect it, insert it, and explain the chosen scale and observations.
2. **Finalize the run instructions with the agreed value.** [README](lab1/README.md), line 15, currently runs Exercise 1 without `--fs`, deliberately removing its spectrum. The final main command must be `python lab1/exercise1.py --fs <agreed-value>` with an actual value. Replace the abbreviated command at line 31 with the full path consistent with the repository-root working directory.
3. **Finish the report’s theory and presentation.** Add a compact DFT/inverse pair, frequency-bin mapping and ideal low-pass reconstruction relationship with its conditions, using only formulas already in the assignment. This is the reviewer’s interpretation of the general requirement to explain the theoretical relationships used, not an official verbatim equation checklist or a request for another numerical algorithm. Replace working/pending wording after completing 1B.
4. **Have the team settle author/group identification and the submission owner.** These remain open; no naming or ownership has been inferred. This is a coordination task, not a prescribed filename convention.
5. **Assemble the required single ZIP:** separate commented Python code, completed report with accessible figures, and short execution instructions. Include the dependencies needed to follow those instructions.
6. **Verify the actual package:** extract into a fresh folder, follow the final documented commands, run the checks, and confirm all nine expected figures and report references. Current clean-copy testing does not replace this final ZIP check.
7. **Submit through eClass and retain confirmation.** Repository completion is separate from upload. The recorded deadline remains 29 October 2026 at 23:30 Europe/Athens, last live-checked on 16 October; this review did not recheck announcements.

**Follow-up — 23 October:** item 3’s theory additions are now complete in [report.md](lab1/report.md): assignment p. 1, equations 1-2; assignment p. 2 reconstruction model; preparation pp. 18/22 FFT spacing and axis conventions. Working/pending wording remains accurate because 1B and team identification are deliberately open. No extra reconstruction algorithm was implemented. No eClass submission pages were accessed or changed.

**Not blockers:** further 3A phase clarification, an additional reconstruction algorithm, a mandatory PDF extension, extra workspace tooling, or broader refactoring. PDF is an optional report format; the specification requires a detailed report, not that particular extension.

## Independent Python expert review — 23 October 2026

Reviewed implementation commit `1d70f6072584f822a2fde22f880aec8aea09a19a` against the supplied assignment, preparation notes, code, report and tests. **Not ready to submit.** This was an independent review; no solution code was changed.

| Review front | Score / 10 | Assessment |
|---|---|---|
| Assignment and preparation compliance | 8 | Specified methods used; final 1B and 3A figures remain missing |
| DSP and mathematical correctness | 9 | No numerical defect found in tested calculations |
| Python clarity and simplicity | 9 | Straightforward, readable scripts and explicit parameters |
| Testing and reproducibility | 8 | All 15 tests and seven exact figure reproductions passed; stale-output behavior reproduced |
| Report completeness and submission readiness | 6.5 | Substantial working report; two figures and final verified ZIP remain unfinished |

### Findings at the reviewed commit

1. **Missing required figures:** 1B needs an explicit physical frequency scale. The 3A phase choice changes sample values but does not change the requested magnitude spectrum at the chosen bin-aligned frequencies; withholding that figure is a conservative process choice, not a mathematical necessity. The final interpretation remains open under the current user instruction.
2. **P2 — earlier outputs survive a pending run:** generate `ex1_spectra.png` using `exercise1.py --fs 1` and `ex3a_spectrum.png` using `exercise3.py --phase-unit degrees`, then rerun both scripts without options. Both files remain unchanged while the scripts report their sections as pending. Relevant branches: [exercise1.py](lab1/exercise1.py), line 79, and [exercise3.py](lab1/exercise3.py), line 43 in the reviewed commit. Explicitly handle or flag existing parameter-dependent outputs and verify this run sequence before packaging. The seven currently committed default figures are unaffected.
3. **Submission package unfinished:** complete the report, include all figures, assemble the required ZIP and run from a fresh extraction. PDF is a practical report option, not an explicit mandated extension. Owners and group naming remain open.

**Evidence:** independent clean-copy run passed all 15 tests and regenerated all seven committed default PNGs byte-for-byte; selected figures visually checked. No fresh dependency installation or other-OS validation was performed. Test results do not establish absolute certainty.

**Resolution — 23 October 2026:** the stale-output issue is fixed and covered by rerun tests. A default Exercise 1 run removes only its old `ex1_spectra.png`; Exercise 3 always regenerates its 3A plot with the current phase convention. The 3A magnitude figure and explanation are complete after verifying phase independence. The scores above remain a historical assessment of `1d70f60`, not a new review.

**Next:** settle 1B’s physical sampling rate, generate its plot, finish the report and verify the extracted ZIP.

## Change log

Add newest entries first. Each entry should identify what changed, checks performed, remaining issues and the next step. Include a commit or PR link when available; do not try to embed a commit's own hash in that same commit.

### 23 October 2026 — Simple Greek report

- Added a Greek Markdown report and standalone HTML/PDF reading copies. Shortened explanations and translated titles, axes, legends and captions for eight figure copies; retained the English artifacts.
- Compared all ten display equations with the English source: exact matches. Ran temporary copies of the unchanged exercise scripts and verified that every plotted array and axis range is identical before and after relabelling. No final 1B figure was generated.
- Verified eight embedded figure hashes, eight captions, ten equations, seven HTML contents links, Greek character support and all 11 rendered PDF pages. Original code and English artifacts are unchanged. The previous 18-test result remains from the theory update; that suite was not rerun for this translation.
- Updated report links and maintenance notes. 1B's physical sampling rate and final plot, group/author details and the verified ZIP remain open. No eClass access, submission or new expert grading. Next: resolve those open decisions, then update both report versions and verify the final package.

### 23 October 2026 — Report organization, typography and review

- Added the report results table, clearer section/subpart headings, ten typeset equations, eight numbered figure captions and sources. Included PDF and standalone HTML reading copies; retained the Markdown source.
- Expert report-only score improved from 8.3/10 to 8.8/10; math and coverage scores are unchanged. No new numerical method or result was introduced.
- Verified content preservation, original figure hashes, embedded assets, captions, navigation and PDF rendering. Documentation links and Git whitespace checked before commit; no numerical-code changes or new numerical test run.
- 1B and team details remain open. No eClass actions. Next: complete those decisions before final report/package verification.

### 23 October 2026 — Report theory and preview

- Added the DFT/inverse pair, normalization and centred frequency-bin explanation, plus the impulse train, specified low-pass filter and resulting ideal reconstruction sum. All come from the supplied assignment/preparation notes; no solution code or methods changed.
- Kept 1B’s physical sampling rate, its final plot, group details and owners open. eClass submissions were not accessed or changed.
- Re-ran all 18 existing tests successfully. Independently checked the written DFT/inverse sums and even/odd centred-bin mapping against NumPy within `1e-10`; reviewed the reconstruction expressions against the rendered specification pages.
- Created a local reading preview from the report with all eight figures embedded. Checked Markdown links, figure references and Git whitespace before commit. The preview is not a submission package.
- Next: settle 1B, finish its plot/explanation and final run command, then complete team details and verify the required ZIP. Upload is outside this change’s scope.

### 23 October 2026 — Independent re-review of the fixes

- Python expert re-reviewed `1c7c2df`; scores changed from 8/9/9/8/6.5 to 9/9/9/9/7.5.
- Independently passed 18 tests, reproduced eight PNGs exactly, and verified both explicit-parameter/default reruns. No numerical defect found; 3A and stale-output findings are resolved.
- Recorded the remaining 1B plot, final explicit-rate instructions, compact report theory additions, team identification and extracted-ZIP verification/upload checklist.
- Documentation-only update; no solution-code changes. Local Markdown links and whitespace checked before commit. No live eClass recheck.

### 23 October 2026 — Stale-figure fix and completed 3A magnitude

- Removed the stale 1B figure when the physical frequency scale is omitted; always regenerate 3A with the current explicit phase convention.
- Added the required 3A magnitude plot and its FFT-bin explanation without adding solution methods. Both phase interpretations give magnitudes within `1e-12`; samples differ.
- All 18 tests passed, including explicit-parameter/default reruns and unrelated-file preservation. A clean copy reproduced all eight default PNGs byte-for-byte; the new plot was visually reviewed.
- Updated report, run instructions, verification evidence and master guide. 1B, group/author details and the final ZIP remain open.
- Next: obtain 1B’s physical sampling rate and complete the remaining report/package.

### 23 October 2026 — Independent Python expert review

- Reviewed implementation commit `1d70f60` on five fronts; recorded the scorecard above.
- Independent checks passed: 15 tests and seven byte-for-byte figure reproductions.
- Recorded a reproduced stale-output issue, the two missing final figures and the unfinished submission package. No solution-code fixes made in this review.
- Next: address the findings before submission; owners and group naming remain open.

### 22 October 2026 — First verified implementation

- Read the assignment and supplied preparation PDF; stayed with their direct sums, FFTs and simple plots.
- Added three scripts, separate verification checks, seven figures, run instructions (including VS Code), and a working report.
- All 15 tests passed; a clean-folder run reproduced seven figures exactly; plots visually reviewed. [Detailed evidence](lab1/VERIFICATION.md).
- Final 1B/3A output choices, owners and group naming remain open. No final ZIP or upload performed.
- Next: obtain the two parameter clarifications and complete the remaining report figures.

### 16 October 2026 — Shared status setup

- Inspected the initial repository at `d2346ae`: README only, no implementation artifacts.
- Added this work board, the maintained DSP master guide and instructions to read/update status for future repository work.
- Carried over verified Lab 1 dates and current Group 69 evidence; labelled Labs 2–4 dates from the README as provisional.
- Validation: documentation and links checked; no application code changed or tests run.
- Next: agree owners, reconcile group naming, and begin Lab 1 implementation.
