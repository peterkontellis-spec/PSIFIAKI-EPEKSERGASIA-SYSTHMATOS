# Lab 1

Three short Python scripts follow the assignment and preparation notes. Owners and final group naming remain open.

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

Open this repository as one folder in VS Code and use its integrated terminal for the commands above. No extra workspace, MATLAB or SciPy is required. If using VS Code's Python run button, select the interpreter inside `.venv`; running through the activated terminal is sufficient without editor-specific configuration. View the saved PNGs and use Markdown Preview for `report.md`. The report still needs completion and a final document format, and the required ZIP is submitted through eClass in a browser.

## Two outputs remain pending

- **1B:** neither PDF gives a sampling frequency for the discrete sequences while the question requests Hz. The script does not invent one. After clarification, run `exercise1.py --fs VALUE`, replacing VALUE with the chosen frequency in Hz.
- **3A:** the assignment prints `+30` without a unit. After clarification, run `exercise3.py --phase-unit radians` or `exercise3.py --phase-unit degrees`. The code supports and checks either interpretation but no final 3A figure is committed yet.

These options only supply missing physical parameters; they do not select alternative numerical methods. With no options, the scripts generate the seven verified figures for 1A/1C, 2 and 3B. They print the pending sections explicitly. A successful run does not mean the whole assignment is finished.

## Numerical choices permitted by the questions

- Exercise 2 uses a 1 ms grid only for plotting the continuous curve and its FFT approximation. Sampling uses exactly the required 20, 10 and 5 Hz rates. Endpoints are excluded to follow `0 < t < T` literally. The plots show samples, not interpolated/reconstructed curves; the report discusses reconstruction using the specified theory.
- Exercise 3A uses 256 Hz, since the brief expressly allows choosing a sampling rate. It uses exactly 128 samples.
- Exercise 3B uses phase 0 radians and 400 samples. Neither is fixed in 3B. All specified frequencies occupy exact FFT bins with this count; the resolution is 50 Hz. The 128-sample requirement belongs to 3A.
- FFT magnitude normalization follows preparation p. 22; the continuous-time approximation in Exercise 2 follows pp. 23/25 (`FFT * dt`). No window functions, filters or interpolation algorithms have been added.

See [report.md](report.md) for the current explanation, [VERIFICATION.md](VERIFICATION.md) for scope/evidence and [../STATUS.md](../STATUS.md) for shared progress. The report is incomplete until 1B and 3A are resolved. No final ZIP has been made or uploaded.
