# DSP shared project status

**Course:** HMMY458 / ΤΗΛ301 — Ψηφιακή Επεξεργασία Σήματος, 2026–2027
**Last updated:** 16 October 2026 (Europe/Athens)
**Current focus:** Lab 1 — due **29 October 2026, 23:30**
**Main requirements reference:** [DSP Master Guide](docs/DSP_Master_Guide.md)

## How we maintain this report

Everyone should read this file before starting work. After each coherent set of repository changes, update the affected rows, next actions, decisions, validation results and change log, and include this file in the same commit as the work. Reconcile teammates' updates before pushing. Read-only reviews need an update only when they reveal new status, requirements or blockers.

Use **Not started**, **In progress**, **Ready for review**, **Done**, or **Blocked**. Name owners only when agreed. Mark work Done only when the files exist and the relevant checks pass; link those files or record the verification evidence. Repository completion and eClass submission are separate milestones. This is a shared manual/agent workflow, not an automatic watcher of every push.

## Current snapshot

- Initial inspection of `main` at `d2346ae` found only [README.txt](README.txt). No exercise code, figures, report or submission ZIP was committed at that point. Teammates' uncommitted/offline work is unknown.
- This setup adds the shared status report, a maintained requirements guide, and agent update instructions.
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

Suggested paths are proposals, not files claimed to exist. Owners are unassigned until the team agrees.

| Work item | Status | Owner | Required outcome / next step |
|---|---|---|---|
| Shared documentation | Done | — | This file, master guide and AGENTS.md added; existing README preserved |
| Team coordination and setup | Not started | Unassigned | Confirm owners and Group 69 naming; agree folder layout, Python dependencies and run instructions |
| Exercise 1: convolution and FFT | Not started | Unassigned | Generate both specified sequences; formula-based convolution; NumPy/SciPy comparison; spectra and convolution theorem |
| Exercise 2: sampling and reconstruction | Not started | Unassigned | Original signal and spectrum; 20/10/5 Hz sampling; reconstruction reasoning; 0.5 s versus 5 s comparison |
| Exercise 3A: alias-free sampling | Not started | Unassigned | 128 samples of specified 20/60 Hz signal; justified sampling rate; Hz spectrum; phase assumption |
| Exercise 3B: aliases at 20 kHz sampling | Not started | Unassigned | Discrete-time formula, all eight frequencies, labelled spectra, sign/phase-aware alias explanation |
| Report and figures | Not started | Unassigned | Theory, formulas, method, results and conclusions for every subquestion; titles and labelled axes |
| Reproducibility and review | Not started | Unassigned | Clean run from documented dependencies; check numerical results, figures and report against brief |
| ZIP and eClass submission | Not started | Unassigned | One ZIP with separate commented code, report and execution instructions; verify upload and retain confirmation |

## Rough work order

1. Agree ownership and a simple structure such as `lab1/exercise1.py`, `exercise2.py`, `exercise3.py`, `figures/`, report source and run instructions. Check for teammate work before starting duplicate implementations.
2. Implement the three exercises, recording parameter assumptions alongside the code. Generate figures reproducibly.
3. Write each report section while its exercise is being checked. Explain theory and observations, not only output.
4. Review every subquestion, numerical check, plot and dependency. Ask unresolved course questions at the 22 October tutorial when useful.
5. Build the ZIP, run its code from a fresh extraction, and verify the group upload before 29 October at 23:30. Select a submission owner explicitly.

## Validation targets

- **Exercise 1:** lengths 9 and 8; full convolution length 16, indices −6 through 9; formula result agrees with library result; padded FFT product agrees with linear convolution within a stated tolerance. State the sample interval used for the Hz axis.
- **Exercise 2:** components at 5 and 2.5 Hz; Nyquist rate 10 samples/s; correct sample times at 20, 10 and 5 Hz; explain the boundary case and finite-record/reconstruction effects. A longer record does not fix aliasing.
- **Exercise 3A:** exactly 128 samples; choose a rate above 120 Hz to avoid the boundary case; record whether `+30` is interpreted as radians or otherwise clarified.
- **Exercise 3B:** 18,000/18,500/19,000/19,500 Hz alias to magnitude-spectrum frequencies 2,000/1,500/1,000/500 Hz at 20 kHz sampling. Account for sine sign/phase. Declare phase and sample-count choices.
- **Delivery:** every required graph is labelled; source code is separate from the report; execution instructions work; ZIP contains all required files; eClass confirmation is recorded separately.

**Checks performed so far:** documentation reviewed against the maintained guide and initial repository contents. No executable project or numerical checks exist yet.

## Open decisions and blockers

| Topic | Next action | Impact |
|---|---|---|
| Task owners / submission owner | Team assigns responsibilities | Prevent duplicate work and missed upload |
| Group 41 versus current eClass Group 69 | Confirm team naming and any old repository description | Use the correct group identification in deliverables |
| Exercise 1 sample interval and spectra interpretation | State assumption / seek clarification; show both inputs together | Correct Hz axes and report explanation |
| Exercise 2 reconstruction method | Choose and document a justified method | Distinguish reconstruction from connecting samples |
| Exercise 3 phase and 3B record length | Record chosen interpretation and parameters | Reproducible results; avoid silently assuming degrees |
| Labs 2–4 schedule | Verify README dates against official assignments/announcements | Dates remain provisional |

## Change log

Add newest entries first. Each entry should identify what changed, checks performed, remaining issues and the next step. Include a commit or PR link when available; do not try to embed a commit's own hash in that same commit.

### 16 October 2026 — Shared status setup

- Inspected the initial repository at `d2346ae`: README only, no implementation artifacts.
- Added this work board, the maintained DSP master guide and instructions to read/update status for future repository work.
- Carried over verified Lab 1 dates and current Group 69 evidence; labelled Labs 2–4 dates from the README as provisional.
- Validation: documentation and links checked; no application code changed or tests run.
- Next: agree owners, reconcile group naming, and begin Lab 1 implementation.
