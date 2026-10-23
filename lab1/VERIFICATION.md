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
