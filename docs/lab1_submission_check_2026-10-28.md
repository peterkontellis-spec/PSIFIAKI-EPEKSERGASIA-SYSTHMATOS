# Lab 1 submission check — 28 October 2026

The user supplied the completed `DSP_REPORT1.pdf`. All three name/ID rows and group number are populated and readable. The exact supplied PDF is included in the local `DSP_Lab1_Submission.zip` delivered through the DSP chat. The PDF was not rewritten.

## Requirements checked

| Supplied requirement | Result and evidence |
|---|---|
| One ZIP containing Python code and detailed report | Pass: one ZIP with six files; one PDF and three exercise scripts, plus README and requirements |
| Comments explaining main parameters/variables | Pass: sequence indices, FFT length and normalization, Hz/seconds, plotting step, sample counts and phase choices are explained in short comments |
| Necessary theory and formulas | Pass: PDF p. 1 DFT/inverse; pp. 2–4 convolution and theorem; pp. 5–8 Nyquist and reconstruction; pp. 9–11 sampling/aliases |
| Figures for every question, separate from code | Pass: nine figures on pp. 2–5 and 7–11; the theory subsection on p. 6 supports the sampling figures on pp. 7–8. No source-code listings in the PDF |
| Main titles, axis titles and useful plotted ranges | Pass: every plot has titles/labels; original and sampled signals cover the requested intervals; spectra show the relevant components and aliases |
| Short implementation explanations and conclusions based on theory | Pass: every exercise links calculations to the stated formulas and interprets the results; final conclusions on p. 11 |
| Short execution instructions | Pass: README gives Python version, environment setup, dependency installation and the exact three run commands |

The note about 1B's unspecified physical sampling frequency remains explicit. Its 1 Hz assumption is not presented as prescribed. The 3A phase convention and 3B sample-count/phase choices are also stated.

## Exact contents of the local submission ZIP

```text
DSP_Lab1/
  README.txt
  lab1/
    DSP_REPORT1.pdf
    exercise1.py
    exercise2.py
    exercise3.py
    requirements.txt
```

The report already embeds all plots. Generated PNGs, development status, review scores and the maintenance test suite are not needed in this submission ZIP. The test suite remains in the repository.

## Verification

- All 11 supplied PDF pages have the same body text, decoded figure/equation pixels and page dimensions as the previously verified Greek report. The only additions are seven first-page identification annotations. All have appearance streams and the print flag; they are visible and readable in the rendered PDF. All 11 pages were rendered and visually checked.
- Comment edits change no Python instructions: parsed syntax trees match the earlier scripts exactly. No calculation or numerical method was changed.
- The final ZIP passes its integrity check, contains six files with relative paths only, and its PDF is byte-identical to the user-supplied file.
- All three scripts ran from a fresh extraction using the documented commands. Nine output PNGs match the repository figures byte-for-byte.
- All 18 existing numerical/rerun checks passed against copies of the extracted scripts in a separate test folder. Python 3.12.14, NumPy 2.5.4 and Matplotlib 3.11.2; existing environment, no fresh dependency installation.

| Artifact | SHA-256 |
|---|---|
| Supplied and packaged PDF | `5468c18b8eb30a29472f69ec65fb8a0ca39d79839601bf34d72340db97d77ed5` |
| Local submission ZIP | `f0d3dd38eb177e5ceec53d570f465d002371ca333b281844a67e94f1c7620d8f` |
| Repository template ZIP | `c2cd55424ce5243a3ca7ef3c219ef006b0438613b1abeb8ef49efb4aab0b8f21` |

The completed names/IDs are held in the user's local submission PDF/ZIP. Repository report copies and `deliverables/DSP_Lab1.zip` retain blank identification fields as reusable templates; the template ZIP has been refreshed with the same commented solution scripts. Use the local submission ZIP from the DSP chat for upload. No eClass access or submission action was performed. The checks found no missing item in the supplied deliverable requirements; they do not predict an instructor's grade.
