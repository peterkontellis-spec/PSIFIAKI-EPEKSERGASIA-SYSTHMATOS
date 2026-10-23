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
- Owners and group naming remain open by user instruction. Exercise 1B’s physical sampling rate and Exercise 3A’s phase unit are not silently assumed; final outputs for those parts remain pending.
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
| Exercise 3A: alias-free sampling | In progress | Unassigned | [Code](lab1/exercise3.py) tested for both phase units; 128 samples at 256 Hz; final phase choice and figure pending |
| Exercise 3B: aliases at 20 kHz sampling | Ready for review | Unassigned | [Code](lab1/exercise3.py), eight spectra in two figures, alias/sign explanation; explicit permitted choices N=400 and phase=0 |
| Report and figures | In progress | Unassigned | [Working report](lab1/report.md), seven reviewed figures; final 1B/3A figures and agreed group/author details remain open |
| Reproducibility and review | Ready for review | Unassigned | [15 numerical tests](lab1/verify.py) pass; clean-folder execution reproduces all seven default figures; [evidence and limits](lab1/VERIFICATION.md) |
| ZIP and eClass submission | Not started | Unassigned | One ZIP with separate commented code, report and execution instructions; verify upload and retain confirmation |

## Rough work order

1. Review the verified scripts and working report; owners and group naming stay open.
2. Clarify the physical sampling rate for 1B and the phase unit for 3A; generate and review those two final plots.
3. Complete the report with those results and agreed group/author details.
4. Repeat only affected checks after any changes, then perform a final review against every subquestion.
5. Build the ZIP, run its code from a fresh extraction, and verify the group upload before 29 October at 23:30. Select a submission owner explicitly.

## Validation targets

- **Exercise 1:** lengths 9 and 8; full convolution length 16, indices −6 through 9; formula result agrees with library result; padded FFT product agrees with linear convolution within a stated tolerance. State the sample interval used for the Hz axis.
- **Exercise 2:** components at 5 and 2.5 Hz; Nyquist rate 10 samples/s; correct sample times at 20, 10 and 5 Hz; explain the boundary case and finite-record/reconstruction effects. A longer record does not fix aliasing.
- **Exercise 3A:** exactly 128 samples; choose a rate above 120 Hz to avoid the boundary case; record whether `+30` is interpreted as radians or otherwise clarified.
- **Exercise 3B:** 18,000/18,500/19,000/19,500 Hz alias to magnitude-spectrum frequencies 2,000/1,500/1,000/500 Hz at 20 kHz sampling. Account for sine sign/phase. Declare phase and sample-count choices.
- **Delivery:** every required graph is labelled; source code is separate from the report; execution instructions work; ZIP contains all required files; eClass confirmation is recorded separately.

**Checks performed so far:** 15 automated tests passed, all scripts ran in a clean copy, seven default figures reproduced byte-for-byte in the checked environment, and figures were visually reviewed. See [VERIFICATION.md](lab1/VERIFICATION.md) for sources, tolerances and remaining limits.

## Open decisions and blockers

| Topic | Next action | Impact |
|---|---|---|
| Task owners / submission owner | Team assigns responsibilities | Prevent duplicate work and missed upload |
| Group 41 versus current eClass Group 69 | Confirm team naming and any old repository description | Use the correct group identification in deliverables |
| Exercise 1 sample interval and spectra interpretation | State assumption / seek clarification; show both inputs together | Correct Hz axes and report explanation |
| Exercise 2 reconstruction discussion | Uses the required original/samples plots and written theory, following preparation pp. 19–21 | No extra numerical reconstruction algorithm introduced |
| Exercise 3 phase and 3B record length | 3A unit still open; 3B uses documented phase 0 and 400 samples because neither is prescribed there | Do not silently assume degrees in 3A |
| Labs 2–4 schedule | Verify README dates against official assignments/announcements | Dates remain provisional |

## Independent Python expert review — 23 October 2026

Reviewed implementation commit `1d70f6072584f822a2fde22f880aec8aea09a19a` against the supplied assignment, preparation notes, code, report and tests. **Not ready to submit.** This was an independent review; no solution code was changed.

| Review front | Score / 10 | Assessment |
|---|---|---|
| Assignment and preparation compliance | 8 | Specified methods used; final 1B and 3A figures remain missing |
| DSP and mathematical correctness | 9 | No numerical defect found in tested calculations |
| Python clarity and simplicity | 9 | Straightforward, readable scripts and explicit parameters |
| Testing and reproducibility | 8 | All 15 tests and seven exact figure reproductions passed; stale-output behavior reproduced |
| Report completeness and submission readiness | 6.5 | Substantial working report; two figures and final verified ZIP remain unfinished |

### Findings

1. **Missing required figures:** 1B needs an explicit physical frequency scale. The 3A phase choice changes sample values but does not change the requested magnitude spectrum at the chosen bin-aligned frequencies; withholding that figure is a conservative process choice, not a mathematical necessity. The final interpretation remains open under the current user instruction.
2. **P2 — earlier outputs survive a pending run:** generate `ex1_spectra.png` using `exercise1.py --fs 1` and `ex3a_spectrum.png` using `exercise3.py --phase-unit degrees`, then rerun both scripts without options. Both files remain unchanged while the scripts report their sections as pending. Relevant branches: [exercise1.py](lab1/exercise1.py), line 79, and [exercise3.py](lab1/exercise3.py), line 43 in the reviewed commit. Explicitly handle or flag existing parameter-dependent outputs and verify this run sequence before packaging. The seven currently committed default figures are unaffected.
3. **Submission package unfinished:** complete the report, include all figures, assemble the required ZIP and run from a fresh extraction. PDF is a practical report option, not an explicit mandated extension. Owners and group naming remain open.

**Evidence:** independent clean-copy run passed all 15 tests and regenerated all seven committed default PNGs byte-for-byte; selected figures visually checked. No fresh dependency installation or other-OS validation was performed. Test results do not establish absolute certainty.

**Next:** settle the final parameter interpretations, address stale outputs, generate the remaining figures, finish the report and verify the extracted ZIP.

## Change log

Add newest entries first. Each entry should identify what changed, checks performed, remaining issues and the next step. Include a commit or PR link when available; do not try to embed a commit's own hash in that same commit.

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
