# Lab 1

Three short Python scripts follow the assignment and preparation notes. Owners and final group naming remain open.

## Read the report

Open [report.pdf](report.pdf) for the paginated reading copy, or [report.html](report.html) for an offline browser preview with contents links. Both include all eight figures and ten typeset equations. The editable source is [report.md](report.md); refresh both reading copies when that source changes.

These are review drafts. Exercise 1B’s physical sampling rate and figure, group identification and authors remain open. Neither reading copy is a final submission package.

## Run

Tested with Python 3.12, NumPy 2.5.4 and Matplotlib 3.11.2.
From the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r lab1/requirements.txt
python lab1/verify.py
python lab1/exercise1.py
python lab1/exercise2.py
python lab1/exercise3.py
```

On Windows, activate with `.venv\Scripts\activate` instead.
For a computer without a display, set `MPLBACKEND=Agg` before running.
The scripts save PNG figures in `lab1/figures/` and do not require interactive plot windows.
`verify.py` is separate checking code, not an additional solution method.

### VS Code

Open this repository as one folder in VS Code and use its integrated terminal for the commands above. No extra workspace, MATLAB or SciPy is required. If using VS Code's Python run button, select the interpreter inside `.venv`; running through the activated terminal is sufficient without editor-specific configuration. View the saved PNGs and use Markdown Preview for `report.md`, or read the formatted PDF/HTML copies. The report still needs the pending 1B result and agreed team details. The required ZIP is separate from these reading copies.

## Exercise 1B remains pending

Neither PDF gives a sampling frequency for the Exercise 1 sequences while the question requests Hz. The script does not invent one. After clarification, run `exercise1.py --fs VALUE`, replacing VALUE with the chosen frequency in Hz. Running without `--fs` removes only the script-generated `figures/ex1_spectra.png`, if present, so an earlier Hz choice cannot remain in the current output folder. Other files are left alone.

## Exercise 3A magnitude plot

The default `exercise3.py` now completes the required plot using the explicit radians convention for the printed `+30`. At 128 samples and 256 Hz, both tones fall on distinct FFT bins, so interpreting the phase as degrees instead gives the same magnitudes within floating-point tolerance. The report explains this; it does not claim that the unspecified unit has been clarified.

`--phase-unit degrees` remains available for an explicit alternative interpretation of the same expression. Every successful run regenerates `ex3a_spectrum.png` with the current convention in its title, including when returning to the default radians run.

With no options, the three scripts generate **eight figures** for 1A/1C, 2, 3A and 3B. A successful run does not mean the whole assignment is finished.

## Numerical choices permitted by the questions

- Exercise 2 uses a 1 ms grid only for plotting the continuous curve and its FFT approximation. Sampling uses exactly the required 20, 10 and 5 Hz rates. Endpoints are excluded to follow `0 < t < T` literally. The plots show samples, not interpolated/reconstructed curves; the report discusses reconstruction using the specified theory.
- Exercise 3A uses 256 Hz, since the brief expressly allows choosing a sampling rate. It uses exactly 128 samples.
- Exercise 3B uses phase 0 radians and 400 samples. Neither is fixed in 3B. All specified frequencies occupy exact FFT bins with this count; the resolution is 50 Hz. The 128-sample requirement belongs to 3A.
- FFT magnitude normalization follows preparation p. 22; the continuous-time approximation in Exercise 2 follows pp. 23/25 (`FFT * dt`). No window functions, filters or interpolation algorithms have been added.

See [report.md](report.md) for the current explanation, [VERIFICATION.md](VERIFICATION.md) for scope/evidence and [../STATUS.md](../STATUS.md) for shared progress. The report is incomplete until 1B and the final group/author details are resolved. No final ZIP has been made or uploaded.
