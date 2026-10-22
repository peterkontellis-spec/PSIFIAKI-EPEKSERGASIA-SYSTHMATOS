# Lab 1 verification - 22 October 2026

## Scope

The current code implements the questions using loops, NumPy FFTs and Matplotlib plots from the assignment/preparation notes. Checked sections: 1A, 1C, 2 and 3B. The calculations for 1B and 3A are tested with explicit parameters, but their final course-specific outputs remain pending the missing frequency-scale and phase-unit decisions. No final ZIP or submission is claimed. Owners and group naming remain open.

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
| 3A | 128 samples at a chosen 256 Hz; FFT; explicit phase-unit choice required | Assignment p. 4; preparation pp. 18/22 |
| 3B | Eight specified frequencies at 20 kHz; normalized two-sided FFTs | Assignment p. 4; preparation p. 22 |

## Checks performed

- **15 automated tests passed** with Python 3.12.14, NumPy 2.5.4 and Matplotlib 3.11.2 on macOS.
- Convolution compared with exact rational arithmetic and NumPy; index support, endpoints, sum, impulse response and commutativity checked.
- FFT product checked against the convolution transform and inverse. Physical-index Fourier sums independently checked origin alignment. Comparisons use explicit absolute tolerances between `1e-12` and `1e-10`, with relative tolerances where appropriate.
- Exercise 2 checks cover known values, the six sample counts for strict open intervals, the 10 Hz boundary identity and the 5 Hz all-20 alias. FFT magnitudes checked against the direct transform sum at selected bins.
- Both possible 3A phase interpretations were tested: 128 samples and the expected +/-20 and +/-60 Hz peaks. Neither interpretation is labelled instructor-confirmed.
- All eight 3B spectra checked for correct bins and magnitude 0.5. Aliased sample identities checked at phases 0, 0.3 and -1.2 radians; off-peak magnitudes stayed below `1e-12`.
- The three scripts and tests ran from a clean copy without pre-existing figures. All **seven default PNGs reproduced byte-for-byte** in the same environment.
- Explicit 1B/3A command-line paths ran in the clean copy. Invalid fs values (0, negative, NaN, infinity) exited with status 2. Test-only ambiguous-parameter figures were not added to the repository.
- All seven published figures were visually inspected for correct titles, axes, legibility and data visibility. Sampling legends were moved into blank plot space and the affected figures regenerated and reinspected.
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

See [README.md](README.md) for setup and the explicit options to use after clarification.

Reference for library conventions: [NumPy FFT](https://numpy.org/doc/stable/reference/routines.fft.html). The lab methods themselves come from the two course PDFs.
