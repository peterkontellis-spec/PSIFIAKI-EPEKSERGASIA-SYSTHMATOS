# Lab 1 verification - updated 23 October 2026

## Scope

The current code implements the questions using loops, NumPy FFTs and Matplotlib plots from the assignment/preparation notes. Checked sections: 1A, 1C, 2, 3A and 3B. The 1B calculation is tested with explicit parameters, but its final Hz plot remains pending the physical frequency scale. The required 3A magnitude result is complete: the two interpretations of the unspecified phase produce identical magnitudes within tolerance at the chosen FFT bins. The calculation uses the explicitly documented radians convention. No final ZIP or submission is claimed. Owners and group naming remain open.

## Source review

The supplied PDFs were read locally. Assignment pages 3-4 were visually checked for the exact equations, intervals, frequencies and deliverables. The preparation document was text-reviewed in full, with relevant convolution, sampling and FFT slides also rendered for inspection.

| Document | SHA-256 |
|---|---|
| Lab1_2026.pdf | `40125605267afb28d655075c67cdacb7e35a31e9c6804026d4c0785eb937e68c` |
| Lab1-Preparation.pdf | `89a5411207ccbf191da49924e999528cd7b79a17e373deb61450e9b0b533ac09` |

These identify the supplied copies, not a claim that no newer course announcement exists. Live eClass deadlines were last checked on 16 October. The supplied assignment still states 29 October at 23:30.

## Question-to-method mapping

| Question | Implementation | Source |
|---|---|---|
| 1A | Direct sum with loops, stem plots, comparison with `np.convolve` | Assignment p. 3; preparation pp. 4-9 |
| 1B | `fft`, `fftfreq`, `fftshift`, common magnitude plot; explicit fs required | Assignment p. 3; preparation p. 22 |
| 1C | Algebraic theorem plus zero-padded FFT product and inverse FFT | Assignment pp. 1/3; preparation pp. 6/22 |
| 2A-B | Fine time grid; FFT multiplied by dt; theoretical Nyquist rate | Assignment p. 3; preparation pp. 18/23/25 |
| 2C | Original curve and exact sampled points; written reconstruction explanation | Assignment p. 3; preparation pp. 19-21 |
| 3A | 128 samples at a chosen 256 Hz; FFT; explicit radians convention, with magnitude invariance verified | Assignment p. 4; preparation pp. 18/22 |
| 3B | Eight specified frequencies at 20 kHz; normalized two-sided FFTs | Assignment p. 4; preparation p. 22 |

## Checks performed

- **18 automated tests passed** with Python 3.12.14, NumPy 2.5.4 and Matplotlib 3.11.2 on macOS.
- Convolution compared with exact rational arithmetic and NumPy; index support, endpoints, sum, impulse response and commutativity checked.
- FFT product checked against the convolution transform and inverse. Physical-index Fourier sums independently checked origin alignment. Comparisons use explicit absolute tolerances between `1e-12` and `1e-10`, with relative tolerances where appropriate.
- Exercise 2 checks cover known values, the six sample counts for strict open intervals, the 10 Hz boundary identity and the 5 Hz all-20 alias. FFT magnitudes checked against the direct transform sum at selected bins.
- Both possible 3A phase interpretations were tested: 128 samples and the expected +/-20 and +/-60 Hz peaks. A direct all-bin comparison shows a maximum difference of `3.7623497442574107e-14`, below absolute tolerance `1e-12` (relative tolerance zero). Samples differ, but the magnitude spectrum is unchanged. Neither interpretation is labelled instructor-confirmed.
- All eight 3B spectra checked for correct bins and magnitude 0.5. Aliased sample identities checked at phases 0, 0.3 and -1.2 radians; off-peak magnitudes stayed below `1e-12`.
- The three scripts and tests ran from a clean copy without pre-existing figures. All **eight default PNGs reproduced byte-for-byte** in the same environment.
- Rerun regression: explicit `--fs 1` followed by the default 1B-pending run removes `ex1_spectra.png`; unrelated teammate files survive; a second default run succeeds with the file absent.
- Rerun regression: default 3A, then explicit degrees, then default again restores the original radians-labelled PNG byte-for-byte. The figure is regenerated, not retained from the earlier convention.
- The earlier 22 October check verified invalid fs values (0, negative, NaN, infinity) exit with status 2; argument validation is unchanged. The new 3A figure is included as the requested magnitude result, with its convention and invariance explained.
- The seven existing published figures were visually inspected on 22 October and are unchanged. The new 3A figure was visually inspected on 23 October for correct peaks, title, axes and legibility.
- Markdown relative links and Git whitespace checks passed before commit.

Tests establish agreement for these inputs and the stated tolerances. They do not prove universal correctness, settle unstated instructor intent or establish that an incomplete assignment is ready to submit.

## Report theory update — 23 October 2026

- Rechecked assignment pp. 1-2 visually and preparation pp. 18/22. The report now states the DFT/inverse pair, FFT frequency-bin mapping and specified impulse-train/ideal-low-pass reconstruction model. The reconstruction sum follows directly by convolving the supplied impulse train with the supplied sinc response.
- Re-ran the existing 18 tests: all passed. Independently evaluated the report’s DFT/inverse sums on the 128-sample 3A signal and checked the centred-bin rule for N=16, 128, 400 and 499 against NumPy, with absolute tolerance `1e-10` and relative tolerance zero. Test-only frequency scales did not set a final 1B value or generate its final figure.
- Only documentation changed; existing solution scripts and eight committed figures remain unchanged. Checked Markdown links and figure references. The local preview embeds all eight figures and retains the pending 1B/group notices.
- No extra reconstruction algorithm, final ZIP, deadline recheck or eClass submission action was performed.

## Report presentation update — 23 October 2026

- The source report was reorganized and typeset without changing the solution code or committed plots. Added a results table, eight numbered captions, the full 3A signal and a short source list.
- Verified that the HTML/PDF contain all eight original figures and ten equations; checked embedded PNG hashes against the source figures, seven HTML contents links and the unresolved 1B/team notices. HTML has no external resources or scripts; local and repository HTML copies are identical.
- Rendered all 11 PDF pages for visual review. The independent expert inspected representative pages and confirmed no content regression or blocking layout defect. The HTML design scan found no issues; browser rendering was not visually rechecked because local-file browser automation is blocked.
- No numerical tests were rerun for presentation-only changes. The 18-test result above is from the theory update. The expert’s report-only estimate increased from 8.3/10 to 8.8/10; it is not an official-grade prediction.

## Greek report update — 23 October 2026

- Added [Greek Markdown](report_el.md), [PDF](report_el.pdf) and [standalone HTML](report_el.html), with shorter explanations and eight Greek-labelled figures in `figures/el/`. All ten display equations match the English source exactly. Numerical choices, conclusions and pending items were preserved.
- Ran temporary copies of the unchanged exercise scripts twice, first capturing the original plotted data and then translating only Matplotlib text. SHA-256 comparisons of all plotted line coordinates, collection segments/offsets and axis ranges matched for all eight figures, both before and after saving. No 1B rate was selected and no 1B figure was produced.
- Checked embedded PNG bytes against the Greek source files, eight numbered captions, ten equations and seven working contents anchors. HTML uses `lang="el"`, contains all assets locally, and has no external resources or scripts. Output and repository copies are identical.
- Checked Greek character coverage in the embedded fonts. The PDF contains 11 pages and 18 images (eight figures and ten equations). All pages were rendered and visually inspected, with representative pages inspected at full size; no missing characters, clipped equations or overlapping text were found. HTML browser rendering was not visually rechecked because local-file automation is blocked.
- Verified that the three solution scripts, verification script, eight original figures and English report files remain byte-for-byte unchanged. No new numerical method was introduced; the 18-test suite was not rerun for translation-only changes. Existing scores apply to the earlier English review, not a new review of this translation.
- The report remains a draft pending 1B, team identification and final package verification. No eClass access or submission action was performed.

## Greek review and wording/layout polish — 23 October 2026

- The independent Python expert reviewed `1f67156`, confirmed the translation preserves the mathematics, and reran all 18 tests in an isolated copy: passed. A separate aesthetics agent inspected the Greek report. Both review means were 8.8/10; the scorecards are in [STATUS.md](../STATUS.md). These are pre-polish scores, not instructor-grade predictions.
- Applied the three reviewed wording edits and the 3B high-frequency continuation heading. Enlarged plot titles, axis labels, ticks and legends in Figures 4–5 and 7–8. Moved sampling legends above their axes to keep the curves visible. Tightened summary-table padding to prevent an isolated overflow line; the final PDF still has 11 pages.
- Ran the unchanged exercise scripts in temporary copies to rebuild the Greek figures. All eight plotted-data hashes (line coordinates, collection segments/offsets and axis limits) match the unmodified plots exactly before and after rendering. Only four Greek PNGs changed; the other four Greek figures and all English figures remain unchanged.
- All ten display equations still match the English source exactly. Checked eight embedded Greek PNGs against their files, eight captions, seven HTML contents links, the page-10 continuation heading and pending 1B/team notices. The final PDF has 18 image objects, with no missing-glyph or unresolved-rendering markers. All 11 pages were rendered and visually reviewed, including detailed checks of the summary, sampling figures and continuation page.
- Solution scripts, verification code and English report files are byte-for-byte unchanged. The 1B text and pending notices remain unchanged, and no 1B figure was generated. No new algorithm or parameter choice was introduced. The 18-test suite was not rerun for these presentation-only edits; its latest pass is the independent Greek review recorded above.
- HTML assets and structure were checked; local-file browser automation remains unavailable. No final ZIP, live deadline recheck or eClass access/submission action.

## Post-polish independent re-review — 23 October 2026

- Both agents reviewed `914f4c7`. The Python expert rated the same report fronts 9/8/9.5/9/9.5; the aesthetics agent rated its five fronts 9/9/9/9/9. Both means are 9.0/10. No additional required report correction was found beyond the deliberately pending 1B and team details; all earlier wording/visual suggestions are resolved.
- The expert rechecked the assignment pp. 1–4 and relevant preparation material pp. 4 and 18–25. All ten equations match the previous Greek and English sources exactly. The three solution scripts, verification script and dependencies are byte-identical to `1f67156`, so the numerical suite was not rerun. The prior independent 18-test pass is the latest numerical result.
- Current Greek HTML checks passed: eight figures/captions, 18 embedded images with alt text, eight PNG byte comparisons, seven valid contents anchors, unique IDs and no scripts. Current PDF checks passed: 11 pages, 18 images, eight captions, the page-10 heading and intact pending notices; output and repository copies are identical.
- Both agents inspected current PDF contact sheets and selected full-size pages; the aesthetics agent closely read seven pages. No clipping, overlap or missing Greek glyphs was found. HTML was source-reviewed, not browser-tested.
- Final instructions using the agreed 1B rate, final report refresh and a ZIP tested after fresh extraction remain delivery tasks. No ZIP exists yet. No report, code or figure edits, no new numerical methods and no eClass access/submission action were part of this review.

## Reproduce

From the repository root, install `lab1/requirements.txt` in a virtual environment, then run:

```sh
python lab1/verify.py
python lab1/exercise1.py
python lab1/exercise2.py
python lab1/exercise3.py
```

See [README.md](README.md) for setup, output-replacement behavior and the remaining 1B option.

Reference for library conventions: [NumPy FFT](https://numpy.org/doc/stable/reference/routines.fft.html). The lab methods themselves come from the two course PDFs.
