# DSP shared project status

**Updated:** 29 October 2026, Europe/Athens

**Course:** HMMY458 / ΤΗΛ301 — Ψηφιακή Επεξεργασία Σήματος, 2026–2027

**Requirements:** [DSP Master Guide](docs/DSP_Master_Guide.md)

## Lab 1

The final local `DSP_Lab1_Group69.zip` passed three separate reviews: specification coverage, independent mathematical cross-checking, and student-style/readability. No further required correction was found. The user's report and revised README are preserved, with short Greek execution instructions restored. A fresh dependency installation, all three script runs, nine exact figure comparisons and all 18 numerical/rerun checks passed. See the [final review](docs/lab1_final_review_2026-10-29.md). The filled package is delivered locally in the DSP chat; repository reports remain blank identity templates. Submission ownership remains unassigned.

| Item | Status | Evidence |
|---|---|---|
| Exercise 1A–C | Complete | [Code](lab1/exercise1.py), three figures and report; 1B uses an explicitly stated 1 Hz convention |
| Exercise 2A–C | Complete | [Code](lab1/exercise2.py), three figures, Nyquist and reconstruction discussion |
| Exercise 3A–B | Complete | [Code](lab1/exercise3.py), required 3A spectrum and all eight 3B frequencies |
| Greek report template | Complete | [PDF](lab1/report_el.pdf), [HTML](lab1/report_el.html), [source](lab1/report_el.md); 11 pages, nine figures, ten display equations |
| English reading copy | Complete | [PDF](lab1/report.pdf), [HTML](lab1/report.html), [source](lab1/report.md) |
| Execution instructions and packages | Verified | Local filled submission ZIP delivered in DSP chat; [repository template ZIP](deliverables/DSP_Lab1.zip) and [instructions](lab1/README.md) remain available |
| Verification | Passed | [18 checks](lab1/verify.py); all nine PNGs reproduced exactly from a fresh ZIP extraction; [evidence](lab1/VERIFICATION.md) |
| Identification fields | Complete in supplied PDF | Three name/ID rows and group number checked visually; the filled PDF is inside the local submission ZIP |
| eClass submission | Outside this work | No access, upload or submission change was performed; submission owner remains unassigned |

## Conventions and remaining actions

- **1B:** the specification requests Hz but does not provide a sampling interval. The user authorized reasonable choices on 27 October and explicitly requested an uncertainty note. Both reports state `fs = 1 Hz`, `Ts = 1 s` as an assumption. Another positive sampling frequency rescales the Hz axis without changing these FFT magnitudes. This is not staff clarification.
- **3A:** `+30` is interpreted in radians. For the chosen 128 samples at 256 Hz, interpreting it in degrees changes the samples but not the requested magnitude spectrum within `1e-12`.
- **3B:** phase 0 and 400 samples are stated choices; sampling is the assigned 20 kHz.
- Have the agreed team member upload the final local `DSP_Lab1_Group69.zip` delivered in this chat and retain confirmation. It contains the completed PDF; the older repository ZIP is a template with blank identity fields.

The supplied assignment gives **29 October 2026, 23:30** for Lab 1. Live eClass information was last checked on **16 October**, not during this update. Labs 2–4 dates in the original [README](README.txt) remain provisional; the [master guide](docs/DSP_Master_Guide.md) records their source and exam requirements.

## Update — 29 October 2026

The user's shorter README had omitted the required execution instructions; restored only a short Greek paragraph and the four commands. Three final reviewers found no additional required correction. Student-style score: 8.8/10, explicitly not an authorship estimate. Verified a fresh dependency installation and execution in Python 3.12; all 18 tests passed and nine plots matched exactly. Delivered the final ZIP with the unchanged filled report and recorded its hash. No eClass action.

## Update — 28 October 2026

Checked the user's filled PDF against every supplied deliverable requirement. Its 11 pages preserve the verified text, figures and equations; all identification fields display correctly. Simplified comments in the three scripts and added concise variable/unit descriptions; parsed instructions are unchanged. Prepared a six-file local submission ZIP and verified its exact PDF bytes, integrity and instructions. All nine plots reproduced exactly, and all 18 checks passed against the extracted code. No missing deliverable requirement found. Refreshed the repository template ZIP with the same scripts. Detailed evidence and hashes are in the [submission check](docs/lab1_submission_check_2026-10-28.md). No eClass action.

## Update — 27 October 2026

Completed 1B and its explanation, removed draft/progress notices from both reports, added the requested identification fields, and tightened pagination so the sources remain with the conclusions. Updated the default 1B run to regenerate the 1 Hz plot, with a regression test that first changes the rate and then restores the default. No numerical method outside the assignment/preparation was added.

Ran all three scripts and all 18 checks after fresh ZIP extraction. Compared all nine generated PNGs byte-for-byte with the repository copies; rejected invalid sampling rates without changing the figures. Checked both 11-page PDFs, all embedded HTML assets, captions, equations and contents links. The ten display equations are unchanged from the previously reviewed reports. Greek figure data and axis ranges match the original calculations. See [verification](lab1/VERIFICATION.md) for tolerances and limits.

Previous agent scores and dated development records are in the [23 October history](docs/status_history_2026-10-23.md). They apply to their named commits; no new expert grade is claimed for this update.

## Maintenance

Read this file and the master guide before repository work. After each coherent change, update the affected results, checks, assumptions and next actions here in the same commit. Preserve teammates' changes and assign owners only by agreement. Repository completion and eClass submission are separate facts. This is a shared status workflow, not an automatic watcher of other commits.
