# DSP repository collaboration

This repository is for DSP (HMMY458 / ΤΗΛ301) only. Keep ΨΥΣ work separate.

## User constraints updated 27 October 2026

- Do not invent owners, names, student IDs or a group number. The user requested blank identification fields at the start of the report; keep them blank until actual values are supplied. Use the neutral delivery filename `DSP_Lab1.zip`.
- Follow the assignment and supplied preparation notes strictly. Keep the solution simple, precise and easy to explain. Do not introduce optional methods or features outside the requested questions.
- Test and verify work before pushing. State the actual checks and numerical tolerances; do not claim absolute certainty from tests.
- On 27 October the user authorized finishing unspecified implementation choices to the best of our ability. State choices explicitly rather than presenting them as assigned values. Exercise 1B now uses `fs = 1 Hz` (`Ts = 1 s`); retain the user's requested note that the specification does not determine the physical sampling frequency. This supersedes the earlier instruction to keep its plot pending. The 3A radians convention and its verified magnitude invariance remain explicit.
- Do not access or change eClass submissions. The user expressly excluded submission actions.


## Before working

1. Read `STATUS.md` and `docs/DSP_Master_Guide.md` before making changes. The user designated the master guide as the main requirements reference unless directed otherwise.
2. Inspect current repository files and Git status; preserve coworkers' changes. Confirm which work already exists before implementing it again.
3. Use official course evidence for requirement/deadline updates, with source and verification date. Treat dates from the existing README as provisional where the guide says they are unverified.

## After changes

1. After every coherent batch of repository changes, update `STATUS.md` before finishing and include the status update in the same commit or PR as the work.
2. Record changed work items, actual completion, relevant file links, checks and results, unresolved issues and concrete next actions. Add a dated change-log entry using Europe/Athens dates.
3. Update `docs/DSP_Master_Guide.md` when verified requirements/deadlines change or its work-status summary becomes stale. Keep it consistent with `STATUS.md`; do not invent official constraints from implementation choices.
4. Run checks appropriate to the change. Documentation-only changes need link/content review, not invented application tests. Record tests that were not run and why when relevant.
5. Do not mark implementation, report, upload or exams complete without evidence. A commit or a ZIP file is not proof of eClass submission.
6. Reconcile incoming team status updates without overwriting them. Leave owners unassigned until responsibility is agreed. Do not claim this workflow automatically watches others' commits.
