# Lab 1 verification — updated 28 October 2026

## Latest submission check

The user's completed PDF and final local six-file submission ZIP were verified on 28 October. All identification annotations display and print correctly; report content is unchanged. Only comments in the exercise scripts were refined. All three scripts ran after extraction, all nine PNGs reproduced exactly, and the 18-check suite passed against the extracted code in a separate test folder. See the [requirement-by-requirement check and current hashes](../docs/lab1_submission_check_2026-10-28.md). The filled PDF/ZIP are local delivery files; repository report files retain blank identity fields. The evidence below records the 27 October template review.

## Result and scope — 27 October

All three exercise scripts ran successfully from a fresh extraction of [DSP_Lab1.zip](../deliverables/DSP_Lab1.zip). All **18 tests passed**. The extracted code reproduced all **nine PNG figures byte-for-byte** in the checked environment. Both reports contain all questions, nine figures and ten display equations. Names, student IDs and group number are deliberately blank fields for the team to fill.

The methods remain the assignment/preparation's direct convolution sum, NumPy FFTs, original-curve/sample plots and written reconstruction theory. No new interpolation or reconstruction algorithm was introduced. No eClass action was performed.

## Sources

The supplied assignment and preparation PDF were reviewed locally; relevant formula and exercise pages were visually checked. Their SHA-256 values identify the copies used:

| Source | SHA-256 |
|---|---|
| Lab1_2026.pdf | `40125605267afb28d655075c67cdacb7e35a31e9c6804026d4c0785eb937e68c` |
| Lab1-Preparation.pdf | `89a5411207ccbf191da49924e999528cd7b79a17e373deb61450e9b0b533ac09` |

These identify supplied documents, not a fresh check of course announcements. Live eClass was last checked on 16 October. The supplied assignment states 29 October at 23:30.

| Question | Method and source |
|---|---|
| 1A | Direct convolution sum, stem plots, `np.convolve` comparison; assignment p. 3, preparation pp. 4–9 |
| 1B | Common length-16 `fft`, `fftfreq`, `fftshift` and magnitude plot; assignment p. 3, preparation p. 22 |
| 1C | Algebraic theorem and padded FFT product/inverse; assignment pp. 1/3, preparation pp. 6/22 |
| 2A–B | Fine time grid, FFT multiplied by dt, theoretical Nyquist rate; assignment p. 3, preparation pp. 18/23/25 |
| 2C | Original curve and exact sampled points, written reconstruction theory; assignment pp. 2–3, preparation pp. 19–21 |
| 3A | 128 samples at 256 Hz, FFT, stated radians convention; assignment p. 4, preparation pp. 18/22 |
| 3B | Eight specified tones at 20 kHz, normalized two-sided FFTs; assignment p. 4, preparation p. 22 |

## Numerical and rerun checks

- Python **3.12.14**, NumPy **2.5.4**, Matplotlib **3.11.2**, macOS; figures rendered with `MPLBACKEND=Agg`. The extracted package used the existing verified virtual environment; dependencies were not freshly downloaded or installed.
- Convolution: correct lengths and indices, exact rational-arithmetic/NumPy comparisons, endpoints, sum, impulse identity and commutativity. Maximum difference from NumPy is `8.882e-16`.
- Convolution theorem: FFT product and inverse agree; physical-index direct sums independently check origin alignment. Maximum FFT-product error is `5.684e-14`. Tests use explicit tolerances between `1e-12` and `1e-10`, with relative tolerance where stated in the test code.
- **1B:** convention `fs = 1 Hz`, bin spacing `0.0625 Hz`, bins `−0.5` to `0.4375 Hz`. Direct physical-index Fourier sums independently match all three normalized spectra within absolute `1e-12`. At zero frequency the magnitudes are **5.625**, **0.325089**, **29.25801**. Rescaling fs from 1 to 20 changes the axis only.
- **1B rerun:** explicit fs 1, then fs 20, then the default restores the exact fs 1 PNG; unrelated teammate files survive. Invalid CLI values `0`, `-1`, `nan`, `inf` return status 2 and leave figures unchanged.
- Exercise 2: known signal values, all six sample counts for strict open intervals, the 10 Hz boundary identity, the 5 Hz constant-20 alias, and selected direct-transform bins.
- **3A:** 128 samples, expected ±20/±60 Hz bins and magnitudes 6/9 for both interpretations of `+30`. Their largest all-bin magnitude difference is `3.7623497442574107e-14`, below absolute `1e-12`, relative tolerance zero. The waveform samples differ. A degrees run followed by the default restores the radians-labelled PNG exactly.
- **3B:** all eight tones have the correct bins and normalized magnitude 0.5. Aliased sample identities also checked at phases 0, 0.3 and −1.2 rad; off-peak magnitudes below `1e-12`. Parseval normalization checked.

The 1 Hz value is a report convention, not a sampling frequency provided by staff. Tests establish agreement for the supplied inputs and stated tolerances; they do not settle unspecified instructor intent.

## Report and package checks

- Greek and English PDF/HTML copies match their repository copies. Each PDF has **11 pages** and **19 image objects**: nine plots and ten equations. All pages rendered and visually inspected; first page, 1B and final Greek page also checked at full size. No clipping, stray source page, missing characters or unfinished labels found.
- All ten display equations match the previously reviewed Greek/English sources at `b91116d`. All nine Greek plotted datasets and axis ranges match the source calculations before and after relabelling. The eight previous plot files in each language are unchanged; the new 1B plot is added.
- HTML: nine figure/caption pairs, ten equation images, seven unique resolving contents links, alt text, no scripts or external assets. All nine embedded PNGs match their source bytes. HTML was structurally checked; browser rendering was not retested because local-file browser automation was unavailable.
- The first page contains three blank name/ID rows and a blank group-number field. Both reports explicitly retain 1B's sampling-frequency uncertainty. Draft/progress notices and internal review scores are absent from the reports.
- ZIP integrity passed; seven files, relative paths only. Its Greek PDF equals the repository PDF. Instructions were executed from a fresh extraction with no pre-existing figures. All nine generated PNGs match the repository. No status history or agent review scores are included in the ZIP.

| Verified artifact | SHA-256 |
|---|---|
| Greek PDF | `b894f5e1c013c1dd01c74308a8fb12973c4cfb4b9abd6fe3468f9fb89ee12fad` |
| English PDF | `6bf293dfa3e4c5c1b565fbf359626a83dd72e38530cfe6d947779a1cb649534b` |
| DSP_Lab1.zip, 27 October version | `e452b0e6f2f7a9ae6503e9aaaeee1b4f5918baffd46cc9dc0980d867efef6743` |

The package contains the requested blank identification fields; fill them before uploading and refresh the PDF in the ZIP. No new agent grading, staff clarification, live deadline check or eClass submission is claimed. Previous scorecards remain in the [dated history](../docs/status_history_2026-10-23.md).

## Reproduce

Follow [README.md](README.md), or extract the ZIP and use its `README.txt`. Run the three scripts and `python lab1/verify.py` from the stated folder. Changing code, assumptions or report content requires refreshing the affected figures/reading copies/package and repeating the relevant checks.
