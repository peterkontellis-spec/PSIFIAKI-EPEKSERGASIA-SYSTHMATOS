# DSP shared project status

**Updated:** 27 October 2026, Europe/Athens

**Course:** HMMY458 / ΤΗΛ301 — Ψηφιακή Επεξεργασία Σήματος, 2026–2027

**Requirements:** [DSP Master Guide](docs/DSP_Master_Guide.md)

## Lab 1

The implementation, Greek report and delivery ZIP are complete and checked. The first page has blank fields for three names, student IDs and the group number, as requested. Fill these before uploading. Owners and identities have not been assigned or invented.

| Item | Status | Evidence |
|---|---|---|
| Exercise 1A–C | Complete | [Code](lab1/exercise1.py), three figures and report; 1B uses an explicitly stated 1 Hz convention |
| Exercise 2A–C | Complete | [Code](lab1/exercise2.py), three figures, Nyquist and reconstruction discussion |
| Exercise 3A–B | Complete | [Code](lab1/exercise3.py), required 3A spectrum and all eight 3B frequencies |
| Greek report | Complete | [PDF](lab1/report_el.pdf), [HTML](lab1/report_el.html), [source](lab1/report_el.md); 11 pages, nine figures, ten display equations |
| English reading copy | Complete | [PDF](lab1/report.pdf), [HTML](lab1/report.html), [source](lab1/report.md) |
| Execution instructions and package | Verified | [DSP_Lab1.zip](deliverables/DSP_Lab1.zip), [instructions](lab1/README.md); code, Greek report and README included |
| Verification | Passed | [18 checks](lab1/verify.py); all nine PNGs reproduced exactly from a fresh ZIP extraction; [evidence](lab1/VERIFICATION.md) |
| Identification fields | Blank by request | Add the actual names, student IDs and group number to the report before upload |
| eClass submission | Outside this work | No access, upload or submission change was performed; submission owner remains unassigned |

## Conventions and remaining actions

- **1B:** the specification requests Hz but does not provide a sampling interval. The user authorized reasonable choices on 27 October and explicitly requested an uncertainty note. Both reports state `fs = 1 Hz`, `Ts = 1 s` as an assumption. Another positive sampling frequency rescales the Hz axis without changing these FFT magnitudes. This is not staff clarification.
- **3A:** `+30` is interpreted in radians. For the chosen 128 samples at 256 Hz, interpreting it in degrees changes the samples but not the requested magnitude spectrum within `1e-12`.
- **3B:** phase 0 and 400 samples are stated choices; sampling is the assigned 20 kHz.
- Fill the requested identification fields, then have the agreed team member upload the ZIP and retain confirmation. The package currently contains the report with those fields blank.

The supplied assignment gives **29 October 2026, 23:30** for Lab 1. Live eClass information was last checked on **16 October**, not during this update. Labs 2–4 dates in the original [README](README.txt) remain provisional; the [master guide](docs/DSP_Master_Guide.md) records their source and exam requirements.

## Update — 27 October 2026

Completed 1B and its explanation, removed draft/progress notices from both reports, added the requested identification fields, and tightened pagination so the sources remain with the conclusions. Updated the default 1B run to regenerate the 1 Hz plot, with a regression test that first changes the rate and then restores the default. No numerical method outside the assignment/preparation was added.

Ran all three scripts and all 18 checks after fresh ZIP extraction. Compared all nine generated PNGs byte-for-byte with the repository copies; rejected invalid sampling rates without changing the figures. Checked both 11-page PDFs, all embedded HTML assets, captions, equations and contents links. The ten display equations are unchanged from the previously reviewed reports. Greek figure data and axis ranges match the original calculations. See [verification](lab1/VERIFICATION.md) for tolerances and limits.

Previous agent scores and dated development records are in the [23 October history](docs/status_history_2026-10-23.md). They apply to their named commits; no new expert grade is claimed for this update.

## Maintenance

Read this file and the master guide before repository work. After each coherent change, update the affected results, checks, assumptions and next actions here in the same commit. Preserve teammates' changes and assign owners only by agreement. Repository completion and eClass submission are separate facts. This is a shared status workflow, not an automatic watcher of other commits.
